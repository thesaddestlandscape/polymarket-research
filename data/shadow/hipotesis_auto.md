# Hipótesis automáticas — 2026-10-22 05:03 UTC
_Generado por shadow_postmortem.py sobre 1003544 resoluciones (PNL=+131210.42€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.495` → IC=-0.255 (n=194)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.114 (n=628)

- **PATRÓN** `py_entrada` > `0.515` → IC=+0.233 (n=797)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.515 (IC base=+0.136)

- **PATRÓN** `n_total_lado` > `65.0` → IC=+0.181 (n=286)

  - _Acción_: Kelly boost +0.90€ cuando `n_total_lado` > 65.0 (IC base=+0.136)

- **PATRÓN** `banda_hit_calibrado` > `0.6242` → IC=+0.264 (n=566)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6242 (IC base=+0.136)

- **PATRÓN** `banda_z` > `9.122` → IC=+0.208 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.122 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.165 (n=311)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 17.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.138 (n=564)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 11.0 (IC base=+0.136)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=923)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `98.0` → IC=+0.152 (n=466)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 98.0 (IC base=+0.136)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **PATRÓN** `py_entrada` > `0.515` → IC=+0.230 (n=686)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.515 (IC base=+0.141)

- **PATRÓN** `n_total_lado` > `69.0` → IC=+0.200 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 69.0 (IC base=+0.141)

- **PATRÓN** `banda_hit_calibrado` > `0.6164` → IC=+0.256 (n=478)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6164 (IC base=+0.141)

- **PATRÓN** `banda_z` > `9.551` → IC=+0.205 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.551 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.176 (n=260)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.141)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.149 (n=824)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.141)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.152 (n=429)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 100.0 (IC base=+0.141)

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
- **FILTRO** `restante_s_al_confirmar` < `142.26` → IC=-0.199 (n=10205)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 142.26
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=30616)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `128.62` → IC=-0.257 (n=1130)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 128.62
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=3392)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `122.31` → IC=-0.286 (n=1099)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 122.31
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=3297)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `167.49` → IC=-0.202 (n=2697)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 167.49
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=8094)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `133.16` → IC=-0.277 (n=1986)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 133.16
  - _Potencial_: sin este filtro IC_bueno=-0.084 (n=5961)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.214 (n=22081)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.107)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.133 (n=4370)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `9057.2294` → IC=+0.173 (n=1984)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 9057.2294 (IC base=+0.107)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.129 (n=18817)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.129 (n=33766)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 11.0 (IC base=+0.125)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.227 (n=17614)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.149 (n=7272)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `7052.6142` → IC=+0.157 (n=2810)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 7052.6142 (IC base=+0.125)

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

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.187 (n=2000)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 17.0 (IC base=+0.183)

- **PATRÓN** `py_entrada` < `0.285` → IC=+0.317 (n=895)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.285 (IC base=+0.183)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.186 (n=2563)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.01 (IC base=+0.183)

- **PATRÓN** `libro_liquidez` > `16179.5763` → IC=+0.192 (n=661)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 16179.5763 (IC base=+0.183)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.61` → IC=+0.172 (n=476)

  - _Acción_: Kelly boost +0.86€ cuando `py_entrada` > 0.61 (IC base=+0.082)

- **PATRÓN** `libro_liquidez` > `6840.9445` → IC=+0.161 (n=125)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 6840.9445 (IC base=+0.082)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.136 (n=1139)

  - _Acción_: Kelly boost +0.68€ cuando `py_entrada` < 0.44 (IC base=+0.081)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.167 (n=4282)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.160)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.162 (n=3636)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 15.0 (IC base=+0.160)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.372 (n=1412)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.160)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.228 (n=792)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.210)

- **PATRÓN** `py_entrada` < `0.265` → IC=+0.348 (n=741)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.265 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.213 (n=2226)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.210)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.144 (n=1083)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.143)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.149 (n=923)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 15.0 (IC base=+0.143)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.263 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.143)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.147 (n=847)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.01 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `2209.7061` → IC=+0.160 (n=469)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 2209.7061 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.162 (n=152)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.069)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.254 (n=853)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.224)

- **PATRÓN** `py_entrada` > `0.83` → IC=+0.420 (n=1170)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.83 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.151 (n=1294)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 7.0 (IC base=+0.149)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.155 (n=683)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 7.0 (IC base=+0.149)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.285 (n=646)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.149)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=858)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.149)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `9.0` → IC=+0.155 (n=326)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 9.0 (IC base=+0.137)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.352 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.137)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.128 (n=280)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.04 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `1081.2334` → IC=+0.127 (n=261)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 1081.2334 (IC base=+0.137)

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
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.201)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.203 (n=15853)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.201)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.236 (n=7682)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.201)

- **PATRÓN** `libro_liquidez` > `4837.3339` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4837.3339 (IC base=+0.201)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.183 (n=2039)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 15.0 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.181 (n=4292)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 18.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.183 (n=4223)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` < 0.73 (IC base=+0.180)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.182 (n=3515)

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

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.227 (n=2342)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.223)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.304 (n=770)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.223)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.189 (n=4231)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.183 (n=3599)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 15.0 (IC base=+0.182)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.182 (n=4404)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` < 0.73 (IC base=+0.182)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.188 (n=3319)

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
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 5.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.193 (n=3543)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.189)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.194 (n=3064)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.71 (IC base=+0.189)

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

- **PATRÓN** `libro_liquidez` > `15539.3062` → IC=+0.433 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15539.3062 (IC base=+0.432)

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

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.208 (n=24329)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.202)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.247 (n=24490)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.202)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.196 (n=3607)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 18.0 (IC base=+0.186)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.187 (n=7744)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 12.0 (IC base=+0.186)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.200 (n=10891)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.71 (IC base=+0.186)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.227 (n=5078)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.227 (n=4973)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.225)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.285 (n=3546)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.225)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.189 (n=4168)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 17.0 (IC base=+0.182)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.212 (n=5535)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.182)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.835` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.835
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.233 (n=3405)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.221)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.223 (n=3900)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.221)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.276 (n=3453)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.221)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.209 (n=3475)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.260 (n=3609)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.209 (n=4042)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.197)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.248 (n=4231)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.197)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.192 (n=8844)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.139 (n=8653)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.96 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `3.76` → IC=+0.136 (n=10589)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 3.76 (IC base=+0.116)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.196 (n=4371)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.119)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.142 (n=4429)

  - _Acción_: Kelly boost +0.71€ cuando `restante_min` > 4.95 (IC base=+0.119)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.129 (n=5310)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 7.0 (IC base=+0.119)

- **PATRÓN** `lag_apertura_s` < `2.75` → IC=+0.146 (n=3988)

  - _Acción_: Kelly boost +0.73€ cuando `lag_apertura_s` < 2.75 (IC base=+0.119)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.189 (n=4473)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` < 0.38 (IC base=+0.114)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.135 (n=4706)

  - _Acción_: Kelly boost +0.67€ cuando `restante_min` > 4.96 (IC base=+0.114)

- **PATRÓN** `lag_apertura_s` < `3.33` → IC=+0.133 (n=5328)

  - _Acción_: Kelly boost +0.67€ cuando `lag_apertura_s` < 3.33 (IC base=+0.114)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.301 (n=1689)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.293)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.381 (n=579)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.293)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.288 (n=768)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.280)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.354 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.280)

- **PATRÓN** `libro_liquidez` > `4530.441` → IC=+0.285 (n=487)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4530.441 (IC base=+0.280)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.321 (n=546)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.297)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.300 (n=800)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.297)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.392 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.297)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.297 (n=905)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.297)

- **PATRÓN** `libro_liquidez` > `2113.1713` → IC=+0.315 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2113.1713 (IC base=+0.297)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4762` → IC=+0.140 (n=13630)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.4762 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.126 (n=13770)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 6.0 (IC base=+0.122)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.124 (n=9511)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 12.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` > `0.3785` → IC=+0.166 (n=13629)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.3785 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` > `0.7907` → IC=+0.275 (n=784)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7907 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` < `0.373` → IC=+0.260 (n=3814)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.373 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.898` → IC=+0.192 (n=5153)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 5.898 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` < `1.2039` → IC=+0.259 (n=3969)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2039 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` > `0.618` → IC=+0.265 (n=3969)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.618 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` > `0.3026` → IC=+0.243 (n=1389)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3026 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` > `2.3483` → IC=+0.229 (n=4402)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3483 (IC base=+0.122)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.125 (n=11390)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.02 (IC base=+0.122)

- **PATRÓN** `ibs_20min` < `0.6849` → IC=+0.130 (n=19068)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` < 0.6849 (IC base=+0.076)

- **PATRÓN** `dist_vwap_pct` > `0.6016` → IC=+0.188 (n=1160)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.6016 (IC base=+0.076)

- **PATRÓN** `dist_vwap_pct` < `0.1563` → IC=+0.187 (n=6155)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` < 0.1563 (IC base=+0.076)

- **PATRÓN** `volumen_regimen` < `0.6958` → IC=+0.188 (n=2879)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 0.6958 (IC base=+0.076)

- **PATRÓN** `volumen_regimen` > `1.0507` → IC=+0.184 (n=2966)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` > 1.0507 (IC base=+0.076)

- **PATRÓN** `volumen_pendiente_norm` > `0.2959` → IC=+0.233 (n=1632)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2959 (IC base=+0.076)

- **PATRÓN** `volumen_spike_ratio` > `2.6807` → IC=+0.207 (n=3712)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6807 (IC base=+0.076)

- **PATRÓN** `ballena_activa_n` < `107.0` → IC=+0.222 (n=10993)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 107.0 (IC base=+0.076)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.208 (n=992)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.200)

- **PATRÓN** `drift_60min` |x|≤ `0.3473` → IC=+0.205 (n=2966)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3473 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.212 (n=1446)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.200)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.203 (n=1984)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.200)

- **PATRÓN** `ibs_20min` > `0.9823` → IC=+0.280 (n=1345)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9823 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.835` → IC=+0.285 (n=1299)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.835 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` > `0.2341` → IC=+0.249 (n=521)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2341 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` > `1.4408` → IC=+0.203 (n=2829)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4408 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.215 (n=3193)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.200)

- **PATRÓN** `libro_liquidez` > `2074.2472` → IC=+0.207 (n=989)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2074.2472 (IC base=+0.200)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.217 (n=1805)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 14.0 (IC base=+0.200)

- **PATRÓN** `sigma_h` < `0.0086` → IC=+0.239 (n=2488)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0086 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.0871` → IC=+0.271 (n=828)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0871 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.256 (n=910)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` < `0.5324` → IC=+0.259 (n=2482)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5324 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` < `0.0942` → IC=+0.240 (n=2225)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0942 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.2886` → IC=+0.263 (n=336)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2886 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` < `1.4413` → IC=+0.243 (n=781)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4413 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `2.6765` → IC=+0.245 (n=781)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6765 (IC base=+0.237)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.241 (n=2801)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.237)

- **PATRÓN** `libro_liquidez` > `1615.42` → IC=+0.247 (n=2217)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1615.42 (IC base=+0.237)

- **PATRÓN** `ballena_activa_n` < `9.0` → IC=+0.240 (n=1086)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 9.0 (IC base=+0.237)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.239 (n=1069)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.229)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.231 (n=1102)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.229)

- **PATRÓN** `drift_60min` |x|≤ `0.1057` → IC=+0.261 (n=1069)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1057 (IC base=+0.229)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.241 (n=2545)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.229)

- **PATRÓN** `ibs_20min` > `0.9483` → IC=+0.281 (n=810)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9483 (IC base=+0.229)

- **PATRÓN** `dist_vwap_pct` > `0.1308` → IC=+0.237 (n=1315)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1308 (IC base=+0.229)

- **PATRÓN** `dist_vwap_pct` < `0.341` → IC=+0.230 (n=2343)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.341 (IC base=+0.229)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.335` → IC=+0.266 (n=366)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.335 (IC base=+0.229)

- **PATRÓN** `volumen_regimen` < `1.2326` → IC=+0.229 (n=2430)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2326 (IC base=+0.229)

- **PATRÓN** `volumen_regimen` > `0.6213` → IC=+0.234 (n=2432)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6213 (IC base=+0.229)

- **PATRÓN** `volumen_pendiente_norm` > `0.2776` → IC=+0.267 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2776 (IC base=+0.229)

- **PATRÓN** `volumen_spike_ratio` > `2.4426` → IC=+0.258 (n=798)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4426 (IC base=+0.229)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.152 (n=2492)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0058 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.0756` → IC=+0.170 (n=829)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.0756 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.156 (n=941)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 17.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` < `0.7272` → IC=+0.177 (n=2486)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.7272 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` < `0.1366` → IC=+0.153 (n=2312)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.1366 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.075` → IC=+0.151 (n=402)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 11.075 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.188` → IC=+0.141 (n=2269)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 4.188 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `1.2046` → IC=+0.141 (n=2486)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 1.2046 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` > `0.0951` → IC=+0.160 (n=905)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.0951 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` < `2.4535` → IC=+0.145 (n=2366)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 2.4535 (IC base=+0.133)

- **PATRÓN** `ballena_activa_n` < `216.0` → IC=+0.175 (n=1013)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 216.0 (IC base=+0.133)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0121` → IC=+0.222 (n=1027)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0121 (IC base=+0.195)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.202 (n=3230)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.195)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.269 (n=1182)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.195)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.236` → IC=+0.274 (n=648)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.236 (IC base=+0.195)

- **PATRÓN** `volumen_pendiente_norm` < `0.0975` → IC=+0.200 (n=2732)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0975 (IC base=+0.195)

- **PATRÓN** `volumen_pendiente_norm` > `0.3522` → IC=+0.214 (n=396)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3522 (IC base=+0.195)

- **PATRÓN** `volumen_spike_ratio` > `2.6984` → IC=+0.211 (n=1356)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6984 (IC base=+0.195)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.202 (n=3693)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.195)

- **PATRÓN** `libro_liquidez` > `1964.6432` → IC=+0.201 (n=1397)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1964.6432 (IC base=+0.195)

- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.223 (n=2439)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0106 (IC base=+0.217)

- **PATRÓN** `drift_60min` |x|≤ `0.1782` → IC=+0.232 (n=1218)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1782 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.244 (n=1041)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.217)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.218 (n=981)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.217)

- **PATRÓN** `ibs_20min` < `0.0185` → IC=+0.277 (n=922)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0185 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.379` → IC=+0.253 (n=334)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.379 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` > `0.3474` → IC=+0.258 (n=398)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3474 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` > `2.7325` → IC=+0.229 (n=1192)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7325 (IC base=+0.217)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.222 (n=1443)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.217)

- **PATRÓN** `libro_liquidez` > `1952.96` → IC=+0.219 (n=1254)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1952.96 (IC base=+0.217)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.222 (n=2257)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 23.0 (IC base=+0.217)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.143 (n=152)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=3726)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.165 (n=547)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0037 (IC base=+0.055)

- **PATRÓN** `ibs_20min` > `0.9538` → IC=+0.232 (n=546)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9538 (IC base=+0.055)

- **PATRÓN** `dist_vwap_pct` > `0.1404` → IC=+0.335 (n=373)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1404 (IC base=+0.055)

- **PATRÓN** `dist_vwap_pct` < `0.5223` → IC=+0.333 (n=649)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5223 (IC base=+0.055)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.146` → IC=+0.191 (n=1180)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 5.146 (IC base=+0.055)

- **PATRÓN** `volumen_regimen` < `0.8578` → IC=+0.334 (n=413)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8578 (IC base=+0.055)

- **PATRÓN** `volumen_regimen` > `1.2247` → IC=+0.352 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2247 (IC base=+0.055)

- **PATRÓN** `volumen_pendiente_norm` < `0.1664` → IC=+0.328 (n=509)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1664 (IC base=+0.055)

- **PATRÓN** `volumen_pendiente_norm` > `0.2965` → IC=+0.349 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2965 (IC base=+0.055)

- **PATRÓN** `volumen_spike_ratio` < `1.4107` → IC=+0.352 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4107 (IC base=+0.055)

- **PATRÓN** `volumen_spike_ratio` > `2.2172` → IC=+0.329 (n=273)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2172 (IC base=+0.055)

- **PATRÓN** `ballena_activa_n` < `131.0` → IC=+0.336 (n=534)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 131.0 (IC base=+0.055)

- **PATRÓN** `ibs_20min` < `0.0929` → IC=+0.178 (n=970)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.0929 (IC base=+0.037)

- **PATRÓN** `dist_vwap_pct` > `0.3309` → IC=+0.148 (n=473)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.3309 (IC base=+0.037)

- **PATRÓN** `dist_vwap_pct` < `0.1314` → IC=+0.140 (n=1582)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.1314 (IC base=+0.037)

- **PATRÓN** `volumen_regimen` < `0.8409` → IC=+0.148 (n=1152)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.8409 (IC base=+0.037)

- **PATRÓN** `volumen_regimen` > `1.1669` → IC=+0.147 (n=576)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` > 1.1669 (IC base=+0.037)

- **PATRÓN** `volumen_pendiente_norm` > `0.2851` → IC=+0.200 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2851 (IC base=+0.037)

- **PATRÓN** `volumen_spike_ratio` < `1.7767` → IC=+0.141 (n=1104)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.7767 (IC base=+0.037)

- **PATRÓN** `volumen_spike_ratio` > `2.1533` → IC=+0.153 (n=751)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 2.1533 (IC base=+0.037)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.173 (n=105)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.072 (n=568)

- **FILTRO** `ibs_20min` < `0.2759` → IC=-0.194 (n=168)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2759
  - _Potencial_: sin este filtro IC_bueno=+0.110 (n=505)

- **FILTRO** `ibs_20min` > `0.2169` → IC=-0.132 (n=3656)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2169
  - _Potencial_: sin este filtro IC_bueno=+0.147 (n=1801)

- **FILTRO** `sigma_ewma_delta_pct` > `8.654` → IC=-0.237 (n=576)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.654
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=4881)

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

- **PATRÓN** `ibs_20min` < `0.2169` → IC=+0.147 (n=1801)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.2169 (IC base=-0.040)

- **PATRÓN** `dist_vwap_pct` > `0.1911` → IC=+0.280 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1911 (IC base=-0.040)

- **PATRÓN** `volumen_regimen` < `0.7052` → IC=+0.306 (n=328)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7052 (IC base=-0.040)

- **PATRÓN** `volumen_pendiente_norm` > `0.0806` → IC=+0.301 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0806 (IC base=-0.040)

- **PATRÓN** `volumen_spike_ratio` < `2.43` → IC=+0.301 (n=680)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.43 (IC base=-0.040)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6099` → IC=-0.181 (n=1002)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6099
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=3012)

- **FILTRO** `ibs_20min` < `0.7571` → IC=-0.150 (n=2649)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7571
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=1365)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.162 (n=968)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=3046)

- **FILTRO** `ibs_20min` > `0.75` → IC=-0.203 (n=1435)

  - _Acción_: SKIP cuando `ibs_20min` > 0.75
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=4338)

- **PATRÓN** `dist_vwap_pct` > `1.0882` → IC=+0.345 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0882 (IC base=-0.065)

- **PATRÓN** `dist_vwap_pct` < `0.2524` → IC=+0.305 (n=609)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2524 (IC base=-0.065)

- **PATRÓN** `volumen_regimen` < `1.1457` → IC=+0.299 (n=708)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1457 (IC base=-0.065)

- **PATRÓN** `volumen_regimen` > `0.704` → IC=+0.317 (n=632)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.704 (IC base=-0.065)

- **PATRÓN** `volumen_pendiente_norm` < `0.0995` → IC=+0.304 (n=665)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0995 (IC base=-0.065)

- **PATRÓN** `volumen_pendiente_norm` > `0.071` → IC=+0.305 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.071 (IC base=-0.065)

- **PATRÓN** `volumen_spike_ratio` < `1.4142` → IC=+0.318 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4142 (IC base=-0.065)

- **PATRÓN** `volumen_spike_ratio` > `1.8367` → IC=+0.306 (n=457)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8367 (IC base=-0.065)

- **PATRÓN** `dist_vwap_pct` > `0.8075` → IC=+0.286 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8075 (IC base=-0.005)

- **PATRÓN** `volumen_regimen` < `0.717` → IC=+0.259 (n=698)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.717 (IC base=-0.005)

- **PATRÓN** `volumen_regimen` > `1.0687` → IC=+0.288 (n=719)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0687 (IC base=-0.005)

- **PATRÓN** `volumen_pendiente_norm` > `0.1038` → IC=+0.284 (n=548)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1038 (IC base=-0.005)

- **PATRÓN** `volumen_spike_ratio` < `2.1803` → IC=+0.264 (n=1288)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1803 (IC base=-0.005)

- **PATRÓN** `volumen_spike_ratio` > `1.4298` → IC=+0.267 (n=1464)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4298 (IC base=-0.005)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.209 (n=5975)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0098 (IC base=+0.096)

