# Hipótesis automáticas — 2026-10-25 04:17 UTC
_Generado por shadow_postmortem.py sobre 1044528 resoluciones (PNL=+137185.53€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.495` → IC=-0.255 (n=194)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.114 (n=630)

- **PATRÓN** `py_entrada` > `0.515` → IC=+0.228 (n=837)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.515 (IC base=+0.134)

- **PATRÓN** `n_total_lado` > `64.0` → IC=+0.180 (n=298)

  - _Acción_: Kelly boost +0.90€ cuando `n_total_lado` > 64.0 (IC base=+0.134)

- **PATRÓN** `banda_hit_calibrado` > `0.6183` → IC=+0.261 (n=588)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6183 (IC base=+0.134)

- **PATRÓN** `banda_z` > `9.008` → IC=+0.216 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.008 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.160 (n=324)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 17.0 (IC base=+0.134)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.140 (n=428)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 8.0 (IC base=+0.134)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.148 (n=961)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.134)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **PATRÓN** `py_entrada` > `0.515` → IC=+0.224 (n=726)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.515 (IC base=+0.139)

- **PATRÓN** `n_total_lado` > `68.0` → IC=+0.197 (n=252)

  - _Acción_: Kelly boost +0.98€ cuando `n_total_lado` > 68.0 (IC base=+0.139)

- **PATRÓN** `banda_hit_calibrado` > `0.6154` → IC=+0.256 (n=501)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6154 (IC base=+0.139)

- **PATRÓN** `banda_z` > `7.591` → IC=+0.191 (n=341)

  - _Acción_: Kelly boost +0.95€ cuando `banda_z` > 7.591 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.169 (n=273)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.143 (n=357)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 8.0 (IC base=+0.139)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.145 (n=862)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.139)

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
- **FILTRO** `restante_s_al_confirmar` < `140.86` → IC=-0.204 (n=10505)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 140.86
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=31516)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `127.62` → IC=-0.258 (n=1145)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 127.62
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=3438)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `120.62` → IC=-0.293 (n=1128)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 120.62
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=3391)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `166.52` → IC=-0.210 (n=2784)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 166.52
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=8355)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `134.14` → IC=-0.272 (n=2026)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 134.14
  - _Potencial_: sin este filtro IC_bueno=-0.084 (n=6080)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.214 (n=22861)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.107)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.129 (n=4491)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.01 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `8909.1861` → IC=+0.171 (n=2053)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 8909.1861 (IC base=+0.107)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.128 (n=19598)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.130 (n=35169)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 11.0 (IC base=+0.125)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.227 (n=18245)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.147 (n=7433)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.01 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `6949.3934` → IC=+0.156 (n=2874)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 6949.3934 (IC base=+0.125)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.194 (n=2077)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 5.0 (IC base=+0.188)

- **PATRÓN** `py_entrada` > `0.765` → IC=+0.364 (n=696)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.765 (IC base=+0.188)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.191 (n=2543)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.01 (IC base=+0.188)

- **PATRÓN** `libro_liquidez` > `16441.1339` → IC=+0.192 (n=660)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 16441.1339 (IC base=+0.188)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.187 (n=1817)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 7.0 (IC base=+0.181)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.185 (n=2032)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 17.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` < `0.285` → IC=+0.317 (n=895)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.285 (IC base=+0.181)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.183 (n=2603)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.01 (IC base=+0.181)

- **PATRÓN** `libro_liquidez` > `16243.2025` → IC=+0.185 (n=672)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 16243.2025 (IC base=+0.181)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.61` → IC=+0.171 (n=493)

  - _Acción_: Kelly boost +0.85€ cuando `py_entrada` > 0.61 (IC base=+0.080)

- **PATRÓN** `libro_liquidez` > `6694.8881` → IC=+0.149 (n=129)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 6694.8881 (IC base=+0.080)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.139 (n=1175)

  - _Acción_: Kelly boost +0.69€ cuando `py_entrada` < 0.44 (IC base=+0.083)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.167 (n=4442)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.161)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.162 (n=3763)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 15.0 (IC base=+0.161)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.378 (n=1418)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.161)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.216 (n=1984)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.208)

- **PATRÓN** `py_entrada` < `0.265` → IC=+0.349 (n=760)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.265 (IC base=+0.208)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.211 (n=2312)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.208)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.146 (n=1121)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.144)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.148 (n=956)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 15.0 (IC base=+0.144)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.262 (n=363)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.144)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.147 (n=883)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `2209.7061` → IC=+0.156 (n=486)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 2209.7061 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.162 (n=152)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.069)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.255 (n=875)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.226)

- **PATRÓN** `py_entrada` > `0.83` → IC=+0.421 (n=1207)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.83 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.150 (n=1313)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 7.0 (IC base=+0.147)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.154 (n=692)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 7.0 (IC base=+0.147)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.285 (n=646)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.147)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.149 (n=872)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.147)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.153 (n=145)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 18.0 (IC base=+0.106)

- **PATRÓN** `py_entrada` > `0.56` → IC=+0.191 (n=383)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.56 (IC base=+0.106)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.135 (n=1150)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 7.0 (IC base=+0.123)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.247 (n=413)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.123)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `11.0` → IC=-0.297 (n=62)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.229 (n=149)

- **FILTRO** `py_entrada` > `0.755` → IC=-0.293 (n=138)

  - _Acción_: SKIP cuando `py_entrada` > 0.755
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=73)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.205 (n=19459)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.200)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.202 (n=16509)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.234 (n=8019)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.200)

- **PATRÓN** `libro_liquidez` > `4837.3339` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4837.3339 (IC base=+0.200)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.182 (n=2123)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 15.0 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.180 (n=4455)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 18.0 (IC base=+0.179)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.183 (n=4372)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` < 0.73 (IC base=+0.179)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.180 (n=3674)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` > 0.71 (IC base=+0.179)

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

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.222 (n=2375)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.221)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.227 (n=1586)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.221)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.304 (n=810)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.221)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.186 (n=4394)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.182 (n=3739)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 15.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.180 (n=4579)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` < 0.73 (IC base=+0.180)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.188 (n=3439)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` > 0.71 (IC base=+0.180)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.257 (n=3796)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.248)

- **PATRÓN** `py_entrada` > `0.79` → IC=+0.362 (n=1255)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.192 (n=4307)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 5.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.194 (n=2752)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 11.0 (IC base=+0.189)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.194 (n=3190)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.71 (IC base=+0.189)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.431 (n=823)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.425)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.426 (n=710)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.425)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.438 (n=838)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.425)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.432 (n=868)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.425)

- **PATRÓN** `libro_liquidez` > `4242.86` → IC=+0.439 (n=536)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4242.86 (IC base=+0.425)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` < `11.0` → IC=+0.443 (n=225)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.435)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.447 (n=355)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.435)

- **PATRÓN** `libro_liquidez` > `20948.5418` → IC=+0.445 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 20948.5418 (IC base=+0.435)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.436 (n=328)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.430)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.429 (n=323)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.430)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.439 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.430)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.436 (n=360)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.430)

- **PATRÓN** `libro_liquidez` > `3609.5867` → IC=+0.444 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3609.5867 (IC base=+0.430)

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
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=11)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.224 (n=27)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.209 (n=25400)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.202)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.248 (n=25544)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.202)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.197 (n=3770)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 18.0 (IC base=+0.185)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.186 (n=8075)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 12.0 (IC base=+0.185)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.200 (n=11394)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.71 (IC base=+0.185)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.229 (n=5293)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.227 (n=5183)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.225)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.287 (n=3680)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.225)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.188 (n=4355)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 17.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.211 (n=5792)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.181)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.835` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.835
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.233 (n=3556)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.220)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.223 (n=4065)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.220)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.274 (n=3596)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.220)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.210 (n=3627)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.261 (n=3758)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.209 (n=4220)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.201 (n=4235)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.248 (n=4412)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.198)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.193 (n=9167)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.140 (n=9122)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.96 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `3.72` → IC=+0.137 (n=11065)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 3.72 (IC base=+0.116)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.197 (n=4529)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` < 0.38 (IC base=+0.119)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.142 (n=4656)

  - _Acción_: Kelly boost +0.71€ cuando `restante_min` > 4.95 (IC base=+0.119)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.128 (n=5545)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 7.0 (IC base=+0.119)

- **PATRÓN** `lag_apertura_s` < `2.71` → IC=+0.144 (n=4172)

  - _Acción_: Kelly boost +0.72€ cuando `lag_apertura_s` < 2.71 (IC base=+0.119)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.188 (n=4638)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` < 0.38 (IC base=+0.114)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.136 (n=4964)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.96 (IC base=+0.114)

- **PATRÓN** `lag_apertura_s` < `3.3` → IC=+0.136 (n=5559)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 3.3 (IC base=+0.114)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.312 (n=1167)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.292)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.384 (n=599)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.292)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.293 (n=525)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.279)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.359 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.279)

- **PATRÓN** `libro_liquidez` > `5057.5759` → IC=+0.284 (n=340)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5057.5759 (IC base=+0.279)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.325 (n=562)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.297)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.299 (n=821)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.297)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.393 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.297)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.298 (n=932)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.297)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.339 (n=85)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.340)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.372 (n=84)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.340)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.385 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.340)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.342 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.340)

- **PATRÓN** `libro_liquidez` > `761.0655` → IC=+0.371 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 761.0655 (IC base=+0.340)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.451 (n=265)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.442)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.443 (n=787)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.442)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.444 (n=554)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.442)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.443 (n=910)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.442)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.437 (n=381)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.434)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.435 (n=258)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.434)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.436 (n=388)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.434)

- **PATRÓN** `py_entrada` > `0.935` → IC=+0.440 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.935 (IC base=+0.434)

- **PATRÓN** `libro_liquidez` > `5384.9318` → IC=+0.444 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5384.9318 (IC base=+0.434)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.469 (n=129)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.451)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.454 (n=366)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.451)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.454 (n=343)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.451)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.453 (n=420)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.451)

- **PATRÓN** `libro_liquidez` > `1998.8822` → IC=+0.469 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1998.8822 (IC base=+0.451)

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
  - _Potencial_: sin este filtro IC_bueno=-0.207 (n=97)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.308 (n=24)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.198 (n=94)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.238 (n=59)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.205 (n=59)

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
  - _Potencial_: sin este filtro IC_bueno=-0.207 (n=97)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.308 (n=24)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.198 (n=94)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.238 (n=59)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.205 (n=59)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4728` → IC=+0.139 (n=14219)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.4728 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.124 (n=14363)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 6.0 (IC base=+0.121)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.125 (n=9912)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 12.0 (IC base=+0.121)

- **PATRÓN** `ibs_20min` > `0.3775` → IC=+0.165 (n=14219)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.3775 (IC base=+0.121)

- **PATRÓN** `dist_vwap_pct` > `0.7959` → IC=+0.277 (n=784)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7959 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.653` → IC=+0.181 (n=7080)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 3.653 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` < `1.2024` → IC=+0.259 (n=4150)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2024 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` > `0.6169` → IC=+0.265 (n=4149)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6169 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` > `0.3038` → IC=+0.240 (n=1455)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3038 (IC base=+0.121)

- **PATRÓN** `volumen_spike_ratio` > `2.3546` → IC=+0.230 (n=4599)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3546 (IC base=+0.121)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.125 (n=11701)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.02 (IC base=+0.121)

- **PATRÓN** `libro_liquidez` > `4693.9553` → IC=+0.148 (n=4740)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 4693.9553 (IC base=+0.121)

- **PATRÓN** `ibs_20min` < `0.5682` → IC=+0.142 (n=17562)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` < 0.5682 (IC base=+0.077)

- **PATRÓN** `dist_vwap_pct` > `0.6149` → IC=+0.189 (n=1154)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.6149 (IC base=+0.077)

- **PATRÓN** `volumen_regimen` < `0.6948` → IC=+0.190 (n=3046)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` < 0.6948 (IC base=+0.077)

- **PATRÓN** `volumen_regimen` > `1.0503` → IC=+0.180 (n=3139)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` > 1.0503 (IC base=+0.077)

- **PATRÓN** `volumen_pendiente_norm` > `0.2975` → IC=+0.233 (n=1725)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2975 (IC base=+0.077)

- **PATRÓN** `volumen_spike_ratio` > `2.6909` → IC=+0.208 (n=3922)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6909 (IC base=+0.077)

- **PATRÓN** `ballena_activa_n` < `106.0` → IC=+0.223 (n=11630)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 106.0 (IC base=+0.077)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.203 (n=1031)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.202)

- **PATRÓN** `drift_60min` |x|≤ `0.3485` → IC=+0.207 (n=3086)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3485 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.215 (n=1158)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.202)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.207 (n=2066)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.202)

- **PATRÓN** `ibs_20min` > `0.9831` → IC=+0.278 (n=1401)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9831 (IC base=+0.202)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.78` → IC=+0.280 (n=1359)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.78 (IC base=+0.202)

- **PATRÓN** `volumen_pendiente_norm` > `0.2836` → IC=+0.259 (n=401)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2836 (IC base=+0.202)

- **PATRÓN** `volumen_spike_ratio` > `1.4434` → IC=+0.205 (n=2947)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4434 (IC base=+0.202)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.217 (n=3325)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `2064.2` → IC=+0.208 (n=1028)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2064.2 (IC base=+0.202)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.220 (n=1855)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.202)

- **PATRÓN** `sigma_h` < `0.0089` → IC=+0.240 (n=2600)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0089 (IC base=+0.239)

- **PATRÓN** `sigma_h` > `0.008` → IC=+0.244 (n=1179)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.008 (IC base=+0.239)

- **PATRÓN** `drift_60min` |x|≤ `0.0875` → IC=+0.274 (n=869)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0875 (IC base=+0.239)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.254 (n=954)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.239)

- **PATRÓN** `ibs_20min` < `0.5357` → IC=+0.259 (n=2596)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5357 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` < `0.0959` → IC=+0.243 (n=2334)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0959 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` > `0.2932` → IC=+0.261 (n=358)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2932 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` < `1.4445` → IC=+0.244 (n=819)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4445 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` > `2.7122` → IC=+0.244 (n=819)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7122 (IC base=+0.239)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.242 (n=2933)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.239)

- **PATRÓN** `libro_liquidez` > `1582.26` → IC=+0.245 (n=2319)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1582.26 (IC base=+0.239)

- **PATRÓN** `ballena_activa_n` < `9.0` → IC=+0.242 (n=1176)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 9.0 (IC base=+0.239)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.239 (n=1123)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0032 (IC base=+0.228)

- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.231 (n=1151)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0051 (IC base=+0.228)

- **PATRÓN** `drift_60min` |x|≤ `0.1055` → IC=+0.257 (n=1117)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1055 (IC base=+0.228)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.240 (n=2655)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.228)

- **PATRÓN** `ibs_20min` > `0.943` → IC=+0.274 (n=846)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.943 (IC base=+0.228)

- **PATRÓN** `dist_vwap_pct` > `0.1873` → IC=+0.237 (n=1215)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1873 (IC base=+0.228)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.308` → IC=+0.270 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.308 (IC base=+0.228)

- **PATRÓN** `volumen_regimen` < `1.2292` → IC=+0.230 (n=2538)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2292 (IC base=+0.228)

- **PATRÓN** `volumen_regimen` > `0.6211` → IC=+0.232 (n=2538)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6211 (IC base=+0.228)

- **PATRÓN** `volumen_pendiente_norm` > `0.2783` → IC=+0.270 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2783 (IC base=+0.228)

- **PATRÓN** `volumen_spike_ratio` > `2.4426` → IC=+0.257 (n=834)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4426 (IC base=+0.228)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.150 (n=2632)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0058 (IC base=+0.132)

- **PATRÓN** `drift_60min` |x|≤ `0.0755` → IC=+0.166 (n=880)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.0755 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.157 (n=995)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 17.0 (IC base=+0.132)

- **PATRÓN** `ibs_20min` < `0.7231` → IC=+0.173 (n=2632)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.7231 (IC base=+0.132)

- **PATRÓN** `dist_vwap_pct` < `0.1349` → IC=+0.151 (n=2491)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.1349 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.992` → IC=+0.149 (n=426)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 10.992 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.119` → IC=+0.139 (n=2399)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` < 4.119 (IC base=+0.132)

- **PATRÓN** `volumen_regimen` < `1.2041` → IC=+0.141 (n=2632)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 1.2041 (IC base=+0.132)

- **PATRÓN** `volumen_pendiente_norm` > `0.1575` → IC=+0.163 (n=711)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` > 0.1575 (IC base=+0.132)

- **PATRÓN** `volumen_spike_ratio` < `2.4538` → IC=+0.142 (n=2512)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.4538 (IC base=+0.132)

- **PATRÓN** `volumen_spike_ratio` > `1.7966` → IC=+0.134 (n=1675)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 1.7966 (IC base=+0.132)

- **PATRÓN** `ballena_activa_n` < `212.0` → IC=+0.172 (n=1073)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 212.0 (IC base=+0.132)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0122` → IC=+0.221 (n=1073)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0122 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.199 (n=3373)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.193)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.267 (n=1236)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.184` → IC=+0.273 (n=684)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.184 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` < `0.0968` → IC=+0.200 (n=2858)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0968 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` > `0.3519` → IC=+0.212 (n=415)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3519 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` > `2.7115` → IC=+0.211 (n=1417)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7115 (IC base=+0.193)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.199 (n=3848)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.04 (IC base=+0.193)

- **PATRÓN** `libro_liquidez` > `1952.3598` → IC=+0.201 (n=1458)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1952.3598 (IC base=+0.193)

- **PATRÓN** `sigma_h` < `0.0107` → IC=+0.222 (n=2559)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0107 (IC base=+0.217)

- **PATRÓN** `drift_60min` |x|≤ `0.1771` → IC=+0.233 (n=1281)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1771 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.244 (n=1096)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.217)

- **PATRÓN** `ibs_20min` < `0.027` → IC=+0.274 (n=970)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.027 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.277` → IC=+0.260 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.277 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` > `0.3494` → IC=+0.263 (n=416)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3494 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` > `2.7408` → IC=+0.226 (n=1255)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7408 (IC base=+0.217)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.223 (n=1479)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.217)

- **PATRÓN** `libro_liquidez` > `1935.2234` → IC=+0.222 (n=1318)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1935.2234 (IC base=+0.217)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.220 (n=2405)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 22.0 (IC base=+0.217)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.144 (n=158)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.046 (n=3884)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.163 (n=571)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0037 (IC base=+0.055)

- **PATRÓN** `ibs_20min` > `0.9523` → IC=+0.232 (n=566)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9523 (IC base=+0.055)

- **PATRÓN** `dist_vwap_pct` > `0.1402` → IC=+0.334 (n=384)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1402 (IC base=+0.055)

- **PATRÓN** `dist_vwap_pct` < `0.3349` → IC=+0.329 (n=607)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3349 (IC base=+0.055)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.174` → IC=+0.193 (n=1221)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 5.174 (IC base=+0.055)

- **PATRÓN** `volumen_regimen` < `0.858` → IC=+0.331 (n=431)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.858 (IC base=+0.055)

- **PATRÓN** `volumen_regimen` > `1.2292` → IC=+0.353 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2292 (IC base=+0.055)

- **PATRÓN** `volumen_pendiente_norm` < `0.0777` → IC=+0.330 (n=416)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0777 (IC base=+0.055)

- **PATRÓN** `volumen_pendiente_norm` > `0.3024` → IC=+0.340 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3024 (IC base=+0.055)

- **PATRÓN** `volumen_spike_ratio` < `1.4123` → IC=+0.354 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4123 (IC base=+0.055)

- **PATRÓN** `ballena_activa_n` < `144.0` → IC=+0.333 (n=634)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 144.0 (IC base=+0.055)

- **PATRÓN** `ibs_20min` < `0.0929` → IC=+0.181 (n=1011)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.0929 (IC base=+0.038)

- **PATRÓN** `dist_vwap_pct` > `0.7361` → IC=+0.157 (n=228)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.7361 (IC base=+0.038)

- **PATRÓN** `volumen_regimen` < `0.8388` → IC=+0.150 (n=1218)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.8388 (IC base=+0.038)

- **PATRÓN** `volumen_regimen` > `1.1677` → IC=+0.137 (n=609)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` > 1.1677 (IC base=+0.038)

- **PATRÓN** `volumen_pendiente_norm` > `0.2847` → IC=+0.198 (n=240)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2847 (IC base=+0.038)

- **PATRÓN** `volumen_spike_ratio` < `1.7769` → IC=+0.140 (n=1170)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.7769 (IC base=+0.038)

- **PATRÓN** `volumen_spike_ratio` > `2.1637` → IC=+0.154 (n=795)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 2.1637 (IC base=+0.038)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.170 (n=110)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.066 (n=597)

- **FILTRO** `ibs_20min` > `0.2143` → IC=-0.133 (n=3809)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2143
  - _Potencial_: sin este filtro IC_bueno=+0.149 (n=1877)

- **FILTRO** `sigma_ewma_delta_pct` > `8.606` → IC=-0.232 (n=603)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.606
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=5083)

- **PATRÓN** `ibs_20min` > `0.7727` → IC=+0.179 (n=241)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.7727 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` > `1.0156` → IC=+0.282 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0156 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` < `0.4957` → IC=+0.264 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4957 (IC base=+0.029)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.383` → IC=+0.130 (n=249)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` > 2.383 (IC base=+0.029)

- **PATRÓN** `volumen_regimen` < `0.871` → IC=+0.264 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.871 (IC base=+0.029)

- **PATRÓN** `volumen_regimen` > `1.0359` → IC=+0.300 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0359 (IC base=+0.029)

- **PATRÓN** `volumen_pendiente_norm` < `0.1597` → IC=+0.277 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1597 (IC base=+0.029)

- **PATRÓN** `volumen_spike_ratio` < `2.4963` → IC=+0.291 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4963 (IC base=+0.029)

- **PATRÓN** `ibs_20min` < `0.2143` → IC=+0.149 (n=1877)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.2143 (IC base=-0.040)

- **PATRÓN** `dist_vwap_pct` > `0.2693` → IC=+0.277 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2693 (IC base=-0.040)

- **PATRÓN** `volumen_regimen` < `0.6963` → IC=+0.299 (n=347)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6963 (IC base=-0.040)

- **PATRÓN** `volumen_pendiente_norm` > `0.0801` → IC=+0.295 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0801 (IC base=-0.040)

- **PATRÓN** `volumen_spike_ratio` < `2.4396` → IC=+0.302 (n=724)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4396 (IC base=-0.040)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6038` → IC=-0.182 (n=1051)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6038
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=3157)

- **FILTRO** `ibs_20min` < `0.76` → IC=-0.153 (n=2776)

  - _Acción_: SKIP cuando `ibs_20min` < 0.76
  - _Potencial_: sin este filtro IC_bueno=+0.102 (n=1432)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.166 (n=1013)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=3195)

- **FILTRO** `ibs_20min` > `0.75` → IC=-0.204 (n=1500)

  - _Acción_: SKIP cuando `ibs_20min` > 0.75
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=4536)

- **PATRÓN** `dist_vwap_pct` > `1.0914` → IC=+0.347 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0914 (IC base=-0.066)

- **PATRÓN** `dist_vwap_pct` < `0.2464` → IC=+0.307 (n=652)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2464 (IC base=-0.066)

- **PATRÓN** `volumen_regimen` < `1.1432` → IC=+0.300 (n=748)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1432 (IC base=-0.066)

- **PATRÓN** `volumen_regimen` > `0.702` → IC=+0.319 (n=668)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.702 (IC base=-0.066)

- **PATRÓN** `volumen_pendiente_norm` < `0.1011` → IC=+0.306 (n=704)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1011 (IC base=-0.066)

- **PATRÓN** `volumen_spike_ratio` < `1.4195` → IC=+0.324 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4195 (IC base=-0.066)

- **PATRÓN** `volumen_spike_ratio` > `1.8466` → IC=+0.312 (n=483)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8466 (IC base=-0.066)

- **PATRÓN** `dist_vwap_pct` > `0.8239` → IC=+0.286 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8239 (IC base=-0.004)

- **PATRÓN** `volumen_regimen` < `0.7188` → IC=+0.265 (n=738)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7188 (IC base=-0.004)

- **PATRÓN** `volumen_regimen` > `1.0685` → IC=+0.287 (n=760)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0685 (IC base=-0.004)

- **PATRÓN** `volumen_pendiente_norm` > `0.1045` → IC=+0.291 (n=577)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1045 (IC base=-0.004)

- **PATRÓN** `volumen_spike_ratio` < `2.1836` → IC=+0.266 (n=1367)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1836 (IC base=-0.004)

- **PATRÓN** `volumen_spike_ratio` > `1.4309` → IC=+0.267 (n=1554)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4309 (IC base=-0.004)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.210 (n=6212)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0099 (IC base=+0.095)

- **PATRÓN** `ibs_20min` > `0.3143` → IC=+0.168 (n=18619)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` > 0.3143 (IC base=+0.095)

- **PATRÓN** `dist_vwap_pct` > `0.9561` → IC=+0.301 (n=1338)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9561 (IC base=+0.095)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.586` → IC=+0.164 (n=8353)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 3.586 (IC base=+0.095)

- **PATRÓN** `volumen_regimen` < `1.1694` → IC=+0.266 (n=6866)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1694 (IC base=+0.095)

- **PATRÓN** `volumen_regimen` > `0.6878` → IC=+0.271 (n=6135)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6878 (IC base=+0.095)

- **PATRÓN** `volumen_pendiente_norm` > `0.2401` → IC=+0.280 (n=2062)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2401 (IC base=+0.095)

- **PATRÓN** `volumen_spike_ratio` > `2.6583` → IC=+0.274 (n=3645)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6583 (IC base=+0.095)

