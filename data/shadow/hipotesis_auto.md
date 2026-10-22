# Hipótesis automáticas — 2026-10-22 01:43 UTC
_Generado por shadow_postmortem.py sobre 1001565 resoluciones (PNL=+130897.62€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.495` → IC=-0.255 (n=194)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.114 (n=628)

- **PATRÓN** `py_entrada` > `0.515` → IC=+0.234 (n=795)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.515 (IC base=+0.136)

- **PATRÓN** `n_total_lado` > `65.0` → IC=+0.179 (n=285)

  - _Acción_: Kelly boost +0.90€ cuando `n_total_lado` > 65.0 (IC base=+0.136)

- **PATRÓN** `banda_hit_calibrado` > `0.6242` → IC=+0.264 (n=566)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6242 (IC base=+0.136)

- **PATRÓN** `banda_z` > `9.122` → IC=+0.208 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.122 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.165 (n=311)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 17.0 (IC base=+0.136)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=921)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `98.0` → IC=+0.153 (n=465)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 98.0 (IC base=+0.136)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **PATRÓN** `py_entrada` > `0.515` → IC=+0.230 (n=684)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.515 (IC base=+0.141)

- **PATRÓN** `n_total_lado` > `69.0` → IC=+0.199 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 69.0 (IC base=+0.141)

- **PATRÓN** `banda_hit_calibrado` > `0.6165` → IC=+0.257 (n=476)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6165 (IC base=+0.141)

- **PATRÓN** `banda_z` > `9.563` → IC=+0.208 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.563 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.176 (n=260)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.141)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.149 (n=822)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.01 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `3103.76` → IC=+0.142 (n=638)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 3103.76 (IC base=+0.141)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.153 (n=428)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 100.0 (IC base=+0.141)

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
  - _Potencial_: sin este filtro IC_bueno=+0.118 (n=108)

- **FILTRO** `hora_utc` < `10.0` → IC=-0.157 (n=33)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=107)

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
- **FILTRO** `restante_s_al_confirmar` < `142.26` → IC=-0.199 (n=10192)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 142.26
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=30580)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `128.62` → IC=-0.257 (n=1130)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 128.62
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=3392)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `122.08` → IC=-0.287 (n=1095)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 122.08
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=3291)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `167.49` → IC=-0.201 (n=2693)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 167.49
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=8080)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `133.17` → IC=-0.277 (n=1985)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 133.17
  - _Potencial_: sin este filtro IC_bueno=-0.084 (n=5956)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.214 (n=22047)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.107)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.133 (n=4368)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `9064.558` → IC=+0.173 (n=1982)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 9064.558 (IC base=+0.107)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.129 (n=18817)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.128 (n=33637)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 11.0 (IC base=+0.125)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.227 (n=17581)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.149 (n=7263)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `7053.9664` → IC=+0.157 (n=2806)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 7053.9664 (IC base=+0.125)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.198 (n=2039)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 5.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.191 (n=1994)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 17.0 (IC base=+0.190)

- **PATRÓN** `py_entrada` > `0.765` → IC=+0.364 (n=696)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.765 (IC base=+0.190)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.193 (n=2502)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.01 (IC base=+0.190)

- **PATRÓN** `libro_liquidez` > `16423.8774` → IC=+0.197 (n=649)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 16423.8774 (IC base=+0.190)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.189 (n=1794)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 7.0 (IC base=+0.183)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.187 (n=1996)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 17.0 (IC base=+0.183)

- **PATRÓN** `py_entrada` < `0.25` → IC=+0.340 (n=660)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.25 (IC base=+0.183)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.185 (n=2560)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.01 (IC base=+0.183)

- **PATRÓN** `libro_liquidez` > `16193.8223` → IC=+0.193 (n=660)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 16193.8223 (IC base=+0.183)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.61` → IC=+0.172 (n=476)

  - _Acción_: Kelly boost +0.86€ cuando `py_entrada` > 0.61 (IC base=+0.083)

- **PATRÓN** `libro_liquidez` > `6840.9445` → IC=+0.161 (n=125)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 6840.9445 (IC base=+0.083)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.136 (n=1138)

  - _Acción_: Kelly boost +0.68€ cuando `py_entrada` < 0.44 (IC base=+0.081)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.167 (n=4282)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.161)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.163 (n=3626)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 15.0 (IC base=+0.161)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.372 (n=1412)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.161)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.228 (n=792)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.211)

- **PATRÓN** `py_entrada` < `0.265` → IC=+0.348 (n=741)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.265 (IC base=+0.211)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.214 (n=2222)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.211)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.145 (n=1082)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.143)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.148 (n=922)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 15.0 (IC base=+0.143)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.263 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.143)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.147 (n=845)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.01 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `2205.8849` → IC=+0.160 (n=468)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 2205.8849 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.162 (n=152)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.069)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.254 (n=853)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.224)

- **PATRÓN** `py_entrada` > `0.83` → IC=+0.420 (n=1169)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.83 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.151 (n=1294)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 7.0 (IC base=+0.149)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.156 (n=682)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 7.0 (IC base=+0.149)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.285 (n=646)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.149)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=857)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.149)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `9.0` → IC=+0.155 (n=326)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 9.0 (IC base=+0.140)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.352 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.140)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.130 (n=279)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.04 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `1131.3588` → IC=+0.130 (n=260)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 1131.3588 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.135 (n=1135)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 7.0 (IC base=+0.123)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.245 (n=410)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.123)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `11.0` → IC=-0.297 (n=62)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.229 (n=149)

- **FILTRO** `py_entrada` > `0.755` → IC=-0.293 (n=138)

  - _Acción_: SKIP cuando `py_entrada` > 0.755
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=73)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.206 (n=18683)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.202)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.203 (n=15816)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.202)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.236 (n=7673)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.202)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `4837.3339` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4837.3339 (IC base=+0.202)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.183 (n=2039)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 15.0 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.182 (n=4283)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 18.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.183 (n=4214)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` < 0.73 (IC base=+0.180)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.182 (n=3509)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` > 0.71 (IC base=+0.180)

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

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.225 (n=2230)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.223)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.228 (n=2336)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.223)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.305 (n=769)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.223)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.189 (n=4231)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.184 (n=3591)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 15.0 (IC base=+0.182)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.189 (n=3312)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` > 0.71 (IC base=+0.182)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.257 (n=3666)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.248)

- **PATRÓN** `py_entrada` > `0.79` → IC=+0.362 (n=1190)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.194 (n=4143)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 5.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.193 (n=3535)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.190)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.194 (n=3058)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.71 (IC base=+0.190)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.431 (n=801)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.426)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.439 (n=822)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.426)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.430 (n=847)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.426)

- **PATRÓN** `libro_liquidez` > `4222.1963` → IC=+0.435 (n=523)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4222.1963 (IC base=+0.426)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.430 (n=314)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.432)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.441 (n=218)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.432)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.445 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.432)

- **PATRÓN** `libro_liquidez` > `12072.2649` → IC=+0.439 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12072.2649 (IC base=+0.432)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.451 (n=221)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.432)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.444 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.432)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.435 (n=353)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.432)

- **PATRÓN** `libro_liquidez` > `4514.7204` → IC=+0.434 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4514.7204 (IC base=+0.432)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.404 (n=144)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.400)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.402 (n=141)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.400)

- **PATRÓN** `py_entrada` > `0.93` → IC=+0.428 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.93 (IC base=+0.400)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.77` → IC=-0.318 (n=31)

  - _Acción_: SKIP cuando `py_entrada` > 0.77
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=11)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=26)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.212 (n=20892)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.202)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.247 (n=24453)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.202)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.196 (n=3607)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 18.0 (IC base=+0.186)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.188 (n=7715)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 12.0 (IC base=+0.186)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.201 (n=10868)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.71 (IC base=+0.186)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.227 (n=5078)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.227 (n=4951)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.225)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.285 (n=3543)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.225)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.189 (n=4168)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 17.0 (IC base=+0.182)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.212 (n=5526)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.182)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.835` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.835
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.233 (n=3405)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.221)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.223 (n=3872)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.221)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.276 (n=3447)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.221)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.206 (n=9300)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.260 (n=3603)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.209 (n=4042)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.199 (n=4042)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.249 (n=4224)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.198)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.192 (n=8828)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.139 (n=8626)

  - _Acción_: Kelly boost +0.69€ cuando `restante_min` > 4.96 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `3.77` → IC=+0.135 (n=10571)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 3.77 (IC base=+0.116)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.195 (n=4361)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.119)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.142 (n=4414)

  - _Acción_: Kelly boost +0.71€ cuando `restante_min` > 4.95 (IC base=+0.119)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.129 (n=5274)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 7.0 (IC base=+0.119)

- **PATRÓN** `lag_apertura_s` < `2.76` → IC=+0.146 (n=3980)

  - _Acción_: Kelly boost +0.73€ cuando `lag_apertura_s` < 2.76 (IC base=+0.119)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.188 (n=4467)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` < 0.38 (IC base=+0.113)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.134 (n=4694)

  - _Acción_: Kelly boost +0.67€ cuando `restante_min` > 4.96 (IC base=+0.113)

- **PATRÓN** `lag_apertura_s` < `3.33` → IC=+0.133 (n=5316)

  - _Acción_: Kelly boost +0.67€ cuando `lag_apertura_s` < 3.33 (IC base=+0.113)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.301 (n=1689)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.293)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.381 (n=579)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.293)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.288 (n=768)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.281)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.354 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.281)

- **PATRÓN** `libro_liquidez` > `4528.2881` → IC=+0.285 (n=487)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4528.2881 (IC base=+0.281)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.321 (n=546)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.298)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.301 (n=799)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.298)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.392 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.298)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.298 (n=665)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.298)

- **PATRÓN** `libro_liquidez` > `2113.1713` → IC=+0.315 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2113.1713 (IC base=+0.298)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.357 (n=82)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.352)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.378 (n=80)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.352)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.391 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.352)

- **PATRÓN** `libro_spread` < `0.07` → IC=+0.357 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.07 (IC base=+0.352)

- **PATRÓN** `libro_liquidez` > `761.0655` → IC=+0.380 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 761.0655 (IC base=+0.352)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.446 (n=780)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.442)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.443 (n=767)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.442)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.445 (n=539)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.442)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.443 (n=886)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.442)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.439 (n=373)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.435)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.437 (n=253)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.435)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.437 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.435)

- **PATRÓN** `py_entrada` > `0.935` → IC=+0.439 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.935 (IC base=+0.435)

- **PATRÓN** `libro_liquidez` > `5360.5654` → IC=+0.434 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5360.5654 (IC base=+0.435)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.469 (n=125)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.450)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.452 (n=355)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.450)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.452 (n=331)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.450)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.451 (n=406)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.450)

- **PATRÓN** `libro_liquidez` > `1981.0007` → IC=+0.468 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1981.0007 (IC base=+0.450)

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

- **FILTRO** `hora_utc` > `15.0` → IC=-0.308 (n=24)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=92)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.238 (n=59)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.195 (n=57)

- **FILTRO** `libro_liquidez` < `1798.9075` → IC=-0.230 (n=87)

  - _Acción_: SKIP cuando `libro_liquidez` < 1798.9075
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=29)

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

- **FILTRO** `hora_utc` > `15.0` → IC=-0.308 (n=24)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=92)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.238 (n=59)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.195 (n=57)

- **FILTRO** `libro_liquidez` < `1798.9075` → IC=-0.230 (n=87)

  - _Acción_: SKIP cuando `libro_liquidez` < 1798.9075
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=29)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4753` → IC=+0.140 (n=13606)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.4753 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.126 (n=13770)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 6.0 (IC base=+0.122)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.125 (n=9480)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 12.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` > `0.3793` → IC=+0.167 (n=13608)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.3793 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` > `0.7908` → IC=+0.275 (n=783)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7908 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` < `0.3728` → IC=+0.260 (n=3809)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3728 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.901` → IC=+0.192 (n=5143)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 5.901 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` < `1.2041` → IC=+0.260 (n=3965)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2041 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` > `0.6183` → IC=+0.266 (n=3965)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6183 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` > `0.3025` → IC=+0.242 (n=1388)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3025 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` > `2.3476` → IC=+0.230 (n=4396)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3476 (IC base=+0.122)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.127 (n=7206)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.01 (IC base=+0.122)

- **PATRÓN** `ibs_20min` < `0.6849` → IC=+0.130 (n=19013)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` < 0.6849 (IC base=+0.075)

- **PATRÓN** `dist_vwap_pct` > `0.5985` → IC=+0.188 (n=1167)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.5985 (IC base=+0.075)

- **PATRÓN** `dist_vwap_pct` < `0.1557` → IC=+0.187 (n=6122)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` < 0.1557 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` < `0.6961` → IC=+0.187 (n=2872)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 0.6961 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` > `1.0505` → IC=+0.183 (n=2956)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` > 1.0505 (IC base=+0.075)

- **PATRÓN** `volumen_pendiente_norm` > `0.2959` → IC=+0.233 (n=1627)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2959 (IC base=+0.075)

- **PATRÓN** `volumen_spike_ratio` > `2.6803` → IC=+0.207 (n=3699)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6803 (IC base=+0.075)

- **PATRÓN** `ballena_activa_n` < `107.0` → IC=+0.222 (n=10958)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 107.0 (IC base=+0.075)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.208 (n=992)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.201)

- **PATRÓN** `drift_60min` |x|≤ `0.3472` → IC=+0.205 (n=2959)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3472 (IC base=+0.201)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.212 (n=1446)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.201)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.204 (n=1976)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.201)

- **PATRÓN** `ibs_20min` > `0.9825` → IC=+0.279 (n=1343)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9825 (IC base=+0.201)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.836` → IC=+0.285 (n=1297)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.836 (IC base=+0.201)

- **PATRÓN** `volumen_pendiente_norm` > `0.2341` → IC=+0.249 (n=520)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2341 (IC base=+0.201)

- **PATRÓN** `volumen_spike_ratio` > `1.4411` → IC=+0.203 (n=2823)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4411 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.215 (n=3185)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.201)

- **PATRÓN** `libro_liquidez` > `2074.38` → IC=+0.208 (n=987)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2074.38 (IC base=+0.201)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.217 (n=1799)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 14.0 (IC base=+0.201)

- **PATRÓN** `sigma_h` < `0.0085` → IC=+0.239 (n=2473)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0085 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.0871` → IC=+0.272 (n=825)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0871 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.256 (n=910)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` < `0.5324` → IC=+0.258 (n=2473)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5324 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` < `0.0941` → IC=+0.239 (n=2219)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0941 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.2886` → IC=+0.263 (n=335)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2886 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` < `1.4411` → IC=+0.242 (n=778)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4411 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `2.6727` → IC=+0.246 (n=778)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6727 (IC base=+0.237)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.241 (n=2790)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.237)

- **PATRÓN** `libro_liquidez` > `1618.281` → IC=+0.247 (n=2209)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1618.281 (IC base=+0.237)

- **PATRÓN** `ballena_activa_n` < `9.0` → IC=+0.239 (n=1083)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 9.0 (IC base=+0.237)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.239 (n=1069)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.229)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.232 (n=1101)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.229)

- **PATRÓN** `drift_60min` |x|≤ `0.1057` → IC=+0.262 (n=1068)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1057 (IC base=+0.229)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.241 (n=2545)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.229)

- **PATRÓN** `ibs_20min` > `0.9484` → IC=+0.281 (n=809)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9484 (IC base=+0.229)

- **PATRÓN** `dist_vwap_pct` > `0.1308` → IC=+0.237 (n=1315)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1308 (IC base=+0.229)

- **PATRÓN** `dist_vwap_pct` < `0.3409` → IC=+0.231 (n=2340)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3409 (IC base=+0.229)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.335` → IC=+0.266 (n=366)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.335 (IC base=+0.229)

- **PATRÓN** `volumen_regimen` < `1.2333` → IC=+0.230 (n=2428)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2333 (IC base=+0.229)

- **PATRÓN** `volumen_regimen` > `0.6219` → IC=+0.234 (n=2427)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6219 (IC base=+0.229)

- **PATRÓN** `volumen_pendiente_norm` > `0.2778` → IC=+0.269 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2778 (IC base=+0.229)

- **PATRÓN** `volumen_spike_ratio` > `2.4426` → IC=+0.258 (n=797)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4426 (IC base=+0.229)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.151 (n=2478)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0057 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.0755` → IC=+0.169 (n=826)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.0755 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.156 (n=941)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 17.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` < `0.7268` → IC=+0.177 (n=2476)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.7268 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` < `0.1358` → IC=+0.153 (n=2297)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.1358 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.071` → IC=+0.150 (n=401)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 11.071 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.189` → IC=+0.141 (n=2261)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` < 4.189 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `1.2044` → IC=+0.141 (n=2476)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 1.2044 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` > `0.0952` → IC=+0.159 (n=902)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.0952 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` < `2.4535` → IC=+0.144 (n=2356)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.4535 (IC base=+0.133)

- **PATRÓN** `ballena_activa_n` < `216.0` → IC=+0.174 (n=1005)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 216.0 (IC base=+0.133)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0121` → IC=+0.224 (n=1026)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0121 (IC base=+0.196)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.202 (n=3230)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.196)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.271 (n=1180)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.196)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.249` → IC=+0.274 (n=647)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.249 (IC base=+0.196)

- **PATRÓN** `volumen_pendiente_norm` < `0.0976` → IC=+0.201 (n=2729)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0976 (IC base=+0.196)

- **PATRÓN** `volumen_pendiente_norm` > `0.352` → IC=+0.213 (n=395)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.352 (IC base=+0.196)

- **PATRÓN** `volumen_spike_ratio` > `2.6967` → IC=+0.212 (n=1354)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6967 (IC base=+0.196)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.203 (n=3687)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.196)

- **PATRÓN** `libro_liquidez` > `1965.3584` → IC=+0.201 (n=1395)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1965.3584 (IC base=+0.196)

- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.223 (n=2433)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0106 (IC base=+0.217)

- **PATRÓN** `drift_60min` |x|≤ `0.178` → IC=+0.233 (n=1214)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.178 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.244 (n=1041)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.217)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.218 (n=971)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.217)

- **PATRÓN** `ibs_20min` < `0.0192` → IC=+0.277 (n=920)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0192 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.37` → IC=+0.253 (n=334)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.37 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` > `0.3473` → IC=+0.259 (n=397)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3473 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` > `2.7276` → IC=+0.229 (n=1189)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7276 (IC base=+0.217)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.222 (n=1442)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.217)

- **PATRÓN** `libro_liquidez` > `1953.345` → IC=+0.220 (n=1251)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1953.345 (IC base=+0.217)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.221 (n=2295)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 24.0 (IC base=+0.217)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.143 (n=152)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=3717)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.165 (n=547)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0037 (IC base=+0.056)

- **PATRÓN** `ibs_20min` > `0.9538` → IC=+0.231 (n=545)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9538 (IC base=+0.056)

- **PATRÓN** `dist_vwap_pct` > `0.1404` → IC=+0.335 (n=373)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1404 (IC base=+0.056)

- **PATRÓN** `dist_vwap_pct` < `0.5197` → IC=+0.334 (n=647)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5197 (IC base=+0.056)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.142` → IC=+0.192 (n=1177)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 5.142 (IC base=+0.056)

- **PATRÓN** `volumen_regimen` < `0.858` → IC=+0.336 (n=413)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.858 (IC base=+0.056)

- **PATRÓN** `volumen_regimen` > `1.2251` → IC=+0.351 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2251 (IC base=+0.056)

- **PATRÓN** `volumen_pendiente_norm` < `0.1663` → IC=+0.329 (n=507)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1663 (IC base=+0.056)

- **PATRÓN** `volumen_pendiente_norm` > `0.2965` → IC=+0.349 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2965 (IC base=+0.056)

- **PATRÓN** `volumen_spike_ratio` < `1.4107` → IC=+0.352 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4107 (IC base=+0.056)

- **PATRÓN** `volumen_spike_ratio` > `2.2172` → IC=+0.329 (n=273)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2172 (IC base=+0.056)

- **PATRÓN** `ballena_activa_n` < `132.0` → IC=+0.339 (n=537)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 132.0 (IC base=+0.056)

- **PATRÓN** `ibs_20min` < `0.093` → IC=+0.176 (n=969)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.093 (IC base=+0.037)

- **PATRÓN** `dist_vwap_pct` > `0.7249` → IC=+0.151 (n=236)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.7249 (IC base=+0.037)

- **PATRÓN** `dist_vwap_pct` < `0.1309` → IC=+0.140 (n=1575)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.1309 (IC base=+0.037)

- **PATRÓN** `volumen_regimen` < `0.8414` → IC=+0.149 (n=1149)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.8414 (IC base=+0.037)

- **PATRÓN** `volumen_regimen` > `1.1677` → IC=+0.146 (n=574)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 1.1677 (IC base=+0.037)

- **PATRÓN** `volumen_pendiente_norm` > `0.2851` → IC=+0.203 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2851 (IC base=+0.037)

- **PATRÓN** `volumen_spike_ratio` < `1.7775` → IC=+0.140 (n=1101)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.7775 (IC base=+0.037)

- **PATRÓN** `volumen_spike_ratio` > `2.155` → IC=+0.153 (n=748)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 2.155 (IC base=+0.037)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.173 (n=105)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.072 (n=568)

- **FILTRO** `ibs_20min` < `0.2759` → IC=-0.194 (n=168)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2759
  - _Potencial_: sin este filtro IC_bueno=+0.110 (n=505)

- **FILTRO** `ibs_20min` > `0.2174` → IC=-0.132 (n=3645)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2174
  - _Potencial_: sin este filtro IC_bueno=+0.146 (n=1800)

- **FILTRO** `sigma_ewma_delta_pct` > `8.654` → IC=-0.238 (n=575)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.654
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=4870)

- **PATRÓN** `ibs_20min` > `0.7857` → IC=+0.188 (n=229)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.7857 (IC base=+0.033)

- **PATRÓN** `dist_vwap_pct` > `1.0155` → IC=+0.285 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0155 (IC base=+0.033)

- **PATRÓN** `dist_vwap_pct` < `0.4916` → IC=+0.264 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4916 (IC base=+0.033)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.37` → IC=+0.143 (n=236)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 2.37 (IC base=+0.033)