- **PATRÓN** `ibs_20min` > `0.3184` → IC=+0.169 (n=17898)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` > 0.3184 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` > `0.9538` → IC=+0.301 (n=1336)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9538 (IC base=+0.096)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.592` → IC=+0.162 (n=8035)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 3.592 (IC base=+0.096)

- **PATRÓN** `volumen_regimen` < `1.172` → IC=+0.264 (n=6597)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.172 (IC base=+0.096)

- **PATRÓN** `volumen_regimen` > `0.6884` → IC=+0.270 (n=5893)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6884 (IC base=+0.096)

- **PATRÓN** `volumen_pendiente_norm` > `0.2399` → IC=+0.278 (n=1970)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2399 (IC base=+0.096)

- **PATRÓN** `volumen_spike_ratio` < `1.4603` → IC=+0.263 (n=3507)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4603 (IC base=+0.096)

- **PATRÓN** `volumen_spike_ratio` > `2.2738` → IC=+0.271 (n=4769)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2738 (IC base=+0.096)

- **PATRÓN** `ballena_activa_n` < `92.0` → IC=+0.296 (n=10117)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 92.0 (IC base=+0.096)

- **PATRÓN** `sigma_h` > `0.0093` → IC=+0.156 (n=5753)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0093 (IC base=+0.074)

- **PATRÓN** `ibs_20min` < `0.6578` → IC=+0.144 (n=17222)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.6578 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` < `0.2437` → IC=+0.266 (n=5394)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2437 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` < `0.7048` → IC=+0.264 (n=2390)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7048 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` > `1.1971` → IC=+0.268 (n=1810)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1971 (IC base=+0.074)

- **PATRÓN** `volumen_pendiente_norm` > `0.2944` → IC=+0.316 (n=1170)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2944 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` < `1.5796` → IC=+0.291 (n=3442)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5796 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` > `2.2668` → IC=+0.284 (n=3546)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2668 (IC base=+0.074)

- **PATRÓN** `ballena_activa_n` < `77.0` → IC=+0.295 (n=7765)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 77.0 (IC base=+0.074)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.581` → IC=-0.131 (n=2453)

  - _Acción_: SKIP cuando `ibs_20min` < 0.581
  - _Potencial_: sin este filtro IC_bueno=+0.191 (n=2454)

- **FILTRO** `ibs_20min` > `0.7399` → IC=-0.215 (n=1037)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7399
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=3118)

- **FILTRO** `sigma_ewma_delta_pct` > `4.353` → IC=-0.210 (n=912)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.353
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=3243)

- **PATRÓN** `ibs_20min` > `0.9217` → IC=+0.316 (n=1227)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9217 (IC base=+0.030)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.963` → IC=+0.216 (n=871)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.963 (IC base=+0.030)

- **PATRÓN** `volumen_pendiente_norm` > `0.2302` → IC=+0.303 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2302 (IC base=+0.030)

- **PATRÓN** `volumen_spike_ratio` < `1.4432` → IC=+0.252 (n=535)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4432 (IC base=+0.030)

- **PATRÓN** `volumen_spike_ratio` > `2.2557` → IC=+0.277 (n=728)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2557 (IC base=+0.030)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.283 (n=1091)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.030)

- **PATRÓN** `ibs_20min` < `0.1653` → IC=+0.163 (n=1039)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` < 0.1653 (IC base=-0.029)

- **PATRÓN** `volumen_pendiente_norm` < `0.0739` → IC=+0.412 (n=496)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0739 (IC base=-0.029)

- **PATRÓN** `volumen_spike_ratio` < `2.6091` → IC=+0.405 (n=558)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.6091 (IC base=-0.029)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.401 (n=521)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 21.0 (IC base=-0.029)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.1157` → IC=+0.218 (n=893)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1157 (IC base=+0.024)

- **PATRÓN** `volumen_regimen` < `1.1961` → IC=+0.195 (n=1745)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` < 1.1961 (IC base=+0.024)

- **PATRÓN** `volumen_regimen` > `0.6835` → IC=+0.203 (n=1559)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6835 (IC base=+0.024)

- **PATRÓN** `volumen_pendiente_norm` < `0.0746` → IC=+0.193 (n=1600)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` < 0.0746 (IC base=+0.024)

- **PATRÓN** `volumen_pendiente_norm` > `0.2762` → IC=+0.233 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2762 (IC base=+0.024)

- **PATRÓN** `volumen_spike_ratio` < `1.425` → IC=+0.218 (n=573)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.425 (IC base=+0.024)

- **PATRÓN** `volumen_spike_ratio` > `2.5021` → IC=+0.196 (n=573)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.5021 (IC base=+0.024)

- **PATRÓN** `ballena_activa_n` < `273.0` → IC=+0.229 (n=1144)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 273.0 (IC base=+0.024)

- **PATRÓN** `dist_vwap_pct` < `0.1661` → IC=+0.233 (n=1166)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1661 (IC base=-0.003)

- **PATRÓN** `volumen_regimen` < `1.1702` → IC=+0.227 (n=1129)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1702 (IC base=-0.003)

- **PATRÓN** `volumen_regimen` > `0.6194` → IC=+0.233 (n=1129)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6194 (IC base=-0.003)

- **PATRÓN** `volumen_pendiente_norm` < `0.1574` → IC=+0.230 (n=1134)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1574 (IC base=-0.003)

- **PATRÓN** `volumen_pendiente_norm` > `0.2706` → IC=+0.296 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2706 (IC base=-0.003)

- **PATRÓN** `volumen_spike_ratio` < `1.5285` → IC=+0.240 (n=475)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5285 (IC base=-0.003)

- **PATRÓN** `volumen_spike_ratio` > `2.1582` → IC=+0.247 (n=489)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1582 (IC base=-0.003)

- **PATRÓN** `ballena_activa_n` < `201.0` → IC=+0.241 (n=365)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 201.0 (IC base=-0.003)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0119` → IC=+0.309 (n=868)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0119 (IC base=+0.267)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.276 (n=2731)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.267)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.309 (n=1374)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.267)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.673` → IC=+0.301 (n=837)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.673 (IC base=+0.267)

- **PATRÓN** `volumen_pendiente_norm` < `0.1317` → IC=+0.279 (n=2401)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1317 (IC base=+0.267)

- **PATRÓN** `volumen_spike_ratio` > `1.6104` → IC=+0.273 (n=2518)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6104 (IC base=+0.267)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.278 (n=3101)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.267)

- **PATRÓN** `libro_liquidez` > `2048.898` → IC=+0.286 (n=868)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2048.898 (IC base=+0.267)

- **PATRÓN** `ballena_activa_n` < `18.0` → IC=+0.286 (n=1535)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 18.0 (IC base=+0.267)

- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.325 (n=1025)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0101 (IC base=+0.292)

- **PATRÓN** `drift_60min` |x|≤ `0.1807` → IC=+0.311 (n=996)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1807 (IC base=+0.292)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.321 (n=867)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.292)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.292 (n=798)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.292)

- **PATRÓN** `ibs_20min` < `0.3704` → IC=+0.295 (n=2262)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3704 (IC base=+0.292)

- **PATRÓN** `ibs_20min` > `0.2629` → IC=+0.298 (n=1025)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2629 (IC base=+0.292)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.522` → IC=+0.310 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.522 (IC base=+0.292)

- **PATRÓN** `volumen_pendiente_norm` < `0.1975` → IC=+0.291 (n=2211)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1975 (IC base=+0.292)

- **PATRÓN** `volumen_pendiente_norm` > `0.3414` → IC=+0.303 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3414 (IC base=+0.292)

- **PATRÓN** `volumen_spike_ratio` < `1.7293` → IC=+0.296 (n=951)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7293 (IC base=+0.292)

- **PATRÓN** `volumen_spike_ratio` > `2.6625` → IC=+0.302 (n=980)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6625 (IC base=+0.292)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.294 (n=1185)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.292)

- **PATRÓN** `libro_liquidez` > `2038.8556` → IC=+0.308 (n=754)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2038.8556 (IC base=+0.292)

- **PATRÓN** `ballena_activa_n` < `18.0` → IC=+0.293 (n=1430)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 18.0 (IC base=+0.292)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.737` → IC=-0.188 (n=1084)

  - _Acción_: SKIP cuando `ibs_20min` > 0.737
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=3257)

- **PATRÓN** `ibs_20min` > `0.8764` → IC=+0.173 (n=1036)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` > 0.8764 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` > `0.1552` → IC=+0.232 (n=794)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1552 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` < `0.3685` → IC=+0.235 (n=1414)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3685 (IC base=+0.029)

- **PATRÓN** `volumen_regimen` < `1.0079` → IC=+0.242 (n=1286)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0079 (IC base=+0.029)

- **PATRÓN** `volumen_regimen` > `0.6671` → IC=+0.231 (n=1305)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6671 (IC base=+0.029)

- **PATRÓN** `volumen_pendiente_norm` < `0.1635` → IC=+0.237 (n=1545)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1635 (IC base=+0.029)

- **PATRÓN** `volumen_pendiente_norm` > `0.1024` → IC=+0.244 (n=463)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1024 (IC base=+0.029)

- **PATRÓN** `volumen_spike_ratio` < `2.4295` → IC=+0.240 (n=1412)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4295 (IC base=+0.029)

- **PATRÓN** `ballena_activa_n` < `103.0` → IC=+0.265 (n=1275)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 103.0 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` < `0.3366` → IC=+0.236 (n=1088)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3366 (IC base=-0.002)

- **PATRÓN** `volumen_regimen` < `1.0307` → IC=+0.240 (n=879)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0307 (IC base=-0.002)

- **PATRÓN** `volumen_pendiente_norm` < `0.1015` → IC=+0.251 (n=923)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1015 (IC base=-0.002)

- **PATRÓN** `volumen_pendiente_norm` > `0.2857` → IC=+0.287 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2857 (IC base=-0.002)

- **PATRÓN** `volumen_spike_ratio` < `1.7982` → IC=+0.273 (n=632)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7982 (IC base=-0.002)

- **PATRÓN** `volumen_spike_ratio` > `2.4393` → IC=+0.255 (n=316)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4393 (IC base=-0.002)

- **PATRÓN** `ballena_activa_n` < `124.0` → IC=+0.260 (n=957)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 124.0 (IC base=-0.002)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7606` → IC=-0.214 (n=1885)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7606
  - _Potencial_: sin este filtro IC_bueno=+0.307 (n=1885)

- **FILTRO** `ibs_20min` > `0.6475` → IC=-0.236 (n=916)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6475
  - _Potencial_: sin este filtro IC_bueno=+0.122 (n=2749)

- **FILTRO** `sigma_ewma_delta_pct` > `8.49` → IC=-0.247 (n=429)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.49
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=3236)

- **PATRÓN** `ibs_20min` > `0.7606` → IC=+0.307 (n=1885)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7606 (IC base=+0.046)

- **PATRÓN** `dist_vwap_pct` > `0.2157` → IC=+0.339 (n=841)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2157 (IC base=+0.046)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.495` → IC=+0.185 (n=586)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 9.495 (IC base=+0.046)

- **PATRÓN** `volumen_regimen` < `0.8471` → IC=+0.334 (n=944)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8471 (IC base=+0.046)

- **PATRÓN** `volumen_regimen` > `0.7021` → IC=+0.327 (n=1263)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7021 (IC base=+0.046)

- **PATRÓN** `volumen_pendiente_norm` < `0.1593` → IC=+0.323 (n=1460)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1593 (IC base=+0.046)

- **PATRÓN** `volumen_pendiente_norm` > `0.275` → IC=+0.356 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.275 (IC base=+0.046)

- **PATRÓN** `volumen_spike_ratio` < `1.4413` → IC=+0.348 (n=459)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4413 (IC base=+0.046)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.341 (n=1209)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 48.0 (IC base=+0.046)

- **PATRÓN** `ibs_20min` < `0.6475` → IC=+0.122 (n=2749)

  - _Acción_: Kelly boost +0.61€ cuando `ibs_20min` < 0.6475 (IC base=+0.032)

- **PATRÓN** `dist_vwap_pct` < `0.2058` → IC=+0.251 (n=1131)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2058 (IC base=+0.032)

- **PATRÓN** `volumen_regimen` < `0.7031` → IC=+0.264 (n=535)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7031 (IC base=+0.032)

- **PATRÓN** `volumen_pendiente_norm` < `0.2246` → IC=+0.243 (n=1366)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2246 (IC base=+0.032)

- **PATRÓN** `volumen_pendiente_norm` > `0.0758` → IC=+0.263 (n=462)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0758 (IC base=+0.032)

- **PATRÓN** `volumen_spike_ratio` < `2.4253` → IC=+0.253 (n=1167)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4253 (IC base=+0.032)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.271 (n=1188)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 52.0 (IC base=+0.032)

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

- **PATRÓN** `sigma_h` > `0.0152` → IC=+0.336 (n=1395)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0152 (IC base=+0.305)

- **PATRÓN** `drift_60min` |x|≤ `0.1874` → IC=+0.306 (n=920)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1874 (IC base=+0.305)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.317 (n=814)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.305)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.306 (n=1024)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.305)

- **PATRÓN** `ibs_20min` < `0.3675` → IC=+0.329 (n=2091)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3675 (IC base=+0.305)

- **PATRÓN** `dist_vwap_pct` < `0.2288` → IC=+0.310 (n=1974)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2288 (IC base=+0.305)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.606` → IC=+0.315 (n=772)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.606 (IC base=+0.305)

- **PATRÓN** `volumen_regimen` < `0.7185` → IC=+0.311 (n=921)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7185 (IC base=+0.305)

- **PATRÓN** `volumen_regimen` > `1.2246` → IC=+0.336 (n=697)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2246 (IC base=+0.305)

- **PATRÓN** `volumen_pendiente_norm` > `0.2838` → IC=+0.355 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2838 (IC base=+0.305)

- **PATRÓN** `volumen_spike_ratio` < `1.4153` → IC=+0.316 (n=638)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4153 (IC base=+0.305)

- **PATRÓN** `volumen_spike_ratio` > `2.1363` → IC=+0.307 (n=867)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1363 (IC base=+0.305)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0115` → IC=+0.226 (n=4404)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0115 (IC base=+0.181)

- **PATRÓN** `drift_60min` |x|≤ `0.0872` → IC=+0.202 (n=4404)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0872 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.191 (n=13706)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` > `0.5582` → IC=+0.235 (n=13210)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5582 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` > `0.1656` → IC=+0.209 (n=5374)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1656 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.201` → IC=+0.263 (n=2594)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.201 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `1.1888` → IC=+0.169 (n=8765)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 1.1888 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` > `0.6234` → IC=+0.165 (n=8765)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 0.6234 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.2927` → IC=+0.207 (n=1932)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2927 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `2.6103` → IC=+0.193 (n=4271)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.6103 (IC base=+0.181)

- **PATRÓN** `libro_liquidez` > `1972.445` → IC=+0.182 (n=11801)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 1972.445 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `94.0` → IC=+0.199 (n=12127)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 94.0 (IC base=+0.181)

- **PATRÓN** `sigma_h` < `0.007` → IC=+0.186 (n=8452)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.007 (IC base=+0.181)

- **PATRÓN** `drift_60min` |x|≤ `0.0796` → IC=+0.228 (n=4225)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0796 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.216 (n=4739)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.238 (n=12673)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` < `0.1755` → IC=+0.175 (n=8974)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.1755 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.015` → IC=+0.199 (n=2068)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 10.015 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.685` → IC=+0.182 (n=11187)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` < 2.685 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `1.1829` → IC=+0.164 (n=9033)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.1829 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.2944` → IC=+0.226 (n=1882)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2944 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `2.6402` → IC=+0.187 (n=3971)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.6402 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.194 (n=11656)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 100.0 (IC base=+0.181)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.233 (n=747)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.216)

- **PATRÓN** `drift_60min` |x|≤ `0.3316` → IC=+0.234 (n=2217)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3316 (IC base=+0.216)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.228 (n=829)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.216)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.221 (n=1494)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.216)

- **PATRÓN** `ibs_20min` > `0.9286` → IC=+0.294 (n=1479)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9286 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.906` → IC=+0.327 (n=704)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.906 (IC base=+0.216)

- **PATRÓN** `volumen_pendiente_norm` > `0.2807` → IC=+0.275 (n=332)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2807 (IC base=+0.216)

- **PATRÓN** `volumen_spike_ratio` > `1.4374` → IC=+0.217 (n=2100)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4374 (IC base=+0.216)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.228 (n=2409)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.216)

- **PATRÓN** `sigma_h` < `0.0082` → IC=+0.253 (n=1719)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0082 (IC base=+0.251)

- **PATRÓN** `sigma_h` > `0.0074` → IC=+0.266 (n=780)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0074 (IC base=+0.251)

- **PATRÓN** `drift_60min` |x|≤ `0.0649` → IC=+0.310 (n=571)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0649 (IC base=+0.251)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.256 (n=1750)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.251)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.253 (n=829)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.251)

- **PATRÓN** `ibs_20min` < `0.2982` → IC=+0.276 (n=1508)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2982 (IC base=+0.251)

- **PATRÓN** `volumen_pendiente_norm` < `0.1004` → IC=+0.253 (n=1493)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1004 (IC base=+0.251)

- **PATRÓN** `volumen_pendiente_norm` > `0.298` → IC=+0.290 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.298 (IC base=+0.251)

- **PATRÓN** `volumen_spike_ratio` < `1.436` → IC=+0.275 (n=541)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.436 (IC base=+0.251)

- **PATRÓN** `volumen_spike_ratio` > `2.7108` → IC=+0.257 (n=541)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7108 (IC base=+0.251)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.256 (n=1936)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.251)

- **PATRÓN** `libro_liquidez` > `1612.68` → IC=+0.260 (n=1530)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1612.68 (IC base=+0.251)

- **PATRÓN** `ballena_activa_n` < `7.0` → IC=+0.254 (n=538)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 7.0 (IC base=+0.251)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.220 (n=669)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.154)

- **PATRÓN** `drift_60min` |x|≤ `0.1597` → IC=+0.182 (n=1331)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.1597 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.170 (n=2099)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 5.0 (IC base=+0.154)

- **PATRÓN** `ibs_20min` > `0.3323` → IC=+0.224 (n=1995)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3323 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` > `0.1371` → IC=+0.216 (n=1197)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1371 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.29` → IC=+0.223 (n=373)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.29 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` < `0.6912` → IC=+0.164 (n=878)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.6912 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` > `0.2807` → IC=+0.190 (n=321)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.2807 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` < `1.413` → IC=+0.172 (n=653)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.413 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` > `2.4993` → IC=+0.168 (n=652)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 2.4993 (IC base=+0.154)

- **PATRÓN** `ballena_activa_n` < `419.0` → IC=+0.158 (n=1918)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 419.0 (IC base=+0.154)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.170 (n=2082)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0059 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.2348` → IC=+0.172 (n=1830)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.2348 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.187 (n=996)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 15.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` < `0.6182` → IC=+0.207 (n=2079)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6182 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` < `0.1434` → IC=+0.172 (n=2118)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` < 0.1434 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.516` → IC=+0.194 (n=396)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 11.516 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.243` → IC=+0.146 (n=1804)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 4.243 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `1.2065` → IC=+0.161 (n=2079)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2065 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` < `0.0934` → IC=+0.149 (n=1767)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` < 0.0934 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `2.4989` → IC=+0.154 (n=1959)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.4989 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `201.0` → IC=+0.178 (n=632)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 201.0 (IC base=+0.146)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0121` → IC=+0.243 (n=744)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0121 (IC base=+0.214)

