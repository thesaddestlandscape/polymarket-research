# Hipótesis automáticas — 2026-11-14 23:05 UTC
_Generado por shadow_postmortem.py sobre 1339224 resoluciones (PNL=+185556.20€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.5` → IC=-0.317 (n=195)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.118 (n=710)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.196 (n=1023)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` > 0.505 (IC base=+0.123)

- **PATRÓN** `n_total_lado` > `62.0` → IC=+0.183 (n=326)

  - _Acción_: Kelly boost +0.91€ cuando `n_total_lado` > 62.0 (IC base=+0.123)

- **PATRÓN** `banda_hit_calibrado` > `0.8128` → IC=+0.274 (n=440)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8128 (IC base=+0.123)

- **PATRÓN** `banda_z` > `8.502` → IC=+0.193 (n=324)

  - _Acción_: Kelly boost +0.97€ cuando `banda_z` > 8.502 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.136 (n=363)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 17.0 (IC base=+0.123)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.124 (n=697)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 12.0 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.136 (n=1060)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.123)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.302 (n=165)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=505)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.193 (n=888)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.505 (IC base=+0.124)

- **PATRÓN** `n_total_lado` > `65.0` → IC=+0.181 (n=283)

  - _Acción_: Kelly boost +0.90€ cuando `n_total_lado` > 65.0 (IC base=+0.124)

- **PATRÓN** `banda_hit_calibrado` > `0.8124` → IC=+0.276 (n=382)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8124 (IC base=+0.124)

- **PATRÓN** `banda_z` > `8.822` → IC=+0.206 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 8.822 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.133 (n=761)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 8.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.125 (n=595)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 12.0 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.131 (n=960)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.01 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `3094.8617` → IC=+0.126 (n=750)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 3094.8617 (IC base=+0.124)

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
  - _Potencial_: sin este filtro IC_bueno=+0.113 (n=109)

- **FILTRO** `hora_utc` < `10.0` → IC=-0.157 (n=33)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=108)

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
- **FILTRO** `ballenas_wallet_edge_medio` < `2.833` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `ballenas_wallet_edge_medio` < 2.833
  - _Potencial_: sin este filtro IC_bueno=+0.375 (n=6)

- **PATRÓN** `py_entrada` > `0.495` → IC=+0.154 (n=50)

  - _Acción_: Kelly boost +0.77€ cuando `py_entrada` > 0.495 (IC base=+0.153)

- **PATRÓN** `n_ballena_banda` > `26.0` → IC=+0.241 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `n_ballena_banda` > 26.0 (IC base=+0.153)

- **PATRÓN** `n_total_lado` > `38.0` → IC=+0.232 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 38.0 (IC base=+0.153)

- **PATRÓN** `banda_hit_calibrado` > `0.6072` → IC=+0.154 (n=24)

  - _Acción_: Kelly boost +0.77€ cuando `banda_hit_calibrado` > 0.6072 (IC base=+0.153)

- **PATRÓN** `banda_z` > `2.517` → IC=+0.227 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 2.517 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.225 (n=38)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.153)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.154 (n=24)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 7.0 (IC base=+0.153)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.198 (n=41)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.02 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `2738.3784` → IC=+0.203 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2738.3784 (IC base=+0.153)

### BALLENAS_TARDIAS
- **FILTRO** `restante_s_al_confirmar` < `131.78` → IC=-0.217 (n=12129)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 131.78
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=36393)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `125.07` → IC=-0.256 (n=1217)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 125.07
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=3654)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `115.68` → IC=-0.277 (n=1233)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 115.68
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=3699)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `restante_s_al_confirmar` < `116.24` → IC=-0.166 (n=3324)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 116.24
  - _Potencial_: sin este filtro IC_bueno=-0.000 (n=9975)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `151.9` → IC=-0.238 (n=3305)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 151.9
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=9917)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `128.27` → IC=-0.267 (n=2285)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 128.27
  - _Potencial_: sin este filtro IC_bueno=-0.091 (n=6856)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.209 (n=28550)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.103)

- **PATRÓN** `libro_liquidez` > `8197.8863` → IC=+0.156 (n=2360)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 8197.8863 (IC base=+0.103)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.128 (n=24788)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.131 (n=29959)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.125)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.225 (n=22565)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.140 (n=8448)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `6445.5424` → IC=+0.142 (n=3275)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 6445.5424 (IC base=+0.125)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.185 (n=2200)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.177)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.358 (n=751)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.177)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.180 (n=2691)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.01 (IC base=+0.177)

- **PATRÓN** `libro_liquidez` > `16308.4461` → IC=+0.180 (n=699)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 16308.4461 (IC base=+0.177)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.185 (n=1914)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 7.0 (IC base=+0.178)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.181 (n=2142)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 17.0 (IC base=+0.178)

- **PATRÓN** `py_entrada` < `0.295` → IC=+0.312 (n=981)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.295 (IC base=+0.178)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.181 (n=2744)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.01 (IC base=+0.178)

- **PATRÓN** `libro_liquidez` > `16073.2055` → IC=+0.184 (n=708)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 16073.2055 (IC base=+0.178)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.61` → IC=+0.167 (n=623)

  - _Acción_: Kelly boost +0.84€ cuando `py_entrada` > 0.61 (IC base=+0.075)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.148 (n=1465)

  - _Acción_: Kelly boost +0.74€ cuando `py_entrada` < 0.44 (IC base=+0.086)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.170 (n=5174)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 6.0 (IC base=+0.167)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.172 (n=4595)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 15.0 (IC base=+0.167)

- **PATRÓN** `py_entrada` > `0.77` → IC=+0.375 (n=1798)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.77 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.208 (n=2473)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.201)

- **PATRÓN** `py_entrada` < `0.275` → IC=+0.332 (n=958)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.275 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.204 (n=2877)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.201)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.142 (n=662)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 15.0 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.143 (n=1189)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 15.0 (IC base=+0.139)

- **PATRÓN** `py_entrada` > `0.675` → IC=+0.255 (n=455)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.675 (IC base=+0.139)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.142 (n=1131)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.156 (n=155)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.075)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.249 (n=963)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.226)

- **PATRÓN** `py_entrada` > `0.83` → IC=+0.420 (n=1342)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.83 (IC base=+0.226)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.157 (n=738)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 7.0 (IC base=+0.145)

- **PATRÓN** `py_entrada` < `0.345` → IC=+0.278 (n=717)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.345 (IC base=+0.145)

### FAVORITO_CONFIRMADO#SOL#60min
- **FILTRO** `libro_liquidez` < `955.8819` → IC=-0.121 (n=159)

  - _Acción_: SKIP cuando `libro_liquidez` < 955.8819
  - _Potencial_: sin este filtro IC_bueno=+0.066 (n=325)

- **PATRÓN** `py_entrada` > `0.55` → IC=+0.166 (n=468)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` > 0.55 (IC base=+0.049)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.142 (n=495)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 17.0 (IC base=+0.123)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.252 (n=450)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.123)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` < `7.0` → IC=-0.257 (n=113)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.254 (n=116)

- **FILTRO** `py_entrada` > `0.755` → IC=-0.299 (n=152)

  - _Acción_: SKIP cuando `py_entrada` > 0.755
  - _Potencial_: sin este filtro IC_bueno=-0.171 (n=77)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.200 (n=24789)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.194)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.196 (n=20883)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 15.0 (IC base=+0.194)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.228 (n=7830)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.194)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.338 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.194)

- **PATRÓN** `libro_liquidez` > `4915.142` → IC=+0.338 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4915.142 (IC base=+0.194)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.172 (n=5652)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 5.0 (IC base=+0.167)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.177 (n=5597)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` < 0.74 (IC base=+0.167)

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

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.211 (n=3394)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.207)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.210 (n=2425)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.207)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.247 (n=1666)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.207)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.181 (n=5527)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 5.0 (IC base=+0.174)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.176 (n=4676)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 15.0 (IC base=+0.174)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.175 (n=5665)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` < 0.73 (IC base=+0.174)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.182 (n=4332)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` > 0.71 (IC base=+0.174)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.257 (n=4383)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.251)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.253 (n=3901)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.251)

- **PATRÓN** `py_entrada` > `0.8` → IC=+0.364 (n=1483)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.8 (IC base=+0.251)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.306 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.251)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.189 (n=5410)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.185)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.188 (n=4573)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 15.0 (IC base=+0.185)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.198 (n=1803)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` > 0.73 (IC base=+0.185)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.430 (n=986)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.426)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.427 (n=977)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.426)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.438 (n=993)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.426)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.432 (n=1053)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.426)

- **PATRÓN** `libro_liquidez` > `4644.67` → IC=+0.442 (n=634)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4644.67 (IC base=+0.426)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.440 (n=399)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.439)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.442 (n=410)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.439)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.448 (n=440)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.439)

- **PATRÓN** `libro_liquidez` > `12510.8319` → IC=+0.444 (n=353)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12510.8319 (IC base=+0.439)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.432 (n=393)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.425)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.428 (n=388)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.425)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.443 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.425)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.430 (n=442)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.425)

- **PATRÓN** `libro_liquidez` > `4796.5955` → IC=+0.431 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4796.5955 (IC base=+0.425)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.401 (n=149)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.398)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.404 (n=144)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.398)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.413 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.398)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `14.0` → IC=-0.324 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.269 (n=37)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.263 (n=36)

- **FILTRO** `libro_liquidez` < `3014.3014` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `libro_liquidez` < 3014.3014
  - _Potencial_: sin este filtro IC_bueno=-0.284 (n=35)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.208 (n=27934)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.239 (n=32521)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.199)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.186 (n=4865)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 18.0 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.178 (n=10360)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 12.0 (IC base=+0.177)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.206 (n=6917)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.177)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.225 (n=13572)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.223)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.285 (n=4530)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.223)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.183 (n=13604)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 7.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.197 (n=11506)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` > 0.72 (IC base=+0.180)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.855` → IC=-0.357 (n=19)

  - _Acción_: SKIP cuando `py_entrada` < 0.855
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.228 (n=4555)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.221 (n=5190)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.218)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.254 (n=7481)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.218)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **FILTRO** `hora_utc` > `3.0` → IC=-0.278 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.214 (n=4610)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.204)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.256 (n=4693)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.204)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.203 (n=4646)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.195)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.197 (n=5360)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 6.0 (IC base=+0.195)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.244 (n=5559)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.195)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.194 (n=11686)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.141 (n=12400)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `3.42` → IC=+0.139 (n=14286)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 3.42 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.193 (n=5701)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.144 (n=5609)

  - _Acción_: Kelly boost +0.72€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.124 (n=7147)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 7.0 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `4.05` → IC=+0.141 (n=7097)

  - _Acción_: Kelly boost +0.70€ cuando `lag_apertura_s` < 4.05 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.195 (n=5985)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.138 (n=7530)

  - _Acción_: Kelly boost +0.69€ cuando `restante_min` > 4.95 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `3.1` → IC=+0.138 (n=7163)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 3.1 (IC base=+0.117)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.305 (n=1420)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.292)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.387 (n=731)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.292)

- **PATRÓN** `libro_liquidez` > `3979.7019` → IC=+0.292 (n=900)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3979.7019 (IC base=+0.292)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.284 (n=954)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.281)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.367 (n=314)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.281)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.314 (n=693)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.295)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.299 (n=1014)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.295)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.392 (n=349)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.295)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` < `16.0` → IC=+0.369 (n=97)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.347)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.393 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.347)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.384 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.347)

- **PATRÓN** `libro_liquidez` > `745.0217` → IC=+0.378 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 745.0217 (IC base=+0.347)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.440 (n=968)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.437)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.443 (n=931)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.437)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.438 (n=451)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.433)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.437 (n=315)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.433)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.432 (n=467)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.433)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.442 (n=342)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.433)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.449 (n=312)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.440)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.439 (n=394)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.440)

- **PATRÓN** `py_entrada` > `0.91` → IC=+0.444 (n=460)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.91 (IC base=+0.440)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.421 (n=36)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.407)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.397 (n=27)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 13.0 (IC base=+0.407)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.447 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.407)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION
- **FILTRO** `hora_utc` < `5.0` → IC=-0.269 (n=24)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=109)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.265 (n=66)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=67)

- **FILTRO** `py_entrada` > `0.715` → IC=-0.351 (n=65)

  - _Acción_: SKIP cuando `py_entrada` > 0.715
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=68)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.242 (n=64)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.190 (n=69)

- **FILTRO** `libro_liquidez` < `1798.9075` → IC=-0.233 (n=99)

  - _Acción_: SKIP cuando `libro_liquidez` < 1798.9075
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=34)

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
- **FILTRO** `hora_utc` < `5.0` → IC=-0.269 (n=24)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=109)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.265 (n=66)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=67)

- **FILTRO** `py_entrada` > `0.715` → IC=-0.351 (n=65)

  - _Acción_: SKIP cuando `py_entrada` > 0.715
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=68)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.242 (n=64)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.190 (n=69)

- **FILTRO** `libro_liquidez` < `1798.9075` → IC=-0.233 (n=99)

  - _Acción_: SKIP cuando `libro_liquidez` < 1798.9075
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=34)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4867` → IC=+0.139 (n=18402)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.4867 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.128 (n=18630)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 6.0 (IC base=+0.123)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.125 (n=12799)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 12.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` > `0.9762` → IC=+0.246 (n=6135)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9762 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` > `0.8067` → IC=+0.281 (n=976)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8067 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.478` → IC=+0.188 (n=9218)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 3.478 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` > `0.6957` → IC=+0.268 (n=4962)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6957 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` > `0.3043` → IC=+0.250 (n=1893)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3043 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` > `2.7502` → IC=+0.234 (n=4424)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7502 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.136 (n=9060)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `4690.9772` → IC=+0.149 (n=6134)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 4690.9772 (IC base=+0.123)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.123 (n=11562)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0063 (IC base=+0.086)

- **PATRÓN** `ibs_20min` < `0.5639` → IC=+0.146 (n=23118)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.5639 (IC base=+0.086)

- **PATRÓN** `dist_vwap_pct` > `0.6325` → IC=+0.191 (n=1482)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.6325 (IC base=+0.086)

- **PATRÓN** `volumen_regimen` < `0.8592` → IC=+0.195 (n=6343)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` < 0.8592 (IC base=+0.086)

- **PATRÓN** `volumen_pendiente_norm` > `0.296` → IC=+0.236 (n=2330)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.296 (IC base=+0.086)

- **PATRÓN** `volumen_spike_ratio` > `2.6669` → IC=+0.215 (n=5379)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6669 (IC base=+0.086)

- **PATRÓN** `ballena_activa_n` < `99.0` → IC=+0.230 (n=16050)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 99.0 (IC base=+0.086)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `drift_60min` |x|≤ `0.3717` → IC=+0.212 (n=3913)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3717 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.227 (n=1902)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.210)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.210 (n=2623)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `0.9846` → IC=+0.277 (n=1774)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9846 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.799` → IC=+0.293 (n=922)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.799 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.2344` → IC=+0.254 (n=689)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2344 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `1.4385` → IC=+0.211 (n=3753)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4385 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.222 (n=4347)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `2029.23` → IC=+0.210 (n=1305)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2029.23 (IC base=+0.210)

- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.221 (n=3565)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 25.0 (IC base=+0.210)

- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.250 (n=1579)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0094 (IC base=+0.243)

- **PATRÓN** `drift_60min` |x|≤ `0.0915` → IC=+0.276 (n=1161)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0915 (IC base=+0.243)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.244 (n=3629)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.243)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.251 (n=1595)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.243)

- **PATRÓN** `ibs_20min` < `0.5664` → IC=+0.260 (n=3482)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5664 (IC base=+0.243)

- **PATRÓN** `volumen_pendiente_norm` < `0.0717` → IC=+0.246 (n=2996)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0717 (IC base=+0.243)

- **PATRÓN** `volumen_pendiente_norm` > `0.2908` → IC=+0.253 (n=468)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2908 (IC base=+0.243)

- **PATRÓN** `volumen_spike_ratio` < `1.4486` → IC=+0.245 (n=1110)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4486 (IC base=+0.243)

- **PATRÓN** `volumen_spike_ratio` > `1.8623` → IC=+0.247 (n=2219)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8623 (IC base=+0.243)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.245 (n=4035)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.243)

- **PATRÓN** `libro_liquidez` > `1777.0438` → IC=+0.249 (n=2321)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1777.0438 (IC base=+0.243)

- **PATRÓN** `ballena_activa_n` < `6.0` → IC=+0.244 (n=1199)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 6.0 (IC base=+0.243)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.237 (n=1107)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.223)

- **PATRÓN** `drift_60min` |x|≤ `0.1114` → IC=+0.250 (n=1458)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1114 (IC base=+0.223)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.235 (n=3472)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.223)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.225 (n=2354)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.223)

- **PATRÓN** `ibs_20min` > `0.8983` → IC=+0.257 (n=1104)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8983 (IC base=+0.223)

- **PATRÓN** `dist_vwap_pct` > `0.1871` → IC=+0.234 (n=1445)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1871 (IC base=+0.223)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.817` → IC=+0.263 (n=483)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.817 (IC base=+0.223)

- **PATRÓN** `volumen_regimen` > `0.6976` → IC=+0.231 (n=2957)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6976 (IC base=+0.223)

- **PATRÓN** `volumen_pendiente_norm` > `0.2781` → IC=+0.270 (n=458)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2781 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` > `2.447` → IC=+0.249 (n=1090)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.447 (IC base=+0.223)

- **PATRÓN** `libro_liquidez` > `15907.6891` → IC=+0.224 (n=1104)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15907.6891 (IC base=+0.223)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.154 (n=3580)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0066 (IC base=+0.134)

- **PATRÓN** `drift_60min` |x|≤ `0.079` → IC=+0.159 (n=1194)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.079 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.155 (n=1345)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 17.0 (IC base=+0.134)

- **PATRÓN** `ibs_20min` < `0.7058` → IC=+0.172 (n=3577)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.7058 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.991` → IC=+0.141 (n=3268)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 3.991 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` < `0.6286` → IC=+0.154 (n=1193)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.6286 (IC base=+0.134)

- **PATRÓN** `volumen_pendiente_norm` > `0.0974` → IC=+0.158 (n=1316)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` > 0.0974 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` < `2.4414` → IC=+0.143 (n=3449)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.4414 (IC base=+0.134)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.134 (n=4647)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.134)

- **PATRÓN** `ballena_activa_n` < `173.0` → IC=+0.193 (n=1133)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 173.0 (IC base=+0.134)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0128` → IC=+0.210 (n=1389)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0128 (IC base=+0.194)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.202 (n=4366)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.194)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.259 (n=1610)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.194)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.966` → IC=+0.282 (n=915)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.966 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` < `0.0972` → IC=+0.196 (n=3722)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` < 0.0972 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` > `0.3519` → IC=+0.225 (n=536)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3519 (IC base=+0.194)

- **PATRÓN** `volumen_spike_ratio` > `2.7279` → IC=+0.211 (n=1839)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7279 (IC base=+0.194)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.198 (n=5028)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.04 (IC base=+0.194)

- **PATRÓN** `libro_liquidez` > `2005.4352` → IC=+0.203 (n=1384)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2005.4352 (IC base=+0.194)

- **PATRÓN** `sigma_h` < `0.0112` → IC=+0.225 (n=3393)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0112 (IC base=+0.222)

- **PATRÓN** `drift_60min` |x|≤ `0.1781` → IC=+0.235 (n=1698)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1781 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.245 (n=1471)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.227 (n=1742)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` < `0.0476` → IC=+0.271 (n=1290)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0476 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.76` → IC=+0.262 (n=418)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.76 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` > `0.3469` → IC=+0.258 (n=561)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3469 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` > `2.1593` → IC=+0.232 (n=2475)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1593 (IC base=+0.222)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.224 (n=1927)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.222)

- **PATRÓN** `libro_liquidez` > `1984.4248` → IC=+0.227 (n=1285)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1984.4248 (IC base=+0.222)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.227 (n=3655)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 23.0 (IC base=+0.222)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.177 (n=215)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.066 (n=5018)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.147 (n=684)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0039 (IC base=+0.061)

- **PATRÓN** `ibs_20min` > `0.9422` → IC=+0.235 (n=681)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9422 (IC base=+0.061)

- **PATRÓN** `dist_vwap_pct` > `0.1424` → IC=+0.341 (n=463)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1424 (IC base=+0.061)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.12` → IC=+0.208 (n=1494)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.12 (IC base=+0.061)

- **PATRÓN** `volumen_regimen` > `1.2486` → IC=+0.358 (n=273)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2486 (IC base=+0.061)

- **PATRÓN** `volumen_pendiente_norm` < `0.1672` → IC=+0.342 (n=661)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1672 (IC base=+0.061)

- **PATRÓN** `volumen_pendiente_norm` > `0.3037` → IC=+0.341 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3037 (IC base=+0.061)

- **PATRÓN** `volumen_spike_ratio` < `1.5458` → IC=+0.353 (n=351)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5458 (IC base=+0.061)

- **PATRÓN** `volumen_spike_ratio` > `2.2887` → IC=+0.340 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2887 (IC base=+0.061)

- **PATRÓN** `ballena_activa_n` < `142.0` → IC=+0.342 (n=810)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 142.0 (IC base=+0.061)

- **PATRÓN** `ibs_20min` < `0.087` → IC=+0.185 (n=1309)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.087 (IC base=+0.056)

- **PATRÓN** `dist_vwap_pct` > `0.5439` → IC=+0.163 (n=422)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 0.5439 (IC base=+0.056)

- **PATRÓN** `volumen_regimen` < `1.0026` → IC=+0.162 (n=2223)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.0026 (IC base=+0.056)

- **PATRÓN** `volumen_pendiente_norm` > `0.2793` → IC=+0.209 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2793 (IC base=+0.056)

- **PATRÓN** `volumen_spike_ratio` > `1.5053` → IC=+0.162 (n=2175)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.5053 (IC base=+0.056)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.182 (n=149)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=799)

- **FILTRO** `ibs_20min` < `0.2667` → IC=-0.176 (n=236)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2667
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=712)