- **PATRÓN** `volumen_regimen` > `1.0233` → IC=+0.308 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0233 (IC base=+0.033)

- **PATRÓN** `volumen_pendiente_norm` < `0.1586` → IC=+0.279 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1586 (IC base=+0.033)

- **PATRÓN** `volumen_spike_ratio` < `2.5444` → IC=+0.290 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5444 (IC base=+0.033)

- **PATRÓN** `volumen_spike_ratio` > `1.5504` → IC=+0.270 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5504 (IC base=+0.033)

- **PATRÓN** `ballena_activa_n` < `38.0` → IC=+0.268 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 38.0 (IC base=+0.033)

- **PATRÓN** `ibs_20min` < `0.2174` → IC=+0.146 (n=1800)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.2174 (IC base=-0.040)

- **PATRÓN** `dist_vwap_pct` > `0.2659` → IC=+0.281 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2659 (IC base=-0.040)

- **PATRÓN** `volumen_regimen` < `0.7052` → IC=+0.305 (n=327)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7052 (IC base=-0.040)

- **PATRÓN** `volumen_pendiente_norm` > `0.0812` → IC=+0.303 (n=318)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0812 (IC base=-0.040)

- **PATRÓN** `volumen_spike_ratio` < `2.43` → IC=+0.300 (n=677)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.43 (IC base=-0.040)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6093` → IC=-0.181 (n=1001)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6093
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=3005)

- **FILTRO** `ibs_20min` < `0.7571` → IC=-0.150 (n=2643)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7571
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=1363)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.162 (n=966)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=3040)

- **FILTRO** `ibs_20min` > `0.75` → IC=-0.203 (n=1435)

  - _Acción_: SKIP cuando `ibs_20min` > 0.75
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=4326)

- **PATRÓN** `dist_vwap_pct` > `1.0882` → IC=+0.345 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0882 (IC base=-0.065)

- **PATRÓN** `dist_vwap_pct` < `0.2486` → IC=+0.305 (n=608)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2486 (IC base=-0.065)

- **PATRÓN** `volumen_regimen` < `1.1457` → IC=+0.298 (n=707)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1457 (IC base=-0.065)

- **PATRÓN** `volumen_regimen` > `0.704` → IC=+0.317 (n=632)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.704 (IC base=-0.065)

- **PATRÓN** `volumen_pendiente_norm` < `0.0986` → IC=+0.303 (n=664)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0986 (IC base=-0.065)

- **PATRÓN** `volumen_pendiente_norm` > `0.071` → IC=+0.305 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.071 (IC base=-0.065)

- **PATRÓN** `volumen_spike_ratio` < `1.4142` → IC=+0.318 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4142 (IC base=-0.065)

- **PATRÓN** `volumen_spike_ratio` > `1.8367` → IC=+0.306 (n=456)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8367 (IC base=-0.065)

- **PATRÓN** `dist_vwap_pct` > `0.8089` → IC=+0.288 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8089 (IC base=-0.005)

- **PATRÓN** `volumen_regimen` < `0.7166` → IC=+0.259 (n=696)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7166 (IC base=-0.005)

- **PATRÓN** `volumen_regimen` > `1.0685` → IC=+0.287 (n=717)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0685 (IC base=-0.005)

- **PATRÓN** `volumen_pendiente_norm` > `0.1044` → IC=+0.285 (n=546)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1044 (IC base=-0.005)

- **PATRÓN** `volumen_spike_ratio` < `2.1803` → IC=+0.264 (n=1285)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1803 (IC base=-0.005)

- **PATRÓN** `volumen_spike_ratio` > `1.4298` → IC=+0.267 (n=1460)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4298 (IC base=-0.005)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.210 (n=5968)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0098 (IC base=+0.097)

- **PATRÓN** `ibs_20min` > `0.3194` → IC=+0.169 (n=17869)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` > 0.3194 (IC base=+0.097)

- **PATRÓN** `dist_vwap_pct` > `0.955` → IC=+0.301 (n=1335)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.955 (IC base=+0.097)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.592` → IC=+0.163 (n=8023)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 3.592 (IC base=+0.097)

- **PATRÓN** `volumen_regimen` < `1.1721` → IC=+0.265 (n=6592)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1721 (IC base=+0.097)

- **PATRÓN** `volumen_regimen` > `0.6884` → IC=+0.271 (n=5888)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6884 (IC base=+0.097)

- **PATRÓN** `volumen_pendiente_norm` > `0.2397` → IC=+0.279 (n=1969)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2397 (IC base=+0.097)

- **PATRÓN** `volumen_spike_ratio` < `1.4599` → IC=+0.263 (n=3504)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4599 (IC base=+0.097)

- **PATRÓN** `volumen_spike_ratio` > `2.2732` → IC=+0.271 (n=4765)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2732 (IC base=+0.097)

- **PATRÓN** `ballena_activa_n` < `92.0` → IC=+0.297 (n=10107)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 92.0 (IC base=+0.097)

- **PATRÓN** `sigma_h` > `0.0093` → IC=+0.155 (n=5738)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0093 (IC base=+0.074)

- **PATRÓN** `ibs_20min` < `0.6585` → IC=+0.144 (n=17184)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.6585 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` < `0.2425` → IC=+0.265 (n=5364)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2425 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` < `0.7048` → IC=+0.264 (n=2381)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7048 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` > `1.1961` → IC=+0.267 (n=1804)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1961 (IC base=+0.074)

- **PATRÓN** `volumen_pendiente_norm` > `0.2944` → IC=+0.316 (n=1166)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2944 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` < `1.5798` → IC=+0.290 (n=3429)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5798 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` > `2.2668` → IC=+0.283 (n=3534)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2668 (IC base=+0.074)

- **PATRÓN** `ballena_activa_n` < `77.0` → IC=+0.295 (n=7736)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 77.0 (IC base=+0.074)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.5817` → IC=-0.130 (n=2448)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5817
  - _Potencial_: sin este filtro IC_bueno=+0.192 (n=2449)

- **FILTRO** `ibs_20min` > `0.7404` → IC=-0.215 (n=1036)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7404
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=3110)

- **FILTRO** `sigma_ewma_delta_pct` > `4.358` → IC=-0.210 (n=909)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.358
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=3237)

- **PATRÓN** `ibs_20min` > `0.9222` → IC=+0.317 (n=1225)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9222 (IC base=+0.031)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.963` → IC=+0.216 (n=869)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.963 (IC base=+0.031)

- **PATRÓN** `volumen_pendiente_norm` > `0.2302` → IC=+0.303 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2302 (IC base=+0.031)

- **PATRÓN** `volumen_spike_ratio` < `1.4432` → IC=+0.252 (n=535)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4432 (IC base=+0.031)

- **PATRÓN** `volumen_spike_ratio` > `2.2557` → IC=+0.276 (n=727)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2557 (IC base=+0.031)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.283 (n=1090)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.031)

- **PATRÓN** `ibs_20min` < `0.1667` → IC=+0.159 (n=1040)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.1667 (IC base=-0.030)

- **PATRÓN** `volumen_pendiente_norm` < `0.0738` → IC=+0.411 (n=492)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0738 (IC base=-0.030)

- **PATRÓN** `volumen_spike_ratio` < `2.5999` → IC=+0.405 (n=553)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5999 (IC base=-0.030)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.400 (n=516)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 21.0 (IC base=-0.030)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `ibs_20min` > `0.8454` → IC=+0.146 (n=1232)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` > 0.8454 (IC base=+0.024)

- **PATRÓN** `dist_vwap_pct` > `0.1157` → IC=+0.218 (n=893)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1157 (IC base=+0.024)

- **PATRÓN** `volumen_regimen` < `1.1961` → IC=+0.195 (n=1744)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 1.1961 (IC base=+0.024)

- **PATRÓN** `volumen_regimen` > `0.6835` → IC=+0.204 (n=1558)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6835 (IC base=+0.024)

- **PATRÓN** `volumen_pendiente_norm` < `0.0746` → IC=+0.193 (n=1600)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` < 0.0746 (IC base=+0.024)

- **PATRÓN** `volumen_pendiente_norm` > `0.2762` → IC=+0.233 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2762 (IC base=+0.024)

- **PATRÓN** `volumen_spike_ratio` < `1.425` → IC=+0.218 (n=573)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.425 (IC base=+0.024)

- **PATRÓN** `volumen_spike_ratio` > `2.4911` → IC=+0.196 (n=573)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.4911 (IC base=+0.024)

- **PATRÓN** `ballena_activa_n` < `273.0` → IC=+0.229 (n=1143)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 273.0 (IC base=+0.024)

- **PATRÓN** `dist_vwap_pct` < `0.2987` → IC=+0.232 (n=1250)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2987 (IC base=-0.004)

- **PATRÓN** `volumen_regimen` < `1.1702` → IC=+0.227 (n=1124)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1702 (IC base=-0.004)

- **PATRÓN** `volumen_regimen` > `0.6195` → IC=+0.233 (n=1124)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6195 (IC base=-0.004)

- **PATRÓN** `volumen_pendiente_norm` > `0.2713` → IC=+0.294 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2713 (IC base=-0.004)

- **PATRÓN** `volumen_spike_ratio` < `1.5317` → IC=+0.237 (n=474)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5317 (IC base=-0.004)

- **PATRÓN** `volumen_spike_ratio` > `2.1598` → IC=+0.246 (n=487)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1598 (IC base=-0.004)

- **PATRÓN** `ballena_activa_n` < `201.0` → IC=+0.242 (n=363)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 201.0 (IC base=-0.004)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0119` → IC=+0.310 (n=867)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0119 (IC base=+0.269)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.276 (n=2731)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.269)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.311 (n=1371)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.269)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.678` → IC=+0.301 (n=837)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.678 (IC base=+0.269)

- **PATRÓN** `volumen_pendiente_norm` < `0.0981` → IC=+0.282 (n=2267)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0981 (IC base=+0.269)

- **PATRÓN** `volumen_spike_ratio` > `1.6104` → IC=+0.274 (n=2513)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6104 (IC base=+0.269)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.280 (n=3096)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.269)

- **PATRÓN** `libro_liquidez` > `2049.0084` → IC=+0.286 (n=867)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2049.0084 (IC base=+0.269)

- **PATRÓN** `ballena_activa_n` < `18.0` → IC=+0.287 (n=1532)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 18.0 (IC base=+0.269)

- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.324 (n=1023)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0101 (IC base=+0.292)

- **PATRÓN** `drift_60min` |x|≤ `0.1806` → IC=+0.310 (n=993)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1806 (IC base=+0.292)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.321 (n=867)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.292)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.292 (n=791)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.292)

- **PATRÓN** `ibs_20min` < `0.3711` → IC=+0.295 (n=2256)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3711 (IC base=+0.292)

- **PATRÓN** `ibs_20min` > `0.2629` → IC=+0.298 (n=1024)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2629 (IC base=+0.292)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.522` → IC=+0.310 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.522 (IC base=+0.292)

- **PATRÓN** `volumen_pendiente_norm` < `0.1975` → IC=+0.291 (n=2205)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1975 (IC base=+0.292)

- **PATRÓN** `volumen_pendiente_norm` > `0.3414` → IC=+0.303 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3414 (IC base=+0.292)

- **PATRÓN** `volumen_spike_ratio` < `1.7295` → IC=+0.297 (n=949)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7295 (IC base=+0.292)

- **PATRÓN** `volumen_spike_ratio` > `2.6617` → IC=+0.302 (n=977)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6617 (IC base=+0.292)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.294 (n=1184)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.292)

- **PATRÓN** `libro_liquidez` > `2039.1572` → IC=+0.309 (n=752)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2039.1572 (IC base=+0.292)

- **PATRÓN** `ballena_activa_n` < `18.0` → IC=+0.293 (n=1423)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 18.0 (IC base=+0.292)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.737` → IC=-0.189 (n=1083)

  - _Acción_: SKIP cuando `ibs_20min` > 0.737
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=3251)

- **PATRÓN** `ibs_20min` > `0.8769` → IC=+0.175 (n=1034)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` > 0.8769 (IC base=+0.030)

- **PATRÓN** `dist_vwap_pct` > `0.1552` → IC=+0.232 (n=794)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1552 (IC base=+0.030)

- **PATRÓN** `dist_vwap_pct` < `0.3685` → IC=+0.235 (n=1411)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3685 (IC base=+0.030)

- **PATRÓN** `volumen_regimen` < `1.0082` → IC=+0.243 (n=1284)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0082 (IC base=+0.030)

- **PATRÓN** `volumen_regimen` > `0.6671` → IC=+0.231 (n=1303)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6671 (IC base=+0.030)

- **PATRÓN** `volumen_pendiente_norm` < `0.1635` → IC=+0.237 (n=1543)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1635 (IC base=+0.030)

- **PATRÓN** `volumen_pendiente_norm` > `0.1024` → IC=+0.243 (n=462)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1024 (IC base=+0.030)

- **PATRÓN** `volumen_spike_ratio` < `2.4348` → IC=+0.239 (n=1410)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4348 (IC base=+0.030)

- **PATRÓN** `ballena_activa_n` < `102.0` → IC=+0.265 (n=1261)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 102.0 (IC base=+0.030)

- **PATRÓN** `dist_vwap_pct` < `0.3357` → IC=+0.235 (n=1082)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3357 (IC base=-0.002)

- **PATRÓN** `volumen_regimen` < `1.0307` → IC=+0.240 (n=875)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0307 (IC base=-0.002)

- **PATRÓN** `volumen_pendiente_norm` < `0.1015` → IC=+0.251 (n=921)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1015 (IC base=-0.002)

- **PATRÓN** `volumen_pendiente_norm` > `0.2852` → IC=+0.291 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2852 (IC base=-0.002)

- **PATRÓN** `volumen_spike_ratio` < `1.7982` → IC=+0.272 (n=629)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7982 (IC base=-0.002)

- **PATRÓN** `volumen_spike_ratio` > `2.4393` → IC=+0.254 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4393 (IC base=-0.002)

- **PATRÓN** `ballena_activa_n` < `124.0` → IC=+0.261 (n=954)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 124.0 (IC base=-0.002)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7619` → IC=-0.214 (n=1881)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7619
  - _Potencial_: sin este filtro IC_bueno=+0.307 (n=1881)

- **FILTRO** `ibs_20min` > `0.6489` → IC=-0.238 (n=913)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6489
  - _Potencial_: sin este filtro IC_bueno=+0.121 (n=2743)

- **FILTRO** `sigma_ewma_delta_pct` > `8.49` → IC=-0.249 (n=428)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.49
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=3228)

- **PATRÓN** `ibs_20min` > `0.7619` → IC=+0.307 (n=1881)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7619 (IC base=+0.046)

- **PATRÓN** `dist_vwap_pct` > `0.2157` → IC=+0.339 (n=841)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2157 (IC base=+0.046)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.495` → IC=+0.186 (n=585)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 9.495 (IC base=+0.046)

- **PATRÓN** `volumen_regimen` < `0.8471` → IC=+0.334 (n=943)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8471 (IC base=+0.046)

- **PATRÓN** `volumen_regimen` > `0.7021` → IC=+0.327 (n=1261)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7021 (IC base=+0.046)

- **PATRÓN** `volumen_pendiente_norm` < `0.159` → IC=+0.323 (n=1457)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.159 (IC base=+0.046)

- **PATRÓN** `volumen_pendiente_norm` > `0.275` → IC=+0.356 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.275 (IC base=+0.046)

- **PATRÓN** `volumen_spike_ratio` < `1.4408` → IC=+0.350 (n=458)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4408 (IC base=+0.046)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.341 (n=1207)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 48.0 (IC base=+0.046)

- **PATRÓN** `ibs_20min` < `0.6489` → IC=+0.121 (n=2743)

  - _Acción_: Kelly boost +0.61€ cuando `ibs_20min` < 0.6489 (IC base=+0.031)

- **PATRÓN** `dist_vwap_pct` < `0.2041` → IC=+0.252 (n=1121)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2041 (IC base=+0.031)

- **PATRÓN** `volumen_regimen` < `0.7014` → IC=+0.262 (n=532)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7014 (IC base=+0.031)

- **PATRÓN** `volumen_pendiente_norm` < `0.2248` → IC=+0.243 (n=1359)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2248 (IC base=+0.031)

- **PATRÓN** `volumen_pendiente_norm` > `0.0758` → IC=+0.264 (n=460)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0758 (IC base=+0.031)

- **PATRÓN** `volumen_spike_ratio` < `2.4253` → IC=+0.252 (n=1161)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4253 (IC base=+0.031)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.271 (n=1181)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 52.0 (IC base=+0.031)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0109` → IC=+0.348 (n=1767)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0109 (IC base=+0.304)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.308 (n=771)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.304)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.314 (n=939)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.304)

- **PATRÓN** `ibs_20min` > `0.6604` → IC=+0.336 (n=1979)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6604 (IC base=+0.304)

- **PATRÓN** `dist_vwap_pct` > `0.209` → IC=+0.331 (n=1124)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.209 (IC base=+0.304)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.813` → IC=+0.324 (n=959)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.813 (IC base=+0.304)

- **PATRÓN** `volumen_regimen` > `0.8621` → IC=+0.321 (n=1319)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8621 (IC base=+0.304)

- **PATRÓN** `volumen_pendiente_norm` > `0.279` → IC=+0.344 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.279 (IC base=+0.304)

- **PATRÓN** `volumen_spike_ratio` > `1.7999` → IC=+0.321 (n=1264)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7999 (IC base=+0.304)

- **PATRÓN** `libro_liquidez` > `2618.726` → IC=+0.310 (n=1319)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2618.726 (IC base=+0.304)

- **PATRÓN** `ballena_activa_n` < `41.0` → IC=+0.338 (n=1705)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 41.0 (IC base=+0.304)

- **PATRÓN** `sigma_h` > `0.0152` → IC=+0.336 (n=1390)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0152 (IC base=+0.305)

- **PATRÓN** `drift_60min` |x|≤ `0.187` → IC=+0.305 (n=918)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.187 (IC base=+0.305)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.317 (n=814)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.305)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.306 (n=1018)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.305)

- **PATRÓN** `ibs_20min` < `0.3676` → IC=+0.329 (n=2086)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3676 (IC base=+0.305)

- **PATRÓN** `dist_vwap_pct` < `0.2283` → IC=+0.309 (n=1967)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2283 (IC base=+0.305)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.603` → IC=+0.315 (n=771)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.603 (IC base=+0.305)

- **PATRÓN** `volumen_regimen` < `0.7185` → IC=+0.311 (n=920)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7185 (IC base=+0.305)

- **PATRÓN** `volumen_regimen` > `1.2242` → IC=+0.335 (n=695)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2242 (IC base=+0.305)

- **PATRÓN** `volumen_pendiente_norm` > `0.2838` → IC=+0.354 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2838 (IC base=+0.305)

- **PATRÓN** `volumen_spike_ratio` < `1.4153` → IC=+0.315 (n=637)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4153 (IC base=+0.305)

- **PATRÓN** `volumen_spike_ratio` > `2.1363` → IC=+0.306 (n=865)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1363 (IC base=+0.305)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0115` → IC=+0.226 (n=4400)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0115 (IC base=+0.181)

- **PATRÓN** `drift_60min` |x|≤ `0.0872` → IC=+0.202 (n=4400)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0872 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.191 (n=13706)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` > `0.5585` → IC=+0.235 (n=13199)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5585 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` > `0.1656` → IC=+0.209 (n=5374)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1656 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.2` → IC=+0.262 (n=2594)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.2 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `1.1889` → IC=+0.169 (n=8756)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 1.1889 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` > `0.6234` → IC=+0.165 (n=8756)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 0.6234 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.2928` → IC=+0.207 (n=1930)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2928 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `2.6108` → IC=+0.193 (n=4267)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.6108 (IC base=+0.181)

- **PATRÓN** `libro_liquidez` > `1972.7784` → IC=+0.182 (n=11791)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 1972.7784 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `94.0` → IC=+0.199 (n=12115)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 94.0 (IC base=+0.181)

- **PATRÓN** `sigma_h` < `0.007` → IC=+0.186 (n=8418)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.007 (IC base=+0.181)

- **PATRÓN** `drift_60min` |x|≤ `0.0796` → IC=+0.229 (n=4215)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0796 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.216 (n=4739)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.237 (n=12630)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` < `0.1751` → IC=+0.175 (n=8934)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` < 0.1751 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.007` → IC=+0.199 (n=2060)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 10.007 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.684` → IC=+0.182 (n=11148)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` < 2.684 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `1.1823` → IC=+0.164 (n=9007)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.1823 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.2945` → IC=+0.226 (n=1875)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2945 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `2.6394` → IC=+0.187 (n=3958)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.6394 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.193 (n=11614)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 100.0 (IC base=+0.181)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.233 (n=747)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.216)