- **PATRÓN** `ballena_activa_n` < `91.0` → IC=+0.299 (n=10512)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 91.0 (IC base=+0.095)

- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.156 (n=5998)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0094 (IC base=+0.075)

- **PATRÓN** `ibs_20min` < `0.6542` → IC=+0.145 (n=17965)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.6542 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` < `0.7028` → IC=+0.267 (n=2517)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7028 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` > `1.1967` → IC=+0.267 (n=1906)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1967 (IC base=+0.075)

- **PATRÓN** `volumen_pendiente_norm` > `0.2951` → IC=+0.319 (n=1236)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2951 (IC base=+0.075)

- **PATRÓN** `volumen_spike_ratio` < `1.5804` → IC=+0.292 (n=3638)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5804 (IC base=+0.075)

- **PATRÓN** `volumen_spike_ratio` > `2.2761` → IC=+0.287 (n=3748)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2761 (IC base=+0.075)

- **PATRÓN** `ballena_activa_n` < `76.0` → IC=+0.297 (n=8201)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 76.0 (IC base=+0.075)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.581` → IC=-0.141 (n=2543)

  - _Acción_: SKIP cuando `ibs_20min` < 0.581
  - _Potencial_: sin este filtro IC_bueno=+0.197 (n=2544)

- **FILTRO** `ibs_20min` > `0.7324` → IC=-0.216 (n=1085)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7324
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=3257)

- **FILTRO** `sigma_ewma_delta_pct` > `4.351` → IC=-0.215 (n=946)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.351
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=3396)

- **PATRÓN** `ibs_20min` > `0.9239` → IC=+0.323 (n=1272)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9239 (IC base=+0.028)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.944` → IC=+0.220 (n=908)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.944 (IC base=+0.028)

- **PATRÓN** `volumen_pendiente_norm` > `0.2302` → IC=+0.311 (n=331)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2302 (IC base=+0.028)

- **PATRÓN** `volumen_spike_ratio` < `1.4467` → IC=+0.258 (n=555)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4467 (IC base=+0.028)

- **PATRÓN** `volumen_spike_ratio` > `2.2732` → IC=+0.283 (n=755)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2732 (IC base=+0.028)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.292 (n=1152)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.028)

- **PATRÓN** `ibs_20min` < `0.1667` → IC=+0.161 (n=1086)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.1667 (IC base=-0.029)

- **PATRÓN** `volumen_pendiente_norm` < `0.0751` → IC=+0.416 (n=544)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0751 (IC base=-0.029)

- **PATRÓN** `volumen_spike_ratio` < `2.6803` → IC=+0.405 (n=621)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.6803 (IC base=-0.029)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.403 (n=575)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 20.0 (IC base=-0.029)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.1149` → IC=+0.215 (n=916)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1149 (IC base=+0.022)

- **PATRÓN** `volumen_regimen` < `1.1952` → IC=+0.198 (n=1825)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_regimen` < 1.1952 (IC base=+0.022)

- **PATRÓN** `volumen_regimen` > `0.6838` → IC=+0.203 (n=1631)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6838 (IC base=+0.022)

- **PATRÓN** `volumen_pendiente_norm` > `0.2783` → IC=+0.244 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2783 (IC base=+0.022)

- **PATRÓN** `volumen_spike_ratio` < `1.4274` → IC=+0.219 (n=600)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4274 (IC base=+0.022)

- **PATRÓN** `volumen_spike_ratio` > `2.4876` → IC=+0.196 (n=600)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.4876 (IC base=+0.022)

- **PATRÓN** `ballena_activa_n` < `270.0` → IC=+0.234 (n=1200)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 270.0 (IC base=+0.022)

- **PATRÓN** `dist_vwap_pct` < `0.1208` → IC=+0.238 (n=1221)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1208 (IC base=-0.002)

- **PATRÓN** `volumen_regimen` < `1.1702` → IC=+0.232 (n=1204)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1702 (IC base=-0.002)

- **PATRÓN** `volumen_regimen` > `0.6187` → IC=+0.236 (n=1204)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6187 (IC base=-0.002)

- **PATRÓN** `volumen_pendiente_norm` > `0.2721` → IC=+0.300 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2721 (IC base=-0.002)

- **PATRÓN** `volumen_spike_ratio` < `1.5377` → IC=+0.245 (n=508)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5377 (IC base=-0.002)

- **PATRÓN** `volumen_spike_ratio` > `2.1651` → IC=+0.254 (n=523)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1651 (IC base=-0.002)

- **PATRÓN** `ballena_activa_n` < `197.0` → IC=+0.247 (n=386)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 197.0 (IC base=-0.002)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0121` → IC=+0.314 (n=897)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0121 (IC base=+0.271)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.279 (n=2821)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.271)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.312 (n=1436)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.271)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.673` → IC=+0.302 (n=870)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.673 (IC base=+0.271)

- **PATRÓN** `volumen_pendiente_norm` < `0.098` → IC=+0.284 (n=2350)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.098 (IC base=+0.271)

- **PATRÓN** `volumen_spike_ratio` > `1.6063` → IC=+0.275 (n=2601)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6063 (IC base=+0.271)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.281 (n=3196)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.271)

- **PATRÓN** `libro_liquidez` > `2038.9984` → IC=+0.287 (n=896)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2038.9984 (IC base=+0.271)

- **PATRÓN** `ballena_activa_n` < `18.0` → IC=+0.291 (n=1639)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 18.0 (IC base=+0.271)

- **PATRÓN** `sigma_h` > `0.0086` → IC=+0.320 (n=1577)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0086 (IC base=+0.293)

- **PATRÓN** `drift_60min` |x|≤ `0.179` → IC=+0.314 (n=1039)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.179 (IC base=+0.293)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.322 (n=902)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.293)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.295 (n=821)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.293)

- **PATRÓN** `ibs_20min` < `0.3724` → IC=+0.295 (n=2360)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3724 (IC base=+0.293)

- **PATRÓN** `ibs_20min` > `0.2668` → IC=+0.300 (n=1070)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2668 (IC base=+0.293)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.44` → IC=+0.309 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.44 (IC base=+0.293)

- **PATRÓN** `volumen_pendiente_norm` < `0.1971` → IC=+0.293 (n=2313)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1971 (IC base=+0.293)

- **PATRÓN** `volumen_pendiente_norm` > `0.3423` → IC=+0.307 (n=377)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3423 (IC base=+0.293)

- **PATRÓN** `volumen_spike_ratio` < `1.7293` → IC=+0.298 (n=994)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7293 (IC base=+0.293)

- **PATRÓN** `volumen_spike_ratio` > `2.6876` → IC=+0.307 (n=1024)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6876 (IC base=+0.293)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.295 (n=1211)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.293)

- **PATRÓN** `libro_liquidez` > `1934.061` → IC=+0.308 (n=1070)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1934.061 (IC base=+0.293)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.296 (n=1497)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 17.0 (IC base=+0.293)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7367` → IC=-0.185 (n=1138)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7367
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=3417)

- **PATRÓN** `ibs_20min` > `0.8719` → IC=+0.167 (n=1092)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` > 0.8719 (IC base=+0.027)

- **PATRÓN** `dist_vwap_pct` > `0.1525` → IC=+0.235 (n=818)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1525 (IC base=+0.027)

- **PATRÓN** `dist_vwap_pct` < `0.2144` → IC=+0.226 (n=1339)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2144 (IC base=+0.027)

- **PATRÓN** `volumen_regimen` < `1.0082` → IC=+0.240 (n=1365)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0082 (IC base=+0.027)

- **PATRÓN** `volumen_regimen` > `0.667` → IC=+0.229 (n=1385)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.667 (IC base=+0.027)

- **PATRÓN** `volumen_pendiente_norm` < `0.1635` → IC=+0.233 (n=1637)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1635 (IC base=+0.027)

- **PATRÓN** `volumen_pendiente_norm` > `0.1024` → IC=+0.238 (n=498)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1024 (IC base=+0.027)

- **PATRÓN** `volumen_spike_ratio` < `2.4714` → IC=+0.236 (n=1501)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4714 (IC base=+0.027)

- **PATRÓN** `ballena_activa_n` < `120.0` → IC=+0.252 (n=1526)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 120.0 (IC base=+0.027)

- **PATRÓN** `volumen_regimen` < `1.1889` → IC=+0.242 (n=1064)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1889 (IC base=-0.000)

- **PATRÓN** `volumen_pendiente_norm` < `0.1012` → IC=+0.250 (n=983)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1012 (IC base=-0.000)

- **PATRÓN** `volumen_pendiente_norm` > `0.2829` → IC=+0.292 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2829 (IC base=-0.000)

- **PATRÓN** `volumen_spike_ratio` < `1.7947` → IC=+0.277 (n=675)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7947 (IC base=-0.000)

- **PATRÓN** `volumen_spike_ratio` > `2.4416` → IC=+0.259 (n=338)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4416 (IC base=-0.000)

- **PATRÓN** `ballena_activa_n` < `123.0` → IC=+0.263 (n=1026)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 123.0 (IC base=-0.000)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7576` → IC=-0.222 (n=1954)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7576
  - _Potencial_: sin este filtro IC_bueno=+0.309 (n=1954)

- **FILTRO** `ibs_20min` > `0.641` → IC=-0.231 (n=951)

  - _Acción_: SKIP cuando `ibs_20min` > 0.641
  - _Potencial_: sin este filtro IC_bueno=+0.124 (n=2854)

- **FILTRO** `sigma_ewma_delta_pct` > `8.436` → IC=-0.245 (n=441)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.436
  - _Potencial_: sin este filtro IC_bueno=+0.072 (n=3364)

- **PATRÓN** `ibs_20min` > `0.7576` → IC=+0.309 (n=1954)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7576 (IC base=+0.043)

- **PATRÓN** `dist_vwap_pct` > `0.213` → IC=+0.340 (n=852)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.213 (IC base=+0.043)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.422` → IC=+0.186 (n=613)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 9.422 (IC base=+0.043)

- **PATRÓN** `volumen_regimen` < `0.8453` → IC=+0.337 (n=972)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8453 (IC base=+0.043)

- **PATRÓN** `volumen_regimen` > `0.6986` → IC=+0.331 (n=1302)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6986 (IC base=+0.043)

- **PATRÓN** `volumen_pendiente_norm` < `0.1583` → IC=+0.328 (n=1506)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1583 (IC base=+0.043)

- **PATRÓN** `volumen_pendiente_norm` > `0.2741` → IC=+0.346 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2741 (IC base=+0.043)

- **PATRÓN** `volumen_spike_ratio` < `1.4413` → IC=+0.350 (n=473)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4413 (IC base=+0.043)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.344 (n=1263)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 48.0 (IC base=+0.043)

- **PATRÓN** `ibs_20min` < `0.641` → IC=+0.124 (n=2854)

  - _Acción_: Kelly boost +0.62€ cuando `ibs_20min` < 0.641 (IC base=+0.035)

- **PATRÓN** `volumen_regimen` < `0.6989` → IC=+0.270 (n=571)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6989 (IC base=+0.035)

- **PATRÓN** `volumen_pendiente_norm` < `0.1008` → IC=+0.243 (n=1230)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1008 (IC base=+0.035)

- **PATRÓN** `volumen_pendiente_norm` > `0.0762` → IC=+0.259 (n=495)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0762 (IC base=+0.035)

- **PATRÓN** `volumen_spike_ratio` < `2.4448` → IC=+0.250 (n=1248)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4448 (IC base=+0.035)

- **PATRÓN** `volumen_spike_ratio` > `1.5523` → IC=+0.242 (n=1115)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5523 (IC base=+0.035)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.271 (n=1268)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 51.0 (IC base=+0.035)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0161` → IC=+0.348 (n=1356)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0161 (IC base=+0.308)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.312 (n=790)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.308)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.317 (n=967)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.308)

- **PATRÓN** `ibs_20min` > `0.6604` → IC=+0.340 (n=2035)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6604 (IC base=+0.308)

- **PATRÓN** `dist_vwap_pct` > `0.2094` → IC=+0.333 (n=1141)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2094 (IC base=+0.308)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.856` → IC=+0.328 (n=987)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.856 (IC base=+0.308)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.14` → IC=+0.310 (n=2314)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 10.14 (IC base=+0.308)

- **PATRÓN** `volumen_regimen` > `0.6276` → IC=+0.317 (n=2034)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6276 (IC base=+0.308)

- **PATRÓN** `volumen_pendiente_norm` > `0.28` → IC=+0.348 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.28 (IC base=+0.308)

- **PATRÓN** `volumen_spike_ratio` > `1.4313` → IC=+0.320 (n=1951)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4313 (IC base=+0.308)

- **PATRÓN** `libro_liquidez` > `2959.7939` → IC=+0.309 (n=678)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2959.7939 (IC base=+0.308)

- **PATRÓN** `ballena_activa_n` < `41.0` → IC=+0.342 (n=1773)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 41.0 (IC base=+0.308)

- **PATRÓN** `sigma_h` > `0.0152` → IC=+0.340 (n=1437)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0152 (IC base=+0.308)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.319 (n=836)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.308)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.308 (n=1053)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.308)

- **PATRÓN** `ibs_20min` < `0.37` → IC=+0.331 (n=2154)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.37 (IC base=+0.308)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.619` → IC=+0.321 (n=798)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.619 (IC base=+0.308)

- **PATRÓN** `volumen_regimen` < `0.7188` → IC=+0.314 (n=948)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7188 (IC base=+0.308)

- **PATRÓN** `volumen_regimen` > `1.2266` → IC=+0.339 (n=718)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2266 (IC base=+0.308)

- **PATRÓN** `volumen_pendiente_norm` > `0.2851` → IC=+0.359 (n=297)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2851 (IC base=+0.308)

- **PATRÓN** `volumen_spike_ratio` < `1.4153` → IC=+0.319 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4153 (IC base=+0.308)

- **PATRÓN** `volumen_spike_ratio` > `2.1396` → IC=+0.312 (n=896)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1396 (IC base=+0.308)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0116` → IC=+0.224 (n=4601)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0116 (IC base=+0.179)

- **PATRÓN** `drift_60min` |x|≤ `0.0868` → IC=+0.200 (n=4595)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0868 (IC base=+0.179)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.188 (n=14274)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.179)

- **PATRÓN** `ibs_20min` > `0.5564` → IC=+0.234 (n=13782)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5564 (IC base=+0.179)

- **PATRÓN** `dist_vwap_pct` > `0.1633` → IC=+0.208 (n=5502)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1633 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.311` → IC=+0.257 (n=3604)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.311 (IC base=+0.179)

- **PATRÓN** `volumen_regimen` < `1.1852` → IC=+0.166 (n=9145)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.1852 (IC base=+0.179)

- **PATRÓN** `volumen_regimen` > `0.6212` → IC=+0.162 (n=9146)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 0.6212 (IC base=+0.179)

- **PATRÓN** `volumen_pendiente_norm` > `0.2936` → IC=+0.205 (n=1998)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2936 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` > `2.6129` → IC=+0.191 (n=4460)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 2.6129 (IC base=+0.179)

- **PATRÓN** `ballena_activa_n` < `92.0` → IC=+0.197 (n=12702)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 92.0 (IC base=+0.179)

- **PATRÓN** `sigma_h` < `0.0093` → IC=+0.184 (n=11701)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0093 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.0796` → IC=+0.226 (n=4430)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0796 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.212 (n=6303)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` < `0.508` → IC=+0.238 (n=13286)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.508 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.942` → IC=+0.198 (n=2155)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 9.942 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.659` → IC=+0.184 (n=11751)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` < 2.659 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` < `1.1829` → IC=+0.164 (n=9472)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.1829 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.2957` → IC=+0.227 (n=1977)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2957 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `2.6472` → IC=+0.190 (n=4174)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 2.6472 (IC base=+0.182)

- **PATRÓN** `ballena_activa_n` < `98.0` → IC=+0.194 (n=12265)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 98.0 (IC base=+0.182)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.231 (n=770)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.218)

- **PATRÓN** `drift_60min` |x|≤ `0.3335` → IC=+0.234 (n=2310)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3335 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.234 (n=862)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.224 (n=1561)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.218)

- **PATRÓN** `ibs_20min` > `0.931` → IC=+0.293 (n=1540)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.931 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.858` → IC=+0.328 (n=730)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.858 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` > `0.2811` → IC=+0.278 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2811 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` < `1.8447` → IC=+0.213 (n=1462)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8447 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` > `1.5423` → IC=+0.221 (n=1959)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5423 (IC base=+0.218)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.230 (n=2514)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.218)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.228 (n=1382)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.218)

- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.253 (n=1793)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0084 (IC base=+0.253)

- **PATRÓN** `sigma_h` > `0.0076` → IC=+0.267 (n=814)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0076 (IC base=+0.253)

- **PATRÓN** `drift_60min` |x|≤ `0.0663` → IC=+0.312 (n=598)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0663 (IC base=+0.253)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.258 (n=1847)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.253)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.255 (n=855)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.253)

- **PATRÓN** `ibs_20min` < `0.313` → IC=+0.278 (n=1577)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.313 (IC base=+0.253)

- **PATRÓN** `volumen_pendiente_norm` < `0.1008` → IC=+0.258 (n=1568)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1008 (IC base=+0.253)

- **PATRÓN** `volumen_pendiente_norm` > `0.3017` → IC=+0.284 (n=276)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3017 (IC base=+0.253)

- **PATRÓN** `volumen_spike_ratio` < `1.4424` → IC=+0.274 (n=568)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4424 (IC base=+0.253)

- **PATRÓN** `volumen_spike_ratio` > `2.7354` → IC=+0.259 (n=567)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7354 (IC base=+0.253)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.256 (n=2029)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.253)

- **PATRÓN** `libro_liquidez` > `1580.2976` → IC=+0.258 (n=1601)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1580.2976 (IC base=+0.253)

- **PATRÓN** `ballena_activa_n` < `9.0` → IC=+0.258 (n=751)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 9.0 (IC base=+0.253)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.214 (n=697)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.064` → IC=+0.195 (n=693)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.064 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.167 (n=2180)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` > `0.3257` → IC=+0.220 (n=2079)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3257 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` > `0.1871` → IC=+0.220 (n=1111)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1871 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.204` → IC=+0.222 (n=386)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.204 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` < `0.6912` → IC=+0.166 (n=915)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.6912 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.2816` → IC=+0.192 (n=329)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2816 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `1.4144` → IC=+0.173 (n=681)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 1.4144 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` > `2.4963` → IC=+0.166 (n=680)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 2.4963 (IC base=+0.151)

- **PATRÓN** `ballena_activa_n` < `417.0` → IC=+0.154 (n=2000)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 417.0 (IC base=+0.151)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.173 (n=2181)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0059 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.2345` → IC=+0.172 (n=1916)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.2345 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.188 (n=1040)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 15.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` < `0.6183` → IC=+0.207 (n=2176)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6183 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.405` → IC=+0.195 (n=415)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 11.405 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` < `1.204` → IC=+0.160 (n=2176)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.204 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` < `0.0699` → IC=+0.150 (n=1774)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` < 0.0699 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` > `0.1584` → IC=+0.148 (n=666)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.1584 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `2.4914` → IC=+0.153 (n=2056)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.4914 (IC base=+0.147)

- **PATRÓN** `ballena_activa_n` < `224.0` → IC=+0.181 (n=876)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 224.0 (IC base=+0.147)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0122` → IC=+0.237 (n=779)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0122 (IC base=+0.211)

- **PATRÓN** `drift_60min` |x|≤ `0.3954` → IC=+0.221 (n=2050)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3954 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.235 (n=856)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.300 (n=1213)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.325` → IC=+0.306 (n=540)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.325 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` < `0.0981` → IC=+0.213 (n=2011)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0981 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.352` → IC=+0.228 (n=332)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.352 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` < `1.766` → IC=+0.210 (n=996)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.766 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `2.7141` → IC=+0.225 (n=1026)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7141 (IC base=+0.211)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.216 (n=2782)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `1937.4308` → IC=+0.223 (n=1057)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1937.4308 (IC base=+0.211)

- **PATRÓN** `sigma_h` < `0.0115` → IC=+0.241 (n=2024)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0115 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.2465` → IC=+0.263 (n=1349)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2465 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.281 (n=769)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` < `0.0159` → IC=+0.298 (n=891)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0159 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.388` → IC=+0.277 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.388 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.3589` → IC=+0.287 (n=336)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3589 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` < `1.7523` → IC=+0.233 (n=853)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7523 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.1662` → IC=+0.238 (n=1291)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1662 (IC base=+0.234)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.234 (n=1055)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `1926.3032` → IC=+0.240 (n=917)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1926.3032 (IC base=+0.234)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.234 (n=1319)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.234)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.201 (n=987)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.0773` → IC=+0.204 (n=748)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0773 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.156 (n=2320)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 5.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` > `0.3022` → IC=+0.208 (n=2242)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3022 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` > `0.1426` → IC=+0.196 (n=1345)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.1426 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.706` → IC=+0.199 (n=513)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.706 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` < `1.0214` → IC=+0.153 (n=1973)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.0214 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` > `0.103` → IC=+0.174 (n=915)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.103 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `1.8256` → IC=+0.146 (n=1465)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.8256 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` > `2.5146` → IC=+0.168 (n=733)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 2.5146 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `7384.5777` → IC=+0.193 (n=1016)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 7384.5777 (IC base=+0.145)

- **PATRÓN** `ballena_activa_n` < `136.0` → IC=+0.152 (n=2185)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 136.0 (IC base=+0.145)

- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.155 (n=2365)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0072 (IC base=+0.128)

- **PATRÓN** `drift_60min` |x|≤ `0.3919` → IC=+0.144 (n=2365)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.3919 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.166 (n=1128)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 15.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` < `0.6819` → IC=+0.185 (n=2366)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.6819 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.607` → IC=+0.150 (n=581)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 9.607 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` < `0.8557` → IC=+0.155 (n=1577)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.8557 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` > `0.3001` → IC=+0.192 (n=361)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.3001 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` < `1.8106` → IC=+0.136 (n=1482)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.8106 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` > `2.5607` → IC=+0.134 (n=741)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 2.5607 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `6990.4137` → IC=+0.191 (n=1072)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 6990.4137 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `114.0` → IC=+0.133 (n=1924)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 114.0 (IC base=+0.128)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0105` → IC=+0.177 (n=1139)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.0105 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.166 (n=1200)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 15.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` > `0.4865` → IC=+0.215 (n=2514)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4865 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` > `0.1947` → IC=+0.192 (n=1434)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.1947 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.447` → IC=+0.282 (n=536)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.447 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `1.1691` → IC=+0.140 (n=2512)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 1.1691 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` < `0.1604` → IC=+0.131 (n=2558)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` < 0.1604 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `1.5438` → IC=+0.145 (n=1073)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.5438 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.129 (n=2618)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.02 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `2710.4123` → IC=+0.210 (n=1139)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2710.4123 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.151 (n=834)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 19.0 (IC base=+0.126)

- **PATRÓN** `sigma_h` < `0.0109` → IC=+0.142 (n=2580)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.0109 (IC base=+0.123)

- **PATRÓN** `drift_60min` |x|≤ `0.1094` → IC=+0.170 (n=861)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.1094 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.142 (n=2629)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 5.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` < `0.6111` → IC=+0.222 (n=2580)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6111 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.762` → IC=+0.130 (n=395)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` > 8.762 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.453` → IC=+0.137 (n=2275)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 2.453 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` < `1.1789` → IC=+0.130 (n=2578)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.1789 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` < `0.1648` → IC=+0.126 (n=2503)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` < 0.1648 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` > `0.2767` → IC=+0.151 (n=350)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.2767 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` < `1.4428` → IC=+0.129 (n=803)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 1.4428 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` > `2.4393` → IC=+0.139 (n=803)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 2.4393 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `2591.9948` → IC=+0.187 (n=1169)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 2591.9948 (IC base=+0.123)

- **PATRÓN** `ballena_activa_n` < `41.0` → IC=+0.130 (n=2110)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 41.0 (IC base=+0.123)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0131` → IC=+0.247 (n=2068)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0131 (IC base=+0.223)

- **PATRÓN** `drift_60min` |x|≤ `0.1721` → IC=+0.240 (n=1018)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1721 (IC base=+0.223)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.226 (n=2390)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.223)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.228 (n=2077)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.223)

- **PATRÓN** `ibs_20min` > `0.66` → IC=+0.258 (n=2321)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.66 (IC base=+0.223)

- **PATRÓN** `dist_vwap_pct` > `0.1826` → IC=+0.229 (n=1481)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1826 (IC base=+0.223)

- **PATRÓN** `dist_vwap_pct` < `0.4782` → IC=+0.224 (n=2083)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4782 (IC base=+0.223)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.655` → IC=+0.253 (n=1053)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.655 (IC base=+0.223)

- **PATRÓN** `volumen_regimen` < `1.1714` → IC=+0.225 (n=2314)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1714 (IC base=+0.223)

- **PATRÓN** `volumen_regimen` > `0.619` → IC=+0.232 (n=2313)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.619 (IC base=+0.223)

- **PATRÓN** `volumen_pendiente_norm` > `0.2308` → IC=+0.264 (n=434)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2308 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` < `2.4647` → IC=+0.228 (n=2254)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4647 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` > `1.8094` → IC=+0.230 (n=1502)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8094 (IC base=+0.223)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.225 (n=3012)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.223)

- **PATRÓN** `libro_liquidez` > `2570.8216` → IC=+0.227 (n=1542)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2570.8216 (IC base=+0.223)

- **PATRÓN** `sigma_h` < `0.0127` → IC=+0.234 (n=1037)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0127 (IC base=+0.232)

- **PATRÓN** `sigma_h` > `0.0226` → IC=+0.242 (n=1069)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0226 (IC base=+0.232)

- **PATRÓN** `drift_60min` |x|≤ `0.0876` → IC=+0.260 (n=786)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0876 (IC base=+0.232)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.252 (n=1149)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.232)

- **PATRÓN** `ibs_20min` < `0.43` → IC=+0.261 (n=2358)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.43 (IC base=+0.232)

- **PATRÓN** `dist_vwap_pct` > `0.3011` → IC=+0.243 (n=609)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3011 (IC base=+0.232)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.305` → IC=+0.265 (n=445)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.305 (IC base=+0.232)