- **FILTRO** `ibs_20min` > `0.2` → IC=-0.129 (n=4888)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2
  - _Potencial_: sin este filtro IC_bueno=+0.156 (n=2464)

- **FILTRO** `sigma_ewma_delta_pct` > `8.302` → IC=-0.230 (n=794)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.302
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=6558)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.181 (n=324)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.75 (IC base=+0.022)

- **PATRÓN** `dist_vwap_pct` > `0.9797` → IC=+0.283 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9797 (IC base=+0.022)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.925` → IC=+0.159 (n=221)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 4.925 (IC base=+0.022)

- **PATRÓN** `volumen_regimen` > `0.6233` → IC=+0.288 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6233 (IC base=+0.022)

- **PATRÓN** `volumen_pendiente_norm` < `0.0791` → IC=+0.282 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0791 (IC base=+0.022)

- **PATRÓN** `volumen_spike_ratio` < `2.1989` → IC=+0.288 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1989 (IC base=+0.022)

- **PATRÓN** `volumen_spike_ratio` > `1.5401` → IC=+0.265 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5401 (IC base=+0.022)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.274 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 40.0 (IC base=+0.022)

- **PATRÓN** `ibs_20min` < `0.2` → IC=+0.156 (n=2464)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.2 (IC base=-0.034)

- **PATRÓN** `dist_vwap_pct` > `0.2308` → IC=+0.286 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2308 (IC base=-0.034)

- **PATRÓN** `volumen_regimen` < `0.6993` → IC=+0.296 (n=483)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6993 (IC base=-0.034)

- **PATRÓN** `volumen_regimen` > `1.0502` → IC=+0.286 (n=497)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0502 (IC base=-0.034)

- **PATRÓN** `volumen_pendiente_norm` > `0.0787` → IC=+0.310 (n=498)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0787 (IC base=-0.034)

- **PATRÓN** `volumen_spike_ratio` < `2.4559` → IC=+0.298 (n=1027)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4559 (IC base=-0.034)

- **PATRÓN** `volumen_spike_ratio` > `1.4108` → IC=+0.291 (n=1027)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4108 (IC base=-0.034)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `ibs_20min` < `0.7905` → IC=-0.157 (n=3762)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7905
  - _Potencial_: sin este filtro IC_bueno=+0.135 (n=1939)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.173 (n=1201)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=4500)

- **FILTRO** `ibs_20min` > `0.7352` → IC=-0.190 (n=1972)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7352
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=5919)

- **PATRÓN** `ibs_20min` > `0.7905` → IC=+0.135 (n=1939)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` > 0.7905 (IC base=-0.057)

- **PATRÓN** `dist_vwap_pct` > `1.0036` → IC=+0.350 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0036 (IC base=-0.057)

- **PATRÓN** `dist_vwap_pct` < `0.2513` → IC=+0.299 (n=1032)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2513 (IC base=-0.057)

- **PATRÓN** `volumen_regimen` > `0.7048` → IC=+0.317 (n=1014)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7048 (IC base=-0.057)

- **PATRÓN** `volumen_pendiente_norm` < `0.108` → IC=+0.301 (n=1083)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.108 (IC base=-0.057)

- **PATRÓN** `volumen_pendiente_norm` > `0.1706` → IC=+0.303 (n=297)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1706 (IC base=-0.057)

- **PATRÓN** `volumen_spike_ratio` < `1.5808` → IC=+0.305 (n=490)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5808 (IC base=-0.057)

- **PATRÓN** `volumen_spike_ratio` > `2.5191` → IC=+0.315 (n=371)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5191 (IC base=-0.057)

- **PATRÓN** `dist_vwap_pct` > `1.0666` → IC=+0.280 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0666 (IC base=+0.006)

- **PATRÓN** `volumen_regimen` < `0.6412` → IC=+0.273 (n=772)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6412 (IC base=+0.006)

- **PATRÓN** `volumen_regimen` > `1.2057` → IC=+0.288 (n=772)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2057 (IC base=+0.006)

- **PATRÓN** `volumen_pendiente_norm` > `0.2847` → IC=+0.290 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2847 (IC base=+0.006)

- **PATRÓN** `volumen_spike_ratio` < `2.4775` → IC=+0.266 (n=2190)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4775 (IC base=+0.006)

- **PATRÓN** `volumen_spike_ratio` > `1.4355` → IC=+0.272 (n=2190)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4355 (IC base=+0.006)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0108` → IC=+0.193 (n=7998)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` > 0.0108 (IC base=+0.087)

- **PATRÓN** `ibs_20min` > `0.9665` → IC=+0.311 (n=7992)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9665 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` > `0.9409` → IC=+0.302 (n=1626)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9409 (IC base=+0.087)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.47` → IC=+0.168 (n=10755)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 3.47 (IC base=+0.087)

- **PATRÓN** `volumen_regimen` > `0.6923` → IC=+0.279 (n=7917)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6923 (IC base=+0.087)

- **PATRÓN** `volumen_pendiente_norm` > `0.2925` → IC=+0.296 (n=1978)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2925 (IC base=+0.087)

- **PATRÓN** `volumen_spike_ratio` > `2.6443` → IC=+0.286 (n=4638)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6443 (IC base=+0.087)

- **PATRÓN** `ballena_activa_n` < `89.0` → IC=+0.309 (n=13540)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 89.0 (IC base=+0.087)

- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.161 (n=7749)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0104 (IC base=+0.085)

- **PATRÓN** `ibs_20min` < `0.5185` → IC=+0.173 (n=20461)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.5185 (IC base=+0.085)

- **PATRÓN** `volumen_regimen` < `0.6973` → IC=+0.281 (n=3430)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6973 (IC base=+0.085)

- **PATRÓN** `volumen_regimen` > `1.1879` → IC=+0.287 (n=2598)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1879 (IC base=+0.085)

- **PATRÓN** `volumen_pendiente_norm` > `0.2946` → IC=+0.330 (n=1728)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2946 (IC base=+0.085)

- **PATRÓN** `volumen_spike_ratio` < `1.4528` → IC=+0.306 (n=3842)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4528 (IC base=+0.085)

- **PATRÓN** `volumen_spike_ratio` > `2.2801` → IC=+0.305 (n=5225)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2801 (IC base=+0.085)

- **PATRÓN** `ballena_activa_n` < `72.0` → IC=+0.312 (n=11514)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 72.0 (IC base=+0.085)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.8034` → IC=-0.137 (n=4257)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8034
  - _Potencial_: sin este filtro IC_bueno=+0.303 (n=2194)

- **FILTRO** `ibs_20min` > `0.7108` → IC=-0.237 (n=1429)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7108
  - _Potencial_: sin este filtro IC_bueno=+0.055 (n=4295)

- **FILTRO** `sigma_ewma_delta_pct` > `4.08` → IC=-0.237 (n=1227)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.08
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=4497)

- **PATRÓN** `ibs_20min` > `0.8034` → IC=+0.303 (n=2194)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8034 (IC base=+0.013)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.962` → IC=+0.188 (n=2146)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 2.962 (IC base=+0.013)

- **PATRÓN** `volumen_pendiente_norm` > `0.2287` → IC=+0.332 (n=409)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2287 (IC base=+0.013)

- **PATRÓN** `volumen_spike_ratio` < `1.4486` → IC=+0.283 (n=681)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4486 (IC base=+0.013)

- **PATRÓN** `volumen_spike_ratio` > `2.2427` → IC=+0.306 (n=925)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2427 (IC base=+0.013)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.318 (n=1421)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.013)

- **PATRÓN** `ibs_20min` < `0.1727` → IC=+0.174 (n=1433)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.1727 (IC base=-0.018)

- **PATRÓN** `volumen_pendiente_norm` < `0.1514` → IC=+0.397 (n=1169)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1514 (IC base=-0.018)

- **PATRÓN** `volumen_spike_ratio` < `1.5386` → IC=+0.418 (n=496)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5386 (IC base=-0.018)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.393 (n=1161)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 22.0 (IC base=-0.018)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.3026` → IC=+0.226 (n=746)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3026 (IC base=+0.010)

- **PATRÓN** `volumen_regimen` < `1.1961` → IC=+0.211 (n=2352)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1961 (IC base=+0.010)

- **PATRÓN** `volumen_regimen` > `0.6948` → IC=+0.219 (n=2101)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6948 (IC base=+0.010)

- **PATRÓN** `volumen_pendiente_norm` > `0.2747` → IC=+0.244 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2747 (IC base=+0.010)

- **PATRÓN** `volumen_spike_ratio` < `1.4165` → IC=+0.230 (n=775)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4165 (IC base=+0.010)

- **PATRÓN** `volumen_spike_ratio` > `2.4707` → IC=+0.212 (n=775)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4707 (IC base=+0.010)

- **PATRÓN** `ballena_activa_n` < `257.0` → IC=+0.243 (n=1546)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 257.0 (IC base=+0.010)

- **PATRÓN** `volumen_regimen` > `1.0184` → IC=+0.267 (n=766)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0184 (IC base=+0.000)

- **PATRÓN** `volumen_pendiente_norm` > `0.2701` → IC=+0.307 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2701 (IC base=+0.000)

- **PATRÓN** `volumen_spike_ratio` < `1.5263` → IC=+0.263 (n=720)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5263 (IC base=+0.000)

- **PATRÓN** `volumen_spike_ratio` > `2.1516` → IC=+0.265 (n=742)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1516 (IC base=+0.000)

- **PATRÓN** `ballena_activa_n` < `182.0` → IC=+0.281 (n=550)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 182.0 (IC base=+0.000)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.323 (n=1516)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0113 (IC base=+0.284)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.294 (n=3343)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.284)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.326 (n=1807)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.284)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.589` → IC=+0.306 (n=2251)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.589 (IC base=+0.284)

- **PATRÓN** `volumen_pendiente_norm` < `0.0974` → IC=+0.296 (n=2937)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0974 (IC base=+0.284)

- **PATRÓN** `volumen_spike_ratio` > `1.6035` → IC=+0.290 (n=3245)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6035 (IC base=+0.284)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.292 (n=4013)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.284)

- **PATRÓN** `libro_liquidez` > `2007.5584` → IC=+0.295 (n=1113)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2007.5584 (IC base=+0.284)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.305 (n=2052)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 14.0 (IC base=+0.284)

- **PATRÓN** `sigma_h` > `0.0091` → IC=+0.334 (n=2043)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0091 (IC base=+0.307)

- **PATRÓN** `drift_60min` |x|≤ `0.1807` → IC=+0.325 (n=1349)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1807 (IC base=+0.307)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.328 (n=1183)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.307)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.310 (n=1380)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.307)

- **PATRÓN** `ibs_20min` > `0.1481` → IC=+0.318 (n=2045)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1481 (IC base=+0.307)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.104` → IC=+0.315 (n=365)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.104 (IC base=+0.307)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.425` → IC=+0.308 (n=3174)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.425 (IC base=+0.307)

- **PATRÓN** `volumen_pendiente_norm` < `0.1987` → IC=+0.308 (n=3028)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1987 (IC base=+0.307)

- **PATRÓN** `volumen_pendiente_norm` > `0.3447` → IC=+0.318 (n=499)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3447 (IC base=+0.307)

- **PATRÓN** `volumen_spike_ratio` > `2.7444` → IC=+0.322 (n=1343)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7444 (IC base=+0.307)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.308 (n=1536)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.307)

- **PATRÓN** `libro_liquidez` > `1983.798` → IC=+0.315 (n=1022)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1983.798 (IC base=+0.307)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.312 (n=2606)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 22.0 (IC base=+0.307)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7174` → IC=-0.179 (n=1512)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7174
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=4540)

- **PATRÓN** `dist_vwap_pct` > `0.1469` → IC=+0.237 (n=1070)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1469 (IC base=+0.022)

- **PATRÓN** `volumen_regimen` < `1.1591` → IC=+0.239 (n=2163)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1591 (IC base=+0.022)

- **PATRÓN** `volumen_pendiente_norm` < `0.1619` → IC=+0.238 (n=2269)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1619 (IC base=+0.022)

- **PATRÓN** `volumen_pendiente_norm` > `0.1026` → IC=+0.244 (n=708)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1026 (IC base=+0.022)

- **PATRÓN** `volumen_spike_ratio` < `2.4234` → IC=+0.243 (n=2101)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4234 (IC base=+0.022)

- **PATRÓN** `ballena_activa_n` < `113.0` → IC=+0.256 (n=2137)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 113.0 (IC base=+0.022)

- **PATRÓN** `dist_vwap_pct` > `0.7515` → IC=+0.265 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7515 (IC base=+0.008)

- **PATRÓN** `volumen_regimen` < `1.1877` → IC=+0.265 (n=1565)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1877 (IC base=+0.008)

- **PATRÓN** `volumen_regimen` > `0.6165` → IC=+0.258 (n=1566)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6165 (IC base=+0.008)

- **PATRÓN** `volumen_pendiente_norm` > `0.2825` → IC=+0.309 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2825 (IC base=+0.008)

- **PATRÓN** `volumen_spike_ratio` < `1.7856` → IC=+0.291 (n=1004)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7856 (IC base=+0.008)

- **PATRÓN** `volumen_spike_ratio` > `2.426` → IC=+0.282 (n=502)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.426 (IC base=+0.008)

- **PATRÓN** `ballena_activa_n` < `115.0` → IC=+0.285 (n=1527)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 115.0 (IC base=+0.008)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7429` → IC=-0.248 (n=2471)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7429
  - _Potencial_: sin este filtro IC_bueno=+0.312 (n=2474)

- **FILTRO** `ibs_20min` > `0.6154` → IC=-0.236 (n=1169)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6154
  - _Potencial_: sin este filtro IC_bueno=+0.158 (n=3526)

- **FILTRO** `sigma_ewma_delta_pct` > `8.282` → IC=-0.268 (n=536)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.282
  - _Potencial_: sin este filtro IC_bueno=+0.102 (n=4159)

- **PATRÓN** `ibs_20min` > `0.7429` → IC=+0.312 (n=2474)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7429 (IC base=+0.032)

- **PATRÓN** `dist_vwap_pct` > `1.0516` → IC=+0.353 (n=351)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0516 (IC base=+0.032)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.449` → IC=+0.156 (n=2005)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 2.449 (IC base=+0.032)

- **PATRÓN** `volumen_regimen` < `0.8384` → IC=+0.345 (n=1201)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8384 (IC base=+0.032)

- **PATRÓN** `volumen_regimen` > `0.6924` → IC=+0.336 (n=1609)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6924 (IC base=+0.032)

- **PATRÓN** `volumen_pendiente_norm` < `0.0982` → IC=+0.335 (n=1696)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0982 (IC base=+0.032)

- **PATRÓN** `volumen_pendiente_norm` > `0.2751` → IC=+0.371 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2751 (IC base=+0.032)

- **PATRÓN** `volumen_spike_ratio` < `1.4267` → IC=+0.362 (n=584)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4267 (IC base=+0.032)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.354 (n=1562)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=+0.032)

- **PATRÓN** `ibs_20min` < `0.6154` → IC=+0.158 (n=3526)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.6154 (IC base=+0.060)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.737` → IC=+0.128 (n=3682)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` < 4.737 (IC base=+0.060)

- **PATRÓN** `volumen_regimen` < `0.6914` → IC=+0.281 (n=788)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6914 (IC base=+0.060)

- **PATRÓN** `volumen_pendiente_norm` > `0.0706` → IC=+0.299 (n=721)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0706 (IC base=+0.060)

- **PATRÓN** `volumen_spike_ratio` < `1.802` → IC=+0.282 (n=1159)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.802 (IC base=+0.060)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.289 (n=1765)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 46.0 (IC base=+0.060)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.358 (n=2276)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.315)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.318 (n=2574)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.315)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.317 (n=2676)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.315)

- **PATRÓN** `ibs_20min` > `0.6571` → IC=+0.343 (n=2547)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6571 (IC base=+0.315)

- **PATRÓN** `dist_vwap_pct` > `0.2128` → IC=+0.335 (n=1344)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2128 (IC base=+0.315)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.81` → IC=+0.337 (n=966)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.81 (IC base=+0.315)

- **PATRÓN** `volumen_regimen` > `0.6291` → IC=+0.325 (n=2547)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6291 (IC base=+0.315)

- **PATRÓN** `volumen_pendiente_norm` > `0.2819` → IC=+0.348 (n=372)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2819 (IC base=+0.315)

- **PATRÓN** `volumen_spike_ratio` > `1.5295` → IC=+0.328 (n=2195)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5295 (IC base=+0.315)

- **PATRÓN** `libro_liquidez` > `2994.483` → IC=+0.328 (n=849)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2994.483 (IC base=+0.315)

- **PATRÓN** `ballena_activa_n` < `39.0` → IC=+0.341 (n=2299)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 39.0 (IC base=+0.315)

- **PATRÓN** `sigma_h` > `0.0147` → IC=+0.352 (n=1831)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0147 (IC base=+0.316)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.318 (n=2755)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.316)

- **PATRÓN** `ibs_20min` < `0.381` → IC=+0.333 (n=2746)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.381 (IC base=+0.316)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.309` → IC=+0.329 (n=507)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.309 (IC base=+0.316)

- **PATRÓN** `volumen_regimen` < `0.7188` → IC=+0.319 (n=1210)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7188 (IC base=+0.316)

- **PATRÓN** `volumen_regimen` > `1.2063` → IC=+0.345 (n=916)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2063 (IC base=+0.316)

- **PATRÓN** `volumen_pendiente_norm` > `0.2839` → IC=+0.369 (n=387)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2839 (IC base=+0.316)

- **PATRÓN** `volumen_spike_ratio` < `1.4133` → IC=+0.323 (n=856)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4133 (IC base=+0.316)

- **PATRÓN** `volumen_spike_ratio` > `2.1456` → IC=+0.320 (n=1162)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1456 (IC base=+0.316)

- **PATRÓN** `libro_liquidez` > `2978.8913` → IC=+0.317 (n=916)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2978.8913 (IC base=+0.316)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.221 (n=5895)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0125 (IC base=+0.172)

- **PATRÓN** `drift_60min` |x|≤ `0.1233` → IC=+0.192 (n=7782)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.1233 (IC base=+0.172)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.183 (n=18382)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.172)

- **PATRÓN** `ibs_20min` > `0.5371` → IC=+0.229 (n=17682)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5371 (IC base=+0.172)

- **PATRÓN** `dist_vwap_pct` > `0.1628` → IC=+0.205 (n=6608)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1628 (IC base=+0.172)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.748` → IC=+0.258 (n=3453)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.748 (IC base=+0.172)

- **PATRÓN** `volumen_regimen` < `1.175` → IC=+0.152 (n=11788)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.175 (IC base=+0.172)

- **PATRÓN** `volumen_regimen` > `0.6224` → IC=+0.151 (n=11788)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.6224 (IC base=+0.172)

- **PATRÓN** `volumen_pendiente_norm` > `0.2929` → IC=+0.203 (n=2552)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2929 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` > `2.5993` → IC=+0.184 (n=5735)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 2.5993 (IC base=+0.172)

- **PATRÓN** `ballena_activa_n` < `86.0` → IC=+0.191 (n=16597)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 86.0 (IC base=+0.172)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.193 (n=7737)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0059 (IC base=+0.186)

- **PATRÓN** `sigma_h` > `0.008` → IC=+0.188 (n=11727)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.008 (IC base=+0.186)

- **PATRÓN** `drift_60min` |x|≤ `0.0822` → IC=+0.222 (n=5858)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0822 (IC base=+0.186)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.213 (n=6638)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.186)

- **PATRÓN** `ibs_20min` < `0.5251` → IC=+0.241 (n=17573)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5251 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.508` → IC=+0.192 (n=2784)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 9.508 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.511` → IC=+0.193 (n=15659)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` < 2.511 (IC base=+0.186)

- **PATRÓN** `volumen_regimen` < `1.1858` → IC=+0.167 (n=12485)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.1858 (IC base=+0.186)

- **PATRÓN** `volumen_pendiente_norm` > `0.294` → IC=+0.222 (n=2638)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.294 (IC base=+0.186)

- **PATRÓN** `volumen_spike_ratio` > `2.6309` → IC=+0.197 (n=5585)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 2.6309 (IC base=+0.186)

