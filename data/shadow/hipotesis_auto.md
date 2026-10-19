# Hipótesis automáticas — 2026-10-19 12:46 UTC
_Generado por shadow_postmortem.py sobre 965547 resoluciones (PNL=+125332.30€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **PATRÓN** `py_entrada` > `0.705` → IC=+0.274 (n=550)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.705 (IC base=+0.138)

- **PATRÓN** `n_total_lado` > `66.0` → IC=+0.182 (n=278)

  - _Acción_: Kelly boost +0.91€ cuando `n_total_lado` > 66.0 (IC base=+0.138)

- **PATRÓN** `banda_hit_calibrado` > `0.8012` → IC=+0.272 (n=550)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8012 (IC base=+0.138)

- **PATRÓN** `banda_z` > `9.212` → IC=+0.204 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.212 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.171 (n=302)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.138)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.154 (n=897)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `98.0` → IC=+0.153 (n=447)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 98.0 (IC base=+0.138)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **PATRÓN** `py_entrada` > `0.55` → IC=+0.271 (n=465)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.55 (IC base=+0.144)

- **PATRÓN** `n_total_lado` > `47.0` → IC=+0.184 (n=464)

  - _Acción_: Kelly boost +0.92€ cuando `n_total_lado` > 47.0 (IC base=+0.144)

- **PATRÓN** `banda_hit_calibrado` > `0.6183` → IC=+0.266 (n=464)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6183 (IC base=+0.144)

- **PATRÓN** `banda_z` > `9.644` → IC=+0.209 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.644 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.184 (n=251)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 17.0 (IC base=+0.144)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.151 (n=798)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `101.0` → IC=+0.154 (n=417)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 101.0 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `9770.2045` → IC=+0.131 (n=204)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 9770.2045 (IC base=+0.017)

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
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=105)

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
- **PATRÓN** `n_ballena_banda` > `30.0` → IC=+0.265 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `n_ballena_banda` > 30.0 (IC base=+0.143)

- **PATRÓN** `n_total_lado` > `43.0` → IC=+0.324 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 43.0 (IC base=+0.143)

- **PATRÓN** `banda_z` > `2.517` → IC=+0.244 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 2.517 (IC base=+0.143)

- **PATRÓN** `ballenas_wallet_edge_medio` > `0.719` → IC=+0.149 (n=35)

  - _Acción_: Kelly boost +0.74€ cuando `ballenas_wallet_edge_medio` > 0.719 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.210 (n=29)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.143)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.200 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `2466.3517` → IC=+0.192 (n=37)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 2466.3517 (IC base=+0.143)

### BALLENAS_TARDIAS
- **FILTRO** `restante_s_al_confirmar` < `142.37` → IC=-0.207 (n=9941)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 142.37
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=29829)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `128.98` → IC=-0.263 (n=1120)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 128.98
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=3360)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `121.52` → IC=-0.288 (n=1078)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 121.52
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=3235)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `167.27` → IC=-0.208 (n=2621)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 167.27
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=7866)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `133.16` → IC=-0.279 (n=1935)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 133.16
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=5807)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.213 (n=21335)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.107)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.136 (n=4285)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `9160.5319` → IC=+0.178 (n=1931)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 9160.5319 (IC base=+0.107)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.130 (n=18030)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.129 (n=32612)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 11.0 (IC base=+0.125)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.227 (n=16848)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.151 (n=7132)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.01 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `7120.6252` → IC=+0.158 (n=2756)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 7120.6252 (IC base=+0.125)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.200 (n=2014)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.194 (n=1970)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 17.0 (IC base=+0.193)

- **PATRÓN** `py_entrada` > `0.775` → IC=+0.364 (n=644)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.775 (IC base=+0.193)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.196 (n=2471)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.01 (IC base=+0.193)

- **PATRÓN** `libro_liquidez` > `16325.2152` → IC=+0.201 (n=641)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16325.2152 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.190 (n=1773)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 7.0 (IC base=+0.184)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.188 (n=1975)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 17.0 (IC base=+0.184)

- **PATRÓN** `py_entrada` < `0.245` → IC=+0.340 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.245 (IC base=+0.184)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.186 (n=2532)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.01 (IC base=+0.184)

- **PATRÓN** `libro_liquidez` > `16125.479` → IC=+0.195 (n=653)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 16125.479 (IC base=+0.184)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.61` → IC=+0.167 (n=466)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` > 0.61 (IC base=+0.081)

- **PATRÓN** `libro_liquidez` > `6857.6712` → IC=+0.164 (n=123)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 6857.6712 (IC base=+0.081)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.140 (n=1103)

  - _Acción_: Kelly boost +0.70€ cuando `py_entrada` < 0.44 (IC base=+0.086)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.168 (n=4142)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.160)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.161 (n=2837)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 12.0 (IC base=+0.160)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.371 (n=1351)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.160)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.221 (n=1837)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.213)

- **PATRÓN** `py_entrada` < `0.26` → IC=+0.360 (n=669)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.26 (IC base=+0.213)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.217 (n=2154)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.213)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.145 (n=1041)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.142)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.149 (n=681)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 11.0 (IC base=+0.142)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.264 (n=337)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.142)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.142 (n=820)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `1879.5451` → IC=+0.155 (n=664)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 1879.5451 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.162 (n=152)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.069)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.246 (n=967)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.222)

- **PATRÓN** `py_entrada` > `0.825` → IC=+0.418 (n=1127)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.825 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.150 (n=1286)
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

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.135 (n=1127)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 7.0 (IC base=+0.124)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.253 (n=406)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.124)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `11.0` → IC=-0.297 (n=62)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=148)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.206 (n=17995)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.201)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.202 (n=15292)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.201)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.234 (n=7431)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.201)

- **PATRÓN** `libro_liquidez` > `4837.3339` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4837.3339 (IC base=+0.201)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.179 (n=4154)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 5.0 (IC base=+0.178)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.181 (n=3494)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 15.0 (IC base=+0.178)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.182 (n=4051)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` < 0.73 (IC base=+0.178)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.179 (n=3397)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` > 0.71 (IC base=+0.178)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.380 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.247 (n=89)

- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=90)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.224 (n=2099)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.223)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.231 (n=1409)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.223)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.308 (n=739)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.223)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.189 (n=4083)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.184 (n=3477)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 15.0 (IC base=+0.182)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.188 (n=3203)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` > 0.71 (IC base=+0.182)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.257 (n=3546)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.248)

- **PATRÓN** `py_entrada` > `0.79` → IC=+0.361 (n=1131)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.193 (n=4007)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 5.0 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.192 (n=2572)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 11.0 (IC base=+0.188)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.193 (n=2955)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.71 (IC base=+0.188)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.432 (n=767)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.428)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.441 (n=796)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.428)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.432 (n=811)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.428)

- **PATRÓN** `libro_liquidez` > `13089.4142` → IC=+0.445 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13089.4142 (IC base=+0.428)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` < `7.0` → IC=+0.451 (n=140)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.437)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.449 (n=331)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.437)

- **PATRÓN** `libro_liquidez` > `15539.3062` → IC=+0.440 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15539.3062 (IC base=+0.437)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.448 (n=208)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.432)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.443 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.432)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.435 (n=337)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.432)

- **PATRÓN** `libro_liquidez` > `4389.547` → IC=+0.441 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4389.547 (IC base=+0.432)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.408 (n=139)
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

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.208 (n=23274)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.202)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.247 (n=23553)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.202)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.187 (n=10930)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.185)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.188 (n=7476)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 12.0 (IC base=+0.185)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.200 (n=10452)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.71 (IC base=+0.185)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.227 (n=4857)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.226 (n=4801)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.224)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.285 (n=3422)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.224)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.191 (n=3982)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 17.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.211 (n=5323)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.181)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.835` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.835
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.231 (n=4894)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.222 (n=3750)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.222)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.278 (n=3324)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.222)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.204 (n=9487)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.261 (n=3467)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.208 (n=3869)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.199 (n=3919)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 6.0 (IC base=+0.197)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.248 (n=4055)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.197)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.191 (n=8455)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.139 (n=8298)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.123 (n=10267)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` < 7.0 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `3.79` → IC=+0.135 (n=10168)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 3.79 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.194 (n=4182)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.120)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.143 (n=4222)

  - _Acción_: Kelly boost +0.71€ cuando `restante_min` > 4.95 (IC base=+0.120)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.130 (n=5097)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.120)

- **PATRÓN** `lag_apertura_s` < `2.78` → IC=+0.146 (n=3829)

  - _Acción_: Kelly boost +0.73€ cuando `lag_apertura_s` < 2.78 (IC base=+0.120)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.188 (n=4273)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` < 0.38 (IC base=+0.114)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.134 (n=4527)

  - _Acción_: Kelly boost +0.67€ cuando `restante_min` > 4.96 (IC base=+0.114)

- **PATRÓN** `lag_apertura_s` < `3.33` → IC=+0.133 (n=5113)

  - _Acción_: Kelly boost +0.66€ cuando `lag_apertura_s` < 3.33 (IC base=+0.114)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.300 (n=1631)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.292)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.293 (n=1613)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.292)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.381 (n=567)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.292)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.286 (n=740)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.278)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.278 (n=637)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.278)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.354 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.278)

- **PATRÓN** `libro_liquidez` > `5416.3978` → IC=+0.289 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5416.3978 (IC base=+0.278)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.323 (n=523)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.297)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.301 (n=776)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.297)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.391 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.297)

- **PATRÓN** `libro_liquidez` > `2112.3487` → IC=+0.313 (n=249)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.445 (n=755)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.441)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.441 (n=748)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.441)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.445 (n=521)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.441)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.437 (n=361)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.435)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.440 (n=247)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.435)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.436 (n=372)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.435)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.441 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.435)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.452 (n=354)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.448)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.451 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.448)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.450 (n=320)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.448)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.449 (n=392)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.448)

- **PATRÓN** `libro_liquidez` > `1966.3827` → IC=+0.461 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1966.3827 (IC base=+0.448)

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

- **FILTRO** `hora_utc` > `15.0` → IC=-0.340 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.199 (n=91)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.250 (n=58)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.207 (n=56)

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

- **FILTRO** `hora_utc` > `15.0` → IC=-0.340 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.199 (n=91)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.250 (n=58)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.207 (n=56)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4779` → IC=+0.137 (n=13068)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.4779 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.123 (n=13207)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 6.0 (IC base=+0.120)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.124 (n=9162)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 12.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` > `0.9809` → IC=+0.248 (n=4356)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9809 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` > `0.7844` → IC=+0.266 (n=725)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7844 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` < `0.3683` → IC=+0.258 (n=3656)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3683 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.689` → IC=+0.181 (n=6484)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 3.689 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` < `1.2014` → IC=+0.257 (n=3784)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2014 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` > `0.6189` → IC=+0.263 (n=3784)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6189 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` > `0.3022` → IC=+0.239 (n=1327)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3022 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` > `2.3421` → IC=+0.227 (n=4210)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3421 (IC base=+0.120)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.121 (n=16083)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.04 (IC base=+0.120)

- **PATRÓN** `ibs_20min` < `0.6857` → IC=+0.129 (n=18287)

  - _Acción_: Kelly boost +0.64€ cuando `ibs_20min` < 0.6857 (IC base=+0.075)

- **PATRÓN** `dist_vwap_pct` < `0.152` → IC=+0.186 (n=5890)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` < 0.152 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` < `0.6964` → IC=+0.183 (n=2750)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 0.6964 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` > `1.0507` → IC=+0.180 (n=2835)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` > 1.0507 (IC base=+0.075)

- **PATRÓN** `volumen_pendiente_norm` > `0.2954` → IC=+0.232 (n=1563)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2954 (IC base=+0.075)

- **PATRÓN** `volumen_spike_ratio` > `2.6775` → IC=+0.207 (n=3542)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6775 (IC base=+0.075)

- **PATRÓN** `ballena_activa_n` < `106.0` → IC=+0.220 (n=10481)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 106.0 (IC base=+0.075)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.215 (n=952)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.197)

- **PATRÓN** `drift_60min` |x|≤ `0.3479` → IC=+0.201 (n=2847)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3479 (IC base=+0.197)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.206 (n=1378)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.203 (n=1914)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.197)

- **PATRÓN** `ibs_20min` > `0.9789` → IC=+0.278 (n=1291)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9789 (IC base=+0.197)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.948` → IC=+0.281 (n=1246)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.948 (IC base=+0.197)

- **PATRÓN** `volumen_pendiente_norm` > `0.2318` → IC=+0.245 (n=501)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2318 (IC base=+0.197)

- **PATRÓN** `volumen_spike_ratio` > `2.2767` → IC=+0.208 (n=1229)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2767 (IC base=+0.197)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.211 (n=3037)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.197)

- **PATRÓN** `libro_liquidez` > `2082.52` → IC=+0.207 (n=949)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2082.52 (IC base=+0.197)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.213 (n=1686)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 14.0 (IC base=+0.197)

- **PATRÓN** `sigma_h` < `0.0085` → IC=+0.239 (n=2383)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0085 (IC base=+0.237)

- **PATRÓN** `sigma_h` > `0.0076` → IC=+0.238 (n=1081)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0076 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.0873` → IC=+0.272 (n=799)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0873 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.254 (n=869)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` < `0.5254` → IC=+0.259 (n=2384)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5254 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` < `0.0937` → IC=+0.239 (n=2131)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0937 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.2861` → IC=+0.254 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2861 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` < `1.437` → IC=+0.241 (n=748)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.437 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `2.6474` → IC=+0.245 (n=748)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6474 (IC base=+0.237)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.240 (n=2669)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.237)

- **PATRÓN** `libro_liquidez` > `1656.86` → IC=+0.245 (n=2128)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1656.86 (IC base=+0.237)

- **PATRÓN** `ballena_activa_n` < `7.0` → IC=+0.241 (n=787)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 7.0 (IC base=+0.237)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.238 (n=1025)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.227)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.230 (n=1059)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.227)

- **PATRÓN** `drift_60min` |x|≤ `0.1061` → IC=+0.260 (n=1025)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1061 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.238 (n=2444)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.227)

- **PATRÓN** `ibs_20min` > `0.9523` → IC=+0.277 (n=777)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9523 (IC base=+0.227)

- **PATRÓN** `dist_vwap_pct` > `0.1279` → IC=+0.234 (n=1262)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1279 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.408` → IC=+0.268 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.408 (IC base=+0.227)

- **PATRÓN** `volumen_regimen` < `1.2292` → IC=+0.230 (n=2329)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2292 (IC base=+0.227)

- **PATRÓN** `volumen_regimen` > `0.6219` → IC=+0.232 (n=2329)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6219 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` > `0.2776` → IC=+0.259 (n=330)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2776 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` < `1.5126` → IC=+0.229 (n=1010)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5126 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` > `2.4426` → IC=+0.252 (n=765)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4426 (IC base=+0.227)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.152 (n=2366)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0057 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.0749` → IC=+0.168 (n=788)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.0749 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.154 (n=892)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 17.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` < `0.7291` → IC=+0.177 (n=2364)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.7291 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.063` → IC=+0.149 (n=383)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 11.063 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.196` → IC=+0.141 (n=2160)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 4.196 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `1.2032` → IC=+0.141 (n=2364)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 1.2032 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` > `0.0973` → IC=+0.160 (n=863)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.0973 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` < `2.4565` → IC=+0.142 (n=2244)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.4565 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` > `1.415` → IC=+0.136 (n=2244)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.415 (IC base=+0.133)

- **PATRÓN** `ballena_activa_n` < `218.0` → IC=+0.174 (n=955)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 218.0 (IC base=+0.133)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0121` → IC=+0.218 (n=987)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0121 (IC base=+0.195)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.200 (n=3105)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.195)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.195 (n=2650)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 15.0 (IC base=+0.195)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.271 (n=1130)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.195)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.269` → IC=+0.274 (n=621)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.269 (IC base=+0.195)

- **PATRÓN** `volumen_pendiente_norm` < `0.0975` → IC=+0.200 (n=2619)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0975 (IC base=+0.195)

- **PATRÓN** `volumen_pendiente_norm` > `0.3519` → IC=+0.209 (n=383)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3519 (IC base=+0.195)

- **PATRÓN** `volumen_spike_ratio` > `2.6967` → IC=+0.211 (n=1301)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6967 (IC base=+0.195)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.202 (n=3531)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.195)

- **PATRÓN** `libro_liquidez` > `1979.26` → IC=+0.201 (n=1342)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1979.26 (IC base=+0.195)

- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.224 (n=2329)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0106 (IC base=+0.217)

- **PATRÓN** `drift_60min` |x|≤ `0.6047` → IC=+0.222 (n=2644)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6047 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.242 (n=986)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.217)

- **PATRÓN** `ibs_20min` < `0.0159` → IC=+0.275 (n=882)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0159 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.43` → IC=+0.245 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.43 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` > `0.348` → IC=+0.257 (n=377)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.348 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` < `1.7283` → IC=+0.213 (n=1104)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7283 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` > `2.7303` → IC=+0.229 (n=1137)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7303 (IC base=+0.217)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.218 (n=1383)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.217)

- **PATRÓN** `libro_liquidez` > `2056.8384` → IC=+0.226 (n=881)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2056.8384 (IC base=+0.217)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.221 (n=2150)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 24.0 (IC base=+0.217)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.144 (n=147)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=3587)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.164 (n=528)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0036 (IC base=+0.053)

- **PATRÓN** `ibs_20min` > `0.9547` → IC=+0.228 (n=527)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9547 (IC base=+0.053)

- **PATRÓN** `dist_vwap_pct` > `0.137` → IC=+0.330 (n=356)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.137 (IC base=+0.053)

- **PATRÓN** `dist_vwap_pct` < `0.3349` → IC=+0.326 (n=549)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3349 (IC base=+0.053)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.12` → IC=+0.186 (n=1136)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 5.12 (IC base=+0.053)

- **PATRÓN** `volumen_regimen` < `0.8577` → IC=+0.333 (n=394)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8577 (IC base=+0.053)

- **PATRÓN** `volumen_regimen` > `1.2208` → IC=+0.344 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2208 (IC base=+0.053)

- **PATRÓN** `volumen_pendiente_norm` > `0.2986` → IC=+0.346 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2986 (IC base=+0.053)

- **PATRÓN** `volumen_spike_ratio` < `1.4107` → IC=+0.345 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4107 (IC base=+0.053)

- **PATRÓN** `volumen_spike_ratio` > `2.2172` → IC=+0.324 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2172 (IC base=+0.053)

- **PATRÓN** `ballena_activa_n` < `132.0` → IC=+0.336 (n=510)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 132.0 (IC base=+0.053)

- **PATRÓN** `ibs_20min` < `0.0931` → IC=+0.174 (n=934)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.0931 (IC base=+0.035)

- **PATRÓN** `dist_vwap_pct` > `0.3201` → IC=+0.141 (n=447)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.3201 (IC base=+0.035)

- **PATRÓN** `dist_vwap_pct` < `0.1292` → IC=+0.134 (n=1521)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.1292 (IC base=+0.035)

- **PATRÓN** `volumen_regimen` < `0.8423` → IC=+0.145 (n=1106)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 0.8423 (IC base=+0.035)

- **PATRÓN** `volumen_regimen` > `1.1684` → IC=+0.132 (n=553)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` > 1.1684 (IC base=+0.035)

- **PATRÓN** `volumen_pendiente_norm` > `0.2862` → IC=+0.197 (n=219)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2862 (IC base=+0.035)

- **PATRÓN** `volumen_spike_ratio` < `1.7769` → IC=+0.137 (n=1060)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.7769 (IC base=+0.035)

- **PATRÓN** `volumen_spike_ratio` > `2.1547` → IC=+0.151 (n=721)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 2.1547 (IC base=+0.035)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.167 (n=100)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=543)

- **FILTRO** `ibs_20min` < `0.2759` → IC=-0.202 (n=159)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2759
  - _Potencial_: sin este filtro IC_bueno=+0.109 (n=484)

- **FILTRO** `ibs_20min` > `0.2174` → IC=-0.132 (n=3521)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2174
  - _Potencial_: sin este filtro IC_bueno=+0.148 (n=1737)

- **FILTRO** `sigma_ewma_delta_pct` > `8.655` → IC=-0.235 (n=553)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.655
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=4705)

- **PATRÓN** `ibs_20min` > `0.7857` → IC=+0.185 (n=220)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.7857 (IC base=+0.032)

- **PATRÓN** `dist_vwap_pct` > `1.0161` → IC=+0.273 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0161 (IC base=+0.032)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.37` → IC=+0.149 (n=226)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 2.37 (IC base=+0.032)

- **PATRÓN** `volumen_regimen` < `0.5734` → IC=+0.261 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.5734 (IC base=+0.032)

- **PATRÓN** `volumen_regimen` > `1.0155` → IC=+0.303 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0155 (IC base=+0.032)

- **PATRÓN** `volumen_pendiente_norm` < `0.0778` → IC=+0.283 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0778 (IC base=+0.032)

- **PATRÓN** `volumen_spike_ratio` < `2.1915` → IC=+0.286 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1915 (IC base=+0.032)

- **PATRÓN** `volumen_spike_ratio` > `1.5481` → IC=+0.262 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5481 (IC base=+0.032)

- **PATRÓN** `ballena_activa_n` < `38.0` → IC=+0.264 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 38.0 (IC base=+0.032)

- **PATRÓN** `ibs_20min` < `0.2174` → IC=+0.148 (n=1737)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` < 0.2174 (IC base=-0.039)

- **PATRÓN** `dist_vwap_pct` > `0.2634` → IC=+0.277 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2634 (IC base=-0.039)

- **PATRÓN** `dist_vwap_pct` < `0.4351` → IC=+0.275 (n=807)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4351 (IC base=-0.039)

- **PATRÓN** `volumen_regimen` < `0.7007` → IC=+0.302 (n=317)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7007 (IC base=-0.039)

- **PATRÓN** `volumen_pendiente_norm` > `0.0805` → IC=+0.301 (n=310)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0805 (IC base=-0.039)

- **PATRÓN** `volumen_spike_ratio` < `2.4253` → IC=+0.298 (n=657)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4253 (IC base=-0.039)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6159` → IC=-0.178 (n=957)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6159
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=2872)

- **FILTRO** `ibs_20min` < `0.7471` → IC=-0.149 (n=2527)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7471
  - _Potencial_: sin este filtro IC_bueno=+0.094 (n=1302)

