# Hipótesis automáticas — 2026-10-27 16:17 UTC
_Generado por shadow_postmortem.py sobre 1079574 resoluciones (PNL=+142421.94€)_

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
- **FILTRO** `restante_s_al_confirmar` < `138.58` → IC=-0.210 (n=10720)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 138.58
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=32161)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `127.45` → IC=-0.261 (n=1151)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 127.45
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=3453)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `119.89` → IC=-0.294 (n=1138)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 119.89
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=3415)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `160.59` → IC=-0.241 (n=2865)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 160.59
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=8598)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `132.83` → IC=-0.259 (n=2071)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 132.83
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=6214)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.213 (n=23530)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.106)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.126 (n=4579)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.01 (IC base=+0.106)

- **PATRÓN** `libro_liquidez` > `8804.9286` → IC=+0.166 (n=2101)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 8804.9286 (IC base=+0.106)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.127 (n=20123)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.131 (n=24648)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 7.0 (IC base=+0.125)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.226 (n=18810)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.146 (n=7583)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.01 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `6836.9618` → IC=+0.155 (n=2935)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 6836.9618 (IC base=+0.125)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.191 (n=2103)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 5.0 (IC base=+0.184)

- **PATRÓN** `py_entrada` > `0.765` → IC=+0.364 (n=696)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.765 (IC base=+0.184)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.187 (n=2574)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.01 (IC base=+0.184)

- **PATRÓN** `libro_liquidez` > `16451.0129` → IC=+0.185 (n=668)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 16451.0129 (IC base=+0.184)

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

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.140 (n=1208)

  - _Acción_: Kelly boost +0.70€ cuando `py_entrada` < 0.44 (IC base=+0.082)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.167 (n=4571)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.162)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.164 (n=3881)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 15.0 (IC base=+0.162)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.377 (n=1475)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.162)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.216 (n=2047)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.207)

- **PATRÓN** `py_entrada` < `0.265` → IC=+0.351 (n=768)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.265 (IC base=+0.207)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.212 (n=2381)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.207)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.147 (n=1155)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 5.0 (IC base=+0.145)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.149 (n=987)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 15.0 (IC base=+0.145)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.263 (n=373)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.145)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.151 (n=912)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.01 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `2214.1072` → IC=+0.156 (n=501)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 2214.1072 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.162 (n=152)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.069)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.254 (n=880)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.226)

- **PATRÓN** `py_entrada` > `0.83` → IC=+0.421 (n=1229)

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

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.204 (n=20151)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.201 (n=17136)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.233 (n=8289)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `4837.3339` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4837.3339 (IC base=+0.199)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.182 (n=2180)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 15.0 (IC base=+0.178)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.180 (n=4608)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 18.0 (IC base=+0.178)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.182 (n=4495)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` < 0.73 (IC base=+0.178)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.179 (n=3810)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` > 0.71 (IC base=+0.178)

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

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.221 (n=2500)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.219)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.224 (n=1680)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.219)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.298 (n=840)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.219)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.186 (n=4542)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.181 (n=3874)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 15.0 (IC base=+0.179)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.188 (n=3543)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` > 0.71 (IC base=+0.179)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.255 (n=3903)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.247)

- **PATRÓN** `py_entrada` > `0.79` → IC=+0.359 (n=1300)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.190 (n=4458)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.187)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.191 (n=3814)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 15.0 (IC base=+0.187)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.192 (n=3302)

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

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.209 (n=26094)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.202)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.247 (n=26399)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.202)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.191 (n=4493)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 17.0 (IC base=+0.185)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.185 (n=8390)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 12.0 (IC base=+0.185)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.198 (n=11826)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` > 0.71 (IC base=+0.185)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.228 (n=5446)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.226 (n=5369)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.225)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.287 (n=3787)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.225)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.188 (n=4478)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 17.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.201 (n=9221)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.181)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.835` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.835
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.230 (n=5485)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.219)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.219 (n=4210)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.219)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.274 (n=3712)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.219)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.207 (n=10031)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.262 (n=3870)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.208 (n=4340)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.199 (n=4373)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.249 (n=4572)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.198)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.193 (n=9445)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.141 (n=9524)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `3.66` → IC=+0.137 (n=11458)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 3.66 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.197 (n=4657)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.119)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.146 (n=4336)

  - _Acción_: Kelly boost +0.73€ cuando `restante_min` > 4.96 (IC base=+0.119)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.128 (n=5745)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 7.0 (IC base=+0.119)

- **PATRÓN** `lag_apertura_s` < `2.67` → IC=+0.146 (n=4313)

  - _Acción_: Kelly boost +0.73€ cuando `lag_apertura_s` < 2.67 (IC base=+0.119)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.190 (n=4788)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.38 (IC base=+0.114)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.136 (n=5188)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.96 (IC base=+0.114)

- **PATRÓN** `lag_apertura_s` < `3.27` → IC=+0.136 (n=5754)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 3.27 (IC base=+0.114)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.304 (n=1782)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.294)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.386 (n=613)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.294)

- **PATRÓN** `libro_liquidez` > `3824.2708` → IC=+0.295 (n=761)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3824.2708 (IC base=+0.294)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.289 (n=810)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.281)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.362 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.281)

- **PATRÓN** `libro_liquidez` > `5084.4032` → IC=+0.298 (n=349)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5084.4032 (IC base=+0.281)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.328 (n=579)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.300)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.302 (n=846)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.300)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.396 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.300)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.301 (n=959)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.300)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4718` → IC=+0.140 (n=14723)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.4718 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.126 (n=14876)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 6.0 (IC base=+0.122)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.126 (n=10293)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 12.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` > `0.3774` → IC=+0.166 (n=14724)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.3774 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` > `0.7747` → IC=+0.274 (n=813)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7747 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` < `0.3651` → IC=+0.260 (n=4216)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3651 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.632` → IC=+0.181 (n=7340)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 3.632 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` > `0.6211` → IC=+0.266 (n=4312)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6211 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` > `0.3043` → IC=+0.246 (n=1516)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3043 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` > `2.3561` → IC=+0.231 (n=4771)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3561 (IC base=+0.122)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.130 (n=7594)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.01 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `4515.7478` → IC=+0.151 (n=4908)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 4515.7478 (IC base=+0.122)

- **PATRÓN** `ibs_20min` < `0.5673` → IC=+0.142 (n=18253)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` < 0.5673 (IC base=+0.077)

- **PATRÓN** `dist_vwap_pct` > `0.5988` → IC=+0.188 (n=1181)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.5988 (IC base=+0.077)

- **PATRÓN** `volumen_regimen` < `0.6982` → IC=+0.190 (n=3195)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` < 0.6982 (IC base=+0.077)

- **PATRÓN** `volumen_pendiente_norm` > `0.2978` → IC=+0.229 (n=1800)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2978 (IC base=+0.077)

- **PATRÓN** `volumen_spike_ratio` > `2.6939` → IC=+0.207 (n=4108)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6939 (IC base=+0.077)

- **PATRÓN** `ballena_activa_n` < `105.0` → IC=+0.223 (n=12198)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 105.0 (IC base=+0.077)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.206 (n=1063)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.205)

- **PATRÓN** `drift_60min` |x|≤ `0.3528` → IC=+0.207 (n=3188)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3528 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.217 (n=1187)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.205)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.210 (n=2141)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.205)

- **PATRÓN** `ibs_20min` > `0.9834` → IC=+0.281 (n=1445)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9834 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.709` → IC=+0.283 (n=1411)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.709 (IC base=+0.205)

- **PATRÓN** `volumen_pendiente_norm` > `0.2844` → IC=+0.261 (n=416)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2844 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` > `1.5504` → IC=+0.209 (n=2723)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5504 (IC base=+0.205)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.220 (n=3460)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.205)

- **PATRÓN** `libro_liquidez` > `2050.72` → IC=+0.208 (n=1063)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2050.72 (IC base=+0.205)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.224 (n=1971)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.205)

- **PATRÓN** `sigma_h` < `0.0091` → IC=+0.242 (n=2711)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0091 (IC base=+0.240)

- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.243 (n=1230)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0082 (IC base=+0.240)

- **PATRÓN** `drift_60min` |x|≤ `0.0873` → IC=+0.276 (n=904)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0873 (IC base=+0.240)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.245 (n=2496)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.240)

- **PATRÓN** `ibs_20min` < `0.5448` → IC=+0.259 (n=2710)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5448 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` < `0.0961` → IC=+0.244 (n=2440)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0961 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` > `0.2943` → IC=+0.258 (n=374)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2943 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` < `1.4468` → IC=+0.242 (n=857)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4468 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` > `1.8781` → IC=+0.243 (n=1712)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8781 (IC base=+0.240)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.242 (n=3081)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.240)

- **PATRÓN** `libro_liquidez` > `1545.1028` → IC=+0.242 (n=2421)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1545.1028 (IC base=+0.240)

- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.239 (n=1146)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 8.0 (IC base=+0.240)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.240 (n=878)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.229)

- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.230 (n=1196)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0051 (IC base=+0.229)

- **PATRÓN** `drift_60min` |x|≤ `0.1062` → IC=+0.258 (n=1157)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1062 (IC base=+0.229)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.240 (n=2751)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.229)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.229 (n=1877)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.229)

- **PATRÓN** `ibs_20min` > `0.9322` → IC=+0.273 (n=878)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9322 (IC base=+0.229)

- **PATRÓN** `dist_vwap_pct` > `0.1871` → IC=+0.237 (n=1240)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1871 (IC base=+0.229)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.219` → IC=+0.266 (n=391)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.219 (IC base=+0.229)

- **PATRÓN** `volumen_regimen` < `1.231` → IC=+0.229 (n=2630)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.231 (IC base=+0.229)

- **PATRÓN** `volumen_regimen` > `0.623` → IC=+0.233 (n=2630)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.623 (IC base=+0.229)

- **PATRÓN** `volumen_pendiente_norm` > `0.2801` → IC=+0.277 (n=374)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2801 (IC base=+0.229)

- **PATRÓN** `volumen_spike_ratio` > `2.4324` → IC=+0.261 (n=864)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4324 (IC base=+0.229)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.151 (n=2762)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0059 (IC base=+0.130)

- **PATRÓN** `drift_60min` |x|≤ `0.077` → IC=+0.165 (n=921)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.077 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.156 (n=1031)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 17.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` < `0.7219` → IC=+0.170 (n=2762)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.7219 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.919` → IC=+0.145 (n=452)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 10.919 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.076` → IC=+0.136 (n=2520)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 4.076 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` < `1.2086` → IC=+0.140 (n=2762)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 1.2086 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` > `0.0966` → IC=+0.154 (n=1010)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` > 0.0966 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` < `2.4565` → IC=+0.140 (n=2639)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 2.4565 (IC base=+0.130)

- **PATRÓN** `ballena_activa_n` < `209.0` → IC=+0.173 (n=1131)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 209.0 (IC base=+0.130)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0123` → IC=+0.216 (n=1113)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0123 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.200 (n=3502)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.193)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.264 (n=1284)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.173` → IC=+0.278 (n=714)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.173 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` < `0.0968` → IC=+0.198 (n=2967)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` < 0.0968 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` > `0.353` → IC=+0.222 (n=433)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.353 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` > `2.7105` → IC=+0.211 (n=1471)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7105 (IC base=+0.193)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.199 (n=3982)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.04 (IC base=+0.193)

- **PATRÓN** `libro_liquidez` > `2032.4984` → IC=+0.202 (n=1112)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2032.4984 (IC base=+0.193)

- **PATRÓN** `sigma_h` < `0.0108` → IC=+0.223 (n=2663)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0108 (IC base=+0.217)

- **PATRÓN** `drift_60min` |x|≤ `0.1763` → IC=+0.233 (n=1329)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1763 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.241 (n=1133)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.217)

- **PATRÓN** `ibs_20min` < `0.03` → IC=+0.271 (n=1007)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.03 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.198` → IC=+0.257 (n=356)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.198 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` > `0.3493` → IC=+0.264 (n=435)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3493 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` > `2.7628` → IC=+0.224 (n=1307)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7628 (IC base=+0.217)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.223 (n=1517)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.217)

- **PATRÓN** `libro_liquidez` > `1920.181` → IC=+0.218 (n=1370)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1920.181 (IC base=+0.217)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.217 (n=2491)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 21.0 (IC base=+0.217)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.142 (n=163)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=4028)

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

- **PATRÓN** `ibs_20min` < `0.092` → IC=+0.183 (n=1048)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.092 (IC base=+0.040)

- **PATRÓN** `dist_vwap_pct` > `0.3328` → IC=+0.147 (n=486)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.3328 (IC base=+0.040)

- **PATRÓN** `volumen_regimen` < `0.8412` → IC=+0.153 (n=1280)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.8412 (IC base=+0.040)

- **PATRÓN** `volumen_pendiente_norm` > `0.2863` → IC=+0.209 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2863 (IC base=+0.040)

- **PATRÓN** `volumen_spike_ratio` < `1.7843` → IC=+0.140 (n=1230)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.7843 (IC base=+0.040)

- **PATRÓN** `volumen_spike_ratio` > `2.1656` → IC=+0.160 (n=837)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 2.1656 (IC base=+0.040)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.181 (n=114)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=616)