- **PATRÓN** `drift_60min` |x|≤ `0.3316` → IC=+0.234 (n=2215)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3316 (IC base=+0.216)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.228 (n=829)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.216)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.222 (n=1492)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.216)

- **PATRÓN** `ibs_20min` > `0.9286` → IC=+0.294 (n=1478)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9286 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.906` → IC=+0.327 (n=704)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.906 (IC base=+0.216)

- **PATRÓN** `volumen_pendiente_norm` > `0.2807` → IC=+0.275 (n=332)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2807 (IC base=+0.216)

- **PATRÓN** `volumen_spike_ratio` > `1.4375` → IC=+0.217 (n=2098)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4375 (IC base=+0.216)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.229 (n=2407)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.216)

- **PATRÓN** `sigma_h` < `0.0082` → IC=+0.252 (n=1713)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0082 (IC base=+0.250)

- **PATRÓN** `sigma_h` > `0.0074` → IC=+0.262 (n=779)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0074 (IC base=+0.250)

- **PATRÓN** `drift_60min` |x|≤ `0.0649` → IC=+0.309 (n=569)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0649 (IC base=+0.250)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.256 (n=1750)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.250)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.252 (n=820)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.250)

- **PATRÓN** `ibs_20min` < `0.2973` → IC=+0.275 (n=1501)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2973 (IC base=+0.250)

- **PATRÓN** `volumen_pendiente_norm` < `0.1004` → IC=+0.253 (n=1489)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1004 (IC base=+0.250)

- **PATRÓN** `volumen_pendiente_norm` > `0.298` → IC=+0.289 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.298 (IC base=+0.250)

- **PATRÓN** `volumen_spike_ratio` < `1.4356` → IC=+0.275 (n=539)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4356 (IC base=+0.250)

- **PATRÓN** `volumen_spike_ratio` > `2.7079` → IC=+0.256 (n=539)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7079 (IC base=+0.250)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.255 (n=1927)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.250)

- **PATRÓN** `libro_liquidez` > `1513.3152` → IC=+0.259 (n=1706)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1513.3152 (IC base=+0.250)

- **PATRÓN** `ballena_activa_n` < `7.0` → IC=+0.254 (n=538)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 7.0 (IC base=+0.250)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.220 (n=669)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.154)

- **PATRÓN** `drift_60min` |x|≤ `0.1597` → IC=+0.182 (n=1330)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.1597 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.170 (n=2099)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 5.0 (IC base=+0.154)

- **PATRÓN** `ibs_20min` > `0.3313` → IC=+0.224 (n=1994)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3313 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` > `0.1371` → IC=+0.216 (n=1197)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1371 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.262` → IC=+0.224 (n=375)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.262 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` < `0.6923` → IC=+0.164 (n=878)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.6923 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` > `0.281` → IC=+0.190 (n=321)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.281 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` < `1.413` → IC=+0.173 (n=652)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.413 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` > `2.5021` → IC=+0.168 (n=651)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 2.5021 (IC base=+0.154)

- **PATRÓN** `ballena_activa_n` < `419.0` → IC=+0.159 (n=1916)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 419.0 (IC base=+0.154)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.170 (n=2073)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0058 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.2346` → IC=+0.172 (n=1823)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.2346 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.187 (n=996)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 15.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` < `0.6155` → IC=+0.206 (n=2071)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6155 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` < `0.1426` → IC=+0.171 (n=2106)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` < 0.1426 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.493` → IC=+0.189 (n=394)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 11.493 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.243` → IC=+0.145 (n=1799)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 4.243 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` < `1.2053` → IC=+0.160 (n=2071)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2053 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` < `0.0938` → IC=+0.148 (n=1761)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` < 0.0938 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `2.4999` → IC=+0.153 (n=1951)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.4999 (IC base=+0.145)

- **PATRÓN** `ballena_activa_n` < `201.0` → IC=+0.178 (n=628)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 201.0 (IC base=+0.145)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0121` → IC=+0.243 (n=744)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0121 (IC base=+0.215)

- **PATRÓN** `drift_60min` |x|≤ `0.3996` → IC=+0.226 (n=1962)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3996 (IC base=+0.215)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.237 (n=818)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.215)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.304 (n=1155)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.215)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.418` → IC=+0.303 (n=515)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.418 (IC base=+0.215)

- **PATRÓN** `volumen_pendiente_norm` < `0.0992` → IC=+0.215 (n=1913)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0992 (IC base=+0.215)

- **PATRÓN** `volumen_pendiente_norm` > `0.3532` → IC=+0.232 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3532 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` < `1.7667` → IC=+0.216 (n=951)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7667 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` > `2.7088` → IC=+0.229 (n=980)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7088 (IC base=+0.215)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.222 (n=2666)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.215)

- **PATRÓN** `libro_liquidez` > `1955.4984` → IC=+0.229 (n=1011)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1955.4984 (IC base=+0.215)

- **PATRÓN** `sigma_h` < `0.0087` → IC=+0.252 (n=1280)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0087 (IC base=+0.235)

- **PATRÓN** `drift_60min` |x|≤ `0.5685` → IC=+0.250 (n=1916)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5685 (IC base=+0.235)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.281 (n=735)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.235)

- **PATRÓN** `ibs_20min` < `0.0102` → IC=+0.302 (n=843)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0102 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.44` → IC=+0.273 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.44 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` > `0.3558` → IC=+0.279 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3558 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` < `1.7477` → IC=+0.238 (n=806)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7477 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` > `2.1531` → IC=+0.236 (n=1221)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1531 (IC base=+0.235)

- **PATRÓN** `libro_liquidez` > `2038.6572` → IC=+0.243 (n=639)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2038.6572 (IC base=+0.235)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.236 (n=1233)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.235)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.209 (n=944)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.0762` → IC=+0.199 (n=716)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0762 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.163 (n=2226)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` > `0.3116` → IC=+0.214 (n=2145)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3116 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.1451` → IC=+0.197 (n=1316)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.1451 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.712` → IC=+0.205 (n=374)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.712 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `1.0223` → IC=+0.158 (n=1887)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.0223 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.1034` → IC=+0.178 (n=882)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.1034 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `1.8235` → IC=+0.152 (n=1402)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 1.8235 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `2.5072` → IC=+0.167 (n=701)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 2.5072 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `4563.1044` → IC=+0.183 (n=1430)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 4563.1044 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `138.0` → IC=+0.158 (n=2082)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 138.0 (IC base=+0.150)

- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.156 (n=2236)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0072 (IC base=+0.128)

- **PATRÓN** `drift_60min` |x|≤ `0.395` → IC=+0.146 (n=2236)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.395 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.170 (n=1066)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 15.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` < `0.6837` → IC=+0.188 (n=2236)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.6837 (IC base=+0.128)

- **PATRÓN** `dist_vwap_pct` < `0.1544` → IC=+0.156 (n=2223)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1544 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.639` → IC=+0.161 (n=553)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 9.639 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` < `0.8556` → IC=+0.156 (n=1491)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.8556 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` > `0.3024` → IC=+0.194 (n=338)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.3024 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` < `1.8106` → IC=+0.136 (n=1398)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.8106 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` > `2.5645` → IC=+0.135 (n=699)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 2.5645 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `7403.6201` → IC=+0.191 (n=1014)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 7403.6201 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `67.0` → IC=+0.153 (n=904)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 67.0 (IC base=+0.128)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.179 (n=1088)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` > 0.0104 (IC base=+0.130)

- **PATRÓN** `drift_60min` |x|≤ `0.4413` → IC=+0.130 (n=2113)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.65€ cuando `drift_60min` |x|≤ 0.4413 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.173 (n=1151)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 15.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` > `0.4884` → IC=+0.218 (n=2400)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4884 (IC base=+0.130)

- **PATRÓN** `dist_vwap_pct` > `0.1966` → IC=+0.193 (n=1403)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.1966 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.516` → IC=+0.282 (n=513)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.516 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` < `1.1755` → IC=+0.145 (n=2401)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 1.1755 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` < `0.161` → IC=+0.136 (n=2433)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` < 0.161 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` < `1.4387` → IC=+0.152 (n=777)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 1.4387 (IC base=+0.130)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.132 (n=2514)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.02 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `2756.9384` → IC=+0.208 (n=1088)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2756.9384 (IC base=+0.130)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.161 (n=742)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 19.0 (IC base=+0.130)

- **PATRÓN** `sigma_h` < `0.0108` → IC=+0.140 (n=2450)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0108 (IC base=+0.121)

- **PATRÓN** `drift_60min` |x|≤ `0.1081` → IC=+0.172 (n=818)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.1081 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.141 (n=2497)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 5.0 (IC base=+0.121)

- **PATRÓN** `ibs_20min` < `0.6` → IC=+0.220 (n=2452)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6 (IC base=+0.121)

- **PATRÓN** `dist_vwap_pct` < `0.1985` → IC=+0.149 (n=2307)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.1985 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.385` → IC=+0.123 (n=492)

  - _Acción_: Kelly boost +0.62€ cuando `sigma_ewma_delta_pct` > 7.385 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.46` → IC=+0.132 (n=2165)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` < 2.46 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` < `1.1785` → IC=+0.130 (n=2449)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.1785 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` > `0.2754` → IC=+0.151 (n=328)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` > 0.2754 (IC base=+0.121)

- **PATRÓN** `volumen_spike_ratio` < `1.4461` → IC=+0.133 (n=763)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 1.4461 (IC base=+0.121)

- **PATRÓN** `volumen_spike_ratio` > `2.4249` → IC=+0.136 (n=762)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 2.4249 (IC base=+0.121)

- **PATRÓN** `libro_liquidez` > `2642.6157` → IC=+0.189 (n=1111)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 2642.6157 (IC base=+0.121)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.130 (n=1999)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 42.0 (IC base=+0.121)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0131` → IC=+0.245 (n=1982)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0131 (IC base=+0.223)

- **PATRÓN** `drift_60min` |x|≤ `0.1748` → IC=+0.241 (n=977)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1748 (IC base=+0.223)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.227 (n=2302)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.223)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.227 (n=1993)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.223)

- **PATRÓN** `ibs_20min` > `0.66` → IC=+0.258 (n=2221)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.66 (IC base=+0.223)

- **PATRÓN** `dist_vwap_pct` > `0.1849` → IC=+0.228 (n=1444)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1849 (IC base=+0.223)

- **PATRÓN** `dist_vwap_pct` < `0.8651` → IC=+0.225 (n=2281)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.8651 (IC base=+0.223)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.613` → IC=+0.250 (n=1007)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.613 (IC base=+0.223)

- **PATRÓN** `volumen_regimen` < `1.179` → IC=+0.225 (n=2218)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.179 (IC base=+0.223)

- **PATRÓN** `volumen_regimen` > `0.6184` → IC=+0.232 (n=2218)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6184 (IC base=+0.223)

- **PATRÓN** `volumen_pendiente_norm` > `0.283` → IC=+0.274 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.283 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` < `2.4697` → IC=+0.228 (n=2159)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4697 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` > `1.8082` → IC=+0.233 (n=1439)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8082 (IC base=+0.223)

- **PATRÓN** `libro_liquidez` > `2954.4444` → IC=+0.226 (n=740)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2954.4444 (IC base=+0.223)

- **PATRÓN** `sigma_h` < `0.0127` → IC=+0.234 (n=991)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0127 (IC base=+0.230)

- **PATRÓN** `sigma_h` > `0.0226` → IC=+0.240 (n=1021)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0226 (IC base=+0.230)

- **PATRÓN** `drift_60min` |x|≤ `0.0889` → IC=+0.264 (n=752)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0889 (IC base=+0.230)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.251 (n=1104)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.230)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.230 (n=1002)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.230)

- **PATRÓN** `ibs_20min` < `0.4279` → IC=+0.258 (n=2251)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4279 (IC base=+0.230)

- **PATRÓN** `dist_vwap_pct` > `0.2981` → IC=+0.241 (n=611)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2981 (IC base=+0.230)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.326` → IC=+0.262 (n=427)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.326 (IC base=+0.230)

- **PATRÓN** `volumen_regimen` > `0.6365` → IC=+0.237 (n=2250)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6365 (IC base=+0.230)

- **PATRÓN** `volumen_pendiente_norm` > `0.28` → IC=+0.286 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.28 (IC base=+0.230)

- **PATRÓN** `volumen_spike_ratio` > `1.4386` → IC=+0.233 (n=2095)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4386 (IC base=+0.230)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.209 (n=1492)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.183)

- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.192 (n=1129)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` > 0.0089 (IC base=+0.183)

- **PATRÓN** `drift_60min` |x|≤ `0.1298` → IC=+0.203 (n=1490)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1298 (IC base=+0.183)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.215 (n=1688)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.183)

- **PATRÓN** `ibs_20min` > `0.4896` → IC=+0.218 (n=3024)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4896 (IC base=+0.183)

- **PATRÓN** `dist_vwap_pct` > `0.8042` → IC=+0.204 (n=525)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8042 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.617` → IC=+0.213 (n=1464)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.617 (IC base=+0.183)

- **PATRÓN** `volumen_regimen` < `0.8627` → IC=+0.205 (n=2031)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8627 (IC base=+0.183)

- **PATRÓN** `volumen_regimen` > `0.6949` → IC=+0.186 (n=2722)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` > 0.6949 (IC base=+0.183)

- **PATRÓN** `volumen_pendiente_norm` > `0.0999` → IC=+0.193 (n=1215)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.0999 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` < `1.429` → IC=+0.197 (n=1097)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 1.429 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` > `2.4856` → IC=+0.187 (n=1097)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.4856 (IC base=+0.183)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.189 (n=3826)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.02 (IC base=+0.183)

- **PATRÓN** `libro_liquidez` > `2672.5659` → IC=+0.190 (n=3024)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 2672.5659 (IC base=+0.183)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.134 (n=1218)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` < 0.0038 (IC base=+0.088)

- **PATRÓN** `ibs_20min` < `0.3846` → IC=+0.161 (n=2437)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.3846 (IC base=+0.088)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.127 (n=1572)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 27.0 (IC base=+0.088)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.208 (n=412)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.181)

- **PATRÓN** `drift_60min` |x|≤ `0.3259` → IC=+0.203 (n=937)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3259 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.208 (n=854)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` > `0.6376` → IC=+0.238 (n=624)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6376 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` > `0.3084` → IC=+0.203 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3084 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.092` → IC=+0.197 (n=401)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 3.092 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.114` → IC=+0.181 (n=901)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` < 4.114 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `0.8745` → IC=+0.206 (n=625)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8745 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.0712` → IC=+0.185 (n=369)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.0712 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` < `2.1976` → IC=+0.189 (n=806)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` < 2.1976 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `1.4097` → IC=+0.182 (n=916)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 1.4097 (IC base=+0.181)

- **PATRÓN** `libro_liquidez` > `14680.2655` → IC=+0.184 (n=624)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 14680.2655 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `159.0` → IC=+0.210 (n=401)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 159.0 (IC base=+0.181)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.183 (n=374)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0029 (IC base=+0.112)

- **PATRÓN** `drift_60min` |x|≤ `0.2682` → IC=+0.137 (n=981)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.68€ cuando `drift_60min` |x|≤ 0.2682 (IC base=+0.112)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.126 (n=1010)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 7.0 (IC base=+0.112)

- **PATRÓN** `ibs_20min` < `0.6327` → IC=+0.162 (n=981)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` < 0.6327 (IC base=+0.112)

- **PATRÓN** `volumen_regimen` > `1.07` → IC=+0.141 (n=505)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 1.07 (IC base=+0.112)

- **PATRÓN** `volumen_pendiente_norm` > `0.1608` → IC=+0.161 (n=296)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.1608 (IC base=+0.112)

- **PATRÓN** `volumen_spike_ratio` < `2.121` → IC=+0.127 (n=969)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 2.121 (IC base=+0.112)

- **PATRÓN** `ballena_activa_n` < `221.0` → IC=+0.160 (n=722)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 221.0 (IC base=+0.112)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.248 (n=696)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=+0.212)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.213 (n=350)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.2091` → IC=+0.226 (n=696)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2091 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.228 (n=1095)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` > `0.3791` → IC=+0.254 (n=932)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3791 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` < `0.2147` → IC=+0.220 (n=920)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2147 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.85` → IC=+0.242 (n=420)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.85 (IC base=+0.212)

- **PATRÓN** `volumen_regimen` < `0.8358` → IC=+0.225 (n=696)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8358 (IC base=+0.212)

- **PATRÓN** `volumen_regimen` > `1.1643` → IC=+0.220 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1643 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` > `0.267` → IC=+0.255 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.267 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` < `1.4231` → IC=+0.234 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4231 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `1.776` → IC=+0.221 (n=687)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.776 (IC base=+0.212)

- **PATRÓN** `ibs_20min` < `0.1051` → IC=+0.166 (n=351)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.1051 (IC base=+0.066)

- **PATRÓN** `libro_liquidez` > `5845.3254` → IC=+0.134 (n=702)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 5845.3254 (IC base=+0.066)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0108` → IC=+0.198 (n=283)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0108 (IC base=+0.169)

- **PATRÓN** `drift_60min` |x|≤ `0.5286` → IC=+0.170 (n=849)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.5286 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.207 (n=606)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.169)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.274 (n=388)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.169)

- **PATRÓN** `dist_vwap_pct` > `0.9868` → IC=+0.245 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9868 (IC base=+0.169)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.081` → IC=+0.239 (n=355)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.081 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` < `1.0562` → IC=+0.184 (n=748)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 1.0562 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` > `0.7107` → IC=+0.178 (n=758)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` > 0.7107 (IC base=+0.169)

- **PATRÓN** `volumen_pendiente_norm` > `0.2314` → IC=+0.191 (n=160)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2314 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` < `1.4411` → IC=+0.191 (n=273)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` < 1.4411 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` > `2.1591` → IC=+0.170 (n=371)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 2.1591 (IC base=+0.169)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.178 (n=879)

  - _Acción_: Kelly boost +0.89€ cuando `libro_spread` < 0.02 (IC base=+0.169)

- **PATRÓN** `libro_liquidez` > `3018.4494` → IC=+0.188 (n=283)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 3018.4494 (IC base=+0.169)

- **PATRÓN** `ibs_20min` < `0.5484` → IC=+0.137 (n=810)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` < 0.5484 (IC base=+0.058)

- **PATRÓN** `libro_liquidez` > `2685.2006` → IC=+0.144 (n=417)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 2685.2006 (IC base=+0.058)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.136 (n=391)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 13.0 (IC base=+0.058)

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

- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.146 (n=227)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` > 0.0125 (IC base=+0.115)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.129 (n=227)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 7.0 (IC base=+0.115)

- **PATRÓN** `ibs_20min` < `0.614` → IC=+0.128 (n=253)

  - _Acción_: Kelly boost +0.64€ cuando `ibs_20min` < 0.614 (IC base=+0.115)

- **PATRÓN** `dist_vwap_pct` > `1.1964` → IC=+0.318 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1964 (IC base=+0.115)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.225` → IC=+0.176 (n=66)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 5.225 (IC base=+0.115)

- **PATRÓN** `volumen_regimen` < `0.9016` → IC=+0.134 (n=170)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 0.9016 (IC base=+0.115)

- **PATRÓN** `volumen_pendiente_norm` > `0.2396` → IC=+0.173 (n=47)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.2396 (IC base=+0.115)

- **PATRÓN** `volumen_spike_ratio` > `2.3609` → IC=+0.127 (n=108)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` > 2.3609 (IC base=+0.115)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.130 (n=233)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 19.0 (IC base=+0.115)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0115` → IC=+0.228 (n=5736)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0115 (IC base=+0.184)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.193 (n=17918)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 5.0 (IC base=+0.184)

- **PATRÓN** `ibs_20min` > `0.4476` → IC=+0.232 (n=17189)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4476 (IC base=+0.184)

- **PATRÓN** `dist_vwap_pct` > `0.9023` → IC=+0.213 (n=2158)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9023 (IC base=+0.184)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.242` → IC=+0.255 (n=4201)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.242 (IC base=+0.184)

- **PATRÓN** `volumen_regimen` < `1.2223` → IC=+0.170 (n=11527)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 1.2223 (IC base=+0.184)

- **PATRÓN** `volumen_pendiente_norm` > `0.2405` → IC=+0.207 (n=3114)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2405 (IC base=+0.184)

- **PATRÓN** `volumen_spike_ratio` > `2.6143` → IC=+0.197 (n=5574)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.6143 (IC base=+0.184)

- **PATRÓN** `libro_liquidez` > `1785.2789` → IC=+0.185 (n=17188)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 1785.2789 (IC base=+0.184)

- **PATRÓN** `ballena_activa_n` < `112.0` → IC=+0.205 (n=15833)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 112.0 (IC base=+0.184)

- **PATRÓN** `sigma_h` < `0.0074` → IC=+0.194 (n=10376)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0074 (IC base=+0.188)

- **PATRÓN** `drift_60min` |x|≤ `0.4902` → IC=+0.192 (n=15549)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.4902 (IC base=+0.188)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.212 (n=5813)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.188)

- **PATRÓN** `ibs_20min` < `0.5835` → IC=+0.243 (n=15549)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5835 (IC base=+0.188)

- **PATRÓN** `dist_vwap_pct` < `0.1769` → IC=+0.171 (n=9453)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` < 0.1769 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.811` → IC=+0.206 (n=2156)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.811 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.557` → IC=+0.191 (n=15047)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` < 3.557 (IC base=+0.188)

- **PATRÓN** `volumen_regimen` < `0.7044` → IC=+0.164 (n=4615)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.7044 (IC base=+0.188)