- **FILTRO** `ibs_20min` > `0.7527` → IC=-0.203 (n=1383)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7527
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=4152)

- **PATRÓN** `dist_vwap_pct` > `0.7406` → IC=+0.332 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7406 (IC base=-0.066)

- **PATRÓN** `dist_vwap_pct` < `0.2486` → IC=+0.302 (n=573)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2486 (IC base=-0.066)

- **PATRÓN** `volumen_regimen` > `0.7043` → IC=+0.312 (n=590)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7043 (IC base=-0.066)

- **PATRÓN** `volumen_pendiente_norm` < `0.0995` → IC=+0.300 (n=619)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0995 (IC base=-0.066)

- **PATRÓN** `volumen_pendiente_norm` > `0.0729` → IC=+0.302 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0729 (IC base=-0.066)

- **PATRÓN** `volumen_spike_ratio` < `1.4195` → IC=+0.323 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4195 (IC base=-0.066)

- **PATRÓN** `volumen_spike_ratio` > `1.8324` → IC=+0.301 (n=425)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8324 (IC base=-0.066)

- **PATRÓN** `dist_vwap_pct` > `0.8133` → IC=+0.274 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8133 (IC base=-0.006)

- **PATRÓN** `volumen_regimen` > `1.0712` → IC=+0.281 (n=684)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0712 (IC base=-0.006)

- **PATRÓN** `volumen_pendiente_norm` > `0.1035` → IC=+0.278 (n=525)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1035 (IC base=-0.006)

- **PATRÓN** `volumen_spike_ratio` < `2.1859` → IC=+0.260 (n=1221)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1859 (IC base=-0.006)

- **PATRÓN** `volumen_spike_ratio` > `1.4311` → IC=+0.262 (n=1387)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4311 (IC base=-0.006)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.207 (n=5743)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0098 (IC base=+0.096)

- **PATRÓN** `ibs_20min` > `0.8824` → IC=+0.281 (n=7812)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8824 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` > `0.9563` → IC=+0.298 (n=1254)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9563 (IC base=+0.096)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.609` → IC=+0.161 (n=7714)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 3.609 (IC base=+0.096)

- **PATRÓN** `volumen_regimen` < `1.1706` → IC=+0.262 (n=6334)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1706 (IC base=+0.096)

- **PATRÓN** `volumen_regimen` > `0.6888` → IC=+0.267 (n=5659)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6888 (IC base=+0.096)

- **PATRÓN** `volumen_pendiente_norm` < `0.0791` → IC=+0.260 (n=9307)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0791 (IC base=+0.096)

- **PATRÓN** `volumen_pendiente_norm` > `0.2399` → IC=+0.275 (n=1880)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2399 (IC base=+0.096)

- **PATRÓN** `volumen_spike_ratio` < `1.4602` → IC=+0.260 (n=3371)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4602 (IC base=+0.096)

- **PATRÓN** `volumen_spike_ratio` > `2.6398` → IC=+0.270 (n=3372)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6398 (IC base=+0.096)

- **PATRÓN** `ballena_activa_n` < `92.0` → IC=+0.293 (n=9700)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 92.0 (IC base=+0.096)

- **PATRÓN** `sigma_h` > `0.0093` → IC=+0.161 (n=5520)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0093 (IC base=+0.074)

- **PATRÓN** `ibs_20min` < `0.6596` → IC=+0.144 (n=16554)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.6596 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` < `0.2386` → IC=+0.263 (n=5186)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2386 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` < `0.706` → IC=+0.258 (n=2298)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.706 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` > `1.1967` → IC=+0.265 (n=1741)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1967 (IC base=+0.074)

- **PATRÓN** `volumen_pendiente_norm` > `0.2943` → IC=+0.316 (n=1116)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2943 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` < `1.5794` → IC=+0.288 (n=3287)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5794 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` > `2.2676` → IC=+0.283 (n=3386)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2676 (IC base=+0.074)

- **PATRÓN** `ballena_activa_n` < `77.0` → IC=+0.293 (n=7406)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 77.0 (IC base=+0.074)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.3703` → IC=-0.180 (n=1559)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3703
  - _Potencial_: sin este filtro IC_bueno=+0.134 (n=3166)

- **FILTRO** `ibs_20min` > `0.7427` → IC=-0.211 (n=989)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7427
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=2971)

- **FILTRO** `sigma_ewma_delta_pct` > `4.435` → IC=-0.203 (n=868)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.435
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=3092)

- **PATRÓN** `ibs_20min` > `0.9163` → IC=+0.307 (n=1182)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9163 (IC base=+0.030)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.029` → IC=+0.214 (n=840)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.029 (IC base=+0.030)

- **PATRÓN** `volumen_pendiente_norm` > `0.2278` → IC=+0.297 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2278 (IC base=+0.030)

- **PATRÓN** `volumen_spike_ratio` < `1.4427` → IC=+0.248 (n=514)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4427 (IC base=+0.030)

- **PATRÓN** `volumen_spike_ratio` > `2.242` → IC=+0.272 (n=699)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.242 (IC base=+0.030)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.277 (n=1047)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.030)

- **PATRÓN** `ibs_20min` < `0.1631` → IC=+0.163 (n=991)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` < 0.1631 (IC base=-0.027)

- **PATRÓN** `volumen_pendiente_norm` < `0.0719` → IC=+0.418 (n=448)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0719 (IC base=-0.027)

- **PATRÓN** `volumen_spike_ratio` < `2.4877` → IC=+0.409 (n=504)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4877 (IC base=-0.027)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.404 (n=465)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 21.0 (IC base=-0.027)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `ibs_20min` > `0.8477` → IC=+0.141 (n=1180)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` > 0.8477 (IC base=+0.024)

- **PATRÓN** `dist_vwap_pct` > `0.1123` → IC=+0.213 (n=859)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1123 (IC base=+0.024)

- **PATRÓN** `volumen_regimen` < `1.1937` → IC=+0.192 (n=1674)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 1.1937 (IC base=+0.024)

- **PATRÓN** `volumen_regimen` > `0.6813` → IC=+0.200 (n=1495)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6813 (IC base=+0.024)

- **PATRÓN** `volumen_pendiente_norm` < `0.0752` → IC=+0.190 (n=1540)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` < 0.0752 (IC base=+0.024)

- **PATRÓN** `volumen_pendiente_norm` > `0.2762` → IC=+0.225 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2762 (IC base=+0.024)

- **PATRÓN** `volumen_spike_ratio` < `1.4262` → IC=+0.216 (n=550)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4262 (IC base=+0.024)

- **PATRÓN** `volumen_spike_ratio` > `2.4876` → IC=+0.192 (n=550)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.4876 (IC base=+0.024)

- **PATRÓN** `ballena_activa_n` < `275.0` → IC=+0.229 (n=1097)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 275.0 (IC base=+0.024)

- **PATRÓN** `volumen_regimen` > `0.6209` → IC=+0.236 (n=1066)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6209 (IC base=-0.003)

- **PATRÓN** `volumen_pendiente_norm` > `0.273` → IC=+0.291 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.273 (IC base=-0.003)

- **PATRÓN** `volumen_spike_ratio` < `1.5351` → IC=+0.237 (n=447)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5351 (IC base=-0.003)

- **PATRÓN** `volumen_spike_ratio` > `2.1657` → IC=+0.249 (n=461)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1657 (IC base=-0.003)

- **PATRÓN** `ballena_activa_n` < `201.0` → IC=+0.235 (n=341)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 201.0 (IC base=-0.003)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0118` → IC=+0.307 (n=839)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0118 (IC base=+0.266)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.272 (n=2641)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.266)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.309 (n=1323)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.266)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.706` → IC=+0.296 (n=802)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.706 (IC base=+0.266)

- **PATRÓN** `volumen_pendiente_norm` < `0.0979` → IC=+0.278 (n=2187)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0979 (IC base=+0.266)

- **PATRÓN** `volumen_spike_ratio` > `1.6104` → IC=+0.272 (n=2430)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6104 (IC base=+0.266)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.277 (n=2984)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.266)

- **PATRÓN** `libro_liquidez` > `1972.96` → IC=+0.283 (n=1141)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1972.96 (IC base=+0.266)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.279 (n=1484)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 19.0 (IC base=+0.266)

- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.327 (n=983)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0101 (IC base=+0.292)

- **PATRÓN** `drift_60min` |x|≤ `0.1824` → IC=+0.311 (n=954)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1824 (IC base=+0.292)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.319 (n=826)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.292)

- **PATRÓN** `ibs_20min` < `0.3684` → IC=+0.295 (n=2167)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3684 (IC base=+0.292)

- **PATRÓN** `ibs_20min` > `0.258` → IC=+0.300 (n=982)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.258 (IC base=+0.292)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.594` → IC=+0.314 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.594 (IC base=+0.292)

- **PATRÓN** `volumen_pendiente_norm` < `0.1975` → IC=+0.290 (n=2115)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1975 (IC base=+0.292)

- **PATRÓN** `volumen_pendiente_norm` > `0.342` → IC=+0.309 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.342 (IC base=+0.292)

- **PATRÓN** `volumen_spike_ratio` < `1.7251` → IC=+0.299 (n=909)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7251 (IC base=+0.292)

- **PATRÓN** `volumen_spike_ratio` > `2.6682` → IC=+0.302 (n=937)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6682 (IC base=+0.292)

- **PATRÓN** `libro_liquidez` > `2051.9584` → IC=+0.307 (n=722)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2051.9584 (IC base=+0.292)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.292 (n=1369)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 19.0 (IC base=+0.292)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.738` → IC=-0.186 (n=1039)

  - _Acción_: SKIP cuando `ibs_20min` > 0.738
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=3121)

- **PATRÓN** `ibs_20min` > `0.8801` → IC=+0.173 (n=983)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` > 0.8801 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` > `0.1518` → IC=+0.234 (n=739)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1518 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` < `0.3624` → IC=+0.232 (n=1337)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3624 (IC base=+0.029)

- **PATRÓN** `volumen_regimen` < `1.0079` → IC=+0.244 (n=1208)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0079 (IC base=+0.029)

- **PATRÓN** `volumen_regimen` > `0.6711` → IC=+0.229 (n=1226)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6711 (IC base=+0.029)

- **PATRÓN** `volumen_pendiente_norm` < `0.1635` → IC=+0.234 (n=1459)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1635 (IC base=+0.029)

- **PATRÓN** `volumen_pendiente_norm` > `0.1022` → IC=+0.248 (n=431)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1022 (IC base=+0.029)

- **PATRÓN** `volumen_spike_ratio` < `1.4` → IC=+0.244 (n=443)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4 (IC base=+0.029)

- **PATRÓN** `ballena_activa_n` < `103.0` → IC=+0.266 (n=1190)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 103.0 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` < `0.328` → IC=+0.230 (n=1038)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.328 (IC base=-0.002)

- **PATRÓN** `volumen_regimen` < `1.1974` → IC=+0.230 (n=950)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1974 (IC base=-0.002)

- **PATRÓN** `volumen_pendiente_norm` < `0.1017` → IC=+0.247 (n=879)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1017 (IC base=-0.002)

- **PATRÓN** `volumen_pendiente_norm` > `0.2862` → IC=+0.291 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2862 (IC base=-0.002)

- **PATRÓN** `volumen_spike_ratio` < `1.7982` → IC=+0.269 (n=600)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7982 (IC base=-0.002)

- **PATRÓN** `volumen_spike_ratio` > `2.4478` → IC=+0.252 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4478 (IC base=-0.002)

- **PATRÓN** `ballena_activa_n` < `125.0` → IC=+0.256 (n=915)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 125.0 (IC base=-0.002)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7619` → IC=-0.211 (n=1810)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7619
  - _Potencial_: sin este filtro IC_bueno=+0.304 (n=1816)

- **FILTRO** `ibs_20min` > `0.6486` → IC=-0.234 (n=889)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6486
  - _Potencial_: sin este filtro IC_bueno=+0.120 (n=2671)

- **FILTRO** `sigma_ewma_delta_pct` > `8.501` → IC=-0.241 (n=411)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.501
  - _Potencial_: sin este filtro IC_bueno=+0.067 (n=3149)

- **PATRÓN** `ibs_20min` > `0.7619` → IC=+0.304 (n=1816)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7619 (IC base=+0.047)

- **PATRÓN** `dist_vwap_pct` > `0.2157` → IC=+0.336 (n=807)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2157 (IC base=+0.047)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.527` → IC=+0.181 (n=566)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 9.527 (IC base=+0.047)

- **PATRÓN** `volumen_regimen` < `0.8471` → IC=+0.332 (n=911)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8471 (IC base=+0.047)

- **PATRÓN** `volumen_regimen` > `0.704` → IC=+0.323 (n=1219)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.704 (IC base=+0.047)

- **PATRÓN** `volumen_pendiente_norm` < `0.1585` → IC=+0.323 (n=1413)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1585 (IC base=+0.047)

- **PATRÓN** `volumen_pendiente_norm` > `0.2752` → IC=+0.348 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2752 (IC base=+0.047)

- **PATRÓN** `volumen_spike_ratio` < `1.4421` → IC=+0.343 (n=443)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4421 (IC base=+0.047)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.340 (n=1172)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 49.0 (IC base=+0.047)

- **PATRÓN** `ibs_20min` < `0.5484` → IC=+0.144 (n=2350)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.5484 (IC base=+0.031)

- **PATRÓN** `dist_vwap_pct` < `0.4541` → IC=+0.250 (n=1269)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4541 (IC base=+0.031)

- **PATRÓN** `volumen_regimen` < `0.7017` → IC=+0.263 (n=517)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7017 (IC base=+0.031)

- **PATRÓN** `volumen_pendiente_norm` < `0.2231` → IC=+0.241 (n=1320)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2231 (IC base=+0.031)

- **PATRÓN** `volumen_pendiente_norm` > `0.0758` → IC=+0.259 (n=446)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0758 (IC base=+0.031)

- **PATRÓN** `volumen_spike_ratio` < `2.4284` → IC=+0.250 (n=1128)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4284 (IC base=+0.031)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.270 (n=1142)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 52.0 (IC base=+0.031)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.344 (n=1721)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0107 (IC base=+0.300)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.302 (n=747)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.300)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.312 (n=925)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.300)

- **PATRÓN** `ibs_20min` > `0.66` → IC=+0.334 (n=1926)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.66 (IC base=+0.300)

- **PATRÓN** `dist_vwap_pct` > `0.2066` → IC=+0.327 (n=1085)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2066 (IC base=+0.300)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.795` → IC=+0.321 (n=935)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.795 (IC base=+0.300)

- **PATRÓN** `volumen_regimen` > `0.6266` → IC=+0.309 (n=1926)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6266 (IC base=+0.300)

- **PATRÓN** `volumen_pendiente_norm` > `0.2791` → IC=+0.342 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2791 (IC base=+0.300)

- **PATRÓN** `volumen_spike_ratio` > `1.4244` → IC=+0.312 (n=1845)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4244 (IC base=+0.300)

- **PATRÓN** `libro_liquidez` > `2637.4126` → IC=+0.314 (n=1284)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2637.4126 (IC base=+0.300)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.334 (n=1665)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 42.0 (IC base=+0.300)

- **PATRÓN** `sigma_h` > `0.0151` → IC=+0.334 (n=1355)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0151 (IC base=+0.302)

- **PATRÓN** `drift_60min` |x|≤ `0.1874` → IC=+0.305 (n=895)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1874 (IC base=+0.302)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.314 (n=787)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.302)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.303 (n=1001)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.302)

- **PATRÓN** `ibs_20min` < `0.3684` → IC=+0.327 (n=2033)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3684 (IC base=+0.302)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.555` → IC=+0.315 (n=754)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.555 (IC base=+0.302)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.078` → IC=+0.303 (n=2417)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 10.078 (IC base=+0.302)

- **PATRÓN** `volumen_regimen` < `0.7186` → IC=+0.307 (n=895)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7186 (IC base=+0.302)

- **PATRÓN** `volumen_regimen` > `1.2266` → IC=+0.332 (n=678)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2266 (IC base=+0.302)

- **PATRÓN** `volumen_pendiente_norm` > `0.2838` → IC=+0.350 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2838 (IC base=+0.302)

- **PATRÓN** `volumen_spike_ratio` < `1.4152` → IC=+0.310 (n=620)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4152 (IC base=+0.302)

- **PATRÓN** `volumen_spike_ratio` > `2.1346` → IC=+0.307 (n=843)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1346 (IC base=+0.302)

- **PATRÓN** `libro_liquidez` > `2632.217` → IC=+0.302 (n=1355)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2632.217 (IC base=+0.302)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.181 (n=4235)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0049 (IC base=+0.180)

- **PATRÓN** `sigma_h` > `0.0115` → IC=+0.224 (n=4231)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0115 (IC base=+0.180)

- **PATRÓN** `drift_60min` |x|≤ `0.1214` → IC=+0.200 (n=5578)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1214 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.190 (n=13146)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` > `0.5588` → IC=+0.234 (n=12672)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5588 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` > `0.1634` → IC=+0.208 (n=5150)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1634 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.266` → IC=+0.259 (n=2493)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.266 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` < `1.1862` → IC=+0.169 (n=8406)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 1.1862 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` > `0.6238` → IC=+0.165 (n=8406)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 0.6238 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.2929` → IC=+0.205 (n=1845)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2929 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `2.6076` → IC=+0.190 (n=4093)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 2.6076 (IC base=+0.180)

- **PATRÓN** `libro_liquidez` > `1983.579` → IC=+0.182 (n=11318)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 1983.579 (IC base=+0.180)

- **PATRÓN** `ballena_activa_n` < `95.0` → IC=+0.198 (n=11586)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 95.0 (IC base=+0.180)

- **PATRÓN** `sigma_h` < `0.007` → IC=+0.185 (n=8140)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.007 (IC base=+0.179)

- **PATRÓN** `drift_60min` |x|≤ `0.0795` → IC=+0.226 (n=4066)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0795 (IC base=+0.179)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.210 (n=5761)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.179)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.236 (n=12220)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5 (IC base=+0.179)

- **PATRÓN** `dist_vwap_pct` < `0.1733` → IC=+0.174 (n=8668)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` < 0.1733 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.041` → IC=+0.197 (n=1996)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 10.041 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.69` → IC=+0.180 (n=10752)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` < 2.69 (IC base=+0.179)

- **PATRÓN** `volumen_regimen` < `1.1824` → IC=+0.163 (n=8704)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.1824 (IC base=+0.179)

- **PATRÓN** `volumen_pendiente_norm` > `0.2938` → IC=+0.225 (n=1803)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2938 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` > `2.6363` → IC=+0.188 (n=3816)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.6363 (IC base=+0.179)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.192 (n=11164)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 100.0 (IC base=+0.179)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.233 (n=709)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.213)

- **PATRÓN** `drift_60min` |x|≤ `0.3316` → IC=+0.229 (n=2119)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3316 (IC base=+0.213)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.216 (n=2217)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.213)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.221 (n=1437)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.213)

- **PATRÓN** `ibs_20min` > `0.9275` → IC=+0.294 (n=1413)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9275 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.986` → IC=+0.330 (n=668)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.986 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` > `0.2803` → IC=+0.270 (n=316)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2803 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` < `1.8383` → IC=+0.207 (n=1335)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8383 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` > `1.5348` → IC=+0.213 (n=1789)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5348 (IC base=+0.213)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.225 (n=2281)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.213)

- **PATRÓN** `libro_liquidez` > `2083.02` → IC=+0.214 (n=707)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2083.02 (IC base=+0.213)

- **PATRÓN** `sigma_h` < `0.0081` → IC=+0.249 (n=1656)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0081 (IC base=+0.249)

- **PATRÓN** `sigma_h` > `0.0073` → IC=+0.258 (n=750)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0073 (IC base=+0.249)

- **PATRÓN** `drift_60min` |x|≤ `0.0951` → IC=+0.304 (n=728)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0951 (IC base=+0.249)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.254 (n=1500)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.249)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.253 (n=803)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.249)

- **PATRÓN** `ibs_20min` < `0.3967` → IC=+0.266 (n=1654)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3967 (IC base=+0.249)

- **PATRÓN** `volumen_pendiente_norm` < `0.1002` → IC=+0.250 (n=1444)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1002 (IC base=+0.249)

- **PATRÓN** `volumen_pendiente_norm` > `0.2967` → IC=+0.284 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2967 (IC base=+0.249)

- **PATRÓN** `volumen_spike_ratio` < `1.4285` → IC=+0.269 (n=522)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4285 (IC base=+0.249)

- **PATRÓN** `volumen_spike_ratio` > `2.6706` → IC=+0.252 (n=522)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6706 (IC base=+0.249)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.254 (n=1858)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.249)

- **PATRÓN** `libro_liquidez` > `1528.4822` → IC=+0.259 (n=1654)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1528.4822 (IC base=+0.249)

- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.255 (n=593)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 8.0 (IC base=+0.249)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.218 (n=641)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.156)

- **PATRÓN** `drift_60min` |x|≤ `0.1597` → IC=+0.183 (n=1271)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.1597 (IC base=+0.156)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.171 (n=2008)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 5.0 (IC base=+0.156)

- **PATRÓN** `ibs_20min` > `0.343` → IC=+0.224 (n=1906)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.343 (IC base=+0.156)

- **PATRÓN** `dist_vwap_pct` > `0.1341` → IC=+0.215 (n=1147)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1341 (IC base=+0.156)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.386` → IC=+0.226 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.386 (IC base=+0.156)

- **PATRÓN** `volumen_regimen` < `0.6895` → IC=+0.166 (n=839)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.6895 (IC base=+0.156)

- **PATRÓN** `volumen_pendiente_norm` > `0.2816` → IC=+0.192 (n=303)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2816 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` < `1.4131` → IC=+0.182 (n=623)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 1.4131 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` > `2.5153` → IC=+0.160 (n=622)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 2.5153 (IC base=+0.156)

- **PATRÓN** `ballena_activa_n` < `421.0` → IC=+0.160 (n=1828)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 421.0 (IC base=+0.156)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.169 (n=2001)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0058 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.2337` → IC=+0.172 (n=1760)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.2337 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.185 (n=956)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 15.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` < `0.6184` → IC=+0.204 (n=2000)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6184 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.493` → IC=+0.193 (n=379)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 11.493 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `1.2053` → IC=+0.159 (n=2000)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2053 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` < `0.0938` → IC=+0.147 (n=1690)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` < 0.0938 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `2.5035` → IC=+0.151 (n=1880)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.5035 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `1.4236` → IC=+0.146 (n=1880)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.4236 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `202.0` → IC=+0.179 (n=606)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 202.0 (IC base=+0.144)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0108` → IC=+0.238 (n=974)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0108 (IC base=+0.214)

- **PATRÓN** `drift_60min` |x|≤ `0.3992` → IC=+0.225 (n=1889)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3992 (IC base=+0.214)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.233 (n=784)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.214)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.303 (n=1110)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.214)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.435` → IC=+0.295 (n=496)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.435 (IC base=+0.214)

