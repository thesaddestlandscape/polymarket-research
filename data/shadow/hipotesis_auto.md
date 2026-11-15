# Hipótesis automáticas — 2026-11-15 00:12 UTC
_Generado por shadow_postmortem.py sobre 1339872 resoluciones (PNL=+185628.82€)_

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
- **FILTRO** `restante_s_al_confirmar` < `131.8` → IC=-0.217 (n=12134)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 131.8
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=36404)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `125.07` → IC=-0.256 (n=1217)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 125.07
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=3654)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `115.68` → IC=-0.277 (n=1233)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 115.68
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=3699)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `restante_s_al_confirmar` < `116.26` → IC=-0.166 (n=3326)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 116.26
  - _Potencial_: sin este filtro IC_bueno=-0.000 (n=9979)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `151.93` → IC=-0.238 (n=3306)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 151.93
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=9920)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `128.13` → IC=-0.267 (n=2286)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 128.13
  - _Potencial_: sin este filtro IC_bueno=-0.091 (n=6860)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.209 (n=28558)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.103)

- **PATRÓN** `libro_liquidez` > `8197.8863` → IC=+0.156 (n=2360)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 8197.8863 (IC base=+0.103)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.128 (n=24809)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.131 (n=29959)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.125)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.225 (n=22566)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.140 (n=8448)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `6444.3224` → IC=+0.142 (n=3276)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 6444.3224 (IC base=+0.125)

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
- **PATRÓN** `py_entrada` > `0.61` → IC=+0.168 (n=624)

  - _Acción_: Kelly boost +0.84€ cuando `py_entrada` > 0.61 (IC base=+0.075)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.148 (n=1465)

  - _Acción_: Kelly boost +0.74€ cuando `py_entrada` < 0.44 (IC base=+0.085)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.170 (n=5178)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 6.0 (IC base=+0.167)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.172 (n=4595)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 15.0 (IC base=+0.167)

- **PATRÓN** `py_entrada` > `0.77` → IC=+0.375 (n=1799)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.77 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.208 (n=2473)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.201)

- **PATRÓN** `py_entrada` < `0.275` → IC=+0.332 (n=958)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.275 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.204 (n=2877)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.201)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.142 (n=663)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 15.0 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.143 (n=1189)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 15.0 (IC base=+0.139)

- **PATRÓN** `py_entrada` > `0.675` → IC=+0.255 (n=455)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.675 (IC base=+0.139)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.142 (n=1132)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.156 (n=155)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.075)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.249 (n=964)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.227)

- **PATRÓN** `py_entrada` > `0.83` → IC=+0.420 (n=1342)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.83 (IC base=+0.227)

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

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.143 (n=496)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 17.0 (IC base=+0.123)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.252 (n=450)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.123)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.755` → IC=-0.299 (n=152)

  - _Acción_: SKIP cuando `py_entrada` > 0.755
  - _Potencial_: sin este filtro IC_bueno=-0.171 (n=77)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.200 (n=23506)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.194)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.196 (n=20883)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 15.0 (IC base=+0.194)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.228 (n=7839)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.194)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.338 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.194)

- **PATRÓN** `libro_liquidez` > `4915.142` → IC=+0.338 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4915.142 (IC base=+0.194)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.172 (n=5657)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 5.0 (IC base=+0.167)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.167 (n=5622)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 18.0 (IC base=+0.167)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.177 (n=5598)

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

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.211 (n=3397)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.207)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.210 (n=2425)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.207)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.247 (n=1667)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.207)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.181 (n=5531)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 5.0 (IC base=+0.174)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.176 (n=4676)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 15.0 (IC base=+0.174)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.175 (n=5668)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` < 0.73 (IC base=+0.174)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.182 (n=4335)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` > 0.71 (IC base=+0.174)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.257 (n=4387)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.252)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.253 (n=3901)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.252)

- **PATRÓN** `py_entrada` > `0.8` → IC=+0.364 (n=1485)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.8 (IC base=+0.252)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.306 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.252)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.189 (n=5414)
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

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.209 (n=27976)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.239 (n=32527)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.199)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.186 (n=4873)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 18.0 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.178 (n=10360)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 12.0 (IC base=+0.177)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.206 (n=6920)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.177)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.225 (n=13578)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.223)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.285 (n=4531)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.223)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.193 (n=4796)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 18.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.197 (n=11508)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` > 0.72 (IC base=+0.180)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.855` → IC=-0.357 (n=19)

  - _Acción_: SKIP cuando `py_entrada` < 0.855
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.228 (n=4562)
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

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.214 (n=4617)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.204)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.256 (n=4694)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.204)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.203 (n=4653)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.195)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.197 (n=5360)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 6.0 (IC base=+0.195)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.244 (n=5559)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.195)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.194 (n=11687)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.141 (n=12401)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `3.42` → IC=+0.139 (n=14287)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 3.42 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.193 (n=5702)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.144 (n=5609)

  - _Acción_: Kelly boost +0.72€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.124 (n=7148)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 7.0 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `4.06` → IC=+0.141 (n=7104)

  - _Acción_: Kelly boost +0.71€ cuando `lag_apertura_s` < 4.06 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.195 (n=5985)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.138 (n=7531)

  - _Acción_: Kelly boost +0.69€ cuando `restante_min` > 4.95 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `3.1` → IC=+0.138 (n=7164)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 3.1 (IC base=+0.117)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.305 (n=1422)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.292)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.387 (n=731)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.292)

- **PATRÓN** `libro_liquidez` > `3979.7019` → IC=+0.292 (n=901)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3979.7019 (IC base=+0.292)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.285 (n=955)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.281)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.367 (n=314)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.281)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.315 (n=694)
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
- **PATRÓN** `drift_60min` |x|≤ `0.4869` → IC=+0.139 (n=18414)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.4869 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.128 (n=18647)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 6.0 (IC base=+0.123)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.125 (n=12799)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 12.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` > `0.9764` → IC=+0.246 (n=6138)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9764 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` > `0.8079` → IC=+0.282 (n=975)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8079 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.479` → IC=+0.188 (n=9224)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 3.479 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` > `0.6953` → IC=+0.268 (n=4965)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6953 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` > `0.3043` → IC=+0.250 (n=1896)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3043 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` > `2.7493` → IC=+0.234 (n=4426)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7493 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.137 (n=9066)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `4693.9553` → IC=+0.149 (n=6138)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 4693.9553 (IC base=+0.123)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.123 (n=11588)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0063 (IC base=+0.086)

- **PATRÓN** `ibs_20min` < `0.5639` → IC=+0.145 (n=23127)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.5639 (IC base=+0.086)

- **PATRÓN** `dist_vwap_pct` > `0.6341` → IC=+0.191 (n=1479)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.6341 (IC base=+0.086)

- **PATRÓN** `volumen_regimen` < `0.8588` → IC=+0.194 (n=6347)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` < 0.8588 (IC base=+0.086)

- **PATRÓN** `volumen_pendiente_norm` > `0.296` → IC=+0.236 (n=2330)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.296 (IC base=+0.086)

- **PATRÓN** `volumen_spike_ratio` > `2.6669` → IC=+0.215 (n=5382)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6669 (IC base=+0.086)

- **PATRÓN** `ballena_activa_n` < `99.0` → IC=+0.230 (n=16058)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 99.0 (IC base=+0.086)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `drift_60min` |x|≤ `0.3724` → IC=+0.212 (n=3916)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3724 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.227 (n=1905)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `0.9849` → IC=+0.277 (n=1775)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9849 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.8` → IC=+0.293 (n=923)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.8 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.2344` → IC=+0.254 (n=690)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2344 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `1.4388` → IC=+0.211 (n=3755)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4388 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.222 (n=4350)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `2029.23` → IC=+0.210 (n=1305)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2029.23 (IC base=+0.210)

- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.221 (n=3567)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 25.0 (IC base=+0.210)

- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.251 (n=1581)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0094 (IC base=+0.243)

- **PATRÓN** `drift_60min` |x|≤ `0.0915` → IC=+0.276 (n=1162)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0915 (IC base=+0.243)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.244 (n=3631)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.243)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.251 (n=1595)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.243)

- **PATRÓN** `ibs_20min` < `0.5667` → IC=+0.260 (n=3485)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5667 (IC base=+0.243)

- **PATRÓN** `volumen_pendiente_norm` < `0.0717` → IC=+0.246 (n=2998)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0717 (IC base=+0.243)

- **PATRÓN** `volumen_pendiente_norm` > `0.2909` → IC=+0.253 (n=468)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2909 (IC base=+0.243)

- **PATRÓN** `volumen_spike_ratio` < `1.4485` → IC=+0.245 (n=1110)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4485 (IC base=+0.243)

- **PATRÓN** `volumen_spike_ratio` > `2.6533` → IC=+0.250 (n=1110)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6533 (IC base=+0.243)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.245 (n=4037)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.243)

- **PATRÓN** `libro_liquidez` > `1777.0488` → IC=+0.249 (n=2322)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1777.0488 (IC base=+0.243)

- **PATRÓN** `ballena_activa_n` < `6.0` → IC=+0.245 (n=1201)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 6.0 (IC base=+0.243)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.237 (n=1107)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.224)

- **PATRÓN** `drift_60min` |x|≤ `0.1114` → IC=+0.250 (n=1458)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1114 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.236 (n=3475)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.225 (n=2354)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` > `0.8988` → IC=+0.257 (n=1104)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8988 (IC base=+0.224)

- **PATRÓN** `dist_vwap_pct` > `0.1873` → IC=+0.234 (n=1444)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1873 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.824` → IC=+0.263 (n=484)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.824 (IC base=+0.224)

- **PATRÓN** `volumen_regimen` > `0.6976` → IC=+0.231 (n=2959)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6976 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` > `0.2785` → IC=+0.269 (n=457)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2785 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` > `2.4471` → IC=+0.249 (n=1090)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4471 (IC base=+0.224)

- **PATRÓN** `libro_liquidez` > `15907.6891` → IC=+0.224 (n=1104)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15907.6891 (IC base=+0.224)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.154 (n=3580)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0066 (IC base=+0.134)

- **PATRÓN** `drift_60min` |x|≤ `0.079` → IC=+0.159 (n=1194)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.079 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.155 (n=1348)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 17.0 (IC base=+0.134)

- **PATRÓN** `ibs_20min` < `0.7058` → IC=+0.172 (n=3579)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.7058 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.991` → IC=+0.141 (n=3271)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 3.991 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` < `0.6283` → IC=+0.154 (n=1193)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.6283 (IC base=+0.134)

- **PATRÓN** `volumen_pendiente_norm` > `0.0723` → IC=+0.156 (n=1458)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` > 0.0723 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` < `2.442` → IC=+0.143 (n=3451)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.442 (IC base=+0.134)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.134 (n=4650)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.134)

- **PATRÓN** `ballena_activa_n` < `173.0` → IC=+0.192 (n=1135)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 173.0 (IC base=+0.134)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0128` → IC=+0.210 (n=1386)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0128 (IC base=+0.194)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.202 (n=4369)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.194)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.258 (n=1612)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.194)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.975` → IC=+0.282 (n=916)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.975 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` < `0.0974` → IC=+0.196 (n=3725)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` < 0.0974 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` > `0.3517` → IC=+0.224 (n=537)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3517 (IC base=+0.194)

- **PATRÓN** `volumen_spike_ratio` > `2.7279` → IC=+0.211 (n=1840)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7279 (IC base=+0.194)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.198 (n=5031)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.04 (IC base=+0.194)

- **PATRÓN** `libro_liquidez` > `2005.4352` → IC=+0.203 (n=1385)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2005.4352 (IC base=+0.194)

- **PATRÓN** `sigma_h` < `0.0112` → IC=+0.225 (n=3393)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0112 (IC base=+0.222)

- **PATRÓN** `drift_60min` |x|≤ `0.1781` → IC=+0.234 (n=1699)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1781 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.244 (n=1473)
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

- **PATRÓN** `volumen_spike_ratio` > `2.1588` → IC=+0.232 (n=2476)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1588 (IC base=+0.222)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.224 (n=1927)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.222)

- **PATRÓN** `libro_liquidez` > `1984.4248` → IC=+0.227 (n=1285)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1984.4248 (IC base=+0.222)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.227 (n=3657)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 23.0 (IC base=+0.222)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.177 (n=215)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.066 (n=5022)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.147 (n=684)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0039 (IC base=+0.062)

- **PATRÓN** `ibs_20min` > `0.9422` → IC=+0.235 (n=681)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9422 (IC base=+0.062)

- **PATRÓN** `dist_vwap_pct` > `0.1424` → IC=+0.341 (n=463)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1424 (IC base=+0.062)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.111` → IC=+0.208 (n=1496)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.111 (IC base=+0.062)

- **PATRÓN** `volumen_regimen` > `1.2486` → IC=+0.358 (n=273)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2486 (IC base=+0.062)

- **PATRÓN** `volumen_pendiente_norm` < `0.1672` → IC=+0.342 (n=661)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1672 (IC base=+0.062)

- **PATRÓN** `volumen_pendiente_norm` > `0.3052` → IC=+0.341 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3052 (IC base=+0.062)

- **PATRÓN** `volumen_spike_ratio` < `1.5458` → IC=+0.353 (n=351)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5458 (IC base=+0.062)

- **PATRÓN** `volumen_spike_ratio` > `2.2842` → IC=+0.341 (n=362)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2842 (IC base=+0.062)

- **PATRÓN** `ballena_activa_n` < `142.0` → IC=+0.343 (n=811)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 142.0 (IC base=+0.062)