- **PATRÓN** `volumen_regimen` < `0.8696` → IC=+0.232 (n=1571)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8696 (IC base=+0.232)

- **PATRÓN** `volumen_regimen` > `0.6399` → IC=+0.236 (n=2355)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6399 (IC base=+0.232)

- **PATRÓN** `volumen_pendiente_norm` > `0.2802` → IC=+0.288 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2802 (IC base=+0.232)

- **PATRÓN** `volumen_spike_ratio` < `2.5331` → IC=+0.227 (n=2199)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5331 (IC base=+0.232)

- **PATRÓN** `volumen_spike_ratio` > `1.4384` → IC=+0.235 (n=2199)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4384 (IC base=+0.232)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.232 (n=3049)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.232)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.206 (n=1537)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.183)

- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.192 (n=1168)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` > 0.0089 (IC base=+0.183)

- **PATRÓN** `drift_60min` |x|≤ `0.1295` → IC=+0.204 (n=1537)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1295 (IC base=+0.183)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.215 (n=1734)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.183)

- **PATRÓN** `ibs_20min` > `0.4878` → IC=+0.218 (n=3119)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4878 (IC base=+0.183)

- **PATRÓN** `dist_vwap_pct` > `0.7932` → IC=+0.206 (n=532)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7932 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.607` → IC=+0.213 (n=1508)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.607 (IC base=+0.183)

- **PATRÓN** `volumen_regimen` < `0.8609` → IC=+0.205 (n=2100)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8609 (IC base=+0.183)

- **PATRÓN** `volumen_pendiente_norm` > `0.0741` → IC=+0.190 (n=1403)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.0741 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` < `1.4274` → IC=+0.193 (n=1132)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 1.4274 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` > `2.4896` → IC=+0.186 (n=1132)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.4896 (IC base=+0.183)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.190 (n=3944)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.02 (IC base=+0.183)

- **PATRÓN** `libro_liquidez` > `2654.6046` → IC=+0.188 (n=3119)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 2654.6046 (IC base=+0.183)

- **PATRÓN** `ibs_20min` < `0.6008` → IC=+0.130 (n=3347)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` < 0.6008 (IC base=+0.082)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.209 (n=421)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.185)

- **PATRÓN** `drift_60min` |x|≤ `0.099` → IC=+0.237 (n=420)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.099 (IC base=+0.185)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.213 (n=870)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.185)

- **PATRÓN** `ibs_20min` > `0.6402` → IC=+0.242 (n=635)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6402 (IC base=+0.185)

- **PATRÓN** `dist_vwap_pct` > `0.3078` → IC=+0.204 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3078 (IC base=+0.185)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.073` → IC=+0.203 (n=409)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.073 (IC base=+0.185)

- **PATRÓN** `volumen_regimen` < `0.8753` → IC=+0.212 (n=636)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8753 (IC base=+0.185)

- **PATRÓN** `volumen_pendiente_norm` > `0.0712` → IC=+0.190 (n=378)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.0712 (IC base=+0.185)

- **PATRÓN** `volumen_spike_ratio` < `2.196` → IC=+0.195 (n=821)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 2.196 (IC base=+0.185)

- **PATRÓN** `libro_liquidez` > `14707.4695` → IC=+0.189 (n=635)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 14707.4695 (IC base=+0.185)

- **PATRÓN** `ballena_activa_n` < `161.0` → IC=+0.203 (n=409)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 161.0 (IC base=+0.185)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.126 (n=1154)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.63€ cuando `sigma_h` < 0.0057 (IC base=+0.100)

- **PATRÓN** `ibs_20min` < `0.6372` → IC=+0.151 (n=1014)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.6372 (IC base=+0.100)

- **PATRÓN** `volumen_pendiente_norm` > `0.1617` → IC=+0.155 (n=305)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` > 0.1617 (IC base=+0.100)

- **PATRÓN** `ballena_activa_n` < `160.0` → IC=+0.171 (n=494)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 160.0 (IC base=+0.100)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.241 (n=740)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.205)

- **PATRÓN** `drift_60min` |x|≤ `0.2091` → IC=+0.219 (n=741)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2091 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.220 (n=1158)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.205)

- **PATRÓN** `ibs_20min` > `0.3758` → IC=+0.247 (n=991)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3758 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` > `0.7901` → IC=+0.209 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7901 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` < `0.2061` → IC=+0.210 (n=991)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2061 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.898` → IC=+0.248 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.898 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` < `1.0194` → IC=+0.215 (n=976)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0194 (IC base=+0.205)

- **PATRÓN** `volumen_pendiente_norm` > `0.2687` → IC=+0.237 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2687 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` < `1.4263` → IC=+0.214 (n=365)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4263 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` > `1.7861` → IC=+0.217 (n=730)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7861 (IC base=+0.205)

- **PATRÓN** `ibs_20min` < `0.1105` → IC=+0.160 (n=369)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.1105 (IC base=+0.067)

- **PATRÓN** `libro_liquidez` > `5290.6382` → IC=+0.125 (n=737)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 5290.6382 (IC base=+0.067)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0109` → IC=+0.194 (n=292)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` > 0.0109 (IC base=+0.170)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.198 (n=783)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 8.0 (IC base=+0.170)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.276 (n=395)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.170)

- **PATRÓN** `dist_vwap_pct` > `0.9658` → IC=+0.247 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9658 (IC base=+0.170)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.095` → IC=+0.240 (n=364)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.095 (IC base=+0.170)

- **PATRÓN** `volumen_regimen` < `0.8875` → IC=+0.194 (n=580)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` < 0.8875 (IC base=+0.170)

- **PATRÓN** `volumen_regimen` > `0.7125` → IC=+0.176 (n=777)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 0.7125 (IC base=+0.170)

- **PATRÓN** `volumen_pendiente_norm` > `0.2299` → IC=+0.193 (n=164)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2299 (IC base=+0.170)

- **PATRÓN** `volumen_spike_ratio` < `1.427` → IC=+0.192 (n=280)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 1.427 (IC base=+0.170)

- **PATRÓN** `volumen_spike_ratio` > `2.1532` → IC=+0.174 (n=381)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 2.1532 (IC base=+0.170)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.182 (n=897)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.02 (IC base=+0.170)

- **PATRÓN** `libro_liquidez` > `3010.3049` → IC=+0.192 (n=290)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 3010.3049 (IC base=+0.170)

- **PATRÓN** `ibs_20min` < `0.5745` → IC=+0.124 (n=859)

  - _Acción_: Kelly boost +0.62€ cuando `ibs_20min` < 0.5745 (IC base=+0.046)

- **PATRÓN** `libro_liquidez` > `2628.7439` → IC=+0.145 (n=443)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 2628.7439 (IC base=+0.046)

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

- **PATRÓN** `sigma_h` > `0.0228` → IC=+0.175 (n=115)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.0228 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `10.0` → IC=+0.135 (n=176)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 10.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` < `0.61` → IC=+0.131 (n=253)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.61 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` > `1.1805` → IC=+0.322 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1805 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.17` → IC=+0.167 (n=67)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 5.17 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` < `0.9016` → IC=+0.134 (n=170)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 0.9016 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` > `1.064` → IC=+0.124 (n=115)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` > 1.064 (IC base=+0.117)

- **PATRÓN** `volumen_pendiente_norm` > `0.2383` → IC=+0.180 (n=48)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.2383 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` > `2.3392` → IC=+0.131 (n=109)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 2.3392 (IC base=+0.117)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.130 (n=233)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 19.0 (IC base=+0.117)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0117` → IC=+0.229 (n=5989)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0117 (IC base=+0.183)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.192 (n=18692)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 5.0 (IC base=+0.183)

- **PATRÓN** `ibs_20min` > `0.4444` → IC=+0.231 (n=17982)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4444 (IC base=+0.183)

- **PATRÓN** `dist_vwap_pct` > `0.901` → IC=+0.213 (n=2171)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.901 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.198` → IC=+0.254 (n=4383)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.198 (IC base=+0.183)

- **PATRÓN** `volumen_regimen` < `1.2192` → IC=+0.169 (n=12049)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 1.2192 (IC base=+0.183)

- **PATRÓN** `volumen_pendiente_norm` > `0.2408` → IC=+0.206 (n=3255)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2408 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` > `2.6204` → IC=+0.196 (n=5830)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.6204 (IC base=+0.183)

- **PATRÓN** `libro_liquidez` > `1755.041` → IC=+0.184 (n=17963)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 1755.041 (IC base=+0.183)

- **PATRÓN** `ballena_activa_n` < `71.0` → IC=+0.208 (n=14656)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 71.0 (IC base=+0.183)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.195 (n=7193)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0056 (IC base=+0.188)

- **PATRÓN** `drift_60min` |x|≤ `0.3755` → IC=+0.193 (n=14386)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.3755 (IC base=+0.188)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.211 (n=6092)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.188)

- **PATRÓN** `ibs_20min` < `0.5872` → IC=+0.242 (n=16349)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5872 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.76` → IC=+0.204 (n=2272)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.76 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.53` → IC=+0.192 (n=15821)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` < 3.53 (IC base=+0.188)

- **PATRÓN** `volumen_regimen` < `0.6318` → IC=+0.168 (n=3676)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 0.6318 (IC base=+0.188)

- **PATRÓN** `volumen_pendiente_norm` > `0.2916` → IC=+0.253 (n=2224)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2916 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` > `2.633` → IC=+0.200 (n=5171)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.633 (IC base=+0.188)

- **PATRÓN** `ballena_activa_n` < `39.0` → IC=+0.218 (n=10297)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 39.0 (IC base=+0.188)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.232 (n=976)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.227)

- **PATRÓN** `drift_60min` |x|≤ `0.3476` → IC=+0.230 (n=2923)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3476 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.241 (n=1420)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.227)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.231 (n=1969)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.227)

- **PATRÓN** `ibs_20min` > `0.9688` → IC=+0.322 (n=1326)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9688 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.32` → IC=+0.350 (n=686)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.32 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` > `0.2828` → IC=+0.292 (n=383)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2828 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` < `1.4494` → IC=+0.227 (n=938)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4494 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` > `2.2994` → IC=+0.238 (n=1275)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2994 (IC base=+0.227)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.245 (n=3136)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.227)

- **PATRÓN** `libro_liquidez` > `2061.8302` → IC=+0.231 (n=975)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2061.8302 (IC base=+0.227)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.252 (n=1774)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.227)

- **PATRÓN** `sigma_h` < `0.0088` → IC=+0.267 (n=2502)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0088 (IC base=+0.265)

- **PATRÓN** `sigma_h` > `0.008` → IC=+0.265 (n=1136)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.008 (IC base=+0.265)

- **PATRÓN** `drift_60min` |x|≤ `0.1182` → IC=+0.289 (n=1100)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1182 (IC base=+0.265)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.271 (n=2301)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.265)

- **PATRÓN** `ibs_20min` < `0.5159` → IC=+0.290 (n=2501)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5159 (IC base=+0.265)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.025` → IC=+0.267 (n=483)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.025 (IC base=+0.265)

- **PATRÓN** `volumen_pendiente_norm` < `0.0964` → IC=+0.268 (n=2249)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0964 (IC base=+0.265)

- **PATRÓN** `volumen_pendiente_norm` > `0.2905` → IC=+0.289 (n=353)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2905 (IC base=+0.265)

- **PATRÓN** `volumen_spike_ratio` < `1.5656` → IC=+0.268 (n=1046)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5656 (IC base=+0.265)

- **PATRÓN** `volumen_spike_ratio` > `2.6781` → IC=+0.280 (n=792)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6781 (IC base=+0.265)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.266 (n=2830)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.265)

- **PATRÓN** `libro_liquidez` > `1582.26` → IC=+0.269 (n=2233)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1582.26 (IC base=+0.265)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.274 (n=1091)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.265)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.200 (n=972)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.104` → IC=+0.165 (n=1283)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.104 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.161 (n=3034)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` > `0.2397` → IC=+0.201 (n=2913)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2397 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.1256` → IC=+0.195 (n=1480)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.1256 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.458` → IC=+0.163 (n=475)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 11.458 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.172` → IC=+0.151 (n=2548)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` < 3.172 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `0.6301` → IC=+0.179 (n=971)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 0.6301 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` < `0.0722` → IC=+0.153 (n=2598)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` < 0.0722 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.2726` → IC=+0.185 (n=420)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.2726 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `2.1781` → IC=+0.158 (n=2510)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.1781 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `1.5329` → IC=+0.154 (n=2549)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.5329 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `236.0` → IC=+0.184 (n=939)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 236.0 (IC base=+0.150)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.162 (n=2471)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0059 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.3233` → IC=+0.153 (n=2467)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.3233 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.170 (n=923)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` < `0.6928` → IC=+0.192 (n=2467)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.6928 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` < `0.1391` → IC=+0.159 (n=2344)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 0.1391 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.205` → IC=+0.159 (n=408)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 11.205 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.437` → IC=+0.142 (n=2482)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 6.437 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` < `1.1913` → IC=+0.152 (n=2467)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.1913 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` > `0.219` → IC=+0.206 (n=460)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.219 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` < `2.4323` → IC=+0.145 (n=2362)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 2.4323 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` > `1.7828` → IC=+0.150 (n=1574)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.7828 (IC base=+0.141)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.142 (n=3202)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.141)

- **PATRÓN** `ballena_activa_n` < `268.0` → IC=+0.153 (n=1005)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 268.0 (IC base=+0.141)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.257 (n=1000)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0125 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.233 (n=3126)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.225 (n=2676)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.303 (n=1119)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.242` → IC=+0.323 (n=641)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.242 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` < `0.1312` → IC=+0.228 (n=2808)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1312 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` > `1.6207` → IC=+0.230 (n=2911)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6207 (IC base=+0.224)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.231 (n=3572)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.224)

- **PATRÓN** `libro_liquidez` > `1950.3247` → IC=+0.237 (n=1357)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1950.3247 (IC base=+0.224)

- **PATRÓN** `sigma_h` < `0.0107` → IC=+0.245 (n=2485)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0107 (IC base=+0.240)

- **PATRÓN** `drift_60min` |x|≤ `0.1797` → IC=+0.260 (n=1244)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1797 (IC base=+0.240)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.264 (n=1067)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.240)

- **PATRÓN** `ibs_20min` < `0.0408` → IC=+0.305 (n=942)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0408 (IC base=+0.240)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.494` → IC=+0.298 (n=320)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.494 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` > `0.3469` → IC=+0.305 (n=413)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3469 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` > `2.1463` → IC=+0.250 (n=1796)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1463 (IC base=+0.240)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.246 (n=1451)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.240)

- **PATRÓN** `libro_liquidez` > `1930.6632` → IC=+0.252 (n=1280)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1930.6632 (IC base=+0.240)

- **PATRÓN** `ballena_activa_n` < `10.0` → IC=+0.253 (n=1190)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 10.0 (IC base=+0.240)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.203 (n=1033)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.4204` → IC=+0.158 (n=3089)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.4204 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.158 (n=3201)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 5.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` > `0.2418` → IC=+0.190 (n=3089)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.2418 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.1418` → IC=+0.171 (n=1610)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.1418 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.035` → IC=+0.160 (n=1397)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 3.035 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `1.0538` → IC=+0.158 (n=2718)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.0538 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.2333` → IC=+0.188 (n=546)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.2333 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `1.5241` → IC=+0.161 (n=1326)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 1.5241 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` > `2.1779` → IC=+0.154 (n=1367)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 2.1779 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `5667.9942` → IC=+0.235 (n=1401)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5667.9942 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `71.0` → IC=+0.169 (n=1304)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 71.0 (IC base=+0.146)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.153 (n=2578)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0075 (IC base=+0.130)

- **PATRÓN** `drift_60min` |x|≤ `0.4355` → IC=+0.139 (n=2577)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.4355 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.156 (n=941)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 17.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` < `0.7344` → IC=+0.185 (n=2577)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.7344 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.265` → IC=+0.156 (n=516)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 9.265 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.163` → IC=+0.132 (n=2239)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` < 3.163 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` < `0.6142` → IC=+0.148 (n=859)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.6142 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` > `0.2966` → IC=+0.217 (n=330)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2966 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` > `1.5395` → IC=+0.139 (n=2217)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 1.5395 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `6753.5393` → IC=+0.211 (n=859)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6753.5393 (IC base=+0.130)

- **PATRÓN** `ballena_activa_n` < `99.0` → IC=+0.132 (n=1678)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 99.0 (IC base=+0.130)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0105` → IC=+0.160 (n=1419)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0105 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.176 (n=1153)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` > `0.44` → IC=+0.200 (n=3119)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.44 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` > `1.0405` → IC=+0.209 (n=530)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0405 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.617` → IC=+0.263 (n=788)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.617 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` < `0.8801` → IC=+0.145 (n=2080)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.8801 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` < `0.1618` → IC=+0.125 (n=3247)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` < 0.1618 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` < `2.4831` → IC=+0.126 (n=3046)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 2.4831 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` > `2.1901` → IC=+0.123 (n=1381)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` > 2.1901 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.128 (n=3238)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.02 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `2751.2995` → IC=+0.243 (n=1040)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2751.2995 (IC base=+0.123)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.142 (n=1004)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 23.0 (IC base=+0.123)

- **PATRÓN** `sigma_h` < `0.0101` → IC=+0.153 (n=2606)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0101 (IC base=+0.117)

- **PATRÓN** `drift_60min` |x|≤ `0.1348` → IC=+0.152 (n=989)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.1348 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.129 (n=3047)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 5.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` < `0.6571` → IC=+0.212 (n=2960)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6571 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.224` → IC=+0.136 (n=2842)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 3.224 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` < `0.6405` → IC=+0.144 (n=987)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.6405 (IC base=+0.117)

- **PATRÓN** `volumen_pendiente_norm` > `0.2246` → IC=+0.169 (n=508)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` > 0.2246 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` < `1.4386` → IC=+0.149 (n=927)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.4386 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `2624.9762` → IC=+0.200 (n=986)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2624.9762 (IC base=+0.117)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.130 (n=2463)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 46.0 (IC base=+0.117)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0138` → IC=+0.255 (n=2619)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0138 (IC base=+0.233)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.238 (n=3052)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.233)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.238 (n=2114)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.233)

- **PATRÓN** `ibs_20min` > `0.6111` → IC=+0.273 (n=2618)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6111 (IC base=+0.233)

- **PATRÓN** `dist_vwap_pct` > `0.1917` → IC=+0.249 (n=1575)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1917 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.737` → IC=+0.271 (n=981)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.737 (IC base=+0.233)

- **PATRÓN** `volumen_regimen` < `1.2221` → IC=+0.239 (n=2930)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2221 (IC base=+0.233)

- **PATRÓN** `volumen_regimen` > `0.6398` → IC=+0.236 (n=2930)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6398 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` > `0.2348` → IC=+0.255 (n=503)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2348 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` > `1.5455` → IC=+0.240 (n=2551)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5455 (IC base=+0.233)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.235 (n=3805)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.233)

- **PATRÓN** `libro_liquidez` > `2945.8225` → IC=+0.238 (n=977)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2945.8225 (IC base=+0.233)

- **PATRÓN** `sigma_h` > `0.0256` → IC=+0.256 (n=1010)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0256 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.241 (n=2853)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` < `0.5156` → IC=+0.267 (n=3025)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5156 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.222` → IC=+0.273 (n=583)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.222 (IC base=+0.234)

- **PATRÓN** `volumen_regimen` > `1.227` → IC=+0.261 (n=1009)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.227 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.2827` → IC=+0.301 (n=406)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2827 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `1.4297` → IC=+0.237 (n=2821)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4297 (IC base=+0.234)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.232 (n=2752)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=+0.234)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.194 (n=5095)

- **PATRÓN** `sigma_h` < `0.005` → IC=+0.245 (n=1770)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.211)

- **PATRÓN** `drift_60min` |x|≤ `0.5067` → IC=+0.220 (n=5300)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5067 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.228 (n=1922)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` > `0.9412` → IC=+0.253 (n=1770)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9412 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` > `0.7009` → IC=+0.212 (n=929)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7009 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` < `0.4327` → IC=+0.213 (n=3777)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4327 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.941` → IC=+0.219 (n=877)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.941 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.58` → IC=+0.211 (n=4715)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.58 (IC base=+0.211)

- **PATRÓN** `volumen_regimen` < `0.7052` → IC=+0.224 (n=1690)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7052 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` < `0.1066` → IC=+0.212 (n=4954)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1066 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.1664` → IC=+0.219 (n=1493)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1664 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` < `1.4536` → IC=+0.219 (n=1740)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4536 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `1.8456` → IC=+0.211 (n=3478)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8456 (IC base=+0.211)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.215 (n=4035)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `3702.7882` → IC=+0.220 (n=3533)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3702.7882 (IC base=+0.211)

- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.240 (n=1281)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.193)

- **PATRÓN** `drift_60min` |x|≤ `0.3882` → IC=+0.213 (n=3373)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3882 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.211 (n=1290)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.211 (n=1704)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.193)

- **PATRÓN** `ibs_20min` < `0.187` → IC=+0.207 (n=1687)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.187 (IC base=+0.193)

- **PATRÓN** `dist_vwap_pct` > `0.6719` → IC=+0.201 (n=664)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6719 (IC base=+0.193)

- **PATRÓN** `dist_vwap_pct` < `0.2386` → IC=+0.190 (n=3506)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` < 0.2386 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.82` → IC=+0.203 (n=3443)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.82 (IC base=+0.193)

- **PATRÓN** `volumen_regimen` < `1.0948` → IC=+0.201 (n=3202)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0948 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` < `0.098` → IC=+0.196 (n=3517)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` < 0.098 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` > `0.2233` → IC=+0.200 (n=774)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2233 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` < `1.5352` → IC=+0.198 (n=1662)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.5352 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` > `1.8164` → IC=+0.200 (n=2517)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8164 (IC base=+0.193)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.194 (n=5095)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.01 (IC base=+0.193)

- **PATRÓN** `ballena_activa_n` < `68.0` → IC=+0.205 (n=2508)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 68.0 (IC base=+0.193)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.275 (n=683)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.261)

- **PATRÓN** `drift_60min` |x|≤ `0.0849` → IC=+0.293 (n=259)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0849 (IC base=+0.261)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.272 (n=301)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.261)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.262 (n=778)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.261)

- **PATRÓN** `ibs_20min` < `0.2533` → IC=+0.287 (n=341)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2533 (IC base=+0.261)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.054` → IC=+0.278 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.054 (IC base=+0.261)

- **PATRÓN** `volumen_regimen` < `1.2148` → IC=+0.268 (n=775)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2148 (IC base=+0.261)

- **PATRÓN** `volumen_regimen` > `0.8668` → IC=+0.271 (n=517)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8668 (IC base=+0.261)

- **PATRÓN** `volumen_pendiente_norm` > `0.2882` → IC=+0.354 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2882 (IC base=+0.261)

- **PATRÓN** `volumen_spike_ratio` < `1.8249` → IC=+0.270 (n=516)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8249 (IC base=+0.261)

- **PATRÓN** `libro_liquidez` > `16263.3319` → IC=+0.274 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16263.3319 (IC base=+0.261)

- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.253 (n=598)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0035 (IC base=+0.175)

- **PATRÓN** `drift_60min` |x|≤ `0.1108` → IC=+0.205 (n=591)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1108 (IC base=+0.175)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.217 (n=490)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.175)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.198 (n=491)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 5.0 (IC base=+0.175)

- **PATRÓN** `ibs_20min` < `0.144` → IC=+0.203 (n=591)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.144 (IC base=+0.175)

- **PATRÓN** `ibs_20min` > `0.6091` → IC=+0.175 (n=608)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` > 0.6091 (IC base=+0.175)

- **PATRÓN** `dist_vwap_pct` > `0.7013` → IC=+0.181 (n=117)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.7013 (IC base=+0.175)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.397` → IC=+0.195 (n=1323)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` < 6.397 (IC base=+0.175)

- **PATRÓN** `volumen_regimen` < `1.2212` → IC=+0.189 (n=1342)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 1.2212 (IC base=+0.175)

- **PATRÓN** `volumen_pendiente_norm` > `0.2207` → IC=+0.202 (n=270)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2207 (IC base=+0.175)

- **PATRÓN** `volumen_spike_ratio` < `2.5034` → IC=+0.182 (n=1334)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 2.5034 (IC base=+0.175)

- **PATRÓN** `volumen_spike_ratio` > `2.1703` → IC=+0.185 (n=605)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.1703 (IC base=+0.175)

- **PATRÓN** `libro_liquidez` > `14911.0423` → IC=+0.189 (n=608)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 14911.0423 (IC base=+0.175)

- **PATRÓN** `ballena_activa_n` < `692.0` → IC=+0.186 (n=1296)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 692.0 (IC base=+0.175)

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

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.197 (n=725)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 15.0 (IC base=+0.193)

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
- **PATRÓN** `sigma_h` < `0.007` → IC=+0.214 (n=1229)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.007 (IC base=+0.196)

- **PATRÓN** `drift_60min` |x|≤ `0.1477` → IC=+0.209 (n=614)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1477 (IC base=+0.196)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.215 (n=503)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.196)

- **PATRÓN** `ibs_20min` < `0.5174` → IC=+0.207 (n=930)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5174 (IC base=+0.196)