- **PATRÓN** `ballena_activa_n` < `91.0` → IC=+0.201 (n=16574)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 91.0 (IC base=+0.186)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` > `0.0109` → IC=+0.263 (n=970)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0109 (IC base=+0.226)

- **PATRÓN** `drift_60min` |x|≤ `0.1046` → IC=+0.257 (n=1277)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1046 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.234 (n=3022)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.226)

- **PATRÓN** `ibs_20min` > `0.9426` → IC=+0.292 (n=1934)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9426 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.46` → IC=+0.328 (n=951)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.46 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` > `0.2811` → IC=+0.284 (n=438)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2811 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` < `1.8355` → IC=+0.225 (n=1846)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8355 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` > `1.4343` → IC=+0.226 (n=2769)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4343 (IC base=+0.226)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.236 (n=3239)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.226)

- **PATRÓN** `sigma_h` < `0.01` → IC=+0.259 (n=2409)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.01 (IC base=+0.256)

- **PATRÓN** `sigma_h` > `0.009` → IC=+0.258 (n=1095)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.009 (IC base=+0.256)

- **PATRÓN** `drift_60min` |x|≤ `0.098` → IC=+0.312 (n=1060)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.098 (IC base=+0.256)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.260 (n=2489)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.256)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.262 (n=2191)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.256)

- **PATRÓN** `ibs_20min` < `0.4403` → IC=+0.274 (n=2409)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4403 (IC base=+0.256)

- **PATRÓN** `sigma_ewma_delta_pct` < `1.955` → IC=+0.262 (n=2384)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 1.955 (IC base=+0.256)

- **PATRÓN** `volumen_pendiente_norm` < `0.1001` → IC=+0.258 (n=2119)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1001 (IC base=+0.256)

- **PATRÓN** `volumen_pendiente_norm` > `0.3017` → IC=+0.275 (n=363)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3017 (IC base=+0.256)

- **PATRÓN** `volumen_spike_ratio` < `1.4472` → IC=+0.274 (n=771)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4472 (IC base=+0.256)

- **PATRÓN** `volumen_spike_ratio` > `2.6968` → IC=+0.261 (n=771)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6968 (IC base=+0.256)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.265 (n=1739)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.256)

- **PATRÓN** `libro_liquidez` > `1777.0436` → IC=+0.264 (n=1606)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1777.0436 (IC base=+0.256)

- **PATRÓN** `ballena_activa_n` < `7.0` → IC=+0.257 (n=914)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 7.0 (IC base=+0.256)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.199 (n=904)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0032 (IC base=+0.127)

- **PATRÓN** `drift_60min` |x|≤ `0.0651` → IC=+0.177 (n=899)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.0651 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.145 (n=2826)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.127)

- **PATRÓN** `ibs_20min` > `0.2551` → IC=+0.204 (n=2696)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2551 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` > `0.1844` → IC=+0.212 (n=1309)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1844 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.619` → IC=+0.208 (n=492)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.619 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` < `0.8585` → IC=+0.130 (n=1798)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 0.8585 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` > `1.0504` → IC=+0.132 (n=1222)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` > 1.0504 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` > `0.2784` → IC=+0.166 (n=414)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.2784 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` < `1.4051` → IC=+0.132 (n=884)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 1.4051 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` > `2.4599` → IC=+0.142 (n=884)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 2.4599 (IC base=+0.127)

- **PATRÓN** `ballena_activa_n` < `396.0` → IC=+0.132 (n=2622)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 396.0 (IC base=+0.127)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.172 (n=2901)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0066 (IC base=+0.152)

- **PATRÓN** `drift_60min` |x|≤ `0.2444` → IC=+0.175 (n=2552)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.2444 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.185 (n=1385)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 15.0 (IC base=+0.152)

- **PATRÓN** `ibs_20min` < `0.6098` → IC=+0.211 (n=2899)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6098 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.918` → IC=+0.177 (n=540)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 10.918 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.032` → IC=+0.157 (n=2528)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 4.032 (IC base=+0.152)

- **PATRÓN** `volumen_regimen` < `1.2032` → IC=+0.163 (n=2899)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2032 (IC base=+0.152)

- **PATRÓN** `volumen_pendiente_norm` < `0.2288` → IC=+0.155 (n=3077)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` < 0.2288 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` < `2.4713` → IC=+0.155 (n=2773)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.4713 (IC base=+0.152)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=3754)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.152)

- **PATRÓN** `ballena_activa_n` < `207.0` → IC=+0.202 (n=1195)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 207.0 (IC base=+0.152)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.01` → IC=+0.224 (n=1996)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.01 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.2509` → IC=+0.232 (n=1996)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2509 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.218 (n=3122)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.290 (n=1594)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.041` → IC=+0.306 (n=713)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.041 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` < `0.0984` → IC=+0.210 (n=2612)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0984 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.3511` → IC=+0.239 (n=423)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3511 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `2.71` → IC=+0.224 (n=1325)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.71 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.213 (n=3623)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `1995.9484` → IC=+0.224 (n=998)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1995.9484 (IC base=+0.210)

- **PATRÓN** `sigma_h` < `0.0109` → IC=+0.248 (n=2357)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0109 (IC base=+0.241)

- **PATRÓN** `drift_60min` |x|≤ `0.2464` → IC=+0.271 (n=1786)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2464 (IC base=+0.241)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.281 (n=1034)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.241)

- **PATRÓN** `ibs_20min` < `0.0409` → IC=+0.294 (n=1179)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0409 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.896` → IC=+0.280 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.896 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` > `0.3537` → IC=+0.288 (n=447)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3537 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` < `1.768` → IC=+0.240 (n=1140)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.768 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` > `2.1795` → IC=+0.253 (n=1727)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1795 (IC base=+0.241)

- **PATRÓN** `libro_liquidez` > `1872.8363` → IC=+0.247 (n=1215)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1872.8363 (IC base=+0.241)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.240 (n=1735)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.241)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.197 (n=976)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0038 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.0787` → IC=+0.182 (n=974)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.0787 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.138 (n=3027)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` > `0.245` → IC=+0.189 (n=2920)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.245 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` > `0.14` → IC=+0.185 (n=1647)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.14 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.227` → IC=+0.200 (n=501)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.227 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `0.8387` → IC=+0.137 (n=1947)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.8387 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` > `0.2874` → IC=+0.169 (n=439)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` > 0.2874 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `1.805` → IC=+0.126 (n=1907)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 1.805 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` > `2.5066` → IC=+0.136 (n=953)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 2.5066 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `6872.8229` → IC=+0.198 (n=1324)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 6872.8229 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `125.0` → IC=+0.127 (n=2865)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 125.0 (IC base=+0.126)

- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.164 (n=2755)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0068 (IC base=+0.132)

- **PATRÓN** `drift_60min` |x|≤ `0.4076` → IC=+0.148 (n=3125)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.4076 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.169 (n=1502)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 15.0 (IC base=+0.132)

- **PATRÓN** `ibs_20min` < `0.6715` → IC=+0.188 (n=3125)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.6715 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.239` → IC=+0.142 (n=746)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 9.239 (IC base=+0.132)

- **PATRÓN** `volumen_regimen` < `0.8521` → IC=+0.152 (n=2085)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.8521 (IC base=+0.132)

- **PATRÓN** `volumen_pendiente_norm` > `0.2938` → IC=+0.180 (n=467)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.2938 (IC base=+0.132)

- **PATRÓN** `volumen_spike_ratio` < `2.1915` → IC=+0.134 (n=2613)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 2.1915 (IC base=+0.132)

- **PATRÓN** `volumen_spike_ratio` > `1.5151` → IC=+0.134 (n=2652)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 1.5151 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `6390.1468` → IC=+0.193 (n=1417)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 6390.1468 (IC base=+0.132)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.158 (n=986)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 48.0 (IC base=+0.132)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0127` → IC=+0.165 (n=1083)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.0127 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.134 (n=3341)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 5.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` > `0.4706` → IC=+0.205 (n=3258)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4706 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` > `0.201` → IC=+0.188 (n=1715)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.201 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.963` → IC=+0.287 (n=684)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.963 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` < `1.0275` → IC=+0.129 (n=2862)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 1.0275 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` < `0.1617` → IC=+0.122 (n=3314)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_pendiente_norm` < 0.1617 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` < `1.7794` → IC=+0.124 (n=2102)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 1.7794 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `2676.0135` → IC=+0.198 (n=1473)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 2676.0135 (IC base=+0.118)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.129 (n=1085)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 16.0 (IC base=+0.118)

- **PATRÓN** `sigma_h` < `0.012` → IC=+0.143 (n=3421)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.012 (IC base=+0.123)

- **PATRÓN** `drift_60min` |x|≤ `0.1149` → IC=+0.164 (n=1139)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.1149 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.138 (n=3491)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` < `0.6471` → IC=+0.221 (n=3416)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6471 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.239` → IC=+0.144 (n=3022)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 2.239 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` < `1.1785` → IC=+0.129 (n=3415)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.1785 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` > `0.8597` → IC=+0.126 (n=2277)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` > 0.8597 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` < `0.1617` → IC=+0.126 (n=3364)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` < 0.1617 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` > `0.275` → IC=+0.150 (n=478)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.275 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` < `1.4338` → IC=+0.141 (n=1078)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.4338 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` > `2.4456` → IC=+0.134 (n=1078)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 2.4456 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `2574.5084` → IC=+0.191 (n=1549)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 2574.5084 (IC base=+0.123)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.130 (n=3225)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 44.0 (IC base=+0.123)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0127` → IC=+0.251 (n=2612)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0127 (IC base=+0.227)

- **PATRÓN** `drift_60min` |x|≤ `0.1653` → IC=+0.243 (n=1287)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1653 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.233 (n=3044)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.227)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.229 (n=2638)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.227)

- **PATRÓN** `ibs_20min` > `0.6667` → IC=+0.258 (n=2926)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6667 (IC base=+0.227)

- **PATRÓN** `dist_vwap_pct` > `1.1281` → IC=+0.237 (n=641)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1281 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.527` → IC=+0.258 (n=1343)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.527 (IC base=+0.227)

- **PATRÓN** `volumen_regimen` > `0.6202` → IC=+0.237 (n=2924)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6202 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` > `0.2347` → IC=+0.268 (n=545)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2347 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` < `2.4668` → IC=+0.230 (n=2854)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4668 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` > `1.4322` → IC=+0.231 (n=2853)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4322 (IC base=+0.227)

- **PATRÓN** `libro_liquidez` > `2595.0652` → IC=+0.231 (n=1949)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2595.0652 (IC base=+0.227)

- **PATRÓN** `sigma_h` < `0.0123` → IC=+0.243 (n=1341)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0123 (IC base=+0.242)

- **PATRÓN** `sigma_h` > `0.0224` → IC=+0.248 (n=1383)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0224 (IC base=+0.242)

- **PATRÓN** `drift_60min` |x|≤ `0.602` → IC=+0.251 (n=3049)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.602 (IC base=+0.242)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.254 (n=1501)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.242)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.247 (n=1357)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.242)

- **PATRÓN** `ibs_20min` < `0.037` → IC=+0.302 (n=1341)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.037 (IC base=+0.242)

- **PATRÓN** `dist_vwap_pct` > `1.1503` → IC=+0.257 (n=270)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1503 (IC base=+0.242)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.109` → IC=+0.272 (n=585)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.109 (IC base=+0.242)

- **PATRÓN** `volumen_regimen` < `0.87` → IC=+0.242 (n=2032)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.87 (IC base=+0.242)

- **PATRÓN** `volumen_regimen` > `1.0461` → IC=+0.248 (n=1383)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0461 (IC base=+0.242)

- **PATRÓN** `volumen_pendiente_norm` > `0.2813` → IC=+0.297 (n=421)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2813 (IC base=+0.242)

- **PATRÓN** `volumen_spike_ratio` < `2.5237` → IC=+0.239 (n=2881)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5237 (IC base=+0.242)

- **PATRÓN** `volumen_spike_ratio` > `1.549` → IC=+0.242 (n=2573)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.549 (IC base=+0.242)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.210 (n=1544)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.156)

- **PATRÓN** `drift_60min` |x|≤ `0.1364` → IC=+0.172 (n=2033)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.1364 (IC base=+0.156)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.168 (n=4825)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.156)

- **PATRÓN** `ibs_20min` > `0.4198` → IC=+0.201 (n=4126)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4198 (IC base=+0.156)

- **PATRÓN** `dist_vwap_pct` > `0.224` → IC=+0.177 (n=1706)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.224 (IC base=+0.156)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.516` → IC=+0.209 (n=758)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.516 (IC base=+0.156)

- **PATRÓN** `volumen_regimen` < `0.8606` → IC=+0.166 (n=2780)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.8606 (IC base=+0.156)

- **PATRÓN** `volumen_regimen` > `1.1961` → IC=+0.164 (n=1389)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 1.1961 (IC base=+0.156)

- **PATRÓN** `volumen_pendiente_norm` > `0.1569` → IC=+0.173 (n=1215)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.1569 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` < `1.528` → IC=+0.160 (n=1982)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 1.528 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` > `1.8093` → IC=+0.159 (n=3003)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.8093 (IC base=+0.156)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.157 (n=3952)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.01 (IC base=+0.156)

- **PATRÓN** `libro_liquidez` > `7329.5036` → IC=+0.186 (n=2094)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 7329.5036 (IC base=+0.156)

- **PATRÓN** `ibs_20min` < `0.3814` → IC=+0.176 (n=3368)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.3814 (IC base=+0.099)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.140 (n=2210)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 23.0 (IC base=+0.099)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.197 (n=1151)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0062 (IC base=+0.185)

- **PATRÓN** `drift_60min` |x|≤ `0.3311` → IC=+0.200 (n=1151)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3311 (IC base=+0.185)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.218 (n=1039)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.185)

- **PATRÓN** `ibs_20min` > `0.6191` → IC=+0.242 (n=767)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6191 (IC base=+0.185)

- **PATRÓN** `dist_vwap_pct` > `0.3106` → IC=+0.221 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3106 (IC base=+0.185)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.949` → IC=+0.213 (n=507)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.949 (IC base=+0.185)

- **PATRÓN** `volumen_regimen` < `0.6279` → IC=+0.210 (n=384)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6279 (IC base=+0.185)

- **PATRÓN** `volumen_pendiente_norm` < `0.2153` → IC=+0.189 (n=1296)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` < 0.2153 (IC base=+0.185)

- **PATRÓN** `volumen_pendiente_norm` > `0.0913` → IC=+0.200 (n=398)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0913 (IC base=+0.185)

- **PATRÓN** `volumen_spike_ratio` < `2.1671` → IC=+0.199 (n=994)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 2.1671 (IC base=+0.185)

- **PATRÓN** `volumen_spike_ratio` > `1.4026` → IC=+0.186 (n=1129)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 1.4026 (IC base=+0.185)

- **PATRÓN** `libro_liquidez` > `13741.2485` → IC=+0.192 (n=767)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 13741.2485 (IC base=+0.185)

- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.161 (n=481)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0031 (IC base=+0.079)

- **PATRÓN** `ibs_20min` < `0.2092` → IC=+0.198 (n=634)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.2092 (IC base=+0.079)

- **PATRÓN** `ballena_activa_n` < `166.0` → IC=+0.174 (n=623)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 166.0 (IC base=+0.079)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.232 (n=620)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.152)

- **PATRÓN** `drift_60min` |x|≤ `0.2134` → IC=+0.157 (n=933)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.2134 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.171 (n=1453)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 5.0 (IC base=+0.152)

- **PATRÓN** `ibs_20min` > `0.7794` → IC=+0.266 (n=634)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7794 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` > `0.5838` → IC=+0.193 (n=294)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.5838 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.898` → IC=+0.204 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.898 (IC base=+0.152)

- **PATRÓN** `volumen_regimen` < `0.8331` → IC=+0.165 (n=934)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8331 (IC base=+0.152)

- **PATRÓN** `volumen_pendiente_norm` > `0.2183` → IC=+0.195 (n=254)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2183 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` > `2.4735` → IC=+0.180 (n=460)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 2.4735 (IC base=+0.152)

- **PATRÓN** `libro_liquidez` > `7934.3279` → IC=+0.176 (n=634)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 7934.3279 (IC base=+0.152)

- **PATRÓN** `ballena_activa_n` < `31.0` → IC=+0.150 (n=461)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 31.0 (IC base=+0.152)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.127 (n=922)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.63€ cuando `sigma_h` < 0.0053 (IC base=+0.096)

- **PATRÓN** `ibs_20min` < `0.087` → IC=+0.202 (n=461)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.087 (IC base=+0.096)

- **PATRÓN** `volumen_regimen` < `0.6774` → IC=+0.133 (n=609)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 0.6774 (IC base=+0.096)

- **PATRÓN** `libro_liquidez` > `7772.1265` → IC=+0.150 (n=627)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 7772.1265 (IC base=+0.096)

- **PATRÓN** `ballena_activa_n` < `61.0` → IC=+0.121 (n=893)

  - _Acción_: Kelly boost +0.61€ cuando `ballena_activa_n` < 61.0 (IC base=+0.096)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.154 (n=397)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0067 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.158 (n=831)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 11.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.266 (n=446)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` > `0.9447` → IC=+0.165 (n=189)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.9447 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.829` → IC=+0.224 (n=462)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.829 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` < `1.0462` → IC=+0.129 (n=1045)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.0462 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` > `0.7001` → IC=+0.125 (n=1060)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` > 0.7001 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` > `0.224` → IC=+0.152 (n=208)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` > 0.224 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` < `1.4125` → IC=+0.147 (n=383)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.4125 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `2751.7394` → IC=+0.157 (n=538)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 2751.7394 (IC base=+0.118)

- **PATRÓN** `ibs_20min` < `0.55` → IC=+0.163 (n=1162)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` < 0.55 (IC base=+0.082)

- **PATRÓN** `libro_liquidez` > `2638.4619` → IC=+0.165 (n=598)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2638.4619 (IC base=+0.082)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0155` → IC=+0.239 (n=289)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0155 (IC base=+0.184)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.224 (n=201)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.184)

- **PATRÓN** `ibs_20min` > `0.9523` → IC=+0.207 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9523 (IC base=+0.184)

- **PATRÓN** `dist_vwap_pct` > `0.2421` → IC=+0.192 (n=219)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.2421 (IC base=+0.184)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.495` → IC=+0.198 (n=432)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` < 5.495 (IC base=+0.184)

- **PATRÓN** `volumen_regimen` > `1.2178` → IC=+0.255 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2178 (IC base=+0.184)

- **PATRÓN** `volumen_pendiente_norm` > `0.0812` → IC=+0.214 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0812 (IC base=+0.184)

- **PATRÓN** `volumen_spike_ratio` < `2.129` → IC=+0.198 (n=356)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 2.129 (IC base=+0.184)

- **PATRÓN** `volumen_spike_ratio` > `1.4102` → IC=+0.195 (n=405)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.4102 (IC base=+0.184)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.198 (n=455)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.03 (IC base=+0.184)

- **PATRÓN** `libro_liquidez` > `2705.7218` → IC=+0.218 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2705.7218 (IC base=+0.184)

- **PATRÓN** `sigma_h` > `0.0105` → IC=+0.174 (n=479)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` > 0.0105 (IC base=+0.155)

- **PATRÓN** `drift_60min` |x|≤ `0.3336` → IC=+0.165 (n=320)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.3336 (IC base=+0.155)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.196 (n=235)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 15.0 (IC base=+0.155)

- **PATRÓN** `ibs_20min` < `0.34` → IC=+0.162 (n=320)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` < 0.34 (IC base=+0.155)

- **PATRÓN** `ibs_20min` > `0.1` → IC=+0.161 (n=479)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` > 0.1 (IC base=+0.155)

- **PATRÓN** `dist_vwap_pct` > `1.1805` → IC=+0.283 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1805 (IC base=+0.155)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.957` → IC=+0.157 (n=464)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 2.957 (IC base=+0.155)

- **PATRÓN** `volumen_regimen` < `1.247` → IC=+0.174 (n=479)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 1.247 (IC base=+0.155)

- **PATRÓN** `volumen_pendiente_norm` < `0.113` → IC=+0.170 (n=443)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` < 0.113 (IC base=+0.155)

- **PATRÓN** `volumen_pendiente_norm` > `0.2358` → IC=+0.193 (n=86)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2358 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` < `1.4819` → IC=+0.205 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4819 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` > `2.6474` → IC=+0.160 (n=154)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 2.6474 (IC base=+0.155)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.170 (n=462)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 20.0 (IC base=+0.155)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0126` → IC=+0.227 (n=7774)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0126 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.190 (n=24314)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` > `0.427` → IC=+0.226 (n=23280)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.427 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` > `0.8911` → IC=+0.215 (n=2645)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8911 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.932` → IC=+0.259 (n=5711)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.932 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` < `1.2131` → IC=+0.160 (n=15684)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2131 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.2406` → IC=+0.209 (n=4181)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2406 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `2.6235` → IC=+0.192 (n=7580)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.6235 (IC base=+0.180)

- **PATRÓN** `ballena_activa_n` < `102.0` → IC=+0.201 (n=21929)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 102.0 (IC base=+0.180)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.200 (n=7183)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.198)

- **PATRÓN** `sigma_h` > `0.0123` → IC=+0.210 (n=7188)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0123 (IC base=+0.198)

- **PATRÓN** `drift_60min` |x|≤ `0.1477` → IC=+0.203 (n=9478)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1477 (IC base=+0.198)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.217 (n=8106)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.198)

- **PATRÓN** `ibs_20min` < `0.4851` → IC=+0.253 (n=18952)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4851 (IC base=+0.198)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.521` → IC=+0.204 (n=20006)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.521 (IC base=+0.198)

- **PATRÓN** `volumen_regimen` < `1.0533` → IC=+0.173 (n=12722)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 1.0533 (IC base=+0.198)

- **PATRÓN** `volumen_pendiente_norm` > `0.293` → IC=+0.257 (n=2960)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.293 (IC base=+0.198)

- **PATRÓN** `volumen_spike_ratio` > `2.6265` → IC=+0.212 (n=6887)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6265 (IC base=+0.198)

- **PATRÓN** `ballena_activa_n` < `90.0` → IC=+0.214 (n=20408)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 90.0 (IC base=+0.198)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.253 (n=1804)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` > `0.8626` → IC=+0.297 (n=2479)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8626 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.835` → IC=+0.343 (n=887)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.835 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.2327` → IC=+0.287 (n=665)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2327 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` < `1.4492` → IC=+0.232 (n=1199)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4492 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.2926` → IC=+0.240 (n=1630)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2926 (IC base=+0.234)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.248 (n=4119)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `2024.9` → IC=+0.237 (n=1240)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2024.9 (IC base=+0.234)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.249 (n=2312)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 14.0 (IC base=+0.234)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.268 (n=3356)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.268)

- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.270 (n=1522)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0094 (IC base=+0.268)

- **PATRÓN** `drift_60min` |x|≤ `0.1239` → IC=+0.295 (n=1476)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1239 (IC base=+0.268)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.269 (n=3488)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.268)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.272 (n=3021)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.268)

- **PATRÓN** `ibs_20min` < `0.5506` → IC=+0.286 (n=3353)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5506 (IC base=+0.268)

- **PATRÓN** `volumen_pendiente_norm` < `0.0977` → IC=+0.270 (n=3057)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0977 (IC base=+0.268)

- **PATRÓN** `volumen_pendiente_norm` > `0.2908` → IC=+0.290 (n=461)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2908 (IC base=+0.268)

- **PATRÓN** `volumen_spike_ratio` < `1.5659` → IC=+0.273 (n=1418)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5659 (IC base=+0.268)

- **PATRÓN** `volumen_spike_ratio` > `2.6526` → IC=+0.282 (n=1074)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6526 (IC base=+0.268)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.273 (n=2407)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.268)

- **PATRÓN** `libro_liquidez` > `1776.9288` → IC=+0.276 (n=2235)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1776.9288 (IC base=+0.268)

- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.278 (n=1226)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 8.0 (IC base=+0.268)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.176 (n=1281)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0032 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.0796` → IC=+0.148 (n=1274)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.0796 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.150 (n=3989)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 5.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` > `0.3074` → IC=+0.202 (n=3413)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3074 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` > `0.3237` → IC=+0.199 (n=1190)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.3237 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.313` → IC=+0.165 (n=796)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 9.313 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `0.6345` → IC=+0.155 (n=1274)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.6345 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` > `1.0681` → IC=+0.143 (n=1732)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 1.0681 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.2707` → IC=+0.184 (n=540)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.2707 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `2.1695` → IC=+0.143 (n=3304)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.1695 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `1.5154` → IC=+0.144 (n=3355)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.5154 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `296.0` → IC=+0.153 (n=2470)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 296.0 (IC base=+0.138)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.172 (n=2938)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0058 (IC base=+0.142)

- **PATRÓN** `drift_60min` |x|≤ `0.0806` → IC=+0.169 (n=1112)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.0806 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.172 (n=1234)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.142)

- **PATRÓN** `ibs_20min` < `0.678` → IC=+0.189 (n=3334)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.678 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.005` → IC=+0.145 (n=3015)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 4.005 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` < `1.043` → IC=+0.153 (n=2934)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 1.043 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` > `0.2208` → IC=+0.193 (n=613)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2208 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` < `2.4301` → IC=+0.148 (n=3224)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 2.4301 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` > `1.7706` → IC=+0.147 (n=2149)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.7706 (IC base=+0.142)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=4334)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.142)

