# Hipótesis automáticas — 2026-10-27 17:23 UTC
_Generado por shadow_postmortem.py sobre 1080255 resoluciones (PNL=+142481.19€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **PATRÓN** `py_entrada` > `0.515` → IC=+0.228 (n=851)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.515 (IC base=+0.135)

- **PATRÓN** `n_total_lado` > `64.0` → IC=+0.183 (n=301)

  - _Acción_: Kelly boost +0.92€ cuando `n_total_lado` > 64.0 (IC base=+0.135)

- **PATRÓN** `banda_hit_calibrado` > `0.618` → IC=+0.263 (n=596)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.618 (IC base=+0.135)

- **PATRÓN** `banda_z` > `8.922` → IC=+0.213 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 8.922 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.161 (n=325)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 17.0 (IC base=+0.135)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.137 (n=436)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 8.0 (IC base=+0.135)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.151 (n=973)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `2653.7599` → IC=+0.139 (n=798)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 2653.7599 (IC base=+0.135)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **PATRÓN** `py_entrada` > `0.515` → IC=+0.224 (n=740)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.515 (IC base=+0.140)

- **PATRÓN** `n_total_lado` > `68.0` → IC=+0.200 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 68.0 (IC base=+0.140)

- **PATRÓN** `banda_hit_calibrado` > `0.6153` → IC=+0.255 (n=509)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6153 (IC base=+0.140)

- **PATRÓN** `banda_z` > `9.307` → IC=+0.197 (n=255)

  - _Acción_: Kelly boost +0.98€ cuando `banda_z` > 9.307 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.170 (n=274)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.140)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.140 (n=365)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 8.0 (IC base=+0.140)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.148 (n=874)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `2713.1399` → IC=+0.141 (n=764)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 2713.1399 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `9643.6217` → IC=+0.129 (n=208)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 9643.6217 (IC base=+0.015)

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
- **FILTRO** `restante_s_al_confirmar` < `138.58` → IC=-0.210 (n=10723)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 138.58
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=32173)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `127.45` → IC=-0.261 (n=1151)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 127.45
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=3453)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `119.89` → IC=-0.294 (n=1138)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 119.89
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=3416)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `160.59` → IC=-0.241 (n=2866)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 160.59
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=8601)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `132.83` → IC=-0.259 (n=2072)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 132.83
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=6219)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.213 (n=23545)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.106)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.126 (n=4581)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.01 (IC base=+0.106)

- **PATRÓN** `libro_liquidez` > `8804.9286` → IC=+0.165 (n=2102)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 8804.9286 (IC base=+0.106)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.127 (n=20132)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.131 (n=24648)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 7.0 (IC base=+0.125)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.226 (n=18812)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.146 (n=7584)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.01 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `6836.9618` → IC=+0.155 (n=2935)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 6836.9618 (IC base=+0.125)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.191 (n=2104)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.184)

- **PATRÓN** `py_entrada` > `0.765` → IC=+0.364 (n=696)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.765 (IC base=+0.184)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.187 (n=2575)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.01 (IC base=+0.184)

- **PATRÓN** `libro_liquidez` > `16453.9907` → IC=+0.184 (n=668)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 16453.9907 (IC base=+0.184)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.187 (n=1843)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 7.0 (IC base=+0.181)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.184 (n=2064)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 17.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` < `0.295` → IC=+0.312 (n=981)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.295 (IC base=+0.181)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.183 (n=2643)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.01 (IC base=+0.181)

- **PATRÓN** `libro_liquidez` > `16197.5868` → IC=+0.187 (n=682)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 16197.5868 (IC base=+0.181)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.61` → IC=+0.174 (n=511)

  - _Acción_: Kelly boost +0.87€ cuando `py_entrada` > 0.61 (IC base=+0.079)

- **PATRÓN** `libro_liquidez` > `7489.3548` → IC=+0.160 (n=98)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 7489.3548 (IC base=+0.079)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.139 (n=1209)

  - _Acción_: Kelly boost +0.70€ cuando `py_entrada` < 0.44 (IC base=+0.082)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.167 (n=4575)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.161)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.164 (n=3881)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 15.0 (IC base=+0.161)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.377 (n=1477)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.161)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.216 (n=2048)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.207)

- **PATRÓN** `py_entrada` < `0.265` → IC=+0.351 (n=768)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.265 (IC base=+0.207)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.211 (n=2382)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.207)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.148 (n=1156)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 5.0 (IC base=+0.145)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.149 (n=987)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 15.0 (IC base=+0.145)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.263 (n=373)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.145)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.151 (n=913)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `2214.1072` → IC=+0.156 (n=501)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 2214.1072 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.162 (n=152)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.069)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.254 (n=880)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.226)

- **PATRÓN** `py_entrada` > `0.83` → IC=+0.421 (n=1230)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.83 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.147 (n=1334)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 7.0 (IC base=+0.146)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.155 (n=699)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 7.0 (IC base=+0.146)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.285 (n=646)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.146)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.146 (n=886)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.01 (IC base=+0.146)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.142 (n=149)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 18.0 (IC base=+0.091)

- **PATRÓN** `py_entrada` > `0.555` → IC=+0.171 (n=429)

  - _Acción_: Kelly boost +0.85€ cuando `py_entrada` > 0.555 (IC base=+0.091)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.132 (n=1292)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 5.0 (IC base=+0.124)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.244 (n=416)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.124)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `10.0` → IC=-0.297 (n=72)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.225 (n=140)

- **FILTRO** `py_entrada` > `0.825` → IC=-0.343 (n=49)

  - _Acción_: SKIP cuando `py_entrada` > 0.825
  - _Potencial_: sin este filtro IC_bueno=-0.221 (n=163)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.203 (n=20173)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.201 (n=17136)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.233 (n=8298)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `4837.3339` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4837.3339 (IC base=+0.199)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.182 (n=2184)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 15.0 (IC base=+0.178)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.180 (n=3888)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 15.0 (IC base=+0.178)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.182 (n=4498)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` < 0.73 (IC base=+0.178)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.179 (n=3812)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` > 0.71 (IC base=+0.178)

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

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.220 (n=2505)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.224 (n=1680)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.218)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.298 (n=841)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.218)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.186 (n=4546)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.181 (n=3874)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 15.0 (IC base=+0.179)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.188 (n=3546)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` > 0.71 (IC base=+0.179)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.255 (n=3907)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.247)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.247 (n=3320)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.247)

- **PATRÓN** `py_entrada` > `0.79` → IC=+0.360 (n=1302)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.79 (IC base=+0.247)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.190 (n=4463)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.187)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.191 (n=3814)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 15.0 (IC base=+0.187)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.192 (n=3306)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.71 (IC base=+0.187)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.431 (n=850)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.426)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.426 (n=860)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.426)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.440 (n=865)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.426)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.432 (n=898)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.426)

- **PATRÓN** `libro_liquidez` > `4330.8939` → IC=+0.440 (n=552)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4330.8939 (IC base=+0.426)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.435 (n=337)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.437)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.440 (n=347)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.437)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.449 (n=371)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.437)

- **PATRÓN** `libro_liquidez` > `20878.8113` → IC=+0.447 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 20878.8113 (IC base=+0.437)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.437 (n=330)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.428)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.429 (n=337)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.428)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.441 (n=337)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.428)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.433 (n=374)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.428)

- **PATRÓN** `libro_liquidez` > `4626.5104` → IC=+0.446 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4626.5104 (IC base=+0.428)

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
- **FILTRO** `py_entrada` > `0.765` → IC=-0.294 (n=32)

  - _Acción_: SKIP cuando `py_entrada` > 0.765
  - _Potencial_: sin este filtro IC_bueno=-0.143 (n=12)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=28)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.208 (n=26106)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.201)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.247 (n=26419)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.201)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.191 (n=4496)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 17.0 (IC base=+0.185)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.185 (n=8390)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 12.0 (IC base=+0.185)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.198 (n=11833)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` > 0.71 (IC base=+0.185)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.228 (n=5455)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.226 (n=5369)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.225)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.287 (n=3787)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.225)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.188 (n=4480)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 17.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.201 (n=9229)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.181)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.835` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.835
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.230 (n=5494)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.219)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.219 (n=4210)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.219)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.274 (n=3715)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.219)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.207 (n=10042)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.262 (n=3876)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.208 (n=4341)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.199 (n=4373)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.248 (n=4575)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.198)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.193 (n=9446)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.141 (n=9527)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `3.66` → IC=+0.137 (n=11462)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 3.66 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.197 (n=4657)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.119)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.146 (n=4337)

  - _Acción_: Kelly boost +0.73€ cuando `restante_min` > 4.96 (IC base=+0.119)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.128 (n=5745)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 7.0 (IC base=+0.119)

- **PATRÓN** `lag_apertura_s` < `2.67` → IC=+0.146 (n=4314)

  - _Acción_: Kelly boost +0.73€ cuando `lag_apertura_s` < 2.67 (IC base=+0.119)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.190 (n=4789)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.38 (IC base=+0.114)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.136 (n=5190)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.96 (IC base=+0.114)

- **PATRÓN** `lag_apertura_s` < `3.28` → IC=+0.136 (n=5774)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 3.28 (IC base=+0.114)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.304 (n=1784)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.295)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.386 (n=613)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.295)

- **PATRÓN** `libro_liquidez` > `3829.7681` → IC=+0.295 (n=761)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3829.7681 (IC base=+0.295)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.290 (n=811)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.281)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.362 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.281)

- **PATRÓN** `libro_liquidez` > `5084.4032` → IC=+0.298 (n=350)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5084.4032 (IC base=+0.281)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.328 (n=580)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.301)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.302 (n=847)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.301)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.396 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.301)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.301 (n=960)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.301)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.341 (n=86)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.343)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.375 (n=86)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.343)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.387 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.343)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.345 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.343)

- **PATRÓN** `libro_liquidez` > `761.0655` → IC=+0.372 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 761.0655 (IC base=+0.343)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.448 (n=825)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.444)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.445 (n=810)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.444)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.451 (n=788)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.444)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.439 (n=393)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.436)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.437 (n=267)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.436)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.438 (n=400)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.436)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.439 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.436)

- **PATRÓN** `libro_liquidez` > `5459.2656` → IC=+0.445 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5459.2656 (IC base=+0.436)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.470 (n=132)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.453)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.455 (n=377)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.453)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.455 (n=353)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.453)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.452 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.453)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min
- **PATRÓN** `hora_utc` > `13.0` → IC=+0.389 (n=25)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 13.0 (IC base=+0.398)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.393 (n=26)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 13.0 (IC base=+0.398)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.431 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.398)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION
- **FILTRO** `hora_utc` < `5.0` → IC=-0.283 (n=21)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.210 (n=98)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.308 (n=24)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.201 (n=95)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.238 (n=59)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.210 (n=60)

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
  - _Potencial_: sin este filtro IC_bueno=-0.210 (n=98)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.308 (n=24)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.201 (n=95)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.238 (n=59)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.210 (n=60)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4717` → IC=+0.140 (n=14735)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.4717 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.125 (n=14892)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 6.0 (IC base=+0.122)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.126 (n=10293)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 12.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` > `0.9799` → IC=+0.247 (n=4912)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9799 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` > `0.775` → IC=+0.275 (n=814)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.775 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` < `0.3656` → IC=+0.260 (n=4216)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3656 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.632` → IC=+0.181 (n=7342)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 3.632 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` > `0.6211` → IC=+0.266 (n=4314)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6211 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` > `0.3043` → IC=+0.246 (n=1516)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3043 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` > `2.3564` → IC=+0.231 (n=4774)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3564 (IC base=+0.122)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.130 (n=7596)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.01 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `4513.6462` → IC=+0.151 (n=4912)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 4513.6462 (IC base=+0.122)

- **PATRÓN** `ibs_20min` < `0.5673` → IC=+0.142 (n=18267)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` < 0.5673 (IC base=+0.077)

- **PATRÓN** `dist_vwap_pct` > `0.5999` → IC=+0.188 (n=1185)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.5999 (IC base=+0.077)

- **PATRÓN** `volumen_regimen` < `0.8669` → IC=+0.187 (n=4847)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 0.8669 (IC base=+0.077)

- **PATRÓN** `volumen_pendiente_norm` > `0.2977` → IC=+0.230 (n=1802)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2977 (IC base=+0.077)

- **PATRÓN** `volumen_spike_ratio` > `2.6929` → IC=+0.207 (n=4112)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6929 (IC base=+0.077)

- **PATRÓN** `ballena_activa_n` < `105.0` → IC=+0.222 (n=12208)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 105.0 (IC base=+0.077)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.206 (n=1066)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.205)

- **PATRÓN** `drift_60min` |x|≤ `0.3537` → IC=+0.207 (n=3191)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3537 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.217 (n=1187)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.205)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.210 (n=2141)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.205)

- **PATRÓN** `ibs_20min` > `0.9834` → IC=+0.281 (n=1447)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9834 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.7` → IC=+0.283 (n=1412)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.7 (IC base=+0.205)

- **PATRÓN** `volumen_pendiente_norm` > `0.2844` → IC=+0.261 (n=416)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2844 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` > `1.5505` → IC=+0.208 (n=2725)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5505 (IC base=+0.205)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.220 (n=3463)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.205)

- **PATRÓN** `libro_liquidez` > `2050.69` → IC=+0.207 (n=1064)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2050.69 (IC base=+0.205)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.224 (n=1974)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.205)

- **PATRÓN** `sigma_h` < `0.0091` → IC=+0.242 (n=2711)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0091 (IC base=+0.239)

- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.242 (n=1229)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0082 (IC base=+0.239)

- **PATRÓN** `drift_60min` |x|≤ `0.0873` → IC=+0.275 (n=905)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0873 (IC base=+0.239)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.245 (n=2498)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.239)

- **PATRÓN** `ibs_20min` < `0.5444` → IC=+0.259 (n=2711)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5444 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` < `0.0962` → IC=+0.244 (n=2444)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0962 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` > `0.2942` → IC=+0.258 (n=374)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2942 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` < `1.4468` → IC=+0.242 (n=857)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4468 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` > `1.8781` → IC=+0.242 (n=1713)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8781 (IC base=+0.239)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.242 (n=3083)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.239)

- **PATRÓN** `libro_liquidez` > `1544.9886` → IC=+0.242 (n=2422)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1544.9886 (IC base=+0.239)

- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.238 (n=1148)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 8.0 (IC base=+0.239)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.240 (n=878)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.229)

- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.230 (n=1196)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0051 (IC base=+0.229)

- **PATRÓN** `drift_60min` |x|≤ `0.1061` → IC=+0.257 (n=1158)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1061 (IC base=+0.229)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.240 (n=2753)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.229)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.229 (n=1877)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.229)

- **PATRÓN** `ibs_20min` > `0.9322` → IC=+0.273 (n=878)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9322 (IC base=+0.229)

- **PATRÓN** `dist_vwap_pct` > `0.1871` → IC=+0.236 (n=1242)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1871 (IC base=+0.229)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.219` → IC=+0.266 (n=391)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.219 (IC base=+0.229)

- **PATRÓN** `volumen_regimen` < `1.231` → IC=+0.229 (n=2632)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.231 (IC base=+0.229)

- **PATRÓN** `volumen_regimen` > `0.6235` → IC=+0.233 (n=2631)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6235 (IC base=+0.229)

- **PATRÓN** `volumen_pendiente_norm` > `0.28` → IC=+0.277 (n=374)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.28 (IC base=+0.229)

- **PATRÓN** `volumen_spike_ratio` > `2.4315` → IC=+0.261 (n=865)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4315 (IC base=+0.229)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.151 (n=2766)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0059 (IC base=+0.130)

- **PATRÓN** `drift_60min` |x|≤ `0.077` → IC=+0.165 (n=923)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.077 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.157 (n=1032)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 17.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` < `0.7206` → IC=+0.170 (n=2766)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.7206 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.919` → IC=+0.145 (n=452)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 10.919 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.076` → IC=+0.136 (n=2523)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 4.076 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` < `1.2085` → IC=+0.140 (n=2766)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 1.2085 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` > `0.0967` → IC=+0.153 (n=1011)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` > 0.0967 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` < `2.455` → IC=+0.140 (n=2643)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 2.455 (IC base=+0.130)

- **PATRÓN** `ballena_activa_n` < `209.0` → IC=+0.173 (n=1135)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 209.0 (IC base=+0.130)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0123` → IC=+0.215 (n=1114)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0123 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.199 (n=3506)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.193)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.264 (n=1286)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.173` → IC=+0.278 (n=714)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.173 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` < `0.0966` → IC=+0.197 (n=2971)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` < 0.0966 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` > `0.353` → IC=+0.222 (n=433)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.353 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` > `2.7105` → IC=+0.211 (n=1472)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7105 (IC base=+0.193)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.198 (n=3986)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.04 (IC base=+0.193)

- **PATRÓN** `libro_liquidez` > `2032.4484` → IC=+0.202 (n=1113)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2032.4484 (IC base=+0.193)

- **PATRÓN** `sigma_h` < `0.0108` → IC=+0.223 (n=2665)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0108 (IC base=+0.217)

- **PATRÓN** `drift_60min` |x|≤ `0.1764` → IC=+0.233 (n=1330)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1764 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.241 (n=1133)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.217)

- **PATRÓN** `ibs_20min` < `0.0306` → IC=+0.271 (n=1008)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0306 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.198` → IC=+0.257 (n=356)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.198 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` > `0.3492` → IC=+0.264 (n=435)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3492 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` > `2.7601` → IC=+0.224 (n=1308)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7601 (IC base=+0.217)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.222 (n=1518)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.217)

- **PATRÓN** `libro_liquidez` > `1920.181` → IC=+0.218 (n=1370)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1920.181 (IC base=+0.217)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.217 (n=2493)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 21.0 (IC base=+0.217)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.142 (n=163)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=4031)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.159 (n=579)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0037 (IC base=+0.058)

- **PATRÓN** `ibs_20min` > `0.9529` → IC=+0.233 (n=578)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9529 (IC base=+0.058)

- **PATRÓN** `dist_vwap_pct` > `0.137` → IC=+0.336 (n=395)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.137 (IC base=+0.058)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.17` → IC=+0.196 (n=1254)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 5.17 (IC base=+0.058)

- **PATRÓN** `volumen_regimen` < `0.8656` → IC=+0.329 (n=448)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8656 (IC base=+0.058)

- **PATRÓN** `volumen_regimen` > `0.691` → IC=+0.340 (n=599)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.691 (IC base=+0.058)

- **PATRÓN** `volumen_pendiente_norm` < `0.0777` → IC=+0.330 (n=432)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0777 (IC base=+0.058)

- **PATRÓN** `volumen_pendiente_norm` > `0.3037` → IC=+0.342 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3037 (IC base=+0.058)

- **PATRÓN** `volumen_spike_ratio` < `1.4167` → IC=+0.350 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4167 (IC base=+0.058)

- **PATRÓN** `volumen_spike_ratio` > `2.2549` → IC=+0.336 (n=297)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2549 (IC base=+0.058)

- **PATRÓN** `ballena_activa_n` < `144.0` → IC=+0.334 (n=661)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 144.0 (IC base=+0.058)

- **PATRÓN** `ibs_20min` < `0.092` → IC=+0.183 (n=1049)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.092 (IC base=+0.041)

- **PATRÓN** `dist_vwap_pct` > `0.7225` → IC=+0.154 (n=241)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` > 0.7225 (IC base=+0.041)

- **PATRÓN** `volumen_regimen` < `0.8409` → IC=+0.152 (n=1281)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.8409 (IC base=+0.041)

- **PATRÓN** `volumen_pendiente_norm` > `0.2863` → IC=+0.210 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2863 (IC base=+0.041)

- **PATRÓN** `volumen_spike_ratio` < `1.7843` → IC=+0.140 (n=1232)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.7843 (IC base=+0.041)

- **PATRÓN** `volumen_spike_ratio` > `2.1656` → IC=+0.161 (n=838)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 2.1656 (IC base=+0.041)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.178 (n=116)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=616)

- **FILTRO** `ibs_20min` > `0.2121` → IC=-0.132 (n=3943)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2121
  - _Potencial_: sin este filtro IC_bueno=+0.150 (n=1947)

- **FILTRO** `sigma_ewma_delta_pct` > `8.575` → IC=-0.231 (n=627)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.575
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=5263)

- **PATRÓN** `ibs_20min` > `0.7632` → IC=+0.173 (n=249)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` > 0.7632 (IC base=+0.026)

- **PATRÓN** `dist_vwap_pct` > `0.9993` → IC=+0.287 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9993 (IC base=+0.026)

- **PATRÓN** `dist_vwap_pct` < `0.4892` → IC=+0.273 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4892 (IC base=+0.026)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.37` → IC=+0.130 (n=255)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` > 2.37 (IC base=+0.026)

- **PATRÓN** `volumen_regimen` > `1.0359` → IC=+0.305 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0359 (IC base=+0.026)

- **PATRÓN** `volumen_pendiente_norm` < `0.1553` → IC=+0.287 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1553 (IC base=+0.026)

- **PATRÓN** `volumen_spike_ratio` < `2.4948` → IC=+0.296 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4948 (IC base=+0.026)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.276 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 37.0 (IC base=+0.026)

- **PATRÓN** `ibs_20min` < `0.2121` → IC=+0.150 (n=1947)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.2121 (IC base=-0.039)

- **PATRÓN** `dist_vwap_pct` > `0.2769` → IC=+0.280 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2769 (IC base=-0.039)

- **PATRÓN** `volumen_regimen` < `0.6941` → IC=+0.303 (n=363)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6941 (IC base=-0.039)

- **PATRÓN** `volumen_pendiente_norm` < `0.1046` → IC=+0.288 (n=678)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1046 (IC base=-0.039)

- **PATRÓN** `volumen_pendiente_norm` > `0.0793` → IC=+0.289 (n=363)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0793 (IC base=-0.039)

- **PATRÓN** `volumen_spike_ratio` < `2.4341` → IC=+0.305 (n=757)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4341 (IC base=-0.039)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.5999` → IC=-0.183 (n=1098)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.5999
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=3295)

- **FILTRO** `ibs_20min` < `0.7624` → IC=-0.152 (n=2899)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7624
  - _Potencial_: sin este filtro IC_bueno=+0.106 (n=1494)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.166 (n=1041)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=3352)

- **FILTRO** `ibs_20min` > `0.749` → IC=-0.202 (n=1565)

  - _Acción_: SKIP cuando `ibs_20min` > 0.749
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=4696)

- **PATRÓN** `dist_vwap_pct` > `1.0292` → IC=+0.343 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0292 (IC base=-0.064)

- **PATRÓN** `dist_vwap_pct` < `0.1794` → IC=+0.310 (n=650)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1794 (IC base=-0.064)

- **PATRÓN** `volumen_regimen` > `0.7043` → IC=+0.319 (n=704)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7043 (IC base=-0.064)

- **PATRÓN** `volumen_pendiente_norm` < `0.1024` → IC=+0.306 (n=744)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1024 (IC base=-0.064)

- **PATRÓN** `volumen_spike_ratio` < `1.4208` → IC=+0.322 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4208 (IC base=-0.064)

- **PATRÓN** `volumen_spike_ratio` > `1.8466` → IC=+0.310 (n=510)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8466 (IC base=-0.064)

- **PATRÓN** `dist_vwap_pct` > `0.8005` → IC=+0.286 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8005 (IC base=-0.003)

- **PATRÓN** `volumen_regimen` < `0.6466` → IC=+0.266 (n=587)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6466 (IC base=-0.003)

- **PATRÓN** `volumen_regimen` > `1.0685` → IC=+0.284 (n=798)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0685 (IC base=-0.003)

- **PATRÓN** `volumen_pendiente_norm` > `0.1687` → IC=+0.289 (n=448)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1687 (IC base=-0.003)

- **PATRÓN** `volumen_spike_ratio` < `2.1776` → IC=+0.264 (n=1440)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1776 (IC base=-0.003)

- **PATRÓN** `volumen_spike_ratio` > `1.4313` → IC=+0.263 (n=1636)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4313 (IC base=-0.003)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.01` → IC=+0.211 (n=6426)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.01 (IC base=+0.094)

- **PATRÓN** `ibs_20min` > `0.3112` → IC=+0.167 (n=19264)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.3112 (IC base=+0.094)

- **PATRÓN** `dist_vwap_pct` > `0.9329` → IC=+0.302 (n=1383)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9329 (IC base=+0.094)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.574` → IC=+0.165 (n=8624)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 3.574 (IC base=+0.094)

- **PATRÓN** `volumen_regimen` < `1.173` → IC=+0.266 (n=7100)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.173 (IC base=+0.094)

- **PATRÓN** `volumen_regimen` > `0.6911` → IC=+0.274 (n=6343)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6911 (IC base=+0.094)

- **PATRÓN** `volumen_pendiente_norm` > `0.2403` → IC=+0.284 (n=2123)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2403 (IC base=+0.094)

- **PATRÓN** `volumen_spike_ratio` > `2.6558` → IC=+0.278 (n=3762)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6558 (IC base=+0.094)

- **PATRÓN** `ballena_activa_n` < `91.0` → IC=+0.301 (n=10880)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 91.0 (IC base=+0.094)

- **PATRÓN** `sigma_h` > `0.0096` → IC=+0.153 (n=6197)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` > 0.0096 (IC base=+0.076)

- **PATRÓN** `ibs_20min` < `0.6505` → IC=+0.146 (n=18592)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.6505 (IC base=+0.076)

- **PATRÓN** `volumen_regimen` < `0.7049` → IC=+0.267 (n=2628)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7049 (IC base=+0.076)

- **PATRÓN** `volumen_regimen` > `1.1965` → IC=+0.265 (n=1991)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1965 (IC base=+0.076)

- **PATRÓN** `volumen_pendiente_norm` > `0.2954` → IC=+0.320 (n=1293)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2954 (IC base=+0.076)

- **PATRÓN** `volumen_spike_ratio` < `1.5822` → IC=+0.293 (n=3808)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5822 (IC base=+0.076)

- **PATRÓN** `volumen_spike_ratio` > `2.2846` → IC=+0.286 (n=3923)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2846 (IC base=+0.076)

- **PATRÓN** `ballena_activa_n` < `76.0` → IC=+0.297 (n=8613)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 76.0 (IC base=+0.076)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.5796` → IC=-0.148 (n=2621)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5796
  - _Potencial_: sin este filtro IC_bueno=+0.201 (n=2621)

- **FILTRO** `ibs_20min` > `0.7296` → IC=-0.219 (n=1124)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7296
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=3380)

- **FILTRO** `sigma_ewma_delta_pct` > `4.322` → IC=-0.220 (n=977)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.322
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=3527)

- **PATRÓN** `ibs_20min` > `0.9258` → IC=+0.329 (n=1311)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9258 (IC base=+0.026)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.884` → IC=+0.219 (n=935)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.884 (IC base=+0.026)

