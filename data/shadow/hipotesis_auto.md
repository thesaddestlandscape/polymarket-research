# Hipótesis automáticas — 2026-10-20 14:25 UTC
_Generado por shadow_postmortem.py sobre 980624 resoluciones (PNL=+127797.20€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.495` → IC=-0.255 (n=194)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=626)

- **PATRÓN** `py_entrada` > `0.515` → IC=+0.236 (n=787)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.515 (IC base=+0.138)

- **PATRÓN** `n_total_lado` > `66.0` → IC=+0.182 (n=278)

  - _Acción_: Kelly boost +0.91€ cuando `n_total_lado` > 66.0 (IC base=+0.138)

- **PATRÓN** `banda_hit_calibrado` > `0.7976` → IC=+0.272 (n=556)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.7976 (IC base=+0.138)

- **PATRÓN** `banda_z` > `9.204` → IC=+0.204 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.204 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.172 (n=306)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.138)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.154 (n=909)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `98.0` → IC=+0.154 (n=457)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 98.0 (IC base=+0.138)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **PATRÓN** `py_entrada` > `0.545` → IC=+0.272 (n=480)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.545 (IC base=+0.144)

- **PATRÓN** `n_total_lado` > `69.0` → IC=+0.199 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 69.0 (IC base=+0.144)

- **PATRÓN** `banda_hit_calibrado` > `0.6174` → IC=+0.265 (n=470)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6174 (IC base=+0.144)

- **PATRÓN** `banda_z` > `9.588` → IC=+0.209 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.588 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.185 (n=255)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 17.0 (IC base=+0.144)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.151 (n=810)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.156 (n=419)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 100.0 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `9753.7972` → IC=+0.135 (n=206)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 9753.7972 (IC base=+0.017)

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
- **FILTRO** `restante_s_al_confirmar` < `142.34` → IC=-0.204 (n=10039)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 142.34
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=30117)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `128.85` → IC=-0.263 (n=1122)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 128.85
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=3369)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `121.5` → IC=-0.287 (n=1079)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 121.5
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=3238)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `167.25` → IC=-0.206 (n=2647)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 167.25
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=7943)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `133.16` → IC=-0.276 (n=1961)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 133.16
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=5883)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.213 (n=21662)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.108)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.136 (n=4316)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.108)

- **PATRÓN** `libro_liquidez` > `9142.8831` → IC=+0.176 (n=1951)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 9142.8831 (IC base=+0.108)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.130 (n=18296)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 17.0 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.129 (n=33130)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 11.0 (IC base=+0.126)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.227 (n=17177)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.150 (n=7188)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.01 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `7095.7162` → IC=+0.159 (n=2777)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 7095.7162 (IC base=+0.126)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.200 (n=2025)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.192)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.192 (n=1981)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 17.0 (IC base=+0.192)

- **PATRÓN** `py_entrada` > `0.775` → IC=+0.364 (n=644)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.775 (IC base=+0.192)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.195 (n=2484)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.01 (IC base=+0.192)

- **PATRÓN** `libro_liquidez` > `16413.1582` → IC=+0.200 (n=644)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16413.1582 (IC base=+0.192)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.189 (n=1785)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 7.0 (IC base=+0.183)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.188 (n=1985)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 17.0 (IC base=+0.183)

- **PATRÓN** `py_entrada` < `0.245` → IC=+0.340 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.245 (IC base=+0.183)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.186 (n=2546)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.01 (IC base=+0.183)

- **PATRÓN** `libro_liquidez` > `16197.5868` → IC=+0.195 (n=656)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 16197.5868 (IC base=+0.183)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.61` → IC=+0.170 (n=470)

  - _Acción_: Kelly boost +0.85€ cuando `py_entrada` > 0.61 (IC base=+0.080)

- **PATRÓN** `libro_liquidez` > `6857.6712` → IC=+0.167 (n=124)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 6857.6712 (IC base=+0.080)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.140 (n=1119)

  - _Acción_: Kelly boost +0.70€ cuando `py_entrada` < 0.44 (IC base=+0.085)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.168 (n=4195)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.161)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.162 (n=2871)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 12.0 (IC base=+0.161)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.371 (n=1375)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.161)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.219 (n=1860)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.212)

- **PATRÓN** `py_entrada` < `0.26` → IC=+0.360 (n=671)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.26 (IC base=+0.212)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.215 (n=2181)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.212)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.146 (n=1059)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.143)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.149 (n=687)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 11.0 (IC base=+0.143)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.264 (n=341)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.143)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=828)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `1885.9178` → IC=+0.154 (n=674)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 1885.9178 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.162 (n=152)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.069)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.246 (n=976)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.222)

- **PATRÓN** `py_entrada` > `0.83` → IC=+0.419 (n=1143)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.83 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.150 (n=1287)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 7.0 (IC base=+0.149)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.159 (n=678)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 7.0 (IC base=+0.149)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.285 (n=646)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.149)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.154 (n=854)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.149)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `9.0` → IC=+0.171 (n=314)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 9.0 (IC base=+0.154)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.347 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.154)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.145 (n=198)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.02 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.136 (n=1134)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 7.0 (IC base=+0.123)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.245 (n=410)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.123)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `11.0` → IC=-0.297 (n=62)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=148)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.206 (n=18264)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.201)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.203 (n=15523)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.201)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.235 (n=7540)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.201)

- **PATRÓN** `libro_liquidez` > `4837.3339` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4837.3339 (IC base=+0.201)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.181 (n=4213)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 5.0 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.182 (n=4199)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 18.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.183 (n=4114)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` < 0.73 (IC base=+0.180)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.181 (n=3445)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` > 0.71 (IC base=+0.180)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.380 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.247 (n=89)

- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=90)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.224 (n=2149)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.231 (n=1437)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.222)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.305 (n=756)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.222)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.188 (n=4142)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.183 (n=3529)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 15.0 (IC base=+0.182)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.187 (n=3253)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` > 0.71 (IC base=+0.182)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.258 (n=3593)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.248)

- **PATRÓN** `py_entrada` > `0.79` → IC=+0.361 (n=1159)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.194 (n=4060)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 5.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.193 (n=2602)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 11.0 (IC base=+0.189)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.193 (n=3001)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.71 (IC base=+0.189)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.433 (n=775)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.427)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.440 (n=803)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.427)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.432 (n=820)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.427)

- **PATRÓN** `libro_liquidez` > `4125.7507` → IC=+0.437 (n=509)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4125.7507 (IC base=+0.427)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.434 (n=303)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.435)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.444 (n=142)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.435)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.446 (n=334)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.435)

- **PATRÓN** `libro_liquidez` > `20754.9559` → IC=+0.441 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 20754.9559 (IC base=+0.435)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.448 (n=211)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.433)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.443 (n=316)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.433)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.436 (n=341)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.433)

- **PATRÓN** `libro_liquidez` > `4437.5111` → IC=+0.441 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4437.5111 (IC base=+0.433)

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

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.209 (n=23608)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.202)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.247 (n=23955)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.202)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.188 (n=11105)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.186)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.188 (n=7588)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 12.0 (IC base=+0.186)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.201 (n=10622)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.71 (IC base=+0.186)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.228 (n=4924)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.227 (n=4872)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.225)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.286 (n=3473)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.225)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.191 (n=4043)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 17.0 (IC base=+0.182)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.211 (n=5425)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.182)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.835` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.835
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.232 (n=4963)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.223 (n=3805)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.222)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.278 (n=3382)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.222)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.206 (n=9083)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.261 (n=3524)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.208 (n=3924)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.199 (n=3976)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 6.0 (IC base=+0.197)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.243 (n=4950)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.197)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.192 (n=8622)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.140 (n=8448)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `3.77` → IC=+0.137 (n=10341)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 3.77 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.195 (n=4266)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.119)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.143 (n=4314)

  - _Acción_: Kelly boost +0.71€ cuando `restante_min` > 4.95 (IC base=+0.119)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.129 (n=5180)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.119)

- **PATRÓN** `lag_apertura_s` < `2.76` → IC=+0.146 (n=3892)

  - _Acción_: Kelly boost +0.73€ cuando `lag_apertura_s` < 2.76 (IC base=+0.119)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.189 (n=4356)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.38 (IC base=+0.114)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.136 (n=4602)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.96 (IC base=+0.114)

- **PATRÓN** `lag_apertura_s` < `3.33` → IC=+0.134 (n=5203)

  - _Acción_: Kelly boost +0.67€ cuando `lag_apertura_s` < 3.33 (IC base=+0.114)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.300 (n=1655)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.292)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.292 (n=1631)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.292)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.381 (n=570)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.292)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.286 (n=751)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.279)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.355 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.279)

- **PATRÓN** `libro_liquidez` > `5025.5141` → IC=+0.288 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5025.5141 (IC base=+0.279)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.321 (n=534)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.297)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.300 (n=785)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.297)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.391 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.297)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.297 (n=889)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.297)

- **PATRÓN** `libro_liquidez` > `2112.3487` → IC=+0.311 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2112.3487 (IC base=+0.297)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.445 (n=765)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.442)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.442 (n=755)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.442)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.445 (n=528)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.442)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.443 (n=868)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.442)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.437 (n=364)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.436)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.440 (n=247)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.436)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.436 (n=374)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.436)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.441 (n=270)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.436)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.453 (n=361)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.449)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.452 (n=349)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.449)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.450 (n=399)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.449)

- **PATRÓN** `libro_liquidez` > `1978.9685` → IC=+0.468 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1978.9685 (IC base=+0.449)

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
  - _Potencial_: sin este filtro IC_bueno=-0.201 (n=95)

- **FILTRO** `py_entrada` > `0.735` → IC=-0.365 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.735
  - _Potencial_: sin este filtro IC_bueno=-0.151 (n=81)

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
  - _Potencial_: sin este filtro IC_bueno=-0.201 (n=95)

- **FILTRO** `py_entrada` > `0.735` → IC=-0.365 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.735
  - _Potencial_: sin este filtro IC_bueno=-0.151 (n=81)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4759` → IC=+0.138 (n=13295)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.4759 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.124 (n=13444)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 6.0 (IC base=+0.121)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.124 (n=9312)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 12.0 (IC base=+0.121)

- **PATRÓN** `ibs_20min` > `0.9804` → IC=+0.248 (n=4437)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9804 (IC base=+0.121)

- **PATRÓN** `dist_vwap_pct` > `0.7752` → IC=+0.267 (n=737)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7752 (IC base=+0.121)

- **PATRÓN** `dist_vwap_pct` < `0.2117` → IC=+0.258 (n=3262)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2117 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.913` → IC=+0.191 (n=5038)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 5.913 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` < `1.2014` → IC=+0.258 (n=3862)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2014 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` > `0.6202` → IC=+0.264 (n=3863)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6202 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` > `0.3025` → IC=+0.242 (n=1349)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3025 (IC base=+0.121)

- **PATRÓN** `volumen_spike_ratio` > `2.3445` → IC=+0.229 (n=4287)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3445 (IC base=+0.121)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.124 (n=11181)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.02 (IC base=+0.121)

- **PATRÓN** `ibs_20min` < `0.685` → IC=+0.130 (n=18593)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` < 0.685 (IC base=+0.075)

- **PATRÓN** `dist_vwap_pct` < `0.1541` → IC=+0.188 (n=6046)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` < 0.1541 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` < `0.6965` → IC=+0.185 (n=2803)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 0.6965 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` > `1.0502` → IC=+0.181 (n=2889)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 1.0502 (IC base=+0.075)

- **PATRÓN** `volumen_pendiente_norm` > `0.2956` → IC=+0.233 (n=1592)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2956 (IC base=+0.075)

- **PATRÓN** `volumen_spike_ratio` > `2.6769` → IC=+0.207 (n=3610)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6769 (IC base=+0.075)

- **PATRÓN** `ballena_activa_n` < `106.0` → IC=+0.221 (n=10683)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 106.0 (IC base=+0.075)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.212 (n=965)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.200)

- **PATRÓN** `drift_60min` |x|≤ `0.347` → IC=+0.203 (n=2892)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.347 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.210 (n=1399)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.200)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.205 (n=1939)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.200)

- **PATRÓN** `ibs_20min` > `0.9802` → IC=+0.281 (n=1311)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9802 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.892` → IC=+0.282 (n=1269)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.892 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` > `0.2333` → IC=+0.249 (n=509)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2333 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` > `1.44` → IC=+0.202 (n=2755)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.44 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.215 (n=3096)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.200)

- **PATRÓN** `libro_liquidez` > `2078.2302` → IC=+0.205 (n=964)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2078.2302 (IC base=+0.200)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.218 (n=1732)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 14.0 (IC base=+0.200)

- **PATRÓN** `sigma_h` < `0.0085` → IC=+0.239 (n=2424)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0085 (IC base=+0.237)

- **PATRÓN** `sigma_h` > `0.0077` → IC=+0.238 (n=1099)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0077 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.0873` → IC=+0.272 (n=811)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0873 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.254 (n=880)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` < `0.5294` → IC=+0.259 (n=2421)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5294 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` < `0.0941` → IC=+0.239 (n=2169)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0941 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.287` → IC=+0.262 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.287 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` < `1.4411` → IC=+0.243 (n=762)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4411 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `2.6588` → IC=+0.244 (n=761)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6588 (IC base=+0.237)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.241 (n=2720)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.237)

- **PATRÓN** `libro_liquidez` > `1634.98` → IC=+0.245 (n=2163)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1634.98 (IC base=+0.237)

- **PATRÓN** `ballena_activa_n` < `7.0` → IC=+0.241 (n=801)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 7.0 (IC base=+0.237)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.238 (n=1043)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.228)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.230 (n=1074)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.228)

- **PATRÓN** `drift_60min` |x|≤ `0.106` → IC=+0.262 (n=1042)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.106 (IC base=+0.228)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.239 (n=2483)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.228)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.228 (n=1686)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.228)

- **PATRÓN** `ibs_20min` > `0.9499` → IC=+0.277 (n=790)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9499 (IC base=+0.228)

- **PATRÓN** `dist_vwap_pct` > `0.1291` → IC=+0.233 (n=1264)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1291 (IC base=+0.228)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.335` → IC=+0.264 (n=358)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.335 (IC base=+0.228)

- **PATRÓN** `volumen_regimen` < `1.231` → IC=+0.230 (n=2368)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.231 (IC base=+0.228)

- **PATRÓN** `volumen_regimen` > `0.623` → IC=+0.232 (n=2368)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.623 (IC base=+0.228)

- **PATRÓN** `volumen_pendiente_norm` > `0.2763` → IC=+0.263 (n=336)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2763 (IC base=+0.228)

- **PATRÓN** `volumen_spike_ratio` < `1.5085` → IC=+0.228 (n=1026)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5085 (IC base=+0.228)

- **PATRÓN** `volumen_spike_ratio` > `2.4426` → IC=+0.255 (n=778)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4426 (IC base=+0.228)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.152 (n=2410)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0057 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.0749` → IC=+0.169 (n=804)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.0749 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.153 (n=908)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 17.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` < `0.7275` → IC=+0.177 (n=2410)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.7275 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.992` → IC=+0.150 (n=390)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 10.992 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.177` → IC=+0.140 (n=2204)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` < 4.177 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `1.2041` → IC=+0.140 (n=2410)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 1.2041 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` > `0.0963` → IC=+0.159 (n=880)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` > 0.0963 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` < `2.4535` → IC=+0.143 (n=2290)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.4535 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` > `1.4138` → IC=+0.135 (n=2290)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 1.4138 (IC base=+0.133)

- **PATRÓN** `ballena_activa_n` < `218.0` → IC=+0.174 (n=980)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 218.0 (IC base=+0.133)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0121` → IC=+0.220 (n=1006)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0121 (IC base=+0.195)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.201 (n=3156)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.195)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.273 (n=1147)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.195)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.27` → IC=+0.276 (n=636)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.27 (IC base=+0.195)

- **PATRÓN** `volumen_pendiente_norm` < `0.0975` → IC=+0.201 (n=2669)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0975 (IC base=+0.195)

- **PATRÓN** `volumen_pendiente_norm` > `0.3526` → IC=+0.212 (n=387)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3526 (IC base=+0.195)

- **PATRÓN** `volumen_spike_ratio` > `2.6928` → IC=+0.211 (n=1322)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6928 (IC base=+0.195)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.202 (n=3594)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.195)

- **PATRÓN** `libro_liquidez` > `1975.3784` → IC=+0.202 (n=1364)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1975.3784 (IC base=+0.195)

- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.224 (n=2373)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0106 (IC base=+0.218)

- **PATRÓN** `drift_60min` |x|≤ `0.461` → IC=+0.224 (n=2371)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.461 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.242 (n=1004)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.218 (n=1243)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.218)

- **PATRÓN** `ibs_20min` < `0.0171` → IC=+0.277 (n=898)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0171 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.402` → IC=+0.246 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.402 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` > `0.3479` → IC=+0.258 (n=386)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3479 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` > `2.726` → IC=+0.231 (n=1160)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.726 (IC base=+0.218)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.220 (n=1417)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.218)

- **PATRÓN** `libro_liquidez` > `2051.9584` → IC=+0.221 (n=898)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2051.9584 (IC base=+0.218)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.222 (n=2215)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 24.0 (IC base=+0.218)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.140 (n=148)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=3646)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.164 (n=536)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0037 (IC base=+0.054)

- **PATRÓN** `ibs_20min` > `0.9536` → IC=+0.229 (n=536)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9536 (IC base=+0.054)

- **PATRÓN** `dist_vwap_pct` > `0.14` → IC=+0.331 (n=358)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.14 (IC base=+0.054)

- **PATRÓN** `dist_vwap_pct` < `0.1896` → IC=+0.329 (n=484)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1896 (IC base=+0.054)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.103` → IC=+0.188 (n=1158)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 5.103 (IC base=+0.054)

- **PATRÓN** `volumen_regimen` < `0.8561` → IC=+0.335 (n=403)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8561 (IC base=+0.054)

- **PATRÓN** `volumen_regimen` > `1.2207` → IC=+0.348 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2207 (IC base=+0.054)

- **PATRÓN** `volumen_pendiente_norm` > `0.2965` → IC=+0.351 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2965 (IC base=+0.054)

- **PATRÓN** `volumen_spike_ratio` < `1.4099` → IC=+0.348 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4099 (IC base=+0.054)

- **PATRÓN** `volumen_spike_ratio` > `2.2171` → IC=+0.328 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2171 (IC base=+0.054)

- **PATRÓN** `ballena_activa_n` < `132.0` → IC=+0.338 (n=524)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 132.0 (IC base=+0.054)

- **PATRÓN** `ibs_20min` < `0.0929` → IC=+0.175 (n=949)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.0929 (IC base=+0.036)

- **PATRÓN** `dist_vwap_pct` > `0.3255` → IC=+0.142 (n=450)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.3255 (IC base=+0.036)

- **PATRÓN** `dist_vwap_pct` < `0.1302` → IC=+0.139 (n=1556)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.1302 (IC base=+0.036)

- **PATRÓN** `volumen_regimen` < `0.8423` → IC=+0.149 (n=1126)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.8423 (IC base=+0.036)

- **PATRÓN** `volumen_regimen` > `1.1677` → IC=+0.139 (n=563)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` > 1.1677 (IC base=+0.036)