- **FILTRO** `ibs_20min` > `0.2121` → IC=-0.133 (n=3940)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2121
  - _Potencial_: sin este filtro IC_bueno=+0.149 (n=1946)

- **FILTRO** `sigma_ewma_delta_pct` > `8.576` → IC=-0.231 (n=627)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.576
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=5259)

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

- **PATRÓN** `volumen_pendiente_norm` < `0.0757` → IC=+0.290 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0757 (IC base=+0.026)

- **PATRÓN** `volumen_spike_ratio` < `2.4948` → IC=+0.296 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4948 (IC base=+0.026)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.276 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 37.0 (IC base=+0.026)

- **PATRÓN** `ibs_20min` < `0.2121` → IC=+0.149 (n=1946)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.2121 (IC base=-0.039)

- **PATRÓN** `dist_vwap_pct` > `0.2735` → IC=+0.279 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2735 (IC base=-0.039)

- **PATRÓN** `volumen_regimen` < `0.6936` → IC=+0.302 (n=362)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6936 (IC base=-0.039)

- **PATRÓN** `volumen_pendiente_norm` < `0.1046` → IC=+0.288 (n=677)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1046 (IC base=-0.039)

- **PATRÓN** `volumen_pendiente_norm` > `0.0793` → IC=+0.289 (n=363)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0793 (IC base=-0.039)

- **PATRÓN** `volumen_spike_ratio` < `2.4353` → IC=+0.305 (n=757)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4353 (IC base=-0.039)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6001` → IC=-0.184 (n=1095)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6001
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=3293)

- **FILTRO** `ibs_20min` < `0.7624` → IC=-0.152 (n=2896)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7624
  - _Potencial_: sin este filtro IC_bueno=+0.106 (n=1492)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.167 (n=1040)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=3348)

- **FILTRO** `ibs_20min` > `0.749` → IC=-0.202 (n=1564)

  - _Acción_: SKIP cuando `ibs_20min` > 0.749
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=4693)

- **PATRÓN** `dist_vwap_pct` > `1.0122` → IC=+0.349 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0122 (IC base=-0.065)

- **PATRÓN** `dist_vwap_pct` < `0.1794` → IC=+0.310 (n=650)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1794 (IC base=-0.065)

- **PATRÓN** `volumen_regimen` > `0.7043` → IC=+0.319 (n=704)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7043 (IC base=-0.065)

- **PATRÓN** `volumen_pendiente_norm` < `0.1017` → IC=+0.305 (n=742)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1017 (IC base=-0.065)

- **PATRÓN** `volumen_pendiente_norm` > `0.0739` → IC=+0.302 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0739 (IC base=-0.065)

- **PATRÓN** `volumen_spike_ratio` < `1.42` → IC=+0.321 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.42 (IC base=-0.065)

- **PATRÓN** `volumen_spike_ratio` > `1.8422` → IC=+0.310 (n=509)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8422 (IC base=-0.065)

- **PATRÓN** `dist_vwap_pct` > `0.8002` → IC=+0.288 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8002 (IC base=-0.003)

- **PATRÓN** `volumen_regimen` < `0.6468` → IC=+0.267 (n=587)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6468 (IC base=-0.003)

- **PATRÓN** `volumen_regimen` > `1.0687` → IC=+0.283 (n=797)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0687 (IC base=-0.003)

- **PATRÓN** `volumen_pendiente_norm` > `0.1687` → IC=+0.289 (n=448)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1687 (IC base=-0.003)

- **PATRÓN** `volumen_spike_ratio` < `2.1776` → IC=+0.263 (n=1439)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1776 (IC base=-0.003)

- **PATRÓN** `volumen_spike_ratio` > `1.4313` → IC=+0.264 (n=1635)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4313 (IC base=-0.003)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.01` → IC=+0.211 (n=6422)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.01 (IC base=+0.094)

- **PATRÓN** `ibs_20min` > `0.3114` → IC=+0.167 (n=19253)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.3114 (IC base=+0.094)

- **PATRÓN** `dist_vwap_pct` > `0.9321` → IC=+0.302 (n=1381)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9321 (IC base=+0.094)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.575` → IC=+0.165 (n=8620)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 3.575 (IC base=+0.094)

- **PATRÓN** `volumen_regimen` < `1.1732` → IC=+0.266 (n=7097)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1732 (IC base=+0.094)

- **PATRÓN** `volumen_regimen` > `0.6911` → IC=+0.274 (n=6341)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6911 (IC base=+0.094)

- **PATRÓN** `volumen_pendiente_norm` > `0.2946` → IC=+0.285 (n=1600)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2946 (IC base=+0.094)

- **PATRÓN** `volumen_spike_ratio` > `2.6541` → IC=+0.277 (n=3760)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6541 (IC base=+0.094)

- **PATRÓN** `ballena_activa_n` < `91.0` → IC=+0.301 (n=10873)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 91.0 (IC base=+0.094)

- **PATRÓN** `sigma_h` > `0.0096` → IC=+0.154 (n=6203)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` > 0.0096 (IC base=+0.076)

- **PATRÓN** `ibs_20min` < `0.6505` → IC=+0.146 (n=18580)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.6505 (IC base=+0.076)

- **PATRÓN** `volumen_regimen` < `0.7051` → IC=+0.267 (n=2629)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7051 (IC base=+0.076)

- **PATRÓN** `volumen_regimen` > `1.1967` → IC=+0.265 (n=1990)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1967 (IC base=+0.076)

- **PATRÓN** `volumen_pendiente_norm` > `0.2955` → IC=+0.320 (n=1290)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2955 (IC base=+0.076)

- **PATRÓN** `volumen_spike_ratio` < `1.5824` → IC=+0.294 (n=3805)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5824 (IC base=+0.076)

- **PATRÓN** `volumen_spike_ratio` > `2.2859` → IC=+0.286 (n=3920)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2859 (IC base=+0.076)

- **PATRÓN** `ballena_activa_n` < `75.0` → IC=+0.297 (n=8576)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 75.0 (IC base=+0.076)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.5794` → IC=-0.149 (n=2619)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5794
  - _Potencial_: sin este filtro IC_bueno=+0.201 (n=2620)

- **FILTRO** `ibs_20min` > `0.7296` → IC=-0.219 (n=1124)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7296
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=3378)

- **FILTRO** `sigma_ewma_delta_pct` > `4.322` → IC=-0.220 (n=977)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.322
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=3525)

- **PATRÓN** `ibs_20min` > `0.9256` → IC=+0.329 (n=1310)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9256 (IC base=+0.026)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.888` → IC=+0.220 (n=933)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.888 (IC base=+0.026)

- **PATRÓN** `volumen_pendiente_norm` > `0.2297` → IC=+0.315 (n=343)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2297 (IC base=+0.026)

- **PATRÓN** `volumen_spike_ratio` < `1.4472` → IC=+0.262 (n=570)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4472 (IC base=+0.026)

- **PATRÓN** `volumen_spike_ratio` > `2.2629` → IC=+0.289 (n=775)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2629 (IC base=+0.026)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.304 (n=1141)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.026)

- **PATRÓN** `ibs_20min` < `0.1687` → IC=+0.161 (n=1127)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.1687 (IC base=-0.028)

- **PATRÓN** `volumen_pendiente_norm` < `0.0739` → IC=+0.415 (n=599)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0739 (IC base=-0.028)

- **PATRÓN** `volumen_spike_ratio` < `2.7127` → IC=+0.409 (n=679)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.7127 (IC base=-0.028)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.405 (n=626)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 19.0 (IC base=-0.028)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.1662` → IC=+0.217 (n=846)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1662 (IC base=+0.020)

- **PATRÓN** `volumen_regimen` < `1.1965` → IC=+0.202 (n=1891)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1965 (IC base=+0.020)

- **PATRÓN** `volumen_regimen` > `0.6924` → IC=+0.206 (n=1689)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6924 (IC base=+0.020)

- **PATRÓN** `volumen_pendiente_norm` > `0.2788` → IC=+0.246 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2788 (IC base=+0.020)

- **PATRÓN** `volumen_spike_ratio` < `1.4262` → IC=+0.226 (n=622)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4262 (IC base=+0.020)

- **PATRÓN** `volumen_spike_ratio` > `2.473` → IC=+0.202 (n=622)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.473 (IC base=+0.020)

- **PATRÓN** `ballena_activa_n` < `268.0` → IC=+0.237 (n=1239)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 268.0 (IC base=+0.020)

- **PATRÓN** `volumen_regimen` < `1.1732` → IC=+0.235 (n=1264)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1732 (IC base=-0.003)

- **PATRÓN** `volumen_regimen` > `0.6206` → IC=+0.239 (n=1263)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6206 (IC base=-0.003)

- **PATRÓN** `volumen_pendiente_norm` > `0.273` → IC=+0.301 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.273 (IC base=-0.003)

- **PATRÓN** `volumen_spike_ratio` < `1.5398` → IC=+0.249 (n=533)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5398 (IC base=-0.003)

- **PATRÓN** `volumen_spike_ratio` > `2.1623` → IC=+0.250 (n=550)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1623 (IC base=-0.003)

- **PATRÓN** `ballena_activa_n` < `216.0` → IC=+0.243 (n=535)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 216.0 (IC base=-0.003)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0122` → IC=+0.323 (n=924)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0122 (IC base=+0.273)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.281 (n=2767)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.273)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.315 (n=1484)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.273)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.706` → IC=+0.305 (n=908)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.706 (IC base=+0.273)

- **PATRÓN** `volumen_pendiente_norm` < `0.0977` → IC=+0.286 (n=2419)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0977 (IC base=+0.273)

- **PATRÓN** `volumen_spike_ratio` > `1.6099` → IC=+0.278 (n=2679)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6099 (IC base=+0.273)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.283 (n=3282)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.273)

- **PATRÓN** `libro_liquidez` > `2032.4484` → IC=+0.289 (n=923)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2032.4484 (IC base=+0.273)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.293 (n=1678)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 17.0 (IC base=+0.273)

- **PATRÓN** `sigma_h` > `0.0086` → IC=+0.321 (n=1625)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0086 (IC base=+0.295)

- **PATRÓN** `drift_60min` |x|≤ `0.1781` → IC=+0.314 (n=1071)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1781 (IC base=+0.295)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.319 (n=924)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.295)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.297 (n=845)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.295)

- **PATRÓN** `ibs_20min` < `0.375` → IC=+0.296 (n=2435)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.375 (IC base=+0.295)

- **PATRÓN** `ibs_20min` > `0.2711` → IC=+0.303 (n=1104)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2711 (IC base=+0.295)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.402` → IC=+0.304 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.402 (IC base=+0.295)

- **PATRÓN** `volumen_pendiente_norm` < `0.1976` → IC=+0.294 (n=2389)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1976 (IC base=+0.295)

- **PATRÓN** `volumen_pendiente_norm` > `0.3431` → IC=+0.310 (n=392)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3431 (IC base=+0.295)

- **PATRÓN** `volumen_spike_ratio` < `1.7322` → IC=+0.299 (n=1027)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7322 (IC base=+0.295)

- **PATRÓN** `volumen_spike_ratio` > `2.7002` → IC=+0.307 (n=1058)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7002 (IC base=+0.295)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.297 (n=1230)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.295)

- **PATRÓN** `libro_liquidez` > `1922.908` → IC=+0.305 (n=1104)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1922.908 (IC base=+0.295)

- **PATRÓN** `ballena_activa_n` < `10.0` → IC=+0.301 (n=1073)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 10.0 (IC base=+0.295)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7352` → IC=-0.185 (n=1182)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7352
  - _Potencial_: sin este filtro IC_bueno=+0.063 (n=3554)

- **PATRÓN** `ibs_20min` > `0.8669` → IC=+0.166 (n=1143)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.8669 (IC base=+0.026)

- **PATRÓN** `dist_vwap_pct` > `0.1505` → IC=+0.234 (n=844)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1505 (IC base=+0.026)

- **PATRÓN** `dist_vwap_pct` < `0.3624` → IC=+0.233 (n=1605)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3624 (IC base=+0.026)

- **PATRÓN** `volumen_regimen` < `1.0083` → IC=+0.237 (n=1430)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0083 (IC base=+0.026)

- **PATRÓN** `volumen_regimen` > `0.667` → IC=+0.233 (n=1452)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.667 (IC base=+0.026)

- **PATRÓN** `volumen_pendiente_norm` < `0.1621` → IC=+0.234 (n=1715)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1621 (IC base=+0.026)

- **PATRÓN** `volumen_pendiente_norm` > `0.1021` → IC=+0.242 (n=517)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1021 (IC base=+0.026)

- **PATRÓN** `volumen_spike_ratio` < `2.4657` → IC=+0.238 (n=1572)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4657 (IC base=+0.026)

- **PATRÓN** `ballena_activa_n` < `119.0` → IC=+0.253 (n=1601)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 119.0 (IC base=+0.026)

- **PATRÓN** `volumen_regimen` < `1.1942` → IC=+0.241 (n=1126)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1942 (IC base=+0.001)

- **PATRÓN** `volumen_pendiente_norm` < `0.1015` → IC=+0.248 (n=1044)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1015 (IC base=+0.001)

- **PATRÓN** `volumen_pendiente_norm` > `0.2852` → IC=+0.301 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2852 (IC base=+0.001)

- **PATRÓN** `volumen_spike_ratio` < `1.794` → IC=+0.273 (n=716)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.794 (IC base=+0.001)

- **PATRÓN** `volumen_spike_ratio` > `2.4427` → IC=+0.258 (n=358)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4427 (IC base=+0.001)

- **PATRÓN** `ballena_activa_n` < `121.0` → IC=+0.263 (n=1085)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 121.0 (IC base=+0.001)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7547` → IC=-0.227 (n=2009)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7547
  - _Potencial_: sin este filtro IC_bueno=+0.312 (n=2011)