- **PATRÓN** `ibs_20min` < `0.087` → IC=+0.184 (n=1310)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.087 (IC base=+0.056)

- **PATRÓN** `dist_vwap_pct` > `0.5445` → IC=+0.164 (n=421)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.5445 (IC base=+0.056)

- **PATRÓN** `volumen_regimen` < `1.0026` → IC=+0.161 (n=2226)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.0026 (IC base=+0.056)

- **PATRÓN** `volumen_pendiente_norm` > `0.279` → IC=+0.210 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.279 (IC base=+0.056)

- **PATRÓN** `volumen_spike_ratio` > `1.5053` → IC=+0.161 (n=2177)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.5053 (IC base=+0.056)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.182 (n=149)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=803)

- **FILTRO** `ibs_20min` < `0.2667` → IC=-0.174 (n=237)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2667
  - _Potencial_: sin este filtro IC_bueno=+0.089 (n=715)

- **FILTRO** `ibs_20min` > `0.2` → IC=-0.129 (n=4889)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2
  - _Potencial_: sin este filtro IC_bueno=+0.156 (n=2465)

- **FILTRO** `sigma_ewma_delta_pct` > `8.302` → IC=-0.230 (n=795)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.302
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=6559)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.180 (n=326)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.75 (IC base=+0.023)

- **PATRÓN** `dist_vwap_pct` > `0.9797` → IC=+0.283 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9797 (IC base=+0.023)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.266` → IC=+0.144 (n=324)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 2.266 (IC base=+0.023)

- **PATRÓN** `volumen_regimen` > `0.6233` → IC=+0.288 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6233 (IC base=+0.023)

- **PATRÓN** `volumen_pendiente_norm` < `0.0797` → IC=+0.282 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0797 (IC base=+0.023)

- **PATRÓN** `volumen_spike_ratio` < `2.1989` → IC=+0.289 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1989 (IC base=+0.023)

- **PATRÓN** `volumen_spike_ratio` > `1.449` → IC=+0.266 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.449 (IC base=+0.023)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.275 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 40.0 (IC base=+0.023)

- **PATRÓN** `ibs_20min` < `0.2` → IC=+0.156 (n=2465)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.2 (IC base=-0.034)

- **PATRÓN** `dist_vwap_pct` > `0.2308` → IC=+0.286 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2308 (IC base=-0.034)

- **PATRÓN** `volumen_regimen` < `0.6981` → IC=+0.294 (n=483)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6981 (IC base=-0.034)

- **PATRÓN** `volumen_regimen` > `1.0493` → IC=+0.286 (n=498)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0493 (IC base=-0.034)

- **PATRÓN** `volumen_pendiente_norm` > `0.0783` → IC=+0.310 (n=498)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0783 (IC base=-0.034)

- **PATRÓN** `volumen_spike_ratio` < `2.4559` → IC=+0.297 (n=1028)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4559 (IC base=-0.034)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `ibs_20min` < `0.7905` → IC=-0.157 (n=3763)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7905
  - _Potencial_: sin este filtro IC_bueno=+0.135 (n=1940)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.173 (n=1201)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=4502)

- **FILTRO** `ibs_20min` > `0.7352` → IC=-0.190 (n=1973)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7352
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=5921)

- **PATRÓN** `ibs_20min` > `0.7905` → IC=+0.135 (n=1940)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` > 0.7905 (IC base=-0.057)

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

- **PATRÓN** `dist_vwap_pct` > `1.0683` → IC=+0.279 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0683 (IC base=+0.006)

- **PATRÓN** `volumen_regimen` < `0.6412` → IC=+0.272 (n=773)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6412 (IC base=+0.006)

- **PATRÓN** `volumen_regimen` > `1.2057` → IC=+0.288 (n=772)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2057 (IC base=+0.006)

- **PATRÓN** `volumen_pendiente_norm` > `0.2847` → IC=+0.290 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2847 (IC base=+0.006)

- **PATRÓN** `volumen_spike_ratio` < `2.4775` → IC=+0.265 (n=2191)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4775 (IC base=+0.006)

- **PATRÓN** `volumen_spike_ratio` > `1.4355` → IC=+0.272 (n=2190)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4355 (IC base=+0.006)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0108` → IC=+0.193 (n=8003)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` > 0.0108 (IC base=+0.087)

- **PATRÓN** `ibs_20min` > `0.9667` → IC=+0.311 (n=7998)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9667 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` > `0.9443` → IC=+0.301 (n=1623)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9443 (IC base=+0.087)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.47` → IC=+0.168 (n=10762)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 3.47 (IC base=+0.087)

- **PATRÓN** `volumen_regimen` > `0.6921` → IC=+0.279 (n=7922)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6921 (IC base=+0.087)

- **PATRÓN** `volumen_pendiente_norm` > `0.2927` → IC=+0.296 (n=1980)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2927 (IC base=+0.087)

- **PATRÓN** `volumen_spike_ratio` > `2.6436` → IC=+0.286 (n=4641)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6436 (IC base=+0.087)

- **PATRÓN** `ballena_activa_n` < `89.0` → IC=+0.309 (n=13549)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 89.0 (IC base=+0.087)

- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.160 (n=7766)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0104 (IC base=+0.085)

- **PATRÓN** `ibs_20min` < `0.5185` → IC=+0.172 (n=20472)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.5185 (IC base=+0.085)

- **PATRÓN** `volumen_regimen` < `0.6969` → IC=+0.280 (n=3430)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6969 (IC base=+0.085)

- **PATRÓN** `volumen_regimen` > `1.1879` → IC=+0.287 (n=2598)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1879 (IC base=+0.085)

- **PATRÓN** `volumen_pendiente_norm` > `0.2946` → IC=+0.330 (n=1728)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2946 (IC base=+0.085)

- **PATRÓN** `volumen_spike_ratio` < `1.4528` → IC=+0.306 (n=3845)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4528 (IC base=+0.085)

- **PATRÓN** `volumen_spike_ratio` > `2.2787` → IC=+0.305 (n=5229)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2787 (IC base=+0.085)

- **PATRÓN** `ballena_activa_n` < `72.0` → IC=+0.312 (n=11522)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 72.0 (IC base=+0.085)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.8036` → IC=-0.138 (n=4260)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8036
  - _Potencial_: sin este filtro IC_bueno=+0.303 (n=2195)

- **FILTRO** `ibs_20min` > `0.7108` → IC=-0.238 (n=1431)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7108
  - _Potencial_: sin este filtro IC_bueno=+0.055 (n=4298)

- **FILTRO** `sigma_ewma_delta_pct` > `4.079` → IC=-0.237 (n=1228)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.079
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=4501)

- **PATRÓN** `ibs_20min` > `0.8036` → IC=+0.303 (n=2195)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8036 (IC base=+0.013)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.964` → IC=+0.189 (n=2147)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 2.964 (IC base=+0.013)

- **PATRÓN** `volumen_pendiente_norm` > `0.2287` → IC=+0.333 (n=410)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2287 (IC base=+0.013)

- **PATRÓN** `volumen_spike_ratio` < `1.4486` → IC=+0.283 (n=681)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4486 (IC base=+0.013)

- **PATRÓN** `volumen_spike_ratio` > `2.2443` → IC=+0.306 (n=926)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2443 (IC base=+0.013)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.304 (n=2054)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 27.0 (IC base=+0.013)

- **PATRÓN** `ibs_20min` < `0.1727` → IC=+0.174 (n=1433)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.1727 (IC base=-0.018)

- **PATRÓN** `volumen_pendiente_norm` < `0.1514` → IC=+0.397 (n=1171)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1514 (IC base=-0.018)

- **PATRÓN** `volumen_spike_ratio` < `1.537` → IC=+0.418 (n=496)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.537 (IC base=-0.018)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.394 (n=1163)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 22.0 (IC base=-0.018)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.3029` → IC=+0.226 (n=745)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3029 (IC base=+0.010)

- **PATRÓN** `volumen_regimen` < `1.1954` → IC=+0.211 (n=2353)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1954 (IC base=+0.010)

- **PATRÓN** `volumen_regimen` > `0.6949` → IC=+0.220 (n=2102)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6949 (IC base=+0.010)

- **PATRÓN** `volumen_pendiente_norm` > `0.275` → IC=+0.244 (n=314)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.275 (IC base=+0.010)

- **PATRÓN** `volumen_spike_ratio` < `1.4168` → IC=+0.230 (n=776)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4168 (IC base=+0.010)

- **PATRÓN** `volumen_spike_ratio` > `2.4707` → IC=+0.212 (n=775)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4707 (IC base=+0.010)

- **PATRÓN** `ballena_activa_n` < `375.0` → IC=+0.228 (n=2320)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 375.0 (IC base=+0.010)

- **PATRÓN** `volumen_regimen` > `1.018` → IC=+0.267 (n=767)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.018 (IC base=+0.000)

- **PATRÓN** `volumen_pendiente_norm` > `0.2697` → IC=+0.304 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2697 (IC base=+0.000)

- **PATRÓN** `volumen_spike_ratio` < `1.5263` → IC=+0.264 (n=721)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5263 (IC base=+0.000)

- **PATRÓN** `volumen_spike_ratio` > `2.1516` → IC=+0.265 (n=742)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1516 (IC base=+0.000)

- **PATRÓN** `ballena_activa_n` < `203.0` → IC=+0.278 (n=727)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 203.0 (IC base=+0.000)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0114` → IC=+0.323 (n=1515)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0114 (IC base=+0.284)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.294 (n=3346)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.284)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.326 (n=1809)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.284)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.589` → IC=+0.306 (n=2252)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.589 (IC base=+0.284)

- **PATRÓN** `volumen_pendiente_norm` < `0.0975` → IC=+0.296 (n=2940)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0975 (IC base=+0.284)

- **PATRÓN** `volumen_spike_ratio` > `3.2535` → IC=+0.298 (n=1083)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.2535 (IC base=+0.284)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.292 (n=4016)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.284)

- **PATRÓN** `libro_liquidez` > `2007.5584` → IC=+0.295 (n=1114)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2007.5584 (IC base=+0.284)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.305 (n=2055)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 14.0 (IC base=+0.284)

- **PATRÓN** `sigma_h` > `0.0091` → IC=+0.334 (n=2045)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0091 (IC base=+0.307)

- **PATRÓN** `drift_60min` |x|≤ `0.1807` → IC=+0.325 (n=1349)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1807 (IC base=+0.307)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.327 (n=1185)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.307)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.310 (n=1380)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.307)

- **PATRÓN** `ibs_20min` > `0.1481` → IC=+0.318 (n=2046)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1481 (IC base=+0.307)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.104` → IC=+0.315 (n=365)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.104 (IC base=+0.307)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.417` → IC=+0.307 (n=3176)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.417 (IC base=+0.307)

- **PATRÓN** `volumen_pendiente_norm` < `0.1986` → IC=+0.308 (n=3030)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1986 (IC base=+0.307)

- **PATRÓN** `volumen_pendiente_norm` > `0.3446` → IC=+0.319 (n=500)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3446 (IC base=+0.307)

- **PATRÓN** `volumen_spike_ratio` > `2.7444` → IC=+0.322 (n=1343)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7444 (IC base=+0.307)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.308 (n=1536)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.307)

- **PATRÓN** `libro_liquidez` > `1983.798` → IC=+0.315 (n=1022)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1983.798 (IC base=+0.307)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.312 (n=2608)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 22.0 (IC base=+0.307)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7174` → IC=-0.179 (n=1513)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7174
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=4541)

- **PATRÓN** `dist_vwap_pct` > `0.1469` → IC=+0.237 (n=1070)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1469 (IC base=+0.022)

- **PATRÓN** `volumen_regimen` < `1.1591` → IC=+0.239 (n=2164)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1591 (IC base=+0.022)

- **PATRÓN** `volumen_pendiente_norm` < `0.1619` → IC=+0.238 (n=2269)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1619 (IC base=+0.022)

- **PATRÓN** `volumen_pendiente_norm` > `0.1026` → IC=+0.244 (n=709)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1026 (IC base=+0.022)

- **PATRÓN** `volumen_spike_ratio` < `2.421` → IC=+0.243 (n=2101)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.421 (IC base=+0.022)

- **PATRÓN** `ballena_activa_n` < `113.0` → IC=+0.256 (n=2138)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 113.0 (IC base=+0.022)

- **PATRÓN** `dist_vwap_pct` > `0.7534` → IC=+0.264 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7534 (IC base=+0.008)

- **PATRÓN** `volumen_regimen` < `1.1877` → IC=+0.265 (n=1566)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1877 (IC base=+0.008)

- **PATRÓN** `volumen_regimen` > `0.6165` → IC=+0.258 (n=1566)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6165 (IC base=+0.008)

- **PATRÓN** `volumen_pendiente_norm` > `0.2825` → IC=+0.309 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2825 (IC base=+0.008)

- **PATRÓN** `volumen_spike_ratio` < `1.5176` → IC=+0.298 (n=663)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5176 (IC base=+0.008)

- **PATRÓN** `volumen_spike_ratio` > `2.426` → IC=+0.282 (n=502)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.426 (IC base=+0.008)