- **PATRÓN** `volumen_pendiente_norm` > `0.2852` → IC=+0.202 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2852 (IC base=+0.036)

- **PATRÓN** `volumen_spike_ratio` < `1.7767` → IC=+0.140 (n=1078)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.7767 (IC base=+0.036)

- **PATRÓN** `volumen_spike_ratio` > `2.1547` → IC=+0.153 (n=733)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 2.1547 (IC base=+0.036)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.167 (n=103)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=552)

- **FILTRO** `ibs_20min` < `0.2727` → IC=-0.191 (n=163)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2727
  - _Potencial_: sin este filtro IC_bueno=+0.105 (n=492)

- **FILTRO** `ibs_20min` > `0.2174` → IC=-0.132 (n=3569)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2174
  - _Potencial_: sin este filtro IC_bueno=+0.148 (n=1763)

- **FILTRO** `sigma_ewma_delta_pct` > `8.665` → IC=-0.238 (n=559)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.665
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=4773)

- **PATRÓN** `ibs_20min` > `0.7857` → IC=+0.180 (n=223)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.7857 (IC base=+0.031)

- **PATRÓN** `dist_vwap_pct` > `1.0156` → IC=+0.273 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0156 (IC base=+0.031)

- **PATRÓN** `dist_vwap_pct` < `0.4892` → IC=+0.262 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4892 (IC base=+0.031)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.1` → IC=+0.149 (n=209)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 3.1 (IC base=+0.031)

- **PATRÓN** `volumen_regimen` > `1.0155` → IC=+0.303 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0155 (IC base=+0.031)

- **PATRÓN** `volumen_pendiente_norm` < `0.1553` → IC=+0.276 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1553 (IC base=+0.031)

- **PATRÓN** `volumen_spike_ratio` < `2.5549` → IC=+0.279 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5549 (IC base=+0.031)

- **PATRÓN** `volumen_spike_ratio` > `1.5481` → IC=+0.258 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5481 (IC base=+0.031)

- **PATRÓN** `ibs_20min` < `0.2174` → IC=+0.148 (n=1763)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` < 0.2174 (IC base=-0.040)

- **PATRÓN** `dist_vwap_pct` > `0.2659` → IC=+0.276 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2659 (IC base=-0.040)

- **PATRÓN** `volumen_regimen` < `0.704` → IC=+0.302 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.704 (IC base=-0.040)

- **PATRÓN** `volumen_pendiente_norm` > `0.0812` → IC=+0.304 (n=314)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0812 (IC base=-0.040)

- **PATRÓN** `volumen_spike_ratio` < `2.43` → IC=+0.300 (n=667)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.43 (IC base=-0.040)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6094` → IC=-0.178 (n=976)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6094
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=2932)

- **FILTRO** `ibs_20min` < `0.75` → IC=-0.151 (n=2565)

  - _Acción_: SKIP cuando `ibs_20min` < 0.75
  - _Potencial_: sin este filtro IC_bueno=+0.096 (n=1343)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.162 (n=958)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=2950)

- **FILTRO** `ibs_20min` > `0.75` → IC=-0.203 (n=1407)

  - _Acción_: SKIP cuando `ibs_20min` > 0.75
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=4227)

- **PATRÓN** `dist_vwap_pct` > `1.0122` → IC=+0.332 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0122 (IC base=-0.066)

- **PATRÓN** `dist_vwap_pct` < `0.2465` → IC=+0.303 (n=597)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2465 (IC base=-0.066)

- **PATRÓN** `volumen_regimen` > `0.7038` → IC=+0.316 (n=611)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7038 (IC base=-0.066)

- **PATRÓN** `volumen_pendiente_norm` < `0.0985` → IC=+0.300 (n=644)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0985 (IC base=-0.066)

- **PATRÓN** `volumen_pendiente_norm` > `0.0704` → IC=+0.305 (n=270)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0704 (IC base=-0.066)

- **PATRÓN** `volumen_spike_ratio` < `1.4142` → IC=+0.316 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4142 (IC base=-0.066)

- **PATRÓN** `volumen_spike_ratio` > `1.8324` → IC=+0.306 (n=441)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8324 (IC base=-0.066)

- **PATRÓN** `dist_vwap_pct` > `0.7978` → IC=+0.271 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7978 (IC base=-0.005)

- **PATRÓN** `volumen_regimen` > `1.0685` → IC=+0.283 (n=699)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0685 (IC base=-0.005)

- **PATRÓN** `volumen_pendiente_norm` > `0.1044` → IC=+0.282 (n=536)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1044 (IC base=-0.005)

- **PATRÓN** `volumen_spike_ratio` < `2.1803` → IC=+0.263 (n=1249)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1803 (IC base=-0.005)

- **PATRÓN** `volumen_spike_ratio` > `1.4311` → IC=+0.263 (n=1419)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4311 (IC base=-0.005)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.209 (n=5833)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0098 (IC base=+0.096)

- **PATRÓN** `ibs_20min` > `0.3204` → IC=+0.168 (n=17483)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` > 0.3204 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` > `0.9477` → IC=+0.297 (n=1275)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9477 (IC base=+0.096)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.592` → IC=+0.161 (n=7840)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 3.592 (IC base=+0.096)

- **PATRÓN** `volumen_regimen` < `1.1704` → IC=+0.264 (n=6436)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1704 (IC base=+0.096)

- **PATRÓN** `volumen_regimen` > `0.6889` → IC=+0.269 (n=5750)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6889 (IC base=+0.096)

- **PATRÓN** `volumen_pendiente_norm` > `0.2397` → IC=+0.278 (n=1910)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2397 (IC base=+0.096)

- **PATRÓN** `volumen_spike_ratio` < `1.4592` → IC=+0.262 (n=3425)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4592 (IC base=+0.096)

- **PATRÓN** `volumen_spike_ratio` > `2.6405` → IC=+0.272 (n=3425)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6405 (IC base=+0.096)

- **PATRÓN** `ballena_activa_n` < `92.0` → IC=+0.295 (n=9865)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 92.0 (IC base=+0.096)

- **PATRÓN** `sigma_h` > `0.0093` → IC=+0.159 (n=5610)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0093 (IC base=+0.074)

- **PATRÓN** `ibs_20min` < `0.6577` → IC=+0.144 (n=16821)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.6577 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` < `0.7056` → IC=+0.261 (n=2338)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7056 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` > `1.1965` → IC=+0.265 (n=1771)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1965 (IC base=+0.074)

- **PATRÓN** `volumen_pendiente_norm` > `0.2947` → IC=+0.318 (n=1143)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2947 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` < `1.5792` → IC=+0.290 (n=3352)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5792 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` > `2.2649` → IC=+0.283 (n=3454)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2649 (IC base=+0.074)

- **PATRÓN** `ballena_activa_n` < `77.0` → IC=+0.295 (n=7558)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 77.0 (IC base=+0.074)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.5801` → IC=-0.128 (n=2400)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5801
  - _Potencial_: sin este filtro IC_bueno=+0.188 (n=2402)

- **FILTRO** `ibs_20min` > `0.7415` → IC=-0.213 (n=1008)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7415
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=3030)

- **FILTRO** `sigma_ewma_delta_pct` > `4.394` → IC=-0.207 (n=885)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.394
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=3153)

- **PATRÓN** `ibs_20min` > `0.9178` → IC=+0.312 (n=1202)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9178 (IC base=+0.030)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.017` → IC=+0.215 (n=851)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.017 (IC base=+0.030)

- **PATRÓN** `volumen_pendiente_norm` > `0.2294` → IC=+0.301 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2294 (IC base=+0.030)

- **PATRÓN** `volumen_spike_ratio` < `1.4427` → IC=+0.252 (n=523)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4427 (IC base=+0.030)

- **PATRÓN** `volumen_spike_ratio` > `2.2427` → IC=+0.274 (n=711)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2427 (IC base=+0.030)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.280 (n=1062)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.030)

- **PATRÓN** `ibs_20min` < `0.1633` → IC=+0.160 (n=1011)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.1633 (IC base=-0.029)

- **PATRÓN** `volumen_pendiente_norm` < `0.0719` → IC=+0.414 (n=466)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0719 (IC base=-0.029)

- **PATRÓN** `volumen_spike_ratio` < `2.5496` → IC=+0.409 (n=526)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5496 (IC base=-0.029)

- **PATRÓN** `ballena_activa_n` < `10.0` → IC=+0.414 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 10.0 (IC base=-0.029)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.1138` → IC=+0.212 (n=866)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1138 (IC base=+0.022)

- **PATRÓN** `volumen_regimen` < `1.1944` → IC=+0.193 (n=1704)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` < 1.1944 (IC base=+0.022)

- **PATRÓN** `volumen_regimen` > `0.6835` → IC=+0.200 (n=1522)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6835 (IC base=+0.022)

- **PATRÓN** `volumen_pendiente_norm` < `0.0744` → IC=+0.190 (n=1568)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` < 0.0744 (IC base=+0.022)

- **PATRÓN** `volumen_pendiente_norm` > `0.2755` → IC=+0.230 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2755 (IC base=+0.022)

- **PATRÓN** `volumen_spike_ratio` < `1.4226` → IC=+0.217 (n=560)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4226 (IC base=+0.022)

- **PATRÓN** `volumen_spike_ratio` > `2.4856` → IC=+0.194 (n=560)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.4856 (IC base=+0.022)

- **PATRÓN** `ballena_activa_n` < `273.0` → IC=+0.228 (n=1117)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 273.0 (IC base=+0.022)

- **PATRÓN** `volumen_regimen` > `0.6201` → IC=+0.236 (n=1091)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6201 (IC base=-0.003)

- **PATRÓN** `volumen_pendiente_norm` > `0.272` → IC=+0.289 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.272 (IC base=-0.003)

- **PATRÓN** `volumen_spike_ratio` < `1.5333` → IC=+0.243 (n=458)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5333 (IC base=-0.003)

- **PATRÓN** `volumen_spike_ratio` > `2.1623` → IC=+0.247 (n=472)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1623 (IC base=-0.003)

- **PATRÓN** `ballena_activa_n` < `201.0` → IC=+0.241 (n=350)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 201.0 (IC base=-0.003)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0118` → IC=+0.310 (n=852)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0118 (IC base=+0.267)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.274 (n=2675)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.267)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.310 (n=1341)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.267)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.287` → IC=+0.303 (n=632)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.287 (IC base=+0.267)

- **PATRÓN** `volumen_pendiente_norm` < `0.098` → IC=+0.280 (n=2223)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.098 (IC base=+0.267)

- **PATRÓN** `volumen_spike_ratio` > `1.6104` → IC=+0.273 (n=2463)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6104 (IC base=+0.267)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.278 (n=3030)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.267)

- **PATRÓN** `libro_liquidez` > `1965.9184` → IC=+0.283 (n=1157)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1965.9184 (IC base=+0.267)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.281 (n=1528)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 19.0 (IC base=+0.267)

- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.327 (n=1002)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0101 (IC base=+0.293)

- **PATRÓN** `drift_60min` |x|≤ `0.1812` → IC=+0.310 (n=970)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1812 (IC base=+0.293)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.318 (n=838)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.293)

- **PATRÓN** `ibs_20min` < `0.3689` → IC=+0.296 (n=2205)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3689 (IC base=+0.293)

- **PATRÓN** `ibs_20min` > `0.2593` → IC=+0.301 (n=1001)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2593 (IC base=+0.293)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.567` → IC=+0.311 (n=295)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.567 (IC base=+0.293)

- **PATRÓN** `volumen_pendiente_norm` < `0.1976` → IC=+0.292 (n=2152)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1976 (IC base=+0.293)

- **PATRÓN** `volumen_pendiente_norm` > `0.342` → IC=+0.308 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.342 (IC base=+0.293)

- **PATRÓN** `volumen_spike_ratio` < `1.5792` → IC=+0.298 (n=702)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5792 (IC base=+0.293)

- **PATRÓN** `volumen_spike_ratio` > `2.6661` → IC=+0.302 (n=954)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6661 (IC base=+0.293)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.293 (n=1164)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.293)

- **PATRÓN** `libro_liquidez` > `2048.3156` → IC=+0.307 (n=735)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2048.3156 (IC base=+0.293)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.294 (n=1417)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 19.0 (IC base=+0.293)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7372` → IC=-0.186 (n=1057)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7372
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=3175)

- **PATRÓN** `ibs_20min` > `0.8775` → IC=+0.172 (n=1004)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` > 0.8775 (IC base=+0.030)

- **PATRÓN** `dist_vwap_pct` > `0.1526` → IC=+0.235 (n=748)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1526 (IC base=+0.030)

- **PATRÓN** `dist_vwap_pct` < `0.2118` → IC=+0.232 (n=1204)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2118 (IC base=+0.030)

- **PATRÓN** `volumen_regimen` < `1.0079` → IC=+0.244 (n=1235)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0079 (IC base=+0.030)

- **PATRÓN** `volumen_regimen` > `0.6711` → IC=+0.232 (n=1253)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6711 (IC base=+0.030)

- **PATRÓN** `volumen_pendiente_norm` > `0.1021` → IC=+0.252 (n=438)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1021 (IC base=+0.030)

- **PATRÓN** `volumen_spike_ratio` < `1.3993` → IC=+0.245 (n=453)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3993 (IC base=+0.030)

- **PATRÓN** `ballena_activa_n` < `103.0` → IC=+0.268 (n=1221)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 103.0 (IC base=+0.030)

- **PATRÓN** `dist_vwap_pct` < `0.194` → IC=+0.232 (n=972)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.194 (IC base=-0.002)

- **PATRÓN** `volumen_regimen` < `1.0319` → IC=+0.236 (n=855)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0319 (IC base=-0.002)

- **PATRÓN** `volumen_pendiente_norm` < `0.101` → IC=+0.249 (n=898)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.101 (IC base=-0.002)

- **PATRÓN** `volumen_pendiente_norm` > `0.2847` → IC=+0.295 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2847 (IC base=-0.002)

- **PATRÓN** `volumen_spike_ratio` < `1.793` → IC=+0.271 (n=614)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.793 (IC base=-0.002)

- **PATRÓN** `volumen_spike_ratio` > `2.4356` → IC=+0.254 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4356 (IC base=-0.002)

- **PATRÓN** `ballena_activa_n` < `109.0` → IC=+0.266 (n=821)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 109.0 (IC base=-0.002)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.76` → IC=-0.215 (n=1841)

  - _Acción_: SKIP cuando `ibs_20min` < 0.76
  - _Potencial_: sin este filtro IC_bueno=+0.305 (n=1845)

- **FILTRO** `ibs_20min` > `0.6471` → IC=-0.234 (n=899)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6471
  - _Potencial_: sin este filtro IC_bueno=+0.120 (n=2706)

- **FILTRO** `sigma_ewma_delta_pct` > `8.508` → IC=-0.243 (n=419)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.508
  - _Potencial_: sin este filtro IC_bueno=+0.068 (n=3186)

- **PATRÓN** `ibs_20min` > `0.76` → IC=+0.305 (n=1845)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.76 (IC base=+0.046)

- **PATRÓN** `dist_vwap_pct` > `0.2146` → IC=+0.336 (n=813)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2146 (IC base=+0.046)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.529` → IC=+0.183 (n=572)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 9.529 (IC base=+0.046)

- **PATRÓN** `volumen_regimen` < `0.8446` → IC=+0.334 (n=922)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8446 (IC base=+0.046)

- **PATRÓN** `volumen_regimen` > `0.7018` → IC=+0.325 (n=1235)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7018 (IC base=+0.046)

- **PATRÓN** `volumen_pendiente_norm` < `0.1583` → IC=+0.323 (n=1431)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1583 (IC base=+0.046)

- **PATRÓN** `volumen_pendiente_norm` > `0.2752` → IC=+0.350 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2752 (IC base=+0.046)

- **PATRÓN** `volumen_spike_ratio` < `1.4368` → IC=+0.349 (n=448)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4368 (IC base=+0.046)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.341 (n=1192)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 49.0 (IC base=+0.046)

- **PATRÓN** `ibs_20min` < `0.6471` → IC=+0.120 (n=2706)

  - _Acción_: Kelly boost +0.60€ cuando `ibs_20min` < 0.6471 (IC base=+0.032)

- **PATRÓN** `dist_vwap_pct` < `0.2801` → IC=+0.249 (n=1168)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2801 (IC base=+0.032)

- **PATRÓN** `volumen_regimen` < `0.7017` → IC=+0.262 (n=527)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7017 (IC base=+0.032)

- **PATRÓN** `volumen_pendiente_norm` < `0.1014` → IC=+0.241 (n=1131)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1014 (IC base=+0.032)

- **PATRÓN** `volumen_pendiente_norm` > `0.0764` → IC=+0.262 (n=455)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0764 (IC base=+0.032)

- **PATRÓN** `volumen_spike_ratio` < `2.4243` → IC=+0.252 (n=1148)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4243 (IC base=+0.032)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.269 (n=1164)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 52.0 (IC base=+0.032)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0108` → IC=+0.346 (n=1742)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0108 (IC base=+0.303)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.304 (n=755)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.303)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.314 (n=934)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.303)

- **PATRÓN** `ibs_20min` > `0.66` → IC=+0.336 (n=1951)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.66 (IC base=+0.303)

- **PATRÓN** `dist_vwap_pct` > `0.2035` → IC=+0.328 (n=1091)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2035 (IC base=+0.303)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.798` → IC=+0.323 (n=946)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.798 (IC base=+0.303)

- **PATRÓN** `volumen_regimen` > `0.6266` → IC=+0.311 (n=1950)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6266 (IC base=+0.303)

- **PATRÓN** `volumen_pendiente_norm` > `0.2791` → IC=+0.345 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2791 (IC base=+0.303)

- **PATRÓN** `volumen_spike_ratio` > `1.425` → IC=+0.314 (n=1867)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.425 (IC base=+0.303)

- **PATRÓN** `libro_liquidez` > `2629.6954` → IC=+0.312 (n=1299)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2629.6954 (IC base=+0.303)

- **PATRÓN** `ballena_activa_n` < `41.0` → IC=+0.336 (n=1672)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 41.0 (IC base=+0.303)

- **PATRÓN** `sigma_h` > `0.0152` → IC=+0.334 (n=1371)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0152 (IC base=+0.303)

- **PATRÓN** `drift_60min` |x|≤ `0.1867` → IC=+0.306 (n=906)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1867 (IC base=+0.303)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.314 (n=793)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.303)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.304 (n=1011)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.303)

- **PATRÓN** `ibs_20min` < `0.3675` → IC=+0.328 (n=2057)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3675 (IC base=+0.303)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.345` → IC=+0.318 (n=387)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.345 (IC base=+0.303)

- **PATRÓN** `volumen_regimen` < `0.7186` → IC=+0.309 (n=905)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7186 (IC base=+0.303)

- **PATRÓN** `volumen_regimen` > `1.2233` → IC=+0.331 (n=686)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2233 (IC base=+0.303)

- **PATRÓN** `volumen_pendiente_norm` > `0.2838` → IC=+0.352 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2838 (IC base=+0.303)

- **PATRÓN** `volumen_spike_ratio` < `1.4161` → IC=+0.311 (n=627)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4161 (IC base=+0.303)

- **PATRÓN** `volumen_spike_ratio` > `2.1363` → IC=+0.306 (n=853)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1363 (IC base=+0.303)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0115` → IC=+0.226 (n=4298)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0115 (IC base=+0.181)