- **FILTRO** `ibs_20min` > `0.6386` → IC=-0.233 (n=975)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6386
  - _Potencial_: sin este filtro IC_bueno=+0.126 (n=2933)

- **FILTRO** `sigma_ewma_delta_pct` > `8.412` → IC=-0.249 (n=448)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.412
  - _Potencial_: sin este filtro IC_bueno=+0.074 (n=3460)

- **PATRÓN** `ibs_20min` > `0.7547` → IC=+0.312 (n=2011)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7547 (IC base=+0.043)

- **PATRÓN** `dist_vwap_pct` > `0.2123` → IC=+0.341 (n=868)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2123 (IC base=+0.043)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.369` → IC=+0.189 (n=629)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 9.369 (IC base=+0.043)

- **PATRÓN** `volumen_regimen` < `0.8515` → IC=+0.336 (n=994)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8515 (IC base=+0.043)

- **PATRÓN** `volumen_regimen` > `0.7018` → IC=+0.334 (n=1332)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7018 (IC base=+0.043)

- **PATRÓN** `volumen_pendiente_norm` < `0.159` → IC=+0.330 (n=1543)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.159 (IC base=+0.043)

- **PATRÓN** `volumen_pendiente_norm` > `0.275` → IC=+0.353 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.275 (IC base=+0.043)

- **PATRÓN** `volumen_spike_ratio` < `1.4421` → IC=+0.352 (n=484)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4421 (IC base=+0.043)

- **PATRÓN** `ballena_activa_n` < `55.0` → IC=+0.346 (n=1447)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 55.0 (IC base=+0.043)

- **PATRÓN** `ibs_20min` < `0.6386` → IC=+0.126 (n=2933)

  - _Acción_: Kelly boost +0.63€ cuando `ibs_20min` < 0.6386 (IC base=+0.037)

- **PATRÓN** `volumen_regimen` < `0.6968` → IC=+0.270 (n=599)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6968 (IC base=+0.037)

- **PATRÓN** `volumen_pendiente_norm` < `0.1591` → IC=+0.240 (n=1412)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1591 (IC base=+0.037)

- **PATRÓN** `volumen_pendiente_norm` > `0.0717` → IC=+0.257 (n=528)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0717 (IC base=+0.037)

- **PATRÓN** `volumen_spike_ratio` < `2.4505` → IC=+0.252 (n=1310)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4505 (IC base=+0.037)

- **PATRÓN** `ballena_activa_n` < `50.0` → IC=+0.265 (n=1336)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 50.0 (IC base=+0.037)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.011` → IC=+0.353 (n=1869)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.011 (IC base=+0.309)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.311 (n=806)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.309)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.317 (n=997)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.309)

- **PATRÓN** `ibs_20min` > `0.7619` → IC=+0.346 (n=1870)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7619 (IC base=+0.309)

- **PATRÓN** `dist_vwap_pct` > `0.2027` → IC=+0.334 (n=1165)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2027 (IC base=+0.309)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.847` → IC=+0.327 (n=1013)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.847 (IC base=+0.309)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.076` → IC=+0.310 (n=2384)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 10.076 (IC base=+0.309)

- **PATRÓN** `volumen_regimen` > `0.8658` → IC=+0.329 (n=1395)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8658 (IC base=+0.309)

- **PATRÓN** `volumen_pendiente_norm` > `0.28` → IC=+0.352 (n=308)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.28 (IC base=+0.309)

- **PATRÓN** `volumen_spike_ratio` > `1.4315` → IC=+0.321 (n=2008)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4315 (IC base=+0.309)

- **PATRÓN** `libro_liquidez` > `2587.1246` → IC=+0.309 (n=1395)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2587.1246 (IC base=+0.309)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.343 (n=1627)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=+0.309)

- **PATRÓN** `sigma_h` > `0.0151` → IC=+0.341 (n=1481)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0151 (IC base=+0.310)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.318 (n=1112)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.310)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.311 (n=1091)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.310)

- **PATRÓN** `ibs_20min` < `0.375` → IC=+0.332 (n=2218)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.375 (IC base=+0.310)

- **PATRÓN** `dist_vwap_pct` < `0.2311` → IC=+0.315 (n=2130)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2311 (IC base=+0.310)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.619` → IC=+0.324 (n=826)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.619 (IC base=+0.310)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.079` → IC=+0.310 (n=2635)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 10.079 (IC base=+0.310)

- **PATRÓN** `volumen_regimen` < `0.721` → IC=+0.314 (n=976)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.721 (IC base=+0.310)

- **PATRÓN** `volumen_regimen` > `1.2246` → IC=+0.340 (n=740)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2246 (IC base=+0.310)

- **PATRÓN** `volumen_pendiente_norm` > `0.2327` → IC=+0.358 (n=408)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2327 (IC base=+0.310)

- **PATRÓN** `volumen_spike_ratio` < `1.4167` → IC=+0.323 (n=681)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4167 (IC base=+0.310)

- **PATRÓN** `volumen_spike_ratio` > `2.1396` → IC=+0.311 (n=925)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1396 (IC base=+0.310)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0118` → IC=+0.227 (n=4766)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0118 (IC base=+0.178)

- **PATRÓN** `drift_60min` |x|≤ `0.1211` → IC=+0.197 (n=6287)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.1211 (IC base=+0.178)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.187 (n=14817)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.178)

- **PATRÓN** `ibs_20min` > `0.5527` → IC=+0.233 (n=14286)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5527 (IC base=+0.178)

- **PATRÓN** `dist_vwap_pct` > `0.1624` → IC=+0.208 (n=5639)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1624 (IC base=+0.178)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.253` → IC=+0.257 (n=3724)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.253 (IC base=+0.178)

- **PATRÓN** `volumen_regimen` < `1.1858` → IC=+0.162 (n=9483)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.1858 (IC base=+0.178)

- **PATRÓN** `volumen_regimen` > `0.6235` → IC=+0.161 (n=9486)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 0.6235 (IC base=+0.178)

- **PATRÓN** `volumen_pendiente_norm` > `0.2938` → IC=+0.207 (n=2066)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2938 (IC base=+0.178)

- **PATRÓN** `volumen_spike_ratio` > `2.6108` → IC=+0.191 (n=4625)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 2.6108 (IC base=+0.178)

- **PATRÓN** `ballena_activa_n` < `90.0` → IC=+0.196 (n=13193)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 90.0 (IC base=+0.178)

- **PATRÓN** `sigma_h` < `0.0112` → IC=+0.185 (n=13815)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0112 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.0796` → IC=+0.226 (n=4608)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0796 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.212 (n=6524)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` < `0.5111` → IC=+0.238 (n=13820)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5111 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.887` → IC=+0.196 (n=2241)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 9.887 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.639` → IC=+0.185 (n=12229)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` < 2.639 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` < `1.1856` → IC=+0.166 (n=9847)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.1856 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.2964` → IC=+0.224 (n=2057)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2964 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `2.6529` → IC=+0.188 (n=4349)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.6529 (IC base=+0.182)

- **PATRÓN** `ballena_activa_n` < `97.0` → IC=+0.195 (n=12799)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 97.0 (IC base=+0.182)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.226 (n=797)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0054 (IC base=+0.222)

- **PATRÓN** `drift_60min` |x|≤ `0.3381` → IC=+0.236 (n=2385)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3381 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.234 (n=882)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.228 (n=1615)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` > `0.9343` → IC=+0.297 (n=1590)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9343 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.805` → IC=+0.331 (n=755)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.805 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` > `0.281` → IC=+0.284 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.281 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` < `1.8412` → IC=+0.219 (n=1511)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8412 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` > `1.4374` → IC=+0.223 (n=2266)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4374 (IC base=+0.222)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.234 (n=2611)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.222)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.235 (n=1465)

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

- **PATRÓN** `drift_60min` |x|≤ `0.0641` → IC=+0.192 (n=718)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.0641 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.164 (n=2259)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` > `0.3184` → IC=+0.216 (n=2152)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3184 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` > `0.1869` → IC=+0.217 (n=1134)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1869 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.145` → IC=+0.214 (n=397)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.145 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `0.6929` → IC=+0.160 (n=947)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.6929 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` > `1.0622` → IC=+0.149 (n=976)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 1.0622 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` > `0.2832` → IC=+0.188 (n=334)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.2832 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `1.414` → IC=+0.169 (n=704)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 1.414 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` > `2.4856` → IC=+0.163 (n=704)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 2.4856 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `223.0` → IC=+0.160 (n=919)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 223.0 (IC base=+0.148)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.174 (n=2265)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0059 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.2361` → IC=+0.174 (n=1992)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.2361 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.188 (n=1078)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 15.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` < `0.6155` → IC=+0.208 (n=2263)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6155 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.325` → IC=+0.191 (n=432)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 11.325 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.155` → IC=+0.148 (n=1960)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 4.155 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `1.2065` → IC=+0.164 (n=2263)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.2065 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` < `0.0933` → IC=+0.152 (n=1937)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` < 0.0933 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `2.4921` → IC=+0.152 (n=2141)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.4921 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `222.0` → IC=+0.182 (n=912)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 222.0 (IC base=+0.148)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.232 (n=1097)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.3954` → IC=+0.221 (n=2129)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3954 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.233 (n=881)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.297 (n=1263)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.305` → IC=+0.306 (n=564)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.305 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` < `0.0979` → IC=+0.212 (n=2093)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0979 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.353` → IC=+0.233 (n=346)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.353 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` < `1.767` → IC=+0.210 (n=1035)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.767 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `2.7137` → IC=+0.226 (n=1066)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7137 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.215 (n=2884)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `1926.1784` → IC=+0.224 (n=1097)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1926.1784 (IC base=+0.210)

- **PATRÓN** `sigma_h` < `0.0105` → IC=+0.242 (n=1852)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0105 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.4198` → IC=+0.256 (n=1850)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4198 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.278 (n=794)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` < `0.0227` → IC=+0.293 (n=925)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0227 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.311` → IC=+0.277 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.311 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.3592` → IC=+0.287 (n=351)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3592 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` < `1.7601` → IC=+0.234 (n=889)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7601 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.1714` → IC=+0.239 (n=1345)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1714 (IC base=+0.234)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.236 (n=1076)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `1913.9884` → IC=+0.242 (n=954)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1913.9884 (IC base=+0.234)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.239 (n=1364)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 14.0 (IC base=+0.234)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.202 (n=1028)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.143)

- **PATRÓN** `drift_60min` |x|≤ `0.0784` → IC=+0.201 (n=776)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0784 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.154 (n=2410)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 5.0 (IC base=+0.143)

- **PATRÓN** `ibs_20min` > `0.2942` → IC=+0.205 (n=2325)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2942 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` > `0.1416` → IC=+0.195 (n=1376)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.1416 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.603` → IC=+0.198 (n=405)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 11.603 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` < `1.022` → IC=+0.150 (n=2047)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 1.022 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` > `0.1028` → IC=+0.172 (n=943)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.1028 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` < `1.826` → IC=+0.144 (n=1520)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.826 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` > `2.516` → IC=+0.164 (n=760)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 2.516 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `7189.7874` → IC=+0.197 (n=1054)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 7189.7874 (IC base=+0.143)

- **PATRÓN** `ballena_activa_n` < `134.0` → IC=+0.149 (n=2264)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 134.0 (IC base=+0.143)

- **PATRÓN** `sigma_h` < `0.0073` → IC=+0.157 (n=2457)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0073 (IC base=+0.130)

- **PATRÓN** `drift_60min` |x|≤ `0.3933` → IC=+0.147 (n=2456)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.3933 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.168 (n=1166)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 15.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` < `0.6789` → IC=+0.187 (n=2456)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.6789 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.547` → IC=+0.153 (n=600)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 9.547 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` < `0.8558` → IC=+0.159 (n=1638)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.8558 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` > `0.3001` → IC=+0.200 (n=374)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3001 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` < `1.81` → IC=+0.136 (n=1542)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.81 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` > `2.5607` → IC=+0.138 (n=771)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 2.5607 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `6626.5173` → IC=+0.188 (n=1114)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 6626.5173 (IC base=+0.130)

- **PATRÓN** `ballena_activa_n` < `112.0` → IC=+0.135 (n=1998)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 112.0 (IC base=+0.130)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0106` → IC=+0.172 (n=1186)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0106 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.152 (n=1841)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 11.0 (IC base=+0.124)