- **PATRÓN** `ballena_activa_n` < `219.0` → IC=+0.169 (n=1051)

  - _Acción_: Kelly boost +0.84€ cuando `ballena_activa_n` < 219.0 (IC base=+0.142)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0132` → IC=+0.242 (n=1298)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0132 (IC base=+0.225)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.235 (n=4070)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.225 (n=3468)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.225)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.302 (n=1443)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.225)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.979` → IC=+0.320 (n=865)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.979 (IC base=+0.225)

- **PATRÓN** `volumen_pendiente_norm` < `0.1316` → IC=+0.227 (n=3680)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1316 (IC base=+0.225)

- **PATRÓN** `volumen_pendiente_norm` > `0.3501` → IC=+0.230 (n=509)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3501 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` > `2.7432` → IC=+0.241 (n=1721)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7432 (IC base=+0.225)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.231 (n=4690)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.225)

- **PATRÓN** `libro_liquidez` > `2004.561` → IC=+0.240 (n=1293)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2004.561 (IC base=+0.225)

- **PATRÓN** `sigma_h` < `0.0111` → IC=+0.250 (n=3287)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0111 (IC base=+0.246)

- **PATRÓN** `sigma_h` > `0.0123` → IC=+0.246 (n=1244)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0123 (IC base=+0.246)

- **PATRÓN** `drift_60min` |x|≤ `0.1804` → IC=+0.261 (n=1641)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1804 (IC base=+0.246)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.265 (n=1429)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.246)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.248 (n=1691)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.246)

- **PATRÓN** `ibs_20min` < `0.0625` → IC=+0.305 (n=1253)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0625 (IC base=+0.246)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.038` → IC=+0.307 (n=391)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.038 (IC base=+0.246)

- **PATRÓN** `volumen_pendiente_norm` > `0.3476` → IC=+0.305 (n=562)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3476 (IC base=+0.246)

- **PATRÓN** `volumen_spike_ratio` > `2.175` → IC=+0.257 (n=2399)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.175 (IC base=+0.246)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.250 (n=1876)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.246)

- **PATRÓN** `libro_liquidez` > `1979.1984` → IC=+0.256 (n=1243)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1979.1984 (IC base=+0.246)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.250 (n=3135)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 21.0 (IC base=+0.246)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.194 (n=1346)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0038 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.3396` → IC=+0.148 (n=3547)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.3396 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.151 (n=4187)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 5.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` > `0.882` → IC=+0.269 (n=1345)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.882 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` > `0.1977` → IC=+0.169 (n=1773)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.1977 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.066` → IC=+0.168 (n=610)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 11.066 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `0.8567` → IC=+0.154 (n=2687)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.8567 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.2323` → IC=+0.192 (n=713)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2323 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `1.5141` → IC=+0.155 (n=1734)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 1.5141 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `2.156` → IC=+0.142 (n=1787)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 2.156 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `7287.1688` → IC=+0.241 (n=1344)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7287.1688 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `87.0` → IC=+0.147 (n=2644)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 87.0 (IC base=+0.138)

- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.172 (n=2984)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0068 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.4448` → IC=+0.160 (n=3391)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.4448 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.176 (n=1258)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` < `0.7054` → IC=+0.200 (n=3392)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7054 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.827` → IC=+0.151 (n=497)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 10.827 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.02` → IC=+0.154 (n=2962)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 3.02 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `0.8558` → IC=+0.161 (n=2261)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8558 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` > `0.2938` → IC=+0.214 (n=431)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2938 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `2.2023` → IC=+0.153 (n=2886)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.2023 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` > `1.525` → IC=+0.156 (n=2930)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.525 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `6596.2331` → IC=+0.225 (n=1131)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6596.2331 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `57.0` → IC=+0.172 (n=1106)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 57.0 (IC base=+0.149)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0128` → IC=+0.151 (n=1369)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` > 0.0128 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.147 (n=2897)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 11.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` > `0.4286` → IC=+0.187 (n=4098)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.4286 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` > `1.0124` → IC=+0.203 (n=651)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0124 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.229` → IC=+0.274 (n=1040)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.229 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` < `0.8745` → IC=+0.133 (n=2730)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 0.8745 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` < `2.4923` → IC=+0.121 (n=3997)

  - _Acción_: Kelly boost +0.60€ cuando `volumen_spike_ratio` < 2.4923 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `2726.3005` → IC=+0.240 (n=1365)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2726.3005 (IC base=+0.117)

- **PATRÓN** `sigma_h` < `0.011` → IC=+0.156 (n=3386)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.011 (IC base=+0.134)

- **PATRÓN** `drift_60min` |x|≤ `0.1396` → IC=+0.154 (n=1281)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.1396 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.169 (n=1821)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 15.0 (IC base=+0.134)

- **PATRÓN** `ibs_20min` < `0.6667` → IC=+0.220 (n=3867)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6667 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.042` → IC=+0.156 (n=3722)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 3.042 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` < `0.6386` → IC=+0.152 (n=1281)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.6386 (IC base=+0.134)

- **PATRÓN** `volumen_pendiente_norm` > `0.2296` → IC=+0.198 (n=681)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2296 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` < `1.4384` → IC=+0.162 (n=1221)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 1.4384 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `2624.9762` → IC=+0.216 (n=1281)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2624.9762 (IC base=+0.134)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.145 (n=3667)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 49.0 (IC base=+0.134)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.259 (n=3741)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0113 (IC base=+0.239)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.245 (n=3915)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.239)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.244 (n=2497)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.239)

- **PATRÓN** `ibs_20min` > `0.6145` → IC=+0.272 (n=3341)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6145 (IC base=+0.239)

- **PATRÓN** `dist_vwap_pct` > `0.1967` → IC=+0.253 (n=1881)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1967 (IC base=+0.239)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.11` → IC=+0.289 (n=657)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.11 (IC base=+0.239)

- **PATRÓN** `volumen_regimen` < `1.219` → IC=+0.240 (n=3740)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.219 (IC base=+0.239)

- **PATRÓN** `volumen_regimen` > `0.6435` → IC=+0.244 (n=3740)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6435 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` > `0.2395` → IC=+0.255 (n=651)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2395 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` > `2.4995` → IC=+0.255 (n=1220)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4995 (IC base=+0.239)

- **PATRÓN** `libro_liquidez` > `2984.1749` → IC=+0.247 (n=1247)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2984.1749 (IC base=+0.239)

- **PATRÓN** `sigma_h` > `0.0255` → IC=+0.268 (n=1296)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0255 (IC base=+0.245)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.250 (n=3670)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.245)

- **PATRÓN** `ibs_20min` < `0.1387` → IC=+0.310 (n=1711)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1387 (IC base=+0.245)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.066` → IC=+0.278 (n=741)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.066 (IC base=+0.245)

- **PATRÓN** `volumen_regimen` < `0.7157` → IC=+0.247 (n=1711)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7157 (IC base=+0.245)

- **PATRÓN** `volumen_regimen` > `1.2141` → IC=+0.267 (n=1296)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2141 (IC base=+0.245)

- **PATRÓN** `volumen_pendiente_norm` > `0.2862` → IC=+0.311 (n=533)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2862 (IC base=+0.245)

- **PATRÓN** `volumen_spike_ratio` > `1.432` → IC=+0.248 (n=3678)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.432 (IC base=+0.245)

- **PATRÓN** `libro_liquidez` > `2971.5749` → IC=+0.247 (n=1296)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2971.5749 (IC base=+0.245)

### GBM_LATE_5M
- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.231 (n=6006)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0106 (IC base=+0.223)

- **PATRÓN** `drift_60min` |x|≤ `0.5217` → IC=+0.232 (n=6814)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5217 (IC base=+0.223)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.230 (n=6879)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.223)

- **PATRÓN** `ibs_20min` > `0.9283` → IC=+0.259 (n=2271)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9283 (IC base=+0.223)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.576` → IC=+0.229 (n=3394)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.576 (IC base=+0.223)

- **PATRÓN** `volumen_regimen` < `0.7035` → IC=+0.232 (n=2137)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7035 (IC base=+0.223)

- **PATRÓN** `volumen_regimen` > `0.8777` → IC=+0.223 (n=3237)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8777 (IC base=+0.223)

- **PATRÓN** `volumen_pendiente_norm` < `0.1043` → IC=+0.224 (n=6369)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1043 (IC base=+0.223)

- **PATRÓN** `volumen_pendiente_norm` > `0.2357` → IC=+0.231 (n=1326)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2357 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` < `2.258` → IC=+0.228 (n=5903)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.258 (IC base=+0.223)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.227 (n=4915)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.223)

- **PATRÓN** `libro_liquidez` > `3698.7496` → IC=+0.230 (n=4542)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3698.7496 (IC base=+0.223)

- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.236 (n=1551)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.203)

- **PATRÓN** `drift_60min` |x|≤ `0.5056` → IC=+0.214 (n=4636)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5056 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.212 (n=1809)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.215 (n=2066)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.203)

- **PATRÓN** `ibs_20min` < `0.0875` → IC=+0.214 (n=1546)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0875 (IC base=+0.203)

- **PATRÓN** `dist_vwap_pct` > `0.6772` → IC=+0.210 (n=747)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6772 (IC base=+0.203)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.762` → IC=+0.217 (n=4187)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.762 (IC base=+0.203)

- **PATRÓN** `volumen_regimen` < `1.095` → IC=+0.209 (n=3837)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.095 (IC base=+0.203)

- **PATRÓN** `volumen_pendiente_norm` < `0.0981` → IC=+0.205 (n=4279)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0981 (IC base=+0.203)

- **PATRÓN** `volumen_pendiente_norm` > `0.2234` → IC=+0.206 (n=928)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2234 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` < `1.5329` → IC=+0.206 (n=2012)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5329 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` > `2.1949` → IC=+0.213 (n=2072)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1949 (IC base=+0.203)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.203 (n=6053)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.203)

- **PATRÓN** `ballena_activa_n` < `30.0` → IC=+0.229 (n=2051)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 30.0 (IC base=+0.203)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.277 (n=824)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.269)

- **PATRÓN** `drift_60min` |x|≤ `0.0853` → IC=+0.300 (n=313)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0853 (IC base=+0.269)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.269 (n=940)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.269)

- **PATRÓN** `ibs_20min` < `0.1406` → IC=+0.294 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1406 (IC base=+0.269)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.122` → IC=+0.290 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.122 (IC base=+0.269)

- **PATRÓN** `volumen_regimen` < `1.2303` → IC=+0.273 (n=937)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2303 (IC base=+0.269)

- **PATRÓN** `volumen_regimen` > `1.0873` → IC=+0.274 (n=427)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0873 (IC base=+0.269)

- **PATRÓN** `volumen_pendiente_norm` > `0.2881` → IC=+0.346 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2881 (IC base=+0.269)

- **PATRÓN** `volumen_spike_ratio` < `2.4907` → IC=+0.276 (n=931)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4907 (IC base=+0.269)

- **PATRÓN** `volumen_spike_ratio` > `2.1972` → IC=+0.269 (n=422)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1972 (IC base=+0.269)

- **PATRÓN** `libro_liquidez` > `12881.3725` → IC=+0.281 (n=624)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12881.3725 (IC base=+0.269)

- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.265 (n=513)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0032 (IC base=+0.175)

- **PATRÓN** `drift_60min` |x|≤ `0.3869` → IC=+0.189 (n=1529)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.3869 (IC base=+0.175)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.218 (n=565)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.175)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.180 (n=570)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 5.0 (IC base=+0.175)

- **PATRÓN** `ibs_20min` < `0.1382` → IC=+0.197 (n=674)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.1382 (IC base=+0.175)

- **PATRÓN** `dist_vwap_pct` > `0.6994` → IC=+0.193 (n=138)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.6994 (IC base=+0.175)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.835` → IC=+0.188 (n=1768)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` < 10.835 (IC base=+0.175)

- **PATRÓN** `volumen_regimen` < `1.091` → IC=+0.189 (n=1346)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` < 1.091 (IC base=+0.175)

- **PATRÓN** `volumen_pendiente_norm` < `0.2705` → IC=+0.178 (n=1806)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` < 0.2705 (IC base=+0.175)

- **PATRÓN** `volumen_pendiente_norm` > `0.1515` → IC=+0.193 (n=467)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.1515 (IC base=+0.175)

- **PATRÓN** `volumen_spike_ratio` < `1.4122` → IC=+0.194 (n=507)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 1.4122 (IC base=+0.175)

- **PATRÓN** `volumen_spike_ratio` > `1.8038` → IC=+0.180 (n=1014)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 1.8038 (IC base=+0.175)

- **PATRÓN** `libro_liquidez` > `14600.5038` → IC=+0.176 (n=693)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 14600.5038 (IC base=+0.175)

- **PATRÓN** `ballena_activa_n` < `691.0` → IC=+0.188 (n=1483)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 691.0 (IC base=+0.175)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` > `0.0123` → IC=+0.238 (n=345)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0123 (IC base=+0.209)

- **PATRÓN** `drift_60min` |x|≤ `0.5997` → IC=+0.212 (n=1031)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5997 (IC base=+0.209)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.231 (n=943)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.209)

- **PATRÓN** `ibs_20min` < `0.7126` → IC=+0.212 (n=688)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7126 (IC base=+0.209)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.252 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.209)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.277` → IC=+0.246 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.277 (IC base=+0.209)

- **PATRÓN** `volumen_pendiente_norm` > `0.2042` → IC=+0.244 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2042 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` > `1.7931` → IC=+0.215 (n=918)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7931 (IC base=+0.209)

- **PATRÓN** `libro_liquidez` > `2777.94` → IC=+0.240 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2777.94 (IC base=+0.209)

- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.221 (n=732)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 8.0 (IC base=+0.209)

- **PATRÓN** `sigma_h` < `0.0116` → IC=+0.242 (n=60)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0116 (IC base=+0.228)

- **PATRÓN** `sigma_h` > `0.0102` → IC=+0.224 (n=27)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0102 (IC base=+0.228)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.300 (n=53)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.228)

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

- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.250 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 8.0 (IC base=+0.228)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.221 (n=1828)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0084 (IC base=+0.209)

- **PATRÓN** `drift_60min` |x|≤ `0.4578` → IC=+0.216 (n=1828)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4578 (IC base=+0.209)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.234 (n=640)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.209)

- **PATRÓN** `ibs_20min` < `0.4751` → IC=+0.218 (n=1220)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4751 (IC base=+0.209)

- **PATRÓN** `ibs_20min` > `0.1447` → IC=+0.211 (n=1828)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1447 (IC base=+0.209)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.365` → IC=+0.216 (n=1853)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 6.365 (IC base=+0.209)

- **PATRÓN** `volumen_regimen` < `0.8663` → IC=+0.217 (n=1219)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8663 (IC base=+0.209)

- **PATRÓN** `volumen_pendiente_norm` < `0.1018` → IC=+0.212 (n=1685)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1018 (IC base=+0.209)

- **PATRÓN** `volumen_pendiente_norm` > `0.0755` → IC=+0.209 (n=779)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0755 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` < `1.403` → IC=+0.228 (n=597)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.403 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` > `1.4939` → IC=+0.210 (n=1598)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4939 (IC base=+0.209)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.242 (n=479)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.199)

- **PATRÓN** `drift_60min` |x|≤ `0.4905` → IC=+0.220 (n=1434)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4905 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.202 (n=535)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.214 (n=974)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.199)

- **PATRÓN** `ibs_20min` < `0.1707` → IC=+0.200 (n=631)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1707 (IC base=+0.199)

- **PATRÓN** `ibs_20min` > `0.612` → IC=+0.209 (n=650)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.612 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` > `0.6324` → IC=+0.217 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6324 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.266` → IC=+0.204 (n=1310)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.266 (IC base=+0.199)

- **PATRÓN** `volumen_regimen` < `1.2516` → IC=+0.207 (n=1434)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2516 (IC base=+0.199)

- **PATRÓN** `volumen_regimen` > `0.7214` → IC=+0.199 (n=1282)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7214 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` > `0.0731` → IC=+0.225 (n=590)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0731 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` < `1.412` → IC=+0.205 (n=470)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.412 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` > `1.7864` → IC=+0.203 (n=937)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7864 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `6539.6068` → IC=+0.208 (n=1281)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6539.6068 (IC base=+0.199)

- **PATRÓN** `ballena_activa_n` < `98.0` → IC=+0.200 (n=1424)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 98.0 (IC base=+0.199)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0085` → IC=+0.239 (n=515)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0085 (IC base=+0.214)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.245 (n=1050)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.214)

- **PATRÓN** `ibs_20min` > `0.9855` → IC=+0.291 (n=390)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9855 (IC base=+0.214)

- **PATRÓN** `dist_vwap_pct` > `0.814` → IC=+0.238 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.814 (IC base=+0.214)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.168` → IC=+0.245 (n=633)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.168 (IC base=+0.214)

- **PATRÓN** `volumen_regimen` < `0.7012` → IC=+0.248 (n=515)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7012 (IC base=+0.214)

- **PATRÓN** `volumen_pendiente_norm` < `0.104` → IC=+0.220 (n=1067)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.104 (IC base=+0.214)

- **PATRÓN** `volumen_pendiente_norm` > `0.2722` → IC=+0.224 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2722 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` < `2.1715` → IC=+0.225 (n=1003)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1715 (IC base=+0.214)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.224 (n=1377)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.214)

- **PATRÓN** `libro_liquidez` > `4364.6181` → IC=+0.253 (n=390)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4364.6181 (IC base=+0.214)

- **PATRÓN** `sigma_h` > `0.0103` → IC=+0.257 (n=540)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0103 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.6362` → IC=+0.250 (n=809)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6362 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.239 (n=752)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.237)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.261 (n=566)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` < `0.64` → IC=+0.262 (n=713)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.64 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.929` → IC=+0.257 (n=760)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.929 (IC base=+0.237)

- **PATRÓN** `volumen_regimen` < `0.7522` → IC=+0.246 (n=356)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7522 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` < `0.0838` → IC=+0.250 (n=689)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0838 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `2.2105` → IC=+0.265 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2105 (IC base=+0.237)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.239 (n=1062)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.237)

- **PATRÓN** `libro_liquidez` > `3872.662` → IC=+0.260 (n=539)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3872.662 (IC base=+0.237)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.273 (n=706)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 34.0 (IC base=+0.237)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.149 (n=781)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0039 (IC base=+0.053)

- **PATRÓN** `ibs_20min` > `0.7497` → IC=+0.183 (n=1495)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.7497 (IC base=+0.053)

- **PATRÓN** `dist_vwap_pct` > `0.1483` → IC=+0.143 (n=1078)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.1483 (IC base=+0.053)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.347` → IC=+0.141 (n=494)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 10.347 (IC base=+0.053)

- **PATRÓN** `ibs_20min` < `0.0688` → IC=+0.259 (n=703)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0688 (IC base=+0.055)

- **PATRÓN** `volumen_pendiente_norm` > `0.1474` → IC=+0.143 (n=435)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_pendiente_norm` > 0.1474 (IC base=+0.055)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.125 (n=652)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.63€ cuando `sigma_h` < 0.0054 (IC base=+0.067)

- **PATRÓN** `ibs_20min` > `0.5427` → IC=+0.159 (n=632)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` > 0.5427 (IC base=+0.067)

- **PATRÓN** `dist_vwap_pct` > `0.1227` → IC=+0.168 (n=323)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.1227 (IC base=+0.067)

- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.131 (n=285)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.65€ cuando `sigma_h` < 0.0035 (IC base=+0.047)

- **PATRÓN** `ibs_20min` < `0.0689` → IC=+0.247 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0689 (IC base=+0.047)

- **PATRÓN** `volumen_pendiente_norm` > `0.2172` → IC=+0.151 (n=127)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` > 0.2172 (IC base=+0.047)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` > `0.6595` → IC=-0.157 (n=167)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6595
  - _Potencial_: sin este filtro IC_bueno=+0.118 (n=503)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.150 (n=332)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0042 (IC base=+0.068)

- **PATRÓN** `ibs_20min` > `0.9347` → IC=+0.258 (n=329)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9347 (IC base=+0.068)

- **PATRÓN** `dist_vwap_pct` > `0.1297` → IC=+0.167 (n=343)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1297 (IC base=+0.068)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.623` → IC=+0.203 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.623 (IC base=+0.068)

- **PATRÓN** `ibs_20min` < `0.1087` → IC=+0.263 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1087 (IC base=+0.034)

### GBM_LATE_60M#SOL#60min
- **PATRÓN** `ibs_20min` > `0.72` → IC=+0.136 (n=542)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` > 0.72 (IC base=+0.027)