- **PATRÓN** `volumen_pendiente_norm` > `0.2299` → IC=+0.317 (n=343)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2299 (IC base=+0.026)

- **PATRÓN** `volumen_spike_ratio` < `1.4484` → IC=+0.261 (n=571)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4484 (IC base=+0.026)

- **PATRÓN** `volumen_spike_ratio` > `2.2635` → IC=+0.289 (n=776)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2635 (IC base=+0.026)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.304 (n=1143)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.026)

- **PATRÓN** `ibs_20min` < `0.1687` → IC=+0.161 (n=1127)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.1687 (IC base=-0.029)

- **PATRÓN** `volumen_pendiente_norm` < `0.0739` → IC=+0.415 (n=599)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0739 (IC base=-0.029)

- **PATRÓN** `volumen_spike_ratio` < `2.7127` → IC=+0.409 (n=679)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.7127 (IC base=-0.029)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.405 (n=626)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 19.0 (IC base=-0.029)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.1662` → IC=+0.217 (n=847)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1662 (IC base=+0.020)

- **PATRÓN** `volumen_regimen` < `1.1961` → IC=+0.202 (n=1891)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1961 (IC base=+0.020)

- **PATRÓN** `volumen_regimen` > `0.6924` → IC=+0.206 (n=1690)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6924 (IC base=+0.020)

- **PATRÓN** `volumen_pendiente_norm` > `0.2788` → IC=+0.246 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2788 (IC base=+0.020)

- **PATRÓN** `volumen_spike_ratio` < `1.4254` → IC=+0.228 (n=622)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4254 (IC base=+0.020)

- **PATRÓN** `volumen_spike_ratio` > `2.473` → IC=+0.202 (n=622)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.473 (IC base=+0.020)

- **PATRÓN** `ballena_activa_n` < `268.0` → IC=+0.237 (n=1240)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 268.0 (IC base=+0.020)

- **PATRÓN** `volumen_regimen` < `1.1716` → IC=+0.235 (n=1266)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1716 (IC base=-0.003)

- **PATRÓN** `volumen_regimen` > `0.6206` → IC=+0.239 (n=1266)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6206 (IC base=-0.003)

- **PATRÓN** `volumen_pendiente_norm` > `0.2728` → IC=+0.301 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2728 (IC base=-0.003)

- **PATRÓN** `volumen_spike_ratio` < `1.5384` → IC=+0.248 (n=534)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5384 (IC base=-0.003)

- **PATRÓN** `volumen_spike_ratio` > `2.1619` → IC=+0.249 (n=552)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1619 (IC base=-0.003)

- **PATRÓN** `ballena_activa_n` < `195.0` → IC=+0.243 (n=407)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 195.0 (IC base=-0.003)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0122` → IC=+0.323 (n=924)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0122 (IC base=+0.273)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.282 (n=2769)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.273)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.315 (n=1485)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.273)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.706` → IC=+0.305 (n=908)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.706 (IC base=+0.273)

- **PATRÓN** `volumen_pendiente_norm` < `0.0976` → IC=+0.286 (n=2421)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0976 (IC base=+0.273)

- **PATRÓN** `volumen_spike_ratio` > `1.6097` → IC=+0.279 (n=2681)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6097 (IC base=+0.273)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.283 (n=3284)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.273)

- **PATRÓN** `libro_liquidez` > `2032.4484` → IC=+0.289 (n=923)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2032.4484 (IC base=+0.273)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.294 (n=1680)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 17.0 (IC base=+0.273)

- **PATRÓN** `sigma_h` > `0.0086` → IC=+0.321 (n=1626)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0086 (IC base=+0.294)

- **PATRÓN** `drift_60min` |x|≤ `0.1782` → IC=+0.314 (n=1072)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1782 (IC base=+0.294)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.319 (n=924)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.294)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.297 (n=845)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.294)

- **PATRÓN** `ibs_20min` < `0.375` → IC=+0.295 (n=2437)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.375 (IC base=+0.294)

- **PATRÓN** `ibs_20min` > `0.2711` → IC=+0.302 (n=1105)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2711 (IC base=+0.294)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.402` → IC=+0.304 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.402 (IC base=+0.294)

- **PATRÓN** `volumen_pendiente_norm` < `0.1976` → IC=+0.294 (n=2391)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1976 (IC base=+0.294)

- **PATRÓN** `volumen_pendiente_norm` > `0.3431` → IC=+0.310 (n=392)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3431 (IC base=+0.294)

- **PATRÓN** `volumen_spike_ratio` < `1.7322` → IC=+0.299 (n=1028)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7322 (IC base=+0.294)

- **PATRÓN** `volumen_spike_ratio` > `2.6992` → IC=+0.307 (n=1059)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6992 (IC base=+0.294)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.296 (n=1231)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.294)

- **PATRÓN** `libro_liquidez` > `1922.908` → IC=+0.305 (n=1104)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1922.908 (IC base=+0.294)

- **PATRÓN** `ballena_activa_n` < `10.0` → IC=+0.301 (n=1074)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 10.0 (IC base=+0.294)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7352` → IC=-0.184 (n=1183)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7352
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=3557)

- **PATRÓN** `ibs_20min` > `0.8665` → IC=+0.166 (n=1145)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.8665 (IC base=+0.026)

- **PATRÓN** `dist_vwap_pct` > `0.1505` → IC=+0.234 (n=845)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1505 (IC base=+0.026)

- **PATRÓN** `dist_vwap_pct` < `0.3624` → IC=+0.233 (n=1605)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3624 (IC base=+0.026)

- **PATRÓN** `volumen_regimen` < `1.0083` → IC=+0.238 (n=1431)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0083 (IC base=+0.026)

- **PATRÓN** `volumen_regimen` > `0.6671` → IC=+0.233 (n=1452)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6671 (IC base=+0.026)

- **PATRÓN** `volumen_pendiente_norm` < `0.1621` → IC=+0.235 (n=1716)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1621 (IC base=+0.026)

- **PATRÓN** `volumen_pendiente_norm` > `0.1021` → IC=+0.242 (n=517)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1021 (IC base=+0.026)

- **PATRÓN** `volumen_spike_ratio` < `2.4657` → IC=+0.238 (n=1573)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4657 (IC base=+0.026)

- **PATRÓN** `ballena_activa_n` < `119.0` → IC=+0.253 (n=1602)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 119.0 (IC base=+0.026)

- **PATRÓN** `volumen_regimen` < `1.1942` → IC=+0.241 (n=1128)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1942 (IC base=+0.001)

- **PATRÓN** `volumen_pendiente_norm` < `0.1015` → IC=+0.247 (n=1046)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1015 (IC base=+0.001)

- **PATRÓN** `volumen_pendiente_norm` > `0.2847` → IC=+0.301 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2847 (IC base=+0.001)

- **PATRÓN** `volumen_spike_ratio` < `1.793` → IC=+0.272 (n=717)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.793 (IC base=+0.001)

- **PATRÓN** `volumen_spike_ratio` > `2.4421` → IC=+0.259 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4421 (IC base=+0.001)

- **PATRÓN** `ballena_activa_n` < `121.0` → IC=+0.262 (n=1087)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 121.0 (IC base=+0.001)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7547` → IC=-0.227 (n=2009)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7547
  - _Potencial_: sin este filtro IC_bueno=+0.312 (n=2012)

- **FILTRO** `ibs_20min` > `0.6386` → IC=-0.233 (n=976)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6386
  - _Potencial_: sin este filtro IC_bueno=+0.126 (n=2934)

- **FILTRO** `sigma_ewma_delta_pct` > `8.409` → IC=-0.249 (n=449)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.409
  - _Potencial_: sin este filtro IC_bueno=+0.074 (n=3461)

- **PATRÓN** `ibs_20min` > `0.7547` → IC=+0.312 (n=2012)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7547 (IC base=+0.043)

- **PATRÓN** `dist_vwap_pct` > `0.2123` → IC=+0.342 (n=869)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2123 (IC base=+0.043)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.367` → IC=+0.189 (n=629)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 9.367 (IC base=+0.043)

- **PATRÓN** `volumen_regimen` < `0.8515` → IC=+0.337 (n=995)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8515 (IC base=+0.043)

- **PATRÓN** `volumen_regimen` > `0.7018` → IC=+0.334 (n=1332)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7018 (IC base=+0.043)

- **PATRÓN** `volumen_pendiente_norm` < `0.159` → IC=+0.331 (n=1544)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.159 (IC base=+0.043)

- **PATRÓN** `volumen_pendiente_norm` > `0.2747` → IC=+0.348 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2747 (IC base=+0.043)

- **PATRÓN** `volumen_spike_ratio` < `1.4421` → IC=+0.352 (n=484)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4421 (IC base=+0.043)

- **PATRÓN** `ballena_activa_n` < `55.0` → IC=+0.346 (n=1448)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 55.0 (IC base=+0.043)

- **PATRÓN** `ibs_20min` < `0.6386` → IC=+0.126 (n=2934)

  - _Acción_: Kelly boost +0.63€ cuando `ibs_20min` < 0.6386 (IC base=+0.037)

- **PATRÓN** `volumen_regimen` < `0.6965` → IC=+0.270 (n=599)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6965 (IC base=+0.037)

- **PATRÓN** `volumen_pendiente_norm` < `0.1591` → IC=+0.240 (n=1413)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1591 (IC base=+0.037)

- **PATRÓN** `volumen_pendiente_norm` > `0.0716` → IC=+0.257 (n=528)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0716 (IC base=+0.037)

- **PATRÓN** `volumen_spike_ratio` < `2.4505` → IC=+0.252 (n=1311)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4505 (IC base=+0.037)

- **PATRÓN** `ballena_activa_n` < `50.0` → IC=+0.266 (n=1337)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 50.0 (IC base=+0.037)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.011` → IC=+0.353 (n=1870)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.011 (IC base=+0.309)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.311 (n=806)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.309)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.317 (n=997)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.309)

- **PATRÓN** `ibs_20min` > `0.7619` → IC=+0.346 (n=1871)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7619 (IC base=+0.309)

- **PATRÓN** `dist_vwap_pct` > `0.2027` → IC=+0.334 (n=1166)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2027 (IC base=+0.309)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.842` → IC=+0.327 (n=1013)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.842 (IC base=+0.309)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.076` → IC=+0.310 (n=2385)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 10.076 (IC base=+0.309)

- **PATRÓN** `volumen_regimen` > `0.8658` → IC=+0.329 (n=1395)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8658 (IC base=+0.309)

- **PATRÓN** `volumen_pendiente_norm` > `0.2801` → IC=+0.352 (n=308)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2801 (IC base=+0.309)

- **PATRÓN** `volumen_spike_ratio` > `1.4315` → IC=+0.321 (n=2009)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4315 (IC base=+0.309)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.343 (n=1628)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=+0.309)

- **PATRÓN** `sigma_h` > `0.0151` → IC=+0.340 (n=1479)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0151 (IC base=+0.309)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.317 (n=1113)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.309)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.311 (n=1091)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.309)

- **PATRÓN** `ibs_20min` < `0.375` → IC=+0.332 (n=2219)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.375 (IC base=+0.309)

- **PATRÓN** `dist_vwap_pct` < `0.2311` → IC=+0.315 (n=2130)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2311 (IC base=+0.309)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.619` → IC=+0.324 (n=826)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.619 (IC base=+0.309)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.083` → IC=+0.310 (n=2637)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 10.083 (IC base=+0.309)

- **PATRÓN** `volumen_regimen` < `0.721` → IC=+0.313 (n=977)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.721 (IC base=+0.309)

- **PATRÓN** `volumen_regimen` > `1.2246` → IC=+0.340 (n=740)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2246 (IC base=+0.309)

- **PATRÓN** `volumen_pendiente_norm` > `0.2852` → IC=+0.361 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2852 (IC base=+0.309)

- **PATRÓN** `volumen_spike_ratio` < `1.4166` → IC=+0.321 (n=681)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4166 (IC base=+0.309)

- **PATRÓN** `volumen_spike_ratio` > `2.139` → IC=+0.311 (n=926)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.139 (IC base=+0.309)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0118` → IC=+0.226 (n=4771)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0118 (IC base=+0.178)

- **PATRÓN** `drift_60min` |x|≤ `0.1212` → IC=+0.197 (n=6294)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.1212 (IC base=+0.178)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.187 (n=14837)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.178)

- **PATRÓN** `ibs_20min` > `0.5526` → IC=+0.233 (n=14302)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5526 (IC base=+0.178)

- **PATRÓN** `dist_vwap_pct` > `0.1629` → IC=+0.207 (n=5648)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1629 (IC base=+0.178)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.251` → IC=+0.256 (n=3727)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.251 (IC base=+0.178)

- **PATRÓN** `volumen_regimen` < `1.1857` → IC=+0.162 (n=9494)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.1857 (IC base=+0.178)

- **PATRÓN** `volumen_regimen` > `0.6235` → IC=+0.161 (n=9496)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 0.6235 (IC base=+0.178)

- **PATRÓN** `volumen_pendiente_norm` > `0.2937` → IC=+0.206 (n=2069)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2937 (IC base=+0.178)

- **PATRÓN** `volumen_spike_ratio` > `2.6103` → IC=+0.191 (n=4631)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 2.6103 (IC base=+0.178)

- **PATRÓN** `ballena_activa_n` < `90.0` → IC=+0.196 (n=13209)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 90.0 (IC base=+0.178)

- **PATRÓN** `sigma_h` < `0.0112` → IC=+0.185 (n=13824)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0112 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.0796` → IC=+0.226 (n=4611)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0796 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.215 (n=5139)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` < `0.5111` → IC=+0.238 (n=13828)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5111 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.887` → IC=+0.196 (n=2241)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 9.887 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.64` → IC=+0.185 (n=12235)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` < 2.64 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` < `1.1845` → IC=+0.165 (n=9854)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.1845 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.2962` → IC=+0.224 (n=2058)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2962 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `2.6529` → IC=+0.188 (n=4350)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.6529 (IC base=+0.182)

- **PATRÓN** `ballena_activa_n` < `97.0` → IC=+0.195 (n=12807)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 97.0 (IC base=+0.182)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.226 (n=797)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0054 (IC base=+0.222)

- **PATRÓN** `drift_60min` |x|≤ `0.3389` → IC=+0.236 (n=2387)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3389 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.234 (n=882)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.228 (n=1615)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` > `0.9346` → IC=+0.297 (n=1591)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9346 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.794` → IC=+0.331 (n=756)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.794 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` > `0.281` → IC=+0.284 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.281 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` < `1.8412` → IC=+0.219 (n=1512)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8412 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` > `1.4374` → IC=+0.223 (n=2269)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4374 (IC base=+0.222)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.234 (n=2614)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.222)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.235 (n=1468)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.222)

- **PATRÓN** `sigma_h` < `0.0087` → IC=+0.254 (n=1867)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0087 (IC base=+0.254)

- **PATRÓN** `drift_60min` |x|≤ `0.0927` → IC=+0.304 (n=821)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0927 (IC base=+0.254)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.259 (n=1922)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.254)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.254 (n=1724)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.254)

- **PATRÓN** `ibs_20min` < `0.0294` → IC=+0.303 (n=822)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0294 (IC base=+0.254)

- **PATRÓN** `volumen_pendiente_norm` < `0.1008` → IC=+0.261 (n=1636)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1008 (IC base=+0.254)

- **PATRÓN** `volumen_pendiente_norm` > `0.3016` → IC=+0.278 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3016 (IC base=+0.254)

- **PATRÓN** `volumen_spike_ratio` < `1.4432` → IC=+0.274 (n=592)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4432 (IC base=+0.254)

- **PATRÓN** `volumen_spike_ratio` > `2.7354` → IC=+0.256 (n=591)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7354 (IC base=+0.254)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.257 (n=2123)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.254)

- **PATRÓN** `libro_liquidez` > `1542.6912` → IC=+0.258 (n=1665)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1542.6912 (IC base=+0.254)

- **PATRÓN** `ballena_activa_n` < `9.0` → IC=+0.259 (n=815)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 9.0 (IC base=+0.254)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.210 (n=720)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.0644` → IC=+0.192 (n=719)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.0644 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.164 (n=2262)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` > `0.3169` → IC=+0.215 (n=2154)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3169 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` > `0.1871` → IC=+0.217 (n=1137)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1871 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.145` → IC=+0.214 (n=397)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.145 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `0.6932` → IC=+0.159 (n=948)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.6932 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` > `1.0621` → IC=+0.150 (n=977)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 1.0621 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` > `0.2827` → IC=+0.188 (n=335)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.2827 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `1.4133` → IC=+0.168 (n=705)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 1.4133 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` > `2.4851` → IC=+0.162 (n=705)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 2.4851 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `223.0` → IC=+0.161 (n=921)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 223.0 (IC base=+0.148)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.173 (n=2267)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0059 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.2355` → IC=+0.174 (n=1994)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.2355 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.187 (n=1081)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 15.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` < `0.6182` → IC=+0.207 (n=2266)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6182 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.356` → IC=+0.191 (n=432)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 11.356 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.159` → IC=+0.148 (n=1963)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 4.159 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` < `1.2065` → IC=+0.163 (n=2266)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.2065 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` < `0.0933` → IC=+0.152 (n=1939)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` < 0.0933 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `2.4919` → IC=+0.152 (n=2143)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.4919 (IC base=+0.147)

- **PATRÓN** `ballena_activa_n` < `195.0` → IC=+0.185 (n=694)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 195.0 (IC base=+0.147)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.231 (n=1098)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.3956` → IC=+0.222 (n=2131)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3956 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.233 (n=881)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.296 (n=1265)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.305` → IC=+0.306 (n=564)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.305 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` < `0.0978` → IC=+0.211 (n=2094)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0978 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.3522` → IC=+0.233 (n=346)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3522 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` < `1.7667` → IC=+0.210 (n=1036)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7667 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `2.7129` → IC=+0.226 (n=1067)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7129 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.215 (n=2887)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `1925.8986` → IC=+0.225 (n=1098)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1925.8986 (IC base=+0.210)

- **PATRÓN** `sigma_h` < `0.0105` → IC=+0.242 (n=1853)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0105 (IC base=+0.233)

- **PATRÓN** `drift_60min` |x|≤ `0.4198` → IC=+0.256 (n=1851)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4198 (IC base=+0.233)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.278 (n=794)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.233)

- **PATRÓN** `ibs_20min` < `0.0229` → IC=+0.292 (n=926)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0229 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.321` → IC=+0.277 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.321 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` > `0.359` → IC=+0.287 (n=351)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.359 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` < `1.7601` → IC=+0.234 (n=889)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7601 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` > `2.1714` → IC=+0.238 (n=1346)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1714 (IC base=+0.233)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.235 (n=1077)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.233)

- **PATRÓN** `libro_liquidez` > `1913.9884` → IC=+0.242 (n=954)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1913.9884 (IC base=+0.233)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.238 (n=1365)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 14.0 (IC base=+0.233)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.202 (n=1028)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.143)

- **PATRÓN** `drift_60min` |x|≤ `0.0786` → IC=+0.201 (n=778)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0786 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.154 (n=2414)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 5.0 (IC base=+0.143)

- **PATRÓN** `ibs_20min` > `0.2932` → IC=+0.204 (n=2328)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2932 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` > `0.1419` → IC=+0.194 (n=1379)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.1419 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.603` → IC=+0.198 (n=405)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 11.603 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` < `1.0218` → IC=+0.149 (n=2049)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 1.0218 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` > `0.1029` → IC=+0.172 (n=943)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.1029 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` < `1.8277` → IC=+0.144 (n=1522)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.8277 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` > `2.516` → IC=+0.163 (n=761)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 2.516 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `7155.9371` → IC=+0.198 (n=1056)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 7155.9371 (IC base=+0.143)

- **PATRÓN** `ballena_activa_n` < `134.0` → IC=+0.149 (n=2268)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 134.0 (IC base=+0.143)

- **PATRÓN** `sigma_h` < `0.0073` → IC=+0.157 (n=2459)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0073 (IC base=+0.130)

- **PATRÓN** `drift_60min` |x|≤ `0.3927` → IC=+0.146 (n=2458)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.3927 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.167 (n=1169)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 15.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` < `0.6789` → IC=+0.187 (n=2458)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.6789 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.547` → IC=+0.153 (n=600)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 9.547 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` < `0.8556` → IC=+0.158 (n=1639)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.8556 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` > `0.3` → IC=+0.200 (n=375)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` < `1.8099` → IC=+0.135 (n=1543)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 1.8099 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` > `1.4242` → IC=+0.132 (n=2314)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 1.4242 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `6626.5173` → IC=+0.189 (n=1115)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 6626.5173 (IC base=+0.130)

- **PATRÓN** `ballena_activa_n` < `112.0` → IC=+0.134 (n=2001)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 112.0 (IC base=+0.130)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0106` → IC=+0.171 (n=1187)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0106 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.152 (n=1844)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 11.0 (IC base=+0.124)

- **PATRÓN** `ibs_20min` > `0.4839` → IC=+0.215 (n=2609)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4839 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` > `0.1943` → IC=+0.192 (n=1467)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.1943 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.369` → IC=+0.287 (n=552)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.369 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` < `1.1752` → IC=+0.135 (n=2609)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 1.1752 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` > `0.7056` → IC=+0.124 (n=2331)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` > 0.7056 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` < `0.1617` → IC=+0.130 (n=2663)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` < 0.1617 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` < `1.5471` → IC=+0.140 (n=1115)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.5471 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.127 (n=2722)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.02 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `2673.9265` → IC=+0.206 (n=1183)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2673.9265 (IC base=+0.124)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.136 (n=2412)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 48.0 (IC base=+0.124)

- **PATRÓN** `sigma_h` < `0.0112` → IC=+0.142 (n=2690)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.0112 (IC base=+0.121)

- **PATRÓN** `drift_60min` |x|≤ `0.1082` → IC=+0.174 (n=896)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.1082 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.140 (n=2747)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 5.0 (IC base=+0.121)

- **PATRÓN** `ibs_20min` < `0.6176` → IC=+0.220 (n=2688)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6176 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.418` → IC=+0.138 (n=2373)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 2.418 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` < `1.1845` → IC=+0.131 (n=2689)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.1845 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` < `0.1648` → IC=+0.127 (n=2614)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` < 0.1648 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` > `0.2782` → IC=+0.135 (n=371)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` > 0.2782 (IC base=+0.121)

- **PATRÓN** `volumen_spike_ratio` < `1.4426` → IC=+0.132 (n=841)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 1.4426 (IC base=+0.121)

- **PATRÓN** `volumen_spike_ratio` > `2.4628` → IC=+0.129 (n=839)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 2.4628 (IC base=+0.121)

- **PATRÓN** `libro_liquidez` > `2553.641` → IC=+0.185 (n=1219)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 2553.641 (IC base=+0.121)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.128 (n=2209)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 40.0 (IC base=+0.121)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0131` → IC=+0.247 (n=2147)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0131 (IC base=+0.222)

- **PATRÓN** `drift_60min` |x|≤ `0.1692` → IC=+0.236 (n=1057)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1692 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.225 (n=2490)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.228 (n=2164)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` > `0.6604` → IC=+0.256 (n=2405)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6604 (IC base=+0.222)

- **PATRÓN** `dist_vwap_pct` > `0.1803` → IC=+0.227 (n=1527)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1803 (IC base=+0.222)

- **PATRÓN** `dist_vwap_pct` < `0.4696` → IC=+0.222 (n=2161)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4696 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.658` → IC=+0.253 (n=1085)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.658 (IC base=+0.222)

- **PATRÓN** `volumen_regimen` < `1.17` → IC=+0.223 (n=2403)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.17 (IC base=+0.222)

- **PATRÓN** `volumen_regimen` > `0.6216` → IC=+0.230 (n=2403)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6216 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` > `0.2311` → IC=+0.266 (n=447)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2311 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` < `2.461` → IC=+0.225 (n=2341)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.461 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` > `1.8078` → IC=+0.231 (n=1561)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8078 (IC base=+0.222)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.223 (n=3129)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.222)

- **PATRÓN** `libro_liquidez` > `2547.7568` → IC=+0.226 (n=1602)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2547.7568 (IC base=+0.222)

- **PATRÓN** `sigma_h` < `0.0126` → IC=+0.235 (n=1076)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0126 (IC base=+0.233)

- **PATRÓN** `sigma_h` > `0.0226` → IC=+0.241 (n=1109)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0226 (IC base=+0.233)

- **PATRÓN** `drift_60min` |x|≤ `0.0876` → IC=+0.258 (n=816)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0876 (IC base=+0.233)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.251 (n=1189)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.233)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.234 (n=1095)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.233)

- **PATRÓN** `ibs_20min` < `0.4305` → IC=+0.259 (n=2444)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4305 (IC base=+0.233)

- **PATRÓN** `dist_vwap_pct` > `0.3017` → IC=+0.242 (n=622)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3017 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.312` → IC=+0.267 (n=466)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.312 (IC base=+0.233)

- **PATRÓN** `volumen_regimen` < `0.8698` → IC=+0.234 (n=1630)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8698 (IC base=+0.233)

- **PATRÓN** `volumen_regimen` > `0.6412` → IC=+0.236 (n=2445)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6412 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` > `0.28` → IC=+0.287 (n=332)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.28 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` < `2.5262` → IC=+0.228 (n=2286)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5262 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` > `1.4363` → IC=+0.234 (n=2286)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4363 (IC base=+0.233)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.210 (n=1193)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.184)

- **PATRÓN** `sigma_h` > `0.0091` → IC=+0.190 (n=1191)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.0091 (IC base=+0.184)

- **PATRÓN** `drift_60min` |x|≤ `0.13` → IC=+0.207 (n=1570)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.13 (IC base=+0.184)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.196 (n=3582)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 6.0 (IC base=+0.184)

- **PATRÓN** `ibs_20min` > `0.4884` → IC=+0.219 (n=3188)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4884 (IC base=+0.184)

- **PATRÓN** `dist_vwap_pct` > `0.7847` → IC=+0.204 (n=542)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7847 (IC base=+0.184)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.597` → IC=+0.214 (n=1550)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.597 (IC base=+0.184)

- **PATRÓN** `volumen_regimen` < `0.863` → IC=+0.206 (n=2137)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.863 (IC base=+0.184)

- **PATRÓN** `volumen_pendiente_norm` > `0.0998` → IC=+0.192 (n=1284)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.0998 (IC base=+0.184)

- **PATRÓN** `volumen_spike_ratio` < `1.4275` → IC=+0.194 (n=1158)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 1.4275 (IC base=+0.184)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.191 (n=4020)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.02 (IC base=+0.184)

- **PATRÓN** `libro_liquidez` > `2630.2029` → IC=+0.188 (n=3188)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 2630.2029 (IC base=+0.184)

- **PATRÓN** `ibs_20min` < `0.6044` → IC=+0.125 (n=3464)

  - _Acción_: Kelly boost +0.63€ cuando `ibs_20min` < 0.6044 (IC base=+0.076)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.198 (n=853)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0047 (IC base=+0.189)

- **PATRÓN** `drift_60min` |x|≤ `0.3259` → IC=+0.211 (n=967)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3259 (IC base=+0.189)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.217 (n=886)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.189)

- **PATRÓN** `ibs_20min` > `0.6402` → IC=+0.246 (n=645)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6402 (IC base=+0.189)

- **PATRÓN** `dist_vwap_pct` > `0.3078` → IC=+0.208 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3078 (IC base=+0.189)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.054` → IC=+0.208 (n=419)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.054 (IC base=+0.189)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.269` → IC=+0.190 (n=1108)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` < 9.269 (IC base=+0.189)