- **PATRÓN** `ibs_20min` > `0.4839` → IC=+0.215 (n=2607)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4839 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` > `0.194` → IC=+0.192 (n=1465)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.194 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.371` → IC=+0.287 (n=551)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.371 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` < `1.1753` → IC=+0.135 (n=2607)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 1.1753 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` > `0.7056` → IC=+0.125 (n=2329)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` > 0.7056 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` < `0.1615` → IC=+0.130 (n=2660)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` < 0.1615 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` < `1.5471` → IC=+0.140 (n=1114)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.5471 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.127 (n=2720)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.02 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `2674.0244` → IC=+0.207 (n=1182)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2674.0244 (IC base=+0.124)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.136 (n=2409)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 48.0 (IC base=+0.124)

- **PATRÓN** `sigma_h` < `0.0112` → IC=+0.142 (n=2687)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.0112 (IC base=+0.122)

- **PATRÓN** `drift_60min` |x|≤ `0.1082` → IC=+0.174 (n=896)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.1082 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.140 (n=2746)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 5.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` < `0.6176` → IC=+0.220 (n=2687)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6176 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.418` → IC=+0.138 (n=2373)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 2.418 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` < `1.1845` → IC=+0.131 (n=2688)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 1.1845 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` < `0.1648` → IC=+0.127 (n=2613)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` < 0.1648 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` > `0.2782` → IC=+0.135 (n=371)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` > 0.2782 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` < `1.4426` → IC=+0.133 (n=840)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 1.4426 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` > `2.4628` → IC=+0.129 (n=839)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 2.4628 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `2553.641` → IC=+0.186 (n=1218)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 2553.641 (IC base=+0.122)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.129 (n=2208)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 40.0 (IC base=+0.122)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0132` → IC=+0.248 (n=2144)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0132 (IC base=+0.222)

- **PATRÓN** `drift_60min` |x|≤ `0.1692` → IC=+0.236 (n=1056)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1692 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.226 (n=2486)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.228 (n=2164)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` > `0.6604` → IC=+0.257 (n=2401)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6604 (IC base=+0.222)

- **PATRÓN** `dist_vwap_pct` > `0.1803` → IC=+0.228 (n=1523)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1803 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.666` → IC=+0.254 (n=1082)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.666 (IC base=+0.222)

- **PATRÓN** `volumen_regimen` < `1.1704` → IC=+0.223 (n=2401)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1704 (IC base=+0.222)

- **PATRÓN** `volumen_regimen` > `0.6223` → IC=+0.230 (n=2400)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6223 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` > `0.2311` → IC=+0.268 (n=446)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2311 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` < `2.461` → IC=+0.226 (n=2338)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.461 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` > `1.8078` → IC=+0.231 (n=1559)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8078 (IC base=+0.222)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.224 (n=3125)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.222)

- **PATRÓN** `libro_liquidez` > `2548.421` → IC=+0.227 (n=1600)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2548.421 (IC base=+0.222)

- **PATRÓN** `sigma_h` < `0.0127` → IC=+0.235 (n=1075)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0127 (IC base=+0.233)

- **PATRÓN** `sigma_h` > `0.0226` → IC=+0.241 (n=1109)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0226 (IC base=+0.233)

- **PATRÓN** `drift_60min` |x|≤ `0.0876` → IC=+0.259 (n=814)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0876 (IC base=+0.233)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.252 (n=1186)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.233)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.234 (n=1095)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.233)

- **PATRÓN** `ibs_20min` < `0.43` → IC=+0.260 (n=2442)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.43 (IC base=+0.233)

- **PATRÓN** `dist_vwap_pct` > `0.3011` → IC=+0.244 (n=619)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3011 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.319` → IC=+0.267 (n=465)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.319 (IC base=+0.233)

- **PATRÓN** `volumen_regimen` < `0.87` → IC=+0.234 (n=1628)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.87 (IC base=+0.233)

- **PATRÓN** `volumen_regimen` > `0.6417` → IC=+0.236 (n=2442)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6417 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` > `0.28` → IC=+0.287 (n=332)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.28 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` < `2.5262` → IC=+0.228 (n=2284)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5262 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` > `1.4366` → IC=+0.235 (n=2283)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4366 (IC base=+0.233)

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

- **PATRÓN** `ibs_20min` < `0.6044` → IC=+0.126 (n=3462)

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

- **PATRÓN** `ibs_20min` < `0.6416` → IC=+0.140 (n=1049)

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
  - _Potencial_: sin este filtro IC_bueno=+0.098 (n=1014)

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

- **PATRÓN** `libro_liquidez` > `2594.3232` → IC=+0.138 (n=459)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 2594.3232 (IC base=+0.033)

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
- **PATRÓN** `sigma_h` > `0.0119` → IC=+0.230 (n=6213)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0119 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.191 (n=19417)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` > `0.4431` → IC=+0.230 (n=18636)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4431 (IC base=+0.182)

- **PATRÓN** `dist_vwap_pct` > `0.1607` → IC=+0.194 (n=6434)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.1607 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.165` → IC=+0.255 (n=4546)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.165 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` < `1.2201` → IC=+0.165 (n=12513)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.2201 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.2412` → IC=+0.206 (n=3371)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2412 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `2.6202` → IC=+0.194 (n=6052)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.6202 (IC base=+0.182)

- **PATRÓN** `ballena_activa_n` < `108.0` → IC=+0.202 (n=17272)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 108.0 (IC base=+0.182)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.196 (n=7504)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0057 (IC base=+0.188)

- **PATRÓN** `drift_60min` |x|≤ `0.3741` → IC=+0.193 (n=14985)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.3741 (IC base=+0.188)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.210 (n=6311)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.188)

- **PATRÓN** `ibs_20min` < `0.59` → IC=+0.241 (n=17032)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.59 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.715` → IC=+0.202 (n=2351)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.715 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.507` → IC=+0.192 (n=16510)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` < 3.507 (IC base=+0.188)

- **PATRÓN** `volumen_regimen` < `0.6329` → IC=+0.169 (n=3831)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 0.6329 (IC base=+0.188)

- **PATRÓN** `volumen_pendiente_norm` > `0.292` → IC=+0.251 (n=2311)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.292 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` > `1.8654` → IC=+0.195 (n=10790)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 1.8654 (IC base=+0.188)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.236 (n=5452)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.188)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `drift_60min` |x|≤ `0.351` → IC=+0.231 (n=3022)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.351 (IC base=+0.230)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.243 (n=1459)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.230)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.234 (n=2039)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.230)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.327 (n=1208)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.230)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.233` → IC=+0.349 (n=709)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.233 (IC base=+0.230)

- **PATRÓN** `volumen_pendiente_norm` > `0.2335` → IC=+0.287 (n=538)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2335 (IC base=+0.230)

- **PATRÓN** `volumen_spike_ratio` < `1.4461` → IC=+0.231 (n=971)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4461 (IC base=+0.230)

- **PATRÓN** `volumen_spike_ratio` > `2.2972` → IC=+0.240 (n=1320)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2972 (IC base=+0.230)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.247 (n=3265)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.230)

- **PATRÓN** `libro_liquidez` > `2049.79` → IC=+0.233 (n=1008)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2049.79 (IC base=+0.230)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.255 (n=1809)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.230)

- **PATRÓN** `sigma_h` < `0.0091` → IC=+0.268 (n=2608)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0091 (IC base=+0.265)

- **PATRÓN** `drift_60min` |x|≤ `0.1186` → IC=+0.290 (n=1148)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1186 (IC base=+0.265)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.271 (n=2396)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.265)

- **PATRÓN** `ibs_20min` < `0.5269` → IC=+0.289 (n=2609)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5269 (IC base=+0.265)

- **PATRÓN** `volumen_pendiente_norm` < `0.0966` → IC=+0.268 (n=2354)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0966 (IC base=+0.265)

- **PATRÓN** `volumen_pendiente_norm` > `0.2907` → IC=+0.289 (n=368)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2907 (IC base=+0.265)

- **PATRÓN** `volumen_spike_ratio` < `1.5681` → IC=+0.268 (n=1093)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5681 (IC base=+0.265)

- **PATRÓN** `volumen_spike_ratio` > `2.6878` → IC=+0.276 (n=828)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6878 (IC base=+0.265)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.266 (n=2971)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.265)

- **PATRÓN** `libro_liquidez` > `1779.9298` → IC=+0.269 (n=1738)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1779.9298 (IC base=+0.265)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.272 (n=1197)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.265)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.189 (n=1011)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0029 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.1044` → IC=+0.161 (n=1330)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.1044 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.159 (n=3145)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 5.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` > `0.233` → IC=+0.202 (n=3020)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.233 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` > `0.1279` → IC=+0.193 (n=1507)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.1279 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.551` → IC=+0.160 (n=636)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 9.551 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.167` → IC=+0.149 (n=2793)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 4.167 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `0.6316` → IC=+0.170 (n=1007)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 0.6316 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` > `1.0767` → IC=+0.150 (n=1369)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 1.0767 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` < `0.0726` → IC=+0.150 (n=2699)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` < 0.0726 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` > `0.2732` → IC=+0.189 (n=435)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.2732 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `2.1711` → IC=+0.155 (n=2603)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.1711 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` > `1.5326` → IC=+0.152 (n=2642)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.5326 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `233.0` → IC=+0.178 (n=974)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 233.0 (IC base=+0.148)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.162 (n=2584)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0059 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.0782` → IC=+0.184 (n=862)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.0782 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.169 (n=956)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` < `0.692` → IC=+0.189 (n=2583)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.692 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.07` → IC=+0.156 (n=428)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 11.07 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `1.1994` → IC=+0.151 (n=2582)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.1994 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.2194` → IC=+0.196 (n=481)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2194 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `2.4305` → IC=+0.146 (n=2476)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 2.4305 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `1.7816` → IC=+0.145 (n=1651)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.7816 (IC base=+0.139)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.140 (n=3351)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `262.0` → IC=+0.151 (n=1057)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 262.0 (IC base=+0.139)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0126` → IC=+0.254 (n=1039)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0126 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.233 (n=3248)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.225 (n=2785)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.302 (n=1165)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.236` → IC=+0.324 (n=668)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.236 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` < `0.1312` → IC=+0.226 (n=2915)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1312 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` > `1.6207` → IC=+0.229 (n=3021)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6207 (IC base=+0.224)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.231 (n=3695)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.224)

- **PATRÓN** `libro_liquidez` > `1934.9386` → IC=+0.238 (n=1407)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1934.9386 (IC base=+0.224)

- **PATRÓN** `sigma_h` < `0.0108` → IC=+0.247 (n=2582)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0108 (IC base=+0.240)

- **PATRÓN** `drift_60min` |x|≤ `0.179` → IC=+0.258 (n=1290)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.179 (IC base=+0.240)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.261 (n=1102)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.240)

- **PATRÓN** `ibs_20min` < `0.0458` → IC=+0.303 (n=977)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0458 (IC base=+0.240)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.408` → IC=+0.293 (n=327)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.408 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` > `0.3473` → IC=+0.306 (n=432)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3473 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` > `2.1472` → IC=+0.250 (n=1867)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1472 (IC base=+0.240)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.247 (n=1486)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.240)

- **PATRÓN** `libro_liquidez` > `1917.4884` → IC=+0.248 (n=1329)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1917.4884 (IC base=+0.240)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.249 (n=1846)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.240)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.198 (n=1072)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0035 (IC base=+0.143)

- **PATRÓN** `drift_60min` |x|≤ `0.4253` → IC=+0.154 (n=3213)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.4253 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.155 (n=3333)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 5.0 (IC base=+0.143)

- **PATRÓN** `ibs_20min` > `0.8127` → IC=+0.260 (n=1457)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8127 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` > `0.5599` → IC=+0.178 (n=769)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.5599 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.028` → IC=+0.159 (n=1442)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 3.028 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` < `1.0533` → IC=+0.153 (n=2827)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 1.0533 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` > `0.2336` → IC=+0.188 (n=566)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.2336 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` < `1.5221` → IC=+0.158 (n=1381)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.5221 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` > `2.1819` → IC=+0.149 (n=1423)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 2.1819 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `5436.372` → IC=+0.232 (n=1457)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5436.372 (IC base=+0.143)

- **PATRÓN** `ballena_activa_n` < `70.0` → IC=+0.156 (n=1375)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 70.0 (IC base=+0.143)

- **PATRÓN** `sigma_h` < `0.0076` → IC=+0.155 (n=2681)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0076 (IC base=+0.132)

- **PATRÓN** `drift_60min` |x|≤ `0.4362` → IC=+0.140 (n=2680)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.4362 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.156 (n=975)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 17.0 (IC base=+0.132)

- **PATRÓN** `ibs_20min` < `0.732` → IC=+0.186 (n=2680)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.732 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.081` → IC=+0.164 (n=406)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 11.081 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.143` → IC=+0.133 (n=2337)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` < 3.143 (IC base=+0.132)

- **PATRÓN** `volumen_regimen` < `0.6934` → IC=+0.148 (n=1180)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.6934 (IC base=+0.132)

- **PATRÓN** `volumen_pendiente_norm` > `0.2959` → IC=+0.221 (n=338)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2959 (IC base=+0.132)