- **PATRÓN** `ibs_20min` > `0.7583` → IC=+0.199 (n=633)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7583 (IC base=+0.196)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.105` → IC=+0.204 (n=1255)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.105 (IC base=+0.196)

- **PATRÓN** `volumen_regimen` < `0.875` → IC=+0.200 (n=930)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.875 (IC base=+0.196)

- **PATRÓN** `volumen_regimen` > `1.2263` → IC=+0.202 (n=465)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2263 (IC base=+0.196)

- **PATRÓN** `volumen_pendiente_norm` > `0.1636` → IC=+0.196 (n=412)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.1636 (IC base=+0.196)

- **PATRÓN** `volumen_spike_ratio` < `2.1452` → IC=+0.203 (n=1201)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1452 (IC base=+0.196)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.196 (n=1430)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.01 (IC base=+0.196)

- **PATRÓN** `libro_liquidez` > `6255.2478` → IC=+0.196 (n=1394)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 6255.2478 (IC base=+0.196)

- **PATRÓN** `sigma_h` < `0.008` → IC=+0.206 (n=1144)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.008 (IC base=+0.188)

- **PATRÓN** `drift_60min` |x|≤ `0.3872` → IC=+0.218 (n=1006)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3872 (IC base=+0.188)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.202 (n=444)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.200 (n=765)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.188)

- **PATRÓN** `ibs_20min` < `0.4019` → IC=+0.194 (n=763)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.4019 (IC base=+0.188)

- **PATRÓN** `ibs_20min` > `0.6239` → IC=+0.195 (n=519)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 0.6239 (IC base=+0.188)

- **PATRÓN** `dist_vwap_pct` > `0.6573` → IC=+0.198 (n=200)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.6573 (IC base=+0.188)

- **PATRÓN** `volumen_regimen` < `1.2445` → IC=+0.200 (n=1144)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2445 (IC base=+0.188)

- **PATRÓN** `volumen_regimen` > `0.7208` → IC=+0.189 (n=1022)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` > 0.7208 (IC base=+0.188)

- **PATRÓN** `volumen_pendiente_norm` > `0.0744` → IC=+0.215 (n=482)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0744 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` < `2.1956` → IC=+0.196 (n=985)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 2.1956 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` > `1.7864` → IC=+0.194 (n=746)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 1.7864 (IC base=+0.188)

- **PATRÓN** `libro_liquidez` > `6625.754` → IC=+0.198 (n=1143)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 6625.754 (IC base=+0.188)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.011` → IC=+0.205 (n=690)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.011 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.208 (n=749)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` > `0.9219` → IC=+0.251 (n=356)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9219 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` > `0.7405` → IC=+0.240 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7405 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.204` → IC=+0.206 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.204 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `0.7016` → IC=+0.229 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7016 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` < `0.1062` → IC=+0.195 (n=706)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` < 0.1062 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` < `2.1551` → IC=+0.187 (n=669)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 2.1551 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `2.4815` → IC=+0.195 (n=254)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.4815 (IC base=+0.181)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.186 (n=915)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.02 (IC base=+0.181)

- **PATRÓN** `libro_liquidez` > `4300.4118` → IC=+0.227 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4300.4118 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.195 (n=771)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 52.0 (IC base=+0.181)

- **PATRÓN** `sigma_h` < `0.0094` → IC=+0.217 (n=387)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0094 (IC base=+0.206)

- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.208 (n=193)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0125 (IC base=+0.206)

- **PATRÓN** `drift_60min` |x|≤ `0.4982` → IC=+0.230 (n=509)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4982 (IC base=+0.206)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.242 (n=394)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 9.0 (IC base=+0.206)

- **PATRÓN** `ibs_20min` < `0.7308` → IC=+0.232 (n=580)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7308 (IC base=+0.206)

- **PATRÓN** `dist_vwap_pct` > `0.512` → IC=+0.212 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.512 (IC base=+0.206)

- **PATRÓN** `dist_vwap_pct` < `0.3065` → IC=+0.208 (n=488)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3065 (IC base=+0.206)

- **PATRÓN** `volumen_regimen` < `0.7555` → IC=+0.216 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7555 (IC base=+0.206)

- **PATRÓN** `volumen_regimen` > `0.9331` → IC=+0.211 (n=386)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.9331 (IC base=+0.206)

- **PATRÓN** `volumen_pendiente_norm` < `0.1071` → IC=+0.225 (n=503)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1071 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` > `2.2075` → IC=+0.239 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2075 (IC base=+0.206)

- **PATRÓN** `libro_liquidez` > `3011.3904` → IC=+0.226 (n=579)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3011.3904 (IC base=+0.206)

- **PATRÓN** `ballena_activa_n` < `29.0` → IC=+0.250 (n=386)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 29.0 (IC base=+0.206)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.153 (n=793)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0041 (IC base=+0.069)

- **PATRÓN** `ibs_20min` > `0.3889` → IC=+0.140 (n=1708)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` > 0.3889 (IC base=+0.069)

- **PATRÓN** `dist_vwap_pct` > `0.1457` → IC=+0.145 (n=877)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` > 0.1457 (IC base=+0.069)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.954` → IC=+0.153 (n=378)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 10.954 (IC base=+0.069)

- **PATRÓN** `volumen_pendiente_norm` > `0.2746` → IC=+0.146 (n=238)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` > 0.2746 (IC base=+0.069)

- **PATRÓN** `ibs_20min` < `0.0363` → IC=+0.266 (n=442)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0363 (IC base=+0.052)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.182` → IC=+0.173 (n=160)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 10.182 (IC base=+0.052)

- **PATRÓN** `volumen_pendiente_norm` > `0.1466` → IC=+0.154 (n=284)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` > 0.1466 (IC base=+0.052)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `ibs_20min` < `0.5136` → IC=-0.122 (n=247)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5136
  - _Potencial_: sin este filtro IC_bueno=+0.195 (n=503)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.133 (n=594)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.66€ cuando `sigma_h` < 0.0057 (IC base=+0.089)

- **PATRÓN** `ibs_20min` > `0.5136` → IC=+0.195 (n=503)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.5136 (IC base=+0.089)

- **PATRÓN** `dist_vwap_pct` > `0.1227` → IC=+0.168 (n=281)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.1227 (IC base=+0.089)

- **PATRÓN** `ibs_20min` < `0.0602` → IC=+0.278 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0602 (IC base=+0.064)

- **PATRÓN** `volumen_pendiente_norm` > `0.2162` → IC=+0.197 (n=87)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2162 (IC base=+0.064)

### GBM_LATE_60M#ETH#60min
- **PATRÓN** `sigma_h` < `0.006` → IC=+0.127 (n=516)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.64€ cuando `sigma_h` < 0.006 (IC base=+0.093)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.153 (n=220)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 17.0 (IC base=+0.093)

- **PATRÓN** `ibs_20min` > `0.4203` → IC=+0.173 (n=555)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` > 0.4203 (IC base=+0.093)

- **PATRÓN** `dist_vwap_pct` > `0.1247` → IC=+0.189 (n=281)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.1247 (IC base=+0.093)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.09` → IC=+0.234 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.09 (IC base=+0.093)

- **PATRÓN** `ibs_20min` < `0.1105` → IC=+0.238 (n=143)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1105 (IC base=+0.018)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.617` → IC=+0.237 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.617 (IC base=+0.018)

### GBM_LATE_60M#SOL#60min
- **PATRÓN** `ibs_20min` > `0.7302` → IC=+0.153 (n=393)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` > 0.7302 (IC base=+0.028)

- **PATRÓN** `dist_vwap_pct` > `0.73` → IC=+0.148 (n=140)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.73 (IC base=+0.028)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.166` → IC=+0.153 (n=125)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 9.166 (IC base=+0.028)

- **PATRÓN** `sigma_h` < `0.0109` → IC=+0.156 (n=274)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0109 (IC base=+0.075)

- **PATRÓN** `ibs_20min` < `0.1282` → IC=+0.227 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1282 (IC base=+0.075)

- **PATRÓN** `dist_vwap_pct` < `0.1599` → IC=+0.135 (n=236)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.1599 (IC base=+0.075)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.474` → IC=+0.338 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.474 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` > `1.0818` → IC=+0.199 (n=81)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_regimen` > 1.0818 (IC base=+0.075)

- **PATRÓN** `volumen_pendiente_norm` > `0.1508` → IC=+0.188 (n=75)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.1508 (IC base=+0.075)

- **PATRÓN** `volumen_spike_ratio` < `2.2044` → IC=+0.145 (n=195)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.2044 (IC base=+0.075)

- **PATRÓN** `volumen_spike_ratio` > `1.5118` → IC=+0.163 (n=197)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 1.5118 (IC base=+0.075)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.134 (n=225)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.06 (IC base=+0.075)

### GBM_LATE_60M_FADE
- **FILTRO** `sigma_h` < `0.0053` → IC=-0.238 (n=162)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0053
  - _Potencial_: sin este filtro IC_bueno=-0.171 (n=162)

- **FILTRO** `dist_vwap_pct` > `0.2334` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2334
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=307)

- **FILTRO** `volumen_regimen` < `0.7721` → IC=-0.295 (n=81)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7721
  - _Potencial_: sin este filtro IC_bueno=-0.173 (n=243)

- **FILTRO** `volumen_spike_ratio` > `2.7682` → IC=-0.203 (n=62)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.7682
  - _Potencial_: sin este filtro IC_bueno=-0.158 (n=188)

- **FILTRO** `libro_liquidez` < `903.6493` → IC=-0.211 (n=81)

  - _Acción_: SKIP cuando `libro_liquidez` < 903.6493
  - _Potencial_: sin este filtro IC_bueno=-0.202 (n=243)

- **FILTRO** `hora_utc` < `5.0` → IC=-0.307 (n=55)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.284 (n=225)

- **FILTRO** `ibs_20min` > `0.5429` → IC=-0.337 (n=139)

  - _Acción_: SKIP cuando `ibs_20min` > 0.5429
  - _Potencial_: sin este filtro IC_bueno=-0.241 (n=141)

- **FILTRO** `dist_vwap_pct` > `0.4614` → IC=-0.405 (n=19)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4614
  - _Potencial_: sin este filtro IC_bueno=-0.280 (n=261)

- **FILTRO** `sigma_ewma_delta_pct` > `10.358` → IC=-0.321 (n=26)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 10.358
  - _Potencial_: sin este filtro IC_bueno=-0.285 (n=254)

- **FILTRO** `volumen_pendiente_norm` > `0.0435` → IC=-0.382 (n=32)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0435
  - _Potencial_: sin este filtro IC_bueno=-0.274 (n=162)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.271 (n=46)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.173 (n=53)

- **FILTRO** `volumen_regimen` < `0.8402` → IC=-0.308 (n=24)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.8402
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=75)

- **FILTRO** `volumen_spike_ratio` > `3.276` → IC=-0.250 (n=18)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 3.276
  - _Potencial_: sin este filtro IC_bueno=-0.183 (n=58)

- **FILTRO** `sigma_h` > `0.0043` → IC=-0.318 (n=31)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0043
  - _Potencial_: sin este filtro IC_bueno=-0.235 (n=96)

- **FILTRO** `volumen_regimen` > `0.8276` → IC=-0.348 (n=31)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8276
  - _Potencial_: sin este filtro IC_bueno=-0.225 (n=96)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.5786` → IC=-0.466 (n=27)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5786
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=82)

- **FILTRO** `hora_utc` < `6.0` → IC=-0.375 (n=22)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.277 (n=83)

- **FILTRO** `ibs_20min` > `0.5241` → IC=-0.370 (n=52)

  - _Acción_: SKIP cuando `ibs_20min` > 0.5241
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=53)

- **FILTRO** `dist_vwap_pct` > `0.1224` → IC=-0.333 (n=28)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1224
  - _Potencial_: sin este filtro IC_bueno=-0.285 (n=77)

- **PATRÓN** `ibs_20min` > `0.9883` → IC=+0.200 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9883 (IC base=-0.158)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.400 (n=18)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.190 (n=98)

- **FILTRO** `dist_vwap_pct` > `0.0608` → IC=-0.250 (n=26)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.0608
  - _Potencial_: sin este filtro IC_bueno=-0.217 (n=90)

- **FILTRO** `volumen_spike_ratio` > `2.3459` → IC=-0.250 (n=30)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.3459
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=61)

- **FILTRO** `sigma_h` < `0.0099` → IC=-0.316 (n=36)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0099
  - _Potencial_: sin este filtro IC_bueno=-0.286 (n=12)

- **FILTRO** `hora_utc` > `11.0` → IC=-0.441 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.243 (n=33)

- **FILTRO** `dist_vwap_pct` < `0.2328` → IC=-0.352 (n=25)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.2328
  - _Potencial_: sin este filtro IC_bueno=-0.260 (n=23)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` > `0.1435` → IC=-0.120 (n=301)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1435
  - _Potencial_: sin este filtro IC_bueno=+0.142 (n=585)

- **PATRÓN** `sigma_h` > `0.0076` → IC=+0.186 (n=192)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0076 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.191 (n=221)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 17.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` > `0.6667` → IC=+0.159 (n=575)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` > 0.6667 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` > `0.5394` → IC=+0.238 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5394 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.589` → IC=+0.134 (n=129)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` > 10.589 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` < `0.6187` → IC=+0.180 (n=192)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 0.6187 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` < `0.0677` → IC=+0.153 (n=401)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` < 0.0677 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` < `1.5055` → IC=+0.175 (n=207)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 1.5055 (IC base=+0.118)

- **PATRÓN** `ibs_20min` < `0.1435` → IC=+0.142 (n=585)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` < 0.1435 (IC base=+0.053)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.069` → IC=+0.170 (n=195)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 9.069 (IC base=+0.053)

- **PATRÓN** `libro_liquidez` > `3247.8769` → IC=+0.129 (n=443)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 3247.8769 (IC base=+0.053)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.6991` → IC=-0.178 (n=57)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6991
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=174)

- **PATRÓN** `sigma_h` > `0.0035` → IC=+0.162 (n=208)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` > 0.0035 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.134 (n=211)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 12.0 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.150 (n=118)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 6.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` < `0.1684` → IC=+0.188 (n=312)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.1684 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` < `0.1038` → IC=+0.138 (n=318)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.1038 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.158` → IC=+0.147 (n=134)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 7.158 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` > `1.0304` → IC=+0.174 (n=142)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` > 1.0304 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` < `0.07` → IC=+0.137 (n=246)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_pendiente_norm` < 0.07 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` > `0.2687` → IC=+0.148 (n=52)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.2687 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` > `1.7963` → IC=+0.151 (n=187)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.7963 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `5390.0556` → IC=+0.143 (n=208)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 5390.0556 (IC base=+0.126)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `volumen_pendiente_norm` > `0.1263` → IC=-0.149 (n=35)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1263
  - _Potencial_: sin este filtro IC_bueno=+0.152 (n=182)

- **FILTRO** `ibs_20min` > `0.1696` → IC=-0.151 (n=107)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1696
  - _Potencial_: sin este filtro IC_bueno=+0.097 (n=209)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.122 (n=191)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0061 (IC base=+0.105)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.196 (n=67)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 18.0 (IC base=+0.105)

- **PATRÓN** `ibs_20min` > `0.8015` → IC=+0.147 (n=171)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` > 0.8015 (IC base=+0.105)

- **PATRÓN** `dist_vwap_pct` < `0.0908` → IC=+0.136 (n=160)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.0908 (IC base=+0.105)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.217` → IC=+0.140 (n=198)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` < 9.217 (IC base=+0.105)

- **PATRÓN** `volumen_regimen` < `0.6141` → IC=+0.182 (n=64)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 0.6141 (IC base=+0.105)

- **PATRÓN** `volumen_pendiente_norm` < `0.1263` → IC=+0.152 (n=182)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` < 0.1263 (IC base=+0.105)

- **PATRÓN** `volumen_spike_ratio` < `1.7943` → IC=+0.176 (n=109)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 1.7943 (IC base=+0.105)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.121 (n=159)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.01 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `1613.7381` → IC=+0.163 (n=191)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 1613.7381 (IC base=+0.105)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.906` → IC=+0.224 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.906 (IC base=+0.013)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.2391` → IC=-0.259 (n=52)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2391
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=103)

- **FILTRO** `dist_vwap_pct` > `0.1699` → IC=-0.150 (n=38)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1699
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=117)

- **PATRÓN** `sigma_h` > `0.0085` → IC=+0.286 (n=96)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0085 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.291 (n=151)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.227)

- **PATRÓN** `ibs_20min` > `0.6` → IC=+0.259 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6 (IC base=+0.227)

- **PATRÓN** `dist_vwap_pct` > `0.6667` → IC=+0.396 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6667 (IC base=+0.227)

- **PATRÓN** `dist_vwap_pct` < `0.2358` → IC=+0.226 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2358 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.152` → IC=+0.333 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.152 (IC base=+0.227)

- **PATRÓN** `volumen_regimen` < `0.7917` → IC=+0.278 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7917 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` > `0.0966` → IC=+0.287 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0966 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` < `1.4815` → IC=+0.359 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4815 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.418` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.418 (IC base=-0.060)

### LATE_WINDOW_5MIN
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.321 (n=76)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3447` → IC=+0.331 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3447 (IC base=+0.324)

- **PATRÓN** `elapsed_s` > `184.3` → IC=+0.392 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 184.3 (IC base=+0.324)

- **PATRÓN** `drift_15min` |x|≤ `1.0104` → IC=+0.457 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0104 (IC base=+0.324)

- **PATRÓN** `drift_60min` |x|≤ `0.9647` → IC=+0.392 (n=63)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9647 (IC base=+0.324)

- **PATRÓN** `ballena_activa_n` < `1071.0` → IC=+0.413 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1071.0 (IC base=+0.324)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3474` → IC=+0.269 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3474 (IC base=+0.237)

- **PATRÓN** `elapsed_s` > `182.9` → IC=+0.250 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 182.9 (IC base=+0.237)

- **PATRÓN** `elapsed_s` < `216.8` → IC=+0.250 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 216.8 (IC base=+0.237)

- **PATRÓN** `drift_15min` |x|≤ `2.3607` → IC=+0.297 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3607 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.6424` → IC=+0.296 (n=47)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6424 (IC base=+0.237)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.321 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.237)

- **PATRÓN** `ballena_activa_n` < `1854.0` → IC=+0.292 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1854.0 (IC base=+0.237)

### LATE_WINDOW_5MIN#BTC#5min
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.321 (n=76)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3447` → IC=+0.331 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3447 (IC base=+0.324)

- **PATRÓN** `elapsed_s` > `184.3` → IC=+0.392 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 184.3 (IC base=+0.324)

- **PATRÓN** `drift_15min` |x|≤ `1.0104` → IC=+0.457 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0104 (IC base=+0.324)

- **PATRÓN** `drift_60min` |x|≤ `0.9647` → IC=+0.392 (n=63)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9647 (IC base=+0.324)

- **PATRÓN** `ballena_activa_n` < `1071.0` → IC=+0.413 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1071.0 (IC base=+0.324)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3474` → IC=+0.269 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3474 (IC base=+0.237)

- **PATRÓN** `elapsed_s` > `182.9` → IC=+0.250 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 182.9 (IC base=+0.237)

- **PATRÓN** `elapsed_s` < `216.8` → IC=+0.250 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 216.8 (IC base=+0.237)

- **PATRÓN** `drift_15min` |x|≤ `2.3607` → IC=+0.297 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3607 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.6424` → IC=+0.296 (n=47)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6424 (IC base=+0.237)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.321 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.237)

- **PATRÓN** `ballena_activa_n` < `1854.0` → IC=+0.292 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1854.0 (IC base=+0.237)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `libro_liquidez` > `2925.8845` → IC=+0.133 (n=448)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 2925.8845 (IC base=+0.099)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `libro_liquidez` > `2925.8845` → IC=+0.133 (n=448)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 2925.8845 (IC base=+0.099)

### LIQUIDACIONES_15M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=204)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=203)

- **FILTRO** `libro_liquidez` < `5529.6254` → IC=-0.176 (n=109)

  - _Acción_: SKIP cuando `libro_liquidez` < 5529.6254
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=110)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=419)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `libro_liquidez` < `11321.3584` → IC=-0.167 (n=25)

  - _Acción_: SKIP cuando `libro_liquidez` < 11321.3584
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=76)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `ballena_activa_n` > `63.0` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `ballena_activa_n` > 63.0
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=9)

- **PATRÓN** `liq_n` > `5.0` → IC=+0.204 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `liq_n` > 5.0 (IC base=+0.056)

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
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=3639)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=108)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=65)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=108)

### LIQUIDACIONES_5M#BNB#5min
- **FILTRO** `hora_utc` > `14.0` → IC=-0.133 (n=47)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.104 (n=132)

### LIQUIDACIONES_5M#BTC#5min
- **FILTRO** `ballena_activa_n` > `558.0` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `ballena_activa_n` > 558.0
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=7)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=1382)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=1336)

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
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=438)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=419)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.143 (n=183)

  - _Acción_: Kelly boost +0.72€ cuando `py_entrada` < 0.495 (IC base=+0.020)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=873)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=873)

- **FILTRO** `py_entrada` < `0.44` → IC=-0.132 (n=275)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=678)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=906)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=906)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=229)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=229)

- **FILTRO** `hora_utc` > `12.0` → IC=-0.129 (n=68)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=176)

- **FILTRO** `py_entrada` < `0.43` → IC=-0.141 (n=76)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=168)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.183 (n=39)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=266)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=290)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=269)

- **FILTRO** `py_entrada` > `0.545` → IC=-0.120 (n=77)

  - _Acción_: SKIP cuando `py_entrada` > 0.545
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=252)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=360)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=360)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.120 (n=185)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=205)

- **FILTRO** `libro_liquidez` < `632.1854` → IC=-0.131 (n=128)

  - _Acción_: SKIP cuando `libro_liquidez` < 632.1854
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=262)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=272)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.129 (n=87)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=200)

### LIQUIDACIONES_DEPTH_FASE0#BNB#15min
- **FILTRO** `restante_min` < `10.75` → IC=-0.136 (n=20)

  - _Acción_: SKIP cuando `restante_min` < 10.75
  - _Potencial_: sin este filtro IC_bueno=+0.078 (n=43)

- **PATRÓN** `py_entrada` < `0.58` → IC=+0.122 (n=43)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` < 0.58 (IC base=+0.008)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `py_entrada` < `0.48` → IC=-0.129 (n=68)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.105 (n=36)

- **FILTRO** `py_entrada` > `0.58` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=27)

- **FILTRO** `restante_min` < `3.93` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `restante_min` < 3.93
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=17)

- **FILTRO** `lag_apertura_s` > `64.36` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `lag_apertura_s` > 64.36
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=17)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.5` → IC=+0.158 (n=217)

  - _Acción_: Kelly boost +0.79€ cuando `py_entrada` < 0.5 (IC base=+0.020)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.157 (n=65)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=300)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.122 (n=88)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=103)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **FILTRO** `py_entrada` < `0.41` → IC=-0.156 (n=123)

  - _Acción_: SKIP cuando `py_entrada` < 0.41
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=252)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.48` → IC=-0.125 (n=361)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=207)

- **FILTRO** `profundidad_ratio` < `43.4` → IC=-0.167 (n=142)

  - _Acción_: SKIP cuando `profundidad_ratio` < 43.4
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=426)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.188 (n=91)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=386)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.170 (n=98)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=437)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.132 (n=142)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=525)

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
- **FILTRO** `py_entrada` < `0.47` → IC=-0.164 (n=6541)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=19916)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.176 (n=6582)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=20624)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.192 (n=1176)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.116 (n=3671)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.175 (n=1130)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.068 (n=3717)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.139 (n=1279)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` > 1.0 (IC base=+0.041)

- **PATRÓN** `libro_liquidez` > `1140.7044` → IC=+0.138 (n=2424)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 1140.7044 (IC base=+0.041)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.127 (n=2267)

  - _Acción_: Kelly boost +0.64€ cuando `py_entrada` < 0.5 (IC base=+0.011)

- **PATRÓN** `libro_liquidez` > `1383.4252` → IC=+0.151 (n=1648)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 1383.4252 (IC base=+0.011)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.151 (n=921)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=2900)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.180 (n=938)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=2920)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` > `0.62` → IC=-0.203 (n=1160)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.078 (n=3799)

- **PATRÓN** `ibs_20min` > `0.9645` → IC=+0.130 (n=1648)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` > 0.9645 (IC base=+0.037)