- **PATRÓN** `dist_vwap_pct` > `0.7302` → IC=+0.145 (n=184)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` > 0.7302 (IC base=+0.027)

- **PATRÓN** `sigma_h` < `0.0097` → IC=+0.183 (n=336)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0097 (IC base=+0.088)

- **PATRÓN** `ibs_20min` < `0.4865` → IC=+0.190 (n=472)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.4865 (IC base=+0.088)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.838` → IC=+0.304 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.838 (IC base=+0.088)

- **PATRÓN** `volumen_regimen` > `1.1079` → IC=+0.200 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1079 (IC base=+0.088)

- **PATRÓN** `volumen_pendiente_norm` > `0.1089` → IC=+0.172 (n=178)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.1089 (IC base=+0.088)

- **PATRÓN** `volumen_spike_ratio` > `2.5569` → IC=+0.151 (n=147)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 2.5569 (IC base=+0.088)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.125 (n=222)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.03 (IC base=+0.088)

### GBM_LATE_60M_FADE
- **FILTRO** `hora_utc` > `7.0` → IC=-0.302 (n=94)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.201 (n=292)

- **FILTRO** `dist_vwap_pct` > `0.2381` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2381
  - _Potencial_: sin este filtro IC_bueno=-0.221 (n=371)

- **FILTRO** `volumen_regimen` < `0.8582` → IC=-0.306 (n=127)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.8582
  - _Potencial_: sin este filtro IC_bueno=-0.186 (n=259)

- **FILTRO** `hora_utc` > `11.0` → IC=-0.304 (n=151)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.246 (n=187)

- **FILTRO** `ibs_20min` > `0.6985` → IC=-0.310 (n=114)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6985
  - _Potencial_: sin este filtro IC_bueno=-0.252 (n=224)

- **FILTRO** `dist_vwap_pct` > `0.4428` → IC=-0.409 (n=20)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4428
  - _Potencial_: sin este filtro IC_bueno=-0.263 (n=318)

- **FILTRO** `volumen_pendiente_norm` > `0.0448` → IC=-0.379 (n=31)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0448
  - _Potencial_: sin este filtro IC_bueno=-0.252 (n=216)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `volumen_regimen` < `1.2266` → IC=-0.297 (n=57)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.2266
  - _Potencial_: sin este filtro IC_bueno=-0.195 (n=57)

- **FILTRO** `ibs_20min` > `0.7502` → IC=-0.265 (n=49)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7502
  - _Potencial_: sin este filtro IC_bueno=-0.240 (n=98)

- **FILTRO** `volumen_regimen` > `0.805` → IC=-0.316 (n=36)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.226 (n=111)

- **FILTRO** `volumen_spike_ratio` > `1.817` → IC=-0.325 (n=38)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.817
  - _Potencial_: sin este filtro IC_bueno=-0.218 (n=76)

- **FILTRO** `libro_liquidez` < `5528.1887` → IC=-0.259 (n=110)

  - _Acción_: SKIP cuando `libro_liquidez` < 5528.1887
  - _Potencial_: sin este filtro IC_bueno=-0.218 (n=37)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `drift_60min` |x|> `0.1568` → IC=-0.324 (n=32)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1568
  - _Potencial_: sin este filtro IC_bueno=-0.128 (n=100)

- **FILTRO** `hora_utc` < `2.0` → IC=-0.179 (n=26)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 2.0
  - _Potencial_: sin este filtro IC_bueno=-0.176 (n=106)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.368 (n=36)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.271 (n=94)

- **FILTRO** `ibs_20min` > `0.7557` → IC=-0.382 (n=32)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7557
  - _Potencial_: sin este filtro IC_bueno=-0.270 (n=98)

- **FILTRO** `volumen_spike_ratio` < `1.4324` → IC=-0.380 (n=23)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.4324
  - _Potencial_: sin este filtro IC_bueno=-0.284 (n=72)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.295 (n=115)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `drift_60min` |x|> `0.2366` → IC=-0.361 (n=34)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2366
  - _Potencial_: sin este filtro IC_bueno=-0.201 (n=105)

- **FILTRO** `volumen_pendiente_norm` > `0.1196` → IC=-0.265 (n=32)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1196
  - _Potencial_: sin este filtro IC_bueno=-0.241 (n=83)

- **FILTRO** `volumen_spike_ratio` < `1.5847` → IC=-0.267 (n=28)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.5847
  - _Potencial_: sin este filtro IC_bueno=-0.242 (n=87)

- **FILTRO** `libro_spread` > `0.06` → IC=-0.250 (n=30)

  - _Acción_: SKIP cuando `libro_spread` > 0.06
  - _Potencial_: sin este filtro IC_bueno=-0.241 (n=110)

- **FILTRO** `sigma_h` < `0.0115` → IC=-0.330 (n=45)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0115
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=16)

- **FILTRO** `volumen_regimen` < `0.9169` → IC=-0.455 (n=20)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9169
  - _Potencial_: sin este filtro IC_bueno=-0.128 (n=41)

- **FILTRO** `libro_spread` > `0.05` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.05
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=42)

### GBM_LATE_60M_PYCONFIRMADO
- **PATRÓN** `sigma_h` > `0.0075` → IC=+0.232 (n=341)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0075 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.190 (n=340)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 16.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` > `0.6774` → IC=+0.183 (n=749)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.6774 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.8192` → IC=+0.292 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8192 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.379` → IC=+0.157 (n=176)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 10.379 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `0.6242` → IC=+0.186 (n=250)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 0.6242 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` < `0.0701` → IC=+0.178 (n=560)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` < 0.0701 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `1.3961` → IC=+0.199 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3961 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.767` → IC=+0.145 (n=263)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 8.767 (IC base=+0.032)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.725` → IC=-0.167 (n=73)

  - _Acción_: SKIP cuando `ibs_20min` < 0.725
  - _Potencial_: sin este filtro IC_bueno=+0.112 (n=222)

- **PATRÓN** `sigma_h` > `0.0065` → IC=+0.149 (n=75)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` > 0.0065 (IC base=+0.042)

- **PATRÓN** `ibs_20min` > `0.7913` → IC=+0.125 (n=198)

  - _Acción_: Kelly boost +0.62€ cuando `ibs_20min` > 0.7913 (IC base=+0.042)

- **PATRÓN** `dist_vwap_pct` > `0.6315` → IC=+0.191 (n=40)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.6315 (IC base=+0.042)

- **PATRÓN** `ibs_20min` < `0.2413` → IC=+0.145 (n=415)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.2413 (IC base=+0.086)

- **PATRÓN** `volumen_pendiente_norm` > `0.2735` → IC=+0.144 (n=71)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_pendiente_norm` > 0.2735 (IC base=+0.086)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `volumen_pendiente_norm` > `0.1814` → IC=-0.167 (n=25)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1814
  - _Potencial_: sin este filtro IC_bueno=+0.141 (n=260)

- **FILTRO** `ibs_20min` > `0.15` → IC=-0.124 (n=147)

  - _Acción_: SKIP cuando `ibs_20min` > 0.15
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=288)

- **PATRÓN** `drift_60min` |x|≤ `0.1025` → IC=+0.133 (n=107)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.67€ cuando `drift_60min` |x|≤ 0.1025 (IC base=+0.115)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.155 (n=85)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 18.0 (IC base=+0.115)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.135 (n=83)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 5.0 (IC base=+0.115)

- **PATRÓN** `ibs_20min` > `0.7163` → IC=+0.145 (n=243)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` > 0.7163 (IC base=+0.115)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.38` → IC=+0.142 (n=252)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 9.38 (IC base=+0.115)

- **PATRÓN** `volumen_regimen` > `1.1915` → IC=+0.163 (n=81)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 1.1915 (IC base=+0.115)

- **PATRÓN** `volumen_pendiente_norm` < `0.1814` → IC=+0.141 (n=260)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` < 0.1814 (IC base=+0.115)

- **PATRÓN** `volumen_spike_ratio` < `2.0546` → IC=+0.154 (n=189)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.0546 (IC base=+0.115)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.126 (n=209)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.01 (IC base=+0.115)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.651` → IC=+0.196 (n=77)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 10.651 (IC base=+0.013)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.075` → IC=-0.226 (n=104)

  - _Acción_: SKIP cuando `ibs_20min` > 0.075
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=106)

- **FILTRO** `dist_vwap_pct` > `0.1871` → IC=-0.176 (n=35)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1871
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=175)

- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.273 (n=130)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0101 (IC base=+0.251)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.270 (n=294)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.251)

- **PATRÓN** `ibs_20min` > `0.6` → IC=+0.281 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6 (IC base=+0.251)

- **PATRÓN** `dist_vwap_pct` > `0.7282` → IC=+0.396 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7282 (IC base=+0.251)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.797` → IC=+0.332 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.797 (IC base=+0.251)

- **PATRÓN** `volumen_regimen` < `0.6071` → IC=+0.306 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6071 (IC base=+0.251)

- **PATRÓN** `volumen_pendiente_norm` > `0.0966` → IC=+0.304 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0966 (IC base=+0.251)

- **PATRÓN** `volumen_spike_ratio` < `1.3986` → IC=+0.335 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3986 (IC base=+0.251)

- **PATRÓN** `volumen_spike_ratio` > `2.3425` → IC=+0.295 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3425 (IC base=+0.251)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.252` → IC=+0.220 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.252 (IC base=-0.071)

### LATE_WINDOW_5MIN
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.326 (n=136)

- **PATRÓN** `drift_ventana_pct` |x|> `0.349` → IC=+0.332 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.349 (IC base=+0.321)

- **PATRÓN** `elapsed_s` > `209.2` → IC=+0.397 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 209.2 (IC base=+0.321)

- **PATRÓN** `drift_15min` |x|≤ `2.2347` → IC=+0.344 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.2347 (IC base=+0.321)

- **PATRÓN** `drift_60min` |x|≤ `0.9647` → IC=+0.382 (n=100)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9647 (IC base=+0.321)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.378 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.321)

- **PATRÓN** `ballena_activa_n` < `1114.0` → IC=+0.361 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1114.0 (IC base=+0.321)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3499` → IC=+0.290 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3499 (IC base=+0.274)

- **PATRÓN** `elapsed_s` > `227.0` → IC=+0.354 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 227.0 (IC base=+0.274)

- **PATRÓN** `drift_15min` |x|≤ `2.2537` → IC=+0.325 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.2537 (IC base=+0.274)

- **PATRÓN** `drift_60min` |x|≤ `0.6716` → IC=+0.310 (n=77)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6716 (IC base=+0.274)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.326 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.274)

- **PATRÓN** `ballena_activa_n` < `1342.0` → IC=+0.373 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1342.0 (IC base=+0.274)

### LATE_WINDOW_5MIN#BTC#5min
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.326 (n=136)

- **PATRÓN** `drift_ventana_pct` |x|> `0.349` → IC=+0.332 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.349 (IC base=+0.321)

- **PATRÓN** `elapsed_s` > `209.2` → IC=+0.397 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 209.2 (IC base=+0.321)

- **PATRÓN** `drift_15min` |x|≤ `2.2347` → IC=+0.344 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.2347 (IC base=+0.321)

- **PATRÓN** `drift_60min` |x|≤ `0.9647` → IC=+0.382 (n=100)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9647 (IC base=+0.321)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.378 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.321)

- **PATRÓN** `ballena_activa_n` < `1114.0` → IC=+0.361 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1114.0 (IC base=+0.321)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3499` → IC=+0.290 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3499 (IC base=+0.274)

- **PATRÓN** `elapsed_s` > `227.0` → IC=+0.354 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 227.0 (IC base=+0.274)

- **PATRÓN** `drift_15min` |x|≤ `2.2537` → IC=+0.325 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.2537 (IC base=+0.274)

- **PATRÓN** `drift_60min` |x|≤ `0.6716` → IC=+0.310 (n=77)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6716 (IC base=+0.274)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.326 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.274)

- **PATRÓN** `ballena_activa_n` < `1342.0` → IC=+0.373 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1342.0 (IC base=+0.274)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.123 (n=1486)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` > 0.5 (IC base=+0.096)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.123 (n=1486)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` > 0.5 (IC base=+0.096)

### LIQUIDACIONES_15M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=256)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=256)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=1063)

### LIQUIDACIONES_15M#BNB#15min
- **PATRÓN** `liq_n` > `2.0` → IC=+0.217 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `liq_n` > 2.0 (IC base=+0.080)

- **PATRÓN** `liq_usd_total` > `1558.02` → IC=+0.239 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `liq_usd_total` > 1558.02 (IC base=+0.080)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.133 (n=77)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.03 (IC base=+0.080)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `libro_liquidez` < `12324.2702` → IC=-0.152 (n=44)

  - _Acción_: SKIP cuando `libro_liquidez` < 12324.2702
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=92)

### LIQUIDACIONES_15M#DOGE#15min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.180 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=46)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.300 (n=18)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.021)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `liq_usd_total` < `1802.5` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `liq_usd_total` < 1802.5
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=41)

- **FILTRO** `py_entrada` < `0.415` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.415
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=45)

### LIQUIDACIONES_15M#SOL#15min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=23)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=262)

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
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=4023)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=181)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.093 (n=138)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.278 (n=34)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=168)

- **FILTRO** `ballena_activa_n` > `44.0` → IC=-0.182 (n=83)

  - _Acción_: SKIP cuando `ballena_activa_n` > 44.0
  - _Potencial_: sin este filtro IC_bueno=+0.213 (n=85)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.213 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=-0.025)

### LIQUIDACIONES_5M#BTC#5min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.167 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=15)

- **FILTRO** `libro_liquidez` < `13988.6712` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `libro_liquidez` < 13988.6712
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=19)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.121 (n=275)

  - _Acción_: Kelly boost +0.60€ cuando `py_entrada` < 0.495 (IC base=+0.023)

### LIQUIDACIONES_5M#DOGE#5min
- **PATRÓN** `liq_n` > `3.0` → IC=+0.300 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `liq_n` > 3.0 (IC base=+0.229)

- **PATRÓN** `liq_usd_total` > `2217.29` → IC=+0.341 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `liq_usd_total` > 2217.29 (IC base=+0.229)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.231 (n=24)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.229)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.246 (n=65)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.229)

- **PATRÓN** `libro_liquidez` > `2732.2827` → IC=+0.250 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2732.2827 (IC base=+0.229)

- **PATRÓN** `ballena_activa_n` < `6.0` → IC=+0.269 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 6.0 (IC base=+0.229)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=1616)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=1570)

- **FILTRO** `hora_utc` > `5.0` → IC=-0.286 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=10)

### LIQUIDACIONES_5M#SOL#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=734)

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
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=491)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=472)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.142 (n=205)

  - _Acción_: Kelly boost +0.71€ cuando `py_entrada` < 0.495 (IC base=+0.009)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=1044)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=1044)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=1356)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=1356)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=305)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=305)

- **FILTRO** `py_entrada` < `0.43` → IC=-0.132 (n=104)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=216)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.136 (n=64)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=374)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=423)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=311)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=413)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=413)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.120 (n=185)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=258)

- **FILTRO** `libro_liquidez` < `564.286` → IC=-0.143 (n=110)

  - _Acción_: SKIP cuando `libro_liquidez` < 564.286
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=333)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=388)

### LIQUIDACIONES_DEPTH_FASE0#BNB#15min
- **FILTRO** `py_entrada` > `0.6` → IC=-0.141 (n=37)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=82)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.180 (n=95)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=115)

- **FILTRO** `hora_utc` > `14.0` → IC=-0.135 (n=94)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=116)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.152 (n=44)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=45)

- **FILTRO** `hora_utc` < `17.0` → IC=-0.142 (n=65)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.077 (n=24)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **FILTRO** `py_entrada` > `0.57` → IC=-0.122 (n=458)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=553)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.148 (n=336)

  - _Acción_: Kelly boost +0.74€ cuando `py_entrada` < 0.5 (IC base=-0.009)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.129 (n=173)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=393)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.124 (n=589)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=640)

- **FILTRO** `py_entrada` > `0.58` → IC=-0.123 (n=369)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=439)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.131 (n=299)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=648)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.126 (n=650)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=348)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.41` → IC=-0.160 (n=374)

  - _Acción_: SKIP cuando `py_entrada` < 0.41
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=778)

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

- **FILTRO** `py_entrada` > `0.505` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=2289)

### MOMENTUM_IBS_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=1413)

### MOMENTUM_IBS_15M_BALLENA
- **FILTRO** `py_entrada` < `0.46` → IC=-0.175 (n=8316)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=26307)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.171 (n=8748)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=27148)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.194 (n=1548)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.114 (n=4883)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.143 (n=2138)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.094 (n=4223)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.137 (n=1648)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` > 1.0 (IC base=+0.040)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.133 (n=2972)

  - _Acción_: Kelly boost +0.66€ cuando `py_entrada` < 0.5 (IC base=+0.014)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` < `0.44` → IC=-0.174 (n=1157)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=3622)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.180 (n=1234)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=3804)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` > `0.62` → IC=-0.197 (n=1590)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.087 (n=4928)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.136 (n=1970)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` > 1.0 (IC base=+0.033)

- **PATRÓN** `libro_liquidez` > `1738.12` → IC=+0.121 (n=2181)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 1738.12 (IC base=+0.033)

### MOMENTUM_IBS_15M_BALLENA#ETH#15min
- **FILTRO** `py_entrada` > `0.575` → IC=-0.175 (n=1256)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=3865)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.485` → IC=-0.162 (n=1599)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=4858)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=2448)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.162 (n=772)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=2372)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.180 (n=973)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=3138)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=4090)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` < `14.0` → IC=-0.157 (n=135)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=437)

- **FILTRO** `hora_utc` > `20.0` → IC=-0.146 (n=125)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 20.0
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=447)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.198 (n=336)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=1105)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `py_entrada` < `0.395` → IC=-0.230 (n=72)

  - _Acción_: SKIP cuando `py_entrada` < 0.395
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=262)

- **FILTRO** `libro_liquidez` < `3613.7014` → IC=-0.152 (n=110)

  - _Acción_: SKIP cuando `libro_liquidez` < 3613.7014
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=224)

- **FILTRO** `hora_utc` < `7.0` → IC=-0.204 (n=113)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.098 (n=364)

- **FILTRO** `drift_20min_pct` |x|> `0.2022` → IC=-0.136 (n=119)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.2022
  - _Potencial_: sin este filtro IC_bueno=-0.119 (n=358)

- **FILTRO** `libro_liquidez` < `3239.0468` → IC=-0.185 (n=157)

  - _Acción_: SKIP cuando `libro_liquidez` < 3239.0468
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=320)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.192 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=979)

- **FILTRO** `libro_liquidez` < `1989.4319` → IC=-0.141 (n=396)

  - _Acción_: SKIP cuando `libro_liquidez` < 1989.4319
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=807)

### MOMENTUM_IBS_15M_FADE#XRP#15min
- **FILTRO** `hora_utc` < `13.0` → IC=-0.238 (n=59)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 13.0
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=242)

### MOMENTUM_IBS_5M#BNB#5min
- **FILTRO** `hora_utc` > `17.0` → IC=-0.157 (n=33)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=45)

- **FILTRO** `drift_7min_pct` |x|> `0.0725` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.0725
  - _Potencial_: sin este filtro IC_bueno=+0.133 (n=28)

- **PATRÓN** `drift_7min_pct` |x|≤ `0.0331` → IC=+0.214 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `drift_7min_pct` |x|≤ 0.0331 (IC base=-0.026)

### MOMENTUM_IBS_5M#BTC#5min
- **FILTRO** `hora_utc` > `18.0` → IC=-0.208 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 18.0
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=93)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.125 (n=46)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 17.0 (IC base=+0.024)

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

### MOMENTUM_IBS_5M_BALLENA
- **FILTRO** `hora_utc` < `8.0` → IC=-0.136 (n=23469)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.091 (n=53326)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.299 (n=18536)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=58259)

- **FILTRO** `ibs_7min` < `0.2143` → IC=-0.236 (n=19160)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2143
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=57635)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.153 (n=25912)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=50883)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.245 (n=23953)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=72153)

- **FILTRO** `ibs_7min` > `0.28` → IC=-0.182 (n=24002)

  - _Acción_: SKIP cuando `ibs_7min` > 0.28
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=72104)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.160 (n=3291)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=10460)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.320 (n=3394)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=10357)

- **FILTRO** `ibs_7min` < `0.7105` → IC=-0.253 (n=4535)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7105
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=9216)

- **FILTRO** `py_entrada` > `0.72` → IC=-0.279 (n=4028)

  - _Acción_: SKIP cuando `py_entrada` > 0.72
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=12584)

- **FILTRO** `ibs_7min` > `0.7715` → IC=-0.211 (n=4152)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7715
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=12460)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.264 (n=3089)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=9647)

- **FILTRO** `ibs_7min` < `0.7134` → IC=-0.211 (n=3184)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7134
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=9552)

- **FILTRO** `ballena_activa_n` > `156.0` → IC=-0.201 (n=3175)

  - _Acción_: SKIP cuando `ballena_activa_n` > 156.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=9561)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.267 (n=2976)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=10048)

- **FILTRO** `ibs_7min` > `0.2651` → IC=-0.192 (n=3255)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2651
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=9769)

- **FILTRO** `ballena_activa_n` > `152.0` → IC=-0.178 (n=3254)

  - _Acción_: SKIP cuando `ballena_activa_n` > 152.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=9770)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.167 (n=3146)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=10039)

- **FILTRO** `py_entrada` < `0.3` → IC=-0.324 (n=3139)

  - _Acción_: SKIP cuando `py_entrada` < 0.3
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=10046)

- **FILTRO** `ibs_7min` < `0.2884` → IC=-0.251 (n=4351)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2884
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=8834)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.202 (n=2559)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=10626)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.259 (n=4231)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=13366)

- **FILTRO** `ibs_7min` > `0.7248` → IC=-0.183 (n=4398)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7248
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=13199)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.264 (n=3083)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=9322)

- **FILTRO** `ibs_7min` < `0.7132` → IC=-0.200 (n=3101)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7132
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=9304)

- **FILTRO** `ballena_activa_n` > `24.0` → IC=-0.191 (n=3100)

  - _Acción_: SKIP cuando `ballena_activa_n` > 24.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=9305)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.260 (n=3001)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=9907)

- **FILTRO** `ibs_7min` > `0.2723` → IC=-0.178 (n=3225)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2723
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=9683)

- **FILTRO** `ballena_activa_n` > `23.0` → IC=-0.169 (n=3223)

  - _Acción_: SKIP cuando `ballena_activa_n` > 23.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=9685)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.32` → IC=-0.302 (n=2951)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=9321)