- **PATRÓN** `volumen_pendiente_norm` < `0.0992` → IC=+0.213 (n=1834)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0992 (IC base=+0.214)

- **PATRÓN** `volumen_pendiente_norm` > `0.3544` → IC=+0.225 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3544 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` < `1.767` → IC=+0.214 (n=915)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.767 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` > `2.7084` → IC=+0.228 (n=943)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7084 (IC base=+0.214)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.221 (n=2557)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.214)

- **PATRÓN** `libro_liquidez` > `1966.82` → IC=+0.226 (n=973)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1966.82 (IC base=+0.214)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.246 (n=1619)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.235)

- **PATRÓN** `drift_60min` |x|≤ `0.1427` → IC=+0.273 (n=809)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1427 (IC base=+0.235)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.281 (n=697)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.235)

- **PATRÓN** `ibs_20min` < `0.0069` → IC=+0.299 (n=809)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0069 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.528` → IC=+0.276 (n=270)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.528 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` > `0.3556` → IC=+0.279 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3556 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` < `1.7477` → IC=+0.235 (n=772)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7477 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` > `2.1513` → IC=+0.239 (n=1169)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1513 (IC base=+0.235)

- **PATRÓN** `libro_liquidez` > `2051.9357` → IC=+0.241 (n=613)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2051.9357 (IC base=+0.235)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.232 (n=1187)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 17.0 (IC base=+0.235)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0074` → IC=+0.174 (n=2058)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0074 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.4062` → IC=+0.168 (n=2057)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.4062 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.164 (n=2134)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` > `0.3118` → IC=+0.213 (n=2058)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3118 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` > `0.1409` → IC=+0.199 (n=1261)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1409 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.767` → IC=+0.200 (n=358)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.767 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` < `1.0234` → IC=+0.160 (n=1810)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.0234 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.1028` → IC=+0.180 (n=842)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.1028 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `1.8198` → IC=+0.150 (n=1345)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.8198 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` > `2.5051` → IC=+0.166 (n=672)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 2.5051 (IC base=+0.151)

- **PATRÓN** `libro_liquidez` > `4600.3072` → IC=+0.186 (n=1371)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 4600.3072 (IC base=+0.151)

- **PATRÓN** `ballena_activa_n` < `140.0` → IC=+0.159 (n=1999)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 140.0 (IC base=+0.151)

- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.154 (n=2165)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0071 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.3953` → IC=+0.144 (n=2164)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.3953 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.167 (n=1026)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 15.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` < `0.6854` → IC=+0.186 (n=2164)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.6854 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` < `0.1525` → IC=+0.156 (n=2160)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1525 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.84` → IC=+0.156 (n=757)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 6.84 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `0.856` → IC=+0.156 (n=1443)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.856 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` > `0.2999` → IC=+0.197 (n=328)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2999 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `1.811` → IC=+0.136 (n=1351)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.811 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` > `1.4242` → IC=+0.127 (n=2026)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` > 1.4242 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `7543.4222` → IC=+0.192 (n=981)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 7543.4222 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `68.0` → IC=+0.146 (n=877)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 68.0 (IC base=+0.126)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0103` → IC=+0.176 (n=1049)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.0103 (IC base=+0.128)

- **PATRÓN** `drift_60min` |x|≤ `0.4413` → IC=+0.129 (n=2035)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.65€ cuando `drift_60min` |x|≤ 0.4413 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.143 (n=2356)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` > `0.5` → IC=+0.215 (n=2312)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5 (IC base=+0.128)

- **PATRÓN** `dist_vwap_pct` > `0.1958` → IC=+0.188 (n=1352)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1958 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.599` → IC=+0.276 (n=494)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.599 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` < `1.175` → IC=+0.143 (n=2312)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 1.175 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` < `0.161` → IC=+0.136 (n=2346)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` < 0.161 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` < `1.4385` → IC=+0.148 (n=748)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.4385 (IC base=+0.128)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.129 (n=2414)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.02 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `2792.8737` → IC=+0.207 (n=1048)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2792.8737 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.167 (n=742)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 20.0 (IC base=+0.128)

- **PATRÓN** `sigma_h` < `0.0108` → IC=+0.139 (n=2366)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` < 0.0108 (IC base=+0.120)

- **PATRÓN** `drift_60min` |x|≤ `0.1079` → IC=+0.174 (n=789)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.1079 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.140 (n=2405)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 5.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` < `0.5932` → IC=+0.219 (n=2363)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5932 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` < `0.1986` → IC=+0.148 (n=2231)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.1986 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.404` → IC=+0.125 (n=475)

  - _Acción_: Kelly boost +0.62€ cuando `sigma_ewma_delta_pct` > 7.404 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.467` → IC=+0.130 (n=2088)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` < 2.467 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` < `1.1753` → IC=+0.130 (n=2364)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.1753 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` < `0.1653` → IC=+0.124 (n=2284)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.1653 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` > `0.275` → IC=+0.151 (n=316)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.275 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` < `1.4479` → IC=+0.135 (n=734)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 1.4479 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` > `2.4253` → IC=+0.137 (n=734)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 2.4253 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `2655.5302` → IC=+0.190 (n=1071)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 2655.5302 (IC base=+0.120)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.130 (n=1912)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 42.0 (IC base=+0.120)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0129` → IC=+0.247 (n=1904)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0129 (IC base=+0.221)

- **PATRÓN** `drift_60min` |x|≤ `0.1289` → IC=+0.238 (n=711)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1289 (IC base=+0.221)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.225 (n=2209)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.221)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.226 (n=1917)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.221)

- **PATRÓN** `ibs_20min` > `0.7419` → IC=+0.267 (n=1906)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7419 (IC base=+0.221)

- **PATRÓN** `dist_vwap_pct` > `0.1837` → IC=+0.227 (n=1380)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1837 (IC base=+0.221)

- **PATRÓN** `dist_vwap_pct` < `0.4796` → IC=+0.223 (n=1908)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4796 (IC base=+0.221)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.611` → IC=+0.250 (n=967)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.611 (IC base=+0.221)

- **PATRÓN** `volumen_regimen` < `1.1768` → IC=+0.224 (n=2131)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1768 (IC base=+0.221)

- **PATRÓN** `volumen_regimen` > `0.6184` → IC=+0.230 (n=2131)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6184 (IC base=+0.221)

- **PATRÓN** `volumen_pendiente_norm` > `0.2826` → IC=+0.271 (n=295)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2826 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` < `2.4638` → IC=+0.227 (n=2074)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4638 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` > `1.8052` → IC=+0.230 (n=1382)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8052 (IC base=+0.221)

- **PATRÓN** `libro_liquidez` > `2616.7194` → IC=+0.227 (n=1421)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2616.7194 (IC base=+0.221)

- **PATRÓN** `sigma_h` < `0.0125` → IC=+0.235 (n=959)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0125 (IC base=+0.228)

- **PATRÓN** `sigma_h` > `0.0226` → IC=+0.239 (n=988)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0226 (IC base=+0.228)

- **PATRÓN** `drift_60min` |x|≤ `0.0889` → IC=+0.261 (n=727)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0889 (IC base=+0.228)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.248 (n=1061)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.228)

- **PATRÓN** `ibs_20min` < `0.426` → IC=+0.256 (n=2179)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.426 (IC base=+0.228)

- **PATRÓN** `dist_vwap_pct` > `0.2938` → IC=+0.234 (n=578)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2938 (IC base=+0.228)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.332` → IC=+0.255 (n=415)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.332 (IC base=+0.228)

- **PATRÓN** `volumen_regimen` > `0.6411` → IC=+0.235 (n=2179)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6411 (IC base=+0.228)

- **PATRÓN** `volumen_pendiente_norm` > `0.2803` → IC=+0.284 (n=295)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2803 (IC base=+0.228)

- **PATRÓN** `volumen_spike_ratio` > `1.4397` → IC=+0.231 (n=2025)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4397 (IC base=+0.228)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.228 (n=2818)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.228)

- **PATRÓN** `libro_liquidez` > `2594.8515` → IC=+0.229 (n=1453)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2594.8515 (IC base=+0.228)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.209 (n=1420)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.182)

- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.191 (n=1074)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.0089 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.1292` → IC=+0.203 (n=1418)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1292 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.215 (n=1592)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` > `0.725` → IC=+0.232 (n=2148)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.725 (IC base=+0.182)

- **PATRÓN** `dist_vwap_pct` > `0.7904` → IC=+0.201 (n=483)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7904 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.64` → IC=+0.212 (n=1393)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.64 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` < `0.8634` → IC=+0.203 (n=1934)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8634 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` > `0.6967` → IC=+0.185 (n=2591)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` > 0.6967 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.0999` → IC=+0.192 (n=1159)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.0999 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` < `1.4332` → IC=+0.198 (n=1044)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.4332 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `2.1994` → IC=+0.188 (n=1419)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.1994 (IC base=+0.182)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.188 (n=3638)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.02 (IC base=+0.182)

- **PATRÓN** `libro_liquidez` > `2685.4936` → IC=+0.188 (n=2879)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 2685.4936 (IC base=+0.182)

- **PATRÓN** `ballena_activa_n` < `150.0` → IC=+0.193 (n=3001)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 150.0 (IC base=+0.182)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.134 (n=1158)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` < 0.0038 (IC base=+0.087)

- **PATRÓN** `ibs_20min` < `0.3839` → IC=+0.161 (n=2313)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.3839 (IC base=+0.087)

- **PATRÓN** `ballena_activa_n` < `28.0` → IC=+0.124 (n=1484)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 28.0 (IC base=+0.087)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.204 (n=404)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.177)

- **PATRÓN** `drift_60min` |x|≤ `0.3265` → IC=+0.199 (n=911)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.3265 (IC base=+0.177)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.205 (n=829)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.177)

- **PATRÓN** `ibs_20min` > `0.6364` → IC=+0.234 (n=607)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6364 (IC base=+0.177)

- **PATRÓN** `dist_vwap_pct` > `0.3049` → IC=+0.197 (n=275)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.3049 (IC base=+0.177)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.092` → IC=+0.197 (n=391)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 3.092 (IC base=+0.177)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.705` → IC=+0.178 (n=966)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` < 6.705 (IC base=+0.177)

- **PATRÓN** `volumen_regimen` < `0.8739` → IC=+0.203 (n=608)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8739 (IC base=+0.177)

- **PATRÓN** `volumen_pendiente_norm` < `0.093` → IC=+0.178 (n=876)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` < 0.093 (IC base=+0.177)

- **PATRÓN** `volumen_pendiente_norm` > `0.0718` → IC=+0.179 (n=359)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.0718 (IC base=+0.177)

- **PATRÓN** `volumen_spike_ratio` < `2.2078` → IC=+0.186 (n=784)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` < 2.2078 (IC base=+0.177)

- **PATRÓN** `libro_liquidez` > `14653.7158` → IC=+0.185 (n=607)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 14653.7158 (IC base=+0.177)

- **PATRÓN** `ballena_activa_n` < `158.0` → IC=+0.203 (n=389)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 158.0 (IC base=+0.177)

- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.186 (n=361)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0028 (IC base=+0.119)

- **PATRÓN** `drift_60min` |x|≤ `0.2687` → IC=+0.142 (n=948)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.2687 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.130 (n=974)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 7.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` < `0.6372` → IC=+0.167 (n=948)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` < 0.6372 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.713` → IC=+0.136 (n=212)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` > 8.713 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` > `1.0619` → IC=+0.150 (n=489)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 1.0619 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` > `0.1612` → IC=+0.166 (n=285)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.1612 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` < `2.121` → IC=+0.131 (n=936)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 2.121 (IC base=+0.119)

- **PATRÓN** `ballena_activa_n` < `218.0` → IC=+0.161 (n=697)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 218.0 (IC base=+0.119)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.248 (n=654)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.216)

- **PATRÓN** `drift_60min` |x|≤ `0.0943` → IC=+0.245 (n=327)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0943 (IC base=+0.216)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.232 (n=1028)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.216)

- **PATRÓN** `ibs_20min` > `0.6851` → IC=+0.273 (n=654)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6851 (IC base=+0.216)

- **PATRÓN** `dist_vwap_pct` > `0.3552` → IC=+0.220 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3552 (IC base=+0.216)

- **PATRÓN** `dist_vwap_pct` < `0.2037` → IC=+0.221 (n=881)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2037 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.883` → IC=+0.244 (n=396)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.883 (IC base=+0.216)

- **PATRÓN** `volumen_regimen` < `0.8358` → IC=+0.226 (n=654)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8358 (IC base=+0.216)

- **PATRÓN** `volumen_regimen` > `1.1649` → IC=+0.223 (n=327)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1649 (IC base=+0.216)

- **PATRÓN** `volumen_pendiente_norm` > `0.1565` → IC=+0.248 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1565 (IC base=+0.216)

- **PATRÓN** `volumen_spike_ratio` < `1.4208` → IC=+0.248 (n=323)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4208 (IC base=+0.216)

- **PATRÓN** `volumen_spike_ratio` > `1.7764` → IC=+0.228 (n=645)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7764 (IC base=+0.216)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.216 (n=1097)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.216)

- **PATRÓN** `ibs_20min` < `0.1073` → IC=+0.160 (n=333)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.1073 (IC base=+0.059)

- **PATRÓN** `libro_liquidez` > `6658.8999` → IC=+0.134 (n=665)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 6658.8999 (IC base=+0.059)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0108` → IC=+0.177 (n=264)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.0108 (IC base=+0.163)

- **PATRÓN** `drift_60min` |x|≤ `0.5317` → IC=+0.165 (n=791)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.5317 (IC base=+0.163)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.218 (n=381)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.163)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.276 (n=368)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.163)

- **PATRÓN** `dist_vwap_pct` > `1.0124` → IC=+0.234 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0124 (IC base=+0.163)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.127` → IC=+0.232 (n=334)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.127 (IC base=+0.163)

- **PATRÓN** `volumen_regimen` < `1.0652` → IC=+0.182 (n=696)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 1.0652 (IC base=+0.163)

- **PATRÓN** `volumen_regimen` > `0.7217` → IC=+0.170 (n=708)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` > 0.7217 (IC base=+0.163)

- **PATRÓN** `volumen_pendiente_norm` > `0.1641` → IC=+0.180 (n=220)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.1641 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` < `1.4513` → IC=+0.180 (n=254)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 1.4513 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` > `2.1805` → IC=+0.172 (n=346)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.1805 (IC base=+0.163)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.168 (n=815)

  - _Acción_: Kelly boost +0.84€ cuando `libro_spread` < 0.02 (IC base=+0.163)

- **PATRÓN** `libro_liquidez` > `3047.4604` → IC=+0.188 (n=264)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 3047.4604 (IC base=+0.163)

- **PATRÓN** `ibs_20min` < `0.5455` → IC=+0.133 (n=750)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.5455 (IC base=+0.052)

- **PATRÓN** `libro_liquidez` > `2721.3379` → IC=+0.141 (n=385)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 2721.3379 (IC base=+0.052)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.127 (n=545)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 21.0 (IC base=+0.052)

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
- **PATRÓN** `sigma_h` > `0.0115` → IC=+0.226 (n=5509)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0115 (IC base=+0.183)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.192 (n=17193)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 5.0 (IC base=+0.183)

- **PATRÓN** `ibs_20min` > `0.4483` → IC=+0.230 (n=16510)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4483 (IC base=+0.183)

- **PATRÓN** `dist_vwap_pct` > `0.9021` → IC=+0.210 (n=2016)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9021 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.27` → IC=+0.255 (n=4028)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.27 (IC base=+0.183)

- **PATRÓN** `volumen_regimen` < `1.221` → IC=+0.170 (n=11065)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 1.221 (IC base=+0.183)

- **PATRÓN** `volumen_pendiente_norm` > `0.2904` → IC=+0.206 (n=2192)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2904 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` > `2.6126` → IC=+0.197 (n=5349)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 2.6126 (IC base=+0.183)

- **PATRÓN** `libro_liquidez` > `1975.0007` → IC=+0.185 (n=14745)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 1975.0007 (IC base=+0.183)

- **PATRÓN** `ballena_activa_n` < `113.0` → IC=+0.203 (n=15143)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 113.0 (IC base=+0.183)

- **PATRÓN** `sigma_h` < `0.0073` → IC=+0.193 (n=9997)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0073 (IC base=+0.187)

- **PATRÓN** `drift_60min` |x|≤ `0.3799` → IC=+0.192 (n=13185)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.3799 (IC base=+0.187)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.209 (n=5562)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.187)

- **PATRÓN** `ibs_20min` < `0.583` → IC=+0.242 (n=14983)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.583 (IC base=+0.187)

- **PATRÓN** `dist_vwap_pct` < `0.1745` → IC=+0.171 (n=9141)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` < 0.1745 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.844` → IC=+0.205 (n=2078)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.844 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.581` → IC=+0.190 (n=14481)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` < 3.581 (IC base=+0.187)

- **PATRÓN** `volumen_regimen` < `0.6332` → IC=+0.162 (n=3373)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.6332 (IC base=+0.187)

- **PATRÓN** `volumen_pendiente_norm` > `0.2905` → IC=+0.252 (n=2028)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2905 (IC base=+0.187)

- **PATRÓN** `volumen_spike_ratio` > `2.6156` → IC=+0.198 (n=4719)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 2.6156 (IC base=+0.187)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.216 (n=9305)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 40.0 (IC base=+0.187)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.235 (n=900)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.223)

- **PATRÓN** `drift_60min` |x|≤ `0.3484` → IC=+0.225 (n=2693)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3484 (IC base=+0.223)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.234 (n=1300)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.223)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.227 (n=1821)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.223)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.328 (n=1057)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.223)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.539` → IC=+0.353 (n=629)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.539 (IC base=+0.223)

- **PATRÓN** `volumen_pendiente_norm` > `0.2796` → IC=+0.285 (n=351)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2796 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` > `2.2721` → IC=+0.235 (n=1172)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2721 (IC base=+0.223)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.240 (n=2858)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.223)

- **PATRÓN** `libro_liquidez` > `2002.86` → IC=+0.229 (n=1221)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2002.86 (IC base=+0.223)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.245 (n=1604)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 17.0 (IC base=+0.223)

- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.266 (n=2296)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0084 (IC base=+0.262)

- **PATRÓN** `drift_60min` |x|≤ `0.1195` → IC=+0.284 (n=1013)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1195 (IC base=+0.262)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.268 (n=2099)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.262)

- **PATRÓN** `ibs_20min` < `0.5086` → IC=+0.288 (n=2296)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5086 (IC base=+0.262)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.174` → IC=+0.265 (n=457)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.174 (IC base=+0.262)

- **PATRÓN** `volumen_pendiente_norm` < `0.095` → IC=+0.262 (n=2058)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.095 (IC base=+0.262)

- **PATRÓN** `volumen_pendiente_norm` > `0.2845` → IC=+0.284 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2845 (IC base=+0.262)

- **PATRÓN** `volumen_spike_ratio` < `1.5574` → IC=+0.264 (n=957)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5574 (IC base=+0.262)

- **PATRÓN** `volumen_spike_ratio` > `2.6409` → IC=+0.270 (n=725)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6409 (IC base=+0.262)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.264 (n=2579)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.262)

- **PATRÓN** `libro_liquidez` > `1656.44` → IC=+0.270 (n=2051)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1656.44 (IC base=+0.262)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.273 (n=940)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.262)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.198 (n=894)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0028 (IC base=+0.152)

- **PATRÓN** `drift_60min` |x|≤ `0.1045` → IC=+0.168 (n=1173)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.1045 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.164 (n=2779)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.152)

- **PATRÓN** `ibs_20min` > `0.3755` → IC=+0.227 (n=2381)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3755 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` > `0.1244` → IC=+0.197 (n=1389)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.1244 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.568` → IC=+0.165 (n=440)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 11.568 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.167` → IC=+0.156 (n=2448)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 4.167 (IC base=+0.152)

- **PATRÓN** `volumen_regimen` < `0.629` → IC=+0.176 (n=890)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.629 (IC base=+0.152)

- **PATRÓN** `volumen_pendiente_norm` < `0.0726` → IC=+0.156 (n=2374)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` < 0.0726 (IC base=+0.152)

- **PATRÓN** `volumen_pendiente_norm` > `0.2723` → IC=+0.182 (n=379)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.2723 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` < `2.189` → IC=+0.161 (n=2292)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 2.189 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` > `1.5326` → IC=+0.155 (n=2328)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.5326 (IC base=+0.152)

- **PATRÓN** `ballena_activa_n` < `266.0` → IC=+0.188 (n=1127)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 266.0 (IC base=+0.152)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.164 (n=2224)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0058 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.256` → IC=+0.164 (n=1957)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.256 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.171 (n=835)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` < `0.7006` → IC=+0.198 (n=2224)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.7006 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.198` → IC=+0.155 (n=369)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 11.198 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.256` → IC=+0.144 (n=2001)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 4.256 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `1.1895` → IC=+0.154 (n=2224)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 1.1895 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` > `0.2182` → IC=+0.196 (n=419)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2182 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `2.4364` → IC=+0.149 (n=2119)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.4364 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `1.7762` → IC=+0.156 (n=1412)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.7762 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `275.0` → IC=+0.159 (n=892)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 275.0 (IC base=+0.144)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0123` → IC=+0.260 (n=918)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0123 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.234 (n=2871)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.226)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.228 (n=2462)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.226)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.302 (n=1021)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.309` → IC=+0.322 (n=583)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.309 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` < `0.132` → IC=+0.230 (n=2566)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.132 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` > `1.6215` → IC=+0.230 (n=2667)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6215 (IC base=+0.226)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.235 (n=3270)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.226)

- **PATRÓN** `libro_liquidez` > `1836.4184` → IC=+0.235 (n=1832)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1836.4184 (IC base=+0.226)

- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.245 (n=2264)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0106 (IC base=+0.241)

- **PATRÓN** `drift_60min` |x|≤ `0.1813` → IC=+0.258 (n=1132)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1813 (IC base=+0.241)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.262 (n=963)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.241)

- **PATRÓN** `ibs_20min` < `0.0295` → IC=+0.306 (n=859)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0295 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.98` → IC=+0.292 (n=412)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.98 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` > `0.3452` → IC=+0.298 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3452 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` > `2.1351` → IC=+0.250 (n=1630)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1351 (IC base=+0.241)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.243 (n=1356)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.241)