- **PATRÓN** `ballena_activa_n` < `115.0` → IC=+0.285 (n=1528)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 115.0 (IC base=+0.008)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7429` → IC=-0.248 (n=2472)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7429
  - _Potencial_: sin este filtro IC_bueno=+0.312 (n=2476)

- **FILTRO** `ibs_20min` > `0.6154` → IC=-0.236 (n=1170)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6154
  - _Potencial_: sin este filtro IC_bueno=+0.158 (n=3527)

- **FILTRO** `sigma_ewma_delta_pct` > `8.282` → IC=-0.268 (n=537)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.282
  - _Potencial_: sin este filtro IC_bueno=+0.102 (n=4160)

- **PATRÓN** `ibs_20min` > `0.7429` → IC=+0.312 (n=2476)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7429 (IC base=+0.032)

- **PATRÓN** `dist_vwap_pct` > `1.0589` → IC=+0.352 (n=349)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0589 (IC base=+0.032)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.449` → IC=+0.156 (n=2006)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 2.449 (IC base=+0.032)

- **PATRÓN** `volumen_regimen` < `0.8382` → IC=+0.345 (n=1202)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8382 (IC base=+0.032)

- **PATRÓN** `volumen_regimen` > `0.691` → IC=+0.336 (n=1611)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.691 (IC base=+0.032)

- **PATRÓN** `volumen_pendiente_norm` < `0.0982` → IC=+0.335 (n=1697)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0982 (IC base=+0.032)

- **PATRÓN** `volumen_pendiente_norm` > `0.2751` → IC=+0.371 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2751 (IC base=+0.032)

- **PATRÓN** `volumen_spike_ratio` < `1.4267` → IC=+0.362 (n=584)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4267 (IC base=+0.032)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.354 (n=1564)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=+0.032)

- **PATRÓN** `ibs_20min` < `0.6154` → IC=+0.158 (n=3527)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.6154 (IC base=+0.059)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.738` → IC=+0.127 (n=3683)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` < 4.738 (IC base=+0.059)

- **PATRÓN** `volumen_regimen` < `0.6912` → IC=+0.280 (n=788)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6912 (IC base=+0.059)

- **PATRÓN** `volumen_pendiente_norm` > `0.0707` → IC=+0.299 (n=720)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0707 (IC base=+0.059)

- **PATRÓN** `volumen_spike_ratio` < `1.802` → IC=+0.282 (n=1159)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.802 (IC base=+0.059)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.289 (n=1765)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 46.0 (IC base=+0.059)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.358 (n=2278)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.315)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.317 (n=2576)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.315)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.317 (n=2676)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.315)

- **PATRÓN** `ibs_20min` > `0.6571` → IC=+0.343 (n=2549)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6571 (IC base=+0.315)

- **PATRÓN** `dist_vwap_pct` > `0.2128` → IC=+0.335 (n=1344)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2128 (IC base=+0.315)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.813` → IC=+0.337 (n=967)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.813 (IC base=+0.315)

- **PATRÓN** `volumen_regimen` > `0.6289` → IC=+0.325 (n=2549)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6289 (IC base=+0.315)

- **PATRÓN** `volumen_pendiente_norm` > `0.2819` → IC=+0.348 (n=373)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2819 (IC base=+0.315)

- **PATRÓN** `volumen_spike_ratio` > `1.4313` → IC=+0.327 (n=2459)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4313 (IC base=+0.315)

- **PATRÓN** `libro_liquidez` > `2994.483` → IC=+0.328 (n=850)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2994.483 (IC base=+0.315)

- **PATRÓN** `ballena_activa_n` < `39.0` → IC=+0.341 (n=2301)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 39.0 (IC base=+0.315)

- **PATRÓN** `sigma_h` > `0.0147` → IC=+0.351 (n=1833)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0147 (IC base=+0.316)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.318 (n=2757)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.316)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.315 (n=2750)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.316)

- **PATRÓN** `ibs_20min` < `0.381` → IC=+0.332 (n=2748)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.381 (IC base=+0.316)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.309` → IC=+0.328 (n=508)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.309 (IC base=+0.316)

- **PATRÓN** `volumen_regimen` < `0.7185` → IC=+0.317 (n=1209)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7185 (IC base=+0.316)

- **PATRÓN** `volumen_regimen` > `1.2063` → IC=+0.345 (n=916)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2063 (IC base=+0.316)

- **PATRÓN** `volumen_pendiente_norm` > `0.2839` → IC=+0.369 (n=387)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2839 (IC base=+0.316)

- **PATRÓN** `volumen_spike_ratio` < `1.4127` → IC=+0.320 (n=855)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4127 (IC base=+0.316)

- **PATRÓN** `volumen_spike_ratio` > `2.1452` → IC=+0.319 (n=1164)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1452 (IC base=+0.316)

- **PATRÓN** `libro_liquidez` > `2978.8913` → IC=+0.317 (n=916)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2978.8913 (IC base=+0.316)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.221 (n=5899)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0125 (IC base=+0.172)

- **PATRÓN** `drift_60min` |x|≤ `0.1234` → IC=+0.191 (n=7788)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.1234 (IC base=+0.172)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.183 (n=18394)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.172)

- **PATRÓN** `ibs_20min` > `0.5372` → IC=+0.229 (n=17692)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5372 (IC base=+0.172)

- **PATRÓN** `dist_vwap_pct` > `0.1629` → IC=+0.205 (n=6607)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1629 (IC base=+0.172)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.751` → IC=+0.258 (n=3456)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.751 (IC base=+0.172)

- **PATRÓN** `volumen_regimen` < `1.175` → IC=+0.152 (n=11794)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.175 (IC base=+0.172)

- **PATRÓN** `volumen_regimen` > `0.6222` → IC=+0.151 (n=11794)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.6222 (IC base=+0.172)

- **PATRÓN** `volumen_pendiente_norm` > `0.293` → IC=+0.203 (n=2554)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.293 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` > `2.5993` → IC=+0.184 (n=5738)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 2.5993 (IC base=+0.172)

- **PATRÓN** `ballena_activa_n` < `86.0` → IC=+0.191 (n=16607)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 86.0 (IC base=+0.172)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.193 (n=7737)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0059 (IC base=+0.186)

- **PATRÓN** `sigma_h` > `0.008` → IC=+0.188 (n=11738)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.008 (IC base=+0.186)

- **PATRÓN** `drift_60min` |x|≤ `0.0823` → IC=+0.222 (n=5863)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0823 (IC base=+0.186)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.213 (n=6649)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.186)

- **PATRÓN** `ibs_20min` < `0.5251` → IC=+0.240 (n=17582)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5251 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.508` → IC=+0.192 (n=2786)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 9.508 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.51` → IC=+0.193 (n=15667)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` < 2.51 (IC base=+0.186)

- **PATRÓN** `volumen_regimen` < `1.1858` → IC=+0.166 (n=12493)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.1858 (IC base=+0.186)

- **PATRÓN** `volumen_pendiente_norm` > `0.294` → IC=+0.222 (n=2638)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.294 (IC base=+0.186)

- **PATRÓN** `volumen_spike_ratio` > `2.6308` → IC=+0.197 (n=5588)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.6308 (IC base=+0.186)

- **PATRÓN** `ballena_activa_n` < `91.0` → IC=+0.200 (n=16582)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 91.0 (IC base=+0.186)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` > `0.0109` → IC=+0.263 (n=968)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0109 (IC base=+0.227)

- **PATRÓN** `drift_60min` |x|≤ `0.1047` → IC=+0.257 (n=1278)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1047 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.234 (n=3025)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.227)

- **PATRÓN** `ibs_20min` > `0.9427` → IC=+0.293 (n=1935)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9427 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.46` → IC=+0.328 (n=952)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.46 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` > `0.2811` → IC=+0.285 (n=439)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2811 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` < `1.8356` → IC=+0.225 (n=1848)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8356 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` > `1.4352` → IC=+0.226 (n=2771)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4352 (IC base=+0.227)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.237 (n=3242)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.227)

- **PATRÓN** `sigma_h` < `0.01` → IC=+0.259 (n=2412)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.01 (IC base=+0.257)

- **PATRÓN** `sigma_h` > `0.009` → IC=+0.258 (n=1097)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.009 (IC base=+0.257)

- **PATRÓN** `drift_60min` |x|≤ `0.098` → IC=+0.312 (n=1061)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.098 (IC base=+0.257)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.260 (n=2491)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.257)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.262 (n=2191)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.257)

- **PATRÓN** `ibs_20min` < `0.4403` → IC=+0.275 (n=2410)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4403 (IC base=+0.257)

- **PATRÓN** `sigma_ewma_delta_pct` < `1.957` → IC=+0.262 (n=2386)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 1.957 (IC base=+0.257)

- **PATRÓN** `volumen_pendiente_norm` < `0.1002` → IC=+0.258 (n=2121)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1002 (IC base=+0.257)

- **PATRÓN** `volumen_pendiente_norm` > `0.302` → IC=+0.274 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.302 (IC base=+0.257)

- **PATRÓN** `volumen_spike_ratio` < `1.4471` → IC=+0.275 (n=771)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4471 (IC base=+0.257)

- **PATRÓN** `volumen_spike_ratio` > `2.6989` → IC=+0.262 (n=771)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6989 (IC base=+0.257)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.265 (n=1739)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.257)

- **PATRÓN** `libro_liquidez` > `1777.0488` → IC=+0.264 (n=1607)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1777.0488 (IC base=+0.257)

- **PATRÓN** `ballena_activa_n` < `7.0` → IC=+0.257 (n=916)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 7.0 (IC base=+0.257)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.199 (n=904)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0032 (IC base=+0.127)

- **PATRÓN** `drift_60min` |x|≤ `0.0651` → IC=+0.177 (n=899)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.0651 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.145 (n=2827)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.127)

- **PATRÓN** `ibs_20min` > `0.2551` → IC=+0.204 (n=2697)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2551 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` > `0.1844` → IC=+0.212 (n=1309)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1844 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.624` → IC=+0.209 (n=493)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.624 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` < `0.8585` → IC=+0.130 (n=1798)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 0.8585 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` > `1.0502` → IC=+0.133 (n=1223)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` > 1.0502 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` > `0.2784` → IC=+0.167 (n=415)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.2784 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` < `1.4051` → IC=+0.132 (n=884)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 1.4051 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` > `2.4599` → IC=+0.142 (n=884)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 2.4599 (IC base=+0.127)

- **PATRÓN** `ballena_activa_n` < `396.0` → IC=+0.132 (n=2623)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 396.0 (IC base=+0.127)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.172 (n=2901)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0066 (IC base=+0.152)

- **PATRÓN** `drift_60min` |x|≤ `0.2444` → IC=+0.175 (n=2552)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.2444 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.185 (n=1387)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 15.0 (IC base=+0.152)

- **PATRÓN** `ibs_20min` < `0.6093` → IC=+0.211 (n=2900)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6093 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.904` → IC=+0.178 (n=541)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 10.904 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.032` → IC=+0.157 (n=2530)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 4.032 (IC base=+0.152)

- **PATRÓN** `volumen_regimen` < `1.2025` → IC=+0.163 (n=2900)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2025 (IC base=+0.152)

- **PATRÓN** `volumen_pendiente_norm` < `0.2288` → IC=+0.155 (n=3079)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` < 0.2288 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` < `2.4713` → IC=+0.156 (n=2774)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.4713 (IC base=+0.152)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=3756)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.152)

- **PATRÓN** `ballena_activa_n` < `207.0` → IC=+0.202 (n=1196)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 207.0 (IC base=+0.152)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.01` → IC=+0.224 (n=1999)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.01 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.2513` → IC=+0.231 (n=1998)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2513 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.218 (n=3125)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.290 (n=1596)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.044` → IC=+0.306 (n=714)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.044 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` < `0.0984` → IC=+0.210 (n=2614)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0984 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.3511` → IC=+0.239 (n=423)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3511 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `2.71` → IC=+0.224 (n=1326)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.71 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.213 (n=3626)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `1995.9484` → IC=+0.223 (n=999)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1995.9484 (IC base=+0.210)

- **PATRÓN** `sigma_h` < `0.0109` → IC=+0.248 (n=2360)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0109 (IC base=+0.241)

- **PATRÓN** `drift_60min` |x|≤ `0.2465` → IC=+0.271 (n=1787)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2465 (IC base=+0.241)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.281 (n=1035)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.241)

- **PATRÓN** `ibs_20min` < `0.0409` → IC=+0.294 (n=1179)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0409 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.896` → IC=+0.280 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.896 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` > `0.3537` → IC=+0.288 (n=447)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3537 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` < `1.7676` → IC=+0.240 (n=1140)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7676 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` > `2.1795` → IC=+0.253 (n=1727)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1795 (IC base=+0.241)

- **PATRÓN** `libro_liquidez` > `1872.8363` → IC=+0.247 (n=1215)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1872.8363 (IC base=+0.241)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.240 (n=1736)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.241)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.197 (n=976)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0038 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.0787` → IC=+0.182 (n=974)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.0787 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.138 (n=3028)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` > `0.245` → IC=+0.189 (n=2921)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.245 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` > `0.14` → IC=+0.185 (n=1647)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.14 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.231` → IC=+0.200 (n=501)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.231 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `0.8387` → IC=+0.137 (n=1948)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.8387 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` > `0.2873` → IC=+0.169 (n=439)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` > 0.2873 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `1.805` → IC=+0.126 (n=1907)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 1.805 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` > `2.5066` → IC=+0.136 (n=954)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 2.5066 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `6875.7972` → IC=+0.198 (n=1324)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 6875.7972 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `125.0` → IC=+0.127 (n=2866)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 125.0 (IC base=+0.126)

- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.164 (n=2755)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0068 (IC base=+0.132)

- **PATRÓN** `drift_60min` |x|≤ `0.4077` → IC=+0.148 (n=3127)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.4077 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.168 (n=1504)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 15.0 (IC base=+0.132)