- **PATRÓN** `drift_60min` |x|≤ `0.0869` → IC=+0.201 (n=4302)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0869 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.190 (n=13376)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` > `0.5573` → IC=+0.235 (n=12893)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5573 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` > `0.1637` → IC=+0.208 (n=5191)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1637 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.232` → IC=+0.262 (n=2536)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.232 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `1.1862` → IC=+0.169 (n=8555)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.1862 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` > `0.6243` → IC=+0.165 (n=8556)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 0.6243 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.2929` → IC=+0.205 (n=1875)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2929 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `2.607` → IC=+0.191 (n=4166)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 2.607 (IC base=+0.181)

- **PATRÓN** `libro_liquidez` > `1979.8184` → IC=+0.182 (n=11519)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 1979.8184 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `95.0` → IC=+0.198 (n=11819)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 95.0 (IC base=+0.181)

- **PATRÓN** `sigma_h` < `0.0091` → IC=+0.183 (n=10924)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0091 (IC base=+0.180)

- **PATRÓN** `drift_60min` |x|≤ `0.0796` → IC=+0.228 (n=4141)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0796 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.209 (n=5844)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.237 (n=12410)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.024` → IC=+0.198 (n=2022)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 10.024 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.684` → IC=+0.181 (n=10945)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` < 2.684 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` < `1.1825` → IC=+0.162 (n=8855)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.1825 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.294` → IC=+0.225 (n=1837)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.294 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `2.6351` → IC=+0.188 (n=3883)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.6351 (IC base=+0.180)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.192 (n=11373)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 100.0 (IC base=+0.180)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.235 (n=722)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.216)

- **PATRÓN** `drift_60min` |x|≤ `0.3312` → IC=+0.231 (n=2157)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3312 (IC base=+0.216)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.227 (n=801)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.216)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.222 (n=1457)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.216)

- **PATRÓN** `ibs_20min` > `0.9275` → IC=+0.297 (n=1439)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9275 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.97` → IC=+0.330 (n=685)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.97 (IC base=+0.216)

- **PATRÓN** `volumen_pendiente_norm` > `0.2805` → IC=+0.271 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2805 (IC base=+0.216)

- **PATRÓN** `volumen_spike_ratio` > `1.4374` → IC=+0.216 (n=2040)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4374 (IC base=+0.216)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.229 (n=2330)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.216)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.225 (n=1290)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 14.0 (IC base=+0.216)

- **PATRÓN** `sigma_h` < `0.0081` → IC=+0.251 (n=1679)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0081 (IC base=+0.250)

- **PATRÓN** `sigma_h` > `0.0073` → IC=+0.264 (n=761)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0073 (IC base=+0.250)

- **PATRÓN** `drift_60min` |x|≤ `0.0941` → IC=+0.304 (n=739)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0941 (IC base=+0.250)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.254 (n=1719)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.250)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.254 (n=814)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.250)

- **PATRÓN** `ibs_20min` < `0.2946` → IC=+0.274 (n=1477)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2946 (IC base=+0.250)

- **PATRÓN** `volumen_pendiente_norm` < `0.1003` → IC=+0.252 (n=1468)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1003 (IC base=+0.250)

- **PATRÓN** `volumen_pendiente_norm` > `0.2975` → IC=+0.289 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2975 (IC base=+0.250)

- **PATRÓN** `volumen_spike_ratio` < `1.4323` → IC=+0.273 (n=530)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4323 (IC base=+0.250)

- **PATRÓN** `volumen_spike_ratio` > `2.6858` → IC=+0.254 (n=530)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6858 (IC base=+0.250)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.255 (n=1890)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.250)

- **PATRÓN** `libro_liquidez` > `1528.9218` → IC=+0.259 (n=1678)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1528.9218 (IC base=+0.250)

- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.254 (n=603)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 8.0 (IC base=+0.250)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.219 (n=652)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.154)

- **PATRÓN** `drift_60min` |x|≤ `0.1597` → IC=+0.184 (n=1297)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.1597 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.168 (n=2048)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.154)

- **PATRÓN** `ibs_20min` > `0.3353` → IC=+0.224 (n=1945)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3353 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` > `0.1352` → IC=+0.214 (n=1154)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1352 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.29` → IC=+0.226 (n=366)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.29 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` < `0.6924` → IC=+0.164 (n=856)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.6924 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` > `0.2804` → IC=+0.193 (n=311)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2804 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` < `1.5085` → IC=+0.171 (n=839)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.5085 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` > `2.4993` → IC=+0.166 (n=635)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 2.4993 (IC base=+0.154)

- **PATRÓN** `ballena_activa_n` < `229.0` → IC=+0.168 (n=827)

  - _Acción_: Kelly boost +0.84€ cuando `ballena_activa_n` < 229.0 (IC base=+0.154)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.169 (n=2041)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0058 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.2342` → IC=+0.173 (n=1796)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.2342 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.184 (n=975)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 15.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` < `0.6183` → IC=+0.206 (n=2041)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6183 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.447` → IC=+0.197 (n=387)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 11.447 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` < `1.2077` → IC=+0.159 (n=2041)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2077 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` < `0.0934` → IC=+0.148 (n=1730)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` < 0.0934 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `2.4989` → IC=+0.152 (n=1921)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.4989 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` > `1.4241` → IC=+0.145 (n=1920)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.4241 (IC base=+0.145)

- **PATRÓN** `ballena_activa_n` < `202.0` → IC=+0.182 (n=621)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 202.0 (IC base=+0.145)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0108` → IC=+0.238 (n=990)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0108 (IC base=+0.214)

- **PATRÓN** `drift_60min` |x|≤ `0.3956` → IC=+0.225 (n=1920)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3956 (IC base=+0.214)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.234 (n=798)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.214)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.304 (n=1128)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.214)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.435` → IC=+0.300 (n=507)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.435 (IC base=+0.214)

- **PATRÓN** `volumen_pendiente_norm` < `0.0992` → IC=+0.214 (n=1870)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0992 (IC base=+0.214)

- **PATRÓN** `volumen_pendiente_norm` > `0.3552` → IC=+0.233 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3552 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` < `1.7667` → IC=+0.216 (n=931)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7667 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` > `2.7105` → IC=+0.226 (n=959)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7105 (IC base=+0.214)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.221 (n=2605)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.214)

- **PATRÓN** `libro_liquidez` > `1960.841` → IC=+0.228 (n=990)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1960.841 (IC base=+0.214)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.247 (n=1647)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.236)

- **PATRÓN** `drift_60min` |x|≤ `0.5725` → IC=+0.251 (n=1870)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5725 (IC base=+0.236)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.280 (n=707)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.236)

- **PATRÓN** `ibs_20min` < `0.0092` → IC=+0.300 (n=823)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0092 (IC base=+0.236)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.512` → IC=+0.274 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.512 (IC base=+0.236)

- **PATRÓN** `volumen_pendiente_norm` > `0.3557` → IC=+0.278 (n=309)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3557 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` < `1.7474` → IC=+0.237 (n=786)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7474 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` > `2.1531` → IC=+0.238 (n=1191)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1531 (IC base=+0.236)

- **PATRÓN** `libro_liquidez` > `2046.5484` → IC=+0.243 (n=624)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2046.5484 (IC base=+0.236)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.239 (n=1184)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.236)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0074` → IC=+0.173 (n=2093)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0074 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.4062` → IC=+0.167 (n=2093)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.4062 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.163 (n=2169)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` > `0.3103` → IC=+0.215 (n=2094)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3103 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.1426` → IC=+0.199 (n=1269)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1426 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.752` → IC=+0.202 (n=364)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.752 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `1.0223` → IC=+0.159 (n=1842)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.0223 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.103` → IC=+0.179 (n=854)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.103 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `1.8174` → IC=+0.150 (n=1368)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.8174 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `2.5051` → IC=+0.166 (n=684)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 2.5051 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `4624.9709` → IC=+0.185 (n=1395)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 4624.9709 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `139.0` → IC=+0.159 (n=2032)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 139.0 (IC base=+0.150)

- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.154 (n=2199)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0072 (IC base=+0.127)

- **PATRÓN** `drift_60min` |x|≤ `0.3949` → IC=+0.145 (n=2198)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.3949 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.166 (n=1039)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 15.0 (IC base=+0.127)

- **PATRÓN** `ibs_20min` < `0.6858` → IC=+0.187 (n=2198)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.6858 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` < `0.1526` → IC=+0.157 (n=2201)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.1526 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.793` → IC=+0.158 (n=770)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 6.793 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` < `0.8558` → IC=+0.155 (n=1466)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.8558 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` > `0.2993` → IC=+0.197 (n=331)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2993 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` < `1.8098` → IC=+0.135 (n=1373)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 1.8098 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` > `1.4241` → IC=+0.127 (n=2058)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` > 1.4241 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `7483.8045` → IC=+0.192 (n=997)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 7483.8045 (IC base=+0.127)

- **PATRÓN** `ballena_activa_n` < `68.0` → IC=+0.148 (n=896)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 68.0 (IC base=+0.127)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0103` → IC=+0.178 (n=1068)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` > 0.0103 (IC base=+0.128)

- **PATRÓN** `drift_60min` |x|≤ `0.4388` → IC=+0.130 (n=2070)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.65€ cuando `drift_60min` |x|≤ 0.4388 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.170 (n=1119)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 15.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` > `0.4878` → IC=+0.216 (n=2353)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4878 (IC base=+0.128)

- **PATRÓN** `dist_vwap_pct` > `0.1959` → IC=+0.189 (n=1362)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.1959 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.571` → IC=+0.279 (n=501)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.571 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` < `1.1741` → IC=+0.144 (n=2353)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 1.1741 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` < `0.161` → IC=+0.136 (n=2386)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` < 0.161 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` < `1.4385` → IC=+0.151 (n=761)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 1.4385 (IC base=+0.128)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.130 (n=2461)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.02 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `2776.8203` → IC=+0.209 (n=1067)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2776.8203 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.167 (n=758)

  - _Acción_: Kelly boost +0.84€ cuando `ballena_activa_n` < 20.0 (IC base=+0.128)

- **PATRÓN** `sigma_h` < `0.0108` → IC=+0.138 (n=2407)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` < 0.0108 (IC base=+0.120)

- **PATRÓN** `drift_60min` |x|≤ `0.108` → IC=+0.174 (n=804)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.108 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.140 (n=2448)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 5.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` < `0.6` → IC=+0.219 (n=2411)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` < `0.1985` → IC=+0.149 (n=2278)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.1985 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.461` → IC=+0.131 (n=2126)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` < 2.461 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` < `1.1765` → IC=+0.129 (n=2404)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 1.1765 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` < `0.1654` → IC=+0.123 (n=2327)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.1654 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` > `0.2763` → IC=+0.150 (n=321)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.2763 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` < `1.4463` → IC=+0.133 (n=747)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 1.4463 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` > `2.4253` → IC=+0.138 (n=746)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 2.4253 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `2653.0738` → IC=+0.193 (n=1090)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 2653.0738 (IC base=+0.120)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.130 (n=1955)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 42.0 (IC base=+0.120)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0129` → IC=+0.246 (n=1935)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0129 (IC base=+0.222)

- **PATRÓN** `drift_60min` |x|≤ `0.1286` → IC=+0.238 (n=724)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1286 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.226 (n=2244)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.226 (n=1950)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` > `0.66` → IC=+0.258 (n=2173)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.66 (IC base=+0.222)

- **PATRÓN** `dist_vwap_pct` > `0.1821` → IC=+0.227 (n=1395)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1821 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.61` → IC=+0.252 (n=986)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.61 (IC base=+0.222)

- **PATRÓN** `volumen_regimen` < `1.1768` → IC=+0.224 (n=2166)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1768 (IC base=+0.222)

- **PATRÓN** `volumen_regimen` > `0.6187` → IC=+0.231 (n=2166)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6187 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` > `0.283` → IC=+0.272 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.283 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` < `2.4665` → IC=+0.227 (n=2107)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4665 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` > `1.8078` → IC=+0.231 (n=1405)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8078 (IC base=+0.222)

- **PATRÓN** `libro_liquidez` > `2847.7662` → IC=+0.225 (n=982)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2847.7662 (IC base=+0.222)

- **PATRÓN** `sigma_h` < `0.0127` → IC=+0.233 (n=975)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0127 (IC base=+0.229)

- **PATRÓN** `sigma_h` > `0.0226` → IC=+0.240 (n=1004)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0226 (IC base=+0.229)

- **PATRÓN** `drift_60min` |x|≤ `0.0881` → IC=+0.261 (n=739)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0881 (IC base=+0.229)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.247 (n=1075)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.229)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.229 (n=991)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.229)

- **PATRÓN** `ibs_20min` < `0.4286` → IC=+0.256 (n=2215)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4286 (IC base=+0.229)

- **PATRÓN** `dist_vwap_pct` > `0.295` → IC=+0.234 (n=577)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.295 (IC base=+0.229)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.326` → IC=+0.259 (n=421)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.326 (IC base=+0.229)

- **PATRÓN** `volumen_regimen` > `0.6409` → IC=+0.236 (n=2214)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6409 (IC base=+0.229)

- **PATRÓN** `volumen_pendiente_norm` > `0.2803` → IC=+0.284 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2803 (IC base=+0.229)

- **PATRÓN** `volumen_spike_ratio` > `1.4386` → IC=+0.231 (n=2060)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4386 (IC base=+0.229)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.206 (n=1457)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.183)

- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.193 (n=1100)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` > 0.0089 (IC base=+0.183)

- **PATRÓN** `drift_60min` |x|≤ `0.129` → IC=+0.203 (n=1451)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.129 (IC base=+0.183)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.216 (n=1624)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.183)

- **PATRÓN** `ibs_20min` > `0.4871` → IC=+0.218 (n=2946)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4871 (IC base=+0.183)

- **PATRÓN** `dist_vwap_pct` > `0.7874` → IC=+0.203 (n=486)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7874 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.623` → IC=+0.211 (n=1426)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.623 (IC base=+0.183)

- **PATRÓN** `volumen_regimen` < `0.8628` → IC=+0.206 (n=1977)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8628 (IC base=+0.183)

- **PATRÓN** `volumen_regimen` > `0.6964` → IC=+0.187 (n=2650)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` > 0.6964 (IC base=+0.183)

- **PATRÓN** `volumen_pendiente_norm` > `0.0998` → IC=+0.193 (n=1180)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.0998 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` < `1.4308` → IC=+0.197 (n=1069)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 1.4308 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` > `2.1935` → IC=+0.189 (n=1453)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 2.1935 (IC base=+0.183)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.190 (n=3723)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.02 (IC base=+0.183)

- **PATRÓN** `libro_liquidez` > `2685.4936` → IC=+0.190 (n=2946)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 2685.4936 (IC base=+0.183)

- **PATRÓN** `ballena_activa_n` < `148.0` → IC=+0.194 (n=3075)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 148.0 (IC base=+0.183)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.136 (n=1189)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` < 0.0038 (IC base=+0.088)

- **PATRÓN** `ibs_20min` < `0.3814` → IC=+0.161 (n=2375)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.3814 (IC base=+0.088)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.126 (n=1507)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 27.0 (IC base=+0.088)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.201 (n=409)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.179)

- **PATRÓN** `drift_60min` |x|≤ `0.3265` → IC=+0.200 (n=928)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3265 (IC base=+0.179)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.207 (n=847)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.179)

- **PATRÓN** `ibs_20min` > `0.6361` → IC=+0.236 (n=619)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6361 (IC base=+0.179)

- **PATRÓN** `dist_vwap_pct` > `0.3064` → IC=+0.198 (n=276)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.3064 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.079` → IC=+0.195 (n=395)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 3.079 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.114` → IC=+0.179 (n=894)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` < 4.114 (IC base=+0.179)

- **PATRÓN** `volumen_regimen` < `0.8753` → IC=+0.205 (n=619)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8753 (IC base=+0.179)

- **PATRÓN** `volumen_pendiente_norm` > `0.0716` → IC=+0.182 (n=366)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.0716 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` < `2.2024` → IC=+0.188 (n=799)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 2.2024 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` > `1.4097` → IC=+0.180 (n=908)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 1.4097 (IC base=+0.179)

- **PATRÓN** `libro_liquidez` > `14680.2655` → IC=+0.183 (n=619)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 14680.2655 (IC base=+0.179)

- **PATRÓN** `ballena_activa_n` < `158.0` → IC=+0.206 (n=396)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 158.0 (IC base=+0.179)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.140 (n=1102)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0057 (IC base=+0.117)

- **PATRÓN** `drift_60min` |x|≤ `0.2682` → IC=+0.142 (n=970)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.2682 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.130 (n=1001)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 7.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` < `0.6327` → IC=+0.168 (n=970)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` < 0.6327 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.694` → IC=+0.129 (n=219)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` > 8.694 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` > `1.0652` → IC=+0.145 (n=500)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 1.0652 (IC base=+0.117)

- **PATRÓN** `volumen_pendiente_norm` > `0.1609` → IC=+0.168 (n=293)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` > 0.1609 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` < `2.1209` → IC=+0.131 (n=958)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 2.1209 (IC base=+0.117)

- **PATRÓN** `ballena_activa_n` < `219.0` → IC=+0.163 (n=714)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 219.0 (IC base=+0.117)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.248 (n=669)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=+0.216)

- **PATRÓN** `drift_60min` |x|≤ `0.0935` → IC=+0.242 (n=335)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0935 (IC base=+0.216)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.231 (n=1047)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.216)

- **PATRÓN** `ibs_20min` > `0.3764` → IC=+0.259 (n=895)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3764 (IC base=+0.216)

- **PATRÓN** `dist_vwap_pct` > `0.3573` → IC=+0.217 (n=306)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3573 (IC base=+0.216)

- **PATRÓN** `dist_vwap_pct` < `0.2053` → IC=+0.222 (n=900)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2053 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.884` → IC=+0.244 (n=405)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.884 (IC base=+0.216)

- **PATRÓN** `volumen_regimen` < `0.8358` → IC=+0.227 (n=668)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8358 (IC base=+0.216)

- **PATRÓN** `volumen_regimen` > `1.1625` → IC=+0.223 (n=334)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1625 (IC base=+0.216)

- **PATRÓN** `volumen_pendiente_norm` > `0.2679` → IC=+0.250 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2679 (IC base=+0.216)

- **PATRÓN** `volumen_spike_ratio` < `1.4231` → IC=+0.241 (n=330)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4231 (IC base=+0.216)

- **PATRÓN** `volumen_spike_ratio` > `2.4632` → IC=+0.238 (n=330)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4632 (IC base=+0.216)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.216 (n=1121)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.216)