- **PATRÓN** `volumen_regimen` < `0.8759` → IC=+0.212 (n=645)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8759 (IC base=+0.189)

- **PATRÓN** `volumen_pendiente_norm` < `0.0925` → IC=+0.191 (n=926)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` < 0.0925 (IC base=+0.189)

- **PATRÓN** `volumen_pendiente_norm` > `0.071` → IC=+0.194 (n=387)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.071 (IC base=+0.189)

- **PATRÓN** `volumen_spike_ratio` < `2.1894` → IC=+0.202 (n=833)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1894 (IC base=+0.189)

- **PATRÓN** `libro_liquidez` > `14680.2655` → IC=+0.192 (n=645)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 14680.2655 (IC base=+0.189)

- **PATRÓN** `ballena_activa_n` < `162.0` → IC=+0.205 (n=415)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 162.0 (IC base=+0.189)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.170 (n=398)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0029 (IC base=+0.088)

- **PATRÓN** `ibs_20min` < `0.6416` → IC=+0.140 (n=1050)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` < 0.6416 (IC base=+0.088)

- **PATRÓN** `ballena_activa_n` < `164.0` → IC=+0.172 (n=516)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 164.0 (IC base=+0.088)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.238 (n=755)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.202)

- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.202 (n=381)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0071 (IC base=+0.202)

- **PATRÓN** `drift_60min` |x|≤ `0.1257` → IC=+0.222 (n=498)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1257 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.218 (n=1181)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.202)

- **PATRÓN** `ibs_20min` > `0.3716` → IC=+0.243 (n=1011)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3716 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` > `0.5587` → IC=+0.209 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5587 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` < `0.207` → IC=+0.204 (n=1019)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.207 (IC base=+0.202)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.82` → IC=+0.231 (n=451)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.82 (IC base=+0.202)

- **PATRÓN** `volumen_regimen` < `1.0196` → IC=+0.210 (n=996)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0196 (IC base=+0.202)

- **PATRÓN** `volumen_pendiente_norm` > `0.1597` → IC=+0.228 (n=296)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1597 (IC base=+0.202)

- **PATRÓN** `volumen_spike_ratio` < `1.4263` → IC=+0.209 (n=373)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4263 (IC base=+0.202)

- **PATRÓN** `volumen_spike_ratio` > `1.7865` → IC=+0.214 (n=746)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7865 (IC base=+0.202)

- **PATRÓN** `ibs_20min` < `0.112` → IC=+0.159 (n=379)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.112 (IC base=+0.067)

- **PATRÓN** `libro_liquidez` > `8405.782` → IC=+0.143 (n=513)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 8405.782 (IC base=+0.067)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **FILTRO** `ibs_20min` > `0.7059` → IC=-0.163 (n=336)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7059
  - _Potencial_: sin este filtro IC_bueno=+0.098 (n=1015)

- **PATRÓN** `sigma_h` > `0.011` → IC=+0.206 (n=294)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.011 (IC base=+0.174)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.202 (n=794)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.174)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.279 (n=401)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.174)

- **PATRÓN** `dist_vwap_pct` > `0.947` → IC=+0.241 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.947 (IC base=+0.174)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.112` → IC=+0.247 (n=373)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.112 (IC base=+0.174)

- **PATRÓN** `volumen_regimen` < `0.8887` → IC=+0.197 (n=588)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 0.8887 (IC base=+0.174)

- **PATRÓN** `volumen_regimen` > `0.7125` → IC=+0.181 (n=787)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` > 0.7125 (IC base=+0.174)

- **PATRÓN** `volumen_pendiente_norm` > `0.2298` → IC=+0.196 (n=166)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2298 (IC base=+0.174)

- **PATRÓN** `volumen_spike_ratio` < `1.4312` → IC=+0.196 (n=284)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 1.4312 (IC base=+0.174)

- **PATRÓN** `volumen_spike_ratio` > `2.1481` → IC=+0.175 (n=386)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 2.1481 (IC base=+0.174)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.187 (n=911)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.02 (IC base=+0.174)

- **PATRÓN** `libro_liquidez` > `3005.0116` → IC=+0.193 (n=294)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 3005.0116 (IC base=+0.174)

- **PATRÓN** `ibs_20min` < `0.2222` → IC=+0.183 (n=446)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.2222 (IC base=+0.033)

- **PATRÓN** `libro_liquidez` > `2591.8999` → IC=+0.139 (n=460)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 2591.8999 (IC base=+0.033)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` < `0.0242` → IC=+0.159 (n=227)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0242 (IC base=+0.148)

- **PATRÓN** `sigma_h` > `0.0072` → IC=+0.172 (n=227)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0072 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.2552` → IC=+0.175 (n=152)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.2552 (IC base=+0.148)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.194 (n=119)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 8.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` > `0.4` → IC=+0.172 (n=227)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` > 0.4 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` > `0.3016` → IC=+0.161 (n=113)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.3016 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` < `1.1352` → IC=+0.154 (n=261)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 1.1352 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.251` → IC=+0.184 (n=194)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` < 3.251 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` > `0.6182` → IC=+0.159 (n=227)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 0.6182 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` < `0.2456` → IC=+0.172 (n=227)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` < 0.2456 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `1.4483` → IC=+0.210 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4483 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` > `2.5669` → IC=+0.167 (n=67)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 2.5669 (IC base=+0.148)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.172 (n=266)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.03 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `2664.8945` → IC=+0.176 (n=103)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 2664.8945 (IC base=+0.148)

- **PATRÓN** `sigma_h` > `0.0103` → IC=+0.150 (n=264)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` > 0.0103 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `10.0` → IC=+0.142 (n=191)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 10.0 (IC base=+0.121)

- **PATRÓN** `ibs_20min` < `0.599` → IC=+0.133 (n=265)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.599 (IC base=+0.121)

- **PATRÓN** `dist_vwap_pct` > `1.1597` → IC=+0.292 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1597 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.225` → IC=+0.171 (n=71)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 5.225 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` < `0.9016` → IC=+0.142 (n=177)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 0.9016 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` > `1.0671` → IC=+0.123 (n=120)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` > 1.0671 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` < `0.1161` → IC=+0.133 (n=243)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_pendiente_norm` < 0.1161 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` > `0.2383` → IC=+0.173 (n=50)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.2383 (IC base=+0.121)

- **PATRÓN** `volumen_spike_ratio` > `2.3673` → IC=+0.129 (n=114)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 2.3673 (IC base=+0.121)

- **PATRÓN** `libro_liquidez` > `2005.7135` → IC=+0.124 (n=264)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 2005.7135 (IC base=+0.121)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.136 (n=245)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 19.0 (IC base=+0.121)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0119` → IC=+0.230 (n=6218)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0119 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.191 (n=19433)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` > `0.4432` → IC=+0.230 (n=18647)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4432 (IC base=+0.182)

- **PATRÓN** `dist_vwap_pct` > `0.1607` → IC=+0.194 (n=6443)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.1607 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.163` → IC=+0.254 (n=4550)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.163 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` < `1.22` → IC=+0.165 (n=12518)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.22 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.2413` → IC=+0.206 (n=3372)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2413 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `2.6202` → IC=+0.194 (n=6057)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.6202 (IC base=+0.182)

- **PATRÓN** `ballena_activa_n` < `108.0` → IC=+0.202 (n=17286)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 108.0 (IC base=+0.182)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.196 (n=7508)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0057 (IC base=+0.188)

- **PATRÓN** `drift_60min` |x|≤ `0.3736` → IC=+0.193 (n=14994)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.3736 (IC base=+0.188)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.210 (n=6313)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.188)

- **PATRÓN** `ibs_20min` < `0.59` → IC=+0.241 (n=17045)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.59 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.712` → IC=+0.202 (n=2352)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.712 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.509` → IC=+0.192 (n=16519)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` < 3.509 (IC base=+0.188)

- **PATRÓN** `volumen_regimen` < `0.6328` → IC=+0.168 (n=3834)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 0.6328 (IC base=+0.188)

- **PATRÓN** `volumen_pendiente_norm` > `0.2919` → IC=+0.251 (n=2312)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2919 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` > `1.8648` → IC=+0.195 (n=10800)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 1.8648 (IC base=+0.188)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.236 (n=5460)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.188)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `drift_60min` |x|≤ `0.3515` → IC=+0.231 (n=3025)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3515 (IC base=+0.230)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.242 (n=1462)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.230)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.234 (n=2039)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.230)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.327 (n=1209)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.230)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.233` → IC=+0.349 (n=709)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.233 (IC base=+0.230)

- **PATRÓN** `volumen_pendiente_norm` > `0.2335` → IC=+0.287 (n=538)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2335 (IC base=+0.230)

- **PATRÓN** `volumen_spike_ratio` < `1.4461` → IC=+0.231 (n=971)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4461 (IC base=+0.230)

- **PATRÓN** `volumen_spike_ratio` > `2.2992` → IC=+0.241 (n=1321)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2992 (IC base=+0.230)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.247 (n=3268)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.230)

- **PATRÓN** `libro_liquidez` > `2049.79` → IC=+0.233 (n=1008)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2049.79 (IC base=+0.230)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.255 (n=1812)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.230)

- **PATRÓN** `sigma_h` < `0.0091` → IC=+0.268 (n=2612)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0091 (IC base=+0.265)

- **PATRÓN** `drift_60min` |x|≤ `0.1182` → IC=+0.289 (n=1148)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1182 (IC base=+0.265)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.271 (n=2398)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.265)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.265 (n=2381)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.265)

- **PATRÓN** `ibs_20min` < `0.5265` → IC=+0.289 (n=2609)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5265 (IC base=+0.265)

- **PATRÓN** `volumen_pendiente_norm` < `0.097` → IC=+0.268 (n=2356)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.097 (IC base=+0.265)

- **PATRÓN** `volumen_pendiente_norm` > `0.2907` → IC=+0.289 (n=368)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2907 (IC base=+0.265)

- **PATRÓN** `volumen_spike_ratio` < `1.5681` → IC=+0.268 (n=1094)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5681 (IC base=+0.265)

- **PATRÓN** `volumen_spike_ratio` > `2.686` → IC=+0.276 (n=829)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.686 (IC base=+0.265)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.265 (n=2973)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.265)

- **PATRÓN** `libro_liquidez` > `1779.9` → IC=+0.269 (n=1739)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1779.9 (IC base=+0.265)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.271 (n=1199)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.265)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.189 (n=1011)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0029 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.1043` → IC=+0.160 (n=1329)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.1043 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.159 (n=3146)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 5.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` > `0.233` → IC=+0.201 (n=3021)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.233 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` > `0.1279` → IC=+0.192 (n=1508)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.1279 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.549` → IC=+0.160 (n=636)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 9.549 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.159` → IC=+0.149 (n=2793)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 4.159 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `0.6316` → IC=+0.170 (n=1007)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 0.6316 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` > `1.0762` → IC=+0.150 (n=1370)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 1.0762 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` < `0.0729` → IC=+0.150 (n=2700)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` < 0.0729 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` > `0.2732` → IC=+0.189 (n=435)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.2732 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `2.1711` → IC=+0.155 (n=2604)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.1711 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` > `1.5323` → IC=+0.152 (n=2643)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.5323 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `233.0` → IC=+0.178 (n=974)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 233.0 (IC base=+0.148)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.161 (n=2588)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0059 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.0782` → IC=+0.183 (n=863)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.0782 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.169 (n=957)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` < `0.6918` → IC=+0.189 (n=2586)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.6918 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.07` → IC=+0.156 (n=428)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 11.07 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `1.1974` → IC=+0.151 (n=2586)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.1974 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.2193` → IC=+0.196 (n=481)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2193 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `2.4301` → IC=+0.145 (n=2480)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 2.4301 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `1.7807` → IC=+0.146 (n=1653)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.7807 (IC base=+0.139)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.140 (n=3356)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `262.0` → IC=+0.150 (n=1062)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 262.0 (IC base=+0.139)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0126` → IC=+0.253 (n=1040)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0126 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.232 (n=3252)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.225 (n=2785)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.302 (n=1165)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.225` → IC=+0.323 (n=670)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.225 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` < `0.1312` → IC=+0.226 (n=2919)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1312 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` > `1.6197` → IC=+0.229 (n=3025)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6197 (IC base=+0.224)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.231 (n=3699)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.224)

- **PATRÓN** `libro_liquidez` > `1934.5485` → IC=+0.238 (n=1408)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1934.5485 (IC base=+0.224)

- **PATRÓN** `sigma_h` < `0.0108` → IC=+0.247 (n=2584)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0108 (IC base=+0.240)

- **PATRÓN** `drift_60min` |x|≤ `0.179` → IC=+0.257 (n=1291)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.179 (IC base=+0.240)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.261 (n=1102)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.240)

- **PATRÓN** `ibs_20min` < `0.0459` → IC=+0.303 (n=978)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0459 (IC base=+0.240)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.418` → IC=+0.293 (n=327)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.418 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` > `0.3473` → IC=+0.306 (n=432)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3473 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` > `2.1472` → IC=+0.250 (n=1868)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1472 (IC base=+0.240)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.247 (n=1487)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.240)

- **PATRÓN** `libro_liquidez` > `1917.4884` → IC=+0.248 (n=1329)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1917.4884 (IC base=+0.240)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.249 (n=1848)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.240)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.198 (n=1072)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0035 (IC base=+0.143)

- **PATRÓN** `drift_60min` |x|≤ `0.4253` → IC=+0.154 (n=3214)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.4253 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.155 (n=3334)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 5.0 (IC base=+0.143)

- **PATRÓN** `ibs_20min` > `0.8127` → IC=+0.260 (n=1457)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8127 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` > `0.5611` → IC=+0.177 (n=769)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.5611 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.03` → IC=+0.159 (n=1441)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 3.03 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` < `1.0538` → IC=+0.153 (n=2828)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 1.0538 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` > `0.2336` → IC=+0.187 (n=567)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.2336 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` < `1.5221` → IC=+0.158 (n=1381)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.5221 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` > `2.1826` → IC=+0.148 (n=1423)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 2.1826 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `5436.372` → IC=+0.232 (n=1457)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5436.372 (IC base=+0.143)

- **PATRÓN** `ballena_activa_n` < `70.0` → IC=+0.156 (n=1375)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 70.0 (IC base=+0.143)

- **PATRÓN** `sigma_h` < `0.0076` → IC=+0.155 (n=2683)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0076 (IC base=+0.132)

- **PATRÓN** `drift_60min` |x|≤ `0.4362` → IC=+0.140 (n=2682)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.4362 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.156 (n=975)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 17.0 (IC base=+0.132)

- **PATRÓN** `ibs_20min` < `0.732` → IC=+0.186 (n=2682)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.732 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.081` → IC=+0.164 (n=406)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 11.081 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.143` → IC=+0.133 (n=2338)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` < 3.143 (IC base=+0.132)

- **PATRÓN** `volumen_regimen` < `0.6934` → IC=+0.147 (n=1181)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.6934 (IC base=+0.132)

- **PATRÓN** `volumen_pendiente_norm` > `0.2956` → IC=+0.221 (n=338)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2956 (IC base=+0.132)

- **PATRÓN** `volumen_spike_ratio` > `1.5382` → IC=+0.142 (n=2309)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.5382 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `6425.7391` → IC=+0.210 (n=894)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6425.7391 (IC base=+0.132)

- **PATRÓN** `ballena_activa_n` < `97.0` → IC=+0.137 (n=1745)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 97.0 (IC base=+0.132)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0106` → IC=+0.151 (n=1473)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` > 0.0106 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.155 (n=2288)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 11.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` > `0.4368` → IC=+0.195 (n=3246)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 0.4368 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` > `1.0126` → IC=+0.207 (n=545)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0126 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.573` → IC=+0.265 (n=822)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.573 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` < `0.8802` → IC=+0.138 (n=2164)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 0.8802 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` < `0.1622` → IC=+0.122 (n=3382)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_pendiente_norm` < 0.1622 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` < `2.4921` → IC=+0.122 (n=3172)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` < 2.4921 (IC base=+0.120)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.124 (n=3380)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.02 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `2714.6923` → IC=+0.244 (n=1082)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2714.6923 (IC base=+0.120)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.130 (n=1035)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 22.0 (IC base=+0.120)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.152 (n=2732)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0103 (IC base=+0.115)

- **PATRÓN** `drift_60min` |x|≤ `0.1345` → IC=+0.150 (n=1034)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.1345 (IC base=+0.115)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.127 (n=3202)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 5.0 (IC base=+0.115)

- **PATRÓN** `ibs_20min` < `0.6667` → IC=+0.206 (n=3116)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6667 (IC base=+0.115)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.202` → IC=+0.138 (n=2971)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 3.202 (IC base=+0.115)

- **PATRÓN** `volumen_regimen` < `0.6409` → IC=+0.144 (n=1034)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.6409 (IC base=+0.115)

- **PATRÓN** `volumen_pendiente_norm` > `0.2255` → IC=+0.160 (n=534)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.2255 (IC base=+0.115)

- **PATRÓN** `volumen_spike_ratio` < `1.4384` → IC=+0.150 (n=974)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.4384 (IC base=+0.115)

- **PATRÓN** `libro_liquidez` > `2580.485` → IC=+0.199 (n=1034)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 2580.485 (IC base=+0.115)

- **PATRÓN** `ballena_activa_n` < `45.0` → IC=+0.129 (n=2581)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 45.0 (IC base=+0.115)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0138` → IC=+0.256 (n=2715)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0138 (IC base=+0.233)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.238 (n=3174)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.233)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.237 (n=2732)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.233)

- **PATRÓN** `ibs_20min` > `0.612` → IC=+0.271 (n=2715)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.612 (IC base=+0.233)

- **PATRÓN** `dist_vwap_pct` > `0.1901` → IC=+0.247 (n=1623)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1901 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.299` → IC=+0.281 (n=514)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.299 (IC base=+0.233)

- **PATRÓN** `volumen_regimen` < `1.2214` → IC=+0.237 (n=3040)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2214 (IC base=+0.233)

- **PATRÓN** `volumen_regimen` > `0.6411` → IC=+0.237 (n=3039)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6411 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` > `0.2358` → IC=+0.255 (n=525)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2358 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` > `1.5427` → IC=+0.240 (n=2649)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5427 (IC base=+0.233)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.234 (n=3947)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.233)

- **PATRÓN** `libro_liquidez` > `2552.6444` → IC=+0.235 (n=2026)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2552.6444 (IC base=+0.233)

- **PATRÓN** `sigma_h` > `0.0256` → IC=+0.257 (n=1046)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0256 (IC base=+0.235)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.241 (n=2952)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.235)

- **PATRÓN** `ibs_20min` < `0.5172` → IC=+0.268 (n=3134)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5172 (IC base=+0.235)

- **PATRÓN** `dist_vwap_pct` < `0.216` → IC=+0.240 (n=2934)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.216 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.96` → IC=+0.278 (n=444)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.96 (IC base=+0.235)

- **PATRÓN** `volumen_regimen` > `1.2237` → IC=+0.258 (n=1045)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2237 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` > `0.2831` → IC=+0.298 (n=419)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2831 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` < `1.8128` → IC=+0.232 (n=1953)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8128 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` > `1.4311` → IC=+0.236 (n=2929)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4311 (IC base=+0.235)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.232 (n=2890)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=+0.235)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.196 (n=5297)

- **PATRÓN** `sigma_h` < `0.005` → IC=+0.246 (n=1832)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.213)

- **PATRÓN** `drift_60min` |x|≤ `0.5033` → IC=+0.223 (n=5495)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5033 (IC base=+0.213)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.229 (n=1978)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.213)

- **PATRÓN** `ibs_20min` > `0.9387` → IC=+0.254 (n=1833)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9387 (IC base=+0.213)

- **PATRÓN** `dist_vwap_pct` < `0.4244` → IC=+0.217 (n=3940)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4244 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.873` → IC=+0.221 (n=906)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.873 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.604` → IC=+0.214 (n=4891)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.604 (IC base=+0.213)

- **PATRÓN** `volumen_regimen` < `0.7082` → IC=+0.224 (n=1761)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7082 (IC base=+0.213)

- **PATRÓN** `volumen_regimen` > `0.8852` → IC=+0.214 (n=2667)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8852 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` < `0.1064` → IC=+0.215 (n=5137)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1064 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` > `0.1658` → IC=+0.218 (n=1546)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1658 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` < `1.4534` → IC=+0.222 (n=1804)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4534 (IC base=+0.213)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.219 (n=4220)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.213)

- **PATRÓN** `libro_liquidez` > `3711.3764` → IC=+0.222 (n=3663)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3711.3764 (IC base=+0.213)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.238 (n=1329)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.195)

- **PATRÓN** `drift_60min` |x|≤ `0.4873` → IC=+0.211 (n=3985)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4873 (IC base=+0.195)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.203 (n=1553)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.195)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.212 (n=1768)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.195)

- **PATRÓN** `ibs_20min` < `0.0865` → IC=+0.207 (n=1329)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0865 (IC base=+0.195)

- **PATRÓN** `dist_vwap_pct` > `0.6518` → IC=+0.203 (n=687)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6518 (IC base=+0.195)

- **PATRÓN** `dist_vwap_pct` < `0.2382` → IC=+0.192 (n=3675)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` < 0.2382 (IC base=+0.195)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.803` → IC=+0.205 (n=3569)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.803 (IC base=+0.195)

- **PATRÓN** `volumen_regimen` < `1.0954` → IC=+0.201 (n=3333)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0954 (IC base=+0.195)

- **PATRÓN** `volumen_pendiente_norm` < `0.0978` → IC=+0.198 (n=3662)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` < 0.0978 (IC base=+0.195)

- **PATRÓN** `volumen_spike_ratio` < `1.5357` → IC=+0.201 (n=1728)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5357 (IC base=+0.195)

- **PATRÓN** `volumen_spike_ratio` > `2.1925` → IC=+0.201 (n=1780)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1925 (IC base=+0.195)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.196 (n=5297)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.01 (IC base=+0.195)

- **PATRÓN** `ballena_activa_n` < `69.0` → IC=+0.207 (n=2609)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 69.0 (IC base=+0.195)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0055` → IC=+0.276 (n=745)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0055 (IC base=+0.266)

- **PATRÓN** `drift_60min` |x|≤ `0.0834` → IC=+0.296 (n=283)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0834 (IC base=+0.266)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.275 (n=848)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.266)

- **PATRÓN** `ibs_20min` < `0.475` → IC=+0.283 (n=565)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.475 (IC base=+0.266)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.096` → IC=+0.283 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.096 (IC base=+0.266)

- **PATRÓN** `volumen_regimen` < `1.2269` → IC=+0.272 (n=847)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2269 (IC base=+0.266)

- **PATRÓN** `volumen_regimen` > `0.8769` → IC=+0.283 (n=564)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8769 (IC base=+0.266)

- **PATRÓN** `volumen_pendiente_norm` > `0.2881` → IC=+0.343 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2881 (IC base=+0.266)

- **PATRÓN** `volumen_spike_ratio` < `1.8118` → IC=+0.270 (n=563)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8118 (IC base=+0.266)

- **PATRÓN** `libro_liquidez` > `15982.9994` → IC=+0.271 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15982.9994 (IC base=+0.266)

- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.254 (n=478)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.181)

- **PATRÓN** `drift_60min` |x|≤ `0.3722` → IC=+0.195 (n=1423)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.3722 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.215 (n=513)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.181)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.198 (n=521)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 5.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` < `0.1385` → IC=+0.204 (n=627)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1385 (IC base=+0.181)

- **PATRÓN** `ibs_20min` > `0.6023` → IC=+0.182 (n=645)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` > 0.6023 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` > `0.675` → IC=+0.201 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.675 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.318` → IC=+0.205 (n=1399)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 6.318 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `1.0915` → IC=+0.194 (n=1253)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` < 1.0915 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.1525` → IC=+0.196 (n=435)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.1525 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` < `2.4927` → IC=+0.188 (n=1416)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 2.4927 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `1.8072` → IC=+0.185 (n=944)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 1.8072 (IC base=+0.181)

- **PATRÓN** `libro_liquidez` > `13012.9559` → IC=+0.182 (n=949)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 13012.9559 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `686.0` → IC=+0.193 (n=1378)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 686.0 (IC base=+0.181)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.218 (n=388)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0107 (IC base=+0.195)

- **PATRÓN** `drift_60min` |x|≤ `0.5868` → IC=+0.203 (n=853)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5868 (IC base=+0.195)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.238 (n=322)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.195)

- **PATRÓN** `ibs_20min` < `0.7077` → IC=+0.195 (n=569)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.7077 (IC base=+0.195)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.240 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.195)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.492` → IC=+0.239 (n=308)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.492 (IC base=+0.195)

- **PATRÓN** `volumen_pendiente_norm` > `0.2085` → IC=+0.235 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2085 (IC base=+0.195)

- **PATRÓN** `volumen_spike_ratio` > `1.825` → IC=+0.203 (n=760)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.825 (IC base=+0.195)

- **PATRÓN** `libro_liquidez` > `2757.065` → IC=+0.221 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2757.065 (IC base=+0.195)

- **PATRÓN** `ballena_activa_n` < `9.0` → IC=+0.199 (n=570)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 9.0 (IC base=+0.195)

- **PATRÓN** `sigma_h` < `0.0116` → IC=+0.242 (n=60)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0116 (IC base=+0.228)

- **PATRÓN** `sigma_h` > `0.009` → IC=+0.286 (n=40)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.009 (IC base=+0.228)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.295 (n=42)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.228)

- **PATRÓN** `ibs_20min` > `0.216` → IC=+0.258 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.216 (IC base=+0.228)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.971` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.971 (IC base=+0.228)

- **PATRÓN** `volumen_pendiente_norm` < `0.1317` → IC=+0.272 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1317 (IC base=+0.228)

- **PATRÓN** `volumen_spike_ratio` < `2.3165` → IC=+0.262 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.3165 (IC base=+0.228)

- **PATRÓN** `volumen_spike_ratio` > `1.7721` → IC=+0.245 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7721 (IC base=+0.228)

- **PATRÓN** `libro_liquidez` > `2388.306` → IC=+0.259 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2388.306 (IC base=+0.228)

- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.250 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 8.0 (IC base=+0.228)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.008` → IC=+0.214 (n=1465)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.008 (IC base=+0.200)

