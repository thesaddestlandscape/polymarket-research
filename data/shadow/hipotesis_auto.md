# Hipótesis automáticas — 2026-10-20 13:17 UTC
_Generado por shadow_postmortem.py sobre 979885 resoluciones (PNL=+127616.06€)_

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
- **FILTRO** `restante_s_al_confirmar` < `142.32` → IC=-0.204 (n=10029)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 142.32
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=30094)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `128.85` → IC=-0.263 (n=1122)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 128.85
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=3366)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `121.5` → IC=-0.287 (n=1079)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 121.5
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=3238)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `167.16` → IC=-0.206 (n=2644)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 167.16
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=7935)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `133.16` → IC=-0.277 (n=1958)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 133.16
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=5877)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.213 (n=21652)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.108)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.135 (n=4314)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.108)

- **PATRÓN** `libro_liquidez` > `9145.1421` → IC=+0.176 (n=1950)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 9145.1421 (IC base=+0.108)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.130 (n=18296)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 17.0 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.129 (n=33130)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 11.0 (IC base=+0.126)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.227 (n=17174)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.150 (n=7187)

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

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.140 (n=1118)

  - _Acción_: Kelly boost +0.70€ cuando `py_entrada` < 0.44 (IC base=+0.086)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.168 (n=4190)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.161)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.162 (n=2871)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 12.0 (IC base=+0.161)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.371 (n=1374)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.161)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.229 (n=773)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.211)

- **PATRÓN** `py_entrada` < `0.26` → IC=+0.360 (n=671)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.26 (IC base=+0.211)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.215 (n=2180)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.211)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.145 (n=1058)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.143)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.149 (n=687)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 11.0 (IC base=+0.143)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.263 (n=340)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.143)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=827)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `1882.3359` → IC=+0.154 (n=674)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 1882.3359 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.162 (n=152)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.069)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.246 (n=976)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.222)

- **PATRÓN** `py_entrada` > `0.83` → IC=+0.419 (n=1142)

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
- **PATRÓN** `hora_utc` > `9.0` → IC=+0.170 (n=313)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 9.0 (IC base=+0.153)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.347 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.153)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.143 (n=197)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.02 (IC base=+0.153)

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

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.206 (n=18245)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.201)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.202 (n=15504)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.201)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.234 (n=7533)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.201)

- **PATRÓN** `libro_liquidez` > `4837.3339` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4837.3339 (IC base=+0.201)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.180 (n=4210)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 5.0 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.181 (n=4196)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 18.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.183 (n=4111)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` < 0.73 (IC base=+0.180)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.181 (n=3442)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` > 0.71 (IC base=+0.180)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.380 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.247 (n=89)

- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=90)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.224 (n=2145)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.231 (n=1437)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.222)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.304 (n=755)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.222)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.188 (n=4138)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.181)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.183 (n=3525)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 15.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.187 (n=3250)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` > 0.71 (IC base=+0.181)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.258 (n=3589)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.248)

- **PATRÓN** `py_entrada` > `0.79` → IC=+0.361 (n=1157)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.194 (n=4056)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 5.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.193 (n=2602)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 11.0 (IC base=+0.189)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.193 (n=2998)

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

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.247 (n=23932)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.202)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.187 (n=11095)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.185)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.188 (n=7588)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 12.0 (IC base=+0.185)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.200 (n=10614)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.71 (IC base=+0.185)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.228 (n=4924)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.227 (n=4872)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.225)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.286 (n=3471)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.225)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.191 (n=4043)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 17.0 (IC base=+0.182)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.211 (n=5419)

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

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.278 (n=3378)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.222)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.204 (n=9628)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.260 (n=3520)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.208 (n=3924)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.199 (n=3976)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 6.0 (IC base=+0.197)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.243 (n=4947)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.197)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.192 (n=8620)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.140 (n=8440)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `3.77` → IC=+0.137 (n=10331)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 3.77 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.195 (n=4264)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.119)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.143 (n=4308)

  - _Acción_: Kelly boost +0.72€ cuando `restante_min` > 4.95 (IC base=+0.119)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.129 (n=5180)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.119)

- **PATRÓN** `lag_apertura_s` < `2.77` → IC=+0.147 (n=3897)

  - _Acción_: Kelly boost +0.74€ cuando `lag_apertura_s` < 2.77 (IC base=+0.119)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.189 (n=4356)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.38 (IC base=+0.114)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.136 (n=4599)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.96 (IC base=+0.114)

- **PATRÓN** `lag_apertura_s` < `3.33` → IC=+0.134 (n=5199)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.445 (n=764)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.442)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.442 (n=754)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.442)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.445 (n=527)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.442)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.443 (n=867)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.442)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.437 (n=363)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.435)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.440 (n=247)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.435)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.436 (n=373)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.435)

- **PATRÓN** `py_entrada` > `0.935` → IC=+0.442 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.935 (IC base=+0.435)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.453 (n=361)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.449)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.452 (n=349)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.449)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.451 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.449)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4759` → IC=+0.138 (n=13282)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.4759 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.124 (n=13427)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 6.0 (IC base=+0.121)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.124 (n=9312)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 12.0 (IC base=+0.121)

- **PATRÓN** `ibs_20min` > `0.9804` → IC=+0.248 (n=4429)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9804 (IC base=+0.121)

- **PATRÓN** `dist_vwap_pct` > `0.7754` → IC=+0.267 (n=735)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7754 (IC base=+0.121)

- **PATRÓN** `dist_vwap_pct` < `0.212` → IC=+0.258 (n=3257)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.212 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.909` → IC=+0.191 (n=5030)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 5.909 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` < `1.1997` → IC=+0.258 (n=3857)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1997 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` > `0.6202` → IC=+0.264 (n=3857)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6202 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` > `0.3023` → IC=+0.241 (n=1346)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3023 (IC base=+0.121)

- **PATRÓN** `volumen_spike_ratio` > `2.3444` → IC=+0.229 (n=4282)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3444 (IC base=+0.121)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.124 (n=11172)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.02 (IC base=+0.121)

- **PATRÓN** `ibs_20min` < `0.6849` → IC=+0.130 (n=18580)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` < 0.6849 (IC base=+0.075)

- **PATRÓN** `dist_vwap_pct` < `0.1538` → IC=+0.188 (n=6040)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` < 0.1538 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` < `0.6964` → IC=+0.185 (n=2801)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 0.6964 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` > `1.0501` → IC=+0.181 (n=2886)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 1.0501 (IC base=+0.075)

- **PATRÓN** `volumen_pendiente_norm` > `0.2954` → IC=+0.235 (n=1592)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2954 (IC base=+0.075)

- **PATRÓN** `volumen_spike_ratio` > `2.6765` → IC=+0.207 (n=3608)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6765 (IC base=+0.075)

- **PATRÓN** `ballena_activa_n` < `106.0` → IC=+0.221 (n=10676)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 106.0 (IC base=+0.075)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.212 (n=965)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.200)

- **PATRÓN** `drift_60min` |x|≤ `0.347` → IC=+0.203 (n=2890)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.347 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.210 (n=1399)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.200)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.205 (n=1939)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.200)

- **PATRÓN** `ibs_20min` > `0.9794` → IC=+0.281 (n=1310)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9794 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.9` → IC=+0.282 (n=1267)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.9 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` > `0.2333` → IC=+0.249 (n=509)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2333 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` > `1.44` → IC=+0.202 (n=2753)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.44 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.214 (n=3093)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.200)

- **PATRÓN** `libro_liquidez` > `2078.6972` → IC=+0.205 (n=963)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2078.6972 (IC base=+0.200)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.217 (n=1729)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 14.0 (IC base=+0.200)

- **PATRÓN** `sigma_h` < `0.0085` → IC=+0.240 (n=2419)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0085 (IC base=+0.237)

- **PATRÓN** `sigma_h` > `0.0077` → IC=+0.238 (n=1097)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0077 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.0873` → IC=+0.272 (n=810)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0873 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.254 (n=880)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` < `0.5294` → IC=+0.259 (n=2420)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5294 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` < `0.0941` → IC=+0.239 (n=2168)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0941 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.287` → IC=+0.261 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.287 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` < `1.4408` → IC=+0.243 (n=760)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4408 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `2.6588` → IC=+0.244 (n=760)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6588 (IC base=+0.237)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.240 (n=2718)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.237)

- **PATRÓN** `libro_liquidez` > `1636.9428` → IC=+0.245 (n=2161)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1636.9428 (IC base=+0.237)

- **PATRÓN** `ballena_activa_n` < `7.0` → IC=+0.241 (n=801)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 7.0 (IC base=+0.237)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.238 (n=1043)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.228)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.230 (n=1076)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.228)

- **PATRÓN** `drift_60min` |x|≤ `0.106` → IC=+0.262 (n=1042)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.106 (IC base=+0.228)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.239 (n=2479)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.228)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.228 (n=1686)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.228)

- **PATRÓN** `ibs_20min` > `0.9495` → IC=+0.276 (n=789)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9495 (IC base=+0.228)

- **PATRÓN** `dist_vwap_pct` > `0.1291` → IC=+0.233 (n=1263)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1291 (IC base=+0.228)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.329` → IC=+0.263 (n=357)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.329 (IC base=+0.228)

- **PATRÓN** `volumen_regimen` < `1.2292` → IC=+0.231 (n=2365)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2292 (IC base=+0.228)

- **PATRÓN** `volumen_regimen` > `0.6226` → IC=+0.232 (n=2366)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6226 (IC base=+0.228)

- **PATRÓN** `volumen_pendiente_norm` > `0.276` → IC=+0.263 (n=335)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.276 (IC base=+0.228)

- **PATRÓN** `volumen_spike_ratio` < `1.5102` → IC=+0.228 (n=1025)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5102 (IC base=+0.228)

- **PATRÓN** `volumen_spike_ratio` > `2.4423` → IC=+0.255 (n=777)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4423 (IC base=+0.228)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.151 (n=2414)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0058 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.0749` → IC=+0.168 (n=803)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.0749 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.153 (n=908)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 17.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` < `0.7276` → IC=+0.176 (n=2409)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.7276 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.006` → IC=+0.150 (n=390)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 11.006 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.188` → IC=+0.140 (n=2201)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` < 4.188 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `1.204` → IC=+0.140 (n=2409)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 1.204 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` > `0.0963` → IC=+0.160 (n=879)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.0963 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` < `2.4535` → IC=+0.143 (n=2288)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.4535 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` > `1.4135` → IC=+0.135 (n=2288)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 1.4135 (IC base=+0.133)

- **PATRÓN** `ballena_activa_n` < `218.0` → IC=+0.174 (n=979)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 218.0 (IC base=+0.133)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0121` → IC=+0.219 (n=1003)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0121 (IC base=+0.195)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.200 (n=3152)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.195)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.272 (n=1145)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.195)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.268` → IC=+0.275 (n=633)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.268 (IC base=+0.195)

- **PATRÓN** `volumen_pendiente_norm` < `0.0975` → IC=+0.200 (n=2667)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0975 (IC base=+0.195)

- **PATRÓN** `volumen_pendiente_norm` > `0.3522` → IC=+0.211 (n=385)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3522 (IC base=+0.195)

- **PATRÓN** `volumen_spike_ratio` > `2.6919` → IC=+0.210 (n=1321)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6919 (IC base=+0.195)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.202 (n=3590)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.195)

- **PATRÓN** `libro_liquidez` > `1975.9` → IC=+0.202 (n=1362)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1975.9 (IC base=+0.195)

- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.224 (n=2372)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0106 (IC base=+0.218)

- **PATRÓN** `drift_60min` |x|≤ `0.461` → IC=+0.225 (n=2369)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.461 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.242 (n=1004)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.218 (n=1243)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.218)

- **PATRÓN** `ibs_20min` < `0.0173` → IC=+0.276 (n=898)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0173 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.402` → IC=+0.246 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.402 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` > `0.3477` → IC=+0.260 (n=386)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3477 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` > `2.726` → IC=+0.230 (n=1159)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.726 (IC base=+0.218)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.220 (n=1417)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.218)

- **PATRÓN** `libro_liquidez` > `2052.1448` → IC=+0.222 (n=897)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2052.1448 (IC base=+0.218)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.222 (n=2213)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 24.0 (IC base=+0.218)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.140 (n=148)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=3644)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.164 (n=536)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0037 (IC base=+0.053)

- **PATRÓN** `ibs_20min` > `0.9536` → IC=+0.228 (n=535)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9536 (IC base=+0.053)

- **PATRÓN** `dist_vwap_pct` > `0.1401` → IC=+0.330 (n=357)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1401 (IC base=+0.053)

- **PATRÓN** `dist_vwap_pct` < `0.19` → IC=+0.329 (n=482)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.19 (IC base=+0.053)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.1` → IC=+0.187 (n=1156)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 5.1 (IC base=+0.053)

- **PATRÓN** `volumen_regimen` < `0.8553` → IC=+0.334 (n=402)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8553 (IC base=+0.053)

- **PATRÓN** `volumen_regimen` > `1.2207` → IC=+0.347 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2207 (IC base=+0.053)

- **PATRÓN** `volumen_pendiente_norm` > `0.2965` → IC=+0.350 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2965 (IC base=+0.053)

- **PATRÓN** `volumen_spike_ratio` < `1.4107` → IC=+0.348 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4107 (IC base=+0.053)

- **PATRÓN** `volumen_spike_ratio` > `2.21` → IC=+0.328 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.21 (IC base=+0.053)

- **PATRÓN** `ballena_activa_n` < `132.0` → IC=+0.338 (n=523)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 132.0 (IC base=+0.053)

- **PATRÓN** `ibs_20min` < `0.093` → IC=+0.174 (n=949)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.093 (IC base=+0.036)

- **PATRÓN** `dist_vwap_pct` > `0.3255` → IC=+0.142 (n=450)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.3255 (IC base=+0.036)

- **PATRÓN** `dist_vwap_pct` < `0.1302` → IC=+0.138 (n=1555)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.1302 (IC base=+0.036)

- **PATRÓN** `volumen_regimen` < `0.8417` → IC=+0.149 (n=1125)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.8417 (IC base=+0.036)

- **PATRÓN** `volumen_regimen` > `1.1669` → IC=+0.139 (n=563)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` > 1.1669 (IC base=+0.036)

- **PATRÓN** `volumen_pendiente_norm` > `0.2851` → IC=+0.202 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2851 (IC base=+0.036)

- **PATRÓN** `volumen_spike_ratio` < `1.7767` → IC=+0.140 (n=1078)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.7767 (IC base=+0.036)

- **PATRÓN** `volumen_spike_ratio` > `2.1545` → IC=+0.152 (n=733)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 2.1545 (IC base=+0.036)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.167 (n=103)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=552)