- **PATRÓN** `drift_60min` |x|≤ `0.3996` → IC=+0.226 (n=1963)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3996 (IC base=+0.214)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.237 (n=818)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.214)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.304 (n=1155)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.214)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.418` → IC=+0.303 (n=515)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.418 (IC base=+0.214)

- **PATRÓN** `volumen_pendiente_norm` < `0.0992` → IC=+0.215 (n=1913)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0992 (IC base=+0.214)

- **PATRÓN** `volumen_pendiente_norm` > `0.3532` → IC=+0.232 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3532 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` < `1.767` → IC=+0.215 (n=952)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.767 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` > `2.7088` → IC=+0.229 (n=980)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7088 (IC base=+0.214)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.221 (n=2667)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.214)

- **PATRÓN** `libro_liquidez` > `1955.4984` → IC=+0.229 (n=1011)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1955.4984 (IC base=+0.214)

- **PATRÓN** `sigma_h` < `0.0087` → IC=+0.252 (n=1284)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0087 (IC base=+0.235)

- **PATRÓN** `drift_60min` |x|≤ `0.2502` → IC=+0.265 (n=1283)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2502 (IC base=+0.235)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.281 (n=735)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.235)

- **PATRÓN** `ibs_20min` < `0.0104` → IC=+0.303 (n=847)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0104 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.468` → IC=+0.273 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.468 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` > `0.3579` → IC=+0.280 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3579 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` < `1.7484` → IC=+0.237 (n=809)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7484 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` > `2.1534` → IC=+0.238 (n=1226)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1534 (IC base=+0.235)

- **PATRÓN** `libro_liquidez` > `2038.3971` → IC=+0.243 (n=641)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2038.3971 (IC base=+0.235)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.236 (n=1242)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.235)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.210 (n=945)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.0762` → IC=+0.199 (n=716)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0762 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.163 (n=2226)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` > `0.3103` → IC=+0.214 (n=2148)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3103 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.1453` → IC=+0.197 (n=1315)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.1453 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.712` → IC=+0.206 (n=375)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.712 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `1.0223` → IC=+0.158 (n=1889)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.0223 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.1034` → IC=+0.178 (n=882)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.1034 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `1.8232` → IC=+0.151 (n=1403)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 1.8232 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `2.5068` → IC=+0.168 (n=702)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 2.5068 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `4556.0916` → IC=+0.183 (n=1431)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 4556.0916 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `138.0` → IC=+0.158 (n=2084)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 138.0 (IC base=+0.150)

- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.156 (n=2244)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0072 (IC base=+0.129)

- **PATRÓN** `drift_60min` |x|≤ `0.3953` → IC=+0.146 (n=2244)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.3953 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.170 (n=1066)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 15.0 (IC base=+0.129)

- **PATRÓN** `ibs_20min` < `0.6837` → IC=+0.187 (n=2244)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.6837 (IC base=+0.129)

- **PATRÓN** `dist_vwap_pct` < `0.1546` → IC=+0.156 (n=2233)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1546 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.646` → IC=+0.159 (n=555)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 9.646 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` < `0.8554` → IC=+0.156 (n=1496)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.8554 (IC base=+0.129)

- **PATRÓN** `volumen_pendiente_norm` > `0.3018` → IC=+0.196 (n=340)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.3018 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` < `1.81` → IC=+0.136 (n=1403)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.81 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` > `2.5607` → IC=+0.135 (n=702)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 2.5607 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `7392.0562` → IC=+0.192 (n=1017)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 7392.0562 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `67.0` → IC=+0.154 (n=908)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 67.0 (IC base=+0.129)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.179 (n=1090)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` > 0.0104 (IC base=+0.130)

- **PATRÓN** `drift_60min` |x|≤ `0.4411` → IC=+0.130 (n=2115)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.65€ cuando `drift_60min` |x|≤ 0.4411 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.173 (n=1151)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 15.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` > `0.4878` → IC=+0.218 (n=2404)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4878 (IC base=+0.130)

- **PATRÓN** `dist_vwap_pct` > `0.197` → IC=+0.193 (n=1403)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.197 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.516` → IC=+0.282 (n=513)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.516 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` < `1.1755` → IC=+0.145 (n=2404)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 1.1755 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` < `0.161` → IC=+0.136 (n=2437)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` < 0.161 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` < `1.4385` → IC=+0.151 (n=778)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 1.4385 (IC base=+0.130)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.132 (n=2518)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.02 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `2754.6285` → IC=+0.208 (n=1090)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2754.6285 (IC base=+0.130)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.162 (n=744)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 19.0 (IC base=+0.130)

- **PATRÓN** `sigma_h` < `0.0108` → IC=+0.140 (n=2457)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0108 (IC base=+0.121)

- **PATRÓN** `drift_60min` |x|≤ `0.108` → IC=+0.172 (n=819)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.108 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.141 (n=2497)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 5.0 (IC base=+0.121)

- **PATRÓN** `ibs_20min` < `0.6` → IC=+0.221 (n=2460)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6 (IC base=+0.121)

- **PATRÓN** `dist_vwap_pct` < `0.199` → IC=+0.149 (n=2318)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.199 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.827` → IC=+0.123 (n=375)

  - _Acción_: Kelly boost +0.62€ cuando `sigma_ewma_delta_pct` > 8.827 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.467` → IC=+0.133 (n=2174)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` < 2.467 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` < `1.1798` → IC=+0.131 (n=2456)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.1798 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` < `0.1651` → IC=+0.124 (n=2383)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.1651 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` > `0.2757` → IC=+0.149 (n=329)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.2757 (IC base=+0.121)

- **PATRÓN** `volumen_spike_ratio` < `1.4461` → IC=+0.134 (n=765)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 1.4461 (IC base=+0.121)

- **PATRÓN** `volumen_spike_ratio` > `2.4253` → IC=+0.135 (n=764)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 2.4253 (IC base=+0.121)

- **PATRÓN** `libro_liquidez` > `2643.337` → IC=+0.190 (n=1114)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 2643.337 (IC base=+0.121)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.131 (n=2008)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 42.0 (IC base=+0.121)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0131` → IC=+0.246 (n=1984)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0131 (IC base=+0.223)

- **PATRÓN** `drift_60min` |x|≤ `0.1748` → IC=+0.241 (n=979)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1748 (IC base=+0.223)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.227 (n=2302)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.223)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.227 (n=1996)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.223)

- **PATRÓN** `ibs_20min` > `0.66` → IC=+0.258 (n=2224)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.66 (IC base=+0.223)

- **PATRÓN** `dist_vwap_pct` > `1.2603` → IC=+0.231 (n=504)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2603 (IC base=+0.223)

- **PATRÓN** `dist_vwap_pct` < `0.8627` → IC=+0.226 (n=2283)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.8627 (IC base=+0.223)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.613` → IC=+0.251 (n=1009)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.613 (IC base=+0.223)

- **PATRÓN** `volumen_regimen` < `1.179` → IC=+0.226 (n=2221)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.179 (IC base=+0.223)

- **PATRÓN** `volumen_regimen` > `0.6187` → IC=+0.232 (n=2220)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6187 (IC base=+0.223)

- **PATRÓN** `volumen_pendiente_norm` > `0.283` → IC=+0.274 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.283 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` < `2.4689` → IC=+0.228 (n=2161)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4689 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` > `1.8082` → IC=+0.233 (n=1441)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8082 (IC base=+0.223)

- **PATRÓN** `libro_liquidez` > `2954.4444` → IC=+0.226 (n=740)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2954.4444 (IC base=+0.223)

- **PATRÓN** `sigma_h` < `0.0127` → IC=+0.235 (n=993)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0127 (IC base=+0.231)

- **PATRÓN** `sigma_h` > `0.0226` → IC=+0.239 (n=1023)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0226 (IC base=+0.231)

- **PATRÓN** `drift_60min` |x|≤ `0.0889` → IC=+0.264 (n=752)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0889 (IC base=+0.231)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.251 (n=1104)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.231)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.231 (n=1009)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.231)

- **PATRÓN** `ibs_20min` < `0.4267` → IC=+0.259 (n=2256)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4267 (IC base=+0.231)

- **PATRÓN** `dist_vwap_pct` > `0.2983` → IC=+0.240 (n=609)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2983 (IC base=+0.231)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.326` → IC=+0.262 (n=427)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.326 (IC base=+0.231)

- **PATRÓN** `volumen_regimen` > `0.6367` → IC=+0.237 (n=2256)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6367 (IC base=+0.231)

- **PATRÓN** `volumen_pendiente_norm` > `0.28` → IC=+0.287 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.28 (IC base=+0.231)

- **PATRÓN** `volumen_spike_ratio` > `1.4388` → IC=+0.234 (n=2100)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4388 (IC base=+0.231)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.209 (n=1492)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.183)

- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.192 (n=1131)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` > 0.0089 (IC base=+0.183)

- **PATRÓN** `drift_60min` |x|≤ `0.1297` → IC=+0.203 (n=1491)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1297 (IC base=+0.183)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.215 (n=1688)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.183)

- **PATRÓN** `ibs_20min` > `0.4901` → IC=+0.218 (n=3027)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4901 (IC base=+0.183)

- **PATRÓN** `dist_vwap_pct` > `0.8042` → IC=+0.204 (n=525)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8042 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.618` → IC=+0.213 (n=1467)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.618 (IC base=+0.183)

- **PATRÓN** `volumen_regimen` < `0.8616` → IC=+0.205 (n=2033)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8616 (IC base=+0.183)

- **PATRÓN** `volumen_regimen` > `0.6949` → IC=+0.187 (n=2723)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` > 0.6949 (IC base=+0.183)

- **PATRÓN** `volumen_pendiente_norm` > `0.0999` → IC=+0.193 (n=1216)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.0999 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` < `1.429` → IC=+0.196 (n=1098)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 1.429 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` > `2.4855` → IC=+0.187 (n=1098)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.4855 (IC base=+0.183)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.189 (n=3830)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.02 (IC base=+0.183)

- **PATRÓN** `libro_liquidez` > `2672.5659` → IC=+0.190 (n=3027)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 2672.5659 (IC base=+0.183)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.132 (n=1227)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.66€ cuando `sigma_h` < 0.0038 (IC base=+0.089)

- **PATRÓN** `ibs_20min` < `0.3846` → IC=+0.161 (n=2440)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` < 0.3846 (IC base=+0.089)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.128 (n=1574)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 27.0 (IC base=+0.089)

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
- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.248 (n=701)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=+0.211)

- **PATRÓN** `drift_60min` |x|≤ `0.2086` → IC=+0.226 (n=698)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2086 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.228 (n=1095)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` > `0.3797` → IC=+0.253 (n=934)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3797 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` < `0.215` → IC=+0.219 (n=926)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.215 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.869` → IC=+0.242 (n=421)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.869 (IC base=+0.211)

- **PATRÓN** `volumen_regimen` < `0.8344` → IC=+0.223 (n=698)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8344 (IC base=+0.211)

- **PATRÓN** `volumen_regimen` > `1.1625` → IC=+0.218 (n=349)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1625 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.267` → IC=+0.255 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.267 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` < `1.4231` → IC=+0.232 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4231 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `1.7756` → IC=+0.222 (n=689)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7756 (IC base=+0.211)

- **PATRÓN** `ibs_20min` < `0.1053` → IC=+0.167 (n=352)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.1053 (IC base=+0.065)

- **PATRÓN** `libro_liquidez` > `5843.1234` → IC=+0.133 (n=703)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 5843.1234 (IC base=+0.065)

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

- **PATRÓN** `ibs_20min` < `0.6752` → IC=+0.121 (n=922)

  - _Acción_: Kelly boost +0.61€ cuando `ibs_20min` < 0.6752 (IC base=+0.059)

- **PATRÓN** `libro_liquidez` > `2688.5612` → IC=+0.145 (n=418)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 2688.5612 (IC base=+0.059)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.137 (n=392)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 13.0 (IC base=+0.059)

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
- **PATRÓN** `sigma_h` > `0.0116` → IC=+0.228 (n=5738)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0116 (IC base=+0.184)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.193 (n=17918)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 5.0 (IC base=+0.184)

- **PATRÓN** `ibs_20min` > `0.4471` → IC=+0.232 (n=17212)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4471 (IC base=+0.184)

- **PATRÓN** `dist_vwap_pct` > `0.9021` → IC=+0.213 (n=2159)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9021 (IC base=+0.184)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.236` → IC=+0.255 (n=4208)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.236 (IC base=+0.184)

- **PATRÓN** `volumen_regimen` < `1.2223` → IC=+0.170 (n=11541)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 1.2223 (IC base=+0.184)

- **PATRÓN** `volumen_pendiente_norm` > `0.2909` → IC=+0.208 (n=2293)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2909 (IC base=+0.184)

- **PATRÓN** `volumen_spike_ratio` > `2.6144` → IC=+0.197 (n=5582)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.6144 (IC base=+0.184)

- **PATRÓN** `libro_liquidez` > `1784.151` → IC=+0.185 (n=17212)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 1784.151 (IC base=+0.184)

- **PATRÓN** `ballena_activa_n` < `112.0` → IC=+0.204 (n=15859)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 112.0 (IC base=+0.184)

- **PATRÓN** `sigma_h` < `0.0074` → IC=+0.194 (n=10420)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0074 (IC base=+0.188)

- **PATRÓN** `drift_60min` |x|≤ `0.4909` → IC=+0.192 (n=15593)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.4909 (IC base=+0.188)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.212 (n=5813)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.188)

- **PATRÓN** `ibs_20min` < `0.5833` → IC=+0.243 (n=15593)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5833 (IC base=+0.188)

- **PATRÓN** `dist_vwap_pct` < `0.1774` → IC=+0.172 (n=9494)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` < 0.1774 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.813` → IC=+0.207 (n=2162)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.813 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.562` → IC=+0.191 (n=15090)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` < 3.562 (IC base=+0.188)

- **PATRÓN** `volumen_regimen` < `0.6325` → IC=+0.166 (n=3506)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.6325 (IC base=+0.188)

- **PATRÓN** `volumen_pendiente_norm` > `0.2907` → IC=+0.252 (n=2110)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2907 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` > `2.617` → IC=+0.197 (n=4921)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 2.617 (IC base=+0.188)

- **PATRÓN** `ballena_activa_n` < `39.0` → IC=+0.217 (n=9646)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 39.0 (IC base=+0.188)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.228 (n=937)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.226)

- **PATRÓN** `drift_60min` |x|≤ `0.3476` → IC=+0.230 (n=2809)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3476 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.239 (n=1367)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.226)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.228 (n=1888)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.226)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.329 (n=1115)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.422` → IC=+0.356 (n=656)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.422 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` > `0.2328` → IC=+0.285 (n=501)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2328 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` > `2.2936` → IC=+0.238 (n=1224)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2936 (IC base=+0.226)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.243 (n=3010)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.226)

- **PATRÓN** `libro_liquidez` > `2074.1802` → IC=+0.229 (n=936)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2074.1802 (IC base=+0.226)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.248 (n=1721)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 17.0 (IC base=+0.226)

- **PATRÓN** `sigma_h` < `0.0085` → IC=+0.267 (n=2392)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0085 (IC base=+0.262)

- **PATRÓN** `drift_60min` |x|≤ `0.1192` → IC=+0.286 (n=1052)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1192 (IC base=+0.262)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.268 (n=2187)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.262)

- **PATRÓN** `ibs_20min` < `0.5132` → IC=+0.288 (n=2390)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5132 (IC base=+0.262)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.122` → IC=+0.264 (n=469)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.122 (IC base=+0.262)

- **PATRÓN** `volumen_pendiente_norm` < `0.0954` → IC=+0.262 (n=2148)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0954 (IC base=+0.262)

- **PATRÓN** `volumen_pendiente_norm` > `0.287` → IC=+0.289 (n=335)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.287 (IC base=+0.262)

- **PATRÓN** `volumen_spike_ratio` < `1.5594` → IC=+0.264 (n=998)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5594 (IC base=+0.262)

- **PATRÓN** `volumen_spike_ratio` > `2.6427` → IC=+0.270 (n=756)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6427 (IC base=+0.262)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.264 (n=2704)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.262)

- **PATRÓN** `libro_liquidez` > `1613.4906` → IC=+0.272 (n=2135)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1613.4906 (IC base=+0.262)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.271 (n=1004)

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

- **PATRÓN** `ibs_20min` > `0.3653` → IC=+0.224 (n=2492)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3653 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` > `0.1276` → IC=+0.196 (n=1450)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.1276 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.511` → IC=+0.163 (n=458)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 11.511 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.153` → IC=+0.154 (n=2567)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 4.153 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` < `0.63` → IC=+0.175 (n=930)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.63 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` < `0.0723` → IC=+0.154 (n=2486)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` < 0.0723 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.272` → IC=+0.182 (n=401)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.272 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `2.1764` → IC=+0.159 (n=2401)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.1764 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` > `1.5289` → IC=+0.158 (n=2437)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.5289 (IC base=+0.151)

- **PATRÓN** `ballena_activa_n` < `239.0` → IC=+0.186 (n=895)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 239.0 (IC base=+0.151)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.166 (n=2333)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0058 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.256` → IC=+0.165 (n=2053)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.256 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.172 (n=873)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` < `0.6967` → IC=+0.198 (n=2332)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.6967 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` < `0.1407` → IC=+0.164 (n=2178)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.1407 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.242` → IC=+0.156 (n=385)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 11.242 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.474` → IC=+0.144 (n=2350)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 6.474 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `1.1967` → IC=+0.154 (n=2332)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 1.1967 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` > `0.2172` → IC=+0.200 (n=434)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2172 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `2.4301` → IC=+0.152 (n=2227)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.4301 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `1.7752` → IC=+0.153 (n=1484)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.7752 (IC base=+0.144)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.144 (n=3027)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `273.0` → IC=+0.161 (n=940)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 273.0 (IC base=+0.144)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0124` → IC=+0.259 (n=955)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0124 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.236 (n=2991)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.226)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.227 (n=2564)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.226)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.303 (n=1074)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.282` → IC=+0.325 (n=610)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.282 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` < `0.1319` → IC=+0.230 (n=2685)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1319 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` > `3.1891` → IC=+0.242 (n=928)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.1891 (IC base=+0.226)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.235 (n=3425)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.226)

- **PATRÓN** `libro_liquidez` > `1964.558` → IC=+0.236 (n=1299)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1964.558 (IC base=+0.226)

- **PATRÓN** `sigma_h` < `0.0118` → IC=+0.244 (n=2693)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0118 (IC base=+0.240)

- **PATRÓN** `drift_60min` |x|≤ `0.1801` → IC=+0.259 (n=1185)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1801 (IC base=+0.240)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.263 (n=1016)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.240)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.241 (n=960)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.240)

- **PATRÓN** `ibs_20min` < `0.0333` → IC=+0.309 (n=898)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0333 (IC base=+0.240)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.603` → IC=+0.299 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.603 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` > `0.3451` → IC=+0.301 (n=400)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3451 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` > `2.1354` → IC=+0.250 (n=1709)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1354 (IC base=+0.240)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.245 (n=1416)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.240)

- **PATRÓN** `libro_liquidez` > `2038.3971` → IC=+0.254 (n=897)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2038.3971 (IC base=+0.240)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.257 (n=1169)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.240)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.206 (n=988)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.424` → IC=+0.159 (n=2962)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.424 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.160 (n=3070)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 5.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` > `0.2455` → IC=+0.194 (n=2961)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 0.2455 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.1433` → IC=+0.171 (n=1586)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.1433 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.122` → IC=+0.160 (n=1202)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 4.122 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `0.8647` → IC=+0.166 (n=1975)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.8647 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.2819` → IC=+0.187 (n=388)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.2819 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `1.5243` → IC=+0.163 (n=1272)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 1.5243 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` > `2.1748` → IC=+0.155 (n=1310)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 2.1748 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `5882.684` → IC=+0.240 (n=1343)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5882.684 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `73.0` → IC=+0.170 (n=1251)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 73.0 (IC base=+0.146)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.153 (n=2457)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0075 (IC base=+0.131)

- **PATRÓN** `drift_60min` |x|≤ `0.4364` → IC=+0.141 (n=2454)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.4364 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.160 (n=897)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 17.0 (IC base=+0.131)

- **PATRÓN** `ibs_20min` < `0.7354` → IC=+0.186 (n=2454)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.7354 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` < `0.1496` → IC=+0.146 (n=2224)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.1496 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.115` → IC=+0.172 (n=376)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 11.115 (IC base=+0.131)

- **PATRÓN** `volumen_regimen` < `0.6962` → IC=+0.146 (n=1080)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 0.6962 (IC base=+0.131)

- **PATRÓN** `volumen_pendiente_norm` > `0.2964` → IC=+0.220 (n=309)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2964 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` > `1.4309` → IC=+0.137 (n=2361)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 1.4309 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `7067.2817` → IC=+0.211 (n=818)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7067.2817 (IC base=+0.131)

- **PATRÓN** `ballena_activa_n` < `67.0` → IC=+0.134 (n=814)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 67.0 (IC base=+0.131)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0103` → IC=+0.162 (n=1353)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` > 0.0103 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.178 (n=1101)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` > `0.4423` → IC=+0.200 (n=2979)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4423 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` > `1.0538` → IC=+0.209 (n=523)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0538 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.364` → IC=+0.247 (n=1103)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.364 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` < `1.2218` → IC=+0.136 (n=2980)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 1.2218 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` < `0.0981` → IC=+0.126 (n=2818)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` < 0.0981 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` > `0.2781` → IC=+0.131 (n=385)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` > 0.2781 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` < `1.5716` → IC=+0.132 (n=1282)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 1.5716 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` > `2.1901` → IC=+0.127 (n=1320)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` > 2.1901 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.130 (n=3100)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.02 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `2485.6642` → IC=+0.230 (n=1351)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2485.6642 (IC base=+0.125)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.142 (n=953)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 24.0 (IC base=+0.125)