- **PATRÓN** `libro_liquidez` > `1454.3594` → IC=+0.122 (n=2423)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 1454.3594 (IC base=+0.037)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.158 (n=1187)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.086 (n=3658)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=2407)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.162 (n=772)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=2331)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.189 (n=911)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=2756)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=3646)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` > `20.0` → IC=-0.146 (n=125)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 20.0
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=447)

- **FILTRO** `py_entrada` < `0.455` → IC=-0.257 (n=142)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=430)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.234 (n=287)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=947)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `py_entrada` < `0.395` → IC=-0.230 (n=72)

  - _Acción_: SKIP cuando `py_entrada` < 0.395
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=262)

- **FILTRO** `ibs_20min` < `0.1975` → IC=-0.223 (n=110)

  - _Acción_: SKIP cuando `ibs_20min` < 0.1975
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=224)

- **FILTRO** `hora_utc` < `9.0` → IC=-0.192 (n=144)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.096 (n=307)

- **FILTRO** `libro_liquidez` < `3742.1782` → IC=-0.170 (n=225)

  - _Acción_: SKIP cuando `libro_liquidez` < 3742.1782
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=226)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=943)

- **FILTRO** `libro_liquidez` < `1786.4389` → IC=-0.161 (n=240)

  - _Acción_: SKIP cuando `libro_liquidez` < 1786.4389
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=722)

- **FILTRO** `ibs_20min` > `0.8939` → IC=-0.131 (n=532)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8939
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=534)

- **FILTRO** `libro_liquidez` < `2096.2738` → IC=-0.169 (n=351)

  - _Acción_: SKIP cuando `libro_liquidez` < 2096.2738
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=715)

### MOMENTUM_IBS_15M_FADE#XRP#15min
- **FILTRO** `hora_utc` < `13.0` → IC=-0.238 (n=59)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 13.0
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=234)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.132 (n=18199)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=40655)

- **FILTRO** `py_entrada` < `0.33` → IC=-0.286 (n=14673)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=44181)

- **FILTRO** `ibs_7min` < `0.2332` → IC=-0.231 (n=14712)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2332
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=44142)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.153 (n=19326)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=39528)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.241 (n=18174)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=55695)

- **FILTRO** `ibs_7min` > `0.2857` → IC=-0.183 (n=18212)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2857
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=55657)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.150 (n=2566)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=7782)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.313 (n=2480)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=7868)

- **FILTRO** `ibs_7min` < `0.7133` → IC=-0.246 (n=3413)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7133
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=6935)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.148 (n=2584)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=7764)

- **FILTRO** `py_entrada` > `0.72` → IC=-0.273 (n=2998)

  - _Acción_: SKIP cuando `py_entrada` > 0.72
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=9806)

- **FILTRO** `ibs_7min` > `0.7692` → IC=-0.211 (n=3200)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7692
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=9604)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.128 (n=2379)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.096 (n=7499)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.264 (n=2332)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=7546)

- **FILTRO** `ibs_7min` < `0.7222` → IC=-0.201 (n=2469)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7222
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=7409)

- **FILTRO** `ballena_activa_n` > `155.0` → IC=-0.191 (n=2464)

  - _Acción_: SKIP cuando `ballena_activa_n` > 155.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=7414)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.260 (n=2477)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=7608)

- **FILTRO** `ibs_7min` > `0.266` → IC=-0.192 (n=2521)

  - _Acción_: SKIP cuando `ibs_7min` > 0.266
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=7564)

- **FILTRO** `ballena_activa_n` > `152.0` → IC=-0.181 (n=2501)

  - _Acción_: SKIP cuando `ballena_activa_n` > 152.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=7584)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.161 (n=2411)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=7410)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.312 (n=2429)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=7392)

- **FILTRO** `ibs_7min` < `0.2941` → IC=-0.247 (n=3238)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2941
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=6583)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.196 (n=2250)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=7571)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.257 (n=3175)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=10430)

- **FILTRO** `ibs_7min` > `0.7321` → IC=-0.177 (n=3401)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7321
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=10204)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.124 (n=3130)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.094 (n=6440)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.263 (n=2282)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=7288)

- **FILTRO** `ibs_7min` < `0.7241` → IC=-0.192 (n=2392)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7241
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=7178)

- **FILTRO** `ballena_activa_n` > `27.0` → IC=-0.192 (n=2316)

  - _Acción_: SKIP cuando `ballena_activa_n` > 27.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=7254)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.262 (n=2245)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=7694)

- **FILTRO** `ibs_7min` > `0.2745` → IC=-0.178 (n=2484)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2745
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=7455)

- **FILTRO** `ballena_activa_n` > `25.0` → IC=-0.173 (n=2480)

  - _Acción_: SKIP cuando `ballena_activa_n` > 25.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=7459)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.284 (n=2359)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=7234)

- **FILTRO** `ibs_7min` < `0.7143` → IC=-0.222 (n=3125)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7143
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=6468)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.219 (n=2296)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=7297)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.192 (n=3471)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=10636)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.32` → IC=-0.295 (n=2314)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=7330)

- **FILTRO** `ibs_7min` < `0.1944` → IC=-0.224 (n=2409)

  - _Acción_: SKIP cuando `ibs_7min` < 0.1944
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=7235)

- **FILTRO** `ballena_activa_n` > `9.0` → IC=-0.198 (n=2351)

  - _Acción_: SKIP cuando `ballena_activa_n` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=7293)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.222 (n=3263)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=10066)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1046` → IC=-0.135 (n=61)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1046
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=121)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `py_entrada` < `0.455` → IC=-0.158 (n=299)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=992)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=1276)

- **FILTRO** `py_entrada` > `0.545` → IC=-0.152 (n=156)

  - _Acción_: SKIP cuando `py_entrada` > 0.545
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=566)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=1458)

- **FILTRO** `py_entrada` > `0.565` → IC=-0.172 (n=260)

  - _Acción_: SKIP cuando `py_entrada` > 0.565
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=856)

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

- **FILTRO** `libro_liquidez` < `3257.9143` → IC=-0.156 (n=181)

  - _Acción_: SKIP cuando `libro_liquidez` < 3257.9143
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=543)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=389)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.3981` → IC=+0.138 (n=1238)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.69€ cuando `delta_ratio` |x|> 0.3981 (IC base=+0.130)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.136 (n=548)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 5.0 (IC base=+0.130)

- **PATRÓN** `total_vol_5m` < `437.4823` → IC=+0.160 (n=413)

  - _Acción_: Kelly boost +0.80€ cuando `total_vol_5m` < 437.4823 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `3556.2094` → IC=+0.148 (n=561)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 3556.2094 (IC base=+0.130)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.143 (n=427)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 11.0 (IC base=+0.130)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.4382` → IC=+0.146 (n=97)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.73€ cuando `delta_ratio` |x|> 0.4382 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.188 (n=139)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 14.0 (IC base=+0.138)

- **PATRÓN** `total_vol_5m` < `371.804` → IC=+0.147 (n=253)

  - _Acción_: Kelly boost +0.74€ cuando `total_vol_5m` < 371.804 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `2534.4132` → IC=+0.194 (n=96)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 2534.4132 (IC base=+0.138)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `delta_ratio` |x|> `0.3992` → IC=+0.130 (n=255)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.65€ cuando `delta_ratio` |x|> 0.3992 (IC base=+0.116)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.135 (n=228)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 14.0 (IC base=+0.116)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.127 (n=306)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.04 (IC base=+0.116)

- **PATRÓN** `libro_liquidez` > `2025.6726` → IC=+0.135 (n=228)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 2025.6726 (IC base=+0.116)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4161` → IC=+0.189 (n=162)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.95€ cuando `delta_ratio` |x|> 0.4161 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.178 (n=119)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 12.0 (IC base=+0.141)

- **PATRÓN** `total_vol_5m` < `384.1453` → IC=+0.225 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 384.1453 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `7586.8038` → IC=+0.146 (n=162)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 7586.8038 (IC base=+0.141)

- **PATRÓN** `ballena_activa_n` < `69.0` → IC=+0.196 (n=110)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 69.0 (IC base=+0.141)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.4324` → IC=+0.233 (n=99)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio` |x|> 0.4324 (IC base=+0.152)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.186 (n=103)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 6.0 (IC base=+0.152)

- **PATRÓN** `total_vol_5m` < `4858.013` → IC=+0.189 (n=146)

  - _Acción_: Kelly boost +0.95€ cuando `total_vol_5m` < 4858.013 (IC base=+0.152)

- **PATRÓN** `libro_liquidez` > `3171.8207` → IC=+0.175 (n=195)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 3171.8207 (IC base=+0.152)

- **PATRÓN** `ballena_activa_n` < `26.0` → IC=+0.162 (n=75)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 26.0 (IC base=+0.152)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `hora_utc` < `10.0` → IC=+0.138 (n=161)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 10.0 (IC base=+0.099)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.165 (n=153)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.01 (IC base=+0.099)

- **PATRÓN** `libro_liquidez` > `3564.823` → IC=+0.142 (n=107)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 3564.823 (IC base=+0.099)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `7.9794` → IC=-0.266 (n=45)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 7.9794
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=139)

- **FILTRO** `sigma_h` > `0.0073` → IC=-0.317 (n=173)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0073
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=523)

- **FILTRO** `T_h` > `129.5348` → IC=-0.191 (n=173)

  - _Acción_: SKIP cuando `T_h` > 129.5348
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=523)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.178 (n=175)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0036 (IC base=-0.080)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0072` → IC=-0.311 (n=51)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0072
  - _Potencial_: sin este filtro IC_bueno=+0.063 (n=156)

- **FILTRO** `T_h` > `87.9872` → IC=-0.255 (n=51)

  - _Acción_: SKIP cuando `T_h` > 87.9872
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=156)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.296 (n=52)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=-0.031)

- **PATRÓN** `pct_vs_K` |x|≤ `1.5815` → IC=+0.134 (n=69)

  - _Acción_: Kelly boost +0.67€ cuando `pct_vs_K` |x|≤ 1.5815 (IC base=-0.031)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `sigma_h` > `0.0062` → IC=-0.232 (n=39)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0062
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=25)

- **FILTRO** `pct_vs_K` |x|> `9.8932` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 9.8932
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=49)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0132` → IC=-0.258 (n=31)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0132
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=95)

- **FILTRO** `T_h` < `62.1856` → IC=-0.151 (n=41)

  - _Acción_: SKIP cuando `T_h` < 62.1856
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=85)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.206 (n=32)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=-0.102)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0095` → IC=-0.235 (n=420)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0095
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=219)

- **FILTRO** `T_h` > `109.3211` → IC=-0.210 (n=319)

  - _Acción_: SKIP cuando `T_h` > 109.3211
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=320)

- **FILTRO** `sigma_h` < `0.005` → IC=-0.234 (n=137)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.005
  - _Potencial_: sin este filtro IC_bueno=-0.213 (n=413)

- **FILTRO** `pct_vs_K` |x|> `2.8988` → IC=-0.404 (n=185)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.8988
  - _Potencial_: sin este filtro IC_bueno=-0.124 (n=365)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `pct_vs_K` |x|> `2.7768` → IC=-0.370 (n=52)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.7768
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=158)

- **FILTRO** `T_h` > `73.0783` → IC=-0.258 (n=147)

  - _Acción_: SKIP cuando `T_h` > 73.0783
  - _Potencial_: sin este filtro IC_bueno=-0.211 (n=50)

- **FILTRO** `pct_vs_K` |x|> `2.9616` → IC=-0.422 (n=49)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.9616
  - _Potencial_: sin este filtro IC_bueno=-0.187 (n=148)

### PRICE_TARGET_GBM_FADE#BTC#reach
- **FILTRO** `T_h` < `139.5329` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `T_h` < 139.5329
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

- **FILTRO** `sigma_h` < `0.0078` → IC=-0.262 (n=19)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0078
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=10)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `sigma_h` < `0.007` → IC=-0.287 (n=92)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.007
  - _Potencial_: sin este filtro IC_bueno=-0.213 (n=92)

- **FILTRO** `T_h` > `69.4221` → IC=-0.263 (n=137)

  - _Acción_: SKIP cuando `T_h` > 69.4221
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=47)

- **FILTRO** `sigma_h` > `0.0091` → IC=-0.364 (n=42)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0091
  - _Potencial_: sin este filtro IC_bueno=-0.114 (n=130)

- **FILTRO** `T_h` > `57.2342` → IC=-0.261 (n=115)

  - _Acción_: SKIP cuando `T_h` > 57.2342
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=57)

- **PATRÓN** `pct_vs_K` |x|≤ `0.7672` → IC=+0.174 (n=44)

  - _Acción_: Kelly boost +0.87€ cuando `pct_vs_K` |x|≤ 0.7672 (IC base=-0.178)

### PRICE_TARGET_GBM_FADE#ETH#reach
- **FILTRO** `T_h` < `145.7969` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `T_h` < 145.7969
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=6)

- **FILTRO** `sigma_h` < `0.0098` → IC=-0.206 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0098
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` < `0.008` → IC=-0.278 (n=43)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.008
  - _Potencial_: sin este filtro IC_bueno=-0.128 (n=135)

- **FILTRO** `T_h` > `71.5479` → IC=-0.196 (n=133)

  - _Acción_: SKIP cuando `T_h` > 71.5479
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=45)

- **FILTRO** `sigma_h` > `0.0152` → IC=-0.375 (n=30)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0152
  - _Potencial_: sin este filtro IC_bueno=-0.181 (n=92)

- **FILTRO** `sigma_h` < `0.0087` → IC=-0.286 (n=40)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0087
  - _Potencial_: sin este filtro IC_bueno=-0.202 (n=82)

- **FILTRO** `T_h` > `33.8406` → IC=-0.263 (n=91)

  - _Acción_: SKIP cuando `T_h` > 33.8406
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=31)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1224` → IC=+0.478 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1224 (IC base=+0.333)

- **PATRÓN** `sigma_h` < `0.0127` → IC=+0.356 (n=88)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0127 (IC base=+0.333)

- **PATRÓN** `T_h` > `0.7452` → IC=+0.382 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.7452 (IC base=+0.333)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.479 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.333)

- **PATRÓN** `edge` > `0.1005` → IC=+0.441 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1005 (IC base=+0.414)

- **PATRÓN** `sigma_h` > `0.0096` → IC=+0.443 (n=156)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0096 (IC base=+0.414)

- **PATRÓN** `T_h` < `0.608` → IC=+0.438 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.608 (IC base=+0.414)

- **PATRÓN** `dist_50` > `0.4975` → IC=+0.491 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4975 (IC base=+0.414)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.478 (n=137)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.414)

### RESOLUTION_SNIPER#BTC#sniper
- **PATRÓN** `edge` > `0.1506` → IC=+0.257 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1506 (IC base=+0.205)

- **PATRÓN** `sigma_h` < `0.0077` → IC=+0.281 (n=30)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0077 (IC base=+0.205)

- **PATRÓN** `dist_50` > `0.346` → IC=+0.284 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.346 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.281 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.205)

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
- **PATRÓN** `edge` > `0.1838` → IC=+0.484 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1838 (IC base=+0.430)

- **PATRÓN** `sigma_h` < `0.0154` → IC=+0.465 (n=55)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0154 (IC base=+0.430)

- **PATRÓN** `T_h` > `0.3968` → IC=+0.453 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.3968 (IC base=+0.430)

- **PATRÓN** `dist_50` > `0.3691` → IC=+0.465 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3691 (IC base=+0.430)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.439 (n=31)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.430)

- **PATRÓN** `edge` > `0.2005` → IC=+0.479 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.2005 (IC base=+0.466)

- **PATRÓN** `sigma_h` < `0.0156` → IC=+0.479 (n=143)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0156 (IC base=+0.466)

- **PATRÓN** `T_h` > `1.486` → IC=+0.481 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.486 (IC base=+0.466)

- **PATRÓN** `dist_50` > `0.4605` → IC=+0.492 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4605 (IC base=+0.466)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.473 (n=145)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.466)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=334)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.067 (n=402)

- **PATRÓN** `streak_estiramiento` < `0.3805` → IC=+0.128 (n=111)

  - _Acción_: Kelly boost +0.64€ cuando `streak_estiramiento` < 0.3805 (IC base=+0.007)

- **PATRÓN** `streak_estiramiento` < `0.835` → IC=+0.130 (n=271)

  - _Acción_: Kelly boost +0.65€ cuando `streak_estiramiento` < 0.835 (IC base=+0.053)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.131 (n=212)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 34.0 (IC base=+0.053)

- **PATRÓN** `libro_liquidez` > `2505.47` → IC=+0.140 (n=145)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 2505.47 (IC base=+0.053)

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
  - _Potencial_: sin este filtro IC_bueno=+0.119 (n=19)

### STREAK_FADE_15M#XRP#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.134 (n=129)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 7.0 (IC base=+0.096)

- **PATRÓN** `streak_estiramiento` < `0.4354` → IC=+0.188 (n=107)

  - _Acción_: Kelly boost +0.94€ cuando `streak_estiramiento` < 0.4354 (IC base=+0.096)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.175 (n=118)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 34.0 (IC base=+0.096)

- **PATRÓN** `libro_liquidez` > `2178.9765` → IC=+0.134 (n=140)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 2178.9765 (IC base=+0.096)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `9.0` → IC=-0.219 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=97)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.196 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=106)

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
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=1038)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=1335)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=1242)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=1273)

### STRUCT_NO_15M
- **FILTRO** `hora_utc` > `6.0` → IC=-0.156 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=13)

- **FILTRO** `py_entrada` < `0.455` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=28)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=4187)

### STRUCT_NO_15M#ETH#15min
- **FILTRO** `hora_utc` > `6.0` → IC=-0.156 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=13)

- **FILTRO** `py_entrada` < `0.455` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=28)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=2341)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.191 (n=1696)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0054 (IC base=+0.172)

- **PATRÓN** `sigma_h` > `0.0121` → IC=+0.188 (n=1285)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.0121 (IC base=+0.172)

- **PATRÓN** `drift_60min` |x|≤ `0.177` → IC=+0.188 (n=3392)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.177 (IC base=+0.172)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1911` → IC=+0.172 (n=1747)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.86€ cuando `delta_ratio_macro` |x|> 0.1911 (IC base=+0.172)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3486` → IC=+0.178 (n=3516)

  - _Acción_: Kelly boost +0.89€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3486 (IC base=+0.172)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.180 (n=3565)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 6.0 (IC base=+0.172)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.173 (n=3554)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 15.0 (IC base=+0.172)

- **PATRÓN** `ibs_15` > `0.5415` → IC=+0.245 (n=3855)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5415 (IC base=+0.172)

- **PATRÓN** `dist_vwap_pct` > `0.1291` → IC=+0.168 (n=1860)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.1291 (IC base=+0.172)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.328` → IC=+0.260 (n=992)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.328 (IC base=+0.172)

- **PATRÓN** `libro_liquidez` > `4610.2227` → IC=+0.188 (n=1285)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 4610.2227 (IC base=+0.172)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=1544)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.250 (n=290)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.0764` → IC=+0.257 (n=290)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0764 (IC base=+0.212)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2573` → IC=+0.242 (n=219)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2573 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.233 (n=687)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.212)

- **PATRÓN** `ibs_15` > `0.7193` → IC=+0.279 (n=658)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7193 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` > `0.1378` → IC=+0.230 (n=383)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1378 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.772` → IC=+0.296 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.772 (IC base=+0.212)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.215 (n=853)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `8349.505` → IC=+0.223 (n=658)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8349.505 (IC base=+0.212)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.186 (n=259)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0036 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.1507` → IC=+0.155 (n=683)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.1507 (IC base=+0.146)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1424` → IC=+0.155 (n=517)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.78€ cuando `delta_ratio_macro` |x|> 0.1424 (IC base=+0.146)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1262` → IC=+0.153 (n=309)

  - _Acción_: Kelly boost +0.76€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1262 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.154 (n=709)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 6.0 (IC base=+0.146)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.150 (n=806)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 17.0 (IC base=+0.146)

- **PATRÓN** `ibs_15` > `0.5211` → IC=+0.236 (n=776)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5211 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.1194` → IC=+0.162 (n=483)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 0.1194 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.521` → IC=+0.279 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.521 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `3217.3698` → IC=+0.152 (n=776)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 3217.3698 (IC base=+0.146)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `ibs_15` > `0.8831` → IC=+0.243 (n=305)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8831 (IC base=+0.086)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.133 (n=488)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.01 (IC base=+0.086)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `15.781` → IC=+0.140 (n=48)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 15.781 (IC base=+0.000)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0241` → IC=+0.228 (n=288)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0241 (IC base=+0.198)

- **PATRÓN** `drift_60min` |x|≤ `0.1304` → IC=+0.222 (n=576)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1304 (IC base=+0.198)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3415` → IC=+0.224 (n=765)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3415 (IC base=+0.198)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.198 (n=787)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 6.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.208 (n=772)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.198)

- **PATRÓN** `ibs_15` > `0.5294` → IC=+0.274 (n=864)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5294 (IC base=+0.198)

- **PATRÓN** `dist_vwap_pct` > `0.1291` → IC=+0.213 (n=489)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1291 (IC base=+0.198)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.324` → IC=+0.230 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.324 (IC base=+0.198)

- **PATRÓN** `libro_liquidez` > `2955.9488` → IC=+0.293 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2955.9488 (IC base=+0.198)

- **PATRÓN** `ibs_15` < `0.1089` → IC=+0.167 (n=793)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.83€ cuando `ibs_15` < 0.1089 (IC base=+0.070)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` > `0.0052` → IC=+0.391 (n=300)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0052 (IC base=+0.365)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1497` → IC=+0.382 (n=440)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1497 (IC base=+0.365)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1392` → IC=+0.390 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1392 (IC base=+0.365)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.377 (n=664)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.365)

- **PATRÓN** `ibs_15` > `0.788` → IC=+0.400 (n=660)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.788 (IC base=+0.365)

- **PATRÓN** `dist_vwap_pct` > `0.1523` → IC=+0.386 (n=383)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1523 (IC base=+0.365)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.219` → IC=+0.390 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.219 (IC base=+0.365)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.369 (n=802)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.365)

- **PATRÓN** `libro_liquidez` > `3851.736` → IC=+0.373 (n=590)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3851.736 (IC base=+0.365)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.363 (n=298)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.361)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.404 (n=113)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.361)

- **PATRÓN** `drift_60min` |x|≤ `0.0553` → IC=+0.370 (n=113)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0553 (IC base=+0.361)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2163` → IC=+0.377 (n=153)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2163 (IC base=+0.361)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1413` → IC=+0.396 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1413 (IC base=+0.361)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.377 (n=316)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.361)

- **PATRÓN** `ibs_15` > `0.8066` → IC=+0.388 (n=338)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8066 (IC base=+0.361)

- **PATRÓN** `dist_vwap_pct` > `0.1089` → IC=+0.378 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1089 (IC base=+0.361)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.255` → IC=+0.382 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.255 (IC base=+0.361)

- **PATRÓN** `libro_liquidez` > `8065.6565` → IC=+0.385 (n=338)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8065.6565 (IC base=+0.361)

- **PATRÓN** `ballena_activa_n` < `493.0` → IC=+0.403 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 493.0 (IC base=+0.361)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.375 (n=142)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.368)

- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.386 (n=147)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0058 (IC base=+0.368)

- **PATRÓN** `drift_60min` |x|≤ `0.1062` → IC=+0.367 (n=216)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1062 (IC base=+0.368)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0842` → IC=+0.383 (n=289)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0842 (IC base=+0.368)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2969` → IC=+0.385 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2969 (IC base=+0.368)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.392 (n=156)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.368)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.379 (n=147)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.368)

- **PATRÓN** `ibs_15` > `0.7504` → IC=+0.411 (n=323)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7504 (IC base=+0.368)

- **PATRÓN** `dist_vwap_pct` > `0.4613` → IC=+0.389 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4613 (IC base=+0.368)

- **PATRÓN** `dist_vwap_pct` < `0.2948` → IC=+0.370 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2948 (IC base=+0.368)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.356` → IC=+0.398 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.356 (IC base=+0.368)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.373 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.368)

- **PATRÓN** `libro_liquidez` > `4001.8474` → IC=+0.399 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4001.8474 (IC base=+0.368)

- **PATRÓN** `ballena_activa_n` < `153.0` → IC=+0.377 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 153.0 (IC base=+0.368)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0068` → IC=-0.175 (n=2254)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0068
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=2255)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.214 (n=1761)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=2748)

- **PATRÓN** `ibs_15` > `0.6332` → IC=+0.280 (n=1092)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6332 (IC base=-0.068)

- **PATRÓN** `dist_vwap_pct` > `0.1109` → IC=+0.208 (n=628)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1109 (IC base=-0.068)

- **PATRÓN** `dist_vwap_pct` < `0.2672` → IC=+0.197 (n=932)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` < 0.2672 (IC base=-0.068)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2301` → IC=+0.272 (n=1271)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2301 (IC base=-0.012)

- **PATRÓN** `ibs_15` < `0.3673` → IC=+0.283 (n=3808)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3673 (IC base=-0.012)

- **PATRÓN** `dist_vwap_pct` > `0.6607` → IC=+0.278 (n=498)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6607 (IC base=-0.012)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0341` → IC=-0.223 (n=2029)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0341
  - _Potencial_: sin este filtro IC_bueno=-0.102 (n=683)

- **FILTRO** `sigma_h` < `0.0035` → IC=-0.231 (n=678)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0035
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=2034)

- **FILTRO** `sigma_ewma_delta_pct` > `23.188` → IC=-0.267 (n=393)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 23.188
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=2319)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.168 (n=269)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0029 (IC base=+0.090)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1138` → IC=+0.267 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1138 (IC base=+0.090)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.125 (n=395)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 15.0 (IC base=+0.090)

- **PATRÓN** `ibs_15` > `0.7591` → IC=+0.330 (n=362)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7591 (IC base=+0.090)

- **PATRÓN** `dist_vwap_pct` > `0.1047` → IC=+0.284 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1047 (IC base=+0.090)

- **PATRÓN** `dist_vwap_pct` < `0.3695` → IC=+0.286 (n=372)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3695 (IC base=+0.090)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.276` → IC=+0.140 (n=234)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 19.276 (IC base=+0.090)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1053` → IC=+0.233 (n=58)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1053 (IC base=-0.193)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1404` → IC=+0.300 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1404 (IC base=-0.193)

- **PATRÓN** `ibs_15` < `0.6128` → IC=+0.321 (n=65)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.6128 (IC base=-0.193)

- **PATRÓN** `dist_vwap_pct` < `0.0415` → IC=+0.321 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0415 (IC base=-0.193)

- **PATRÓN** `ballena_activa_n` < `381.0` → IC=+0.303 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 381.0 (IC base=-0.193)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.161 (n=714)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.164 (n=483)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0058 (IC base=+0.153)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.163 (n=366)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` > 0.0049 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.0721` → IC=+0.189 (n=242)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.0721 (IC base=+0.153)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.296` → IC=+0.197 (n=423)

  - _Acción_: Kelly boost +0.98€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.296 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.173 (n=393)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 11.0 (IC base=+0.153)

- **PATRÓN** `ibs_15` > `0.5879` → IC=+0.248 (n=549)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5879 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` > `0.4682` → IC=+0.176 (n=143)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.4682 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` < `0.1597` → IC=+0.154 (n=431)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.1597 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.379` → IC=+0.252 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.379 (IC base=+0.153)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.161 (n=714)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.01 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `9584.2249` → IC=+0.154 (n=183)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 9584.2249 (IC base=+0.153)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.254 (n=946)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.246)