- **PATRÓN** `drift_60min` |x|≤ `0.1468` → IC=+0.211 (n=646)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1468 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.217 (n=514)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.200)

- **PATRÓN** `ibs_20min` < `0.5123` → IC=+0.210 (n=977)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5123 (IC base=+0.200)

- **PATRÓN** `ibs_20min` > `0.8679` → IC=+0.203 (n=489)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8679 (IC base=+0.200)

- **PATRÓN** `dist_vwap_pct` < `0.2113` → IC=+0.209 (n=1313)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2113 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.109` → IC=+0.209 (n=1328)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.109 (IC base=+0.200)

- **PATRÓN** `volumen_regimen` < `1.0594` → IC=+0.201 (n=1289)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0594 (IC base=+0.200)

- **PATRÓN** `volumen_regimen` > `0.6413` → IC=+0.201 (n=1465)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6413 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` < `0.105` → IC=+0.204 (n=1352)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.105 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` < `2.4559` → IC=+0.207 (n=1435)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4559 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.201 (n=1505)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.200)

- **PATRÓN** `sigma_h` < `0.0081` → IC=+0.204 (n=1205)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0081 (IC base=+0.188)

- **PATRÓN** `drift_60min` |x|≤ `0.3841` → IC=+0.216 (n=1060)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3841 (IC base=+0.188)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.200 (n=458)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.200 (n=814)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.188)

- **PATRÓN** `ibs_20min` < `0.3985` → IC=+0.195 (n=804)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.3985 (IC base=+0.188)

- **PATRÓN** `ibs_20min` > `0.0884` → IC=+0.192 (n=1205)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.0884 (IC base=+0.188)

- **PATRÓN** `dist_vwap_pct` > `0.6351` → IC=+0.203 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6351 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.718` → IC=+0.190 (n=1230)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` < 6.718 (IC base=+0.188)

- **PATRÓN** `volumen_regimen` < `0.6415` → IC=+0.223 (n=402)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6415 (IC base=+0.188)

- **PATRÓN** `volumen_pendiente_norm` > `0.074` → IC=+0.215 (n=499)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.074 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` < `2.1958` → IC=+0.195 (n=1038)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 2.1958 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` > `1.7867` → IC=+0.190 (n=786)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 1.7867 (IC base=+0.188)

- **PATRÓN** `libro_liquidez` > `5466.7724` → IC=+0.199 (n=1205)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5466.7724 (IC base=+0.188)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.230 (n=268)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.184)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.211 (n=774)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.184)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.264 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.184)

- **PATRÓN** `dist_vwap_pct` > `0.7289` → IC=+0.243 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7289 (IC base=+0.184)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.273` → IC=+0.206 (n=437)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.273 (IC base=+0.184)

- **PATRÓN** `volumen_regimen` < `0.6342` → IC=+0.237 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6342 (IC base=+0.184)

- **PATRÓN** `volumen_pendiente_norm` < `0.1066` → IC=+0.196 (n=722)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` < 0.1066 (IC base=+0.184)

- **PATRÓN** `volumen_pendiente_norm` > `0.0799` → IC=+0.187 (n=356)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.0799 (IC base=+0.184)

- **PATRÓN** `volumen_spike_ratio` < `1.565` → IC=+0.190 (n=343)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` < 1.565 (IC base=+0.184)

- **PATRÓN** `volumen_spike_ratio` > `2.4815` → IC=+0.202 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4815 (IC base=+0.184)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.189 (n=940)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.02 (IC base=+0.184)

- **PATRÓN** `libro_liquidez` > `3567.7418` → IC=+0.209 (n=535)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3567.7418 (IC base=+0.184)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.192 (n=695)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 43.0 (IC base=+0.184)

- **PATRÓN** `sigma_h` < `0.0094` → IC=+0.219 (n=390)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0094 (IC base=+0.208)

- **PATRÓN** `sigma_h` > `0.0126` → IC=+0.211 (n=195)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0126 (IC base=+0.208)

- **PATRÓN** `drift_60min` |x|≤ `0.5007` → IC=+0.231 (n=514)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5007 (IC base=+0.208)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.243 (n=395)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 9.0 (IC base=+0.208)

- **PATRÓN** `ibs_20min` < `0.7273` → IC=+0.234 (n=584)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7273 (IC base=+0.208)

- **PATRÓN** `dist_vwap_pct` > `0.512` → IC=+0.214 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.512 (IC base=+0.208)

- **PATRÓN** `dist_vwap_pct` < `0.3064` → IC=+0.209 (n=493)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3064 (IC base=+0.208)

- **PATRÓN** `volumen_regimen` < `0.7555` → IC=+0.218 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7555 (IC base=+0.208)

- **PATRÓN** `volumen_regimen` > `0.9335` → IC=+0.211 (n=389)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.9335 (IC base=+0.208)

- **PATRÓN** `volumen_pendiente_norm` < `0.1067` → IC=+0.226 (n=508)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1067 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` > `2.2044` → IC=+0.242 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2044 (IC base=+0.208)

- **PATRÓN** `libro_liquidez` > `2998.9426` → IC=+0.227 (n=584)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2998.9426 (IC base=+0.208)

- **PATRÓN** `ballena_activa_n` < `29.0` → IC=+0.253 (n=390)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 29.0 (IC base=+0.208)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.149 (n=825)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0042 (IC base=+0.065)

- **PATRÓN** `ibs_20min` > `0.3864` → IC=+0.135 (n=1777)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` > 0.3864 (IC base=+0.065)

- **PATRÓN** `dist_vwap_pct` > `0.1461` → IC=+0.147 (n=907)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` > 0.1461 (IC base=+0.065)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.814` → IC=+0.150 (n=392)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 10.814 (IC base=+0.065)

- **PATRÓN** `ibs_20min` < `0.0426` → IC=+0.261 (n=475)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0426 (IC base=+0.048)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.917` → IC=+0.176 (n=171)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 9.917 (IC base=+0.048)

- **PATRÓN** `volumen_pendiente_norm` > `0.1467` → IC=+0.160 (n=304)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.1467 (IC base=+0.048)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `ibs_20min` < `0.5149` → IC=-0.121 (n=254)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5149
  - _Potencial_: sin este filtro IC_bueno=+0.192 (n=517)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.132 (n=610)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.66€ cuando `sigma_h` < 0.0057 (IC base=+0.087)

- **PATRÓN** `ibs_20min` > `0.5149` → IC=+0.192 (n=517)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.5149 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` > `0.1218` → IC=+0.172 (n=288)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.1218 (IC base=+0.087)

- **PATRÓN** `ibs_20min` < `0.0674` → IC=+0.283 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0674 (IC base=+0.055)

- **PATRÓN** `volumen_pendiente_norm` > `0.2164` → IC=+0.188 (n=91)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.2164 (IC base=+0.055)

### GBM_LATE_60M#ETH#60min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.145 (n=407)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.005 (IC base=+0.086)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.138 (n=299)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 15.0 (IC base=+0.086)

- **PATRÓN** `ibs_20min` > `0.3924` → IC=+0.166 (n=579)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.3924 (IC base=+0.086)

- **PATRÓN** `dist_vwap_pct` > `0.1269` → IC=+0.193 (n=291)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.1269 (IC base=+0.086)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.996` → IC=+0.213 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.996 (IC base=+0.086)

- **PATRÓN** `ibs_20min` < `0.0322` → IC=+0.248 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0322 (IC base=+0.015)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.547` → IC=+0.217 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.547 (IC base=+0.015)

### GBM_LATE_60M#SOL#60min
- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.197 (n=216)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 1.0 (IC base=+0.024)

- **PATRÓN** `dist_vwap_pct` > `0.4664` → IC=+0.136 (n=212)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` > 0.4664 (IC base=+0.024)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.025` → IC=+0.140 (n=134)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 9.025 (IC base=+0.024)

- **PATRÓN** `sigma_h` < `0.0102` → IC=+0.159 (n=268)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0102 (IC base=+0.076)

- **PATRÓN** `ibs_20min` < `0.2` → IC=+0.211 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2 (IC base=+0.076)

- **PATRÓN** `dist_vwap_pct` < `0.1716` → IC=+0.139 (n=264)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.1716 (IC base=+0.076)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.219` → IC=+0.339 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.219 (IC base=+0.076)

- **PATRÓN** `volumen_regimen` > `1.1167` → IC=+0.192 (n=92)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` > 1.1167 (IC base=+0.076)

- **PATRÓN** `volumen_pendiente_norm` > `0.1508` → IC=+0.198 (n=84)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.1508 (IC base=+0.076)

- **PATRÓN** `volumen_spike_ratio` > `1.8174` → IC=+0.157 (n=167)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.8174 (IC base=+0.076)

### GBM_LATE_60M_FADE
- **FILTRO** `sigma_h` < `0.0054` → IC=-0.238 (n=166)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0054
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=166)

- **FILTRO** `hora_utc` > `8.0` → IC=-0.331 (n=69)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.175 (n=263)

- **FILTRO** `dist_vwap_pct` > `0.2351` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2351
  - _Potencial_: sin este filtro IC_bueno=-0.201 (n=316)

- **FILTRO** `volumen_regimen` < `0.7732` → IC=-0.300 (n=83)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7732
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=249)

- **FILTRO** `hora_utc` < `5.0` → IC=-0.310 (n=56)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.292 (n=234)

- **FILTRO** `dist_vwap_pct` > `0.3644` → IC=-0.406 (n=30)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3644
  - _Potencial_: sin este filtro IC_bueno=-0.282 (n=260)

- **FILTRO** `sigma_ewma_delta_pct` > `10.138` → IC=-0.321 (n=26)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 10.138
  - _Potencial_: sin este filtro IC_bueno=-0.293 (n=264)

- **FILTRO** `volumen_pendiente_norm` > `0.0435` → IC=-0.382 (n=32)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0435
  - _Potencial_: sin este filtro IC_bueno=-0.286 (n=171)

- **FILTRO** `libro_liquidez` < `1541.8747` → IC=-0.314 (n=95)

  - _Acción_: SKIP cuando `libro_liquidez` < 1541.8747
  - _Potencial_: sin este filtro IC_bueno=-0.287 (n=195)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `volumen_regimen` < `1.2175` → IC=-0.292 (n=51)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.2175
  - _Potencial_: sin este filtro IC_bueno=-0.160 (n=51)

- **FILTRO** `sigma_h` > `0.0043` → IC=-0.318 (n=31)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0043
  - _Potencial_: sin este filtro IC_bueno=-0.245 (n=100)

- **FILTRO** `volumen_regimen` > `0.8276` → IC=-0.353 (n=32)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8276
  - _Potencial_: sin este filtro IC_bueno=-0.233 (n=99)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `sigma_h` < `0.0027` → IC=-0.293 (n=27)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0027
  - _Potencial_: sin este filtro IC_bueno=-0.109 (n=85)

- **FILTRO** `ibs_20min` < `0.5843` → IC=-0.467 (n=28)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5843
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=84)

- **FILTRO** `hora_utc` < `6.0` → IC=-0.375 (n=22)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.291 (n=89)

- **FILTRO** `ibs_20min` > `0.7162` → IC=-0.397 (n=37)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7162
  - _Potencial_: sin este filtro IC_bueno=-0.263 (n=74)

- **FILTRO** `volumen_spike_ratio` < `1.442` → IC=-0.357 (n=19)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.442
  - _Potencial_: sin este filtro IC_bueno=-0.303 (n=59)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.400 (n=18)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=100)

- **FILTRO** `dist_vwap_pct` > `0.0608` → IC=-0.250 (n=26)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.0608
  - _Potencial_: sin este filtro IC_bueno=-0.223 (n=92)

- **FILTRO** `volumen_regimen` < `0.7506` → IC=-0.339 (n=29)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7506
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=89)

- **FILTRO** `libro_spread` > `0.06` → IC=-0.242 (n=29)

  - _Acción_: SKIP cuando `libro_spread` > 0.06
  - _Potencial_: sin este filtro IC_bueno=-0.225 (n=89)

- **FILTRO** `hora_utc` > `11.0` → IC=-0.441 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.243 (n=33)

- **FILTRO** `dist_vwap_pct` < `0.2328` → IC=-0.352 (n=25)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.2328
  - _Potencial_: sin este filtro IC_bueno=-0.260 (n=23)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` > `0.1429` → IC=-0.122 (n=305)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1429
  - _Potencial_: sin este filtro IC_bueno=+0.131 (n=597)

- **PATRÓN** `sigma_h` > `0.0077` → IC=+0.203 (n=197)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0077 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.195 (n=224)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 17.0 (IC base=+0.127)

- **PATRÓN** `ibs_20min` > `0.6686` → IC=+0.167 (n=590)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` > 0.6686 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` > `0.5387` → IC=+0.238 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5387 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.656` → IC=+0.131 (n=323)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` > 3.656 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.636` → IC=+0.132 (n=436)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` < 2.636 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` < `0.6195` → IC=+0.185 (n=198)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 0.6195 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` < `0.069` → IC=+0.168 (n=419)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` < 0.069 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` < `1.3956` → IC=+0.189 (n=162)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` < 1.3956 (IC base=+0.127)

- **PATRÓN** `ibs_20min` < `0.1429` → IC=+0.131 (n=597)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.1429 (IC base=+0.045)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.023` → IC=+0.167 (n=196)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 9.023 (IC base=+0.045)

- **PATRÓN** `libro_liquidez` > `3247.8769` → IC=+0.120 (n=451)

  - _Acción_: Kelly boost +0.60€ cuando `libro_liquidez` > 3247.8769 (IC base=+0.045)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.7055` → IC=-0.172 (n=59)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7055
  - _Potencial_: sin este filtro IC_bueno=+0.072 (n=178)

- **PATRÓN** `sigma_h` > `0.0036` → IC=+0.145 (n=212)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` > 0.0036 (IC base=+0.117)

- **PATRÓN** `ibs_20min` < `0.1754` → IC=+0.175 (n=318)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.1754 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` < `0.2512` → IC=+0.131 (n=367)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.2512 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.158` → IC=+0.147 (n=134)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 7.158 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` > `1.0363` → IC=+0.164 (n=144)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 1.0363 (IC base=+0.117)

- **PATRÓN** `volumen_pendiente_norm` > `0.2687` → IC=+0.148 (n=52)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.2687 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` > `1.7861` → IC=+0.148 (n=191)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.7861 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `5390.0556` → IC=+0.131 (n=212)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 5390.0556 (IC base=+0.117)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `volumen_pendiente_norm` > `0.1302` → IC=-0.149 (n=35)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1302
  - _Potencial_: sin este filtro IC_bueno=+0.165 (n=189)

- **FILTRO** `ibs_20min` > `0.1644` → IC=-0.140 (n=109)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1644
  - _Potencial_: sin este filtro IC_bueno=+0.079 (n=214)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.139 (n=131)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.004 (IC base=+0.116)

- **PATRÓN** `drift_60min` |x|≤ `0.1024` → IC=+0.129 (n=87)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.65€ cuando `drift_60min` |x|≤ 0.1024 (IC base=+0.116)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.196 (n=67)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 18.0 (IC base=+0.116)

- **PATRÓN** `ibs_20min` > `0.8015` → IC=+0.157 (n=176)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` > 0.8015 (IC base=+0.116)

- **PATRÓN** `dist_vwap_pct` < `0.0943` → IC=+0.140 (n=162)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.0943 (IC base=+0.116)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.217` → IC=+0.152 (n=205)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` < 9.217 (IC base=+0.116)

- **PATRÓN** `volumen_regimen` < `0.6195` → IC=+0.191 (n=66)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 0.6195 (IC base=+0.116)

- **PATRÓN** `volumen_pendiente_norm` < `0.1302` → IC=+0.165 (n=189)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` < 0.1302 (IC base=+0.116)

- **PATRÓN** `volumen_spike_ratio` < `1.7963` → IC=+0.187 (n=113)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` < 1.7963 (IC base=+0.116)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.135 (n=165)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.116)

- **PATRÓN** `libro_liquidez` > `1620.5728` → IC=+0.177 (n=196)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 1620.5728 (IC base=+0.116)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.828` → IC=+0.217 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.828 (IC base=+0.005)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.2308` → IC=-0.264 (n=53)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2308
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=103)

- **FILTRO** `dist_vwap_pct` > `0.3368` → IC=-0.167 (n=25)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3368
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=131)

- **PATRÓN** `sigma_h` < `0.0098` → IC=+0.231 (n=217)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0098 (IC base=+0.231)

- **PATRÓN** `sigma_h` > `0.0088` → IC=+0.280 (n=98)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0088 (IC base=+0.231)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.295 (n=154)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.231)

- **PATRÓN** `ibs_20min` > `0.6053` → IC=+0.262 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6053 (IC base=+0.231)

- **PATRÓN** `dist_vwap_pct` > `0.6667` → IC=+0.398 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6667 (IC base=+0.231)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.017` → IC=+0.336 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.017 (IC base=+0.231)

- **PATRÓN** `volumen_regimen` < `0.7917` → IC=+0.276 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7917 (IC base=+0.231)

- **PATRÓN** `volumen_pendiente_norm` > `0.0966` → IC=+0.282 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0966 (IC base=+0.231)

- **PATRÓN** `volumen_spike_ratio` < `1.4814` → IC=+0.349 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4814 (IC base=+0.231)

- **PATRÓN** `libro_liquidez` > `738.2599` → IC=+0.233 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 738.2599 (IC base=+0.231)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.418` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.418 (IC base=-0.063)

### LATE_WINDOW_5MIN
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.317 (n=80)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3447` → IC=+0.331 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3447 (IC base=+0.314)

- **PATRÓN** `elapsed_s` > `184.3` → IC=+0.379 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 184.3 (IC base=+0.314)

- **PATRÓN** `drift_15min` |x|≤ `1.0104` → IC=+0.417 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0104 (IC base=+0.314)

- **PATRÓN** `drift_60min` |x|≤ `0.9647` → IC=+0.379 (n=64)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9647 (IC base=+0.314)

- **PATRÓN** `ballena_activa_n` < `1071.0` → IC=+0.375 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1071.0 (IC base=+0.314)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3474` → IC=+0.261 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3474 (IC base=+0.237)

- **PATRÓN** `elapsed_s` > `187.9` → IC=+0.261 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 187.9 (IC base=+0.237)

- **PATRÓN** `elapsed_s` < `216.8` → IC=+0.246 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 216.8 (IC base=+0.237)

- **PATRÓN** `drift_15min` |x|≤ `2.3682` → IC=+0.306 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3682 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.6424` → IC=+0.304 (n=49)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6424 (IC base=+0.237)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.317 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.237)

- **PATRÓN** `ballena_activa_n` < `1814.0` → IC=+0.287 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1814.0 (IC base=+0.237)

### LATE_WINDOW_5MIN#BTC#5min
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.317 (n=80)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3447` → IC=+0.331 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3447 (IC base=+0.314)

- **PATRÓN** `elapsed_s` > `184.3` → IC=+0.379 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 184.3 (IC base=+0.314)

- **PATRÓN** `drift_15min` |x|≤ `1.0104` → IC=+0.417 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0104 (IC base=+0.314)

- **PATRÓN** `drift_60min` |x|≤ `0.9647` → IC=+0.379 (n=64)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9647 (IC base=+0.314)

- **PATRÓN** `ballena_activa_n` < `1071.0` → IC=+0.375 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1071.0 (IC base=+0.314)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3474` → IC=+0.261 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3474 (IC base=+0.237)

- **PATRÓN** `elapsed_s` > `187.9` → IC=+0.261 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 187.9 (IC base=+0.237)

- **PATRÓN** `elapsed_s` < `216.8` → IC=+0.246 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 216.8 (IC base=+0.237)

- **PATRÓN** `drift_15min` |x|≤ `2.3682` → IC=+0.306 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3682 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.6424` → IC=+0.304 (n=49)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6424 (IC base=+0.237)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.317 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.237)

- **PATRÓN** `ballena_activa_n` < `1814.0` → IC=+0.287 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1814.0 (IC base=+0.237)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `libro_liquidez` > `2919.5028` → IC=+0.135 (n=466)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 2919.5028 (IC base=+0.099)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `libro_liquidez` > `2919.5028` → IC=+0.135 (n=466)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 2919.5028 (IC base=+0.099)

### LIQUIDACIONES_15M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=213)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=213)

- **FILTRO** `libro_liquidez` < `5828.7817` → IC=-0.155 (n=114)

  - _Acción_: SKIP cuando `libro_liquidez` < 5828.7817
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=115)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=447)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `libro_liquidez` < `11419.5026` → IC=-0.143 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 11419.5026
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=81)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `liq_usd_total` < `4006.09` → IC=-0.143 (n=26)

  - _Acción_: SKIP cuando `liq_usd_total` < 4006.09
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=26)

- **FILTRO** `hora_utc` < `10.0` → IC=-0.184 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=35)

- **PATRÓN** `liq_n` > `5.0` → IC=+0.186 (n=33)

  - _Acción_: Kelly boost +0.93€ cuando `liq_n` > 5.0 (IC base=+0.069)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.149 (n=35)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 8.0 (IC base=+0.069)

### LIQUIDACIONES_15M#XRP#15min
- **FILTRO** `liq_n` < `7.0` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `liq_n` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.309 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

- **FILTRO** `libro_liquidez` < `2892.3985` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `libro_liquidez` < 2892.3985
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

### LIQUIDACIONES_5M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.121 (n=85)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=3711)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.132 (n=112)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=69)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.278 (n=34)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.114 (n=99)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.132 (n=112)

### LIQUIDACIONES_5M#BNB#5min
- **FILTRO** `hora_utc` > `14.0` → IC=-0.133 (n=47)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.104 (n=132)

### LIQUIDACIONES_5M#BTC#5min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=21)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.167 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.125 (n=14)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.124 (n=261)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` < 0.495 (IC base=+0.022)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=1437)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=1391)

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
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=712)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=720)

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
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=440)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=421)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.147 (n=185)

  - _Acción_: Kelly boost +0.74€ cuando `py_entrada` < 0.495 (IC base=+0.022)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=889)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=889)

- **FILTRO** `py_entrada` < `0.44` → IC=-0.132 (n=275)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=694)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=959)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=959)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=232)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=232)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.200 (n=48)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=284)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=317)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=276)

- **FILTRO** `py_entrada` > `0.545` → IC=-0.120 (n=77)

  - _Acción_: SKIP cuando `py_entrada` > 0.545
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=270)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=366)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=366)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.120 (n=185)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=211)

- **FILTRO** `libro_liquidez` < `641.5292` → IC=-0.136 (n=130)

  - _Acción_: SKIP cuando `libro_liquidez` < 641.5292
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=266)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=280)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.129 (n=87)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=208)

### LIQUIDACIONES_DEPTH_FASE0#BNB#15min
- **FILTRO** `restante_min` < `9.67` → IC=-0.278 (n=25)

  - _Acción_: SKIP cuando `restante_min` < 9.67
  - _Potencial_: sin este filtro IC_bueno=+0.070 (n=77)

- **PATRÓN** `py_entrada` < `0.59` → IC=+0.125 (n=46)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` < 0.59 (IC base=+0.007)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.148 (n=69)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.119 (n=40)

- **FILTRO** `py_entrada` > `0.58` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=28)

- **FILTRO** `hora_utc` < `17.0` → IC=-0.191 (n=40)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=14)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.5` → IC=+0.159 (n=227)

  - _Acción_: Kelly boost +0.80€ cuando `py_entrada` < 0.5 (IC base=+0.013)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.130 (n=125)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=497)

- **FILTRO** `profundidad_ratio` < `43.4` → IC=-0.143 (n=155)

  - _Acción_: SKIP cuando `profundidad_ratio` < 43.4
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=467)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.125 (n=246)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=267)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.120 (n=364)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=378)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.145 (n=108)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=470)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` > `0.61` → IC=-0.126 (n=89)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=274)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.141 (n=154)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=559)

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
- **FILTRO** `py_entrada` < `0.47` → IC=-0.164 (n=6849)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=20647)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.176 (n=6849)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.046 (n=21435)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.191 (n=1233)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=3823)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.179 (n=1169)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=3854)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.138 (n=1324)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` > 1.0 (IC base=+0.042)

- **PATRÓN** `libro_liquidez` > `1057.9652` → IC=+0.138 (n=2528)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 1057.9652 (IC base=+0.042)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.130 (n=2357)

  - _Acción_: Kelly boost +0.65€ cuando `py_entrada` < 0.5 (IC base=+0.011)

- **PATRÓN** `libro_liquidez` > `1234.5172` → IC=+0.151 (n=1708)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 1234.5172 (IC base=+0.011)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` > `0.57` → IC=-0.185 (n=975)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=3039)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` > `0.62` → IC=-0.202 (n=1220)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.078 (n=3929)

- **PATRÓN** `ibs_20min` > `0.9652` → IC=+0.128 (n=1716)

  - _Acción_: Kelly boost +0.64€ cuando `ibs_20min` > 0.9652 (IC base=+0.036)

- **PATRÓN** `libro_liquidez` > `1752.2` → IC=+0.122 (n=1716)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 1752.2 (IC base=+0.036)