- **PATRÓN** `ibs_20min` < `0.6715` → IC=+0.188 (n=3127)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.6715 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.22` → IC=+0.142 (n=746)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 9.22 (IC base=+0.132)

- **PATRÓN** `volumen_regimen` < `0.852` → IC=+0.151 (n=2085)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.852 (IC base=+0.132)

- **PATRÓN** `volumen_pendiente_norm` > `0.2938` → IC=+0.180 (n=467)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.2938 (IC base=+0.132)

- **PATRÓN** `volumen_spike_ratio` < `2.1913` → IC=+0.133 (n=2614)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 2.1913 (IC base=+0.132)

- **PATRÓN** `volumen_spike_ratio` > `1.5151` → IC=+0.134 (n=2654)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 1.5151 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `6390.1468` → IC=+0.193 (n=1418)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 6390.1468 (IC base=+0.132)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.157 (n=987)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 48.0 (IC base=+0.132)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0127` → IC=+0.165 (n=1085)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.0127 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.134 (n=3343)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 5.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` > `0.4706` → IC=+0.204 (n=3260)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4706 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` > `0.201` → IC=+0.188 (n=1715)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.201 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.972` → IC=+0.287 (n=685)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.972 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` < `1.0272` → IC=+0.128 (n=2861)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 1.0272 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` < `0.1618` → IC=+0.122 (n=3315)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_pendiente_norm` < 0.1618 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` < `1.7794` → IC=+0.123 (n=2103)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 1.7794 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `2676.0135` → IC=+0.198 (n=1474)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 2676.0135 (IC base=+0.118)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.129 (n=1085)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 16.0 (IC base=+0.118)

- **PATRÓN** `sigma_h` < `0.012` → IC=+0.143 (n=3421)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.012 (IC base=+0.123)

- **PATRÓN** `drift_60min` |x|≤ `0.1149` → IC=+0.164 (n=1139)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.1149 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.137 (n=3493)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` < `0.6471` → IC=+0.221 (n=3418)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6471 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.239` → IC=+0.144 (n=3023)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 2.239 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` < `1.1785` → IC=+0.129 (n=3417)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 1.1785 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` > `0.8596` → IC=+0.126 (n=2278)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` > 0.8596 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` < `0.1614` → IC=+0.126 (n=3366)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` < 0.1614 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` > `0.275` → IC=+0.150 (n=478)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.275 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` < `1.4338` → IC=+0.140 (n=1079)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.4338 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` > `2.4432` → IC=+0.135 (n=1079)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 2.4432 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `2575.0977` → IC=+0.191 (n=1549)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 2575.0977 (IC base=+0.123)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.130 (n=3227)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 44.0 (IC base=+0.123)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0127` → IC=+0.250 (n=2614)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0127 (IC base=+0.227)

- **PATRÓN** `drift_60min` |x|≤ `0.1653` → IC=+0.243 (n=1288)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1653 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.233 (n=3046)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.227)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.229 (n=2638)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.227)

- **PATRÓN** `ibs_20min` > `0.6667` → IC=+0.258 (n=2928)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6667 (IC base=+0.227)

- **PATRÓN** `dist_vwap_pct` > `1.1299` → IC=+0.237 (n=641)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1299 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.527` → IC=+0.258 (n=1344)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.527 (IC base=+0.227)

- **PATRÓN** `volumen_regimen` > `0.6199` → IC=+0.237 (n=2925)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6199 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` > `0.2347` → IC=+0.268 (n=546)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2347 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` < `2.4665` → IC=+0.230 (n=2855)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4665 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` > `1.4322` → IC=+0.231 (n=2855)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4322 (IC base=+0.227)

- **PATRÓN** `libro_liquidez` > `2595.0652` → IC=+0.231 (n=1950)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2595.0652 (IC base=+0.227)

- **PATRÓN** `sigma_h` < `0.0124` → IC=+0.243 (n=1342)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0124 (IC base=+0.242)

- **PATRÓN** `sigma_h` > `0.0224` → IC=+0.248 (n=1383)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0224 (IC base=+0.242)

- **PATRÓN** `drift_60min` |x|≤ `0.602` → IC=+0.251 (n=3050)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.602 (IC base=+0.242)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.253 (n=1503)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.242)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.247 (n=1357)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.242)

- **PATRÓN** `ibs_20min` < `0.037` → IC=+0.301 (n=1342)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.037 (IC base=+0.242)

- **PATRÓN** `dist_vwap_pct` > `1.1506` → IC=+0.260 (n=269)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1506 (IC base=+0.242)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.109` → IC=+0.270 (n=586)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.109 (IC base=+0.242)

- **PATRÓN** `volumen_regimen` < `0.87` → IC=+0.242 (n=2034)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.87 (IC base=+0.242)

- **PATRÓN** `volumen_regimen` > `0.6413` → IC=+0.244 (n=3049)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6413 (IC base=+0.242)

- **PATRÓN** `volumen_pendiente_norm` > `0.2812` → IC=+0.297 (n=421)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2812 (IC base=+0.242)

- **PATRÓN** `volumen_spike_ratio` < `2.5167` → IC=+0.239 (n=2882)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5167 (IC base=+0.242)

- **PATRÓN** `volumen_spike_ratio` > `1.5489` → IC=+0.242 (n=2575)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5489 (IC base=+0.242)

- **PATRÓN** `libro_liquidez` > `2960.6154` → IC=+0.242 (n=1017)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2960.6154 (IC base=+0.242)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.210 (n=1544)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.156)

- **PATRÓN** `drift_60min` |x|≤ `0.1364` → IC=+0.172 (n=2033)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.1364 (IC base=+0.156)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.168 (n=4827)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.156)

- **PATRÓN** `ibs_20min` > `0.4194` → IC=+0.201 (n=4128)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4194 (IC base=+0.156)

- **PATRÓN** `dist_vwap_pct` > `0.2244` → IC=+0.177 (n=1706)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.2244 (IC base=+0.156)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.516` → IC=+0.209 (n=758)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.516 (IC base=+0.156)

- **PATRÓN** `volumen_regimen` < `0.8605` → IC=+0.166 (n=2780)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.8605 (IC base=+0.156)

- **PATRÓN** `volumen_regimen` > `1.1957` → IC=+0.163 (n=1390)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 1.1957 (IC base=+0.156)

- **PATRÓN** `volumen_pendiente_norm` > `0.1569` → IC=+0.173 (n=1215)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.1569 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` < `1.528` → IC=+0.161 (n=1984)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 1.528 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` > `1.809` → IC=+0.158 (n=3005)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.809 (IC base=+0.156)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.157 (n=3954)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.01 (IC base=+0.156)

- **PATRÓN** `libro_liquidez` > `7325.3761` → IC=+0.186 (n=2095)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 7325.3761 (IC base=+0.156)

- **PATRÓN** `ibs_20min` < `0.3814` → IC=+0.175 (n=3371)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.3814 (IC base=+0.098)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.140 (n=2211)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 23.0 (IC base=+0.098)

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

- **PATRÓN** `ibs_20min` < `0.2095` → IC=+0.198 (n=636)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.2095 (IC base=+0.079)

- **PATRÓN** `ballena_activa_n` < `166.0` → IC=+0.174 (n=623)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 166.0 (IC base=+0.079)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.232 (n=620)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.2136` → IC=+0.157 (n=934)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.2136 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.171 (n=1455)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 5.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` > `0.7791` → IC=+0.265 (n=635)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7791 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` > `0.5849` → IC=+0.192 (n=293)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.5849 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.884` → IC=+0.204 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.884 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` < `0.8322` → IC=+0.165 (n=934)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8322 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` > `1.1614` → IC=+0.152 (n=467)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 1.1614 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` > `0.2178` → IC=+0.195 (n=254)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2178 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` > `2.4735` → IC=+0.180 (n=460)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 2.4735 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `7934.036` → IC=+0.177 (n=635)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 7934.036 (IC base=+0.153)

- **PATRÓN** `ballena_activa_n` < `31.0` → IC=+0.151 (n=462)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 31.0 (IC base=+0.153)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.126 (n=924)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.63€ cuando `sigma_h` < 0.0053 (IC base=+0.096)

- **PATRÓN** `ibs_20min` < `0.087` → IC=+0.200 (n=462)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.087 (IC base=+0.096)

- **PATRÓN** `volumen_regimen` < `0.6769` → IC=+0.134 (n=610)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 0.6769 (IC base=+0.096)

- **PATRÓN** `libro_liquidez` > `7772.1265` → IC=+0.149 (n=628)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 7772.1265 (IC base=+0.096)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.130 (n=452)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 34.0 (IC base=+0.096)

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

- **PATRÓN** `ibs_20min` < `0.5484` → IC=+0.163 (n=1162)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` < 0.5484 (IC base=+0.082)

- **PATRÓN** `libro_liquidez` > `2638.5742` → IC=+0.166 (n=599)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2638.5742 (IC base=+0.082)

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
- **PATRÓN** `sigma_h` > `0.0126` → IC=+0.227 (n=7769)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0126 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.190 (n=24330)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` > `0.4268` → IC=+0.226 (n=23295)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4268 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` > `0.8917` → IC=+0.215 (n=2643)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8917 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.933` → IC=+0.259 (n=5716)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.933 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` < `1.2131` → IC=+0.160 (n=15694)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2131 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.2406` → IC=+0.209 (n=4186)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2406 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `2.6236` → IC=+0.192 (n=7585)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.6236 (IC base=+0.180)

- **PATRÓN** `ballena_activa_n` < `102.0` → IC=+0.201 (n=21941)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 102.0 (IC base=+0.180)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.200 (n=7183)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.198)

- **PATRÓN** `sigma_h` > `0.0123` → IC=+0.209 (n=7182)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0123 (IC base=+0.198)

- **PATRÓN** `drift_60min` |x|≤ `0.1478` → IC=+0.203 (n=9484)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1478 (IC base=+0.198)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.217 (n=8120)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.198)

- **PATRÓN** `ibs_20min` < `0.4851` → IC=+0.253 (n=18962)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4851 (IC base=+0.198)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.521` → IC=+0.204 (n=20019)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.521 (IC base=+0.198)

- **PATRÓN** `volumen_regimen` < `0.7005` → IC=+0.176 (n=6364)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.7005 (IC base=+0.198)

- **PATRÓN** `volumen_pendiente_norm` > `0.293` → IC=+0.257 (n=2960)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.293 (IC base=+0.198)

- **PATRÓN** `volumen_spike_ratio` > `2.6264` → IC=+0.212 (n=6889)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6264 (IC base=+0.198)

- **PATRÓN** `ballena_activa_n` < `91.0` → IC=+0.214 (n=20461)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 91.0 (IC base=+0.198)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.253 (n=1807)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` > `0.8629` → IC=+0.297 (n=2480)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8629 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.852` → IC=+0.343 (n=887)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.852 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.2327` → IC=+0.287 (n=666)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2327 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` < `1.4492` → IC=+0.232 (n=1200)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4492 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.2936` → IC=+0.240 (n=1631)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2936 (IC base=+0.234)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.248 (n=4122)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `2024.9` → IC=+0.237 (n=1240)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2024.9 (IC base=+0.234)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.249 (n=2313)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 14.0 (IC base=+0.234)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.268 (n=3356)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.268)

- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.270 (n=1521)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0094 (IC base=+0.268)

- **PATRÓN** `drift_60min` |x|≤ `0.1239` → IC=+0.295 (n=1476)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1239 (IC base=+0.268)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.269 (n=3490)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.268)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.272 (n=3021)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.268)

- **PATRÓN** `ibs_20min` < `0.5506` → IC=+0.286 (n=3355)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5506 (IC base=+0.268)

- **PATRÓN** `volumen_pendiente_norm` < `0.0978` → IC=+0.270 (n=3059)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0978 (IC base=+0.268)

- **PATRÓN** `volumen_pendiente_norm` > `0.2908` → IC=+0.290 (n=461)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2908 (IC base=+0.268)

- **PATRÓN** `volumen_spike_ratio` < `1.5659` → IC=+0.273 (n=1419)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5659 (IC base=+0.268)

- **PATRÓN** `volumen_spike_ratio` > `2.6526` → IC=+0.282 (n=1075)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6526 (IC base=+0.268)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.273 (n=2407)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.268)

- **PATRÓN** `libro_liquidez` > `1776.9842` → IC=+0.276 (n=2236)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1776.9842 (IC base=+0.268)

- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.278 (n=1228)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 8.0 (IC base=+0.268)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.176 (n=1281)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0032 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.0797` → IC=+0.148 (n=1275)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.0797 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.150 (n=3992)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 5.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` > `0.3074` → IC=+0.202 (n=3415)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3074 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` > `0.3238` → IC=+0.199 (n=1190)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.3238 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.313` → IC=+0.166 (n=797)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 9.313 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `0.6345` → IC=+0.155 (n=1275)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.6345 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` > `1.068` → IC=+0.143 (n=1733)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 1.068 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.2716` → IC=+0.184 (n=540)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.2716 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `2.1695` → IC=+0.143 (n=3306)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.1695 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `1.5157` → IC=+0.144 (n=3356)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.5157 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `296.0` → IC=+0.153 (n=2471)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 296.0 (IC base=+0.138)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.172 (n=2938)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0058 (IC base=+0.142)

- **PATRÓN** `drift_60min` |x|≤ `0.0807` → IC=+0.169 (n=1113)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.0807 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.172 (n=1237)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.142)