- **FILTRO** `ibs_7min` < `0.7` → IC=-0.236 (n=4039)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=8233)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.219 (n=3008)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=9264)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.199 (n=4467)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=14127)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.133 (n=4008)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.110 (n=8438)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.312 (n=3006)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=9440)

- **FILTRO** `ibs_7min` < `0.73` → IC=-0.224 (n=4097)

  - _Acción_: SKIP cuando `ibs_7min` < 0.73
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=8349)

- **FILTRO** `ballena_activa_n` > `9.0` → IC=-0.208 (n=2747)

  - _Acción_: SKIP cuando `ballena_activa_n` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.092 (n=9699)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.228 (n=4297)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=13074)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1046` → IC=-0.135 (n=61)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1046
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=121)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `py_entrada` < `0.455` → IC=-0.163 (n=304)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=1015)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=1304)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=1458)

- **FILTRO** `py_entrada` > `0.565` → IC=-0.172 (n=260)

  - _Acción_: SKIP cuando `py_entrada` > 0.565
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=915)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `ballena_activa_n` > `3.0` → IC=-0.143 (n=166)

  - _Acción_: SKIP cuando `ballena_activa_n` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=333)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.231 (n=50)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=450)

- **FILTRO** `py_entrada` > `0.58` → IC=-0.216 (n=192)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=585)

- **FILTRO** `libro_liquidez` < `3305.4837` → IC=-0.148 (n=194)

  - _Acción_: SKIP cuando `libro_liquidez` < 3305.4837
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=583)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.4307` → IC=+0.147 (n=706)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.73€ cuando `delta_ratio` |x|> 0.4307 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.130 (n=1402)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 14.0 (IC base=+0.125)

- **PATRÓN** `total_vol_5m` < `422.506` → IC=+0.158 (n=519)

  - _Acción_: Kelly boost +0.79€ cuando `total_vol_5m` < 422.506 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `3557.6032` → IC=+0.138 (n=705)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 3557.6032 (IC base=+0.125)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `14.0` → IC=+0.179 (n=185)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 14.0 (IC base=+0.135)

- **PATRÓN** `total_vol_5m` < `372.075` → IC=+0.159 (n=323)

  - _Acción_: Kelly boost +0.79€ cuando `total_vol_5m` < 372.075 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `2520.4138` → IC=+0.236 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2520.4138 (IC base=+0.135)

- **PATRÓN** `ballena_activa_n` < `6.0` → IC=+0.141 (n=182)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 6.0 (IC base=+0.135)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `delta_ratio` |x|> `0.3994` → IC=+0.136 (n=322)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.68€ cuando `delta_ratio` |x|> 0.3994 (IC base=+0.121)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.138 (n=302)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 15.0 (IC base=+0.121)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4162` → IC=+0.175 (n=195)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.88€ cuando `delta_ratio` |x|> 0.4162 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.151 (n=270)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 5.0 (IC base=+0.129)

- **PATRÓN** `total_vol_5m` < `852.6939` → IC=+0.157 (n=292)

  - _Acción_: Kelly boost +0.78€ cuando `total_vol_5m` < 852.6939 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `59.0` → IC=+0.176 (n=100)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 59.0 (IC base=+0.129)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.3978` → IC=+0.167 (n=262)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.83€ cuando `delta_ratio` |x|> 0.3978 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.172 (n=190)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 12.0 (IC base=+0.141)

- **PATRÓN** `total_vol_5m` < `4621.455` → IC=+0.178 (n=175)

  - _Acción_: Kelly boost +0.89€ cuando `total_vol_5m` < 4621.455 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `3720.1604` → IC=+0.155 (n=175)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 3720.1604 (IC base=+0.141)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `hora_utc` < `14.0` → IC=+0.130 (n=287)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 14.0 (IC base=+0.098)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.134 (n=203)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.098)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `7.3154` → IC=-0.250 (n=58)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 7.3154
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=176)

- **FILTRO** `pct_vs_K` |x|> `3.3889` → IC=-0.179 (n=306)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.3889
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=597)

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.157 (n=298)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0045 (IC base=-0.045)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `pct_vs_K` |x|> `4.2515` → IC=-0.239 (n=67)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.2515
  - _Potencial_: sin este filtro IC_bueno=+0.078 (n=204)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.293 (n=90)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=-0.002)

- **PATRÓN** `pct_vs_K` |x|≤ `1.73` → IC=+0.196 (n=90)

  - _Acción_: Kelly boost +0.98€ cuando `pct_vs_K` |x|≤ 1.73 (IC base=-0.002)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `T_h` < `251.7955` → IC=-0.192 (n=63)

  - _Acción_: SKIP cuando `T_h` < 251.7955
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=21)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `T_h` < `69.4642` → IC=-0.144 (n=57)

  - _Acción_: SKIP cuando `T_h` < 69.4642
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=116)

### PRICE_TARGET_GBM#SOL#reach
- **FILTRO** `sigma_h` < `0.0164` → IC=-0.192 (n=24)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0164
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

- **FILTRO** `T_h` < `146.0708` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `T_h` < 146.0708
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=16)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0115` → IC=-0.240 (n=605)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0115
  - _Potencial_: sin este filtro IC_bueno=-0.194 (n=204)

- **FILTRO** `T_h` < `113.0321` → IC=-0.240 (n=533)

  - _Acción_: SKIP cuando `T_h` < 113.0321
  - _Potencial_: sin este filtro IC_bueno=-0.205 (n=276)

- **FILTRO** `sigma_h` < `0.0076` → IC=-0.190 (n=356)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0076
  - _Potencial_: sin este filtro IC_bueno=-0.132 (n=357)

- **FILTRO** `pct_vs_K` |x|> `3.0033` → IC=-0.400 (n=178)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.0033
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=535)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `sigma_h` < `0.009` → IC=-0.207 (n=172)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.009
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=92)

- **FILTRO** `T_h` < `60.8769` → IC=-0.219 (n=87)

  - _Acción_: SKIP cuando `T_h` < 60.8769
  - _Potencial_: sin este filtro IC_bueno=-0.193 (n=177)

- **FILTRO** `T_h` > `143.4358` → IC=-0.216 (n=65)

  - _Acción_: SKIP cuando `T_h` > 143.4358
  - _Potencial_: sin este filtro IC_bueno=-0.157 (n=199)

- **FILTRO** `pct_vs_K` |x|> `2.4709` → IC=-0.346 (n=89)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.4709
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=175)

### PRICE_TARGET_GBM_FADE#BTC#reach
- **FILTRO** `T_h` < `139.5329` → IC=-0.340 (n=23)

  - _Acción_: SKIP cuando `T_h` < 139.5329
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=13)

- **FILTRO** `sigma_h` < `0.0089` → IC=-0.241 (n=25)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0089
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **FILTRO** `T_h` > `144.6658` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `T_h` > 144.6658
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=18)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `sigma_h` < `0.0091` → IC=-0.322 (n=116)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0091
  - _Potencial_: sin este filtro IC_bueno=-0.246 (n=116)

- **FILTRO** `T_h` < `68.1921` → IC=-0.295 (n=76)

  - _Acción_: SKIP cuando `T_h` < 68.1921
  - _Potencial_: sin este filtro IC_bueno=-0.279 (n=156)

- **FILTRO** `sigma_h` < `0.0055` → IC=-0.209 (n=53)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0055
  - _Potencial_: sin este filtro IC_bueno=-0.110 (n=162)

- **FILTRO** `T_h` > `56.6209` → IC=-0.199 (n=144)

  - _Acción_: SKIP cuando `T_h` > 56.6209
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=71)

- **FILTRO** `pct_vs_K` |x|> `2.875` → IC=-0.393 (n=73)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.875
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=142)

- **PATRÓN** `pct_vs_K` |x|≤ `0.9248` → IC=+0.196 (n=54)

  - _Acción_: Kelly boost +0.98€ cuando `pct_vs_K` |x|≤ 0.9248 (IC base=-0.136)

### PRICE_TARGET_GBM_FADE#ETH#reach
- **FILTRO** `sigma_h` < `0.0095` → IC=-0.152 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0095
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **FILTRO** `T_h` < `132.3532` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `T_h` < 132.3532
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=10)

- **FILTRO** `sigma_h` < `0.0098` → IC=-0.222 (n=16)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0098
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=17)

- **FILTRO** `T_h` > `145.2755` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `T_h` > 145.2755
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=17)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0147` → IC=-0.207 (n=56)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0147
  - _Potencial_: sin este filtro IC_bueno=-0.201 (n=172)

- **FILTRO** `sigma_h` < `0.0085` → IC=-0.246 (n=57)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0085
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=171)

- **FILTRO** `T_h` > `64.3086` → IC=-0.221 (n=170)

  - _Acción_: SKIP cuando `T_h` > 64.3086
  - _Potencial_: sin este filtro IC_bueno=-0.150 (n=58)

- **FILTRO** `sigma_h` > `0.0139` → IC=-0.318 (n=53)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0139
  - _Potencial_: sin este filtro IC_bueno=-0.094 (n=104)

- **FILTRO** `sigma_h` < `0.0087` → IC=-0.281 (n=39)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0087
  - _Potencial_: sin este filtro IC_bueno=-0.133 (n=118)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1171` → IC=+0.443 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1171 (IC base=+0.331)

- **PATRÓN** `sigma_h` > `0.0128` → IC=+0.354 (n=53)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0128 (IC base=+0.331)

- **PATRÓN** `T_h` < `0.3392` → IC=+0.402 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.3392 (IC base=+0.331)

- **PATRÓN** `T_h` > `0.8789` → IC=+0.375 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.8789 (IC base=+0.331)

- **PATRÓN** `dist_50` > `0.4692` → IC=+0.482 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4692 (IC base=+0.331)

- **PATRÓN** `edge` > `0.1005` → IC=+0.427 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1005 (IC base=+0.389)

- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.409 (n=184)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0097 (IC base=+0.389)

- **PATRÓN** `T_h` < `0.7218` → IC=+0.418 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.7218 (IC base=+0.389)

- **PATRÓN** `T_h` > `1.4833` → IC=+0.393 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4833 (IC base=+0.389)

- **PATRÓN** `dist_50` > `0.3653` → IC=+0.442 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3653 (IC base=+0.389)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.410 (n=333)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.389)

### RESOLUTION_SNIPER#BTC#sniper
- **PATRÓN** `edge` > `0.1235` → IC=+0.274 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1235 (IC base=+0.174)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.259 (n=27)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.174)

- **PATRÓN** `sigma_h` > `0.0092` → IC=+0.210 (n=29)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0092 (IC base=+0.174)

- **PATRÓN** `T_h` > `0.8187` → IC=+0.196 (n=54)

  - _Acción_: Kelly boost +0.98€ cuando `T_h` > 0.8187 (IC base=+0.174)

- **PATRÓN** `dist_50` > `0.3225` → IC=+0.290 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3225 (IC base=+0.174)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.226 (n=60)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.174)

### RESOLUTION_SNIPER#ETH#sniper
- **PATRÓN** `edge` > `0.1023` → IC=+0.464 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1023 (IC base=+0.407)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.421 (n=61)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0103 (IC base=+0.407)

- **PATRÓN** `T_h` < `1.2415` → IC=+0.436 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 1.2415 (IC base=+0.407)

- **PATRÓN** `dist_50` > `0.4084` → IC=+0.482 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4084 (IC base=+0.407)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.444 (n=34)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.407)

### RESOLUTION_SNIPER#SOL#sniper
- **PATRÓN** `edge` > `0.175` → IC=+0.486 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.175 (IC base=+0.436)

- **PATRÓN** `sigma_h` < `0.0155` → IC=+0.468 (n=60)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0155 (IC base=+0.436)

- **PATRÓN** `T_h` > `0.5264` → IC=+0.452 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.5264 (IC base=+0.436)

- **PATRÓN** `dist_50` > `0.354` → IC=+0.471 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.354 (IC base=+0.436)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.441 (n=32)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.436)

- **PATRÓN** `edge` > `0.2005` → IC=+0.471 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.2005 (IC base=+0.463)

- **PATRÓN** `sigma_h` < `0.0156` → IC=+0.474 (n=152)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0156 (IC base=+0.463)

- **PATRÓN** `T_h` < `0.8021` → IC=+0.457 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.8021 (IC base=+0.463)

- **PATRÓN** `T_h` > `1.4857` → IC=+0.481 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4857 (IC base=+0.463)

- **PATRÓN** `dist_50` > `0.4578` → IC=+0.493 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4578 (IC base=+0.463)

- **PATRÓN** `hora_utc` < `2.0` → IC=+0.485 (n=63)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 2.0 (IC base=+0.463)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=454)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.072 (n=491)

- **PATRÓN** `streak_estiramiento` < `0.8175` → IC=+0.127 (n=338)

  - _Acción_: Kelly boost +0.63€ cuando `streak_estiramiento` < 0.8175 (IC base=+0.060)

- **PATRÓN** `ballena_activa_n` < `29.0` → IC=+0.124 (n=251)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 29.0 (IC base=+0.060)

### STREAK_FADE_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=17)

- **PATRÓN** `ballena_activa_n` < `58.0` → IC=+0.147 (n=15)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 58.0 (IC base=+0.078)

### STREAK_FADE_15M#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=30)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.140 (n=23)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.140 (n=23)

  - _Acción_: Kelly boost +0.70€ cuando `py_entrada` < 0.495 (IC base=+0.025)

### STREAK_FADE_15M#XRP#15min
- **FILTRO** `regimen_ma_toques` < `2.0` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `regimen_ma_toques` < 2.0
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=195)

- **FILTRO** `streak_estiramiento` > `0.5115` → IC=-0.173 (n=53)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.5115
  - _Potencial_: sin este filtro IC_bueno=+0.094 (n=163)

- **PATRÓN** `streak_estiramiento` < `0.2033` → IC=+0.149 (n=55)

  - _Acción_: Kelly boost +0.75€ cuando `streak_estiramiento` < 0.2033 (IC base=+0.022)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.145 (n=122)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 11.0 (IC base=+0.093)

- **PATRÓN** `streak_estiramiento` < `0.5637` → IC=+0.173 (n=166)

  - _Acción_: Kelly boost +0.86€ cuando `streak_estiramiento` < 0.5637 (IC base=+0.093)

- **PATRÓN** `ballena_activa_n` < `31.0` → IC=+0.156 (n=161)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 31.0 (IC base=+0.093)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.194 (n=47)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=92)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=71)

- **FILTRO** `libro_liquidez` < `3678.6572` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 3678.6572
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=78)

- **FILTRO** `streak_len` > `3.0` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=53)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.136 (n=31)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=38)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=820)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=826)

### STREAK_FADE_60M
- **FILTRO** `py_entrada` < `0.515` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=23)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=23)

- **FILTRO** `streak_estiramiento` > `0.6439` → IC=-0.123 (n=59)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.6439
  - _Potencial_: sin este filtro IC_bueno=+0.182 (n=20)

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
- **PATRÓN** `streak_estiramiento` < `0.6439` → IC=+0.167 (n=19)

  - _Acción_: Kelly boost +0.83€ cuando `streak_estiramiento` < 0.6439 (IC base=+0.017)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=1085)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=1349)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=1244)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=1305)

### STRUCT_NO_15M
- **FILTRO** `hora_utc` < `15.0` → IC=-0.167 (n=25)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.107 (n=26)

- **FILTRO** `hora_utc` > `4.0` → IC=-0.167 (n=37)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=14)

- **FILTRO** `py_entrada` < `0.455` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.105 (n=36)

- **FILTRO** `libro_liquidez` < `6744.0765` → IC=-0.175 (n=38)

  - _Acción_: SKIP cuando `libro_liquidez` < 6744.0765
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=13)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=5094)

### STRUCT_NO_15M#ETH#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.167 (n=25)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.107 (n=26)

- **FILTRO** `hora_utc` > `4.0` → IC=-0.167 (n=37)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=14)

- **FILTRO** `py_entrada` < `0.455` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.105 (n=36)

- **FILTRO** `libro_liquidez` < `6744.0765` → IC=-0.175 (n=38)

  - _Acción_: SKIP cuando `libro_liquidez` < 6744.0765
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=13)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=2952)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0055` → IC=+0.184 (n=1888)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0055 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.224` → IC=+0.158 (n=5661)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.224 (IC base=+0.138)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1339` → IC=+0.153 (n=2337)

  - _Acción_: Kelly boost +0.77€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1339 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.145 (n=5982)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 4.0 (IC base=+0.138)

- **PATRÓN** `ibs_15` > `0.5714` → IC=+0.219 (n=5069)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5714 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` > `0.1371` → IC=+0.128 (n=2605)

  - _Acción_: Kelly boost +0.64€ cuando `dist_vwap_pct` > 0.1371 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.234` → IC=+0.239 (n=1069)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.234 (IC base=+0.138)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=3177)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `4471.5193` → IC=+0.171 (n=1887)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 4471.5193 (IC base=+0.138)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=2214)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.219 (n=819)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.202)

- **PATRÓN** `drift_60min` |x|≤ `0.058` → IC=+0.256 (n=273)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.058 (IC base=+0.202)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2675` → IC=+0.227 (n=273)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2675 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.229 (n=754)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.202)

- **PATRÓN** `ibs_15` > `0.7077` → IC=+0.272 (n=819)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7077 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` > `0.3751` → IC=+0.225 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3751 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` < `0.1096` → IC=+0.204 (n=558)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1096 (IC base=+0.202)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.371` → IC=+0.310 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.371 (IC base=+0.202)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.205 (n=1061)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `11832.5463` → IC=+0.219 (n=546)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11832.5463 (IC base=+0.202)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.146 (n=1021)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0071 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.1091` → IC=+0.150 (n=681)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.1091 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.139 (n=934)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 6.0 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.134 (n=1024)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 16.0 (IC base=+0.133)

- **PATRÓN** `ibs_15` > `0.4915` → IC=+0.220 (n=1021)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.4915 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` > `0.1194` → IC=+0.151 (n=632)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.1194 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.063` → IC=+0.283 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.063 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `6020.1719` → IC=+0.173 (n=463)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 6020.1719 (IC base=+0.133)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `ibs_15` > `0.7627` → IC=+0.129 (n=744)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.64€ cuando `ibs_15` > 0.7627 (IC base=+0.050)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` < `0.0192` → IC=+0.166 (n=957)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0192 (IC base=+0.151)

- **PATRÓN** `sigma_h` > `0.0126` → IC=+0.154 (n=1435)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` > 0.0126 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.228` → IC=+0.178 (n=1436)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.228 (IC base=+0.151)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.095` → IC=+0.213 (n=444)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.095 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.156 (n=1321)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 6.0 (IC base=+0.151)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.152 (n=1017)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 11.0 (IC base=+0.151)

- **PATRÓN** `ibs_15` > `0.5333` → IC=+0.222 (n=1286)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5333 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` > `0.2002` → IC=+0.169 (n=645)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.2002 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.649` → IC=+0.183 (n=238)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 21.649 (IC base=+0.151)

- **PATRÓN** `libro_liquidez` > `2939.6834` → IC=+0.192 (n=651)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 2939.6834 (IC base=+0.151)

- **PATRÓN** `ibs_15` < `0.1139` → IC=+0.151 (n=1100)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.75€ cuando `ibs_15` < 0.1139 (IC base=+0.069)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` > `0.0054` → IC=+0.397 (n=346)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0054 (IC base=+0.364)

- **PATRÓN** `drift_60min` |x|≤ `0.1109` → IC=+0.365 (n=508)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1109 (IC base=+0.364)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1501` → IC=+0.378 (n=507)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1501 (IC base=+0.364)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.134` → IC=+0.380 (n=297)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.134 (IC base=+0.364)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.373 (n=803)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.364)

- **PATRÓN** `ibs_15` > `0.7903` → IC=+0.394 (n=762)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7903 (IC base=+0.364)

- **PATRÓN** `dist_vwap_pct` > `0.1529` → IC=+0.381 (n=451)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1529 (IC base=+0.364)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.963` → IC=+0.396 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.963 (IC base=+0.364)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.368 (n=927)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.364)

- **PATRÓN** `libro_liquidez` > `3882.8993` → IC=+0.374 (n=681)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3882.8993 (IC base=+0.364)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.404 (n=123)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0051 (IC base=+0.362)

- **PATRÓN** `drift_60min` |x|≤ `0.1523` → IC=+0.362 (n=325)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1523 (IC base=+0.362)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2196` → IC=+0.376 (n=167)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2196 (IC base=+0.362)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1436` → IC=+0.399 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1436 (IC base=+0.362)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.381 (n=341)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.362)

- **PATRÓN** `ibs_15` > `0.8078` → IC=+0.384 (n=369)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8078 (IC base=+0.362)

- **PATRÓN** `dist_vwap_pct` > `0.3751` → IC=+0.392 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3751 (IC base=+0.362)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.163` → IC=+0.392 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.163 (IC base=+0.362)

- **PATRÓN** `libro_liquidez` > `8119.484` → IC=+0.384 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8119.484 (IC base=+0.362)

- **PATRÓN** `ballena_activa_n` < `487.0` → IC=+0.401 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 487.0 (IC base=+0.362)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.369 (n=394)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.365)

- **PATRÓN** `sigma_h` > `0.006` → IC=+0.384 (n=179)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.006 (IC base=+0.365)

- **PATRÓN** `drift_60min` |x|≤ `0.1074` → IC=+0.368 (n=263)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1074 (IC base=+0.365)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1293` → IC=+0.383 (n=262)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1293 (IC base=+0.365)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2951` → IC=+0.373 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2951 (IC base=+0.365)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.371 (n=394)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.365)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.371 (n=184)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.365)

- **PATRÓN** `ibs_15` > `0.764` → IC=+0.394 (n=393)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.764 (IC base=+0.365)

- **PATRÓN** `dist_vwap_pct` > `0.1212` → IC=+0.373 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1212 (IC base=+0.365)