- **PATRÓN** `volumen_pendiente_norm` > `0.2905` → IC=+0.253 (n=2099)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2905 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` > `2.6156` → IC=+0.197 (n=4906)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 2.6156 (IC base=+0.188)

- **PATRÓN** `ballena_activa_n` < `39.0` → IC=+0.217 (n=9614)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 39.0 (IC base=+0.188)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.228 (n=937)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.226)

- **PATRÓN** `drift_60min` |x|≤ `0.3475` → IC=+0.230 (n=2803)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3475 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.239 (n=1367)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.226)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.228 (n=1881)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.226)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.329 (n=1114)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.427` → IC=+0.355 (n=655)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.427 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` > `0.2328` → IC=+0.285 (n=500)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2328 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` > `2.2926` → IC=+0.238 (n=1221)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2926 (IC base=+0.226)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.243 (n=3003)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.226)

- **PATRÓN** `libro_liquidez` > `2074.3377` → IC=+0.230 (n=935)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2074.3377 (IC base=+0.226)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.248 (n=1716)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 17.0 (IC base=+0.226)

- **PATRÓN** `sigma_h` < `0.0085` → IC=+0.266 (n=2384)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0085 (IC base=+0.262)

- **PATRÓN** `drift_60min` |x|≤ `0.1192` → IC=+0.286 (n=1048)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1192 (IC base=+0.262)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.268 (n=2187)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.262)

- **PATRÓN** `ibs_20min` < `0.5134` → IC=+0.288 (n=2382)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5134 (IC base=+0.262)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.122` → IC=+0.264 (n=468)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.122 (IC base=+0.262)

- **PATRÓN** `volumen_pendiente_norm` < `0.0953` → IC=+0.262 (n=2142)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0953 (IC base=+0.262)

- **PATRÓN** `volumen_pendiente_norm` > `0.2866` → IC=+0.291 (n=333)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2866 (IC base=+0.262)

- **PATRÓN** `volumen_spike_ratio` < `1.5578` → IC=+0.265 (n=994)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5578 (IC base=+0.262)

- **PATRÓN** `volumen_spike_ratio` > `2.6409` → IC=+0.271 (n=753)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6409 (IC base=+0.262)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.264 (n=2693)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.262)

- **PATRÓN** `libro_liquidez` > `1616.236` → IC=+0.271 (n=2128)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1616.236 (IC base=+0.262)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.271 (n=999)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.262)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.200 (n=937)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.1044` → IC=+0.166 (n=1227)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.1044 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.162 (n=2906)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` > `0.3656` → IC=+0.224 (n=2490)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3656 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` > `0.1276` → IC=+0.196 (n=1450)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.1276 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.511` → IC=+0.163 (n=458)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 11.511 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.159` → IC=+0.153 (n=2566)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 4.159 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` < `0.63` → IC=+0.175 (n=930)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.63 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` < `0.0723` → IC=+0.154 (n=2484)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` < 0.0723 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.2723` → IC=+0.182 (n=400)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.2723 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `2.1781` → IC=+0.159 (n=2400)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.1781 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` > `1.5284` → IC=+0.157 (n=2436)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.5284 (IC base=+0.151)

- **PATRÓN** `ballena_activa_n` < `239.0` → IC=+0.186 (n=895)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 239.0 (IC base=+0.151)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.164 (n=2322)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0058 (IC base=+0.143)

- **PATRÓN** `drift_60min` |x|≤ `0.2555` → IC=+0.164 (n=2043)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.2555 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.172 (n=873)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.143)

- **PATRÓN** `ibs_20min` < `0.6967` → IC=+0.198 (n=2322)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.6967 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` < `0.1394` → IC=+0.163 (n=2164)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.1394 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.232` → IC=+0.154 (n=383)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 11.232 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.461` → IC=+0.143 (n=2340)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 6.461 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` < `1.1954` → IC=+0.153 (n=2322)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 1.1954 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` > `0.2175` → IC=+0.199 (n=433)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2175 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` < `2.4301` → IC=+0.151 (n=2217)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.4301 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` > `1.7755` → IC=+0.153 (n=1478)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.7755 (IC base=+0.143)

- **PATRÓN** `ballena_activa_n` < `274.0` → IC=+0.160 (n=938)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 274.0 (IC base=+0.143)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0124` → IC=+0.259 (n=954)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0124 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.236 (n=2991)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.227)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.229 (n=2558)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.227)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.303 (n=1074)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.282` → IC=+0.327 (n=609)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.282 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` < `0.0974` → IC=+0.232 (n=2534)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0974 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` > `3.1781` → IC=+0.244 (n=927)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.1781 (IC base=+0.227)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.236 (n=3419)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.227)

- **PATRÓN** `libro_liquidez` > `1814.9584` → IC=+0.234 (n=1907)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1814.9584 (IC base=+0.227)

- **PATRÓN** `sigma_h` < `0.0118` → IC=+0.244 (n=2685)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0118 (IC base=+0.240)

- **PATRÓN** `drift_60min` |x|≤ `0.1798` → IC=+0.260 (n=1181)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1798 (IC base=+0.240)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.263 (n=1016)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.240)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.242 (n=950)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.240)

- **PATRÓN** `ibs_20min` < `0.0343` → IC=+0.307 (n=895)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0343 (IC base=+0.240)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.597` → IC=+0.298 (n=310)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.597 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` > `0.3447` → IC=+0.303 (n=399)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3447 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` > `2.1336` → IC=+0.250 (n=1704)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1336 (IC base=+0.240)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.245 (n=1415)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.240)

- **PATRÓN** `libro_liquidez` > `1946.888` → IC=+0.252 (n=1217)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1946.888 (IC base=+0.240)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.256 (n=1163)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.240)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.206 (n=987)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.4236` → IC=+0.159 (n=2957)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.4236 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.160 (n=3070)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 5.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` > `0.2458` → IC=+0.194 (n=2958)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 0.2458 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.143` → IC=+0.171 (n=1587)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.143 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.13` → IC=+0.161 (n=1200)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 4.13 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `0.8648` → IC=+0.166 (n=1972)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.8648 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.2814` → IC=+0.186 (n=387)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.2814 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `1.5243` → IC=+0.163 (n=1270)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 1.5243 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` > `2.1776` → IC=+0.155 (n=1308)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 2.1776 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `5896.858` → IC=+0.242 (n=1341)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5896.858 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `73.0` → IC=+0.169 (n=1250)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 73.0 (IC base=+0.146)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.152 (n=2452)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0075 (IC base=+0.130)

- **PATRÓN** `drift_60min` |x|≤ `0.4369` → IC=+0.141 (n=2449)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.4369 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.160 (n=897)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 17.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` < `0.7354` → IC=+0.186 (n=2449)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.7354 (IC base=+0.130)

- **PATRÓN** `dist_vwap_pct` < `0.1494` → IC=+0.146 (n=2216)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.1494 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.115` → IC=+0.171 (n=375)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 11.115 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` < `0.6969` → IC=+0.144 (n=1078)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.6969 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` > `0.2964` → IC=+0.222 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2964 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` > `1.4309` → IC=+0.137 (n=2355)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 1.4309 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `7095.984` → IC=+0.211 (n=816)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7095.984 (IC base=+0.130)

- **PATRÓN** `ballena_activa_n` < `130.0` → IC=+0.132 (n=2092)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 130.0 (IC base=+0.130)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0103` → IC=+0.163 (n=1349)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` > 0.0103 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.178 (n=1101)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 17.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` > `0.4426` → IC=+0.200 (n=2975)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4426 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` > `1.0559` → IC=+0.209 (n=523)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0559 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.364` → IC=+0.248 (n=1102)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.364 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `1.2216` → IC=+0.136 (n=2975)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 1.2216 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` < `0.1618` → IC=+0.126 (n=3094)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` < 0.1618 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` > `0.2781` → IC=+0.131 (n=385)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` > 0.2781 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `1.5716` → IC=+0.132 (n=1279)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 1.5716 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` > `2.1901` → IC=+0.127 (n=1318)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` > 2.1901 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.131 (n=3095)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.02 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `2485.976` → IC=+0.231 (n=1349)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2485.976 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.142 (n=950)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 24.0 (IC base=+0.126)

- **PATRÓN** `sigma_h` < `0.01` → IC=+0.152 (n=2474)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.01 (IC base=+0.116)

- **PATRÓN** `drift_60min` |x|≤ `0.1341` → IC=+0.153 (n=937)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.1341 (IC base=+0.116)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.129 (n=2900)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 5.0 (IC base=+0.116)

- **PATRÓN** `ibs_20min` < `0.6495` → IC=+0.212 (n=2811)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6495 (IC base=+0.116)

- **PATRÓN** `dist_vwap_pct` < `0.2138` → IC=+0.135 (n=2424)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.2138 (IC base=+0.116)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.241` → IC=+0.134 (n=2707)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` < 3.241 (IC base=+0.116)

- **PATRÓN** `volumen_regimen` < `0.7102` → IC=+0.138 (n=1237)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 0.7102 (IC base=+0.116)

- **PATRÓN** `volumen_pendiente_norm` > `0.2243` → IC=+0.174 (n=477)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.2243 (IC base=+0.116)

- **PATRÓN** `volumen_spike_ratio` < `1.4386` → IC=+0.150 (n=878)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.4386 (IC base=+0.116)

- **PATRÓN** `libro_liquidez` > `2664.6803` → IC=+0.205 (n=937)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2664.6803 (IC base=+0.116)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.131 (n=2328)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 47.0 (IC base=+0.116)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0138` → IC=+0.253 (n=2510)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0138 (IC base=+0.232)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.238 (n=2933)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.232)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.236 (n=2026)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.232)

- **PATRÓN** `ibs_20min` > `0.6111` → IC=+0.272 (n=2509)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6111 (IC base=+0.232)

- **PATRÓN** `dist_vwap_pct` > `0.1912` → IC=+0.249 (n=1542)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1912 (IC base=+0.232)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.726` → IC=+0.273 (n=941)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.726 (IC base=+0.232)

- **PATRÓN** `volumen_regimen` < `1.2311` → IC=+0.239 (n=2808)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2311 (IC base=+0.232)

- **PATRÓN** `volumen_regimen` > `0.6389` → IC=+0.236 (n=2808)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6389 (IC base=+0.232)

- **PATRÓN** `volumen_pendiente_norm` > `0.2872` → IC=+0.262 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2872 (IC base=+0.232)

- **PATRÓN** `volumen_spike_ratio` > `2.4972` → IC=+0.252 (n=912)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4972 (IC base=+0.232)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.234 (n=3648)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.232)

- **PATRÓN** `libro_liquidez` > `2955.9488` → IC=+0.239 (n=936)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2955.9488 (IC base=+0.232)

- **PATRÓN** `sigma_h` > `0.0255` → IC=+0.253 (n=968)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0255 (IC base=+0.231)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.238 (n=2738)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.231)

- **PATRÓN** `ibs_20min` < `0.5152` → IC=+0.266 (n=2905)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5152 (IC base=+0.231)

- **PATRÓN** `dist_vwap_pct` < `0.2923` → IC=+0.235 (n=2790)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2923 (IC base=+0.231)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.209` → IC=+0.267 (n=560)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.209 (IC base=+0.231)

- **PATRÓN** `volumen_regimen` > `1.2292` → IC=+0.260 (n=969)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2292 (IC base=+0.231)

- **PATRÓN** `volumen_pendiente_norm` > `0.2821` → IC=+0.300 (n=383)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2821 (IC base=+0.231)

- **PATRÓN** `volumen_spike_ratio` > `1.4324` → IC=+0.234 (n=2701)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4324 (IC base=+0.231)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.194 (n=5039)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.245 (n=1736)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.211)

- **PATRÓN** `drift_60min` |x|≤ `0.5113` → IC=+0.221 (n=5204)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5113 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.227 (n=1891)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` > `0.9412` → IC=+0.251 (n=1737)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9412 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` > `0.1722` → IC=+0.213 (n=1954)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1722 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` < `0.4352` → IC=+0.214 (n=3711)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4352 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.975` → IC=+0.221 (n=853)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.975 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.585` → IC=+0.212 (n=4632)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.585 (IC base=+0.211)

- **PATRÓN** `volumen_regimen` < `0.706` → IC=+0.223 (n=1664)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.706 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` < `0.1071` → IC=+0.211 (n=4866)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1071 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.1669` → IC=+0.223 (n=1462)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1669 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` < `1.4557` → IC=+0.219 (n=1707)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4557 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `1.8475` → IC=+0.212 (n=3413)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8475 (IC base=+0.211)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.216 (n=3994)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `3738.4996` → IC=+0.220 (n=3468)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3738.4996 (IC base=+0.211)

- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.239 (n=1265)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.193)

- **PATRÓN** `drift_60min` |x|≤ `0.49` → IC=+0.208 (n=3791)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.49 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.214 (n=1277)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.209 (n=1687)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.193)

- **PATRÓN** `ibs_20min` < `0.7337` → IC=+0.199 (n=3791)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7337 (IC base=+0.193)

- **PATRÓN** `dist_vwap_pct` > `0.6725` → IC=+0.202 (n=663)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6725 (IC base=+0.193)

- **PATRÓN** `dist_vwap_pct` < `0.4234` → IC=+0.191 (n=3811)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` < 0.4234 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.812` → IC=+0.203 (n=3402)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.812 (IC base=+0.193)

- **PATRÓN** `volumen_regimen` < `1.0954` → IC=+0.202 (n=3165)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0954 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` < `0.0978` → IC=+0.198 (n=3482)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` < 0.0978 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` > `0.2228` → IC=+0.194 (n=763)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2228 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` < `1.5338` → IC=+0.200 (n=1645)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5338 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` > `2.1925` → IC=+0.201 (n=1693)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1925 (IC base=+0.193)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.194 (n=5039)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.01 (IC base=+0.193)

- **PATRÓN** `ballena_activa_n` < `169.0` → IC=+0.203 (n=3280)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 169.0 (IC base=+0.193)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.275 (n=672)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.260)

- **PATRÓN** `sigma_h` > `0.0034` → IC=+0.260 (n=684)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0034 (IC base=+0.260)

- **PATRÓN** `drift_60min` |x|≤ `0.0853` → IC=+0.294 (n=255)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0853 (IC base=+0.260)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.271 (n=400)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.260)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.260 (n=766)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.260)

- **PATRÓN** `ibs_20min` < `0.4896` → IC=+0.279 (n=510)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4896 (IC base=+0.260)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.054` → IC=+0.274 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.054 (IC base=+0.260)

- **PATRÓN** `volumen_regimen` < `1.2151` → IC=+0.268 (n=764)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2151 (IC base=+0.260)

- **PATRÓN** `volumen_regimen` > `0.8685` → IC=+0.273 (n=509)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8685 (IC base=+0.260)

- **PATRÓN** `volumen_pendiente_norm` > `0.2881` → IC=+0.350 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2881 (IC base=+0.260)

- **PATRÓN** `volumen_spike_ratio` < `1.8249` → IC=+0.267 (n=508)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8249 (IC base=+0.260)

- **PATRÓN** `libro_liquidez` > `16321.2566` → IC=+0.274 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16321.2566 (IC base=+0.260)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.252 (n=583)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.176)

- **PATRÓN** `drift_60min` |x|≤ `0.3685` → IC=+0.192 (n=1324)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.3685 (IC base=+0.176)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.223 (n=482)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.196 (n=485)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 5.0 (IC base=+0.176)

- **PATRÓN** `ibs_20min` < `0.1382` → IC=+0.206 (n=583)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1382 (IC base=+0.176)

- **PATRÓN** `ibs_20min` > `0.6081` → IC=+0.177 (n=601)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` > 0.6081 (IC base=+0.176)

- **PATRÓN** `dist_vwap_pct` > `0.7021` → IC=+0.181 (n=117)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.7021 (IC base=+0.176)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.38` → IC=+0.195 (n=1307)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` < 6.38 (IC base=+0.176)

- **PATRÓN** `volumen_regimen` < `1.2185` → IC=+0.190 (n=1324)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` < 1.2185 (IC base=+0.176)

- **PATRÓN** `volumen_pendiente_norm` > `0.2192` → IC=+0.199 (n=267)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2192 (IC base=+0.176)

- **PATRÓN** `volumen_spike_ratio` < `1.4032` → IC=+0.194 (n=439)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 1.4032 (IC base=+0.176)

- **PATRÓN** `volumen_spike_ratio` > `2.166` → IC=+0.188 (n=597)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.166 (IC base=+0.176)

- **PATRÓN** `libro_liquidez` > `14902.9256` → IC=+0.188 (n=601)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 14902.9256 (IC base=+0.176)

- **PATRÓN** `ballena_activa_n` < `694.0` → IC=+0.189 (n=1280)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 694.0 (IC base=+0.176)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` < `0.007` → IC=+0.196 (n=363)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.007 (IC base=+0.193)

- **PATRÓN** `sigma_h` > `0.0105` → IC=+0.215 (n=373)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0105 (IC base=+0.193)

- **PATRÓN** `drift_60min` |x|≤ `0.587` → IC=+0.204 (n=820)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.587 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.245 (n=296)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.193)

- **PATRÓN** `ibs_20min` < `0.7037` → IC=+0.196 (n=547)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.7037 (IC base=+0.193)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.239 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.492` → IC=+0.234 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.492 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` > `0.2099` → IC=+0.238 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2099 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` > `2.8704` → IC=+0.205 (n=371)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8704 (IC base=+0.193)

- **PATRÓN** `libro_liquidez` > `2543.292` → IC=+0.219 (n=372)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2543.292 (IC base=+0.193)

- **PATRÓN** `ballena_activa_n` < `10.0` → IC=+0.197 (n=553)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 10.0 (IC base=+0.193)

- **PATRÓN** `sigma_h` < `0.011` → IC=+0.229 (n=57)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.011 (IC base=+0.227)

- **PATRÓN** `sigma_h` > `0.0086` → IC=+0.275 (n=38)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0086 (IC base=+0.227)

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
- **PATRÓN** `sigma_h` < `0.008` → IC=+0.214 (n=1381)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.008 (IC base=+0.198)

- **PATRÓN** `drift_60min` |x|≤ `0.4596` → IC=+0.206 (n=1381)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4596 (IC base=+0.198)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.216 (n=502)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.198)

- **PATRÓN** `ibs_20min` < `0.5194` → IC=+0.210 (n=921)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5194 (IC base=+0.198)

- **PATRÓN** `ibs_20min` > `0.7607` → IC=+0.199 (n=626)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7607 (IC base=+0.198)

- **PATRÓN** `dist_vwap_pct` < `0.4078` → IC=+0.211 (n=1377)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4078 (IC base=+0.198)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.112` → IC=+0.206 (n=1241)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.112 (IC base=+0.198)

- **PATRÓN** `volumen_regimen` < `0.8782` → IC=+0.201 (n=921)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8782 (IC base=+0.198)

- **PATRÓN** `volumen_regimen` > `1.2314` → IC=+0.204 (n=461)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2314 (IC base=+0.198)

- **PATRÓN** `volumen_pendiente_norm` < `0.105` → IC=+0.201 (n=1270)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.105 (IC base=+0.198)

- **PATRÓN** `volumen_spike_ratio` < `2.4495` → IC=+0.206 (n=1351)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4495 (IC base=+0.198)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.199 (n=1416)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.01 (IC base=+0.198)

- **PATRÓN** `sigma_h` < `0.008` → IC=+0.205 (n=1130)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.008 (IC base=+0.187)

- **PATRÓN** `drift_60min` |x|≤ `0.4924` → IC=+0.211 (n=1129)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4924 (IC base=+0.187)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.202 (n=441)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.187)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.198 (n=755)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 10.0 (IC base=+0.187)

- **PATRÓN** `ibs_20min` < `0.3984` → IC=+0.194 (n=753)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.3984 (IC base=+0.187)

- **PATRÓN** `ibs_20min` > `0.0867` → IC=+0.190 (n=1129)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.0867 (IC base=+0.187)

- **PATRÓN** `dist_vwap_pct` > `0.6705` → IC=+0.197 (n=199)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.6705 (IC base=+0.187)

- **PATRÓN** `dist_vwap_pct` < `0.2251` → IC=+0.189 (n=1090)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` < 0.2251 (IC base=+0.187)

- **PATRÓN** `volumen_regimen` < `1.2445` → IC=+0.199 (n=1129)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_regimen` < 1.2445 (IC base=+0.187)

- **PATRÓN** `volumen_regimen` > `0.721` → IC=+0.187 (n=1009)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` > 0.721 (IC base=+0.187)

- **PATRÓN** `volumen_pendiente_norm` > `0.0742` → IC=+0.208 (n=474)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0742 (IC base=+0.187)

- **PATRÓN** `volumen_spike_ratio` < `2.1925` → IC=+0.196 (n=973)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 2.1925 (IC base=+0.187)

- **PATRÓN** `volumen_spike_ratio` > `2.5255` → IC=+0.190 (n=369)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 2.5255 (IC base=+0.187)

- **PATRÓN** `libro_liquidez` > `6738.937` → IC=+0.197 (n=1129)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 6738.937 (IC base=+0.187)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.011` → IC=+0.204 (n=678)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.011 (IC base=+0.185)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.210 (n=737)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.185)

- **PATRÓN** `ibs_20min` > `0.9259` → IC=+0.250 (n=350)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9259 (IC base=+0.185)

- **PATRÓN** `dist_vwap_pct` > `0.7421` → IC=+0.240 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7421 (IC base=+0.185)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.218` → IC=+0.206 (n=413)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.218 (IC base=+0.185)