### MOMENTUM_IBS_15M_BALLENA#ETH#15min
- **FILTRO** `py_entrada` > `0.575` → IC=-0.185 (n=1006)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=3051)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.151 (n=1248)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=3805)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=2410)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.162 (n=772)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=2334)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.189 (n=911)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=2821)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=3711)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` < `14.0` → IC=-0.157 (n=135)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=437)

- **FILTRO** `hora_utc` > `20.0` → IC=-0.146 (n=125)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 20.0
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=447)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.146 (n=80)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=-0.098 (n=254)

- **FILTRO** `py_entrada` < `0.395` → IC=-0.230 (n=72)

  - _Acción_: SKIP cuando `py_entrada` < 0.395
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=262)

- **FILTRO** `hora_utc` < `7.0` → IC=-0.204 (n=113)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.099 (n=340)

- **FILTRO** `drift_20min_pct` |x|> `0.2047` → IC=-0.143 (n=113)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.2047
  - _Potencial_: sin este filtro IC_bueno=-0.120 (n=340)

- **FILTRO** `libro_liquidez` < `3183.3406` → IC=-0.182 (n=149)

  - _Acción_: SKIP cuando `libro_liquidez` < 3183.3406
  - _Potencial_: sin este filtro IC_bueno=-0.098 (n=304)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=946)

- **FILTRO** `ballena_activa_n` > `25.0` → IC=-0.197 (n=354)

  - _Acción_: SKIP cuando `ballena_activa_n` > 25.0
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=708)

### MOMENTUM_IBS_15M_FADE#XRP#15min
- **FILTRO** `hora_utc` < `13.0` → IC=-0.238 (n=59)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 13.0
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=234)

### MOMENTUM_IBS_5M#BNB#5min
- **FILTRO** `hora_utc` > `17.0` → IC=-0.157 (n=33)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=44)

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

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.138 (n=45)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 17.0 (IC base=+0.030)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.133 (n=18871)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=42233)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.296 (n=14229)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=46875)

- **FILTRO** `ibs_7min` < `0.2307` → IC=-0.231 (n=15275)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2307
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=45829)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.153 (n=20685)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=40419)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.242 (n=18933)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=57744)

- **FILTRO** `ibs_7min` > `0.2841` → IC=-0.181 (n=19163)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2841
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=57514)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.153 (n=2660)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=8112)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.316 (n=2611)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=8161)

- **FILTRO** `ibs_7min` < `0.7117` → IC=-0.248 (n=3554)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7117
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=7218)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.148 (n=2601)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=8171)

- **FILTRO** `py_entrada` > `0.72` → IC=-0.277 (n=3159)

  - _Acción_: SKIP cuando `py_entrada` > 0.72
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=10089)

- **FILTRO** `ibs_7min` > `0.7719` → IC=-0.214 (n=3311)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7719
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=9937)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.128 (n=2452)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.097 (n=7790)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.263 (n=2426)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=7816)

- **FILTRO** `ibs_7min` < `0.7192` → IC=-0.205 (n=2559)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7192
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=7683)

- **FILTRO** `ballena_activa_n` > `155.0` → IC=-0.193 (n=2550)

  - _Acción_: SKIP cuando `ballena_activa_n` > 155.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=7692)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.258 (n=2586)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=7865)

- **FILTRO** `ibs_7min` > `0.2661` → IC=-0.192 (n=2611)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2661
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=7840)

- **FILTRO** `ballena_activa_n` > `152.0` → IC=-0.179 (n=2594)

  - _Acción_: SKIP cuando `ballena_activa_n` > 152.0
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=7857)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.162 (n=2516)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=7744)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.312 (n=2545)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=7715)

- **FILTRO** `ibs_7min` < `0.291` → IC=-0.249 (n=3385)

  - _Acción_: SKIP cuando `ibs_7min` < 0.291
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=6875)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.197 (n=2286)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=7974)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.259 (n=3305)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=10767)

- **FILTRO** `ibs_7min` > `0.7308` → IC=-0.180 (n=3515)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7308
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=10557)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.124 (n=3240)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.094 (n=6683)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.264 (n=2394)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=7529)

- **FILTRO** `ibs_7min` < `0.7222` → IC=-0.195 (n=2480)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7222
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=7443)

- **FILTRO** `ballena_activa_n` > `26.0` → IC=-0.188 (n=2443)

  - _Acción_: SKIP cuando `ballena_activa_n` > 26.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=7480)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.260 (n=2341)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=7973)

- **FILTRO** `ibs_7min` > `0.275` → IC=-0.173 (n=2578)

  - _Acción_: SKIP cuando `ibs_7min` > 0.275
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=7736)

- **FILTRO** `ballena_activa_n` > `25.0` → IC=-0.172 (n=2534)

  - _Acción_: SKIP cuando `ballena_activa_n` > 25.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=7780)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.283 (n=2460)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=7476)

- **FILTRO** `ibs_7min` < `0.7143` → IC=-0.224 (n=3273)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7143
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=6663)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.222 (n=2357)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=7579)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.193 (n=3537)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=11218)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.32` → IC=-0.296 (n=2421)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=7550)

- **FILTRO** `ibs_7min` < `0.1875` → IC=-0.227 (n=2490)

  - _Acción_: SKIP cuando `ibs_7min` < 0.1875
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=7481)

- **FILTRO** `ballena_activa_n` > `9.0` → IC=-0.199 (n=2381)

  - _Acción_: SKIP cuando `ballena_activa_n` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=7590)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.222 (n=3423)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=10414)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1046` → IC=-0.135 (n=61)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1046
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=121)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `py_entrada` < `0.455` → IC=-0.160 (n=301)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=1004)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=1290)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.122 (n=215)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=525)

- **FILTRO** `py_entrada` > `0.545` → IC=-0.156 (n=158)

  - _Acción_: SKIP cuando `py_entrada` > 0.545
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=582)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=1458)

- **FILTRO** `py_entrada` > `0.565` → IC=-0.172 (n=260)

  - _Acción_: SKIP cuando `py_entrada` > 0.565
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=861)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.122 (n=220)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=279)

- **FILTRO** `ballena_activa_n` > `3.0` → IC=-0.143 (n=166)

  - _Acción_: SKIP cuando `ballena_activa_n` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=332)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.231 (n=50)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=449)

- **FILTRO** `libro_liquidez` < `3265.4723` → IC=-0.152 (n=182)

  - _Acción_: SKIP cuando `libro_liquidez` < 3265.4723
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=549)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.4304` → IC=+0.151 (n=583)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.76€ cuando `delta_ratio` |x|> 0.4304 (IC base=+0.127)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.137 (n=672)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 6.0 (IC base=+0.127)

- **PATRÓN** `total_vol_5m` < `3975.783` → IC=+0.146 (n=856)

  - _Acción_: Kelly boost +0.73€ cuando `total_vol_5m` < 3975.783 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `3479.5432` → IC=+0.145 (n=582)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 3479.5432 (IC base=+0.127)

- **PATRÓN** `ballena_activa_n` < `10.0` → IC=+0.132 (n=430)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 10.0 (IC base=+0.127)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.4385` → IC=+0.131 (n=101)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.66€ cuando `delta_ratio` |x|> 0.4385 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.176 (n=146)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 14.0 (IC base=+0.130)

- **PATRÓN** `total_vol_5m` < `280.725` → IC=+0.150 (n=201)

  - _Acción_: Kelly boost +0.75€ cuando `total_vol_5m` < 280.725 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `2523.0565` → IC=+0.209 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2523.0565 (IC base=+0.130)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `delta_ratio` |x|> `0.3992` → IC=+0.128 (n=264)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.64€ cuando `delta_ratio` |x|> 0.3992 (IC base=+0.115)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.135 (n=236)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 14.0 (IC base=+0.115)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.124 (n=317)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.04 (IC base=+0.115)

- **PATRÓN** `libro_liquidez` > `2303.65` → IC=+0.135 (n=176)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 2303.65 (IC base=+0.115)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4161` → IC=+0.193 (n=164)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.96€ cuando `delta_ratio` |x|> 0.4161 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.185 (n=87)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 15.0 (IC base=+0.139)

- **PATRÓN** `total_vol_5m` < `384.1453` → IC=+0.212 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 384.1453 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `7573.3328` → IC=+0.145 (n=164)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 7573.3328 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `60.0` → IC=+0.194 (n=83)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 60.0 (IC base=+0.139)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.4322` → IC=+0.224 (n=103)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio` |x|> 0.4322 (IC base=+0.150)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.193 (n=164)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 12.0 (IC base=+0.150)

- **PATRÓN** `total_vol_5m` < `4761.643` → IC=+0.193 (n=151)

  - _Acción_: Kelly boost +0.96€ cuando `total_vol_5m` < 4761.643 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `3106.4902` → IC=+0.176 (n=202)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 3106.4902 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `28.0` → IC=+0.160 (n=98)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 28.0 (IC base=+0.150)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `hora_utc` < `13.0` → IC=+0.127 (n=218)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 13.0 (IC base=+0.101)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.173 (n=166)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.01 (IC base=+0.101)

- **PATRÓN** `libro_liquidez` > `3728.089` → IC=+0.147 (n=83)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 3728.089 (IC base=+0.101)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `7.7861` → IC=-0.284 (n=49)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 7.7861
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=148)

- **FILTRO** `sigma_h` > `0.0074` → IC=-0.309 (n=181)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0074
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=545)

- **FILTRO** `T_h` > `129.5932` → IC=-0.183 (n=181)

  - _Acción_: SKIP cuando `T_h` > 129.5932
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=545)

- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.149 (n=240)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0043 (IC base=-0.080)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0073` → IC=-0.300 (n=53)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0073
  - _Potencial_: sin este filtro IC_bueno=+0.055 (n=162)

- **FILTRO** `T_h` > `87.9872` → IC=-0.245 (n=53)

  - _Acción_: SKIP cuando `T_h` > 87.9872
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=162)

- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.286 (n=54)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=-0.035)

- **PATRÓN** `pct_vs_K` |x|≤ `1.5815` → IC=+0.144 (n=71)

  - _Acción_: Kelly boost +0.72€ cuando `pct_vs_K` |x|≤ 1.5815 (IC base=-0.035)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `sigma_h` > `0.0105` → IC=-0.180 (n=23)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0105
  - _Potencial_: sin este filtro IC_bueno=-0.112 (n=47)

- **FILTRO** `pct_vs_K` |x|> `9.1619` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 9.1619
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=53)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.013` → IC=-0.243 (n=33)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.013
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=101)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0095` → IC=-0.238 (n=437)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0095
  - _Potencial_: sin este filtro IC_bueno=-0.110 (n=226)

- **FILTRO** `T_h` > `80.4727` → IC=-0.213 (n=444)

  - _Acción_: SKIP cuando `T_h` > 80.4727
  - _Potencial_: sin este filtro IC_bueno=-0.156 (n=219)

- **FILTRO** `sigma_h` < `0.005` → IC=-0.236 (n=142)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.005
  - _Potencial_: sin este filtro IC_bueno=-0.215 (n=426)

- **FILTRO** `pct_vs_K` |x|> `3.2846` → IC=-0.429 (n=138)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.2846
  - _Potencial_: sin este filtro IC_bueno=-0.153 (n=430)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `T_h` > `71.159` → IC=-0.201 (n=145)

  - _Acción_: SKIP cuando `T_h` > 71.159
  - _Potencial_: sin este filtro IC_bueno=-0.105 (n=74)

- **FILTRO** `T_h` > `73.068` → IC=-0.260 (n=152)

  - _Acción_: SKIP cuando `T_h` > 73.068
  - _Potencial_: sin este filtro IC_bueno=-0.222 (n=52)

- **FILTRO** `pct_vs_K` |x|> `2.9616` → IC=-0.423 (n=50)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.9616
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=154)

### PRICE_TARGET_GBM_FADE#BTC#reach
- **FILTRO** `sigma_h` < `0.0085` → IC=-0.250 (n=22)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0085
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `sigma_h` < `0.0071` → IC=-0.294 (n=95)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0071
  - _Potencial_: sin este filtro IC_bueno=-0.222 (n=95)

- **FILTRO** `T_h` > `69.4221` → IC=-0.271 (n=142)

  - _Acción_: SKIP cuando `T_h` > 69.4221
  - _Potencial_: sin este filtro IC_bueno=-0.220 (n=48)

- **FILTRO** `sigma_h` > `0.009` → IC=-0.348 (n=44)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.009
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=133)

- **FILTRO** `T_h` > `57.2198` → IC=-0.250 (n=118)

  - _Acción_: SKIP cuando `T_h` > 57.2198
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=59)

### PRICE_TARGET_GBM_FADE#ETH#reach
- **FILTRO** `sigma_h` < `0.0099` → IC=-0.222 (n=16)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0099
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

- **FILTRO** `T_h` > `126.9278` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `T_h` > 126.9278
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` < `0.0082` → IC=-0.292 (n=46)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0082
  - _Potencial_: sin este filtro IC_bueno=-0.120 (n=140)

- **FILTRO** `T_h` > `71.5479` → IC=-0.202 (n=139)

  - _Acción_: SKIP cuando `T_h` > 71.5479
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=47)

- **FILTRO** `sigma_h` > `0.015` → IC=-0.379 (n=31)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.015
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=94)

- **FILTRO** `sigma_h` < `0.0087` → IC=-0.291 (n=41)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0087
  - _Potencial_: sin este filtro IC_bueno=-0.209 (n=84)

- **FILTRO** `T_h` > `33.8406` → IC=-0.268 (n=93)

  - _Acción_: SKIP cuando `T_h` > 33.8406
  - _Potencial_: sin este filtro IC_bueno=-0.147 (n=32)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1208` → IC=+0.468 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1208 (IC base=+0.338)

- **PATRÓN** `sigma_h` < `0.0146` → IC=+0.357 (n=103)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0146 (IC base=+0.338)

- **PATRÓN** `sigma_h` > `0.0106` → IC=+0.371 (n=68)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0106 (IC base=+0.338)

- **PATRÓN** `T_h` > `0.7452` → IC=+0.386 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.7452 (IC base=+0.338)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.480 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.338)

- **PATRÓN** `edge` > `0.1005` → IC=+0.437 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1005 (IC base=+0.409)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.414 (n=79)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0075 (IC base=+0.409)

- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.431 (n=158)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0097 (IC base=+0.409)

- **PATRÓN** `T_h` < `0.6127` → IC=+0.439 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.6127 (IC base=+0.409)

- **PATRÓN** `T_h` > `1.484` → IC=+0.414 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.484 (IC base=+0.409)

- **PATRÓN** `dist_50` > `0.376` → IC=+0.446 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.376 (IC base=+0.409)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.471 (n=138)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.409)

### RESOLUTION_SNIPER#BTC#sniper
- **PATRÓN** `edge` > `0.1506` → IC=+0.257 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1506 (IC base=+0.205)

- **PATRÓN** `sigma_h` < `0.0077` → IC=+0.281 (n=30)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0077 (IC base=+0.205)

- **PATRÓN** `T_h` < `1.484` → IC=+0.257 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 1.484 (IC base=+0.205)

- **PATRÓN** `dist_50` > `0.346` → IC=+0.284 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.346 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.281 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.205)

### RESOLUTION_SNIPER#ETH#sniper
- **PATRÓN** `edge` > `0.1023` → IC=+0.460 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1023 (IC base=+0.409)

- **PATRÓN** `sigma_h` < `0.0101` → IC=+0.411 (n=54)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0101 (IC base=+0.409)

- **PATRÓN** `sigma_h` > `0.0062` → IC=+0.395 (n=55)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0062 (IC base=+0.409)

- **PATRÓN** `T_h` < `1.2716` → IC=+0.429 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 1.2716 (IC base=+0.409)

- **PATRÓN** `dist_50` > `0.3502` → IC=+0.446 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3502 (IC base=+0.409)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.400 (n=28)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.409)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.441 (n=32)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.409)

### RESOLUTION_SNIPER#SOL#sniper
- **PATRÓN** `edge` > `0.1745` → IC=+0.485 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1745 (IC base=+0.433)

- **PATRÓN** `sigma_h` < `0.0161` → IC=+0.455 (n=65)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0161 (IC base=+0.433)

- **PATRÓN** `T_h` > `0.3968` → IC=+0.455 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.3968 (IC base=+0.433)

- **PATRÓN** `dist_50` > `0.3326` → IC=+0.470 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3326 (IC base=+0.433)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.441 (n=32)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.433)

- **PATRÓN** `edge` > `0.2005` → IC=+0.469 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.2005 (IC base=+0.461)

- **PATRÓN** `sigma_h` < `0.0156` → IC=+0.473 (n=145)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0156 (IC base=+0.461)

- **PATRÓN** `T_h` < `0.8279` → IC=+0.455 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.8279 (IC base=+0.461)

- **PATRÓN** `T_h` > `1.486` → IC=+0.481 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.486 (IC base=+0.461)

- **PATRÓN** `dist_50` > `0.4597` → IC=+0.492 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4597 (IC base=+0.461)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.466 (n=146)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.461)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=344)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.074 (n=414)

- **PATRÓN** `streak_estiramiento` < `0.3028` → IC=+0.163 (n=87)

  - _Acción_: Kelly boost +0.81€ cuando `streak_estiramiento` < 0.3028 (IC base=+0.015)

- **PATRÓN** `streak_estiramiento` < `0.8251` → IC=+0.142 (n=280)

  - _Acción_: Kelly boost +0.71€ cuando `streak_estiramiento` < 0.8251 (IC base=+0.060)

- **PATRÓN** `ballena_activa_n` < `33.0` → IC=+0.137 (n=210)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 33.0 (IC base=+0.060)

- **PATRÓN** `libro_liquidez` > `2502.8663` → IC=+0.136 (n=149)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 2502.8663 (IC base=+0.060)

### STREAK_FADE_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=17)

### STREAK_FADE_15M#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.113 (n=29)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=20)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.136 (n=20)

  - _Acción_: Kelly boost +0.68€ cuando `py_entrada` < 0.495 (IC base=+0.013)

### STREAK_FADE_15M#XRP#15min
- **FILTRO** `streak_estiramiento` > `0.4392` → IC=-0.203 (n=35)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.4392
  - _Potencial_: sin este filtro IC_bueno=+0.113 (n=109)

- **PATRÓN** `streak_estiramiento` < `0.3906` → IC=+0.122 (n=96)

  - _Acción_: Kelly boost +0.61€ cuando `streak_estiramiento` < 0.3906 (IC base=+0.026)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.133 (n=156)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 5.0 (IC base=+0.107)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.130 (n=106)

  - _Acción_: Kelly boost +0.65€ cuando `py_entrada` < 0.495 (IC base=+0.107)

- **PATRÓN** `streak_estiramiento` < `0.437` → IC=+0.204 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `streak_estiramiento` < 0.437 (IC base=+0.107)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.188 (n=126)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 34.0 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `2229.7597` → IC=+0.144 (n=130)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 2229.7597 (IC base=+0.107)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `9.0` → IC=-0.219 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=98)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.196 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=107)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=71)

- **FILTRO** `libro_liquidez` < `3678.6572` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 3678.6572
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=78)

- **FILTRO** `hora_utc` < `15.0` → IC=-0.210 (n=29)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=35)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=34)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=826)

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
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=1044)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=1335)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=1244)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=1292)

### STRUCT_NO_15M
- **FILTRO** `hora_utc` < `16.0` → IC=-0.167 (n=22)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.125 (n=22)

- **FILTRO** `py_entrada` < `0.455` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.113 (n=29)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=4288)

### STRUCT_NO_15M#ETH#15min
- **FILTRO** `hora_utc` < `16.0` → IC=-0.167 (n=22)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.125 (n=22)

- **FILTRO** `py_entrada` < `0.455` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.113 (n=29)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=2417)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0055` → IC=+0.188 (n=1751)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0055 (IC base=+0.166)

- **PATRÓN** `sigma_h` > `0.0124` → IC=+0.178 (n=1326)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` > 0.0124 (IC base=+0.166)

- **PATRÓN** `drift_60min` |x|≤ `0.1782` → IC=+0.184 (n=3502)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.1782 (IC base=+0.166)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1323` → IC=+0.175 (n=1600)

  - _Acción_: Kelly boost +0.87€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1323 (IC base=+0.166)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.175 (n=3678)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 6.0 (IC base=+0.166)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.167 (n=3685)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 15.0 (IC base=+0.166)

- **PATRÓN** `ibs_15` > `0.5333` → IC=+0.239 (n=3983)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5333 (IC base=+0.166)

- **PATRÓN** `dist_vwap_pct` > `0.1292` → IC=+0.163 (n=1924)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.1292 (IC base=+0.166)

- **PATRÓN** `dist_vwap_pct` < `0.4882` → IC=+0.152 (n=3635)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.4882 (IC base=+0.166)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.249` → IC=+0.256 (n=1023)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.249 (IC base=+0.166)

- **PATRÓN** `libro_liquidez` > `4564.5735` → IC=+0.181 (n=1326)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 4564.5735 (IC base=+0.166)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=1603)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.222 (n=677)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.206)

- **PATRÓN** `drift_60min` |x|≤ `0.0763` → IC=+0.250 (n=298)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0763 (IC base=+0.206)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2616` → IC=+0.224 (n=226)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2616 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.227 (n=709)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.206)

- **PATRÓN** `ibs_15` > `0.7223` → IC=+0.272 (n=677)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7223 (IC base=+0.206)

- **PATRÓN** `dist_vwap_pct` > `0.2372` → IC=+0.224 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2372 (IC base=+0.206)

- **PATRÓN** `dist_vwap_pct` < `0.5123` → IC=+0.211 (n=765)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5123 (IC base=+0.206)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.503` → IC=+0.301 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.503 (IC base=+0.206)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.208 (n=877)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.206)

- **PATRÓN** `libro_liquidez` > `8119.484` → IC=+0.217 (n=677)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8119.484 (IC base=+0.206)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.161 (n=808)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0067 (IC base=+0.142)

- **PATRÓN** `drift_60min` |x|≤ `0.151` → IC=+0.152 (n=711)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.151 (IC base=+0.142)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1412` → IC=+0.152 (n=539)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.76€ cuando `delta_ratio_macro` |x|> 0.1412 (IC base=+0.142)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1262` → IC=+0.152 (n=323)

  - _Acción_: Kelly boost +0.76€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1262 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.153 (n=738)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 6.0 (IC base=+0.142)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.145 (n=843)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 17.0 (IC base=+0.142)

- **PATRÓN** `ibs_15` > `0.6258` → IC=+0.260 (n=722)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6258 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` > `0.1197` → IC=+0.163 (n=494)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.1197 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.132` → IC=+0.271 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.132 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `5837.0711` → IC=+0.164 (n=367)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 5837.0711 (IC base=+0.142)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `ibs_15` > `0.2246` → IC=-0.123 (n=152)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.2246
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=298)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `ibs_15` > `0.88` → IC=+0.234 (n=321)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.88 (IC base=+0.080)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.127 (n=504)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.01 (IC base=+0.080)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0242` → IC=+0.229 (n=297)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0242 (IC base=+0.194)

- **PATRÓN** `drift_60min` |x|≤ `0.2004` → IC=+0.207 (n=892)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2004 (IC base=+0.194)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0965` → IC=+0.248 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0965 (IC base=+0.194)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.204 (n=800)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.194)

- **PATRÓN** `ibs_15` > `0.5156` → IC=+0.273 (n=891)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5156 (IC base=+0.194)

- **PATRÓN** `dist_vwap_pct` > `0.13` → IC=+0.211 (n=506)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.13 (IC base=+0.194)

- **PATRÓN** `dist_vwap_pct` < `0.7374` → IC=+0.194 (n=1038)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` < 0.7374 (IC base=+0.194)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.324` → IC=+0.233 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.324 (IC base=+0.194)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.195 (n=614)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.02 (IC base=+0.194)

- **PATRÓN** `libro_liquidez` > `2950.3352` → IC=+0.289 (n=297)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2950.3352 (IC base=+0.194)

- **PATRÓN** `ibs_15` < `0.1071` → IC=+0.169 (n=805)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.85€ cuando `ibs_15` < 0.1071 (IC base=+0.070)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` > `0.0057` → IC=+0.394 (n=225)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0057 (IC base=+0.365)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1501` → IC=+0.378 (n=449)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1501 (IC base=+0.365)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1379` → IC=+0.385 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1379 (IC base=+0.365)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.378 (n=678)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.365)

- **PATRÓN** `ibs_15` > `0.788` → IC=+0.398 (n=676)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.788 (IC base=+0.365)

- **PATRÓN** `dist_vwap_pct` > `0.1523` → IC=+0.385 (n=390)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1523 (IC base=+0.365)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.99` → IC=+0.393 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.99 (IC base=+0.365)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.369 (n=820)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.365)

- **PATRÓN** `libro_liquidez` > `3859.8614` → IC=+0.373 (n=603)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3859.8614 (IC base=+0.365)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.365 (n=302)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.358)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.397 (n=115)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.358)

- **PATRÓN** `drift_60min` |x|≤ `0.0553` → IC=+0.363 (n=115)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0553 (IC base=+0.358)

- **PATRÓN** `drift_15min` |x|≤ `0.5133` → IC=+0.357 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.5133 (IC base=+0.358)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1556` → IC=+0.365 (n=228)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1556 (IC base=+0.358)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1436` → IC=+0.390 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1436 (IC base=+0.358)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.378 (n=343)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.358)

- **PATRÓN** `ibs_15` > `0.8077` → IC=+0.384 (n=343)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8077 (IC base=+0.358)

- **PATRÓN** `dist_vwap_pct` > `0.3751` → IC=+0.382 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3751 (IC base=+0.358)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.163` → IC=+0.383 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.163 (IC base=+0.358)

- **PATRÓN** `libro_liquidez` > `8119.484` → IC=+0.381 (n=343)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8119.484 (IC base=+0.358)

- **PATRÓN** `ballena_activa_n` < `497.0` → IC=+0.397 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 497.0 (IC base=+0.358)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.368 (n=332)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0064 (IC base=+0.369)

- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.389 (n=151)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0058 (IC base=+0.369)

- **PATRÓN** `drift_60min` |x|≤ `0.1074` → IC=+0.370 (n=222)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1074 (IC base=+0.369)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0842` → IC=+0.383 (n=297)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0842 (IC base=+0.369)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2969` → IC=+0.385 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2969 (IC base=+0.369)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.394 (n=158)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.369)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.377 (n=152)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.369)

- **PATRÓN** `ibs_15` > `0.7557` → IC=+0.410 (n=332)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7557 (IC base=+0.369)

- **PATRÓN** `dist_vwap_pct` > `0.159` → IC=+0.379 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.159 (IC base=+0.369)

- **PATRÓN** `dist_vwap_pct` < `0.2918` → IC=+0.371 (n=308)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2918 (IC base=+0.369)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.293` → IC=+0.401 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.293 (IC base=+0.369)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.374 (n=372)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.369)

- **PATRÓN** `libro_liquidez` > `4045.1116` → IC=+0.402 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4045.1116 (IC base=+0.369)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0069` → IC=-0.175 (n=2289)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0069
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=2291)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.213 (n=1794)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=2786)

- **FILTRO** `libro_liquidez` < `4240.9508` → IC=-0.154 (n=3022)

  - _Acción_: SKIP cuando `libro_liquidez` < 4240.9508
  - _Potencial_: sin este filtro IC_bueno=+0.097 (n=1558)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.138` → IC=+0.217 (n=411)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.138 (IC base=-0.068)

- **PATRÓN** `ibs_15` > `0.6326` → IC=+0.279 (n=1104)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6326 (IC base=-0.068)

- **PATRÓN** `dist_vwap_pct` > `0.1115` → IC=+0.205 (n=636)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1115 (IC base=-0.068)

- **PATRÓN** `dist_vwap_pct` < `0.4263` → IC=+0.201 (n=1086)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4263 (IC base=-0.068)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2301` → IC=+0.273 (n=1312)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2301 (IC base=-0.011)

- **PATRÓN** `ibs_15` < `0.3676` → IC=+0.282 (n=3931)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3676 (IC base=-0.011)

- **PATRÓN** `dist_vwap_pct` > `0.8734` → IC=+0.276 (n=381)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8734 (IC base=-0.011)