- **PATRÓN** `dist_vwap_pct` < `0.2796` → IC=+0.365 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2796 (IC base=+0.365)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.356` → IC=+0.392 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.356 (IC base=+0.365)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.368 (n=446)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.365)

- **PATRÓN** `libro_liquidez` > `4202.8422` → IC=+0.379 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4202.8422 (IC base=+0.365)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0075` → IC=-0.201 (n=2783)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0075
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=2784)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.221 (n=2365)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=3202)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1411` → IC=+0.215 (n=478)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1411 (IC base=-0.085)

- **PATRÓN** `ibs_15` > `0.6307` → IC=+0.275 (n=1255)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6307 (IC base=-0.085)

- **PATRÓN** `dist_vwap_pct` > `0.1113` → IC=+0.199 (n=731)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.1113 (IC base=-0.085)

- **PATRÓN** `dist_vwap_pct` < `0.2602` → IC=+0.196 (n=1081)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` < 0.2602 (IC base=-0.085)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2325` → IC=+0.272 (n=1724)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2325 (IC base=-0.001)

- **PATRÓN** `ibs_15` < `0.3704` → IC=+0.286 (n=5170)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3704 (IC base=-0.001)

- **PATRÓN** `dist_vwap_pct` > `0.6647` → IC=+0.285 (n=705)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6647 (IC base=-0.001)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0433` → IC=-0.226 (n=2398)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0433
  - _Potencial_: sin este filtro IC_bueno=-0.098 (n=1185)

- **FILTRO** `sigma_ewma_delta_pct` > `22.158` → IC=-0.247 (n=505)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 22.158
  - _Potencial_: sin este filtro IC_bueno=-0.173 (n=3078)

- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.149 (n=340)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0031 (IC base=+0.067)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2673` → IC=+0.287 (n=148)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2673 (IC base=+0.067)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1453` → IC=+0.267 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1453 (IC base=+0.067)

- **PATRÓN** `ibs_15` > `0.7639` → IC=+0.314 (n=444)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7639 (IC base=+0.067)

- **PATRÓN** `dist_vwap_pct` > `0.1041` → IC=+0.272 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1041 (IC base=+0.067)

- **PATRÓN** `dist_vwap_pct` < `0.2432` → IC=+0.274 (n=401)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2432 (IC base=+0.067)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.088` → IC=+0.149 (n=226)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 22.088 (IC base=+0.067)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0742` → IC=+0.224 (n=74)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0742 (IC base=-0.184)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0866` → IC=+0.308 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0866 (IC base=-0.184)

- **PATRÓN** `ibs_15` < `0.6255` → IC=+0.289 (n=74)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.6255 (IC base=-0.184)

- **PATRÓN** `dist_vwap_pct` < `0.0453` → IC=+0.303 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0453 (IC base=-0.184)

- **PATRÓN** `ballena_activa_n` < `393.0` → IC=+0.300 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 393.0 (IC base=-0.184)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.152 (n=819)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.159 (n=552)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0059 (IC base=+0.146)

- **PATRÓN** `sigma_h` > `0.0052` → IC=+0.150 (n=418)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` > 0.0052 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.159` → IC=+0.163 (n=553)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.159 (IC base=+0.146)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3014` → IC=+0.196 (n=492)

  - _Acción_: Kelly boost +0.98€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3014 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.162 (n=448)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 11.0 (IC base=+0.146)

- **PATRÓN** `ibs_15` > `0.5684` → IC=+0.239 (n=627)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5684 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.6245` → IC=+0.161 (n=116)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 0.6245 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` < `0.2675` → IC=+0.147 (n=585)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.2675 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.001` → IC=+0.258 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.001 (IC base=+0.146)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=819)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `7295.1819` → IC=+0.162 (n=285)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 7295.1819 (IC base=+0.146)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.256 (n=1349)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0062 (IC base=+0.245)

- **PATRÓN** `drift_60min` |x|≤ `0.3616` → IC=+0.247 (n=1781)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3616 (IC base=+0.245)

- **PATRÓN** `drift_15min` |x|≤ `0.7918` → IC=+0.257 (n=1781)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7918 (IC base=+0.245)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2095` → IC=+0.266 (n=917)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2095 (IC base=+0.245)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.258 (n=749)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.245)

- **PATRÓN** `ibs_15` < `0.3851` → IC=+0.274 (n=2023)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3851 (IC base=+0.245)

- **PATRÓN** `dist_vwap_pct` > `0.3838` → IC=+0.275 (n=486)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3838 (IC base=+0.245)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.409` → IC=+0.251 (n=782)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.409 (IC base=+0.245)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.254` → IC=+0.249 (n=2120)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.254 (IC base=+0.245)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1882` → IC=-0.274 (n=326)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1882
  - _Potencial_: sin este filtro IC_bueno=-0.178 (n=980)

- **FILTRO** `sigma_h` > `0.0105` → IC=-0.238 (n=444)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0105
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=862)

- **FILTRO** `drift_60min` |x|> `0.1726` → IC=-0.271 (n=444)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1726
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=862)

- **FILTRO** `drift_15min` |x|> `0.9226` → IC=-0.293 (n=326)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.9226
  - _Potencial_: sin este filtro IC_bueno=-0.172 (n=980)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1478` → IC=+0.188 (n=46)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.94€ cuando `delta_ratio_macro` |x|> 0.1478 (IC base=-0.203)

- **PATRÓN** `ibs_15` > `0.9231` → IC=+0.380 (n=23)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9231 (IC base=-0.203)

- **PATRÓN** `dist_vwap_pct` < `0.1327` → IC=+0.167 (n=55)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.1327 (IC base=-0.203)

- **PATRÓN** `ibs_15` < `0.38` → IC=+0.299 (n=884)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.38 (IC base=-0.027)

- **PATRÓN** `dist_vwap_pct` > `0.7023` → IC=+0.243 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7023 (IC base=-0.027)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1176` → IC=-0.262 (n=793)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1176
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=795)

- **FILTRO** `sigma_h` > `0.0155` → IC=-0.248 (n=1063)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0155
  - _Potencial_: sin este filtro IC_bueno=-0.162 (n=525)

- **FILTRO** `drift_15min` |x|> `1.2727` → IC=-0.279 (n=396)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.2727
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=1192)

- **FILTRO** `libro_spread` > `0.04` → IC=-0.273 (n=20)

  - _Acción_: SKIP cuando `libro_spread` > 0.04
  - _Potencial_: sin este filtro IC_bueno=-0.219 (n=1568)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.220)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.220)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1675` → IC=+0.283 (n=560)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1675 (IC base=-0.012)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1185` → IC=+0.298 (n=538)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1185 (IC base=-0.012)

- **PATRÓN** `ibs_15` < `0.3273` → IC=+0.296 (n=1235)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3273 (IC base=-0.012)

- **PATRÓN** `dist_vwap_pct` > `0.7632` → IC=+0.336 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7632 (IC base=-0.012)

### UPDOWN_GBM_ETH_15M_HORA7
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.143 (n=54)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.0065 (IC base=+0.103)

- **PATRÓN** `drift_60min` |x|≤ `0.1891` → IC=+0.125 (n=54)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.62€ cuando `drift_60min` |x|≤ 0.1891 (IC base=+0.103)

- **PATRÓN** `drift_15min` |x|≤ `0.7315` → IC=+0.161 (n=54)

  - _Acción_: Kelly boost +0.80€ cuando `drift_15min` |x|≤ 0.7315 (IC base=+0.103)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2386` → IC=+0.194 (n=34)

  - _Acción_: Kelly boost +0.97€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2386 (IC base=+0.103)

- **PATRÓN** `ibs_15` > `0.8407` → IC=+0.315 (n=25)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8407 (IC base=+0.103)

- **PATRÓN** `dist_vwap_pct` > `0.4542` → IC=+0.132 (n=17)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` > 0.4542 (IC base=+0.103)

- **PATRÓN** `dist_vwap_pct` < `0.1207` → IC=+0.194 (n=34)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` < 0.1207 (IC base=+0.103)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.154 (n=24)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 49.0 (IC base=+0.103)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.143 (n=54)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.0065 (IC base=+0.103)

- **PATRÓN** `drift_60min` |x|≤ `0.1891` → IC=+0.125 (n=54)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.62€ cuando `drift_60min` |x|≤ 0.1891 (IC base=+0.103)

- **PATRÓN** `drift_15min` |x|≤ `0.7315` → IC=+0.161 (n=54)

  - _Acción_: Kelly boost +0.80€ cuando `drift_15min` |x|≤ 0.7315 (IC base=+0.103)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2386` → IC=+0.194 (n=34)

  - _Acción_: Kelly boost +0.97€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2386 (IC base=+0.103)

- **PATRÓN** `ibs_15` > `0.8407` → IC=+0.315 (n=25)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8407 (IC base=+0.103)

- **PATRÓN** `dist_vwap_pct` > `0.4542` → IC=+0.132 (n=17)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` > 0.4542 (IC base=+0.103)

- **PATRÓN** `dist_vwap_pct` < `0.1207` → IC=+0.194 (n=34)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` < 0.1207 (IC base=+0.103)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.154 (n=24)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 49.0 (IC base=+0.103)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.298 (n=464)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0033 (IC base=+0.282)

- **PATRÓN** `sigma_h` > `0.0064` → IC=+0.283 (n=464)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0064 (IC base=+0.282)

- **PATRÓN** `drift_60min` |x|≤ `0.0712` → IC=+0.309 (n=612)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0712 (IC base=+0.282)

- **PATRÓN** `delta_ratio_macro` |x|> `0.152` → IC=+0.284 (n=927)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.152 (IC base=+0.282)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2216` → IC=+0.290 (n=850)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2216 (IC base=+0.282)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.295 (n=1444)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.282)

- **PATRÓN** `ibs_15` > `0.8379` → IC=+0.310 (n=1391)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8379 (IC base=+0.282)

- **PATRÓN** `dist_vwap_pct` > `0.2659` → IC=+0.311 (n=596)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2659 (IC base=+0.282)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.932` → IC=+0.386 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.932 (IC base=+0.282)

- **PATRÓN** `libro_liquidez` > `13139.6259` → IC=+0.300 (n=464)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13139.6259 (IC base=+0.282)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.304 (n=324)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.275)

- **PATRÓN** `drift_60min` |x|≤ `0.0763` → IC=+0.304 (n=324)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0763 (IC base=+0.275)

- **PATRÓN** `drift_15min` |x|≤ `0.3845` → IC=+0.275 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3845 (IC base=+0.275)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2694` → IC=+0.282 (n=246)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2694 (IC base=+0.275)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2304` → IC=+0.281 (n=442)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2304 (IC base=+0.275)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.293 (n=773)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.275)

- **PATRÓN** `ibs_15` > `0.9195` → IC=+0.325 (n=490)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9195 (IC base=+0.275)

- **PATRÓN** `dist_vwap_pct` > `0.2534` → IC=+0.314 (n=309)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2534 (IC base=+0.275)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.742` → IC=+0.390 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.742 (IC base=+0.275)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.277 (n=951)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.275)

- **PATRÓN** `libro_liquidez` > `15745.2501` → IC=+0.314 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15745.2501 (IC base=+0.275)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.293 (n=656)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0069 (IC base=+0.289)

- **PATRÓN** `sigma_h` > `0.0053` → IC=+0.290 (n=437)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0053 (IC base=+0.289)

- **PATRÓN** `drift_60min` |x|≤ `0.1093` → IC=+0.309 (n=438)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1093 (IC base=+0.289)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0654` → IC=+0.290 (n=656)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0654 (IC base=+0.289)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1008` → IC=+0.312 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1008 (IC base=+0.289)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.299 (n=630)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.289)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.290 (n=465)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.289)

- **PATRÓN** `ibs_15` > `0.8466` → IC=+0.318 (n=656)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8466 (IC base=+0.289)

- **PATRÓN** `dist_vwap_pct` > `0.2787` → IC=+0.318 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2787 (IC base=+0.289)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.243` → IC=+0.374 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.243 (IC base=+0.289)

### UPDOWN_OU_5M
- **FILTRO** `delta_ratio_macro` |x|≤ `0.126` → IC=-0.156 (n=94)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.126
  - _Potencial_: sin este filtro IC_bueno=-0.099 (n=285)

- **FILTRO** `ballena_activa_n` > `32.0` → IC=-0.130 (n=260)

  - _Acción_: SKIP cuando `ballena_activa_n` > 32.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=87)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.1228` → IC=-0.212 (n=123)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1228
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=371)

- **FILTRO** `sigma_h` > `0.007` → IC=-0.180 (n=123)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.007
  - _Potencial_: sin este filtro IC_bueno=-0.090 (n=371)

### UPDOWN_OU_5M#BNB#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1682` → IC=-0.191 (n=40)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1682
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=41)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.160 (n=48)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=54)

### UPDOWN_OU_5M#BTC#5min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1387` → IC=-0.143 (n=54)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1387
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=165)

- **FILTRO** `sigma_h` < `0.0059` → IC=-0.167 (n=43)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0059
  - _Potencial_: sin este filtro IC_bueno=-0.147 (n=15)

- **FILTRO** `ballena_activa_n` > `595.0` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `ballena_activa_n` > 595.0
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=34)

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
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1177` → IC=-0.167 (n=16)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1177
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=48)

- **FILTRO** `sigma_h` < `0.0054` → IC=-0.321 (n=26)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0054
  - _Potencial_: sin este filtro IC_bueno=-0.318 (n=9)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `sigma_h` < `0.0111` → IC=-0.151 (n=41)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0111
  - _Potencial_: sin este filtro IC_bueno=-0.125 (n=14)

- **FILTRO** `ballena_activa_n` > `42.0` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `ballena_activa_n` > 42.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=34)

- **FILTRO** `sigma_h` < `0.0057` → IC=-0.210 (n=29)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0057
  - _Potencial_: sin este filtro IC_bueno=-0.156 (n=30)

- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.0863` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.0863
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=10)

### WEEKLY_PRICE
- **PATRÓN** `ratio` < `0.9699` → IC=+0.353 (n=400)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9699 (IC base=+0.151)

- **PATRÓN** `T_h` > `117.6267` → IC=+0.356 (n=2953)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 117.6267 (IC base=+0.338)

- **PATRÓN** `ratio` > `1.02` → IC=+0.390 (n=518)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.02 (IC base=+0.338)

### WEEKLY_PRICE#BTC
- **PATRÓN** `ratio` < `0.9932` → IC=+0.228 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9932 (IC base=+0.108)

- **PATRÓN** `T_h` > `111.9558` → IC=+0.322 (n=1065)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9558 (IC base=+0.304)

- **PATRÓN** `ratio` > `1.0175` → IC=+0.372 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0175 (IC base=+0.304)

### WEEKLY_PRICE#ETH
- **PATRÓN** `ratio` < `0.9841` → IC=+0.381 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9841 (IC base=+0.199)

- **PATRÓN** `T_h` > `111.9965` → IC=+0.357 (n=1074)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9965 (IC base=+0.326)