- **PATRÓN** `drift_15min` |x|≤ `0.7706` → IC=+0.260 (n=1249)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7706 (IC base=+0.246)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1551` → IC=+0.265 (n=946)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1551 (IC base=+0.246)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.249 (n=524)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.246)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.248 (n=1258)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.246)

- **PATRÓN** `ibs_15` < `0.3777` → IC=+0.278 (n=1419)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3777 (IC base=+0.246)

- **PATRÓN** `dist_vwap_pct` > `0.1544` → IC=+0.263 (n=520)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1544 (IC base=+0.246)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.392` → IC=+0.254 (n=631)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.392 (IC base=+0.246)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.448` → IC=+0.251 (n=1480)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.448 (IC base=+0.246)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1485` → IC=-0.230 (n=353)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1485
  - _Potencial_: sin este filtro IC_bueno=-0.168 (n=687)

- **FILTRO** `sigma_h` > `0.0106` → IC=-0.232 (n=259)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0106
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=781)

- **FILTRO** `drift_60min` |x|> `0.1729` → IC=-0.251 (n=352)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1729
  - _Potencial_: sin este filtro IC_bueno=-0.157 (n=688)

- **FILTRO** `drift_15min` |x|> `0.888` → IC=-0.282 (n=259)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.888
  - _Potencial_: sin este filtro IC_bueno=-0.158 (n=781)

- **FILTRO** `sigma_ewma_delta_pct` > `17.738` → IC=-0.147 (n=545)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 17.738
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=4346)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1478` → IC=+0.181 (n=45)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.90€ cuando `delta_ratio_macro` |x|> 0.1478 (IC base=-0.189)

- **PATRÓN** `ibs_15` > `0.5625` → IC=+0.234 (n=62)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5625 (IC base=-0.189)

- **PATRÓN** `dist_vwap_pct` < `0.1292` → IC=+0.167 (n=52)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.1292 (IC base=-0.189)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.233 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=-0.189)

- **PATRÓN** `ibs_15` < `0.3793` → IC=+0.290 (n=630)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3793 (IC base=-0.038)

- **PATRÓN** `dist_vwap_pct` < `0.2588` → IC=+0.236 (n=590)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2588 (IC base=-0.038)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0197` → IC=-0.253 (n=617)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0197
  - _Potencial_: sin este filtro IC_bueno=-0.168 (n=618)

- **FILTRO** `drift_15min` |x|> `0.7503` → IC=-0.250 (n=617)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.7503
  - _Potencial_: sin este filtro IC_bueno=-0.171 (n=618)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.211)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.211)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0695` → IC=+0.277 (n=796)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0695 (IC base=-0.025)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1174` → IC=+0.295 (n=388)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1174 (IC base=-0.025)

- **PATRÓN** `ibs_15` < `0.137` → IC=+0.317 (n=595)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.137 (IC base=-0.025)

- **PATRÓN** `dist_vwap_pct` > `0.786` → IC=+0.353 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.786 (IC base=-0.025)

### UPDOWN_GBM_ETH_15M_HORA7
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.237 (n=17)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.096)

- **PATRÓN** `drift_60min` |x|≤ `0.1798` → IC=+0.139 (n=34)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.1798 (IC base=+0.096)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.235` → IC=+0.220 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.235 (IC base=+0.096)

- **PATRÓN** `ibs_15` > `0.8489` → IC=+0.342 (n=17)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8489 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` < `0.1025` → IC=+0.200 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1025 (IC base=+0.096)

- **PATRÓN** `ballena_activa_n` < `102.0` → IC=+0.156 (n=30)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 102.0 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` > `0.198` → IC=+0.121 (n=64)

  - _Acción_: Kelly boost +0.61€ cuando `dist_vwap_pct` > 0.198 (IC base=+0.048)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.237 (n=17)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.096)

- **PATRÓN** `drift_60min` |x|≤ `0.1798` → IC=+0.139 (n=34)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.1798 (IC base=+0.096)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.235` → IC=+0.220 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.235 (IC base=+0.096)

- **PATRÓN** `ibs_15` > `0.8489` → IC=+0.342 (n=17)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8489 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` < `0.1025` → IC=+0.200 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1025 (IC base=+0.096)

- **PATRÓN** `ballena_activa_n` < `102.0` → IC=+0.156 (n=30)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 102.0 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` > `0.198` → IC=+0.121 (n=64)

  - _Acción_: Kelly boost +0.61€ cuando `dist_vwap_pct` > 0.198 (IC base=+0.048)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.300 (n=383)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.290)

- **PATRÓN** `drift_60min` |x|≤ `0.0541` → IC=+0.323 (n=383)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0541 (IC base=+0.290)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1466` → IC=+0.295 (n=764)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1466 (IC base=+0.290)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2242` → IC=+0.301 (n=688)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2242 (IC base=+0.290)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.306 (n=1189)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.290)

- **PATRÓN** `ibs_15` > `0.8389` → IC=+0.319 (n=1147)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8389 (IC base=+0.290)

- **PATRÓN** `dist_vwap_pct` > `0.2684` → IC=+0.324 (n=493)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2684 (IC base=+0.290)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.52` → IC=+0.379 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.52 (IC base=+0.290)

- **PATRÓN** `libro_liquidez` > `12101.5966` → IC=+0.308 (n=520)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12101.5966 (IC base=+0.290)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.312 (n=205)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.284)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.304 (n=279)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.284)

- **PATRÓN** `drift_60min` |x|≤ `0.0585` → IC=+0.321 (n=205)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0585 (IC base=+0.284)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2616` → IC=+0.302 (n=205)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2616 (IC base=+0.284)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3877` → IC=+0.290 (n=541)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3877 (IC base=+0.284)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.305 (n=643)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.284)

- **PATRÓN** `ibs_15` > `0.829` → IC=+0.308 (n=614)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.829 (IC base=+0.284)

- **PATRÓN** `dist_vwap_pct` > `0.2546` → IC=+0.326 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2546 (IC base=+0.284)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.589` → IC=+0.378 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.589 (IC base=+0.284)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.285 (n=794)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.284)

- **PATRÓN** `libro_liquidez` > `16113.4131` → IC=+0.331 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16113.4131 (IC base=+0.284)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.304 (n=534)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.295)

- **PATRÓN** `drift_60min` |x|≤ `0.0523` → IC=+0.322 (n=178)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0523 (IC base=+0.295)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0665` → IC=+0.298 (n=534)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0665 (IC base=+0.295)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3048` → IC=+0.311 (n=431)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3048 (IC base=+0.295)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.312 (n=514)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.295)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.297 (n=482)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.295)

- **PATRÓN** `ibs_15` > `0.8494` → IC=+0.327 (n=534)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8494 (IC base=+0.295)

- **PATRÓN** `dist_vwap_pct` > `0.2815` → IC=+0.323 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2815 (IC base=+0.295)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.52` → IC=+0.375 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.52 (IC base=+0.295)

### UPDOWN_OU_5M
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1232` → IC=-0.155 (n=85)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1232
  - _Potencial_: sin este filtro IC_bueno=-0.099 (n=260)

- **FILTRO** `ballena_activa_n` > `42.0` → IC=-0.136 (n=234)

  - _Acción_: SKIP cuando `ballena_activa_n` > 42.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=79)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.1228` → IC=-0.211 (n=119)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1228
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=365)

- **FILTRO** `sigma_h` > `0.007` → IC=-0.180 (n=120)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.007
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=364)

- **FILTRO** `drift_15min` |x|> `0.4386` → IC=-0.151 (n=164)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.4386
  - _Potencial_: sin este filtro IC_bueno=-0.090 (n=320)

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
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=151)

- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.2377` → IC=-0.125 (n=94)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.2377
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=95)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.2021` → IC=-0.250 (n=26)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2021
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=27)

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
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1371` → IC=-0.167 (n=19)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1371
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=39)

- **FILTRO** `drift_15min` |x|> `0.1605` → IC=-0.340 (n=23)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.1605
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.075` → IC=-0.278 (n=25)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.075
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=13)

- **FILTRO** `sigma_h` < `0.0051` → IC=-0.250 (n=18)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0051
  - _Potencial_: sin este filtro IC_bueno=-0.159 (n=39)

- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.0863` → IC=-0.204 (n=25)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.0863
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
- **PATRÓN** `T_h` > `87.7391` → IC=+0.192 (n=508)

  - _Acción_: Kelly boost +0.96€ cuando `T_h` > 87.7391 (IC base=+0.185)

- **PATRÓN** `ratio` < `0.973` → IC=+0.408 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.973 (IC base=+0.185)

- **PATRÓN** `T_h` > `115.2222` → IC=+0.354 (n=2331)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 115.2222 (IC base=+0.337)

- **PATRÓN** `ratio` > `1.0229` → IC=+0.378 (n=374)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0229 (IC base=+0.337)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `109.5528` → IC=+0.176 (n=211)

  - _Acción_: Kelly boost +0.88€ cuando `T_h` > 109.5528 (IC base=+0.152)

- **PATRÓN** `ratio` < `0.9839` → IC=+0.318 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9839 (IC base=+0.152)

- **PATRÓN** `T_h` > `111.9836` → IC=+0.307 (n=808)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9836 (IC base=+0.296)

- **PATRÓN** `ratio` > `1.0451` → IC=+0.408 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0451 (IC base=+0.296)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `83.3501` → IC=+0.235 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 83.3501 (IC base=+0.227)

- **PATRÓN** `ratio` < `0.9854` → IC=+0.398 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9854 (IC base=+0.227)

- **PATRÓN** `T_h` > `111.9952` → IC=+0.353 (n=833)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9952 (IC base=+0.325)