- **FILTRO** `ibs_20min` < `0.2727` → IC=-0.191 (n=163)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2727
  - _Potencial_: sin este filtro IC_bueno=+0.105 (n=492)

- **FILTRO** `ibs_20min` > `0.2169` → IC=-0.132 (n=3570)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2169
  - _Potencial_: sin este filtro IC_bueno=+0.148 (n=1759)

- **FILTRO** `sigma_ewma_delta_pct` > `8.662` → IC=-0.238 (n=559)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.662
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=4770)

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

- **PATRÓN** `ibs_20min` < `0.2169` → IC=+0.148 (n=1759)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` < 0.2169 (IC base=-0.039)

- **PATRÓN** `dist_vwap_pct` > `0.2659` → IC=+0.276 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2659 (IC base=-0.039)

- **PATRÓN** `volumen_regimen` < `0.704` → IC=+0.302 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.704 (IC base=-0.039)

- **PATRÓN** `volumen_pendiente_norm` > `0.0812` → IC=+0.304 (n=314)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0812 (IC base=-0.039)

- **PATRÓN** `volumen_spike_ratio` < `2.43` → IC=+0.300 (n=667)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.43 (IC base=-0.039)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6094` → IC=-0.178 (n=976)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6094
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=2929)

- **FILTRO** `ibs_20min` < `0.75` → IC=-0.151 (n=2563)

  - _Acción_: SKIP cuando `ibs_20min` < 0.75
  - _Potencial_: sin este filtro IC_bueno=+0.096 (n=1342)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.162 (n=958)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=2947)

- **FILTRO** `ibs_20min` > `0.75` → IC=-0.203 (n=1404)

  - _Acción_: SKIP cuando `ibs_20min` > 0.75
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=4225)

- **PATRÓN** `dist_vwap_pct` > `1.0122` → IC=+0.332 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0122 (IC base=-0.066)

- **PATRÓN** `dist_vwap_pct` < `0.2479` → IC=+0.304 (n=596)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2479 (IC base=-0.066)

- **PATRÓN** `volumen_regimen` > `0.704` → IC=+0.315 (n=610)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.704 (IC base=-0.066)

- **PATRÓN** `volumen_pendiente_norm` < `0.0985` → IC=+0.302 (n=643)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0985 (IC base=-0.066)

- **PATRÓN** `volumen_pendiente_norm` > `0.0704` → IC=+0.305 (n=270)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0704 (IC base=-0.066)

- **PATRÓN** `volumen_spike_ratio` < `1.4142` → IC=+0.316 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4142 (IC base=-0.066)

- **PATRÓN** `volumen_spike_ratio` > `1.8324` → IC=+0.308 (n=440)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8324 (IC base=-0.066)

- **PATRÓN** `dist_vwap_pct` > `0.7982` → IC=+0.270 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7982 (IC base=-0.005)

- **PATRÓN** `volumen_regimen` > `1.0687` → IC=+0.283 (n=698)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0687 (IC base=-0.005)

- **PATRÓN** `volumen_pendiente_norm` > `0.1042` → IC=+0.284 (n=535)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1042 (IC base=-0.005)

- **PATRÓN** `volumen_spike_ratio` < `2.1788` → IC=+0.263 (n=1248)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1788 (IC base=-0.005)

- **PATRÓN** `volumen_spike_ratio` > `1.4309` → IC=+0.263 (n=1418)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4309 (IC base=-0.005)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.209 (n=5829)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0098 (IC base=+0.096)

- **PATRÓN** `ibs_20min` > `0.3206` → IC=+0.168 (n=17466)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` > 0.3206 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` > `0.9483` → IC=+0.298 (n=1273)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9483 (IC base=+0.096)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.592` → IC=+0.161 (n=7832)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 3.592 (IC base=+0.096)

- **PATRÓN** `volumen_regimen` < `1.1691` → IC=+0.264 (n=6429)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1691 (IC base=+0.096)

- **PATRÓN** `volumen_regimen` > `0.6886` → IC=+0.269 (n=5744)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6886 (IC base=+0.096)

- **PATRÓN** `volumen_pendiente_norm` > `0.2396` → IC=+0.277 (n=1907)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2396 (IC base=+0.096)

- **PATRÓN** `volumen_spike_ratio` < `1.4592` → IC=+0.262 (n=3421)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4592 (IC base=+0.096)

- **PATRÓN** `volumen_spike_ratio` > `2.6405` → IC=+0.272 (n=3421)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6405 (IC base=+0.096)

- **PATRÓN** `ballena_activa_n` < `92.0` → IC=+0.295 (n=9853)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 92.0 (IC base=+0.096)

- **PATRÓN** `sigma_h` > `0.0093` → IC=+0.159 (n=5602)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0093 (IC base=+0.075)

- **PATRÓN** `ibs_20min` < `0.6577` → IC=+0.144 (n=16808)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.6577 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` < `0.7056` → IC=+0.261 (n=2338)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7056 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` > `1.1961` → IC=+0.266 (n=1770)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1961 (IC base=+0.075)

- **PATRÓN** `volumen_pendiente_norm` > `0.2944` → IC=+0.318 (n=1143)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2944 (IC base=+0.075)

- **PATRÓN** `volumen_spike_ratio` < `1.5792` → IC=+0.290 (n=3351)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5792 (IC base=+0.075)

- **PATRÓN** `volumen_spike_ratio` > `2.2644` → IC=+0.283 (n=3452)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2644 (IC base=+0.075)

- **PATRÓN** `ballena_activa_n` < `77.0` → IC=+0.295 (n=7552)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 77.0 (IC base=+0.075)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.5801` → IC=-0.128 (n=2399)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5801
  - _Potencial_: sin este filtro IC_bueno=+0.189 (n=2399)

- **FILTRO** `ibs_20min` > `0.7414` → IC=-0.212 (n=1008)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7414
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=3025)

- **FILTRO** `sigma_ewma_delta_pct` > `4.394` → IC=-0.206 (n=884)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.394
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=3149)

- **PATRÓN** `ibs_20min` > `0.9178` → IC=+0.312 (n=1200)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9178 (IC base=+0.030)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.017` → IC=+0.215 (n=850)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.017 (IC base=+0.030)

- **PATRÓN** `volumen_pendiente_norm` > `0.2294` → IC=+0.301 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2294 (IC base=+0.030)

- **PATRÓN** `volumen_spike_ratio` < `1.4427` → IC=+0.252 (n=522)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4427 (IC base=+0.030)

- **PATRÓN** `volumen_spike_ratio` > `2.2427` → IC=+0.274 (n=710)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2427 (IC base=+0.030)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.280 (n=1060)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.030)

- **PATRÓN** `ibs_20min` < `0.1633` → IC=+0.161 (n=1009)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.1633 (IC base=-0.029)

- **PATRÓN** `volumen_pendiente_norm` < `0.0715` → IC=+0.414 (n=465)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0715 (IC base=-0.029)

- **PATRÓN** `volumen_spike_ratio` < `2.5496` → IC=+0.409 (n=525)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5496 (IC base=-0.029)

- **PATRÓN** `ballena_activa_n` < `10.0` → IC=+0.414 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 10.0 (IC base=-0.029)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.1138` → IC=+0.212 (n=866)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1138 (IC base=+0.022)

- **PATRÓN** `volumen_regimen` < `1.1937` → IC=+0.193 (n=1703)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` < 1.1937 (IC base=+0.022)

- **PATRÓN** `volumen_regimen` > `0.6831` → IC=+0.200 (n=1520)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6831 (IC base=+0.022)

- **PATRÓN** `volumen_pendiente_norm` < `0.0741` → IC=+0.190 (n=1566)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` < 0.0741 (IC base=+0.022)

- **PATRÓN** `volumen_pendiente_norm` > `0.2755` → IC=+0.229 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2755 (IC base=+0.022)

- **PATRÓN** `volumen_spike_ratio` < `1.4234` → IC=+0.218 (n=559)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4234 (IC base=+0.022)

- **PATRÓN** `volumen_spike_ratio` > `2.4876` → IC=+0.193 (n=559)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.4876 (IC base=+0.022)

- **PATRÓN** `ballena_activa_n` < `273.0` → IC=+0.229 (n=1115)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 273.0 (IC base=+0.022)

- **PATRÓN** `volumen_regimen` > `0.6201` → IC=+0.235 (n=1090)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6201 (IC base=-0.003)

- **PATRÓN** `volumen_pendiente_norm` > `0.272` → IC=+0.289 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.272 (IC base=-0.003)

- **PATRÓN** `volumen_spike_ratio` < `1.5333` → IC=+0.243 (n=458)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5333 (IC base=-0.003)

- **PATRÓN** `volumen_spike_ratio` > `2.1626` → IC=+0.246 (n=471)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1626 (IC base=-0.003)

- **PATRÓN** `ballena_activa_n` < `201.0` → IC=+0.241 (n=349)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 201.0 (IC base=-0.003)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0118` → IC=+0.309 (n=852)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0118 (IC base=+0.266)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.273 (n=2671)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.266)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.310 (n=1339)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.266)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.284` → IC=+0.302 (n=629)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.284 (IC base=+0.266)

- **PATRÓN** `volumen_pendiente_norm` < `0.098` → IC=+0.280 (n=2221)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.098 (IC base=+0.266)

- **PATRÓN** `volumen_spike_ratio` > `1.6104` → IC=+0.273 (n=2460)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6104 (IC base=+0.266)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.277 (n=3026)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.266)

- **PATRÓN** `libro_liquidez` > `1967.22` → IC=+0.282 (n=1155)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1967.22 (IC base=+0.266)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.281 (n=1525)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 19.0 (IC base=+0.266)

- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.328 (n=1001)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0101 (IC base=+0.293)

- **PATRÓN** `drift_60min` |x|≤ `0.1819` → IC=+0.311 (n=970)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1819 (IC base=+0.293)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.318 (n=838)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.293)

- **PATRÓN** `ibs_20min` < `0.3689` → IC=+0.296 (n=2203)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3689 (IC base=+0.293)

- **PATRÓN** `ibs_20min` > `0.2597` → IC=+0.300 (n=999)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2597 (IC base=+0.293)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.566` → IC=+0.311 (n=295)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.566 (IC base=+0.293)

- **PATRÓN** `volumen_pendiente_norm` < `0.1976` → IC=+0.291 (n=2151)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1976 (IC base=+0.293)

- **PATRÓN** `volumen_pendiente_norm` > `0.3414` → IC=+0.311 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3414 (IC base=+0.293)

- **PATRÓN** `volumen_spike_ratio` < `1.7274` → IC=+0.297 (n=926)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7274 (IC base=+0.293)

- **PATRÓN** `volumen_spike_ratio` > `2.6641` → IC=+0.302 (n=954)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6641 (IC base=+0.293)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.293 (n=1164)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.293)

- **PATRÓN** `libro_liquidez` > `2048.3156` → IC=+0.307 (n=735)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2048.3156 (IC base=+0.293)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.295 (n=1415)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 19.0 (IC base=+0.293)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7372` → IC=-0.186 (n=1056)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7372
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=3172)

- **PATRÓN** `ibs_20min` > `0.8773` → IC=+0.172 (n=1003)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` > 0.8773 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` > `0.1528` → IC=+0.234 (n=746)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1528 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` < `0.2131` → IC=+0.232 (n=1202)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2131 (IC base=+0.029)

- **PATRÓN** `volumen_regimen` < `1.0074` → IC=+0.244 (n=1233)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0074 (IC base=+0.029)

- **PATRÓN** `volumen_regimen` > `0.6704` → IC=+0.232 (n=1251)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6704 (IC base=+0.029)

- **PATRÓN** `volumen_pendiente_norm` > `0.102` → IC=+0.252 (n=437)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.102 (IC base=+0.029)

- **PATRÓN** `volumen_spike_ratio` < `1.3986` → IC=+0.244 (n=452)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3986 (IC base=+0.029)

- **PATRÓN** `ballena_activa_n` < `103.0` → IC=+0.267 (n=1219)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 103.0 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` < `0.194` → IC=+0.232 (n=972)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.194 (IC base=-0.001)

- **PATRÓN** `volumen_regimen` < `1.0319` → IC=+0.236 (n=855)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0319 (IC base=-0.001)

- **PATRÓN** `volumen_pendiente_norm` < `0.101` → IC=+0.249 (n=898)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.101 (IC base=-0.001)

- **PATRÓN** `volumen_pendiente_norm` > `0.2847` → IC=+0.295 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2847 (IC base=-0.001)

- **PATRÓN** `volumen_spike_ratio` < `1.793` → IC=+0.271 (n=614)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.793 (IC base=-0.001)

- **PATRÓN** `volumen_spike_ratio` > `2.4356` → IC=+0.254 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4356 (IC base=-0.001)

- **PATRÓN** `ballena_activa_n` < `109.0` → IC=+0.266 (n=821)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 109.0 (IC base=-0.001)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.76` → IC=-0.214 (n=1839)

  - _Acción_: SKIP cuando `ibs_20min` < 0.76
  - _Potencial_: sin este filtro IC_bueno=+0.305 (n=1844)

- **FILTRO** `ibs_20min` > `0.6471` → IC=-0.233 (n=898)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6471
  - _Potencial_: sin este filtro IC_bueno=+0.120 (n=2705)

- **FILTRO** `sigma_ewma_delta_pct` > `8.508` → IC=-0.243 (n=418)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.508
  - _Potencial_: sin este filtro IC_bueno=+0.068 (n=3185)

- **PATRÓN** `ibs_20min` > `0.76` → IC=+0.305 (n=1844)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.76 (IC base=+0.046)

- **PATRÓN** `dist_vwap_pct` > `0.2157` → IC=+0.336 (n=813)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2157 (IC base=+0.046)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.529` → IC=+0.183 (n=572)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 9.529 (IC base=+0.046)

- **PATRÓN** `volumen_regimen` < `0.8446` → IC=+0.334 (n=921)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8446 (IC base=+0.046)

- **PATRÓN** `volumen_regimen` > `0.7018` → IC=+0.325 (n=1234)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7018 (IC base=+0.046)

- **PATRÓN** `volumen_pendiente_norm` < `0.1583` → IC=+0.323 (n=1430)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1583 (IC base=+0.046)

- **PATRÓN** `volumen_pendiente_norm` > `0.2752` → IC=+0.350 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2752 (IC base=+0.046)

- **PATRÓN** `volumen_spike_ratio` < `1.4408` → IC=+0.349 (n=448)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4408 (IC base=+0.046)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.341 (n=1191)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 49.0 (IC base=+0.046)

- **PATRÓN** `ibs_20min` < `0.6471` → IC=+0.120 (n=2705)

  - _Acción_: Kelly boost +0.60€ cuando `ibs_20min` < 0.6471 (IC base=+0.032)