- **PATRÓN** `ibs_20min` < `0.6796` → IC=+0.189 (n=3338)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.6796 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.005` → IC=+0.144 (n=3018)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 4.005 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` < `1.0421` → IC=+0.153 (n=2936)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 1.0421 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` > `0.2208` → IC=+0.193 (n=613)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2208 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` < `2.4301` → IC=+0.147 (n=3226)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 2.4301 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` > `1.7697` → IC=+0.147 (n=2150)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.7697 (IC base=+0.142)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=4336)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.142)

- **PATRÓN** `ballena_activa_n` < `219.0` → IC=+0.169 (n=1052)

  - _Acción_: Kelly boost +0.84€ cuando `ballena_activa_n` < 219.0 (IC base=+0.142)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0132` → IC=+0.242 (n=1301)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0132 (IC base=+0.225)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.235 (n=4073)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.225 (n=3468)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.225)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.302 (n=1445)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.225)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.981` → IC=+0.320 (n=866)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.981 (IC base=+0.225)

- **PATRÓN** `volumen_pendiente_norm` < `0.1319` → IC=+0.226 (n=3682)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1319 (IC base=+0.225)

- **PATRÓN** `volumen_pendiente_norm` > `0.3501` → IC=+0.230 (n=509)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3501 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` > `2.7497` → IC=+0.241 (n=1722)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7497 (IC base=+0.225)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.231 (n=4693)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.225)

- **PATRÓN** `libro_liquidez` > `2004.561` → IC=+0.240 (n=1294)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2004.561 (IC base=+0.225)

- **PATRÓN** `sigma_h` < `0.0111` → IC=+0.250 (n=3287)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0111 (IC base=+0.245)

- **PATRÓN** `drift_60min` |x|≤ `0.1805` → IC=+0.261 (n=1643)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1805 (IC base=+0.245)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.265 (n=1431)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.245)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.248 (n=1691)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.245)

- **PATRÓN** `ibs_20min` < `0.0625` → IC=+0.305 (n=1253)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0625 (IC base=+0.245)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.038` → IC=+0.307 (n=391)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.038 (IC base=+0.245)

- **PATRÓN** `volumen_pendiente_norm` > `0.3476` → IC=+0.305 (n=562)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3476 (IC base=+0.245)

- **PATRÓN** `volumen_spike_ratio` > `2.1748` → IC=+0.257 (n=2400)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1748 (IC base=+0.245)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.250 (n=1876)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.245)

- **PATRÓN** `libro_liquidez` > `1979.1872` → IC=+0.255 (n=1244)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1979.1872 (IC base=+0.245)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.250 (n=3137)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 21.0 (IC base=+0.245)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.194 (n=1346)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0038 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.3397` → IC=+0.148 (n=3548)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.3397 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.151 (n=4189)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 5.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` > `0.882` → IC=+0.269 (n=1345)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.882 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.1977` → IC=+0.169 (n=1773)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.1977 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.068` → IC=+0.168 (n=609)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 11.068 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `0.8567` → IC=+0.154 (n=2689)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.8567 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.2323` → IC=+0.193 (n=714)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2323 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `1.5143` → IC=+0.155 (n=1736)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 1.5143 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `2.156` → IC=+0.142 (n=1788)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 2.156 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `7287.1688` → IC=+0.241 (n=1344)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7287.1688 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `87.0` → IC=+0.147 (n=2645)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 87.0 (IC base=+0.139)

- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.172 (n=2986)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0069 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.445` → IC=+0.160 (n=3394)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.445 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.175 (n=1261)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 17.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` < `0.7054` → IC=+0.199 (n=3394)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7054 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.827` → IC=+0.151 (n=497)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 10.827 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.019` → IC=+0.153 (n=2965)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 3.019 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `0.8555` → IC=+0.161 (n=2263)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.8555 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` > `0.2937` → IC=+0.215 (n=433)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2937 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `2.2021` → IC=+0.152 (n=2887)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.2021 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` > `1.525` → IC=+0.156 (n=2931)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.525 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `6600.8502` → IC=+0.224 (n=1131)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6600.8502 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `89.0` → IC=+0.164 (n=2224)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 89.0 (IC base=+0.149)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0128` → IC=+0.152 (n=1367)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` > 0.0128 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.147 (n=2900)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 11.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` > `0.4286` → IC=+0.187 (n=4100)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.4286 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` > `1.0139` → IC=+0.204 (n=650)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0139 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.234` → IC=+0.274 (n=1040)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.234 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` < `0.8739` → IC=+0.132 (n=2732)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 0.8739 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` < `2.4923` → IC=+0.121 (n=3999)

  - _Acción_: Kelly boost +0.60€ cuando `volumen_spike_ratio` < 2.4923 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `2726.3005` → IC=+0.240 (n=1366)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2726.3005 (IC base=+0.117)

- **PATRÓN** `sigma_h` < `0.011` → IC=+0.156 (n=3386)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.011 (IC base=+0.134)

- **PATRÓN** `drift_60min` |x|≤ `0.1399` → IC=+0.153 (n=1282)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.1399 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.169 (n=1823)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 15.0 (IC base=+0.134)

- **PATRÓN** `ibs_20min` < `0.6667` → IC=+0.220 (n=3868)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6667 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.042` → IC=+0.156 (n=3724)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 3.042 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` < `0.6386` → IC=+0.152 (n=1283)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.6386 (IC base=+0.134)

- **PATRÓN** `volumen_pendiente_norm` > `0.2296` → IC=+0.198 (n=681)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2296 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` < `1.4381` → IC=+0.162 (n=1220)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 1.4381 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `2624.9762` → IC=+0.216 (n=1282)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2624.9762 (IC base=+0.134)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.145 (n=3669)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 49.0 (IC base=+0.134)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.259 (n=3743)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0113 (IC base=+0.239)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.245 (n=3917)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.239)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.244 (n=2497)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.239)

- **PATRÓN** `ibs_20min` > `0.6145` → IC=+0.271 (n=3343)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6145 (IC base=+0.239)

- **PATRÓN** `dist_vwap_pct` > `0.197` → IC=+0.252 (n=1880)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.197 (IC base=+0.239)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.11` → IC=+0.289 (n=657)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.11 (IC base=+0.239)

- **PATRÓN** `volumen_regimen` < `1.219` → IC=+0.240 (n=3742)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.219 (IC base=+0.239)

- **PATRÓN** `volumen_regimen` > `0.6434` → IC=+0.244 (n=3742)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6434 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` > `0.2397` → IC=+0.255 (n=652)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2397 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` > `2.4984` → IC=+0.254 (n=1221)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4984 (IC base=+0.239)

- **PATRÓN** `libro_liquidez` > `2984.8754` → IC=+0.246 (n=1247)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2984.8754 (IC base=+0.239)

- **PATRÓN** `sigma_h` > `0.0255` → IC=+0.268 (n=1297)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0255 (IC base=+0.245)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.250 (n=3672)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.245)

- **PATRÓN** `ibs_20min` < `0.1388` → IC=+0.310 (n=1712)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1388 (IC base=+0.245)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.07` → IC=+0.277 (n=741)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.07 (IC base=+0.245)

- **PATRÓN** `volumen_regimen` < `0.7156` → IC=+0.246 (n=1712)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7156 (IC base=+0.245)

- **PATRÓN** `volumen_regimen` > `1.214` → IC=+0.267 (n=1297)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.214 (IC base=+0.245)

- **PATRÓN** `volumen_pendiente_norm` > `0.2861` → IC=+0.312 (n=534)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2861 (IC base=+0.245)

- **PATRÓN** `volumen_spike_ratio` > `1.432` → IC=+0.248 (n=3679)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.432 (IC base=+0.245)

- **PATRÓN** `libro_liquidez` > `2971.4954` → IC=+0.247 (n=1297)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2971.4954 (IC base=+0.245)

### GBM_LATE_5M
- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.231 (n=6007)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0106 (IC base=+0.223)

- **PATRÓN** `drift_60min` |x|≤ `0.5218` → IC=+0.232 (n=6820)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5218 (IC base=+0.223)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.230 (n=6887)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.223)

- **PATRÓN** `ibs_20min` > `0.9284` → IC=+0.259 (n=2274)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9284 (IC base=+0.223)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.574` → IC=+0.229 (n=3400)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.574 (IC base=+0.223)

- **PATRÓN** `volumen_regimen` < `0.7035` → IC=+0.232 (n=2138)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7035 (IC base=+0.223)

- **PATRÓN** `volumen_regimen` > `0.8776` → IC=+0.223 (n=3238)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8776 (IC base=+0.223)

- **PATRÓN** `volumen_pendiente_norm` < `0.1043` → IC=+0.224 (n=6376)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1043 (IC base=+0.223)

- **PATRÓN** `volumen_pendiente_norm` > `0.1649` → IC=+0.231 (n=1925)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1649 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` < `2.258` → IC=+0.228 (n=5908)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.258 (IC base=+0.223)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.227 (n=4916)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.223)

- **PATRÓN** `libro_liquidez` > `3697.2924` → IC=+0.230 (n=4547)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3697.2924 (IC base=+0.223)

- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.236 (n=1551)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.203)

- **PATRÓN** `drift_60min` |x|≤ `0.3977` → IC=+0.218 (n=4088)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3977 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.215 (n=1555)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.215 (n=2066)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.203)

- **PATRÓN** `ibs_20min` < `0.0881` → IC=+0.214 (n=1549)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0881 (IC base=+0.203)

- **PATRÓN** `dist_vwap_pct` > `0.6774` → IC=+0.210 (n=746)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6774 (IC base=+0.203)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.762` → IC=+0.217 (n=4196)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.762 (IC base=+0.203)

- **PATRÓN** `volumen_regimen` < `1.0948` → IC=+0.209 (n=3838)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0948 (IC base=+0.203)

- **PATRÓN** `volumen_pendiente_norm` < `0.0981` → IC=+0.205 (n=4287)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0981 (IC base=+0.203)

- **PATRÓN** `volumen_pendiente_norm` > `0.0735` → IC=+0.204 (n=2062)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0735 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` < `1.5329` → IC=+0.206 (n=2016)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5329 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` > `2.1958` → IC=+0.212 (n=2077)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1958 (IC base=+0.203)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.203 (n=6056)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.203)

- **PATRÓN** `ballena_activa_n` < `30.0` → IC=+0.228 (n=2063)

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

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.244 (n=1051)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.214)

- **PATRÓN** `ibs_20min` > `0.9855` → IC=+0.289 (n=391)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9855 (IC base=+0.214)

- **PATRÓN** `dist_vwap_pct` > `0.8142` → IC=+0.238 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8142 (IC base=+0.214)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.168` → IC=+0.245 (n=633)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.168 (IC base=+0.214)

- **PATRÓN** `volumen_regimen` < `0.701` → IC=+0.247 (n=515)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.701 (IC base=+0.214)

- **PATRÓN** `volumen_pendiente_norm` < `0.104` → IC=+0.220 (n=1068)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.104 (IC base=+0.214)

- **PATRÓN** `volumen_pendiente_norm` > `0.2722` → IC=+0.224 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2722 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` < `2.1715` → IC=+0.225 (n=1004)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1715 (IC base=+0.214)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.223 (n=1378)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.214)

- **PATRÓN** `libro_liquidez` > `4364.6181` → IC=+0.253 (n=390)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4364.6181 (IC base=+0.214)

- **PATRÓN** `sigma_h` > `0.0103` → IC=+0.257 (n=541)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0103 (IC base=+0.238)

- **PATRÓN** `drift_60min` |x|≤ `0.635` → IC=+0.250 (n=811)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.635 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.240 (n=755)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.238)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.261 (n=566)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.238)

- **PATRÓN** `ibs_20min` < `0.64` → IC=+0.263 (n=714)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.64 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.913` → IC=+0.258 (n=761)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.913 (IC base=+0.238)

- **PATRÓN** `volumen_regimen` < `0.6704` → IC=+0.251 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6704 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` < `0.0825` → IC=+0.251 (n=692)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0825 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` > `2.2105` → IC=+0.265 (n=360)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2105 (IC base=+0.238)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.239 (n=1065)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.238)

- **PATRÓN** `libro_liquidez` > `3873.4371` → IC=+0.262 (n=541)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3873.4371 (IC base=+0.238)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.274 (n=709)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 34.0 (IC base=+0.238)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.149 (n=781)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0039 (IC base=+0.053)

- **PATRÓN** `ibs_20min` > `0.7472` → IC=+0.183 (n=1497)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.7472 (IC base=+0.053)

- **PATRÓN** `dist_vwap_pct` > `0.1486` → IC=+0.142 (n=1077)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.1486 (IC base=+0.053)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.347` → IC=+0.140 (n=495)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 10.347 (IC base=+0.053)

- **PATRÓN** `ibs_20min` < `0.625` → IC=+0.140 (n=1599)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` < 0.625 (IC base=+0.055)

- **PATRÓN** `volumen_pendiente_norm` > `0.1474` → IC=+0.143 (n=435)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_pendiente_norm` > 0.1474 (IC base=+0.055)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.125 (n=652)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.63€ cuando `sigma_h` < 0.0054 (IC base=+0.067)

- **PATRÓN** `ibs_20min` > `0.5412` → IC=+0.160 (n=633)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` > 0.5412 (IC base=+0.067)

- **PATRÓN** `dist_vwap_pct` > `0.1239` → IC=+0.168 (n=323)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.1239 (IC base=+0.067)

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

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.146 (n=334)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0042 (IC base=+0.068)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.122 (n=379)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 15.0 (IC base=+0.068)