- **PATRÓN** `ratio` > `1.0093` → IC=+0.336 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0093 (IC base=+0.325)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.0788` → IC=+0.439 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.0788 (IC base=+0.399)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5415 sube el IC de +0.172 a +0.245 en UPDOWN_GBM#15min (n=3855). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7193 sube el IC de +0.212 a +0.279 en UPDOWN_GBM#BTC#15min (n=658). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.5211 sube el IC de +0.146 a +0.236 en UPDOWN_GBM#ETH#15min (n=776). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.8831 sube el IC de +0.086 a +0.243 en UPDOWN_GBM#SOL#15min (n=305). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5294 sube el IC de +0.198 a +0.274 en UPDOWN_GBM#XRP#15min (n=864). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1089 sube el IC de +0.070 a +0.167 en UPDOWN_GBM#XRP#15min (n=793). Ya aplicado como kelly_boost=+0.83€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6332 sube el IC de -0.068 a +0.280 en UPDOWN_GBM_15M_TARDIO (n=1092). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3673 sube el IC de -0.012 a +0.283 en UPDOWN_GBM_15M_TARDIO (n=3808). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7591 sube el IC de +0.090 a +0.330 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=362). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.6128 sube el IC de -0.193 a +0.321 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=65). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.5879 sube el IC de +0.153 a +0.248 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=549). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3777 sube el IC de +0.246 a +0.278 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=1419). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de -0.189 a +0.234 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=62). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3793 sube el IC de -0.038 a +0.290 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=630). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.211 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.137 sube el IC de -0.025 a +0.317 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=595). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_YES, IBS > 0.8489 sube el IC de +0.096 a +0.342 en UPDOWN_GBM_ETH_15M_HORA7 (n=17). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_YES, IBS > 0.8489 sube el IC de +0.096 a +0.342 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=17). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8389 sube el IC de +0.290 a +0.319 en UPDOWN_GBM_IBS_ALTO (n=1147). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.829 sube el IC de +0.284 a +0.308 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=614). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8494 sube el IC de +0.295 a +0.327 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=534). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.788 sube el IC de +0.365 a +0.400 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=660). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8066 sube el IC de +0.361 a +0.388 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=338). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7504 sube el IC de +0.368 a +0.411 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=323). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1998 | +0.090 | +211.24€ | 1 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1998 | +0.090 | +211.24€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1606 | +0.093 | +182.50€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1606 | +0.093 | +182.50€ | 0 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 284 | +0.070 | +11.30€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 284 | +0.070 | +11.30€ | 5 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 77 | +0.108 | +17.77€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 77 | +0.108 | +17.77€ | 0 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 796 | -0.006 | +88.52€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 796 | -0.006 | +88.52€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE | 6 | +0.000 | +1.70€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE#15min | 6 | +0.000 | +1.70€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 605 | -0.032 | +55.23€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 605 | -0.032 | +55.23€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 149 | +0.089 | +26.84€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 149 | +0.089 | +26.84€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 36 | +0.026 | +4.76€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 36 | +0.026 | +4.76€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 42021 | -0.083 | -5218.03€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 2407 | +0.049 | -267.66€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 39614 | -0.091 | -4950.37€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4583 | -0.115 | -745.37€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4583 | -0.115 | -745.37€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 2407 | +0.049 | -267.66€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 2407 | +0.049 | -267.66€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 4519 | -0.112 | -880.80€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 4519 | -0.112 | -880.80€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 11267 | -0.025 | -1146.94€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 11267 | -0.025 | -1146.94€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 11139 | -0.110 | -844.40€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 11139 | -0.110 | -844.40€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 8106 | -0.131 | -1332.87€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 8106 | -0.131 | -1332.87€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 38113 | -0.014 | +3226.69€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 9844 | +0.004 | +1635.58€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 28269 | -0.021 | +1591.12€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 38113 | -0.014 | +3226.69€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 9844 | +0.004 | +1635.58€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 28269 | -0.021 | +1591.12€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 154699 | +0.115 | -6130.64€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 19410 | +0.181 | -635.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 690 | -0.012 | -72.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 125437 | +0.107 | -5092.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 9162 | +0.097 | -329.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 20794 | +0.108 | -1273.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 63 | -0.162 | +9.93€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 20716 | +0.109 | -1271.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 29804 | +0.127 | -460.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5323 | +0.184 | -206.13€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 20780 | +0.121 | -124.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 3659 | +0.081 | -107.60€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 20849 | +0.099 | -1449.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 78 | -0.113 | -2.92€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 20756 | +0.101 | -1435.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 32937 | +0.124 | -619.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 8480 | +0.177 | -191.28€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 21073 | +0.107 | -369.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 3372 | +0.101 | -50.28€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 29496 | +0.115 | -1415.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 5394 | +0.198 | -253.92€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 593 | +0.019 | -18.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 21378 | +0.096 | -970.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 2131 | +0.119 | -172.08€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO#XRP | 20819 | +0.107 | -912.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 72 | -0.095 | +9.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 20734 | +0.108 | -921.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 24923 | +0.196 | -1523.80€ | 2 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 24923 | +0.196 | -1523.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 5655 | +0.179 | -478.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 5655 | +0.179 | -478.91€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 3275 | +0.203 | -77.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 3275 | +0.203 | -77.39€ | 3 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 5588 | +0.179 | -455.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 5588 | +0.179 | -455.44€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 4820 | +0.248 | -169.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 4820 | +0.248 | -169.25€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 5506 | +0.188 | -356.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 5506 | +0.188 | -356.57€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 1071 | +0.425 | -39.24€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 1071 | +0.425 | -39.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 426 | +0.435 | -7.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 426 | +0.435 | -7.66€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE#15min | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 424 | +0.430 | -10.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 424 | +0.430 | -10.70€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 207 | +0.400 | -17.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 207 | +0.400 | -17.00€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 87349 | +0.202 | -6201.51€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 87349 | +0.202 | -6201.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 15009 | +0.185 | -1545.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 15009 | +0.185 | -1545.93€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 14098 | +0.225 | -461.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 14098 | +0.225 | -461.74€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 14973 | +0.181 | -1574.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 14973 | +0.181 | -1574.96€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 14204 | +0.219 | -549.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 14204 | +0.219 | -549.98€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 14491 | +0.203 | -935.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 14491 | +0.203 | -935.92€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 14574 | +0.198 | -1132.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 14574 | +0.198 | -1132.98€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 33493 | +0.116 | +216.36€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 33493 | +0.116 | +216.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 16657 | +0.119 | +181.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 16657 | +0.119 | +181.43€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 16836 | +0.114 | +34.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 16836 | +0.114 | +34.93€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 2178 | +0.292 | -12.38€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 2178 | +0.292 | -12.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 1000 | +0.279 | -28.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 1000 | +0.279 | -28.13€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 1055 | +0.297 | +13.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 1055 | +0.297 | +13.31€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 123 | +0.340 | +2.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 123 | +0.340 | +2.44€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 1000 | +0.442 | +5.32€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 1000 | +0.442 | +5.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 485 | +0.434 | -6.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 485 | +0.434 | -6.42€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 468 | +0.451 | +11.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 468 | +0.451 | +11.04€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 47 | +0.398 | +0.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 47 | +0.398 | +0.70€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1741 | +0.069 | -73.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 682 | +0.042 | -65.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 1059 | +0.086 | -8.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 80 | +0.110 | +3.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 80 | +0.110 | +3.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1331 | +0.077 | -32.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 272 | +0.040 | -24.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 1059 | +0.086 | -8.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 330 | +0.027 | -45.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 330 | +0.027 | -45.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 66589 | +0.101 | -1626.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 5374 | +0.091 | +60.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 61215 | +0.102 | -1686.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 36559 | +0.106 | -387.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 5374 | +0.091 | +60.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 31185 | +0.108 | -448.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 13816 | +0.109 | -73.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 13816 | +0.109 | -73.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 16214 | +0.083 | -1164.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 16214 | +0.083 | -1164.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 899 | +0.192 | -110.13€ | 3 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 899 | +0.192 | -110.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 899 | +0.192 | -110.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 899 | +0.192 | -110.13€ | 3 | 4 |
| ✅ GBM_LATE_15M | 45567 | +0.095 | +24098.45€ | 0 | 19 |
| ✅ GBM_LATE_15M#15min | 45567 | +0.095 | +24098.45€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 7573 | +0.219 | +6339.21€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 7573 | +0.219 | +6339.21€ | 0 | 23 |
| ✅ GBM_LATE_15M#BTC | 6892 | +0.179 | +5296.85€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 6892 | +0.179 | +5296.85€ | 0 | 23 |
| ✅ GBM_LATE_15M#DOGE | 8162 | +0.205 | +6336.07€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 8162 | +0.205 | +6336.07€ | 0 | 19 |
| ✅ GBM_LATE_15M#ETH | 6303 | +0.044 | +1818.33€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 6303 | +0.044 | +1818.33€ | 1 | 18 |
| ✅ GBM_LATE_15M#SOL | 6393 | -0.032 | +1399.66€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 6393 | -0.032 | +1399.66€ | 3 | 13 |
| ✅ GBM_LATE_15M#XRP | 10244 | -0.030 | +2908.33€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 10244 | -0.030 | +2908.33€ | 4 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 48773 | +0.085 | +26823.86€ | 0 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 48773 | +0.085 | +26823.86€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 9429 | +0.002 | +4767.82€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 9429 | +0.002 | +4767.82€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 10399 | +0.010 | +2573.27€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 10399 | +0.010 | +2573.27€ | 0 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 6729 | +0.281 | +7311.75€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 6729 | +0.281 | +7311.75€ | 0 | 23 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 8921 | +0.013 | +2273.99€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 8921 | +0.013 | +2273.99€ | 1 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 7713 | +0.039 | +3224.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 7713 | +0.039 | +3224.81€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 5582 | +0.308 | +6672.22€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 5582 | +0.308 | +6672.22€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 36090 | +0.180 | +29430.17€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 36090 | +0.180 | +29430.17€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 5468 | +0.234 | +4942.92€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 5468 | +0.234 | +4942.92€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 5671 | +0.149 | +4199.96€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 5671 | +0.149 | +4199.96€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 5803 | +0.222 | +4959.22€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 5803 | +0.222 | +4959.22€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 6140 | +0.137 | +4743.24€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 6140 | +0.137 | +4743.24€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 6784 | +0.124 | +5083.21€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 6784 | +0.124 | +5083.21€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 6224 | +0.228 | +5501.62€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 6224 | +0.228 | +5501.62€ | 0 | 28 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 9725 | +0.130 | +4747.31€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 9725 | +0.130 | +4747.31€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 409 | +0.154 | +256.59€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 409 | +0.154 | +256.59€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 2805 | +0.139 | +1562.17€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 2805 | +0.139 | +1562.17€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 471 | +0.151 | +242.85€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 471 | +0.151 | +242.85€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 2952 | +0.136 | +1423.56€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 2952 | +0.136 | +1423.56€ | 0 | 13 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 2460 | +0.104 | +971.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 2460 | +0.104 | +971.77€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 628 | +0.133 | +290.38€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 628 | +0.133 | +290.38€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO | 45746 | +0.186 | +36862.75€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#15min | 45746 | +0.186 | +36862.75€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 7229 | +0.245 | +6825.17€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 7229 | +0.245 | +6825.17€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 7171 | +0.146 | +4945.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 7171 | +0.146 | +4945.71€ | 0 | 26 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 7753 | +0.232 | +6900.02€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 7753 | +0.232 | +6900.02€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 7553 | +0.139 | +5409.63€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 7553 | +0.139 | +5409.63€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 8101 | +0.120 | +5638.58€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 8101 | +0.120 | +5638.58€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 7939 | +0.234 | +7143.65€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 7939 | +0.234 | +7143.65€ | 0 | 20 |
| ✅ GBM_LATE_5M | 12176 | +0.203 | +9553.37€ | 1 | 30 |
| ✅ GBM_LATE_5M#5min | 12176 | +0.203 | +9553.37€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 1037 | +0.245 | +978.75€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 1037 | +0.245 | +978.75€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 2821 | +0.207 | +2414.49€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 2821 | +0.207 | +2414.49€ | 0 | 25 |
| ✅ GBM_LATE_5M#DOGE | 1167 | +0.196 | +861.83€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1167 | +0.196 | +861.83€ | 0 | 19 |
| ✅ GBM_LATE_5M#ETH | 3382 | +0.192 | +2372.82€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 3382 | +0.192 | +2372.82€ | 0 | 25 |
| ✅ GBM_LATE_5M#SOL | 1816 | +0.192 | +1396.00€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 1816 | +0.192 | +1396.00€ | 0 | 25 |
| ✅ GBM_LATE_5M#XRP | 1953 | +0.209 | +1529.48€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1953 | +0.209 | +1529.48€ | 0 | 0 |
| ✅ GBM_LATE_60M | 3837 | +0.063 | +1188.48€ | 0 | 8 |
| ✅ GBM_LATE_60M#60min | 3837 | +0.063 | +1188.48€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 1404 | +0.078 | +480.98€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 1404 | +0.078 | +480.98€ | 1 | 5 |
| ✅ GBM_LATE_60M#ETH | 1242 | +0.065 | +427.84€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 1242 | +0.065 | +427.84€ | 0 | 7 |
| ✅ GBM_LATE_60M#SOL | 1191 | +0.042 | +279.66€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 1191 | +0.042 | +279.66€ | 0 | 12 |
| 🚫 GBM_LATE_60M_FADE | 604 | -0.246 | -22.82€ | 10 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 604 | -0.246 | -22.82€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 226 | -0.246 | -14.71€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 226 | -0.246 | -14.71€ | 5 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 214 | -0.232 | +0.46€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 214 | -0.232 | +0.46€ | 4 | 1 |
| 🚫 GBM_LATE_60M_FADE#SOL | 164 | -0.259 | -8.56€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 164 | -0.259 | -8.56€ | 6 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 1651 | +0.083 | +416.41€ | 1 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 1651 | +0.083 | +416.41€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 646 | +0.080 | +157.44€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 646 | +0.080 | +157.44€ | 1 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 570 | +0.054 | +90.79€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 570 | +0.054 | +90.79€ | 2 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 435 | +0.125 | +168.18€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 435 | +0.125 | +168.18€ | 2 | 10 |
| ✅ LATE_WINDOW_5MIN | 176 | +0.281 | +176.56€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 176 | +0.281 | +176.56€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 176 | +0.281 | +176.56€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 176 | +0.281 | +176.56€ | 1 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 3615 | +0.101 | +877.27€ | 0 | 1 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 3615 | +0.101 | +877.27€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 3615 | +0.101 | +877.27€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 3615 | +0.101 | +877.27€ | 0 | 1 |
| ✅ LIQUIDACIONES_15M | 659 | -0.025 | -9.14€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 659 | -0.025 | -9.14€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 6 | -0.037 | -1.04€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 6 | -0.037 | -1.04€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 199 | -0.012 | +2.25€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 199 | -0.012 | +2.25€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 27 | -0.155 | -4.74€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 27 | -0.155 | -4.74€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 147 | +0.017 | +4.77€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 147 | +0.017 | +4.77€ | 1 | 1 |
| ✅ LIQUIDACIONES_15M#SOL | 228 | -0.009 | -0.44€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 228 | -0.009 | -0.44€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 3853 | +0.015 | +85.43€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 3853 | +0.015 | +85.43€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 185 | +0.029 | -0.77€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 185 | +0.029 | -0.77€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 799 | +0.007 | +29.01€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 799 | +0.007 | +29.01€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE | 211 | -0.002 | +0.52€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 211 | -0.002 | +0.52€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 1432 | +0.022 | +27.61€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1432 | +0.022 | +27.61€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 758 | +0.012 | +2.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 758 | +0.012 | +2.16€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 468 | +0.013 | +26.91€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 468 | +0.013 | +26.91€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 1874 | -0.039 | -28.42€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1874 | -0.039 | -28.42€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 549 | -0.028 | -10.91€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 549 | -0.028 | -10.91€ | 6 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 648 | -0.018 | +4.56€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 648 | -0.018 | +4.56€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 677 | -0.069 | -22.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 677 | -0.069 | -22.07€ | 6 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 10179 | -0.027 | +1.71€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 4841 | -0.035 | -85.65€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 5338 | -0.020 | +87.36€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 315 | -0.036 | -9.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 161 | -0.009 | +4.34€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 154 | -0.064 | -13.45€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 2594 | -0.017 | +38.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 1224 | -0.020 | +5.95€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 1370 | -0.013 | +32.97€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 1102 | -0.032 | -2.65€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 556 | -0.047 | -21.19€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 546 | -0.016 | +18.54€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 2243 | -0.037 | -52.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 1045 | -0.047 | -51.55€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 1198 | -0.028 | -0.90€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 1979 | -0.019 | +37.23€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 954 | -0.029 | -2.87€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 1025 | -0.009 | +40.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 1946 | -0.034 | -10.21€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 901 | -0.044 | -20.33€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 1045 | -0.026 | +10.12€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 53663 | -0.000 | +2745.68€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 53663 | -0.000 | +2745.68€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 9694 | +0.026 | +1245.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 9694 | +0.026 | +1245.85€ | 2 | 4 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 7679 | -0.034 | -111.25€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 7679 | -0.034 | -111.25€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 9804 | +0.025 | +1036.18€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 9804 | +0.025 | +1036.18€ | 1 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 7532 | -0.048 | -142.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 7532 | -0.048 | -142.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 9085 | -0.004 | +262.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 9085 | -0.004 | +262.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 9869 | +0.016 | +455.53€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 9869 | +0.016 | +455.53€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 6771 | -0.057 | -147.86€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 6771 | -0.057 | -147.86€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1233 | -0.002 | -17.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1233 | -0.002 | -17.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1806 | -0.071 | -34.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1806 | -0.071 | -34.70€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 61 | -0.024 | -0.66€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 61 | -0.024 | -0.66€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 785 | -0.120 | -34.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 785 | -0.120 | -34.37€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 2028 | -0.071 | -34.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 2028 | -0.071 | -34.84€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 858 | -0.016 | -26.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 858 | -0.016 | -26.02€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3370 | +0.004 | +1.01€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3370 | +0.004 | +1.01€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 131 | -0.034 | -0.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 131 | -0.034 | -0.72€ | 2 | 1 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 132723 | -0.077 | +1615.50€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 132723 | -0.077 | +1615.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 23152 | -0.077 | +1141.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 23152 | -0.077 | +1141.75€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 19963 | -0.101 | -1039.51€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 19963 | -0.101 | -1039.51€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 23426 | -0.068 | +1212.86€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 23426 | -0.068 | +1212.86€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 19509 | -0.098 | -641.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 19509 | -0.098 | -641.36€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 23700 | -0.058 | +310.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 23700 | -0.058 | +310.85€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 22973 | -0.068 | +630.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 22973 | -0.068 | +630.91€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 8846 | -0.034 | -182.64€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 8846 | -0.034 | -182.64€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 1002 | -0.017 | -19.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 1002 | -0.017 | -19.42€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 2013 | -0.047 | -27.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 2013 | -0.047 | -27.22€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2607 | -0.027 | -42.51€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2607 | -0.027 | -42.51€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1223 | -0.058 | -29.86€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1223 | -0.058 | -29.86€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 992 | -0.030 | -31.69€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 992 | -0.030 | -31.69€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1784 | +0.124 | +735.61€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#5min | 1648 | +0.130 | +723.02€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 382 | +0.138 | +192.47€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 382 | +0.138 | +192.47€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#DOGE | 339 | +0.116 | +115.04€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 339 | +0.116 | +115.04€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#ETH | 324 | +0.141 | +164.54€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 324 | +0.141 | +164.54€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#SOL | 291 | +0.152 | +161.22€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 291 | +0.152 | +161.22€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#XRP | 312 | +0.099 | +89.76€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 312 | +0.099 | +89.76€ | 0 | 3 |
| ✅ ORDER_FLOW_5M_REACTIVO | 1624 | -0.020 | -34.19€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 1624 | -0.020 | -34.19€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 308 | -0.006 | +6.16€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 308 | -0.006 | +6.16€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 288 | -0.031 | -6.49€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 288 | -0.031 | -6.49€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 412 | -0.048 | -36.62€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 412 | -0.048 | -36.62€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 350 | +0.006 | +3.54€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 350 | +0.006 | +3.54€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 266 | -0.011 | -0.77€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 266 | -0.011 | -0.77€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 947 | -0.071 | -45.63€ | 3 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 440 | -0.109 | -78.60€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 344 | -0.136 | -66.01€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 96 | -0.010 | -12.59€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 332 | -0.030 | +24.64€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 241 | -0.018 | +27.10€ | 2 | 2 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 91 | -0.059 | -2.46€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 175 | -0.054 | +8.34€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 144 | -0.062 | +3.95€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 31 | -0.015 | +4.39€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 729 | -0.083 | -34.95€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 218 | -0.032 | -10.67€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 1189 | -0.205 | -68.44€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC | 464 | -0.206 | -42.85€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#atexpiry | 407 | -0.209 | -42.62€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 57 | -0.178 | -0.23€ | 2 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 404 | -0.207 | -32.20€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 356 | -0.218 | -39.21€ | 4 | 1 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 48 | -0.120 | +7.01€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 321 | -0.200 | +6.61€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 300 | -0.195 | +4.49€ | 5 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 21 | -0.239 | +2.12€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 1063 | -0.209 | -77.34€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 126 | -0.172 | +8.90€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 477 | +0.391 | +450.78€ | 0 | 9 |
| ✅ RESOLUTION_SNIPER#BTC | 80 | +0.171 | +63.15€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 80 | +0.171 | +63.15€ | 0 | 4 |
| ✅ RESOLUTION_SNIPER#ETH | 110 | +0.366 | +102.82€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 110 | +0.366 | +102.82€ | 0 | 8 |
| ✅ RESOLUTION_SNIPER#SOL | 287 | +0.459 | +284.81€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 287 | +0.459 | +284.81€ | 0 | 10 |
| ✅ RESOLUTION_SNIPER#sniper | 477 | +0.391 | +450.78€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 774 | +0.032 | +50.72€ | 2 | 4 |
| ✅ STREAK_FADE_15M#15min | 774 | +0.032 | +50.72€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 307 | +0.021 | +2.87€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 307 | +0.021 | +2.87€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 63 | -0.008 | -1.05€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 63 | -0.008 | -1.05€ | 1 | 0 |
| ✅ STREAK_FADE_15M#SOL | 78 | +0.000 | +3.29€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 78 | +0.000 | +3.29€ | 2 | 0 |
| ✅ STREAK_FADE_15M#XRP | 326 | +0.058 | +45.61€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 326 | +0.058 | +45.61€ | 0 | 4 |
| ✅ STREAK_FADE_5M | 3460 | -0.022 | -137.83€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3460 | -0.022 | -137.83€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 1061 | -0.021 | -36.50€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 1061 | -0.021 | -36.50€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 596 | -0.030 | -28.08€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 596 | -0.030 | -28.08€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 168 | -0.041 | -14.30€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 168 | -0.041 | -14.30€ | 4 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1635 | -0.019 | -58.95€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1635 | -0.019 | -58.95€ | 1 | 0 |
| ✅ STREAK_FADE_60M | 103 | -0.052 | -9.27€ | 6 | 0 |
| ✅ STREAK_FADE_60M#60min | 103 | -0.052 | -9.27€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 43 | -0.100 | -5.07€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 43 | -0.100 | -5.07€ | 4 | 0 |
| ✅ STREAK_FADE_60M#SOL | 60 | -0.016 | -4.20€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 60 | -0.016 | -4.20€ | 0 | 2 |
| ✅ STREAK_MOM_5M | 11236 | +0.015 | +76.76€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 11236 | +0.015 | +76.76€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2852 | +0.020 | +28.42€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2852 | +0.020 | +28.42€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2922 | +0.017 | +32.42€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2922 | +0.017 | +32.42€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2905 | +0.009 | -2.38€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2905 | +0.009 | -2.38€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2557 | +0.014 | +18.30€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2557 | +0.014 | +18.30€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 10203 | +0.014 | -47.00€ | 2 | 0 |
| ✅ STRUCT_NO_15M#15min | 10203 | +0.014 | -47.00€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 4206 | +0.018 | -5.30€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 4206 | +0.018 | -5.30€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3622 | +0.011 | -28.05€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3622 | +0.011 | -28.05€ | 2 | 0 |
| ✅ STRUCT_NO_15M#SOL | 2375 | +0.009 | -13.65€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 2375 | +0.009 | -13.65€ | 1 | 0 |
| ✅ UPDOWN_GBM | 81734 | +0.055 | +7310.28€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 20105 | +0.084 | +4396.62€ | 0 | 11 |
| ✅ UPDOWN_GBM#240min | 2607 | +0.003 | +27.37€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 53855 | +0.052 | +2793.31€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 4877 | +0.006 | +96.65€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 6851 | +0.089 | +1075.72€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1576 | +0.156 | +698.08€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 77 | -0.006 | -0.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 5198 | +0.070 | +378.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 18281 | +0.056 | +1574.95€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 2688 | +0.089 | +648.29€ | 0 | 9 |
| ✅ UPDOWN_GBM#BTC#240min | 715 | +0.006 | +12.01€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 12585 | +0.062 | +845.78€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 2188 | +0.003 | +66.24€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 105 | -0.070 | +2.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 8711 | +0.070 | +925.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1555 | +0.147 | +610.96€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 78 | +0.013 | -1.79€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 7078 | +0.054 | +316.21€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 19178 | +0.046 | +1289.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 4841 | +0.070 | +744.29€ | 0 | 10 |
| ✅ UPDOWN_GBM#ETH#240min | 691 | +0.006 | +16.42€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 11812 | +0.045 | +505.69€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 1737 | +0.009 | +20.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 97 | -0.106 | +2.21€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 17908 | +0.034 | +930.14€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 5125 | +0.035 | +414.71€ | 0 | 2 |
| ✅ UPDOWN_GBM#SOL#240min | 658 | -0.009 | +1.65€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 11087 | +0.040 | +510.43€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 952 | +0.006 | +10.02€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 86 | -0.136 | -6.66€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 10803 | +0.066 | +1516.92€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 4320 | +0.104 | +1280.29€ | 0 | 10 |
| ✅ UPDOWN_GBM#XRP#240min | 388 | +0.010 | -0.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 6095 | +0.043 | +236.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 288 | -0.103 | -1.83€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 880 | +0.365 | +322.52€ | 0 | 9 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 880 | +0.365 | +322.52€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 450 | +0.361 | +153.90€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 450 | +0.361 | +153.90€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 430 | +0.368 | +168.62€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 430 | +0.368 | +168.62€ | 0 | 14 |
| ✅ UPDOWN_GBM_15M_TARDIO | 20743 | -0.024 | +4906.38€ | 2 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 20743 | -0.024 | +4906.38€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1718 | -0.056 | +502.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1718 | -0.056 | +502.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 3783 | -0.113 | +145.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 3783 | -0.113 | +145.57€ | 3 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 948 | +0.216 | +770.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 948 | +0.216 | +770.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 2622 | +0.221 | +1725.22€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 2622 | +0.221 | +1725.22€ | 1 | 20 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 5931 | -0.064 | +749.42€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 5931 | -0.064 | +749.42€ | 5 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 5741 | -0.065 | +1012.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 5741 | -0.065 | +1012.89€ | 2 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 247 | +0.058 | +19.74€ | 0 | 7 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 247 | +0.058 | +19.74€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 247 | +0.058 | +19.74€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 247 | +0.058 | +19.74€ | 0 | 7 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1529 | +0.290 | +1303.38€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1529 | +0.290 | +1303.38€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 818 | +0.284 | +653.85€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 818 | +0.284 | +653.85€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 711 | +0.295 | +649.52€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 711 | +0.295 | +649.52€ | 0 | 9 |
| ✅ UPDOWN_OU_5M | 829 | -0.113 | -82.82€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#5min | 829 | -0.113 | -82.82€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 254 | -0.082 | -19.18€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 254 | -0.082 | -19.18€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 90 | -0.174 | -10.68€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 90 | -0.174 | -10.68€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 102 | -0.173 | -3.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 102 | -0.173 | -3.61€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 38 | -0.175 | -6.61€ | 2 | 0 |
| ✅ WEEKLY_PRICE | 3824 | +0.304 | +1811.38€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 1417 | +0.258 | +182.56€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 1468 | +0.299 | +658.44€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 939 | +0.380 | +970.38€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**✅ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: n≥15 y IC<-0.05
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: IC=+0.023 n=1029 — no justifica filtro, seguir monitorizando
  - _Datos_: n=1029 IC=+0.023 PNL=+46.33€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 729 celda(s) pasan gate riguroso completo de 2746 evaluadas (n>=40) y 3809 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.035 < 0.08 — monitorear
  - _Datos_: n=5125 IC=+0.035 PNL=+414.71€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=1468/15 IC=+0.299 PNL=+658.44€ | BTC: n=1417/15 IC=+0.258 PNL=+182.56€ | SOL: n=939/15 IC=+0.380 PNL=+970.38€

**🟡 H-KALMAN** — Kalman filter para drift adaptativo
  - _Umbral_: n≥200 por subtipo para calibrar parámetros Q/R del KF
  - _Acción_: Sustituir DRIFT_DAMPING por KalmanDrift en fetch_binance_klines.py
  - _Estado_: 31 subtypes con n≥200: UPDOWN_GBM, UPDOWN_GBM#ETH#60min, UPDOWN_GBM#ETH, UPDOWN_GBM#60min, UPDOWN_GBM#BTC#60min
  - _Bloqueante_: N_INSUFICIENTE


### ⏳ Acumulando datos

**⏳ H-IBS-15** — IBS-15 como señal de mean-reversion
  - _Umbral_: 40
  - _Acción_: Añadir ibs_15 como boost/filtro en FEATURE_RULES de shadow_postmortem.py
  - _Estado_: Solo 0 ops con ibs_15 (feature añadida 2026-06-27). Esperar n≥40.

**⏳ H-HORA-GBM** — hora_utc causal automático en GBM (forward)
  - _Umbral_: 20
  - _Acción_: El sistema lo aplica automáticamente vía FEATURE_RULES. Verificar en strategy_params.json.
  - _Estado_: Solo 0 ops GBM con hora_utc en features. Esperar n≥20 para patrones.

**⏳ H-WINDOW-MOMENTUM** — Momentum de outcome entre ventanas 15min contiguas
  - _Umbral_: n≥60 alineadas y gap IC≥0.08 vs contrarias — y descartar que sea proxy de drift_15min/60min
  - _Acción_: Si confirma e independiente de drift → capturar prev_window_outcome como feature en shadow_predict y boost ×1.1-1.2 en señales alineadas
  - _Estado_: alineada_con_outcome_prev IC=+0.140 n=834/60 | contraria IC=+0.194 n=869 | gap=-0.053 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=496, boost estimado=+0.017. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 0/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=1736/40 IC=+0.009 PNL=+20.90€ | BTC#60min: n=2186/40 IC=+0.003 PNL=+65.57€ | SOL#60min: n=952/40 IC=+0.006 PNL=+10.02€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.047 n=593215 | tras_1loss IC=+0.096 n=450554 | tras_2loss IC=+0.066 n=181950/40 | gap=-0.018 (umbral 0.05)

**⏳ H-BTC-LEADS-ETH** — ETH/SOL GBM contrario al drift_15min de BTC del mismo ciclo
  - _Umbral_: n≥40 en contrario_BTC y gap≥0.08 — y descartar confound con drift propio antes de actuar
  - _Acción_: Si se confirma y no es confound → boost en ETH/SOL cuando decisión contraria a drift_15min BTC
  - _Estado_: alineado_BTC IC=+0.000 n=0 | contrario_BTC IC=+0.000 n=0/40 | gap=+0.000 (umbral 0.08) — SIN CONFIRMAR independencia de filtros propios de ETH


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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.194 > 0.08 con n=798 PNL=+587.54€
  - _Datos_: n=798 IC=+0.194 PNL=+587.54€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.165 > 0.08 con n=905 PNL=+504.52€
  - _Datos_: n=905 IC=+0.165 PNL=+504.52€

**🟡 H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: n≥25 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.162 > 0.08 con n=66 PNL=+33.08€
  - _Datos_: n=66 IC=+0.162 PNL=+33.08€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.334 > 0.1 con n=3123 PNL=+1748.79€
  - _Datos_: n=3123 IC=+0.334 PNL=+1748.79€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=764 IC=+0.070 PNL=+82.88€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=764 IC=+0.070 PNL=+82.88€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=89 IC=+0.181 PNL=+58.85€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=89 IC=+0.181 PNL=+58.85€

**⏳ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: 30
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

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
  - _Estado_: n=3277 IC=+0.009 PNL=+13.45€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=3277 IC=+0.009 PNL=+13.45€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=1597 IC=+0.000 PNL=+83.04€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=1597 IC=+0.000 PNL=+83.04€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=1029 IC=+0.023 PNL=+46.33€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=1029 IC=+0.023 PNL=+46.33€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.172 > 0.1 con n=5138 PNL=+3118.36€
  - _Datos_: n=5138 IC=+0.172 PNL=+3118.36€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=2686 IC=+0.089 PNL=+643.99€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=2686 IC=+0.089 PNL=+643.99€

**⏳ H-CUSTOM-DRIFT15-ZONA-MUERTA** — GBM#15min drift_15min ∈ [-0.3,+0.3] — zona muerta de señal
  - _Hipótesis_: Análisis n=127 GBM#15min: cuando drift_15min está entre -0.3 y +0.3 (mercado sin dirección clara) el IC es negativo (-0.043). Cuando drift>0.3 IC=+0.100 (n=28). Cuando drift<-1 IC=+0.048 (reversión). La señal requiere mercado con dirección clara.
  - _Umbral_: 50
  - _Acción_: Filtrar señales GBM#15min cuando drift_15min ∈ [-0.3, +0.3] — validar con n≥50 antes de implementar
  - _Estado_: 0/50 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)
  - _Bloqueante_: FILTRO_YA_IMPLEMENTADO: confirmada 2026-07-01 (IC=-0.037 n=52) e implementada en shadow_predict.py (skip si drift_15min∈[-0.3,0.3)) -- verificado 26-Ago con 2177 filas post-TWAP reales, 0 caen en la zona filtrada. Frozen by design, no falta n

**⏳ H-CUSTOM-DRIFT15-MOMENTUM** — GBM#15min drift_15min > 0.3 — zona de momentum (señal fuerte)
  - _Hipótesis_: Cuando drift_15min > 0.3%/h el GBM captura bien la dirección: IC=+0.100 n=28 en todos GBM#15min; IC=+0.152 n=13 solo BTC. El mercado tiene dirección clara y el GBM la sigue. Hipótesis: este rango es donde la señal es real.
  - _Umbral_: 40
  - _Acción_: Si se confirma IC>0.10 con n≥40 → boost ×1.2 en GBM#15min cuando drift_15min>0.3
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-LONGSHOT-BIAS** — Longshot bias — ¿mejor IC cuando py_mkt < 0.20 o > 0.80?
  - _Hipótesis_: Jon-Becker repo documenta formalmente: contratos a 1-20 cents tienen win_rate < precio implícito (compradores pierden sistemáticamente en longshots). En nuestro sistema: cuando py_mkt<0.20 el GBM predice BUY_NO con edge estructural adicional al del modelo. ¿Se confirma en nuestros datos? Buscar en feature pct_spot_vs_ref si los mercados extremos tienen mejor IC en BUY_NO.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 en mercados extremos → boost ×1.2 en BUY_NO cuando py_mkt<0.20
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-ETH15-REVERSION** — ETH#15min con drift_15min < -1 — ¿mean reversion?
  - _Hipótesis_: ETH y BTC tienen patrones opuestos: BTC funciona con momentum (drift>0.3). ETH funciona con reversión (drift<-1): 9/14 (64%) IC=+0.087. La hipótesis es que ETH tiene más mean-reversion que BTC en 15min.
  - _Umbral_: 20
  - _Acción_: Si ETH drift<-1 confirma IC>0.08 con n≥20 → boost ×1.1 en ETH#15min cuando drift_15min<-1
  - _Estado_: 0/20 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-09H** — GBM a las 09h UTC — bloqueada 2026-06-29
  - _Hipótesis_: IC=-0.158 n=19 PNL=-11.62€. Bloqueada manualmente el 2026-06-29 añadiendo hora 9 a meta.gbm_blacklist_hours_auto. Esta hipótesis monitorea que el IC siga siendo negativo para justificar el bloqueo.
  - _Umbral_: n≥25 para confirmar el bloqueo es necesario
  - _Acción_: Si IC sube a >-0.05 con n≥30 → evaluar desbloquear. Si se mantiene <-0.10 → confirmar bloqueo permanente.
  - _Estado_: n=1044 IC=+0.037 PNL=+89.22€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=1044 IC=+0.037 PNL=+89.22€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=132 IC=+0.000 PNL=-0.12€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=132 IC=+0.000 PNL=-0.12€

**⏳ H-FUNDING-HIGH-BUYNO** — Funding rate alto (>p90 real ≈0.009%/8h) → BUY_NO tiene más edge
  - _Hipótesis_: Cuando funding perps Binance está en el decil superior real (>0.009%/8h, ver recalibración 06-Ago), los longs están sobrecargados y pagan por mantener. Hipótesis: BUY_NO GBM tiene IC superior en este régimen vs funding neutral. RECALIBRADO 06-Ago: el umbral original (0.03) era FÍSICAMENTE IMPOSIBLE -- el máximo real observado en 5428 filas de UPDOWN_GBM (feature funding_rate_8h = round(fr*100,5), fr=lastFundingRate crudo de Binance) es 0.01, y nunca lo cruzaba -- n=0 desde que se creó, atrapada sin poder acumular ni una fila. Recalibrado a p90 real (percentiles: p50=0.00368, p75=0.00651, p90=0.00943, p95=p99=p100=0.01 -- el feature satura en 0.01 en el 8.4% de las filas, sin evidencia de que sea un bug de captura, no de que sea funding genuinamente extremo). n=332 BUY_NO ya disponibles con el umbral nuevo (>>umbral_n=40), frente a n=0 con el original.
  - _Umbral_: 40
  - _Acción_: Si IC_funding_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en BUY_NO cuando funding_rate_8h > 0.009
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-FUNDING-NEGATIVE-BUYYES** — Funding rate negativo (<-0.01%/8h) → BUY_YES tiene más edge (short squeeze)
  - _Hipótesis_: Cuando funding < -0.01%/8h, los shorts están pagando por mantener la posición. Históricamente precede squeezes en cripto. Hipótesis: BUY_YES GBM tiene IC superior en régimen de funding negativo.
  - _Umbral_: 30
  - _Acción_: Si se confirma → boost ×1.1 en BUY_YES cuando funding_rate_8h < -0.01
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔶 H-LATE-WINDOW-5MIN** — Late-window BTC 5min — arbitraje timing vs Polymarket
  - _Hipótesis_: Inspirado en VyvanseWithMarijuana (36.5% ROI, $42k vol). A T+160-270s dentro de una ventana BTC 5min, si BTC ya se movió >0.3%, Polymarket no ha actualizado precio → edge estructural. Estrategia LATE_WINDOW_5MIN en shadow hasta n≥30. FIX 2026-07-02: la estrategia llevaba 0 predicciones desde su creacion porque HORIZONTE_MIN_HORAS=0.05 (3min) descartaba todo mercado a <3min de expirar — y su zona de entrada (160-270s de una ventana de 5min) deja 30-140s restantes, siempre bajo el suelo. Corregido en shadow_predict (zona late-window marcada _solo_late, 30s-3min, solo evaluada por esta estrategia). El reloj de acumulacion empieza de verdad hoy. Contexto extra: el estudio de ballenas de hoy confirma que comprar el lado ganador a mitad/final de ventana es el playbook comun de los 3 mayores ganadores verificados de estos mercados (Bonereaper +$19.9k/mes, wowitsamazing +$10k/mes, zhangfan151 +$8.7k/mes).
  - _Umbral_: n≥30 y IC>+0.05
  - _Acción_: Si IC≥0.08 con n≥30 → proponer pasar a live con stake mínimo (0.50€). Si IC<0 con n≥30 → el lag de Polymarket en BTC es insuficiente.
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.281 n=176) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=176 IC=+0.281 PNL=+176.56€

**⏳ H-DVOL-SPIKE-BUYNO** — DVOL spike (sigma_h alto) → BUY_NO tiene más edge (panic regime)
  - _Hipótesis_: Inspirado en 'The Volatility Edge' (Concretum Research, 2025): en equities, VIX spikes identifican regímenes de pánico donde los moves están sobreamplificados por feedback loops (deleveraging, hedgers, etc). En cripto el análogo es DVOL (Deribit BTC IV). Sin acceso a DVOL, usamos sigma_h como proxy (vol realizada 1h). Hipótesis: cuando sigma_h > 0.004/h (≈ vol diaria >9.6%), los mercados de predicción exageran la bajada en 15min → BUY_NO tiene IC superior porque el pánico se revierte intraday. Activar cuando n≥200 en BUY_NO #15min para tener potencia suficiente para subdividir por régimen.
  - _Umbral_: 40
  - _Acción_: Si IC_sigma_alto > IC_baseline + 0.08 con n≥40 → boost ×1.2 en BUY_NO cuando sigma_h>0.004. Pendiente integrar DVOL real (Deribit API) cuando n≥500.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-POLY-DRIFT-CONFIRM** — poly_drift_5obs: ¿el precio YES interno de Polymarket confirma nuestra señal?
  - _Hipótesis_: Feature nueva 2026-06-27: drift del precio YES en Polymarket en últimas 5 obs (~5min). Si poly_drift<0 y decidimos BUY_NO (o poly_drift>0 y BUY_YES) → confluencia. Si diverge → reducción de stake. Hipótesis: confluencia Binance+Polymarket mejora IC; divergencia empeora.
  - _Umbral_: 40
  - _Acción_: Si IC_confluencia>IC_divergencia con n≥40 → mantener el boost. Si no → retirar.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-OF-VOLUMEN-ALTO** — ORDER_FLOW_5M con total_vol_5m alto — ¿volumen extremo mejora el IC?
  - _Hipótesis_: Inspirado en un artículo sobre 'volume trading strategy' (mean-reversion en SPY): la idea es que un mismo movimiento de precio con volumen inusualmente alto refleja pánico/liquidación forzada y tiene más probabilidad de revertir que el mismo movimiento con volumen normal. No es transplantable tal cual (esa estrategia opera en barras diarias de SPY, nosotros en ventanas de 15-60min de cripto), pero el feature total_vol_5m ya se captura en cada predicción de ORDER_FLOW_5M (shadow_predict.py) y nunca se ha usado como filtro independiente — solo sirve de denominador para calcular delta_ratio. Hipótesis: dentro de las señales que ya pasan el filtro de delta_ratio, un total_vol_5m alto (volumen real, no solo desequilibrio) mejora el IC. Distribución real en predictions_*.csv (n=843): mediana=1696, p75=108522 (muy asimétrica) — se usa p75 como umbral de 'volumen alto'.
  - _Umbral_: 40
  - _Acción_: Si IC_volumen_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en ORDER_FLOW_5M cuando total_vol_5m>100000
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-CROSS-WINDOW-SPREAD-POS** — GBM 15min/60min: spread positivo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Inspirado en un artículo sobre bots de Polymarket: mercados de distinta duración del mismo activo (ej. BTC#15min vs BTC#60min) no repriciician a la misma velocidad — uno puede quedarse rezagado tras un movimiento. Si el spread entre ambos se sale de lo normal, puede indicar que uno de los dos aún no ha incorporado la información que el otro ya tiene. No es transplantable tal cual (el artículo lo usa para arbitraje comprando ambos lados a la vez, algo que no hacemos — ver idea_bidirectional_accumulation aparcada), pero el feature cross_window_spread (precio_yes propio menos precio_yes de la ventana relacionada, sin normalizar aún por z-score) ya se captura para GBM#15min (contra 60min) y GBM#60min (contra 15min) desde el 2026-07-01, sin cambiar ninguna decisión. Esta hipótesis cubre el lado positivo (mercado propio más caro que el relacionado); ver H-CUSTOM-CROSS-WINDOW-SPREAD-NEG para el lado negativo.
  - _Umbral_: 40
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread, y evaluar si merece la pena normalizar a z-score con más histórico
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-CROSS-WINDOW-SPREAD-NEG** — GBM 15min/60min: spread negativo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Lado negativo de H-CUSTOM-CROSS-WINDOW-SPREAD-POS (mercado propio más barato que el relacionado). Mismo feature cross_window_spread, mismo origen (artículo sobre bots de Polymarket), umbral simétrico.
  - _Umbral_: 40
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-MOON-LLENA** — Fase lunar: ¿rendimiento peor cerca de luna llena?
  - _Hipótesis_: Inspirado en el paper de Fornero (2023, 43 Jornadas SADAF) sobre astrología financiera: 5 estudios peer-review (Dichev & Janes 2003, Yuan et al. 2006, Keef & Khaled 2011, Floros & Tan 2013, Liu & Tseng 2009) en 25-62 mercados bursátiles encuentran rendimientos 5-10%/año más bajos cerca de luna llena que de luna nueva. El propio paper es escéptico de la astrología como tal, pero el mecanismo que documenta no es místico: sesgo de humor de inversores minoristas (más fuerte en acciones con dominancia retail, casi nulo en institucional). Polymarket es un mercado muy retail/cripto — hipótesis: si el mecanismo transfiere, debería verse peor IC cerca de luna llena (moon_phase≈0.5) que en el resto del ciclo.
  - _Umbral_: 200
  - _Acción_: Si IC cerca de luna llena < IC resto del ciclo con margen ≥0.05 y ≥3 ciclos lunares cubiertos → considerar boost/filtro por moon_phase. No implementar con menos de 3 ciclos aunque n sea alto — el efecto es de calendario lento, no de volumen.
  - _Estado_: 0/200 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-MERCURY-RETROGRADO** — Mercurio retrógrado: ¿rendimiento peor durante la ventana?
  - _Hipótesis_: Mismo origen que H-CUSTOM-MOON-LLENA (paper de Fornero, 43 Jornadas SADAF 2023). Qi, Wang & Zhang (2022, 48 mercados, 1973-2019): rendimientos 3.33%/año más bajos durante Mercurio retrógrado. Kou & Ma (2022) en China (99.8% cuentas retail): hasta -31% anualizado. Ambos estudios confirman que el mecanismo es la creencia/superstición de inversores retail (mayor efecto cuanto más retail y más supersticioso el mercado), no un efecto astral literal — Polymarket encaja en ese perfil. Ventanas 2026 (fuente pública, actualizar cada año): 26-feb a 20-mar, 29-jun a 23-jul, 24-oct a 13-nov.
  - _Umbral_: 100
  - _Acción_: Si IC en mercury_retrogrado=1 < IC en mercury_retrogrado=0 con margen ≥0.05 y ≥2 ventanas distintas cubiertas → considerar boost/filtro. No implementar tras una sola ventana (jun-jul 2026) por more que n sea alto — sería solo un evento, no un patrón.
  - _Estado_: 0/100 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-SMART-MONEY-CONSENSUS** — Consenso de wallets 'smart money' — ¿confirma nuestra dirección?
  - _Hipótesis_: Javi propuso estudiar bots/wallets que operan bien en nuestros mismos mercados. En vez de creer artículos (ya verificamos 2 veces esta semana que las narrativas no aguantan el cruce con datos reales), smart_money_tracker.py mide el track record REAL de wallets activas en BTC/ETH/SOL/XRP Up-or-Down 5/15/60min vía data-api.polymarket.com/positions, filtrado a posiciones 'Up or Down'. Clasifica como 'smart' las wallets con n>=10 posiciones, win_rate>=0.55 y pnl_total>0. smart_money_consensus es el sesgo direccional reciente (Up-Down)/(Up+Down) de esas wallets 'smart' por activo. Hipótesis: si nuestra decisión (BUY_YES/BUY_NO) coincide con el consenso smart money, mejor IC que cuando diverge. RESET METODOLOGICO 2026-07-02: la clasificacion 'smart' original via /positions estaba INVERTIDA para wallets de alta frecuencia (el endpoint solo retiene el residuo perdedor sin redimir; verificado: 'wowitsamazing' figuraba como -$478k y es +$10k/mes en el leaderboard oficial). Desde 2026-07-02T06:12Z el consenso se construye solo con wallets verificadas en el leaderboard oficial (pnl_mes>=$1000, 24 wallets). Los valores de smart_money_consensus capturados en features ANTES de esa fecha provienen de la clasificacion rota — descontar ese tramo al evaluar.
  - _Umbral_: 40
  - _Acción_: Si IC en confluencia (decisión coincide con signo de smart_money_consensus) supera en >=0.05 al IC en divergencia, con n≥40 en cada lado → boost ×1.1-1.2 cuando coincide, considerar reducir stake cuando diverge fuerte.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🟡 H-CUSTOM-OF-EDGE-ALTO** — ORDER_FLOW_5M: edge alto (>0.20) rinde mejor que edge cerca del suelo
  - _Hipótesis_: Analizado 2026-07-01 sobre 794 resoluciones de ORDER_FLOW_5M: edge_neto en [0.025,0.198) -> IC=-0.009 (n=397, PNL=-10.49€) vs edge_neto en [0.198,0.385] -> IC=+0.029 (n=397, PNL=+16.43€). Comprobado que NO es un efecto general: en UPDOWN_GBM el patrón se invierte (edge bajo IC=-0.002 vs edge alto IC=-0.033), así que este filtro debe quedar scoped solo a ORDER_FLOW_5M, no aplicarse a otras estrategias. CORREGIDO 2026-07-01 (mismo día, encontrado por auditoría): el filtro original usaba 'edge_neto' con solo feature_lo, pero edge_neto está firmado por dirección (negativo en BUY_NO, positivo en BUY_YES) y ORDER_FLOW_5M solo genera BUY_NO desde 2026-06-25 — el filtro nunca podía matchear ningún BUY_NO real, solo el remanente BUY_YES histórico de antes del 25-jun (n=151, datos muertos, no crecen hacia adelante). Cambiado a 'edge_direccional' (siempre positivo, = abs(edge_neto)) + decision=BUY_NO explícito. Con el fix: n=227, IC=+0.0502, PNL=+19.15€ — señal real y viva.
  - _Umbral_: n≥80 en cada mitad (bajo/alto) para confirmar con más margen que el análisis inicial
  - _Acción_: Si se confirma con n≥80 y el gap se mantiene ≥0.03 → subir EDGE_MINIMO solo para ORDER_FLOW_5M a ~0.20 (o escalar Kelly con la magnitud del edge)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.124 > 0.02 con n=1034 PNL=+430.78€
  - _Datos_: n=1034 IC=+0.124 PNL=+430.78€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=213 IC=-0.091 PNL=+19.65€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=213 IC=-0.091 PNL=+19.65€

**⏳ H-CUSTOM-WEEKLY-INRANGE-BUYYES** — WEEKLY_PRICE BUY_YES con in_range=1 — ¿estructuralmente sobrevalorado?
  - _Hipótesis_: Analizado 2026-07-01, n=10 (evidencia mínima): BUY_YES cuando in_range=1 fue 0/3 (todo pérdida). Mecanismo propuesto: acertar un rango de precio estrecho al vencimiento es intrínsecamente poco probable, el mercado puede estar sobrevalorando el 'sí'. Ver H-CUSTOM-WEEKLY-PCTDIST-BUYNO para el lado complementario (BUY_NO con pct_dist alto).
  - _Umbral_: 25
  - _Acción_: Si se confirma con n≥25 → filtro causal in_range==1 + BUY_YES → skip en WEEKLY_PRICE
  - _Estado_: 0/25 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-WEEKLY-PCTDIST-BUYNO** — WEEKLY_PRICE BUY_NO con pct_dist alto — cuanto más lejos del rango, más seguro
  - _Hipótesis_: Analizado 2026-07-01, n=10 (evidencia mínima): BUY_NO con pct_dist>=2.09% fue 4/4 victorias (rango 2.09%-23.4%); BUY_NO con pct_dist<8% (pero fuera del corte anterior) tuvo derrotas. Patrón: cuanto más lejos está el spot del rango objetivo al momento de la predicción, más fiable el BUY_NO. Complementa H-CUSTOM-WEEKLY-INRANGE-BUYYES.
  - _Umbral_: 25
  - _Acción_: Si se confirma con n≥25 → boost ×1.2 en WEEKLY_PRICE BUY_NO cuando pct_dist≥2
  - _Estado_: 0/25 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-BUYYES-GLOBAL-MALO** — UPDOWN_GBM BUY_YES global — ¿estructuralmente peor que BUY_NO en todas las estrategias activas?
  - _Hipótesis_: Analizado 2026-07-01: patrón cross-estrategia consistente en las 4 estrategias activas — BUY_NO gana a BUY_YES sin excepción (UPDOWN_GBM IC=+0.058 n=154 vs -0.046 n=412; ORDER_FLOW_5M +0.053 n=439 vs -0.043 n=355; PRICE_TARGET_GBM +0.011 n=45 vs -0.267 n=28; WEEKLY_PRICE +0.115 n=50 vs -0.315 n=25). Mecanismo propuesto: sesgo retail comprando 'Up'/'YES' en cripto infla el precio de YES por encima de su valor justo en Polymarket — consistente con la sobreconfianza del modelo en probabilidades altas de YES detectada en la calibración Platt (ver idea_calibracion_platt). ORDER_FLOW_5M (solo genera BUY_NO desde 2026-06-25) y WEEKLY_PRICE (H-WEEKLY-BUYNO) ya actúan sobre este mismo patrón; UPDOWN_GBM y PRICE_TARGET_GBM (ver H-CUSTOM-PRICETARGET-BUYYES-MALO) todavía no tienen un tratamiento sistemático equivalente, solo filtros puntuales por hora/subtipo.
  - _Umbral_: n≥50 y IC<-0.05 para confirmar bloqueo global (a día de hoy ya está en n=412, IC=-0.046 — muy cerca)
  - _Acción_: Si se confirma con n≥50 → exigir evidencia direccional más fuerte por subtipo antes de permitir BUY_YES en live (barra asimétrica frente a BUY_NO), en vez de auto-desactivar de golpe todo BUY_YES de GBM
  - _Estado_: n=32368 IC=+0.074 PNL=+4665.54€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=32368 IC=+0.074 PNL=+4665.54€

**⏳ H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: 120
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: 0/120 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.139 < -0.1 con n=541 PNL=+70.28€
  - _Datos_: n=541 IC=-0.139 PNL=+70.28€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=3169 IC=+0.070 PNL=+417.35€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=3169 IC=+0.070 PNL=+417.35€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=152 IC=-0.097 PNL=+3.71€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=152 IC=-0.097 PNL=+3.71€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.113 > 0.1 con n=868 PNL=+238.09€
  - _Datos_: n=868 IC=+0.113 PNL=+238.09€

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
  - _Estado_: n=34756 IC=-0.134 PNL=+2723.89€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=34756 IC=-0.134 PNL=+2723.89€

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
  - _Estado_: n=3507 IC=+0.132 PNL=+2177.20€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=3507 IC=+0.132 PNL=+2177.20€

**⏳ H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: 40
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=8363 IC=+0.053 PNL=+672.62€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=8363 IC=+0.053 PNL=+672.62€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.096 > 0.08 con n=3697 PNL=+2042.10€
  - _Datos_: n=3697 IC=+0.096 PNL=+2042.10€

**⏳ H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: 80
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: 0/80 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.224 < -0.1 con n=3633 PNL=-318.26€
  - _Datos_: n=3633 IC=-0.224 PNL=-318.26€

**⏳ H-CUSTOM-GBMLATE-ANCHURA-MERCADO** — GBM_LATE_15M BUY_YES — anchura de mercado (retorno concurrente de los otros 3 majors) como modificador secundario
  - _Hipótesis_: Detectado 2026-07-09 buscando explicar por qué varias pérdidas de la racha=4 comparten ventana de 15min. Con precios reales (05-09jul, ~20k muestras BTC) se calculó el retorno concurrente de los OTROS 3 majors desde el inicio de la ventana hasta el momento exacto de la decisión (sin fuga de datos, nunca el precio de cierre) y se cruzó con resultados reales de GBM_LATE_15M BUY_YES: n=802, magnitud media de los otros 3 en deciles limpios y monótonos (decil1 IC=-0.146 hit 35% → decil6-9 IC≈+0.20/+0.29 hit 70-80%). NO es redundante con drift_ventana_pct propio del par (correlación solo 0.26); controlando por el drift propio, la anchura sigue añadiendo información (dentro de drift propio>=0, que es el 90% de los casos: IC=0.127 si anchura baja vs IC=0.211 si anchura alta). Funciona en espejo para BUY_NO (shadow, n=685, anchura negativa 0/3→3/3: hit 47.4%→70.3%). CAVEAT importante: NO explica los clusters concretos de racha=4 en vivo — 6 de los 8 eventos históricos tienen anchura ALTA en al menos 2 de las 4 pérdidas (ver notas de sesión 09-Jul), y el backtest directo sobre trades.csv real (n=105-116) es inconcluso/contradictorio (gate anchura>=3 empeora el PnL real, -2.11€ vs +32.32€ sin filtro — probablemente confusión por mezcla de pares en una muestra pequeña, SOL domina ese bucket y SOL es el par MENOS sensible a esta señal: IC 0.132→0.143 apenas cambia, vs ETH 0.038→0.192). Tratar como MODIFICADOR del filtro primario H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT, no como filtro independiente — ver esa hipótesis para la tabla cruzada. Feature `mercado_anchura_pct` añadida 2026-07-09 en shadow_predict.py (_s_gbm_late), puro logging, no cambia ninguna decisión — empieza a acumular desde cero en predicciones nuevas. ACTUALIZACIÓN 12-Jul (desagregación por activo, n fresco): BTC n=35 ic=+0.392 z=+4.90, ETH n=32 ic=+0.353 z=+4.24, XRP n=31 ic=+0.288 z=+3.41 -- los 3 MUY fuertes y consistentes. SOL sigue siendo el único débil (n=30 ic=+0.094 z=+1.10), confirma el caveat ya escrito arriba (SOL insensible). Con XRP incluido, el patrón deja de ser '3 activos + SOL raro' para ser una regla casi universal salvo SOL -- candidato fuerte para boost Kelly restringido a BTC/ETH/XRP (excluir SOL explícitamente) en vez de aplicar a las 4 monedas por igual.
  - _Umbral_: 100
  - _Acción_: Si confirma con n≥100 IC≥0.20 → boost Kelly cuando mercado_anchura_pct≥0.056 Y prob_yes_modelo≥0.53 (la celda 'doble buena', hit 72.7% retrospectivo). No usar como filtro solo — ver CAVEAT de los clusters de racha en la descripción, y el análisis por-par (SOL insensible) antes de aplicar a las 4 monedas por igual.
  - _Estado_: 0/100 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-OF5M-SMARTMONEY-CONTRARIO** — ORDER_FLOW_5M SOL BUY_NO — smart money EN CONTRA del flujo CEX, no a favor, predice mejor
  - _Hipótesis_: Detectado 11-Jul revisando el backlog quant-desk (reencuadre de ORDER_FLOW_5M). ORDER_FLOW_5M solo dispara BUY_NO (presión vendedora en Binance). Split retrospectivo SOL#5min por smart_money_consensus (ya logueado, nunca cruzado con esta estrategia): cuando el consenso on-chain es BAJISTA (smart_money_consensus<0, 'confirma' la señal CEX) el hit cae a 47.1% (ic_bayes=-0.026, n=17); cuando el consenso es ALCISTA/neutro (smart_money_consensus>=0, CONTRARIO a la señal CEX) el hit sube a 65.0% (ic_bayes=+0.136, n=20, pnl/trade+0.294). Contraintuitivo: la 'confirmación' de dos fuentes empeora, la divergencia mejora. Hipótesis mecánica: el flujo de Binance ya captura la información rápida de 5min; smart money on-chain se mueve más lento (posiciones ya tomadas), así que cuando coincide con el flujo CEX puede ser la MISMA información ya vista dos veces sin dar nada nuevo (o incluso momentum ya agotado), mientras que la divergencia indica que el flujo CEX es el que se está moviendo AHORA sobre información fresca que smart money aún no reflejó. Distinto del cierre 08-Jul del consenso poblacional plano (n=2494, ruido puro) — aquello era agregado sobre TODAS las estrategias; esto es específico del mecanismo de ORDER_FLOW_5M. n=17/20 insuficiente para concluir (regla del proyecto n≥15 es el mínimo absoluto, no un veredicto) — vigilar forward.
  - _Umbral_: 40
  - _Acción_: Si confirma con n≥40 e ic_bayes contrario≥+0.08 (con alineado claramente peor) → boost Kelly en ORDER_FLOW_5M BUY_NO cuando smart_money_consensus>=0; considerar filtro/veto cuando smart_money_consensus<0 y muy negativo (posible señal 'ya vista', sin ventaja).
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-ETH15-SIGMA-ACCEL** — GBM_LATE_15M ETH — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: sigma_ewma_delta_pct = (sigma_h_ewma10-sigma_h)/sigma_h. Verificado ad-hoc n=47: cuando la vol reciente (EWMA half-life 10min) supera la ventana plana, hit sube de 59.5% (agregado ETH) a 66.0%, ic_bayes=+0.153. Efecto NO uniforme entre activos (ver hermanas BTC/XRP) -- desagregar por activo es obligatorio, el agregado GBM_LATE_15M diluye esto a ruido.
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en ETH#15min
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-BTC15-SIGMA-ACCEL** — GBM_LATE_15M BTC — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: mismo mecanismo que ETH (ver H-CUSTOM-ETH15-SIGMA-ACCEL). Verificado ad-hoc n=35: hit sube de 63.6% (agregado BTC) a 68.6%, ic_bayes=+0.176.
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en BTC#15min
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-XRP15-SIGMA-DECEL** — GBM_LATE_15M XRP — vol DESacelerando (EWMA10<=flat) mejora la señal (signo opuesto a ETH/BTC)
  - _Hipótesis_: 12-Jul: XRP muestra el signo CONTRARIO a ETH/BTC -- cuando la vol reciente cae por debajo de la ventana plana, hit sube de 63.9% (agregado XRP) a 68.8%, ic_bayes=+0.180 (n=48). Cuando acelera, hit CAE a 57.1%. Confirma que este feature no puede tratarse con un umbral global -- cada activo necesita su propio signo. REFUTADA 13-Jul: recalculado con n=61 (más del doble del n original) usando el mismo método riguroso (percentiles + permutación 20k) que confirmó BTC/SOL/ETH -- el signo se INVIRTIÓ: decel (sigma<0) da IC=-0.065 n=21 (malo), accel (sigma>=0) da IC=+0.071 n=40 (bueno). XRP en realidad tiene el MISMO signo que BTC/ETH (sigma alto=bueno), solo que más débil -- coherente con el patrón ganador ya auto-descubierto por postmortem (sigma_ewma_delta_pct>5.563, ic_patron=+0.20 n=18, mismo signo). El hallazgo ad-hoc del 12-Jul con n=48 no replicó con más datos -- probable ruido de una muestra menor/distinta. Ver idea_estrategia_mercado_bajista... no, ver project_sigma_filtro_sol_xrp_no_promociona_13jul (memoria) para el detalle completo.
  - _Umbral_: 40
  - _Acción_: REFUTADA -- no implementar kelly_boost por sigma<0 en XRP. El signo correcto es el opuesto (sigma alto=bueno), ya cubierto por el patron_ganador automático de postmortem sobre GBM_LATE_15M#XRP#15min -- no hace falta ninguna acción manual adicional.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-SMARTMONEY-FAVORITO-SOL** — FAVORITO_CONFIRMADO SOL — alineado con smart_money_consensus bate ir en contra (REABRE hallazgo cerrado 08-Jul)
  - _Hipótesis_: 12-Jul: el cierre 08-Jul (n=2494, sin desagregar por estrategia/activo) encontro ruido puro. Desagregando por estrategia+activo (mecanismo nuevo): FAVORITO_CONFIRMADO#SOL alineado con smart_money_consensus (|consenso|>0.1, n_wallets>=3) hit=78.4% (n=37) vs contrario hit=52.4% (n=42), z=+2.41. GBM_LATE_15M tambien muestra el mismo signo en BTC/ETH/XRP (z=0.86-1.61, mas debil) pero SOL plano ahi -- inconsistencia entre estrategias que hay que entender antes de actuar.
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 y z>=2 -> considerar boost condicionado a alineacion con smart_money_consensus en FAVORITO_CONFIRMADO#SOL
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-FAVORITO-SOL-ALTACONVICCION** — FAVORITO_CONFIRMADO SOL BUY_YES alta conviccion (py_entrada alto) — UNICO caso positivo en fill-ability de hoy
  - _Hipótesis_: 12-Jul: auditoria de fill-ability de las 8 candidatas encontro las 8 negativas en agregado. Pero desagregando FAVORITO_CONFIRMADO por activo (mecanismo nuevo, no mirado hasta hoy): SOL#BUY_YES con py_entrada>=0.665-0.695 da pnl/trade POSITIVO en el subconjunto fillable real (+0.12 a +0.41 EUR/trade, n=6-17 segun el corte exacto) -- unico resultado positivo de toda la auditoria de candidatas. n todavia bajo, necesita mas dato antes de proponer nada.
  - _Umbral_: 40
  - _Acción_: Seguir acumulando snapshots candidato_evaluacion para SOL#15min#BUY_YES en FAVORITO_CONFIRMADO; re-evaluar fill-ability con n>=40 antes de proponer whitelist
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM18H-XRP-EXCEPCION** — UPDOWN_GBM XRP a las 18h UTC -- puede estar mal incluida en el blacklist horario global
  - _Hipótesis_: 12-Jul: gbm_blacklist_hours_auto=[9,10,18] bloquea GBM en las 4 monedas a las 18h. Desagregando por activo (h9/h10 no tienen dato retrospectivo -- el propio blacklist impide que se genere): BTC ic=-0.140 (n=48), ETH ic=-0.136 (n=42), SOL ic=-0.167 (n=22) consistentes con el bloqueo, pero XRP ic=+0.100 (n=23) -- signo OPUESTO. El bloqueo agregado puede estar sobre-bloqueando XRP especificamente.
  - _Umbral_: n>=40 y IC>0.08
  - _Acción_: Si confirma con n>=40 IC>0.08 -> considerar excepcion de XRP en gbm_blacklist_hours_auto para la hora 18 (shadow puro, UPDOWN_GBM no esta live)
  - _Estado_: n=74 IC=+0.026 PNL=+9.96€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=74 IC=+0.026 PNL=+9.96€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.102 n=1824) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=1824 IC=+0.102 PNL=+400.39€

**⏳ H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.410 n=597) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=597 IC=+0.410 PNL=+854.62€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=14999 IC=+0.185 PNL=-1546.42€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=14999 IC=+0.185 PNL=-1546.42€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.223 > 0.1 con n=240 PNL=+161.07€
  - _Datos_: n=240 IC=+0.223 PNL=+161.07€