- **PATRÓN** `ratio` > `1.0288` → IC=+0.407 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0288 (IC base=+0.326)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.0624` → IC=+0.417 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.0624 (IC base=+0.397)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5714 sube el IC de +0.138 a +0.219 en UPDOWN_GBM#15min (n=5069). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7077 sube el IC de +0.202 a +0.272 en UPDOWN_GBM#BTC#15min (n=819). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.4915 sube el IC de +0.133 a +0.220 en UPDOWN_GBM#ETH#15min (n=1021). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5333 sube el IC de +0.151 a +0.222 en UPDOWN_GBM#XRP#15min (n=1286). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1139 sube el IC de +0.069 a +0.151 en UPDOWN_GBM#XRP#15min (n=1100). Ya aplicado como kelly_boost=+0.75€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6307 sube el IC de -0.085 a +0.275 en UPDOWN_GBM_15M_TARDIO (n=1255). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3704 sube el IC de -0.001 a +0.286 en UPDOWN_GBM_15M_TARDIO (n=5170). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7639 sube el IC de +0.067 a +0.314 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=444). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.6255 sube el IC de -0.184 a +0.289 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=74). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.5684 sube el IC de +0.146 a +0.239 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=627). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3851 sube el IC de +0.245 a +0.274 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=2023). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.9231 sube el IC de -0.203 a +0.380 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=23). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.38 sube el IC de -0.027 a +0.299 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=884). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.220 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3273 sube el IC de -0.012 a +0.296 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=1235). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_YES, IBS > 0.8407 sube el IC de +0.103 a +0.315 en UPDOWN_GBM_ETH_15M_HORA7 (n=25). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_YES, IBS > 0.8407 sube el IC de +0.103 a +0.315 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=25). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8379 sube el IC de +0.282 a +0.310 en UPDOWN_GBM_IBS_ALTO (n=1391). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.9195 sube el IC de +0.275 a +0.325 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=490). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8466 sube el IC de +0.289 a +0.318 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=656). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7903 sube el IC de +0.364 a +0.394 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=762). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8078 sube el IC de +0.362 a +0.384 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=369). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.764 sube el IC de +0.365 a +0.394 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=393). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 2199 | +0.082 | +219.39€ | 1 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 2199 | +0.082 | +219.39€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1789 | +0.082 | +180.85€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1789 | +0.082 | +180.85€ | 1 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 285 | +0.068 | +10.79€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 285 | +0.068 | +10.79€ | 5 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 94 | +0.125 | +28.08€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 94 | +0.125 | +28.08€ | 1 | 9 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 1181 | -0.015 | +81.12€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 1181 | -0.015 | +81.12€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE | 7 | +0.019 | +3.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE#15min | 7 | +0.019 | +3.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 897 | -0.033 | +59.12€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 897 | -0.033 | +59.12€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 192 | +0.067 | +25.24€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 192 | +0.067 | +25.24€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 85 | -0.017 | -6.49€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 85 | -0.017 | -6.49€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 48522 | -0.084 | -6251.00€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 3057 | +0.079 | -306.75€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 45465 | -0.095 | -5944.24€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4871 | -0.111 | -816.69€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4871 | -0.111 | -816.69€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 3057 | +0.079 | -306.75€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 3057 | +0.079 | -306.75€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 4932 | -0.103 | -939.80€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 4932 | -0.103 | -939.80€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 13299 | -0.042 | -1287.87€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 13299 | -0.042 | -1287.87€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 13222 | -0.112 | -1377.66€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 13222 | -0.112 | -1377.66€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 9141 | -0.135 | -1522.23€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 9141 | -0.135 | -1522.23€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 51149 | -0.012 | +2815.03€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 13205 | +0.004 | +1495.79€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 37944 | -0.018 | +1319.24€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 51149 | -0.012 | +2815.03€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 13205 | +0.004 | +1495.79€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 37944 | -0.018 | +1319.24€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 194491 | +0.113 | -8091.70€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#15min | 22183 | +0.180 | -698.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 894 | +0.015 | -72.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 160333 | +0.105 | -6913.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 11081 | +0.094 | -407.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 26570 | +0.103 | -1884.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 79 | -0.179 | +10.89€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 26476 | +0.104 | -1883.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 36724 | +0.124 | -625.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5625 | +0.178 | -235.00€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 26540 | +0.120 | -200.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 4517 | +0.080 | -166.85€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 26619 | +0.098 | -1936.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 90 | -0.109 | +14.44€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 26514 | +0.099 | -1939.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 41562 | +0.123 | -859.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 10421 | +0.179 | -250.26€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 26963 | +0.105 | -537.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 4166 | +0.103 | -63.61€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#SOL | 36416 | +0.111 | -1641.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 5876 | +0.198 | -253.99€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 797 | +0.041 | -18.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 27345 | +0.095 | -1192.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 2398 | +0.104 | -176.73€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO#XRP | 26600 | +0.107 | -1144.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 92 | -0.117 | +15.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 26495 | +0.108 | -1160.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 31547 | +0.191 | -2263.09€ | 2 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 31547 | +0.191 | -2263.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 7145 | +0.166 | -771.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 7145 | +0.166 | -771.18€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 4610 | +0.195 | -185.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 4610 | +0.195 | -185.93€ | 3 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 7003 | +0.173 | -634.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 7003 | +0.173 | -634.43€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 5838 | +0.251 | -201.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 5838 | +0.251 | -201.88€ | 0 | 4 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 6872 | +0.184 | -483.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 6872 | +0.184 | -483.42€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 1268 | +0.426 | -45.64€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 1268 | +0.426 | -45.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 526 | +0.439 | -4.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 526 | +0.439 | -4.44€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE#15min | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 515 | +0.425 | -18.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 515 | +0.425 | -18.96€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 213 | +0.398 | -18.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 213 | +0.398 | -18.37€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 111601 | +0.199 | -8322.60€ | 3 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 111601 | +0.199 | -8322.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 19316 | +0.177 | -2252.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 19316 | +0.177 | -2252.38€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 17996 | +0.223 | -620.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 17996 | +0.223 | -620.52€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 19159 | +0.180 | -2044.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 19159 | +0.180 | -2044.31€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 18143 | +0.217 | -733.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 18143 | +0.217 | -733.02€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 18418 | +0.203 | -1159.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 18418 | +0.203 | -1159.40€ | 1 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 18569 | +0.195 | -1512.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 18569 | +0.195 | -1512.96€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 43182 | +0.117 | +372.08€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 43182 | +0.117 | +372.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 21500 | +0.117 | +212.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 21500 | +0.117 | +212.61€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 21682 | +0.117 | +159.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 21682 | +0.117 | +159.47€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 2647 | +0.292 | -21.77€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 2647 | +0.292 | -21.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 1207 | +0.281 | -31.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 1207 | +0.281 | -31.84€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 1298 | +0.295 | +3.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 1298 | +0.295 | +3.35€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 142 | +0.347 | +6.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 142 | +0.347 | +6.73€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 1219 | +0.437 | -8.24€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 1219 | +0.437 | -8.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 582 | +0.433 | -9.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 582 | +0.433 | -9.62€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 585 | +0.440 | -0.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 585 | +0.440 | -0.03€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 52 | +0.407 | +1.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 52 | +0.407 | +1.41€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1968 | +0.067 | -91.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 725 | +0.046 | -64.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 1243 | +0.078 | -26.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1534 | +0.074 | -45.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 291 | +0.053 | -19.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 1243 | +0.078 | -26.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 87694 | +0.101 | -2027.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 7084 | +0.097 | +166.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 80610 | +0.101 | -2194.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 47914 | +0.105 | -448.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 7084 | +0.097 | +166.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 40830 | +0.107 | -615.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 18707 | +0.109 | -82.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 18707 | +0.109 | -82.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 21073 | +0.081 | -1496.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 21073 | +0.081 | -1496.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 914 | +0.186 | -109.27€ | 5 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 914 | +0.186 | -109.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 914 | +0.186 | -109.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 914 | +0.186 | -109.27€ | 5 | 4 |
| ✅ GBM_LATE_15M | 59557 | +0.101 | +33416.92€ | 0 | 18 |
| ✅ GBM_LATE_15M#15min | 59557 | +0.101 | +33416.92€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 9859 | +0.226 | +8510.72€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 9859 | +0.226 | +8510.72€ | 0 | 22 |
| ✅ GBM_LATE_15M#BTC | 9181 | +0.177 | +7285.49€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 9181 | +0.177 | +7285.49€ | 0 | 21 |
| ✅ GBM_LATE_15M#DOGE | 10672 | +0.207 | +8453.67€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 10672 | +0.207 | +8453.67€ | 0 | 20 |
| ✅ GBM_LATE_15M#ETH | 7953 | +0.058 | +2612.79€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 7953 | +0.058 | +2612.79€ | 1 | 15 |
| ✅ GBM_LATE_15M#SOL | 8300 | -0.027 | +2191.15€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 8300 | -0.027 | +2191.15€ | 4 | 15 |
| ✅ GBM_LATE_15M#XRP | 13592 | -0.021 | +4363.09€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 13592 | -0.021 | +4363.09€ | 3 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 62961 | +0.086 | +36691.86€ | 0 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 62961 | +0.086 | +36691.86€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 12175 | -0.002 | +6496.47€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 12175 | -0.002 | +6496.47€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 13550 | +0.005 | +3650.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 13550 | +0.005 | +3650.77€ | 0 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 8535 | +0.295 | +9778.10€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 8535 | +0.295 | +9778.10€ | 0 | 22 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 12004 | +0.015 | +3775.23€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 12004 | +0.015 | +3775.23€ | 1 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 9640 | +0.045 | +4336.82€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 9640 | +0.045 | +4336.82€ | 3 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 7057 | +0.316 | +8654.48€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 7057 | +0.316 | +8654.48€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 47003 | +0.179 | +39002.47€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 47003 | +0.179 | +39002.47€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 7078 | +0.240 | +6600.46€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 7078 | +0.240 | +6600.46€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 7458 | +0.140 | +5559.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 7458 | +0.140 | +5559.76€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 7562 | +0.225 | +6578.02€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 7562 | +0.225 | +6578.02€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 8059 | +0.130 | +6244.13€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 8059 | +0.130 | +6244.13€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 8885 | +0.121 | +6754.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 8885 | +0.121 | +6754.83€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 7961 | +0.234 | +7265.26€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 7961 | +0.234 | +7265.26€ | 0 | 25 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 12892 | +0.126 | +6514.34€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 12892 | +0.126 | +6514.34€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 669 | +0.162 | +439.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 669 | +0.162 | +439.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 3455 | +0.126 | +1878.00€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 3455 | +0.126 | +1878.00€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 507 | +0.158 | +290.79€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 507 | +0.158 | +290.79€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 3707 | +0.124 | +1803.49€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 3707 | +0.124 | +1803.49€ | 0 | 16 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 3339 | +0.099 | +1333.56€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 3339 | +0.099 | +1333.56€ | 0 | 12 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 1215 | +0.169 | +768.67€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 1215 | +0.169 | +768.67€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO | 59752 | +0.189 | +49482.14€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#15min | 59752 | +0.189 | +49482.14€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 9427 | +0.250 | +9122.55€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 9427 | +0.250 | +9122.55€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 9539 | +0.140 | +6714.97€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 9539 | +0.140 | +6714.97€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 10142 | +0.235 | +9189.10€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 10142 | +0.235 | +9189.10€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 9894 | +0.143 | +7376.51€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 9894 | +0.143 | +7376.51€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 10581 | +0.125 | +7569.25€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 10581 | +0.125 | +7569.25€ | 0 | 18 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 10169 | +0.242 | +9509.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 10169 | +0.242 | +9509.76€ | 0 | 20 |
| ✅ GBM_LATE_5M | 15265 | +0.215 | +12639.34€ | 0 | 26 |
| ✅ GBM_LATE_5M#5min | 15265 | +0.215 | +12639.34€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 1525 | +0.247 | +1447.13€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 1525 | +0.247 | +1447.13€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 3286 | +0.211 | +2831.05€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 3286 | +0.211 | +2831.05€ | 0 | 25 |
| ✅ GBM_LATE_5M#DOGE | 1453 | +0.210 | +1160.11€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1453 | +0.210 | +1160.11€ | 0 | 19 |
| ✅ GBM_LATE_5M#ETH | 4348 | +0.205 | +3290.79€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 4348 | +0.205 | +3290.79€ | 0 | 26 |
| ✅ GBM_LATE_5M#SOL | 2637 | +0.224 | +2320.83€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 2637 | +0.224 | +2320.83€ | 0 | 23 |
| ✅ GBM_LATE_5M#XRP | 2016 | +0.209 | +1589.43€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 2016 | +0.209 | +1589.43€ | 0 | 0 |
| ✅ GBM_LATE_60M | 5344 | +0.054 | +1448.61€ | 0 | 6 |
| ✅ GBM_LATE_60M#60min | 5344 | +0.054 | +1448.61€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 1847 | +0.058 | +547.32€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 1847 | +0.058 | +547.32€ | 0 | 6 |
| ✅ GBM_LATE_60M#ETH | 1705 | +0.054 | +546.32€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 1705 | +0.054 | +546.32€ | 1 | 5 |
| ✅ GBM_LATE_60M#SOL | 1792 | +0.050 | +354.97€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 1792 | +0.050 | +354.97€ | 0 | 9 |
| 🚫 GBM_LATE_60M_FADE | 724 | -0.249 | -35.03€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 724 | -0.249 | -35.03€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 261 | -0.253 | -19.53€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 261 | -0.253 | -19.53€ | 5 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 262 | -0.242 | -6.68€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 262 | -0.242 | -6.68€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 201 | -0.249 | -8.83€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 201 | -0.249 | -8.83€ | 7 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 2196 | +0.084 | +552.87€ | 0 | 9 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 2196 | +0.084 | +552.87€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 848 | +0.071 | +191.94€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 848 | +0.071 | +191.94€ | 1 | 5 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 758 | +0.057 | +151.57€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 758 | +0.057 | +151.57€ | 2 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 590 | +0.137 | +209.37€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 590 | +0.137 | +209.37€ | 2 | 10 |
| ✅ LATE_WINDOW_5MIN | 285 | +0.298 | +326.07€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 285 | +0.298 | +326.07€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 285 | +0.298 | +326.07€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 285 | +0.298 | +326.07€ | 1 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 4459 | +0.096 | +1004.62€ | 0 | 1 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 4459 | +0.096 | +1004.62€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 4459 | +0.096 | +1004.62€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 4459 | +0.096 | +1004.62€ | 0 | 1 |
| ✅ LIQUIDACIONES_15M | 1356 | +0.010 | +56.90€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 1356 | +0.010 | +56.90€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 130 | +0.076 | +22.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 130 | +0.076 | +22.46€ | 0 | 3 |
| ✅ LIQUIDACIONES_15M#BTC | 289 | +0.002 | +10.97€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 289 | +0.002 | +10.97€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 79 | -0.031 | -0.05€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 79 | -0.031 | -0.05€ | 1 | 1 |
| ✅ LIQUIDACIONES_15M#ETH | 329 | +0.023 | +20.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 329 | +0.023 | +20.16€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 330 | -0.009 | +3.61€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 330 | -0.009 | +3.61€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 199 | +0.007 | -0.24€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 199 | +0.007 | -0.24€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 4310 | +0.017 | +151.57€ | 5 | 1 |
| ✅ LIQUIDACIONES_5M#5min | 4310 | +0.017 | +151.57€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 239 | +0.006 | -5.14€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 239 | +0.006 | -5.14€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 827 | +0.015 | +40.58€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 827 | +0.015 | +40.58€ | 2 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 280 | +0.053 | +58.67€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 280 | +0.053 | +58.67€ | 0 | 6 |
| ✅ LIQUIDACIONES_5M#ETH | 1668 | +0.019 | +28.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1668 | +0.019 | +28.11€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 775 | +0.012 | +3.41€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 775 | +0.012 | +3.41€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 521 | +0.003 | +25.94€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 521 | +0.003 | +25.94€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 2495 | -0.033 | -5.63€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 2495 | -0.033 | -5.63€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 758 | -0.030 | -10.89€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 758 | -0.030 | -10.89€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 891 | -0.011 | +19.30€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 891 | -0.011 | +19.30€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 846 | -0.058 | -14.03€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 846 | -0.058 | -14.03€ | 5 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 17211 | -0.033 | -216.51€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 8291 | -0.035 | -123.43€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 8920 | -0.031 | -93.08€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 613 | -0.058 | -40.55€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 314 | -0.038 | -5.91€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 299 | -0.078 | -34.64€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 4516 | -0.029 | -48.33€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 2149 | -0.025 | -0.96€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 2367 | -0.032 | -47.37€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 1650 | -0.032 | +2.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 839 | -0.041 | -18.08€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 811 | -0.021 | +20.68€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 3899 | -0.034 | -69.85€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 1862 | -0.033 | -25.86€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 2037 | -0.035 | -43.99€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 3307 | -0.023 | +43.69€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 1601 | -0.030 | -3.64€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 1706 | -0.016 | +47.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 3226 | -0.044 | -104.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 1526 | -0.052 | -68.97€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 1700 | -0.038 | -35.10€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M | 14662 | -0.012 | -218.19€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 14662 | -0.012 | -218.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC | 3379 | -0.021 | -71.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 3379 | -0.021 | -71.38€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 3075 | -0.015 | -29.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 3075 | -0.015 | -29.21€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL | 3388 | -0.018 | -66.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 3388 | -0.018 | -66.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 70519 | +0.000 | +3851.33€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 70519 | +0.000 | +3851.33€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 12792 | +0.027 | +1775.92€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 12792 | +0.027 | +1775.92€ | 2 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 9817 | -0.037 | -147.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 9817 | -0.037 | -147.00€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 12932 | +0.026 | +1462.15€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 12932 | +0.026 | +1462.15€ | 1 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 9783 | -0.052 | -246.53€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 9783 | -0.052 | -246.53€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 12033 | -0.003 | +344.82€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 12033 | -0.003 | +344.82€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 13162 | +0.019 | +661.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 13162 | +0.019 | +661.97€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 7256 | -0.053 | -107.17€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 7256 | -0.053 | -107.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1267 | -0.001 | -13.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1267 | -0.001 | -13.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 2013 | -0.060 | -18.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 2013 | -0.060 | -18.75€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 93 | -0.016 | +0.13€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 93 | -0.016 | +0.13€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 811 | -0.119 | -34.68€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 811 | -0.119 | -34.68€ | 5 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 2206 | -0.068 | -13.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 2206 | -0.068 | -13.17€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 866 | -0.017 | -26.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 866 | -0.017 | -26.93€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3381 | +0.003 | +0.01€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3381 | +0.003 | +0.01€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 133 | -0.033 | -0.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 133 | -0.033 | -0.70€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 197 | +0.007 | -1.76€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 197 | +0.007 | -1.76€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 139 | -0.004 | -2.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 139 | -0.004 | -2.34€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1326 | +0.006 | +6.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1326 | +0.006 | +6.37€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1391 | +0.007 | -0.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1391 | +0.007 | -0.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 195 | -0.013 | -1.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 195 | -0.013 | -1.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 172901 | -0.077 | +2341.15€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 172901 | -0.077 | +2341.15€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 30363 | -0.077 | +1733.62€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 30363 | -0.077 | +1733.62€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 25760 | -0.101 | -1230.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 25760 | -0.101 | -1230.55€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 30782 | -0.067 | +1528.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 30782 | -0.067 | +1528.56€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 25313 | -0.099 | -848.14€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 25313 | -0.099 | -848.14€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 30866 | -0.059 | +251.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 30866 | -0.059 | +251.37€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 29817 | -0.069 | +906.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 29817 | -0.069 | +906.29€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 9128 | -0.035 | -183.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 9128 | -0.035 | -183.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 1008 | -0.017 | -19.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 1008 | -0.017 | -19.32€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 2125 | -0.046 | -27.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 2125 | -0.046 | -27.88€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2666 | -0.024 | -34.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2666 | -0.024 | -34.56€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1277 | -0.064 | -31.53€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1277 | -0.064 | -31.53€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 1043 | -0.037 | -38.11€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 1043 | -0.037 | -38.11€ | 0 | 0 |
| ✅ ORDER_FLOW_5M | 2209 | +0.121 | +889.50€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#5min | 2073 | +0.125 | +876.91€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 489 | +0.135 | +241.25€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 489 | +0.135 | +241.25€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#DOGE | 428 | +0.121 | +155.28€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 428 | +0.121 | +155.28€ | 0 | 2 |
| ✅ ORDER_FLOW_5M#ETH | 389 | +0.129 | +180.25€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 389 | +0.129 | +180.25€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 349 | +0.141 | +178.93€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 349 | +0.141 | +178.93€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#XRP | 418 | +0.098 | +121.20€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 418 | +0.098 | +121.20€ | 0 | 2 |
| ✅ ORDER_FLOW_5M_REACTIVO | 2288 | -0.017 | -15.59€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 2288 | -0.017 | -15.59€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 413 | +0.011 | +22.83€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 413 | +0.011 | +22.83€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 422 | -0.040 | -20.40€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 422 | -0.040 | -20.40€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 566 | -0.041 | -33.81€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 566 | -0.041 | -33.81€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 464 | +0.006 | +10.60€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 464 | +0.006 | +10.60€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 423 | -0.013 | +5.19€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 423 | -0.013 | +5.19€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 1204 | -0.052 | +49.46€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 557 | -0.087 | -29.48€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 436 | -0.094 | -8.94€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 121 | -0.061 | -20.55€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 420 | -0.014 | +51.21€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 305 | +0.005 | +59.22€ | 1 | 2 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 115 | -0.064 | -8.00€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 227 | -0.037 | +27.73€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 191 | -0.029 | +25.89€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 36 | -0.079 | +1.84€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 932 | -0.048 | +76.17€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 272 | -0.066 | -26.71€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE | 1522 | -0.198 | -68.41€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 598 | -0.192 | -32.30€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 528 | -0.189 | -27.85€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#reach | 70 | -0.208 | -4.45€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 509 | -0.204 | -36.81€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 447 | -0.215 | -43.96€ | 5 | 1 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 62 | -0.125 | +7.14€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 415 | -0.195 | +0.71€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 385 | -0.193 | -1.44€ | 5 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 30 | -0.219 | +2.15€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#atexpiry | 1360 | -0.199 | -73.25€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 162 | -0.183 | +4.84€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 550 | +0.373 | +507.74€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#BTC | 118 | +0.150 | +90.77€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 118 | +0.150 | +90.77€ | 0 | 6 |
| ✅ RESOLUTION_SNIPER#ETH | 125 | +0.366 | +104.29€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 125 | +0.366 | +104.29€ | 0 | 5 |
| ✅ RESOLUTION_SNIPER#SOL | 307 | +0.458 | +312.67€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 307 | +0.458 | +312.67€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#sniper | 550 | +0.373 | +507.74€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 983 | +0.037 | +78.98€ | 2 | 2 |
| ✅ STREAK_FADE_15M#15min | 983 | +0.037 | +78.98€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 359 | +0.015 | +2.34€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 359 | +0.015 | +2.34€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 75 | +0.019 | +1.57€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 75 | +0.019 | +1.57€ | 1 | 1 |
| ✅ STREAK_FADE_15M#SOL | 83 | +0.018 | +6.06€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 83 | +0.018 | +6.06€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 466 | +0.060 | +69.02€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 466 | +0.060 | +69.02€ | 2 | 4 |
| ✅ STREAK_FADE_5M | 3602 | -0.023 | -143.82€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3602 | -0.023 | -143.82€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 1127 | -0.023 | -40.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 1127 | -0.023 | -40.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 619 | -0.028 | -27.08€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 619 | -0.028 | -27.08€ | 1 | 0 |
| ✅ STREAK_FADE_5M#SOL | 173 | -0.043 | -14.79€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 173 | -0.043 | -14.79€ | 4 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1683 | -0.020 | -61.74€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1683 | -0.020 | -61.74€ | 2 | 0 |
| ✅ STREAK_FADE_60M | 123 | -0.044 | -13.49€ | 3 | 0 |
| ✅ STREAK_FADE_60M#60min | 123 | -0.044 | -13.49€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 45 | -0.074 | -4.16€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 45 | -0.074 | -4.16€ | 4 | 0 |
| ✅ STREAK_FADE_60M#SOL | 78 | -0.025 | -9.34€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 78 | -0.025 | -9.34€ | 0 | 1 |
| ✅ STREAK_MOM_5M | 11568 | +0.014 | +72.81€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 11568 | +0.014 | +72.81€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2995 | +0.018 | +24.38€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2995 | +0.018 | +24.38€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 3048 | +0.016 | +32.71€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 3048 | +0.016 | +32.71€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2934 | +0.009 | -2.53€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2934 | +0.009 | -2.53€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2591 | +0.014 | +18.26€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2591 | +0.014 | +18.26€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 12429 | +0.018 | +0.52€ | 4 | 0 |
| ✅ STRUCT_NO_15M#15min | 12429 | +0.018 | +0.52€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 5113 | +0.021 | +4.40€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 5113 | +0.021 | +4.40€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 4330 | +0.018 | -0.40€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 4330 | +0.018 | -0.40€ | 4 | 0 |
| ✅ STRUCT_NO_15M#SOL | 2986 | +0.014 | -3.47€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 2986 | +0.014 | -3.47€ | 1 | 0 |
| ✅ UPDOWN_GBM | 112537 | +0.060 | +10699.36€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 27420 | +0.079 | +5467.66€ | 0 | 9 |
| ✅ UPDOWN_GBM#240min | 3274 | -0.001 | +34.51€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 74766 | +0.062 | +5088.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 6694 | -0.003 | +117.35€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 9603 | +0.103 | +1728.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1782 | +0.163 | +818.90€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 90 | -0.011 | -2.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 7731 | +0.091 | +911.93€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 25567 | +0.058 | +2279.37€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 3681 | +0.080 | +828.22€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 942 | -0.001 | +18.80€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 17824 | +0.068 | +1353.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 2981 | -0.005 | +75.95€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 139 | -0.067 | +2.53€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 12304 | +0.076 | +1347.05€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1761 | +0.154 | +738.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 86 | +0.023 | -0.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 10457 | +0.063 | +609.48€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 26584 | +0.050 | +1883.08€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 6461 | +0.072 | +1000.66€ | 0 | 8 |
| ✅ UPDOWN_GBM#ETH#240min | 912 | +0.004 | +15.51€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 16614 | +0.052 | +825.54€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 2469 | +0.000 | +40.88€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 128 | -0.108 | +0.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 23730 | +0.040 | +1336.06€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 7430 | +0.032 | +445.61€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#240min | 847 | -0.011 | +4.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 14095 | +0.052 | +895.41€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 1244 | -0.002 | +0.52€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#daily | 114 | -0.147 | -10.16€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 14747 | +0.074 | +2126.81€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 6305 | +0.094 | +1635.83€ | 0 | 11 |
| ✅ UPDOWN_GBM#XRP#240min | 397 | +0.006 | -1.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 8045 | +0.062 | +492.60€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 381 | -0.106 | -7.15€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 1015 | +0.364 | +377.14€ | 0 | 10 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 1015 | +0.364 | +377.14€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 491 | +0.362 | +172.01€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 491 | +0.362 | +172.01€ | 0 | 10 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 524 | +0.365 | +205.13€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 524 | +0.365 | +205.13€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO | 26502 | -0.019 | +6656.57€ | 2 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 26502 | -0.019 | +6656.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1981 | -0.051 | +561.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1981 | -0.051 | +561.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 4940 | -0.115 | +284.34€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 4940 | -0.115 | +284.34€ | 2 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 1071 | +0.222 | +899.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 1071 | +0.222 | +899.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 3533 | +0.221 | +2281.45€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 3533 | +0.221 | +2281.45€ | 1 | 20 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 7546 | -0.057 | +1140.48€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 7546 | -0.057 | +1140.48€ | 4 | 5 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 7431 | -0.056 | +1489.25€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 7431 | -0.056 | +1489.25€ | 4 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 326 | +0.061 | +33.64€ | 0 | 8 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 326 | +0.061 | +33.64€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 326 | +0.061 | +33.64€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 326 | +0.061 | +33.64€ | 0 | 8 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1854 | +0.282 | +1560.33€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1854 | +0.282 | +1560.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 980 | +0.275 | +772.09€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 980 | +0.275 | +772.09€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 874 | +0.289 | +788.24€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 874 | +0.289 | +788.24€ | 0 | 10 |
| ✅ UPDOWN_OU_5M | 873 | -0.114 | -87.23€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 873 | -0.114 | -87.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 277 | -0.081 | -20.93€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 277 | -0.081 | -20.93€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 99 | -0.183 | -12.98€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 99 | -0.183 | -12.98€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 114 | -0.172 | -3.97€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 114 | -0.172 | -3.97€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 4885 | +0.299 | +2192.82€ | 0 | 3 |
| ✅ WEEKLY_PRICE#BTC | 1868 | +0.256 | +248.75€ | 0 | 3 |
| ✅ WEEKLY_PRICE#ETH | 1889 | +0.293 | +803.62€ | 0 | 3 |
| ✅ WEEKLY_PRICE#SOL | 1128 | +0.381 | +1140.45€ | 0 | 1 |