- **PATRÓN** `volumen_spike_ratio` > `1.5382` → IC=+0.142 (n=2308)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.5382 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `6425.7391` → IC=+0.210 (n=894)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6425.7391 (IC base=+0.132)

- **PATRÓN** `ballena_activa_n` < `97.0` → IC=+0.137 (n=1743)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 97.0 (IC base=+0.132)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0106` → IC=+0.152 (n=1471)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` > 0.0106 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.155 (n=2285)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 11.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` > `0.4375` → IC=+0.195 (n=3244)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.4375 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` > `1.0143` → IC=+0.207 (n=545)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0143 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.576` → IC=+0.265 (n=822)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.576 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` < `0.8809` → IC=+0.138 (n=2163)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 0.8809 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` < `0.1618` → IC=+0.122 (n=3380)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_pendiente_norm` < 0.1618 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` < `2.4914` → IC=+0.122 (n=3169)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` < 2.4914 (IC base=+0.120)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.124 (n=3377)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.02 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `2715.618` → IC=+0.244 (n=1081)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2715.618 (IC base=+0.120)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.130 (n=1033)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 22.0 (IC base=+0.120)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.152 (n=2732)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0103 (IC base=+0.115)

- **PATRÓN** `drift_60min` |x|≤ `0.1345` → IC=+0.150 (n=1034)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.1345 (IC base=+0.115)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.127 (n=3199)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 5.0 (IC base=+0.115)

- **PATRÓN** `ibs_20min` < `0.6667` → IC=+0.207 (n=3114)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6667 (IC base=+0.115)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.201` → IC=+0.138 (n=2970)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 3.201 (IC base=+0.115)

- **PATRÓN** `volumen_regimen` < `0.6409` → IC=+0.144 (n=1033)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.6409 (IC base=+0.115)

- **PATRÓN** `volumen_pendiente_norm` > `0.2255` → IC=+0.160 (n=534)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.2255 (IC base=+0.115)

- **PATRÓN** `volumen_spike_ratio` < `1.44` → IC=+0.149 (n=973)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.44 (IC base=+0.115)

- **PATRÓN** `libro_liquidez` > `2580.485` → IC=+0.199 (n=1033)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 2580.485 (IC base=+0.115)

- **PATRÓN** `ballena_activa_n` < `45.0` → IC=+0.129 (n=2578)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 45.0 (IC base=+0.115)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0138` → IC=+0.256 (n=2714)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0138 (IC base=+0.233)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.238 (n=3170)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.233)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.237 (n=2732)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.233)

- **PATRÓN** `ibs_20min` > `0.9959` → IC=+0.318 (n=1012)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9959 (IC base=+0.233)

- **PATRÓN** `dist_vwap_pct` > `0.1899` → IC=+0.248 (n=1619)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1899 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.302` → IC=+0.281 (n=513)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.302 (IC base=+0.233)

- **PATRÓN** `volumen_regimen` < `1.2215` → IC=+0.238 (n=3037)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2215 (IC base=+0.233)

- **PATRÓN** `volumen_regimen` > `0.6415` → IC=+0.237 (n=3036)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6415 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` > `0.2358` → IC=+0.255 (n=525)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2358 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` > `1.5427` → IC=+0.240 (n=2646)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5427 (IC base=+0.233)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.235 (n=3943)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.233)

- **PATRÓN** `libro_liquidez` > `2552.8916` → IC=+0.235 (n=2024)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2552.8916 (IC base=+0.233)

- **PATRÓN** `sigma_h` > `0.0256` → IC=+0.257 (n=1046)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0256 (IC base=+0.235)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.241 (n=2949)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.235)

- **PATRÓN** `ibs_20min` < `0.5172` → IC=+0.268 (n=3132)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5172 (IC base=+0.235)

- **PATRÓN** `dist_vwap_pct` < `0.2159` → IC=+0.240 (n=2934)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2159 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.971` → IC=+0.278 (n=444)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.971 (IC base=+0.235)

- **PATRÓN** `volumen_regimen` > `1.2244` → IC=+0.258 (n=1044)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2244 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` > `0.2831` → IC=+0.298 (n=419)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2831 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` < `1.8128` → IC=+0.232 (n=1952)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8128 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` > `1.4311` → IC=+0.236 (n=2927)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4311 (IC base=+0.235)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.232 (n=2887)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=+0.235)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.196 (n=5294)

- **PATRÓN** `sigma_h` < `0.005` → IC=+0.246 (n=1832)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.213)

- **PATRÓN** `drift_60min` |x|≤ `0.504` → IC=+0.223 (n=5488)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.504 (IC base=+0.213)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.229 (n=1978)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.213)

- **PATRÓN** `ibs_20min` > `0.9392` → IC=+0.253 (n=1829)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9392 (IC base=+0.213)

- **PATRÓN** `dist_vwap_pct` < `0.4235` → IC=+0.217 (n=3938)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4235 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.874` → IC=+0.221 (n=904)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.874 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.607` → IC=+0.214 (n=4884)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.607 (IC base=+0.213)

- **PATRÓN** `volumen_regimen` < `0.7085` → IC=+0.224 (n=1758)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7085 (IC base=+0.213)

- **PATRÓN** `volumen_regimen` > `0.8857` → IC=+0.214 (n=2662)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8857 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` < `0.1066` → IC=+0.215 (n=5131)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1066 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` > `0.1659` → IC=+0.218 (n=1546)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1659 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` < `1.4536` → IC=+0.221 (n=1802)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4536 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` > `2.5922` → IC=+0.213 (n=1801)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5922 (IC base=+0.213)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.219 (n=4213)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.213)

- **PATRÓN** `libro_liquidez` > `3712.408` → IC=+0.222 (n=3658)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3712.408 (IC base=+0.213)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.238 (n=1329)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.194)

- **PATRÓN** `drift_60min` |x|≤ `0.4873` → IC=+0.210 (n=3982)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4873 (IC base=+0.194)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.203 (n=1550)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.194)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.212 (n=1768)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.194)

- **PATRÓN** `ibs_20min` < `0.0864` → IC=+0.207 (n=1328)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0864 (IC base=+0.194)

- **PATRÓN** `dist_vwap_pct` > `0.6514` → IC=+0.202 (n=685)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6514 (IC base=+0.194)

- **PATRÓN** `dist_vwap_pct` < `0.2381` → IC=+0.192 (n=3675)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` < 0.2381 (IC base=+0.194)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.797` → IC=+0.205 (n=3566)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.797 (IC base=+0.194)

- **PATRÓN** `volumen_regimen` < `1.0958` → IC=+0.201 (n=3331)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0958 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` < `0.0979` → IC=+0.198 (n=3662)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` < 0.0979 (IC base=+0.194)

- **PATRÓN** `volumen_spike_ratio` < `1.5361` → IC=+0.200 (n=1727)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5361 (IC base=+0.194)

- **PATRÓN** `volumen_spike_ratio` > `1.8164` → IC=+0.199 (n=2616)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8164 (IC base=+0.194)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.196 (n=5294)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.01 (IC base=+0.194)

- **PATRÓN** `ballena_activa_n` < `69.0` → IC=+0.206 (n=2607)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 69.0 (IC base=+0.194)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0055` → IC=+0.276 (n=745)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0055 (IC base=+0.265)

- **PATRÓN** `drift_60min` |x|≤ `0.0834` → IC=+0.296 (n=282)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0834 (IC base=+0.265)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.275 (n=847)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.265)

- **PATRÓN** `ibs_20min` < `0.4742` → IC=+0.283 (n=564)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4742 (IC base=+0.265)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.058` → IC=+0.283 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.058 (IC base=+0.265)

- **PATRÓN** `volumen_regimen` < `1.2269` → IC=+0.271 (n=846)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2269 (IC base=+0.265)

- **PATRÓN** `volumen_regimen` > `0.8759` → IC=+0.281 (n=564)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8759 (IC base=+0.265)

- **PATRÓN** `volumen_pendiente_norm` > `0.2882` → IC=+0.350 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2882 (IC base=+0.265)

- **PATRÓN** `volumen_spike_ratio` < `1.8139` → IC=+0.270 (n=563)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8139 (IC base=+0.265)

- **PATRÓN** `libro_liquidez` > `15982.9994` → IC=+0.271 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15982.9994 (IC base=+0.265)

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
- **PATRÓN** `sigma_h` < `0.008` → IC=+0.213 (n=1463)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.008 (IC base=+0.199)

- **PATRÓN** `drift_60min` |x|≤ `0.1468` → IC=+0.211 (n=645)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1468 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.217 (n=514)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.199 (n=1298)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.199)

- **PATRÓN** `ibs_20min` < `0.5128` → IC=+0.210 (n=977)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5128 (IC base=+0.199)

- **PATRÓN** `ibs_20min` > `0.7559` → IC=+0.202 (n=663)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7559 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.112` → IC=+0.208 (n=1327)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.112 (IC base=+0.199)

- **PATRÓN** `volumen_regimen` < `1.061` → IC=+0.200 (n=1288)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.061 (IC base=+0.199)

- **PATRÓN** `volumen_regimen` > `0.6413` → IC=+0.201 (n=1463)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6413 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` < `0.1051` → IC=+0.204 (n=1351)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1051 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` < `2.4588` → IC=+0.206 (n=1433)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4588 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.200 (n=1503)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

- **PATRÓN** `sigma_h` < `0.0081` → IC=+0.204 (n=1204)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0081 (IC base=+0.187)

- **PATRÓN** `drift_60min` |x|≤ `0.3844` → IC=+0.215 (n=1059)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3844 (IC base=+0.187)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.199 (n=456)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 16.0 (IC base=+0.187)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.200 (n=814)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.187)

- **PATRÓN** `ibs_20min` < `0.3984` → IC=+0.194 (n=803)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.3984 (IC base=+0.187)

- **PATRÓN** `ibs_20min` > `0.0884` → IC=+0.191 (n=1203)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.0884 (IC base=+0.187)

- **PATRÓN** `dist_vwap_pct` > `0.6347` → IC=+0.201 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6347 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.718` → IC=+0.189 (n=1228)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` < 6.718 (IC base=+0.187)

- **PATRÓN** `volumen_regimen` < `0.6415` → IC=+0.223 (n=402)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6415 (IC base=+0.187)

- **PATRÓN** `volumen_pendiente_norm` > `0.074` → IC=+0.214 (n=498)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.074 (IC base=+0.187)

- **PATRÓN** `volumen_spike_ratio` < `2.1958` → IC=+0.195 (n=1037)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 2.1958 (IC base=+0.187)

- **PATRÓN** `volumen_spike_ratio` > `2.5255` → IC=+0.191 (n=393)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.5255 (IC base=+0.187)

- **PATRÓN** `libro_liquidez` > `5485.836` → IC=+0.200 (n=1203)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5485.836 (IC base=+0.187)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0112` → IC=+0.205 (n=703)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0112 (IC base=+0.185)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.213 (n=768)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.185)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.263 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.185)

- **PATRÓN** `dist_vwap_pct` > `0.7336` → IC=+0.242 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7336 (IC base=+0.185)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.273` → IC=+0.205 (n=436)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.273 (IC base=+0.185)

- **PATRÓN** `volumen_regimen` < `0.7037` → IC=+0.229 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7037 (IC base=+0.185)

- **PATRÓN** `volumen_pendiente_norm` < `0.1066` → IC=+0.198 (n=717)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` < 0.1066 (IC base=+0.185)

- **PATRÓN** `volumen_spike_ratio` < `1.5649` → IC=+0.194 (n=341)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 1.5649 (IC base=+0.185)

- **PATRÓN** `volumen_spike_ratio` > `2.4918` → IC=+0.200 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4918 (IC base=+0.185)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.190 (n=934)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.02 (IC base=+0.185)

- **PATRÓN** `libro_liquidez` > `4286.507` → IC=+0.228 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4286.507 (IC base=+0.185)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.193 (n=689)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 43.0 (IC base=+0.185)

- **PATRÓN** `sigma_h` < `0.0094` → IC=+0.219 (n=389)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0094 (IC base=+0.207)

- **PATRÓN** `drift_60min` |x|≤ `0.5007` → IC=+0.230 (n=513)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5007 (IC base=+0.207)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.243 (n=395)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 9.0 (IC base=+0.207)

- **PATRÓN** `ibs_20min` < `0.6404` → IC=+0.234 (n=513)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6404 (IC base=+0.207)

- **PATRÓN** `dist_vwap_pct` > `0.5012` → IC=+0.210 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5012 (IC base=+0.207)

- **PATRÓN** `dist_vwap_pct` < `0.3064` → IC=+0.209 (n=493)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3064 (IC base=+0.207)

- **PATRÓN** `volumen_regimen` < `1.126` → IC=+0.211 (n=513)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.126 (IC base=+0.207)

- **PATRÓN** `volumen_regimen` > `0.9335` → IC=+0.211 (n=389)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.9335 (IC base=+0.207)

- **PATRÓN** `volumen_pendiente_norm` < `0.1071` → IC=+0.225 (n=507)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1071 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` > `2.2063` → IC=+0.241 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2063 (IC base=+0.207)