- **PATRÓN** `libro_liquidez` > `2051.9316` → IC=+0.255 (n=858)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2051.9316 (IC base=+0.241)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.257 (n=1057)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.241)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.197 (n=1250)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0039 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.4207` → IC=+0.158 (n=2841)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.4207 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.160 (n=2949)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 5.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` > `0.2483` → IC=+0.194 (n=2841)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 0.2483 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.141` → IC=+0.171 (n=1513)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.141 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.136` → IC=+0.160 (n=1150)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 4.136 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `0.8653` → IC=+0.165 (n=1894)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.8653 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.2805` → IC=+0.190 (n=369)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.2805 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `1.5247` → IC=+0.161 (n=1220)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 1.5247 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` > `2.1683` → IC=+0.158 (n=1257)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 2.1683 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `6327.6958` → IC=+0.243 (n=1288)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6327.6958 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `74.0` → IC=+0.174 (n=1209)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 74.0 (IC base=+0.146)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.149 (n=2364)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0075 (IC base=+0.128)

- **PATRÓN** `drift_60min` |x|≤ `0.4405` → IC=+0.139 (n=2362)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.4405 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.153 (n=860)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 17.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` < `0.7373` → IC=+0.183 (n=2362)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.7373 (IC base=+0.128)

- **PATRÓN** `dist_vwap_pct` < `0.1467` → IC=+0.143 (n=2143)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.1467 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.137` → IC=+0.170 (n=359)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 11.137 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` < `0.6992` → IC=+0.141 (n=1039)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 0.6992 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` > `0.2969` → IC=+0.223 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2969 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` > `1.4309` → IC=+0.135 (n=2270)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.4309 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `7246.0232` → IC=+0.214 (n=787)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7246.0232 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `67.0` → IC=+0.130 (n=773)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 67.0 (IC base=+0.128)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0103` → IC=+0.155 (n=1301)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` > 0.0103 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.177 (n=1048)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 17.0 (IC base=+0.124)

- **PATRÓN** `ibs_20min` > `0.4432` → IC=+0.198 (n=2858)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.4432 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` > `1.0677` → IC=+0.207 (n=496)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0677 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.741` → IC=+0.268 (n=722)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.741 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` < `1.2209` → IC=+0.135 (n=2858)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 1.2209 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` < `0.098` → IC=+0.125 (n=2697)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` < 0.098 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` > `0.2785` → IC=+0.133 (n=369)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` > 0.2785 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` < `1.8319` → IC=+0.127 (n=1861)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 1.8319 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` > `1.4632` → IC=+0.126 (n=2792)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` > 1.4632 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.136 (n=1948)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `2496.4887` → IC=+0.230 (n=1296)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2496.4887 (IC base=+0.124)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.146 (n=891)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 24.0 (IC base=+0.124)

- **PATRÓN** `sigma_h` < `0.01` → IC=+0.151 (n=2399)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.01 (IC base=+0.117)

- **PATRÓN** `drift_60min` |x|≤ `0.1335` → IC=+0.156 (n=908)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.1335 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.130 (n=2806)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 5.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` < `0.6463` → IC=+0.211 (n=2722)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6463 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` < `0.2146` → IC=+0.136 (n=2341)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.2146 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.263` → IC=+0.134 (n=2622)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` < 3.263 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` < `0.7108` → IC=+0.139 (n=1199)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 0.7108 (IC base=+0.117)

- **PATRÓN** `volumen_pendiente_norm` > `0.2248` → IC=+0.172 (n=464)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.2248 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` < `1.442` → IC=+0.156 (n=850)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.442 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `2673.0949` → IC=+0.207 (n=908)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2673.0949 (IC base=+0.117)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.134 (n=2236)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 47.0 (IC base=+0.117)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0136` → IC=+0.249 (n=2417)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0136 (IC base=+0.229)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.235 (n=2820)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.229)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.237 (n=1808)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.229)

- **PATRÓN** `ibs_20min` > `0.61` → IC=+0.271 (n=2417)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.61 (IC base=+0.229)

- **PATRÓN** `dist_vwap_pct` > `0.1894` → IC=+0.246 (n=1467)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1894 (IC base=+0.229)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.744` → IC=+0.269 (n=906)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.744 (IC base=+0.229)

- **PATRÓN** `volumen_regimen` < `1.2287` → IC=+0.237 (n=2703)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2287 (IC base=+0.229)

- **PATRÓN** `volumen_regimen` > `0.6399` → IC=+0.232 (n=2703)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6399 (IC base=+0.229)

- **PATRÓN** `volumen_pendiente_norm` > `0.2873` → IC=+0.254 (n=340)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2873 (IC base=+0.229)

- **PATRÓN** `volumen_spike_ratio` > `2.4984` → IC=+0.247 (n=877)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4984 (IC base=+0.229)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.231 (n=3510)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.229)

- **PATRÓN** `libro_liquidez` > `2623.5735` → IC=+0.237 (n=1802)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2623.5735 (IC base=+0.229)

- **PATRÓN** `sigma_h` > `0.0255` → IC=+0.251 (n=936)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0255 (IC base=+0.229)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.236 (n=2640)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.229)

- **PATRÓN** `ibs_20min` < `0.5144` → IC=+0.264 (n=2809)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5144 (IC base=+0.229)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.19` → IC=+0.266 (n=537)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.19 (IC base=+0.229)

- **PATRÓN** `volumen_regimen` > `1.2299` → IC=+0.258 (n=936)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2299 (IC base=+0.229)

- **PATRÓN** `volumen_pendiente_norm` > `0.2816` → IC=+0.298 (n=374)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2816 (IC base=+0.229)

- **PATRÓN** `volumen_spike_ratio` > `1.432` → IC=+0.232 (n=2606)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.432 (IC base=+0.229)

- **PATRÓN** `libro_liquidez` > `2374.1526` → IC=+0.229 (n=2509)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2374.1526 (IC base=+0.229)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.193 (n=4894)

- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.245 (n=1678)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=+0.208)

- **PATRÓN** `drift_60min` |x|≤ `0.5048` → IC=+0.218 (n=5029)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5048 (IC base=+0.208)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.223 (n=1827)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.208)

- **PATRÓN** `ibs_20min` > `0.9401` → IC=+0.248 (n=1679)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9401 (IC base=+0.208)

- **PATRÓN** `dist_vwap_pct` > `0.1706` → IC=+0.208 (n=1864)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1706 (IC base=+0.208)

- **PATRÓN** `dist_vwap_pct` < `0.4307` → IC=+0.212 (n=3612)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4307 (IC base=+0.208)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.02` → IC=+0.214 (n=821)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.02 (IC base=+0.208)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.617` → IC=+0.209 (n=4479)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.617 (IC base=+0.208)

- **PATRÓN** `volumen_regimen` < `0.7046` → IC=+0.220 (n=1607)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7046 (IC base=+0.208)

- **PATRÓN** `volumen_pendiente_norm` < `0.1066` → IC=+0.208 (n=4698)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1066 (IC base=+0.208)

- **PATRÓN** `volumen_pendiente_norm` > `0.1669` → IC=+0.222 (n=1413)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1669 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` < `1.4555` → IC=+0.214 (n=1651)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4555 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` > `1.8464` → IC=+0.209 (n=3301)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8464 (IC base=+0.208)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.213 (n=3866)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.208)

- **PATRÓN** `libro_liquidez` > `2926.428` → IC=+0.214 (n=4493)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2926.428 (IC base=+0.208)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.240 (n=1228)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.191)

- **PATRÓN** `drift_60min` |x|≤ `0.4897` → IC=+0.207 (n=3683)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4897 (IC base=+0.191)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.212 (n=1246)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.207 (n=1643)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.191)

- **PATRÓN** `ibs_20min` < `0.7333` → IC=+0.198 (n=3684)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.7333 (IC base=+0.191)

- **PATRÓN** `dist_vwap_pct` > `0.6743` → IC=+0.200 (n=624)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6743 (IC base=+0.191)

- **PATRÓN** `dist_vwap_pct` < `0.4192` → IC=+0.189 (n=3713)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` < 0.4192 (IC base=+0.191)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.841` → IC=+0.202 (n=3298)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.841 (IC base=+0.191)

- **PATRÓN** `volumen_regimen` < `1.0971` → IC=+0.201 (n=3070)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0971 (IC base=+0.191)

- **PATRÓN** `volumen_pendiente_norm` < `0.0976` → IC=+0.195 (n=3376)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` < 0.0976 (IC base=+0.191)

- **PATRÓN** `volumen_pendiente_norm` > `0.2229` → IC=+0.193 (n=745)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2229 (IC base=+0.191)

- **PATRÓN** `volumen_spike_ratio` < `1.5338` → IC=+0.196 (n=1598)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 1.5338 (IC base=+0.191)

- **PATRÓN** `volumen_spike_ratio` > `2.1904` → IC=+0.200 (n=1646)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1904 (IC base=+0.191)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.193 (n=4894)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.01 (IC base=+0.191)

- **PATRÓN** `ballena_activa_n` < `177.0` → IC=+0.200 (n=3176)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 177.0 (IC base=+0.191)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.274 (n=663)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.257)

- **PATRÓN** `drift_60min` |x|≤ `0.0855` → IC=+0.292 (n=253)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0855 (IC base=+0.257)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.262 (n=753)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.257)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.260 (n=336)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.257)

- **PATRÓN** `ibs_20min` < `0.4903` → IC=+0.274 (n=503)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4903 (IC base=+0.257)

- **PATRÓN** `dist_vwap_pct` < `0.1871` → IC=+0.269 (n=681)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1871 (IC base=+0.257)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.071` → IC=+0.270 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.071 (IC base=+0.257)

- **PATRÓN** `volumen_regimen` < `1.2148` → IC=+0.265 (n=754)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2148 (IC base=+0.257)

- **PATRÓN** `volumen_regimen` > `0.8658` → IC=+0.266 (n=502)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8658 (IC base=+0.257)

- **PATRÓN** `volumen_pendiente_norm` > `0.2917` → IC=+0.358 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2917 (IC base=+0.257)

- **PATRÓN** `volumen_spike_ratio` < `1.8257` → IC=+0.263 (n=501)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8257 (IC base=+0.257)

- **PATRÓN** `libro_liquidez` > `16282.3675` → IC=+0.267 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16282.3675 (IC base=+0.257)

- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.233 (n=874)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.176)

- **PATRÓN** `drift_60min` |x|≤ `0.369` → IC=+0.192 (n=1309)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.369 (IC base=+0.176)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.222 (n=476)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.201 (n=480)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.176)

- **PATRÓN** `ibs_20min` < `0.1385` → IC=+0.206 (n=576)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1385 (IC base=+0.176)

- **PATRÓN** `ibs_20min` > `0.6084` → IC=+0.178 (n=594)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.6084 (IC base=+0.176)

- **PATRÓN** `dist_vwap_pct` > `0.7` → IC=+0.186 (n=116)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.7 (IC base=+0.176)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.379` → IC=+0.194 (n=1290)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` < 6.379 (IC base=+0.176)

- **PATRÓN** `volumen_regimen` < `1.2228` → IC=+0.191 (n=1309)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 1.2228 (IC base=+0.176)

- **PATRÓN** `volumen_pendiente_norm` > `0.2196` → IC=+0.199 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2196 (IC base=+0.176)

- **PATRÓN** `volumen_spike_ratio` < `2.5013` → IC=+0.182 (n=1302)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 2.5013 (IC base=+0.176)

- **PATRÓN** `volumen_spike_ratio` > `1.8045` → IC=+0.186 (n=868)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 1.8045 (IC base=+0.176)

- **PATRÓN** `libro_liquidez` > `14889.24` → IC=+0.186 (n=594)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 14889.24 (IC base=+0.176)

- **PATRÓN** `ballena_activa_n` < `696.0` → IC=+0.188 (n=1265)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 696.0 (IC base=+0.176)

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
- **PATRÓN** `sigma_h` < `0.008` → IC=+0.213 (n=1375)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.008 (IC base=+0.197)

- **PATRÓN** `drift_60min` |x|≤ `0.4596` → IC=+0.204 (n=1375)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4596 (IC base=+0.197)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.215 (n=499)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.197)

- **PATRÓN** `ibs_20min` < `0.5189` → IC=+0.209 (n=917)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5189 (IC base=+0.197)

- **PATRÓN** `ibs_20min` > `0.8776` → IC=+0.199 (n=459)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.8776 (IC base=+0.197)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.114` → IC=+0.205 (n=1237)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.114 (IC base=+0.197)

- **PATRÓN** `volumen_regimen` < `0.8782` → IC=+0.200 (n=917)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8782 (IC base=+0.197)

- **PATRÓN** `volumen_regimen` > `1.2314` → IC=+0.203 (n=460)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2314 (IC base=+0.197)

- **PATRÓN** `volumen_pendiente_norm` < `0.105` → IC=+0.200 (n=1264)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.105 (IC base=+0.197)

- **PATRÓN** `volumen_spike_ratio` < `2.4554` → IC=+0.205 (n=1346)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4554 (IC base=+0.197)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.198 (n=1411)

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
- **PATRÓN** `sigma_h` < `0.0107` → IC=+0.202 (n=645)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0107 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.201 (n=754)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 3.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` > `0.925` → IC=+0.246 (n=333)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.925 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` > `0.743` → IC=+0.238 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.743 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.204` → IC=+0.212 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.204 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` < `0.6985` → IC=+0.226 (n=323)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6985 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` < `0.1062` → IC=+0.191 (n=661)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` < 0.1062 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.079` → IC=+0.191 (n=328)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.079 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` < `1.5672` → IC=+0.196 (n=314)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 1.5672 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `2.4815` → IC=+0.204 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4815 (IC base=+0.180)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.186 (n=854)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.02 (IC base=+0.180)

- **PATRÓN** `libro_liquidez` > `3548.428` → IC=+0.211 (n=489)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3548.428 (IC base=+0.180)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.198 (n=716)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 52.0 (IC base=+0.180)

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
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.156 (n=724)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0039 (IC base=+0.072)

- **PATRÓN** `ibs_20min` > `0.3947` → IC=+0.148 (n=1548)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` > 0.3947 (IC base=+0.072)

- **PATRÓN** `dist_vwap_pct` > `0.3558` → IC=+0.159 (n=544)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.3558 (IC base=+0.072)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.993` → IC=+0.167 (n=451)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 8.993 (IC base=+0.072)

- **PATRÓN** `ibs_20min` < `0.2016` → IC=+0.237 (n=557)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2016 (IC base=+0.058)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.358` → IC=+0.169 (n=131)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 10.358 (IC base=+0.058)

- **PATRÓN** `volumen_pendiente_norm` > `0.1468` → IC=+0.177 (n=230)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.1468 (IC base=+0.058)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.133 (n=548)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.66€ cuando `sigma_h` < 0.0056 (IC base=+0.088)

- **PATRÓN** `ibs_20min` > `0.5149` → IC=+0.191 (n=461)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.5149 (IC base=+0.088)

- **PATRÓN** `dist_vwap_pct` > `0.1218` → IC=+0.157 (n=260)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.1218 (IC base=+0.088)

- **PATRÓN** `ibs_20min` < `0.0544` → IC=+0.283 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0544 (IC base=+0.075)

- **PATRÓN** `volumen_pendiente_norm` > `0.2162` → IC=+0.199 (n=71)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2162 (IC base=+0.075)

### GBM_LATE_60M#ETH#60min
- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.131 (n=472)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.65€ cuando `sigma_h` < 0.0059 (IC base=+0.096)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.160 (n=204)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 17.0 (IC base=+0.096)

- **PATRÓN** `ibs_20min` > `0.6203` → IC=+0.209 (n=451)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6203 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` > `0.1246` → IC=+0.196 (n=264)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.1246 (IC base=+0.096)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.194` → IC=+0.261 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.194 (IC base=+0.096)

- **PATRÓN** `volumen_regimen` < `0.8144` → IC=+0.128 (n=337)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 0.8144 (IC base=+0.096)

- **PATRÓN** `volumen_pendiente_norm` > `0.2854` → IC=+0.171 (n=71)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.2854 (IC base=+0.096)

- **PATRÓN** `ibs_20min` < `0.0314` → IC=+0.302 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0314 (IC base=+0.020)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.686` → IC=+0.233 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.686 (IC base=+0.020)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `ibs_20min` > `0.1379` → IC=-0.202 (n=65)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1379
  - _Potencial_: sin este filtro IC_bueno=+0.226 (n=199)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.169 (n=354)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` > 0.75 (IC base=+0.033)

- **PATRÓN** `dist_vwap_pct` > `0.4722` → IC=+0.126 (n=188)

  - _Acción_: Kelly boost +0.63€ cuando `dist_vwap_pct` > 0.4722 (IC base=+0.033)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.381` → IC=+0.167 (n=112)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 9.381 (IC base=+0.033)

- **PATRÓN** `volumen_pendiente_norm` > `0.2317` → IC=+0.131 (n=101)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_pendiente_norm` > 0.2317 (IC base=+0.033)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.154 (n=229)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0103 (IC base=+0.076)

- **PATRÓN** `ibs_20min` < `0.1379` → IC=+0.226 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1379 (IC base=+0.076)

- **PATRÓN** `dist_vwap_pct` > `0.2223` → IC=+0.147 (n=49)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.2223 (IC base=+0.076)

- **PATRÓN** `dist_vwap_pct` < `0.1716` → IC=+0.147 (n=185)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.1716 (IC base=+0.076)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.739` → IC=+0.304 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.739 (IC base=+0.076)

- **PATRÓN** `volumen_regimen` > `1.0818` → IC=+0.221 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0818 (IC base=+0.076)

- **PATRÓN** `volumen_pendiente_norm` > `0.1518` → IC=+0.246 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1518 (IC base=+0.076)

- **PATRÓN** `volumen_spike_ratio` > `1.4089` → IC=+0.174 (n=176)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 1.4089 (IC base=+0.076)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.157 (n=170)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.06 (IC base=+0.076)

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
  - _Potencial_: sin este filtro IC_bueno=-0.264 (n=193)

- **FILTRO** `dist_vwap_pct` > `0.4428` → IC=-0.409 (n=20)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4428
  - _Potencial_: sin este filtro IC_bueno=-0.270 (n=237)

- **FILTRO** `volumen_pendiente_norm` > `0.0465` → IC=-0.371 (n=29)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0465
  - _Potencial_: sin este filtro IC_bueno=-0.264 (n=142)

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

- **FILTRO** `sigma_h` > `0.0042` → IC=-0.267 (n=28)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0042
  - _Potencial_: sin este filtro IC_bueno=-0.247 (n=85)

- **FILTRO** `volumen_regimen` > `0.8213` → IC=-0.333 (n=28)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8213
  - _Potencial_: sin este filtro IC_bueno=-0.224 (n=85)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.6627` → IC=-0.443 (n=33)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6627
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=68)

- **FILTRO** `sigma_h` > `0.0048` → IC=-0.346 (n=24)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0048
  - _Potencial_: sin este filtro IC_bueno=-0.263 (n=74)

- **FILTRO** `hora_utc` < `6.0` → IC=-0.375 (n=22)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.256 (n=76)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.277 (n=83)

- **FILTRO** `libro_liquidez` < `1541.8747` → IC=-0.304 (n=49)

  - _Acción_: SKIP cuando `libro_liquidez` < 1541.8747
  - _Potencial_: sin este filtro IC_bueno=-0.265 (n=49)

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

- **FILTRO** `volumen_regimen` < `0.9949` → IC=-0.420 (n=23)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9949
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=23)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` > `0.1622` → IC=-0.124 (n=275)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1622
  - _Potencial_: sin este filtro IC_bueno=+0.154 (n=535)

- **PATRÓN** `sigma_h` > `0.006` → IC=+0.186 (n=234)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.006 (IC base=+0.113)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.178 (n=200)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 17.0 (IC base=+0.113)

- **PATRÓN** `ibs_20min` > `0.6842` → IC=+0.151 (n=516)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` > 0.6842 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` > `0.741` → IC=+0.207 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.741 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` < `0.6275` → IC=+0.174 (n=173)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.6275 (IC base=+0.113)

- **PATRÓN** `volumen_pendiente_norm` < `0.2267` → IC=+0.144 (n=464)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_pendiente_norm` < 0.2267 (IC base=+0.113)

- **PATRÓN** `volumen_spike_ratio` < `1.7943` → IC=+0.156 (n=277)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.7943 (IC base=+0.113)

- **PATRÓN** `ibs_20min` < `0.1622` → IC=+0.154 (n=535)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.1622 (IC base=+0.059)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.099` → IC=+0.185 (n=182)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 9.099 (IC base=+0.059)

- **PATRÓN** `volumen_pendiente_norm` > `0.2227` → IC=+0.124 (n=123)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` > 0.2227 (IC base=+0.059)

- **PATRÓN** `libro_liquidez` > `3239.2397` → IC=+0.139 (n=405)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 3239.2397 (IC base=+0.059)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.6781` → IC=-0.222 (n=52)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6781
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=159)

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
  - _Potencial_: sin este filtro IC_bueno=+0.111 (n=196)

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

- **PATRÓN** `sigma_ewma_delta_pct` > `11.059` → IC=+0.232 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.059 (IC base=+0.027)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.4` → IC=-0.278 (n=34)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=104)

- **FILTRO** `volumen_spike_ratio` > `2.1066` → IC=-0.194 (n=34)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.1066
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=67)

- **PATRÓN** `hora_utc` > `13.0` → IC=+0.308 (n=118)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 13.0 (IC base=+0.247)

- **PATRÓN** `ibs_20min` > `0.6522` → IC=+0.272 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6522 (IC base=+0.247)

- **PATRÓN** `dist_vwap_pct` > `0.6843` → IC=+0.384 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6843 (IC base=+0.247)

- **PATRÓN** `dist_vwap_pct` < `0.2335` → IC=+0.253 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2335 (IC base=+0.247)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.318` → IC=+0.317 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.318 (IC base=+0.247)