- **PATRÓN** `ibs_20min` < `0.1051` → IC=+0.165 (n=341)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` < 0.1051 (IC base=+0.063)

- **PATRÓN** `libro_liquidez` > `6456.6331` → IC=+0.136 (n=682)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 6456.6331 (IC base=+0.063)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0108` → IC=+0.187 (n=273)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.0108 (IC base=+0.167)

- **PATRÓN** `drift_60min` |x|≤ `0.5314` → IC=+0.168 (n=817)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.5314 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.221 (n=392)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.167)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.275 (n=375)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.167)

- **PATRÓN** `dist_vwap_pct` > `0.9831` → IC=+0.240 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9831 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.973` → IC=+0.249 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.973 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` < `1.059` → IC=+0.185 (n=719)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 1.059 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` > `0.7156` → IC=+0.175 (n=730)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` > 0.7156 (IC base=+0.167)

- **PATRÓN** `volumen_pendiente_norm` > `0.1632` → IC=+0.184 (n=223)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.1632 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` < `1.4446` → IC=+0.187 (n=263)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` < 1.4446 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` > `2.1768` → IC=+0.174 (n=357)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 2.1768 (IC base=+0.167)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.175 (n=845)

  - _Acción_: Kelly boost +0.88€ cuando `libro_spread` < 0.02 (IC base=+0.167)

- **PATRÓN** `libro_liquidez` > `3033.338` → IC=+0.191 (n=273)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 3033.338 (IC base=+0.167)

- **PATRÓN** `ibs_20min` < `0.5455` → IC=+0.135 (n=774)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` < 0.5455 (IC base=+0.053)

- **PATRÓN** `libro_liquidez` > `2711.5941` → IC=+0.146 (n=399)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 2711.5941 (IC base=+0.053)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.125 (n=574)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 21.0 (IC base=+0.053)

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
- **PATRÓN** `sigma_h` > `0.0115` → IC=+0.227 (n=5599)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0115 (IC base=+0.183)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.192 (n=17487)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 5.0 (IC base=+0.183)

- **PATRÓN** `ibs_20min` > `0.4474` → IC=+0.231 (n=16789)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4474 (IC base=+0.183)

- **PATRÓN** `dist_vwap_pct` > `0.8904` → IC=+0.208 (n=2046)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8904 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.259` → IC=+0.255 (n=4104)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.259 (IC base=+0.183)

- **PATRÓN** `volumen_regimen` < `1.2218` → IC=+0.170 (n=11258)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 1.2218 (IC base=+0.183)

- **PATRÓN** `volumen_pendiente_norm` > `0.2905` → IC=+0.207 (n=2228)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2905 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` > `2.6123` → IC=+0.197 (n=5443)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 2.6123 (IC base=+0.183)

- **PATRÓN** `libro_liquidez` > `1972.3921` → IC=+0.185 (n=14996)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 1972.3921 (IC base=+0.183)

- **PATRÓN** `ballena_activa_n` < `112.0` → IC=+0.204 (n=15409)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 112.0 (IC base=+0.183)

- **PATRÓN** `sigma_h` < `0.0096` → IC=+0.192 (n=13415)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0096 (IC base=+0.188)

- **PATRÓN** `drift_60min` |x|≤ `0.4907` → IC=+0.192 (n=15231)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.4907 (IC base=+0.188)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.210 (n=5645)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.188)

- **PATRÓN** `ibs_20min` < `0.5833` → IC=+0.243 (n=15239)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5833 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.817` → IC=+0.207 (n=2113)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.817 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.572` → IC=+0.191 (n=14731)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` < 3.572 (IC base=+0.188)

- **PATRÓN** `volumen_regimen` < `0.6333` → IC=+0.163 (n=3428)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.6333 (IC base=+0.188)

- **PATRÓN** `volumen_pendiente_norm` > `0.2904` → IC=+0.254 (n=2063)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2904 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` > `2.2582` → IC=+0.197 (n=6529)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.2582 (IC base=+0.188)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.216 (n=9507)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 40.0 (IC base=+0.188)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.236 (n=916)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.226)

- **PATRÓN** `drift_60min` |x|≤ `0.3474` → IC=+0.228 (n=2737)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3474 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.238 (n=1321)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.226)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.229 (n=1845)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.226)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.332 (n=1085)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.498` → IC=+0.354 (n=641)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.498 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` > `0.2318` → IC=+0.281 (n=487)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2318 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` < `1.445` → IC=+0.222 (n=876)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.445 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` > `2.2784` → IC=+0.237 (n=1192)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2784 (IC base=+0.226)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.243 (n=2916)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.226)

- **PATRÓN** `libro_liquidez` > `1997.365` → IC=+0.228 (n=1241)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1997.365 (IC base=+0.226)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.249 (n=1648)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 17.0 (IC base=+0.226)

- **PATRÓN** `sigma_h` < `0.0085` → IC=+0.267 (n=2334)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0085 (IC base=+0.262)

- **PATRÓN** `drift_60min` |x|≤ `0.1192` → IC=+0.285 (n=1027)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1192 (IC base=+0.262)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.268 (n=2135)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.262)

- **PATRÓN** `ibs_20min` < `0.5106` → IC=+0.288 (n=2334)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5106 (IC base=+0.262)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.154` → IC=+0.266 (n=463)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.154 (IC base=+0.262)

- **PATRÓN** `volumen_pendiente_norm` < `0.0952` → IC=+0.262 (n=2096)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0952 (IC base=+0.262)

- **PATRÓN** `volumen_pendiente_norm` > `0.286` → IC=+0.290 (n=327)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.286 (IC base=+0.262)

- **PATRÓN** `volumen_spike_ratio` < `1.5578` → IC=+0.265 (n=973)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5578 (IC base=+0.262)

- **PATRÓN** `volumen_spike_ratio` > `2.6411` → IC=+0.271 (n=737)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6411 (IC base=+0.262)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.264 (n=2628)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.262)

- **PATRÓN** `libro_liquidez` > `1633.064` → IC=+0.270 (n=2084)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1633.064 (IC base=+0.262)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.272 (n=961)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.262)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.199 (n=909)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.1044` → IC=+0.166 (n=1197)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.1044 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.161 (n=2837)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` > `0.3676` → IC=+0.225 (n=2431)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3676 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.1253` → IC=+0.196 (n=1397)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.1253 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.479` → IC=+0.162 (n=448)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 11.479 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.15` → IC=+0.152 (n=2501)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` < 4.15 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `0.6306` → IC=+0.175 (n=908)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.6306 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` < `0.072` → IC=+0.153 (n=2427)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` < 0.072 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.2716` → IC=+0.183 (n=389)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.2716 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `2.1833` → IC=+0.159 (n=2341)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.1833 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `1.5282` → IC=+0.155 (n=2376)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.5282 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `265.0` → IC=+0.183 (n=1150)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 265.0 (IC base=+0.150)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.165 (n=2265)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0058 (IC base=+0.143)

- **PATRÓN** `drift_60min` |x|≤ `0.256` → IC=+0.165 (n=1993)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.256 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.171 (n=848)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.143)

- **PATRÓN** `ibs_20min` < `0.6969` → IC=+0.198 (n=2265)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.6969 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.179` → IC=+0.159 (n=376)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 11.179 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` < `1.1917` → IC=+0.153 (n=2265)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 1.1917 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` > `0.2175` → IC=+0.195 (n=424)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2175 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` < `2.4315` → IC=+0.150 (n=2160)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.4315 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` > `1.7752` → IC=+0.154 (n=1440)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.7752 (IC base=+0.143)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=2940)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.143)

- **PATRÓN** `ballena_activa_n` < `275.0` → IC=+0.158 (n=920)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 275.0 (IC base=+0.143)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0123` → IC=+0.260 (n=932)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0123 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.234 (n=2920)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.226)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.227 (n=2507)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.226)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.305 (n=1042)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.303` → IC=+0.324 (n=596)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.303 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` < `0.0969` → IC=+0.231 (n=2475)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0969 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` > `3.1891` → IC=+0.241 (n=905)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.1891 (IC base=+0.226)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.235 (n=3332)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.226)

- **PATRÓN** `libro_liquidez` > `1827.0163` → IC=+0.234 (n=1863)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1827.0163 (IC base=+0.226)

- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.246 (n=2307)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0106 (IC base=+0.241)

- **PATRÓN** `drift_60min` |x|≤ `0.1809` → IC=+0.258 (n=1153)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1809 (IC base=+0.241)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.262 (n=980)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.241)

- **PATRÓN** `ibs_20min` < `0.0316` → IC=+0.307 (n=874)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0316 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.632` → IC=+0.294 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.632 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` > `0.3452` → IC=+0.300 (n=389)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3452 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` > `2.1351` → IC=+0.252 (n=1661)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1351 (IC base=+0.241)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.244 (n=1390)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.241)

- **PATRÓN** `libro_liquidez` > `2046.5484` → IC=+0.255 (n=875)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2046.5484 (IC base=+0.241)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.259 (n=1108)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.241)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.204 (n=975)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.4207` → IC=+0.159 (n=2887)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.4207 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.160 (n=2995)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 5.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` > `0.2458` → IC=+0.195 (n=2887)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 0.2458 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.1412` → IC=+0.172 (n=1524)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.1412 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.123` → IC=+0.160 (n=1171)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 4.123 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `0.8653` → IC=+0.166 (n=1925)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.8653 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.2802` → IC=+0.192 (n=375)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2802 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `1.5247` → IC=+0.163 (n=1240)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 1.5247 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` > `2.1716` → IC=+0.158 (n=1277)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 2.1716 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `6181.5625` → IC=+0.242 (n=1309)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6181.5625 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `74.0` → IC=+0.172 (n=1232)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 74.0 (IC base=+0.146)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.151 (n=2401)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0075 (IC base=+0.130)

- **PATRÓN** `drift_60min` |x|≤ `0.4377` → IC=+0.140 (n=2400)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.4377 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.156 (n=872)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 17.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` < `0.7369` → IC=+0.185 (n=2400)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.7369 (IC base=+0.130)

- **PATRÓN** `dist_vwap_pct` < `0.1485` → IC=+0.146 (n=2189)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.1485 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.071` → IC=+0.175 (n=367)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 11.071 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` < `0.6988` → IC=+0.144 (n=1057)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.6988 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` > `0.2961` → IC=+0.221 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2961 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` < `2.2242` → IC=+0.132 (n=2032)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 2.2242 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` > `1.4292` → IC=+0.136 (n=2307)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.4292 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `7204.7935` → IC=+0.213 (n=800)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7204.7935 (IC base=+0.130)

- **PATRÓN** `ballena_activa_n` < `67.0` → IC=+0.132 (n=787)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 67.0 (IC base=+0.130)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0085` → IC=+0.152 (n=1938)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` > 0.0085 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.178 (n=1065)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` > `0.4423` → IC=+0.200 (n=2907)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4423 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` > `1.0588` → IC=+0.208 (n=502)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0588 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.739` → IC=+0.267 (n=735)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.739 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` < `1.2211` → IC=+0.136 (n=2908)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 1.2211 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` < `0.1615` → IC=+0.126 (n=3025)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` < 0.1615 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` > `0.2791` → IC=+0.133 (n=374)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_pendiente_norm` > 0.2791 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` < `1.8311` → IC=+0.127 (n=1895)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 1.8311 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` > `2.1924` → IC=+0.130 (n=1288)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 2.1924 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.130 (n=3020)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.02 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `2497.3328` → IC=+0.231 (n=1318)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2497.3328 (IC base=+0.125)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.145 (n=911)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 24.0 (IC base=+0.125)

- **PATRÓN** `sigma_h` < `0.01` → IC=+0.152 (n=2435)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.01 (IC base=+0.117)

- **PATRÓN** `drift_60min` |x|≤ `0.1332` → IC=+0.155 (n=922)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.1332 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.131 (n=2854)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 5.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` < `0.6471` → IC=+0.213 (n=2768)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6471 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` < `0.2136` → IC=+0.136 (n=2393)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.2136 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.253` → IC=+0.134 (n=2667)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` < 3.253 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` < `0.7104` → IC=+0.140 (n=1217)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 0.7104 (IC base=+0.117)

- **PATRÓN** `volumen_pendiente_norm` > `0.2252` → IC=+0.174 (n=474)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.2252 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` < `1.4404` → IC=+0.153 (n=863)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 1.4404 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `2673.0464` → IC=+0.209 (n=922)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2673.0464 (IC base=+0.117)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.133 (n=2278)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 47.0 (IC base=+0.117)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0137` → IC=+0.251 (n=2451)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0137 (IC base=+0.231)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.236 (n=2862)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.231)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.238 (n=1832)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.231)

- **PATRÓN** `ibs_20min` > `0.61` → IC=+0.272 (n=2457)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.61 (IC base=+0.231)

- **PATRÓN** `dist_vwap_pct` > `0.1882` → IC=+0.246 (n=1479)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1882 (IC base=+0.231)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.737` → IC=+0.272 (n=922)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.737 (IC base=+0.231)

- **PATRÓN** `volumen_regimen` < `1.2311` → IC=+0.237 (n=2743)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2311 (IC base=+0.231)

- **PATRÓN** `volumen_regimen` > `0.64` → IC=+0.233 (n=2743)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.64 (IC base=+0.231)

- **PATRÓN** `volumen_pendiente_norm` > `0.2873` → IC=+0.257 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2873 (IC base=+0.231)

- **PATRÓN** `volumen_spike_ratio` > `2.5002` → IC=+0.252 (n=890)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5002 (IC base=+0.231)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.232 (n=3563)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.231)

- **PATRÓN** `libro_liquidez` > `2615.82` → IC=+0.237 (n=1829)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2615.82 (IC base=+0.231)

- **PATRÓN** `sigma_h` > `0.0255` → IC=+0.252 (n=951)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0255 (IC base=+0.230)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.237 (n=2682)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.230)

- **PATRÓN** `ibs_20min` < `0.5152` → IC=+0.264 (n=2850)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5152 (IC base=+0.230)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.196` → IC=+0.266 (n=545)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.196 (IC base=+0.230)

- **PATRÓN** `volumen_regimen` > `1.2292` → IC=+0.259 (n=951)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2292 (IC base=+0.230)

- **PATRÓN** `volumen_pendiente_norm` > `0.2819` → IC=+0.297 (n=378)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2819 (IC base=+0.230)

- **PATRÓN** `volumen_spike_ratio` > `1.4315` → IC=+0.232 (n=2647)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4315 (IC base=+0.230)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.194 (n=4944)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.246 (n=1693)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.209)

- **PATRÓN** `drift_60min` |x|≤ `0.5027` → IC=+0.219 (n=5066)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5027 (IC base=+0.209)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.225 (n=1839)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.209)

- **PATRÓN** `ibs_20min` > `0.9405` → IC=+0.249 (n=1689)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9405 (IC base=+0.209)

- **PATRÓN** `dist_vwap_pct` < `0.2455` → IC=+0.211 (n=3246)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2455 (IC base=+0.209)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.018` → IC=+0.217 (n=828)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.018 (IC base=+0.209)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.606` → IC=+0.210 (n=4510)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.606 (IC base=+0.209)

- **PATRÓN** `volumen_regimen` < `0.7051` → IC=+0.221 (n=1625)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7051 (IC base=+0.209)

- **PATRÓN** `volumen_pendiente_norm` < `0.1066` → IC=+0.209 (n=4732)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1066 (IC base=+0.209)

- **PATRÓN** `volumen_pendiente_norm` > `0.1667` → IC=+0.223 (n=1425)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1667 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` < `1.4541` → IC=+0.216 (n=1663)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4541 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` > `1.8451` → IC=+0.210 (n=3325)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8451 (IC base=+0.209)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.214 (n=3900)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.209)

- **PATRÓN** `libro_liquidez` > `2928.9788` → IC=+0.216 (n=4526)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2928.9788 (IC base=+0.209)

- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.240 (n=1241)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.193)

- **PATRÓN** `drift_60min` |x|≤ `0.4876` → IC=+0.208 (n=3720)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4876 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.214 (n=1254)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.208 (n=1658)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.193)

- **PATRÓN** `ibs_20min` < `0.7333` → IC=+0.199 (n=3720)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.7333 (IC base=+0.193)

- **PATRÓN** `dist_vwap_pct` > `0.6717` → IC=+0.200 (n=627)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6717 (IC base=+0.193)

- **PATRÓN** `dist_vwap_pct` < `0.2386` → IC=+0.190 (n=3415)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` < 0.2386 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.836` → IC=+0.203 (n=3335)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.836 (IC base=+0.193)

- **PATRÓN** `volumen_regimen` < `1.0964` → IC=+0.202 (n=3103)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0964 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` < `0.0976` → IC=+0.197 (n=3412)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` < 0.0976 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` > `0.2228` → IC=+0.195 (n=751)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2228 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` < `1.5326` → IC=+0.199 (n=1614)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.5326 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` > `2.1885` → IC=+0.201 (n=1662)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1885 (IC base=+0.193)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.194 (n=4944)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.01 (IC base=+0.193)

- **PATRÓN** `ballena_activa_n` < `176.0` → IC=+0.202 (n=3208)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 176.0 (IC base=+0.193)

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

- **PATRÓN** `drift_60min` |x|≤ `0.3687` → IC=+0.194 (n=1321)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.3687 (IC base=+0.178)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.225 (n=481)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.178)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.200 (n=482)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.178)

- **PATRÓN** `ibs_20min` < `0.1382` → IC=+0.207 (n=582)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1382 (IC base=+0.178)

- **PATRÓN** `ibs_20min` > `0.6081` → IC=+0.179 (n=599)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.6081 (IC base=+0.178)

- **PATRÓN** `dist_vwap_pct` > `0.7021` → IC=+0.186 (n=116)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.7021 (IC base=+0.178)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.38` → IC=+0.197 (n=1304)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` < 6.38 (IC base=+0.178)

- **PATRÓN** `volumen_regimen` < `1.2212` → IC=+0.192 (n=1321)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 1.2212 (IC base=+0.178)

- **PATRÓN** `volumen_pendiente_norm` > `0.2183` → IC=+0.202 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2183 (IC base=+0.178)

- **PATRÓN** `volumen_spike_ratio` < `1.4018` → IC=+0.196 (n=438)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 1.4018 (IC base=+0.178)

- **PATRÓN** `volumen_spike_ratio` > `1.8036` → IC=+0.187 (n=876)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 1.8036 (IC base=+0.178)

- **PATRÓN** `libro_liquidez` > `14901.4739` → IC=+0.191 (n=599)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 14901.4739 (IC base=+0.178)

- **PATRÓN** `ballena_activa_n` < `694.0` → IC=+0.190 (n=1277)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 694.0 (IC base=+0.178)

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
- **PATRÓN** `sigma_h` < `0.008` → IC=+0.214 (n=1378)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.008 (IC base=+0.197)

- **PATRÓN** `drift_60min` |x|≤ `0.4596` → IC=+0.205 (n=1378)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4596 (IC base=+0.197)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.215 (n=500)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.197)

- **PATRÓN** `ibs_20min` < `0.5194` → IC=+0.209 (n=919)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5194 (IC base=+0.197)

- **PATRÓN** `ibs_20min` > `0.7607` → IC=+0.199 (n=625)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.7607 (IC base=+0.197)