- **PATRÓN** `libro_liquidez` > `3008.1204` → IC=+0.228 (n=583)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3008.1204 (IC base=+0.207)

- **PATRÓN** `ballena_activa_n` < `29.0` → IC=+0.252 (n=389)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 29.0 (IC base=+0.207)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.150 (n=822)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0042 (IC base=+0.065)

- **PATRÓN** `ibs_20min` > `0.3865` → IC=+0.136 (n=1776)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` > 0.3865 (IC base=+0.065)

- **PATRÓN** `dist_vwap_pct` > `0.1458` → IC=+0.146 (n=906)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` > 0.1458 (IC base=+0.065)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.814` → IC=+0.150 (n=392)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 10.814 (IC base=+0.065)

- **PATRÓN** `ibs_20min` < `0.0418` → IC=+0.261 (n=474)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0418 (IC base=+0.049)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.872` → IC=+0.172 (n=172)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 9.872 (IC base=+0.049)

- **PATRÓN** `volumen_pendiente_norm` > `0.1468` → IC=+0.160 (n=304)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.1468 (IC base=+0.049)

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

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0674 (IC base=+0.056)

- **PATRÓN** `volumen_pendiente_norm` > `0.2164` → IC=+0.188 (n=91)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.2164 (IC base=+0.056)

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

- **PATRÓN** `ibs_20min` < `0.0314` → IC=+0.254 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0314 (IC base=+0.016)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.547` → IC=+0.217 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.547 (IC base=+0.016)

### GBM_LATE_60M#SOL#60min
- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.197 (n=216)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 1.0 (IC base=+0.024)

- **PATRÓN** `dist_vwap_pct` > `0.4664` → IC=+0.134 (n=211)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` > 0.4664 (IC base=+0.024)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.025` → IC=+0.140 (n=134)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 9.025 (IC base=+0.024)

- **PATRÓN** `sigma_h` < `0.0102` → IC=+0.159 (n=268)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0102 (IC base=+0.077)

- **PATRÓN** `ibs_20min` < `0.2` → IC=+0.211 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2 (IC base=+0.077)

- **PATRÓN** `dist_vwap_pct` < `0.1699` → IC=+0.139 (n=264)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.1699 (IC base=+0.077)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.219` → IC=+0.339 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.219 (IC base=+0.077)

- **PATRÓN** `volumen_regimen` > `1.1218` → IC=+0.188 (n=91)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` > 1.1218 (IC base=+0.077)

- **PATRÓN** `volumen_pendiente_norm` > `0.1517` → IC=+0.206 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1517 (IC base=+0.077)

- **PATRÓN** `volumen_spike_ratio` < `2.2151` → IC=+0.135 (n=220)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 2.2151 (IC base=+0.077)

- **PATRÓN** `volumen_spike_ratio` > `1.8302` → IC=+0.155 (n=166)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.8302 (IC base=+0.077)

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
- **PATRÓN** `libro_liquidez` > `2919.5711` → IC=+0.136 (n=465)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 2919.5711 (IC base=+0.099)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `libro_liquidez` > `2919.5711` → IC=+0.136 (n=465)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 2919.5711 (IC base=+0.099)

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
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=446)

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
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=888)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=888)

- **FILTRO** `py_entrada` < `0.44` → IC=-0.132 (n=275)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=693)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=957)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=957)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=232)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=232)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=316)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=275)

- **FILTRO** `py_entrada` > `0.545` → IC=-0.120 (n=77)

  - _Acción_: SKIP cuando `py_entrada` > 0.545
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=269)

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
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=496)

- **FILTRO** `profundidad_ratio` < `43.4` → IC=-0.143 (n=155)

  - _Acción_: SKIP cuando `profundidad_ratio` < 43.4
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=466)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.184 (n=96)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=415)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.120 (n=364)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=378)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.145 (n=108)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=469)

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
- **FILTRO** `py_entrada` < `0.47` → IC=-0.164 (n=6844)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=20630)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.177 (n=6842)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.046 (n=21423)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.191 (n=1233)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=3819)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.178 (n=1167)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=3852)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.138 (n=1324)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` > 1.0 (IC base=+0.042)

- **PATRÓN** `libro_liquidez` > `1056.9996` → IC=+0.138 (n=2526)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 1056.9996 (IC base=+0.042)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.130 (n=2357)

  - _Acción_: Kelly boost +0.65€ cuando `py_entrada` < 0.5 (IC base=+0.011)

- **PATRÓN** `libro_liquidez` > `1234.9858` → IC=+0.151 (n=1707)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 1234.9858 (IC base=+0.011)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` > `0.57` → IC=-0.185 (n=974)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=3038)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` > `0.62` → IC=-0.203 (n=1219)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.078 (n=3927)

- **PATRÓN** `ibs_20min` > `0.965` → IC=+0.128 (n=1716)

  - _Acción_: Kelly boost +0.64€ cuando `ibs_20min` > 0.965 (IC base=+0.036)

- **PATRÓN** `libro_liquidez` > `1752.2` → IC=+0.122 (n=1716)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 1752.2 (IC base=+0.036)

### MOMENTUM_IBS_15M_BALLENA#ETH#15min
- **FILTRO** `py_entrada` > `0.575` → IC=-0.185 (n=1006)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=3048)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.152 (n=1247)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=3801)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=2410)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.162 (n=772)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=2334)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.189 (n=911)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=2820)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=3710)

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
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=707)

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
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=42203)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.296 (n=14226)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=46848)

- **FILTRO** `ibs_7min` < `0.2304` → IC=-0.231 (n=15267)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2304
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=45807)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.153 (n=20678)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=40396)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.242 (n=18912)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=57702)

- **FILTRO** `ibs_7min` > `0.2842` → IC=-0.181 (n=19149)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2842
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=57465)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.153 (n=2660)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=8107)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.316 (n=2611)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=8156)

- **FILTRO** `ibs_7min` < `0.7115` → IC=-0.248 (n=3550)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7115
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=7217)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.148 (n=2601)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=8166)

- **FILTRO** `py_entrada` > `0.72` → IC=-0.278 (n=3154)

  - _Acción_: SKIP cuando `py_entrada` > 0.72
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=10083)

- **FILTRO** `ibs_7min` > `0.7722` → IC=-0.214 (n=3308)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7722
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=9929)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.128 (n=2452)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.097 (n=7787)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.263 (n=2426)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=7813)

- **FILTRO** `ibs_7min` < `0.7192` → IC=-0.205 (n=2559)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7192
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=7680)

- **FILTRO** `ballena_activa_n` > `155.0` → IC=-0.193 (n=2550)

  - _Acción_: SKIP cuando `ballena_activa_n` > 155.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=7689)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.258 (n=2581)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=7860)

- **FILTRO** `ibs_7min` > `0.2661` → IC=-0.192 (n=2609)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2661
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=7832)

- **FILTRO** `ballena_activa_n` > `152.0` → IC=-0.179 (n=2591)

  - _Acción_: SKIP cuando `ballena_activa_n` > 152.0
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=7850)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.162 (n=2516)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=7735)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.312 (n=2544)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=7707)

- **FILTRO** `ibs_7min` < `0.2903` → IC=-0.248 (n=3381)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2903
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=6870)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.197 (n=2286)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=7965)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.259 (n=3303)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=10760)

- **FILTRO** `ibs_7min` > `0.7308` → IC=-0.180 (n=3514)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7308
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=10549)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.124 (n=3240)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.094 (n=6680)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.264 (n=2394)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=7526)

- **FILTRO** `ibs_7min` < `0.7222` → IC=-0.195 (n=2480)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7222
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=7440)

- **FILTRO** `ballena_activa_n` > `26.0` → IC=-0.188 (n=2443)

  - _Acción_: SKIP cuando `ballena_activa_n` > 26.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=7477)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.260 (n=2338)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=7966)

- **FILTRO** `ibs_7min` > `0.2749` → IC=-0.172 (n=2575)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2749
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=7729)

- **FILTRO** `ballena_activa_n` > `25.0` → IC=-0.172 (n=2533)

  - _Acción_: SKIP cuando `ballena_activa_n` > 25.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=7771)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.283 (n=2459)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=7471)

- **FILTRO** `ibs_7min` < `0.7143` → IC=-0.224 (n=3271)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7143
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=6659)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.221 (n=2355)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=7575)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.194 (n=3536)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=11206)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.32` → IC=-0.296 (n=2421)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=7546)

- **FILTRO** `ibs_7min` < `0.1887` → IC=-0.226 (n=2491)

  - _Acción_: SKIP cuando `ibs_7min` < 0.1887
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=7476)

- **FILTRO** `ballena_activa_n` > `9.0` → IC=-0.199 (n=2381)

  - _Acción_: SKIP cuando `ballena_activa_n` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=7586)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.222 (n=3418)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=10409)

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

- **FILTRO** `pct_vs_K` |x|> `2.0709` → IC=-0.369 (n=281)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.0709
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=287)

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
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=4286)

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
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=2415)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0055` → IC=+0.188 (n=1749)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0055 (IC base=+0.167)

- **PATRÓN** `sigma_h` > `0.0124` → IC=+0.177 (n=1325)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` > 0.0124 (IC base=+0.167)

- **PATRÓN** `drift_60min` |x|≤ `0.1781` → IC=+0.184 (n=3498)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.1781 (IC base=+0.167)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1323` → IC=+0.175 (n=1598)

  - _Acción_: Kelly boost +0.88€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1323 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.176 (n=3673)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 6.0 (IC base=+0.167)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.167 (n=3684)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` < 15.0 (IC base=+0.167)

- **PATRÓN** `ibs_15` > `0.5333` → IC=+0.240 (n=3979)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5333 (IC base=+0.167)

- **PATRÓN** `dist_vwap_pct` > `0.1291` → IC=+0.164 (n=1919)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.1291 (IC base=+0.167)

- **PATRÓN** `dist_vwap_pct` < `0.4873` → IC=+0.152 (n=3634)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.4873 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.108` → IC=+0.262 (n=774)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.108 (IC base=+0.167)

- **PATRÓN** `libro_liquidez` > `4564.5735` → IC=+0.182 (n=1325)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 4564.5735 (IC base=+0.167)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=1602)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.221 (n=676)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.206)

- **PATRÓN** `drift_60min` |x|≤ `0.0763` → IC=+0.250 (n=298)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0763 (IC base=+0.206)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2616` → IC=+0.227 (n=225)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2616 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.228 (n=708)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.206)

- **PATRÓN** `ibs_15` > `0.7223` → IC=+0.273 (n=676)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7223 (IC base=+0.206)

- **PATRÓN** `dist_vwap_pct` > `0.2353` → IC=+0.227 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2353 (IC base=+0.206)

- **PATRÓN** `dist_vwap_pct` < `0.5108` → IC=+0.211 (n=765)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5108 (IC base=+0.206)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.394` → IC=+0.302 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.394 (IC base=+0.206)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.208 (n=876)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.206)

- **PATRÓN** `libro_liquidez` > `8119.484` → IC=+0.218 (n=676)

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

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `ibs_15` > `0.88` → IC=+0.234 (n=321)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.88 (IC base=+0.081)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.128 (n=503)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.01 (IC base=+0.081)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0242` → IC=+0.229 (n=297)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0242 (IC base=+0.194)

- **PATRÓN** `drift_60min` |x|≤ `0.2` → IC=+0.206 (n=890)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2 (IC base=+0.194)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3432` → IC=+0.222 (n=790)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3432 (IC base=+0.194)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.204 (n=800)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.194)

- **PATRÓN** `ibs_15` > `0.5156` → IC=+0.273 (n=889)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5156 (IC base=+0.194)

- **PATRÓN** `dist_vwap_pct` > `0.13` → IC=+0.211 (n=504)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.13 (IC base=+0.194)

- **PATRÓN** `dist_vwap_pct` < `0.7261` → IC=+0.195 (n=1036)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` < 0.7261 (IC base=+0.194)

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
- **FILTRO** `sigma_h` > `0.0069` → IC=-0.175 (n=2287)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0069
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=2288)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.213 (n=1790)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=2785)

- **FILTRO** `libro_liquidez` < `4242.2689` → IC=-0.154 (n=3019)

  - _Acción_: SKIP cuando `libro_liquidez` < 4242.2689
  - _Potencial_: sin este filtro IC_bueno=+0.098 (n=1556)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.138` → IC=+0.217 (n=411)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.138 (IC base=-0.068)

- **PATRÓN** `ibs_15` > `0.6326` → IC=+0.279 (n=1104)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6326 (IC base=-0.068)

- **PATRÓN** `dist_vwap_pct` > `0.1115` → IC=+0.205 (n=636)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1115 (IC base=-0.068)

- **PATRÓN** `dist_vwap_pct` < `0.4263` → IC=+0.201 (n=1086)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4263 (IC base=-0.068)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2301` → IC=+0.273 (n=1309)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2301 (IC base=-0.011)

- **PATRÓN** `ibs_15` < `0.3676` → IC=+0.282 (n=3927)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3676 (IC base=-0.011)

- **PATRÓN** `dist_vwap_pct` > `0.8718` → IC=+0.276 (n=378)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8718 (IC base=-0.011)

- **PATRÓN** `dist_vwap_pct` < `0.1641` → IC=+0.247 (n=2948)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1641 (IC base=-0.011)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0334` → IC=-0.222 (n=2112)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0334
  - _Potencial_: sin este filtro IC_bueno=-0.097 (n=705)