- **PATRÓN** `volumen_regimen` < `0.6991` → IC=+0.230 (n=339)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6991 (IC base=+0.185)

- **PATRÓN** `volumen_pendiente_norm` < `0.1062` → IC=+0.196 (n=695)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` < 0.1062 (IC base=+0.185)

- **PATRÓN** `volumen_pendiente_norm` > `0.0788` → IC=+0.195 (n=342)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.0788 (IC base=+0.185)

- **PATRÓN** `volumen_spike_ratio` < `1.5649` → IC=+0.195 (n=329)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 1.5649 (IC base=+0.185)

- **PATRÓN** `volumen_spike_ratio` > `2.4746` → IC=+0.213 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4746 (IC base=+0.185)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.189 (n=899)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.02 (IC base=+0.185)

- **PATRÓN** `libro_liquidez` > `2931.085` → IC=+0.200 (n=771)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2931.085 (IC base=+0.185)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.200 (n=758)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 52.0 (IC base=+0.185)

- **PATRÓN** `sigma_h` < `0.0094` → IC=+0.215 (n=380)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0094 (IC base=+0.207)

- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.208 (n=190)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0125 (IC base=+0.207)

- **PATRÓN** `drift_60min` |x|≤ `0.6042` → IC=+0.227 (n=570)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6042 (IC base=+0.207)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.242 (n=386)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 9.0 (IC base=+0.207)

- **PATRÓN** `ibs_20min` < `0.7273` → IC=+0.229 (n=570)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7273 (IC base=+0.207)

- **PATRÓN** `dist_vwap_pct` > `0.8337` → IC=+0.212 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8337 (IC base=+0.207)

- **PATRÓN** `dist_vwap_pct` < `0.3056` → IC=+0.209 (n=476)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3056 (IC base=+0.207)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.848` → IC=+0.214 (n=516)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.848 (IC base=+0.207)

- **PATRÓN** `volumen_regimen` < `1.1312` → IC=+0.212 (n=501)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1312 (IC base=+0.207)

- **PATRÓN** `volumen_regimen` > `0.9331` → IC=+0.209 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.9331 (IC base=+0.207)

- **PATRÓN** `volumen_pendiente_norm` < `0.1071` → IC=+0.228 (n=495)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1071 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` > `2.2075` → IC=+0.239 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2075 (IC base=+0.207)

- **PATRÓN** `libro_liquidez` > `3019.8404` → IC=+0.224 (n=570)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3019.8404 (IC base=+0.207)

- **PATRÓN** `ballena_activa_n` < `29.0` → IC=+0.251 (n=379)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 29.0 (IC base=+0.207)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.160 (n=756)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.004 (IC base=+0.072)

- **PATRÓN** `ibs_20min` > `0.3924` → IC=+0.144 (n=1624)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` > 0.3924 (IC base=+0.072)

- **PATRÓN** `dist_vwap_pct` > `0.1487` → IC=+0.146 (n=857)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` > 0.1487 (IC base=+0.072)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.91` → IC=+0.156 (n=472)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 8.91 (IC base=+0.072)

- **PATRÓN** `volumen_pendiente_norm` > `0.2748` → IC=+0.148 (n=225)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.2748 (IC base=+0.072)

- **PATRÓN** `ibs_20min` < `0.0263` → IC=+0.266 (n=400)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0263 (IC base=+0.053)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.316` → IC=+0.164 (n=144)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 10.316 (IC base=+0.053)

- **PATRÓN** `volumen_pendiente_norm` > `0.1457` → IC=+0.154 (n=255)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` > 0.1457 (IC base=+0.053)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.135 (n=568)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` < 0.0056 (IC base=+0.093)

- **PATRÓN** `ibs_20min` > `0.3574` → IC=+0.172 (n=537)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` > 0.3574 (IC base=+0.093)

- **PATRÓN** `dist_vwap_pct` > `0.2913` → IC=+0.179 (n=188)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.2913 (IC base=+0.093)

- **PATRÓN** `sigma_h` < `0.003` → IC=+0.128 (n=189)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.64€ cuando `sigma_h` < 0.003 (IC base=+0.066)

- **PATRÓN** `ibs_20min` < `0.0653` → IC=+0.278 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0653 (IC base=+0.066)

- **PATRÓN** `volumen_pendiente_norm` > `0.2123` → IC=+0.183 (n=77)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.2123 (IC base=+0.066)

### GBM_LATE_60M#ETH#60min
- **PATRÓN** `sigma_h` < `0.006` → IC=+0.126 (n=493)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.63€ cuando `sigma_h` < 0.006 (IC base=+0.091)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.146 (n=213)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 17.0 (IC base=+0.091)

- **PATRÓN** `ibs_20min` > `0.4223` → IC=+0.172 (n=529)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` > 0.4223 (IC base=+0.091)

- **PATRÓN** `dist_vwap_pct` > `0.1247` → IC=+0.190 (n=275)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.1247 (IC base=+0.091)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.194` → IC=+0.237 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.194 (IC base=+0.091)

- **PATRÓN** `volumen_pendiente_norm` > `0.2854` → IC=+0.162 (n=75)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.2854 (IC base=+0.091)

- **PATRÓN** `ibs_20min` < `0.1105` → IC=+0.256 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1105 (IC base=+0.020)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.686` → IC=+0.235 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.686 (IC base=+0.020)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `ibs_20min` > `0.1786` → IC=-0.194 (n=70)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1786
  - _Potencial_: sin este filtro IC_bueno=+0.213 (n=214)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.168 (n=372)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` > 0.75 (IC base=+0.034)

- **PATRÓN** `dist_vwap_pct` > `0.4722` → IC=+0.134 (n=200)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` > 0.4722 (IC base=+0.034)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.265` → IC=+0.158 (n=118)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 9.265 (IC base=+0.034)

- **PATRÓN** `volumen_pendiente_norm` > `0.2775` → IC=+0.142 (n=79)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` > 0.2775 (IC base=+0.034)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.154 (n=244)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0103 (IC base=+0.072)

- **PATRÓN** `ibs_20min` < `0.1786` → IC=+0.213 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1786 (IC base=+0.072)

- **PATRÓN** `dist_vwap_pct` < `0.1685` → IC=+0.139 (n=200)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.1685 (IC base=+0.072)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.474` → IC=+0.312 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.474 (IC base=+0.072)

- **PATRÓN** `volumen_regimen` > `1.0779` → IC=+0.199 (n=71)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_regimen` > 1.0779 (IC base=+0.072)

- **PATRÓN** `volumen_pendiente_norm` > `0.1486` → IC=+0.216 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1486 (IC base=+0.072)

- **PATRÓN** `volumen_spike_ratio` < `2.18` → IC=+0.147 (n=168)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 2.18 (IC base=+0.072)

- **PATRÓN** `volumen_spike_ratio` > `1.4069` → IC=+0.158 (n=191)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.4069 (IC base=+0.072)

### GBM_LATE_60M_FADE
- **FILTRO** `hora_utc` > `8.0` → IC=-0.324 (n=66)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.165 (n=249)

- **FILTRO** `dist_vwap_pct` > `0.2316` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2316
  - _Potencial_: sin este filtro IC_bueno=-0.190 (n=298)

- **FILTRO** `volumen_spike_ratio` > `2.8031` → IC=-0.210 (n=60)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.8031
  - _Potencial_: sin este filtro IC_bueno=-0.145 (n=181)

- **FILTRO** `libro_liquidez` < `891.5381` → IC=-0.225 (n=78)

  - _Acción_: SKIP cuando `libro_liquidez` < 891.5381
  - _Potencial_: sin este filtro IC_bueno=-0.190 (n=237)

- **FILTRO** `drift_60min` |x|> `0.1941` → IC=-0.321 (n=65)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1941
  - _Potencial_: sin este filtro IC_bueno=-0.270 (n=198)

- **FILTRO** `ibs_20min` > `0.5429` → IC=-0.331 (n=134)

  - _Acción_: SKIP cuando `ibs_20min` > 0.5429
  - _Potencial_: sin este filtro IC_bueno=-0.244 (n=135)

- **FILTRO** `dist_vwap_pct` > `0.4497` → IC=-0.405 (n=19)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4497
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=250)

- **FILTRO** `sigma_ewma_delta_pct` > `10.342` → IC=-0.321 (n=26)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 10.342
  - _Potencial_: sin este filtro IC_bueno=-0.284 (n=243)

- **FILTRO** `volumen_pendiente_norm` > `0.0448` → IC=-0.379 (n=31)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0448
  - _Potencial_: sin este filtro IC_bueno=-0.273 (n=152)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `volumen_regimen` < `1.2175` → IC=-0.284 (n=49)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.2175
  - _Potencial_: sin este filtro IC_bueno=-0.147 (n=49)

- **FILTRO** `sigma_h` > `0.0043` → IC=-0.339 (n=29)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0043
  - _Potencial_: sin este filtro IC_bueno=-0.231 (n=91)

- **FILTRO** `volumen_regimen` > `0.8276` → IC=-0.371 (n=29)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8276
  - _Potencial_: sin este filtro IC_bueno=-0.220 (n=91)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `hora_utc` > `9.0` → IC=-0.315 (n=25)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.098 (n=80)

- **FILTRO** `volumen_regimen` < `0.7407` → IC=-0.286 (n=26)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7407
  - _Potencial_: sin este filtro IC_bueno=-0.105 (n=79)

- **FILTRO** `sigma_h` > `0.0048` → IC=-0.352 (n=25)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0048
  - _Potencial_: sin este filtro IC_bueno=-0.272 (n=77)

- **FILTRO** `hora_utc` < `6.0` → IC=-0.375 (n=22)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.268 (n=80)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.286 (n=87)

- **FILTRO** `libro_liquidez` < `1599.2889` → IC=-0.311 (n=51)

  - _Acción_: SKIP cuando `libro_liquidez` < 1599.2889
  - _Potencial_: sin este filtro IC_bueno=-0.274 (n=51)

- **PATRÓN** `ibs_20min` > `0.941` → IC=+0.158 (n=36)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` > 0.941 (IC base=-0.154)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `drift_60min` |x|> `0.2367` → IC=-0.397 (n=27)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2367
  - _Potencial_: sin este filtro IC_bueno=-0.151 (n=84)

- **FILTRO** `volumen_regimen` < `0.7468` → IC=-0.333 (n=28)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7468
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=84)

- **FILTRO** `volumen_spike_ratio` > `2.3736` → IC=-0.242 (n=29)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.3736
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=58)

- **FILTRO** `libro_spread` > `0.06` → IC=-0.242 (n=29)

  - _Acción_: SKIP cuando `libro_spread` > 0.06
  - _Potencial_: sin este filtro IC_bueno=-0.206 (n=83)

- **FILTRO** `sigma_h` < `0.006` → IC=-0.324 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.006
  - _Potencial_: sin este filtro IC_bueno=-0.294 (n=32)

- **FILTRO** `hora_utc` > `11.0` → IC=-0.441 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.235 (n=32)

- **FILTRO** `volumen_regimen` < `0.9949` → IC=-0.420 (n=23)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9949
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=24)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` > `0.1524` → IC=-0.121 (n=286)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1524
  - _Potencial_: sin este filtro IC_bueno=+0.142 (n=556)

- **PATRÓN** `sigma_h` > `0.0061` → IC=+0.202 (n=246)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0061 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.192 (n=212)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 17.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` > `0.6871` → IC=+0.159 (n=543)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` > 0.6871 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` > `0.5394` → IC=+0.238 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5394 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.695` → IC=+0.129 (n=300)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` > 3.695 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` < `0.6187` → IC=+0.189 (n=181)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 0.6187 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` < `0.1532` → IC=+0.158 (n=448)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` < 0.1532 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` < `1.7943` → IC=+0.169 (n=294)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 1.7943 (IC base=+0.123)

- **PATRÓN** `ibs_20min` < `0.1524` → IC=+0.142 (n=556)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` < 0.1524 (IC base=+0.052)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.108` → IC=+0.180 (n=145)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 11.108 (IC base=+0.052)

- **PATRÓN** `libro_liquidez` > `3284.2124` → IC=+0.131 (n=421)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 3284.2124 (IC base=+0.052)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.6946` → IC=-0.190 (n=56)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6946
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=169)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.183 (n=99)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` > 0.0049 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.139 (n=203)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 12.0 (IC base=+0.130)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.149 (n=112)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 6.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` < `0.1681` → IC=+0.192 (n=297)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.1681 (IC base=+0.130)

- **PATRÓN** `dist_vwap_pct` < `0.2503` → IC=+0.148 (n=339)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.2503 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.176` → IC=+0.167 (n=94)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 10.176 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` > `0.6182` → IC=+0.145 (n=297)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 0.6182 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` < `0.0743` → IC=+0.140 (n=234)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_pendiente_norm` < 0.0743 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` > `0.2726` → IC=+0.173 (n=50)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.2726 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` < `2.5144` → IC=+0.163 (n=265)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 2.5144 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` > `1.5218` → IC=+0.148 (n=237)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.5218 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `5390.0556` → IC=+0.135 (n=198)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 5390.0556 (IC base=+0.130)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `volumen_pendiente_norm` > `0.1263` → IC=-0.149 (n=35)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1263
  - _Potencial_: sin este filtro IC_bueno=+0.152 (n=179)

- **FILTRO** `ibs_20min` > `0.327` → IC=-0.167 (n=76)

  - _Acción_: SKIP cuando `ibs_20min` > 0.327
  - _Potencial_: sin este filtro IC_bueno=+0.079 (n=231)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.123 (n=189)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0061 (IC base=+0.105)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.196 (n=67)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 18.0 (IC base=+0.105)

- **PATRÓN** `ibs_20min` > `0.9094` → IC=+0.164 (n=126)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` > 0.9094 (IC base=+0.105)

- **PATRÓN** `dist_vwap_pct` < `0.0908` → IC=+0.138 (n=158)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.0908 (IC base=+0.105)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.015` → IC=+0.150 (n=141)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 3.015 (IC base=+0.105)

- **PATRÓN** `volumen_regimen` < `0.6141` → IC=+0.192 (n=63)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 0.6141 (IC base=+0.105)

- **PATRÓN** `volumen_pendiente_norm` < `0.1263` → IC=+0.152 (n=179)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` < 0.1263 (IC base=+0.105)

- **PATRÓN** `volumen_spike_ratio` < `1.7963` → IC=+0.182 (n=108)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 1.7963 (IC base=+0.105)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.121 (n=159)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.01 (IC base=+0.105)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.957` → IC=+0.232 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.957 (IC base=+0.018)

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

- **PATRÓN** `hora_utc` > `13.0` → IC=+0.319 (n=125)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 13.0 (IC base=+0.259)

- **PATRÓN** `ibs_20min` > `0.6522` → IC=+0.282 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6522 (IC base=+0.259)

- **PATRÓN** `dist_vwap_pct` > `0.6843` → IC=+0.394 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6843 (IC base=+0.259)

- **PATRÓN** `dist_vwap_pct` < `0.2335` → IC=+0.262 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2335 (IC base=+0.259)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.331` → IC=+0.320 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.331 (IC base=+0.259)

- **PATRÓN** `volumen_regimen` < `0.5724` → IC=+0.328 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.5724 (IC base=+0.259)

- **PATRÓN** `volumen_pendiente_norm` > `0.1048` → IC=+0.341 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1048 (IC base=+0.259)

- **PATRÓN** `volumen_spike_ratio` < `1.4833` → IC=+0.402 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4833 (IC base=+0.259)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.264 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.259)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.321` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.321 (IC base=-0.091)

### LATE_WINDOW_5MIN
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.331 (n=69)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3447` → IC=+0.325 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3447 (IC base=+0.319)

- **PATRÓN** `elapsed_s` > `184.3` → IC=+0.389 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 184.3 (IC base=+0.319)

- **PATRÓN** `drift_15min` |x|≤ `1.0295` → IC=+0.457 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0295 (IC base=+0.319)

- **PATRÓN** `drift_60min` |x|≤ `0.9647` → IC=+0.389 (n=61)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9647 (IC base=+0.319)

- **PATRÓN** `ballena_activa_n` < `1114.0` → IC=+0.370 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1114.0 (IC base=+0.319)

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

- **PATRÓN** `drift_ventana_pct` |x|> `0.3447` → IC=+0.325 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3447 (IC base=+0.319)

- **PATRÓN** `elapsed_s` > `184.3` → IC=+0.389 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 184.3 (IC base=+0.319)

- **PATRÓN** `drift_15min` |x|≤ `1.0295` → IC=+0.457 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0295 (IC base=+0.319)

- **PATRÓN** `drift_60min` |x|≤ `0.9647` → IC=+0.389 (n=61)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9647 (IC base=+0.319)

- **PATRÓN** `ballena_activa_n` < `1114.0` → IC=+0.370 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1114.0 (IC base=+0.319)

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
- **PATRÓN** `libro_liquidez` > `2944.9354` → IC=+0.137 (n=425)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 2944.9354 (IC base=+0.103)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `libro_liquidez` > `2944.9354` → IC=+0.137 (n=425)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 2944.9354 (IC base=+0.103)

### LIQUIDACIONES_15M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=196)

- **FILTRO** `libro_liquidez` < `5350.5492` → IC=-0.167 (n=106)

  - _Acción_: SKIP cuando `libro_liquidez` < 5350.5492
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=106)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=324)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `libro_liquidez` < `10893.2451` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `libro_liquidez` < 10893.2451
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=71)

- **FILTRO** `py_entrada` < `0.515` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.105 (n=41)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `ballena_activa_n` > `63.0` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `ballena_activa_n` > 63.0
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=9)

### LIQUIDACIONES_15M#XRP#15min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.309 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### LIQUIDACIONES_5M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.121 (n=85)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=3565)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.160 (n=104)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.160 (n=104)

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
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=1330)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=1284)

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
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=709)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=717)

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
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=422)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=403)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.145 (n=181)

  - _Acción_: Kelly boost +0.72€ cuando `py_entrada` < 0.495 (IC base=+0.025)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=845)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=845)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=850)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=850)

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

- **FILTRO** `py_entrada` < `0.445` → IC=-0.124 (n=91)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=145)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.183 (n=39)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=244)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=268)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=259)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=350)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=350)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.120 (n=185)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=195)

- **FILTRO** `libro_liquidez` < `625.8426` → IC=-0.138 (n=125)

  - _Acción_: SKIP cuando `libro_liquidez` < 625.8426
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=255)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=261)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.129 (n=87)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=189)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `py_entrada` < `0.48` → IC=-0.131 (n=63)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.129 (n=33)

- **FILTRO** `hora_utc` < `15.0` → IC=-0.204 (n=25)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.132 (n=17)

### LIQUIDACIONES_DEPTH_FASE0#BTC#15min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.122 (n=239)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=278)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.49` → IC=+0.155 (n=198)

  - _Acción_: Kelly boost +0.78€ cuando `py_entrada` < 0.49 (IC base=+0.018)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.172 (n=59)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=263)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.137 (n=155)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=178)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.159 (n=42)

  - _Acción_: Kelly boost +0.80€ cuando `py_entrada` < 0.5 (IC base=+0.052)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.48` → IC=-0.125 (n=321)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=177)

- **FILTRO** `profundidad_ratio` < `41.6` → IC=-0.156 (n=123)

  - _Acción_: SKIP cuando `profundidad_ratio` < 41.6
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=375)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.139 (n=206)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.055 (n=234)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.159 (n=89)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=385)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.144 (n=130)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=477)

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
- **FILTRO** `py_entrada` < `0.47` → IC=-0.163 (n=6180)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.066 (n=19056)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.177 (n=6248)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=19637)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.193 (n=1130)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.118 (n=3478)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.175 (n=1069)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.067 (n=3547)

- **PATRÓN** `py_entrada` > `0.495` → IC=+0.130 (n=3104)

  - _Acción_: Kelly boost +0.65€ cuando `py_entrada` > 0.495 (IC base=+0.042)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.144 (n=1213)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` > 1.0 (IC base=+0.042)

- **PATRÓN** `libro_liquidez` > `1249.264` → IC=+0.136 (n=2304)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 1249.264 (IC base=+0.042)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.128 (n=2159)

  - _Acción_: Kelly boost +0.64€ cuando `py_entrada` < 0.5 (IC base=+0.011)

- **PATRÓN** `libro_liquidez` > `1460.096` → IC=+0.152 (n=1570)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 1460.096 (IC base=+0.011)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.151 (n=863)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=2819)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.177 (n=899)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=2765)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` > `0.61` → IC=-0.188 (n=1180)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.077 (n=3543)

- **PATRÓN** `ibs_20min` > `0.9645` → IC=+0.132 (n=1567)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` > 0.9645 (IC base=+0.039)