- **PATRÓN** `ibs_20min` > `0.9347` → IC=+0.258 (n=329)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9347 (IC base=+0.068)

- **PATRÓN** `dist_vwap_pct` > `0.1297` → IC=+0.167 (n=343)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1297 (IC base=+0.068)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.613` → IC=+0.203 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.613 (IC base=+0.068)

- **PATRÓN** `volumen_pendiente_norm` > `0.2818` → IC=+0.150 (n=101)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.2818 (IC base=+0.068)

- **PATRÓN** `ibs_20min` < `0.1087` → IC=+0.263 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1087 (IC base=+0.034)

### GBM_LATE_60M#SOL#60min
- **PATRÓN** `ibs_20min` > `0.72` → IC=+0.136 (n=542)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` > 0.72 (IC base=+0.027)

- **PATRÓN** `dist_vwap_pct` > `0.7329` → IC=+0.143 (n=183)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` > 0.7329 (IC base=+0.027)

- **PATRÓN** `sigma_h` < `0.0097` → IC=+0.183 (n=336)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0097 (IC base=+0.088)

- **PATRÓN** `ibs_20min` < `0.1772` → IC=+0.248 (n=316)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1772 (IC base=+0.088)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.827` → IC=+0.304 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.827 (IC base=+0.088)

- **PATRÓN** `volumen_regimen` > `1.1079` → IC=+0.200 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1079 (IC base=+0.088)

- **PATRÓN** `volumen_pendiente_norm` > `0.1084` → IC=+0.169 (n=179)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` > 0.1084 (IC base=+0.088)

- **PATRÓN** `volumen_spike_ratio` > `2.5364` → IC=+0.153 (n=148)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 2.5364 (IC base=+0.088)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.127 (n=223)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.03 (IC base=+0.088)

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
- **FILTRO** `sigma_h` < `0.0063` → IC=-0.208 (n=87)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0063
  - _Potencial_: sin este filtro IC_bueno=-0.117 (n=45)

- **FILTRO** `ibs_20min` < `0.5872` → IC=-0.471 (n=33)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5872
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=99)

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

- **FILTRO** `sigma_ewma_delta_pct` > `2.394` → IC=-0.326 (n=21)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 2.394
  - _Potencial_: sin este filtro IC_bueno=-0.191 (n=40)

- **FILTRO** `volumen_regimen` < `0.9169` → IC=-0.455 (n=20)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9169
  - _Potencial_: sin este filtro IC_bueno=-0.128 (n=41)

- **FILTRO** `libro_spread` > `0.05` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.05
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=42)

### GBM_LATE_60M_PYCONFIRMADO
- **PATRÓN** `sigma_h` > `0.0076` → IC=+0.234 (n=340)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0076 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.191 (n=341)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 16.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` > `0.6757` → IC=+0.183 (n=750)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.6757 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.8196` → IC=+0.292 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8196 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.607` → IC=+0.154 (n=409)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 3.607 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `0.6242` → IC=+0.186 (n=250)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 0.6242 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` < `0.0701` → IC=+0.178 (n=561)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` < 0.0701 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `1.396` → IC=+0.199 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.396 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.767` → IC=+0.143 (n=264)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 8.767 (IC base=+0.031)

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

- **PATRÓN** `ibs_20min` < `0.2418` → IC=+0.143 (n=416)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.2418 (IC base=+0.085)

- **PATRÓN** `volumen_pendiente_norm` > `0.2735` → IC=+0.144 (n=71)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_pendiente_norm` > 0.2735 (IC base=+0.085)

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
- **FILTRO** `ibs_20min` > `0.0667` → IC=-0.229 (n=105)

  - _Acción_: SKIP cuando `ibs_20min` > 0.0667
  - _Potencial_: sin este filtro IC_bueno=+0.087 (n=107)

- **FILTRO** `dist_vwap_pct` > `0.1871` → IC=-0.176 (n=35)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1871
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=177)

- **PATRÓN** `sigma_h` > `0.0102` → IC=+0.273 (n=130)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0102 (IC base=+0.252)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.271 (n=295)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.252)

- **PATRÓN** `ibs_20min` > `0.6` → IC=+0.281 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6 (IC base=+0.252)

- **PATRÓN** `dist_vwap_pct` > `0.737` → IC=+0.396 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.737 (IC base=+0.252)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.824` → IC=+0.333 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.824 (IC base=+0.252)

- **PATRÓN** `volumen_regimen` < `0.6071` → IC=+0.306 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6071 (IC base=+0.252)

- **PATRÓN** `volumen_pendiente_norm` > `0.0966` → IC=+0.304 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0966 (IC base=+0.252)

- **PATRÓN** `volumen_spike_ratio` < `1.3961` → IC=+0.335 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3961 (IC base=+0.252)

- **PATRÓN** `volumen_spike_ratio` > `2.309` → IC=+0.297 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.309 (IC base=+0.252)

### LATE_WINDOW_5MIN
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.326 (n=136)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3486` → IC=+0.337 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3486 (IC base=+0.325)

- **PATRÓN** `elapsed_s` > `209.2` → IC=+0.400 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 209.2 (IC base=+0.325)

- **PATRÓN** `drift_15min` |x|≤ `2.2347` → IC=+0.348 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.2347 (IC base=+0.325)

- **PATRÓN** `drift_60min` |x|≤ `0.8028` → IC=+0.391 (n=90)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.8028 (IC base=+0.325)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.381 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.325)

- **PATRÓN** `ballena_activa_n` < `1105.0` → IC=+0.389 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1105.0 (IC base=+0.325)

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

- **PATRÓN** `drift_ventana_pct` |x|> `0.3486` → IC=+0.337 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3486 (IC base=+0.325)

- **PATRÓN** `elapsed_s` > `209.2` → IC=+0.400 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 209.2 (IC base=+0.325)

- **PATRÓN** `drift_15min` |x|≤ `2.2347` → IC=+0.348 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.2347 (IC base=+0.325)

- **PATRÓN** `drift_60min` |x|≤ `0.8028` → IC=+0.391 (n=90)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.8028 (IC base=+0.325)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.381 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.325)

- **PATRÓN** `ballena_activa_n` < `1105.0` → IC=+0.389 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1105.0 (IC base=+0.325)

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
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=1064)

### LIQUIDACIONES_15M#BNB#15min
- **PATRÓN** `liq_n` > `2.0` → IC=+0.204 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `liq_n` > 2.0 (IC base=+0.076)

- **PATRÓN** `liq_usd_total` > `1558.02` → IC=+0.223 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `liq_usd_total` > 1558.02 (IC base=+0.076)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.125 (n=78)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.03 (IC base=+0.076)

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
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=1045)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=1045)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=1357)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=1357)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=306)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=306)

- **FILTRO** `py_entrada` < `0.43` → IC=-0.132 (n=104)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=217)

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

### LIQUIDACIONES_DEPTH_FASE0#BTC#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.138 (n=332)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=823)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **FILTRO** `py_entrada` > `0.57` → IC=-0.124 (n=461)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.085 (n=555)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.150 (n=338)

  - _Acción_: Kelly boost +0.75€ cuando `py_entrada` < 0.5 (IC base=-0.010)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.131 (n=174)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=393)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.125 (n=590)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=640)

- **FILTRO** `py_entrada` > `0.58` → IC=-0.124 (n=370)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=440)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.129 (n=300)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=649)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.125 (n=652)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.073 (n=349)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.41` → IC=-0.161 (n=375)

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
- **FILTRO** `py_entrada` < `0.46` → IC=-0.175 (n=8325)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=26321)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.171 (n=8754)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=27163)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.194 (n=1549)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.114 (n=4887)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.144 (n=2139)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.094 (n=4226)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.137 (n=1649)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` > 1.0 (IC base=+0.040)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.133 (n=2975)

  - _Acción_: Kelly boost +0.66€ cuando `py_entrada` < 0.5 (IC base=+0.014)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` < `0.44` → IC=-0.174 (n=1158)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=3623)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.180 (n=1235)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=3805)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` > `0.62` → IC=-0.196 (n=1592)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.087 (n=4931)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.136 (n=1972)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` > 1.0 (IC base=+0.033)

- **PATRÓN** `libro_liquidez` > `1738.24` → IC=+0.121 (n=2183)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 1738.24 (IC base=+0.033)

### MOMENTUM_IBS_15M_BALLENA#ETH#15min
- **FILTRO** `py_entrada` > `0.575` → IC=-0.175 (n=1257)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=3867)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.485` → IC=-0.162 (n=1601)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=4860)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=2448)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.162 (n=772)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=2372)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.180 (n=973)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=3140)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=4092)

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
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=1106)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `py_entrada` < `0.395` → IC=-0.230 (n=72)

  - _Acción_: SKIP cuando `py_entrada` < 0.395
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=262)

- **FILTRO** `ibs_20min` < `0.1975` → IC=-0.223 (n=110)

  - _Acción_: SKIP cuando `ibs_20min` < 0.1975
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=224)

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
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=243)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.136 (n=23473)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.091 (n=53355)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.299 (n=18543)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=58285)

- **FILTRO** `ibs_7min` < `0.2143` → IC=-0.235 (n=19166)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2143
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=57662)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.153 (n=25920)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=50908)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.245 (n=23963)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=72193)

- **FILTRO** `ibs_7min` > `0.28` → IC=-0.182 (n=24014)

  - _Acción_: SKIP cuando `ibs_7min` > 0.28
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=72142)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.159 (n=3292)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=10468)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.319 (n=3398)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=10362)

- **FILTRO** `ibs_7min` < `0.7105` → IC=-0.253 (n=4539)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7105
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=9221)

- **FILTRO** `py_entrada` > `0.72` → IC=-0.279 (n=4029)

  - _Acción_: SKIP cuando `py_entrada` > 0.72
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=12590)

- **FILTRO** `ibs_7min` > `0.7714` → IC=-0.211 (n=4153)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7714
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=12466)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.264 (n=3089)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=9651)

- **FILTRO** `ibs_7min` < `0.7134` → IC=-0.211 (n=3185)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7134
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=9555)

- **FILTRO** `ballena_activa_n` > `156.0` → IC=-0.201 (n=3175)

  - _Acción_: SKIP cuando `ballena_activa_n` > 156.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=9565)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.267 (n=2977)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=10054)

- **FILTRO** `ibs_7min` > `0.2651` → IC=-0.192 (n=3257)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2651
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=9774)

- **FILTRO** `ballena_activa_n` > `152.0` → IC=-0.178 (n=3256)

  - _Acción_: SKIP cuando `ballena_activa_n` > 152.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=9775)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.167 (n=3146)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=10046)

- **FILTRO** `py_entrada` < `0.3` → IC=-0.324 (n=3139)

  - _Acción_: SKIP cuando `py_entrada` < 0.3
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=10053)

- **FILTRO** `ibs_7min` < `0.2892` → IC=-0.250 (n=4353)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2892
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=8839)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.202 (n=2559)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=10633)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.259 (n=4233)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=13373)

- **FILTRO** `ibs_7min` > `0.7248` → IC=-0.183 (n=4401)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7248
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=13205)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.264 (n=3084)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=9325)

- **FILTRO** `ibs_7min` < `0.7132` → IC=-0.200 (n=3102)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7132
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=9307)

- **FILTRO** `ballena_activa_n` > `24.0` → IC=-0.191 (n=3101)

  - _Acción_: SKIP cuando `ballena_activa_n` > 24.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=9308)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.259 (n=3003)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=9913)

- **FILTRO** `ibs_7min` > `0.2723` → IC=-0.179 (n=3228)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2723
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=9688)

- **FILTRO** `ballena_activa_n` > `23.0` → IC=-0.168 (n=3225)

  - _Acción_: SKIP cuando `ballena_activa_n` > 23.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=9691)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.32` → IC=-0.302 (n=2952)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=9324)

- **FILTRO** `ibs_7min` < `0.7` → IC=-0.237 (n=4041)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=8235)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.220 (n=3010)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=9266)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.199 (n=4471)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=14132)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.133 (n=4009)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.110 (n=8442)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.312 (n=3007)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=9444)

- **FILTRO** `ibs_7min` < `0.73` → IC=-0.224 (n=4099)

  - _Acción_: SKIP cuando `ibs_7min` < 0.73
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=8352)

- **FILTRO** `ballena_activa_n` > `9.0` → IC=-0.208 (n=2747)

  - _Acción_: SKIP cuando `ballena_activa_n` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.092 (n=9704)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.228 (n=4297)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=13084)

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

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.157 (n=298)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0045 (IC base=-0.045)

### PRICE_TARGET_GBM#ETH#atexpiry
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

- **FILTRO** `T_h` < `87.9918` → IC=-0.241 (n=404)

  - _Acción_: SKIP cuando `T_h` < 87.9918
  - _Potencial_: sin este filtro IC_bueno=-0.215 (n=405)

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

- **FILTRO** `pct_vs_K` |x|> `1.0451` → IC=-0.254 (n=197)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 1.0451
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=67)

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

- **FILTRO** `sigma_h` < `0.0087` → IC=-0.281 (n=39)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0087
  - _Potencial_: sin este filtro IC_bueno=-0.133 (n=118)

- **FILTRO** `pct_vs_K` |x|> `3.01` → IC=-0.427 (n=53)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.01
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=104)

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
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=1306)

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
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=5095)

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
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=2954)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0055` → IC=+0.184 (n=1889)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0055 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.2241` → IC=+0.158 (n=5669)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.2241 (IC base=+0.138)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3545` → IC=+0.145 (n=5313)

  - _Acción_: Kelly boost +0.72€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3545 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.144 (n=5989)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 4.0 (IC base=+0.138)