- **FILTRO** `sigma_h` > `0.0067` → IC=-0.210 (n=704)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0067
  - _Potencial_: sin este filtro IC_bueno=-0.185 (n=2113)

- **FILTRO** `sigma_h` < `0.0035` → IC=-0.232 (n=704)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0035
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=2113)

- **FILTRO** `sigma_ewma_delta_pct` > `22.923` → IC=-0.270 (n=406)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 22.923
  - _Potencial_: sin este filtro IC_bueno=-0.178 (n=2411)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.161 (n=275)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0029 (IC base=+0.086)

- **PATRÓN** `ibs_15` > `0.7609` → IC=+0.327 (n=368)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7609 (IC base=+0.086)

- **PATRÓN** `dist_vwap_pct` > `0.1051` → IC=+0.282 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1051 (IC base=+0.086)

- **PATRÓN** `dist_vwap_pct` < `0.4958` → IC=+0.289 (n=410)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4958 (IC base=+0.086)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.15` → IC=+0.145 (n=240)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 19.15 (IC base=+0.086)

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

- **PATRÓN** `drift_15min` |x|≤ `0.7702` → IC=+0.256 (n=1307)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7702 (IC base=+0.245)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1535` → IC=+0.266 (n=990)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1535 (IC base=+0.245)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.245 (n=1064)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.245)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.247 (n=1324)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.245)

- **PATRÓN** `ibs_15` < `0.3774` → IC=+0.278 (n=1486)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3774 (IC base=+0.245)

- **PATRÓN** `dist_vwap_pct` > `0.1547` → IC=+0.261 (n=538)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1547 (IC base=+0.245)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.392` → IC=+0.253 (n=653)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.392 (IC base=+0.245)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `drift_60min` |x|> `0.1724` → IC=-0.244 (n=358)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1724
  - _Potencial_: sin este filtro IC_bueno=-0.159 (n=696)

- **FILTRO** `drift_15min` |x|> `0.888` → IC=-0.281 (n=263)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.888
  - _Potencial_: sin este filtro IC_bueno=-0.157 (n=791)

- **FILTRO** `sigma_ewma_delta_pct` > `6.602` → IC=-0.201 (n=242)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.602
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=812)

- **FILTRO** `sigma_ewma_delta_pct` > `17.651` → IC=-0.148 (n=557)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 17.651
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=4427)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1478` → IC=+0.181 (n=45)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.90€ cuando `delta_ratio_macro` |x|> 0.1478 (IC base=-0.188)

- **PATRÓN** `ibs_15` > `0.5625` → IC=+0.234 (n=62)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5625 (IC base=-0.188)

- **PATRÓN** `dist_vwap_pct` < `0.4298` → IC=+0.162 (n=75)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.4298 (IC base=-0.188)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.214 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 37.0 (IC base=-0.188)

- **PATRÓN** `ibs_15` < `0.3814` → IC=+0.290 (n=661)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3814 (IC base=-0.036)

- **PATRÓN** `dist_vwap_pct` < `0.2583` → IC=+0.237 (n=622)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2583 (IC base=-0.036)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0199` → IC=-0.246 (n=625)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0199
  - _Potencial_: sin este filtro IC_bueno=-0.171 (n=627)

- **FILTRO** `drift_60min` |x|> `0.1513` → IC=-0.217 (n=312)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1513
  - _Potencial_: sin este filtro IC_bueno=-0.206 (n=940)

- **FILTRO** `sigma_ewma_delta_pct` > `7.426` → IC=-0.211 (n=392)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 7.426
  - _Potencial_: sin este filtro IC_bueno=-0.208 (n=860)

- **FILTRO** `libro_spread` > `0.04` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.04
  - _Potencial_: sin este filtro IC_bueno=-0.208 (n=1233)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.209)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.209)

- **PATRÓN** `delta_ratio_macro` |x|> `0.07` → IC=+0.273 (n=814)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.07 (IC base=-0.024)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1182` → IC=+0.287 (n=397)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1182 (IC base=-0.024)

- **PATRÓN** `ibs_15` < `0.1368` → IC=+0.311 (n=607)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.1368 (IC base=-0.024)

- **PATRÓN** `dist_vwap_pct` > `0.7735` → IC=+0.350 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7735 (IC base=-0.024)

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
- **PATRÓN** `sigma_h` < `0.006` → IC=+0.289 (n=1181)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.006 (IC base=+0.285)

- **PATRÓN** `drift_60min` |x|≤ `0.0537` → IC=+0.321 (n=394)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0537 (IC base=+0.285)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1495` → IC=+0.287 (n=787)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1495 (IC base=+0.285)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.224` → IC=+0.295 (n=710)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.224 (IC base=+0.285)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.302 (n=1228)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.285)

- **PATRÓN** `ibs_15` > `0.8388` → IC=+0.316 (n=1181)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8388 (IC base=+0.285)

- **PATRÓN** `dist_vwap_pct` > `0.2628` → IC=+0.319 (n=506)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2628 (IC base=+0.285)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.173` → IC=+0.373 (n=338)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.173 (IC base=+0.285)

- **PATRÓN** `libro_liquidez` > `12007.5914` → IC=+0.305 (n=536)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12007.5914 (IC base=+0.285)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.307 (n=211)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.277)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.288 (n=286)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.277)

- **PATRÓN** `drift_60min` |x|≤ `0.0585` → IC=+0.312 (n=211)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0585 (IC base=+0.277)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2654` → IC=+0.279 (n=211)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2654 (IC base=+0.277)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.388` → IC=+0.282 (n=558)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.388 (IC base=+0.277)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.298 (n=663)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.277)

- **PATRÓN** `ibs_15` > `0.8292` → IC=+0.304 (n=631)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8292 (IC base=+0.277)

- **PATRÓN** `dist_vwap_pct` > `0.2515` → IC=+0.317 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2515 (IC base=+0.277)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.503` → IC=+0.376 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.503 (IC base=+0.277)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.278 (n=816)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.277)

- **PATRÓN** `libro_liquidez` > `12796.3088` → IC=+0.306 (n=421)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12796.3088 (IC base=+0.277)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.306 (n=550)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0067 (IC base=+0.293)

- **PATRÓN** `drift_60min` |x|≤ `0.1076` → IC=+0.316 (n=367)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1076 (IC base=+0.293)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0669` → IC=+0.295 (n=550)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0669 (IC base=+0.293)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1019` → IC=+0.336 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1019 (IC base=+0.293)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.312 (n=530)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.293)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.294 (n=499)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.293)

- **PATRÓN** `ibs_15` > `0.8494` → IC=+0.326 (n=550)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8494 (IC base=+0.293)