- **PATRÓN** `dist_vwap_pct` < `0.1645` → IC=+0.247 (n=2949)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1645 (IC base=-0.011)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0334` → IC=-0.222 (n=2114)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0334
  - _Potencial_: sin este filtro IC_bueno=-0.097 (n=705)

- **FILTRO** `sigma_h` > `0.0067` → IC=-0.210 (n=704)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0067
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=2115)

- **FILTRO** `sigma_h` < `0.0035` → IC=-0.232 (n=704)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0035
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=2115)

- **FILTRO** `sigma_ewma_delta_pct` > `22.95` → IC=-0.270 (n=406)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 22.95
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=2413)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.161 (n=275)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0029 (IC base=+0.085)

- **PATRÓN** `ibs_15` > `0.7609` → IC=+0.327 (n=368)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7609 (IC base=+0.085)

- **PATRÓN** `dist_vwap_pct` > `0.1051` → IC=+0.282 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1051 (IC base=+0.085)

- **PATRÓN** `dist_vwap_pct` < `0.4958` → IC=+0.289 (n=410)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4958 (IC base=+0.085)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.15` → IC=+0.145 (n=240)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 19.15 (IC base=+0.085)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1026` → IC=+0.230 (n=61)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1026 (IC base=-0.191)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1323` → IC=+0.339 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1323 (IC base=-0.191)

- **PATRÓN** `ibs_15` < `0.618` → IC=+0.314 (n=68)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.618 (IC base=-0.191)

- **PATRÓN** `dist_vwap_pct` < `0.0415` → IC=+0.325 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0415 (IC base=-0.191)

- **PATRÓN** `ballena_activa_n` < `288.0` → IC=+0.372 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 288.0 (IC base=-0.191)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.159 (n=722)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.163 (n=488)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0058 (IC base=+0.152)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.161 (n=370)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` > 0.005 (IC base=+0.152)

- **PATRÓN** `drift_60min` |x|≤ `0.0721` → IC=+0.187 (n=244)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.0721 (IC base=+0.152)

- **PATRÓN** `drift_15min` |x|≤ `0.4011` → IC=+0.152 (n=185)

  - _Acción_: Kelly boost +0.76€ cuando `drift_15min` |x|≤ 0.4011 (IC base=+0.152)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.296` → IC=+0.193 (n=428)

  - _Acción_: Kelly boost +0.97€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.296 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.163 (n=561)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.152)

- **PATRÓN** `ibs_15` > `0.5867` → IC=+0.244 (n=556)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5867 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` > `0.4682` → IC=+0.167 (n=145)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.4682 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` < `0.1594` → IC=+0.154 (n=434)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.1594 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.12` → IC=+0.257 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.12 (IC base=+0.152)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.159 (n=722)

  - _Acción_: Kelly boost +0.79€ cuando `libro_spread` < 0.01 (IC base=+0.152)

- **PATRÓN** `libro_liquidez` > `9553.1781` → IC=+0.158 (n=185)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 9553.1781 (IC base=+0.152)

- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.263 (n=496)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.245)

- **PATRÓN** `drift_60min` |x|≤ `0.1036` → IC=+0.245 (n=497)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1036 (IC base=+0.245)

- **PATRÓN** `drift_15min` |x|≤ `0.7702` → IC=+0.256 (n=1309)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7702 (IC base=+0.245)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1536` → IC=+0.266 (n=992)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1536 (IC base=+0.245)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.245 (n=544)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.245)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.247 (n=1324)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.245)

- **PATRÓN** `ibs_15` < `0.3774` → IC=+0.277 (n=1488)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3774 (IC base=+0.245)

- **PATRÓN** `dist_vwap_pct` > `0.1547` → IC=+0.261 (n=541)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1547 (IC base=+0.245)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.389` → IC=+0.253 (n=654)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.389 (IC base=+0.245)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `drift_60min` |x|> `0.1723` → IC=-0.245 (n=359)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1723
  - _Potencial_: sin este filtro IC_bueno=-0.160 (n=697)

- **FILTRO** `drift_15min` |x|> `0.888` → IC=-0.281 (n=263)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.888
  - _Potencial_: sin este filtro IC_bueno=-0.158 (n=793)

- **FILTRO** `sigma_ewma_delta_pct` > `6.65` → IC=-0.205 (n=242)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.65
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=814)

- **FILTRO** `sigma_ewma_delta_pct` > `17.642` → IC=-0.148 (n=557)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 17.642
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=4431)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1478` → IC=+0.181 (n=45)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.90€ cuando `delta_ratio_macro` |x|> 0.1478 (IC base=-0.189)

- **PATRÓN** `ibs_15` > `0.5625` → IC=+0.234 (n=62)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5625 (IC base=-0.189)

- **PATRÓN** `dist_vwap_pct` < `0.4298` → IC=+0.162 (n=75)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.4298 (IC base=-0.189)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.214 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 37.0 (IC base=-0.189)

- **PATRÓN** `ibs_15` < `0.381` → IC=+0.290 (n=661)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.381 (IC base=-0.036)

- **PATRÓN** `dist_vwap_pct` < `0.2583` → IC=+0.237 (n=622)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2583 (IC base=-0.036)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0158` → IC=-0.236 (n=840)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0158
  - _Potencial_: sin este filtro IC_bueno=-0.151 (n=414)

- **FILTRO** `libro_spread` > `0.04` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.04
  - _Potencial_: sin este filtro IC_bueno=-0.207 (n=1235)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.209)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.209)

- **PATRÓN** `delta_ratio_macro` |x|> `0.07` → IC=+0.273 (n=816)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.07 (IC base=-0.024)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1182` → IC=+0.287 (n=398)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1182 (IC base=-0.024)

- **PATRÓN** `ibs_15` < `0.137` → IC=+0.312 (n=609)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.137 (IC base=-0.024)

- **PATRÓN** `dist_vwap_pct` > `0.7759` → IC=+0.346 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7759 (IC base=-0.024)

### UPDOWN_GBM_ETH_15M_HORA7
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.200 (n=18)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.089)

- **PATRÓN** `drift_60min` |x|≤ `0.1094` → IC=+0.167 (n=28)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.1094 (IC base=+0.089)

- **PATRÓN** `drift_15min` |x|≤ `0.3927` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3927 (IC base=+0.089)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.235` → IC=+0.204 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.235 (IC base=+0.089)

- **PATRÓN** `ibs_15` > `0.8434` → IC=+0.357 (n=19)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8434 (IC base=+0.089)

- **PATRÓN** `dist_vwap_pct` < `0.0974` → IC=+0.167 (n=22)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.0974 (IC base=+0.089)

- **PATRÓN** `libro_liquidez` > `3810.744` → IC=+0.141 (n=37)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 3810.744 (IC base=+0.089)

- **PATRÓN** `ballena_activa_n` < `102.0` → IC=+0.129 (n=33)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 102.0 (IC base=+0.089)

- **PATRÓN** `dist_vwap_pct` > `0.1533` → IC=+0.125 (n=70)

  - _Acción_: Kelly boost +0.62€ cuando `dist_vwap_pct` > 0.1533 (IC base=+0.053)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.200 (n=18)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.089)

- **PATRÓN** `drift_60min` |x|≤ `0.1094` → IC=+0.167 (n=28)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.1094 (IC base=+0.089)

- **PATRÓN** `drift_15min` |x|≤ `0.3927` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3927 (IC base=+0.089)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.235` → IC=+0.204 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.235 (IC base=+0.089)

- **PATRÓN** `ibs_15` > `0.8434` → IC=+0.357 (n=19)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8434 (IC base=+0.089)

- **PATRÓN** `dist_vwap_pct` < `0.0974` → IC=+0.167 (n=22)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.0974 (IC base=+0.089)

- **PATRÓN** `libro_liquidez` > `3810.744` → IC=+0.141 (n=37)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 3810.744 (IC base=+0.089)

- **PATRÓN** `ballena_activa_n` < `102.0` → IC=+0.129 (n=33)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 102.0 (IC base=+0.089)

- **PATRÓN** `dist_vwap_pct` > `0.1533` → IC=+0.125 (n=70)

  - _Acción_: Kelly boost +0.62€ cuando `dist_vwap_pct` > 0.1533 (IC base=+0.053)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.006` → IC=+0.289 (n=1183)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.006 (IC base=+0.284)

- **PATRÓN** `drift_60min` |x|≤ `0.0538` → IC=+0.319 (n=395)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0538 (IC base=+0.284)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1495` → IC=+0.286 (n=788)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1495 (IC base=+0.284)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.224` → IC=+0.294 (n=711)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.224 (IC base=+0.284)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.301 (n=1230)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.284)

- **PATRÓN** `ibs_15` > `0.8389` → IC=+0.314 (n=1182)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8389 (IC base=+0.284)

- **PATRÓN** `dist_vwap_pct` > `0.263` → IC=+0.315 (n=507)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.263 (IC base=+0.284)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.34` → IC=+0.379 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.34 (IC base=+0.284)

- **PATRÓN** `libro_liquidez` > `12019.5515` → IC=+0.303 (n=536)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12019.5515 (IC base=+0.284)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.307 (n=211)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.276)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.285 (n=287)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.276)

- **PATRÓN** `drift_60min` |x|≤ `0.0585` → IC=+0.312 (n=211)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0585 (IC base=+0.276)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2654` → IC=+0.276 (n=212)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2654 (IC base=+0.276)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3892` → IC=+0.282 (n=559)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3892 (IC base=+0.276)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.297 (n=664)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.276)

- **PATRÓN** `ibs_15` > `0.8292` → IC=+0.303 (n=632)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8292 (IC base=+0.276)

- **PATRÓN** `dist_vwap_pct` > `0.2516` → IC=+0.313 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2516 (IC base=+0.276)

- **PATRÓN** `dist_vwap_pct` < `0.547` → IC=+0.277 (n=710)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.547 (IC base=+0.276)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.503` → IC=+0.376 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.503 (IC base=+0.276)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.277 (n=817)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.276)

- **PATRÓN** `libro_liquidez` > `12879.5491` → IC=+0.304 (n=421)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12879.5491 (IC base=+0.276)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.306 (n=551)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0067 (IC base=+0.292)

- **PATRÓN** `drift_60min` |x|≤ `0.1077` → IC=+0.316 (n=368)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1077 (IC base=+0.292)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0665` → IC=+0.296 (n=551)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0665 (IC base=+0.292)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1028` → IC=+0.331 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1028 (IC base=+0.292)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.310 (n=531)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.292)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.294 (n=499)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.292)

- **PATRÓN** `ibs_15` > `0.8494` → IC=+0.325 (n=551)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8494 (IC base=+0.292)

- **PATRÓN** `dist_vwap_pct` > `0.2797` → IC=+0.320 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2797 (IC base=+0.292)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.34` → IC=+0.371 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.34 (IC base=+0.292)

### UPDOWN_OU_5M
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1259` → IC=-0.156 (n=88)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1259
  - _Potencial_: sin este filtro IC_bueno=-0.102 (n=264)

- **FILTRO** `ballena_activa_n` > `39.0` → IC=-0.133 (n=238)

  - _Acción_: SKIP cuando `ballena_activa_n` > 39.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=82)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.1228` → IC=-0.211 (n=119)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1228
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=368)

- **FILTRO** `sigma_h` > `0.007` → IC=-0.183 (n=121)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.007
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=366)

- **FILTRO** `drift_15min` |x|> `0.3082` → IC=-0.141 (n=243)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.3082
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=244)

### UPDOWN_OU_5M#BNB#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1682` → IC=-0.191 (n=40)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1682
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=41)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.160 (n=48)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=54)

### UPDOWN_OU_5M#BTC#5min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1342` → IC=-0.154 (n=50)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1342
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=153)

- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.2203` → IC=-0.129 (n=95)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.2203
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=96)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.2065` → IC=-0.259 (n=27)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2065
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=28)