- **PATRÓN** `dist_vwap_pct` < `0.2166` → IC=+0.209 (n=1220)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2166 (IC base=+0.197)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.114` → IC=+0.206 (n=1239)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.114 (IC base=+0.197)

- **PATRÓN** `volumen_regimen` < `0.8778` → IC=+0.201 (n=919)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8778 (IC base=+0.197)

- **PATRÓN** `volumen_regimen` > `1.2314` → IC=+0.203 (n=460)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2314 (IC base=+0.197)

- **PATRÓN** `volumen_pendiente_norm` < `0.105` → IC=+0.200 (n=1266)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.105 (IC base=+0.197)

- **PATRÓN** `volumen_pendiente_norm` > `0.1638` → IC=+0.197 (n=411)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.1638 (IC base=+0.197)

- **PATRÓN** `volumen_spike_ratio` < `2.4495` → IC=+0.205 (n=1348)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4495 (IC base=+0.197)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.198 (n=1413)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.01 (IC base=+0.197)

- **PATRÓN** `sigma_h` < `0.008` → IC=+0.205 (n=1128)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.008 (IC base=+0.188)

- **PATRÓN** `drift_60min` |x|≤ `0.4923` → IC=+0.210 (n=1127)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4923 (IC base=+0.188)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.203 (n=439)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.198 (n=755)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 10.0 (IC base=+0.188)

- **PATRÓN** `ibs_20min` < `0.3986` → IC=+0.195 (n=752)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.3986 (IC base=+0.188)

- **PATRÓN** `ibs_20min` > `0.0867` → IC=+0.190 (n=1127)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.0867 (IC base=+0.188)

- **PATRÓN** `dist_vwap_pct` > `0.6674` → IC=+0.199 (n=197)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.6674 (IC base=+0.188)

- **PATRÓN** `dist_vwap_pct` < `0.2251` → IC=+0.189 (n=1090)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` < 0.2251 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.355` → IC=+0.195 (n=1025)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` < 4.355 (IC base=+0.188)

- **PATRÓN** `volumen_regimen` < `0.6394` → IC=+0.222 (n=376)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6394 (IC base=+0.188)

- **PATRÓN** `volumen_regimen` > `0.7214` → IC=+0.188 (n=1007)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` > 0.7214 (IC base=+0.188)

- **PATRÓN** `volumen_pendiente_norm` > `0.0742` → IC=+0.208 (n=474)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0742 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` < `2.1925` → IC=+0.197 (n=971)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 2.1925 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` > `2.5255` → IC=+0.192 (n=368)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.5255 (IC base=+0.188)

- **PATRÓN** `libro_liquidez` > `6773.2837` → IC=+0.196 (n=1127)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 6773.2837 (IC base=+0.188)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.220 (n=326)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0071 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.203 (n=762)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 3.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` > `0.925` → IC=+0.246 (n=336)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.925 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` > `0.7405` → IC=+0.236 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7405 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.222` → IC=+0.204 (n=400)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.222 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `0.6947` → IC=+0.226 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6947 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` < `0.1062` → IC=+0.193 (n=668)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` < 0.1062 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.0788` → IC=+0.192 (n=332)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.0788 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` < `1.5661` → IC=+0.196 (n=317)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 1.5661 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `2.4815` → IC=+0.207 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4815 (IC base=+0.181)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.187 (n=863)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.02 (IC base=+0.181)

- **PATRÓN** `libro_liquidez` > `3092.0404` → IC=+0.202 (n=662)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3092.0404 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.198 (n=724)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 52.0 (IC base=+0.181)

- **PATRÓN** `sigma_h` < `0.0093` → IC=+0.209 (n=362)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0093 (IC base=+0.205)

- **PATRÓN** `sigma_h` > `0.0126` → IC=+0.216 (n=181)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0126 (IC base=+0.205)

- **PATRÓN** `drift_60min` |x|≤ `0.6042` → IC=+0.228 (n=543)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6042 (IC base=+0.205)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.240 (n=371)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 9.0 (IC base=+0.205)

- **PATRÓN** `ibs_20min` < `0.7273` → IC=+0.225 (n=543)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7273 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` > `0.8487` → IC=+0.220 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8487 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` < `0.3064` → IC=+0.204 (n=458)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3064 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.868` → IC=+0.213 (n=486)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.868 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` < `0.7555` → IC=+0.218 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7555 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` > `0.9335` → IC=+0.206 (n=362)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.9335 (IC base=+0.205)

- **PATRÓN** `volumen_pendiente_norm` < `0.1073` → IC=+0.224 (n=469)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1073 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` > `2.2044` → IC=+0.244 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2044 (IC base=+0.205)

- **PATRÓN** `libro_liquidez` > `2981.8939` → IC=+0.225 (n=543)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2981.8939 (IC base=+0.205)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.236 (n=536)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 46.0 (IC base=+0.205)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.158 (n=737)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.004 (IC base=+0.070)

- **PATRÓN** `ibs_20min` > `0.3885` → IC=+0.143 (n=1583)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` > 0.3885 (IC base=+0.070)

- **PATRÓN** `dist_vwap_pct` > `0.3558` → IC=+0.159 (n=546)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.3558 (IC base=+0.070)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.991` → IC=+0.157 (n=461)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 8.991 (IC base=+0.070)

- **PATRÓN** `volumen_pendiente_norm` > `0.2748` → IC=+0.142 (n=219)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` > 0.2748 (IC base=+0.070)

- **PATRÓN** `ibs_20min` < `0.2051` → IC=+0.233 (n=582)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2051 (IC base=+0.057)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.358` → IC=+0.171 (n=138)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 10.358 (IC base=+0.057)

- **PATRÓN** `volumen_pendiente_norm` > `0.1467` → IC=+0.175 (n=238)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.1467 (IC base=+0.057)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.131 (n=553)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.65€ cuando `sigma_h` < 0.0056 (IC base=+0.087)

- **PATRÓN** `ibs_20min` > `0.5149` → IC=+0.190 (n=466)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.5149 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` > `0.1218` → IC=+0.154 (n=261)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` > 0.1218 (IC base=+0.087)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.123 (n=274)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0037 (IC base=+0.074)

- **PATRÓN** `ibs_20min` < `0.0493` → IC=+0.279 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0493 (IC base=+0.074)

- **PATRÓN** `volumen_pendiente_norm` > `0.2164` → IC=+0.197 (n=74)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2164 (IC base=+0.074)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` > `0.7006` → IC=-0.181 (n=92)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7006
  - _Potencial_: sin este filtro IC_bueno=+0.121 (n=278)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.129 (n=483)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.64€ cuando `sigma_h` < 0.006 (IC base=+0.092)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.157 (n=208)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 17.0 (IC base=+0.092)

- **PATRÓN** `ibs_20min` > `0.4223` → IC=+0.176 (n=516)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` > 0.4223 (IC base=+0.092)

- **PATRÓN** `dist_vwap_pct` > `0.1247` → IC=+0.199 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1247 (IC base=+0.092)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.204` → IC=+0.248 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.204 (IC base=+0.092)

- **PATRÓN** `volumen_regimen` < `0.8145` → IC=+0.125 (n=345)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` < 0.8145 (IC base=+0.092)

- **PATRÓN** `volumen_pendiente_norm` > `0.2854` → IC=+0.167 (n=73)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.2854 (IC base=+0.092)

- **PATRÓN** `ibs_20min` < `0.0314` → IC=+0.300 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0314 (IC base=+0.019)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.686` → IC=+0.239 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.686 (IC base=+0.019)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `ibs_20min` > `0.16` → IC=-0.204 (n=69)

  - _Acción_: SKIP cuando `ibs_20min` > 0.16
  - _Potencial_: sin este filtro IC_bueno=+0.224 (n=208)

- **PATRÓN** `ibs_20min` > `0.7458` → IC=+0.164 (n=364)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` > 0.7458 (IC base=+0.032)

- **PATRÓN** `dist_vwap_pct` > `0.7321` → IC=+0.142 (n=132)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.7321 (IC base=+0.032)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.332` → IC=+0.164 (n=117)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 9.332 (IC base=+0.032)

- **PATRÓN** `volumen_pendiente_norm` > `0.2784` → IC=+0.133 (n=77)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_pendiente_norm` > 0.2784 (IC base=+0.032)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.156 (n=239)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0103 (IC base=+0.075)

- **PATRÓN** `ibs_20min` < `0.16` → IC=+0.224 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.16 (IC base=+0.075)

- **PATRÓN** `dist_vwap_pct` < `0.1716` → IC=+0.141 (n=196)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.1716 (IC base=+0.075)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.474` → IC=+0.312 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.474 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` > `1.0779` → IC=+0.208 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0779 (IC base=+0.075)

- **PATRÓN** `volumen_pendiente_norm` > `0.1508` → IC=+0.234 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1508 (IC base=+0.075)

- **PATRÓN** `volumen_spike_ratio` < `2.18` → IC=+0.157 (n=164)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.18 (IC base=+0.075)

- **PATRÓN** `volumen_spike_ratio` > `1.3981` → IC=+0.160 (n=186)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.3981 (IC base=+0.075)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.147 (n=182)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.06 (IC base=+0.075)

### GBM_LATE_60M_FADE
- **FILTRO** `hora_utc` > `8.0` → IC=-0.336 (n=65)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.168 (n=245)

- **FILTRO** `dist_vwap_pct` > `0.2306` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2306
  - _Potencial_: sin este filtro IC_bueno=-0.195 (n=293)

- **FILTRO** `volumen_spike_ratio` > `2.8366` → IC=-0.200 (n=58)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.8366
  - _Potencial_: sin este filtro IC_bueno=-0.156 (n=178)

- **FILTRO** `libro_liquidez` < `888.9132` → IC=-0.222 (n=77)

  - _Acción_: SKIP cuando `libro_liquidez` < 888.9132
  - _Potencial_: sin este filtro IC_bueno=-0.198 (n=233)

- **FILTRO** `sigma_h` > `0.0052` → IC=-0.336 (n=65)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0052
  - _Potencial_: sin este filtro IC_bueno=-0.270 (n=198)

- **FILTRO** `dist_vwap_pct` > `0.4684` → IC=-0.405 (n=19)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4684
  - _Potencial_: sin este filtro IC_bueno=-0.276 (n=244)

- **FILTRO** `sigma_ewma_delta_pct` > `10.371` → IC=-0.321 (n=26)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 10.371
  - _Potencial_: sin este filtro IC_bueno=-0.282 (n=237)

- **FILTRO** `volumen_pendiente_norm` > `0.0465` → IC=-0.371 (n=29)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0465
  - _Potencial_: sin este filtro IC_bueno=-0.273 (n=148)

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

- **FILTRO** `volumen_regimen` < `0.5547` → IC=-0.274 (n=29)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.5547
  - _Potencial_: sin este filtro IC_bueno=-0.253 (n=87)

- **FILTRO** `volumen_spike_ratio` > `1.4938` → IC=-0.337 (n=41)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.4938
  - _Potencial_: sin este filtro IC_bueno=-0.204 (n=42)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `sigma_h` < `0.0026` → IC=-0.321 (n=26)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0026
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=78)

- **FILTRO** `drift_60min` |x|> `0.149` → IC=-0.315 (n=25)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.149
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=79)

- **FILTRO** `hora_utc` < `6.0` → IC=-0.375 (n=22)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.265 (n=79)

- **FILTRO** `ibs_20min` > `0.725` → IC=-0.389 (n=34)

  - _Acción_: SKIP cuando `ibs_20min` > 0.725
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=67)

- **FILTRO** `volumen_spike_ratio` < `1.442` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.442
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=52)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.284 (n=86)

- **FILTRO** `libro_liquidez` < `1582.3345` → IC=-0.308 (n=50)

  - _Acción_: SKIP cuando `libro_liquidez` < 1582.3345
  - _Potencial_: sin este filtro IC_bueno=-0.274 (n=51)

- **PATRÓN** `ibs_20min` > `0.941` → IC=+0.158 (n=36)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` > 0.941 (IC base=-0.151)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.395 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=92)

- **FILTRO** `ibs_20min` < `0.25` → IC=-0.284 (n=35)

  - _Acción_: SKIP cuando `ibs_20min` < 0.25
  - _Potencial_: sin este filtro IC_bueno=-0.197 (n=74)

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

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` > `0.156` → IC=-0.123 (n=279)

  - _Acción_: SKIP cuando `ibs_20min` > 0.156
  - _Potencial_: sin este filtro IC_bueno=+0.146 (n=544)

- **PATRÓN** `sigma_h` > `0.006` → IC=+0.195 (n=237)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` > 0.006 (IC base=+0.113)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.176 (n=202)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.113)

- **PATRÓN** `ibs_20min` > `0.6818` → IC=+0.149 (n=522)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` > 0.6818 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` > `0.7375` → IC=+0.211 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7375 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` < `0.6249` → IC=+0.172 (n=175)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` < 0.6249 (IC base=+0.113)

- **PATRÓN** `volumen_pendiente_norm` < `0.1532` → IC=+0.148 (n=427)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` < 0.1532 (IC base=+0.113)

- **PATRÓN** `volumen_spike_ratio` < `1.415` → IC=+0.171 (n=141)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.415 (IC base=+0.113)

- **PATRÓN** `ibs_20min` < `0.156` → IC=+0.146 (n=544)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.156 (IC base=+0.055)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.085` → IC=+0.177 (n=184)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 9.085 (IC base=+0.055)

- **PATRÓN** `volumen_pendiente_norm` > `0.2227` → IC=+0.122 (n=125)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_pendiente_norm` > 0.2227 (IC base=+0.055)

- **PATRÓN** `libro_liquidez` > `3242.4514` → IC=+0.135 (n=412)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 3242.4514 (IC base=+0.055)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.6889` → IC=-0.209 (n=53)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6889
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=161)

- **PATRÓN** `sigma_h` > `0.0035` → IC=+0.168 (n=191)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` > 0.0035 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.153 (n=194)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 12.0 (IC base=+0.135)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.143 (n=110)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 6.0 (IC base=+0.135)

- **PATRÓN** `ibs_20min` < `0.1684` → IC=+0.196 (n=287)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.1684 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.158` → IC=+0.164 (n=123)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 7.158 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.645` → IC=+0.135 (n=228)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` < 4.645 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` > `0.6211` → IC=+0.150 (n=287)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 0.6211 (IC base=+0.135)

- **PATRÓN** `volumen_pendiente_norm` < `0.0706` → IC=+0.152 (n=222)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` < 0.0706 (IC base=+0.135)

- **PATRÓN** `volumen_pendiente_norm` > `0.2726` → IC=+0.167 (n=49)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.2726 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` < `2.5202` → IC=+0.171 (n=256)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 2.5202 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` > `1.4447` → IC=+0.150 (n=255)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.4447 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `4595.2336` → IC=+0.143 (n=256)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 4595.2336 (IC base=+0.135)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `volumen_pendiente_norm` > `0.1263` → IC=-0.149 (n=35)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1263
  - _Potencial_: sin este filtro IC_bueno=+0.142 (n=171)

- **FILTRO** `ibs_20min` > `0.3277` → IC=-0.162 (n=75)

  - _Acción_: SKIP cuando `ibs_20min` > 0.3277
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=226)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.140 (n=123)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0039 (IC base=+0.096)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.191 (n=66)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 18.0 (IC base=+0.096)

- **PATRÓN** `ibs_20min` > `0.8015` → IC=+0.139 (n=164)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` > 0.8015 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` < `0.0908` → IC=+0.137 (n=155)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.0908 (IC base=+0.096)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.015` → IC=+0.142 (n=135)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 3.015 (IC base=+0.096)

- **PATRÓN** `volumen_regimen` < `0.6229` → IC=+0.182 (n=61)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 0.6229 (IC base=+0.096)

- **PATRÓN** `volumen_pendiente_norm` < `0.1263` → IC=+0.142 (n=171)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` < 0.1263 (IC base=+0.096)

- **PATRÓN** `volumen_spike_ratio` < `1.7963` → IC=+0.170 (n=104)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.7963 (IC base=+0.096)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.906` → IC=+0.219 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.906 (IC base=+0.021)

- **PATRÓN** `volumen_pendiente_norm` > `0.275` → IC=+0.136 (n=31)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` > 0.275 (IC base=+0.021)

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
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 13.0 (IC base=+0.251)

- **PATRÓN** `ibs_20min` > `0.6452` → IC=+0.275 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6452 (IC base=+0.251)

- **PATRÓN** `dist_vwap_pct` > `0.6502` → IC=+0.389 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6502 (IC base=+0.251)

- **PATRÓN** `dist_vwap_pct` < `0.2189` → IC=+0.257 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2189 (IC base=+0.251)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.318` → IC=+0.320 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.318 (IC base=+0.251)

- **PATRÓN** `volumen_regimen` < `0.5792` → IC=+0.323 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.5792 (IC base=+0.251)

- **PATRÓN** `volumen_pendiente_norm` > `0.1048` → IC=+0.333 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1048 (IC base=+0.251)

- **PATRÓN** `volumen_spike_ratio` < `1.4854` → IC=+0.397 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4854 (IC base=+0.251)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.253 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.251)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.321` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.321 (IC base=-0.091)

### LATE_WINDOW_5MIN
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.331 (n=69)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3447` → IC=+0.323 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3447 (IC base=+0.317)

- **PATRÓN** `elapsed_s` > `184.3` → IC=+0.389 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 184.3 (IC base=+0.317)

- **PATRÓN** `drift_15min` |x|≤ `1.0466` → IC=+0.457 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0466 (IC base=+0.317)

- **PATRÓN** `drift_60min` |x|≤ `0.969` → IC=+0.373 (n=61)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.969 (IC base=+0.317)

- **PATRÓN** `ballena_activa_n` < `1114.0` → IC=+0.370 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1114.0 (IC base=+0.317)

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

- **PATRÓN** `drift_ventana_pct` |x|> `0.3447` → IC=+0.323 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3447 (IC base=+0.317)

- **PATRÓN** `elapsed_s` > `184.3` → IC=+0.389 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 184.3 (IC base=+0.317)

- **PATRÓN** `drift_15min` |x|≤ `1.0466` → IC=+0.457 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0466 (IC base=+0.317)

- **PATRÓN** `drift_60min` |x|≤ `0.969` → IC=+0.373 (n=61)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.969 (IC base=+0.317)

- **PATRÓN** `ballena_activa_n` < `1114.0` → IC=+0.370 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1114.0 (IC base=+0.317)

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
- **PATRÓN** `libro_liquidez` > `2846.2656` → IC=+0.132 (n=569)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 2846.2656 (IC base=+0.101)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `libro_liquidez` > `2846.2656` → IC=+0.132 (n=569)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 2846.2656 (IC base=+0.101)

### LIQUIDACIONES_15M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=193)

- **FILTRO** `libro_liquidez` < `2848.5092` → IC=-0.204 (n=52)

  - _Acción_: SKIP cuando `libro_liquidez` < 2848.5092
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=157)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=304)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `libro_liquidez` < `10893.2451` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `libro_liquidez` < 10893.2451
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=69)

- **FILTRO** `py_entrada` < `0.515` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=33)