- **PATRÓN** `dist_vwap_pct` > `0.2788` → IC=+0.324 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2788 (IC base=+0.293)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.34` → IC=+0.371 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.34 (IC base=+0.293)

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

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5333 sube el IC de +0.167 a +0.240 en UPDOWN_GBM#15min (n=3979). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7223 sube el IC de +0.206 a +0.273 en UPDOWN_GBM#BTC#15min (n=676). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.6258 sube el IC de +0.142 a +0.260 en UPDOWN_GBM#ETH#15min (n=722). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.88 sube el IC de +0.081 a +0.234 en UPDOWN_GBM#SOL#15min (n=321). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5156 sube el IC de +0.194 a +0.273 en UPDOWN_GBM#XRP#15min (n=889). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1071 sube el IC de +0.070 a +0.169 en UPDOWN_GBM#XRP#15min (n=805). Ya aplicado como kelly_boost=+0.85€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6326 sube el IC de -0.068 a +0.279 en UPDOWN_GBM_15M_TARDIO (n=1104). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3676 sube el IC de -0.011 a +0.282 en UPDOWN_GBM_15M_TARDIO (n=3927). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7609 sube el IC de +0.086 a +0.327 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=368). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.618 sube el IC de -0.191 a +0.314 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=68). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.5867 sube el IC de +0.152 a +0.244 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=556). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3774 sube el IC de +0.245 a +0.278 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=1486). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de -0.188 a +0.234 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=62). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3814 sube el IC de -0.036 a +0.290 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=661). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.209 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.1368 sube el IC de -0.024 a +0.311 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=607). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_YES, IBS > 0.8434 sube el IC de +0.089 a +0.357 en UPDOWN_GBM_ETH_15M_HORA7 (n=19). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_YES, IBS > 0.8434 sube el IC de +0.089 a +0.357 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=19). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8388 sube el IC de +0.285 a +0.316 en UPDOWN_GBM_IBS_ALTO (n=1181). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8292 sube el IC de +0.277 a +0.304 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=631). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8494 sube el IC de +0.293 a +0.326 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=550). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
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
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 815 | -0.010 | +84.09€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 815 | -0.010 | +84.09€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE | 6 | +0.000 | +1.70€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE#15min | 6 | +0.000 | +1.70€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 624 | -0.037 | +50.80€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 624 | -0.037 | +50.80€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 149 | +0.089 | +26.84€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 149 | +0.089 | +26.84€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 36 | +0.026 | +4.76€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 36 | +0.026 | +4.76€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 42881 | -0.083 | -5530.75€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 2495 | +0.056 | -275.89€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 40386 | -0.092 | -5254.86€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4604 | -0.117 | -760.86€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4604 | -0.117 | -760.86€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 2495 | +0.056 | -275.89€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 2495 | +0.056 | -275.89€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 4553 | -0.113 | -863.06€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 4553 | -0.113 | -863.06€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 11481 | -0.024 | -1190.74€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 11481 | -0.024 | -1190.74€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 11463 | -0.117 | -1083.32€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 11463 | -0.117 | -1083.32€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 8285 | -0.124 | -1356.88€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 8285 | -0.124 | -1356.88€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 39774 | -0.013 | +3214.98€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 10263 | +0.004 | +1625.16€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 29511 | -0.019 | +1589.83€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 39774 | -0.013 | +3214.98€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 10263 | +0.004 | +1625.16€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 29511 | -0.019 | +1589.83€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 159741 | +0.115 | -6327.62€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 19803 | +0.181 | -664.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 716 | -0.008 | -73.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 129813 | +0.107 | -5267.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 9409 | +0.096 | -322.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 21515 | +0.107 | -1328.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 65 | -0.172 | +7.58€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 21435 | +0.109 | -1324.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 30707 | +0.127 | -475.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5397 | +0.182 | -219.40€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 21503 | +0.121 | -124.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 3765 | +0.081 | -109.79€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 21570 | +0.100 | -1493.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 80 | -0.122 | -5.27€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 21475 | +0.101 | -1477.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 34022 | +0.124 | -637.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 8726 | +0.177 | -193.52€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 21815 | +0.107 | -392.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 3469 | +0.101 | -43.25€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 30386 | +0.114 | -1433.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 5461 | +0.198 | -260.86€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 619 | +0.022 | -19.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 22131 | +0.096 | -983.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 2175 | +0.116 | -169.25€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO#XRP | 21541 | +0.107 | -959.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 74 | -0.105 | +6.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 21454 | +0.108 | -965.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 25770 | +0.195 | -1623.31€ | 2 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 25770 | +0.195 | -1623.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 5839 | +0.178 | -506.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 5839 | +0.178 | -506.25€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 3442 | +0.202 | -88.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 3442 | +0.202 | -88.77€ | 3 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 5771 | +0.178 | -478.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 5771 | +0.178 | -478.07€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 4950 | +0.247 | -180.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 4950 | +0.247 | -180.89€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 5689 | +0.186 | -383.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 5689 | +0.186 | -383.07€ | 0 | 3 |
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
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 90366 | +0.201 | -6444.98€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 90366 | +0.201 | -6444.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 15539 | +0.185 | -1615.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 15539 | +0.185 | -1615.69€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 14581 | +0.225 | -479.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 14581 | +0.225 | -479.04€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 15494 | +0.181 | -1631.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 15494 | +0.181 | -1631.38€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 14695 | +0.218 | -580.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 14695 | +0.218 | -580.23€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 14983 | +0.203 | -958.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 14983 | +0.203 | -958.27€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 15074 | +0.198 | -1180.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 15074 | +0.198 | -1180.37€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 34676 | +0.117 | +264.02€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 34676 | +0.117 | +264.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 17242 | +0.119 | +207.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 17242 | +0.119 | +207.82€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 17434 | +0.114 | +56.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 17434 | +0.114 | +56.20€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 2236 | +0.294 | -0.08€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 2236 | +0.294 | -0.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 1026 | +0.281 | -24.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 1026 | +0.281 | -24.57€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 1085 | +0.300 | +20.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 1085 | +0.300 | +20.84€ | 0 | 4 |
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
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 69180 | +0.101 | -1649.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 5583 | +0.092 | +69.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 63597 | +0.102 | -1719.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 37947 | +0.106 | -388.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 5583 | +0.092 | +69.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 32364 | +0.108 | -458.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 14418 | +0.110 | -59.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 14418 | +0.110 | -59.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 16815 | +0.083 | -1201.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 16815 | +0.083 | -1201.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 900 | +0.191 | -110.64€ | 3 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 900 | +0.191 | -110.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 900 | +0.191 | -110.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 900 | +0.191 | -110.64€ | 3 | 4 |
| ✅ GBM_LATE_15M | 47285 | +0.096 | +25185.15€ | 0 | 18 |
| ✅ GBM_LATE_15M#15min | 47285 | +0.096 | +25185.15€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 7862 | +0.221 | +6633.37€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 7862 | +0.221 | +6633.37€ | 0 | 23 |
| ✅ GBM_LATE_15M#BTC | 7188 | +0.178 | +5574.04€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 7188 | +0.178 | +5574.04€ | 0 | 22 |
| ✅ GBM_LATE_15M#DOGE | 8472 | +0.204 | +6570.69€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 8472 | +0.204 | +6570.69€ | 0 | 19 |
| ✅ GBM_LATE_15M#ETH | 6502 | +0.047 | +1907.13€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 6502 | +0.047 | +1907.13€ | 1 | 17 |
| ✅ GBM_LATE_15M#SOL | 6616 | -0.032 | +1451.64€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 6616 | -0.032 | +1451.64€ | 3 | 14 |
| ✅ GBM_LATE_15M#XRP | 10645 | -0.028 | +3048.29€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 10645 | -0.028 | +3048.29€ | 4 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 50442 | +0.085 | +27846.35€ | 0 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 50442 | +0.085 | +27846.35€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 9741 | +0.001 | +4904.07€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 9741 | +0.001 | +4904.07€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 10787 | +0.009 | +2716.39€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 10787 | +0.009 | +2716.39€ | 0 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 6934 | +0.283 | +7588.65€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 6934 | +0.283 | +7588.65€ | 0 | 23 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 9306 | +0.013 | +2420.64€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 9306 | +0.013 | +2420.64€ | 1 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 7928 | +0.040 | +3323.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 7928 | +0.040 | +3323.94€ | 3 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 5746 | +0.309 | +6892.66€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 5746 | +0.309 | +6892.66€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 37463 | +0.180 | +30634.26€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 37463 | +0.180 | +30634.26€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 5664 | +0.236 | +5175.43€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 5664 | +0.236 | +5175.43€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 5886 | +0.148 | +4396.63€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 5886 | +0.148 | +4396.63€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 6028 | +0.221 | +5137.06€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 6028 | +0.221 | +5137.06€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 6374 | +0.137 | +4967.86€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 6374 | +0.137 | +4967.86€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 7057 | +0.123 | +5257.45€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 7057 | +0.123 | +5257.45€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 6454 | +0.228 | +5699.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 6454 | +0.228 | +5699.83€ | 0 | 27 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 10002 | +0.127 | +4851.82€ | 0 | 13 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 10002 | +0.127 | +4851.82€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 455 | +0.161 | +292.82€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 455 | +0.161 | +292.82€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 2877 | +0.134 | +1580.92€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 2877 | +0.134 | +1580.92€ | 0 | 16 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 476 | +0.153 | +248.05€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 476 | +0.153 | +248.05€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 3016 | +0.135 | +1443.04€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 3016 | +0.135 | +1443.04€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 2524 | +0.099 | +982.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 2524 | +0.099 | +982.16€ | 1 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 654 | +0.134 | +304.84€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 654 | +0.134 | +304.84€ | 0 | 26 |
| ✅ GBM_LATE_15M_TARDIO | 47547 | +0.185 | +38384.44€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#15min | 47547 | +0.185 | +38384.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 7505 | +0.246 | +7133.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 7505 | +0.246 | +7133.71€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 7468 | +0.144 | +5184.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 7468 | +0.144 | +5184.77€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 8042 | +0.232 | +7157.48€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 8042 | +0.232 | +7157.48€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 7856 | +0.138 | +5637.41€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 7856 | +0.138 | +5637.41€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 8454 | +0.118 | +5866.21€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 8454 | +0.118 | +5866.21€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 8222 | +0.234 | +7404.85€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 8222 | +0.234 | +7404.85€ | 0 | 22 |
| ✅ GBM_LATE_5M | 12625 | +0.205 | +10000.20€ | 1 | 29 |
| ✅ GBM_LATE_5M#5min | 12625 | +0.205 | +10000.20€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 1037 | +0.245 | +978.75€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 1037 | +0.245 | +978.75€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 3024 | +0.212 | +2635.86€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 3024 | +0.212 | +2635.86€ | 0 | 24 |
| ✅ GBM_LATE_5M#DOGE | 1216 | +0.197 | +905.95€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1216 | +0.197 | +905.95€ | 0 | 20 |
| ✅ GBM_LATE_5M#ETH | 3554 | +0.194 | +2520.49€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 3554 | +0.194 | +2520.49€ | 0 | 25 |
| ✅ GBM_LATE_5M#SOL | 1841 | +0.195 | +1429.66€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 1841 | +0.195 | +1429.66€ | 0 | 24 |
| ✅ GBM_LATE_5M#XRP | 1953 | +0.209 | +1529.48€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1953 | +0.209 | +1529.48€ | 0 | 0 |
| ✅ GBM_LATE_60M | 4027 | +0.059 | +1193.51€ | 0 | 7 |
| ✅ GBM_LATE_60M#60min | 4027 | +0.059 | +1193.51€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 1452 | +0.074 | +489.16€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 1452 | +0.074 | +489.16€ | 1 | 5 |
| ✅ GBM_LATE_60M#ETH | 1305 | +0.060 | +416.02€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 1305 | +0.060 | +416.02€ | 0 | 7 |
| ✅ GBM_LATE_60M#SOL | 1270 | +0.041 | +288.34€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 1270 | +0.041 | +288.34€ | 0 | 11 |
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
| ✅ LEADLAG_BTC_XRP_15M | 3772 | +0.100 | +905.48€ | 0 | 1 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 3772 | +0.100 | +905.48€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 3772 | +0.100 | +905.48€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 3772 | +0.100 | +905.48€ | 0 | 1 |
| ✅ LIQUIDACIONES_15M | 696 | -0.020 | -5.24€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 696 | -0.020 | -5.24€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 6 | -0.037 | -1.04€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 6 | -0.037 | -1.04€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 212 | -0.019 | +1.36€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 212 | -0.019 | +1.36€ | 1 | 0 |
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
| ✅ LIQUIDACIONES_60M | 1940 | -0.039 | -28.39€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1940 | -0.039 | -28.39€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 578 | -0.029 | -11.99€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 578 | -0.029 | -11.99€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 671 | -0.017 | +5.72€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 671 | -0.017 | +5.72€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 691 | -0.069 | -22.13€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 691 | -0.069 | -22.13€ | 6 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 10860 | -0.029 | -28.86€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 5184 | -0.034 | -66.42€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 5676 | -0.025 | +37.55€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 332 | -0.039 | -11.61€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 169 | -0.009 | +5.35€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 163 | -0.070 | -16.96€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 2791 | -0.017 | +42.69€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 1323 | -0.021 | +9.39€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 1468 | -0.014 | +33.30€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 1149 | -0.026 | +16.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 583 | -0.033 | -1.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 566 | -0.018 | +17.53€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 2411 | -0.040 | -68.86€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 1132 | -0.048 | -51.83€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 1279 | -0.033 | -17.04€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 2102 | -0.023 | +21.95€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 1013 | -0.030 | -2.71€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 55739 | -0.000 | +2852.82€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 55739 | -0.000 | +2852.82€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 10071 | +0.026 | +1297.12€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 10071 | +0.026 | +1297.12€ | 2 | 4 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 7947 | -0.035 | -134.11€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 7947 | -0.035 | -134.11€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 10191 | +0.024 | +1057.18€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 10191 | +0.024 | +1057.18€ | 1 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 7818 | -0.048 | -151.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 7818 | -0.048 | -151.97€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 9444 | -0.005 | +260.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 9444 | -0.005 | +260.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 10268 | +0.017 | +523.83€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 10268 | +0.017 | +523.83€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 6838 | -0.057 | -152.50€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 6838 | -0.057 | -152.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1235 | -0.002 | -17.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1235 | -0.002 | -17.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1860 | -0.072 | -38.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1860 | -0.072 | -38.20€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 63 | -0.038 | -1.68€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 63 | -0.038 | -1.68€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 787 | -0.120 | -34.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 787 | -0.120 | -34.24€ | 5 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 2035 | -0.071 | -35.13€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 2035 | -0.071 | -35.13€ | 2 | 0 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 137688 | -0.077 | +1747.98€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 137688 | -0.077 | +1747.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 24004 | -0.079 | +1270.40€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 24004 | -0.079 | +1270.40€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 20680 | -0.100 | -1033.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 20680 | -0.100 | -1033.55€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 24314 | -0.069 | +1191.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 24314 | -0.069 | +1191.49€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 20224 | -0.097 | -631.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 20224 | -0.097 | -631.42€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 24672 | -0.058 | +294.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 24672 | -0.058 | +294.75€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 23794 | -0.069 | +656.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 23794 | -0.069 | +656.31€ | 4 | 0 |
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
| ✅ ORDER_FLOW_5M_REACTIVO | 1695 | -0.018 | -32.20€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 1695 | -0.018 | -32.20€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 324 | -0.003 | +6.74€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 324 | -0.003 | +6.74€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 304 | -0.026 | -4.87€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 304 | -0.026 | -4.87€ | 0 | 0 |
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
| ✅ STRUCT_NO_15M | 10377 | +0.014 | -44.37€ | 2 | 0 |
| ✅ STRUCT_NO_15M#15min | 10377 | +0.014 | -44.37€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 4305 | +0.019 | -4.03€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 4305 | +0.019 | -4.03€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3623 | +0.010 | -28.56€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3623 | +0.010 | -28.56€ | 2 | 0 |
| ✅ STRUCT_NO_15M#SOL | 2449 | +0.010 | -11.78€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 2449 | +0.010 | -11.78€ | 1 | 0 |
| ✅ UPDOWN_GBM | 84448 | +0.055 | +7555.52€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 20610 | +0.083 | +4446.04€ | 0 | 11 |
| ✅ UPDOWN_GBM#240min | 2686 | +0.003 | +33.21€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 55794 | +0.053 | +2996.02€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 5055 | +0.004 | +86.28€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 6936 | +0.091 | +1107.27€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1576 | +0.156 | +698.08€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 77 | -0.006 | -0.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 5283 | +0.073 | +410.04€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 19198 | +0.057 | +1655.58€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 2798 | +0.086 | +654.09€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 744 | +0.005 | +14.25€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 13274 | +0.064 | +922.81€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 2273 | +0.001 | +62.74€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 109 | -0.077 | +1.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 8924 | +0.071 | +940.48€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1555 | +0.147 | +610.96€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 78 | +0.013 | -1.79€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 7291 | +0.055 | +331.31€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 19976 | +0.046 | +1336.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 5014 | +0.071 | +767.25€ | 0 | 10 |
| ✅ UPDOWN_GBM#ETH#240min | 717 | +0.008 | +18.67€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 12323 | +0.046 | +534.69€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 1820 | +0.005 | +14.52€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 102 | -0.106 | +1.55€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 18390 | +0.035 | +966.02€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 5270 | +0.035 | +418.14€ | 0 | 2 |
| ✅ UPDOWN_GBM#SOL#240min | 682 | -0.009 | +2.99€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 11386 | +0.041 | +543.29€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 962 | +0.005 | +9.03€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#daily | 90 | -0.141 | -7.42€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 11022 | +0.067 | +1551.32€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 4397 | +0.103 | +1297.51€ | 0 | 11 |
| ✅ UPDOWN_GBM#XRP#240min | 388 | +0.010 | -0.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 6237 | +0.045 | +253.88€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 301 | -0.107 | -4.19€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 899 | +0.365 | +326.37€ | 0 | 9 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 899 | +0.365 | +326.37€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 457 | +0.358 | +152.01€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 457 | +0.358 | +152.01€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 442 | +0.369 | +174.36€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 442 | +0.369 | +174.36€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO | 21153 | -0.023 | +5002.12€ | 3 | 8 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 21153 | -0.023 | +5002.12€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1718 | -0.056 | +502.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1718 | -0.056 | +502.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 3915 | -0.114 | +143.31€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 3915 | -0.114 | +143.31€ | 4 | 10 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 948 | +0.216 | +770.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 948 | +0.216 | +770.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 2719 | +0.220 | +1758.80€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 2719 | +0.220 | +1758.80€ | 1 | 21 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 6038 | -0.063 | +782.53€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 6038 | -0.063 | +782.53€ | 4 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 5815 | -0.064 | +1044.21€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 5815 | -0.064 | +1044.21€ | 4 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 258 | +0.061 | +24.94€ | 0 | 9 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 258 | +0.061 | +24.94€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 258 | +0.061 | +24.94€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 258 | +0.061 | +24.94€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1574 | +0.285 | +1311.40€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1574 | +0.285 | +1311.40€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 841 | +0.277 | +650.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 841 | +0.277 | +650.57€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 733 | +0.293 | +660.82€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 733 | +0.293 | +660.82€ | 0 | 9 |
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