- **PATRÓN** `volumen_regimen` < `0.5821` → IC=+0.320 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.5821 (IC base=+0.247)

- **PATRÓN** `volumen_pendiente_norm` > `0.1057` → IC=+0.331 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1057 (IC base=+0.247)

- **PATRÓN** `volumen_spike_ratio` < `1.4907` → IC=+0.395 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4907 (IC base=+0.247)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.247 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.247)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.321` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.321 (IC base=-0.086)

### LATE_WINDOW_5MIN
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.329 (n=68)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3349` → IC=+0.320 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3349 (IC base=+0.312)

- **PATRÓN** `elapsed_s` > `184.3` → IC=+0.385 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 184.3 (IC base=+0.312)

- **PATRÓN** `drift_15min` |x|≤ `1.0295` → IC=+0.455 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0295 (IC base=+0.312)

- **PATRÓN** `drift_60min` |x|≤ `0.969` → IC=+0.369 (n=59)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.969 (IC base=+0.312)

- **PATRÓN** `ballena_activa_n` < `1114.0` → IC=+0.364 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1114.0 (IC base=+0.312)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3369` → IC=+0.258 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3369 (IC base=+0.236)

- **PATRÓN** `elapsed_s` > `186.2` → IC=+0.246 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 186.2 (IC base=+0.236)

- **PATRÓN** `elapsed_s` < `216.4` → IC=+0.263 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 216.4 (IC base=+0.236)

- **PATRÓN** `drift_15min` |x|≤ `1.4538` → IC=+0.339 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.4538 (IC base=+0.236)

- **PATRÓN** `drift_60min` |x|≤ `0.947` → IC=+0.273 (n=64)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.947 (IC base=+0.236)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.329 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.236)

- **PATRÓN** `ballena_activa_n` < `1854.0` → IC=+0.288 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1854.0 (IC base=+0.236)

### LATE_WINDOW_5MIN#BTC#5min
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.329 (n=68)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3349` → IC=+0.320 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3349 (IC base=+0.312)

- **PATRÓN** `elapsed_s` > `184.3` → IC=+0.385 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 184.3 (IC base=+0.312)

- **PATRÓN** `drift_15min` |x|≤ `1.0295` → IC=+0.455 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0295 (IC base=+0.312)

- **PATRÓN** `drift_60min` |x|≤ `0.969` → IC=+0.369 (n=59)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.969 (IC base=+0.312)

- **PATRÓN** `ballena_activa_n` < `1114.0` → IC=+0.364 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1114.0 (IC base=+0.312)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3369` → IC=+0.258 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3369 (IC base=+0.236)

- **PATRÓN** `elapsed_s` > `186.2` → IC=+0.246 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 186.2 (IC base=+0.236)

- **PATRÓN** `elapsed_s` < `216.4` → IC=+0.263 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 216.4 (IC base=+0.236)

- **PATRÓN** `drift_15min` |x|≤ `1.4538` → IC=+0.339 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.4538 (IC base=+0.236)

- **PATRÓN** `drift_60min` |x|≤ `0.947` → IC=+0.273 (n=64)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.947 (IC base=+0.236)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.329 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.236)

- **PATRÓN** `ballena_activa_n` < `1854.0` → IC=+0.288 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1854.0 (IC base=+0.236)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `libro_liquidez` > `2851.1607` → IC=+0.134 (n=560)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 2851.1607 (IC base=+0.099)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `libro_liquidez` > `2851.1607` → IC=+0.134 (n=560)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 2851.1607 (IC base=+0.099)

### LIQUIDACIONES_15M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=190)

- **FILTRO** `libro_liquidez` < `2842.6585` → IC=-0.198 (n=51)

  - _Acción_: SKIP cuando `libro_liquidez` < 2842.6585
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=155)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=293)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `libro_liquidez` < `10724.0239` → IC=-0.208 (n=22)

  - _Acción_: SKIP cuando `libro_liquidez` < 10724.0239
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=68)

- **FILTRO** `liq_n` < `5.0` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `liq_n` < 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.184 (n=17)

- **FILTRO** `py_entrada` < `0.515` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.081 (n=29)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `ballena_activa_n` > `66.0` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `ballena_activa_n` > 66.0
  - _Potencial_: sin este filtro IC_bueno=+0.200 (n=8)

- **FILTRO** `ballena_activa_n` > `55.0` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `ballena_activa_n` > 55.0
  - _Potencial_: sin este filtro IC_bueno=+0.143 (n=12)

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
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=3481)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.160 (n=104)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.160 (n=104)

- **FILTRO** `ballena_activa_n` > `115.0` → IC=-0.205 (n=59)

  - _Acción_: SKIP cuando `ballena_activa_n` > 115.0
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=32)

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
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=1273)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=1227)

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
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=714)

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
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=414)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=395)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.140 (n=173)

  - _Acción_: Kelly boost +0.70€ cuando `py_entrada` < 0.495 (IC base=+0.021)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=838)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=838)

- **FILTRO** `py_entrada` < `0.44` → IC=-0.132 (n=259)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=659)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=799)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=799)

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
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=222)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=246)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=254)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=348)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=348)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.120 (n=185)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=193)

- **FILTRO** `libro_liquidez` < `612.0892` → IC=-0.135 (n=124)

  - _Acción_: SKIP cuando `libro_liquidez` < 612.0892
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=254)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=255)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.129 (n=87)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=183)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.4` → IC=-0.121 (n=1340)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=3503)

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
- **PATRÓN** `py_entrada` < `0.46` → IC=+0.174 (n=142)

  - _Acción_: Kelly boost +0.87€ cuando `py_entrada` < 0.46 (IC base=+0.009)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.184 (n=55)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=246)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.151 (n=147)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=167)

- **PATRÓN** `py_entrada` < `0.57` → IC=+0.125 (n=78)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` < 0.57 (IC base=+0.061)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.53` → IC=-0.126 (n=335)

  - _Acción_: SKIP cuando `py_entrada` < 0.53
  - _Potencial_: sin este filtro IC_bueno=+0.107 (n=120)

- **FILTRO** `profundidad_ratio` < `56.1` → IC=-0.158 (n=150)

  - _Acción_: SKIP cuando `profundidad_ratio` < 56.1
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=305)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.139 (n=189)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=212)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `profundidad_ratio` < `21.2` → IC=-0.141 (n=140)

  - _Acción_: SKIP cuando `profundidad_ratio` < 21.2
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=287)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.171 (n=83)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=350)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.123 (n=279)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=302)

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
- **FILTRO** `py_entrada` < `0.47` → IC=-0.165 (n=5878)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=18304)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.174 (n=5995)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=18854)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.194 (n=1078)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.116 (n=3313)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.172 (n=1030)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.068 (n=3414)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.144 (n=1152)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` > 1.0 (IC base=+0.040)

- **PATRÓN** `libro_liquidez` > `1329.3248` → IC=+0.136 (n=2196)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 1329.3248 (IC base=+0.040)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.127 (n=2070)

  - _Acción_: Kelly boost +0.64€ cuando `py_entrada` < 0.5 (IC base=+0.012)

- **PATRÓN** `libro_liquidez` > `1504.9852` → IC=+0.152 (n=1511)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 1504.9852 (IC base=+0.012)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.157 (n=814)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=2736)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.177 (n=866)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=2661)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.174 (n=1076)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.107 (n=3328)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.200 (n=1061)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.074 (n=3474)

- **PATRÓN** `ibs_20min` > `0.9643` → IC=+0.131 (n=1501)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` > 0.9643 (IC base=+0.038)

- **PATRÓN** `libro_liquidez` > `1821.4584` → IC=+0.125 (n=1498)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 1821.4584 (IC base=+0.038)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.155 (n=1066)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.082 (n=3330)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=2362)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.162 (n=758)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=2300)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.208 (n=761)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=2784)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=3524)

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
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=867)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `py_entrada` < `0.395` → IC=-0.230 (n=72)

  - _Acción_: SKIP cuando `py_entrada` < 0.395
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=262)

- **FILTRO** `ibs_20min` < `0.1975` → IC=-0.223 (n=110)

  - _Acción_: SKIP cuando `ibs_20min` < 0.1975
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=224)

- **FILTRO** `py_entrada` > `0.615` → IC=-0.216 (n=86)

  - _Acción_: SKIP cuando `py_entrada` > 0.615
  - _Potencial_: sin este filtro IC_bueno=-0.103 (n=353)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=909)

- **FILTRO** `libro_liquidez` < `1756.5026` → IC=-0.162 (n=232)

  - _Acción_: SKIP cuando `libro_liquidez` < 1756.5026
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=696)

- **FILTRO** `libro_liquidez` < `2083.4373` → IC=-0.168 (n=347)

  - _Acción_: SKIP cuando `libro_liquidez` < 2083.4373
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=705)

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
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=37156)

- **FILTRO** `py_entrada` < `0.33` → IC=-0.285 (n=13223)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=40653)

- **FILTRO** `ibs_7min` < `0.2386` → IC=-0.229 (n=13464)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2386
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=40412)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.152 (n=18013)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=35863)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.240 (n=16610)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=51247)

- **FILTRO** `ibs_7min` > `0.2857` → IC=-0.182 (n=16793)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2857
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=51064)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.146 (n=2696)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=6696)

- **FILTRO** `py_entrada` < `0.46` → IC=-0.236 (n=4646)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=4746)

- **FILTRO** `ibs_7min` < `0.7121` → IC=-0.244 (n=3098)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7121
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=6294)

- **FILTRO** `ballena_activa_n` > `6.0` → IC=-0.178 (n=2015)

  - _Acción_: SKIP cuando `ballena_activa_n` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=7377)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.270 (n=2912)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=8852)

- **FILTRO** `ibs_7min` > `0.7709` → IC=-0.210 (n=2940)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7709
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=8824)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.265 (n=2118)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=6984)

- **FILTRO** `ibs_7min` < `0.7268` → IC=-0.199 (n=2275)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7268
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=6827)

- **FILTRO** `ballena_activa_n` > `154.0` → IC=-0.192 (n=2258)

  - _Acción_: SKIP cuando `ballena_activa_n` > 154.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=6844)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.262 (n=2281)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=6959)

- **FILTRO** `ibs_7min` > `0.2686` → IC=-0.195 (n=2309)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2686
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=6931)

- **FILTRO** `ballena_activa_n` > `151.0` → IC=-0.184 (n=2297)

  - _Acción_: SKIP cuando `ballena_activa_n` > 151.0
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=6943)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.159 (n=2200)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=6726)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.316 (n=2192)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=6734)

- **FILTRO** `ibs_7min` < `0.2978` → IC=-0.246 (n=2945)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2978
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=5981)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.195 (n=2134)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=6792)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.254 (n=2915)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=9612)

- **FILTRO** `ibs_7min` > `0.7342` → IC=-0.177 (n=3130)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7342
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=9397)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.262 (n=2055)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=6724)

- **FILTRO** `ibs_7min` < `0.7301` → IC=-0.187 (n=2194)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7301
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=6585)

- **FILTRO** `ballena_activa_n` > `27.0` → IC=-0.189 (n=2181)

  - _Acción_: SKIP cuando `ballena_activa_n` > 27.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=6598)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.269 (n=2042)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=7065)

- **FILTRO** `ibs_7min` > `0.275` → IC=-0.181 (n=2276)

  - _Acción_: SKIP cuando `ibs_7min` > 0.275
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=6831)

- **FILTRO** `ballena_activa_n` > `26.0` → IC=-0.175 (n=2252)

  - _Acción_: SKIP cuando `ballena_activa_n` > 26.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=6855)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.283 (n=2110)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=6736)

- **FILTRO** `ibs_7min` < `0.2143` → IC=-0.232 (n=2196)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2143
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=6650)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.219 (n=2130)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=6716)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.189 (n=3130)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=9830)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.32` → IC=-0.291 (n=2069)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=6762)

- **FILTRO** `ibs_7min` < `0.2069` → IC=-0.221 (n=2206)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2069
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=6625)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.201 (n=1977)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=6854)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.215 (n=2984)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=9275)

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
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=493)

- **FILTRO** `py_entrada` > `0.545` → IC=-0.152 (n=156)

  - _Acción_: SKIP cuando `py_entrada` > 0.545
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=546)

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
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=848)

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

- **FILTRO** `libro_liquidez` < `3257.5356` → IC=-0.159 (n=174)

  - _Acción_: SKIP cuando `libro_liquidez` < 3257.5356
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=525)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=387)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.3982` → IC=+0.141 (n=1146)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.71€ cuando `delta_ratio` |x|> 0.3982 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.133 (n=537)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 14.0 (IC base=+0.130)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.133 (n=431)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 4.0 (IC base=+0.130)

- **PATRÓN** `total_vol_5m` < `134023.4` → IC=+0.144 (n=1008)

  - _Acción_: Kelly boost +0.72€ cuando `total_vol_5m` < 134023.4 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `3639.8241` → IC=+0.151 (n=519)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 3639.8241 (IC base=+0.130)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.150 (n=372)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 11.0 (IC base=+0.130)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.4376` → IC=+0.148 (n=89)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.74€ cuando `delta_ratio` |x|> 0.4376 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.215 (n=128)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.142)

- **PATRÓN** `total_vol_5m` < `289.181` → IC=+0.146 (n=179)

  - _Acción_: Kelly boost +0.73€ cuando `total_vol_5m` < 289.181 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `2584.1425` → IC=+0.214 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2584.1425 (IC base=+0.142)

- **PATRÓN** `ballena_activa_n` < `7.0` → IC=+0.167 (n=97)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 7.0 (IC base=+0.142)

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
- **PATRÓN** `delta_ratio` |x|> `0.4161` → IC=+0.182 (n=152)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.91€ cuando `delta_ratio` |x|> 0.4161 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.155 (n=236)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 4.0 (IC base=+0.137)

- **PATRÓN** `total_vol_5m` < `385.7846` → IC=+0.218 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 385.7846 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `7760.8` → IC=+0.143 (n=152)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 7760.8 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `70.0` → IC=+0.199 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 70.0 (IC base=+0.137)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.4326` → IC=+0.245 (n=92)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio` |x|> 0.4326 (IC base=+0.153)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.177 (n=187)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 15.0 (IC base=+0.153)

- **PATRÓN** `total_vol_5m` < `4970.298` → IC=+0.186 (n=135)

  - _Acción_: Kelly boost +0.93€ cuando `total_vol_5m` < 4970.298 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `3257.229` → IC=+0.167 (n=181)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 3257.229 (IC base=+0.153)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.157 (n=68)

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

- **FILTRO** `sigma_h` > `0.006` → IC=-0.304 (n=217)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.006
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=423)

- **FILTRO** `T_h` > `129.6211` → IC=-0.200 (n=158)

  - _Acción_: SKIP cuando `T_h` > 129.6211
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=482)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.181 (n=161)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0034 (IC base=-0.079)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0069` → IC=-0.337 (n=47)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0069
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=144)

- **FILTRO** `T_h` > `87.9957` → IC=-0.276 (n=47)

  - _Acción_: SKIP cuando `T_h` > 87.9957
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=144)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.300 (n=48)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=-0.034)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `pct_vs_K` |x|> `9.8932` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 9.8932
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=49)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0106` → IC=-0.244 (n=37)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0106
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=73)

- **FILTRO** `T_h` < `42.1838` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `T_h` < 42.1838
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=83)

- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.233 (n=28)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0054 (IC base=-0.089)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0102` → IC=-0.220 (n=452)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0102
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=151)

- **FILTRO** `T_h` > `70.6078` → IC=-0.200 (n=452)

  - _Acción_: SKIP cuando `T_h` > 70.6078
  - _Potencial_: sin este filtro IC_bueno=-0.141 (n=151)

- **FILTRO** `sigma_h` < `0.0049` → IC=-0.258 (n=126)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0049
  - _Potencial_: sin este filtro IC_bueno=-0.223 (n=384)

- **FILTRO** `pct_vs_K` |x|> `3.3088` → IC=-0.438 (n=127)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.3088
  - _Potencial_: sin este filtro IC_bueno=-0.162 (n=383)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `sigma_h` < `0.0044` → IC=-0.206 (n=49)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0044
  - _Potencial_: sin este filtro IC_bueno=-0.140 (n=148)

- **FILTRO** `pct_vs_K` |x|> `2.7876` → IC=-0.363 (n=49)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.7876
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=148)

- **FILTRO** `sigma_h` < `0.0046` → IC=-0.271 (n=59)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0046
  - _Potencial_: sin este filtro IC_bueno=-0.266 (n=122)

- **FILTRO** `T_h` > `144.2373` → IC=-0.287 (n=45)

  - _Acción_: SKIP cuando `T_h` > 144.2373
  - _Potencial_: sin este filtro IC_bueno=-0.261 (n=136)

- **FILTRO** `pct_vs_K` |x|> `2.9891` → IC=-0.436 (n=45)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.9891
  - _Potencial_: sin este filtro IC_bueno=-0.210 (n=136)

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
- **FILTRO** `pct_vs_K` |x|> `3.2523` → IC=-0.402 (n=59)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.2523
  - _Potencial_: sin este filtro IC_bueno=-0.175 (n=115)

- **FILTRO** `sigma_h` > `0.0088` → IC=-0.378 (n=39)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0088
  - _Potencial_: sin este filtro IC_bueno=-0.120 (n=119)

- **FILTRO** `sigma_h` < `0.005` → IC=-0.207 (n=39)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.005
  - _Potencial_: sin este filtro IC_bueno=-0.178 (n=119)

- **FILTRO** `T_h` > `57.7851` → IC=-0.283 (n=104)

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
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=124)

- **FILTRO** `T_h` > `94.227` → IC=-0.223 (n=110)

  - _Acción_: SKIP cuando `T_h` > 94.227
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=55)

- **FILTRO** `sigma_h` > `0.0132` → IC=-0.350 (n=38)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0132
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=74)

- **FILTRO** `sigma_h` < `0.0085` → IC=-0.263 (n=36)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0085
  - _Potencial_: sin este filtro IC_bueno=-0.231 (n=76)

- **FILTRO** `T_h` > `46.6251` → IC=-0.305 (n=75)

  - _Acción_: SKIP cuando `T_h` > 46.6251
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=37)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1224` → IC=+0.476 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1224 (IC base=+0.336)

- **PATRÓN** `sigma_h` < `0.0135` → IC=+0.351 (n=92)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0135 (IC base=+0.336)

- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.375 (n=62)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0099 (IC base=+0.336)

- **PATRÓN** `T_h` > `0.7758` → IC=+0.389 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.7758 (IC base=+0.336)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.477 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.336)

- **PATRÓN** `edge` > `0.099` → IC=+0.441 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.099 (IC base=+0.415)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.434 (n=196)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0081 (IC base=+0.415)

- **PATRÓN** `T_h` < `0.608` → IC=+0.434 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.608 (IC base=+0.415)

- **PATRÓN** `T_h` > `1.484` → IC=+0.422 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.484 (IC base=+0.415)

- **PATRÓN** `dist_50` > `0.3874` → IC=+0.459 (n=219)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3874 (IC base=+0.415)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.478 (n=136)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.415)

### RESOLUTION_SNIPER#BTC#sniper
- **PATRÓN** `dist_50` > `0.47` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.180)

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
- **PATRÓN** `edge` > `0.1885` → IC=+0.483 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1885 (IC base=+0.437)

- **PATRÓN** `sigma_h` < `0.016` → IC=+0.466 (n=57)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.016 (IC base=+0.437)

- **PATRÓN** `T_h` > `0.4307` → IC=+0.449 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.4307 (IC base=+0.437)

- **PATRÓN** `dist_50` > `0.3326` → IC=+0.466 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3326 (IC base=+0.437)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.438 (n=30)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.437)

- **PATRÓN** `edge` > `0.1961` → IC=+0.479 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1961 (IC base=+0.465)

- **PATRÓN** `sigma_h` < `0.0156` → IC=+0.479 (n=139)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0156 (IC base=+0.465)

- **PATRÓN** `T_h` > `1.1543` → IC=+0.479 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.1543 (IC base=+0.465)

- **PATRÓN** `dist_50` > `0.4373` → IC=+0.486 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4373 (IC base=+0.465)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.472 (n=143)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.465)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=302)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=380)

- **PATRÓN** `streak_estiramiento` < `0.5597` → IC=+0.182 (n=171)

  - _Acción_: Kelly boost +0.91€ cuando `streak_estiramiento` < 0.5597 (IC base=+0.043)

- **PATRÓN** `libro_liquidez` > `2756.3002` → IC=+0.150 (n=101)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2756.3002 (IC base=+0.043)

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

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.133 (n=115)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 7.0 (IC base=+0.085)

- **PATRÓN** `streak_estiramiento` < `0.4496` → IC=+0.184 (n=96)

  - _Acción_: Kelly boost +0.92€ cuando `streak_estiramiento` < 0.4496 (IC base=+0.085)

- **PATRÓN** `ballena_activa_n` < `29.0` → IC=+0.167 (n=85)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 29.0 (IC base=+0.085)

- **PATRÓN** `libro_liquidez` > `2414.7926` → IC=+0.155 (n=114)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 2414.7926 (IC base=+0.085)

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
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=986)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=1330)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=1129)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=1173)

### STRUCT_NO_15M
- **FILTRO** `hora_utc` < `14.0` → IC=-0.278 (n=16)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=18)

- **FILTRO** `py_entrada` < `0.455` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=19)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=3972)

### STRUCT_NO_15M#ETH#15min
- **FILTRO** `hora_utc` < `14.0` → IC=-0.278 (n=16)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=18)

- **FILTRO** `py_entrada` < `0.455` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=19)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=2180)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.197 (n=1546)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0053 (IC base=+0.179)

- **PATRÓN** `sigma_h` > `0.0119` → IC=+0.197 (n=1172)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` > 0.0119 (IC base=+0.179)