- **PATRÓN** `dist_vwap_pct` < `0.2801` → IC=+0.249 (n=1167)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2801 (IC base=+0.032)

- **PATRÓN** `volumen_regimen` < `0.7014` → IC=+0.261 (n=526)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7014 (IC base=+0.032)

- **PATRÓN** `volumen_pendiente_norm` < `0.1017` → IC=+0.242 (n=1131)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1017 (IC base=+0.032)

- **PATRÓN** `volumen_pendiente_norm` > `0.0775` → IC=+0.261 (n=454)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0775 (IC base=+0.032)

- **PATRÓN** `volumen_spike_ratio` < `2.4243` → IC=+0.253 (n=1147)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4243 (IC base=+0.032)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.270 (n=1163)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 52.0 (IC base=+0.032)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0108` → IC=+0.346 (n=1739)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0108 (IC base=+0.302)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.304 (n=755)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.302)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.314 (n=934)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.302)

- **PATRÓN** `ibs_20min` > `0.66` → IC=+0.335 (n=1948)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.66 (IC base=+0.302)

- **PATRÓN** `dist_vwap_pct` > `0.2044` → IC=+0.328 (n=1090)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2044 (IC base=+0.302)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.798` → IC=+0.323 (n=945)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.798 (IC base=+0.302)

- **PATRÓN** `volumen_regimen` > `0.6266` → IC=+0.311 (n=1947)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6266 (IC base=+0.302)

- **PATRÓN** `volumen_pendiente_norm` > `0.279` → IC=+0.344 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.279 (IC base=+0.302)

- **PATRÓN** `volumen_spike_ratio` > `1.4247` → IC=+0.314 (n=1865)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4247 (IC base=+0.302)

- **PATRÓN** `libro_liquidez` > `2630.254` → IC=+0.311 (n=1298)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2630.254 (IC base=+0.302)

- **PATRÓN** `ballena_activa_n` < `41.0` → IC=+0.336 (n=1669)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 41.0 (IC base=+0.302)

- **PATRÓN** `sigma_h` > `0.0152` → IC=+0.334 (n=1370)
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

- **PATRÓN** `ibs_20min` < `0.3675` → IC=+0.328 (n=2056)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3675 (IC base=+0.303)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.345` → IC=+0.318 (n=387)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.345 (IC base=+0.303)

- **PATRÓN** `volumen_regimen` < `0.7186` → IC=+0.309 (n=905)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7186 (IC base=+0.303)

- **PATRÓN** `volumen_regimen` > `1.224` → IC=+0.331 (n=685)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.224 (IC base=+0.303)

- **PATRÓN** `volumen_pendiente_norm` > `0.2831` → IC=+0.352 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2831 (IC base=+0.303)

- **PATRÓN** `volumen_spike_ratio` < `1.4161` → IC=+0.311 (n=627)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4161 (IC base=+0.303)

- **PATRÓN** `volumen_spike_ratio` > `2.1353` → IC=+0.306 (n=854)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1353 (IC base=+0.303)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0115` → IC=+0.225 (n=4299)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0115 (IC base=+0.180)

- **PATRÓN** `drift_60min` |x|≤ `0.0868` → IC=+0.202 (n=4293)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0868 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.190 (n=13357)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` > `0.557` → IC=+0.235 (n=12879)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.557 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` > `0.1637` → IC=+0.208 (n=5186)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1637 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.226` → IC=+0.261 (n=2532)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.226 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` < `1.1861` → IC=+0.169 (n=8549)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.1861 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` > `0.6242` → IC=+0.164 (n=8547)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 0.6242 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.2929` → IC=+0.204 (n=1868)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2929 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `2.6063` → IC=+0.190 (n=4162)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 2.6063 (IC base=+0.180)

- **PATRÓN** `libro_liquidez` > `1979.9172` → IC=+0.181 (n=11505)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 1979.9172 (IC base=+0.180)

- **PATRÓN** `ballena_activa_n` < `95.0` → IC=+0.198 (n=11804)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 95.0 (IC base=+0.180)

- **PATRÓN** `sigma_h` < `0.0091` → IC=+0.183 (n=10919)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0091 (IC base=+0.180)

- **PATRÓN** `drift_60min` |x|≤ `0.0795` → IC=+0.228 (n=4132)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0795 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.209 (n=5844)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.237 (n=12402)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.024` → IC=+0.198 (n=2022)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 10.024 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.684` → IC=+0.181 (n=10938)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` < 2.684 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` < `1.1825` → IC=+0.162 (n=8850)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.1825 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.2939` → IC=+0.226 (n=1834)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2939 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `2.635` → IC=+0.188 (n=3881)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.635 (IC base=+0.180)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.192 (n=11365)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 100.0 (IC base=+0.180)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.235 (n=722)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.216)

- **PATRÓN** `drift_60min` |x|≤ `0.3312` → IC=+0.231 (n=2155)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3312 (IC base=+0.216)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.227 (n=801)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.216)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.222 (n=1457)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.216)

- **PATRÓN** `ibs_20min` > `0.9275` → IC=+0.296 (n=1437)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9275 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.97` → IC=+0.329 (n=684)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.97 (IC base=+0.216)

- **PATRÓN** `volumen_pendiente_norm` > `0.2805` → IC=+0.271 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2805 (IC base=+0.216)

- **PATRÓN** `volumen_spike_ratio` > `1.4374` → IC=+0.216 (n=2038)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4374 (IC base=+0.216)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.228 (n=2327)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.216)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.225 (n=1287)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 14.0 (IC base=+0.216)

- **PATRÓN** `sigma_h` < `0.0081` → IC=+0.251 (n=1679)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0081 (IC base=+0.250)

- **PATRÓN** `sigma_h` > `0.0073` → IC=+0.264 (n=762)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0073 (IC base=+0.250)

- **PATRÓN** `drift_60min` |x|≤ `0.0941` → IC=+0.304 (n=738)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0941 (IC base=+0.250)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.254 (n=1718)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.250)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.254 (n=814)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.250)

- **PATRÓN** `ibs_20min` < `0.2941` → IC=+0.273 (n=1476)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2941 (IC base=+0.250)

- **PATRÓN** `volumen_pendiente_norm` < `0.1003` → IC=+0.252 (n=1468)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1003 (IC base=+0.250)

- **PATRÓN** `volumen_pendiente_norm` > `0.2975` → IC=+0.288 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2975 (IC base=+0.250)

- **PATRÓN** `volumen_spike_ratio` < `1.4323` → IC=+0.273 (n=530)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4323 (IC base=+0.250)

- **PATRÓN** `volumen_spike_ratio` > `2.6858` → IC=+0.253 (n=529)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6858 (IC base=+0.250)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.255 (n=1889)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.250)

- **PATRÓN** `libro_liquidez` > `1528.9218` → IC=+0.259 (n=1677)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1528.9218 (IC base=+0.250)

- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.254 (n=603)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 8.0 (IC base=+0.250)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.219 (n=652)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.1597` → IC=+0.184 (n=1296)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.1597 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.168 (n=2045)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` > `0.3353` → IC=+0.224 (n=1943)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3353 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` > `0.1352` → IC=+0.213 (n=1153)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1352 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.288` → IC=+0.226 (n=366)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.288 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` < `0.6923` → IC=+0.164 (n=855)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.6923 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` > `0.2801` → IC=+0.193 (n=311)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2801 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `1.5098` → IC=+0.171 (n=838)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.5098 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` > `2.4971` → IC=+0.166 (n=635)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 2.4971 (IC base=+0.153)

- **PATRÓN** `ballena_activa_n` < `229.0` → IC=+0.169 (n=826)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 229.0 (IC base=+0.153)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.169 (n=2039)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0058 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.2342` → IC=+0.174 (n=1794)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.2342 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.184 (n=975)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 15.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` < `0.6183` → IC=+0.206 (n=2039)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6183 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.447` → IC=+0.197 (n=387)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 11.447 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` < `1.2068` → IC=+0.159 (n=2039)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.2068 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` < `0.0934` → IC=+0.148 (n=1729)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` < 0.0934 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `2.4989` → IC=+0.152 (n=1919)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.4989 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` > `1.424` → IC=+0.145 (n=1919)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.424 (IC base=+0.145)

- **PATRÓN** `ballena_activa_n` < `201.0` → IC=+0.181 (n=615)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 201.0 (IC base=+0.145)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0108` → IC=+0.237 (n=989)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0108 (IC base=+0.213)

- **PATRÓN** `drift_60min` |x|≤ `0.3959` → IC=+0.225 (n=1918)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3959 (IC base=+0.213)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.234 (n=798)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.213)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.304 (n=1126)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.418` → IC=+0.299 (n=505)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.418 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` < `0.0992` → IC=+0.213 (n=1868)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0992 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` > `0.3549` → IC=+0.232 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3549 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` < `1.766` → IC=+0.215 (n=929)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.766 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` > `2.7088` → IC=+0.226 (n=958)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7088 (IC base=+0.213)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.220 (n=2601)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.213)

- **PATRÓN** `libro_liquidez` > `1961.26` → IC=+0.227 (n=988)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1961.26 (IC base=+0.213)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.247 (n=1646)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.236)

- **PATRÓN** `drift_60min` |x|≤ `0.5751` → IC=+0.250 (n=1869)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5751 (IC base=+0.236)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.280 (n=707)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.236)

- **PATRÓN** `ibs_20min` < `0.0092` → IC=+0.300 (n=823)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0092 (IC base=+0.236)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.512` → IC=+0.274 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.512 (IC base=+0.236)

- **PATRÓN** `volumen_pendiente_norm` > `0.3557` → IC=+0.281 (n=308)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3557 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` < `1.7474` → IC=+0.237 (n=786)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7474 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` > `2.1514` → IC=+0.239 (n=1190)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1514 (IC base=+0.236)

- **PATRÓN** `libro_liquidez` > `2048.1081` → IC=+0.242 (n=623)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2048.1081 (IC base=+0.236)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.238 (n=1183)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.236)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0074` → IC=+0.174 (n=2091)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0074 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.4062` → IC=+0.167 (n=2092)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.4062 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.163 (n=2166)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` > `0.3103` → IC=+0.214 (n=2091)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3103 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.1426` → IC=+0.199 (n=1267)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.1426 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.82` → IC=+0.199 (n=486)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 9.82 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `1.0218` → IC=+0.159 (n=1840)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.0218 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.1029` → IC=+0.178 (n=853)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.1029 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `1.817` → IC=+0.150 (n=1367)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.817 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `2.5051` → IC=+0.166 (n=683)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 2.5051 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `4615.2008` → IC=+0.185 (n=1394)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 4615.2008 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `139.0` → IC=+0.159 (n=2030)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 139.0 (IC base=+0.150)

- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.154 (n=2198)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0072 (IC base=+0.127)

- **PATRÓN** `drift_60min` |x|≤ `0.3949` → IC=+0.145 (n=2197)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.3949 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.166 (n=1039)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 15.0 (IC base=+0.127)

- **PATRÓN** `ibs_20min` < `0.6858` → IC=+0.187 (n=2197)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.6858 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` < `0.1533` → IC=+0.157 (n=2201)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.1533 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.793` → IC=+0.158 (n=770)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 6.793 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` < `0.8557` → IC=+0.156 (n=1465)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.8557 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` > `0.2993` → IC=+0.197 (n=331)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2993 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` < `1.8098` → IC=+0.135 (n=1372)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.8098 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` > `2.5475` → IC=+0.129 (n=686)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 2.5475 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `7496.4524` → IC=+0.192 (n=996)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 7496.4524 (IC base=+0.127)

- **PATRÓN** `ballena_activa_n` < `68.0` → IC=+0.148 (n=896)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 68.0 (IC base=+0.127)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0103` → IC=+0.177 (n=1067)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` > 0.0103 (IC base=+0.128)

- **PATRÓN** `drift_60min` |x|≤ `0.4388` → IC=+0.130 (n=2069)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.65€ cuando `drift_60min` |x|≤ 0.4388 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.170 (n=1119)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 15.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` > `0.4878` → IC=+0.216 (n=2351)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4878 (IC base=+0.128)

- **PATRÓN** `dist_vwap_pct` > `0.1959` → IC=+0.189 (n=1361)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1959 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.569` → IC=+0.279 (n=500)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.569 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` < `1.1724` → IC=+0.144 (n=2351)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 1.1724 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` < `0.161` → IC=+0.136 (n=2385)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` < 0.161 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` < `1.4387` → IC=+0.151 (n=761)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 1.4387 (IC base=+0.128)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.129 (n=2459)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.02 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `2775.0073` → IC=+0.209 (n=1066)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2775.0073 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.167 (n=757)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 20.0 (IC base=+0.128)

- **PATRÓN** `sigma_h` < `0.0108` → IC=+0.139 (n=2405)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` < 0.0108 (IC base=+0.120)

- **PATRÓN** `drift_60min` |x|≤ `0.1079` → IC=+0.175 (n=801)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.1079 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.141 (n=2446)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 5.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` < `0.5968` → IC=+0.219 (n=2402)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5968 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` < `0.1985` → IC=+0.149 (n=2276)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.1985 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.461` → IC=+0.131 (n=2124)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` < 2.461 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` < `1.1756` → IC=+0.129 (n=2402)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 1.1756 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` < `0.1654` → IC=+0.124 (n=2326)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.1654 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` > `0.276` → IC=+0.149 (n=320)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.276 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` < `1.4463` → IC=+0.134 (n=746)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 1.4463 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` > `2.4253` → IC=+0.138 (n=746)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 2.4253 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `2653.9292` → IC=+0.193 (n=1089)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 2653.9292 (IC base=+0.120)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.130 (n=1953)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 42.0 (IC base=+0.120)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0129` → IC=+0.247 (n=1932)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0129 (IC base=+0.222)

- **PATRÓN** `drift_60min` |x|≤ `0.1748` → IC=+0.237 (n=953)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1748 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.226 (n=2240)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.226 (n=1946)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` > `0.66` → IC=+0.258 (n=2169)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.66 (IC base=+0.222)

- **PATRÓN** `dist_vwap_pct` > `0.1824` → IC=+0.227 (n=1393)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1824 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.606` → IC=+0.251 (n=985)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.606 (IC base=+0.222)

- **PATRÓN** `volumen_regimen` < `1.1767` → IC=+0.224 (n=2163)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1767 (IC base=+0.222)