- **PATRÓN** `libro_liquidez` > `1799.8784` → IC=+0.128 (n=1567)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 1799.8784 (IC base=+0.039)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.157 (n=1122)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=3479)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=2401)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.162 (n=772)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=2325)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.208 (n=761)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=2823)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=3563)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` > `20.0` → IC=-0.146 (n=125)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 20.0
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=445)

- **FILTRO** `py_entrada` < `0.455` → IC=-0.257 (n=142)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=428)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.234 (n=287)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=893)

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
  - _Potencial_: sin este filtro IC_bueno=-0.095 (n=299)

- **FILTRO** `ibs_20min` > `0.9798` → IC=-0.188 (n=110)

  - _Acción_: SKIP cuando `ibs_20min` > 0.9798
  - _Potencial_: sin este filtro IC_bueno=-0.105 (n=332)

- **FILTRO** `libro_liquidez` < `3730.8295` → IC=-0.168 (n=221)

  - _Acción_: SKIP cuando `libro_liquidez` < 3730.8295
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=221)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=939)

- **FILTRO** `libro_liquidez` < `1784.2378` → IC=-0.164 (n=239)

  - _Acción_: SKIP cuando `libro_liquidez` < 1784.2378
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=719)

- **FILTRO** `libro_liquidez` < `2089.8344` → IC=-0.170 (n=349)

  - _Acción_: SKIP cuando `libro_liquidez` < 2089.8344
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=710)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.130 (n=17306)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=38826)

- **FILTRO** `py_entrada` < `0.33` → IC=-0.285 (n=13835)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=42297)

- **FILTRO** `ibs_7min` < `0.2358` → IC=-0.228 (n=14033)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2358
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=42099)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.152 (n=18651)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=37481)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.242 (n=17334)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=53160)

- **FILTRO** `ibs_7min` > `0.2857` → IC=-0.182 (n=17459)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2857
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=53035)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.148 (n=2795)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=7034)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.311 (n=2344)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=7485)

- **FILTRO** `ibs_7min` < `0.7125` → IC=-0.242 (n=3243)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7125
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=6586)

- **FILTRO** `ballena_activa_n` > `6.0` → IC=-0.180 (n=2053)

  - _Acción_: SKIP cuando `ballena_activa_n` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=7776)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.272 (n=3039)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=9183)

- **FILTRO** `ibs_7min` > `0.7713` → IC=-0.211 (n=3055)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7713
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=9167)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.128 (n=2266)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.095 (n=7201)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.265 (n=2215)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=7252)

- **FILTRO** `ibs_7min` < `0.726` → IC=-0.198 (n=2365)

  - _Acción_: SKIP cuando `ibs_7min` < 0.726
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=7102)

- **FILTRO** `ballena_activa_n` > `155.0` → IC=-0.190 (n=2348)

  - _Acción_: SKIP cuando `ballena_activa_n` > 155.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=7119)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.263 (n=2365)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=7240)

- **FILTRO** `ibs_7min` > `0.2678` → IC=-0.194 (n=2399)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2678
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=7206)

- **FILTRO** `ballena_activa_n` > `152.0` → IC=-0.183 (n=2385)

  - _Acción_: SKIP cuando `ballena_activa_n` > 152.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=7220)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.159 (n=2290)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=7036)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.312 (n=2294)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=7032)

- **FILTRO** `ibs_7min` < `0.2941` → IC=-0.245 (n=3074)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2941
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=6252)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.194 (n=2212)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=7114)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.254 (n=3035)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=9964)

- **FILTRO** `ibs_7min` > `0.7341` → IC=-0.178 (n=3249)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7341
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=9750)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.124 (n=2973)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.091 (n=6172)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.261 (n=2145)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=7000)

- **FILTRO** `ibs_7min` < `0.7281` → IC=-0.184 (n=2286)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7281
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=6859)

- **FILTRO** `ballena_activa_n` > `27.0` → IC=-0.188 (n=2247)

  - _Acción_: SKIP cuando `ballena_activa_n` > 27.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=6898)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.268 (n=2140)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=7331)

- **FILTRO** `ibs_7min` > `0.2751` → IC=-0.178 (n=2367)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2751
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=7104)

- **FILTRO** `ballena_activa_n` > `26.0` → IC=-0.178 (n=2312)

  - _Acción_: SKIP cuando `ballena_activa_n` > 26.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=7159)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.284 (n=2215)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=6975)

- **FILTRO** `ibs_7min` < `0.7143` → IC=-0.221 (n=2966)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7143
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=6224)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.217 (n=2218)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=6972)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.191 (n=3287)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=10174)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.32` → IC=-0.293 (n=2174)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=7001)

- **FILTRO** `ibs_7min` < `0.2` → IC=-0.222 (n=2283)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=6892)

- **FILTRO** `ballena_activa_n` > `9.0` → IC=-0.197 (n=2286)

  - _Acción_: SKIP cuando `ballena_activa_n` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=6889)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.219 (n=3126)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=9610)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1046` → IC=-0.135 (n=61)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1046
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=120)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `py_entrada` < `0.455` → IC=-0.158 (n=299)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=986)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=1270)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.121 (n=209)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=496)

- **FILTRO** `py_entrada` > `0.545` → IC=-0.152 (n=156)

  - _Acción_: SKIP cuando `py_entrada` > 0.545
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=549)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=1458)

- **FILTRO** `py_entrada` > `0.565` → IC=-0.172 (n=260)

  - _Acción_: SKIP cuando `py_entrada` > 0.565
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=851)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `py_entrada` < `0.475` → IC=-0.122 (n=162)

  - _Acción_: SKIP cuando `py_entrada` < 0.475
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=333)

- **FILTRO** `ballena_activa_n` > `3.0` → IC=-0.143 (n=166)

  - _Acción_: SKIP cuando `ballena_activa_n` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=328)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.231 (n=50)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=445)

- **FILTRO** `libro_liquidez` < `3255.5511` → IC=-0.152 (n=179)

  - _Acción_: SKIP cuando `libro_liquidez` < 3255.5511
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=539)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=387)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.3981` → IC=+0.138 (n=1178)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.69€ cuando `delta_ratio` |x|> 0.3981 (IC base=+0.129)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.135 (n=612)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 6.0 (IC base=+0.129)

- **PATRÓN** `total_vol_5m` < `432.5464` → IC=+0.156 (n=393)

  - _Acción_: Kelly boost +0.78€ cuando `total_vol_5m` < 432.5464 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `3606.826` → IC=+0.149 (n=534)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 3606.826 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.149 (n=388)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 11.0 (IC base=+0.129)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.4377` → IC=+0.149 (n=92)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.74€ cuando `delta_ratio` |x|> 0.4377 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.193 (n=135)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 14.0 (IC base=+0.135)

- **PATRÓN** `total_vol_5m` < `372.075` → IC=+0.145 (n=243)

  - _Acción_: Kelly boost +0.72€ cuando `total_vol_5m` < 372.075 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `2558.8539` → IC=+0.202 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2558.8539 (IC base=+0.135)

- **PATRÓN** `ballena_activa_n` < `6.0` → IC=+0.156 (n=91)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 6.0 (IC base=+0.135)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `delta_ratio` |x|> `0.3992` → IC=+0.133 (n=243)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.66€ cuando `delta_ratio` |x|> 0.3992 (IC base=+0.118)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.135 (n=217)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 14.0 (IC base=+0.118)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.128 (n=291)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.04 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `2340.1091` → IC=+0.134 (n=162)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 2340.1091 (IC base=+0.118)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4161` → IC=+0.181 (n=155)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.91€ cuando `delta_ratio` |x|> 0.4161 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.154 (n=241)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 4.0 (IC base=+0.138)

- **PATRÓN** `total_vol_5m` < `384.339` → IC=+0.214 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 384.339 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `7706.3933` → IC=+0.143 (n=155)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 7706.3933 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `70.0` → IC=+0.195 (n=103)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 70.0 (IC base=+0.138)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.4324` → IC=+0.250 (n=94)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio` |x|> 0.4324 (IC base=+0.150)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.172 (n=190)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 15.0 (IC base=+0.150)

- **PATRÓN** `total_vol_5m` < `4950.202` → IC=+0.186 (n=138)

  - _Acción_: Kelly boost +0.93€ cuando `total_vol_5m` < 4950.202 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `2945.8122` → IC=+0.160 (n=207)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 2945.8122 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.162 (n=72)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 27.0 (IC base=+0.150)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `hora_utc` < `14.0` → IC=+0.126 (n=201)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 14.0 (IC base=+0.100)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.179 (n=135)

  - _Acción_: Kelly boost +0.89€ cuando `libro_spread` < 0.01 (IC base=+0.100)

- **PATRÓN** `libro_liquidez` > `3589.6144` → IC=+0.167 (n=100)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 3589.6144 (IC base=+0.100)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `7.9794` → IC=-0.266 (n=45)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 7.9794
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=139)

- **FILTRO** `sigma_h` > `0.0072` → IC=-0.333 (n=166)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0072
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=501)

- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.180 (n=167)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0035 (IC base=-0.086)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0069` → IC=-0.343 (n=49)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0069
  - _Potencial_: sin este filtro IC_bueno=+0.070 (n=149)

- **FILTRO** `T_h` > `87.9936` → IC=-0.245 (n=49)

  - _Acción_: SKIP cuando `T_h` > 87.9936
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=149)

- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.308 (n=50)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=-0.035)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `sigma_h` > `0.0062` → IC=-0.232 (n=39)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0062
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=25)

- **FILTRO** `pct_vs_K` |x|> `9.8932` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 9.8932
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=49)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0086` → IC=-0.233 (n=58)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0086
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=60)

- **FILTRO** `T_h` < `60.2781` → IC=-0.150 (n=38)

  - _Acción_: SKIP cuando `T_h` < 60.2781
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=80)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0094` → IC=-0.226 (n=407)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0094
  - _Potencial_: sin este filtro IC_bueno=-0.099 (n=210)

- **FILTRO** `T_h` > `87.6765` → IC=-0.199 (n=413)

  - _Acción_: SKIP cuando `T_h` > 87.6765
  - _Potencial_: sin este filtro IC_bueno=-0.150 (n=204)

- **FILTRO** `pct_vs_K` |x|> `3.3065` → IC=-0.433 (n=132)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.3065
  - _Potencial_: sin este filtro IC_bueno=-0.168 (n=398)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `T_h` > `71.159` → IC=-0.176 (n=134)

  - _Acción_: SKIP cuando `T_h` > 71.159
  - _Potencial_: sin este filtro IC_bueno=-0.109 (n=67)

- **FILTRO** `pct_vs_K` |x|> `2.7856` → IC=-0.365 (n=50)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.7856
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=151)

- **FILTRO** `T_h` > `73.6519` → IC=-0.282 (n=140)

  - _Acción_: SKIP cuando `T_h` > 73.6519
  - _Potencial_: sin este filtro IC_bueno=-0.240 (n=48)

- **FILTRO** `pct_vs_K` |x|> `2.9891` → IC=-0.436 (n=45)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.9891
  - _Potencial_: sin este filtro IC_bueno=-0.217 (n=143)

### PRICE_TARGET_GBM_FADE#BTC#reach
- **FILTRO** `T_h` < `139.5329` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `T_h` < 139.5329
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

- **FILTRO** `sigma_h` < `0.0078` → IC=-0.262 (n=19)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0078
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=10)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `pct_vs_K` |x|> `3.2636` → IC=-0.387 (n=60)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.2636
  - _Potencial_: sin este filtro IC_bueno=-0.175 (n=118)

- **FILTRO** `sigma_h` > `0.0091` → IC=-0.384 (n=41)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0091
  - _Potencial_: sin este filtro IC_bueno=-0.119 (n=124)

- **FILTRO** `T_h` > `57.7851` → IC=-0.277 (n=110)

  - _Acción_: SKIP cuando `T_h` > 57.7851
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=55)

### PRICE_TARGET_GBM_FADE#ETH#reach
- **FILTRO** `T_h` < `145.7969` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `T_h` < 145.7969
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=6)

- **FILTRO** `sigma_h` < `0.0098` → IC=-0.206 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0098
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` < `0.008` → IC=-0.273 (n=42)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.008
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=129)

- **FILTRO** `T_h` > `94.0115` → IC=-0.224 (n=114)

  - _Acción_: SKIP cuando `T_h` > 94.0115
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=57)

- **FILTRO** `sigma_h` > `0.0135` → IC=-0.357 (n=40)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0135
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=78)

- **FILTRO** `sigma_h` < `0.0086` → IC=-0.275 (n=38)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0086
  - _Potencial_: sin este filtro IC_bueno=-0.232 (n=80)

- **FILTRO** `T_h` > `41.2641` → IC=-0.290 (n=79)

  - _Acción_: SKIP cuando `T_h` > 41.2641
  - _Potencial_: sin este filtro IC_bueno=-0.159 (n=39)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1236` → IC=+0.477 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1236 (IC base=+0.343)

- **PATRÓN** `sigma_h` < `0.0138` → IC=+0.359 (n=97)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0138 (IC base=+0.343)

- **PATRÓN** `sigma_h` > `0.0102` → IC=+0.394 (n=64)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0102 (IC base=+0.343)

- **PATRÓN** `T_h` < `0.3604` → IC=+0.386 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.3604 (IC base=+0.343)

- **PATRÓN** `T_h` > `0.7606` → IC=+0.379 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.7606 (IC base=+0.343)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.479 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.343)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.359 (n=90)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.343)

- **PATRÓN** `edge` > `0.0992` → IC=+0.442 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.0992 (IC base=+0.416)

- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.440 (n=149)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0097 (IC base=+0.416)

- **PATRÓN** `T_h` < `0.5967` → IC=+0.436 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.5967 (IC base=+0.416)

- **PATRÓN** `T_h` > `1.484` → IC=+0.422 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.484 (IC base=+0.416)

- **PATRÓN** `dist_50` > `0.3772` → IC=+0.456 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3772 (IC base=+0.416)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.478 (n=136)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.416)

### RESOLUTION_SNIPER#BTC#sniper
- **PATRÓN** `edge` > `0.1831` → IC=+0.239 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1831 (IC base=+0.186)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.186)

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
- **PATRÓN** `edge` > `0.1838` → IC=+0.484 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1838 (IC base=+0.440)

- **PATRÓN** `sigma_h` < `0.0163` → IC=+0.468 (n=60)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0163 (IC base=+0.440)

- **PATRÓN** `T_h` > `0.3968` → IC=+0.452 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.3968 (IC base=+0.440)

- **PATRÓN** `dist_50` > `0.354` → IC=+0.468 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.354 (IC base=+0.440)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.438 (n=30)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.440)

- **PATRÓN** `edge` > `0.2005` → IC=+0.479 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.2005 (IC base=+0.465)

- **PATRÓN** `sigma_h` < `0.0156` → IC=+0.479 (n=140)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0156 (IC base=+0.465)

- **PATRÓN** `T_h` > `1.4874` → IC=+0.480 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4874 (IC base=+0.465)

- **PATRÓN** `dist_50` > `0.4659` → IC=+0.492 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4659 (IC base=+0.465)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.472 (n=143)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.465)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=314)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=390)

- **PATRÓN** `streak_estiramiento` < `0.8382` → IC=+0.125 (n=262)

  - _Acción_: Kelly boost +0.62€ cuando `streak_estiramiento` < 0.8382 (IC base=+0.049)

- **PATRÓN** `libro_liquidez` > `2526.0042` → IC=+0.143 (n=141)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 2526.0042 (IC base=+0.049)

### STREAK_FADE_15M#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=28)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.119 (n=19)

### STREAK_FADE_15M#XRP#15min
- **PATRÓN** `streak_estiramiento` < `0.2566` → IC=+0.159 (n=39)

  - _Acción_: Kelly boost +0.79€ cuando `streak_estiramiento` < 0.2566 (IC base=+0.000)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.136 (n=119)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 7.0 (IC base=+0.091)

- **PATRÓN** `streak_estiramiento` < `0.4496` → IC=+0.196 (n=100)

  - _Acción_: Kelly boost +0.98€ cuando `streak_estiramiento` < 0.4496 (IC base=+0.091)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.161 (n=110)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 35.0 (IC base=+0.091)

- **PATRÓN** `libro_liquidez` > `2223.4384` → IC=+0.139 (n=131)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 2223.4384 (IC base=+0.091)

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

- **FILTRO** `streak_estiramiento` > `1.1496` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `streak_estiramiento` > 1.1496
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=43)

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

  - _Acción_: Kelly boost +1.00€ cuando `regimen_ma_toques` > 4.0 (IC base=+0.056)

- **PATRÓN** `volumen_racha` < `17126.646` → IC=+0.206 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_racha` < 17126.646 (IC base=+0.056)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=1016)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=1331)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=1166)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=1214)

### STRUCT_NO_15M
- **FILTRO** `hora_utc` < `16.0` → IC=-0.214 (n=19)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.091 (n=20)

- **FILTRO** `py_entrada` < `0.455` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=24)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=4079)

### STRUCT_NO_15M#ETH#15min
- **FILTRO** `hora_utc` < `16.0` → IC=-0.214 (n=19)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.091 (n=20)

- **FILTRO** `py_entrada` < `0.455` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=24)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=2261)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.195 (n=1235)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0047 (IC base=+0.176)

- **PATRÓN** `sigma_h` > `0.012` → IC=+0.198 (n=1235)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.012 (IC base=+0.176)

- **PATRÓN** `drift_60min` |x|≤ `0.177` → IC=+0.191 (n=3262)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.177 (IC base=+0.176)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1909` → IC=+0.177 (n=1681)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.89€ cuando `delta_ratio_macro` |x|> 0.1909 (IC base=+0.176)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1331` → IC=+0.185 (n=1482)

  - _Acción_: Kelly boost +0.92€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1331 (IC base=+0.176)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.185 (n=3423)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 6.0 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.179 (n=3408)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 15.0 (IC base=+0.176)

- **PATRÓN** `ibs_15` > `0.5475` → IC=+0.252 (n=3704)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5475 (IC base=+0.176)

- **PATRÓN** `dist_vwap_pct` > `0.1291` → IC=+0.170 (n=1794)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.1291 (IC base=+0.176)

- **PATRÓN** `dist_vwap_pct` < `0.6687` → IC=+0.164 (n=3540)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.6687 (IC base=+0.176)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.468` → IC=+0.258 (n=956)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.468 (IC base=+0.176)

- **PATRÓN** `libro_liquidez` > `4653.0512` → IC=+0.193 (n=1235)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 4653.0512 (IC base=+0.176)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=1470)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.255 (n=210)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0026 (IC base=+0.218)

- **PATRÓN** `sigma_h` > `0.0046` → IC=+0.219 (n=286)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0046 (IC base=+0.218)

- **PATRÓN** `drift_60min` |x|≤ `0.0592` → IC=+0.274 (n=210)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0592 (IC base=+0.218)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2526` → IC=+0.244 (n=209)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2526 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.238 (n=628)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.218)

- **PATRÓN** `ibs_15` > `0.7223` → IC=+0.284 (n=627)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7223 (IC base=+0.218)

- **PATRÓN** `dist_vwap_pct` > `0.1382` → IC=+0.233 (n=365)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1382 (IC base=+0.218)

- **PATRÓN** `dist_vwap_pct` < `0.5302` → IC=+0.224 (n=709)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5302 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.108` → IC=+0.299 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.108 (IC base=+0.218)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.219 (n=814)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.218)

- **PATRÓN** `libro_liquidez` > `8715.5535` → IC=+0.230 (n=627)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8715.5535 (IC base=+0.218)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `sigma_ewma_delta_pct` > `28.269` → IC=-0.203 (n=35)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 28.269
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=807)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.187 (n=247)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0035 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.1075` → IC=+0.151 (n=491)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.1075 (IC base=+0.144)

- **PATRÓN** `drift_15min` |x|≤ `0.3963` → IC=+0.145 (n=246)

  - _Acción_: Kelly boost +0.73€ cuando `drift_15min` |x|≤ 0.3963 (IC base=+0.144)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1428` → IC=+0.150 (n=490)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.75€ cuando `delta_ratio_macro` |x|> 0.1428 (IC base=+0.144)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.129` → IC=+0.157 (n=292)

  - _Acción_: Kelly boost +0.78€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.129 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.152 (n=674)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 6.0 (IC base=+0.144)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.150 (n=766)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 17.0 (IC base=+0.144)

- **PATRÓN** `ibs_15` > `0.5373` → IC=+0.239 (n=735)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5373 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` > `0.1197` → IC=+0.157 (n=459)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.1197 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.577` → IC=+0.270 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.577 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `3217.9115` → IC=+0.150 (n=735)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 3217.9115 (IC base=+0.144)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `sigma_ewma_delta_pct` > `17.774` → IC=-0.192 (n=37)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 17.774
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=349)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `ibs_15` > `0.8868` → IC=+0.249 (n=285)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8868 (IC base=+0.095)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.086` → IC=+0.173 (n=163)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 17.086 (IC base=+0.095)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.134 (n=471)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.095)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.024` → IC=+0.232 (n=282)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.024 (IC base=+0.202)

- **PATRÓN** `drift_60min` |x|≤ `0.1305` → IC=+0.225 (n=565)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1305 (IC base=+0.202)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0952` → IC=+0.246 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0952 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.203 (n=768)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.202)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.212 (n=756)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.202)

- **PATRÓN** `ibs_15` > `0.5294` → IC=+0.276 (n=847)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5294 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` > `0.1272` → IC=+0.212 (n=491)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1272 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` < `0.7022` → IC=+0.202 (n=982)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.7022 (IC base=+0.202)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.077` → IC=+0.233 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.077 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `2959.5754` → IC=+0.292 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2959.5754 (IC base=+0.202)

- **PATRÓN** `ibs_15` < `0.1094` → IC=+0.162 (n=784)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.81€ cuando `ibs_15` < 0.1094 (IC base=+0.068)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` > `0.0056` → IC=+0.394 (n=214)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0056 (IC base=+0.364)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1476` → IC=+0.383 (n=427)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1476 (IC base=+0.364)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1403` → IC=+0.386 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1403 (IC base=+0.364)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.377 (n=646)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.364)

- **PATRÓN** `ibs_15` > `0.7863` → IC=+0.401 (n=641)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7863 (IC base=+0.364)

- **PATRÓN** `dist_vwap_pct` > `0.1477` → IC=+0.380 (n=372)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1477 (IC base=+0.364)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.239` → IC=+0.387 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.239 (IC base=+0.364)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.368 (n=781)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.364)