- **PATRÓN** `liq_n` > `6.0` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `liq_n` > 6.0 (IC base=-0.025)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `ballena_activa_n` > `63.0` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `ballena_activa_n` > 63.0
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
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=3525)

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
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=1298)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=1252)

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
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=419)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=400)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.139 (n=178)

  - _Acción_: Kelly boost +0.69€ cuando `py_entrada` < 0.495 (IC base=+0.022)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=841)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=841)

- **FILTRO** `py_entrada` < `0.44` → IC=-0.132 (n=259)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=662)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=825)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=825)

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
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=232)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=256)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=256)

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
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=259)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.129 (n=87)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=187)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.4` → IC=-0.124 (n=1386)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=3593)

### LIQUIDACIONES_DEPTH_FASE0#BNB#15min
- **FILTRO** `py_entrada` > `0.59` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=34)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.145 (n=60)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.122 (n=35)

- **FILTRO** `py_entrada` > `0.47` → IC=-0.143 (n=26)

  - _Acción_: SKIP cuando `py_entrada` > 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=10)

- **FILTRO** `hora_utc` < `17.0` → IC=-0.155 (n=27)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=9)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.46` → IC=+0.173 (n=148)

  - _Acción_: Kelly boost +0.87€ cuando `py_entrada` < 0.46 (IC base=+0.011)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.190 (n=56)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=251)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.143 (n=152)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=174)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.151 (n=41)

  - _Acción_: Kelly boost +0.76€ cuando `py_entrada` < 0.5 (IC base=+0.051)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.53` → IC=-0.127 (n=349)

  - _Acción_: SKIP cuando `py_entrada` < 0.53
  - _Potencial_: sin este filtro IC_bueno=+0.107 (n=120)

- **FILTRO** `profundidad_ratio` < `56.1` → IC=-0.167 (n=154)

  - _Acción_: SKIP cuando `profundidad_ratio` < 56.1
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=315)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.136 (n=196)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=219)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `profundidad_ratio` < `20.7` → IC=-0.137 (n=144)

  - _Acción_: SKIP cuando `profundidad_ratio` < 20.7
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=298)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.178 (n=85)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=363)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.120 (n=285)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=307)

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
- **FILTRO** `py_entrada` < `0.47` → IC=-0.166 (n=6007)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=18617)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.176 (n=6083)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=19217)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.196 (n=1097)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=3383)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.174 (n=1044)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.068 (n=3471)

- **PATRÓN** `py_entrada` > `0.495` → IC=+0.129 (n=3019)

  - _Acción_: Kelly boost +0.64€ cuando `py_entrada` > 0.495 (IC base=+0.041)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.145 (n=1182)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` > 1.0 (IC base=+0.041)

- **PATRÓN** `libro_liquidez` > `1306.896` → IC=+0.137 (n=2240)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 1306.896 (IC base=+0.041)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.128 (n=2114)

  - _Acción_: Kelly boost +0.64€ cuando `py_entrada` < 0.5 (IC base=+0.012)

- **PATRÓN** `libro_liquidez` > `1501.4735` → IC=+0.155 (n=1536)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 1501.4735 (IC base=+0.012)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.158 (n=834)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=2764)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.178 (n=881)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=2707)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.175 (n=1094)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.107 (n=3395)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.203 (n=1075)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.076 (n=3544)

- **PATRÓN** `ibs_20min` > `0.9645` → IC=+0.131 (n=1527)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` > 0.9645 (IC base=+0.038)

- **PATRÓN** `libro_liquidez` > `1539.24` → IC=+0.120 (n=2245)

  - _Acción_: Kelly boost +0.60€ cuando `libro_liquidez` > 1539.24 (IC base=+0.038)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.159 (n=1094)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=3392)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=2375)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.162 (n=758)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=2313)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.208 (n=761)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=2806)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=3546)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` > `20.0` → IC=-0.146 (n=125)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 20.0
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=438)

- **FILTRO** `py_entrada` < `0.445` → IC=-0.264 (n=138)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=425)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.234 (n=287)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=883)

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

- **FILTRO** `drift_20min_pct` |x|> `0.2067` → IC=-0.149 (n=109)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.2067
  - _Potencial_: sin este filtro IC_bueno=-0.119 (n=331)

- **FILTRO** `ibs_20min` > `0.9803` → IC=-0.194 (n=109)

  - _Acción_: SKIP cuando `ibs_20min` > 0.9803
  - _Potencial_: sin este filtro IC_bueno=-0.104 (n=331)

- **FILTRO** `libro_liquidez` < `3728.8927` → IC=-0.167 (n=220)

  - _Acción_: SKIP cuando `libro_liquidez` < 3728.8927
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=220)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=920)

- **FILTRO** `libro_liquidez` < `1762.8003` → IC=-0.161 (n=234)

  - _Acción_: SKIP cuando `libro_liquidez` < 1762.8003
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=705)

- **FILTRO** `libro_liquidez` < `2083.7972` → IC=-0.169 (n=348)

  - _Acción_: SKIP cuando `libro_liquidez` < 2083.7972
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=708)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.129 (n=16980)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=37835)

- **FILTRO** `py_entrada` < `0.33` → IC=-0.285 (n=13490)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=41325)

- **FILTRO** `ibs_7min` < `0.2381` → IC=-0.230 (n=13699)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2381
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=41116)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.153 (n=18258)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=36557)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.242 (n=16929)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=52054)

- **FILTRO** `ibs_7min` > `0.2857` → IC=-0.183 (n=17049)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2857
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=51934)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.148 (n=2737)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=6828)

- **FILTRO** `py_entrada` < `0.46` → IC=-0.236 (n=4726)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=4839)

- **FILTRO** `ibs_7min` < `0.7126` → IC=-0.244 (n=3156)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7126
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=6409)

- **FILTRO** `ballena_activa_n` > `6.0` → IC=-0.179 (n=2032)

  - _Acción_: SKIP cuando `ballena_activa_n` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=7533)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.271 (n=2970)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=8989)

- **FILTRO** `ibs_7min` > `0.7708` → IC=-0.211 (n=2989)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7708
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=8970)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.266 (n=2163)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=7080)

- **FILTRO** `ibs_7min` < `0.726` → IC=-0.201 (n=2310)

  - _Acción_: SKIP cuando `ibs_7min` < 0.726
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=6933)

- **FILTRO** `ballena_activa_n` > `154.0` → IC=-0.192 (n=2306)

  - _Acción_: SKIP cuando `ballena_activa_n` > 154.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=6937)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.265 (n=2317)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=7089)

- **FILTRO** `ibs_7min` > `0.2678` → IC=-0.197 (n=2349)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2678
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=7057)

- **FILTRO** `ballena_activa_n` > `151.0` → IC=-0.183 (n=2346)

  - _Acción_: SKIP cuando `ballena_activa_n` > 151.0
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=7060)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.158 (n=2239)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=6859)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.314 (n=2240)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=6858)

- **FILTRO** `ibs_7min` < `0.2963` → IC=-0.247 (n=3001)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2963
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=6097)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.195 (n=2160)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=6938)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.255 (n=2974)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=9758)

- **FILTRO** `ibs_7min` > `0.7338` → IC=-0.178 (n=3182)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7338
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=9550)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.262 (n=2094)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=6840)

- **FILTRO** `ibs_7min` < `0.7289` → IC=-0.187 (n=2232)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7289
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=6702)

- **FILTRO** `ballena_activa_n` > `27.0` → IC=-0.188 (n=2214)

  - _Acción_: SKIP cuando `ballena_activa_n` > 27.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=6720)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.270 (n=2089)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=7169)

- **FILTRO** `ibs_7min` > `0.2749` → IC=-0.180 (n=2314)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2749
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=6944)

- **FILTRO** `ballena_activa_n` > `26.0` → IC=-0.177 (n=2280)

  - _Acción_: SKIP cuando `ballena_activa_n` > 26.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=6978)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.284 (n=2154)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=6841)

- **FILTRO** `ibs_7min` < `0.2143` → IC=-0.233 (n=2240)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2143
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=6755)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.218 (n=2164)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=6831)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.191 (n=3187)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=9985)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.32` → IC=-0.292 (n=2116)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=6864)

- **FILTRO** `ibs_7min` < `0.2025` → IC=-0.222 (n=2245)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2025
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=6735)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.202 (n=1993)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=6987)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.216 (n=3047)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=9409)

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

- **FILTRO** `libro_liquidez` < `3255.5511` → IC=-0.155 (n=175)

  - _Acción_: SKIP cuando `libro_liquidez` < 3255.5511
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=528)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=387)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.3981` → IC=+0.140 (n=1162)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.70€ cuando `delta_ratio` |x|> 0.3981 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.131 (n=545)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 14.0 (IC base=+0.129)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.132 (n=436)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 4.0 (IC base=+0.129)

- **PATRÓN** `total_vol_5m` < `134023.4` → IC=+0.141 (n=1021)

  - _Acción_: Kelly boost +0.71€ cuando `total_vol_5m` < 134023.4 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `3649.4534` → IC=+0.148 (n=526)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 3649.4534 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.149 (n=377)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 11.0 (IC base=+0.129)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.4374` → IC=+0.152 (n=90)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.76€ cuando `delta_ratio` |x|> 0.4374 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.204 (n=130)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.137)

- **PATRÓN** `total_vol_5m` < `289.181` → IC=+0.143 (n=180)

  - _Acción_: Kelly boost +0.71€ cuando `total_vol_5m` < 289.181 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `2576.9482` → IC=+0.206 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2576.9482 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `7.0` → IC=+0.160 (n=98)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 7.0 (IC base=+0.137)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `delta_ratio` |x|> `0.3994` → IC=+0.135 (n=239)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.67€ cuando `delta_ratio` |x|> 0.3994 (IC base=+0.116)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.131 (n=215)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 14.0 (IC base=+0.116)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.125 (n=286)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.04 (IC base=+0.116)

- **PATRÓN** `libro_liquidez` > `2340.1091` → IC=+0.134 (n=159)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 2340.1091 (IC base=+0.116)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.416` → IC=+0.175 (n=155)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.88€ cuando `delta_ratio` |x|> 0.416 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.188 (n=78)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 16.0 (IC base=+0.137)

- **PATRÓN** `total_vol_5m` < `384.1453` → IC=+0.211 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 384.1453 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `7706.3933` → IC=+0.143 (n=155)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 7706.3933 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `70.0` → IC=+0.195 (n=103)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 70.0 (IC base=+0.137)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.4324` → IC=+0.250 (n=94)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio` |x|> 0.4324 (IC base=+0.152)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.172 (n=190)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 15.0 (IC base=+0.152)

- **PATRÓN** `total_vol_5m` < `4950.202` → IC=+0.186 (n=138)

  - _Acción_: Kelly boost +0.93€ cuando `total_vol_5m` < 4950.202 (IC base=+0.152)

- **PATRÓN** `libro_liquidez` > `3257.229` → IC=+0.161 (n=184)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 3257.229 (IC base=+0.152)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.162 (n=72)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 27.0 (IC base=+0.152)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `hora_utc` < `14.0` → IC=+0.126 (n=196)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 14.0 (IC base=+0.101)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.192 (n=131)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.01 (IC base=+0.101)

- **PATRÓN** `libro_liquidez` > `3584.1484` → IC=+0.160 (n=98)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 3584.1484 (IC base=+0.101)

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
- **FILTRO** `sigma_h` > `0.0072` → IC=-0.197 (n=31)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0072
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=33)

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

- **FILTRO** `sigma_h` < `0.0049` → IC=-0.248 (n=129)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0049
  - _Potencial_: sin este filtro IC_bueno=-0.221 (n=388)

- **FILTRO** `pct_vs_K` |x|> `3.3065` → IC=-0.431 (n=129)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.3065
  - _Potencial_: sin este filtro IC_bueno=-0.159 (n=388)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `sigma_h` < `0.0044` → IC=-0.206 (n=49)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0044
  - _Potencial_: sin este filtro IC_bueno=-0.142 (n=149)

- **FILTRO** `pct_vs_K` |x|> `2.7876` → IC=-0.363 (n=49)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.7876
  - _Potencial_: sin este filtro IC_bueno=-0.089 (n=149)

- **FILTRO** `T_h` > `144.2373` → IC=-0.287 (n=45)

  - _Acción_: SKIP cuando `T_h` > 144.2373
  - _Potencial_: sin este filtro IC_bueno=-0.257 (n=138)

- **FILTRO** `pct_vs_K` |x|> `2.9891` → IC=-0.436 (n=45)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.9891
  - _Potencial_: sin este filtro IC_bueno=-0.207 (n=138)

### PRICE_TARGET_GBM_FADE#BTC#reach
- **FILTRO** `T_h` < `139.5329` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `T_h` < 139.5329
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

- **FILTRO** `sigma_h` < `0.0078` → IC=-0.262 (n=19)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0078
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=10)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `pct_vs_K` |x|> `3.2636` → IC=-0.402 (n=59)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.2636
  - _Potencial_: sin este filtro IC_bueno=-0.181 (n=117)

- **FILTRO** `sigma_h` > `0.0089` → IC=-0.357 (n=40)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0089
  - _Potencial_: sin este filtro IC_bueno=-0.118 (n=121)

- **FILTRO** `sigma_h` < `0.005` → IC=-0.214 (n=40)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.005
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=121)

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
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=306)

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
- **PATRÓN** `streak_estiramiento` < `0.258` → IC=+0.175 (n=38)

  - _Acción_: Kelly boost +0.88€ cuando `streak_estiramiento` < 0.258 (IC base=+0.008)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.136 (n=116)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 7.0 (IC base=+0.087)

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
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=42)

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

  - _Acción_: Kelly boost +1.00€ cuando `regimen_ma_toques` > 4.0 (IC base=+0.045)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=996)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=1330)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=1138)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=1195)

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
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=4002)

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
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=2211)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.200 (n=1202)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.179)

- **PATRÓN** `sigma_h` > `0.012` → IC=+0.197 (n=1201)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` > 0.012 (IC base=+0.179)

- **PATRÓN** `drift_60min` |x|≤ `0.1752` → IC=+0.194 (n=3174)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.1752 (IC base=+0.179)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1331` → IC=+0.192 (n=1437)

  - _Acción_: Kelly boost +0.96€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1331 (IC base=+0.179)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.186 (n=3337)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 6.0 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.182 (n=3322)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 15.0 (IC base=+0.179)

- **PATRÓN** `ibs_15` > `0.5548` → IC=+0.254 (n=3603)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5548 (IC base=+0.179)

- **PATRÓN** `dist_vwap_pct` > `0.1286` → IC=+0.170 (n=1717)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.1286 (IC base=+0.179)

- **PATRÓN** `dist_vwap_pct` < `0.3141` → IC=+0.166 (n=2854)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.3141 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.542` → IC=+0.257 (n=937)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.542 (IC base=+0.179)

- **PATRÓN** `libro_liquidez` > `4676.7697` → IC=+0.197 (n=1201)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 4676.7697 (IC base=+0.179)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=1427)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.254 (n=270)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.221)

- **PATRÓN** `drift_60min` |x|≤ `0.0584` → IC=+0.268 (n=205)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0584 (IC base=+0.221)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2522` → IC=+0.248 (n=204)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2522 (IC base=+0.221)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2297` → IC=+0.235 (n=356)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2297 (IC base=+0.221)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.241 (n=612)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.221)

- **PATRÓN** `ibs_15` > `0.7184` → IC=+0.287 (n=612)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7184 (IC base=+0.221)

- **PATRÓN** `dist_vwap_pct` > `0.2385` → IC=+0.243 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2385 (IC base=+0.221)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.96` → IC=+0.304 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.96 (IC base=+0.221)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.222 (n=794)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.221)

- **PATRÓN** `libro_liquidez` > `8860.1302` → IC=+0.231 (n=612)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8860.1302 (IC base=+0.221)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.188 (n=238)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0035 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.0668` → IC=+0.158 (n=314)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.0668 (IC base=+0.147)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1438` → IC=+0.152 (n=475)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.76€ cuando `delta_ratio_macro` |x|> 0.1438 (IC base=+0.147)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1312` → IC=+0.166 (n=282)

  - _Acción_: Kelly boost +0.83€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1312 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.155 (n=654)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 6.0 (IC base=+0.147)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.152 (n=743)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 17.0 (IC base=+0.147)

- **PATRÓN** `ibs_15` > `0.5415` → IC=+0.243 (n=713)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5415 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` > `0.1194` → IC=+0.161 (n=440)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.1194 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.707` → IC=+0.265 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.707 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `3215.6409` → IC=+0.154 (n=713)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 3215.6409 (IC base=+0.147)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `sigma_ewma_delta_pct` > `17.763` → IC=-0.175 (n=38)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 17.763
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=333)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `drift_60min` |x|≤ `0.1757` → IC=+0.137 (n=543)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.68€ cuando `drift_60min` |x|≤ 0.1757 (IC base=+0.097)

- **PATRÓN** `ibs_15` > `0.8929` → IC=+0.258 (n=271)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8929 (IC base=+0.097)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.356` → IC=+0.156 (n=155)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 17.356 (IC base=+0.097)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.135 (n=450)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.097)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `8.524` → IC=+0.132 (n=74)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` > 8.524 (IC base=+0.007)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0239` → IC=+0.236 (n=275)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0239 (IC base=+0.202)

- **PATRÓN** `drift_60min` |x|≤ `0.0864` → IC=+0.237 (n=363)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0864 (IC base=+0.202)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3374` → IC=+0.231 (n=726)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3374 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.202 (n=752)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.202)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.214 (n=736)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.202)

- **PATRÓN** `ibs_15` > `0.5354` → IC=+0.281 (n=824)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5354 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` > `0.1292` → IC=+0.209 (n=475)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1292 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` < `0.3258` → IC=+0.202 (n=796)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3258 (IC base=+0.202)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.103` → IC=+0.228 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.103 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `2964.5226` → IC=+0.294 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2964.5226 (IC base=+0.202)

- **PATRÓN** `ibs_15` < `0.1111` → IC=+0.157 (n=783)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.79€ cuando `ibs_15` < 0.1111 (IC base=+0.066)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` > `0.0056` → IC=+0.392 (n=211)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0056 (IC base=+0.366)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1497` → IC=+0.384 (n=421)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1497 (IC base=+0.366)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1403` → IC=+0.384 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1403 (IC base=+0.366)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.379 (n=636)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.366)

- **PATRÓN** `ibs_15` > `0.7873` → IC=+0.401 (n=632)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7873 (IC base=+0.366)

- **PATRÓN** `dist_vwap_pct` > `0.1461` → IC=+0.385 (n=362)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1461 (IC base=+0.366)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.239` → IC=+0.386 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.239 (IC base=+0.366)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.370 (n=769)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.366)

- **PATRÓN** `libro_liquidez` > `3505.1277` → IC=+0.374 (n=632)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3505.1277 (IC base=+0.366)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.366 (n=289)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.366)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.402 (n=110)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.366)

- **PATRÓN** `drift_60min` |x|≤ `0.0553` → IC=+0.366 (n=110)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0553 (IC base=+0.366)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1537` → IC=+0.382 (n=218)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1537 (IC base=+0.366)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1371` → IC=+0.393 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1371 (IC base=+0.366)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.385 (n=328)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.366)