- **PATRÓN** `volumen_regimen` > `0.6187` → IC=+0.230 (n=2163)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6187 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` > `0.2826` → IC=+0.270 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2826 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` < `2.4647` → IC=+0.227 (n=2104)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4647 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` > `1.8078` → IC=+0.231 (n=1403)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8078 (IC base=+0.222)

- **PATRÓN** `libro_liquidez` > `2848.85` → IC=+0.224 (n=981)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2848.85 (IC base=+0.222)

- **PATRÓN** `sigma_h` < `0.0127` → IC=+0.233 (n=974)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0127 (IC base=+0.229)

- **PATRÓN** `sigma_h` > `0.0226` → IC=+0.240 (n=1004)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0226 (IC base=+0.229)

- **PATRÓN** `drift_60min` |x|≤ `0.0876` → IC=+0.261 (n=738)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0876 (IC base=+0.229)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.247 (n=1075)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.229)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.229 (n=991)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.229)

- **PATRÓN** `ibs_20min` < `0.4286` → IC=+0.257 (n=2213)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4286 (IC base=+0.229)

- **PATRÓN** `dist_vwap_pct` > `0.295` → IC=+0.234 (n=577)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.295 (IC base=+0.229)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.33` → IC=+0.258 (n=420)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.33 (IC base=+0.229)

- **PATRÓN** `volumen_regimen` > `0.6401` → IC=+0.236 (n=2213)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6401 (IC base=+0.229)

- **PATRÓN** `volumen_pendiente_norm` > `0.2802` → IC=+0.287 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2802 (IC base=+0.229)

- **PATRÓN** `volumen_spike_ratio` > `1.4386` → IC=+0.231 (n=2058)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4386 (IC base=+0.229)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.206 (n=1456)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.183)

- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.193 (n=1099)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` > 0.0089 (IC base=+0.183)

- **PATRÓN** `drift_60min` |x|≤ `0.0946` → IC=+0.205 (n=1098)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0946 (IC base=+0.183)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.216 (n=1624)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.183)

- **PATRÓN** `ibs_20min` > `0.4857` → IC=+0.217 (n=2940)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4857 (IC base=+0.183)

- **PATRÓN** `dist_vwap_pct` > `0.7874` → IC=+0.202 (n=485)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7874 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.62` → IC=+0.211 (n=1421)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.62 (IC base=+0.183)

- **PATRÓN** `volumen_regimen` < `0.8626` → IC=+0.205 (n=1974)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8626 (IC base=+0.183)

- **PATRÓN** `volumen_regimen` > `0.6964` → IC=+0.187 (n=2644)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` > 0.6964 (IC base=+0.183)

- **PATRÓN** `volumen_pendiente_norm` > `0.0998` → IC=+0.193 (n=1177)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.0998 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` < `1.4312` → IC=+0.197 (n=1067)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 1.4312 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` > `2.1943` → IC=+0.189 (n=1450)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.1943 (IC base=+0.183)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.189 (n=3717)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.02 (IC base=+0.183)

- **PATRÓN** `libro_liquidez` > `2685.4936` → IC=+0.190 (n=2940)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 2685.4936 (IC base=+0.183)

- **PATRÓN** `ballena_activa_n` < `148.0` → IC=+0.194 (n=3068)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 148.0 (IC base=+0.183)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.136 (n=1189)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` < 0.0038 (IC base=+0.088)

- **PATRÓN** `ibs_20min` < `0.3814` → IC=+0.161 (n=2373)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.3814 (IC base=+0.088)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.127 (n=1504)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 27.0 (IC base=+0.088)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.202 (n=408)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.179)

- **PATRÓN** `drift_60min` |x|≤ `0.3265` → IC=+0.201 (n=927)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3265 (IC base=+0.179)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.207 (n=845)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.179)

- **PATRÓN** `ibs_20min` > `0.6354` → IC=+0.237 (n=618)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6354 (IC base=+0.179)

- **PATRÓN** `dist_vwap_pct` > `0.3078` → IC=+0.198 (n=276)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.3078 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.069` → IC=+0.195 (n=395)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 3.069 (IC base=+0.179)

- **PATRÓN** `volumen_regimen` < `0.8745` → IC=+0.205 (n=618)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8745 (IC base=+0.179)

- **PATRÓN** `volumen_pendiente_norm` > `0.0716` → IC=+0.184 (n=365)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.0716 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` < `2.2054` → IC=+0.189 (n=798)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 2.2054 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` > `1.4107` → IC=+0.181 (n=906)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 1.4107 (IC base=+0.179)

- **PATRÓN** `libro_liquidez` > `14663.1359` → IC=+0.184 (n=618)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 14663.1359 (IC base=+0.179)

- **PATRÓN** `ballena_activa_n` < `158.0` → IC=+0.206 (n=396)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 158.0 (IC base=+0.179)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.140 (n=1102)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0057 (IC base=+0.117)

- **PATRÓN** `drift_60min` |x|≤ `0.2682` → IC=+0.142 (n=969)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.2682 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.130 (n=1000)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 7.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` < `0.6327` → IC=+0.167 (n=969)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` < 0.6327 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.694` → IC=+0.129 (n=219)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` > 8.694 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` > `1.063` → IC=+0.145 (n=500)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 1.063 (IC base=+0.117)

- **PATRÓN** `volumen_pendiente_norm` > `0.1612` → IC=+0.168 (n=293)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` > 0.1612 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` < `2.121` → IC=+0.131 (n=958)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 2.121 (IC base=+0.117)

- **PATRÓN** `ballena_activa_n` < `218.0` → IC=+0.163 (n=713)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 218.0 (IC base=+0.117)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.247 (n=667)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.215)

- **PATRÓN** `drift_60min` |x|≤ `0.0935` → IC=+0.242 (n=335)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0935 (IC base=+0.215)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.230 (n=1044)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.215)

- **PATRÓN** `ibs_20min` > `0.3758` → IC=+0.259 (n=893)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3758 (IC base=+0.215)

- **PATRÓN** `dist_vwap_pct` > `0.3577` → IC=+0.216 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3577 (IC base=+0.215)

- **PATRÓN** `dist_vwap_pct` < `0.2068` → IC=+0.221 (n=899)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2068 (IC base=+0.215)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.883` → IC=+0.243 (n=403)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.883 (IC base=+0.215)

- **PATRÓN** `volumen_regimen` < `0.8344` → IC=+0.227 (n=667)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8344 (IC base=+0.215)

- **PATRÓN** `volumen_regimen` > `1.1614` → IC=+0.222 (n=333)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1614 (IC base=+0.215)

- **PATRÓN** `volumen_pendiente_norm` > `0.2679` → IC=+0.248 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2679 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` < `1.4224` → IC=+0.243 (n=329)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4224 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` > `2.4672` → IC=+0.240 (n=329)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4672 (IC base=+0.215)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.215 (n=1118)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.215)

- **PATRÓN** `ibs_20min` < `0.1051` → IC=+0.165 (n=341)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` < 0.1051 (IC base=+0.063)

- **PATRÓN** `libro_liquidez` > `6456.6331` → IC=+0.136 (n=682)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 6456.6331 (IC base=+0.063)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0108` → IC=+0.186 (n=272)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0108 (IC base=+0.167)

- **PATRÓN** `drift_60min` |x|≤ `0.5315` → IC=+0.168 (n=817)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.5315 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.221 (n=392)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.167)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.275 (n=375)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.167)

- **PATRÓN** `dist_vwap_pct` > `0.9868` → IC=+0.240 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9868 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.1` → IC=+0.234 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.1 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` < `1.0604` → IC=+0.185 (n=719)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 1.0604 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` > `0.7156` → IC=+0.174 (n=729)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` > 0.7156 (IC base=+0.167)

- **PATRÓN** `volumen_pendiente_norm` > `0.1632` → IC=+0.184 (n=223)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.1632 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` < `1.4478` → IC=+0.183 (n=263)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` < 1.4478 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` > `2.1768` → IC=+0.174 (n=357)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 2.1768 (IC base=+0.167)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.175 (n=844)

  - _Acción_: Kelly boost +0.87€ cuando `libro_spread` < 0.02 (IC base=+0.167)

- **PATRÓN** `libro_liquidez` > `3033.9327` → IC=+0.190 (n=272)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 3033.9327 (IC base=+0.167)

- **PATRÓN** `ibs_20min` < `0.5455` → IC=+0.135 (n=774)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` < 0.5455 (IC base=+0.054)

- **PATRÓN** `libro_liquidez` > `2711.5941` → IC=+0.147 (n=398)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 2711.5941 (IC base=+0.054)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.126 (n=573)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 21.0 (IC base=+0.054)

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
- **PATRÓN** `sigma_h` > `0.0115` → IC=+0.227 (n=5596)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0115 (IC base=+0.183)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.192 (n=17465)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 5.0 (IC base=+0.183)

- **PATRÓN** `ibs_20min` > `0.4474` → IC=+0.231 (n=16771)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4474 (IC base=+0.183)

- **PATRÓN** `dist_vwap_pct` > `0.8911` → IC=+0.209 (n=2041)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8911 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.26` → IC=+0.255 (n=4101)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.26 (IC base=+0.183)

- **PATRÓN** `volumen_regimen` < `1.2211` → IC=+0.170 (n=11245)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 1.2211 (IC base=+0.183)

- **PATRÓN** `volumen_pendiente_norm` > `0.2903` → IC=+0.205 (n=2224)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2903 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` > `2.6123` → IC=+0.197 (n=5437)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 2.6123 (IC base=+0.183)

- **PATRÓN** `libro_liquidez` > `1972.2956` → IC=+0.185 (n=14982)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 1972.2956 (IC base=+0.183)

- **PATRÓN** `ballena_activa_n` < `112.0` → IC=+0.204 (n=15394)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 112.0 (IC base=+0.183)

- **PATRÓN** `sigma_h` < `0.0096` → IC=+0.192 (n=13409)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0096 (IC base=+0.188)

- **PATRÓN** `drift_60min` |x|≤ `0.4908` → IC=+0.192 (n=15224)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.4908 (IC base=+0.188)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.210 (n=5645)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.188)

- **PATRÓN** `ibs_20min` < `0.5833` → IC=+0.243 (n=15230)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5833 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.817` → IC=+0.207 (n=2112)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.817 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.571` → IC=+0.191 (n=14722)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` < 3.571 (IC base=+0.188)

- **PATRÓN** `volumen_regimen` < `0.7049` → IC=+0.163 (n=4520)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.7049 (IC base=+0.188)

- **PATRÓN** `volumen_pendiente_norm` > `0.2903` → IC=+0.254 (n=2060)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2903 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` > `2.2577` → IC=+0.197 (n=6525)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.2577 (IC base=+0.188)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.217 (n=9499)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 40.0 (IC base=+0.188)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.236 (n=916)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.225)

- **PATRÓN** `drift_60min` |x|≤ `0.3474` → IC=+0.227 (n=2735)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3474 (IC base=+0.225)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.238 (n=1321)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.229 (n=1845)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.225)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.331 (n=1083)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.225)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.499` → IC=+0.354 (n=640)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.499 (IC base=+0.225)

- **PATRÓN** `volumen_pendiente_norm` > `0.2319` → IC=+0.283 (n=486)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2319 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` < `1.4457` → IC=+0.222 (n=876)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4457 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` > `2.2863` → IC=+0.237 (n=1190)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2863 (IC base=+0.225)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.243 (n=2913)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.225)

- **PATRÓN** `libro_liquidez` > `1997.6779` → IC=+0.228 (n=1240)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1997.6779 (IC base=+0.225)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.249 (n=1645)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 17.0 (IC base=+0.225)

- **PATRÓN** `sigma_h` < `0.0085` → IC=+0.267 (n=2333)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0085 (IC base=+0.262)

- **PATRÓN** `drift_60min` |x|≤ `0.1192` → IC=+0.285 (n=1026)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1192 (IC base=+0.262)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.268 (n=2133)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.262)

- **PATRÓN** `ibs_20min` < `0.5106` → IC=+0.288 (n=2332)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5106 (IC base=+0.262)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.147` → IC=+0.266 (n=463)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.147 (IC base=+0.262)

- **PATRÓN** `volumen_pendiente_norm` < `0.0952` → IC=+0.262 (n=2095)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0952 (IC base=+0.262)

- **PATRÓN** `volumen_pendiente_norm` > `0.286` → IC=+0.290 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.286 (IC base=+0.262)

- **PATRÓN** `volumen_spike_ratio` < `1.5578` → IC=+0.265 (n=972)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5578 (IC base=+0.262)

- **PATRÓN** `volumen_spike_ratio` > `2.6411` → IC=+0.271 (n=736)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6411 (IC base=+0.262)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.264 (n=2626)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.262)

- **PATRÓN** `libro_liquidez` > `1633.22` → IC=+0.270 (n=2083)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1633.22 (IC base=+0.262)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.271 (n=960)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.262)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.199 (n=909)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.1044` → IC=+0.166 (n=1196)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.1044 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.161 (n=2833)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` > `0.3683` → IC=+0.224 (n=2428)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3683 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.1253` → IC=+0.195 (n=1396)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.1253 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.479` → IC=+0.162 (n=448)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 11.479 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.15` → IC=+0.152 (n=2498)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` < 4.15 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `0.6305` → IC=+0.174 (n=906)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.6305 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` < `0.072` → IC=+0.153 (n=2425)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` < 0.072 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.2713` → IC=+0.181 (n=387)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.2713 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `2.1826` → IC=+0.159 (n=2338)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.1826 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `1.528` → IC=+0.155 (n=2375)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.528 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `265.0` → IC=+0.184 (n=1149)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 265.0 (IC base=+0.150)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.165 (n=2263)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0058 (IC base=+0.143)

- **PATRÓN** `drift_60min` |x|≤ `0.2565` → IC=+0.164 (n=1992)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.2565 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.171 (n=848)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.143)

- **PATRÓN** `ibs_20min` < `0.6969` → IC=+0.198 (n=2263)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.6969 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.179` → IC=+0.159 (n=376)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 11.179 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` < `1.1907` → IC=+0.154 (n=2263)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 1.1907 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` > `0.2172` → IC=+0.195 (n=424)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2172 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` < `2.4315` → IC=+0.149 (n=2158)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.4315 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` > `1.7751` → IC=+0.153 (n=1439)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.7751 (IC base=+0.143)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=2938)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.143)

- **PATRÓN** `ballena_activa_n` < `275.0` → IC=+0.158 (n=919)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 275.0 (IC base=+0.143)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0123` → IC=+0.259 (n=933)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0123 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.234 (n=2916)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.226)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.227 (n=2503)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.226)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.304 (n=1039)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.303` → IC=+0.324 (n=595)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.303 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` < `0.0966` → IC=+0.231 (n=2472)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0966 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` > `3.1837` → IC=+0.241 (n=904)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.1837 (IC base=+0.226)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.234 (n=3328)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.226)

- **PATRÓN** `libro_liquidez` > `1975.9` → IC=+0.237 (n=1266)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1975.9 (IC base=+0.226)

- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.246 (n=2306)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0106 (IC base=+0.241)

- **PATRÓN** `drift_60min` |x|≤ `0.1813` → IC=+0.258 (n=1153)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1813 (IC base=+0.241)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.262 (n=980)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.241)

- **PATRÓN** `ibs_20min` < `0.0316` → IC=+0.307 (n=874)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0316 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.632` → IC=+0.294 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.632 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` > `0.3452` → IC=+0.303 (n=388)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3452 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` > `2.1336` → IC=+0.252 (n=1660)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1336 (IC base=+0.241)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.244 (n=1390)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.241)