- **PATRÓN** `sigma_h` < `0.01` → IC=+0.152 (n=2483)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.01 (IC base=+0.117)

- **PATRÓN** `drift_60min` |x|≤ `0.1344` → IC=+0.153 (n=940)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.1344 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.129 (n=2900)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 5.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` < `0.6471` → IC=+0.212 (n=2820)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6471 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` < `0.2143` → IC=+0.136 (n=2434)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.2143 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.243` → IC=+0.134 (n=2715)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` < 3.243 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` < `0.7104` → IC=+0.139 (n=1240)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 0.7104 (IC base=+0.117)

- **PATRÓN** `volumen_pendiente_norm` > `0.2243` → IC=+0.174 (n=479)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.2243 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` < `1.4384` → IC=+0.152 (n=880)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 1.4384 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `2661.95` → IC=+0.205 (n=940)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2661.95 (IC base=+0.117)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.132 (n=2337)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 47.0 (IC base=+0.117)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0138` → IC=+0.253 (n=2512)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0138 (IC base=+0.232)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.238 (n=2933)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.232)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.235 (n=2031)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.232)

- **PATRÓN** `ibs_20min` > `0.6111` → IC=+0.272 (n=2512)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6111 (IC base=+0.232)

- **PATRÓN** `dist_vwap_pct` > `0.1917` → IC=+0.249 (n=1540)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1917 (IC base=+0.232)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.725` → IC=+0.273 (n=942)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.725 (IC base=+0.232)

- **PATRÓN** `volumen_regimen` < `1.2311` → IC=+0.239 (n=2812)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2311 (IC base=+0.232)

- **PATRÓN** `volumen_regimen` > `0.6389` → IC=+0.235 (n=2811)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6389 (IC base=+0.232)

- **PATRÓN** `volumen_pendiente_norm` > `0.2871` → IC=+0.262 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2871 (IC base=+0.232)

- **PATRÓN** `volumen_spike_ratio` > `2.4962` → IC=+0.251 (n=913)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4962 (IC base=+0.232)

- **PATRÓN** `libro_liquidez` > `2955.4057` → IC=+0.238 (n=937)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2955.4057 (IC base=+0.232)

- **PATRÓN** `sigma_h` > `0.0255` → IC=+0.255 (n=970)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0255 (IC base=+0.232)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.238 (n=2738)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.232)

- **PATRÓN** `ibs_20min` < `0.5146` → IC=+0.266 (n=2911)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5146 (IC base=+0.232)

- **PATRÓN** `dist_vwap_pct` < `0.2133` → IC=+0.236 (n=2678)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2133 (IC base=+0.232)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.218` → IC=+0.267 (n=561)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.218 (IC base=+0.232)

- **PATRÓN** `volumen_regimen` > `1.2298` → IC=+0.260 (n=970)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2298 (IC base=+0.232)

- **PATRÓN** `volumen_pendiente_norm` > `0.2821` → IC=+0.298 (n=385)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2821 (IC base=+0.232)

- **PATRÓN** `volumen_spike_ratio` > `1.4343` → IC=+0.234 (n=2707)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4343 (IC base=+0.232)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.194 (n=5042)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.245 (n=1736)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.211)

- **PATRÓN** `drift_60min` |x|≤ `0.5107` → IC=+0.221 (n=5203)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5107 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.227 (n=1891)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` > `0.9412` → IC=+0.251 (n=1737)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9412 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` > `0.1722` → IC=+0.213 (n=1954)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1722 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` < `0.4352` → IC=+0.214 (n=3712)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4352 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.975` → IC=+0.220 (n=854)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.975 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.59` → IC=+0.212 (n=4632)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.59 (IC base=+0.211)

- **PATRÓN** `volumen_regimen` < `0.706` → IC=+0.223 (n=1664)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.706 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` < `0.1071` → IC=+0.211 (n=4866)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1071 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.1669` → IC=+0.222 (n=1463)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1669 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` < `1.4557` → IC=+0.219 (n=1707)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4557 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `1.8473` → IC=+0.211 (n=3414)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8473 (IC base=+0.211)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.216 (n=3994)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `3737.1156` → IC=+0.220 (n=3469)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3737.1156 (IC base=+0.211)

- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.239 (n=1265)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.193)

- **PATRÓN** `drift_60min` |x|≤ `0.49` → IC=+0.209 (n=3793)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.49 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.214 (n=1277)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.209 (n=1690)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.193)

- **PATRÓN** `ibs_20min` < `0.7337` → IC=+0.199 (n=3794)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7337 (IC base=+0.193)

- **PATRÓN** `dist_vwap_pct` > `0.6734` → IC=+0.202 (n=662)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6734 (IC base=+0.193)

- **PATRÓN** `dist_vwap_pct` < `0.4239` → IC=+0.191 (n=3817)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` < 0.4239 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.806` → IC=+0.203 (n=3405)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.806 (IC base=+0.193)

- **PATRÓN** `volumen_regimen` < `1.0959` → IC=+0.202 (n=3167)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0959 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` < `0.0979` → IC=+0.198 (n=3486)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` < 0.0979 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` > `0.2229` → IC=+0.195 (n=764)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2229 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` < `1.5338` → IC=+0.200 (n=1645)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5338 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` > `2.1931` → IC=+0.201 (n=1695)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1931 (IC base=+0.193)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.194 (n=5042)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.01 (IC base=+0.193)

- **PATRÓN** `ballena_activa_n` < `169.0` → IC=+0.203 (n=3282)

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

- **PATRÓN** `drift_60min` |x|≤ `0.3687` → IC=+0.192 (n=1325)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.3687 (IC base=+0.176)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.223 (n=482)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.195 (n=486)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 5.0 (IC base=+0.176)

- **PATRÓN** `ibs_20min` < `0.1382` → IC=+0.205 (n=584)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1382 (IC base=+0.176)

- **PATRÓN** `ibs_20min` > `0.6081` → IC=+0.177 (n=601)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` > 0.6081 (IC base=+0.176)

- **PATRÓN** `dist_vwap_pct` > `0.7048` → IC=+0.181 (n=117)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.7048 (IC base=+0.176)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.38` → IC=+0.195 (n=1308)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` < 6.38 (IC base=+0.176)

- **PATRÓN** `volumen_regimen` < `1.2212` → IC=+0.190 (n=1325)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` < 1.2212 (IC base=+0.176)

- **PATRÓN** `volumen_pendiente_norm` > `0.2192` → IC=+0.199 (n=267)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2192 (IC base=+0.176)

- **PATRÓN** `volumen_spike_ratio` < `1.4035` → IC=+0.195 (n=440)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 1.4035 (IC base=+0.176)

- **PATRÓN** `volumen_spike_ratio` > `2.166` → IC=+0.187 (n=598)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.166 (IC base=+0.176)

- **PATRÓN** `libro_liquidez` > `14903.0336` → IC=+0.187 (n=601)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 14903.0336 (IC base=+0.176)

- **PATRÓN** `ballena_activa_n` < `692.0` → IC=+0.188 (n=1279)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 692.0 (IC base=+0.176)

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

- **PATRÓN** `drift_60min` |x|≤ `0.1485` → IC=+0.216 (n=608)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1485 (IC base=+0.198)

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

- **PATRÓN** `volumen_spike_ratio` < `1.4147` → IC=+0.217 (n=451)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4147 (IC base=+0.198)

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
- **PATRÓN** `sigma_h` < `0.011` → IC=+0.205 (n=679)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.011 (IC base=+0.184)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.210 (n=737)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.184)

- **PATRÓN** `ibs_20min` > `0.9259` → IC=+0.250 (n=350)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9259 (IC base=+0.184)

- **PATRÓN** `dist_vwap_pct` > `0.7421` → IC=+0.240 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7421 (IC base=+0.184)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.222` → IC=+0.204 (n=414)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.222 (IC base=+0.184)

- **PATRÓN** `volumen_regimen` < `0.7001` → IC=+0.228 (n=340)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7001 (IC base=+0.184)

- **PATRÓN** `volumen_pendiente_norm` < `0.1062` → IC=+0.196 (n=695)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` < 0.1062 (IC base=+0.184)

- **PATRÓN** `volumen_pendiente_norm` > `0.079` → IC=+0.192 (n=342)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.079 (IC base=+0.184)

- **PATRÓN** `volumen_spike_ratio` < `1.5649` → IC=+0.195 (n=329)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 1.5649 (IC base=+0.184)

- **PATRÓN** `volumen_spike_ratio` > `2.4746` → IC=+0.213 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4746 (IC base=+0.184)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.189 (n=899)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.02 (IC base=+0.184)

- **PATRÓN** `libro_liquidez` > `4301.4058` → IC=+0.226 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4301.4058 (IC base=+0.184)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.199 (n=759)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 52.0 (IC base=+0.184)

- **PATRÓN** `sigma_h` < `0.0094` → IC=+0.215 (n=381)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0094 (IC base=+0.208)

- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.211 (n=192)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0125 (IC base=+0.208)

- **PATRÓN** `drift_60min` |x|≤ `0.6042` → IC=+0.228 (n=572)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6042 (IC base=+0.208)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.244 (n=388)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 9.0 (IC base=+0.208)

- **PATRÓN** `ibs_20min` < `0.7273` → IC=+0.230 (n=572)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7273 (IC base=+0.208)

- **PATRÓN** `dist_vwap_pct` > `0.8487` → IC=+0.210 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8487 (IC base=+0.208)

- **PATRÓN** `dist_vwap_pct` < `0.3064` → IC=+0.210 (n=478)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3064 (IC base=+0.208)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.848` → IC=+0.215 (n=518)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.848 (IC base=+0.208)

- **PATRÓN** `volumen_regimen` < `1.1361` → IC=+0.213 (n=503)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1361 (IC base=+0.208)

- **PATRÓN** `volumen_regimen` > `0.9335` → IC=+0.210 (n=381)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.9335 (IC base=+0.208)

- **PATRÓN** `volumen_pendiente_norm` < `0.1072` → IC=+0.229 (n=496)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1072 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` > `2.2105` → IC=+0.244 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2105 (IC base=+0.208)

- **PATRÓN** `libro_liquidez` > `3032.781` → IC=+0.224 (n=571)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3032.781 (IC base=+0.208)

- **PATRÓN** `ballena_activa_n` < `29.0` → IC=+0.252 (n=381)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 29.0 (IC base=+0.208)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.160 (n=757)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.004 (IC base=+0.072)

- **PATRÓN** `ibs_20min` > `0.3924` → IC=+0.145 (n=1627)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` > 0.3924 (IC base=+0.072)

- **PATRÓN** `dist_vwap_pct` > `0.149` → IC=+0.146 (n=856)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` > 0.149 (IC base=+0.072)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.91` → IC=+0.155 (n=473)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 8.91 (IC base=+0.072)

- **PATRÓN** `volumen_pendiente_norm` > `0.2755` → IC=+0.148 (n=225)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.2755 (IC base=+0.072)

- **PATRÓN** `ibs_20min` < `0.026` → IC=+0.267 (n=402)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.026 (IC base=+0.054)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.344` → IC=+0.169 (n=146)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 10.344 (IC base=+0.054)

- **PATRÓN** `volumen_pendiente_norm` > `0.146` → IC=+0.159 (n=256)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` > 0.146 (IC base=+0.054)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.136 (n=569)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` < 0.0056 (IC base=+0.093)

- **PATRÓN** `ibs_20min` > `0.3574` → IC=+0.172 (n=538)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` > 0.3574 (IC base=+0.093)

- **PATRÓN** `dist_vwap_pct` > `0.2913` → IC=+0.179 (n=188)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.2913 (IC base=+0.093)

- **PATRÓN** `sigma_h` < `0.003` → IC=+0.128 (n=189)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.64€ cuando `sigma_h` < 0.003 (IC base=+0.067)

- **PATRÓN** `ibs_20min` < `0.0617` → IC=+0.278 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0617 (IC base=+0.067)

- **PATRÓN** `volumen_pendiente_norm` > `0.2135` → IC=+0.188 (n=78)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.2135 (IC base=+0.067)

### GBM_LATE_60M#ETH#60min
- **PATRÓN** `sigma_h` < `0.006` → IC=+0.127 (n=494)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.64€ cuando `sigma_h` < 0.006 (IC base=+0.091)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.146 (n=213)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 17.0 (IC base=+0.091)

- **PATRÓN** `ibs_20min` > `0.4221` → IC=+0.173 (n=531)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` > 0.4221 (IC base=+0.091)

- **PATRÓN** `dist_vwap_pct` > `0.1247` → IC=+0.190 (n=275)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.1247 (IC base=+0.091)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.128` → IC=+0.239 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.128 (IC base=+0.091)

- **PATRÓN** `volumen_pendiente_norm` > `0.2854` → IC=+0.162 (n=75)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.2854 (IC base=+0.091)

- **PATRÓN** `ibs_20min` < `0.1105` → IC=+0.258 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1105 (IC base=+0.020)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.686` → IC=+0.226 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.686 (IC base=+0.020)

### GBM_LATE_60M#SOL#60min
- **PATRÓN** `ibs_20min` > `0.7458` → IC=+0.167 (n=373)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.7458 (IC base=+0.034)

- **PATRÓN** `dist_vwap_pct` > `0.7372` → IC=+0.143 (n=138)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.7372 (IC base=+0.034)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.265` → IC=+0.153 (n=119)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 9.265 (IC base=+0.034)

- **PATRÓN** `volumen_pendiente_norm` > `0.2779` → IC=+0.142 (n=79)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` > 0.2779 (IC base=+0.034)

- **PATRÓN** `sigma_h` < `0.0105` → IC=+0.149 (n=246)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0105 (IC base=+0.073)

- **PATRÓN** `ibs_20min` < `0.1667` → IC=+0.218 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1667 (IC base=+0.073)

- **PATRÓN** `dist_vwap_pct` < `0.1699` → IC=+0.140 (n=201)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.1699 (IC base=+0.073)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.495` → IC=+0.318 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.495 (IC base=+0.073)

- **PATRÓN** `volumen_regimen` > `1.0779` → IC=+0.203 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0779 (IC base=+0.073)

- **PATRÓN** `volumen_pendiente_norm` > `0.1486` → IC=+0.221 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1486 (IC base=+0.073)

- **PATRÓN** `volumen_spike_ratio` < `2.1848` → IC=+0.143 (n=169)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.1848 (IC base=+0.073)

- **PATRÓN** `volumen_spike_ratio` > `1.4069` → IC=+0.160 (n=192)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.4069 (IC base=+0.073)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.139 (n=189)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.06 (IC base=+0.073)

### GBM_LATE_60M_FADE
- **FILTRO** `sigma_h` < `0.0068` → IC=-0.224 (n=208)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0068
  - _Potencial_: sin este filtro IC_bueno=-0.149 (n=109)

- **FILTRO** `dist_vwap_pct` > `0.2334` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2334
  - _Potencial_: sin este filtro IC_bueno=-0.189 (n=300)

- **FILTRO** `volumen_regimen` < `0.7666` → IC=-0.315 (n=79)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7666
  - _Potencial_: sin este filtro IC_bueno=-0.158 (n=238)

- **FILTRO** `libro_liquidez` < `902.1333` → IC=-0.216 (n=79)

  - _Acción_: SKIP cuando `libro_liquidez` < 902.1333
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=238)

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
- **FILTRO** `sigma_h` < `0.0026` → IC=-0.321 (n=26)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0026
  - _Potencial_: sin este filtro IC_bueno=-0.090 (n=81)

- **FILTRO** `drift_60min` |x|> `0.149` → IC=-0.321 (n=26)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.149
  - _Potencial_: sin este filtro IC_bueno=-0.090 (n=81)

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

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.190 (n=27)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 1.0 (IC base=-0.151)

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
- **FILTRO** `ibs_20min` > `0.1511` → IC=-0.123 (n=287)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1511
  - _Potencial_: sin este filtro IC_bueno=+0.145 (n=559)

- **PATRÓN** `sigma_h` > `0.0061` → IC=+0.196 (n=248)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` > 0.0061 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.192 (n=212)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 17.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` > `0.6842` → IC=+0.158 (n=545)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` > 0.6842 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` > `0.5394` → IC=+0.238 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5394 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.066` → IC=+0.130 (n=125)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` > 11.066 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` < `0.6187` → IC=+0.185 (n=182)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 0.6187 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` < `0.1529` → IC=+0.155 (n=450)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` < 0.1529 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` < `1.7943` → IC=+0.167 (n=295)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 1.7943 (IC base=+0.122)

- **PATRÓN** `ibs_20min` < `0.1511` → IC=+0.145 (n=559)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.1511 (IC base=+0.054)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.108` → IC=+0.182 (n=146)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 11.108 (IC base=+0.054)

- **PATRÓN** `libro_liquidez` > `3284.2124` → IC=+0.133 (n=423)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 3284.2124 (IC base=+0.054)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.6946` → IC=-0.190 (n=56)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6946
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=169)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.186 (n=100)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0049 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.139 (n=203)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 12.0 (IC base=+0.132)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.155 (n=114)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 6.0 (IC base=+0.132)

- **PATRÓN** `ibs_20min` < `0.1667` → IC=+0.197 (n=298)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.1667 (IC base=+0.132)

- **PATRÓN** `dist_vwap_pct` < `0.2503` → IC=+0.150 (n=341)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.2503 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.158` → IC=+0.164 (n=129)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 7.158 (IC base=+0.132)

- **PATRÓN** `volumen_regimen` > `0.6194` → IC=+0.150 (n=298)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 0.6194 (IC base=+0.132)

- **PATRÓN** `volumen_pendiente_norm` < `0.0701` → IC=+0.141 (n=235)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` < 0.0701 (IC base=+0.132)

- **PATRÓN** `volumen_pendiente_norm` > `0.2726` → IC=+0.173 (n=50)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.2726 (IC base=+0.132)

- **PATRÓN** `volumen_spike_ratio` < `2.5144` → IC=+0.165 (n=267)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 2.5144 (IC base=+0.132)

- **PATRÓN** `volumen_spike_ratio` > `1.5218` → IC=+0.150 (n=238)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.5218 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `5391.3885` → IC=+0.142 (n=199)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 5391.3885 (IC base=+0.132)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `volumen_pendiente_norm` > `0.1263` → IC=-0.149 (n=35)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1263
  - _Potencial_: sin este filtro IC_bueno=+0.152 (n=179)

- **FILTRO** `ibs_20min` > `0.327` → IC=-0.167 (n=76)

  - _Acción_: SKIP cuando `ibs_20min` > 0.327
  - _Potencial_: sin este filtro IC_bueno=+0.081 (n=232)

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

- **PATRÓN** `sigma_ewma_delta_pct` > `11.059` → IC=+0.237 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.059 (IC base=+0.019)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.1154` → IC=-0.208 (n=70)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1154
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=71)

- **PATRÓN** `hora_utc` > `13.0` → IC=+0.319 (n=125)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 13.0 (IC base=+0.253)

- **PATRÓN** `ibs_20min` > `0.6452` → IC=+0.283 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6452 (IC base=+0.253)

- **PATRÓN** `dist_vwap_pct` > `0.6843` → IC=+0.394 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6843 (IC base=+0.253)

- **PATRÓN** `dist_vwap_pct` < `0.2335` → IC=+0.252 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2335 (IC base=+0.253)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.318` → IC=+0.323 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.318 (IC base=+0.253)

- **PATRÓN** `volumen_regimen` < `0.5724` → IC=+0.315 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.5724 (IC base=+0.253)

- **PATRÓN** `volumen_pendiente_norm` > `0.1` → IC=+0.344 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1 (IC base=+0.253)

- **PATRÓN** `volumen_spike_ratio` < `1.4815` → IC=+0.385 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4815 (IC base=+0.253)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.321` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.321 (IC base=-0.087)

### LATE_WINDOW_5MIN
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.333 (n=70)

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

- **PATRÓN** `drift_ventana_pct` |x|> `0.3366` → IC=+0.265 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3366 (IC base=+0.242)

- **PATRÓN** `elapsed_s` > `186.2` → IC=+0.254 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 186.2 (IC base=+0.242)

- **PATRÓN** `elapsed_s` < `202.5` → IC=+0.283 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 202.5 (IC base=+0.242)

- **PATRÓN** `drift_15min` |x|≤ `2.3607` → IC=+0.300 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3607 (IC base=+0.242)

- **PATRÓN** `drift_60min` |x|≤ `0.9999` → IC=+0.279 (n=66)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9999 (IC base=+0.242)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.333 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.242)

- **PATRÓN** `ballena_activa_n` < `1862.0` → IC=+0.294 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1862.0 (IC base=+0.242)

### LATE_WINDOW_5MIN#BTC#5min
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.333 (n=70)

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

- **PATRÓN** `drift_ventana_pct` |x|> `0.3366` → IC=+0.265 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3366 (IC base=+0.242)