- **FILTRO** `ballena_activa_n` > `595.0` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `ballena_activa_n` > 595.0
  - _Potencial_: sin este filtro IC_bueno=-0.118 (n=32)

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
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1149` → IC=-0.206 (n=15)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1149
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=45)

- **FILTRO** `drift_15min` |x|> `0.1649` → IC=-0.333 (n=22)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.1649
  - _Potencial_: sin este filtro IC_bueno=-0.269 (n=11)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `sigma_h` < `0.0083` → IC=-0.167 (n=31)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0083
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=17)

- **FILTRO** `ballena_activa_n` > `19.0` → IC=-0.206 (n=32)

  - _Acción_: SKIP cuando `ballena_activa_n` > 19.0
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=11)

- **FILTRO** `sigma_h` < `0.0051` → IC=-0.250 (n=18)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0051
  - _Potencial_: sin este filtro IC_bueno=-0.159 (n=39)

- **FILTRO** `drift_15min` |x|> `0.2309` → IC=-0.225 (n=38)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.2309
  - _Potencial_: sin este filtro IC_bueno=-0.119 (n=19)

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
- **PATRÓN** `T_h` > `103.5964` → IC=+0.179 (n=475)

  - _Acción_: Kelly boost +0.90€ cuando `T_h` > 103.5964 (IC base=+0.176)

- **PATRÓN** `ratio` < `0.973` → IC=+0.393 (n=316)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.973 (IC base=+0.176)

- **PATRÓN** `T_h` > `115.2222` → IC=+0.354 (n=2441)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 115.2222 (IC base=+0.335)

- **PATRÓN** `ratio` > `1.0221` → IC=+0.377 (n=396)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0221 (IC base=+0.335)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `111.2289` → IC=+0.158 (n=223)

  - _Acción_: Kelly boost +0.79€ cuando `T_h` > 111.2289 (IC base=+0.141)

- **PATRÓN** `ratio` < `0.9831` → IC=+0.309 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9831 (IC base=+0.141)

- **PATRÓN** `T_h` > `111.9836` → IC=+0.309 (n=851)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9836 (IC base=+0.295)

- **PATRÓN** `ratio` > `1.0429` → IC=+0.414 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0429 (IC base=+0.295)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `83.3501` → IC=+0.223 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 83.3501 (IC base=+0.220)

- **PATRÓN** `ratio` < `0.9854` → IC=+0.392 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9854 (IC base=+0.220)

- **PATRÓN** `T_h` > `111.9957` → IC=+0.352 (n=870)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9957 (IC base=+0.322)

- **PATRÓN** `ratio` > `1.0321` → IC=+0.391 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0321 (IC base=+0.322)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.0625` → IC=+0.437 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.0625 (IC base=+0.398)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5333 sube el IC de +0.166 a +0.239 en UPDOWN_GBM#15min (n=3983). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7223 sube el IC de +0.206 a +0.272 en UPDOWN_GBM#BTC#15min (n=677). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.6258 sube el IC de +0.142 a +0.260 en UPDOWN_GBM#ETH#15min (n=722). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.88 sube el IC de +0.080 a +0.234 en UPDOWN_GBM#SOL#15min (n=321). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5156 sube el IC de +0.194 a +0.273 en UPDOWN_GBM#XRP#15min (n=891). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1071 sube el IC de +0.070 a +0.169 en UPDOWN_GBM#XRP#15min (n=805). Ya aplicado como kelly_boost=+0.85€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6326 sube el IC de -0.068 a +0.279 en UPDOWN_GBM_15M_TARDIO (n=1104). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3676 sube el IC de -0.011 a +0.282 en UPDOWN_GBM_15M_TARDIO (n=3931). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7609 sube el IC de +0.085 a +0.327 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=368). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.618 sube el IC de -0.191 a +0.314 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=68). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.5867 sube el IC de +0.152 a +0.244 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=556). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3774 sube el IC de +0.245 a +0.277 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=1488). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de -0.189 a +0.234 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=62). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.381 sube el IC de -0.036 a +0.290 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=661). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.209 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.137 sube el IC de -0.024 a +0.312 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=609). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_YES, IBS > 0.8434 sube el IC de +0.089 a +0.357 en UPDOWN_GBM_ETH_15M_HORA7 (n=19). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_YES, IBS > 0.8434 sube el IC de +0.089 a +0.357 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=19). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8389 sube el IC de +0.284 a +0.314 en UPDOWN_GBM_IBS_ALTO (n=1182). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8292 sube el IC de +0.276 a +0.303 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=632). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8494 sube el IC de +0.292 a +0.325 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=551). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.788 sube el IC de +0.365 a +0.398 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=676). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8077 sube el IC de +0.358 a +0.384 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=343). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7557 sube el IC de +0.369 a +0.410 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=332). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 2020 | +0.090 | +216.83€ | 0 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 2020 | +0.090 | +216.83€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1628 | +0.093 | +188.10€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1628 | +0.093 | +188.10€ | 0 | 9 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 284 | +0.070 | +11.30€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 284 | +0.070 | +11.30€ | 5 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 77 | +0.108 | +17.77€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 77 | +0.108 | +17.77€ | 0 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 816 | -0.010 | +86.02€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 816 | -0.010 | +86.02€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE | 6 | +0.000 | +1.70€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE#15min | 6 | +0.000 | +1.70€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 625 | -0.036 | +52.72€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 625 | -0.036 | +52.72€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 149 | +0.089 | +26.84€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 149 | +0.089 | +26.84€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 36 | +0.026 | +4.76€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 36 | +0.026 | +4.76€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 42896 | -0.083 | -5534.50€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 2497 | +0.055 | -276.85€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 40399 | -0.092 | -5257.65€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4604 | -0.117 | -760.86€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4604 | -0.117 | -760.86€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 2497 | +0.055 | -276.85€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 2497 | +0.055 | -276.85€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 4554 | -0.113 | -862.35€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 4554 | -0.113 | -862.35€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 11483 | -0.024 | -1190.01€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 11483 | -0.024 | -1190.01€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 11467 | -0.118 | -1087.61€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 11467 | -0.118 | -1087.61€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 8291 | -0.124 | -1356.83€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 8291 | -0.124 | -1356.83€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 39806 | -0.013 | +3212.22€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 10272 | +0.004 | +1625.31€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 29534 | -0.020 | +1586.91€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 39806 | -0.013 | +3212.22€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 10272 | +0.004 | +1625.31€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 29534 | -0.020 | +1586.91€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 159831 | +0.115 | -6333.87€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 19810 | +0.181 | -670.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 716 | -0.008 | -73.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 129892 | +0.107 | -5267.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 9413 | +0.096 | -322.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 21528 | +0.107 | -1330.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 65 | -0.172 | +7.58€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 21448 | +0.108 | -1325.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 30723 | +0.126 | -477.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5398 | +0.182 | -221.44€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 21516 | +0.121 | -123.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 3767 | +0.081 | -110.02€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 21583 | +0.100 | -1491.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 80 | -0.122 | -5.27€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 21488 | +0.101 | -1475.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 34042 | +0.124 | -643.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 8731 | +0.177 | -197.39€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 21828 | +0.107 | -394.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 3471 | +0.101 | -43.00€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 30401 | +0.114 | -1434.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 5462 | +0.198 | -260.87€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 619 | +0.022 | -19.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 22145 | +0.096 | -984.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 2175 | +0.116 | -169.25€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO#XRP | 21554 | +0.107 | -956.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 74 | -0.105 | +6.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 21467 | +0.108 | -963.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 25792 | +0.195 | -1630.26€ | 2 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 25792 | +0.195 | -1630.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 5843 | +0.178 | -506.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 5843 | +0.178 | -506.16€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 3447 | +0.202 | -91.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 3447 | +0.202 | -91.42€ | 3 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 5775 | +0.178 | -479.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 5775 | +0.178 | -479.42€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 4954 | +0.247 | -182.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 4954 | +0.247 | -182.62€ | 0 | 4 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 5694 | +0.186 | -384.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 5694 | +0.186 | -384.40€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 1103 | +0.426 | -39.84€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 1103 | +0.426 | -39.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 442 | +0.437 | -5.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 442 | +0.437 | -5.83€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE#15min | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 440 | +0.428 | -13.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 440 | +0.428 | -13.14€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 207 | +0.400 | -17.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 207 | +0.400 | -17.00€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 90425 | +0.201 | -6460.72€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 90425 | +0.201 | -6460.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 15549 | +0.185 | -1620.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 15549 | +0.185 | -1620.66€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 14590 | +0.225 | -481.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 14590 | +0.225 | -481.29€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 15505 | +0.181 | -1633.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 15505 | +0.181 | -1633.15€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 14704 | +0.218 | -582.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 14704 | +0.218 | -582.71€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 14994 | +0.203 | -961.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 14994 | +0.203 | -961.70€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 15083 | +0.198 | -1181.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 15083 | +0.198 | -1181.23€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 34695 | +0.117 | +267.54€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 34695 | +0.117 | +267.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 17251 | +0.119 | +209.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 17251 | +0.119 | +209.15€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 17444 | +0.114 | +58.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 17444 | +0.114 | +58.38€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 2238 | +0.295 | +1.19€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 2238 | +0.295 | +1.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 1027 | +0.281 | -23.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 1027 | +0.281 | -23.77€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 1086 | +0.301 | +21.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 1086 | +0.301 | +21.32€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 125 | +0.343 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 125 | +0.343 | +3.65€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 1029 | +0.444 | +8.98€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 1029 | +0.444 | +8.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 500 | +0.436 | -4.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 500 | +0.436 | -4.48€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 482 | +0.453 | +12.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 482 | +0.453 | +12.76€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 47 | +0.398 | +0.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 47 | +0.398 | +0.70€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1771 | +0.069 | -77.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 699 | +0.045 | -64.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 1072 | +0.084 | -12.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1352 | +0.076 | -35.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 280 | +0.046 | -22.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 1072 | +0.084 | -12.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 337 | +0.028 | -45.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 337 | +0.028 | -45.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 69229 | +0.101 | -1645.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 5587 | +0.092 | +71.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 63642 | +0.102 | -1716.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 37973 | +0.106 | -385.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 5587 | +0.092 | +71.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 32386 | +0.108 | -456.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 14429 | +0.110 | -56.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 14429 | +0.110 | -56.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 16827 | +0.083 | -1203.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 16827 | +0.083 | -1203.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 900 | +0.191 | -110.64€ | 3 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 900 | +0.191 | -110.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 900 | +0.191 | -110.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 900 | +0.191 | -110.64€ | 3 | 4 |
| ✅ GBM_LATE_15M | 47321 | +0.096 | +25204.90€ | 0 | 18 |
| ✅ GBM_LATE_15M#15min | 47321 | +0.096 | +25204.90€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 7867 | +0.221 | +6635.13€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 7867 | +0.221 | +6635.13€ | 0 | 23 |
| ✅ GBM_LATE_15M#BTC | 7195 | +0.178 | +5580.15€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 7195 | +0.178 | +5580.15€ | 0 | 22 |
| ✅ GBM_LATE_15M#DOGE | 8478 | +0.204 | +6570.45€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 8478 | +0.204 | +6570.45€ | 0 | 19 |
| ✅ GBM_LATE_15M#ETH | 6505 | +0.047 | +1908.37€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 6505 | +0.047 | +1908.37€ | 1 | 17 |
| ✅ GBM_LATE_15M#SOL | 6622 | -0.032 | +1459.17€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 6622 | -0.032 | +1459.17€ | 3 | 14 |
| ✅ GBM_LATE_15M#XRP | 10654 | -0.028 | +3051.64€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 10654 | -0.028 | +3051.64€ | 4 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 50473 | +0.085 | +27876.58€ | 0 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 50473 | +0.085 | +27876.58€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 9746 | +0.001 | +4912.84€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 9746 | +0.001 | +4912.84€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 10796 | +0.009 | +2726.42€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 10796 | +0.009 | +2726.42€ | 0 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 6938 | +0.283 | +7592.49€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 6938 | +0.283 | +7592.49€ | 0 | 23 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 9314 | +0.013 | +2425.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 9314 | +0.013 | +2425.28€ | 1 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 7931 | +0.040 | +3326.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 7931 | +0.040 | +3326.93€ | 3 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 5748 | +0.309 | +6892.62€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 5748 | +0.309 | +6892.62€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 37494 | +0.180 | +30639.03€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 37494 | +0.180 | +30639.03€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 5667 | +0.236 | +5177.31€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 5667 | +0.236 | +5177.31€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 5892 | +0.148 | +4402.66€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 5892 | +0.148 | +4402.66€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 6032 | +0.221 | +5132.90€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 6032 | +0.221 | +5132.90€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 6381 | +0.136 | +4970.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 6381 | +0.136 | +4970.16€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 7061 | +0.123 | +5258.46€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 7061 | +0.123 | +5258.46€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 6461 | +0.227 | +5697.55€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 6461 | +0.227 | +5697.55€ | 0 | 28 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 10005 | +0.127 | +4851.91€ | 0 | 13 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 10005 | +0.127 | +4851.91€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 455 | +0.161 | +292.82€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 455 | +0.161 | +292.82€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 2879 | +0.134 | +1582.15€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 2879 | +0.134 | +1582.15€ | 0 | 16 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 476 | +0.153 | +248.05€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 476 | +0.153 | +248.05€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 3016 | +0.135 | +1443.04€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 3016 | +0.135 | +1443.04€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 2525 | +0.099 | +981.00€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 2525 | +0.099 | +981.00€ | 1 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 654 | +0.134 | +304.84€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 654 | +0.134 | +304.84€ | 0 | 26 |
| ✅ GBM_LATE_15M_TARDIO | 47580 | +0.185 | +38392.24€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#15min | 47580 | +0.185 | +38392.24€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 7510 | +0.246 | +7135.47€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 7510 | +0.246 | +7135.47€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 7474 | +0.144 | +5188.97€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 7474 | +0.144 | +5188.97€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 8048 | +0.232 | +7157.24€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 8048 | +0.232 | +7157.24€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 7859 | +0.138 | +5635.10€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 7859 | +0.138 | +5635.10€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 8460 | +0.118 | +5872.89€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 8460 | +0.118 | +5872.89€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 8229 | +0.234 | +7402.57€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 8229 | +0.234 | +7402.57€ | 0 | 22 |
| ✅ GBM_LATE_5M | 12638 | +0.205 | +10013.64€ | 1 | 28 |
| ✅ GBM_LATE_5M#5min | 12638 | +0.205 | +10013.64€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 1037 | +0.245 | +978.75€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 1037 | +0.245 | +978.75€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 3025 | +0.213 | +2637.86€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 3025 | +0.213 | +2637.86€ | 0 | 24 |
| ✅ GBM_LATE_5M#DOGE | 1216 | +0.197 | +905.95€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1216 | +0.197 | +905.95€ | 0 | 20 |
| ✅ GBM_LATE_5M#ETH | 3559 | +0.195 | +2530.29€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 3559 | +0.195 | +2530.29€ | 0 | 25 |
| ✅ GBM_LATE_5M#SOL | 1848 | +0.194 | +1431.30€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 1848 | +0.194 | +1431.30€ | 0 | 26 |
| ✅ GBM_LATE_5M#XRP | 1953 | +0.209 | +1529.48€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1953 | +0.209 | +1529.48€ | 0 | 0 |
| ✅ GBM_LATE_60M | 4031 | +0.059 | +1192.34€ | 0 | 7 |
| ✅ GBM_LATE_60M#60min | 4031 | +0.059 | +1192.34€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 1453 | +0.073 | +488.59€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 1453 | +0.073 | +488.59€ | 1 | 5 |
| ✅ GBM_LATE_60M#ETH | 1306 | +0.060 | +415.51€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 1306 | +0.060 | +415.51€ | 0 | 7 |
| ✅ GBM_LATE_60M#SOL | 1272 | +0.041 | +288.25€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 1272 | +0.041 | +288.25€ | 0 | 10 |
| 🚫 GBM_LATE_60M_FADE | 622 | -0.252 | -30.78€ | 9 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 622 | -0.252 | -30.78€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 233 | -0.253 | -18.28€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 233 | -0.253 | -18.28€ | 3 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 223 | -0.238 | -2.91€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 223 | -0.238 | -2.91€ | 5 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 166 | -0.262 | -9.58€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 166 | -0.262 | -9.58€ | 6 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 1688 | +0.083 | +414.06€ | 1 | 12 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 1688 | +0.083 | +414.06€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 660 | +0.079 | +152.71€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 660 | +0.079 | +152.71€ | 1 | 8 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 584 | +0.055 | +91.01€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 584 | +0.055 | +91.01€ | 2 | 12 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 444 | +0.128 | +170.34€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 444 | +0.128 | +170.34€ | 2 | 11 |
| ✅ LATE_WINDOW_5MIN | 181 | +0.276 | +178.48€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 181 | +0.276 | +178.48€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 181 | +0.276 | +178.48€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 181 | +0.276 | +178.48€ | 1 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 3775 | +0.100 | +904.42€ | 0 | 1 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 3775 | +0.100 | +904.42€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 3775 | +0.100 | +904.42€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 3775 | +0.100 | +904.42€ | 0 | 1 |
| ✅ LIQUIDACIONES_15M | 697 | -0.019 | -4.54€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 697 | -0.019 | -4.54€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 6 | -0.037 | -1.04€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 6 | -0.037 | -1.04€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 213 | -0.016 | +2.05€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 213 | -0.016 | +2.05€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 27 | -0.155 | -4.74€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 27 | -0.155 | -4.74€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 166 | +0.030 | +7.05€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 166 | +0.030 | +7.05€ | 2 | 2 |
| ✅ LIQUIDACIONES_15M#SOL | 233 | -0.002 | +2.06€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 233 | -0.002 | +2.06€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 3929 | +0.017 | +97.25€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 3929 | +0.017 | +97.25€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 185 | +0.029 | -0.77€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 185 | +0.029 | -0.77€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 812 | +0.013 | +37.25€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 812 | +0.013 | +37.25€ | 2 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 214 | -0.005 | -1.58€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 214 | -0.005 | -1.58€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 1487 | +0.023 | +31.24€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1487 | +0.023 | +31.24€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 761 | +0.011 | +1.65€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 761 | +0.011 | +1.65€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 470 | +0.015 | +29.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 470 | +0.015 | +29.46€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 1943 | -0.039 | -28.82€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1943 | -0.039 | -28.82€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 579 | -0.030 | -12.50€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 579 | -0.030 | -12.50€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 673 | -0.017 | +5.80€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 673 | -0.017 | +5.80€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 691 | -0.069 | -22.13€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 691 | -0.069 | -22.13€ | 6 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 10866 | -0.029 | -26.26€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 5190 | -0.034 | -63.81€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 5676 | -0.025 | +37.55€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 332 | -0.039 | -11.61€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 169 | -0.009 | +5.35€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 163 | -0.070 | -16.96€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 2792 | -0.017 | +44.38€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 1324 | -0.020 | +11.08€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 1468 | -0.014 | +33.30€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 1150 | -0.026 | +15.00€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 584 | -0.034 | -2.52€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 566 | -0.018 | +17.53€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 2414 | -0.040 | -67.62€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 1135 | -0.047 | -50.58€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 1279 | -0.033 | -17.04€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 2103 | -0.023 | +22.69€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 1014 | -0.029 | -1.97€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 1089 | -0.017 | +24.66€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 2075 | -0.038 | -29.10€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 964 | -0.045 | -25.16€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 1111 | -0.032 | -3.94€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 55780 | -0.000 | +2852.52€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 55780 | -0.000 | +2852.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 10079 | +0.026 | +1298.14€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 10079 | +0.026 | +1298.14€ | 2 | 4 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 7952 | -0.035 | -133.08€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 7952 | -0.035 | -133.08€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 10196 | +0.023 | +1056.83€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 10196 | +0.023 | +1056.83€ | 1 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 7825 | -0.048 | -154.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 7825 | -0.048 | -154.00€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 9451 | -0.005 | +260.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 9451 | -0.005 | +260.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 10277 | +0.017 | +524.61€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 10277 | +0.017 | +524.61€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 6839 | -0.057 | -151.89€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 6839 | -0.057 | -151.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1235 | -0.002 | -17.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1235 | -0.002 | -17.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1860 | -0.072 | -38.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1860 | -0.072 | -38.20€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 63 | -0.038 | -1.68€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 63 | -0.038 | -1.68€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 787 | -0.120 | -34.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 787 | -0.120 | -34.24€ | 5 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 2036 | -0.071 | -34.51€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 2036 | -0.071 | -34.51€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 858 | -0.016 | -26.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 858 | -0.016 | -26.02€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3371 | +0.004 | +0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3371 | +0.004 | +0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 132 | -0.037 | -1.23€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 132 | -0.037 | -1.23€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 193 | +0.013 | -0.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 193 | +0.013 | -0.26€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 139 | -0.004 | -2.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 139 | -0.004 | -2.34€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1325 | +0.006 | +6.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1325 | +0.006 | +6.88€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1391 | +0.007 | -0.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1391 | +0.007 | -0.19€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 191 | -0.008 | -2.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 191 | -0.008 | -2.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 137781 | -0.077 | +1751.86€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 137781 | -0.077 | +1751.86€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 24020 | -0.079 | +1280.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 24020 | -0.079 | +1280.85€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 20693 | -0.100 | -1036.01€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 20693 | -0.100 | -1036.01€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 24332 | -0.069 | +1184.06€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 24332 | -0.069 | +1184.06€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 20237 | -0.097 | -634.04€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 20237 | -0.097 | -634.04€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 24691 | -0.058 | +298.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 24691 | -0.058 | +298.02€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 23808 | -0.069 | +658.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 23808 | -0.069 | +658.98€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 8894 | -0.034 | -179.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 8894 | -0.034 | -179.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 1002 | -0.017 | -19.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 1002 | -0.017 | -19.42€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 2045 | -0.047 | -28.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 2045 | -0.047 | -28.54€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2612 | -0.026 | -40.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2612 | -0.026 | -40.54€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1230 | -0.058 | -27.64€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1230 | -0.058 | -27.64€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 996 | -0.030 | -31.63€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 996 | -0.030 | -31.63€ | 0 | 0 |
| ✅ ORDER_FLOW_5M | 1846 | +0.122 | +748.44€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#5min | 1710 | +0.127 | +735.85€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 401 | +0.130 | +189.59€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 401 | +0.130 | +189.59€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#DOGE | 351 | +0.115 | +118.57€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 351 | +0.115 | +118.57€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#ETH | 328 | +0.139 | +164.63€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 328 | +0.139 | +164.63€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#SOL | 301 | +0.150 | +164.82€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 301 | +0.150 | +164.82€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#XRP | 329 | +0.101 | +98.25€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 329 | +0.101 | +98.25€ | 0 | 3 |
| ✅ ORDER_FLOW_5M_REACTIVO | 1696 | -0.018 | -33.27€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 1696 | -0.018 | -33.27€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 324 | -0.003 | +6.74€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 324 | -0.003 | +6.74€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 305 | -0.028 | -5.94€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 305 | -0.028 | -5.94€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 429 | -0.052 | -41.89€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 429 | -0.052 | -41.89€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 360 | +0.008 | +4.87€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 360 | +0.008 | +4.87€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 278 | -0.007 | +2.95€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 278 | -0.007 | +2.95€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 990 | -0.073 | -45.81€ | 3 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 459 | -0.107 | -77.97€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 357 | -0.132 | -63.90€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 102 | -0.019 | -14.08€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 347 | -0.033 | +24.24€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 249 | -0.022 | +27.82€ | 2 | 2 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 98 | -0.060 | -3.59€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 184 | -0.059 | +7.93€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 152 | -0.065 | +4.05€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 32 | -0.029 | +3.88€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 758 | -0.083 | -32.02€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 232 | -0.038 | -13.79€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 1231 | -0.207 | -76.70€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC | 481 | -0.208 | -46.79€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#atexpiry | 423 | -0.211 | -46.05€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 58 | -0.183 | -0.74€ | 1 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 416 | -0.210 | -35.28€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 367 | -0.221 | -41.78€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 49 | -0.128 | +6.50€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 334 | -0.199 | +5.36€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 311 | -0.197 | +2.65€ | 5 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 23 | -0.220 | +2.71€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 1101 | -0.211 | -85.17€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 130 | -0.174 | +8.47€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 485 | +0.389 | +464.78€ | 0 | 12 |
| ✅ RESOLUTION_SNIPER#BTC | 80 | +0.171 | +63.15€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 80 | +0.171 | +63.15€ | 0 | 5 |
| ✅ RESOLUTION_SNIPER#ETH | 112 | +0.360 | +101.13€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 112 | +0.360 | +101.13€ | 0 | 7 |
| ✅ RESOLUTION_SNIPER#SOL | 293 | +0.456 | +300.51€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 293 | +0.456 | +300.51€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#sniper | 485 | +0.389 | +464.78€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 796 | +0.040 | +72.17€ | 2 | 4 |
| ✅ STREAK_FADE_15M#15min | 796 | +0.040 | +72.17€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 307 | +0.021 | +2.87€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 307 | +0.021 | +2.87€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 66 | +0.000 | -0.10€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 66 | +0.000 | -0.10€ | 1 | 0 |
| ✅ STREAK_FADE_15M#SOL | 79 | +0.006 | +4.43€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 79 | +0.006 | +4.43€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 344 | +0.072 | +64.97€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 344 | +0.072 | +64.97€ | 1 | 6 |
| ✅ STREAK_FADE_5M | 3533 | -0.023 | -141.96€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3533 | -0.023 | -141.96€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 1127 | -0.023 | -40.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 1127 | -0.023 | -40.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 599 | -0.029 | -27.49€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 599 | -0.029 | -27.49€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 168 | -0.041 | -14.30€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 168 | -0.041 | -14.30€ | 4 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1639 | -0.019 | -59.97€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1639 | -0.019 | -59.97€ | 1 | 0 |
| ✅ STREAK_FADE_60M | 103 | -0.052 | -9.27€ | 6 | 0 |
| ✅ STREAK_FADE_60M#60min | 103 | -0.052 | -9.27€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 43 | -0.100 | -5.07€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 43 | -0.100 | -5.07€ | 4 | 0 |
| ✅ STREAK_FADE_60M#SOL | 60 | -0.016 | -4.20€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 60 | -0.016 | -4.20€ | 0 | 2 |
| ✅ STREAK_MOM_5M | 11310 | +0.015 | +78.75€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 11310 | +0.015 | +78.75€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2888 | +0.020 | +29.31€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2888 | +0.020 | +29.31€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2937 | +0.018 | +35.20€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2937 | +0.018 | +35.20€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2907 | +0.008 | -3.40€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2907 | +0.008 | -3.40€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2578 | +0.014 | +17.65€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2578 | +0.014 | +17.65€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 10381 | +0.014 | -44.43€ | 2 | 0 |
| ✅ STRUCT_NO_15M#15min | 10381 | +0.014 | -44.43€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 4307 | +0.019 | -4.06€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 4307 | +0.019 | -4.06€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3623 | +0.010 | -28.56€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3623 | +0.010 | -28.56€ | 2 | 0 |
| ✅ STRUCT_NO_15M#SOL | 2451 | +0.010 | -11.81€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 2451 | +0.010 | -11.81€ | 1 | 0 |
| ✅ UPDOWN_GBM | 84516 | +0.055 | +7556.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 20629 | +0.083 | +4443.29€ | 0 | 11 |
| ✅ UPDOWN_GBM#240min | 2686 | +0.003 | +33.21€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 55839 | +0.053 | +2998.63€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 5059 | +0.004 | +87.29€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 6940 | +0.091 | +1107.30€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1576 | +0.156 | +698.08€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 77 | -0.006 | -0.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 5287 | +0.073 | +410.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 19216 | +0.057 | +1656.20€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 2802 | +0.086 | +653.99€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 744 | +0.005 | +14.25€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 13287 | +0.064 | +923.03€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 2274 | +0.001 | +63.24€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 109 | -0.077 | +1.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 8928 | +0.071 | +941.53€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1555 | +0.147 | +610.96€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 78 | +0.013 | -1.79€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 7295 | +0.055 | +332.36€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 19989 | +0.046 | +1335.05€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 5017 | +0.071 | +767.65€ | 0 | 10 |
| ✅ UPDOWN_GBM#ETH#240min | 717 | +0.008 | +18.67€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 12331 | +0.045 | +532.66€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 1822 | +0.005 | +14.52€ | 1 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 102 | -0.106 | +1.55€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 18407 | +0.035 | +963.45€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 5276 | +0.035 | +415.29€ | 0 | 2 |
| ✅ UPDOWN_GBM#SOL#240min | 682 | -0.009 | +2.99€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 11396 | +0.041 | +543.06€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 963 | +0.006 | +9.54€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#daily | 90 | -0.141 | -7.42€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 11034 | +0.067 | +1554.69€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 4403 | +0.103 | +1297.32€ | 0 | 11 |
| ✅ UPDOWN_GBM#XRP#240min | 388 | +0.010 | -0.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 6243 | +0.046 | +257.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 301 | -0.107 | -4.19€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 899 | +0.365 | +326.37€ | 0 | 9 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 899 | +0.365 | +326.37€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 457 | +0.358 | +152.01€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 457 | +0.358 | +152.01€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 442 | +0.369 | +174.36€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 442 | +0.369 | +174.36€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO | 21171 | -0.023 | +5009.00€ | 3 | 8 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 21171 | -0.023 | +5009.00€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1718 | -0.056 | +502.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1718 | -0.056 | +502.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 3918 | -0.114 | +143.10€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 3918 | -0.114 | +143.10€ | 4 | 10 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 948 | +0.216 | +770.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 948 | +0.216 | +770.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 2722 | +0.220 | +1760.45€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 2722 | +0.220 | +1760.45€ | 1 | 21 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 6044 | -0.063 | +783.76€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 6044 | -0.063 | +783.76€ | 4 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 5821 | -0.064 | +1048.42€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 5821 | -0.064 | +1048.42€ | 2 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 258 | +0.061 | +24.94€ | 0 | 9 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 258 | +0.061 | +24.94€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 258 | +0.061 | +24.94€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 258 | +0.061 | +24.94€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1576 | +0.284 | +1307.93€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1576 | +0.284 | +1307.93€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 842 | +0.276 | +648.84€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 842 | +0.276 | +648.84€ | 0 | 12 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 734 | +0.292 | +659.09€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 734 | +0.292 | +659.09€ | 0 | 9 |
| ✅ UPDOWN_OU_5M | 839 | -0.114 | -84.67€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#5min | 839 | -0.114 | -84.67€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 258 | -0.085 | -20.19€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 258 | -0.085 | -20.19€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 93 | -0.174 | -11.12€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 93 | -0.174 | -11.12€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 105 | -0.173 | -4.00€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 105 | -0.173 | -4.00€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 38 | -0.175 | -6.61€ | 2 | 0 |
| ✅ WEEKLY_PRICE | 3989 | +0.301 | +1842.77€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 1492 | +0.255 | +175.33€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 1531 | +0.294 | +665.08€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 966 | +0.380 | +1002.36€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**〰️ H-IBS-15** — IBS-15 como señal de mean-reversion
  - _Umbral_: n≥40 ops con ibs_15 en features y spread_IC>0.15 entre buckets
  - _Acción_: Añadir ibs_15 como boost/filtro en FEATURE_RULES de shadow_postmortem.py
  - _Estado_: Spread bajo (0.041) — sin ventaja clara. oversold(IBS<0.3): IC=+0.066 n=29358 | neutral: IC=+0.058 n=31302 | overbought(IBS>0.7): IC=+0.099 n=29591
  - _Datos_: n=93816 IC=+0.075 PNL=+13929.91€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 743 celda(s) pasan gate riguroso completo de 2765 evaluadas (n>=40) y 3843 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.035 < 0.08 — monitorear
  - _Datos_: n=5270 IC=+0.035 PNL=+418.14€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=1531/15 IC=+0.294 PNL=+665.08€ | BTC: n=1492/15 IC=+0.255 PNL=+175.33€ | SOL: n=966/15 IC=+0.380 PNL=+1002.36€

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
  - _Estado_: 84386 ops, 22 horas distintas. Sin hora con n≥15 y IC extremo aún.

**⏳ H-WINDOW-MOMENTUM** — Momentum de outcome entre ventanas 15min contiguas
  - _Umbral_: n≥60 alineadas y gap IC≥0.08 vs contrarias — y descartar que sea proxy de drift_15min/60min
  - _Acción_: Si confirma e independiente de drift → capturar prev_window_outcome como feature en shadow_predict y boost ×1.1-1.2 en señales alineadas
  - _Estado_: alineada_con_outcome_prev IC=+0.143 n=866/60 | contraria IC=+0.187 n=903 | gap=-0.044 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=507, boost estimado=+0.016. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 301 ops con delta_ratio

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=1820/40 IC=+0.005 PNL=+14.51€ | BTC#60min: n=2273/40 IC=+0.001 PNL=+62.74€ | SOL#60min: n=962/40 IC=+0.005 PNL=+9.03€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.047 n=613409 | tras_1loss IC=+0.097 n=465860 | tras_2loss IC=+0.066 n=187909/40 | gap=-0.019 (umbral 0.05)

**⏳ H-BTC-LEADS-ETH** — ETH/SOL GBM contrario al drift_15min de BTC del mismo ciclo
  - _Umbral_: n≥40 en contrario_BTC y gap≥0.08 — y descartar confound con drift propio antes de actuar
  - _Acción_: Si se confirma y no es confound → boost en ETH/SOL cuando decisión contraria a drift_15min BTC
  - _Estado_: alineado_BTC IC=+0.040 n=12303 | contrario_BTC IC=+0.054 n=10815/40 | gap=+0.015 (umbral 0.08) — SIN CONFIRMAR independencia de filtros propios de ETH


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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.191 > 0.08 con n=830 PNL=+606.34€
  - _Datos_: n=830 IC=+0.191 PNL=+606.34€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.162 > 0.08 con n=933 PNL=+510.88€
  - _Datos_: n=933 IC=+0.162 PNL=+510.88€

**🟡 H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: n≥25 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.162 > 0.08 con n=69 PNL=+34.91€
  - _Datos_: n=69 IC=+0.162 PNL=+34.91€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.332 > 0.1 con n=3257 PNL=+1805.67€
  - _Datos_: n=3257 IC=+0.332 PNL=+1805.67€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=801 IC=+0.069 PNL=+82.00€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=801 IC=+0.069 PNL=+82.00€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=93 IC=+0.195 PNL=+66.73€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=93 IC=+0.195 PNL=+66.73€

**〰️ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: n=80430 IC=+0.055 PNL=+7262.33€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=80430 IC=+0.055 PNL=+7262.33€

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
  - _Estado_: n=3399 IC=+0.007 PNL=+5.40€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=3399 IC=+0.007 PNL=+5.40€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=1656 IC=-0.003 PNL=+80.88€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=1656 IC=-0.003 PNL=+80.88€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=1047 IC=+0.024 PNL=+52.25€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=1047 IC=+0.024 PNL=+52.25€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.167 > 0.1 con n=5299 PNL=+3128.66€
  - _Datos_: n=5299 IC=+0.167 PNL=+3128.66€

**〰️ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: n=2920 IC=+0.067 PNL=+218.96€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=2920 IC=+0.067 PNL=+218.96€

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=2798 IC=+0.086 PNL=+654.09€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=2798 IC=+0.086 PNL=+654.09€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.098 > 0.08 con n=11932 PNL=+3265.49€
  - _Datos_: n=11932 IC=+0.098 PNL=+3265.49€

**〰️ H-CUSTOM-LONGSHOT-BIAS** — Longshot bias — ¿mejor IC cuando py_mkt < 0.20 o > 0.80?
  - _Hipótesis_: Jon-Becker repo documenta formalmente: contratos a 1-20 cents tienen win_rate < precio implícito (compradores pierden sistemáticamente en longshots). En nuestro sistema: cuando py_mkt<0.20 el GBM predice BUY_NO con edge estructural adicional al del modelo. ¿Se confirma en nuestros datos? Buscar en feature pct_spot_vs_ref si los mercados extremos tienen mejor IC en BUY_NO.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 en mercados extremos → boost ×1.2 en BUY_NO cuando py_mkt<0.20
  - _Estado_: n=461 IC=-0.228 PNL=-2.71€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=461 IC=-0.228 PNL=-2.71€

**〰️ H-CUSTOM-ETH15-REVERSION** — ETH#15min con drift_15min < -1 — ¿mean reversion?
  - _Hipótesis_: ETH y BTC tienen patrones opuestos: BTC funciona con momentum (drift>0.3). ETH funciona con reversión (drift<-1): 9/14 (64%) IC=+0.087. La hipótesis es que ETH tiene más mean-reversion que BTC en 15min.
  - _Umbral_: n≥20 y IC>+0.08
  - _Acción_: Si ETH drift<-1 confirma IC>0.08 con n≥20 → boost ×1.1 en ETH#15min cuando drift_15min<-1
  - _Estado_: n=485 IC=-0.019 PNL=-7.08€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=485 IC=-0.019 PNL=-7.08€

**〰️ H-CUSTOM-GBM-09H** — GBM a las 09h UTC — bloqueada 2026-06-29
  - _Hipótesis_: IC=-0.158 n=19 PNL=-11.62€. Bloqueada manualmente el 2026-06-29 añadiendo hora 9 a meta.gbm_blacklist_hours_auto. Esta hipótesis monitorea que el IC siga siendo negativo para justificar el bloqueo.
  - _Umbral_: n≥25 para confirmar el bloqueo es necesario
  - _Acción_: Si IC sube a >-0.05 con n≥30 → evaluar desbloquear. Si se mantiene <-0.10 → confirmar bloqueo permanente.
  - _Estado_: n=1078 IC=+0.039 PNL=+90.17€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=1078 IC=+0.039 PNL=+90.17€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=138 IC=-0.007 PNL=-1.31€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=138 IC=-0.007 PNL=-1.31€

**〰️ H-FUNDING-HIGH-BUYNO** — Funding rate alto (>p90 real ≈0.009%/8h) → BUY_NO tiene más edge
  - _Hipótesis_: Cuando funding perps Binance está en el decil superior real (>0.009%/8h, ver recalibración 06-Ago), los longs están sobrecargados y pagan por mantener. Hipótesis: BUY_NO GBM tiene IC superior en este régimen vs funding neutral. RECALIBRADO 06-Ago: el umbral original (0.03) era FÍSICAMENTE IMPOSIBLE -- el máximo real observado en 5428 filas de UPDOWN_GBM (feature funding_rate_8h = round(fr*100,5), fr=lastFundingRate crudo de Binance) es 0.01, y nunca lo cruzaba -- n=0 desde que se creó, atrapada sin poder acumular ni una fila. Recalibrado a p90 real (percentiles: p50=0.00368, p75=0.00651, p90=0.00943, p95=p99=p100=0.01 -- el feature satura en 0.01 en el 8.4% de las filas, sin evidencia de que sea un bug de captura, no de que sea funding genuinamente extremo). n=332 BUY_NO ya disponibles con el umbral nuevo (>>umbral_n=40), frente a n=0 con el original.
  - _Umbral_: n≥40 y IC>+0.05 diferencial vs baseline
  - _Acción_: Si IC_funding_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en BUY_NO cuando funding_rate_8h > 0.009
  - _Estado_: n=9376 IC=+0.026 PNL=+319.26€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=9376 IC=+0.026 PNL=+319.26€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.276 n=181) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=181 IC=+0.276 PNL=+178.48€

**〰️ H-DVOL-SPIKE-BUYNO** — DVOL spike (sigma_h alto) → BUY_NO tiene más edge (panic regime)
  - _Hipótesis_: Inspirado en 'The Volatility Edge' (Concretum Research, 2025): en equities, VIX spikes identifican regímenes de pánico donde los moves están sobreamplificados por feedback loops (deleveraging, hedgers, etc). En cripto el análogo es DVOL (Deribit BTC IV). Sin acceso a DVOL, usamos sigma_h como proxy (vol realizada 1h). Hipótesis: cuando sigma_h > 0.004/h (≈ vol diaria >9.6%), los mercados de predicción exageran la bajada en 15min → BUY_NO tiene IC superior porque el pánico se revierte intraday. Activar cuando n≥200 en BUY_NO #15min para tener potencia suficiente para subdividir por régimen.
  - _Umbral_: n≥200 BUY_NO #15min total, luego n≥40 en subconjunto sigma_h>0.004 y IC>+0.10
  - _Acción_: Si IC_sigma_alto > IC_baseline + 0.08 con n≥40 → boost ×1.2 en BUY_NO cuando sigma_h>0.004. Pendiente integrar DVOL real (Deribit API) cuando n≥500.
  - _Estado_: n=13654 IC=+0.054 PNL=+1191.53€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=13654 IC=+0.054 PNL=+1191.53€

**〰️ H-CUSTOM-POLY-DRIFT-CONFIRM** — poly_drift_5obs: ¿el precio YES interno de Polymarket confirma nuestra señal?
  - _Hipótesis_: Feature nueva 2026-06-27: drift del precio YES en Polymarket en últimas 5 obs (~5min). Si poly_drift<0 y decidimos BUY_NO (o poly_drift>0 y BUY_YES) → confluencia. Si diverge → reducción de stake. Hipótesis: confluencia Binance+Polymarket mejora IC; divergencia empeora.
  - _Umbral_: n≥40 en confluencia vs divergencia para validar el boost ×1.1
  - _Acción_: Si IC_confluencia>IC_divergencia con n≥40 → mantener el boost. Si no → retirar.
  - _Estado_: n=5102 IC=+0.062 PNL=+759.32€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=5102 IC=+0.062 PNL=+759.32€