- **PATRÓN** `libro_liquidez` > `2048.1081` → IC=+0.254 (n=873)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2048.1081 (IC base=+0.241)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.258 (n=1107)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.241)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.198 (n=1271)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0039 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.4207` → IC=+0.158 (n=2884)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.4207 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.160 (n=2991)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 5.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` > `0.2458` → IC=+0.194 (n=2884)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 0.2458 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.1417` → IC=+0.171 (n=1522)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.1417 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.123` → IC=+0.160 (n=1170)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 4.123 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `0.8651` → IC=+0.167 (n=1924)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.8651 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.2802` → IC=+0.191 (n=373)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.2802 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `1.5241` → IC=+0.163 (n=1238)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 1.5241 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` > `2.1683` → IC=+0.157 (n=1276)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 2.1683 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `6189.8682` → IC=+0.242 (n=1307)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6189.8682 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `74.0` → IC=+0.172 (n=1232)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 74.0 (IC base=+0.146)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.151 (n=2400)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0075 (IC base=+0.129)

- **PATRÓN** `drift_60min` |x|≤ `0.4377` → IC=+0.140 (n=2399)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.4377 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.156 (n=872)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 17.0 (IC base=+0.129)

- **PATRÓN** `ibs_20min` < `0.7369` → IC=+0.185 (n=2399)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.7369 (IC base=+0.129)

- **PATRÓN** `dist_vwap_pct` < `0.1485` → IC=+0.146 (n=2188)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.1485 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.071` → IC=+0.175 (n=367)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 11.071 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` < `0.6988` → IC=+0.144 (n=1057)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.6988 (IC base=+0.129)

- **PATRÓN** `volumen_pendiente_norm` > `0.2959` → IC=+0.221 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2959 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` < `2.2238` → IC=+0.131 (n=2030)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 2.2238 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` > `1.4287` → IC=+0.135 (n=2307)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.4287 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `7204.7935` → IC=+0.213 (n=800)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7204.7935 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `67.0` → IC=+0.132 (n=786)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 67.0 (IC base=+0.129)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0103` → IC=+0.158 (n=1318)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0103 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.178 (n=1065)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` > `0.4423` → IC=+0.199 (n=2905)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4423 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` > `1.0588` → IC=+0.208 (n=502)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0588 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.739` → IC=+0.267 (n=735)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.739 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` < `1.221` → IC=+0.136 (n=2905)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 1.221 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` < `0.1615` → IC=+0.126 (n=3022)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` < 0.1615 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` > `0.2794` → IC=+0.133 (n=374)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_pendiente_norm` > 0.2794 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` < `2.4804` → IC=+0.125 (n=2838)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 2.4804 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` > `2.1924` → IC=+0.130 (n=1287)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 2.1924 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.130 (n=3017)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.02 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `2497.3328` → IC=+0.231 (n=1317)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2497.3328 (IC base=+0.125)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.146 (n=910)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 24.0 (IC base=+0.125)

- **PATRÓN** `sigma_h` < `0.01` → IC=+0.153 (n=2434)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.01 (IC base=+0.118)

- **PATRÓN** `drift_60min` |x|≤ `0.1335` → IC=+0.155 (n=922)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.1335 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.131 (n=2851)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 5.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` < `0.6471` → IC=+0.213 (n=2767)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6471 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` < `0.2141` → IC=+0.136 (n=2391)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.2141 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.252` → IC=+0.135 (n=2665)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` < 3.252 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` < `0.7102` → IC=+0.140 (n=1216)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 0.7102 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` > `0.2252` → IC=+0.174 (n=473)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.2252 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` < `1.4414` → IC=+0.155 (n=862)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.4414 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `2673.057` → IC=+0.209 (n=921)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2673.057 (IC base=+0.118)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.134 (n=2276)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 47.0 (IC base=+0.118)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0137` → IC=+0.250 (n=2448)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0137 (IC base=+0.231)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.236 (n=2858)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.231)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.238 (n=1832)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.231)

- **PATRÓN** `ibs_20min` > `0.61` → IC=+0.272 (n=2454)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.61 (IC base=+0.231)

- **PATRÓN** `dist_vwap_pct` > `0.1891` → IC=+0.246 (n=1477)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1891 (IC base=+0.231)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.737` → IC=+0.271 (n=921)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.737 (IC base=+0.231)

- **PATRÓN** `volumen_regimen` < `1.2308` → IC=+0.238 (n=2740)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2308 (IC base=+0.231)

- **PATRÓN** `volumen_regimen` > `0.64` → IC=+0.233 (n=2740)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.64 (IC base=+0.231)

- **PATRÓN** `volumen_pendiente_norm` > `0.2873` → IC=+0.256 (n=346)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2873 (IC base=+0.231)

- **PATRÓN** `volumen_spike_ratio` > `2.5001` → IC=+0.251 (n=889)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5001 (IC base=+0.231)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.232 (n=3560)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.231)

- **PATRÓN** `libro_liquidez` > `2615.934` → IC=+0.236 (n=1827)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2615.934 (IC base=+0.231)

- **PATRÓN** `sigma_h` > `0.0255` → IC=+0.252 (n=951)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0255 (IC base=+0.230)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.237 (n=2680)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.230)

- **PATRÓN** `ibs_20min` < `0.5152` → IC=+0.265 (n=2848)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5152 (IC base=+0.230)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.19` → IC=+0.267 (n=543)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.19 (IC base=+0.230)

- **PATRÓN** `volumen_regimen` > `1.2292` → IC=+0.259 (n=951)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2292 (IC base=+0.230)

- **PATRÓN** `volumen_pendiente_norm` > `0.2816` → IC=+0.299 (n=377)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2816 (IC base=+0.230)

- **PATRÓN** `volumen_spike_ratio` > `1.4311` → IC=+0.232 (n=2646)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4311 (IC base=+0.230)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.194 (n=4942)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.246 (n=1693)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.209)

- **PATRÓN** `drift_60min` |x|≤ `0.5027` → IC=+0.219 (n=5063)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5027 (IC base=+0.209)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.225 (n=1839)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.209)

- **PATRÓN** `ibs_20min` > `0.9404` → IC=+0.248 (n=1688)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9404 (IC base=+0.209)

- **PATRÓN** `dist_vwap_pct` < `0.2457` → IC=+0.211 (n=3244)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2457 (IC base=+0.209)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.02` → IC=+0.216 (n=827)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.02 (IC base=+0.209)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.606` → IC=+0.210 (n=4509)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.606 (IC base=+0.209)

- **PATRÓN** `volumen_regimen` < `0.7051` → IC=+0.221 (n=1624)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7051 (IC base=+0.209)

- **PATRÓN** `volumen_pendiente_norm` < `0.1066` → IC=+0.209 (n=4730)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1066 (IC base=+0.209)

- **PATRÓN** `volumen_pendiente_norm` > `0.1667` → IC=+0.222 (n=1423)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1667 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` < `1.4541` → IC=+0.216 (n=1663)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4541 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` > `1.8446` → IC=+0.209 (n=3324)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8446 (IC base=+0.209)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.214 (n=3897)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.209)

- **PATRÓN** `libro_liquidez` > `2928.9788` → IC=+0.216 (n=4523)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2928.9788 (IC base=+0.209)

- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.240 (n=1241)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.193)

- **PATRÓN** `drift_60min` |x|≤ `0.4876` → IC=+0.209 (n=3718)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4876 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.214 (n=1254)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.208 (n=1658)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.193)

- **PATRÓN** `ibs_20min` < `0.7333` → IC=+0.199 (n=3719)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7333 (IC base=+0.193)

- **PATRÓN** `dist_vwap_pct` > `0.6718` → IC=+0.200 (n=627)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6718 (IC base=+0.193)

- **PATRÓN** `dist_vwap_pct` < `0.2386` → IC=+0.190 (n=3413)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` < 0.2386 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.835` → IC=+0.203 (n=3334)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.835 (IC base=+0.193)

- **PATRÓN** `volumen_regimen` < `1.0964` → IC=+0.202 (n=3102)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0964 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` < `0.0976` → IC=+0.197 (n=3412)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` < 0.0976 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` > `0.2227` → IC=+0.195 (n=749)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2227 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` < `1.5322` → IC=+0.199 (n=1613)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.5322 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` > `2.1876` → IC=+0.201 (n=1662)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1876 (IC base=+0.193)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.194 (n=4942)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.01 (IC base=+0.193)

- **PATRÓN** `ballena_activa_n` < `177.0` → IC=+0.202 (n=3211)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 177.0 (IC base=+0.193)

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
- **PATRÓN** `sigma_h` < `0.0108` → IC=+0.201 (n=651)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0108 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.202 (n=760)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 3.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` > `0.925` → IC=+0.245 (n=335)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.925 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` > `0.7405` → IC=+0.234 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7405 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.222` → IC=+0.203 (n=398)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.222 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `0.6947` → IC=+0.226 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6947 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` < `0.1062` → IC=+0.192 (n=667)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` < 0.1062 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.079` → IC=+0.190 (n=330)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.079 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` < `1.565` → IC=+0.195 (n=316)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 1.565 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `2.4766` → IC=+0.207 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4766 (IC base=+0.181)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.186 (n=861)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.02 (IC base=+0.181)

- **PATRÓN** `libro_liquidez` > `3092.0404` → IC=+0.201 (n=660)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3092.0404 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.198 (n=723)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 52.0 (IC base=+0.181)

- **PATRÓN** `sigma_h` < `0.0093` → IC=+0.209 (n=362)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0093 (IC base=+0.204)

- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.210 (n=181)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0125 (IC base=+0.204)

- **PATRÓN** `drift_60min` |x|≤ `0.6042` → IC=+0.228 (n=542)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6042 (IC base=+0.204)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.240 (n=371)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 9.0 (IC base=+0.204)

- **PATRÓN** `ibs_20min` < `0.7273` → IC=+0.225 (n=543)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7273 (IC base=+0.204)

- **PATRÓN** `dist_vwap_pct` > `0.8487` → IC=+0.220 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8487 (IC base=+0.204)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.868` → IC=+0.213 (n=486)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.868 (IC base=+0.204)

- **PATRÓN** `volumen_regimen` < `0.7555` → IC=+0.218 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7555 (IC base=+0.204)

- **PATRÓN** `volumen_regimen` > `0.9335` → IC=+0.205 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.9335 (IC base=+0.204)

- **PATRÓN** `volumen_pendiente_norm` < `0.1073` → IC=+0.224 (n=469)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1073 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` > `2.1983` → IC=+0.240 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1983 (IC base=+0.204)

- **PATRÓN** `libro_liquidez` > `2981.8939` → IC=+0.224 (n=542)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2981.8939 (IC base=+0.204)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.236 (n=535)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 46.0 (IC base=+0.204)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.158 (n=737)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.004 (IC base=+0.069)

- **PATRÓN** `ibs_20min` > `0.3879` → IC=+0.142 (n=1581)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` > 0.3879 (IC base=+0.069)

- **PATRÓN** `dist_vwap_pct` > `0.3572` → IC=+0.158 (n=544)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.3572 (IC base=+0.069)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.991` → IC=+0.157 (n=461)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 8.991 (IC base=+0.069)

- **PATRÓN** `volumen_pendiente_norm` > `0.2748` → IC=+0.142 (n=219)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` > 0.2748 (IC base=+0.069)

- **PATRÓN** `ibs_20min` < `0.2028` → IC=+0.234 (n=581)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2028 (IC base=+0.058)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.344` → IC=+0.176 (n=137)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 10.344 (IC base=+0.058)

- **PATRÓN** `volumen_pendiente_norm` > `0.1467` → IC=+0.178 (n=237)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.1467 (IC base=+0.058)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.132 (n=552)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.66€ cuando `sigma_h` < 0.0056 (IC base=+0.086)

- **PATRÓN** `ibs_20min` > `0.5149` → IC=+0.190 (n=465)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.5149 (IC base=+0.086)

- **PATRÓN** `dist_vwap_pct` > `0.1227` → IC=+0.153 (n=260)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.1227 (IC base=+0.086)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.123 (n=274)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0037 (IC base=+0.075)

- **PATRÓN** `ibs_20min` < `0.0493` → IC=+0.279 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0493 (IC base=+0.075)

- **PATRÓN** `volumen_pendiente_norm` > `0.2162` → IC=+0.207 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2162 (IC base=+0.075)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` > `0.7006` → IC=-0.181 (n=92)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7006
  - _Potencial_: sin este filtro IC_bueno=+0.121 (n=278)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.132 (n=481)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.66€ cuando `sigma_h` < 0.006 (IC base=+0.092)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.157 (n=208)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 17.0 (IC base=+0.092)

- **PATRÓN** `ibs_20min` > `0.4221` → IC=+0.176 (n=516)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` > 0.4221 (IC base=+0.092)

- **PATRÓN** `dist_vwap_pct` > `0.1246` → IC=+0.196 (n=264)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.1246 (IC base=+0.092)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.194` → IC=+0.250 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.194 (IC base=+0.092)

- **PATRÓN** `volumen_regimen` < `0.5769` → IC=+0.138 (n=172)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 0.5769 (IC base=+0.092)

- **PATRÓN** `volumen_pendiente_norm` > `0.2854` → IC=+0.167 (n=73)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.2854 (IC base=+0.092)

- **PATRÓN** `ibs_20min` < `0.0314` → IC=+0.300 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0314 (IC base=+0.019)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.686` → IC=+0.239 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.686 (IC base=+0.019)

### GBM_LATE_60M#SOL#60min
- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.166 (n=363)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.75 (IC base=+0.031)

- **PATRÓN** `dist_vwap_pct` > `0.7321` → IC=+0.142 (n=132)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.7321 (IC base=+0.031)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.332` → IC=+0.164 (n=117)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 9.332 (IC base=+0.031)