- **PATRÓN** `libro_liquidez` > `10218.4138` → IC=+0.384 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10218.4138 (IC base=+0.364)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.363 (n=291)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.362)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.402 (n=110)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.362)

- **PATRÓN** `drift_60min` |x|≤ `0.0554` → IC=+0.367 (n=111)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0554 (IC base=+0.362)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2147` → IC=+0.388 (n=150)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2147 (IC base=+0.362)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1413` → IC=+0.393 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1413 (IC base=+0.362)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.380 (n=331)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.362)

- **PATRÓN** `ibs_15` > `0.8048` → IC=+0.392 (n=330)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8048 (IC base=+0.362)

- **PATRÓN** `dist_vwap_pct` > `0.2499` → IC=+0.387 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2499 (IC base=+0.362)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.521` → IC=+0.380 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.521 (IC base=+0.362)

- **PATRÓN** `libro_liquidez` > `16828.3206` → IC=+0.402 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16828.3206 (IC base=+0.362)

- **PATRÓN** `ballena_activa_n` < `493.0` → IC=+0.404 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 493.0 (IC base=+0.362)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.370 (n=137)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.365)

- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.388 (n=141)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0058 (IC base=+0.365)

- **PATRÓN** `delta_ratio_macro` |x|> `0.087` → IC=+0.382 (n=278)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.087 (IC base=+0.365)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2969` → IC=+0.385 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2969 (IC base=+0.365)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.389 (n=151)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.365)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.374 (n=141)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.365)

- **PATRÓN** `ibs_15` > `0.7485` → IC=+0.410 (n=311)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7485 (IC base=+0.365)

- **PATRÓN** `dist_vwap_pct` > `0.4658` → IC=+0.386 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4658 (IC base=+0.365)

- **PATRÓN** `dist_vwap_pct` < `0.2961` → IC=+0.368 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2961 (IC base=+0.365)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.293` → IC=+0.393 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.293 (IC base=+0.365)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.369 (n=350)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.365)

- **PATRÓN** `libro_liquidez` > `4001.8474` → IC=+0.395 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4001.8474 (IC base=+0.365)

- **PATRÓN** `ballena_activa_n` < `159.0` → IC=+0.376 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 159.0 (IC base=+0.365)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0124` → IC=-0.228 (n=1102)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0124
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=3311)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.213 (n=1725)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=2688)

- **FILTRO** `libro_liquidez` < `4202.8528` → IC=-0.154 (n=2912)

  - _Acción_: SKIP cuando `libro_liquidez` < 4202.8528
  - _Potencial_: sin este filtro IC_bueno=+0.098 (n=1501)

- **PATRÓN** `ibs_15` > `0.6326` → IC=+0.280 (n=1065)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6326 (IC base=-0.068)

- **PATRÓN** `dist_vwap_pct` > `0.1115` → IC=+0.205 (n=611)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1115 (IC base=-0.068)

- **PATRÓN** `dist_vwap_pct` < `0.4306` → IC=+0.199 (n=1041)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` < 0.4306 (IC base=-0.068)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2306` → IC=+0.269 (n=1223)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2306 (IC base=-0.013)

- **PATRÓN** `ibs_15` < `0.3605` → IC=+0.283 (n=3668)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3605 (IC base=-0.013)

- **PATRÓN** `dist_vwap_pct` > `0.6602` → IC=+0.276 (n=498)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6602 (IC base=-0.013)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0067` → IC=-0.216 (n=647)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0067
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=1945)

- **FILTRO** `sigma_h` < `0.0035` → IC=-0.228 (n=648)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0035
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=1944)

- **FILTRO** `sigma_ewma_delta_pct` > `23.3` → IC=-0.273 (n=372)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 23.3
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=2220)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=66)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.195 (n=2526)

- **FILTRO** `libro_liquidez` < `11045.5521` → IC=-0.218 (n=648)

  - _Acción_: SKIP cuando `libro_liquidez` < 11045.5521
  - _Potencial_: sin este filtro IC_bueno=-0.187 (n=1944)

- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.173 (n=258)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0028 (IC base=+0.095)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2081` → IC=+0.281 (n=158)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2081 (IC base=+0.095)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1125` → IC=+0.274 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1125 (IC base=+0.095)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.122 (n=774)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 5.0 (IC base=+0.095)

- **PATRÓN** `ibs_15` > `0.7572` → IC=+0.331 (n=348)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7572 (IC base=+0.095)

- **PATRÓN** `dist_vwap_pct` > `0.1051` → IC=+0.282 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1051 (IC base=+0.095)

- **PATRÓN** `dist_vwap_pct` < `0.5105` → IC=+0.296 (n=386)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5105 (IC base=+0.095)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.603` → IC=+0.130 (n=387)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` > 8.603 (IC base=+0.095)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0659` → IC=+0.214 (n=61)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0659 (IC base=-0.195)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.159` → IC=+0.293 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.159 (IC base=-0.195)

- **PATRÓN** `ibs_15` < `0.6128` → IC=+0.309 (n=61)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.6128 (IC base=-0.195)

- **PATRÓN** `dist_vwap_pct` < `0.0459` → IC=+0.288 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0459 (IC base=-0.195)

- **PATRÓN** `ballena_activa_n` < `291.0` → IC=+0.364 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 291.0 (IC base=-0.195)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.156 (n=696)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.162 (n=471)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0058 (IC base=+0.149)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.157 (n=357)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0049 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.0544` → IC=+0.191 (n=179)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.0544 (IC base=+0.149)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2995` → IC=+0.193 (n=411)

  - _Acción_: Kelly boost +0.96€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2995 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.170 (n=383)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 11.0 (IC base=+0.149)

- **PATRÓN** `ibs_15` > `0.5959` → IC=+0.247 (n=535)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5959 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.4686` → IC=+0.171 (n=141)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.4686 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.243` → IC=+0.245 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.243 (IC base=+0.149)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.156 (n=696)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.01 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `7935.7814` → IC=+0.153 (n=243)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 7935.7814 (IC base=+0.149)

- **PATRÓN** `sigma_h` < `0.0077` → IC=+0.251 (n=1339)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0077 (IC base=+0.245)

- **PATRÓN** `drift_15min` |x|≤ `0.7722` → IC=+0.257 (n=1180)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7722 (IC base=+0.245)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2176` → IC=+0.262 (n=607)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2176 (IC base=+0.245)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.253 (n=495)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.245)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.246 (n=514)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.245)

- **PATRÓN** `ibs_15` < `0.3707` → IC=+0.276 (n=1339)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3707 (IC base=+0.245)

- **PATRÓN** `dist_vwap_pct` > `0.6145` → IC=+0.264 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6145 (IC base=+0.245)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.405` → IC=+0.255 (n=594)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.405 (IC base=+0.245)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `sigma_h` > `0.0105` → IC=-0.247 (n=255)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0105
  - _Potencial_: sin este filtro IC_bueno=-0.171 (n=769)

- **FILTRO** `drift_60min` |x|> `0.1729` → IC=-0.251 (n=348)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1729
  - _Potencial_: sin este filtro IC_bueno=-0.158 (n=676)

- **FILTRO** `drift_15min` |x|> `0.888` → IC=-0.282 (n=255)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.888
  - _Potencial_: sin este filtro IC_bueno=-0.159 (n=769)

- **FILTRO** `sigma_ewma_delta_pct` > `6.585` → IC=-0.203 (n=237)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.585
  - _Potencial_: sin este filtro IC_bueno=-0.186 (n=787)

- **FILTRO** `sigma_ewma_delta_pct` > `17.898` → IC=-0.149 (n=534)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 17.898
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=4244)

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

- **PATRÓN** `delta_ratio_macro` |x|> `0.0819` → IC=+0.236 (n=524)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0819 (IC base=-0.041)

- **PATRÓN** `ibs_15` < `0.3529` → IC=+0.292 (n=589)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3529 (IC base=-0.041)

- **PATRÓN** `dist_vwap_pct` < `0.4416` → IC=+0.242 (n=615)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4416 (IC base=-0.041)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0198` → IC=-0.253 (n=606)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0198
  - _Potencial_: sin este filtro IC_bueno=-0.165 (n=607)

- **FILTRO** `drift_60min` |x|> `0.1534` → IC=-0.215 (n=303)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1534
  - _Potencial_: sin este filtro IC_bueno=-0.207 (n=910)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.209)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.209)

- **PATRÓN** `delta_ratio_macro` |x|> `0.069` → IC=+0.275 (n=784)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.069 (IC base=-0.026)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1165` → IC=+0.294 (n=381)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1165 (IC base=-0.026)

- **PATRÓN** `ibs_15` < `0.1376` → IC=+0.314 (n=585)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.1376 (IC base=-0.026)

- **PATRÓN** `dist_vwap_pct` > `0.7759` → IC=+0.354 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7759 (IC base=-0.026)

### UPDOWN_GBM_ETH_15M_HORA7
- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.222 (n=16)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0036 (IC base=+0.080)

- **PATRÓN** `drift_15min` |x|≤ `0.3927` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3927 (IC base=+0.080)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2386` → IC=+0.208 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2386 (IC base=+0.080)

- **PATRÓN** `ibs_15` > `0.8434` → IC=+0.342 (n=17)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8434 (IC base=+0.080)

- **PATRÓN** `dist_vwap_pct` < `0.1207` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` < 0.1207 (IC base=+0.080)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.222 (n=16)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0036 (IC base=+0.080)

- **PATRÓN** `drift_15min` |x|≤ `0.3927` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3927 (IC base=+0.080)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2386` → IC=+0.208 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2386 (IC base=+0.080)

- **PATRÓN** `ibs_15` > `0.8434` → IC=+0.342 (n=17)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8434 (IC base=+0.080)

- **PATRÓN** `dist_vwap_pct` < `0.1207` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` < 0.1207 (IC base=+0.080)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.297 (n=967)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.291)

- **PATRÓN** `drift_60min` |x|≤ `0.0534` → IC=+0.321 (n=367)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0534 (IC base=+0.291)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2423` → IC=+0.310 (n=366)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2423 (IC base=+0.291)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.224` → IC=+0.302 (n=655)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.224 (IC base=+0.291)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.308 (n=1143)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.291)

- **PATRÓN** `ibs_15` > `0.8393` → IC=+0.319 (n=1098)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8393 (IC base=+0.291)

- **PATRÓN** `dist_vwap_pct` > `0.2727` → IC=+0.323 (n=477)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2727 (IC base=+0.291)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.589` → IC=+0.378 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.589 (IC base=+0.291)

- **PATRÓN** `libro_liquidez` > `12246.363` → IC=+0.312 (n=498)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12246.363 (IC base=+0.291)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.308 (n=259)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.289)

- **PATRÓN** `sigma_h` > `0.0046` → IC=+0.303 (n=267)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0046 (IC base=+0.289)

- **PATRÓN** `drift_60min` |x|≤ `0.0584` → IC=+0.314 (n=197)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0584 (IC base=+0.289)

- **PATRÓN** `delta_ratio_macro` |x|> `0.258` → IC=+0.313 (n=196)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.258 (IC base=+0.289)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.307 (n=589)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.289)

- **PATRÓN** `ibs_15` > `0.8303` → IC=+0.315 (n=588)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8303 (IC base=+0.289)

- **PATRÓN** `dist_vwap_pct` > `0.1463` → IC=+0.320 (n=337)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1463 (IC base=+0.289)

- **PATRÓN** `dist_vwap_pct` < `0.5513` → IC=+0.288 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5513 (IC base=+0.289)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.701` → IC=+0.380 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.701 (IC base=+0.289)

- **PATRÓN** `libro_liquidez` > `16178.7073` → IC=+0.333 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16178.7073 (IC base=+0.289)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.303 (n=511)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.293)

- **PATRÓN** `drift_60min` |x|≤ `0.0518` → IC=+0.321 (n=171)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0518 (IC base=+0.293)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1451` → IC=+0.298 (n=340)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1451 (IC base=+0.293)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3049` → IC=+0.306 (n=411)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3049 (IC base=+0.293)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.314 (n=492)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.293)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.297 (n=461)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.293)

- **PATRÓN** `ibs_15` > `0.8489` → IC=+0.320 (n=510)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8489 (IC base=+0.293)

- **PATRÓN** `dist_vwap_pct` > `0.2899` → IC=+0.319 (n=219)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2899 (IC base=+0.293)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.52` → IC=+0.368 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.52 (IC base=+0.293)

### UPDOWN_OU_5M
- **FILTRO** `drift_60min` |x|> `0.2656` → IC=-0.140 (n=84)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2656
  - _Potencial_: sin este filtro IC_bueno=-0.107 (n=255)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.1226` → IC=-0.151 (n=84)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1226
  - _Potencial_: sin este filtro IC_bueno=-0.103 (n=255)

- **FILTRO** `ballena_activa_n` > `44.0` → IC=-0.136 (n=229)

  - _Acción_: SKIP cuando `ballena_activa_n` > 44.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=78)

- **FILTRO** `sigma_h` < `0.0051` → IC=-0.180 (n=120)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0051
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=360)

- **FILTRO** `ballena_activa_n` > `41.0` → IC=-0.216 (n=72)

  - _Acción_: SKIP cuando `ballena_activa_n` > 41.0
  - _Potencial_: sin este filtro IC_bueno=-0.138 (n=147)

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

- **FILTRO** `drift_15min` |x|> `0.3423` → IC=-0.289 (n=17)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.3423
  - _Potencial_: sin este filtro IC_bueno=-0.095 (n=35)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.2021` → IC=-0.250 (n=26)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2021
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=26)

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
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=38)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.3147` → IC=-0.385 (n=24)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.3147
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.0611` → IC=-0.259 (n=27)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.0611
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=10)

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
- **PATRÓN** `T_h` > `87.7391` → IC=+0.193 (n=490)

  - _Acción_: Kelly boost +0.97€ cuando `T_h` > 87.7391 (IC base=+0.192)

- **PATRÓN** `ratio` < `0.973` → IC=+0.408 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.973 (IC base=+0.192)

- **PATRÓN** `T_h` > `115.2222` → IC=+0.352 (n=2232)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 115.2222 (IC base=+0.336)

- **PATRÓN** `ratio` > `1.0229` → IC=+0.374 (n=363)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0229 (IC base=+0.336)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `109.5528` → IC=+0.178 (n=203)

  - _Acción_: Kelly boost +0.89€ cuando `T_h` > 109.5528 (IC base=+0.161)

- **PATRÓN** `ratio` < `0.983` → IC=+0.332 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.983 (IC base=+0.161)

- **PATRÓN** `T_h` > `111.9824` → IC=+0.302 (n=772)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9824 (IC base=+0.292)

- **PATRÓN** `ratio` > `1.0189` → IC=+0.333 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0189 (IC base=+0.292)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `83.3501` → IC=+0.234 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 83.3501 (IC base=+0.232)

- **PATRÓN** `ratio` < `0.9854` → IC=+0.399 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9854 (IC base=+0.232)

- **PATRÓN** `T_h` > `111.9905` → IC=+0.351 (n=805)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9905 (IC base=+0.324)