- **PATRÓN** `drift_60min` |x|≤ `0.1737` → IC=+0.193 (n=3092)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.1737 (IC base=+0.179)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.134` → IC=+0.189 (n=1398)

  - _Acción_: Kelly boost +0.94€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.134 (IC base=+0.179)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.187 (n=3250)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 6.0 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.182 (n=3241)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 15.0 (IC base=+0.179)

- **PATRÓN** `ibs_15` > `0.5625` → IC=+0.255 (n=3513)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5625 (IC base=+0.179)

- **PATRÓN** `dist_vwap_pct` > `0.1269` → IC=+0.170 (n=1687)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.1269 (IC base=+0.179)

- **PATRÓN** `dist_vwap_pct` < `0.4924` → IC=+0.167 (n=3131)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` < 0.4924 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.518` → IC=+0.254 (n=917)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.518 (IC base=+0.179)

- **PATRÓN** `libro_liquidez` > `4721.7851` → IC=+0.198 (n=1171)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 4721.7851 (IC base=+0.179)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=1391)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.243 (n=403)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0038 (IC base=+0.220)

- **PATRÓN** `drift_60min` |x|≤ `0.0585` → IC=+0.265 (n=202)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0585 (IC base=+0.220)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2522` → IC=+0.249 (n=201)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2522 (IC base=+0.220)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.240 (n=603)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.220)

- **PATRÓN** `ibs_15` > `0.7199` → IC=+0.285 (n=603)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7199 (IC base=+0.220)

- **PATRÓN** `dist_vwap_pct` > `0.2385` → IC=+0.243 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2385 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.108` → IC=+0.306 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.108 (IC base=+0.220)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.221 (n=782)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.220)

- **PATRÓN** `libro_liquidez` > `8999.1204` → IC=+0.229 (n=603)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8999.1204 (IC base=+0.220)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.189 (n=233)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0034 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.0491` → IC=+0.157 (n=234)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.0491 (IC base=+0.145)

- **PATRÓN** `drift_15min` |x|≤ `0.3957` → IC=+0.151 (n=233)

  - _Acción_: Kelly boost +0.76€ cuando `drift_15min` |x|≤ 0.3957 (IC base=+0.145)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1451` → IC=+0.151 (n=465)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.75€ cuando `delta_ratio_macro` |x|> 0.1451 (IC base=+0.145)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1326` → IC=+0.161 (n=275)

  - _Acción_: Kelly boost +0.80€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1326 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.155 (n=638)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 6.0 (IC base=+0.145)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.149 (n=697)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 16.0 (IC base=+0.145)

- **PATRÓN** `ibs_15` > `0.5467` → IC=+0.245 (n=697)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5467 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` > `0.1186` → IC=+0.160 (n=436)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.1186 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.827` → IC=+0.269 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.827 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `3209.7303` → IC=+0.154 (n=697)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 3209.7303 (IC base=+0.145)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `sigma_ewma_delta_pct` > `17.725` → IC=-0.183 (n=39)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 17.725
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=321)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `ibs_15` > `0.8947` → IC=+0.250 (n=258)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8947 (IC base=+0.096)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.134 (n=424)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.096)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `8.407` → IC=+0.149 (n=72)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 8.407 (IC base=+0.013)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0238` → IC=+0.244 (n=268)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0238 (IC base=+0.202)

- **PATRÓN** `drift_60min` |x|≤ `0.0857` → IC=+0.236 (n=354)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0857 (IC base=+0.202)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3354` → IC=+0.233 (n=707)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3354 (IC base=+0.202)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.217 (n=715)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.202)

- **PATRÓN** `ibs_15` > `0.5429` → IC=+0.282 (n=804)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5429 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` > `0.1887` → IC=+0.210 (n=409)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1887 (IC base=+0.202)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.101` → IC=+0.223 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.101 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `2968.8332` → IC=+0.300 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2968.8332 (IC base=+0.202)

- **PATRÓN** `ibs_15` < `0.1111` → IC=+0.157 (n=768)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.79€ cuando `ibs_15` < 0.1111 (IC base=+0.066)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.366 (n=415)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.366)

- **PATRÓN** `sigma_h` > `0.0056` → IC=+0.390 (n=207)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0056 (IC base=+0.366)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1505` → IC=+0.385 (n=415)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1505 (IC base=+0.366)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2297` → IC=+0.386 (n=357)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2297 (IC base=+0.366)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.380 (n=623)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.366)

- **PATRÓN** `ibs_15` > `0.788` → IC=+0.402 (n=622)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.788 (IC base=+0.366)

- **PATRÓN** `dist_vwap_pct` > `0.1452` → IC=+0.382 (n=363)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1452 (IC base=+0.366)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.671` → IC=+0.384 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.671 (IC base=+0.366)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.371 (n=756)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.366)

- **PATRÓN** `libro_liquidez` > `3840.073` → IC=+0.376 (n=555)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3840.073 (IC base=+0.366)

- **PATRÓN** `ballena_activa_n` < `422.0` → IC=+0.382 (n=549)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 422.0 (IC base=+0.366)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.368 (n=285)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.366)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.400 (n=108)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.366)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2146` → IC=+0.386 (n=147)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2146 (IC base=+0.366)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1413` → IC=+0.399 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1413 (IC base=+0.366)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.385 (n=302)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.366)

- **PATRÓN** `ibs_15` > `0.8066` → IC=+0.393 (n=324)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8066 (IC base=+0.366)

- **PATRÓN** `dist_vwap_pct` > `0.2448` → IC=+0.398 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2448 (IC base=+0.366)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.742` → IC=+0.378 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.742 (IC base=+0.366)

- **PATRÓN** `libro_liquidez` > `15400.5519` → IC=+0.393 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15400.5519 (IC base=+0.366)

- **PATRÓN** `ballena_activa_n` < `489.0` → IC=+0.414 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 489.0 (IC base=+0.366)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.366 (n=132)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.365)

- **PATRÓN** `sigma_h` > `0.0057` → IC=+0.383 (n=135)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0057 (IC base=+0.365)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0904` → IC=+0.377 (n=266)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0904 (IC base=+0.365)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2986` → IC=+0.383 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2986 (IC base=+0.365)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.389 (n=142)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.365)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.372 (n=139)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.365)

- **PATRÓN** `ibs_15` > `0.7485` → IC=+0.413 (n=298)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7485 (IC base=+0.365)

- **PATRÓN** `dist_vwap_pct` > `0.4536` → IC=+0.381 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4536 (IC base=+0.365)

- **PATRÓN** `dist_vwap_pct` < `0.2815` → IC=+0.366 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2815 (IC base=+0.365)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.889` → IC=+0.389 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.889 (IC base=+0.365)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.369 (n=334)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.365)

- **PATRÓN** `libro_liquidez` > `3951.6306` → IC=+0.391 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3951.6306 (IC base=+0.365)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0123` → IC=-0.224 (n=1066)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0123
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=3202)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.210 (n=1662)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=2606)

- **FILTRO** `libro_liquidez` < `4188.399` → IC=-0.152 (n=2816)

  - _Acción_: SKIP cuando `libro_liquidez` < 4188.399
  - _Potencial_: sin este filtro IC_bueno=+0.099 (n=1452)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1405` → IC=+0.187 (n=688)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.93€ cuando `delta_ratio_macro` |x|> 0.1405 (IC base=-0.067)

- **PATRÓN** `ibs_15` > `0.6341` → IC=+0.283 (n=1032)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6341 (IC base=-0.067)

- **PATRÓN** `dist_vwap_pct` > `0.1113` → IC=+0.209 (n=593)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1113 (IC base=-0.067)

- **PATRÓN** `dist_vwap_pct` < `0.4229` → IC=+0.201 (n=1007)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4229 (IC base=-0.067)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2304` → IC=+0.268 (n=1176)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2304 (IC base=-0.013)

- **PATRÓN** `ibs_15` < `0.361` → IC=+0.282 (n=3529)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.361 (IC base=-0.013)

- **PATRÓN** `dist_vwap_pct` > `0.6604` → IC=+0.279 (n=454)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6604 (IC base=-0.013)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0067` → IC=-0.217 (n=620)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0067
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=1864)

- **FILTRO** `sigma_h` < `0.0034` → IC=-0.229 (n=621)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=1863)

- **FILTRO** `hora_utc` < `15.0` → IC=-0.199 (n=1540)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=944)

- **FILTRO** `sigma_ewma_delta_pct` > `23.321` → IC=-0.267 (n=358)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 23.321
  - _Potencial_: sin este filtro IC_bueno=-0.183 (n=2126)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.216 (n=65)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.194 (n=2419)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.121 (n=743)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0053 (IC base=+0.097)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2047` → IC=+0.292 (n=152)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2047 (IC base=+0.097)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1125` → IC=+0.275 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1125 (IC base=+0.097)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.135 (n=360)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 15.0 (IC base=+0.097)

- **PATRÓN** `ibs_15` > `0.7566` → IC=+0.333 (n=334)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7566 (IC base=+0.097)

- **PATRÓN** `dist_vwap_pct` > `0.1047` → IC=+0.292 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1047 (IC base=+0.097)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.536` → IC=+0.133 (n=374)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` > 8.536 (IC base=+0.097)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0659` → IC=+0.212 (n=57)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0659 (IC base=-0.195)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.159` → IC=+0.278 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.159 (IC base=-0.195)

- **PATRÓN** `ibs_15` < `0.6255` → IC=+0.300 (n=58)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.6255 (IC base=-0.195)

- **PATRÓN** `dist_vwap_pct` < `0.0474` → IC=+0.276 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0474 (IC base=-0.195)

- **PATRÓN** `ballena_activa_n` < `291.0` → IC=+0.375 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 291.0 (IC base=-0.195)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.161 (n=670)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.165 (n=454)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0058 (IC base=+0.153)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.162 (n=344)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` > 0.0048 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.0692` → IC=+0.194 (n=227)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.0692 (IC base=+0.153)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3021` → IC=+0.192 (n=394)

  - _Acción_: Kelly boost +0.96€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3021 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.165 (n=517)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.153)

- **PATRÓN** `ibs_15` > `0.6098` → IC=+0.253 (n=516)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6098 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` > `0.4589` → IC=+0.164 (n=135)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.4589 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` < `0.1597` → IC=+0.154 (n=403)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.1597 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.422` → IC=+0.253 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.422 (IC base=+0.153)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.161 (n=670)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.01 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `10004.8873` → IC=+0.161 (n=172)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 10004.8873 (IC base=+0.153)

- **PATRÓN** `sigma_h` < `0.0077` → IC=+0.251 (n=1263)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0077 (IC base=+0.245)

- **PATRÓN** `drift_15min` |x|≤ `0.766` → IC=+0.257 (n=1111)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.766 (IC base=+0.245)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1586` → IC=+0.257 (n=842)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1586 (IC base=+0.245)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3339` → IC=+0.245 (n=1223)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3339 (IC base=+0.245)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.248 (n=898)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.245)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.248 (n=490)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.245)

- **PATRÓN** `ibs_15` < `0.3695` → IC=+0.275 (n=1263)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3695 (IC base=+0.245)

- **PATRÓN** `dist_vwap_pct` > `0.5987` → IC=+0.268 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5987 (IC base=+0.245)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.186` → IC=+0.257 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.186 (IC base=+0.245)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.505` → IC=+0.249 (n=1319)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.505 (IC base=+0.245)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `drift_60min` |x|> `0.1729` → IC=-0.255 (n=333)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1729
  - _Potencial_: sin este filtro IC_bueno=-0.154 (n=651)

- **FILTRO** `drift_15min` |x|> `0.888` → IC=-0.281 (n=245)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.888
  - _Potencial_: sin este filtro IC_bueno=-0.157 (n=739)

- **FILTRO** `sigma_ewma_delta_pct` > `6.572` → IC=-0.203 (n=230)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.572
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=754)

- **FILTRO** `sigma_ewma_delta_pct` > `17.972` → IC=-0.148 (n=513)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 17.972
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=4089)

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

- **PATRÓN** `delta_ratio_macro` |x|> `0.0646` → IC=+0.236 (n=559)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0646 (IC base=-0.040)

- **PATRÓN** `ibs_15` < `0.3542` → IC=+0.288 (n=559)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3542 (IC base=-0.040)

- **PATRÓN** `dist_vwap_pct` < `0.4496` → IC=+0.242 (n=587)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4496 (IC base=-0.040)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0197` → IC=-0.249 (n=587)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0197
  - _Potencial_: sin este filtro IC_bueno=-0.163 (n=588)

- **FILTRO** `sigma_ewma_delta_pct` > `7.41` → IC=-0.210 (n=367)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 7.41
  - _Potencial_: sin este filtro IC_bueno=-0.204 (n=808)

- **FILTRO** `libro_spread` > `0.04` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.04
  - _Potencial_: sin este filtro IC_bueno=-0.205 (n=1156)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.206)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.206)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0679` → IC=+0.273 (n=756)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0679 (IC base=-0.025)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1155` → IC=+0.295 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1155 (IC base=-0.025)

- **PATRÓN** `ibs_15` < `0.3333` → IC=+0.293 (n=848)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3333 (IC base=-0.025)

- **PATRÓN** `dist_vwap_pct` > `0.7764` → IC=+0.350 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7764 (IC base=-0.025)

### UPDOWN_GBM_ETH_15M_HORA7
- **PATRÓN** `ibs_15` > `0.8434` → IC=+0.333 (n=16)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8434 (IC base=+0.074)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **PATRÓN** `ibs_15` > `0.8434` → IC=+0.333 (n=16)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8434 (IC base=+0.074)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.298 (n=931)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.292)

- **PATRÓN** `drift_60min` |x|≤ `0.0531` → IC=+0.320 (n=354)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0531 (IC base=+0.292)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2423` → IC=+0.308 (n=353)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2423 (IC base=+0.292)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2257` → IC=+0.309 (n=628)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2257 (IC base=+0.292)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.309 (n=1103)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.292)

- **PATRÓN** `ibs_15` > `0.8388` → IC=+0.322 (n=1058)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8388 (IC base=+0.292)

- **PATRÓN** `dist_vwap_pct` > `0.2684` → IC=+0.328 (n=456)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2684 (IC base=+0.292)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.589` → IC=+0.377 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.589 (IC base=+0.292)

- **PATRÓN** `libro_liquidez` > `12357.9012` → IC=+0.311 (n=480)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12357.9012 (IC base=+0.292)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.314 (n=251)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.289)

- **PATRÓN** `sigma_h` > `0.0046` → IC=+0.292 (n=258)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0046 (IC base=+0.289)

- **PATRÓN** `drift_60min` |x|≤ `0.0571` → IC=+0.312 (n=190)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0571 (IC base=+0.289)

- **PATRÓN** `delta_ratio_macro` |x|> `0.258` → IC=+0.312 (n=190)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.258 (IC base=+0.289)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.307 (n=569)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.289)

- **PATRÓN** `ibs_15` > `0.8279` → IC=+0.316 (n=569)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8279 (IC base=+0.289)

- **PATRÓN** `dist_vwap_pct` > `0.2546` → IC=+0.330 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2546 (IC base=+0.289)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.589` → IC=+0.383 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.589 (IC base=+0.289)

- **PATRÓN** `libro_liquidez` > `16196.8854` → IC=+0.328 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16196.8854 (IC base=+0.289)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.307 (n=490)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.295)

- **PATRÓN** `drift_60min` |x|≤ `0.0518` → IC=+0.319 (n=164)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0518 (IC base=+0.295)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1466` → IC=+0.299 (n=326)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1466 (IC base=+0.295)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1067` → IC=+0.334 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1067 (IC base=+0.295)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.310 (n=503)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.295)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.298 (n=444)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.295)

- **PATRÓN** `ibs_15` > `0.8516` → IC=+0.325 (n=489)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8516 (IC base=+0.295)