**🟡 H-CUSTOM-OF-VOLUMEN-ALTO** — ORDER_FLOW_5M con total_vol_5m alto — ¿volumen extremo mejora el IC?
  - _Hipótesis_: Inspirado en un artículo sobre 'volume trading strategy' (mean-reversion en SPY): la idea es que un mismo movimiento de precio con volumen inusualmente alto refleja pánico/liquidación forzada y tiene más probabilidad de revertir que el mismo movimiento con volumen normal. No es transplantable tal cual (esa estrategia opera en barras diarias de SPY, nosotros en ventanas de 15-60min de cripto), pero el feature total_vol_5m ya se captura en cada predicción de ORDER_FLOW_5M (shadow_predict.py) y nunca se ha usado como filtro independiente — solo sirve de denominador para calcular delta_ratio. Hipótesis: dentro de las señales que ya pasan el filtro de delta_ratio, un total_vol_5m alto (volumen real, no solo desequilibrio) mejora el IC. Distribución real en predictions_*.csv (n=843): mediana=1696, p75=108522 (muy asimétrica) — se usa p75 como umbral de 'volumen alto'.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC_volumen_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en ORDER_FLOW_5M cuando total_vol_5m>100000
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.107 > 0.08 con n=612 PNL=+192.20€
  - _Datos_: n=612 IC=+0.107 PNL=+192.20€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-POS** — GBM 15min/60min: spread positivo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Inspirado en un artículo sobre bots de Polymarket: mercados de distinta duración del mismo activo (ej. BTC#15min vs BTC#60min) no repriciician a la misma velocidad — uno puede quedarse rezagado tras un movimiento. Si el spread entre ambos se sale de lo normal, puede indicar que uno de los dos aún no ha incorporado la información que el otro ya tiene. No es transplantable tal cual (el artículo lo usa para arbitraje comprando ambos lados a la vez, algo que no hacemos — ver idea_bidirectional_accumulation aparcada), pero el feature cross_window_spread (precio_yes propio menos precio_yes de la ventana relacionada, sin normalizar aún por z-score) ya se captura para GBM#15min (contra 60min) y GBM#60min (contra 15min) desde el 2026-07-01, sin cambiar ninguna decisión. Esta hipótesis cubre el lado positivo (mercado propio más caro que el relacionado); ver H-CUSTOM-CROSS-WINDOW-SPREAD-NEG para el lado negativo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread, y evaluar si merece la pena normalizar a z-score con más histórico
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.138 > 0.08 con n=1329 PNL=+363.32€
  - _Datos_: n=1329 IC=+0.138 PNL=+363.32€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-NEG** — GBM 15min/60min: spread negativo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Lado negativo de H-CUSTOM-CROSS-WINDOW-SPREAD-POS (mercado propio más barato que el relacionado). Mismo feature cross_window_spread, mismo origen (artículo sobre bots de Polymarket), umbral simétrico.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.096 > 0.08 con n=1070 PNL=+489.28€
  - _Datos_: n=1070 IC=+0.096 PNL=+489.28€

**〰️ H-CUSTOM-MOON-LLENA** — Fase lunar: ¿rendimiento peor cerca de luna llena?
  - _Hipótesis_: Inspirado en el paper de Fornero (2023, 43 Jornadas SADAF) sobre astrología financiera: 5 estudios peer-review (Dichev & Janes 2003, Yuan et al. 2006, Keef & Khaled 2011, Floros & Tan 2013, Liu & Tseng 2009) en 25-62 mercados bursátiles encuentran rendimientos 5-10%/año más bajos cerca de luna llena que de luna nueva. El propio paper es escéptico de la astrología como tal, pero el mecanismo que documenta no es místico: sesgo de humor de inversores minoristas (más fuerte en acciones con dominancia retail, casi nulo en institucional). Polymarket es un mercado muy retail/cripto — hipótesis: si el mecanismo transfiere, debería verse peor IC cerca de luna llena (moon_phase≈0.5) que en el resto del ciclo.
  - _Umbral_: n≥200 PERO ADEMÁS necesita cubrir al menos 3 ciclos lunares completos (~90 días de calendario) — no evaluar solo por n, aunque el volumen diario ya lo cruce en horas
  - _Acción_: Si IC cerca de luna llena < IC resto del ciclo con margen ≥0.05 y ≥3 ciclos lunares cubiertos → considerar boost/filtro por moon_phase. No implementar con menos de 3 ciclos aunque n sea alto — el efecto es de calendario lento, no de volumen.
  - _Estado_: n=86432 IC=+0.123 PNL=+34296.65€ — sin señal clara aún (umbral IC: min=None max=-0.03)
  - _Datos_: n=86432 IC=+0.123 PNL=+34296.65€

**〰️ H-CUSTOM-MERCURY-RETROGRADO** — Mercurio retrógrado: ¿rendimiento peor durante la ventana?
  - _Hipótesis_: Mismo origen que H-CUSTOM-MOON-LLENA (paper de Fornero, 43 Jornadas SADAF 2023). Qi, Wang & Zhang (2022, 48 mercados, 1973-2019): rendimientos 3.33%/año más bajos durante Mercurio retrógrado. Kou & Ma (2022) en China (99.8% cuentas retail): hasta -31% anualizado. Ambos estudios confirman que el mecanismo es la creencia/superstición de inversores retail (mayor efecto cuanto más retail y más supersticioso el mercado), no un efecto astral literal — Polymarket encaja en ese perfil. Ventanas 2026 (fuente pública, actualizar cada año): 26-feb a 20-mar, 29-jun a 23-jul, 24-oct a 13-nov.
  - _Umbral_: n≥100 PERO ADEMÁS necesita cubrir al menos 2-3 ventanas de retrogradación distintas (no solo la de jun-jul 2026) — esperar mínimo hasta después de la ventana de oct-nov 2026
  - _Acción_: Si IC en mercury_retrogrado=1 < IC en mercury_retrogrado=0 con margen ≥0.05 y ≥2 ventanas distintas cubiertas → considerar boost/filtro. No implementar tras una sola ventana (jun-jul 2026) por more que n sea alto — sería solo un evento, no un patrón.
  - _Estado_: n=19829 IC=+0.132 PNL=+8659.47€ — sin señal clara aún (umbral IC: min=None max=-0.03)
  - _Datos_: n=19829 IC=+0.132 PNL=+8659.47€

**〰️ H-CUSTOM-SMART-MONEY-CONSENSUS** — Consenso de wallets 'smart money' — ¿confirma nuestra dirección?
  - _Hipótesis_: Javi propuso estudiar bots/wallets que operan bien en nuestros mismos mercados. En vez de creer artículos (ya verificamos 2 veces esta semana que las narrativas no aguantan el cruce con datos reales), smart_money_tracker.py mide el track record REAL de wallets activas en BTC/ETH/SOL/XRP Up-or-Down 5/15/60min vía data-api.polymarket.com/positions, filtrado a posiciones 'Up or Down'. Clasifica como 'smart' las wallets con n>=10 posiciones, win_rate>=0.55 y pnl_total>0. smart_money_consensus es el sesgo direccional reciente (Up-Down)/(Up+Down) de esas wallets 'smart' por activo. Hipótesis: si nuestra decisión (BUY_YES/BUY_NO) coincide con el consenso smart money, mejor IC que cuando diverge. RESET METODOLOGICO 2026-07-02: la clasificacion 'smart' original via /positions estaba INVERTIDA para wallets de alta frecuencia (el endpoint solo retiene el residuo perdedor sin redimir; verificado: 'wowitsamazing' figuraba como -$478k y es +$10k/mes en el leaderboard oficial). Desde 2026-07-02T06:12Z el consenso se construye solo con wallets verificadas en el leaderboard oficial (pnl_mes>=$1000, 24 wallets). Los valores de smart_money_consensus capturados en features ANTES de esa fecha provienen de la clasificacion rota — descontar ese tramo al evaluar.
  - _Umbral_: n≥40 y IC>+0.08 — además necesita que existan wallets 'smart' acumuladas (0 al empezar, se van descubriendo cada ciclo)
  - _Acción_: Si IC en confluencia (decisión coincide con signo de smart_money_consensus) supera en >=0.05 al IC en divergencia, con n≥40 en cada lado → boost ×1.1-1.2 cuando coincide, considerar reducir stake cuando diverge fuerte.
  - _Estado_: n=12637 IC=+0.057 PNL=+1229.38€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=12637 IC=+0.057 PNL=+1229.38€

**🟡 H-CUSTOM-OF-EDGE-ALTO** — ORDER_FLOW_5M: edge alto (>0.20) rinde mejor que edge cerca del suelo
  - _Hipótesis_: Analizado 2026-07-01 sobre 794 resoluciones de ORDER_FLOW_5M: edge_neto en [0.025,0.198) -> IC=-0.009 (n=397, PNL=-10.49€) vs edge_neto en [0.198,0.385] -> IC=+0.029 (n=397, PNL=+16.43€). Comprobado que NO es un efecto general: en UPDOWN_GBM el patrón se invierte (edge bajo IC=-0.002 vs edge alto IC=-0.033), así que este filtro debe quedar scoped solo a ORDER_FLOW_5M, no aplicarse a otras estrategias. CORREGIDO 2026-07-01 (mismo día, encontrado por auditoría): el filtro original usaba 'edge_neto' con solo feature_lo, pero edge_neto está firmado por dirección (negativo en BUY_NO, positivo en BUY_YES) y ORDER_FLOW_5M solo genera BUY_NO desde 2026-06-25 — el filtro nunca podía matchear ningún BUY_NO real, solo el remanente BUY_YES histórico de antes del 25-jun (n=151, datos muertos, no crecen hacia adelante). Cambiado a 'edge_direccional' (siempre positivo, = abs(edge_neto)) + decision=BUY_NO explícito. Con el fix: n=227, IC=+0.0502, PNL=+19.15€ — señal real y viva.
  - _Umbral_: n≥80 en cada mitad (bajo/alto) para confirmar con más margen que el análisis inicial
  - _Acción_: Si se confirma con n≥80 y el gap se mantiene ≥0.03 → subir EDGE_MINIMO solo para ORDER_FLOW_5M a ~0.20 (o escalar Kelly con la magnitud del edge)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.123 > 0.02 con n=1071 PNL=+442.56€
  - _Datos_: n=1071 IC=+0.123 PNL=+442.56€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=226 IC=-0.097 PNL=+16.29€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=226 IC=-0.097 PNL=+16.29€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.450 > 0.1 con n=1824 PNL=+1778.75€
  - _Datos_: n=1824 IC=+0.450 PNL=+1778.75€

**〰️ H-CUSTOM-GBM-BUYYES-GLOBAL-MALO** — UPDOWN_GBM BUY_YES global — ¿estructuralmente peor que BUY_NO en todas las estrategias activas?
  - _Hipótesis_: Analizado 2026-07-01: patrón cross-estrategia consistente en las 4 estrategias activas — BUY_NO gana a BUY_YES sin excepción (UPDOWN_GBM IC=+0.058 n=154 vs -0.046 n=412; ORDER_FLOW_5M +0.053 n=439 vs -0.043 n=355; PRICE_TARGET_GBM +0.011 n=45 vs -0.267 n=28; WEEKLY_PRICE +0.115 n=50 vs -0.315 n=25). Mecanismo propuesto: sesgo retail comprando 'Up'/'YES' en cripto infla el precio de YES por encima de su valor justo en Polymarket — consistente con la sobreconfianza del modelo en probabilidades altas de YES detectada en la calibración Platt (ver idea_calibracion_platt). ORDER_FLOW_5M (solo genera BUY_NO desde 2026-06-25) y WEEKLY_PRICE (H-WEEKLY-BUYNO) ya actúan sobre este mismo patrón; UPDOWN_GBM y PRICE_TARGET_GBM (ver H-CUSTOM-PRICETARGET-BUYYES-MALO) todavía no tienen un tratamiento sistemático equivalente, solo filtros puntuales por hora/subtipo.
  - _Umbral_: n≥50 y IC<-0.05 para confirmar bloqueo global (a día de hoy ya está en n=412, IC=-0.046 — muy cerca)
  - _Acción_: Si se confirma con n≥50 → exigir evidencia direccional más fuerte por subtipo antes de permitir BUY_YES en live (barra asimétrica frente a BUY_NO), en vez de auto-desactivar de golpe todo BUY_YES de GBM
  - _Estado_: n=33643 IC=+0.073 PNL=+4759.55€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=33643 IC=+0.073 PNL=+4759.55€

**🟡 H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: n≥120 y IC>+0.10 (el n=61 del descubrimiento está incluido — exigir ~doble para confirmar forward)
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.202 > 0.1 con n=7387 PNL=+4277.19€
  - _Datos_: n=7387 IC=+0.202 PNL=+4277.19€

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.137 < -0.1 con n=587 PNL=+81.01€
  - _Datos_: n=587 IC=-0.137 PNL=+81.01€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=3212 IC=+0.070 PNL=+427.18€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=3212 IC=+0.070 PNL=+427.18€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=159 IC=-0.109 PNL=+0.85€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=159 IC=-0.109 PNL=+0.85€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.113 > 0.1 con n=892 PNL=+246.78€
  - _Datos_: n=892 IC=+0.113 PNL=+246.78€

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
  - _Estado_: n=36084 IC=-0.135 PNL=+2674.12€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=36084 IC=-0.135 PNL=+2674.12€

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
  - _Estado_: n=3682 IC=+0.130 PNL=+2319.97€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=3682 IC=+0.130 PNL=+2319.97€

**🟡 H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: n≥40 forward y IC>+0.08 (barra live estándar)
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.198 > 0.08 con n=4463 PNL=+3164.18€
  - _Datos_: n=4463 IC=+0.198 PNL=+3164.18€

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=8695 IC=+0.053 PNL=+702.54€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=8695 IC=+0.053 PNL=+702.54€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.097 > 0.08 con n=3862 PNL=+2137.08€
  - _Datos_: n=3862 IC=+0.097 PNL=+2137.08€

**🟡 H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: n≥80 (elevado desde el estándar 40, por ser recorte post-hoc) y IC>+0.08 en BTC específicamente
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.206 > 0.08 con n=899 PNL=+497.13€
  - _Datos_: n=899 IC=+0.206 PNL=+497.13€

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.222 < -0.1 con n=3788 PNL=-316.83€
  - _Datos_: n=3788 IC=-0.222 PNL=-316.83€

**🟡 H-CUSTOM-GBMLATE-ANCHURA-MERCADO** — GBM_LATE_15M BUY_YES — anchura de mercado (retorno concurrente de los otros 3 majors) como modificador secundario
  - _Hipótesis_: Detectado 2026-07-09 buscando explicar por qué varias pérdidas de la racha=4 comparten ventana de 15min. Con precios reales (05-09jul, ~20k muestras BTC) se calculó el retorno concurrente de los OTROS 3 majors desde el inicio de la ventana hasta el momento exacto de la decisión (sin fuga de datos, nunca el precio de cierre) y se cruzó con resultados reales de GBM_LATE_15M BUY_YES: n=802, magnitud media de los otros 3 en deciles limpios y monótonos (decil1 IC=-0.146 hit 35% → decil6-9 IC≈+0.20/+0.29 hit 70-80%). NO es redundante con drift_ventana_pct propio del par (correlación solo 0.26); controlando por el drift propio, la anchura sigue añadiendo información (dentro de drift propio>=0, que es el 90% de los casos: IC=0.127 si anchura baja vs IC=0.211 si anchura alta). Funciona en espejo para BUY_NO (shadow, n=685, anchura negativa 0/3→3/3: hit 47.4%→70.3%). CAVEAT importante: NO explica los clusters concretos de racha=4 en vivo — 6 de los 8 eventos históricos tienen anchura ALTA en al menos 2 de las 4 pérdidas (ver notas de sesión 09-Jul), y el backtest directo sobre trades.csv real (n=105-116) es inconcluso/contradictorio (gate anchura>=3 empeora el PnL real, -2.11€ vs +32.32€ sin filtro — probablemente confusión por mezcla de pares en una muestra pequeña, SOL domina ese bucket y SOL es el par MENOS sensible a esta señal: IC 0.132→0.143 apenas cambia, vs ETH 0.038→0.192). Tratar como MODIFICADOR del filtro primario H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT, no como filtro independiente — ver esa hipótesis para la tabla cruzada. Feature `mercado_anchura_pct` añadida 2026-07-09 en shadow_predict.py (_s_gbm_late), puro logging, no cambia ninguna decisión — empieza a acumular desde cero en predicciones nuevas. ACTUALIZACIÓN 12-Jul (desagregación por activo, n fresco): BTC n=35 ic=+0.392 z=+4.90, ETH n=32 ic=+0.353 z=+4.24, XRP n=31 ic=+0.288 z=+3.41 -- los 3 MUY fuertes y consistentes. SOL sigue siendo el único débil (n=30 ic=+0.094 z=+1.10), confirma el caveat ya escrito arriba (SOL insensible). Con XRP incluido, el patrón deja de ser '3 activos + SOL raro' para ser una regla casi universal salvo SOL -- candidato fuerte para boost Kelly restringido a BTC/ETH/XRP (excluir SOL explícitamente) en vez de aplicar a las 4 monedas por igual.
  - _Umbral_: n≥100 forward (feature nueva, sin histórico) e IC>+0.20 en la zona alta (mercado_anchura_pct≥0.056, el decil superior observado)
  - _Acción_: Si confirma con n≥100 IC≥0.20 → boost Kelly cuando mercado_anchura_pct≥0.056 Y prob_yes_modelo≥0.53 (la celda 'doble buena', hit 72.7% retrospectivo). No usar como filtro solo — ver CAVEAT de los clusters de racha en la descripción, y el análisis por-par (SOL insensible) antes de aplicar a las 4 monedas por igual.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.216 > 0.2 con n=9723 PNL=+7892.07€
  - _Datos_: n=9723 IC=+0.216 PNL=+7892.07€

**🟡 H-CUSTOM-OF5M-SMARTMONEY-CONTRARIO** — ORDER_FLOW_5M SOL BUY_NO — smart money EN CONTRA del flujo CEX, no a favor, predice mejor
  - _Hipótesis_: Detectado 11-Jul revisando el backlog quant-desk (reencuadre de ORDER_FLOW_5M). ORDER_FLOW_5M solo dispara BUY_NO (presión vendedora en Binance). Split retrospectivo SOL#5min por smart_money_consensus (ya logueado, nunca cruzado con esta estrategia): cuando el consenso on-chain es BAJISTA (smart_money_consensus<0, 'confirma' la señal CEX) el hit cae a 47.1% (ic_bayes=-0.026, n=17); cuando el consenso es ALCISTA/neutro (smart_money_consensus>=0, CONTRARIO a la señal CEX) el hit sube a 65.0% (ic_bayes=+0.136, n=20, pnl/trade+0.294). Contraintuitivo: la 'confirmación' de dos fuentes empeora, la divergencia mejora. Hipótesis mecánica: el flujo de Binance ya captura la información rápida de 5min; smart money on-chain se mueve más lento (posiciones ya tomadas), así que cuando coincide con el flujo CEX puede ser la MISMA información ya vista dos veces sin dar nada nuevo (o incluso momentum ya agotado), mientras que la divergencia indica que el flujo CEX es el que se está moviendo AHORA sobre información fresca que smart money aún no reflejó. Distinto del cierre 08-Jul del consenso poblacional plano (n=2494, ruido puro) — aquello era agregado sobre TODAS las estrategias; esto es específico del mecanismo de ORDER_FLOW_5M. n=17/20 insuficiente para concluir (regla del proyecto n≥15 es el mínimo absoluto, no un veredicto) — vigilar forward.
  - _Umbral_: n≥40 en cada rama (contrario y alineado) para separar señal de ruido
  - _Acción_: Si confirma con n≥40 e ic_bayes contrario≥+0.08 (con alineado claramente peor) → boost Kelly en ORDER_FLOW_5M BUY_NO cuando smart_money_consensus>=0; considerar filtro/veto cuando smart_money_consensus<0 y muy negativo (posible señal 'ya vista', sin ventaja).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.113 > 0.08 con n=135 PNL=+55.30€
  - _Datos_: n=135 IC=+0.113 PNL=+55.30€

**🟡 H-CUSTOM-ETH15-SIGMA-ACCEL** — GBM_LATE_15M ETH — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: sigma_ewma_delta_pct = (sigma_h_ewma10-sigma_h)/sigma_h. Verificado ad-hoc n=47: cuando la vol reciente (EWMA half-life 10min) supera la ventana plana, hit sube de 59.5% (agregado ETH) a 66.0%, ic_bayes=+0.153. Efecto NO uniforme entre activos (ver hermanas BTC/XRP) -- desagregar por activo es obligatorio, el agregado GBM_LATE_15M diluye esto a ruido.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en ETH#15min
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.084 > 0.08 con n=3516 PNL=+1265.40€
  - _Datos_: n=3516 IC=+0.084 PNL=+1265.40€

**🟡 H-CUSTOM-BTC15-SIGMA-ACCEL** — GBM_LATE_15M BTC — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: mismo mecanismo que ETH (ver H-CUSTOM-ETH15-SIGMA-ACCEL). Verificado ad-hoc n=35: hit sube de 63.6% (agregado BTC) a 68.6%, ic_bayes=+0.176.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en BTC#15min
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.175 > 0.08 con n=3338 PNL=+2572.30€
  - _Datos_: n=3338 IC=+0.175 PNL=+2572.30€

**〰️ H-CUSTOM-XRP15-SIGMA-DECEL** — GBM_LATE_15M XRP — vol DESacelerando (EWMA10<=flat) mejora la señal (signo opuesto a ETH/BTC)
  - _Hipótesis_: 12-Jul: XRP muestra el signo CONTRARIO a ETH/BTC -- cuando la vol reciente cae por debajo de la ventana plana, hit sube de 63.9% (agregado XRP) a 68.8%, ic_bayes=+0.180 (n=48). Cuando acelera, hit CAE a 57.1%. Confirma que este feature no puede tratarse con un umbral global -- cada activo necesita su propio signo. REFUTADA 13-Jul: recalculado con n=61 (más del doble del n original) usando el mismo método riguroso (percentiles + permutación 20k) que confirmó BTC/SOL/ETH -- el signo se INVIRTIÓ: decel (sigma<0) da IC=-0.065 n=21 (malo), accel (sigma>=0) da IC=+0.071 n=40 (bueno). XRP en realidad tiene el MISMO signo que BTC/ETH (sigma alto=bueno), solo que más débil -- coherente con el patrón ganador ya auto-descubierto por postmortem (sigma_ewma_delta_pct>5.563, ic_patron=+0.20 n=18, mismo signo). El hallazgo ad-hoc del 12-Jul con n=48 no replicó con más datos -- probable ruido de una muestra menor/distinta. Ver idea_estrategia_mercado_bajista... no, ver project_sigma_filtro_sol_xrp_no_promociona_13jul (memoria) para el detalle completo.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: REFUTADA -- no implementar kelly_boost por sigma<0 en XRP. El signo correcto es el opuesto (sigma alto=bueno), ya cubierto por el patron_ganador automático de postmortem sobre GBM_LATE_15M#XRP#15min -- no hace falta ninguna acción manual adicional.
  - _Estado_: n=5558 IC=-0.023 PNL=+1571.41€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=5558 IC=-0.023 PNL=+1571.41€

**〰️ H-CUSTOM-SMARTMONEY-FAVORITO-SOL** — FAVORITO_CONFIRMADO SOL — alineado con smart_money_consensus bate ir en contra (REABRE hallazgo cerrado 08-Jul)
  - _Hipótesis_: 12-Jul: el cierre 08-Jul (n=2494, sin desagregar por estrategia/activo) encontro ruido puro. Desagregando por estrategia+activo (mecanismo nuevo): FAVORITO_CONFIRMADO#SOL alineado con smart_money_consensus (|consenso|>0.1, n_wallets>=3) hit=78.4% (n=37) vs contrario hit=52.4% (n=42), z=+2.41. GBM_LATE_15M tambien muestra el mismo signo en BTC/ETH/XRP (z=0.86-1.61, mas debil) pero SOL plano ahi -- inconsistencia entre estrategias que hay que entender antes de actuar.
  - _Umbral_: n>=40 por lado y z>=2
  - _Acción_: Si confirma con n>=40 y z>=2 -> considerar boost condicionado a alineacion con smart_money_consensus en FAVORITO_CONFIRMADO#SOL
  - _Estado_: n=724 IC=+0.070 PNL=-44.22€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=724 IC=+0.070 PNL=-44.22€

**🟡 H-CUSTOM-FAVORITO-SOL-ALTACONVICCION** — FAVORITO_CONFIRMADO SOL BUY_YES alta conviccion (py_entrada alto) — UNICO caso positivo en fill-ability de hoy
  - _Hipótesis_: 12-Jul: auditoria de fill-ability de las 8 candidatas encontro las 8 negativas en agregado. Pero desagregando FAVORITO_CONFIRMADO por activo (mecanismo nuevo, no mirado hasta hoy): SOL#BUY_YES con py_entrada>=0.665-0.695 da pnl/trade POSITIVO en el subconjunto fillable real (+0.12 a +0.41 EUR/trade, n=6-17 segun el corte exacto) -- unico resultado positivo de toda la auditoria de candidatas. n todavia bajo, necesita mas dato antes de proponer nada.
  - _Umbral_: n>=40 y pnl/trade fillable > 0 sostenido
  - _Acción_: Seguir acumulando snapshots candidato_evaluacion para SOL#15min#BUY_YES en FAVORITO_CONFIRMADO; re-evaluar fill-ability con n>=40 antes de proponer whitelist
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.245 > 0.08 con n=5151 PNL=-391.74€
  - _Datos_: n=5151 IC=+0.245 PNL=-391.74€

**〰️ H-CUSTOM-GBM18H-XRP-EXCEPCION** — UPDOWN_GBM XRP a las 18h UTC -- puede estar mal incluida en el blacklist horario global
  - _Hipótesis_: 12-Jul: gbm_blacklist_hours_auto=[9,10,18] bloquea GBM en las 4 monedas a las 18h. Desagregando por activo (h9/h10 no tienen dato retrospectivo -- el propio blacklist impide que se genere): BTC ic=-0.140 (n=48), ETH ic=-0.136 (n=42), SOL ic=-0.167 (n=22) consistentes con el bloqueo, pero XRP ic=+0.100 (n=23) -- signo OPUESTO. El bloqueo agregado puede estar sobre-bloqueando XRP especificamente.
  - _Umbral_: n>=40 y IC>0.08
  - _Acción_: Si confirma con n>=40 IC>0.08 -> considerar excepcion de XRP en gbm_blacklist_hours_auto para la hora 18 (shadow puro, UPDOWN_GBM no esta live)
  - _Estado_: n=76 IC=+0.026 PNL=+11.18€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=76 IC=+0.026 PNL=+11.18€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.102 n=1913) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=1913 IC=+0.102 PNL=+412.97€

**🟡 H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: n>=40 y IC>=0.08
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.304 > 0.08 con n=528 PNL=+141.06€
  - _Datos_: n=528 IC=+0.304 PNL=+141.06€

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.408 n=619) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=619 IC=+0.408 PNL=+885.10€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=15539 IC=+0.185 PNL=-1615.69€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=15539 IC=+0.185 PNL=-1615.69€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.230 > 0.1 con n=246 PNL=+170.67€
  - _Datos_: n=246 IC=+0.230 PNL=+170.67€