- **PATRÓN** `volumen_pendiente_norm` > `0.2784` → IC=+0.133 (n=77)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_pendiente_norm` > 0.2784 (IC base=+0.031)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.158 (n=238)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0103 (IC base=+0.077)

- **PATRÓN** `ibs_20min` < `0.16` → IC=+0.224 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.16 (IC base=+0.077)

- **PATRÓN** `dist_vwap_pct` < `0.1716` → IC=+0.145 (n=195)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.1716 (IC base=+0.077)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.739` → IC=+0.312 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.739 (IC base=+0.077)

- **PATRÓN** `volumen_regimen` > `1.0779` → IC=+0.218 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0779 (IC base=+0.077)

- **PATRÓN** `volumen_pendiente_norm` > `0.1517` → IC=+0.234 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1517 (IC base=+0.077)

- **PATRÓN** `volumen_spike_ratio` < `2.1557` → IC=+0.154 (n=163)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.1557 (IC base=+0.077)

- **PATRÓN** `volumen_spike_ratio` > `1.3981` → IC=+0.163 (n=185)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 1.3981 (IC base=+0.077)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.150 (n=181)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.06 (IC base=+0.077)

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

- **FILTRO** `volumen_spike_ratio` > `2.3922` → IC=-0.340 (n=23)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.3922
  - _Potencial_: sin este filtro IC_bueno=-0.271 (n=46)

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
  - _Potencial_: sin este filtro IC_bueno=+0.148 (n=543)

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

- **PATRÓN** `ibs_20min` < `0.156` → IC=+0.148 (n=543)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` < 0.156 (IC base=+0.056)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.085` → IC=+0.177 (n=184)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 9.085 (IC base=+0.056)

- **PATRÓN** `libro_liquidez` > `3242.4514` → IC=+0.137 (n=411)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 3242.4514 (IC base=+0.056)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.6889` → IC=-0.209 (n=53)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6889
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=161)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.184 (n=96)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` > 0.0049 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.156 (n=193)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 12.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.143 (n=110)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 6.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` < `0.1684` → IC=+0.198 (n=286)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.1684 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.158` → IC=+0.164 (n=123)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 7.158 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` > `1.0364` → IC=+0.182 (n=130)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 1.0364 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` < `0.0706` → IC=+0.155 (n=221)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` < 0.0706 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.2726` → IC=+0.167 (n=49)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.2726 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `2.5202` → IC=+0.173 (n=255)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 2.5202 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `1.5382` → IC=+0.143 (n=228)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.5382 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `4588.7853` → IC=+0.147 (n=256)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 4588.7853 (IC base=+0.137)

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
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=3523)

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
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=1297)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=1251)

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
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=418)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=399)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.137 (n=177)

  - _Acción_: Kelly boost +0.68€ cuando `py_entrada` < 0.495 (IC base=+0.021)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=840)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=840)

- **FILTRO** `py_entrada` < `0.44` → IC=-0.132 (n=259)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=661)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=822)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=822)

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
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=231)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=255)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=255)

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
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=258)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.129 (n=87)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=186)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.4` → IC=-0.124 (n=1384)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=3585)

### LIQUIDACIONES_DEPTH_FASE0#BNB#15min
- **FILTRO** `py_entrada` > `0.59` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=34)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.145 (n=60)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.122 (n=35)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.46` → IC=+0.176 (n=146)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` < 0.46 (IC base=+0.013)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.190 (n=56)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=251)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.143 (n=152)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=174)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.151 (n=41)

  - _Acción_: Kelly boost +0.76€ cuando `py_entrada` < 0.5 (IC base=+0.054)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.53` → IC=-0.129 (n=348)

  - _Acción_: SKIP cuando `py_entrada` < 0.53
  - _Potencial_: sin este filtro IC_bueno=+0.107 (n=120)

- **FILTRO** `profundidad_ratio` < `56.1` → IC=-0.167 (n=154)

  - _Acción_: SKIP cuando `profundidad_ratio` < 56.1
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=314)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.136 (n=196)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=219)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `profundidad_ratio` < `20.7` → IC=-0.137 (n=144)

  - _Acción_: SKIP cuando `profundidad_ratio` < 20.7
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=296)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.174 (n=84)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=361)

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
- **FILTRO** `py_entrada` < `0.47` → IC=-0.166 (n=6002)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=18601)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.176 (n=6079)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=19203)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.196 (n=1096)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=3380)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.174 (n=1043)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.068 (n=3469)

- **PATRÓN** `py_entrada` > `0.495` → IC=+0.128 (n=3016)

  - _Acción_: Kelly boost +0.64€ cuando `py_entrada` > 0.495 (IC base=+0.040)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.145 (n=1181)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` > 1.0 (IC base=+0.040)

- **PATRÓN** `libro_liquidez` > `1306.896` → IC=+0.137 (n=2238)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 1306.896 (IC base=+0.040)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.128 (n=2113)

  - _Acción_: Kelly boost +0.64€ cuando `py_entrada` < 0.5 (IC base=+0.012)

- **PATRÓN** `libro_liquidez` > `1502.3972` → IC=+0.155 (n=1535)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 1502.3972 (IC base=+0.012)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.158 (n=834)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=2761)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.178 (n=881)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=2705)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.175 (n=1094)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.106 (n=3391)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.203 (n=1074)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.076 (n=3542)

- **PATRÓN** `ibs_20min` > `0.9645` → IC=+0.131 (n=1525)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` > 0.9645 (IC base=+0.038)

- **PATRÓN** `libro_liquidez` > `1539.75` → IC=+0.120 (n=2243)

  - _Acción_: Kelly boost +0.60€ cuando `libro_liquidez` > 1539.75 (IC base=+0.038)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.159 (n=1092)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=3390)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=2372)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.162 (n=758)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=2310)

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
  - _Potencial_: sin este filtro IC_bueno=-0.095 (n=437)

- **FILTRO** `py_entrada` < `0.445` → IC=-0.264 (n=138)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=424)

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
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=918)

- **FILTRO** `libro_liquidez` < `1762.8003` → IC=-0.161 (n=234)

  - _Acción_: SKIP cuando `libro_liquidez` < 1762.8003
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=703)

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
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=37783)

- **FILTRO** `py_entrada` < `0.33` → IC=-0.285 (n=13482)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=41281)

- **FILTRO** `ibs_7min` < `0.2376` → IC=-0.230 (n=13690)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2376
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=41073)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.153 (n=18240)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=36523)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.242 (n=16914)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=52032)

- **FILTRO** `ibs_7min` > `0.2857` → IC=-0.182 (n=17031)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2857
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=51915)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.148 (n=2737)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=6821)

- **FILTRO** `py_entrada` < `0.46` → IC=-0.236 (n=4723)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=4835)

- **FILTRO** `ibs_7min` < `0.7129` → IC=-0.244 (n=3154)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7129
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=6404)

- **FILTRO** `ballena_activa_n` > `6.0` → IC=-0.179 (n=2032)

  - _Acción_: SKIP cuando `ballena_activa_n` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=7526)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.271 (n=2966)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=8986)

- **FILTRO** `ibs_7min` > `0.7703` → IC=-0.211 (n=2986)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7703
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=8966)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.266 (n=2162)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=7074)

- **FILTRO** `ibs_7min` < `0.7258` → IC=-0.201 (n=2308)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7258
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=6928)

- **FILTRO** `ballena_activa_n` > `154.0` → IC=-0.192 (n=2303)

  - _Acción_: SKIP cuando `ballena_activa_n` > 154.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=6933)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.265 (n=2316)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=7083)

- **FILTRO** `ibs_7min` > `0.2678` → IC=-0.197 (n=2347)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2678
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=7052)

- **FILTRO** `ballena_activa_n` > `151.0` → IC=-0.183 (n=2342)

  - _Acción_: SKIP cuando `ballena_activa_n` > 151.0
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=7057)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.158 (n=2239)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=6850)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.314 (n=2239)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=6850)

- **FILTRO** `ibs_7min` < `0.2963` → IC=-0.246 (n=2999)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2963
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=6090)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.195 (n=2159)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=6930)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.255 (n=2969)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=9755)

- **FILTRO** `ibs_7min` > `0.7333` → IC=-0.178 (n=3178)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7333
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=9546)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.262 (n=2094)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=6830)

- **FILTRO** `ibs_7min` < `0.7289` → IC=-0.187 (n=2231)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7289
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=6693)

- **FILTRO** `ballena_activa_n` > `27.0` → IC=-0.189 (n=2209)

  - _Acción_: SKIP cuando `ballena_activa_n` > 27.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=6715)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.270 (n=2088)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=7167)

- **FILTRO** `ibs_7min` > `0.2748` → IC=-0.180 (n=2313)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2748
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=6942)

- **FILTRO** `ballena_activa_n` > `26.0` → IC=-0.176 (n=2279)

  - _Acción_: SKIP cuando `ballena_activa_n` > 26.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=6976)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.284 (n=2153)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=6834)

- **FILTRO** `ibs_7min` < `0.2143` → IC=-0.233 (n=2238)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2143
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=6749)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.219 (n=2161)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=6826)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.191 (n=3186)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=9980)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.32` → IC=-0.292 (n=2113)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=6856)

- **FILTRO** `ibs_7min` < `0.2` → IC=-0.223 (n=2224)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=6745)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.202 (n=1992)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=6977)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.216 (n=3045)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=9405)

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
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=3999)

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
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=2209)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.200 (n=1201)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.179)

- **PATRÓN** `sigma_h` > `0.012` → IC=+0.196 (n=1199)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` > 0.012 (IC base=+0.179)

- **PATRÓN** `drift_60min` |x|≤ `0.1752` → IC=+0.194 (n=3168)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.1752 (IC base=+0.179)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1333` → IC=+0.191 (n=1435)

  - _Acción_: Kelly boost +0.96€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1333 (IC base=+0.179)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.186 (n=3329)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 6.0 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.182 (n=3314)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 15.0 (IC base=+0.179)

- **PATRÓN** `ibs_15` > `0.5548` → IC=+0.254 (n=3597)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5548 (IC base=+0.179)

- **PATRÓN** `dist_vwap_pct` > `0.1289` → IC=+0.170 (n=1711)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.1289 (IC base=+0.179)

- **PATRÓN** `dist_vwap_pct` < `0.3149` → IC=+0.166 (n=2848)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.3149 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.542` → IC=+0.256 (n=934)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.542 (IC base=+0.179)

- **PATRÓN** `libro_liquidez` > `4676.7697` → IC=+0.197 (n=1199)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 4676.7697 (IC base=+0.179)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=1425)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.253 (n=269)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.221)

- **PATRÓN** `drift_60min` |x|≤ `0.0582` → IC=+0.267 (n=204)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0582 (IC base=+0.221)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2522` → IC=+0.248 (n=204)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2522 (IC base=+0.221)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2297` → IC=+0.234 (n=355)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2297 (IC base=+0.221)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.239 (n=642)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.221)

- **PATRÓN** `ibs_15` > `0.7176` → IC=+0.287 (n=612)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7176 (IC base=+0.221)

- **PATRÓN** `dist_vwap_pct` > `0.2385` → IC=+0.243 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2385 (IC base=+0.221)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.96` → IC=+0.304 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.96 (IC base=+0.221)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.222 (n=793)

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

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1312` → IC=+0.164 (n=281)

  - _Acción_: Kelly boost +0.82€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1312 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.155 (n=653)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 6.0 (IC base=+0.147)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.152 (n=742)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 17.0 (IC base=+0.147)

- **PATRÓN** `ibs_15` > `0.5415` → IC=+0.242 (n=712)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5415 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` > `0.1194` → IC=+0.160 (n=439)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.1194 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.577` → IC=+0.263 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.577 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `3215.6409` → IC=+0.154 (n=712)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 3215.6409 (IC base=+0.147)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `sigma_ewma_delta_pct` > `17.774` → IC=-0.192 (n=37)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 17.774
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=333)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `drift_60min` |x|≤ `0.1757` → IC=+0.137 (n=540)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.68€ cuando `drift_60min` |x|≤ 0.1757 (IC base=+0.097)

- **PATRÓN** `ibs_15` > `0.8929` → IC=+0.258 (n=271)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8929 (IC base=+0.097)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.356` → IC=+0.154 (n=154)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 17.356 (IC base=+0.097)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.136 (n=448)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.097)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `8.524` → IC=+0.132 (n=74)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` > 8.524 (IC base=+0.007)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0239` → IC=+0.239 (n=274)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0239 (IC base=+0.202)

- **PATRÓN** `drift_60min` |x|≤ `0.0864` → IC=+0.239 (n=362)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0864 (IC base=+0.202)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3383` → IC=+0.230 (n=724)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3383 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.202 (n=749)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.202)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.214 (n=733)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.202)

- **PATRÓN** `ibs_15` > `0.5354` → IC=+0.280 (n=822)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5354 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` > `0.1292` → IC=+0.207 (n=473)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1292 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` < `0.3267` → IC=+0.202 (n=794)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3267 (IC base=+0.202)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.889` → IC=+0.224 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.889 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `2964.7894` → IC=+0.293 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2964.7894 (IC base=+0.202)

- **PATRÓN** `ibs_15` < `0.1111` → IC=+0.158 (n=781)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.79€ cuando `ibs_15` < 0.1111 (IC base=+0.066)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` > `0.0056` → IC=+0.392 (n=211)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0056 (IC base=+0.366)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1501` → IC=+0.384 (n=420)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1501 (IC base=+0.366)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1413` → IC=+0.384 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1413 (IC base=+0.366)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.379 (n=635)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.366)

- **PATRÓN** `ibs_15` > `0.7873` → IC=+0.401 (n=631)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7873 (IC base=+0.366)

- **PATRÓN** `dist_vwap_pct` > `0.1461` → IC=+0.384 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1461 (IC base=+0.366)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.239` → IC=+0.385 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.239 (IC base=+0.366)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.370 (n=768)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.366)

- **PATRÓN** `libro_liquidez` > `3505.1277` → IC=+0.374 (n=631)

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
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.364)

- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.386 (n=138)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0058 (IC base=+0.364)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0897` → IC=+0.380 (n=272)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0897 (IC base=+0.364)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.298` → IC=+0.381 (n=242)

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

- **PATRÓN** `sigma_ewma_delta_pct` > `21.861` → IC=+0.390 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.861 (IC base=+0.364)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.368 (n=340)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.364)

- **PATRÓN** `libro_liquidez` > `3991.4206` → IC=+0.393 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3991.4206 (IC base=+0.364)

- **PATRÓN** `ballena_activa_n` < `137.0` → IC=+0.367 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 137.0 (IC base=+0.364)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0069` → IC=-0.174 (n=2165)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0069
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=2166)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.212 (n=1691)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=2640)

- **PATRÓN** `ibs_15` > `0.6324` → IC=+0.282 (n=1046)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6324 (IC base=-0.068)

- **PATRÓN** `dist_vwap_pct` > `0.1113` → IC=+0.208 (n=595)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1113 (IC base=-0.068)