- **PATRÓN** `dist_vwap_pct` > `0.2815` → IC=+0.328 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2815 (IC base=+0.295)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.63` → IC=+0.361 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.63 (IC base=+0.295)

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
- **PATRÓN** `T_h` > `85.7585` → IC=+0.187 (n=474)

  - _Acción_: Kelly boost +0.93€ cuando `T_h` > 85.7585 (IC base=+0.186)

- **PATRÓN** `ratio` < `0.973` → IC=+0.407 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.973 (IC base=+0.186)

- **PATRÓN** `T_h` > `112.3739` → IC=+0.352 (n=2152)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 112.3739 (IC base=+0.335)

- **PATRÓN** `ratio` > `1.0229` → IC=+0.373 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0229 (IC base=+0.335)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `107.5733` → IC=+0.167 (n=196)

  - _Acción_: Kelly boost +0.83€ cuando `T_h` > 107.5733 (IC base=+0.153)

- **PATRÓN** `ratio` < `0.9838` → IC=+0.318 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9838 (IC base=+0.153)

- **PATRÓN** `T_h` > `111.3978` → IC=+0.303 (n=744)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.3978 (IC base=+0.291)

- **PATRÓN** `ratio` > `1.0455` → IC=+0.403 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0455 (IC base=+0.291)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `83.3501` → IC=+0.232 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 83.3501 (IC base=+0.229)

- **PATRÓN** `ratio` < `0.9854` → IC=+0.401 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9854 (IC base=+0.229)

- **PATRÓN** `T_h` > `111.9836` → IC=+0.353 (n=786)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9836 (IC base=+0.324)

- **PATRÓN** `ratio` > `1.0347` → IC=+0.395 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0347 (IC base=+0.324)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.1003` → IC=+0.445 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1003 (IC base=+0.399)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de +0.179 a +0.255 en UPDOWN_GBM#15min (n=3513). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7199 sube el IC de +0.220 a +0.285 en UPDOWN_GBM#BTC#15min (n=603). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.5467 sube el IC de +0.145 a +0.245 en UPDOWN_GBM#ETH#15min (n=697). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.8947 sube el IC de +0.096 a +0.250 en UPDOWN_GBM#SOL#15min (n=258). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5429 sube el IC de +0.202 a +0.282 en UPDOWN_GBM#XRP#15min (n=804). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1111 sube el IC de +0.066 a +0.157 en UPDOWN_GBM#XRP#15min (n=768). Ya aplicado como kelly_boost=+0.79€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6341 sube el IC de -0.067 a +0.283 en UPDOWN_GBM_15M_TARDIO (n=1032). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.361 sube el IC de -0.013 a +0.282 en UPDOWN_GBM_15M_TARDIO (n=3529). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7566 sube el IC de +0.097 a +0.333 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=334). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.6255 sube el IC de -0.195 a +0.300 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=58). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6098 sube el IC de +0.153 a +0.253 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=516). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3695 sube el IC de +0.245 a +0.275 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=1263). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de -0.189 a +0.234 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=62). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3542 sube el IC de -0.040 a +0.288 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=559). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.206 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3333 sube el IC de -0.025 a +0.293 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=848). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_YES, IBS > 0.8434 sube el IC de +0.074 a +0.333 en UPDOWN_GBM_ETH_15M_HORA7 (n=16). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_YES, IBS > 0.8434 sube el IC de +0.074 a +0.333 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=16). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8388 sube el IC de +0.292 a +0.322 en UPDOWN_GBM_IBS_ALTO (n=1058). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8279 sube el IC de +0.289 a +0.316 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=569). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8516 sube el IC de +0.295 a +0.325 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=489). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.788 sube el IC de +0.366 a +0.402 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=622). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8066 sube el IC de +0.366 a +0.393 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=324). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7485 sube el IC de +0.365 a +0.413 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=298). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1915 | +0.090 | +209.70€ | 0 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1915 | +0.090 | +209.70€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1527 | +0.094 | +183.05€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1527 | +0.094 | +183.05€ | 0 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 281 | +0.069 | +11.17€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 281 | +0.069 | +11.17€ | 4 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 76 | +0.103 | +15.81€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 76 | +0.103 | +15.81€ | 0 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 613 | -0.006 | +66.96€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 613 | -0.006 | +66.96€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 447 | -0.028 | +37.63€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 447 | -0.028 | +37.63€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 128 | +0.061 | +22.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 128 | +0.061 | +22.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 35 | +0.013 | +3.73€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 35 | +0.013 | +3.73€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 39770 | -0.083 | -4985.68€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 2174 | +0.031 | -250.38€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 37596 | -0.090 | -4735.30€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4480 | -0.116 | -773.00€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4480 | -0.116 | -773.00€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 2174 | +0.031 | -250.38€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 2174 | +0.031 | -250.38€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 4313 | -0.105 | -874.78€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 4313 | -0.105 | -874.78€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 10574 | -0.023 | -970.40€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 10574 | -0.023 | -970.40€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 10487 | -0.107 | -812.34€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 10487 | -0.107 | -812.34€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 7742 | -0.135 | -1304.77€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 7742 | -0.135 | -1304.77€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 34442 | -0.016 | +3404.54€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 8909 | +0.005 | +1692.05€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 25533 | -0.023 | +1712.49€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 34442 | -0.016 | +3404.54€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 8909 | +0.005 | +1692.05€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 25533 | -0.023 | +1712.49€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 143261 | +0.115 | -5810.09€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 18465 | +0.183 | -546.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 630 | -0.019 | -68.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 115567 | +0.106 | -4875.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 8599 | +0.101 | -319.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 19167 | +0.108 | -1177.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 61 | -0.151 | +10.95€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 19091 | +0.109 | -1177.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 27778 | +0.128 | -393.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5171 | +0.189 | -171.21€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 19154 | +0.120 | -104.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 3411 | +0.083 | -96.34€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 19219 | +0.099 | -1355.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 72 | -0.122 | -6.14€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 19132 | +0.100 | -1338.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 30466 | +0.125 | -557.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 7900 | +0.178 | -132.55€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 19405 | +0.107 | -360.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 3149 | +0.100 | -55.55€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 27444 | +0.115 | -1393.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 5194 | +0.195 | -253.31€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 533 | +0.014 | -14.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 19678 | +0.095 | -957.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 2039 | +0.132 | -167.72€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#XRP | 19187 | +0.105 | -932.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 67 | -0.080 | +6.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 19107 | +0.106 | -938.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 23039 | +0.197 | -1391.05€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 23039 | +0.197 | -1391.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 5247 | +0.178 | -451.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 5247 | +0.178 | -451.11€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 2903 | +0.204 | -61.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 2903 | +0.204 | -61.12€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 5187 | +0.181 | -408.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 5187 | +0.181 | -408.72€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 4503 | +0.248 | -148.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 4503 | +0.248 | -148.50€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 5120 | +0.187 | -335.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 5120 | +0.187 | -335.37€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 1006 | +0.428 | -32.64€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 1006 | +0.428 | -32.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 395 | +0.437 | -4.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 395 | +0.437 | -4.98€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE#15min | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 395 | +0.432 | -8.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 395 | +0.432 | -8.38€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 202 | +0.402 | -15.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 202 | +0.402 | -15.42€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 80531 | +0.201 | -5752.04€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 80531 | +0.201 | -5752.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 13831 | +0.185 | -1431.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 13831 | +0.185 | -1431.50€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 13012 | +0.224 | -452.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 13012 | +0.224 | -452.02€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 13789 | +0.181 | -1443.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 13789 | +0.181 | -1443.17€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 13080 | +0.221 | -483.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 13080 | +0.221 | -483.58€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 13358 | +0.202 | -871.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 13358 | +0.202 | -871.49€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 13461 | +0.197 | -1070.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 13461 | +0.197 | -1070.28€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 30792 | +0.117 | +207.41€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 30792 | +0.117 | +207.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 15305 | +0.120 | +181.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 15305 | +0.120 | +181.66€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 15487 | +0.114 | +25.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 15487 | +0.114 | +25.75€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 2053 | +0.292 | -9.67€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 2053 | +0.292 | -9.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 940 | +0.278 | -28.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 940 | +0.278 | -28.88€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 994 | +0.297 | +13.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 994 | +0.297 | +13.90€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 119 | +0.351 | +5.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 119 | +0.351 | +5.31€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 947 | +0.441 | +3.24€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 947 | +0.441 | +3.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 461 | +0.435 | -4.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 461 | +0.435 | -4.91€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 440 | +0.448 | +7.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 440 | +0.448 | +7.60€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 46 | +0.396 | +0.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 46 | +0.396 | +0.55€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1621 | +0.073 | -59.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 626 | +0.054 | -48.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 995 | +0.085 | -10.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 73 | +0.113 | +3.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 73 | +0.113 | +3.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1245 | +0.081 | -20.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 250 | +0.068 | -10.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 995 | +0.085 | -10.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 303 | +0.028 | -42.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 303 | +0.028 | -42.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 60739 | +0.100 | -1541.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 4912 | +0.090 | +41.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 55827 | +0.101 | -1583.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 33433 | +0.105 | -379.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 4912 | +0.090 | +41.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 28521 | +0.108 | -421.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 12454 | +0.109 | -64.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 12454 | +0.109 | -64.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 14852 | +0.082 | -1097.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 14852 | +0.082 | -1097.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 895 | +0.192 | -111.46€ | 3 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 895 | +0.192 | -111.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 895 | +0.192 | -111.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 895 | +0.192 | -111.46€ | 3 | 4 |
| ✅ GBM_LATE_15M | 41801 | +0.094 | +21794.49€ | 0 | 19 |
| ✅ GBM_LATE_15M#15min | 41801 | +0.094 | +21794.49€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 6971 | +0.215 | +5713.42€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 6971 | +0.215 | +5713.42€ | 0 | 23 |
| ✅ GBM_LATE_15M#BTC | 6256 | +0.180 | +4771.33€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 6256 | +0.180 | +4771.33€ | 0 | 23 |
| ✅ GBM_LATE_15M#DOGE | 7470 | +0.205 | +5816.73€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 7470 | +0.205 | +5816.73€ | 0 | 21 |
| ✅ GBM_LATE_15M#ETH | 5839 | +0.041 | +1624.44€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 5839 | +0.041 | +1624.44€ | 1 | 19 |
| ✅ GBM_LATE_15M#SOL | 5901 | -0.031 | +1246.67€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 5901 | -0.031 | +1246.67€ | 4 | 15 |
| ✅ GBM_LATE_15M#XRP | 9364 | -0.031 | +2621.89€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 9364 | -0.031 | +2621.89€ | 3 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 44992 | +0.086 | +24460.48€ | 0 | 20 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 44992 | +0.086 | +24460.48€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 8685 | +0.004 | +4389.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 8685 | +0.004 | +4389.77€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 9510 | +0.010 | +2243.19€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 9510 | +0.010 | +2243.19€ | 0 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 6243 | +0.278 | +6695.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 6243 | +0.278 | +6695.87€ | 0 | 21 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 8090 | +0.013 | +1994.88€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 8090 | +0.013 | +1994.88€ | 1 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 7186 | +0.039 | +2971.57€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 7186 | +0.039 | +2971.57€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 5278 | +0.301 | +6165.21€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 5278 | +0.301 | +6165.21€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 33152 | +0.180 | +26808.44€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 33152 | +0.180 | +26808.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 5030 | +0.229 | +4451.57€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 5030 | +0.229 | +4451.57€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 5207 | +0.150 | +3853.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 5207 | +0.150 | +3853.16€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 5311 | +0.224 | +4577.01€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 5311 | +0.224 | +4577.01€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 5626 | +0.138 | +4268.65€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 5626 | +0.138 | +4268.65€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 6232 | +0.124 | +4644.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 6232 | +0.124 | +4644.94€ | 0 | 26 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 5746 | +0.225 | +5013.11€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 5746 | +0.225 | +5013.11€ | 0 | 26 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 8921 | +0.133 | +4339.59€ | 0 | 18 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 8921 | +0.133 | +4339.59€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 405 | +0.154 | +252.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 405 | +0.154 | +252.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 2650 | +0.146 | +1523.79€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 2650 | +0.146 | +1523.79€ | 0 | 22 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 418 | +0.148 | +207.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 418 | +0.148 | +207.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 2636 | +0.137 | +1242.35€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 2636 | +0.137 | +1242.35€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 2186 | +0.106 | +829.52€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 2186 | +0.106 | +829.52€ | 0 | 16 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 626 | +0.134 | +283.67€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 626 | +0.134 | +283.67€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO | 41982 | +0.185 | +33544.35€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#15min | 41982 | +0.185 | +33544.35€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 6651 | +0.241 | +6186.15€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 6651 | +0.241 | +6186.15€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 6517 | +0.149 | +4476.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 6517 | +0.149 | +4476.77€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 7093 | +0.233 | +6341.27€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 7093 | +0.233 | +6341.27€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 6935 | +0.138 | +4933.20€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 6935 | +0.138 | +4933.20€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 7439 | +0.121 | +5132.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 7439 | +0.121 | +5132.16€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 7347 | +0.229 | +6474.80€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 7347 | +0.229 | +6474.80€ | 0 | 20 |
| ✅ GBM_LATE_5M | 11614 | +0.201 | +8970.98€ | 1 | 30 |
| ✅ GBM_LATE_5M#5min | 11614 | +0.201 | +8970.98€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 984 | +0.242 | +916.10€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 984 | +0.242 | +916.10€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 2749 | +0.206 | +2337.01€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 2749 | +0.206 | +2337.01€ | 0 | 26 |
| ✅ GBM_LATE_5M#DOGE | 1110 | +0.193 | +808.37€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1110 | +0.193 | +808.37€ | 0 | 19 |
| ✅ GBM_LATE_5M#ETH | 3331 | +0.193 | +2335.31€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 3331 | +0.193 | +2335.31€ | 0 | 25 |
| ✅ GBM_LATE_5M#SOL | 1685 | +0.189 | +1265.70€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 1685 | +0.189 | +1265.70€ | 0 | 27 |
| ✅ GBM_LATE_5M#XRP | 1755 | +0.200 | +1308.49€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1755 | +0.200 | +1308.49€ | 0 | 0 |
| ✅ GBM_LATE_60M | 3400 | +0.067 | +1122.96€ | 0 | 7 |
| ✅ GBM_LATE_60M#60min | 3400 | +0.067 | +1122.96€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 1256 | +0.083 | +467.86€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 1256 | +0.083 | +467.86€ | 0 | 5 |
| ✅ GBM_LATE_60M#ETH | 1094 | +0.069 | +384.95€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 1094 | +0.069 | +384.95€ | 0 | 9 |
| ✅ GBM_LATE_60M#SOL | 1050 | +0.046 | +270.16€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 1050 | +0.046 | +270.16€ | 1 | 13 |
| 🚫 GBM_LATE_60M_FADE | 562 | -0.245 | -24.24€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 562 | -0.245 | -24.24€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 210 | -0.245 | -14.04€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 210 | -0.245 | -14.04€ | 5 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 199 | -0.226 | -2.48€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 199 | -0.226 | -2.48€ | 5 | 1 |
| 🚫 GBM_LATE_60M_FADE#SOL | 153 | -0.261 | -7.72€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 153 | -0.261 | -7.72€ | 4 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 1498 | +0.084 | +388.26€ | 1 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 1498 | +0.084 | +388.26€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 587 | +0.082 | +145.94€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 587 | +0.082 | +145.94€ | 1 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 538 | +0.057 | +80.05€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 538 | +0.057 | +80.05€ | 2 | 9 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 373 | +0.124 | +162.26€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 373 | +0.124 | +162.26€ | 2 | 10 |
| ✅ LATE_WINDOW_5MIN | 163 | +0.276 | +158.78€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 163 | +0.276 | +158.78€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 163 | +0.276 | +158.78€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 163 | +0.276 | +158.78€ | 1 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 3350 | +0.100 | +822.42€ | 0 | 1 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 3350 | +0.100 | +822.42€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 3350 | +0.100 | +822.42€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 3350 | +0.100 | +822.42€ | 0 | 1 |
| ✅ LIQUIDACIONES_15M | 520 | -0.048 | -21.95€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 520 | -0.048 | -21.95€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 143 | -0.017 | +1.52€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 143 | -0.017 | +1.52€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 99 | -0.054 | -5.61€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 99 | -0.054 | -5.61€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 197 | -0.007 | -0.99€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 197 | -0.007 | -0.99€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M | 3691 | +0.017 | +85.08€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 3691 | +0.017 | +85.08€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 181 | +0.019 | -2.82€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 181 | +0.019 | -2.82€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 781 | +0.013 | +34.06€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 781 | +0.013 | +34.06€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE | 207 | -0.012 | -4.18€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 207 | -0.012 | -4.18€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 1323 | +0.027 | +32.53€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1323 | +0.027 | +32.53€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 755 | +0.011 | +1.37€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 755 | +0.011 | +1.37€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 444 | +0.013 | +24.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 444 | +0.013 | +24.11€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 1732 | -0.040 | -27.22€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1732 | -0.040 | -27.22€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 497 | -0.029 | -10.53€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 497 | -0.029 | -10.53€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 587 | -0.014 | +6.25€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 587 | -0.014 | +6.25€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 648 | -0.071 | -22.94€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 648 | -0.071 | -22.94€ | 6 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 8506 | -0.028 | -7.94€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 4040 | -0.037 | -90.36€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 4466 | -0.019 | +82.42€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 259 | -0.040 | -9.72€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 132 | -0.022 | -0.45€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 127 | -0.058 | -9.26€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 2120 | -0.019 | +15.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 1012 | -0.024 | -4.00€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 1108 | -0.015 | +19.12€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 937 | -0.024 | +12.51€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 470 | -0.042 | -12.78€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 467 | -0.005 | +25.29€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 1840 | -0.043 | -65.30€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 856 | -0.055 | -58.85€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 984 | -0.033 | -6.45€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 1660 | -0.021 | +25.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 790 | -0.035 | -11.43€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 870 | -0.007 | +36.89€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 1690 | -0.028 | +13.99€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 780 | -0.036 | -2.84€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 910 | -0.022 | +16.84€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 49031 | -0.001 | +2435.49€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 49031 | -0.001 | +2435.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 8835 | +0.026 | +1120.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 8835 | +0.026 | +1120.79€ | 2 | 4 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 7077 | -0.034 | -102.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 7077 | -0.034 | -102.31€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 8939 | +0.024 | +931.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 8939 | +0.024 | +931.46€ | 2 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 6921 | -0.048 | -150.41€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 6921 | -0.048 | -150.41€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 8287 | -0.005 | +229.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 8287 | -0.005 | +229.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 8972 | +0.015 | +406.65€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 8972 | +0.015 | +406.65€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 6604 | -0.060 | -163.61€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 6604 | -0.060 | -163.61€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1225 | -0.000 | -15.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1225 | -0.000 | -15.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1715 | -0.080 | -46.59€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1715 | -0.080 | -46.59€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 54 | -0.054 | -2.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 54 | -0.054 | -2.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 773 | -0.119 | -32.95€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 773 | -0.119 | -32.95€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1980 | -0.075 | -40.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1980 | -0.075 | -40.88€ | 3 | 0 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 121733 | -0.076 | +1736.57€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 121733 | -0.076 | +1736.57€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 21156 | -0.077 | +1092.96€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 21156 | -0.077 | +1092.96€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 18342 | -0.099 | -948.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 18342 | -0.099 | -948.22€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 21453 | -0.067 | +1163.64€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 21453 | -0.067 | +1163.64€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 17886 | -0.097 | -612.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 17886 | -0.097 | -612.37€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 21806 | -0.056 | +333.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 21806 | -0.056 | +333.24€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 21090 | -0.066 | +707.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 21090 | -0.066 | +707.32€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 8753 | -0.034 | -181.58€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 8753 | -0.034 | -181.58€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 1001 | -0.017 | -18.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 1001 | -0.017 | -18.91€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1985 | -0.046 | -24.74€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1985 | -0.046 | -24.74€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1008 | -0.022 | -32.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1008 | -0.022 | -32.80€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2599 | -0.026 | -41.83€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2599 | -0.026 | -41.83€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1191 | -0.055 | -28.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1191 | -0.055 | -28.38€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 969 | -0.030 | -34.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 969 | -0.030 | -34.93€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1662 | +0.124 | +680.46€ | 0 | 6 |
| ✅ ORDER_FLOW_5M#5min | 1526 | +0.130 | +667.87€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 356 | +0.142 | +185.97€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 356 | +0.142 | +185.97€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#DOGE | 313 | +0.113 | +102.27€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 313 | +0.113 | +102.27€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#ETH | 304 | +0.137 | +148.74€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 304 | +0.137 | +148.74€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#SOL | 269 | +0.153 | +149.89€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 269 | +0.153 | +149.89€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#XRP | 284 | +0.098 | +80.99€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 284 | +0.098 | +80.99€ | 0 | 3 |
| ✅ ORDER_FLOW_5M_REACTIVO | 1423 | -0.010 | -7.24€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 1423 | -0.010 | -7.24€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 276 | +0.004 | +11.92€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 276 | +0.004 | +11.92€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 242 | -0.012 | -0.17€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 242 | -0.012 | -0.17€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 367 | -0.039 | -25.14€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 367 | -0.039 | -25.14€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 305 | +0.015 | +5.77€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 305 | +0.015 | +5.77€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 233 | -0.011 | +0.38€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 233 | -0.011 | +0.38€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 891 | -0.070 | -41.98€ | 3 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 416 | -0.110 | -76.93€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 320 | -0.140 | -64.34€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 96 | -0.010 | -12.59€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 316 | -0.031 | +25.39€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 225 | -0.020 | +27.85€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 91 | -0.059 | -2.46€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 159 | -0.040 | +9.56€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 128 | -0.046 | +5.17€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 31 | -0.015 | +4.39€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 673 | -0.082 | -31.31€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 218 | -0.032 | -10.67€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 1113 | -0.208 | -68.85€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC | 435 | -0.209 | -41.94€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#atexpiry | 378 | -0.213 | -41.71€ | 5 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 57 | -0.178 | -0.23€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 380 | -0.212 | -33.75€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 332 | -0.225 | -40.76€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 48 | -0.120 | +7.01€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 298 | -0.197 | +6.84€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 277 | -0.192 | +4.72€ | 5 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 21 | -0.239 | +2.12€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 987 | -0.212 | -77.75€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 126 | -0.172 | +8.90€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 448 | +0.393 | +417.97€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#BTC | 67 | +0.152 | +54.00€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 67 | +0.152 | +54.00€ | 0 | 1 |
| ✅ RESOLUTION_SNIPER#ETH | 107 | +0.362 | +89.61€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 107 | +0.362 | +89.61€ | 0 | 8 |
| ✅ RESOLUTION_SNIPER#SOL | 274 | +0.460 | +274.37€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 274 | +0.460 | +274.37€ | 0 | 10 |
| ✅ RESOLUTION_SNIPER#sniper | 448 | +0.393 | +417.97€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 720 | +0.028 | +32.66€ | 2 | 2 |
| ✅ STREAK_FADE_15M#15min | 720 | +0.028 | +32.66€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 302 | +0.023 | +3.35€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 302 | +0.023 | +3.35€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 59 | -0.008 | -1.64€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 59 | -0.008 | -1.64€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 73 | -0.007 | +0.78€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 73 | -0.007 | +0.78€ | 3 | 1 |
| ✅ STREAK_FADE_15M#XRP | 286 | +0.049 | +30.18€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 286 | +0.049 | +30.18€ | 0 | 5 |
| ✅ STREAK_FADE_5M | 3440 | -0.022 | -134.81€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3440 | -0.022 | -134.81€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 1057 | -0.021 | -36.50€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 1057 | -0.021 | -36.50€ | 0 | 0 |
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
| ✅ STREAK_MOM_5M | 10800 | +0.017 | +95.65€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 10800 | +0.017 | +95.65€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2757 | +0.021 | +29.36€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2757 | +0.021 | +29.36€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2811 | +0.019 | +38.19€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2811 | +0.019 | +38.19€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2888 | +0.009 | -0.95€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2888 | +0.009 | -0.95€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2344 | +0.019 | +29.05€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2344 | +0.019 | +29.05€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 9818 | +0.013 | -51.69€ | 2 | 0 |
| ✅ STRUCT_NO_15M#15min | 9818 | +0.013 | -51.69€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 3991 | +0.017 | -11.32€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 3991 | +0.017 | -11.32€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3613 | +0.011 | -26.65€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3613 | +0.011 | -26.65€ | 2 | 0 |
| ✅ STRUCT_NO_15M#SOL | 2214 | +0.009 | -13.72€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 2214 | +0.009 | -13.72€ | 1 | 0 |
| ✅ UPDOWN_GBM | 75510 | +0.053 | +6661.34€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 18766 | +0.083 | +4116.52€ | 0 | 11 |
| ✅ UPDOWN_GBM#240min | 2433 | +0.004 | +22.59€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 49622 | +0.050 | +2435.77€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 4426 | +0.008 | +85.67€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 6851 | +0.089 | +1075.72€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1576 | +0.156 | +698.08€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 77 | -0.006 | -0.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 5198 | +0.070 | +378.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 16154 | +0.056 | +1384.12€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 2422 | +0.089 | +588.87€ | 0 | 9 |
| ✅ UPDOWN_GBM#BTC#240min | 651 | +0.010 | +10.20€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 11013 | +0.061 | +724.72€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 1973 | +0.004 | +56.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 95 | -0.067 | +3.48€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 8350 | +0.069 | +883.75€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1555 | +0.147 | +610.96€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 78 | +0.013 | -1.79€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 6717 | +0.051 | +274.58€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 17277 | +0.044 | +1119.67€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 4437 | +0.065 | +644.48€ | 0 | 11 |
| ✅ UPDOWN_GBM#ETH#240min | 635 | +0.005 | +15.93€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 10565 | +0.044 | +435.47€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 1552 | +0.013 | +20.52€ | 1 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 88 | -0.100 | +3.28€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 16533 | +0.032 | +802.12€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 4641 | +0.034 | +383.36€ | 0 | 2 |
| ✅ UPDOWN_GBM#SOL#240min | 604 | -0.008 | -0.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 10309 | +0.037 | +415.43€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 901 | +0.008 | +8.31€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 78 | -0.125 | -4.14€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 10343 | +0.064 | +1397.80€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 4135 | +0.101 | +1190.78€ | 0 | 9 |
| ✅ UPDOWN_GBM#XRP#240min | 388 | +0.010 | -0.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 5820 | +0.041 | +207.09€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 261 | -0.097 | +2.63€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 828 | +0.366 | +308.42€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 828 | +0.366 | +308.42€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 431 | +0.366 | +153.31€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 431 | +0.366 | +153.31€ | 0 | 10 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 397 | +0.365 | +155.12€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 397 | +0.365 | +155.12€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO | 19600 | -0.025 | +4610.79€ | 3 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 19600 | -0.025 | +4610.79€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1718 | -0.056 | +502.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1718 | -0.056 | +502.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 3474 | -0.112 | +133.06€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 3474 | -0.112 | +133.06€ | 5 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 948 | +0.216 | +770.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 948 | +0.216 | +770.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 2370 | +0.218 | +1550.07€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 2370 | +0.218 | +1550.07€ | 1 | 21 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 5586 | -0.066 | +666.29€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 5586 | -0.066 | +666.29€ | 4 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 5504 | -0.064 | +988.11€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 5504 | -0.064 | +988.11€ | 3 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 227 | +0.042 | +9.93€ | 0 | 1 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 227 | +0.042 | +9.93€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 227 | +0.042 | +9.93€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 227 | +0.042 | +9.93€ | 0 | 1 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1410 | +0.292 | +1209.15€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1410 | +0.292 | +1209.15€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 758 | +0.289 | +614.79€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 758 | +0.289 | +614.79€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 652 | +0.295 | +594.36€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 652 | +0.295 | +594.36€ | 0 | 9 |
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
| ✅ WEEKLY_PRICE | 3569 | +0.302 | +1687.40€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 1313 | +0.254 | +157.79€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 1371 | +0.297 | +613.35€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 885 | +0.379 | +916.26€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**〰️ H-IBS-15** — IBS-15 como señal de mean-reversion
  - _Umbral_: n≥40 ops con ibs_15 en features y spread_IC>0.15 entre buckets
  - _Acción_: Añadir ibs_15 como boost/filtro en FEATURE_RULES de shadow_postmortem.py
  - _Estado_: Spread bajo (0.043) — sin ventaja clara. oversold(IBS<0.3): IC=+0.063 n=26229 | neutral: IC=+0.057 n=27820 | overbought(IBS>0.7): IC=+0.100 n=26743
  - _Datos_: n=83986 IC=+0.074 PNL=+12492.57€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 709 celda(s) pasan gate riguroso completo de 2675 evaluadas (n>=40) y 3726 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.034 < 0.08 — monitorear
  - _Datos_: n=4641 IC=+0.034 PNL=+383.36€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=1371/15 IC=+0.297 PNL=+613.35€ | BTC: n=1313/15 IC=+0.254 PNL=+157.79€ | SOL: n=885/15 IC=+0.379 PNL=+916.26€

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
  - _Estado_: 75448 ops, 22 horas distintas. Sin hora con n≥15 y IC extremo aún.