- **PATRÓN** `ibs_15` > `0.5714` → IC=+0.218 (n=5073)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5714 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` > `0.1371` → IC=+0.128 (n=2605)

  - _Acción_: Kelly boost +0.64€ cuando `dist_vwap_pct` > 0.1371 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.233` → IC=+0.240 (n=1070)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.233 (IC base=+0.138)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=3178)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `4463.6973` → IC=+0.171 (n=1889)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 4463.6973 (IC base=+0.138)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=2218)

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
- **PATRÓN** `ibs_15` > `0.7619` → IC=+0.130 (n=750)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.65€ cuando `ibs_15` > 0.7619 (IC base=+0.050)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` < `0.0193` → IC=+0.167 (n=959)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0193 (IC base=+0.150)

- **PATRÓN** `sigma_h` > `0.0126` → IC=+0.153 (n=1437)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` > 0.0126 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.2282` → IC=+0.178 (n=1438)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.2282 (IC base=+0.150)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0946` → IC=+0.209 (n=445)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0946 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.155 (n=1324)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 6.0 (IC base=+0.150)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.152 (n=1017)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 11.0 (IC base=+0.150)

- **PATRÓN** `ibs_15` > `0.5333` → IC=+0.221 (n=1288)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5333 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.2007` → IC=+0.169 (n=644)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.2007 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.665` → IC=+0.182 (n=328)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 17.665 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `2939.6834` → IC=+0.191 (n=652)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 2939.6834 (IC base=+0.150)

- **PATRÓN** `ibs_15` < `0.1136` → IC=+0.150 (n=1099)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.75€ cuando `ibs_15` < 0.1136 (IC base=+0.069)

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
- **FILTRO** `sigma_h` > `0.0075` → IC=-0.201 (n=2784)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0075
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=2785)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.221 (n=2366)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=3203)

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
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2325 (IC base=-0.002)

- **PATRÓN** `ibs_15` < `0.3704` → IC=+0.286 (n=5172)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3704 (IC base=-0.002)

- **PATRÓN** `dist_vwap_pct` > `0.6649` → IC=+0.285 (n=704)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6649 (IC base=-0.002)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0433` → IC=-0.226 (n=2399)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0433
  - _Potencial_: sin este filtro IC_bueno=-0.099 (n=1186)

- **FILTRO** `sigma_ewma_delta_pct` > `22.129` → IC=-0.248 (n=506)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 22.129
  - _Potencial_: sin este filtro IC_bueno=-0.173 (n=3079)

- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.149 (n=340)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0031 (IC base=+0.068)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2673` → IC=+0.287 (n=148)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2673 (IC base=+0.068)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1453` → IC=+0.267 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1453 (IC base=+0.068)

- **PATRÓN** `ibs_15` > `0.7639` → IC=+0.314 (n=444)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7639 (IC base=+0.068)

- **PATRÓN** `dist_vwap_pct` > `0.1041` → IC=+0.272 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1041 (IC base=+0.068)

- **PATRÓN** `dist_vwap_pct` < `0.2432` → IC=+0.274 (n=401)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2432 (IC base=+0.068)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.088` → IC=+0.149 (n=226)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 22.088 (IC base=+0.068)

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

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.255 (n=1350)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0062 (IC base=+0.244)

- **PATRÓN** `drift_60min` |x|≤ `0.3616` → IC=+0.247 (n=1781)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3616 (IC base=+0.244)

- **PATRÓN** `drift_15min` |x|≤ `0.7918` → IC=+0.257 (n=1781)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7918 (IC base=+0.244)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2094` → IC=+0.267 (n=919)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2094 (IC base=+0.244)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.257 (n=750)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.244)

- **PATRÓN** `ibs_15` < `0.3851` → IC=+0.273 (n=2024)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3851 (IC base=+0.244)

- **PATRÓN** `dist_vwap_pct` > `0.384` → IC=+0.276 (n=485)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.384 (IC base=+0.244)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.409` → IC=+0.251 (n=782)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.409 (IC base=+0.244)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.262` → IC=+0.249 (n=2122)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.262 (IC base=+0.244)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1882` → IC=-0.274 (n=326)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1882
  - _Potencial_: sin este filtro IC_bueno=-0.178 (n=981)

- **FILTRO** `sigma_h` > `0.0105` → IC=-0.240 (n=444)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0105
  - _Potencial_: sin este filtro IC_bueno=-0.183 (n=863)

- **FILTRO** `drift_60min` |x|> `0.1726` → IC=-0.271 (n=444)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1726
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=863)

- **FILTRO** `drift_15min` |x|> `0.9228` → IC=-0.293 (n=326)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.9228
  - _Potencial_: sin este filtro IC_bueno=-0.172 (n=981)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1478` → IC=+0.188 (n=46)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.94€ cuando `delta_ratio_macro` |x|> 0.1478 (IC base=-0.203)

- **PATRÓN** `ibs_15` > `0.9231` → IC=+0.380 (n=23)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9231 (IC base=-0.203)

- **PATRÓN** `dist_vwap_pct` < `0.1327` → IC=+0.167 (n=55)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.1327 (IC base=-0.203)

- **PATRÓN** `ibs_15` < `0.38` → IC=+0.298 (n=885)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.38 (IC base=-0.027)

- **PATRÓN** `dist_vwap_pct` > `0.7025` → IC=+0.243 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7025 (IC base=-0.027)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1176` → IC=-0.262 (n=793)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1176
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=795)

- **FILTRO** `drift_15min` |x|> `1.2727` → IC=-0.279 (n=396)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.2727
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=1192)