- **PATRÓN** `elapsed_s` > `186.2` → IC=+0.254 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 186.2 (IC base=+0.242)

- **PATRÓN** `elapsed_s` < `202.5` → IC=+0.283 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 202.5 (IC base=+0.242)

- **PATRÓN** `drift_15min` |x|≤ `2.3607` → IC=+0.300 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3607 (IC base=+0.242)

- **PATRÓN** `drift_60min` |x|≤ `0.9999` → IC=+0.279 (n=66)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9999 (IC base=+0.242)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.333 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.242)

- **PATRÓN** `ballena_activa_n` < `1862.0` → IC=+0.294 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1862.0 (IC base=+0.242)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `libro_liquidez` > `2943.5682` → IC=+0.136 (n=427)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 2943.5682 (IC base=+0.102)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `libro_liquidez` > `2943.5682` → IC=+0.136 (n=427)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 2943.5682 (IC base=+0.102)

### LIQUIDACIONES_15M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=196)

- **FILTRO** `libro_liquidez` < `5350.5492` → IC=-0.167 (n=106)

  - _Acción_: SKIP cuando `libro_liquidez` < 5350.5492
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=106)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=331)

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

- **PATRÓN** `ballena_activa_n` < `107.0` → IC=+0.136 (n=31)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 107.0 (IC base=+0.038)

### LIQUIDACIONES_15M#XRP#15min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.309 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### LIQUIDACIONES_5M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.121 (n=85)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=3569)

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
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=1334)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=1288)

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
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=849)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=849)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=855)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=855)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=222)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=222)

- **FILTRO** `hora_utc` > `12.0` → IC=-0.132 (n=66)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=171)

- **FILTRO** `py_entrada` < `0.415` → IC=-0.133 (n=47)

  - _Acción_: SKIP cuando `py_entrada` < 0.415
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=190)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.183 (n=39)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=246)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=270)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=261)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=351)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=351)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.120 (n=185)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=196)

- **FILTRO** `libro_liquidez` < `625.8426` → IC=-0.138 (n=125)

  - _Acción_: SKIP cuando `libro_liquidez` < 625.8426
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=256)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=263)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.129 (n=87)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=191)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `py_entrada` < `0.48` → IC=-0.131 (n=63)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.129 (n=33)

- **FILTRO** `hora_utc` < `15.0` → IC=-0.204 (n=25)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.132 (n=17)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.49` → IC=+0.155 (n=198)

  - _Acción_: Kelly boost +0.78€ cuando `py_entrada` < 0.49 (IC base=+0.018)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.172 (n=59)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=268)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.141 (n=157)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=181)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.159 (n=42)

  - _Acción_: Kelly boost +0.80€ cuando `py_entrada` < 0.5 (IC base=+0.052)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.53` → IC=-0.120 (n=377)

  - _Acción_: SKIP cuando `py_entrada` < 0.53
  - _Potencial_: sin este filtro IC_bueno=+0.081 (n=127)

- **FILTRO** `profundidad_ratio` < `41.6` → IC=-0.159 (n=124)

  - _Acción_: SKIP cuando `profundidad_ratio` < 41.6
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=380)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.136 (n=207)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.055 (n=234)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.159 (n=89)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=390)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.144 (n=133)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=479)

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
- **FILTRO** `py_entrada` < `0.47` → IC=-0.163 (n=6196)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=19083)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.177 (n=6256)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=19695)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.192 (n=1131)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.118 (n=3485)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.174 (n=1070)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.068 (n=3558)

- **PATRÓN** `py_entrada` > `0.495` → IC=+0.130 (n=3110)

  - _Acción_: Kelly boost +0.65€ cuando `py_entrada` > 0.495 (IC base=+0.042)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.145 (n=1214)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` > 1.0 (IC base=+0.042)

- **PATRÓN** `libro_liquidez` > `1249.264` → IC=+0.136 (n=2308)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 1249.264 (IC base=+0.042)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.129 (n=2167)

  - _Acción_: Kelly boost +0.64€ cuando `py_entrada` < 0.5 (IC base=+0.012)

- **PATRÓN** `libro_liquidez` > `1455.19` → IC=+0.152 (n=1574)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 1455.19 (IC base=+0.012)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.150 (n=865)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=2823)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.177 (n=899)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=2775)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` > `0.61` → IC=-0.187 (n=1181)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.077 (n=3553)

- **PATRÓN** `ibs_20min` > `0.9645` → IC=+0.132 (n=1569)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` > 0.9645 (IC base=+0.039)

- **PATRÓN** `libro_liquidez` > `1520.6184` → IC=+0.120 (n=2306)

  - _Acción_: Kelly boost +0.60€ cuando `libro_liquidez` > 1520.6184 (IC base=+0.039)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.156 (n=1125)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=3485)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=2401)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.162 (n=772)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=2325)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.208 (n=761)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=2826)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=3566)

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

- **FILTRO** `ibs_20min` < `0.1975` → IC=-0.223 (n=110)

  - _Acción_: SKIP cuando `ibs_20min` < 0.1975
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=224)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.131 (n=17401)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=38826)

- **FILTRO** `py_entrada` < `0.33` → IC=-0.285 (n=13868)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=42359)

- **FILTRO** `ibs_7min` < `0.2353` → IC=-0.229 (n=14038)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2353
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=42189)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.152 (n=18678)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=37549)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.241 (n=17368)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=53304)

- **FILTRO** `ibs_7min` > `0.2857` → IC=-0.182 (n=17490)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2857
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=53182)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.149 (n=2810)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=7034)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.311 (n=2350)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=7494)

- **FILTRO** `ibs_7min` < `0.7121` → IC=-0.243 (n=3248)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7121
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=6596)

- **FILTRO** `ballena_activa_n` > `6.0` → IC=-0.181 (n=2056)

  - _Acción_: SKIP cuando `ballena_activa_n` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=7788)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.271 (n=3046)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=9206)

- **FILTRO** `ibs_7min` > `0.7703` → IC=-0.211 (n=3062)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7703
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=9190)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.130 (n=2282)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.095 (n=7201)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.265 (n=2222)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=7261)

- **FILTRO** `ibs_7min` < `0.7256` → IC=-0.199 (n=2370)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7256
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=7113)

- **FILTRO** `ballena_activa_n` > `155.0` → IC=-0.190 (n=2353)

  - _Acción_: SKIP cuando `ballena_activa_n` > 155.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=7130)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.262 (n=2371)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=7258)

- **FILTRO** `ibs_7min` > `0.2678` → IC=-0.194 (n=2405)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2678
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=7224)

- **FILTRO** `ballena_activa_n` > `152.0` → IC=-0.182 (n=2394)

  - _Acción_: SKIP cuando `ballena_activa_n` > 152.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=7235)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.161 (n=2304)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=7036)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.312 (n=2300)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=7040)

- **FILTRO** `ibs_7min` < `0.2941` → IC=-0.246 (n=3081)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2941
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=6259)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.195 (n=2214)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=7126)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.254 (n=3039)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=9991)

- **FILTRO** `ibs_7min` > `0.7333` → IC=-0.178 (n=3256)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7333
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=9774)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.125 (n=2988)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.091 (n=6172)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.261 (n=2149)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=7011)

- **FILTRO** `ibs_7min` < `0.7279` → IC=-0.186 (n=2289)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7279
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=6871)

- **FILTRO** `ballena_activa_n` > `27.0` → IC=-0.188 (n=2250)

  - _Acción_: SKIP cuando `ballena_activa_n` > 27.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=6910)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.267 (n=2143)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=7353)

- **FILTRO** `ibs_7min` > `0.2755` → IC=-0.179 (n=2372)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2755
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=7124)

- **FILTRO** `ballena_activa_n` > `26.0` → IC=-0.179 (n=2316)

  - _Acción_: SKIP cuando `ballena_activa_n` > 26.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=7180)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.284 (n=2220)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=6984)

- **FILTRO** `ibs_7min` < `0.7143` → IC=-0.222 (n=2976)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7143
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=6228)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.217 (n=2221)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=6983)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.191 (n=3296)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=10200)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.32` → IC=-0.293 (n=2178)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=7018)

- **FILTRO** `ibs_7min` < `0.2` → IC=-0.222 (n=2289)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=6907)

- **FILTRO** `ballena_activa_n` > `9.0` → IC=-0.197 (n=2288)

  - _Acción_: SKIP cuando `ballena_activa_n` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=6908)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.218 (n=3132)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=9637)

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
- **PATRÓN** `delta_ratio` |x|> `0.3981` → IC=+0.139 (n=1181)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.70€ cuando `delta_ratio` |x|> 0.3981 (IC base=+0.129)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.137 (n=617)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 6.0 (IC base=+0.129)

- **PATRÓN** `total_vol_5m` < `436.8284` → IC=+0.154 (n=394)

  - _Acción_: Kelly boost +0.77€ cuando `total_vol_5m` < 436.8284 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `3599.4239` → IC=+0.149 (n=536)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 3599.4239 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.147 (n=389)

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
- **PATRÓN** `delta_ratio` |x|> `0.3988` → IC=+0.134 (n=244)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.67€ cuando `delta_ratio` |x|> 0.3988 (IC base=+0.118)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.134 (n=219)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 14.0 (IC base=+0.118)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.127 (n=293)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.04 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `2349.306` → IC=+0.130 (n=163)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 2349.306 (IC base=+0.118)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4161` → IC=+0.183 (n=156)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.92€ cuando `delta_ratio` |x|> 0.4161 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.154 (n=241)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 4.0 (IC base=+0.140)

- **PATRÓN** `total_vol_5m` < `384.339` → IC=+0.214 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 384.339 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `7697.7504` → IC=+0.146 (n=156)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 7697.7504 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `70.0` → IC=+0.195 (n=103)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 70.0 (IC base=+0.140)

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
- **PATRÓN** `hora_utc` < `14.0` → IC=+0.128 (n=202)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 14.0 (IC base=+0.101)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.181 (n=136)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.01 (IC base=+0.101)

- **PATRÓN** `libro_liquidez` > `3589.6144` → IC=+0.167 (n=100)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 3589.6144 (IC base=+0.101)

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
- **FILTRO** `sigma_h` > `0.0137` → IC=-0.274 (n=29)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0137
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=89)

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

- **FILTRO** `sigma_h` < `0.005` → IC=-0.246 (n=132)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.005
  - _Potencial_: sin este filtro IC_bueno=-0.230 (n=398)

- **FILTRO** `pct_vs_K` |x|> `3.3065` → IC=-0.433 (n=132)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.3065
  - _Potencial_: sin este filtro IC_bueno=-0.168 (n=398)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `sigma_h` < `0.0044` → IC=-0.192 (n=50)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0044
  - _Potencial_: sin este filtro IC_bueno=-0.141 (n=151)

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

- **FILTRO** `sigma_h` < `0.0051` → IC=-0.221 (n=41)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0051
  - _Potencial_: sin este filtro IC_bueno=-0.175 (n=124)

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

- **PATRÓN** `edge` > `0.0992` → IC=+0.443 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.0992 (IC base=+0.417)

- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.440 (n=149)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0097 (IC base=+0.417)

- **PATRÓN** `T_h` < `0.5922` → IC=+0.435 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.5922 (IC base=+0.417)

- **PATRÓN** `T_h` > `1.484` → IC=+0.422 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.484 (IC base=+0.417)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.472 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.417)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.478 (n=137)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.417)

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

- **PATRÓN** `edge` > `0.2005` → IC=+0.479 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.2005 (IC base=+0.465)

- **PATRÓN** `sigma_h` < `0.0156` → IC=+0.479 (n=141)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0156 (IC base=+0.465)

- **PATRÓN** `T_h` > `0.6729` → IC=+0.465 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.6729 (IC base=+0.465)

- **PATRÓN** `dist_50` > `0.4658` → IC=+0.492 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4658 (IC base=+0.465)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.473 (n=144)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.465)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=317)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=391)

- **PATRÓN** `streak_estiramiento` < `0.8382` → IC=+0.126 (n=263)

  - _Acción_: Kelly boost +0.63€ cuando `streak_estiramiento` < 0.8382 (IC base=+0.051)

- **PATRÓN** `libro_liquidez` > `2526.0042` → IC=+0.143 (n=141)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 2526.0042 (IC base=+0.051)

### STREAK_FADE_15M#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=28)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.119 (n=19)

### STREAK_FADE_15M#XRP#15min
- **PATRÓN** `streak_estiramiento` < `0.258` → IC=+0.167 (n=40)

  - _Acción_: Kelly boost +0.83€ cuando `streak_estiramiento` < 0.258 (IC base=+0.000)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.136 (n=119)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 7.0 (IC base=+0.093)

- **PATRÓN** `streak_estiramiento` < `0.5577` → IC=+0.172 (n=114)

  - _Acción_: Kelly boost +0.86€ cuando `streak_estiramiento` < 0.5577 (IC base=+0.093)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.164 (n=111)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 35.0 (IC base=+0.093)

- **PATRÓN** `libro_liquidez` > `2388.626` → IC=+0.150 (n=118)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2388.626 (IC base=+0.093)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `9.0` → IC=-0.219 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=94)

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
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=1018)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=1332)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=1168)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=1217)

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
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=4084)

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
- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.193 (n=1633)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0054 (IC base=+0.176)

- **PATRÓN** `sigma_h` > `0.012` → IC=+0.197 (n=1237)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.012 (IC base=+0.176)

- **PATRÓN** `drift_60min` |x|≤ `0.177` → IC=+0.191 (n=3266)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.177 (IC base=+0.176)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1909` → IC=+0.177 (n=1683)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.89€ cuando `delta_ratio_macro` |x|> 0.1909 (IC base=+0.176)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3486` → IC=+0.183 (n=3373)

  - _Acción_: Kelly boost +0.91€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3486 (IC base=+0.176)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.185 (n=3423)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 6.0 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.179 (n=3416)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 15.0 (IC base=+0.176)

- **PATRÓN** `ibs_15` > `0.5475` → IC=+0.252 (n=3710)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5475 (IC base=+0.176)

- **PATRÓN** `dist_vwap_pct` > `0.1292` → IC=+0.170 (n=1794)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.1292 (IC base=+0.176)

- **PATRÓN** `dist_vwap_pct` < `0.4946` → IC=+0.163 (n=3324)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.4946 (IC base=+0.176)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.468` → IC=+0.258 (n=957)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.468 (IC base=+0.176)

- **PATRÓN** `libro_liquidez` > `4647.0394` → IC=+0.193 (n=1237)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 4647.0394 (IC base=+0.176)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=1477)

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

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.187 (n=247)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0035 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.1075` → IC=+0.151 (n=491)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.1075 (IC base=+0.144)

- **PATRÓN** `drift_15min` |x|≤ `0.3963` → IC=+0.145 (n=246)

  - _Acción_: Kelly boost +0.73€ cuando `drift_15min` |x|≤ 0.3963 (IC base=+0.144)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1424` → IC=+0.151 (n=491)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.76€ cuando `delta_ratio_macro` |x|> 0.1424 (IC base=+0.144)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.129` → IC=+0.157 (n=292)

  - _Acción_: Kelly boost +0.78€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.129 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.152 (n=674)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 6.0 (IC base=+0.144)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.150 (n=767)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 17.0 (IC base=+0.144)

- **PATRÓN** `ibs_15` > `0.5373` → IC=+0.240 (n=736)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5373 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` > `0.1197` → IC=+0.157 (n=459)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.1197 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.577` → IC=+0.271 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.577 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `3217.9115` → IC=+0.150 (n=736)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 3217.9115 (IC base=+0.144)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `sigma_ewma_delta_pct` > `17.763` → IC=-0.175 (n=38)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 17.763
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=351)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `ibs_15` > `0.8878` → IC=+0.243 (n=286)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8878 (IC base=+0.094)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.063` → IC=+0.169 (n=164)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 17.063 (IC base=+0.094)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.134 (n=471)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.094)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `15.781` → IC=+0.140 (n=48)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 15.781 (IC base=+0.002)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.024` → IC=+0.233 (n=283)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.024 (IC base=+0.201)

- **PATRÓN** `drift_60min` |x|≤ `0.1305` → IC=+0.225 (n=566)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1305 (IC base=+0.201)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0952` → IC=+0.246 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0952 (IC base=+0.201)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.203 (n=768)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.201)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.212 (n=758)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.201)

- **PATRÓN** `ibs_15` > `0.5306` → IC=+0.277 (n=847)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5306 (IC base=+0.201)

- **PATRÓN** `dist_vwap_pct` > `0.1288` → IC=+0.211 (n=490)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1288 (IC base=+0.201)

- **PATRÓN** `dist_vwap_pct` < `0.7008` → IC=+0.202 (n=984)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.7008 (IC base=+0.201)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.798` → IC=+0.229 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.798 (IC base=+0.201)

- **PATRÓN** `libro_liquidez` > `2959.1226` → IC=+0.293 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2959.1226 (IC base=+0.201)

- **PATRÓN** `ibs_15` < `0.1094` → IC=+0.162 (n=785)
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
- **FILTRO** `sigma_h` > `0.0069` → IC=-0.175 (n=2207)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0069
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=2209)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.214 (n=1728)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=2688)

- **FILTRO** `libro_liquidez` < `4202.8422` → IC=-0.154 (n=2914)

  - _Acción_: SKIP cuando `libro_liquidez` < 4202.8422
  - _Potencial_: sin este filtro IC_bueno=+0.098 (n=1502)

- **PATRÓN** `ibs_15` > `0.6326` → IC=+0.280 (n=1065)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6326 (IC base=-0.069)

- **PATRÓN** `dist_vwap_pct` > `0.1115` → IC=+0.205 (n=611)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1115 (IC base=-0.069)

- **PATRÓN** `dist_vwap_pct` < `0.4306` → IC=+0.199 (n=1041)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` < 0.4306 (IC base=-0.069)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2311` → IC=+0.269 (n=1226)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2311 (IC base=-0.013)

- **PATRÓN** `ibs_15` < `0.3605` → IC=+0.284 (n=3677)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3605 (IC base=-0.013)

- **PATRÓN** `dist_vwap_pct` > `0.6585` → IC=+0.276 (n=499)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6585 (IC base=-0.013)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0067` → IC=-0.218 (n=648)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0067
  - _Potencial_: sin este filtro IC_bueno=-0.187 (n=1948)

- **FILTRO** `sigma_h` < `0.0035` → IC=-0.228 (n=649)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0035
  - _Potencial_: sin este filtro IC_bueno=-0.183 (n=1947)

- **FILTRO** `sigma_ewma_delta_pct` > `23.3` → IC=-0.271 (n=373)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 23.3
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=2223)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=66)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.194 (n=2530)

- **FILTRO** `libro_liquidez` < `11008.8338` → IC=-0.217 (n=649)

  - _Acción_: SKIP cuando `libro_liquidez` < 11008.8338
  - _Potencial_: sin este filtro IC_bueno=-0.187 (n=1947)

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

- **PATRÓN** `sigma_h` < `0.0077` → IC=+0.250 (n=1346)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0077 (IC base=+0.245)

- **PATRÓN** `drift_15min` |x|≤ `0.7725` → IC=+0.257 (n=1185)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7725 (IC base=+0.245)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2187` → IC=+0.263 (n=610)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2187 (IC base=+0.245)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.253 (n=495)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.245)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.247 (n=523)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.245)

- **PATRÓN** `ibs_15` < `0.3735` → IC=+0.277 (n=1346)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3735 (IC base=+0.245)

- **PATRÓN** `dist_vwap_pct` > `0.6145` → IC=+0.264 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6145 (IC base=+0.245)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.405` → IC=+0.256 (n=600)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.405 (IC base=+0.245)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `sigma_h` > `0.0105` → IC=-0.248 (n=256)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0105
  - _Potencial_: sin este filtro IC_bueno=-0.171 (n=771)

- **FILTRO** `drift_60min` |x|> `0.173` → IC=-0.251 (n=347)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.173
  - _Potencial_: sin este filtro IC_bueno=-0.160 (n=680)

- **FILTRO** `drift_15min` |x|> `0.89` → IC=-0.283 (n=256)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.89
  - _Potencial_: sin este filtro IC_bueno=-0.160 (n=771)

- **FILTRO** `sigma_ewma_delta_pct` > `6.602` → IC=-0.203 (n=237)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.602
  - _Potencial_: sin este filtro IC_bueno=-0.187 (n=790)