**⏳ H-WINDOW-MOMENTUM** — Momentum de outcome entre ventanas 15min contiguas
  - _Umbral_: n≥60 alineadas y gap IC≥0.08 vs contrarias — y descartar que sea proxy de drift_15min/60min
  - _Acción_: Si confirma e independiente de drift → capturar prev_window_outcome como feature en shadow_predict y boost ×1.1-1.2 en señales alineadas
  - _Estado_: alineada_con_outcome_prev IC=+0.138 n=775/60 | contraria IC=+0.190 n=801 | gap=-0.051 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=460, boost estimado=+0.016. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 269 ops con delta_ratio

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=1552/40 IC=+0.013 PNL=+20.52€ | BTC#60min: n=1973/40 IC=+0.004 PNL=+56.84€ | SOL#60min: n=901/40 IC=+0.008 PNL=+8.31€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.048 n=548241 | tras_1loss IC=+0.095 n=417005 | tras_2loss IC=+0.064 n=168947/40 | gap=-0.016 (umbral 0.05)

**⏳ H-BTC-LEADS-ETH** — ETH/SOL GBM contrario al drift_15min de BTC del mismo ciclo
  - _Umbral_: n≥40 en contrario_BTC y gap≥0.08 — y descartar confound con drift propio antes de actuar
  - _Acción_: Si se confirma y no es confound → boost en ETH/SOL cuando decisión contraria a drift_15min BTC
  - _Estado_: alineado_BTC IC=+0.036 n=10504 | contrario_BTC IC=+0.052 n=9216/40 | gap=+0.016 (umbral 0.08) — SIN CONFIRMAR independencia de filtros propios de ETH


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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.171 > 0.08 con n=812 PNL=+466.16€
  - _Datos_: n=812 IC=+0.171 PNL=+466.16€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.332 > 0.1 con n=2913 PNL=+1617.24€
  - _Datos_: n=2913 IC=+0.332 PNL=+1617.24€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=669 IC=+0.075 PNL=+79.22€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=669 IC=+0.075 PNL=+79.22€

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
  - _Estado_: n=71518 IC=+0.053 PNL=+6368.25€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=71518 IC=+0.053 PNL=+6368.25€

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
  - _Estado_: n=2981 IC=+0.009 PNL=+7.35€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2981 IC=+0.009 PNL=+7.35€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=1445 IC=+0.006 PNL=+78.32€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=1445 IC=+0.006 PNL=+78.32€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=932 IC=+0.022 PNL=+35.81€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=932 IC=+0.022 PNL=+35.81€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.179 > 0.1 con n=4684 PNL=+2968.37€
  - _Datos_: n=4684 IC=+0.179 PNL=+2968.37€

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
  - _Estado_: n=2422 IC=+0.089 PNL=+588.87€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=2422 IC=+0.089 PNL=+588.87€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.098 > 0.08 con n=10798 PNL=+3041.36€
  - _Datos_: n=10798 IC=+0.098 PNL=+3041.36€

**〰️ H-CUSTOM-LONGSHOT-BIAS** — Longshot bias — ¿mejor IC cuando py_mkt < 0.20 o > 0.80?
  - _Hipótesis_: Jon-Becker repo documenta formalmente: contratos a 1-20 cents tienen win_rate < precio implícito (compradores pierden sistemáticamente en longshots). En nuestro sistema: cuando py_mkt<0.20 el GBM predice BUY_NO con edge estructural adicional al del modelo. ¿Se confirma en nuestros datos? Buscar en feature pct_spot_vs_ref si los mercados extremos tienen mejor IC en BUY_NO.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 en mercados extremos → boost ×1.2 en BUY_NO cuando py_mkt<0.20
  - _Estado_: n=339 IC=-0.230 PNL=-1.54€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=339 IC=-0.230 PNL=-1.54€

**〰️ H-CUSTOM-ETH15-REVERSION** — ETH#15min con drift_15min < -1 — ¿mean reversion?
  - _Hipótesis_: ETH y BTC tienen patrones opuestos: BTC funciona con momentum (drift>0.3). ETH funciona con reversión (drift<-1): 9/14 (64%) IC=+0.087. La hipótesis es que ETH tiene más mean-reversion que BTC en 15min.
  - _Umbral_: n≥20 y IC>+0.08
  - _Acción_: Si ETH drift<-1 confirma IC>0.08 con n≥20 → boost ×1.1 en ETH#15min cuando drift_15min<-1
  - _Estado_: n=423 IC=-0.027 PNL=-10.58€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=423 IC=-0.027 PNL=-10.58€

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
  - _Estado_: n=8275 IC=+0.019 PNL=+194.94€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=8275 IC=+0.019 PNL=+194.94€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.276 n=163) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=163 IC=+0.276 PNL=+158.78€

**〰️ H-DVOL-SPIKE-BUYNO** — DVOL spike (sigma_h alto) → BUY_NO tiene más edge (panic regime)
  - _Hipótesis_: Inspirado en 'The Volatility Edge' (Concretum Research, 2025): en equities, VIX spikes identifican regímenes de pánico donde los moves están sobreamplificados por feedback loops (deleveraging, hedgers, etc). En cripto el análogo es DVOL (Deribit BTC IV). Sin acceso a DVOL, usamos sigma_h como proxy (vol realizada 1h). Hipótesis: cuando sigma_h > 0.004/h (≈ vol diaria >9.6%), los mercados de predicción exageran la bajada en 15min → BUY_NO tiene IC superior porque el pánico se revierte intraday. Activar cuando n≥200 en BUY_NO #15min para tener potencia suficiente para subdividir por régimen.
  - _Umbral_: n≥200 BUY_NO #15min total, luego n≥40 en subconjunto sigma_h>0.004 y IC>+0.10
  - _Acción_: Si IC_sigma_alto > IC_baseline + 0.08 con n≥40 → boost ×1.2 en BUY_NO cuando sigma_h>0.004. Pendiente integrar DVOL real (Deribit API) cuando n≥500.
  - _Estado_: n=12483 IC=+0.050 PNL=+1037.92€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=12483 IC=+0.050 PNL=+1037.92€

**〰️ H-CUSTOM-POLY-DRIFT-CONFIRM** — poly_drift_5obs: ¿el precio YES interno de Polymarket confirma nuestra señal?
  - _Hipótesis_: Feature nueva 2026-06-27: drift del precio YES en Polymarket en últimas 5 obs (~5min). Si poly_drift<0 y decidimos BUY_NO (o poly_drift>0 y BUY_YES) → confluencia. Si diverge → reducción de stake. Hipótesis: confluencia Binance+Polymarket mejora IC; divergencia empeora.
  - _Umbral_: n≥40 en confluencia vs divergencia para validar el boost ×1.1
  - _Acción_: Si IC_confluencia>IC_divergencia con n≥40 → mantener el boost. Si no → retirar.
  - _Estado_: n=4474 IC=+0.063 PNL=+650.14€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=4474 IC=+0.063 PNL=+650.14€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.150 > 0.08 con n=1118 PNL=+319.41€
  - _Datos_: n=1118 IC=+0.150 PNL=+319.41€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-NEG** — GBM 15min/60min: spread negativo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Lado negativo de H-CUSTOM-CROSS-WINDOW-SPREAD-POS (mercado propio más barato que el relacionado). Mismo feature cross_window_spread, mismo origen (artículo sobre bots de Polymarket), umbral simétrico.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.103 > 0.08 con n=880 PNL=+445.37€
  - _Datos_: n=880 IC=+0.103 PNL=+445.37€

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
  - _Estado_: n=11373 IC=+0.057 PNL=+1118.44€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=11373 IC=+0.057 PNL=+1118.44€

**🟡 H-CUSTOM-OF-EDGE-ALTO** — ORDER_FLOW_5M: edge alto (>0.20) rinde mejor que edge cerca del suelo
  - _Hipótesis_: Analizado 2026-07-01 sobre 794 resoluciones de ORDER_FLOW_5M: edge_neto en [0.025,0.198) -> IC=-0.009 (n=397, PNL=-10.49€) vs edge_neto en [0.198,0.385] -> IC=+0.029 (n=397, PNL=+16.43€). Comprobado que NO es un efecto general: en UPDOWN_GBM el patrón se invierte (edge bajo IC=-0.002 vs edge alto IC=-0.033), así que este filtro debe quedar scoped solo a ORDER_FLOW_5M, no aplicarse a otras estrategias. CORREGIDO 2026-07-01 (mismo día, encontrado por auditoría): el filtro original usaba 'edge_neto' con solo feature_lo, pero edge_neto está firmado por dirección (negativo en BUY_NO, positivo en BUY_YES) y ORDER_FLOW_5M solo genera BUY_NO desde 2026-06-25 — el filtro nunca podía matchear ningún BUY_NO real, solo el remanente BUY_YES histórico de antes del 25-jun (n=151, datos muertos, no crecen hacia adelante). Cambiado a 'edge_direccional' (siempre positivo, = abs(edge_neto)) + decision=BUY_NO explícito. Con el fix: n=227, IC=+0.0502, PNL=+19.15€ — señal real y viva.
  - _Umbral_: n≥80 en cada mitad (bajo/alto) para confirmar con más margen que el análisis inicial
  - _Acción_: Si se confirma con n≥80 y el gap se mantiene ≥0.03 → subir EDGE_MINIMO solo para ORDER_FLOW_5M a ~0.20 (o escalar Kelly con la magnitud del edge)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.127 > 0.02 con n=962 PNL=+408.27€
  - _Datos_: n=962 IC=+0.127 PNL=+408.27€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.449 > 0.1 con n=1627 PNL=+1585.23€
  - _Datos_: n=1627 IC=+0.449 PNL=+1585.23€

**〰️ H-CUSTOM-GBM-BUYYES-GLOBAL-MALO** — UPDOWN_GBM BUY_YES global — ¿estructuralmente peor que BUY_NO en todas las estrategias activas?
  - _Hipótesis_: Analizado 2026-07-01: patrón cross-estrategia consistente en las 4 estrategias activas — BUY_NO gana a BUY_YES sin excepción (UPDOWN_GBM IC=+0.058 n=154 vs -0.046 n=412; ORDER_FLOW_5M +0.053 n=439 vs -0.043 n=355; PRICE_TARGET_GBM +0.011 n=45 vs -0.267 n=28; WEEKLY_PRICE +0.115 n=50 vs -0.315 n=25). Mecanismo propuesto: sesgo retail comprando 'Up'/'YES' en cripto infla el precio de YES por encima de su valor justo en Polymarket — consistente con la sobreconfianza del modelo en probabilidades altas de YES detectada en la calibración Platt (ver idea_calibracion_platt). ORDER_FLOW_5M (solo genera BUY_NO desde 2026-06-25) y WEEKLY_PRICE (H-WEEKLY-BUYNO) ya actúan sobre este mismo patrón; UPDOWN_GBM y PRICE_TARGET_GBM (ver H-CUSTOM-PRICETARGET-BUYYES-MALO) todavía no tienen un tratamiento sistemático equivalente, solo filtros puntuales por hora/subtipo.
  - _Umbral_: n≥50 y IC<-0.05 para confirmar bloqueo global (a día de hoy ya está en n=412, IC=-0.046 — muy cerca)
  - _Acción_: Si se confirma con n≥50 → exigir evidencia direccional más fuerte por subtipo antes de permitir BUY_YES en live (barra asimétrica frente a BUY_NO), en vez de auto-desactivar de golpe todo BUY_YES de GBM
  - _Estado_: n=29563 IC=+0.074 PNL=+4314.35€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=29563 IC=+0.074 PNL=+4314.35€

**🟡 H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: n≥120 y IC>+0.10 (el n=61 del descubrimiento está incluido — exigir ~doble para confirmar forward)
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.209 > 0.1 con n=6658 PNL=+3998.35€
  - _Datos_: n=6658 IC=+0.209 PNL=+3998.35€

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.144 < -0.1 con n=473 PNL=+49.78€
  - _Datos_: n=473 IC=-0.144 PNL=+49.78€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=3063 IC=+0.066 PNL=+372.64€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=3063 IC=+0.066 PNL=+372.64€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=139 IC=-0.082 PNL=+8.08€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=139 IC=-0.082 PNL=+8.08€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.113 > 0.1 con n=786 PNL=+215.06€
  - _Datos_: n=786 IC=+0.113 PNL=+215.06€

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
  - _Estado_: n=31475 IC=-0.134 PNL=+2513.76€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=31475 IC=-0.134 PNL=+2513.76€

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
  - _Estado_: n=3151 IC=+0.133 PNL=+1919.55€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=3151 IC=+0.133 PNL=+1919.55€

**🟡 H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: n≥40 forward y IC>+0.08 (barra live estándar)
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.206 > 0.08 con n=4049 PNL=+2980.04€
  - _Datos_: n=4049 IC=+0.206 PNL=+2980.04€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.219 > 0.08 con n=802 PNL=+477.35€
  - _Datos_: n=802 IC=+0.219 PNL=+477.35€

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.222 < -0.1 con n=3263 PNL=-251.57€
  - _Datos_: n=3263 IC=-0.222 PNL=-251.57€

**🟡 H-CUSTOM-GBMLATE-ANCHURA-MERCADO** — GBM_LATE_15M BUY_YES — anchura de mercado (retorno concurrente de los otros 3 majors) como modificador secundario
  - _Hipótesis_: Detectado 2026-07-09 buscando explicar por qué varias pérdidas de la racha=4 comparten ventana de 15min. Con precios reales (05-09jul, ~20k muestras BTC) se calculó el retorno concurrente de los OTROS 3 majors desde el inicio de la ventana hasta el momento exacto de la decisión (sin fuga de datos, nunca el precio de cierre) y se cruzó con resultados reales de GBM_LATE_15M BUY_YES: n=802, magnitud media de los otros 3 en deciles limpios y monótonos (decil1 IC=-0.146 hit 35% → decil6-9 IC≈+0.20/+0.29 hit 70-80%). NO es redundante con drift_ventana_pct propio del par (correlación solo 0.26); controlando por el drift propio, la anchura sigue añadiendo información (dentro de drift propio>=0, que es el 90% de los casos: IC=0.127 si anchura baja vs IC=0.211 si anchura alta). Funciona en espejo para BUY_NO (shadow, n=685, anchura negativa 0/3→3/3: hit 47.4%→70.3%). CAVEAT importante: NO explica los clusters concretos de racha=4 en vivo — 6 de los 8 eventos históricos tienen anchura ALTA en al menos 2 de las 4 pérdidas (ver notas de sesión 09-Jul), y el backtest directo sobre trades.csv real (n=105-116) es inconcluso/contradictorio (gate anchura>=3 empeora el PnL real, -2.11€ vs +32.32€ sin filtro — probablemente confusión por mezcla de pares en una muestra pequeña, SOL domina ese bucket y SOL es el par MENOS sensible a esta señal: IC 0.132→0.143 apenas cambia, vs ETH 0.038→0.192). Tratar como MODIFICADOR del filtro primario H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT, no como filtro independiente — ver esa hipótesis para la tabla cruzada. Feature `mercado_anchura_pct` añadida 2026-07-09 en shadow_predict.py (_s_gbm_late), puro logging, no cambia ninguna decisión — empieza a acumular desde cero en predicciones nuevas. ACTUALIZACIÓN 12-Jul (desagregación por activo, n fresco): BTC n=35 ic=+0.392 z=+4.90, ETH n=32 ic=+0.353 z=+4.24, XRP n=31 ic=+0.288 z=+3.41 -- los 3 MUY fuertes y consistentes. SOL sigue siendo el único débil (n=30 ic=+0.094 z=+1.10), confirma el caveat ya escrito arriba (SOL insensible). Con XRP incluido, el patrón deja de ser '3 activos + SOL raro' para ser una regla casi universal salvo SOL -- candidato fuerte para boost Kelly restringido a BTC/ETH/XRP (excluir SOL explícitamente) en vez de aplicar a las 4 monedas por igual.
  - _Umbral_: n≥100 forward (feature nueva, sin histórico) e IC>+0.20 en la zona alta (mercado_anchura_pct≥0.056, el decil superior observado)
  - _Acción_: Si confirma con n≥100 IC≥0.20 → boost Kelly cuando mercado_anchura_pct≥0.056 Y prob_yes_modelo≥0.53 (la celda 'doble buena', hit 72.7% retrospectivo). No usar como filtro solo — ver CAVEAT de los clusters de racha en la descripción, y el análisis por-par (SOL insensible) antes de aplicar a las 4 monedas por igual.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.208 > 0.2 con n=8591 PNL=+6762.85€
  - _Datos_: n=8591 IC=+0.208 PNL=+6762.85€

**🟡 H-CUSTOM-OF5M-SMARTMONEY-CONTRARIO** — ORDER_FLOW_5M SOL BUY_NO — smart money EN CONTRA del flujo CEX, no a favor, predice mejor
  - _Hipótesis_: Detectado 11-Jul revisando el backlog quant-desk (reencuadre de ORDER_FLOW_5M). ORDER_FLOW_5M solo dispara BUY_NO (presión vendedora en Binance). Split retrospectivo SOL#5min por smart_money_consensus (ya logueado, nunca cruzado con esta estrategia): cuando el consenso on-chain es BAJISTA (smart_money_consensus<0, 'confirma' la señal CEX) el hit cae a 47.1% (ic_bayes=-0.026, n=17); cuando el consenso es ALCISTA/neutro (smart_money_consensus>=0, CONTRARIO a la señal CEX) el hit sube a 65.0% (ic_bayes=+0.136, n=20, pnl/trade+0.294). Contraintuitivo: la 'confirmación' de dos fuentes empeora, la divergencia mejora. Hipótesis mecánica: el flujo de Binance ya captura la información rápida de 5min; smart money on-chain se mueve más lento (posiciones ya tomadas), así que cuando coincide con el flujo CEX puede ser la MISMA información ya vista dos veces sin dar nada nuevo (o incluso momentum ya agotado), mientras que la divergencia indica que el flujo CEX es el que se está moviendo AHORA sobre información fresca que smart money aún no reflejó. Distinto del cierre 08-Jul del consenso poblacional plano (n=2494, ruido puro) — aquello era agregado sobre TODAS las estrategias; esto es específico del mecanismo de ORDER_FLOW_5M. n=17/20 insuficiente para concluir (regla del proyecto n≥15 es el mínimo absoluto, no un veredicto) — vigilar forward.
  - _Umbral_: n≥40 en cada rama (contrario y alineado) para separar señal de ruido
  - _Acción_: Si confirma con n≥40 e ic_bayes contrario≥+0.08 (con alineado claramente peor) → boost Kelly en ORDER_FLOW_5M BUY_NO cuando smart_money_consensus>=0; considerar filtro/veto cuando smart_money_consensus<0 y muy negativo (posible señal 'ya vista', sin ventaja).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.126 > 0.08 con n=121 PNL=+55.81€
  - _Datos_: n=121 IC=+0.126 PNL=+55.81€

**〰️ H-CUSTOM-ETH15-SIGMA-ACCEL** — GBM_LATE_15M ETH — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: sigma_ewma_delta_pct = (sigma_h_ewma10-sigma_h)/sigma_h. Verificado ad-hoc n=47: cuando la vol reciente (EWMA half-life 10min) supera la ventana plana, hit sube de 59.5% (agregado ETH) a 66.0%, ic_bayes=+0.153. Efecto NO uniforme entre activos (ver hermanas BTC/XRP) -- desagregar por activo es obligatorio, el agregado GBM_LATE_15M diluye esto a ruido.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en ETH#15min
  - _Estado_: n=3145 IC=+0.080 PNL=+1078.62€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=3145 IC=+0.080 PNL=+1078.62€

**🟡 H-CUSTOM-BTC15-SIGMA-ACCEL** — GBM_LATE_15M BTC — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: mismo mecanismo que ETH (ver H-CUSTOM-ETH15-SIGMA-ACCEL). Verificado ad-hoc n=35: hit sube de 63.6% (agregado BTC) a 68.6%, ic_bayes=+0.176.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en BTC#15min
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.179 > 0.08 con n=2899 PNL=+2183.73€
  - _Datos_: n=2899 IC=+0.179 PNL=+2183.73€

**〰️ H-CUSTOM-XRP15-SIGMA-DECEL** — GBM_LATE_15M XRP — vol DESacelerando (EWMA10<=flat) mejora la señal (signo opuesto a ETH/BTC)
  - _Hipótesis_: 12-Jul: XRP muestra el signo CONTRARIO a ETH/BTC -- cuando la vol reciente cae por debajo de la ventana plana, hit sube de 63.9% (agregado XRP) a 68.8%, ic_bayes=+0.180 (n=48). Cuando acelera, hit CAE a 57.1%. Confirma que este feature no puede tratarse con un umbral global -- cada activo necesita su propio signo. REFUTADA 13-Jul: recalculado con n=61 (más del doble del n original) usando el mismo método riguroso (percentiles + permutación 20k) que confirmó BTC/SOL/ETH -- el signo se INVIRTIÓ: decel (sigma<0) da IC=-0.065 n=21 (malo), accel (sigma>=0) da IC=+0.071 n=40 (bueno). XRP en realidad tiene el MISMO signo que BTC/ETH (sigma alto=bueno), solo que más débil -- coherente con el patrón ganador ya auto-descubierto por postmortem (sigma_ewma_delta_pct>5.563, ic_patron=+0.20 n=18, mismo signo). El hallazgo ad-hoc del 12-Jul con n=48 no replicó con más datos -- probable ruido de una muestra menor/distinta. Ver idea_estrategia_mercado_bajista... no, ver project_sigma_filtro_sol_xrp_no_promociona_13jul (memoria) para el detalle completo.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: REFUTADA -- no implementar kelly_boost por sigma<0 en XRP. El signo correcto es el opuesto (sigma alto=bueno), ya cubierto por el patron_ganador automático de postmortem sobre GBM_LATE_15M#XRP#15min -- no hace falta ninguna acción manual adicional.
  - _Estado_: n=4894 IC=-0.025 PNL=+1385.71€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=4894 IC=-0.025 PNL=+1385.71€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.243 > 0.08 con n=4734 PNL=-375.75€
  - _Datos_: n=4734 IC=+0.243 PNL=-375.75€

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
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.101 n=1704) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=1704 IC=+0.101 PNL=+373.15€

**🟡 H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: n>=40 y IC>=0.08
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.316 > 0.08 con n=444 PNL=+131.85€
  - _Datos_: n=444 IC=+0.316 PNL=+131.85€

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.415 n=565) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=565 IC=+0.415 PNL=+818.04€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=13831 IC=+0.185 PNL=-1431.50€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=13831 IC=+0.185 PNL=-1431.50€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.216 > 0.1 con n=227 PNL=+147.67€
  - _Datos_: n=227 IC=+0.216 PNL=+147.67€