- **PATRÓN** `dist_vwap_pct` < `0.2664` → IC=+0.198 (n=894)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` < 0.2664 (IC base=-0.068)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2307` → IC=+0.268 (n=1197)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2307 (IC base=-0.013)

- **PATRÓN** `ibs_15` < `0.359` → IC=+0.282 (n=3589)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.359 (IC base=-0.013)

- **PATRÓN** `dist_vwap_pct` > `0.655` → IC=+0.279 (n=455)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.655 (IC base=-0.013)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0067` → IC=-0.219 (n=631)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0067
  - _Potencial_: sin este filtro IC_bueno=-0.186 (n=1895)

- **FILTRO** `sigma_h` < `0.0039` → IC=-0.223 (n=833)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0039
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=1693)

- **FILTRO** `hora_utc` < `12.0` → IC=-0.199 (n=1172)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.190 (n=1354)

- **FILTRO** `sigma_ewma_delta_pct` > `23.14` → IC=-0.268 (n=365)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 23.14
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=2161)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.216 (n=65)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.194 (n=2461)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.120 (n=754)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.60€ cuando `sigma_h` < 0.0053 (IC base=+0.095)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2047` → IC=+0.295 (n=154)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2047 (IC base=+0.095)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1079` → IC=+0.277 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1079 (IC base=+0.095)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.135 (n=368)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 15.0 (IC base=+0.095)

- **PATRÓN** `ibs_15` > `0.7572` → IC=+0.336 (n=339)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7572 (IC base=+0.095)

- **PATRÓN** `dist_vwap_pct` > `0.1051` → IC=+0.291 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1051 (IC base=+0.095)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.545` → IC=+0.129 (n=378)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` > 8.545 (IC base=+0.095)

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

- **PATRÓN** `sigma_h` < `0.0077` → IC=+0.253 (n=1291)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0077 (IC base=+0.246)

- **PATRÓN** `drift_15min` |x|≤ `0.7675` → IC=+0.258 (n=1136)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7675 (IC base=+0.246)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2176` → IC=+0.262 (n=586)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2176 (IC base=+0.246)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.251 (n=471)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.246)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.248 (n=1154)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.246)

- **PATRÓN** `ibs_15` < `0.3695` → IC=+0.277 (n=1291)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3695 (IC base=+0.246)

- **PATRÓN** `dist_vwap_pct` > `0.2147` → IC=+0.263 (n=408)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2147 (IC base=+0.246)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.425` → IC=+0.258 (n=577)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.425 (IC base=+0.246)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `sigma_h` > `0.0105` → IC=-0.242 (n=250)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0105
  - _Potencial_: sin este filtro IC_bueno=-0.175 (n=754)

- **FILTRO** `drift_60min` |x|> `0.1729` → IC=-0.257 (n=340)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1729
  - _Potencial_: sin este filtro IC_bueno=-0.158 (n=664)

- **FILTRO** `drift_15min` |x|> `0.888` → IC=-0.282 (n=250)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.888
  - _Potencial_: sin este filtro IC_bueno=-0.161 (n=754)

- **FILTRO** `sigma_ewma_delta_pct` > `17.96` → IC=-0.146 (n=523)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 17.96
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=4153)

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
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.082 (IC base=-0.039)

- **PATRÓN** `ibs_15` < `0.3529` → IC=+0.292 (n=576)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3529 (IC base=-0.039)

- **PATRÓN** `dist_vwap_pct` < `0.4441` → IC=+0.244 (n=607)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4441 (IC base=-0.039)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0198` → IC=-0.250 (n=595)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0198
  - _Potencial_: sin este filtro IC_bueno=-0.163 (n=597)

- **FILTRO** `sigma_ewma_delta_pct` > `7.426` → IC=-0.212 (n=373)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 7.426
  - _Potencial_: sin este filtro IC_bueno=-0.204 (n=819)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.207)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.207)

- **PATRÓN** `delta_ratio_macro` |x|> `0.069` → IC=+0.273 (n=769)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.069 (IC base=-0.026)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1165` → IC=+0.295 (n=374)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1165 (IC base=-0.026)

- **PATRÓN** `ibs_15` < `0.3333` → IC=+0.292 (n=864)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3333 (IC base=-0.026)

- **PATRÓN** `dist_vwap_pct` > `0.7727` → IC=+0.350 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7727 (IC base=-0.026)

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
- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.300 (n=943)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.294)

- **PATRÓN** `drift_60min` |x|≤ `0.053` → IC=+0.322 (n=358)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.053 (IC base=+0.294)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2423` → IC=+0.311 (n=357)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2423 (IC base=+0.294)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2244` → IC=+0.309 (n=637)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2244 (IC base=+0.294)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.310 (n=1117)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.294)

- **PATRÓN** `ibs_15` > `0.8382` → IC=+0.322 (n=1071)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8382 (IC base=+0.294)

- **PATRÓN** `dist_vwap_pct` > `0.2698` → IC=+0.328 (n=457)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2698 (IC base=+0.294)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.497` → IC=+0.379 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.497 (IC base=+0.294)

- **PATRÓN** `libro_liquidez` > `12324.6448` → IC=+0.311 (n=486)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12324.6448 (IC base=+0.294)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.312 (n=253)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.290)

- **PATRÓN** `sigma_h` > `0.0046` → IC=+0.302 (n=261)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0046 (IC base=+0.290)

- **PATRÓN** `drift_60min` |x|≤ `0.0569` → IC=+0.320 (n=192)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0569 (IC base=+0.290)

- **PATRÓN** `delta_ratio_macro` |x|> `0.258` → IC=+0.314 (n=192)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.258 (IC base=+0.290)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.308 (n=575)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.290)

- **PATRÓN** `ibs_15` > `0.8279` → IC=+0.316 (n=575)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8279 (IC base=+0.290)