- **FILTRO** `sigma_ewma_delta_pct` > `17.894` → IC=-0.148 (n=535)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 17.894
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=4254)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1478` → IC=+0.181 (n=45)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.90€ cuando `delta_ratio_macro` |x|> 0.1478 (IC base=-0.191)

- **PATRÓN** `ibs_15` > `0.5625` → IC=+0.234 (n=62)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5625 (IC base=-0.191)

- **PATRÓN** `dist_vwap_pct` < `0.4298` → IC=+0.162 (n=75)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.4298 (IC base=-0.191)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.233 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=-0.191)

- **PATRÓN** `ibs_15` < `0.3529` → IC=+0.293 (n=591)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3529 (IC base=-0.040)

- **PATRÓN** `dist_vwap_pct` < `0.4416` → IC=+0.242 (n=618)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4416 (IC base=-0.040)

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

- **PATRÓN** `delta_ratio_macro` |x|> `0.069` → IC=+0.275 (n=785)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.069 (IC base=-0.026)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1169` → IC=+0.292 (n=382)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1169 (IC base=-0.026)

- **PATRÓN** `ibs_15` < `0.1376` → IC=+0.315 (n=586)
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

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2242` → IC=+0.302 (n=656)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2242 (IC base=+0.291)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.308 (n=1143)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.291)

- **PATRÓN** `ibs_15` > `0.8393` → IC=+0.319 (n=1099)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8393 (IC base=+0.291)

- **PATRÓN** `dist_vwap_pct` > `0.2727` → IC=+0.323 (n=477)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2727 (IC base=+0.291)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.589` → IC=+0.378 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.589 (IC base=+0.291)

- **PATRÓN** `libro_liquidez` > `12245.063` → IC=+0.310 (n=499)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12245.063 (IC base=+0.291)

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
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.294)

- **PATRÓN** `drift_60min` |x|≤ `0.0518` → IC=+0.321 (n=171)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0518 (IC base=+0.294)

- **PATRÓN** `delta_ratio_macro` |x|> `0.145` → IC=+0.299 (n=341)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.145 (IC base=+0.294)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3049` → IC=+0.307 (n=412)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3049 (IC base=+0.294)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.314 (n=492)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.294)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.297 (n=462)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.294)

- **PATRÓN** `ibs_15` > `0.8489` → IC=+0.321 (n=511)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8489 (IC base=+0.294)

- **PATRÓN** `dist_vwap_pct` > `0.2899` → IC=+0.319 (n=219)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2899 (IC base=+0.294)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.52` → IC=+0.369 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.52 (IC base=+0.294)

### UPDOWN_OU_5M
- **FILTRO** `drift_60min` |x|> `0.2626` → IC=-0.132 (n=85)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2626
  - _Potencial_: sin este filtro IC_bueno=-0.108 (n=256)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.1232` → IC=-0.155 (n=85)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1232
  - _Potencial_: sin este filtro IC_bueno=-0.101 (n=256)

- **FILTRO** `ballena_activa_n` > `44.0` → IC=-0.136 (n=229)

  - _Acción_: SKIP cuando `ballena_activa_n` > 44.0
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=80)

- **FILTRO** `sigma_h` < `0.0051` → IC=-0.180 (n=120)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0051
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=361)

- **FILTRO** `ballena_activa_n` > `24.0` → IC=-0.206 (n=107)

  - _Acción_: SKIP cuando `ballena_activa_n` > 24.0
  - _Potencial_: sin este filtro IC_bueno=-0.117 (n=113)

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
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=150)

- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.2395` → IC=-0.121 (n=93)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.2395
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
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=39)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.3147` → IC=-0.385 (n=24)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.3147
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.0611` → IC=-0.259 (n=27)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.0611
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=10)

- **FILTRO** `sigma_h` < `0.0051` → IC=-0.250 (n=18)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0051
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=37)

- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.0905` → IC=-0.220 (n=23)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.0905
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

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

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5475 sube el IC de +0.176 a +0.252 en UPDOWN_GBM#15min (n=3710). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7223 sube el IC de +0.218 a +0.284 en UPDOWN_GBM#BTC#15min (n=627). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.5373 sube el IC de +0.144 a +0.240 en UPDOWN_GBM#ETH#15min (n=736). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.8878 sube el IC de +0.094 a +0.243 en UPDOWN_GBM#SOL#15min (n=286). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5306 sube el IC de +0.201 a +0.277 en UPDOWN_GBM#XRP#15min (n=847). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1094 sube el IC de +0.068 a +0.162 en UPDOWN_GBM#XRP#15min (n=785). Ya aplicado como kelly_boost=+0.81€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6326 sube el IC de -0.069 a +0.280 en UPDOWN_GBM_15M_TARDIO (n=1065). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3605 sube el IC de -0.013 a +0.284 en UPDOWN_GBM_15M_TARDIO (n=3677). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7572 sube el IC de +0.095 a +0.331 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=348). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.6128 sube el IC de -0.195 a +0.309 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=61). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.5959 sube el IC de +0.149 a +0.247 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=535). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3735 sube el IC de +0.245 a +0.277 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=1346). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de -0.191 a +0.234 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=62). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3529 sube el IC de -0.040 a +0.293 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=591). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.209 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.1376 sube el IC de -0.026 a +0.315 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=586). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_YES, IBS > 0.8434 sube el IC de +0.080 a +0.342 en UPDOWN_GBM_ETH_15M_HORA7 (n=17). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_YES, IBS > 0.8434 sube el IC de +0.080 a +0.342 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=17). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8393 sube el IC de +0.291 a +0.319 en UPDOWN_GBM_IBS_ALTO (n=1099). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8303 sube el IC de +0.289 a +0.315 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=588). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8489 sube el IC de +0.294 a +0.321 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=511). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7863 sube el IC de +0.364 a +0.401 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=641). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8048 sube el IC de +0.362 a +0.392 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=330). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7485 sube el IC de +0.365 a +0.410 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=311). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1949 | +0.090 | +214.25€ | 1 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1949 | +0.090 | +214.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1557 | +0.093 | +185.52€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1557 | +0.093 | +185.52€ | 0 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 284 | +0.070 | +11.30€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 284 | +0.070 | +11.30€ | 5 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 77 | +0.108 | +17.77€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 77 | +0.108 | +17.77€ | 0 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 715 | -0.001 | +81.28€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 715 | -0.001 | +81.28€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE | 5 | +0.018 | +2.77€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE#15min | 5 | +0.018 | +2.77€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 526 | -0.030 | +45.85€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 526 | -0.030 | +45.85€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 148 | +0.093 | +27.91€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 148 | +0.093 | +27.91€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 36 | +0.026 | +4.76€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 36 | +0.026 | +4.76€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 40821 | -0.080 | -5046.21€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 2277 | +0.038 | -261.10€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 38544 | -0.087 | -4785.11€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4522 | -0.114 | -779.00€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4522 | -0.114 | -779.00€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 2277 | +0.038 | -261.10€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 2277 | +0.038 | -261.10€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 4396 | -0.106 | -882.17€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 4396 | -0.106 | -882.17€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 10888 | -0.019 | -1007.51€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 10888 | -0.019 | -1007.51€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 10791 | -0.104 | -798.30€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 10791 | -0.104 | -798.30€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 7947 | -0.132 | -1318.12€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 7947 | -0.132 | -1318.12€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 36158 | -0.015 | +3300.50€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 9363 | +0.005 | +1660.35€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 26795 | -0.022 | +1640.15€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 36158 | -0.015 | +3300.50€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 9363 | +0.005 | +1660.35€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 26795 | -0.022 | +1640.15€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 148677 | +0.115 | -5978.70€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 18919 | +0.182 | -593.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 656 | -0.014 | -68.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 120237 | +0.107 | -4987.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 8865 | +0.099 | -329.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 19935 | +0.107 | -1232.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 61 | -0.151 | +10.95€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 19859 | +0.109 | -1231.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 28728 | +0.127 | -445.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5236 | +0.187 | -185.25€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 19919 | +0.120 | -126.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 3531 | +0.082 | -111.86€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 19990 | +0.100 | -1377.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 75 | -0.123 | -6.95€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 19900 | +0.101 | -1359.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 31633 | +0.124 | -591.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 8173 | +0.177 | -167.58€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 20194 | +0.107 | -360.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 3254 | +0.100 | -54.17€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 28434 | +0.115 | -1400.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 5305 | +0.197 | -249.13€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 559 | +0.019 | -14.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 20490 | +0.095 | -973.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 2080 | +0.126 | -163.46€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#XRP | 19957 | +0.106 | -930.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 69 | -0.091 | +4.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 19875 | +0.107 | -935.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 23931 | +0.197 | -1426.00€ | 2 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 23931 | +0.197 | -1426.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 5442 | +0.180 | -454.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 5442 | +0.180 | -454.70€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 3079 | +0.204 | -66.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 3079 | +0.204 | -66.39€ | 3 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 5378 | +0.181 | -425.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 5378 | +0.181 | -425.52€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 4657 | +0.248 | -155.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 4657 | +0.248 | -155.96€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 5296 | +0.189 | -337.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 5296 | +0.189 | -337.20€ | 0 | 3 |
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
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 83763 | +0.202 | -5947.06€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 83763 | +0.202 | -5947.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 14388 | +0.186 | -1474.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 14388 | +0.186 | -1474.78€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 13524 | +0.225 | -456.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 13524 | +0.225 | -456.99€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 14343 | +0.182 | -1491.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 14343 | +0.182 | -1491.07€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 13615 | +0.220 | -508.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 13615 | +0.220 | -508.94€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 13898 | +0.202 | -907.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 13898 | +0.202 | -907.97€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 13995 | +0.197 | -1107.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 13995 | +0.197 | -1107.31€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 32080 | +0.116 | +175.01€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 32080 | +0.116 | +175.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 15950 | +0.119 | +160.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 15950 | +0.119 | +160.16€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 16130 | +0.114 | +14.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 16130 | +0.114 | +14.84€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 2121 | +0.293 | -6.59€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 2121 | +0.293 | -6.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 974 | +0.280 | -26.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 974 | +0.280 | -26.06€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 1027 | +0.297 | +13.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 1027 | +0.297 | +13.35€ | 0 | 5 |
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
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1684 | +0.071 | -69.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 649 | +0.048 | -56.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 1035 | +0.084 | -12.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 74 | +0.118 | +4.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 74 | +0.118 | +4.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1294 | +0.079 | -28.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 259 | +0.056 | -16.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 1035 | +0.084 | -12.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 316 | +0.025 | -44.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 316 | +0.025 | -44.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 63530 | +0.100 | -1635.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 5133 | +0.090 | +43.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 58397 | +0.101 | -1679.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 34931 | +0.105 | -418.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 5133 | +0.090 | +43.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 29798 | +0.108 | -461.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 13102 | +0.108 | -86.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 13102 | +0.108 | -86.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 15497 | +0.082 | -1130.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 15497 | +0.082 | -1130.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 897 | +0.193 | -109.11€ | 4 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 897 | +0.193 | -109.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 897 | +0.193 | -109.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 897 | +0.193 | -109.11€ | 4 | 4 |
| ✅ GBM_LATE_15M | 43588 | +0.095 | +22903.71€ | 0 | 20 |
| ✅ GBM_LATE_15M#15min | 43588 | +0.095 | +22903.71€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 7261 | +0.217 | +6015.05€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 7261 | +0.217 | +6015.05€ | 0 | 22 |
| ✅ GBM_LATE_15M#BTC | 6553 | +0.180 | +5044.09€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 6553 | +0.180 | +5044.09€ | 0 | 23 |
| ✅ GBM_LATE_15M#DOGE | 7795 | +0.205 | +6076.13€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 7795 | +0.205 | +6076.13€ | 0 | 20 |
| ✅ GBM_LATE_15M#ETH | 6062 | +0.043 | +1727.24€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 6062 | +0.043 | +1727.24€ | 1 | 20 |
| ✅ GBM_LATE_15M#SOL | 6130 | -0.032 | +1301.09€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 6130 | -0.032 | +1301.09€ | 4 | 14 |
| ✅ GBM_LATE_15M#XRP | 9787 | -0.030 | +2740.12€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 9787 | -0.030 | +2740.12€ | 4 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 46821 | +0.085 | +25586.87€ | 0 | 19 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 46821 | +0.085 | +25586.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 9062 | +0.003 | +4605.86€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 9062 | +0.003 | +4605.86€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 9933 | +0.010 | +2389.78€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 9933 | +0.010 | +2389.78€ | 0 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 6486 | +0.279 | +6982.82€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 6486 | +0.279 | +6982.82€ | 0 | 23 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 8482 | +0.013 | +2107.67€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 8482 | +0.013 | +2107.67€ | 1 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 7435 | +0.039 | +3091.23€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 7435 | +0.039 | +3091.23€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 5423 | +0.305 | +6409.51€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 5423 | +0.305 | +6409.51€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 34503 | +0.181 | +28118.30€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 34503 | +0.181 | +28118.30€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 5238 | +0.232 | +4693.79€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 5238 | +0.232 | +4693.79€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 5431 | +0.150 | +4042.48€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 5431 | +0.150 | +4042.48€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 5536 | +0.224 | +4779.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 5536 | +0.224 | +4779.83€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 5853 | +0.139 | +4481.78€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 5853 | +0.139 | +4481.78€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 6478 | +0.126 | +4863.02€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 6478 | +0.126 | +4863.02€ | 0 | 26 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 5967 | +0.227 | +5257.39€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 5967 | +0.227 | +5257.39€ | 0 | 25 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 9393 | +0.134 | +4604.62€ | 0 | 17 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 9393 | +0.134 | +4604.62€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 406 | +0.154 | +254.75€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 406 | +0.154 | +254.75€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 2733 | +0.143 | +1543.60€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 2733 | +0.143 | +1543.60€ | 0 | 20 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 467 | +0.150 | +239.09€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 467 | +0.150 | +239.09€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 2800 | +0.138 | +1347.00€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 2800 | +0.138 | +1347.00€ | 0 | 13 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 2360 | +0.112 | +938.54€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 2360 | +0.112 | +938.54€ | 0 | 16 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 627 | +0.133 | +281.63€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 627 | +0.133 | +281.63€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO | 43739 | +0.186 | +35139.44€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#15min | 43739 | +0.186 | +35139.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 6930 | +0.243 | +6490.40€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 6930 | +0.243 | +6490.40€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 6826 | +0.148 | +4702.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 6826 | +0.148 | +4702.77€ | 0 | 26 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 7407 | +0.233 | +6621.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 7407 | +0.233 | +6621.12€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 7219 | +0.139 | +5158.92€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 7219 | +0.139 | +5158.92€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 7729 | +0.121 | +5358.66€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 7729 | +0.121 | +5358.66€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 7628 | +0.232 | +6807.57€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 7628 | +0.232 | +6807.57€ | 0 | 19 |
| ✅ GBM_LATE_5M | 11994 | +0.203 | +9400.57€ | 1 | 30 |
| ✅ GBM_LATE_5M#5min | 11994 | +0.203 | +9400.57€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 986 | +0.243 | +920.10€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 986 | +0.243 | +920.10€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 2784 | +0.207 | +2381.88€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 2784 | +0.207 | +2381.88€ | 0 | 26 |
| ✅ GBM_LATE_5M#DOGE | 1167 | +0.196 | +861.83€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1167 | +0.196 | +861.83€ | 0 | 19 |
| ✅ GBM_LATE_5M#ETH | 3345 | +0.193 | +2357.45€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 3345 | +0.193 | +2357.45€ | 0 | 26 |
| ✅ GBM_LATE_5M#SOL | 1789 | +0.195 | +1381.78€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 1789 | +0.195 | +1381.78€ | 0 | 27 |
| ✅ GBM_LATE_5M#XRP | 1923 | +0.208 | +1497.52€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1923 | +0.208 | +1497.52€ | 0 | 0 |
| ✅ GBM_LATE_60M | 3609 | +0.066 | +1158.26€ | 0 | 8 |
| ✅ GBM_LATE_60M#60min | 3609 | +0.066 | +1158.26€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 1329 | +0.082 | +479.50€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 1329 | +0.082 | +479.50€ | 0 | 6 |
| ✅ GBM_LATE_60M#ETH | 1169 | +0.065 | +394.01€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 1169 | +0.065 | +394.01€ | 0 | 8 |
| ✅ GBM_LATE_60M#SOL | 1111 | +0.045 | +284.75€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 1111 | +0.045 | +284.75€ | 0 | 13 |
| 🚫 GBM_LATE_60M_FADE | 586 | -0.241 | -16.72€ | 9 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 586 | -0.241 | -16.72€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 218 | -0.245 | -13.71€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 218 | -0.245 | -13.71€ | 3 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 209 | -0.225 | +3.01€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 209 | -0.225 | +3.01€ | 6 | 1 |
| 🚫 GBM_LATE_60M_FADE#SOL | 159 | -0.252 | -6.01€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 159 | -0.252 | -6.01€ | 7 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 1571 | +0.086 | +403.55€ | 1 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 1571 | +0.086 | +403.55€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 622 | +0.082 | +151.74€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 622 | +0.082 | +151.74€ | 1 | 12 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 559 | +0.058 | +90.53€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 559 | +0.058 | +90.53€ | 2 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 390 | +0.130 | +161.29€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 390 | +0.130 | +161.29€ | 1 | 9 |
| ✅ LATE_WINDOW_5MIN | 168 | +0.282 | +168.63€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 168 | +0.282 | +168.63€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 168 | +0.282 | +168.63€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 168 | +0.282 | +168.63€ | 1 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 3465 | +0.102 | +858.97€ | 0 | 1 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 3465 | +0.102 | +858.97€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 3465 | +0.102 | +858.97€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 3465 | +0.102 | +858.97€ | 0 | 1 |
| ✅ LIQUIDACIONES_15M | 564 | -0.032 | -12.49€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 564 | -0.032 | -12.49€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 159 | -0.003 | +4.85€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 159 | -0.003 | +4.85€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 25 | -0.167 | -4.79€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 25 | -0.167 | -4.79€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 113 | -0.004 | +0.29€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 113 | -0.004 | +0.29€ | 1 | 1 |
| ✅ LIQUIDACIONES_15M#SOL | 210 | -0.009 | -1.32€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 210 | -0.009 | -1.32€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M | 3779 | +0.017 | +89.32€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 3779 | +0.017 | +89.32€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 183 | +0.024 | -1.79€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 183 | +0.024 | -1.79€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 795 | +0.008 | +29.93€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 795 | +0.008 | +29.93€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE | 207 | -0.012 | -4.18€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 207 | -0.012 | -4.18€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 1384 | +0.027 | +34.10€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1384 | +0.027 | +34.10€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 758 | +0.012 | +2.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 758 | +0.012 | +2.16€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 452 | +0.018 | +29.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 452 | +0.018 | +29.11€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 1799 | -0.041 | -30.34€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1799 | -0.041 | -30.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 522 | -0.030 | -11.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 522 | -0.030 | -11.92€ | 6 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 618 | -0.018 | +4.61€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 618 | -0.018 | +4.61€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 659 | -0.070 | -23.04€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 659 | -0.070 | -23.04€ | 6 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 9266 | -0.028 | -9.37€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 4404 | -0.038 | -104.77€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 4862 | -0.018 | +95.41€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 281 | -0.030 | -5.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 143 | -0.010 | +2.73€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 138 | -0.050 | -7.84€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 2317 | -0.023 | -0.72€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 1103 | -0.030 | -17.68€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 1214 | -0.016 | +16.96€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 1005 | -0.028 | +4.49€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 506 | -0.047 | -18.55€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 499 | -0.009 | +23.04€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 2038 | -0.040 | -55.90€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 945 | -0.053 | -59.24€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 1093 | -0.028 | +3.35€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 1810 | -0.016 | +45.91€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 867 | -0.028 | +1.72€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 943 | -0.005 | +44.19€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 1815 | -0.032 | +1.95€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 840 | -0.042 | -13.75€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 975 | -0.024 | +15.71€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 51230 | +0.000 | +2609.96€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 51230 | +0.000 | +2609.96€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 9244 | +0.027 | +1197.57€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 9244 | +0.027 | +1197.57€ | 2 | 5 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 7362 | -0.033 | -87.73€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 7362 | -0.033 | -87.73€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 9346 | +0.025 | +983.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 9346 | +0.025 | +983.27€ | 1 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 7207 | -0.047 | -145.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 7207 | -0.047 | -145.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 8667 | -0.004 | +233.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 8667 | -0.004 | +233.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 9404 | +0.016 | +428.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 9404 | +0.016 | +428.77€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 6685 | -0.058 | -155.44€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 6685 | -0.058 | -155.44€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1226 | -0.001 | -15.82€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1226 | -0.001 | -15.82€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1750 | -0.076 | -41.08€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1750 | -0.076 | -41.08€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 59 | -0.041 | -1.76€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 59 | -0.041 | -1.76€ | 0 | 0 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 126899 | -0.077 | +1656.63€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 126899 | -0.077 | +1656.63€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 22096 | -0.077 | +1102.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 22096 | -0.077 | +1102.98€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 19112 | -0.101 | -1015.59€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 19112 | -0.101 | -1015.59€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 22370 | -0.068 | +1192.74€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 22370 | -0.068 | +1192.74€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 18656 | -0.097 | -605.73€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 18656 | -0.097 | -605.73€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 22700 | -0.057 | +327.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 22700 | -0.057 | +327.55€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 21965 | -0.067 | +654.68€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 21965 | -0.067 | +654.68€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 8787 | -0.034 | -186.63€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 8787 | -0.034 | -186.63€ | 0 | 0 |
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
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 973 | -0.031 | -35.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 973 | -0.031 | -35.91€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1710 | +0.124 | +699.02€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#5min | 1574 | +0.129 | +686.42€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 368 | +0.135 | +181.26€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 368 | +0.135 | +181.26€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#DOGE | 325 | +0.118 | +112.01€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 325 | +0.118 | +112.01€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#ETH | 312 | +0.140 | +156.62€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 312 | +0.140 | +156.62€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#SOL | 275 | +0.150 | +149.73€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 275 | +0.150 | +149.73€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#XRP | 294 | +0.101 | +86.80€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 294 | +0.101 | +86.80€ | 0 | 3 |
| ✅ ORDER_FLOW_5M_REACTIVO | 1516 | -0.017 | -27.51€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 1516 | -0.017 | -27.51€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 296 | +0.000 | +9.58€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 296 | +0.000 | +9.58€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 264 | -0.023 | -3.54€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 264 | -0.023 | -3.54€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 392 | -0.046 | -32.92€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 392 | -0.046 | -32.92€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 319 | +0.002 | -1.04€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 319 | +0.002 | -1.04€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 245 | -0.010 | +0.42€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 245 | -0.010 | +0.42€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 918 | -0.075 | -51.04€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 428 | -0.114 | -81.18€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 332 | -0.144 | -68.58€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 96 | -0.010 | -12.59€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 323 | -0.032 | +23.57€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 232 | -0.021 | +26.03€ | 1 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 91 | -0.059 | -2.46€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 167 | -0.056 | +6.57€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 136 | -0.065 | +2.18€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 31 | -0.015 | +4.39€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 700 | -0.088 | -40.37€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 218 | -0.032 | -10.67€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 1147 | -0.208 | -68.82€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC | 446 | -0.210 | -42.51€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#atexpiry | 389 | -0.214 | -42.28€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 57 | -0.178 | -0.23€ | 2 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 391 | -0.210 | -31.29€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 343 | -0.222 | -38.30€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 48 | -0.120 | +7.01€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 310 | -0.199 | +4.99€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 289 | -0.194 | +2.87€ | 5 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 21 | -0.239 | +2.12€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 1021 | -0.212 | -77.72€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 126 | -0.172 | +8.90€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 460 | +0.396 | +438.23€ | 0 | 13 |
| ✅ RESOLUTION_SNIPER#BTC | 69 | +0.162 | +55.45€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 69 | +0.162 | +55.45€ | 0 | 2 |
| ✅ RESOLUTION_SNIPER#ETH | 110 | +0.366 | +102.82€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 110 | +0.366 | +102.82€ | 0 | 8 |
| ✅ RESOLUTION_SNIPER#SOL | 281 | +0.461 | +279.96€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 281 | +0.461 | +279.96€ | 0 | 10 |
| ✅ RESOLUTION_SNIPER#sniper | 460 | +0.396 | +438.23€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 746 | +0.029 | +43.65€ | 2 | 2 |
| ✅ STREAK_FADE_15M#15min | 746 | +0.029 | +43.65€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 306 | +0.019 | +2.32€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 306 | +0.019 | +2.32€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 62 | +0.000 | -0.54€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 62 | +0.000 | -0.54€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 77 | -0.006 | +1.97€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 77 | -0.006 | +1.97€ | 2 | 0 |
| ✅ STREAK_FADE_15M#XRP | 301 | +0.054 | +39.90€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 301 | +0.054 | +39.90€ | 0 | 5 |
| ✅ STREAK_FADE_5M | 3443 | -0.021 | -133.25€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3443 | -0.021 | -133.25€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 1059 | -0.020 | -35.48€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 1059 | -0.020 | -35.48€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 591 | -0.026 | -25.53€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 591 | -0.026 | -25.53€ | 1 | 0 |
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
| ✅ STREAK_MOM_5M | 11007 | +0.015 | +81.81€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 11007 | +0.015 | +81.81€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2812 | +0.020 | +28.62€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2812 | +0.020 | +28.62€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2878 | +0.017 | +33.42€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2878 | +0.017 | +33.42€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2890 | +0.009 | -1.97€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2890 | +0.009 | -1.97€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2427 | +0.015 | +21.74€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2427 | +0.015 | +21.74€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 10016 | +0.013 | -51.63€ | 2 | 0 |
| ✅ STRUCT_NO_15M#15min | 10016 | +0.013 | -51.63€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 4103 | +0.017 | -10.03€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 4103 | +0.017 | -10.03€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3618 | +0.011 | -28.16€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3618 | +0.011 | -28.16€ | 2 | 0 |
| ✅ STRUCT_NO_15M#SOL | 2295 | +0.009 | -13.44€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 2295 | +0.009 | -13.44€ | 1 | 0 |
| ✅ UPDOWN_GBM | 78788 | +0.054 | +6982.41€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 19557 | +0.083 | +4276.77€ | 0 | 12 |
| ✅ UPDOWN_GBM#240min | 2516 | +0.004 | +23.89€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 51766 | +0.050 | +2588.91€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 4672 | +0.007 | +93.62€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 6851 | +0.089 | +1075.72€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1576 | +0.156 | +698.08€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 77 | -0.006 | -0.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 5198 | +0.070 | +378.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 17147 | +0.055 | +1472.21€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 2554 | +0.088 | +622.10€ | 0 | 11 |
| ✅ UPDOWN_GBM#BTC#240min | 682 | +0.009 | +11.09€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 11732 | +0.061 | +770.45€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 2079 | +0.005 | +65.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 100 | -0.069 | +3.57€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 8615 | +0.070 | +918.64€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1555 | +0.147 | +610.96€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 78 | +0.013 | -1.79€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 6982 | +0.054 | +309.47€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 18197 | +0.045 | +1183.04€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 4658 | +0.067 | +680.90€ | 0 | 11 |
| ✅ UPDOWN_GBM#ETH#240min | 662 | +0.006 | +15.77€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 11142 | +0.044 | +465.56€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 1642 | +0.010 | +18.09€ | 1 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 93 | -0.100 | +2.72€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 17335 | +0.033 | +862.59€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 4948 | +0.034 | +406.73€ | 0 | 3 |
| ✅ UPDOWN_GBM#SOL#240min | 629 | -0.009 | -0.27€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 10725 | +0.038 | +450.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 951 | +0.007 | +10.53€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 82 | -0.131 | -5.24€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 10641 | +0.065 | +1472.03€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 4266 | +0.103 | +1258.00€ | 0 | 11 |
| ✅ UPDOWN_GBM#XRP#240min | 388 | +0.010 | -0.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 5987 | +0.041 | +214.10€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 275 | -0.099 | +1.05€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 854 | +0.364 | +312.74€ | 0 | 9 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 854 | +0.364 | +312.74€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 440 | +0.362 | +151.21€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 440 | +0.362 | +151.21€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 414 | +0.365 | +161.54€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 414 | +0.365 | +161.54€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO | 20284 | -0.025 | +4689.35€ | 3 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 20284 | -0.025 | +4689.35€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1718 | -0.056 | +502.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1718 | -0.056 | +502.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 3627 | -0.112 | +126.95€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 3627 | -0.112 | +126.95€ | 5 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 948 | +0.216 | +770.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 948 | +0.216 | +770.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 2507 | +0.218 | +1627.88€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 2507 | +0.218 | +1627.88€ | 1 | 18 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 5816 | -0.067 | +677.60€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 5816 | -0.067 | +677.60€ | 5 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 5668 | -0.065 | +983.66€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 5668 | -0.065 | +983.66€ | 2 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 236 | +0.050 | +14.42€ | 0 | 5 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 236 | +0.050 | +14.42€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 236 | +0.050 | +14.42€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 236 | +0.050 | +14.42€ | 0 | 5 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1465 | +0.291 | +1254.82€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1465 | +0.291 | +1254.82€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 784 | +0.289 | +638.48€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 784 | +0.289 | +638.48€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 681 | +0.294 | +616.34€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 681 | +0.294 | +616.34€ | 0 | 9 |
| ✅ UPDOWN_OU_5M | 822 | -0.113 | -83.92€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#5min | 822 | -0.113 | -83.92€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 251 | -0.081 | -18.64€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 251 | -0.081 | -18.64€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 89 | -0.170 | -10.17€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 89 | -0.170 | -10.17€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 99 | -0.183 | -5.76€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 99 | -0.183 | -5.76€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 38 | -0.175 | -6.61€ | 2 | 0 |
| ✅ WEEKLY_PRICE | 3691 | +0.304 | +1736.67€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 1360 | +0.257 | +170.41€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 1419 | +0.299 | +634.07€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 912 | +0.380 | +932.19€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**〰️ H-IBS-15** — IBS-15 como señal de mean-reversion
  - _Umbral_: n≥40 ops con ibs_15 en features y spread_IC>0.15 entre buckets
  - _Acción_: Añadir ibs_15 como boost/filtro en FEATURE_RULES de shadow_postmortem.py
  - _Estado_: Spread bajo (0.042) — sin ventaja clara. oversold(IBS<0.3): IC=+0.064 n=27337 | neutral: IC=+0.057 n=29118 | overbought(IBS>0.7): IC=+0.099 n=27745
  - _Datos_: n=87520 IC=+0.074 PNL=+13013.29€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 722 celda(s) pasan gate riguroso completo de 2717 evaluadas (n>=40) y 3759 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.034 < 0.08 — monitorear
  - _Datos_: n=4942 IC=+0.034 PNL=+406.84€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=1419/15 IC=+0.299 PNL=+634.07€ | BTC: n=1360/15 IC=+0.257 PNL=+170.41€ | SOL: n=912/15 IC=+0.380 PNL=+932.19€

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
  - _Estado_: 78656 ops, 22 horas distintas. Sin hora con n≥15 y IC extremo aún.

**⏳ H-WINDOW-MOMENTUM** — Momentum de outcome entre ventanas 15min contiguas
  - _Umbral_: n≥60 alineadas y gap IC≥0.08 vs contrarias — y descartar que sea proxy de drift_15min/60min
  - _Acción_: Si confirma e independiente de drift → capturar prev_window_outcome como feature en shadow_predict y boost ×1.1-1.2 en señales alineadas
  - _Estado_: alineada_con_outcome_prev IC=+0.140 n=795/60 | contraria IC=+0.192 n=830 | gap=-0.052 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=471, boost estimado=+0.017. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 275 ops con delta_ratio

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=1640/40 IC=+0.010 PNL=+18.21€ | BTC#60min: n=2077/40 IC=+0.005 PNL=+65.03€ | SOL#60min: n=951/40 IC=+0.007 PNL=+10.53€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.048 n=569887 | tras_1loss IC=+0.096 n=432753 | tras_2loss IC=+0.065 n=174870/40 | gap=-0.018 (umbral 0.05)

**⏳ H-BTC-LEADS-ETH** — ETH/SOL GBM contrario al drift_15min de BTC del mismo ciclo
  - _Umbral_: n≥40 en contrario_BTC y gap≥0.08 — y descartar confound con drift propio antes de actuar
  - _Acción_: Si se confirma y no es confound → boost en ETH/SOL cuando decisión contraria a drift_15min BTC
  - _Estado_: alineado_BTC IC=+0.036 n=11150 | contrario_BTC IC=+0.053 n=9786/40 | gap=+0.017 (umbral 0.08) — SIN CONFIRMAR independencia de filtros propios de ETH


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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.199 > 0.08 con n=769 PNL=+576.80€
  - _Datos_: n=769 IC=+0.199 PNL=+576.80€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.172 > 0.08 con n=864 PNL=+501.29€
  - _Datos_: n=864 IC=+0.172 PNL=+501.29€

**🟡 H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: n≥25 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.151 > 0.08 con n=64 PNL=+29.12€
  - _Datos_: n=64 IC=+0.151 PNL=+29.12€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.333 > 0.1 con n=3014 PNL=+1657.39€
  - _Datos_: n=3014 IC=+0.333 PNL=+1657.39€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=718 IC=+0.072 PNL=+81.45€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=718 IC=+0.072 PNL=+81.45€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=85 IC=+0.190 PNL=+58.97€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=85 IC=+0.190 PNL=+58.97€

**〰️ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: n=74707 IC=+0.053 PNL=+6681.36€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=74707 IC=+0.053 PNL=+6681.36€

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
  - _Estado_: n=3139 IC=+0.010 PNL=+18.74€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=3139 IC=+0.010 PNL=+18.74€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=1529 IC=-0.000 PNL=+75.03€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=1529 IC=-0.000 PNL=+75.03€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=986 IC=+0.021 PNL=+42.07€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=986 IC=+0.021 PNL=+42.07€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.176 > 0.1 con n=4941 PNL=+3067.08€
  - _Datos_: n=4941 IC=+0.176 PNL=+3067.08€

**〰️ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: n=2918 IC=+0.068 PNL=+219.16€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=2918 IC=+0.068 PNL=+219.16€

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=2551 IC=+0.088 PNL=+620.58€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=2551 IC=+0.088 PNL=+620.58€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.098 > 0.08 con n=11263 PNL=+3180.10€
  - _Datos_: n=11263 IC=+0.098 PNL=+3180.10€

**〰️ H-CUSTOM-LONGSHOT-BIAS** — Longshot bias — ¿mejor IC cuando py_mkt < 0.20 o > 0.80?
  - _Hipótesis_: Jon-Becker repo documenta formalmente: contratos a 1-20 cents tienen win_rate < precio implícito (compradores pierden sistemáticamente en longshots). En nuestro sistema: cuando py_mkt<0.20 el GBM predice BUY_NO con edge estructural adicional al del modelo. ¿Se confirma en nuestros datos? Buscar en feature pct_spot_vs_ref si los mercados extremos tienen mejor IC en BUY_NO.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 en mercados extremos → boost ×1.2 en BUY_NO cuando py_mkt<0.20
  - _Estado_: n=378 IC=-0.237 PNL=-7.53€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=378 IC=-0.237 PNL=-7.53€

**〰️ H-CUSTOM-ETH15-REVERSION** — ETH#15min con drift_15min < -1 — ¿mean reversion?
  - _Hipótesis_: ETH y BTC tienen patrones opuestos: BTC funciona con momentum (drift>0.3). ETH funciona con reversión (drift<-1): 9/14 (64%) IC=+0.087. La hipótesis es que ETH tiene más mean-reversion que BTC en 15min.
  - _Umbral_: n≥20 y IC>+0.08
  - _Acción_: Si ETH drift<-1 confirma IC>0.08 con n≥20 → boost ×1.1 en ETH#15min cuando drift_15min<-1
  - _Estado_: n=446 IC=-0.025 PNL=-14.35€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=446 IC=-0.025 PNL=-14.35€

**〰️ H-CUSTOM-GBM-09H** — GBM a las 09h UTC — bloqueada 2026-06-29
  - _Hipótesis_: IC=-0.158 n=19 PNL=-11.62€. Bloqueada manualmente el 2026-06-29 añadiendo hora 9 a meta.gbm_blacklist_hours_auto. Esta hipótesis monitorea que el IC siga siendo negativo para justificar el bloqueo.
  - _Umbral_: n≥25 para confirmar el bloqueo es necesario
  - _Acción_: Si IC sube a >-0.05 con n≥30 → evaluar desbloquear. Si se mantiene <-0.10 → confirmar bloqueo permanente.
  - _Estado_: n=1007 IC=+0.035 PNL=+85.18€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=1007 IC=+0.035 PNL=+85.18€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=124 IC=+0.016 PNL=+2.04€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=124 IC=+0.016 PNL=+2.04€

**〰️ H-FUNDING-HIGH-BUYNO** — Funding rate alto (>p90 real ≈0.009%/8h) → BUY_NO tiene más edge
  - _Hipótesis_: Cuando funding perps Binance está en el decil superior real (>0.009%/8h, ver recalibración 06-Ago), los longs están sobrecargados y pagan por mantener. Hipótesis: BUY_NO GBM tiene IC superior en este régimen vs funding neutral. RECALIBRADO 06-Ago: el umbral original (0.03) era FÍSICAMENTE IMPOSIBLE -- el máximo real observado en 5428 filas de UPDOWN_GBM (feature funding_rate_8h = round(fr*100,5), fr=lastFundingRate crudo de Binance) es 0.01, y nunca lo cruzaba -- n=0 desde que se creó, atrapada sin poder acumular ni una fila. Recalibrado a p90 real (percentiles: p50=0.00368, p75=0.00651, p90=0.00943, p95=p99=p100=0.01 -- el feature satura en 0.01 en el 8.4% de las filas, sin evidencia de que sea un bug de captura, no de que sea funding genuinamente extremo). n=332 BUY_NO ya disponibles con el umbral nuevo (>>umbral_n=40), frente a n=0 con el original.
  - _Umbral_: n≥40 y IC>+0.05 diferencial vs baseline
  - _Acción_: Si IC_funding_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en BUY_NO cuando funding_rate_8h > 0.009
  - _Estado_: n=8617 IC=+0.021 PNL=+232.49€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=8617 IC=+0.021 PNL=+232.49€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.282 n=168) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=168 IC=+0.282 PNL=+168.63€

**〰️ H-DVOL-SPIKE-BUYNO** — DVOL spike (sigma_h alto) → BUY_NO tiene más edge (panic regime)
  - _Hipótesis_: Inspirado en 'The Volatility Edge' (Concretum Research, 2025): en equities, VIX spikes identifican regímenes de pánico donde los moves están sobreamplificados por feedback loops (deleveraging, hedgers, etc). En cripto el análogo es DVOL (Deribit BTC IV). Sin acceso a DVOL, usamos sigma_h como proxy (vol realizada 1h). Hipótesis: cuando sigma_h > 0.004/h (≈ vol diaria >9.6%), los mercados de predicción exageran la bajada en 15min → BUY_NO tiene IC superior porque el pánico se revierte intraday. Activar cuando n≥200 en BUY_NO #15min para tener potencia suficiente para subdividir por régimen.
  - _Umbral_: n≥200 BUY_NO #15min total, luego n≥40 en subconjunto sigma_h>0.004 y IC>+0.10
  - _Acción_: Si IC_sigma_alto > IC_baseline + 0.08 con n≥40 → boost ×1.2 en BUY_NO cuando sigma_h>0.004. Pendiente integrar DVOL real (Deribit API) cuando n≥500.
  - _Estado_: n=12967 IC=+0.051 PNL=+1082.50€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=12967 IC=+0.051 PNL=+1082.50€

**〰️ H-CUSTOM-POLY-DRIFT-CONFIRM** — poly_drift_5obs: ¿el precio YES interno de Polymarket confirma nuestra señal?
  - _Hipótesis_: Feature nueva 2026-06-27: drift del precio YES en Polymarket en últimas 5 obs (~5min). Si poly_drift<0 y decidimos BUY_NO (o poly_drift>0 y BUY_YES) → confluencia. Si diverge → reducción de stake. Hipótesis: confluencia Binance+Polymarket mejora IC; divergencia empeora.
  - _Umbral_: n≥40 en confluencia vs divergencia para validar el boost ×1.1
  - _Acción_: Si IC_confluencia>IC_divergencia con n≥40 → mantener el boost. Si no → retirar.
  - _Estado_: n=4686 IC=+0.064 PNL=+698.67€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=4686 IC=+0.064 PNL=+698.67€

**🟡 H-CUSTOM-OF-VOLUMEN-ALTO** — ORDER_FLOW_5M con total_vol_5m alto — ¿volumen extremo mejora el IC?
  - _Hipótesis_: Inspirado en un artículo sobre 'volume trading strategy' (mean-reversion en SPY): la idea es que un mismo movimiento de precio con volumen inusualmente alto refleja pánico/liquidación forzada y tiene más probabilidad de revertir que el mismo movimiento con volumen normal. No es transplantable tal cual (esa estrategia opera en barras diarias de SPY, nosotros en ventanas de 15-60min de cripto), pero el feature total_vol_5m ya se captura en cada predicción de ORDER_FLOW_5M (shadow_predict.py) y nunca se ha usado como filtro independiente — solo sirve de denominador para calcular delta_ratio. Hipótesis: dentro de las señales que ya pasan el filtro de delta_ratio, un total_vol_5m alto (volumen real, no solo desequilibrio) mejora el IC. Distribución real en predictions_*.csv (n=843): mediana=1696, p75=108522 (muy asimétrica) — se usa p75 como umbral de 'volumen alto'.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC_volumen_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en ORDER_FLOW_5M cuando total_vol_5m>100000
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.111 > 0.08 con n=559 PNL=+181.42€
  - _Datos_: n=559 IC=+0.111 PNL=+181.42€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-POS** — GBM 15min/60min: spread positivo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Inspirado en un artículo sobre bots de Polymarket: mercados de distinta duración del mismo activo (ej. BTC#15min vs BTC#60min) no repriciician a la misma velocidad — uno puede quedarse rezagado tras un movimiento. Si el spread entre ambos se sale de lo normal, puede indicar que uno de los dos aún no ha incorporado la información que el otro ya tiene. No es transplantable tal cual (el artículo lo usa para arbitraje comprando ambos lados a la vez, algo que no hacemos — ver idea_bidirectional_accumulation aparcada), pero el feature cross_window_spread (precio_yes propio menos precio_yes de la ventana relacionada, sin normalizar aún por z-score) ya se captura para GBM#15min (contra 60min) y GBM#60min (contra 15min) desde el 2026-07-01, sin cambiar ninguna decisión. Esta hipótesis cubre el lado positivo (mercado propio más caro que el relacionado); ver H-CUSTOM-CROSS-WINDOW-SPREAD-NEG para el lado negativo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread, y evaluar si merece la pena normalizar a z-score con más histórico
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.147 > 0.08 con n=1189 PNL=+330.63€
  - _Datos_: n=1189 IC=+0.147 PNL=+330.63€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-NEG** — GBM 15min/60min: spread negativo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Lado negativo de H-CUSTOM-CROSS-WINDOW-SPREAD-POS (mercado propio más barato que el relacionado). Mismo feature cross_window_spread, mismo origen (artículo sobre bots de Polymarket), umbral simétrico.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.096 > 0.08 con n=935 PNL=+439.33€
  - _Datos_: n=935 IC=+0.096 PNL=+439.33€

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
  - _Estado_: n=11823 IC=+0.057 PNL=+1151.58€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=11823 IC=+0.057 PNL=+1151.58€

**🟡 H-CUSTOM-OF-EDGE-ALTO** — ORDER_FLOW_5M: edge alto (>0.20) rinde mejor que edge cerca del suelo
  - _Hipótesis_: Analizado 2026-07-01 sobre 794 resoluciones de ORDER_FLOW_5M: edge_neto en [0.025,0.198) -> IC=-0.009 (n=397, PNL=-10.49€) vs edge_neto en [0.198,0.385] -> IC=+0.029 (n=397, PNL=+16.43€). Comprobado que NO es un efecto general: en UPDOWN_GBM el patrón se invierte (edge bajo IC=-0.002 vs edge alto IC=-0.033), así que este filtro debe quedar scoped solo a ORDER_FLOW_5M, no aplicarse a otras estrategias. CORREGIDO 2026-07-01 (mismo día, encontrado por auditoría): el filtro original usaba 'edge_neto' con solo feature_lo, pero edge_neto está firmado por dirección (negativo en BUY_NO, positivo en BUY_YES) y ORDER_FLOW_5M solo genera BUY_NO desde 2026-06-25 — el filtro nunca podía matchear ningún BUY_NO real, solo el remanente BUY_YES histórico de antes del 25-jun (n=151, datos muertos, no crecen hacia adelante). Cambiado a 'edge_direccional' (siempre positivo, = abs(edge_neto)) + decision=BUY_NO explícito. Con el fix: n=227, IC=+0.0502, PNL=+19.15€ — señal real y viva.
  - _Umbral_: n≥80 en cada mitad (bajo/alto) para confirmar con más margen que el análisis inicial
  - _Acción_: Si se confirma con n≥80 y el gap se mantiene ≥0.03 → subir EDGE_MINIMO solo para ORDER_FLOW_5M a ~0.20 (o escalar Kelly con la magnitud del edge)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.124 > 0.02 con n=986 PNL=+411.45€
  - _Datos_: n=986 IC=+0.124 PNL=+411.45€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.450 > 0.1 con n=1690 PNL=+1630.58€
  - _Datos_: n=1690 IC=+0.450 PNL=+1630.58€

**〰️ H-CUSTOM-GBM-BUYYES-GLOBAL-MALO** — UPDOWN_GBM BUY_YES global — ¿estructuralmente peor que BUY_NO en todas las estrategias activas?
  - _Hipótesis_: Analizado 2026-07-01: patrón cross-estrategia consistente en las 4 estrategias activas — BUY_NO gana a BUY_YES sin excepción (UPDOWN_GBM IC=+0.058 n=154 vs -0.046 n=412; ORDER_FLOW_5M +0.053 n=439 vs -0.043 n=355; PRICE_TARGET_GBM +0.011 n=45 vs -0.267 n=28; WEEKLY_PRICE +0.115 n=50 vs -0.315 n=25). Mecanismo propuesto: sesgo retail comprando 'Up'/'YES' en cripto infla el precio de YES por encima de su valor justo en Polymarket — consistente con la sobreconfianza del modelo en probabilidades altas de YES detectada en la calibración Platt (ver idea_calibracion_platt). ORDER_FLOW_5M (solo genera BUY_NO desde 2026-06-25) y WEEKLY_PRICE (H-WEEKLY-BUYNO) ya actúan sobre este mismo patrón; UPDOWN_GBM y PRICE_TARGET_GBM (ver H-CUSTOM-PRICETARGET-BUYYES-MALO) todavía no tienen un tratamiento sistemático equivalente, solo filtros puntuales por hora/subtipo.
  - _Umbral_: n≥50 y IC<-0.05 para confirmar bloqueo global (a día de hoy ya está en n=412, IC=-0.046 — muy cerca)
  - _Acción_: Si se confirma con n≥50 → exigir evidencia direccional más fuerte por subtipo antes de permitir BUY_YES en live (barra asimétrica frente a BUY_NO), en vez de auto-desactivar de golpe todo BUY_YES de GBM
  - _Estado_: n=31010 IC=+0.074 PNL=+4503.94€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=31010 IC=+0.074 PNL=+4503.94€

**🟡 H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: n≥120 y IC>+0.10 (el n=61 del descubrimiento está incluido — exigir ~doble para confirmar forward)
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.206 > 0.1 con n=6910 PNL=+4102.94€
  - _Datos_: n=6910 IC=+0.206 PNL=+4102.94€

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.140 < -0.1 con n=504 PNL=+59.86€
  - _Datos_: n=504 IC=-0.140 PNL=+59.86€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=3136 IC=+0.068 PNL=+397.58€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=3136 IC=+0.068 PNL=+397.58€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=148 IC=-0.107 PNL=+3.49€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=148 IC=-0.107 PNL=+3.49€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.111 > 0.1 con n=830 PNL=+223.43€
  - _Datos_: n=830 IC=+0.111 PNL=+223.43€

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
  - _Estado_: n=33098 IC=-0.132 PNL=+2863.01€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=33098 IC=-0.132 PNL=+2863.01€

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
  - _Estado_: n=3310 IC=+0.133 PNL=+2036.13€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=3310 IC=+0.133 PNL=+2036.13€

**🟡 H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: n≥40 forward y IC>+0.08 (barra live estándar)
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.204 > 0.08 con n=4206 PNL=+3055.09€
  - _Datos_: n=4206 IC=+0.204 PNL=+3055.09€

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=8049 IC=+0.051 PNL=+635.73€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=8049 IC=+0.051 PNL=+635.73€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.095 > 0.08 con n=3534 PNL=+1941.10€
  - _Datos_: n=3534 IC=+0.095 PNL=+1941.10€

**🟡 H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: n≥80 (elevado desde el estándar 40, por ser recorte post-hoc) y IC>+0.08 en BTC específicamente
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.218 > 0.08 con n=834 PNL=+497.02€
  - _Datos_: n=834 IC=+0.218 PNL=+497.02€

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.223 < -0.1 con n=3430 PNL=-291.57€
  - _Datos_: n=3430 IC=-0.223 PNL=-291.57€

**🟡 H-CUSTOM-GBMLATE-ANCHURA-MERCADO** — GBM_LATE_15M BUY_YES — anchura de mercado (retorno concurrente de los otros 3 majors) como modificador secundario
  - _Hipótesis_: Detectado 2026-07-09 buscando explicar por qué varias pérdidas de la racha=4 comparten ventana de 15min. Con precios reales (05-09jul, ~20k muestras BTC) se calculó el retorno concurrente de los OTROS 3 majors desde el inicio de la ventana hasta el momento exacto de la decisión (sin fuga de datos, nunca el precio de cierre) y se cruzó con resultados reales de GBM_LATE_15M BUY_YES: n=802, magnitud media de los otros 3 en deciles limpios y monótonos (decil1 IC=-0.146 hit 35% → decil6-9 IC≈+0.20/+0.29 hit 70-80%). NO es redundante con drift_ventana_pct propio del par (correlación solo 0.26); controlando por el drift propio, la anchura sigue añadiendo información (dentro de drift propio>=0, que es el 90% de los casos: IC=0.127 si anchura baja vs IC=0.211 si anchura alta). Funciona en espejo para BUY_NO (shadow, n=685, anchura negativa 0/3→3/3: hit 47.4%→70.3%). CAVEAT importante: NO explica los clusters concretos de racha=4 en vivo — 6 de los 8 eventos históricos tienen anchura ALTA en al menos 2 de las 4 pérdidas (ver notas de sesión 09-Jul), y el backtest directo sobre trades.csv real (n=105-116) es inconcluso/contradictorio (gate anchura>=3 empeora el PnL real, -2.11€ vs +32.32€ sin filtro — probablemente confusión por mezcla de pares en una muestra pequeña, SOL domina ese bucket y SOL es el par MENOS sensible a esta señal: IC 0.132→0.143 apenas cambia, vs ETH 0.038→0.192). Tratar como MODIFICADOR del filtro primario H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT, no como filtro independiente — ver esa hipótesis para la tabla cruzada. Feature `mercado_anchura_pct` añadida 2026-07-09 en shadow_predict.py (_s_gbm_late), puro logging, no cambia ninguna decisión — empieza a acumular desde cero en predicciones nuevas. ACTUALIZACIÓN 12-Jul (desagregación por activo, n fresco): BTC n=35 ic=+0.392 z=+4.90, ETH n=32 ic=+0.353 z=+4.24, XRP n=31 ic=+0.288 z=+3.41 -- los 3 MUY fuertes y consistentes. SOL sigue siendo el único débil (n=30 ic=+0.094 z=+1.10), confirma el caveat ya escrito arriba (SOL insensible). Con XRP incluido, el patrón deja de ser '3 activos + SOL raro' para ser una regla casi universal salvo SOL -- candidato fuerte para boost Kelly restringido a BTC/ETH/XRP (excluir SOL explícitamente) en vez de aplicar a las 4 monedas por igual.
  - _Umbral_: n≥100 forward (feature nueva, sin histórico) e IC>+0.20 en la zona alta (mercado_anchura_pct≥0.056, el decil superior observado)
  - _Acción_: Si confirma con n≥100 IC≥0.20 → boost Kelly cuando mercado_anchura_pct≥0.056 Y prob_yes_modelo≥0.53 (la celda 'doble buena', hit 72.7% retrospectivo). No usar como filtro solo — ver CAVEAT de los clusters de racha en la descripción, y el análisis por-par (SOL insensible) antes de aplicar a las 4 monedas por igual.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.211 > 0.2 con n=8999 PNL=+7172.78€
  - _Datos_: n=8999 IC=+0.211 PNL=+7172.78€

**🟡 H-CUSTOM-OF5M-SMARTMONEY-CONTRARIO** — ORDER_FLOW_5M SOL BUY_NO — smart money EN CONTRA del flujo CEX, no a favor, predice mejor
  - _Hipótesis_: Detectado 11-Jul revisando el backlog quant-desk (reencuadre de ORDER_FLOW_5M). ORDER_FLOW_5M solo dispara BUY_NO (presión vendedora en Binance). Split retrospectivo SOL#5min por smart_money_consensus (ya logueado, nunca cruzado con esta estrategia): cuando el consenso on-chain es BAJISTA (smart_money_consensus<0, 'confirma' la señal CEX) el hit cae a 47.1% (ic_bayes=-0.026, n=17); cuando el consenso es ALCISTA/neutro (smart_money_consensus>=0, CONTRARIO a la señal CEX) el hit sube a 65.0% (ic_bayes=+0.136, n=20, pnl/trade+0.294). Contraintuitivo: la 'confirmación' de dos fuentes empeora, la divergencia mejora. Hipótesis mecánica: el flujo de Binance ya captura la información rápida de 5min; smart money on-chain se mueve más lento (posiciones ya tomadas), así que cuando coincide con el flujo CEX puede ser la MISMA información ya vista dos veces sin dar nada nuevo (o incluso momentum ya agotado), mientras que la divergencia indica que el flujo CEX es el que se está moviendo AHORA sobre información fresca que smart money aún no reflejó. Distinto del cierre 08-Jul del consenso poblacional plano (n=2494, ruido puro) — aquello era agregado sobre TODAS las estrategias; esto es específico del mecanismo de ORDER_FLOW_5M. n=17/20 insuficiente para concluir (regla del proyecto n≥15 es el mínimo absoluto, no un veredicto) — vigilar forward.
  - _Umbral_: n≥40 en cada rama (contrario y alineado) para separar señal de ruido
  - _Acción_: Si confirma con n≥40 e ic_bayes contrario≥+0.08 (con alineado claramente peor) → boost Kelly en ORDER_FLOW_5M BUY_NO cuando smart_money_consensus>=0; considerar filtro/veto cuando smart_money_consensus<0 y muy negativo (posible señal 'ya vista', sin ventaja).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.122 > 0.08 con n=125 PNL=+55.74€
  - _Datos_: n=125 IC=+0.122 PNL=+55.74€

**🟡 H-CUSTOM-ETH15-SIGMA-ACCEL** — GBM_LATE_15M ETH — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: sigma_ewma_delta_pct = (sigma_h_ewma10-sigma_h)/sigma_h. Verificado ad-hoc n=47: cuando la vol reciente (EWMA half-life 10min) supera la ventana plana, hit sube de 59.5% (agregado ETH) a 66.0%, ic_bayes=+0.153. Efecto NO uniforme entre activos (ver hermanas BTC/XRP) -- desagregar por activo es obligatorio, el agregado GBM_LATE_15M diluye esto a ruido.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en ETH#15min
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.083 > 0.08 con n=3268 PNL=+1153.56€
  - _Datos_: n=3268 IC=+0.083 PNL=+1153.56€

**🟡 H-CUSTOM-BTC15-SIGMA-ACCEL** — GBM_LATE_15M BTC — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: mismo mecanismo que ETH (ver H-CUSTOM-ETH15-SIGMA-ACCEL). Verificado ad-hoc n=35: hit sube de 63.6% (agregado BTC) a 68.6%, ic_bayes=+0.176.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en BTC#15min
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.179 > 0.08 con n=3040 PNL=+2319.40€
  - _Datos_: n=3040 IC=+0.179 PNL=+2319.40€

**〰️ H-CUSTOM-XRP15-SIGMA-DECEL** — GBM_LATE_15M XRP — vol DESacelerando (EWMA10<=flat) mejora la señal (signo opuesto a ETH/BTC)
  - _Hipótesis_: 12-Jul: XRP muestra el signo CONTRARIO a ETH/BTC -- cuando la vol reciente cae por debajo de la ventana plana, hit sube de 63.9% (agregado XRP) a 68.8%, ic_bayes=+0.180 (n=48). Cuando acelera, hit CAE a 57.1%. Confirma que este feature no puede tratarse con un umbral global -- cada activo necesita su propio signo. REFUTADA 13-Jul: recalculado con n=61 (más del doble del n original) usando el mismo método riguroso (percentiles + permutación 20k) que confirmó BTC/SOL/ETH -- el signo se INVIRTIÓ: decel (sigma<0) da IC=-0.065 n=21 (malo), accel (sigma>=0) da IC=+0.071 n=40 (bueno). XRP en realidad tiene el MISMO signo que BTC/ETH (sigma alto=bueno), solo que más débil -- coherente con el patrón ganador ya auto-descubierto por postmortem (sigma_ewma_delta_pct>5.563, ic_patron=+0.20 n=18, mismo signo). El hallazgo ad-hoc del 12-Jul con n=48 no replicó con más datos -- probable ruido de una muestra menor/distinta. Ver idea_estrategia_mercado_bajista... no, ver project_sigma_filtro_sol_xrp_no_promociona_13jul (memoria) para el detalle completo.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: REFUTADA -- no implementar kelly_boost por sigma<0 en XRP. El signo correcto es el opuesto (sigma alto=bueno), ya cubierto por el patron_ganador automático de postmortem sobre GBM_LATE_15M#XRP#15min -- no hace falta ninguna acción manual adicional.
  - _Estado_: n=5112 IC=-0.025 PNL=+1434.13€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=5112 IC=-0.025 PNL=+1434.13€

**〰️ H-CUSTOM-SMARTMONEY-FAVORITO-SOL** — FAVORITO_CONFIRMADO SOL — alineado con smart_money_consensus bate ir en contra (REABRE hallazgo cerrado 08-Jul)
  - _Hipótesis_: 12-Jul: el cierre 08-Jul (n=2494, sin desagregar por estrategia/activo) encontro ruido puro. Desagregando por estrategia+activo (mecanismo nuevo): FAVORITO_CONFIRMADO#SOL alineado con smart_money_consensus (|consenso|>0.1, n_wallets>=3) hit=78.4% (n=37) vs contrario hit=52.4% (n=42), z=+2.41. GBM_LATE_15M tambien muestra el mismo signo en BTC/ETH/XRP (z=0.86-1.61, mas debil) pero SOL plano ahi -- inconsistencia entre estrategias que hay que entender antes de actuar.
  - _Umbral_: n>=40 por lado y z>=2
  - _Acción_: Si confirma con n>=40 y z>=2 -> considerar boost condicionado a alineacion con smart_money_consensus en FAVORITO_CONFIRMADO#SOL
  - _Estado_: n=690 IC=+0.074 PNL=-50.44€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=690 IC=+0.074 PNL=-50.44€

**🟡 H-CUSTOM-FAVORITO-SOL-ALTACONVICCION** — FAVORITO_CONFIRMADO SOL BUY_YES alta conviccion (py_entrada alto) — UNICO caso positivo en fill-ability de hoy
  - _Hipótesis_: 12-Jul: auditoria de fill-ability de las 8 candidatas encontro las 8 negativas en agregado. Pero desagregando FAVORITO_CONFIRMADO por activo (mecanismo nuevo, no mirado hasta hoy): SOL#BUY_YES con py_entrada>=0.665-0.695 da pnl/trade POSITIVO en el subconjunto fillable real (+0.12 a +0.41 EUR/trade, n=6-17 segun el corte exacto) -- unico resultado positivo de toda la auditoria de candidatas. n todavia bajo, necesita mas dato antes de proponer nada.
  - _Umbral_: n>=40 y pnl/trade fillable > 0 sostenido
  - _Acción_: Seguir acumulando snapshots candidato_evaluacion para SOL#15min#BUY_YES en FAVORITO_CONFIRMADO; re-evaluar fill-ability con n>=40 antes de proponer whitelist
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.244 > 0.08 con n=4890 PNL=-380.10€
  - _Datos_: n=4890 IC=+0.244 PNL=-380.10€

**〰️ H-CUSTOM-GBM18H-XRP-EXCEPCION** — UPDOWN_GBM XRP a las 18h UTC -- puede estar mal incluida en el blacklist horario global
  - _Hipótesis_: 12-Jul: gbm_blacklist_hours_auto=[9,10,18] bloquea GBM en las 4 monedas a las 18h. Desagregando por activo (h9/h10 no tienen dato retrospectivo -- el propio blacklist impide que se genere): BTC ic=-0.140 (n=48), ETH ic=-0.136 (n=42), SOL ic=-0.167 (n=22) consistentes con el bloqueo, pero XRP ic=+0.100 (n=23) -- signo OPUESTO. El bloqueo agregado puede estar sobre-bloqueando XRP especificamente.
  - _Umbral_: n>=40 y IC>0.08
  - _Acción_: Si confirma con n>=40 IC>0.08 -> considerar excepcion de XRP en gbm_blacklist_hours_auto para la hora 18 (shadow puro, UPDOWN_GBM no esta live)
  - _Estado_: n=70 IC=+0.028 PNL=+10.59€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=70 IC=+0.028 PNL=+10.59€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.103 n=1758) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=1758 IC=+0.103 PNL=+389.87€

**🟡 H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: n>=40 y IC>=0.08
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.309 > 0.08 con n=464 PNL=+133.10€
  - _Datos_: n=464 IC=+0.309 PNL=+133.10€

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.411 n=572) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=572 IC=+0.411 PNL=+818.84€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=14378 IC=+0.186 PNL=-1469.87€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=14378 IC=+0.186 PNL=-1469.87€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.226 > 0.1 con n=235 PNL=+159.44€
  - _Datos_: n=235 IC=+0.226 PNL=+159.44€