- **PATRÓN** `ibs_15` > `0.8066` → IC=+0.391 (n=328)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8066 (IC base=+0.366)

- **PATRÓN** `dist_vwap_pct` > `0.2458` → IC=+0.398 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2458 (IC base=+0.366)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.571` → IC=+0.379 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.571 (IC base=+0.366)

- **PATRÓN** `libro_liquidez` > `16828.3206` → IC=+0.402 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16828.3206 (IC base=+0.366)

- **PATRÓN** `ballena_activa_n` < `493.0` → IC=+0.411 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 493.0 (IC base=+0.366)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.368 (n=134)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.365)

- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.386 (n=138)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0058 (IC base=+0.365)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0897` → IC=+0.380 (n=273)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0897 (IC base=+0.365)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.298` → IC=+0.382 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.298 (IC base=+0.365)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.392 (n=146)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.365)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.372 (n=139)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.365)

- **PATRÓN** `ibs_15` > `0.7479` → IC=+0.412 (n=304)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7479 (IC base=+0.365)

- **PATRÓN** `dist_vwap_pct` > `0.4536` → IC=+0.381 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4536 (IC base=+0.365)

- **PATRÓN** `dist_vwap_pct` < `0.2918` → IC=+0.367 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2918 (IC base=+0.365)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.861` → IC=+0.392 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.861 (IC base=+0.365)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.369 (n=341)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.365)

- **PATRÓN** `libro_liquidez` > `4001.8474` → IC=+0.393 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4001.8474 (IC base=+0.365)

- **PATRÓN** `ballena_activa_n` < `137.0` → IC=+0.368 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 137.0 (IC base=+0.365)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0069` → IC=-0.175 (n=2166)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0069
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=2168)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.212 (n=1692)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=2642)

- **PATRÓN** `ibs_15` > `0.6324` → IC=+0.283 (n=1047)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6324 (IC base=-0.068)

- **PATRÓN** `dist_vwap_pct` > `0.1122` → IC=+0.208 (n=595)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1122 (IC base=-0.068)

- **PATRÓN** `dist_vwap_pct` < `0.2664` → IC=+0.198 (n=895)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` < 0.2664 (IC base=-0.068)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2306` → IC=+0.268 (n=1198)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2306 (IC base=-0.013)

- **PATRÓN** `ibs_15` < `0.3596` → IC=+0.282 (n=3593)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3596 (IC base=-0.013)

- **PATRÓN** `dist_vwap_pct` > `0.6529` → IC=+0.277 (n=456)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6529 (IC base=-0.013)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0067` → IC=-0.218 (n=632)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0067
  - _Potencial_: sin este filtro IC_bueno=-0.187 (n=1898)

- **FILTRO** `sigma_h` < `0.0039` → IC=-0.223 (n=833)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0039
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=1697)

- **FILTRO** `sigma_ewma_delta_pct` > `23.159` → IC=-0.269 (n=366)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 23.159
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=2164)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.216 (n=65)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.194 (n=2465)

- **FILTRO** `libro_liquidez` < `11410.2889` → IC=-0.219 (n=632)

  - _Acción_: SKIP cuando `libro_liquidez` < 11410.2889
  - _Potencial_: sin este filtro IC_bueno=-0.186 (n=1898)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.122 (n=754)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0053 (IC base=+0.096)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2047` → IC=+0.296 (n=155)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2047 (IC base=+0.096)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1079` → IC=+0.279 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1079 (IC base=+0.096)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.135 (n=368)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 15.0 (IC base=+0.096)

- **PATRÓN** `ibs_15` > `0.7572` → IC=+0.336 (n=340)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7572 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` > `0.1051` → IC=+0.292 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1051 (IC base=+0.096)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.545` → IC=+0.130 (n=379)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` > 8.545 (IC base=+0.096)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0659` → IC=+0.210 (n=60)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0659 (IC base=-0.195)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.159` → IC=+0.286 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.159 (IC base=-0.195)

- **PATRÓN** `ibs_15` < `0.618` → IC=+0.290 (n=60)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.618 (IC base=-0.195)

- **PATRÓN** `dist_vwap_pct` < `0.0459` → IC=+0.284 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0459 (IC base=-0.195)

- **PATRÓN** `ballena_activa_n` < `291.0` → IC=+0.360 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 291.0 (IC base=-0.195)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.158 (n=682)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.162 (n=462)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0058 (IC base=+0.150)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.156 (n=350)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0049 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.0704` → IC=+0.191 (n=231)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.0704 (IC base=+0.150)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3021` → IC=+0.193 (n=402)

  - _Acción_: Kelly boost +0.97€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3021 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.162 (n=527)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.150)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.151 (n=539)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 17.0 (IC base=+0.150)

- **PATRÓN** `ibs_15` > `0.5959` → IC=+0.248 (n=525)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5959 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.4658` → IC=+0.164 (n=135)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.4658 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` < `0.1598` → IC=+0.151 (n=414)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.1598 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.395` → IC=+0.238 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.395 (IC base=+0.150)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.158 (n=682)

  - _Acción_: Kelly boost +0.79€ cuando `libro_spread` < 0.01 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `9700.4747` → IC=+0.161 (n=175)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 9700.4747 (IC base=+0.150)

- **PATRÓN** `sigma_h` < `0.0077` → IC=+0.252 (n=1293)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0077 (IC base=+0.246)

- **PATRÓN** `drift_15min` |x|≤ `0.7686` → IC=+0.259 (n=1139)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7686 (IC base=+0.246)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1574` → IC=+0.258 (n=862)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1574 (IC base=+0.246)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.251 (n=471)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.246)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.248 (n=1156)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.246)

- **PATRÓN** `ibs_15` < `0.3696` → IC=+0.276 (n=1293)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3696 (IC base=+0.246)

- **PATRÓN** `dist_vwap_pct` > `0.2147` → IC=+0.263 (n=408)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2147 (IC base=+0.246)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.425` → IC=+0.257 (n=578)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.425 (IC base=+0.246)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `sigma_h` > `0.0105` → IC=-0.243 (n=251)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0105
  - _Potencial_: sin este filtro IC_bueno=-0.175 (n=754)

- **FILTRO** `drift_60min` |x|> `0.1729` → IC=-0.257 (n=340)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1729
  - _Potencial_: sin este filtro IC_bueno=-0.158 (n=665)

- **FILTRO** `drift_15min` |x|> `0.888` → IC=-0.283 (n=251)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.888
  - _Potencial_: sin este filtro IC_bueno=-0.161 (n=754)

- **FILTRO** `sigma_ewma_delta_pct` > `17.984` → IC=-0.148 (n=523)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 17.984
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=4157)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1478` → IC=+0.181 (n=45)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.90€ cuando `delta_ratio_macro` |x|> 0.1478 (IC base=-0.192)

- **PATRÓN** `ibs_15` > `0.5625` → IC=+0.234 (n=62)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5625 (IC base=-0.192)

- **PATRÓN** `dist_vwap_pct` < `0.1292` → IC=+0.167 (n=52)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.1292 (IC base=-0.192)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.233 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=-0.192)

- **PATRÓN** `delta_ratio_macro` |x|> `0.082` → IC=+0.236 (n=514)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.082 (IC base=-0.040)

- **PATRÓN** `ibs_15` < `0.3529` → IC=+0.293 (n=577)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3529 (IC base=-0.040)

- **PATRÓN** `dist_vwap_pct` < `0.4438` → IC=+0.244 (n=607)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4438 (IC base=-0.040)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0197` → IC=-0.251 (n=596)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0197
  - _Potencial_: sin este filtro IC_bueno=-0.163 (n=597)

- **FILTRO** `sigma_ewma_delta_pct` > `7.426` → IC=-0.212 (n=373)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 7.426
  - _Potencial_: sin este filtro IC_bueno=-0.204 (n=820)

- **FILTRO** `libro_spread` > `0.04` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.04
  - _Potencial_: sin este filtro IC_bueno=-0.206 (n=1174)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.207)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.207)

- **PATRÓN** `delta_ratio_macro` |x|> `0.069` → IC=+0.272 (n=771)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.069 (IC base=-0.026)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1165` → IC=+0.293 (n=375)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1165 (IC base=-0.026)

- **PATRÓN** `ibs_15` < `0.3333` → IC=+0.291 (n=865)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3333 (IC base=-0.026)

- **PATRÓN** `dist_vwap_pct` > `0.7702` → IC=+0.351 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7702 (IC base=-0.026)

### UPDOWN_GBM_ETH_15M_HORA7
- **PATRÓN** `ibs_15` > `0.8434` → IC=+0.333 (n=16)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8434 (IC base=+0.062)

- **PATRÓN** `dist_vwap_pct` < `0.1207` → IC=+0.147 (n=15)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.1207 (IC base=+0.062)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **PATRÓN** `ibs_15` > `0.8434` → IC=+0.333 (n=16)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8434 (IC base=+0.062)

- **PATRÓN** `dist_vwap_pct` < `0.1207` → IC=+0.147 (n=15)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.1207 (IC base=+0.062)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.300 (n=944)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.294)

- **PATRÓN** `drift_60min` |x|≤ `0.053` → IC=+0.322 (n=358)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.053 (IC base=+0.294)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2423` → IC=+0.311 (n=358)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2423 (IC base=+0.294)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2243` → IC=+0.309 (n=638)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2243 (IC base=+0.294)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.310 (n=1119)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.294)

- **PATRÓN** `ibs_15` > `0.8382` → IC=+0.322 (n=1073)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8382 (IC base=+0.294)

- **PATRÓN** `dist_vwap_pct` > `0.2698` → IC=+0.328 (n=458)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2698 (IC base=+0.294)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.497` → IC=+0.379 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.497 (IC base=+0.294)

- **PATRÓN** `libro_liquidez` > `12324.2702` → IC=+0.312 (n=487)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12324.2702 (IC base=+0.294)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.312 (n=254)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.291)

- **PATRÓN** `sigma_h` > `0.0046` → IC=+0.302 (n=261)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0046 (IC base=+0.291)

- **PATRÓN** `drift_60min` |x|≤ `0.0569` → IC=+0.320 (n=192)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0569 (IC base=+0.291)

- **PATRÓN** `delta_ratio_macro` |x|> `0.258` → IC=+0.314 (n=192)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.258 (IC base=+0.291)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.308 (n=576)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.291)

- **PATRÓN** `ibs_15` > `0.8279` → IC=+0.317 (n=576)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8279 (IC base=+0.291)

- **PATRÓN** `dist_vwap_pct` > `0.2546` → IC=+0.330 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2546 (IC base=+0.291)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.497` → IC=+0.384 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.497 (IC base=+0.291)

- **PATRÓN** `libro_liquidez` > `16201.6469` → IC=+0.330 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16201.6469 (IC base=+0.291)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.308 (n=498)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.297)

- **PATRÓN** `drift_60min` |x|≤ `0.0515` → IC=+0.321 (n=166)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0515 (IC base=+0.297)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0673` → IC=+0.300 (n=498)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0673 (IC base=+0.297)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2166` → IC=+0.320 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2166 (IC base=+0.297)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.311 (n=512)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.297)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.299 (n=451)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.297)

- **PATRÓN** `ibs_15` > `0.8489` → IC=+0.324 (n=498)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8489 (IC base=+0.297)

- **PATRÓN** `dist_vwap_pct` > `0.285` → IC=+0.330 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.285 (IC base=+0.297)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.513` → IC=+0.365 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.513 (IC base=+0.297)

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

- **FILTRO** `sigma_h` > `0.0029` → IC=-0.157 (n=33)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0029
  - _Potencial_: sin este filtro IC_bueno=-0.132 (n=17)

- **FILTRO** `drift_60min` |x|> `0.2244` → IC=-0.222 (n=16)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2244
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=34)

- **FILTRO** `drift_15min` |x|> `0.3481` → IC=-0.278 (n=16)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.3481
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=34)

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

- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.0905` → IC=-0.220 (n=23)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.0905
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

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

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5548 sube el IC de +0.179 a +0.254 en UPDOWN_GBM#15min (n=3603). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7184 sube el IC de +0.221 a +0.287 en UPDOWN_GBM#BTC#15min (n=612). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.5415 sube el IC de +0.147 a +0.243 en UPDOWN_GBM#ETH#15min (n=713). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.8929 sube el IC de +0.097 a +0.258 en UPDOWN_GBM#SOL#15min (n=271). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5354 sube el IC de +0.202 a +0.281 en UPDOWN_GBM#XRP#15min (n=824). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1111 sube el IC de +0.066 a +0.157 en UPDOWN_GBM#XRP#15min (n=783). Ya aplicado como kelly_boost=+0.79€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6324 sube el IC de -0.068 a +0.283 en UPDOWN_GBM_15M_TARDIO (n=1047). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3596 sube el IC de -0.013 a +0.282 en UPDOWN_GBM_15M_TARDIO (n=3593). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7572 sube el IC de +0.096 a +0.336 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=340). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.618 sube el IC de -0.195 a +0.290 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=60). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.5959 sube el IC de +0.150 a +0.248 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=525). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3696 sube el IC de +0.246 a +0.276 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=1293). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de -0.192 a +0.234 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=62). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3529 sube el IC de -0.040 a +0.293 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=577). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.207 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3333 sube el IC de -0.026 a +0.291 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=865). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_YES, IBS > 0.8434 sube el IC de +0.062 a +0.333 en UPDOWN_GBM_ETH_15M_HORA7 (n=16). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_YES, IBS > 0.8434 sube el IC de +0.062 a +0.333 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=16). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8382 sube el IC de +0.294 a +0.322 en UPDOWN_GBM_IBS_ALTO (n=1073). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8279 sube el IC de +0.291 a +0.317 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=576). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8489 sube el IC de +0.297 a +0.324 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=498). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7873 sube el IC de +0.366 a +0.401 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=632). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8066 sube el IC de +0.366 a +0.391 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=328). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7479 sube el IC de +0.365 a +0.412 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=304). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1932 | +0.091 | +218.55€ | 1 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1932 | +0.091 | +218.55€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1542 | +0.095 | +189.61€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1542 | +0.095 | +189.61€ | 0 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 282 | +0.070 | +11.51€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 282 | +0.070 | +11.51€ | 4 | 9 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 77 | +0.108 | +17.77€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 77 | +0.108 | +17.77€ | 0 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 649 | +0.001 | +76.31€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 649 | +0.001 | +76.31€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 470 | -0.025 | +43.60€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 470 | -0.025 | +43.60€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 140 | +0.077 | +24.60€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 140 | +0.077 | +24.60€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 36 | +0.026 | +4.76€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 36 | +0.026 | +4.76€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 40156 | -0.082 | -5045.85€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 2206 | +0.032 | -258.74€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 37950 | -0.089 | -4787.11€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4491 | -0.116 | -776.69€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4491 | -0.116 | -776.69€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 2206 | +0.032 | -258.74€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 2206 | +0.032 | -258.74€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 4317 | -0.105 | -875.34€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 4317 | -0.105 | -875.34€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 10708 | -0.022 | -1002.03€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 10708 | -0.022 | -1002.03€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 10590 | -0.105 | -811.99€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 10590 | -0.105 | -811.99€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 7844 | -0.134 | -1321.06€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 7844 | -0.134 | -1321.06€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 35116 | -0.015 | +3342.28€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 9087 | +0.005 | +1670.27€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 26029 | -0.022 | +1672.01€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 35116 | -0.015 | +3342.28€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 9087 | +0.005 | +1670.27€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 26029 | -0.022 | +1672.01€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 145421 | +0.116 | -5774.47€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 18635 | +0.183 | -564.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 639 | -0.016 | -68.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 117436 | +0.107 | -4817.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 8711 | +0.100 | -324.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 19475 | +0.108 | -1178.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 61 | -0.151 | +10.95€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 19399 | +0.109 | -1178.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 28164 | +0.129 | -392.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5199 | +0.188 | -177.45€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 19462 | +0.121 | -87.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 3461 | +0.082 | -104.80€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 19529 | +0.100 | -1350.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 74 | -0.118 | -5.77€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 19440 | +0.101 | -1333.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 30922 | +0.125 | -549.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 7999 | +0.178 | -140.23€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 19720 | +0.108 | -348.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 3191 | +0.100 | -52.32€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 27835 | +0.116 | -1380.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 5234 | +0.196 | -257.27€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 542 | +0.017 | -14.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 20000 | +0.096 | -941.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 2059 | +0.130 | -167.30€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#XRP | 19496 | +0.106 | -922.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 68 | -0.086 | +5.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 19415 | +0.107 | -928.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 23382 | +0.197 | -1399.25€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 23382 | +0.197 | -1399.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 5321 | +0.180 | -445.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 5321 | +0.180 | -445.52€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 2969 | +0.203 | -65.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 2969 | +0.203 | -65.94€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 5262 | +0.181 | -417.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 5262 | +0.181 | -417.18€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 4563 | +0.248 | -149.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 4563 | +0.248 | -149.15€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 5188 | +0.188 | -335.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 5188 | +0.188 | -335.21€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 1017 | +0.427 | -33.26€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 1017 | +0.427 | -33.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 400 | +0.435 | -6.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 400 | +0.435 | -6.41€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE#15min | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 400 | +0.433 | -7.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 400 | +0.433 | -7.74€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 203 | +0.402 | -15.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 203 | +0.402 | -15.25€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 81789 | +0.202 | -5798.32€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 81789 | +0.202 | -5798.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 14049 | +0.186 | -1440.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 14049 | +0.186 | -1440.58€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 13210 | +0.225 | -447.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 13210 | +0.225 | -447.92€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 14006 | +0.182 | -1455.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 14006 | +0.182 | -1455.82€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 13284 | +0.221 | -481.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 13284 | +0.221 | -481.18€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 13571 | +0.202 | -883.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 13571 | +0.202 | -883.04€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 13669 | +0.197 | -1089.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 13669 | +0.197 | -1089.78€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 31312 | +0.117 | +198.69€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 31312 | +0.117 | +198.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 15564 | +0.119 | +167.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 15564 | +0.119 | +167.72€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 15748 | +0.114 | +30.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 15748 | +0.114 | +30.97€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 2079 | +0.292 | -8.23€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 2079 | +0.292 | -8.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 952 | +0.279 | -27.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 952 | +0.279 | -27.03€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 1008 | +0.297 | +13.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 1008 | +0.297 | +13.49€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 119 | +0.351 | +5.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 119 | +0.351 | +5.31€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 957 | +0.442 | +4.38€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 957 | +0.442 | +4.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 464 | +0.436 | -4.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 464 | +0.436 | -4.56€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 447 | +0.449 | +8.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 447 | +0.449 | +8.39€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 46 | +0.396 | +0.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 46 | +0.396 | +0.55€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1649 | +0.072 | -63.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 637 | +0.052 | -51.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 1012 | +0.084 | -12.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 74 | +0.118 | +4.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 74 | +0.118 | +4.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1267 | +0.080 | -24.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 255 | +0.064 | -11.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 1012 | +0.084 | -12.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 308 | +0.026 | -43.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 308 | +0.026 | -43.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 61828 | +0.101 | -1558.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 5000 | +0.091 | +52.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 56828 | +0.101 | -1610.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 34017 | +0.106 | -377.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 5000 | +0.091 | +52.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 29017 | +0.108 | -429.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 12705 | +0.109 | -71.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 12705 | +0.109 | -71.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 15106 | +0.082 | -1109.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 15106 | +0.082 | -1109.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 897 | +0.193 | -109.11€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 897 | +0.193 | -109.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 897 | +0.193 | -109.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 897 | +0.193 | -109.11€ | 2 | 4 |
| ✅ GBM_LATE_15M | 42516 | +0.095 | +22280.96€ | 0 | 19 |
| ✅ GBM_LATE_15M#15min | 42516 | +0.095 | +22280.96€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 7082 | +0.217 | +5854.84€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 7082 | +0.217 | +5854.84€ | 0 | 23 |
| ✅ GBM_LATE_15M#BTC | 6370 | +0.180 | +4886.07€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 6370 | +0.180 | +4886.07€ | 0 | 24 |
| ✅ GBM_LATE_15M#DOGE | 7599 | +0.206 | +5932.52€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 7599 | +0.206 | +5932.52€ | 0 | 20 |
| ✅ GBM_LATE_15M#ETH | 5936 | +0.042 | +1677.54€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 5936 | +0.042 | +1677.54€ | 1 | 19 |
| ✅ GBM_LATE_15M#SOL | 5987 | -0.032 | +1258.84€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 5987 | -0.032 | +1258.84€ | 4 | 13 |
| ✅ GBM_LATE_15M#XRP | 9542 | -0.030 | +2671.15€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 9542 | -0.030 | +2671.15€ | 4 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 45737 | +0.085 | +24884.66€ | 0 | 18 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 45737 | +0.085 | +24884.66€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 8840 | +0.003 | +4447.75€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 8840 | +0.003 | +4447.75€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 9681 | +0.009 | +2287.41€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 9681 | +0.009 | +2287.41€ | 0 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 6340 | +0.279 | +6825.09€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 6340 | +0.279 | +6825.09€ | 0 | 22 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 8246 | +0.014 | +2050.37€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 8246 | +0.014 | +2050.37€ | 1 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 7291 | +0.039 | +3001.60€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 7291 | +0.039 | +3001.60€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 5339 | +0.303 | +6272.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 5339 | +0.303 | +6272.44€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 33726 | +0.180 | +27366.63€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 33726 | +0.180 | +27366.63€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 5112 | +0.231 | +4568.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 5112 | +0.231 | +4568.77€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 5313 | +0.149 | +3934.53€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 5313 | +0.149 | +3934.53€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 5402 | +0.224 | +4663.10€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 5402 | +0.224 | +4663.10€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 5720 | +0.139 | +4365.07€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 5720 | +0.139 | +4365.07€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 6340 | +0.124 | +4727.82€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 6340 | +0.124 | +4727.82€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 5839 | +0.225 | +5107.34€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 5839 | +0.225 | +5107.34€ | 0 | 24 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 9144 | +0.134 | +4486.92€ | 0 | 18 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 9144 | +0.134 | +4486.92€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 405 | +0.154 | +252.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 405 | +0.154 | +252.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 2706 | +0.145 | +1554.92€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 2706 | +0.145 | +1554.92€ | 0 | 22 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 449 | +0.150 | +227.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 449 | +0.150 | +227.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 2698 | +0.139 | +1291.25€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 2698 | +0.139 | +1291.25€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 2260 | +0.108 | +876.31€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 2260 | +0.108 | +876.31€ | 0 | 16 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 626 | +0.134 | +283.67€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 626 | +0.134 | +283.67€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO | 42689 | +0.185 | +34219.82€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#15min | 42689 | +0.185 | +34219.82€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 6759 | +0.242 | +6325.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 6759 | +0.242 | +6325.72€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 6646 | +0.147 | +4554.53€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 6646 | +0.147 | +4554.53€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 7218 | +0.234 | +6465.23€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 7218 | +0.234 | +6465.23€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 7047 | +0.139 | +5045.43€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 7047 | +0.139 | +5045.43€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 7563 | +0.121 | +5228.84€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 7563 | +0.121 | +5228.84€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 7456 | +0.230 | +6600.09€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 7456 | +0.230 | +6600.09€ | 0 | 19 |
| ✅ GBM_LATE_5M | 11713 | +0.202 | +9107.65€ | 1 | 29 |
| ✅ GBM_LATE_5M#5min | 11713 | +0.202 | +9107.65€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 984 | +0.242 | +916.10€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 984 | +0.242 | +916.10€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 2778 | +0.208 | +2391.40€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 2778 | +0.208 | +2391.40€ | 0 | 25 |
| ✅ GBM_LATE_5M#DOGE | 1110 | +0.193 | +808.37€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1110 | +0.193 | +808.37€ | 0 | 19 |
| ✅ GBM_LATE_5M#ETH | 3338 | +0.193 | +2345.42€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 3338 | +0.193 | +2345.42€ | 0 | 28 |
| ✅ GBM_LATE_5M#SOL | 1710 | +0.192 | +1299.28€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 1710 | +0.192 | +1299.28€ | 0 | 27 |
| ✅ GBM_LATE_5M#XRP | 1793 | +0.201 | +1347.07€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1793 | +0.201 | +1347.07€ | 0 | 0 |
| ✅ GBM_LATE_60M | 3496 | +0.065 | +1142.74€ | 0 | 8 |
| ✅ GBM_LATE_60M#60min | 3496 | +0.065 | +1142.74€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 1283 | +0.081 | +474.18€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 1283 | +0.081 | +474.18€ | 0 | 6 |
| ✅ GBM_LATE_60M#ETH | 1128 | +0.066 | +386.98€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 1128 | +0.066 | +386.98€ | 1 | 9 |
| ✅ GBM_LATE_60M#SOL | 1085 | +0.045 | +281.58€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 1085 | +0.045 | +281.58€ | 1 | 13 |
| 🚫 GBM_LATE_60M_FADE | 573 | -0.244 | -22.02€ | 8 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 573 | -0.244 | -22.02€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 213 | -0.249 | -15.57€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 213 | -0.249 | -15.57€ | 5 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 205 | -0.225 | +0.05€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 205 | -0.225 | +0.05€ | 7 | 1 |
| 🚫 GBM_LATE_60M_FADE#SOL | 155 | -0.258 | -6.50€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 155 | -0.258 | -6.50€ | 5 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 1519 | +0.082 | +379.15€ | 1 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 1519 | +0.082 | +379.15€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 596 | +0.079 | +139.92€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 596 | +0.079 | +139.92€ | 1 | 12 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 544 | +0.055 | +78.03€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 544 | +0.055 | +78.03€ | 2 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 379 | +0.125 | +161.20€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 379 | +0.125 | +161.20€ | 3 | 10 |
| ✅ LATE_WINDOW_5MIN | 166 | +0.280 | +164.71€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 166 | +0.280 | +164.71€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 166 | +0.280 | +164.71€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 166 | +0.280 | +164.71€ | 1 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 3407 | +0.101 | +840.13€ | 0 | 1 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 3407 | +0.101 | +840.13€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 3407 | +0.101 | +840.13€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 3407 | +0.101 | +840.13€ | 0 | 1 |
| ✅ LIQUIDACIONES_15M | 534 | -0.043 | -19.18€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 534 | -0.043 | -19.18€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 149 | -0.017 | +1.90€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 149 | -0.017 | +1.90€ | 2 | 1 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 103 | -0.033 | -3.27€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 103 | -0.033 | -3.27€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 201 | -0.007 | -0.95€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 201 | -0.007 | -0.95€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M | 3735 | +0.015 | +79.70€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 3735 | +0.015 | +79.70€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 181 | +0.019 | -2.82€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 181 | +0.019 | -2.82€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 794 | +0.007 | +29.41€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 794 | +0.007 | +29.41€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE | 207 | -0.012 | -4.18€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 207 | -0.012 | -4.18€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 1348 | +0.024 | +29.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1348 | +0.024 | +29.92€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 756 | +0.012 | +1.99€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 756 | +0.012 | +1.99€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 449 | +0.014 | +25.38€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 449 | +0.014 | +25.38€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 1761 | -0.039 | -27.29€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1761 | -0.039 | -27.29€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 507 | -0.030 | -11.61€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 507 | -0.030 | -11.61€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 601 | -0.014 | +6.50€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 601 | -0.014 | +6.50€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 653 | -0.070 | -22.18€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 653 | -0.070 | -22.18€ | 6 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 8752 | -0.028 | -20.53€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 4144 | -0.037 | -89.31€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 4608 | -0.020 | +68.78€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 266 | -0.041 | -11.42€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 135 | -0.025 | -1.89€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 131 | -0.056 | -9.54€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 2182 | -0.021 | +9.54€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 1038 | -0.024 | -2.66€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 1144 | -0.018 | +12.21€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 960 | -0.026 | +8.79€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 478 | -0.044 | -14.59€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 482 | -0.008 | +23.38€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 1907 | -0.042 | -65.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 884 | -0.053 | -55.88€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 1023 | -0.033 | -9.57€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 1714 | -0.022 | +21.71€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 816 | -0.034 | -10.73€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 898 | -0.010 | +32.44€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 1723 | -0.029 | +16.30€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 793 | -0.037 | -3.56€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 930 | -0.021 | +19.86€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 49924 | -0.000 | +2472.46€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 49924 | -0.000 | +2472.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 8995 | +0.026 | +1143.16€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 8995 | +0.026 | +1143.16€ | 2 | 5 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 7186 | -0.033 | -98.16€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 7186 | -0.033 | -98.16€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 9108 | +0.025 | +943.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 9108 | +0.025 | +943.30€ | 2 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 7034 | -0.048 | -153.74€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 7034 | -0.048 | -153.74€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 8443 | -0.004 | +232.14€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 8443 | -0.004 | +232.14€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 9158 | +0.015 | +405.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 9158 | +0.015 | +405.75€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 6639 | -0.059 | -162.16€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 6639 | -0.059 | -162.16€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1225 | -0.000 | -15.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1225 | -0.000 | -15.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1733 | -0.079 | -45.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1733 | -0.079 | -45.75€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 55 | -0.061 | -2.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 55 | -0.061 | -2.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 774 | -0.120 | -33.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 774 | -0.120 | -33.46€ | 6 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1995 | -0.074 | -39.25€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1995 | -0.074 | -39.25€ | 3 | 0 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 123798 | -0.076 | +1610.51€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 123798 | -0.076 | +1610.51€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 21524 | -0.077 | +1075.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 21524 | -0.077 | +1075.54€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 18649 | -0.101 | -1024.35€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 18649 | -0.101 | -1024.35€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 21830 | -0.068 | +1180.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 21830 | -0.068 | +1180.36€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 18192 | -0.097 | -622.63€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 18192 | -0.097 | -622.63€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 22167 | -0.057 | +310.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 22167 | -0.057 | +310.19€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 21436 | -0.067 | +691.39€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 21436 | -0.067 | +691.39€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 8762 | -0.034 | -182.47€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 8762 | -0.034 | -182.47€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 1001 | -0.017 | -18.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 1001 | -0.017 | -18.91€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1987 | -0.046 | -24.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1987 | -0.046 | -24.71€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1008 | -0.022 | -32.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1008 | -0.022 | -32.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2600 | -0.026 | -42.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2600 | -0.026 | -42.34€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1195 | -0.055 | -27.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1195 | -0.055 | -27.77€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 971 | -0.031 | -35.95€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 971 | -0.031 | -35.95€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1682 | +0.123 | +686.82€ | 0 | 6 |
| ✅ ORDER_FLOW_5M#5min | 1546 | +0.129 | +674.23€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 359 | +0.137 | +179.85€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 359 | +0.137 | +179.85€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#DOGE | 318 | +0.116 | +107.54€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 318 | +0.116 | +107.54€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#ETH | 309 | +0.137 | +150.62€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 309 | +0.137 | +150.62€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#SOL | 274 | +0.152 | +151.77€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 274 | +0.152 | +151.77€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#XRP | 286 | +0.101 | +84.44€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 286 | +0.101 | +84.44€ | 0 | 3 |
| ✅ ORDER_FLOW_5M_REACTIVO | 1459 | -0.015 | -20.55€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 1459 | -0.015 | -20.55€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 283 | -0.002 | +8.79€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 283 | -0.002 | +8.79€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 250 | -0.016 | -0.49€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 250 | -0.016 | -0.49€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 380 | -0.047 | -32.61€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 380 | -0.047 | -32.61€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 311 | +0.008 | +3.23€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 311 | +0.008 | +3.23€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 235 | -0.011 | +0.52€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 235 | -0.011 | +0.52€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 900 | -0.069 | -41.12€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 420 | -0.109 | -76.71€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 324 | -0.138 | -64.11€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 96 | -0.010 | -12.59€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 318 | -0.028 | +26.47€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 227 | -0.015 | +28.93€ | 1 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 91 | -0.059 | -2.46€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 162 | -0.043 | +9.12€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 131 | -0.049 | +4.73€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 31 | -0.015 | +4.39€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 682 | -0.080 | -30.45€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 218 | -0.032 | -10.67€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 1125 | -0.207 | -69.66€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC | 438 | -0.209 | -41.88€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#atexpiry | 381 | -0.213 | -41.65€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 57 | -0.178 | -0.23€ | 2 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 385 | -0.211 | -33.99€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 337 | -0.223 | -41.00€ | 3 | 0 |
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
| ✅ STREAK_FADE_15M | 725 | +0.030 | +37.59€ | 2 | 2 |
| ✅ STREAK_FADE_15M#15min | 725 | +0.030 | +37.59€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 302 | +0.023 | +3.35€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 302 | +0.023 | +3.35€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 60 | -0.016 | -2.15€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 60 | -0.016 | -2.15€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 73 | -0.007 | +0.78€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 73 | -0.007 | +0.78€ | 3 | 1 |
| ✅ STREAK_FADE_15M#XRP | 290 | +0.055 | +35.62€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 290 | +0.055 | +35.62€ | 0 | 5 |
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
| ✅ STREAK_FADE_60M | 102 | -0.058 | -9.71€ | 5 | 0 |
| ✅ STREAK_FADE_60M#60min | 102 | -0.058 | -9.71€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 43 | -0.100 | -5.07€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 43 | -0.100 | -5.07€ | 4 | 0 |
| ✅ STREAK_FADE_60M#SOL | 59 | -0.025 | -4.64€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 59 | -0.025 | -4.64€ | 0 | 1 |
| ✅ STREAK_MOM_5M | 10879 | +0.016 | +86.68€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 10879 | +0.016 | +86.68€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2780 | +0.021 | +28.77€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2780 | +0.021 | +28.77€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2836 | +0.019 | +36.58€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2836 | +0.019 | +36.58€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2888 | +0.009 | -0.95€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2888 | +0.009 | -0.95€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2375 | +0.016 | +22.29€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2375 | +0.016 | +22.29€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 9882 | +0.013 | -48.01€ | 2 | 0 |
| ✅ STRUCT_NO_15M#15min | 9882 | +0.013 | -48.01€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 4021 | +0.018 | -8.19€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 4021 | +0.018 | -8.19€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3616 | +0.011 | -27.14€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3616 | +0.011 | -27.14€ | 2 | 0 |
| ✅ STRUCT_NO_15M#SOL | 2245 | +0.010 | -12.69€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 2245 | +0.010 | -12.69€ | 1 | 0 |
| ✅ UPDOWN_GBM | 76840 | +0.054 | +6811.11€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 19107 | +0.083 | +4207.61€ | 0 | 11 |
| ✅ UPDOWN_GBM#240min | 2463 | +0.003 | +22.33€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 50473 | +0.050 | +2496.96€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 4531 | +0.006 | +84.95€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 6851 | +0.089 | +1075.72€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1576 | +0.156 | +698.08€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 77 | -0.006 | -0.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 5198 | +0.070 | +378.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 16544 | +0.056 | +1424.14€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 2472 | +0.090 | +606.57€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 662 | +0.009 | +10.16€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 11296 | +0.061 | +745.04€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 2018 | +0.003 | +59.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 96 | -0.071 | +2.97€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 8455 | +0.069 | +897.14€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1555 | +0.147 | +610.96€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 78 | +0.013 | -1.79€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 6822 | +0.052 | +287.97€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 17641 | +0.045 | +1153.69€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 4525 | +0.066 | +670.29€ | 0 | 10 |
| ✅ UPDOWN_GBM#ETH#240min | 645 | +0.005 | +15.29€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 10795 | +0.044 | +447.73€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 1587 | +0.011 | +17.61€ | 1 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 89 | -0.104 | +2.77€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 16863 | +0.033 | +836.55€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 4783 | +0.035 | +403.55€ | 0 | 4 |
| ✅ UPDOWN_GBM#SOL#240min | 613 | -0.009 | -0.43€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 10462 | +0.037 | +430.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 926 | +0.005 | +7.95€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 79 | -0.130 | -4.65€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 10484 | +0.064 | +1425.69€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 4196 | +0.102 | +1218.16€ | 0 | 11 |
| ✅ UPDOWN_GBM#XRP#240min | 388 | +0.010 | -0.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 5900 | +0.041 | +207.60€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 264 | -0.102 | +1.10€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 842 | +0.366 | +313.21€ | 0 | 9 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 842 | +0.366 | +313.21€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 437 | +0.366 | +154.77€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 437 | +0.366 | +154.77€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 405 | +0.365 | +158.44€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 405 | +0.365 | +158.44€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO | 19887 | -0.025 | +4650.09€ | 2 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 19887 | -0.025 | +4650.09€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1718 | -0.056 | +502.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1718 | -0.056 | +502.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 3535 | -0.112 | +132.79€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 3535 | -0.112 | +132.79€ | 5 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 948 | +0.216 | +770.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 948 | +0.216 | +770.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 2422 | +0.219 | +1593.65€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 2422 | +0.219 | +1593.65€ | 1 | 20 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 5685 | -0.067 | +663.06€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 5685 | -0.067 | +663.06€ | 4 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 5579 | -0.065 | +987.32€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 5579 | -0.065 | +987.32€ | 3 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 232 | +0.047 | +11.12€ | 0 | 2 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 232 | +0.047 | +11.12€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 232 | +0.047 | +11.12€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 232 | +0.047 | +11.12€ | 0 | 2 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1430 | +0.294 | +1237.42€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1430 | +0.294 | +1237.42€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 767 | +0.291 | +625.58€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 767 | +0.291 | +625.58€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 663 | +0.297 | +611.84€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 663 | +0.297 | +611.84€ | 0 | 9 |
| ✅ UPDOWN_OU_5M | 815 | -0.112 | -83.16€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#5min | 815 | -0.112 | -83.16€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 248 | -0.080 | -18.10€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 248 | -0.080 | -18.10€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 87 | -0.163 | -9.15€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 87 | -0.163 | -9.15€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 97 | -0.187 | -6.55€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 97 | -0.187 | -6.55€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 38 | -0.175 | -6.61€ | 2 | 0 |
| ✅ WEEKLY_PRICE | 3610 | +0.303 | +1706.47€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 1328 | +0.255 | +162.57€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 1388 | +0.298 | +621.15€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 894 | +0.380 | +922.75€ | 0 | 1 |