- **PATRÓN** `dist_vwap_pct` > `0.2546` → IC=+0.330 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2546 (IC base=+0.290)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.497` → IC=+0.384 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.497 (IC base=+0.290)

- **PATRÓN** `libro_liquidez` > `16201.6469` → IC=+0.330 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16201.6469 (IC base=+0.290)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.308 (n=497)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.297)

- **PATRÓN** `drift_60min` |x|≤ `0.0515` → IC=+0.321 (n=166)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0515 (IC base=+0.297)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0673` → IC=+0.300 (n=497)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0673 (IC base=+0.297)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2199` → IC=+0.320 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2199 (IC base=+0.297)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.311 (n=511)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.297)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.299 (n=450)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.297)

- **PATRÓN** `ibs_15` > `0.8494` → IC=+0.326 (n=497)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8494 (IC base=+0.297)

- **PATRÓN** `dist_vwap_pct` > `0.2899` → IC=+0.330 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2899 (IC base=+0.297)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.387` → IC=+0.365 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.387 (IC base=+0.297)

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

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5548 sube el IC de +0.179 a +0.254 en UPDOWN_GBM#15min (n=3597). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7176 sube el IC de +0.221 a +0.287 en UPDOWN_GBM#BTC#15min (n=612). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.5415 sube el IC de +0.147 a +0.242 en UPDOWN_GBM#ETH#15min (n=712). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.8929 sube el IC de +0.097 a +0.258 en UPDOWN_GBM#SOL#15min (n=271). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5354 sube el IC de +0.202 a +0.280 en UPDOWN_GBM#XRP#15min (n=822). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1111 sube el IC de +0.066 a +0.158 en UPDOWN_GBM#XRP#15min (n=781). Ya aplicado como kelly_boost=+0.79€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6324 sube el IC de -0.068 a +0.282 en UPDOWN_GBM_15M_TARDIO (n=1046). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.359 sube el IC de -0.013 a +0.282 en UPDOWN_GBM_15M_TARDIO (n=3589). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7572 sube el IC de +0.095 a +0.336 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=339). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.618 sube el IC de -0.195 a +0.290 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=60). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.5959 sube el IC de +0.150 a +0.248 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=525). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3695 sube el IC de +0.246 a +0.277 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=1291). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de -0.192 a +0.234 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=62). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3529 sube el IC de -0.039 a +0.292 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=576). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.207 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3333 sube el IC de -0.026 a +0.292 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=864). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_YES, IBS > 0.8434 sube el IC de +0.062 a +0.333 en UPDOWN_GBM_ETH_15M_HORA7 (n=16). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_YES, IBS > 0.8434 sube el IC de +0.062 a +0.333 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=16). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8382 sube el IC de +0.294 a +0.322 en UPDOWN_GBM_IBS_ALTO (n=1071). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8279 sube el IC de +0.290 a +0.316 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=575). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8494 sube el IC de +0.297 a +0.326 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=497). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7873 sube el IC de +0.366 a +0.401 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=631). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8066 sube el IC de +0.366 a +0.391 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=328). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7479 sube el IC de +0.364 a +0.411 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=303). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

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
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 644 | +0.002 | +78.57€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 644 | +0.002 | +78.57€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 468 | -0.023 | +45.74€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 468 | -0.023 | +45.74€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 137 | +0.075 | +24.72€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 137 | +0.075 | +24.72€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 36 | +0.026 | +4.76€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 36 | +0.026 | +4.76€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 40123 | -0.083 | -5050.82€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 2204 | +0.032 | -257.78€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 37919 | -0.089 | -4793.05€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4488 | -0.116 | -775.98€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4488 | -0.116 | -775.98€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 2204 | +0.032 | -257.78€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 2204 | +0.032 | -257.78€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 4317 | -0.105 | -875.34€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 4317 | -0.105 | -875.34€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 10700 | -0.022 | -1003.74€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 10700 | -0.022 | -1003.74€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 10579 | -0.105 | -815.48€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 10579 | -0.105 | -815.48€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 7835 | -0.134 | -1322.50€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 7835 | -0.134 | -1322.50€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 35084 | -0.015 | +3343.94€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 9078 | +0.004 | +1670.00€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 26006 | -0.022 | +1673.95€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 35084 | -0.015 | +3343.94€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 9078 | +0.004 | +1670.00€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 26006 | -0.022 | +1673.95€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 145325 | +0.116 | -5775.07€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 18626 | +0.182 | -565.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 639 | -0.016 | -68.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 117354 | +0.107 | -4811.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 8706 | +0.100 | -330.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 19462 | +0.108 | -1176.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 61 | -0.151 | +10.95€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 19386 | +0.109 | -1176.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 28148 | +0.129 | -392.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5199 | +0.188 | -177.45€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 19448 | +0.121 | -88.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 3459 | +0.083 | -104.57€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 19515 | +0.100 | -1351.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 74 | -0.118 | -5.77€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 19426 | +0.101 | -1334.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 30901 | +0.125 | -548.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 7993 | +0.178 | -142.52€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 19707 | +0.108 | -345.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 3189 | +0.100 | -52.08€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 27817 | +0.116 | -1384.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 5231 | +0.196 | -256.69€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 542 | +0.017 | -14.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 19986 | +0.096 | -940.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 2058 | +0.130 | -173.42€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#XRP | 19482 | +0.106 | -921.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 68 | -0.086 | +5.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 19401 | +0.107 | -926.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 23363 | +0.197 | -1403.18€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 23363 | +0.197 | -1403.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 5318 | +0.180 | -446.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 5318 | +0.180 | -446.75€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 2965 | +0.203 | -66.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 2965 | +0.203 | -66.00€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 5258 | +0.181 | -418.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 5258 | +0.181 | -418.72€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 4559 | +0.248 | -150.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 4559 | +0.248 | -150.23€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 5184 | +0.188 | -335.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 5184 | +0.188 | -335.24€ | 0 | 3 |
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
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 81721 | +0.202 | -5805.75€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 81721 | +0.202 | -5805.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 14039 | +0.185 | -1442.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 14039 | +0.185 | -1442.76€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 13198 | +0.225 | -448.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 13198 | +0.225 | -448.01€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 13994 | +0.182 | -1458.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 13994 | +0.182 | -1458.53€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 13274 | +0.221 | -483.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 13274 | +0.221 | -483.34€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 13559 | +0.202 | -883.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 13559 | +0.202 | -883.05€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 13657 | +0.197 | -1090.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 13657 | +0.197 | -1090.06€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 31288 | +0.117 | +209.80€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 31288 | +0.117 | +209.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 15553 | +0.119 | +174.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 15553 | +0.119 | +174.00€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 15735 | +0.114 | +35.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 15735 | +0.114 | +35.80€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 2079 | +0.292 | -8.23€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 2079 | +0.292 | -8.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 952 | +0.279 | -27.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 952 | +0.279 | -27.03€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 1008 | +0.297 | +13.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 1008 | +0.297 | +13.49€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 119 | +0.351 | +5.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 119 | +0.351 | +5.31€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 956 | +0.442 | +4.26€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 956 | +0.442 | +4.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 463 | +0.435 | -4.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 463 | +0.435 | -4.68€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 447 | +0.449 | +8.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 447 | +0.449 | +8.39€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 46 | +0.396 | +0.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 46 | +0.396 | +0.55€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1648 | +0.071 | -64.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 637 | +0.052 | -51.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 1011 | +0.083 | -13.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 74 | +0.118 | +4.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 74 | +0.118 | +4.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1266 | +0.080 | -25.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 255 | +0.064 | -11.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 1011 | +0.083 | -13.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 308 | +0.026 | -43.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 308 | +0.026 | -43.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 61777 | +0.101 | -1553.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 4996 | +0.091 | +52.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 56781 | +0.101 | -1606.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 33989 | +0.106 | -374.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 4996 | +0.091 | +52.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 28993 | +0.108 | -427.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 12694 | +0.109 | -66.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 12694 | +0.109 | -66.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 15094 | +0.082 | -1112.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 15094 | +0.082 | -1112.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 897 | +0.193 | -109.11€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 897 | +0.193 | -109.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 897 | +0.193 | -109.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 897 | +0.193 | -109.11€ | 2 | 4 |
| ✅ GBM_LATE_15M | 42482 | +0.095 | +22247.85€ | 0 | 19 |
| ✅ GBM_LATE_15M#15min | 42482 | +0.095 | +22247.85€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 7077 | +0.217 | +5845.12€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 7077 | +0.217 | +5845.12€ | 0 | 23 |
| ✅ GBM_LATE_15M#BTC | 6363 | +0.180 | +4873.61€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 6363 | +0.180 | +4873.61€ | 0 | 24 |
| ✅ GBM_LATE_15M#DOGE | 7593 | +0.206 | +5924.76€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 7593 | +0.206 | +5924.76€ | 0 | 20 |
| ✅ GBM_LATE_15M#ETH | 5931 | +0.042 | +1669.51€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 5931 | +0.042 | +1669.51€ | 1 | 19 |
| ✅ GBM_LATE_15M#SOL | 5984 | -0.032 | +1262.05€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 5984 | -0.032 | +1262.05€ | 4 | 13 |
| ✅ GBM_LATE_15M#XRP | 9534 | -0.030 | +2672.80€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 9534 | -0.030 | +2672.80€ | 4 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 45696 | +0.085 | +24862.87€ | 0 | 18 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 45696 | +0.085 | +24862.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 8831 | +0.004 | +4447.31€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 8831 | +0.004 | +4447.31€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 9672 | +0.009 | +2285.50€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 9672 | +0.009 | +2285.50€ | 0 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 6334 | +0.279 | +6817.33€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 6334 | +0.279 | +6817.33€ | 0 | 22 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 8238 | +0.013 | +2043.42€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 8238 | +0.013 | +2043.42€ | 1 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 7286 | +0.039 | +3004.88€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 7286 | +0.039 | +3004.88€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 5335 | +0.303 | +6264.43€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 5335 | +0.303 | +6264.43€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 33697 | +0.180 | +27338.26€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 33697 | +0.180 | +27338.26€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 5108 | +0.231 | +4560.97€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 5108 | +0.231 | +4560.97€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 5308 | +0.149 | +3932.68€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 5308 | +0.149 | +3932.68€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 5396 | +0.224 | +4655.34€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 5396 | +0.224 | +4655.34€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 5716 | +0.139 | +4361.97€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 5716 | +0.139 | +4361.97€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 6336 | +0.124 | +4723.89€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 6336 | +0.124 | +4723.89€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 5833 | +0.225 | +5103.41€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 5833 | +0.225 | +5103.41€ | 0 | 24 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 9131 | +0.134 | +4469.23€ | 0 | 18 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 9131 | +0.134 | +4469.23€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 405 | +0.154 | +252.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 405 | +0.154 | +252.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 2703 | +0.145 | +1549.92€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 2703 | +0.145 | +1549.92€ | 0 | 21 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 444 | +0.148 | +222.18€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 444 | +0.148 | +222.18€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 2695 | +0.138 | +1284.99€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 2695 | +0.138 | +1284.99€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 2258 | +0.108 | +875.64€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 2258 | +0.108 | +875.64€ | 0 | 16 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 626 | +0.134 | +283.67€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 626 | +0.134 | +283.67€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO | 42655 | +0.185 | +34169.54€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#15min | 42655 | +0.185 | +34169.54€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 6754 | +0.242 | +6316.00€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 6754 | +0.242 | +6316.00€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 6640 | +0.147 | +4540.03€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 6640 | +0.147 | +4540.03€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 7212 | +0.233 | +6457.47€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 7212 | +0.233 | +6457.47€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 7042 | +0.139 | +5031.41€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 7042 | +0.139 | +5031.41€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 7557 | +0.121 | +5228.48€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 7557 | +0.121 | +5228.48€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 7450 | +0.230 | +6596.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 7450 | +0.230 | +6596.16€ | 0 | 19 |
| ✅ GBM_LATE_5M | 11707 | +0.202 | +9101.78€ | 1 | 29 |
| ✅ GBM_LATE_5M#5min | 11707 | +0.202 | +9101.78€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 984 | +0.242 | +916.10€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 984 | +0.242 | +916.10€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 2778 | +0.208 | +2391.40€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 2778 | +0.208 | +2391.40€ | 0 | 25 |
| ✅ GBM_LATE_5M#DOGE | 1110 | +0.193 | +808.37€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1110 | +0.193 | +808.37€ | 0 | 19 |
| ✅ GBM_LATE_5M#ETH | 3338 | +0.193 | +2345.42€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 3338 | +0.193 | +2345.42€ | 0 | 28 |
| ✅ GBM_LATE_5M#SOL | 1707 | +0.191 | +1291.25€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 1707 | +0.191 | +1291.25€ | 0 | 26 |
| ✅ GBM_LATE_5M#XRP | 1790 | +0.202 | +1349.23€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1790 | +0.202 | +1349.23€ | 0 | 0 |
| ✅ GBM_LATE_60M | 3491 | +0.065 | +1143.24€ | 0 | 8 |
| ✅ GBM_LATE_60M#60min | 3491 | +0.065 | +1143.24€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 1281 | +0.081 | +474.96€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 1281 | +0.081 | +474.96€ | 0 | 6 |
| ✅ GBM_LATE_60M#ETH | 1127 | +0.066 | +385.90€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 1127 | +0.066 | +385.90€ | 1 | 9 |
| ✅ GBM_LATE_60M#SOL | 1083 | +0.045 | +282.38€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 1083 | +0.045 | +282.38€ | 0 | 13 |
| 🚫 GBM_LATE_60M_FADE | 573 | -0.244 | -22.02€ | 8 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 573 | -0.244 | -22.02€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 213 | -0.249 | -15.57€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 213 | -0.249 | -15.57€ | 5 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 205 | -0.225 | +0.05€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 205 | -0.225 | +0.05€ | 7 | 1 |
| 🚫 GBM_LATE_60M_FADE#SOL | 155 | -0.258 | -6.50€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 155 | -0.258 | -6.50€ | 5 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 1518 | +0.082 | +381.19€ | 1 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 1518 | +0.082 | +381.19€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 595 | +0.080 | +141.96€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 595 | +0.080 | +141.96€ | 1 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 544 | +0.055 | +78.03€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 544 | +0.055 | +78.03€ | 2 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 379 | +0.125 | +161.20€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 379 | +0.125 | +161.20€ | 3 | 10 |
| ✅ LATE_WINDOW_5MIN | 165 | +0.278 | +162.71€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 165 | +0.278 | +162.71€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 165 | +0.278 | +162.71€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 165 | +0.278 | +162.71€ | 1 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 3406 | +0.101 | +841.16€ | 0 | 1 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 3406 | +0.101 | +841.16€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 3406 | +0.101 | +841.16€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 3406 | +0.101 | +841.16€ | 0 | 1 |
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
| ✅ LIQUIDACIONES_5M | 3733 | +0.015 | +77.92€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 3733 | +0.015 | +77.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 181 | +0.019 | -2.82€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 181 | +0.019 | -2.82€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 794 | +0.007 | +29.41€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 794 | +0.007 | +29.41€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE | 207 | -0.012 | -4.18€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 207 | -0.012 | -4.18€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 1347 | +0.024 | +29.42€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1347 | +0.024 | +29.42€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 756 | +0.012 | +1.99€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 756 | +0.012 | +1.99€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 448 | +0.013 | +24.10€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 448 | +0.013 | +24.10€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 1757 | -0.039 | -26.37€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1757 | -0.039 | -26.37€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 506 | -0.029 | -11.10€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 506 | -0.029 | -11.10€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 599 | -0.014 | +6.40€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 599 | -0.014 | +6.40€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 652 | -0.069 | -21.67€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 652 | -0.069 | -21.67€ | 6 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 8728 | -0.028 | -10.53€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 4136 | -0.037 | -90.50€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 4592 | -0.019 | +79.97€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 264 | -0.038 | -9.28€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 135 | -0.025 | -1.89€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 129 | -0.050 | -7.39€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 2175 | -0.020 | +12.65€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 1036 | -0.024 | -3.21€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 1139 | -0.016 | +15.87€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 959 | -0.025 | +9.86€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 478 | -0.044 | -14.59€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 481 | -0.007 | +24.45€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 1903 | -0.042 | -66.35€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 883 | -0.054 | -57.44€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 1020 | -0.032 | -8.92€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 1709 | -0.021 | +23.56€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 813 | -0.034 | -9.33€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 896 | -0.010 | +32.89€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 1718 | -0.028 | +19.03€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 791 | -0.037 | -4.04€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 927 | -0.020 | +23.07€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 49885 | -0.001 | +2464.54€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 49885 | -0.001 | +2464.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 8988 | +0.026 | +1141.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 8988 | +0.026 | +1141.60€ | 2 | 5 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 7181 | -0.034 | -98.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 7181 | -0.034 | -98.71€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 9101 | +0.024 | +940.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 9101 | +0.024 | +940.93€ | 2 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 7029 | -0.048 | -152.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 7029 | -0.048 | -152.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 8436 | -0.005 | +230.41€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 8436 | -0.005 | +230.41€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 9150 | +0.015 | +402.68€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 9150 | +0.015 | +402.68€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 6636 | -0.059 | -162.70€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 6636 | -0.059 | -162.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1225 | -0.000 | -15.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1225 | -0.000 | -15.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1732 | -0.079 | -46.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1732 | -0.079 | -46.27€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 55 | -0.061 | -2.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 55 | -0.061 | -2.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 774 | -0.120 | -33.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 774 | -0.120 | -33.46€ | 6 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1993 | -0.074 | -39.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1993 | -0.074 | -39.26€ | 3 | 0 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 123709 | -0.076 | +1585.05€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 123709 | -0.076 | +1585.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 21510 | -0.077 | +1076.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 21510 | -0.077 | +1076.52€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 18635 | -0.101 | -1030.18€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 18635 | -0.101 | -1030.18€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 21813 | -0.068 | +1182.68€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 21813 | -0.068 | +1182.68€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 18179 | -0.097 | -637.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 18179 | -0.097 | -637.21€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 22153 | -0.057 | +311.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 22153 | -0.057 | +311.87€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 21419 | -0.067 | +681.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 21419 | -0.067 | +681.36€ | 4 | 0 |
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
| ✅ ORDER_FLOW_5M_REACTIVO | 1457 | -0.015 | -18.40€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 1457 | -0.015 | -18.40€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 283 | -0.002 | +8.79€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 283 | -0.002 | +8.79€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 250 | -0.016 | -0.49€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 250 | -0.016 | -0.49€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 379 | -0.046 | -31.54€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 379 | -0.046 | -31.54€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 311 | +0.008 | +3.23€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 311 | +0.008 | +3.23€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 234 | -0.009 | +1.59€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 234 | -0.009 | +1.59€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 900 | -0.069 | -41.12€ | 3 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 420 | -0.109 | -76.71€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 324 | -0.138 | -64.11€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 96 | -0.010 | -12.59€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 318 | -0.028 | +26.47€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 227 | -0.015 | +28.93€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 91 | -0.059 | -2.46€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 162 | -0.043 | +9.12€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 131 | -0.049 | +4.73€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 31 | -0.015 | +4.39€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 682 | -0.080 | -30.45€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 218 | -0.032 | -10.67€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 1125 | -0.207 | -69.66€ | 5 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC | 438 | -0.209 | -41.88€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#atexpiry | 381 | -0.213 | -41.65€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 57 | -0.178 | -0.23€ | 2 | 0 |
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
| ✅ STREAK_MOM_5M | 10878 | +0.016 | +86.18€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 10878 | +0.016 | +86.18€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2779 | +0.020 | +28.27€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2779 | +0.020 | +28.27€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2836 | +0.019 | +36.58€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2836 | +0.019 | +36.58€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2888 | +0.009 | -0.95€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2888 | +0.009 | -0.95€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2375 | +0.016 | +22.29€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2375 | +0.016 | +22.29€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 9877 | +0.013 | -48.44€ | 2 | 0 |
| ✅ STRUCT_NO_15M#15min | 9877 | +0.013 | -48.44€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 4018 | +0.018 | -7.65€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 4018 | +0.018 | -7.65€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3616 | +0.011 | -27.14€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3616 | +0.011 | -27.14€ | 2 | 0 |
| ✅ STRUCT_NO_15M#SOL | 2243 | +0.009 | -13.65€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 2243 | +0.009 | -13.65€ | 1 | 0 |
| ✅ UPDOWN_GBM | 76786 | +0.054 | +6807.50€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 19087 | +0.083 | +4204.01€ | 0 | 11 |
| ✅ UPDOWN_GBM#240min | 2463 | +0.003 | +22.33€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 50444 | +0.050 | +2497.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 4526 | +0.006 | +84.41€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 6851 | +0.089 | +1075.72€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1576 | +0.156 | +698.08€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 77 | -0.006 | -0.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 5198 | +0.070 | +378.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 16529 | +0.056 | +1423.08€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 2469 | +0.090 | +605.51€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 662 | +0.009 | +10.16€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 11286 | +0.061 | +744.97€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 2016 | +0.003 | +59.47€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 96 | -0.071 | +2.97€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 8451 | +0.069 | +897.17€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1555 | +0.147 | +610.96€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 78 | +0.013 | -1.79€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 6818 | +0.052 | +288.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 17627 | +0.045 | +1154.61€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 4521 | +0.066 | +669.97€ | 0 | 10 |
| ✅ UPDOWN_GBM#ETH#240min | 645 | +0.005 | +15.29€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 10787 | +0.044 | +448.93€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 1585 | +0.011 | +17.65€ | 1 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 89 | -0.104 | +2.77€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 16852 | +0.033 | +835.52€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 4777 | +0.035 | +403.14€ | 0 | 4 |
| ✅ UPDOWN_GBM#SOL#240min | 613 | -0.009 | -0.43€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 10458 | +0.037 | +430.16€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 925 | +0.005 | +7.29€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 79 | -0.130 | -4.65€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 10474 | +0.064 | +1423.24€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 4189 | +0.102 | +1216.35€ | 0 | 11 |
| ✅ UPDOWN_GBM#XRP#240min | 388 | +0.010 | -0.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 5897 | +0.040 | +206.95€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 264 | -0.102 | +1.10€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 841 | +0.366 | +312.33€ | 0 | 9 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 841 | +0.366 | +312.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 437 | +0.366 | +154.77€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 437 | +0.366 | +154.77€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 404 | +0.364 | +157.56€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 404 | +0.364 | +157.56€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO | 19869 | -0.025 | +4653.73€ | 2 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 19869 | -0.025 | +4653.73€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1718 | -0.056 | +502.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1718 | -0.056 | +502.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 3530 | -0.112 | +130.48€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 3530 | -0.112 | +130.48€ | 5 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 948 | +0.216 | +770.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 948 | +0.216 | +770.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 2420 | +0.219 | +1594.76€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 2420 | +0.219 | +1594.76€ | 1 | 20 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 5680 | -0.066 | +665.91€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 5680 | -0.066 | +665.91€ | 4 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 5573 | -0.065 | +989.32€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 5573 | -0.065 | +989.32€ | 2 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 232 | +0.047 | +11.12€ | 0 | 2 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 232 | +0.047 | +11.12€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 232 | +0.047 | +11.12€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 232 | +0.047 | +11.12€ | 0 | 2 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1428 | +0.294 | +1234.46€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1428 | +0.294 | +1234.46€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 766 | +0.290 | +623.50€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 766 | +0.290 | +623.50€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 662 | +0.297 | +610.96€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 662 | +0.297 | +610.96€ | 0 | 9 |
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