- **FILTRO** `sigma_ewma_delta_pct` > `7.447` → IC=-0.223 (n=486)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 7.447
  - _Potencial_: sin este filtro IC_bueno=-0.218 (n=1102)

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

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5714 sube el IC de +0.138 a +0.218 en UPDOWN_GBM#15min (n=5073). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7077 sube el IC de +0.202 a +0.272 en UPDOWN_GBM#BTC#15min (n=819). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.4915 sube el IC de +0.133 a +0.220 en UPDOWN_GBM#ETH#15min (n=1021). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5333 sube el IC de +0.150 a +0.221 en UPDOWN_GBM#XRP#15min (n=1288). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1136 sube el IC de +0.069 a +0.150 en UPDOWN_GBM#XRP#15min (n=1099). Ya aplicado como kelly_boost=+0.75€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6307 sube el IC de -0.085 a +0.275 en UPDOWN_GBM_15M_TARDIO (n=1255). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3704 sube el IC de -0.002 a +0.286 en UPDOWN_GBM_15M_TARDIO (n=5172). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7639 sube el IC de +0.068 a +0.314 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=444). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.6255 sube el IC de -0.184 a +0.289 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=74). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.5684 sube el IC de +0.146 a +0.239 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=627). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3851 sube el IC de +0.244 a +0.273 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=2024). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.9231 sube el IC de -0.203 a +0.380 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=23). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.38 sube el IC de -0.027 a +0.298 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=885). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
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
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 1183 | -0.016 | +78.98€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 1183 | -0.016 | +78.98€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE | 7 | +0.019 | +3.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE#15min | 7 | +0.019 | +3.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 898 | -0.033 | +58.05€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 898 | -0.033 | +58.05€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 193 | +0.064 | +24.17€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 193 | +0.064 | +24.17€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 85 | -0.017 | -6.49€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 85 | -0.017 | -6.49€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 48538 | -0.084 | -6257.78€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 3058 | +0.079 | -306.43€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 45480 | -0.095 | -5951.36€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4871 | -0.111 | -816.69€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4871 | -0.111 | -816.69€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 3058 | +0.079 | -306.43€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 3058 | +0.079 | -306.43€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 4932 | -0.103 | -939.80€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 4932 | -0.103 | -939.80€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 13305 | -0.042 | -1290.07€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 13305 | -0.042 | -1290.07€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 13226 | -0.112 | -1379.71€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 13226 | -0.112 | -1379.71€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 9146 | -0.135 | -1525.09€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 9146 | -0.135 | -1525.09€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 51174 | -0.012 | +2808.77€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 13211 | +0.004 | +1493.13€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 37963 | -0.018 | +1315.63€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 51174 | -0.012 | +2808.77€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 13211 | +0.004 | +1493.13€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 37963 | -0.018 | +1315.63€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 194567 | +0.113 | -8080.83€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#15min | 22188 | +0.180 | -695.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 894 | +0.015 | -72.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 160399 | +0.105 | -6906.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 11086 | +0.094 | -406.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 26581 | +0.103 | -1884.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 79 | -0.179 | +10.89€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 26487 | +0.104 | -1883.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 36737 | +0.124 | -622.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5625 | +0.178 | -235.00€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 26551 | +0.120 | -198.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 4519 | +0.080 | -167.37€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 26630 | +0.098 | -1934.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 90 | -0.109 | +14.44€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 26525 | +0.099 | -1937.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 41579 | +0.123 | -858.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 10425 | +0.179 | -248.24€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 26974 | +0.105 | -538.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 4168 | +0.103 | -63.25€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#SOL | 36429 | +0.111 | -1638.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 5877 | +0.198 | -253.25€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 797 | +0.041 | -18.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 27356 | +0.095 | -1191.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 2399 | +0.104 | -175.63€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO#XRP | 26611 | +0.107 | -1142.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 92 | -0.117 | +15.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 26506 | +0.108 | -1157.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 31567 | +0.191 | -2262.15€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 31567 | +0.191 | -2262.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 7150 | +0.166 | -772.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 7150 | +0.166 | -772.60€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 4613 | +0.195 | -184.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 4613 | +0.195 | -184.79€ | 3 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 7007 | +0.173 | -634.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 7007 | +0.173 | -634.40€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 5842 | +0.252 | -200.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 5842 | +0.252 | -200.87€ | 0 | 4 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 6876 | +0.184 | -483.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 6876 | +0.184 | -483.25€ | 0 | 3 |
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
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 111643 | +0.199 | -8314.88€ | 3 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 111643 | +0.199 | -8314.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 19324 | +0.177 | -2250.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 19324 | +0.177 | -2250.89€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 18002 | +0.223 | -618.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 18002 | +0.223 | -618.23€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 19166 | +0.180 | -2041.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 19166 | +0.180 | -2041.55€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 18150 | +0.217 | -731.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 18150 | +0.217 | -731.60€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 18425 | +0.203 | -1159.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 18425 | +0.203 | -1159.54€ | 1 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 18576 | +0.195 | -1513.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 18576 | +0.195 | -1513.06€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 43201 | +0.117 | +371.99€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 43201 | +0.117 | +371.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 21510 | +0.117 | +211.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 21510 | +0.117 | +211.00€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 21691 | +0.117 | +160.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 21691 | +0.117 | +160.99€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 2649 | +0.292 | -20.58€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 2649 | +0.292 | -20.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 1208 | +0.281 | -31.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 1208 | +0.281 | -31.30€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 1299 | +0.295 | +3.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 1299 | +0.295 | +3.99€ | 0 | 3 |
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
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 87736 | +0.100 | -2031.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 7087 | +0.097 | +165.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 80649 | +0.101 | -2196.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 47935 | +0.105 | -449.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 7087 | +0.097 | +165.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 40848 | +0.107 | -614.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 18718 | +0.109 | -83.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 18718 | +0.109 | -83.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 21083 | +0.081 | -1498.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 21083 | +0.081 | -1498.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 914 | +0.186 | -109.27€ | 5 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 914 | +0.186 | -109.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 914 | +0.186 | -109.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 914 | +0.186 | -109.27€ | 5 | 4 |
| ✅ GBM_LATE_15M | 59590 | +0.101 | +33426.87€ | 0 | 18 |
| ✅ GBM_LATE_15M#15min | 59590 | +0.101 | +33426.87€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 9864 | +0.226 | +8520.53€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 9864 | +0.226 | +8520.53€ | 0 | 21 |
| ✅ GBM_LATE_15M#BTC | 9187 | +0.177 | +7288.86€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 9187 | +0.177 | +7288.86€ | 0 | 21 |
| ✅ GBM_LATE_15M#DOGE | 10677 | +0.207 | +8455.47€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 10677 | +0.207 | +8455.47€ | 0 | 20 |
| ✅ GBM_LATE_15M#ETH | 7959 | +0.058 | +2609.52€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 7959 | +0.058 | +2609.52€ | 1 | 15 |
| ✅ GBM_LATE_15M#SOL | 8306 | -0.027 | +2192.52€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 8306 | -0.027 | +2192.52€ | 4 | 14 |
| ✅ GBM_LATE_15M#XRP | 13597 | -0.021 | +4359.97€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 13597 | -0.021 | +4359.97€ | 3 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 62997 | +0.086 | +36699.90€ | 0 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 62997 | +0.086 | +36699.90€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 12184 | -0.002 | +6496.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 12184 | -0.002 | +6496.93€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 13558 | +0.005 | +3656.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 13558 | +0.005 | +3656.08€ | 0 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 8540 | +0.295 | +9779.90€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 8540 | +0.295 | +9779.90€ | 0 | 22 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 12009 | +0.015 | +3780.00€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 12009 | +0.015 | +3780.00€ | 1 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 9645 | +0.045 | +4336.68€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 9645 | +0.045 | +4336.68€ | 3 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 7061 | +0.315 | +8650.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 7061 | +0.315 | +8650.32€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 47026 | +0.179 | +39007.20€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 47026 | +0.179 | +39007.20€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 7083 | +0.240 | +6610.27€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 7083 | +0.240 | +6610.27€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 7461 | +0.140 | +5561.48€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 7461 | +0.140 | +5561.48€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 7566 | +0.225 | +6581.86€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 7566 | +0.225 | +6581.86€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 8062 | +0.129 | +6241.89€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 8062 | +0.129 | +6241.89€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 8889 | +0.120 | +6750.59€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 8889 | +0.120 | +6750.59€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 7965 | +0.234 | +7261.10€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 7965 | +0.234 | +7261.10€ | 0 | 26 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 12901 | +0.126 | +6513.26€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 12901 | +0.126 | +6513.26€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 669 | +0.162 | +439.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 669 | +0.162 | +439.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 3456 | +0.126 | +1877.19€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 3456 | +0.126 | +1877.19€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 507 | +0.158 | +290.79€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 507 | +0.158 | +290.79€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 3713 | +0.124 | +1803.37€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 3713 | +0.124 | +1803.37€ | 0 | 17 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 3341 | +0.099 | +1333.41€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 3341 | +0.099 | +1333.41€ | 0 | 12 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 1215 | +0.169 | +768.67€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 1215 | +0.169 | +768.67€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO | 59782 | +0.189 | +49498.02€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#15min | 59782 | +0.189 | +49498.02€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 9432 | +0.250 | +9132.35€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 9432 | +0.250 | +9132.35€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 9545 | +0.140 | +6718.35€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 9545 | +0.140 | +6718.35€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 10147 | +0.235 | +9190.90€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 10147 | +0.235 | +9190.90€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 9899 | +0.143 | +7374.54€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 9899 | +0.143 | +7374.54€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 10586 | +0.125 | +7576.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 10586 | +0.125 | +7576.28€ | 0 | 18 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 10173 | +0.242 | +9505.60€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 10173 | +0.242 | +9505.60€ | 0 | 20 |
| ✅ GBM_LATE_5M | 15286 | +0.215 | +12656.38€ | 0 | 26 |
| ✅ GBM_LATE_5M#5min | 15286 | +0.215 | +12656.38€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 1542 | +0.246 | +1460.45€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 1542 | +0.246 | +1460.45€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 3286 | +0.211 | +2831.05€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 3286 | +0.211 | +2831.05€ | 0 | 25 |
| ✅ GBM_LATE_5M#DOGE | 1453 | +0.210 | +1160.11€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1453 | +0.210 | +1160.11€ | 0 | 19 |
| ✅ GBM_LATE_5M#ETH | 4348 | +0.205 | +3290.79€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 4348 | +0.205 | +3290.79€ | 0 | 26 |
| ✅ GBM_LATE_5M#SOL | 2641 | +0.224 | +2324.55€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 2641 | +0.224 | +2324.55€ | 0 | 23 |
| ✅ GBM_LATE_5M#XRP | 2016 | +0.209 | +1589.43€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 2016 | +0.209 | +1589.43€ | 0 | 0 |
| ✅ GBM_LATE_60M | 5349 | +0.054 | +1450.72€ | 0 | 6 |
| ✅ GBM_LATE_60M#60min | 5349 | +0.054 | +1450.72€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 1848 | +0.058 | +548.25€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 1848 | +0.058 | +548.25€ | 0 | 6 |
| ✅ GBM_LATE_60M#ETH | 1706 | +0.054 | +547.89€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 1706 | +0.054 | +547.89€ | 1 | 7 |
| ✅ GBM_LATE_60M#SOL | 1795 | +0.050 | +354.58€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 1795 | +0.050 | +354.58€ | 0 | 9 |
| 🚫 GBM_LATE_60M_FADE | 724 | -0.249 | -35.03€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 724 | -0.249 | -35.03€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 261 | -0.253 | -19.53€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 261 | -0.253 | -19.53€ | 5 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 262 | -0.242 | -6.68€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 262 | -0.242 | -6.68€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 201 | -0.249 | -8.83€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 201 | -0.249 | -8.83€ | 7 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 2200 | +0.084 | +552.78€ | 0 | 9 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 2200 | +0.084 | +552.78€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 849 | +0.070 | +191.06€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 849 | +0.070 | +191.06€ | 1 | 5 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 758 | +0.057 | +151.57€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 758 | +0.057 | +151.57€ | 2 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 593 | +0.137 | +210.15€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 593 | +0.137 | +210.15€ | 2 | 9 |
| ✅ LATE_WINDOW_5MIN | 288 | +0.300 | +331.84€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 288 | +0.300 | +331.84€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 288 | +0.300 | +331.84€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 288 | +0.300 | +331.84€ | 1 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 4459 | +0.096 | +1004.62€ | 0 | 1 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 4459 | +0.096 | +1004.62€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 4459 | +0.096 | +1004.62€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 4459 | +0.096 | +1004.62€ | 0 | 1 |
| ✅ LIQUIDACIONES_15M | 1357 | +0.010 | +55.07€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 1357 | +0.010 | +55.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 131 | +0.071 | +20.62€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 131 | +0.071 | +20.62€ | 0 | 3 |
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
| ✅ LIQUIDACIONES_60M | 2497 | -0.033 | -5.55€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 2497 | -0.033 | -5.55€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 759 | -0.030 | -10.31€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 759 | -0.030 | -10.31€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 892 | -0.011 | +18.79€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 892 | -0.011 | +18.79€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 846 | -0.058 | -14.03€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 846 | -0.058 | -14.03€ | 5 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 17244 | -0.033 | -209.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 8310 | -0.035 | -120.26€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 8934 | -0.031 | -89.20€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 613 | -0.058 | -40.55€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 314 | -0.038 | -5.91€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 299 | -0.078 | -34.64€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 4529 | -0.028 | -45.99€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 2154 | -0.025 | -1.87€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 2375 | -0.031 | -44.12€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 1651 | -0.032 | +1.53€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 840 | -0.042 | -19.15€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 811 | -0.021 | +20.68€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 3907 | -0.034 | -68.50€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 1867 | -0.032 | -23.36€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 2040 | -0.035 | -45.14€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 3312 | -0.023 | +47.73€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 1605 | -0.030 | -1.03€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 1707 | -0.016 | +48.77€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 3232 | -0.044 | -103.68€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 1530 | -0.052 | -68.94€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 1702 | -0.038 | -34.74€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 70563 | +0.000 | +3851.61€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 70563 | +0.000 | +3851.61€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 12801 | +0.027 | +1774.90€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 12801 | +0.027 | +1774.90€ | 2 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 9821 | -0.038 | -148.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 9821 | -0.038 | -148.70€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 12942 | +0.026 | +1466.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 12942 | +0.026 | +1466.00€ | 1 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 9788 | -0.052 | -246.15€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 9788 | -0.052 | -246.15€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 12042 | -0.004 | +345.14€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 12042 | -0.004 | +345.14€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 13169 | +0.019 | +660.41€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 13169 | +0.019 | +660.41€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 7258 | -0.053 | -108.19€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 7258 | -0.053 | -108.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1267 | -0.001 | -13.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1267 | -0.001 | -13.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 2014 | -0.060 | -19.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 2014 | -0.060 | -19.26€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 93 | -0.016 | +0.13€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 93 | -0.016 | +0.13€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 811 | -0.119 | -34.68€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 811 | -0.119 | -34.68€ | 5 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 2206 | -0.068 | -13.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 2206 | -0.068 | -13.17€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 867 | -0.018 | -27.44€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 867 | -0.018 | -27.44€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 172984 | -0.077 | +2357.55€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 172984 | -0.077 | +2357.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 30379 | -0.077 | +1735.65€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 30379 | -0.077 | +1735.65€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 25771 | -0.101 | -1226.83€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 25771 | -0.101 | -1226.83€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 30798 | -0.067 | +1526.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 30798 | -0.067 | +1526.98€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 25325 | -0.099 | -847.12€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 25325 | -0.099 | -847.12€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 30879 | -0.059 | +260.45€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 30879 | -0.059 | +260.45€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 29832 | -0.069 | +908.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 29832 | -0.069 | +908.42€ | 5 | 0 |
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
| ✅ ORDER_FLOW_5M_REACTIVO | 2289 | -0.017 | -16.66€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 2289 | -0.017 | -16.66€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 413 | +0.011 | +22.83€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 413 | +0.011 | +22.83€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 422 | -0.040 | -20.40€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 422 | -0.040 | -20.40€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 566 | -0.041 | -33.81€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 566 | -0.041 | -33.81€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 465 | +0.005 | +9.52€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 465 | +0.005 | +9.52€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 423 | -0.013 | +5.19€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 423 | -0.013 | +5.19€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 1204 | -0.052 | +49.46€ | 1 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 557 | -0.087 | -29.48€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 436 | -0.094 | -8.94€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 121 | -0.061 | -20.55€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 420 | -0.014 | +51.21€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 305 | +0.005 | +59.22€ | 0 | 2 |
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
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 447 | -0.215 | -43.96€ | 4 | 1 |
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
| ✅ STREAK_FADE_5M | 3603 | -0.023 | -143.28€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3603 | -0.023 | -143.28€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 1127 | -0.023 | -40.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 1127 | -0.023 | -40.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 619 | -0.028 | -27.08€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 619 | -0.028 | -27.08€ | 1 | 0 |
| ✅ STREAK_FADE_5M#SOL | 173 | -0.043 | -14.79€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 173 | -0.043 | -14.79€ | 4 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1684 | -0.020 | -61.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1684 | -0.020 | -61.20€ | 2 | 0 |
| ✅ STREAK_FADE_60M | 123 | -0.044 | -13.49€ | 3 | 0 |
| ✅ STREAK_FADE_60M#60min | 123 | -0.044 | -13.49€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 45 | -0.074 | -4.16€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 45 | -0.074 | -4.16€ | 4 | 0 |
| ✅ STREAK_FADE_60M#SOL | 78 | -0.025 | -9.34€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 78 | -0.025 | -9.34€ | 0 | 1 |
| ✅ STREAK_MOM_5M | 11569 | +0.014 | +73.36€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 11569 | +0.014 | +73.36€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2995 | +0.018 | +24.38€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2995 | +0.018 | +24.38€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 3048 | +0.016 | +32.71€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 3048 | +0.016 | +32.71€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2934 | +0.009 | -2.53€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2934 | +0.009 | -2.53€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2592 | +0.014 | +18.80€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2592 | +0.014 | +18.80€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 12434 | +0.018 | -0.05€ | 4 | 0 |
| ✅ STRUCT_NO_15M#15min | 12434 | +0.018 | -0.05€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 5114 | +0.021 | +4.88€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 5114 | +0.021 | +4.88€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 4332 | +0.018 | -1.42€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 4332 | +0.018 | -1.42€ | 4 | 0 |
| ✅ STRUCT_NO_15M#SOL | 2988 | +0.014 | -3.50€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 2988 | +0.014 | -3.50€ | 1 | 0 |
| ✅ UPDOWN_GBM | 112591 | +0.060 | +10694.75€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 27437 | +0.078 | +5461.00€ | 0 | 9 |
| ✅ UPDOWN_GBM#240min | 3274 | -0.001 | +34.51€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 74794 | +0.062 | +5091.52€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 6703 | -0.003 | +116.71€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 9611 | +0.103 | +1730.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1782 | +0.163 | +818.90€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 90 | -0.011 | -2.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 7739 | +0.091 | +913.94€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 25576 | +0.058 | +2277.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 3683 | +0.080 | +828.19€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 942 | -0.001 | +18.80€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 17828 | +0.068 | +1352.51€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 2984 | -0.005 | +75.35€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 139 | -0.067 | +2.53€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 12314 | +0.076 | +1347.37€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1763 | +0.154 | +737.64€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 86 | +0.023 | -0.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 10465 | +0.063 | +610.60€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 26592 | +0.050 | +1880.78€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 6464 | +0.072 | +998.95€ | 0 | 8 |
| ✅ UPDOWN_GBM#ETH#240min | 912 | +0.004 | +15.51€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 16616 | +0.052 | +825.53€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 2472 | +0.000 | +40.30€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 128 | -0.108 | +0.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 23742 | +0.040 | +1337.72€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 7435 | +0.032 | +445.80€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#240min | 847 | -0.011 | +4.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 14099 | +0.052 | +896.35€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 1247 | -0.002 | +1.05€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#daily | 114 | -0.147 | -10.16€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 14754 | +0.074 | +2122.50€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 6310 | +0.093 | +1631.53€ | 0 | 11 |
| ✅ UPDOWN_GBM#XRP#240min | 397 | +0.006 | -1.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 8047 | +0.062 | +492.58€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 381 | -0.106 | -7.15€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 1015 | +0.364 | +377.14€ | 0 | 10 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 1015 | +0.364 | +377.14€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 491 | +0.362 | +172.01€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 491 | +0.362 | +172.01€ | 0 | 10 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 524 | +0.365 | +205.13€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 524 | +0.365 | +205.13€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO | 26515 | -0.019 | +6649.19€ | 2 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 26515 | -0.019 | +6649.19€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1981 | -0.051 | +561.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1981 | -0.051 | +561.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 4943 | -0.115 | +283.96€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 4943 | -0.115 | +283.96€ | 2 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 1072 | +0.223 | +901.85€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 1072 | +0.223 | +901.85€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 3534 | +0.221 | +2279.41€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 3534 | +0.221 | +2279.41€ | 1 | 20 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 7550 | -0.058 | +1135.74€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 7550 | -0.058 | +1135.74€ | 4 | 5 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 7435 | -0.056 | +1487.07€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 7435 | -0.056 | +1487.07€ | 4 | 6 |
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