- **PATRÓN** `ratio` > `1.0347` → IC=+0.391 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0347 (IC base=+0.324)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.0966` → IC=+0.441 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.0966 (IC base=+0.399)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5475 sube el IC de +0.176 a +0.252 en UPDOWN_GBM#15min (n=3704). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7223 sube el IC de +0.218 a +0.284 en UPDOWN_GBM#BTC#15min (n=627). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.5373 sube el IC de +0.144 a +0.239 en UPDOWN_GBM#ETH#15min (n=735). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.8868 sube el IC de +0.095 a +0.249 en UPDOWN_GBM#SOL#15min (n=285). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5294 sube el IC de +0.202 a +0.276 en UPDOWN_GBM#XRP#15min (n=847). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1094 sube el IC de +0.068 a +0.162 en UPDOWN_GBM#XRP#15min (n=784). Ya aplicado como kelly_boost=+0.81€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6326 sube el IC de -0.068 a +0.280 en UPDOWN_GBM_15M_TARDIO (n=1065). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3605 sube el IC de -0.013 a +0.283 en UPDOWN_GBM_15M_TARDIO (n=3668). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7572 sube el IC de +0.095 a +0.331 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=348). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.6128 sube el IC de -0.195 a +0.309 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=61). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.5959 sube el IC de +0.149 a +0.247 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=535). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3707 sube el IC de +0.245 a +0.276 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=1339). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de -0.190 a +0.234 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=62). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3529 sube el IC de -0.041 a +0.292 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=589). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.209 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.1376 sube el IC de -0.026 a +0.314 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=585). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_YES, IBS > 0.8434 sube el IC de +0.080 a +0.342 en UPDOWN_GBM_ETH_15M_HORA7 (n=17). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_YES, IBS > 0.8434 sube el IC de +0.080 a +0.342 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=17). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8393 sube el IC de +0.291 a +0.319 en UPDOWN_GBM_IBS_ALTO (n=1098). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8303 sube el IC de +0.289 a +0.315 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=588). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8489 sube el IC de +0.293 a +0.320 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=510). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7863 sube el IC de +0.364 a +0.401 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=641). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8048 sube el IC de +0.362 a +0.392 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=330). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7485 sube el IC de +0.365 a +0.410 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=311). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1947 | +0.090 | +214.59€ | 1 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1947 | +0.090 | +214.59€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1555 | +0.093 | +185.86€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1555 | +0.093 | +185.86€ | 0 | 9 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 284 | +0.070 | +11.30€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 284 | +0.070 | +11.30€ | 5 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 77 | +0.108 | +17.77€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 77 | +0.108 | +17.77€ | 0 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 707 | -0.002 | +79.11€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 707 | -0.002 | +79.11€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE | 5 | +0.018 | +2.77€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE#15min | 5 | +0.018 | +2.77€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 518 | -0.033 | +43.67€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 518 | -0.033 | +43.67€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 148 | +0.093 | +27.91€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 148 | +0.093 | +27.91€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 36 | +0.026 | +4.76€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 36 | +0.026 | +4.76€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 40772 | -0.080 | -5030.78€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 2275 | +0.038 | -260.45€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 38497 | -0.087 | -4770.32€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4522 | -0.114 | -779.00€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4522 | -0.114 | -779.00€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 2275 | +0.038 | -260.45€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 2275 | +0.038 | -260.45€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 4386 | -0.106 | -879.02€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 4386 | -0.106 | -879.02€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 10875 | -0.019 | -1007.48€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 10875 | -0.019 | -1007.48€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 10773 | -0.103 | -787.47€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 10773 | -0.103 | -787.47€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 7941 | -0.132 | -1317.35€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 7941 | -0.132 | -1317.35€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 36066 | -0.015 | +3302.30€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 9338 | +0.005 | +1658.77€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 26728 | -0.022 | +1643.54€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 36066 | -0.015 | +3302.30€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 9338 | +0.005 | +1658.77€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 26728 | -0.022 | +1643.54€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 148391 | +0.115 | -5973.87€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 18895 | +0.182 | -583.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 654 | -0.014 | -68.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 119990 | +0.106 | -4995.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 8852 | +0.099 | -325.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 19894 | +0.107 | -1231.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 61 | -0.151 | +10.95€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 19818 | +0.109 | -1230.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 28678 | +0.128 | -441.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5232 | +0.187 | -187.47€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 19879 | +0.120 | -121.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 3525 | +0.082 | -110.82€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 19949 | +0.100 | -1372.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 75 | -0.123 | -6.95€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 19859 | +0.101 | -1354.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 31572 | +0.124 | -591.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 8158 | +0.178 | -156.63€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 20153 | +0.107 | -371.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 3249 | +0.100 | -54.30€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 28382 | +0.115 | -1405.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 5300 | +0.197 | -248.39€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 557 | +0.019 | -14.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 20447 | +0.095 | -981.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 2078 | +0.127 | -160.61€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#XRP | 19916 | +0.106 | -931.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 69 | -0.091 | +4.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 19834 | +0.107 | -936.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 23894 | +0.198 | -1414.21€ | 2 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 23894 | +0.198 | -1414.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 5433 | +0.180 | -450.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 5433 | +0.180 | -450.91€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 3073 | +0.204 | -64.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 3073 | +0.204 | -64.46€ | 3 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 5370 | +0.181 | -421.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 5370 | +0.181 | -421.27€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 4651 | +0.248 | -155.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 4651 | +0.248 | -155.43€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 5288 | +0.189 | -335.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 5288 | +0.189 | -335.89€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 1046 | +0.426 | -38.28€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 1046 | +0.426 | -38.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 412 | +0.432 | -9.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 412 | +0.432 | -9.38€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE#15min | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 413 | +0.432 | -8.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 413 | +0.432 | -8.03€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 207 | +0.400 | -17.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 207 | +0.400 | -17.00€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 83601 | +0.202 | -5910.94€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 83601 | +0.202 | -5910.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 14359 | +0.186 | -1465.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 14359 | +0.186 | -1465.52€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 13502 | +0.225 | -452.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 13502 | +0.225 | -452.50€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 14316 | +0.182 | -1486.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 14316 | +0.182 | -1486.53€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 13587 | +0.220 | -506.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 13587 | +0.220 | -506.37€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 13871 | +0.202 | -900.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 13871 | +0.202 | -900.69€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 13966 | +0.198 | -1099.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 13966 | +0.198 | -1099.34€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 32009 | +0.116 | +168.39€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 32009 | +0.116 | +168.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 15914 | +0.119 | +158.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 15914 | +0.119 | +158.83€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 16095 | +0.113 | +9.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 16095 | +0.113 | +9.55€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 2119 | +0.293 | -2.51€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 2119 | +0.293 | -2.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 973 | +0.281 | -24.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 973 | +0.281 | -24.02€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 1026 | +0.298 | +15.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 1026 | +0.298 | +15.39€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 120 | +0.352 | +6.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 120 | +0.352 | +6.11€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 975 | +0.442 | +4.37€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 975 | +0.442 | +4.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 475 | +0.435 | -5.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 475 | +0.435 | -5.55€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 454 | +0.450 | +9.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 454 | +0.450 | +9.36€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 46 | +0.396 | +0.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 46 | +0.396 | +0.55€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1680 | +0.072 | -64.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 647 | +0.050 | -54.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 1033 | +0.086 | -10.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 74 | +0.118 | +4.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 74 | +0.118 | +4.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1291 | +0.080 | -25.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 258 | +0.058 | -15.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 1033 | +0.086 | -10.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 315 | +0.027 | -43.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 315 | +0.027 | -43.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 63389 | +0.100 | -1633.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 5121 | +0.089 | +37.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 58268 | +0.101 | -1671.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 34854 | +0.105 | -422.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 5121 | +0.089 | +37.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 29733 | +0.108 | -460.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 13071 | +0.108 | -89.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 13071 | +0.108 | -89.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 15464 | +0.083 | -1121.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 15464 | +0.083 | -1121.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 897 | +0.193 | -109.11€ | 4 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 897 | +0.193 | -109.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 897 | +0.193 | -109.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 897 | +0.193 | -109.11€ | 4 | 4 |
| ✅ GBM_LATE_15M | 43490 | +0.095 | +22845.09€ | 0 | 20 |
| ✅ GBM_LATE_15M#15min | 43490 | +0.095 | +22845.09€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 7242 | +0.217 | +6002.22€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 7242 | +0.217 | +6002.22€ | 0 | 22 |
| ✅ GBM_LATE_15M#BTC | 6537 | +0.180 | +5029.92€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 6537 | +0.180 | +5029.92€ | 0 | 23 |
| ✅ GBM_LATE_15M#DOGE | 7779 | +0.206 | +6076.67€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 7779 | +0.206 | +6076.67€ | 0 | 20 |
| ✅ GBM_LATE_15M#ETH | 6047 | +0.044 | +1721.97€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 6047 | +0.044 | +1721.97€ | 1 | 20 |
| ✅ GBM_LATE_15M#SOL | 6118 | -0.032 | +1285.77€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 6118 | -0.032 | +1285.77€ | 4 | 14 |
| ✅ GBM_LATE_15M#XRP | 9767 | -0.030 | +2728.53€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 9767 | -0.030 | +2728.53€ | 4 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 46733 | +0.085 | +25535.84€ | 0 | 19 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 46733 | +0.085 | +25535.84€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 9043 | +0.003 | +4592.09€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 9043 | +0.003 | +4592.09€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 9914 | +0.010 | +2378.75€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 9914 | +0.010 | +2378.75€ | 0 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 6474 | +0.280 | +6983.21€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 6474 | +0.280 | +6983.21€ | 0 | 23 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 8467 | +0.013 | +2103.96€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 8467 | +0.013 | +2103.96€ | 1 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 7418 | +0.039 | +3076.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 7418 | +0.039 | +3076.08€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 5417 | +0.305 | +6401.74€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 5417 | +0.305 | +6401.74€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 34433 | +0.181 | +28028.41€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 34433 | +0.181 | +28028.41€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 5227 | +0.231 | +4680.42€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 5227 | +0.231 | +4680.42€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 5419 | +0.149 | +4021.13€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 5419 | +0.149 | +4021.13€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 5525 | +0.224 | +4774.22€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 5525 | +0.224 | +4774.22€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 5840 | +0.139 | +4462.70€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 5840 | +0.139 | +4462.70€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 6465 | +0.126 | +4848.23€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 6465 | +0.126 | +4848.23€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 5957 | +0.227 | +5241.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 5957 | +0.227 | +5241.71€ | 0 | 25 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 9381 | +0.134 | +4593.85€ | 0 | 17 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 9381 | +0.134 | +4593.85€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 405 | +0.154 | +252.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 405 | +0.154 | +252.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 2733 | +0.143 | +1543.60€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 2733 | +0.143 | +1543.60€ | 0 | 21 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 467 | +0.150 | +239.09€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 467 | +0.150 | +239.09€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 2793 | +0.139 | +1345.75€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 2793 | +0.139 | +1345.75€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 2356 | +0.111 | +930.95€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 2356 | +0.111 | +930.95€ | 0 | 16 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 627 | +0.133 | +281.63€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 627 | +0.133 | +281.63€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO | 43648 | +0.186 | +35058.32€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#15min | 43648 | +0.186 | +35058.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 6912 | +0.243 | +6475.54€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 6912 | +0.243 | +6475.54€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 6811 | +0.148 | +4680.54€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 6811 | +0.148 | +4680.54€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 7391 | +0.234 | +6621.66€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 7391 | +0.234 | +6621.66€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 7206 | +0.139 | +5149.92€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 7206 | +0.139 | +5149.92€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 7713 | +0.121 | +5336.61€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 7713 | +0.121 | +5336.61€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 7615 | +0.232 | +6794.04€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 7615 | +0.232 | +6794.04€ | 0 | 20 |
| ✅ GBM_LATE_5M | 11990 | +0.203 | +9401.62€ | 1 | 30 |
| ✅ GBM_LATE_5M#5min | 11990 | +0.203 | +9401.62€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 986 | +0.243 | +920.10€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 986 | +0.243 | +920.10€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 2783 | +0.207 | +2383.92€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 2783 | +0.207 | +2383.92€ | 0 | 26 |
| ✅ GBM_LATE_5M#DOGE | 1167 | +0.196 | +861.83€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1167 | +0.196 | +861.83€ | 0 | 19 |
| ✅ GBM_LATE_5M#ETH | 3345 | +0.193 | +2357.45€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 3345 | +0.193 | +2357.45€ | 0 | 26 |
| ✅ GBM_LATE_5M#SOL | 1786 | +0.195 | +1380.79€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 1786 | +0.195 | +1380.79€ | 0 | 27 |
| ✅ GBM_LATE_5M#XRP | 1923 | +0.208 | +1497.52€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1923 | +0.208 | +1497.52€ | 0 | 0 |
| ✅ GBM_LATE_60M | 3601 | +0.065 | +1139.24€ | 0 | 8 |
| ✅ GBM_LATE_60M#60min | 3601 | +0.065 | +1139.24€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 1327 | +0.082 | +473.50€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 1327 | +0.082 | +473.50€ | 0 | 6 |
| ✅ GBM_LATE_60M#ETH | 1165 | +0.066 | +380.03€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 1165 | +0.066 | +380.03€ | 0 | 8 |
| ✅ GBM_LATE_60M#SOL | 1109 | +0.045 | +285.71€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 1109 | +0.045 | +285.71€ | 1 | 12 |
| 🚫 GBM_LATE_60M_FADE | 584 | -0.242 | -20.70€ | 9 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 584 | -0.242 | -20.70€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 218 | -0.245 | -13.71€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 218 | -0.245 | -13.71€ | 3 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 207 | -0.227 | -0.97€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 207 | -0.227 | -0.97€ | 6 | 1 |
| 🚫 GBM_LATE_60M_FADE#SOL | 159 | -0.252 | -6.01€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 159 | -0.252 | -6.01€ | 7 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 1565 | +0.085 | +398.09€ | 1 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 1565 | +0.085 | +398.09€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 620 | +0.080 | +148.97€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 620 | +0.080 | +148.97€ | 1 | 12 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 558 | +0.057 | +84.74€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 558 | +0.057 | +84.74€ | 2 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 387 | +0.132 | +164.38€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 387 | +0.132 | +164.38€ | 3 | 10 |
| ✅ LATE_WINDOW_5MIN | 167 | +0.281 | +166.63€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 167 | +0.281 | +166.63€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 167 | +0.281 | +166.63€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 167 | +0.281 | +166.63€ | 1 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 3456 | +0.103 | +862.23€ | 0 | 1 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 3456 | +0.103 | +862.23€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 3456 | +0.103 | +862.23€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 3456 | +0.103 | +862.23€ | 0 | 1 |
| ✅ LIQUIDACIONES_15M | 557 | -0.037 | -15.27€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 557 | -0.037 | -15.27€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 159 | -0.003 | +4.85€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 159 | -0.003 | +4.85€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 110 | -0.018 | -1.38€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 110 | -0.018 | -1.38€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 207 | -0.012 | -1.88€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 207 | -0.012 | -1.88€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M | 3775 | +0.017 | +89.38€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 3775 | +0.017 | +89.38€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 183 | +0.024 | -1.79€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 183 | +0.024 | -1.79€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 795 | +0.008 | +29.93€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 795 | +0.008 | +29.93€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE | 207 | -0.012 | -4.18€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 207 | -0.012 | -4.18€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 1380 | +0.027 | +34.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1380 | +0.027 | +34.16€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 758 | +0.012 | +2.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 758 | +0.012 | +2.16€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 452 | +0.018 | +29.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 452 | +0.018 | +29.11€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 1790 | -0.041 | -31.28€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1790 | -0.041 | -31.28€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 519 | -0.032 | -12.62€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 519 | -0.032 | -12.62€ | 6 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 615 | -0.017 | +5.05€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 615 | -0.017 | +5.05€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 656 | -0.071 | -23.71€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 656 | -0.071 | -23.71€ | 6 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 9198 | -0.027 | +7.80€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 4371 | -0.037 | -92.66€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 4827 | -0.018 | +100.47€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 281 | -0.030 | -5.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 143 | -0.010 | +2.73€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 138 | -0.050 | -7.84€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 2296 | -0.021 | +6.01€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 1094 | -0.029 | -14.95€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 1202 | -0.014 | +20.96€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 995 | -0.026 | +10.70€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 501 | -0.045 | -15.88€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 494 | -0.006 | +26.59€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 2022 | -0.040 | -54.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 938 | -0.052 | -56.64€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 1084 | -0.029 | +2.20€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 1801 | -0.016 | +47.64€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 862 | -0.028 | +2.73€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 939 | -0.005 | +44.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 1803 | -0.032 | +3.00€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 833 | -0.040 | -10.64€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 970 | -0.025 | +13.64€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 51121 | -0.000 | +2585.48€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 51121 | -0.000 | +2585.48€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 9224 | +0.026 | +1190.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 9224 | +0.026 | +1190.60€ | 2 | 5 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 7346 | -0.033 | -90.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 7346 | -0.033 | -90.50€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 9329 | +0.025 | +977.43€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 9329 | +0.025 | +977.43€ | 1 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 7193 | -0.048 | -150.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 7193 | -0.048 | -150.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 8646 | -0.004 | +235.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 8646 | -0.004 | +235.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 9383 | +0.015 | +423.15€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 9383 | +0.015 | +423.15€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 6682 | -0.058 | -156.03€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 6682 | -0.058 | -156.03€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1225 | -0.000 | -15.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1225 | -0.000 | -15.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1750 | -0.076 | -41.08€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1750 | -0.076 | -41.08€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 57 | -0.059 | -2.86€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 57 | -0.059 | -2.86€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 776 | -0.119 | -33.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 776 | -0.119 | -33.30€ | 5 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 2017 | -0.073 | -37.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 2017 | -0.073 | -37.98€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 857 | -0.016 | -25.51€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 857 | -0.016 | -25.51€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3368 | +0.004 | -1.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3368 | +0.004 | -1.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 131 | -0.034 | -0.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 131 | -0.034 | -0.72€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 192 | +0.015 | +1.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 192 | +0.015 | +1.02€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 139 | -0.004 | -2.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 139 | -0.004 | -2.34€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1325 | +0.006 | +6.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1325 | +0.006 | +6.88€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1391 | +0.007 | -0.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1391 | +0.007 | -0.19€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 190 | -0.010 | -6.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 190 | -0.010 | -6.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 126626 | -0.077 | +1652.08€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 126626 | -0.077 | +1652.08€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 22051 | -0.077 | +1084.14€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 22051 | -0.077 | +1084.14€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 19072 | -0.101 | -1013.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 19072 | -0.101 | -1013.97€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 22325 | -0.068 | +1197.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 22325 | -0.068 | +1197.31€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 18616 | -0.097 | -591.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 18616 | -0.097 | -591.71€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 22651 | -0.057 | +318.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 22651 | -0.057 | +318.78€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 21911 | -0.068 | +657.53€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 21911 | -0.068 | +657.53€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 8785 | -0.034 | -186.66€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 8785 | -0.034 | -186.66€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 1001 | -0.017 | -18.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 1001 | -0.017 | -18.91€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1990 | -0.047 | -26.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1990 | -0.047 | -26.24€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1008 | -0.022 | -32.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1008 | -0.022 | -32.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2602 | -0.026 | -42.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2602 | -0.026 | -42.21€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1213 | -0.057 | -30.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1213 | -0.057 | -30.56€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 971 | -0.031 | -35.95€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 971 | -0.031 | -35.95€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1705 | +0.123 | +693.52€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#5min | 1569 | +0.129 | +680.93€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 368 | +0.135 | +181.26€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 368 | +0.135 | +181.26€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#DOGE | 323 | +0.118 | +112.20€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 323 | +0.118 | +112.20€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#ETH | 310 | +0.138 | +152.62€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 310 | +0.138 | +152.62€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#SOL | 275 | +0.150 | +149.73€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 275 | +0.150 | +149.73€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#XRP | 293 | +0.100 | +85.11€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 293 | +0.100 | +85.11€ | 0 | 3 |
| ✅ ORDER_FLOW_5M_REACTIVO | 1510 | -0.018 | -28.56€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 1510 | -0.018 | -28.56€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 293 | -0.005 | +7.03€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 293 | -0.005 | +7.03€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 263 | -0.021 | -2.47€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 263 | -0.021 | -2.47€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 391 | -0.047 | -33.57€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 391 | -0.047 | -33.57€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 319 | +0.002 | -1.04€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 319 | +0.002 | -1.04€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 244 | -0.008 | +1.49€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 244 | -0.008 | +1.49€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 918 | -0.075 | -51.04€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 428 | -0.114 | -81.18€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 332 | -0.144 | -68.58€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 96 | -0.010 | -12.59€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 323 | -0.032 | +23.57€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 232 | -0.021 | +26.03€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 91 | -0.059 | -2.46€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 167 | -0.056 | +6.57€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 136 | -0.065 | +2.18€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 31 | -0.015 | +4.39€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 700 | -0.088 | -40.37€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 218 | -0.032 | -10.67€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 1147 | -0.208 | -68.82€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC | 446 | -0.210 | -42.51€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#atexpiry | 389 | -0.214 | -42.28€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 57 | -0.178 | -0.23€ | 2 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 391 | -0.210 | -31.29€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 343 | -0.222 | -38.30€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 48 | -0.120 | +7.01€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 310 | -0.199 | +4.99€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 289 | -0.194 | +2.87€ | 5 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 21 | -0.239 | +2.12€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 1021 | -0.212 | -77.72€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 126 | -0.172 | +8.90€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 459 | +0.396 | +437.07€ | 0 | 13 |
| ✅ RESOLUTION_SNIPER#BTC | 69 | +0.162 | +55.45€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 69 | +0.162 | +55.45€ | 0 | 2 |
| ✅ RESOLUTION_SNIPER#ETH | 110 | +0.366 | +102.82€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 110 | +0.366 | +102.82€ | 0 | 8 |
| ✅ RESOLUTION_SNIPER#SOL | 280 | +0.461 | +278.80€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 280 | +0.461 | +278.80€ | 0 | 10 |
| ✅ RESOLUTION_SNIPER#sniper | 459 | +0.396 | +437.07€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 742 | +0.030 | +42.35€ | 2 | 2 |
| ✅ STREAK_FADE_15M#15min | 742 | +0.030 | +42.35€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 305 | +0.021 | +2.83€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 305 | +0.021 | +2.83€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 62 | +0.000 | -0.54€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 62 | +0.000 | -0.54€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 77 | -0.006 | +1.97€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 77 | -0.006 | +1.97€ | 2 | 0 |
| ✅ STREAK_FADE_15M#XRP | 298 | +0.053 | +38.10€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 298 | +0.053 | +38.10€ | 0 | 5 |
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
| ✅ STREAK_FADE_60M | 103 | -0.052 | -9.27€ | 6 | 0 |
| ✅ STREAK_FADE_60M#60min | 103 | -0.052 | -9.27€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 43 | -0.100 | -5.07€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 43 | -0.100 | -5.07€ | 4 | 0 |
| ✅ STREAK_FADE_60M#SOL | 60 | -0.016 | -4.20€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 60 | -0.016 | -4.20€ | 0 | 2 |
| ✅ STREAK_MOM_5M | 10998 | +0.016 | +83.37€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 10998 | +0.016 | +83.37€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2811 | +0.020 | +29.13€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2811 | +0.020 | +29.13€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2876 | +0.017 | +32.42€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2876 | +0.017 | +32.42€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2889 | +0.009 | -1.46€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2889 | +0.009 | -1.46€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2422 | +0.016 | +23.28€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2422 | +0.016 | +23.28€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 10011 | +0.013 | -52.98€ | 2 | 0 |
| ✅ STRUCT_NO_15M#15min | 10011 | +0.013 | -52.98€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 4098 | +0.017 | -11.39€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 4098 | +0.017 | -11.39€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3618 | +0.011 | -28.16€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3618 | +0.011 | -28.16€ | 2 | 0 |
| ✅ STRUCT_NO_15M#SOL | 2295 | +0.009 | -13.44€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 2295 | +0.009 | -13.44€ | 1 | 0 |
| ✅ UPDOWN_GBM | 78596 | +0.054 | +6962.51€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 19516 | +0.083 | +4268.96€ | 0 | 12 |
| ✅ UPDOWN_GBM#240min | 2514 | +0.004 | +23.42€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 51629 | +0.050 | +2578.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 4660 | +0.007 | +92.73€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 6851 | +0.089 | +1075.72€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1576 | +0.156 | +698.08€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 77 | -0.006 | -0.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 5198 | +0.070 | +378.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 17091 | +0.055 | +1463.12€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 2549 | +0.088 | +620.59€ | 0 | 11 |
| ✅ UPDOWN_GBM#BTC#240min | 680 | +0.009 | +10.63€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 11688 | +0.061 | +763.78€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 2074 | +0.004 | +64.56€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 100 | -0.069 | +3.57€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 8599 | +0.070 | +915.50€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1555 | +0.147 | +610.96€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 78 | +0.013 | -1.79€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 6966 | +0.054 | +306.33€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 18140 | +0.045 | +1174.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 4644 | +0.066 | +675.75€ | 0 | 11 |
| ✅ UPDOWN_GBM#ETH#240min | 662 | +0.006 | +15.77€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 11105 | +0.044 | +462.48€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 1636 | +0.010 | +18.16€ | 1 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 93 | -0.100 | +2.72€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 17284 | +0.033 | +864.04€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 4931 | +0.034 | +407.00€ | 0 | 3 |
| ✅ UPDOWN_GBM#SOL#240min | 629 | -0.009 | -0.27€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 10692 | +0.038 | +452.54€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 950 | +0.006 | +10.01€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#daily | 82 | -0.131 | -5.24€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 10629 | +0.065 | +1471.10€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 4261 | +0.103 | +1256.59€ | 0 | 11 |
| ✅ UPDOWN_GBM#XRP#240min | 388 | +0.010 | -0.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 5980 | +0.041 | +214.58€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 275 | -0.099 | +1.05€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 854 | +0.364 | +312.74€ | 0 | 9 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 854 | +0.364 | +312.74€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 440 | +0.362 | +151.21€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 440 | +0.362 | +151.21€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 414 | +0.365 | +161.54€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 414 | +0.365 | +161.54€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO | 20250 | -0.025 | +4671.42€ | 3 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 20250 | -0.025 | +4671.42€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1718 | -0.056 | +502.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1718 | -0.056 | +502.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 3623 | -0.112 | +125.76€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 3623 | -0.112 | +125.76€ | 5 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 948 | +0.216 | +770.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 948 | +0.216 | +770.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 2498 | +0.218 | +1621.13€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 2498 | +0.218 | +1621.13€ | 1 | 18 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 5802 | -0.067 | +667.22€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 5802 | -0.067 | +667.22€ | 5 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 5661 | -0.065 | +984.03€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 5661 | -0.065 | +984.03€ | 2 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 236 | +0.050 | +14.42€ | 0 | 5 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 236 | +0.050 | +14.42€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 236 | +0.050 | +14.42€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 236 | +0.050 | +14.42€ | 0 | 5 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1464 | +0.291 | +1252.27€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1464 | +0.291 | +1252.27€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 784 | +0.289 | +638.48€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 784 | +0.289 | +638.48€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 680 | +0.293 | +613.78€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 680 | +0.293 | +613.78€ | 0 | 9 |
| ✅ UPDOWN_OU_5M | 819 | -0.114 | -85.20€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#5min | 819 | -0.114 | -85.20€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 250 | -0.083 | -19.12€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 250 | -0.083 | -19.12€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 88 | -0.167 | -9.66€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 88 | -0.167 | -9.66€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 98 | -0.190 | -7.06€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 98 | -0.190 | -7.06€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 38 | -0.175 | -6.61€ | 2 | 0 |
| ✅ WEEKLY_PRICE | 3691 | +0.304 | +1736.67€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 1360 | +0.257 | +170.41€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 1419 | +0.299 | +634.07€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 912 | +0.380 | +932.19€ | 0 | 1 |