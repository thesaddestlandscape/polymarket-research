# Hipótesis automáticas — 2026-11-15 13:14 UTC
_Generado por shadow_postmortem.py sobre 1348285 resoluciones (PNL=+187030.44€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.5` → IC=-0.317 (n=195)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.116 (n=720)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.196 (n=1026)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` > 0.505 (IC base=+0.122)

- **PATRÓN** `n_total_lado` > `62.0` → IC=+0.183 (n=326)

  - _Acción_: Kelly boost +0.91€ cuando `n_total_lado` > 62.0 (IC base=+0.122)

- **PATRÓN** `banda_hit_calibrado` > `0.8128` → IC=+0.275 (n=442)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8128 (IC base=+0.122)

- **PATRÓN** `banda_z` > `8.477` → IC=+0.194 (n=325)

  - _Acción_: Kelly boost +0.97€ cuando `banda_z` > 8.477 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.129 (n=877)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 8.0 (IC base=+0.122)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.123 (n=701)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 12.0 (IC base=+0.122)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.136 (n=1062)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.122)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.302 (n=165)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.113 (n=515)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.193 (n=891)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.505 (IC base=+0.124)

- **PATRÓN** `n_total_lado` > `45.0` → IC=+0.161 (n=571)

  - _Acción_: Kelly boost +0.81€ cuando `n_total_lado` > 45.0 (IC base=+0.124)

- **PATRÓN** `banda_hit_calibrado` > `0.8125` → IC=+0.273 (n=382)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8125 (IC base=+0.124)

- **PATRÓN** `banda_z` > `8.77` → IC=+0.207 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 8.77 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.134 (n=763)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 8.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.124 (n=599)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 12.0 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.132 (n=962)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.01 (IC base=+0.124)

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
- **FILTRO** `restante_s_al_confirmar` < `131.7` → IC=-0.217 (n=12196)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 131.7
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=36594)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `125.06` → IC=-0.256 (n=1221)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 125.06
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=3664)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `115.59` → IC=-0.277 (n=1240)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 115.59
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=3722)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `restante_s_al_confirmar` < `116.17` → IC=-0.166 (n=3344)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 116.17
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=10037)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `152.1` → IC=-0.238 (n=3322)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 152.1
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=9969)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `128.04` → IC=-0.267 (n=2299)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 128.04
  - _Potencial_: sin este filtro IC_bueno=-0.092 (n=6897)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.209 (n=28670)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.103)

- **PATRÓN** `libro_liquidez` > `8157.6321` → IC=+0.156 (n=2367)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 8157.6321 (IC base=+0.103)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.128 (n=24810)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 17.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.130 (n=30265)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.124)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.224 (n=22675)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.140 (n=8472)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `6438.3421` → IC=+0.143 (n=3286)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 6438.3421 (IC base=+0.124)

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
- **PATRÓN** `py_entrada` > `0.61` → IC=+0.168 (n=628)

  - _Acción_: Kelly boost +0.84€ cuando `py_entrada` > 0.61 (IC base=+0.075)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.148 (n=1472)

  - _Acción_: Kelly boost +0.74€ cuando `py_entrada` < 0.44 (IC base=+0.086)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.170 (n=5194)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 6.0 (IC base=+0.167)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.171 (n=4628)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 15.0 (IC base=+0.167)

- **PATRÓN** `py_entrada` > `0.77` → IC=+0.375 (n=1806)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.77 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.207 (n=2481)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` < `0.275` → IC=+0.332 (n=960)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.275 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.204 (n=2893)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.200)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.142 (n=663)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 15.0 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.143 (n=1199)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 15.0 (IC base=+0.139)

- **PATRÓN** `py_entrada` > `0.675` → IC=+0.257 (n=458)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.675 (IC base=+0.139)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.141 (n=1138)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.156 (n=155)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.075)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.249 (n=964)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.227)

- **PATRÓN** `py_entrada` > `0.83` → IC=+0.420 (n=1346)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.83 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.145 (n=1438)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 7.0 (IC base=+0.145)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.156 (n=740)
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
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 17.0 (IC base=+0.124)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.253 (n=452)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.124)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.755` → IC=-0.299 (n=152)

  - _Acción_: SKIP cuando `py_entrada` > 0.755
  - _Potencial_: sin este filtro IC_bueno=-0.171 (n=77)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.200 (n=24901)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.194)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.196 (n=21047)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 15.0 (IC base=+0.194)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.228 (n=7879)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.194)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.338 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.194)

- **PATRÓN** `libro_liquidez` > `4915.142` → IC=+0.338 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4915.142 (IC base=+0.194)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.172 (n=5680)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 5.0 (IC base=+0.167)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.167 (n=5660)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` < 18.0 (IC base=+0.167)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.178 (n=5620)

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

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.212 (n=3412)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.207)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.213 (n=2277)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.207)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.247 (n=1681)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.207)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.182 (n=5549)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 5.0 (IC base=+0.174)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.176 (n=4710)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 15.0 (IC base=+0.174)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.175 (n=5692)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` < 0.73 (IC base=+0.174)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.183 (n=4353)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` > 0.71 (IC base=+0.174)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.257 (n=4401)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.251)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.253 (n=3928)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.251)

- **PATRÓN** `py_entrada` > `0.8` → IC=+0.364 (n=1492)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.189 (n=5433)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.185)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.191 (n=3455)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 11.0 (IC base=+0.185)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.192 (n=4032)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.71 (IC base=+0.185)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.430 (n=986)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.425)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.427 (n=982)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.425)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.437 (n=995)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.425)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.431 (n=1058)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.425)

- **PATRÓN** `libro_liquidez` > `4632.9843` → IC=+0.442 (n=637)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4632.9843 (IC base=+0.425)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.440 (n=399)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.440)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.442 (n=412)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.440)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.448 (n=441)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.440)

- **PATRÓN** `libro_liquidez` > `12497.2329` → IC=+0.444 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12497.2329 (IC base=+0.440)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.432 (n=393)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.423)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.426 (n=391)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.423)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.440 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.423)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.428 (n=445)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.423)

- **PATRÓN** `libro_liquidez` > `4792.7768` → IC=+0.424 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4792.7768 (IC base=+0.423)

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
- **FILTRO** `py_entrada` > `0.765` → IC=-0.306 (n=34)

  - _Acción_: SKIP cuando `py_entrada` > 0.765
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=19)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.244 (n=37)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.205 (n=32580)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.239 (n=32681)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.199)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.186 (n=4873)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 18.0 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.178 (n=10472)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 12.0 (IC base=+0.177)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.205 (n=6954)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.177)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.225 (n=13630)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.223)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.286 (n=4554)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.223)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.183 (n=13661)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 7.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.198 (n=11573)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` > 0.72 (IC base=+0.180)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.855` → IC=-0.357 (n=19)

  - _Acción_: SKIP cuando `py_entrada` < 0.855
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.228 (n=4562)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.220 (n=5247)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.218)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.253 (n=7513)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.218)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **FILTRO** `py_entrada` < `0.775` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **FILTRO** `libro_liquidez` < `3197.0694` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `libro_liquidez` < 3197.0694
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.207 (n=12402)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.204)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.256 (n=4718)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.204)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.202 (n=5423)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.198 (n=5417)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 6.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.245 (n=5585)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.196)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.194 (n=11751)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.140 (n=12502)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.96 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `3.41` → IC=+0.138 (n=14354)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 3.41 (IC base=+0.116)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.193 (n=5732)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.143 (n=5654)

  - _Acción_: Kelly boost +0.72€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `2.54` → IC=+0.143 (n=5413)

  - _Acción_: Kelly boost +0.71€ cuando `lag_apertura_s` < 2.54 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.194 (n=6019)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.137 (n=7589)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.95 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `3.08` → IC=+0.137 (n=7204)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 3.08 (IC base=+0.116)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.305 (n=1425)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.292)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.388 (n=737)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.292)

- **PATRÓN** `libro_liquidez` > `3990.1291` → IC=+0.293 (n=906)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3990.1291 (IC base=+0.292)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.286 (n=959)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.281)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.368 (n=317)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.281)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.314 (n=696)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.295)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.300 (n=1021)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.295)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.393 (n=352)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.441 (n=973)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.437)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.444 (n=936)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.437)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.439 (n=453)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.434)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.438 (n=319)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.434)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.432 (n=471)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.434)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.438 (n=466)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.434)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.449 (n=312)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.441)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.440 (n=396)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.441)

- **PATRÓN** `py_entrada` > `0.91` → IC=+0.444 (n=464)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.91 (IC base=+0.441)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.440 (n=379)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.441)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4899` → IC=+0.139 (n=18519)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.4899 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.128 (n=18721)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 6.0 (IC base=+0.123)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.126 (n=12939)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 12.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` > `0.9762` → IC=+0.247 (n=6174)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9762 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` > `0.8217` → IC=+0.287 (n=999)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8217 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.488` → IC=+0.189 (n=9283)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 3.488 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` > `0.6958` → IC=+0.269 (n=5000)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6958 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` > `0.3044` → IC=+0.252 (n=1910)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3044 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` > `2.7474` → IC=+0.234 (n=4454)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7474 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.137 (n=9116)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `4723.5886` → IC=+0.150 (n=6173)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 4723.5886 (IC base=+0.123)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.123 (n=11655)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0063 (IC base=+0.086)

- **PATRÓN** `ibs_20min` < `0.5643` → IC=+0.145 (n=23288)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.5643 (IC base=+0.086)

- **PATRÓN** `dist_vwap_pct` > `0.6413` → IC=+0.192 (n=1534)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.6413 (IC base=+0.086)

- **PATRÓN** `volumen_regimen` < `0.8576` → IC=+0.195 (n=6395)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` < 0.8576 (IC base=+0.086)

- **PATRÓN** `volumen_pendiente_norm` > `0.2961` → IC=+0.236 (n=2342)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2961 (IC base=+0.086)

- **PATRÓN** `volumen_spike_ratio` > `2.6666` → IC=+0.215 (n=5425)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6666 (IC base=+0.086)

- **PATRÓN** `ballena_activa_n` < `99.0` → IC=+0.230 (n=16187)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 99.0 (IC base=+0.086)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.248 (n=1314)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0107 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.3743` → IC=+0.213 (n=3938)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3743 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.227 (n=1905)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.210)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.211 (n=2649)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `0.9844` → IC=+0.278 (n=1785)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9844 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.81` → IC=+0.294 (n=927)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.81 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.2346` → IC=+0.258 (n=695)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2346 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `1.4411` → IC=+0.212 (n=3777)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4411 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.223 (n=4380)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.210)

- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.222 (n=3596)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 25.0 (IC base=+0.210)

- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.250 (n=1592)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0094 (IC base=+0.242)

- **PATRÓN** `drift_60min` |x|≤ `0.0921` → IC=+0.276 (n=1172)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0921 (IC base=+0.242)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.247 (n=1310)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.242)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.249 (n=1619)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.242)

- **PATRÓN** `ibs_20min` < `0.4805` → IC=+0.260 (n=3091)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4805 (IC base=+0.242)

- **PATRÓN** `volumen_pendiente_norm` < `0.0718` → IC=+0.245 (n=3027)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0718 (IC base=+0.242)

- **PATRÓN** `volumen_pendiente_norm` > `0.2911` → IC=+0.251 (n=471)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2911 (IC base=+0.242)

- **PATRÓN** `volumen_spike_ratio` < `1.4485` → IC=+0.242 (n=1120)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4485 (IC base=+0.242)

- **PATRÓN** `volumen_spike_ratio` > `1.8623` → IC=+0.246 (n=2239)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8623 (IC base=+0.242)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.243 (n=4075)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.242)

- **PATRÓN** `libro_liquidez` > `1778.837` → IC=+0.246 (n=2341)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1778.837 (IC base=+0.242)

- **PATRÓN** `ballena_activa_n` < `6.0` → IC=+0.244 (n=1212)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 6.0 (IC base=+0.242)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.236 (n=1117)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.224)

- **PATRÓN** `drift_60min` |x|≤ `0.1118` → IC=+0.248 (n=1468)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1118 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.236 (n=3493)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.225 (n=2383)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` > `0.8988` → IC=+0.257 (n=1112)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8988 (IC base=+0.224)

- **PATRÓN** `dist_vwap_pct` > `0.1888` → IC=+0.233 (n=1463)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1888 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.817` → IC=+0.265 (n=487)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.817 (IC base=+0.224)

- **PATRÓN** `volumen_regimen` > `0.6975` → IC=+0.232 (n=2979)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6975 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` > `0.2783` → IC=+0.270 (n=459)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2783 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` > `2.4452` → IC=+0.250 (n=1098)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4452 (IC base=+0.224)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.154 (n=3612)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0066 (IC base=+0.134)

- **PATRÓN** `drift_60min` |x|≤ `0.0793` → IC=+0.158 (n=1204)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.0793 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.155 (n=1348)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 17.0 (IC base=+0.134)

- **PATRÓN** `ibs_20min` < `0.7059` → IC=+0.172 (n=3610)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.7059 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.995` → IC=+0.141 (n=3300)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 3.995 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` < `0.6267` → IC=+0.154 (n=1204)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.6267 (IC base=+0.134)

- **PATRÓN** `volumen_pendiente_norm` > `0.0724` → IC=+0.157 (n=1470)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` > 0.0724 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` < `2.4413` → IC=+0.143 (n=3481)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.4413 (IC base=+0.134)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.134 (n=4690)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.134)

- **PATRÓN** `ballena_activa_n` < `172.0` → IC=+0.190 (n=1140)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 172.0 (IC base=+0.134)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0129` → IC=+0.211 (n=1396)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0129 (IC base=+0.194)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.202 (n=4386)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.194)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.258 (n=1618)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.194)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.987` → IC=+0.284 (n=920)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.987 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` < `0.0975` → IC=+0.196 (n=3745)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` < 0.0975 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` > `0.3519` → IC=+0.225 (n=539)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3519 (IC base=+0.194)

- **PATRÓN** `volumen_spike_ratio` > `2.7274` → IC=+0.211 (n=1851)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7274 (IC base=+0.194)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.198 (n=5060)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.04 (IC base=+0.194)

- **PATRÓN** `libro_liquidez` > `2003.6763` → IC=+0.204 (n=1392)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2003.6763 (IC base=+0.194)

- **PATRÓN** `sigma_h` < `0.0112` → IC=+0.225 (n=3420)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0112 (IC base=+0.222)

- **PATRÓN** `drift_60min` |x|≤ `0.1785` → IC=+0.235 (n=1709)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1785 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.244 (n=1473)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.228 (n=1765)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` < `0.0476` → IC=+0.273 (n=1299)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0476 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.771` → IC=+0.264 (n=422)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.771 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` > `0.3467` → IC=+0.258 (n=565)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3467 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` > `2.1568` → IC=+0.232 (n=2494)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1568 (IC base=+0.222)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.224 (n=1933)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.222)

- **PATRÓN** `libro_liquidez` > `1982.1984` → IC=+0.226 (n=1294)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1982.1984 (IC base=+0.222)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.227 (n=3693)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 23.0 (IC base=+0.222)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.174 (n=216)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.066 (n=5056)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.147 (n=687)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0039 (IC base=+0.063)

- **PATRÓN** `ibs_20min` > `0.9422` → IC=+0.237 (n=686)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9422 (IC base=+0.063)

- **PATRÓN** `dist_vwap_pct` > `0.146` → IC=+0.343 (n=469)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.146 (IC base=+0.063)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.122` → IC=+0.209 (n=1505)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.122 (IC base=+0.063)

- **PATRÓN** `volumen_regimen` > `1.2486` → IC=+0.359 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2486 (IC base=+0.063)

- **PATRÓN** `volumen_pendiente_norm` < `0.1677` → IC=+0.343 (n=666)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1677 (IC base=+0.063)

- **PATRÓN** `volumen_pendiente_norm` > `0.3061` → IC=+0.344 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3061 (IC base=+0.063)

- **PATRÓN** `volumen_spike_ratio` < `1.5524` → IC=+0.354 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5524 (IC base=+0.063)

- **PATRÓN** `volumen_spike_ratio` > `2.2934` → IC=+0.344 (n=364)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2934 (IC base=+0.063)

- **PATRÓN** `ballena_activa_n` < `142.0` → IC=+0.344 (n=816)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 142.0 (IC base=+0.063)

- **PATRÓN** `ibs_20min` < `0.087` → IC=+0.185 (n=1319)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.087 (IC base=+0.056)

- **PATRÓN** `dist_vwap_pct` > `0.5497` → IC=+0.168 (n=435)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.5497 (IC base=+0.056)

- **PATRÓN** `volumen_regimen` < `1.0014` → IC=+0.161 (n=2241)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.0014 (IC base=+0.056)

- **PATRÓN** `volumen_pendiente_norm` > `0.2799` → IC=+0.211 (n=323)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2799 (IC base=+0.056)

- **PATRÓN** `volumen_spike_ratio` > `1.5064` → IC=+0.162 (n=2191)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.5064 (IC base=+0.056)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.182 (n=149)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=803)

- **FILTRO** `ibs_20min` < `0.2667` → IC=-0.174 (n=237)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2667
  - _Potencial_: sin este filtro IC_bueno=+0.089 (n=715)

- **FILTRO** `ibs_20min` > `0.2` → IC=-0.130 (n=4914)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2
  - _Potencial_: sin este filtro IC_bueno=+0.155 (n=2483)

- **FILTRO** `sigma_ewma_delta_pct` > `8.306` → IC=-0.232 (n=799)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.306
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=6598)

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

- **PATRÓN** `ibs_20min` < `0.2` → IC=+0.155 (n=2483)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.2 (IC base=-0.034)

- **PATRÓN** `volumen_regimen` < `0.6968` → IC=+0.291 (n=487)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6968 (IC base=-0.034)

- **PATRÓN** `volumen_regimen` > `1.0468` → IC=+0.286 (n=502)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0468 (IC base=-0.034)

- **PATRÓN** `volumen_pendiente_norm` > `0.0781` → IC=+0.309 (n=502)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0781 (IC base=-0.034)

- **PATRÓN** `volumen_spike_ratio` < `2.4493` → IC=+0.294 (n=1038)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4493 (IC base=-0.034)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `ibs_20min` < `0.7922` → IC=-0.157 (n=3787)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7922
  - _Potencial_: sin este filtro IC_bueno=+0.137 (n=1951)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.174 (n=1203)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=4535)

- **FILTRO** `ibs_20min` > `0.7352` → IC=-0.190 (n=1986)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7352
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=5959)

- **PATRÓN** `ibs_20min` > `0.7922` → IC=+0.137 (n=1951)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` > 0.7922 (IC base=-0.057)

- **PATRÓN** `dist_vwap_pct` > `1.0349` → IC=+0.347 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0349 (IC base=-0.057)

- **PATRÓN** `volumen_regimen` > `0.7065` → IC=+0.318 (n=1024)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7065 (IC base=-0.057)

- **PATRÓN** `volumen_pendiente_norm` < `0.108` → IC=+0.302 (n=1094)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.108 (IC base=-0.057)

- **PATRÓN** `volumen_pendiente_norm` > `0.1706` → IC=+0.302 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1706 (IC base=-0.057)

- **PATRÓN** `volumen_spike_ratio` < `1.5853` → IC=+0.307 (n=495)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5853 (IC base=-0.057)

- **PATRÓN** `volumen_spike_ratio` > `2.516` → IC=+0.312 (n=375)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.516 (IC base=-0.057)

- **PATRÓN** `dist_vwap_pct` > `1.0731` → IC=+0.286 (n=269)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0731 (IC base=+0.006)

- **PATRÓN** `volumen_regimen` < `0.6408` → IC=+0.273 (n=777)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6408 (IC base=+0.006)

- **PATRÓN** `volumen_regimen` > `1.2033` → IC=+0.288 (n=777)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2033 (IC base=+0.006)

- **PATRÓN** `volumen_pendiente_norm` > `0.2843` → IC=+0.290 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2843 (IC base=+0.006)

- **PATRÓN** `volumen_spike_ratio` < `2.47` → IC=+0.265 (n=2205)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.47 (IC base=+0.006)

- **PATRÓN** `volumen_spike_ratio` > `1.434` → IC=+0.272 (n=2205)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.434 (IC base=+0.006)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0109` → IC=+0.193 (n=8057)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` > 0.0109 (IC base=+0.087)

- **PATRÓN** `ibs_20min` > `0.866` → IC=+0.285 (n=10950)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.866 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` > `0.9554` → IC=+0.300 (n=1661)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9554 (IC base=+0.087)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.475` → IC=+0.168 (n=10831)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 3.475 (IC base=+0.087)

- **PATRÓN** `volumen_regimen` > `0.6924` → IC=+0.279 (n=7978)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6924 (IC base=+0.087)

- **PATRÓN** `volumen_pendiente_norm` > `0.2928` → IC=+0.297 (n=1996)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2928 (IC base=+0.087)

- **PATRÓN** `volumen_spike_ratio` > `2.6413` → IC=+0.286 (n=4673)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6413 (IC base=+0.087)

- **PATRÓN** `ballena_activa_n` < `89.0` → IC=+0.309 (n=13643)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 89.0 (IC base=+0.087)

- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.161 (n=7810)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0104 (IC base=+0.085)

- **PATRÓN** `ibs_20min` < `0.5185` → IC=+0.172 (n=20623)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.5185 (IC base=+0.085)

- **PATRÓN** `volumen_regimen` < `0.6964` → IC=+0.279 (n=3460)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6964 (IC base=+0.085)

- **PATRÓN** `volumen_regimen` > `1.1866` → IC=+0.286 (n=2621)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1866 (IC base=+0.085)

- **PATRÓN** `volumen_pendiente_norm` > `0.2947` → IC=+0.329 (n=1741)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2947 (IC base=+0.085)

- **PATRÓN** `volumen_spike_ratio` < `1.4527` → IC=+0.305 (n=3883)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4527 (IC base=+0.085)

- **PATRÓN** `volumen_spike_ratio` > `2.2774` → IC=+0.305 (n=5280)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2774 (IC base=+0.085)

- **PATRÓN** `ballena_activa_n` < `72.0` → IC=+0.311 (n=11639)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 72.0 (IC base=+0.085)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.8036` → IC=-0.138 (n=4290)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8036
  - _Potencial_: sin este filtro IC_bueno=+0.304 (n=2211)

- **FILTRO** `ibs_20min` > `0.71` → IC=-0.239 (n=1441)

  - _Acción_: SKIP cuando `ibs_20min` > 0.71
  - _Potencial_: sin este filtro IC_bueno=+0.055 (n=4335)

- **FILTRO** `sigma_ewma_delta_pct` > `4.08` → IC=-0.238 (n=1237)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.08
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=4539)

- **PATRÓN** `ibs_20min` > `0.8036` → IC=+0.304 (n=2211)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8036 (IC base=+0.013)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.97` → IC=+0.188 (n=2163)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 2.97 (IC base=+0.013)

- **PATRÓN** `volumen_pendiente_norm` > `0.2292` → IC=+0.334 (n=413)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2292 (IC base=+0.013)

- **PATRÓN** `volumen_spike_ratio` < `1.4491` → IC=+0.283 (n=685)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4491 (IC base=+0.013)

- **PATRÓN** `volumen_spike_ratio` > `2.242` → IC=+0.307 (n=931)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.242 (IC base=+0.013)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.306 (n=2066)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 27.0 (IC base=+0.013)

- **PATRÓN** `ibs_20min` < `0.1726` → IC=+0.172 (n=1445)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.1726 (IC base=-0.018)

- **PATRÓN** `volumen_pendiente_norm` < `0.1515` → IC=+0.394 (n=1194)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1515 (IC base=-0.018)

- **PATRÓN** `volumen_spike_ratio` < `1.4257` → IC=+0.417 (n=383)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4257 (IC base=-0.018)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.389 (n=1187)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 22.0 (IC base=-0.018)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.6575` → IC=+0.232 (n=412)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6575 (IC base=+0.010)

- **PATRÓN** `volumen_regimen` > `0.6949` → IC=+0.221 (n=2113)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6949 (IC base=+0.010)

- **PATRÓN** `volumen_pendiente_norm` > `0.2748` → IC=+0.245 (n=316)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2748 (IC base=+0.010)

- **PATRÓN** `volumen_spike_ratio` < `1.4161` → IC=+0.231 (n=779)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4161 (IC base=+0.010)

- **PATRÓN** `volumen_spike_ratio` > `2.4647` → IC=+0.213 (n=779)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4647 (IC base=+0.010)

- **PATRÓN** `ballena_activa_n` < `375.0` → IC=+0.230 (n=2333)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 375.0 (IC base=+0.010)

- **PATRÓN** `volumen_regimen` < `0.6785` → IC=+0.252 (n=752)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6785 (IC base=+0.001)

- **PATRÓN** `volumen_regimen` > `1.0128` → IC=+0.268 (n=774)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0128 (IC base=+0.001)

- **PATRÓN** `volumen_pendiente_norm` > `0.2707` → IC=+0.308 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2707 (IC base=+0.001)

- **PATRÓN** `volumen_spike_ratio` < `1.5262` → IC=+0.263 (n=727)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5262 (IC base=+0.001)

- **PATRÓN** `volumen_spike_ratio` > `2.1506` → IC=+0.265 (n=750)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1506 (IC base=+0.001)

- **PATRÓN** `ballena_activa_n` < `202.0` → IC=+0.279 (n=732)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 202.0 (IC base=+0.001)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0114` → IC=+0.322 (n=1523)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0114 (IC base=+0.284)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.294 (n=3359)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.284)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.326 (n=1812)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.284)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.588` → IC=+0.306 (n=2265)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.588 (IC base=+0.284)

- **PATRÓN** `volumen_pendiente_norm` < `0.0976` → IC=+0.296 (n=2953)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0976 (IC base=+0.284)

- **PATRÓN** `volumen_spike_ratio` > `1.6016` → IC=+0.290 (n=3265)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6016 (IC base=+0.284)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.292 (n=4040)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.284)

- **PATRÓN** `libro_liquidez` > `2006.0984` → IC=+0.295 (n=1120)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2006.0984 (IC base=+0.284)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.304 (n=2072)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 14.0 (IC base=+0.284)

- **PATRÓN** `sigma_h` > `0.0091` → IC=+0.334 (n=2059)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0091 (IC base=+0.307)

- **PATRÓN** `drift_60min` |x|≤ `0.1812` → IC=+0.324 (n=1360)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1812 (IC base=+0.307)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.327 (n=1185)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.307)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.310 (n=1402)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.307)

- **PATRÓN** `ibs_20min` > `0.1489` → IC=+0.318 (n=2059)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1489 (IC base=+0.307)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.119` → IC=+0.314 (n=368)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.119 (IC base=+0.307)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.425` → IC=+0.307 (n=3198)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.425 (IC base=+0.307)

- **PATRÓN** `volumen_pendiente_norm` < `0.1989` → IC=+0.307 (n=3057)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1989 (IC base=+0.307)

- **PATRÓN** `volumen_pendiente_norm` > `0.3446` → IC=+0.318 (n=504)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3446 (IC base=+0.307)

- **PATRÓN** `volumen_spike_ratio` > `2.7444` → IC=+0.322 (n=1354)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7444 (IC base=+0.307)

- **PATRÓN** `libro_liquidez` > `1982.0392` → IC=+0.314 (n=1030)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1982.0392 (IC base=+0.307)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.312 (n=2637)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 22.0 (IC base=+0.307)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7163` → IC=-0.181 (n=1523)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7163
  - _Potencial_: sin este filtro IC_bueno=+0.072 (n=4572)

- **PATRÓN** `dist_vwap_pct` > `0.1481` → IC=+0.234 (n=1088)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1481 (IC base=+0.022)

- **PATRÓN** `dist_vwap_pct` < `0.2145` → IC=+0.234 (n=1932)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2145 (IC base=+0.022)

- **PATRÓN** `volumen_regimen` < `1.1603` → IC=+0.237 (n=2181)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1603 (IC base=+0.022)

- **PATRÓN** `volumen_regimen` > `0.673` → IC=+0.233 (n=1948)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.673 (IC base=+0.022)

- **PATRÓN** `volumen_pendiente_norm` < `0.1623` → IC=+0.236 (n=2287)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1623 (IC base=+0.022)

- **PATRÓN** `volumen_pendiente_norm` > `0.103` → IC=+0.245 (n=715)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.103 (IC base=+0.022)

- **PATRÓN** `volumen_spike_ratio` < `2.4234` → IC=+0.241 (n=2119)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4234 (IC base=+0.022)

- **PATRÓN** `ballena_activa_n` < `114.0` → IC=+0.254 (n=2161)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 114.0 (IC base=+0.022)

- **PATRÓN** `ibs_20min` < `0.0913` → IC=+0.153 (n=1524)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.0913 (IC base=+0.009)

- **PATRÓN** `dist_vwap_pct` > `0.7714` → IC=+0.262 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7714 (IC base=+0.009)

- **PATRÓN** `volumen_regimen` < `1.1877` → IC=+0.264 (n=1580)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1877 (IC base=+0.009)

- **PATRÓN** `volumen_regimen` > `0.6161` → IC=+0.257 (n=1579)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6161 (IC base=+0.009)

- **PATRÓN** `volumen_pendiente_norm` > `0.2847` → IC=+0.300 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2847 (IC base=+0.009)

- **PATRÓN** `volumen_spike_ratio` < `1.787` → IC=+0.292 (n=1013)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.787 (IC base=+0.009)

- **PATRÓN** `volumen_spike_ratio` > `2.4299` → IC=+0.276 (n=507)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4299 (IC base=+0.009)

- **PATRÓN** `ballena_activa_n` < `115.0` → IC=+0.285 (n=1540)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 115.0 (IC base=+0.009)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7429` → IC=-0.248 (n=2493)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7429
  - _Potencial_: sin este filtro IC_bueno=+0.312 (n=2494)

- **FILTRO** `ibs_20min` > `0.6143` → IC=-0.236 (n=1182)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6143
  - _Potencial_: sin este filtro IC_bueno=+0.157 (n=3549)

- **FILTRO** `sigma_ewma_delta_pct` > `8.282` → IC=-0.269 (n=540)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.282
  - _Potencial_: sin este filtro IC_bueno=+0.101 (n=4191)

- **PATRÓN** `ibs_20min` > `0.7429` → IC=+0.312 (n=2494)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7429 (IC base=+0.032)

- **PATRÓN** `dist_vwap_pct` > `0.2217` → IC=+0.347 (n=1015)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2217 (IC base=+0.032)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.445` → IC=+0.156 (n=2019)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 2.445 (IC base=+0.032)

- **PATRÓN** `volumen_regimen` < `0.8384` → IC=+0.346 (n=1211)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8384 (IC base=+0.032)

- **PATRÓN** `volumen_regimen` > `0.6911` → IC=+0.337 (n=1622)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6911 (IC base=+0.032)

- **PATRÓN** `volumen_pendiente_norm` > `0.2751` → IC=+0.373 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2751 (IC base=+0.032)

- **PATRÓN** `volumen_spike_ratio` < `1.4244` → IC=+0.363 (n=588)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4244 (IC base=+0.032)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.354 (n=1577)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=+0.032)

- **PATRÓN** `ibs_20min` < `0.6143` → IC=+0.157 (n=3549)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.6143 (IC base=+0.059)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.739` → IC=+0.127 (n=3710)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` < 4.739 (IC base=+0.059)

- **PATRÓN** `volumen_regimen` < `0.6909` → IC=+0.278 (n=796)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6909 (IC base=+0.059)

- **PATRÓN** `volumen_pendiente_norm` > `0.0706` → IC=+0.296 (n=725)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0706 (IC base=+0.059)

- **PATRÓN** `volumen_spike_ratio` < `1.802` → IC=+0.280 (n=1172)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.802 (IC base=+0.059)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.287 (n=1785)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 46.0 (IC base=+0.059)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.357 (n=2298)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.315)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.317 (n=2589)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.315)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.315 (n=1796)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.315)

- **PATRÓN** `ibs_20min` > `0.656` → IC=+0.342 (n=2572)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.656 (IC base=+0.315)

- **PATRÓN** `dist_vwap_pct` > `0.2136` → IC=+0.334 (n=1367)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2136 (IC base=+0.315)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.735` → IC=+0.333 (n=1270)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.735 (IC base=+0.315)

- **PATRÓN** `volumen_regimen` > `0.629` → IC=+0.325 (n=2571)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.629 (IC base=+0.315)

- **PATRÓN** `volumen_pendiente_norm` > `0.2816` → IC=+0.347 (n=376)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2816 (IC base=+0.315)

- **PATRÓN** `volumen_spike_ratio` > `1.4307` → IC=+0.326 (n=2481)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4307 (IC base=+0.315)

- **PATRÓN** `libro_liquidez` > `2642.1577` → IC=+0.322 (n=1714)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2642.1577 (IC base=+0.315)

- **PATRÓN** `ballena_activa_n` < `39.0` → IC=+0.340 (n=2324)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 39.0 (IC base=+0.315)

- **PATRÓN** `sigma_h` > `0.0093` → IC=+0.333 (n=2772)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0093 (IC base=+0.316)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.318 (n=2773)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.316)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.316 (n=2778)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.316)

- **PATRÓN** `ibs_20min` < `0.3818` → IC=+0.332 (n=2769)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3818 (IC base=+0.316)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.309` → IC=+0.327 (n=512)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.309 (IC base=+0.316)

- **PATRÓN** `volumen_regimen` < `0.7179` → IC=+0.317 (n=1219)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7179 (IC base=+0.316)

- **PATRÓN** `volumen_regimen` > `1.2052` → IC=+0.345 (n=923)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2052 (IC base=+0.316)

- **PATRÓN** `volumen_pendiente_norm` > `0.2831` → IC=+0.370 (n=389)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2831 (IC base=+0.316)

- **PATRÓN** `volumen_spike_ratio` < `1.4118` → IC=+0.321 (n=862)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4118 (IC base=+0.316)

- **PATRÓN** `volumen_spike_ratio` > `2.1412` → IC=+0.319 (n=1172)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1412 (IC base=+0.316)

- **PATRÓN** `libro_liquidez` > `2976.1495` → IC=+0.316 (n=923)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2976.1495 (IC base=+0.316)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.221 (n=5944)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0125 (IC base=+0.172)

- **PATRÓN** `drift_60min` |x|≤ `0.1239` → IC=+0.192 (n=7839)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.1239 (IC base=+0.172)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.183 (n=18477)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.172)

- **PATRÓN** `ibs_20min` > `0.5378` → IC=+0.229 (n=17805)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5378 (IC base=+0.172)

- **PATRÓN** `dist_vwap_pct` > `0.1638` → IC=+0.205 (n=6691)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1638 (IC base=+0.172)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.99` → IC=+0.254 (n=4651)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.99 (IC base=+0.172)

- **PATRÓN** `volumen_regimen` < `1.0284` → IC=+0.152 (n=10450)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.0284 (IC base=+0.172)

- **PATRÓN** `volumen_regimen` > `0.6218` → IC=+0.152 (n=11874)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.6218 (IC base=+0.172)

- **PATRÓN** `volumen_pendiente_norm` > `0.2933` → IC=+0.205 (n=2573)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2933 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` > `2.5984` → IC=+0.185 (n=5776)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 2.5984 (IC base=+0.172)

- **PATRÓN** `ballena_activa_n` < `86.0` → IC=+0.191 (n=16722)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 86.0 (IC base=+0.172)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.193 (n=7799)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0059 (IC base=+0.186)

- **PATRÓN** `sigma_h` > `0.008` → IC=+0.187 (n=11811)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.008 (IC base=+0.186)

- **PATRÓN** `drift_60min` |x|≤ `0.0826` → IC=+0.223 (n=5901)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0826 (IC base=+0.186)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.213 (n=6649)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.186)

- **PATRÓN** `ibs_20min` < `0.5256` → IC=+0.240 (n=17691)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5256 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.512` → IC=+0.192 (n=2802)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 9.512 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.387` → IC=+0.191 (n=18346)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` < 5.387 (IC base=+0.186)

- **PATRÓN** `volumen_regimen` < `1.1845` → IC=+0.166 (n=12567)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.1845 (IC base=+0.186)

- **PATRÓN** `volumen_pendiente_norm` > `0.294` → IC=+0.221 (n=2654)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.294 (IC base=+0.186)

- **PATRÓN** `volumen_spike_ratio` > `2.631` → IC=+0.197 (n=5625)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 2.631 (IC base=+0.186)

- **PATRÓN** `ballena_activa_n` < `91.0` → IC=+0.201 (n=16694)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 91.0 (IC base=+0.186)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` > `0.0109` → IC=+0.264 (n=976)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0109 (IC base=+0.227)

- **PATRÓN** `drift_60min` |x|≤ `0.1048` → IC=+0.257 (n=1285)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1048 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.234 (n=3037)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.227)

- **PATRÓN** `ibs_20min` > `0.9425` → IC=+0.293 (n=1947)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9425 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.491` → IC=+0.329 (n=955)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.491 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` > `0.2814` → IC=+0.286 (n=442)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2814 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` < `1.8355` → IC=+0.226 (n=1859)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8355 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` > `1.4363` → IC=+0.228 (n=2788)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4363 (IC base=+0.227)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.238 (n=3265)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.227)

- **PATRÓN** `sigma_h` < `0.01` → IC=+0.259 (n=2430)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.01 (IC base=+0.256)

- **PATRÓN** `sigma_h` > `0.009` → IC=+0.258 (n=1104)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.009 (IC base=+0.256)

- **PATRÓN** `drift_60min` |x|≤ `0.0984` → IC=+0.310 (n=1069)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0984 (IC base=+0.256)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.260 (n=2509)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.256)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.261 (n=2216)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.256)

- **PATRÓN** `ibs_20min` < `0.4419` → IC=+0.274 (n=2429)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4419 (IC base=+0.256)

- **PATRÓN** `sigma_ewma_delta_pct` < `1.961` → IC=+0.261 (n=2400)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 1.961 (IC base=+0.256)

- **PATRÓN** `volumen_pendiente_norm` < `0.0995` → IC=+0.258 (n=2140)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0995 (IC base=+0.256)

- **PATRÓN** `volumen_pendiente_norm` > `0.302` → IC=+0.273 (n=363)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.302 (IC base=+0.256)

- **PATRÓN** `volumen_spike_ratio` < `1.4468` → IC=+0.272 (n=778)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4468 (IC base=+0.256)

- **PATRÓN** `volumen_spike_ratio` > `2.6989` → IC=+0.264 (n=777)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6989 (IC base=+0.256)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.264 (n=1751)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.256)

- **PATRÓN** `libro_liquidez` > `1779.8688` → IC=+0.263 (n=1619)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1779.8688 (IC base=+0.256)

- **PATRÓN** `ballena_activa_n` < `6.0` → IC=+0.258 (n=774)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 6.0 (IC base=+0.256)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.196 (n=912)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0032 (IC base=+0.128)

- **PATRÓN** `drift_60min` |x|≤ `0.0651` → IC=+0.177 (n=905)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.0651 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.145 (n=2840)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` > `0.2563` → IC=+0.205 (n=2714)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2563 (IC base=+0.128)

- **PATRÓN** `dist_vwap_pct` > `0.1852` → IC=+0.214 (n=1328)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1852 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.624` → IC=+0.209 (n=497)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.624 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` < `0.8578` → IC=+0.130 (n=1810)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 0.8578 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` > `1.0496` → IC=+0.134 (n=1231)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` > 1.0496 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` > `0.2781` → IC=+0.169 (n=418)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.2781 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` < `1.5036` → IC=+0.132 (n=1174)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 1.5036 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` > `2.4598` → IC=+0.141 (n=890)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 2.4598 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `395.0` → IC=+0.133 (n=2636)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 395.0 (IC base=+0.128)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.172 (n=2919)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0066 (IC base=+0.152)

- **PATRÓN** `drift_60min` |x|≤ `0.2451` → IC=+0.175 (n=2569)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.2451 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.185 (n=1387)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 15.0 (IC base=+0.152)

- **PATRÓN** `ibs_20min` < `0.6098` → IC=+0.211 (n=2919)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6098 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.899` → IC=+0.178 (n=544)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 10.899 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.03` → IC=+0.158 (n=2547)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` < 4.03 (IC base=+0.152)

- **PATRÓN** `volumen_regimen` < `1.2025` → IC=+0.164 (n=2919)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.2025 (IC base=+0.152)

- **PATRÓN** `volumen_pendiente_norm` < `0.2285` → IC=+0.155 (n=3101)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` < 0.2285 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` < `2.468` → IC=+0.156 (n=2793)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.468 (IC base=+0.152)

- **PATRÓN** `ballena_activa_n` < `207.0` → IC=+0.201 (n=1210)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 207.0 (IC base=+0.152)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0116` → IC=+0.226 (n=1368)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0116 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.2514` → IC=+0.231 (n=2010)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2514 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.218 (n=3138)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.290 (n=1600)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.044` → IC=+0.307 (n=717)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.044 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` < `0.0984` → IC=+0.210 (n=2628)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0984 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.3511` → IC=+0.240 (n=425)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3511 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `2.7084` → IC=+0.225 (n=1334)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7084 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.213 (n=3648)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `1994.83` → IC=+0.222 (n=1004)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1994.83 (IC base=+0.210)

- **PATRÓN** `sigma_h` < `0.0109` → IC=+0.248 (n=2374)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0109 (IC base=+0.241)

- **PATRÓN** `drift_60min` |x|≤ `0.2473` → IC=+0.271 (n=1798)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2473 (IC base=+0.241)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.281 (n=1035)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.241)

- **PATRÓN** `ibs_20min` < `0.0415` → IC=+0.295 (n=1188)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0415 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.89` → IC=+0.279 (n=355)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.89 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` > `0.3537` → IC=+0.288 (n=450)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3537 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` < `1.768` → IC=+0.242 (n=1148)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.768 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` > `2.1802` → IC=+0.252 (n=1738)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1802 (IC base=+0.241)

- **PATRÓN** `libro_liquidez` > `1873.4052` → IC=+0.249 (n=1222)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1873.4052 (IC base=+0.241)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.241 (n=1753)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.241)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.197 (n=982)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0038 (IC base=+0.127)

- **PATRÓN** `drift_60min` |x|≤ `0.0792` → IC=+0.182 (n=980)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.0792 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.138 (n=3041)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.127)

- **PATRÓN** `ibs_20min` > `0.2452` → IC=+0.188 (n=2939)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.2452 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` > `0.1419` → IC=+0.186 (n=1665)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1419 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.227` → IC=+0.202 (n=505)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.227 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` < `0.8387` → IC=+0.137 (n=1961)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.8387 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` > `0.2875` → IC=+0.173 (n=444)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.2875 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` < `1.8048` → IC=+0.127 (n=1919)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 1.8048 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` > `2.5083` → IC=+0.137 (n=960)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 2.5083 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `6870.2468` → IC=+0.197 (n=1333)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 6870.2468 (IC base=+0.127)

- **PATRÓN** `ballena_activa_n` < `125.0` → IC=+0.127 (n=2884)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 125.0 (IC base=+0.127)

- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.164 (n=2774)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0068 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.4104` → IC=+0.149 (n=3149)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.4104 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.168 (n=1504)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 15.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` < `0.6714` → IC=+0.188 (n=3149)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.6714 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.249` → IC=+0.142 (n=752)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 9.249 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `0.8509` → IC=+0.151 (n=2101)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.8509 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` > `0.2939` → IC=+0.176 (n=471)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.2939 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` < `2.1959` → IC=+0.134 (n=2634)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 2.1959 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` > `1.4125` → IC=+0.134 (n=2993)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 1.4125 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `6400.6695` → IC=+0.193 (n=1428)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 6400.6695 (IC base=+0.133)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.158 (n=991)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 48.0 (IC base=+0.133)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0127` → IC=+0.171 (n=1094)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.0127 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.134 (n=3360)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 5.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` > `0.4717` → IC=+0.204 (n=3274)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4717 (IC base=+0.119)

- **PATRÓN** `dist_vwap_pct` > `0.202` → IC=+0.188 (n=1737)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.202 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.005` → IC=+0.289 (n=691)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.005 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` < `1.0272` → IC=+0.129 (n=2881)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 1.0272 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` < `0.1621` → IC=+0.122 (n=3338)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_pendiente_norm` < 0.1621 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` < `1.7799` → IC=+0.124 (n=2118)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 1.7799 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `2676.9091` → IC=+0.196 (n=1485)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 2676.9091 (IC base=+0.119)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.129 (n=1093)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 16.0 (IC base=+0.119)

- **PATRÓN** `sigma_h` < `0.012` → IC=+0.143 (n=3436)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.012 (IC base=+0.123)

- **PATRÓN** `drift_60min` |x|≤ `0.1154` → IC=+0.164 (n=1145)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.1154 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.137 (n=3506)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` < `0.6471` → IC=+0.220 (n=3438)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6471 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.237` → IC=+0.144 (n=3037)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 2.237 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` < `1.1777` → IC=+0.129 (n=3435)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 1.1777 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` > `0.8589` → IC=+0.125 (n=2290)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` > 0.8589 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` < `0.162` → IC=+0.126 (n=3386)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` < 0.162 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` > `0.275` → IC=+0.149 (n=480)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.275 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` < `1.4348` → IC=+0.141 (n=1085)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.4348 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` > `2.4465` → IC=+0.133 (n=1085)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 2.4465 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `2580.3305` → IC=+0.192 (n=1557)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 2580.3305 (IC base=+0.123)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.130 (n=3245)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 44.0 (IC base=+0.123)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0108` → IC=+0.248 (n=2947)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0108 (IC base=+0.226)

- **PATRÓN** `drift_60min` |x|≤ `0.1657` → IC=+0.241 (n=1297)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1657 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.232 (n=3061)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.226)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.228 (n=2667)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.226)

- **PATRÓN** `ibs_20min` > `0.6667` → IC=+0.257 (n=2950)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6667 (IC base=+0.226)

- **PATRÓN** `dist_vwap_pct` > `0.1821` → IC=+0.231 (n=1800)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1821 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.547` → IC=+0.257 (n=1353)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.547 (IC base=+0.226)

- **PATRÓN** `volumen_regimen` > `0.6199` → IC=+0.236 (n=2947)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6199 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` > `0.2348` → IC=+0.266 (n=550)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2348 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` < `2.4638` → IC=+0.228 (n=2877)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4638 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` > `1.4317` → IC=+0.231 (n=2877)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4317 (IC base=+0.226)

- **PATRÓN** `libro_liquidez` > `2593.0216` → IC=+0.232 (n=1965)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2593.0216 (IC base=+0.226)

- **PATRÓN** `sigma_h` < `0.0123` → IC=+0.242 (n=1349)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0123 (IC base=+0.241)

- **PATRÓN** `sigma_h` > `0.0223` → IC=+0.248 (n=1392)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0223 (IC base=+0.241)

- **PATRÓN** `drift_60min` |x|≤ `0.6043` → IC=+0.250 (n=3066)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6043 (IC base=+0.241)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.253 (n=1503)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.241)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.246 (n=1371)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.241)

- **PATRÓN** `ibs_20min` < `0.037` → IC=+0.302 (n=1349)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.037 (IC base=+0.241)

- **PATRÓN** `dist_vwap_pct` > `1.1575` → IC=+0.254 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1575 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.125` → IC=+0.269 (n=590)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.125 (IC base=+0.241)

- **PATRÓN** `volumen_regimen` < `0.8684` → IC=+0.241 (n=2044)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8684 (IC base=+0.241)

- **PATRÓN** `volumen_regimen` > `1.0453` → IC=+0.249 (n=1390)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0453 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` > `0.2811` → IC=+0.293 (n=424)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2811 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` < `2.5151` → IC=+0.239 (n=2899)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5151 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` > `1.547` → IC=+0.242 (n=2589)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.547 (IC base=+0.241)

- **PATRÓN** `libro_liquidez` > `2959.5754` → IC=+0.241 (n=1022)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2959.5754 (IC base=+0.241)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.209 (n=1550)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.156)

- **PATRÓN** `drift_60min` |x|≤ `0.1375` → IC=+0.172 (n=2045)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.1375 (IC base=+0.156)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.168 (n=4839)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.156)

- **PATRÓN** `ibs_20min` > `0.4222` → IC=+0.201 (n=4152)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4222 (IC base=+0.156)

- **PATRÓN** `dist_vwap_pct` > `0.8467` → IC=+0.183 (n=693)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.8467 (IC base=+0.156)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.54` → IC=+0.210 (n=759)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.54 (IC base=+0.156)

- **PATRÓN** `volumen_regimen` < `0.8606` → IC=+0.167 (n=2799)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.8606 (IC base=+0.156)

- **PATRÓN** `volumen_regimen` > `1.1944` → IC=+0.164 (n=1399)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 1.1944 (IC base=+0.156)

- **PATRÓN** `volumen_pendiente_norm` > `0.1569` → IC=+0.173 (n=1219)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.1569 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` < `1.5274` → IC=+0.162 (n=1995)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 1.5274 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` > `1.8077` → IC=+0.158 (n=3022)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.8077 (IC base=+0.156)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.157 (n=3968)

  - _Acción_: Kelly boost +0.79€ cuando `libro_spread` < 0.01 (IC base=+0.156)

- **PATRÓN** `libro_liquidez` > `7287.1688` → IC=+0.188 (n=2107)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 7287.1688 (IC base=+0.156)

- **PATRÓN** `ibs_20min` < `0.3823` → IC=+0.175 (n=3390)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.3823 (IC base=+0.098)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.140 (n=2224)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 23.0 (IC base=+0.098)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.197 (n=1154)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0062 (IC base=+0.185)

- **PATRÓN** `drift_60min` |x|≤ `0.3322` → IC=+0.200 (n=1153)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3322 (IC base=+0.185)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.218 (n=1039)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.185)

- **PATRÓN** `ibs_20min` > `0.6198` → IC=+0.243 (n=768)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6198 (IC base=+0.185)

- **PATRÓN** `dist_vwap_pct` > `0.311` → IC=+0.221 (n=346)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.311 (IC base=+0.185)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.949` → IC=+0.214 (n=508)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.949 (IC base=+0.185)

- **PATRÓN** `volumen_regimen` < `0.629` → IC=+0.211 (n=385)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.629 (IC base=+0.185)

- **PATRÓN** `volumen_pendiente_norm` < `0.2153` → IC=+0.189 (n=1298)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` < 0.2153 (IC base=+0.185)

- **PATRÓN** `volumen_pendiente_norm` > `0.0913` → IC=+0.200 (n=398)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0913 (IC base=+0.185)

- **PATRÓN** `volumen_spike_ratio` < `2.1671` → IC=+0.199 (n=995)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1671 (IC base=+0.185)

- **PATRÓN** `volumen_spike_ratio` > `1.4026` → IC=+0.187 (n=1131)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 1.4026 (IC base=+0.185)

- **PATRÓN** `libro_liquidez` > `13741.2485` → IC=+0.192 (n=768)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 13741.2485 (IC base=+0.185)

- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.160 (n=483)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0032 (IC base=+0.079)

- **PATRÓN** `ibs_20min` < `0.2095` → IC=+0.196 (n=637)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.2095 (IC base=+0.079)

- **PATRÓN** `ballena_activa_n` < `166.0` → IC=+0.174 (n=623)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 166.0 (IC base=+0.079)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.232 (n=620)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.152)

- **PATRÓN** `drift_60min` |x|≤ `0.2149` → IC=+0.159 (n=938)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.2149 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.171 (n=1458)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 5.0 (IC base=+0.152)

- **PATRÓN** `ibs_20min` > `0.7791` → IC=+0.266 (n=638)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7791 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` > `0.8532` → IC=+0.194 (n=220)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.8532 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.907` → IC=+0.204 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.907 (IC base=+0.152)

- **PATRÓN** `volumen_regimen` < `0.8331` → IC=+0.165 (n=938)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8331 (IC base=+0.152)

- **PATRÓN** `volumen_pendiente_norm` > `0.2183` → IC=+0.197 (n=255)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2183 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` > `2.4732` → IC=+0.181 (n=462)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 2.4732 (IC base=+0.152)

- **PATRÓN** `libro_liquidez` > `7912.0475` → IC=+0.178 (n=638)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 7912.0475 (IC base=+0.152)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.123 (n=932)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0053 (IC base=+0.097)

- **PATRÓN** `ibs_20min` < `0.0873` → IC=+0.202 (n=465)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0873 (IC base=+0.097)

- **PATRÓN** `volumen_regimen` < `0.6769` → IC=+0.136 (n=614)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.6769 (IC base=+0.097)

- **PATRÓN** `libro_liquidez` > `7738.3514` → IC=+0.152 (n=633)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 7738.3514 (IC base=+0.097)

- **PATRÓN** `ballena_activa_n` < `61.0` → IC=+0.121 (n=903)

  - _Acción_: Kelly boost +0.60€ cuando `ballena_activa_n` < 61.0 (IC base=+0.097)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` < `0.0094` → IC=+0.146 (n=804)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0094 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.157 (n=835)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 11.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` > `0.5385` → IC=+0.186 (n=1072)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.5385 (IC base=+0.119)

- **PATRÓN** `dist_vwap_pct` > `0.9658` → IC=+0.177 (n=193)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.9658 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.859` → IC=+0.224 (n=465)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.859 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` < `1.0461` → IC=+0.132 (n=1057)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 1.0461 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` > `0.701` → IC=+0.126 (n=1072)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` > 0.701 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` > `0.224` → IC=+0.151 (n=210)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.224 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` < `1.4112` → IC=+0.149 (n=388)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.4112 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `2751.7394` → IC=+0.156 (n=544)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 2751.7394 (IC base=+0.119)

- **PATRÓN** `ibs_20min` < `0.36` → IC=+0.190 (n=889)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.36 (IC base=+0.082)

- **PATRÓN** `libro_liquidez` > `2639.8649` → IC=+0.168 (n=604)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 2639.8649 (IC base=+0.082)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0157` → IC=+0.238 (n=292)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0157 (IC base=+0.184)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.224 (n=208)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.184)

- **PATRÓN** `ibs_20min` > `0.9524` → IC=+0.211 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9524 (IC base=+0.184)

- **PATRÓN** `dist_vwap_pct` > `0.93` → IC=+0.196 (n=110)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.93 (IC base=+0.184)

- **PATRÓN** `dist_vwap_pct` < `0.3233` → IC=+0.184 (n=384)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` < 0.3233 (IC base=+0.184)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.495` → IC=+0.199 (n=437)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.495 (IC base=+0.184)

- **PATRÓN** `volumen_regimen` > `1.2169` → IC=+0.250 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2169 (IC base=+0.184)

- **PATRÓN** `volumen_pendiente_norm` > `0.0806` → IC=+0.218 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0806 (IC base=+0.184)

- **PATRÓN** `volumen_spike_ratio` < `2.1215` → IC=+0.197 (n=361)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 2.1215 (IC base=+0.184)

- **PATRÓN** `volumen_spike_ratio` > `1.4098` → IC=+0.194 (n=410)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 1.4098 (IC base=+0.184)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.199 (n=459)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.03 (IC base=+0.184)

- **PATRÓN** `libro_liquidez` > `2696.9888` → IC=+0.218 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2696.9888 (IC base=+0.184)

- **PATRÓN** `sigma_h` > `0.0105` → IC=+0.169 (n=485)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.0105 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.3406` → IC=+0.163 (n=324)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.3406 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.196 (n=235)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 15.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` < `0.3415` → IC=+0.163 (n=324)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` < 0.3415 (IC base=+0.151)

- **PATRÓN** `ibs_20min` > `0.1` → IC=+0.157 (n=485)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` > 0.1 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` > `1.1964` → IC=+0.268 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1964 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.969` → IC=+0.153 (n=122)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 4.969 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.009` → IC=+0.153 (n=468)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 3.009 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` < `1.2424` → IC=+0.172 (n=485)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` < 1.2424 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` < `0.1134` → IC=+0.168 (n=450)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` < 0.1134 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.2358` → IC=+0.193 (n=86)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2358 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `1.4792` → IC=+0.196 (n=156)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 1.4792 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` > `2.6321` → IC=+0.165 (n=156)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 2.6321 (IC base=+0.151)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.169 (n=466)

  - _Acción_: Kelly boost +0.84€ cuando `ballena_activa_n` < 20.0 (IC base=+0.151)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0126` → IC=+0.227 (n=7815)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0126 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.191 (n=24439)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` > `0.4278` → IC=+0.226 (n=23436)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4278 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` > `0.9022` → IC=+0.216 (n=2705)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9022 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.946` → IC=+0.260 (n=5747)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.946 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `1.2132` → IC=+0.160 (n=15794)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2132 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.2408` → IC=+0.211 (n=4208)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2408 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `2.623` → IC=+0.192 (n=7632)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.623 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `102.0` → IC=+0.201 (n=22090)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 102.0 (IC base=+0.181)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.200 (n=7247)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.198)

- **PATRÓN** `sigma_h` > `0.0123` → IC=+0.208 (n=7247)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0123 (IC base=+0.198)

- **PATRÓN** `drift_60min` |x|≤ `0.4961` → IC=+0.199 (n=21705)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4961 (IC base=+0.198)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.217 (n=8120)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.198)

- **PATRÓN** `ibs_20min` < `0.4857` → IC=+0.252 (n=19109)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4857 (IC base=+0.198)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.368` → IC=+0.203 (n=21193)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.368 (IC base=+0.198)

- **PATRÓN** `volumen_regimen` < `1.0525` → IC=+0.173 (n=12819)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` < 1.0525 (IC base=+0.198)

- **PATRÓN** `volumen_pendiente_norm` > `0.2932` → IC=+0.255 (n=2980)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2932 (IC base=+0.198)

- **PATRÓN** `volumen_spike_ratio` > `2.6252` → IC=+0.212 (n=6942)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6252 (IC base=+0.198)

- **PATRÓN** `ballena_activa_n` < `91.0` → IC=+0.214 (n=20620)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 91.0 (IC base=+0.198)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` > `0.0109` → IC=+0.275 (n=1249)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0109 (IC base=+0.235)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.253 (n=1807)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.235)

- **PATRÓN** `ibs_20min` > `0.8629` → IC=+0.297 (n=2495)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8629 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.869` → IC=+0.343 (n=892)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.869 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` > `0.2328` → IC=+0.290 (n=670)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2328 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` < `1.4494` → IC=+0.233 (n=1206)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4494 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` > `2.2917` → IC=+0.241 (n=1641)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2917 (IC base=+0.235)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.249 (n=4150)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.235)

- **PATRÓN** `libro_liquidez` > `2023.6668` → IC=+0.237 (n=1247)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2023.6668 (IC base=+0.235)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.249 (n=2329)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 14.0 (IC base=+0.235)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.267 (n=3384)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.267)

- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.269 (n=1537)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0094 (IC base=+0.267)

- **PATRÓN** `drift_60min` |x|≤ `0.1242` → IC=+0.295 (n=1490)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1242 (IC base=+0.267)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.268 (n=3513)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.267)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.270 (n=3058)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.267)

- **PATRÓN** `ibs_20min` < `0.4679` → IC=+0.287 (n=2976)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4679 (IC base=+0.267)

- **PATRÓN** `volumen_pendiente_norm` < `0.0978` → IC=+0.269 (n=3086)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0978 (IC base=+0.267)

- **PATRÓN** `volumen_pendiente_norm` > `0.2913` → IC=+0.285 (n=467)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2913 (IC base=+0.267)

- **PATRÓN** `volumen_spike_ratio` < `1.5659` → IC=+0.272 (n=1431)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5659 (IC base=+0.267)

- **PATRÓN** `volumen_spike_ratio` > `2.6528` → IC=+0.279 (n=1084)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6528 (IC base=+0.267)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.271 (n=2426)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.267)

- **PATRÓN** `libro_liquidez` > `1778.5998` → IC=+0.273 (n=2255)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1778.5998 (IC base=+0.267)

- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.276 (n=1244)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 8.0 (IC base=+0.267)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.176 (n=1288)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0032 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.0799` → IC=+0.150 (n=1285)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.0799 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.151 (n=4007)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 5.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` > `0.1948` → IC=+0.188 (n=3843)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.1948 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` > `0.3255` → IC=+0.200 (n=1206)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3255 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.313` → IC=+0.167 (n=802)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 9.313 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `0.6338` → IC=+0.155 (n=1282)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.6338 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` > `1.068` → IC=+0.144 (n=1743)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 1.068 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.2713` → IC=+0.186 (n=542)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.2713 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `2.1664` → IC=+0.143 (n=3324)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.1664 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `1.5138` → IC=+0.144 (n=3374)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.5138 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `296.0` → IC=+0.153 (n=2493)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 296.0 (IC base=+0.138)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.171 (n=2966)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0058 (IC base=+0.142)

- **PATRÓN** `drift_60min` |x|≤ `0.0808` → IC=+0.169 (n=1122)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.0808 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.172 (n=1237)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.142)

- **PATRÓN** `ibs_20min` < `0.6796` → IC=+0.189 (n=3366)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.6796 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.023` → IC=+0.145 (n=3044)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 4.023 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` < `1.0418` → IC=+0.153 (n=2961)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 1.0418 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` > `0.2209` → IC=+0.195 (n=617)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2209 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` < `2.4295` → IC=+0.147 (n=3254)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 2.4295 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` > `1.7697` → IC=+0.147 (n=2169)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.7697 (IC base=+0.142)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=4373)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.142)

- **PATRÓN** `ballena_activa_n` < `218.0` → IC=+0.170 (n=1059)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 218.0 (IC base=+0.142)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0118` → IC=+0.238 (n=1772)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0118 (IC base=+0.225)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.235 (n=4089)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.225 (n=3497)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.225)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.301 (n=1451)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.225)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.981` → IC=+0.321 (n=871)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.981 (IC base=+0.225)

- **PATRÓN** `volumen_pendiente_norm` < `0.1316` → IC=+0.226 (n=3703)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1316 (IC base=+0.225)

- **PATRÓN** `volumen_pendiente_norm` > `0.3501` → IC=+0.231 (n=511)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3501 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` > `2.7432` → IC=+0.241 (n=1732)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7432 (IC base=+0.225)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.231 (n=4721)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.225)

- **PATRÓN** `libro_liquidez` > `2002.2484` → IC=+0.240 (n=1301)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2002.2484 (IC base=+0.225)

- **PATRÓN** `sigma_h` < `0.0111` → IC=+0.250 (n=3310)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0111 (IC base=+0.245)

- **PATRÓN** `drift_60min` |x|≤ `0.1808` → IC=+0.260 (n=1653)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1808 (IC base=+0.245)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.265 (n=1431)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.245)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.249 (n=1714)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.245)

- **PATRÓN** `ibs_20min` < `0.0625` → IC=+0.304 (n=1258)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0625 (IC base=+0.245)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.038` → IC=+0.308 (n=394)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.038 (IC base=+0.245)

- **PATRÓN** `volumen_pendiente_norm` > `0.3478` → IC=+0.303 (n=566)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3478 (IC base=+0.245)

- **PATRÓN** `volumen_spike_ratio` > `2.1738` → IC=+0.257 (n=2418)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1738 (IC base=+0.245)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.249 (n=1882)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.245)

- **PATRÓN** `libro_liquidez` > `1977.8984` → IC=+0.254 (n=1252)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1977.8984 (IC base=+0.245)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.250 (n=3170)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 21.0 (IC base=+0.245)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.194 (n=1357)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0038 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.3416` → IC=+0.148 (n=3573)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.3416 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.150 (n=4210)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 5.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` > `0.882` → IC=+0.269 (n=1353)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.882 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` > `0.1993` → IC=+0.167 (n=1797)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.1993 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.207` → IC=+0.167 (n=820)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 9.207 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `0.8567` → IC=+0.153 (n=2707)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.8567 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.2324` → IC=+0.196 (n=721)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2324 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `1.5144` → IC=+0.156 (n=1746)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.5144 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `2.1572` → IC=+0.142 (n=1799)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 2.1572 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `5654.5914` → IC=+0.229 (n=1840)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5654.5914 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `87.0` → IC=+0.146 (n=2662)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 87.0 (IC base=+0.138)

- **PATRÓN** `sigma_h` < `0.008` → IC=+0.166 (n=3421)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.008 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.4464` → IC=+0.160 (n=3420)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.4464 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.175 (n=1261)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 17.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` < `0.7048` → IC=+0.200 (n=3420)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7048 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.019` → IC=+0.154 (n=2987)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 3.019 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `0.8534` → IC=+0.162 (n=2280)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8534 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` > `0.2942` → IC=+0.208 (n=437)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2942 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `2.2024` → IC=+0.153 (n=2910)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.2024 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` > `1.5252` → IC=+0.156 (n=2955)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.5252 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `6616.4778` → IC=+0.224 (n=1140)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6616.4778 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `89.0` → IC=+0.165 (n=2245)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 89.0 (IC base=+0.149)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0128` → IC=+0.155 (n=1375)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0128 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.147 (n=2907)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 11.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` > `0.4286` → IC=+0.187 (n=4130)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.4286 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` > `1.024` → IC=+0.207 (n=667)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.024 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.244` → IC=+0.273 (n=1047)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.244 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` < `0.8739` → IC=+0.134 (n=2751)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 0.8739 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` < `2.4921` → IC=+0.121 (n=4025)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` < 2.4921 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `2727.939` → IC=+0.239 (n=1375)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2727.939 (IC base=+0.117)

- **PATRÓN** `sigma_h` < `0.011` → IC=+0.156 (n=3408)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.011 (IC base=+0.134)

- **PATRÓN** `drift_60min` |x|≤ `0.1406` → IC=+0.152 (n=1290)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.1406 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.169 (n=1823)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 15.0 (IC base=+0.134)

- **PATRÓN** `ibs_20min` < `0.5417` → IC=+0.240 (n=3404)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5417 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.045` → IC=+0.156 (n=3749)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 3.045 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` < `1.1903` → IC=+0.139 (n=3868)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 1.1903 (IC base=+0.134)

- **PATRÓN** `volumen_pendiente_norm` > `0.2303` → IC=+0.196 (n=683)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2303 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` < `1.4384` → IC=+0.162 (n=1229)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 1.4384 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `2625.0238` → IC=+0.215 (n=1290)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2625.0238 (IC base=+0.134)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.145 (n=3694)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 49.0 (IC base=+0.134)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.258 (n=3769)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0113 (IC base=+0.239)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.245 (n=3937)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.239)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.244 (n=2529)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.239)

- **PATRÓN** `ibs_20min` > `0.6146` → IC=+0.271 (n=3367)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6146 (IC base=+0.239)

- **PATRÓN** `dist_vwap_pct` > `0.1988` → IC=+0.251 (n=1907)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1988 (IC base=+0.239)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.126` → IC=+0.291 (n=663)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.126 (IC base=+0.239)

- **PATRÓN** `volumen_regimen` < `1.2177` → IC=+0.240 (n=3769)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2177 (IC base=+0.239)

- **PATRÓN** `volumen_regimen` > `0.6434` → IC=+0.244 (n=3769)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6434 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` > `0.2393` → IC=+0.255 (n=655)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2393 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` > `2.4955` → IC=+0.253 (n=1230)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4955 (IC base=+0.239)

- **PATRÓN** `libro_liquidez` > `2982.5888` → IC=+0.246 (n=1256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2982.5888 (IC base=+0.239)

- **PATRÓN** `sigma_h` > `0.0254` → IC=+0.268 (n=1306)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0254 (IC base=+0.244)

- **PATRÓN** `drift_60min` |x|≤ `0.6467` → IC=+0.244 (n=3916)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6467 (IC base=+0.244)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.249 (n=3688)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.244)

- **PATRÓN** `ibs_20min` < `0.1385` → IC=+0.310 (n=1723)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1385 (IC base=+0.244)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.066` → IC=+0.276 (n=745)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.066 (IC base=+0.244)

- **PATRÓN** `volumen_regimen` < `0.7152` → IC=+0.244 (n=1724)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7152 (IC base=+0.244)

- **PATRÓN** `volumen_regimen` > `1.2132` → IC=+0.267 (n=1305)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2132 (IC base=+0.244)

- **PATRÓN** `volumen_pendiente_norm` > `0.2855` → IC=+0.311 (n=538)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2855 (IC base=+0.244)

- **PATRÓN** `volumen_spike_ratio` > `1.4288` → IC=+0.248 (n=3705)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4288 (IC base=+0.244)

- **PATRÓN** `libro_liquidez` > `2969.9944` → IC=+0.247 (n=1305)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2969.9944 (IC base=+0.244)

### GBM_LATE_5M
- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.231 (n=6078)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0106 (IC base=+0.224)

- **PATRÓN** `drift_60min` |x|≤ `0.5274` → IC=+0.233 (n=6903)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5274 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.231 (n=6951)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` > `0.9294` → IC=+0.262 (n=2302)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9294 (IC base=+0.224)

- **PATRÓN** `dist_vwap_pct` < `0.2505` → IC=+0.226 (n=4397)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2505 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.479` → IC=+0.231 (n=2297)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.479 (IC base=+0.224)

- **PATRÓN** `volumen_regimen` < `0.7046` → IC=+0.232 (n=2151)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7046 (IC base=+0.224)

- **PATRÓN** `volumen_regimen` > `0.8782` → IC=+0.224 (n=3257)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8782 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` < `0.1045` → IC=+0.225 (n=6451)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1045 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` > `0.2362` → IC=+0.232 (n=1336)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2362 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` < `2.2575` → IC=+0.228 (n=5976)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.2575 (IC base=+0.224)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.227 (n=4950)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.224)

- **PATRÓN** `libro_liquidez` > `2585.263` → IC=+0.228 (n=6902)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2585.263 (IC base=+0.224)

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.235 (n=1577)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0045 (IC base=+0.203)

- **PATRÓN** `drift_60min` |x|≤ `0.4044` → IC=+0.219 (n=4164)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4044 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.211 (n=1821)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.215 (n=2134)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.203)

- **PATRÓN** `ibs_20min` < `0.0885` → IC=+0.213 (n=1578)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0885 (IC base=+0.203)

- **PATRÓN** `dist_vwap_pct` > `0.6838` → IC=+0.211 (n=766)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6838 (IC base=+0.203)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.764` → IC=+0.218 (n=4279)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.764 (IC base=+0.203)

- **PATRÓN** `volumen_regimen` < `1.0948` → IC=+0.210 (n=3862)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0948 (IC base=+0.203)

- **PATRÓN** `volumen_pendiente_norm` < `0.0983` → IC=+0.206 (n=4372)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0983 (IC base=+0.203)

- **PATRÓN** `volumen_pendiente_norm` > `0.2239` → IC=+0.204 (n=944)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2239 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` < `1.533` → IC=+0.206 (n=2052)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.533 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` > `2.1968` → IC=+0.212 (n=2114)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1968 (IC base=+0.203)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.203 (n=6085)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.203)

- **PATRÓN** `ballena_activa_n` < `28.0` → IC=+0.228 (n=2075)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 28.0 (IC base=+0.203)

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
- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.220 (n=1833)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0084 (IC base=+0.209)

- **PATRÓN** `drift_60min` |x|≤ `0.458` → IC=+0.217 (n=1833)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.458 (IC base=+0.209)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.234 (n=640)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.209)

- **PATRÓN** `ibs_20min` < `0.4751` → IC=+0.218 (n=1222)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4751 (IC base=+0.209)

- **PATRÓN** `ibs_20min` > `0.1447` → IC=+0.211 (n=1833)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1447 (IC base=+0.209)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.374` → IC=+0.216 (n=1858)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 6.374 (IC base=+0.209)

- **PATRÓN** `volumen_regimen` < `0.8664` → IC=+0.217 (n=1222)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8664 (IC base=+0.209)

- **PATRÓN** `volumen_pendiente_norm` < `0.1018` → IC=+0.212 (n=1689)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1018 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` < `1.4029` → IC=+0.227 (n=598)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4029 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` > `1.4937` → IC=+0.210 (n=1602)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4937 (IC base=+0.209)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.209 (n=1818)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.209)

- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.213 (n=1439)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0084 (IC base=+0.199)

- **PATRÓN** `drift_60min` |x|≤ `0.4905` → IC=+0.219 (n=1438)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4905 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.202 (n=535)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.214 (n=976)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.199)

- **PATRÓN** `ibs_20min` < `0.3937` → IC=+0.199 (n=959)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3937 (IC base=+0.199)

- **PATRÓN** `ibs_20min` > `0.0847` → IC=+0.202 (n=1437)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.0847 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` > `0.6347` → IC=+0.209 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6347 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.266` → IC=+0.204 (n=1313)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.266 (IC base=+0.199)

- **PATRÓN** `volumen_regimen` < `1.2528` → IC=+0.207 (n=1438)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2528 (IC base=+0.199)

- **PATRÓN** `volumen_regimen` > `0.7214` → IC=+0.199 (n=1285)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7214 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` > `0.0728` → IC=+0.225 (n=591)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0728 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` < `1.4106` → IC=+0.205 (n=470)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4106 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` > `1.7864` → IC=+0.202 (n=940)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7864 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `6540.7204` → IC=+0.208 (n=1284)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6540.7204 (IC base=+0.199)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0086` → IC=+0.240 (n=526)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0086 (IC base=+0.217)

- **PATRÓN** `sigma_h` > `0.0121` → IC=+0.221 (n=542)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0121 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.240 (n=1214)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.217)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.216 (n=1095)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.217)

- **PATRÓN** `ibs_20min` > `0.9009` → IC=+0.283 (n=542)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9009 (IC base=+0.217)

- **PATRÓN** `dist_vwap_pct` > `0.8369` → IC=+0.253 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8369 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.193` → IC=+0.249 (n=643)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.193 (IC base=+0.217)

- **PATRÓN** `volumen_regimen` < `0.7044` → IC=+0.246 (n=526)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7044 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` < `0.1056` → IC=+0.222 (n=1090)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1056 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` > `0.2735` → IC=+0.231 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2735 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` < `2.1646` → IC=+0.226 (n=1024)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1646 (IC base=+0.217)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.226 (n=1408)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.217)

- **PATRÓN** `libro_liquidez` > `4380.4698` → IC=+0.251 (n=399)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4380.4698 (IC base=+0.217)

- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.253 (n=556)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0104 (IC base=+0.238)

- **PATRÓN** `drift_60min` |x|≤ `0.6536` → IC=+0.252 (n=835)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6536 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.240 (n=767)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.238)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.259 (n=592)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.238)

- **PATRÓN** `ibs_20min` < `0.6404` → IC=+0.261 (n=734)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6404 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.968` → IC=+0.259 (n=787)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.968 (IC base=+0.238)

- **PATRÓN** `volumen_regimen` < `0.7447` → IC=+0.256 (n=367)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7447 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` < `0.084` → IC=+0.255 (n=711)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.084 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` > `2.2116` → IC=+0.268 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2116 (IC base=+0.238)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.239 (n=1091)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.238)

- **PATRÓN** `libro_liquidez` > `3904.822` → IC=+0.262 (n=556)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3904.822 (IC base=+0.238)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.274 (n=737)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 34.0 (IC base=+0.238)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.149 (n=787)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0039 (IC base=+0.053)

- **PATRÓN** `ibs_20min` > `0.7458` → IC=+0.183 (n=1506)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.7458 (IC base=+0.053)

- **PATRÓN** `dist_vwap_pct` > `0.1492` → IC=+0.142 (n=1090)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.1492 (IC base=+0.053)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.347` → IC=+0.139 (n=497)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 10.347 (IC base=+0.053)

- **PATRÓN** `ibs_20min` < `0.6202` → IC=+0.143 (n=1617)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` < 0.6202 (IC base=+0.058)

- **PATRÓN** `volumen_pendiente_norm` > `0.1476` → IC=+0.146 (n=442)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` > 0.1476 (IC base=+0.058)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `ibs_20min` < `0.5412` → IC=-0.121 (n=312)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5412
  - _Potencial_: sin este filtro IC_bueno=+0.160 (n=636)

- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.124 (n=653)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0054 (IC base=+0.067)

- **PATRÓN** `ibs_20min` > `0.5412` → IC=+0.160 (n=636)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` > 0.5412 (IC base=+0.067)

- **PATRÓN** `dist_vwap_pct` > `0.1239` → IC=+0.168 (n=326)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.1239 (IC base=+0.067)

- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.131 (n=288)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.66€ cuando `sigma_h` < 0.0035 (IC base=+0.049)

- **PATRÓN** `ibs_20min` < `0.0674` → IC=+0.254 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0674 (IC base=+0.049)

- **PATRÓN** `volumen_pendiente_norm` > `0.2162` → IC=+0.157 (n=129)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` > 0.2162 (IC base=+0.049)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` > `0.5459` → IC=-0.134 (n=230)

  - _Acción_: SKIP cuando `ibs_20min` > 0.5459
  - _Potencial_: sin este filtro IC_bueno=+0.147 (n=448)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.146 (n=334)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0042 (IC base=+0.068)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.122 (n=379)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 15.0 (IC base=+0.068)

- **PATRÓN** `ibs_20min` > `0.9322` → IC=+0.259 (n=330)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9322 (IC base=+0.068)

- **PATRÓN** `dist_vwap_pct` > `0.1313` → IC=+0.165 (n=347)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.1313 (IC base=+0.068)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.613` → IC=+0.198 (n=157)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 11.613 (IC base=+0.068)

- **PATRÓN** `volumen_pendiente_norm` > `0.2815` → IC=+0.150 (n=101)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.2815 (IC base=+0.068)

- **PATRÓN** `ibs_20min` < `0.1037` → IC=+0.266 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1037 (IC base=+0.036)

### GBM_LATE_60M#SOL#60min
- **PATRÓN** `ibs_20min` > `0.7174` → IC=+0.138 (n=547)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` > 0.7174 (IC base=+0.027)

- **PATRÓN** `dist_vwap_pct` > `0.7377` → IC=+0.144 (n=189)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` > 0.7377 (IC base=+0.027)

- **PATRÓN** `sigma_h` < `0.0097` → IC=+0.181 (n=340)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0097 (IC base=+0.091)

- **PATRÓN** `ibs_20min` < `0.1772` → IC=+0.251 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1772 (IC base=+0.091)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.849` → IC=+0.314 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.849 (IC base=+0.091)

- **PATRÓN** `volumen_regimen` > `1.1079` → IC=+0.204 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1079 (IC base=+0.091)

- **PATRÓN** `volumen_pendiente_norm` > `0.1089` → IC=+0.172 (n=181)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.1089 (IC base=+0.091)

- **PATRÓN** `volumen_spike_ratio` > `2.5663` → IC=+0.156 (n=149)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 2.5663 (IC base=+0.091)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.130 (n=228)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.03 (IC base=+0.091)

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

- **FILTRO** `sigma_h` < `0.0062` → IC=-0.287 (n=252)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0062
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=86)

- **FILTRO** `ibs_20min` > `0.6985` → IC=-0.310 (n=114)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6985
  - _Potencial_: sin este filtro IC_bueno=-0.252 (n=224)

- **FILTRO** `dist_vwap_pct` > `0.4428` → IC=-0.409 (n=20)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4428
  - _Potencial_: sin este filtro IC_bueno=-0.263 (n=318)

- **FILTRO** `sigma_ewma_delta_pct` > `9.683` → IC=-0.300 (n=28)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 9.683
  - _Potencial_: sin este filtro IC_bueno=-0.269 (n=310)

- **FILTRO** `volumen_pendiente_norm` > `0.0448` → IC=-0.379 (n=31)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0448
  - _Potencial_: sin este filtro IC_bueno=-0.252 (n=216)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `ibs_20min` < `0.0864` → IC=-0.269 (n=37)

  - _Acción_: SKIP cuando `ibs_20min` < 0.0864
  - _Potencial_: sin este filtro IC_bueno=-0.234 (n=77)

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
- **FILTRO** `hora_utc` < `2.0` → IC=-0.179 (n=26)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 2.0
  - _Potencial_: sin este filtro IC_bueno=-0.176 (n=106)

- **FILTRO** `hora_utc` > `9.0` → IC=-0.318 (n=31)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.131 (n=101)

- **FILTRO** `volumen_regimen` < `0.7435` → IC=-0.271 (n=33)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7435
  - _Potencial_: sin este filtro IC_bueno=-0.144 (n=99)

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
- **FILTRO** `ibs_20min` > `0.2459` → IC=-0.145 (n=302)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2459
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=910)

- **PATRÓN** `sigma_h` > `0.0076` → IC=+0.233 (n=343)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0076 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.162 (n=797)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` > `0.6774` → IC=+0.185 (n=757)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.6774 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` > `0.8305` → IC=+0.303 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8305 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.392` → IC=+0.161 (n=178)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 10.392 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `0.6229` → IC=+0.193 (n=252)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 0.6229 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` < `0.069` → IC=+0.180 (n=564)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` < 0.069 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `1.3956` → IC=+0.197 (n=216)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.3956 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.831` → IC=+0.136 (n=267)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` > 8.831 (IC base=+0.030)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.7302` → IC=-0.171 (n=74)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7302
  - _Potencial_: sin este filtro IC_bueno=+0.116 (n=222)

- **PATRÓN** `sigma_h` > `0.0066` → IC=+0.158 (n=74)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0066 (IC base=+0.044)

- **PATRÓN** `ibs_20min` > `0.7913` → IC=+0.127 (n=199)

  - _Acción_: Kelly boost +0.63€ cuando `ibs_20min` > 0.7913 (IC base=+0.044)

- **PATRÓN** `dist_vwap_pct` > `0.6482` → IC=+0.198 (n=41)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.6482 (IC base=+0.044)

- **PATRÓN** `ibs_20min` < `0.2471` → IC=+0.141 (n=419)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` < 0.2471 (IC base=+0.082)

- **PATRÓN** `volumen_pendiente_norm` > `0.2751` → IC=+0.144 (n=71)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_pendiente_norm` > 0.2751 (IC base=+0.082)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `volumen_pendiente_norm` > `0.1803` → IC=-0.167 (n=25)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1803
  - _Potencial_: sin este filtro IC_bueno=+0.143 (n=261)

- **FILTRO** `ibs_20min` > `0.15` → IC=-0.129 (n=149)

  - _Acción_: SKIP cuando `ibs_20min` > 0.15
  - _Potencial_: sin este filtro IC_bueno=+0.079 (n=290)

- **PATRÓN** `drift_60min` |x|≤ `0.1025` → IC=+0.133 (n=107)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.67€ cuando `drift_60min` |x|≤ 0.1025 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.155 (n=85)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 18.0 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.135 (n=83)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 5.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` > `0.7163` → IC=+0.145 (n=243)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` > 0.7163 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.38` → IC=+0.142 (n=252)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 9.38 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` < `0.6249` → IC=+0.167 (n=82)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.6249 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` > `1.1915` → IC=+0.163 (n=81)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 1.1915 (IC base=+0.117)

- **PATRÓN** `volumen_pendiente_norm` < `0.1803` → IC=+0.143 (n=261)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` < 0.1803 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` < `2.0546` → IC=+0.154 (n=189)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.0546 (IC base=+0.117)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.126 (n=209)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.01 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.659` → IC=+0.175 (n=78)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 10.659 (IC base=+0.008)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.0556` → IC=-0.222 (n=106)

  - _Acción_: SKIP cuando `ibs_20min` > 0.0556
  - _Potencial_: sin este filtro IC_bueno=+0.095 (n=109)

- **PATRÓN** `sigma_h` > `0.0115` → IC=+0.278 (n=97)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0115 (IC base=+0.253)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.281 (n=267)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.253)

- **PATRÓN** `ibs_20min` > `0.6` → IC=+0.282 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6 (IC base=+0.253)

- **PATRÓN** `dist_vwap_pct` > `0.7375` → IC=+0.399 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7375 (IC base=+0.253)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.867` → IC=+0.337 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.867 (IC base=+0.253)

- **PATRÓN** `volumen_regimen` < `0.5991` → IC=+0.318 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.5991 (IC base=+0.253)

- **PATRÓN** `volumen_pendiente_norm` > `0.2694` → IC=+0.309 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2694 (IC base=+0.253)

- **PATRÓN** `volumen_spike_ratio` < `1.3956` → IC=+0.325 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3956 (IC base=+0.253)

- **PATRÓN** `volumen_spike_ratio` > `2.309` → IC=+0.300 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.309 (IC base=+0.253)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.285` → IC=+0.214 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.285 (IC base=-0.062)

### LATE_WINDOW_5MIN
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.337 (n=145)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3649` → IC=+0.351 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3649 (IC base=+0.332)

- **PATRÓN** `elapsed_s` > `209.5` → IC=+0.408 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 209.5 (IC base=+0.332)

- **PATRÓN** `drift_15min` |x|≤ `2.8661` → IC=+0.350 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.8661 (IC base=+0.332)

- **PATRÓN** `drift_60min` |x|≤ `1.0022` → IC=+0.385 (n=111)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 1.0022 (IC base=+0.332)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.385 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.332)

- **PATRÓN** `ballena_activa_n` < `1105.0` → IC=+0.397 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1105.0 (IC base=+0.332)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3495` → IC=+0.302 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3495 (IC base=+0.287)

- **PATRÓN** `elapsed_s` > `228.5` → IC=+0.360 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 228.5 (IC base=+0.287)

- **PATRÓN** `drift_15min` |x|≤ `2.3354` → IC=+0.326 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3354 (IC base=+0.287)

- **PATRÓN** `drift_60min` |x|≤ `0.6801` → IC=+0.321 (n=82)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6801 (IC base=+0.287)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.337 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.287)

- **PATRÓN** `ballena_activa_n` < `1335.0` → IC=+0.381 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1335.0 (IC base=+0.287)

### LATE_WINDOW_5MIN#BTC#5min
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.337 (n=145)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3649` → IC=+0.351 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3649 (IC base=+0.332)

- **PATRÓN** `elapsed_s` > `209.5` → IC=+0.408 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 209.5 (IC base=+0.332)

- **PATRÓN** `drift_15min` |x|≤ `2.8661` → IC=+0.350 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.8661 (IC base=+0.332)

- **PATRÓN** `drift_60min` |x|≤ `1.0022` → IC=+0.385 (n=111)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 1.0022 (IC base=+0.332)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.385 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.332)

- **PATRÓN** `ballena_activa_n` < `1105.0` → IC=+0.397 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1105.0 (IC base=+0.332)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3495` → IC=+0.302 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3495 (IC base=+0.287)

- **PATRÓN** `elapsed_s` > `228.5` → IC=+0.360 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 228.5 (IC base=+0.287)

- **PATRÓN** `drift_15min` |x|≤ `2.3354` → IC=+0.326 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3354 (IC base=+0.287)

- **PATRÓN** `drift_60min` |x|≤ `0.6801` → IC=+0.321 (n=82)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6801 (IC base=+0.287)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.337 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.287)

- **PATRÓN** `ballena_activa_n` < `1335.0` → IC=+0.381 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1335.0 (IC base=+0.287)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.123 (n=1487)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` > 0.5 (IC base=+0.097)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.123 (n=1487)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` > 0.5 (IC base=+0.097)

### LIQUIDACIONES_15M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=257)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=257)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=1089)

### LIQUIDACIONES_15M#BNB#15min
- **PATRÓN** `liq_n` > `2.0` → IC=+0.209 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `liq_n` > 2.0 (IC base=+0.072)

- **PATRÓN** `liq_usd_total` > `1217.25` → IC=+0.214 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `liq_usd_total` > 1217.25 (IC base=+0.072)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.175 (n=38)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 6.0 (IC base=+0.072)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.122 (n=80)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.03 (IC base=+0.072)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `libro_liquidez` < `12324.2702` → IC=-0.152 (n=44)

  - _Acción_: SKIP cuando `libro_liquidez` < 12324.2702
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=92)

### LIQUIDACIONES_15M#DOGE#15min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.141 (n=37)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=+0.214 (n=40)

- **FILTRO** `py_entrada` < `0.5` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.094 (n=62)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.214 (n=40)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.044)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `liq_usd_total` < `1802.5` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `liq_usd_total` < 1802.5
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=41)

- **FILTRO** `py_entrada` < `0.415` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.415
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=45)

- **PATRÓN** `liq_usd_total` > `5115.78` → IC=+0.123 (n=136)

  - _Acción_: Kelly boost +0.62€ cuando `liq_usd_total` > 5115.78 (IC base=+0.057)

### LIQUIDACIONES_15M#SOL#15min
- **FILTRO** `hora_utc` > `4.0` → IC=-0.180 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 4.0
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=16)

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
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=4059)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=191)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.080 (n=148)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.278 (n=34)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=178)

- **FILTRO** `ballena_activa_n` > `31.0` → IC=-0.167 (n=88)

  - _Acción_: SKIP cuando `ballena_activa_n` > 31.0
  - _Potencial_: sin este filtro IC_bueno=+0.185 (n=90)

- **PATRÓN** `ballena_activa_n` < `31.0` → IC=+0.185 (n=90)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 31.0 (IC base=-0.028)

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
- **PATRÓN** `liq_n` > `3.0` → IC=+0.289 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `liq_n` > 3.0 (IC base=+0.195)

- **PATRÓN** `liq_usd_total` > `1930.81` → IC=+0.296 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `liq_usd_total` > 1930.81 (IC base=+0.195)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.237 (n=74)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 3.0 (IC base=+0.195)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.201 (n=75)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.195)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.221 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.195)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=1620)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=1574)

- **FILTRO** `hora_utc` > `5.0` → IC=-0.286 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=10)

### LIQUIDACIONES_5M#SOL#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=735)

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
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=522)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=503)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.135 (n=220)

  - _Acción_: Kelly boost +0.68€ cuando `py_entrada` < 0.495 (IC base=+0.007)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=1052)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=1052)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=1369)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=1369)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=309)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=309)

- **FILTRO** `py_entrada` < `0.43` → IC=-0.132 (n=104)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=220)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.136 (n=64)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=378)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=427)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=313)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=415)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=415)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.120 (n=185)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=260)

- **FILTRO** `libro_liquidez` < `565.29` → IC=-0.137 (n=111)

  - _Acción_: SKIP cuando `libro_liquidez` < 565.29
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=334)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=389)

### LIQUIDACIONES_DEPTH_FASE0#BNB#15min
- **FILTRO** `py_entrada` > `0.6` → IC=-0.159 (n=39)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=84)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `hora_utc` > `14.0` → IC=-0.135 (n=94)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=122)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.167 (n=46)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=47)

- **FILTRO** `hora_utc` < `9.0` → IC=-0.267 (n=28)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=65)

### LIQUIDACIONES_DEPTH_FASE0#BTC#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.138 (n=335)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=837)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **FILTRO** `py_entrada` > `0.57` → IC=-0.124 (n=477)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.082 (n=565)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.147 (n=344)

  - _Acción_: Kelly boost +0.74€ cuando `py_entrada` < 0.5 (IC base=-0.013)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.133 (n=178)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=397)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.125 (n=601)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=650)

- **FILTRO** `py_entrada` > `0.58` → IC=-0.122 (n=376)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=449)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.133 (n=303)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=655)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.126 (n=659)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.075 (n=360)

- **FILTRO** `hora_utc` < `7.0` → IC=-0.132 (n=131)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=416)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.41` → IC=-0.159 (n=388)

  - _Acción_: SKIP cuando `py_entrada` < 0.41
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=790)

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
- **FILTRO** `py_entrada` < `0.46` → IC=-0.175 (n=8379)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=26491)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.170 (n=8794)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=27330)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.188 (n=1618)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=4859)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.143 (n=2153)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.094 (n=4254)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.137 (n=1662)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` > 1.0 (IC base=+0.040)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.132 (n=2997)

  - _Acción_: Kelly boost +0.66€ cuando `py_entrada` < 0.5 (IC base=+0.014)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` < `0.44` → IC=-0.175 (n=1167)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=3640)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.180 (n=1242)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=3826)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` > `0.62` → IC=-0.197 (n=1596)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=4964)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.136 (n=1984)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` > 1.0 (IC base=+0.033)

- **PATRÓN** `libro_liquidez` > `1739.0954` → IC=+0.121 (n=2198)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 1739.0954 (IC base=+0.033)

### MOMENTUM_IBS_15M_BALLENA#ETH#15min
- **FILTRO** `py_entrada` > `0.575` → IC=-0.175 (n=1263)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=3895)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.485` → IC=-0.163 (n=1608)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=4895)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=2448)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.162 (n=772)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=2372)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.180 (n=973)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=3145)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=4097)

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
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=1108)

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

- **FILTRO** `libro_liquidez` < `1991.6564` → IC=-0.139 (n=397)

  - _Acción_: SKIP cuando `libro_liquidez` < 1991.6564
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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.135 (n=23736)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.091 (n=53580)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.299 (n=18659)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=58657)

- **FILTRO** `ibs_7min` < `0.2143` → IC=-0.235 (n=19301)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2143
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=58015)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.153 (n=26064)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=51252)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.245 (n=24094)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=72643)

- **FILTRO** `ibs_7min` > `0.28` → IC=-0.182 (n=24170)

  - _Acción_: SKIP cuando `ibs_7min` > 0.28
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=72567)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.159 (n=3324)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=10513)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.320 (n=3419)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=10418)

- **FILTRO** `ibs_7min` < `0.7101` → IC=-0.255 (n=4565)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7101
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=9272)

- **FILTRO** `py_entrada` > `0.72` → IC=-0.278 (n=4063)

  - _Acción_: SKIP cuando `py_entrada` > 0.72
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=12670)

- **FILTRO** `ibs_7min` > `0.7713` → IC=-0.210 (n=4183)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7713
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=12550)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.263 (n=3106)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=9712)

- **FILTRO** `ibs_7min` < `0.7135` → IC=-0.210 (n=3204)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7135
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=9614)

- **FILTRO** `ballena_activa_n` > `156.0` → IC=-0.201 (n=3195)

  - _Acción_: SKIP cuando `ballena_activa_n` > 156.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=9623)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.267 (n=2987)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=10120)

- **FILTRO** `ibs_7min` > `0.2649` → IC=-0.192 (n=3275)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2649
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=9832)

- **FILTRO** `ballena_activa_n` > `152.0` → IC=-0.178 (n=3269)

  - _Acción_: SKIP cuando `ballena_activa_n` > 152.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=9838)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.166 (n=3185)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=10094)

- **FILTRO** `py_entrada` < `0.3` → IC=-0.324 (n=3159)

  - _Acción_: SKIP cuando `py_entrada` < 0.3
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=10120)

- **FILTRO** `ibs_7min` < `0.2895` → IC=-0.250 (n=4382)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2895
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=8897)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.203 (n=2566)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=10713)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.260 (n=4256)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=13456)

- **FILTRO** `ibs_7min` > `0.725` → IC=-0.183 (n=4427)

  - _Acción_: SKIP cuando `ibs_7min` > 0.725
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=13285)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.264 (n=3108)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=9382)

- **FILTRO** `ibs_7min` < `0.7131` → IC=-0.200 (n=3121)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7131
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=9369)

- **FILTRO** `ballena_activa_n` > `24.0` → IC=-0.192 (n=3117)

  - _Acción_: SKIP cuando `ballena_activa_n` > 24.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=9373)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.259 (n=3017)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=9970)

- **FILTRO** `ibs_7min` > `0.2724` → IC=-0.178 (n=3246)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2724
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=9741)

- **FILTRO** `ballena_activa_n` > `23.0` → IC=-0.168 (n=3235)

  - _Acción_: SKIP cuando `ballena_activa_n` > 23.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=9752)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.32` → IC=-0.301 (n=2970)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=9391)

- **FILTRO** `ibs_7min` < `0.7` → IC=-0.235 (n=4068)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=8293)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.219 (n=3022)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=9339)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.199 (n=4491)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=14218)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.133 (n=4054)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.109 (n=8477)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.312 (n=3028)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=9503)

- **FILTRO** `ibs_7min` < `0.73` → IC=-0.223 (n=4131)

  - _Acción_: SKIP cuando `ibs_7min` < 0.73
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=8400)

- **FILTRO** `ballena_activa_n` > `8.0` → IC=-0.191 (n=3131)

  - _Acción_: SKIP cuando `ballena_activa_n` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.092 (n=9400)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.228 (n=4317)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=13172)

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
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=918)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `ballena_activa_n` > `3.0` → IC=-0.143 (n=166)

  - _Acción_: SKIP cuando `ballena_activa_n` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=334)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.231 (n=50)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=451)

- **FILTRO** `py_entrada` > `0.58` → IC=-0.216 (n=192)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=587)

- **FILTRO** `libro_liquidez` < `3305.4837` → IC=-0.148 (n=194)

  - _Acción_: SKIP cuando `libro_liquidez` < 3305.4837
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=585)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.4305` → IC=+0.147 (n=712)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.74€ cuando `delta_ratio` |x|> 0.4305 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.130 (n=1412)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 14.0 (IC base=+0.125)

- **PATRÓN** `total_vol_5m` < `424.4741` → IC=+0.156 (n=521)

  - _Acción_: Kelly boost +0.78€ cuando `total_vol_5m` < 424.4741 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `3557.5792` → IC=+0.139 (n=709)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 3557.5792 (IC base=+0.125)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `14.0` → IC=+0.179 (n=185)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 14.0 (IC base=+0.136)

- **PATRÓN** `total_vol_5m` < `375.759` → IC=+0.160 (n=324)

  - _Acción_: Kelly boost +0.80€ cuando `total_vol_5m` < 375.759 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `2520.4138` → IC=+0.236 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2520.4138 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `6.0` → IC=+0.143 (n=183)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 6.0 (IC base=+0.136)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `delta_ratio` |x|> `0.3994` → IC=+0.135 (n=324)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.67€ cuando `delta_ratio` |x|> 0.3994 (IC base=+0.120)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.139 (n=286)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 14.0 (IC base=+0.120)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4164` → IC=+0.175 (n=195)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.88€ cuando `delta_ratio` |x|> 0.4164 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.151 (n=270)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 5.0 (IC base=+0.130)

- **PATRÓN** `total_vol_5m` < `852.6939` → IC=+0.158 (n=293)

  - _Acción_: Kelly boost +0.79€ cuando `total_vol_5m` < 852.6939 (IC base=+0.130)

- **PATRÓN** `ballena_activa_n` < `59.0` → IC=+0.180 (n=101)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 59.0 (IC base=+0.130)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.3978` → IC=+0.164 (n=263)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.82€ cuando `delta_ratio` |x|> 0.3978 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.168 (n=191)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` < 12.0 (IC base=+0.139)

- **PATRÓN** `total_vol_5m` < `5917.212` → IC=+0.167 (n=232)

  - _Acción_: Kelly boost +0.83€ cuando `total_vol_5m` < 5917.212 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `3737.086` → IC=+0.150 (n=175)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 3737.086 (IC base=+0.139)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `hora_utc` < `14.0` → IC=+0.130 (n=290)
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

- **FILTRO** `sigma_h` < `0.0072` → IC=-0.204 (n=174)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0072
  - _Potencial_: sin este filtro IC_bueno=-0.109 (n=90)

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

- **FILTRO** `pct_vs_K` |x|> `2.06` → IC=-0.390 (n=107)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.06
  - _Potencial_: sin este filtro IC_bueno=+0.118 (n=108)

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

- **FILTRO** `T_h` > `40.3216` → IC=-0.201 (n=105)

  - _Acción_: SKIP cuando `T_h` > 40.3216
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=52)

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
  - _Potencial_: sin este filtro IC_bueno=+0.070 (n=496)

- **PATRÓN** `streak_estiramiento` < `0.8251` → IC=+0.128 (n=342)

  - _Acción_: Kelly boost +0.64€ cuando `streak_estiramiento` < 0.8251 (IC base=+0.059)

- **PATRÓN** `ballena_activa_n` < `29.0` → IC=+0.125 (n=254)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 29.0 (IC base=+0.059)

### STREAK_FADE_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=17)

### STREAK_FADE_15M#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=30)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.154 (n=24)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.154 (n=24)

  - _Acción_: Kelly boost +0.77€ cuando `py_entrada` < 0.495 (IC base=+0.037)

### STREAK_FADE_15M#XRP#15min
- **FILTRO** `streak_estiramiento` > `0.5115` → IC=-0.173 (n=53)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.5115
  - _Potencial_: sin este filtro IC_bueno=+0.094 (n=163)

- **PATRÓN** `streak_estiramiento` < `0.2033` → IC=+0.149 (n=55)

  - _Acción_: Kelly boost +0.75€ cuando `streak_estiramiento` < 0.2033 (IC base=+0.022)

- **PATRÓN** `hora_utc` > `10.0` → IC=+0.145 (n=136)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 10.0 (IC base=+0.090)

- **PATRÓN** `streak_estiramiento` < `0.5763` → IC=+0.165 (n=168)

  - _Acción_: Kelly boost +0.82€ cuando `streak_estiramiento` < 0.5763 (IC base=+0.090)

- **PATRÓN** `ballena_activa_n` < `31.0` → IC=+0.154 (n=163)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 31.0 (IC base=+0.090)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.194 (n=47)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=93)

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
- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=826)

### STREAK_FADE_60M
- **FILTRO** `py_entrada` < `0.515` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.093 (n=25)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=25)

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
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=1307)

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
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=5123)

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
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=2964)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.180 (n=2514)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0065 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.2252` → IC=+0.157 (n=5715)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.2252 (IC base=+0.136)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1331` → IC=+0.149 (n=2359)

  - _Acción_: Kelly boost +0.75€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1331 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.147 (n=5275)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 6.0 (IC base=+0.136)

- **PATRÓN** `ibs_15` > `0.5714` → IC=+0.217 (n=5112)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5714 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.138` → IC=+0.124 (n=2647)

  - _Acción_: Kelly boost +0.62€ cuando `dist_vwap_pct` > 0.138 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.241` → IC=+0.237 (n=1079)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.241 (IC base=+0.136)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=3192)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `4450.0357` → IC=+0.171 (n=1905)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 4450.0357 (IC base=+0.136)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=2243)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.219 (n=823)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.201)

- **PATRÓN** `drift_60min` |x|≤ `0.058` → IC=+0.255 (n=276)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.058 (IC base=+0.201)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2674` → IC=+0.228 (n=274)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2674 (IC base=+0.201)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2264` → IC=+0.210 (n=494)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2264 (IC base=+0.201)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.229 (n=758)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.201)

- **PATRÓN** `ibs_15` > `0.7082` → IC=+0.271 (n=822)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7082 (IC base=+0.201)

- **PATRÓN** `dist_vwap_pct` > `0.3775` → IC=+0.220 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3775 (IC base=+0.201)

- **PATRÓN** `dist_vwap_pct` < `0.1108` → IC=+0.203 (n=560)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1108 (IC base=+0.201)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.345` → IC=+0.306 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.345 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.204 (n=1066)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.201)

- **PATRÓN** `libro_liquidez` > `11817.8916` → IC=+0.220 (n=548)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11817.8916 (IC base=+0.201)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.147 (n=1028)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0071 (IC base=+0.132)

- **PATRÓN** `drift_60min` |x|≤ `0.1094` → IC=+0.150 (n=687)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.1094 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.138 (n=940)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 6.0 (IC base=+0.132)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.132 (n=1033)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 16.0 (IC base=+0.132)

- **PATRÓN** `ibs_15` > `0.4915` → IC=+0.218 (n=1028)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.4915 (IC base=+0.132)

- **PATRÓN** `dist_vwap_pct` > `0.1197` → IC=+0.148 (n=640)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.1197 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.055` → IC=+0.279 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.055 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `6020.1719` → IC=+0.171 (n=466)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 6020.1719 (IC base=+0.132)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `ibs_15` > `0.7627` → IC=+0.129 (n=756)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.65€ cuando `ibs_15` > 0.7627 (IC base=+0.051)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` < `0.0192` → IC=+0.163 (n=968)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0192 (IC base=+0.147)

- **PATRÓN** `sigma_h` > `0.0126` → IC=+0.150 (n=1451)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` > 0.0126 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.2294` → IC=+0.177 (n=1452)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.2294 (IC base=+0.147)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0933` → IC=+0.203 (n=452)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0933 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.154 (n=1332)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 6.0 (IC base=+0.147)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.150 (n=1279)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 14.0 (IC base=+0.147)

- **PATRÓN** `ibs_15` > `0.5333` → IC=+0.218 (n=1300)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5333 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` > `0.2034` → IC=+0.162 (n=654)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 0.2034 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.643` → IC=+0.183 (n=241)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 21.643 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `2936.5659` → IC=+0.191 (n=658)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 2936.5659 (IC base=+0.147)

- **PATRÓN** `ibs_15` < `0.1143` → IC=+0.150 (n=1111)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.75€ cuando `ibs_15` < 0.1143 (IC base=+0.069)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `drift_60min` |x|≤ `0.1105` → IC=+0.365 (n=509)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1105 (IC base=+0.365)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1497` → IC=+0.378 (n=508)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1497 (IC base=+0.365)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1344` → IC=+0.380 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1344 (IC base=+0.365)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.374 (n=805)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.365)

- **PATRÓN** `ibs_15` > `0.7904` → IC=+0.394 (n=763)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7904 (IC base=+0.365)

- **PATRÓN** `dist_vwap_pct` > `0.1529` → IC=+0.381 (n=453)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1529 (IC base=+0.365)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.976` → IC=+0.396 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.976 (IC base=+0.365)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.368 (n=929)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.365)

- **PATRÓN** `libro_liquidez` > `3887.2465` → IC=+0.376 (n=682)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3887.2465 (IC base=+0.365)

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
- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.369 (n=395)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0067 (IC base=+0.365)

- **PATRÓN** `sigma_h` > `0.0061` → IC=+0.384 (n=179)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0061 (IC base=+0.365)

- **PATRÓN** `drift_60min` |x|≤ `0.1066` → IC=+0.368 (n=264)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1066 (IC base=+0.365)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1291` → IC=+0.383 (n=263)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1291 (IC base=+0.365)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2951` → IC=+0.374 (n=323)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2951 (IC base=+0.365)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.372 (n=396)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.365)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.371 (n=184)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.365)

- **PATRÓN** `ibs_15` > `0.764` → IC=+0.394 (n=395)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.764 (IC base=+0.365)

- **PATRÓN** `dist_vwap_pct` > `0.1581` → IC=+0.375 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1581 (IC base=+0.365)

- **PATRÓN** `dist_vwap_pct` < `0.6387` → IC=+0.367 (n=450)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6387 (IC base=+0.365)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.991` → IC=+0.394 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.991 (IC base=+0.365)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.369 (n=448)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.365)

- **PATRÓN** `libro_liquidez` > `4202.8422` → IC=+0.379 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4202.8422 (IC base=+0.365)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0076` → IC=-0.203 (n=2793)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0076
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=2795)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.221 (n=2377)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=3211)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1404` → IC=+0.217 (n=478)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1404 (IC base=-0.085)

- **PATRÓN** `ibs_15` > `0.6314` → IC=+0.274 (n=1257)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6314 (IC base=-0.085)

- **PATRÓN** `dist_vwap_pct` > `0.1115` → IC=+0.198 (n=733)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.1115 (IC base=-0.085)

- **PATRÓN** `dist_vwap_pct` < `0.4183` → IC=+0.198 (n=1243)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` < 0.4183 (IC base=-0.085)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2323` → IC=+0.272 (n=1734)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2323 (IC base=-0.002)

- **PATRÓN** `ibs_15` < `0.3705` → IC=+0.286 (n=5202)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3705 (IC base=-0.002)

- **PATRÓN** `dist_vwap_pct` > `0.6715` → IC=+0.283 (n=723)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6715 (IC base=-0.002)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0433` → IC=-0.226 (n=2418)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0433
  - _Potencial_: sin este filtro IC_bueno=-0.098 (n=1191)

- **FILTRO** `sigma_ewma_delta_pct` > `22.182` → IC=-0.250 (n=510)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 22.182
  - _Potencial_: sin este filtro IC_bueno=-0.173 (n=3099)

- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.147 (n=341)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0031 (IC base=+0.068)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2668` → IC=+0.281 (n=149)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2668 (IC base=+0.068)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.145` → IC=+0.268 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.145 (IC base=+0.068)

- **PATRÓN** `ibs_15` > `0.7639` → IC=+0.314 (n=445)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7639 (IC base=+0.068)

- **PATRÓN** `dist_vwap_pct` > `0.1043` → IC=+0.274 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1043 (IC base=+0.068)

- **PATRÓN** `dist_vwap_pct` < `0.3693` → IC=+0.278 (n=462)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3693 (IC base=+0.068)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.006` → IC=+0.149 (n=226)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 22.006 (IC base=+0.068)

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
  - _Potencial_: sin este filtro IC_bueno=+0.151 (n=820)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.160 (n=553)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0059 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.159` → IC=+0.163 (n=553)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.159 (IC base=+0.145)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3014` → IC=+0.195 (n=493)

  - _Acción_: Kelly boost +0.97€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3014 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.162 (n=448)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 11.0 (IC base=+0.145)

- **PATRÓN** `ibs_15` > `0.5684` → IC=+0.238 (n=628)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5684 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` > `0.6245` → IC=+0.155 (n=117)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.6245 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` < `0.4449` → IC=+0.147 (n=666)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.4449 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.973` → IC=+0.260 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.973 (IC base=+0.145)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.151 (n=820)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.01 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `7295.1819` → IC=+0.162 (n=285)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 7295.1819 (IC base=+0.145)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.255 (n=1363)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0062 (IC base=+0.244)

- **PATRÓN** `drift_60min` |x|≤ `0.4584` → IC=+0.247 (n=2044)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4584 (IC base=+0.244)

- **PATRÓN** `drift_15min` |x|≤ `0.7948` → IC=+0.257 (n=1798)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7948 (IC base=+0.244)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2091` → IC=+0.268 (n=927)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2091 (IC base=+0.244)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.257 (n=750)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.244)

- **PATRÓN** `ibs_15` < `0.3849` → IC=+0.273 (n=2044)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3849 (IC base=+0.244)

- **PATRÓN** `dist_vwap_pct` > `0.3875` → IC=+0.276 (n=499)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3875 (IC base=+0.244)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.409` → IC=+0.251 (n=788)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.409 (IC base=+0.244)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1886` → IC=-0.279 (n=328)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1886
  - _Potencial_: sin este filtro IC_bueno=-0.176 (n=987)

- **FILTRO** `drift_60min` |x|> `0.1726` → IC=-0.268 (n=447)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1726
  - _Potencial_: sin este filtro IC_bueno=-0.168 (n=868)

- **FILTRO** `drift_15min` |x|> `0.9292` → IC=-0.291 (n=328)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.9292
  - _Potencial_: sin este filtro IC_bueno=-0.172 (n=987)

- **FILTRO** `sigma_ewma_delta_pct` > `6.067` → IC=-0.204 (n=292)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.067
  - _Potencial_: sin este filtro IC_bueno=-0.202 (n=1023)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1478` → IC=+0.188 (n=46)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.94€ cuando `delta_ratio_macro` |x|> 0.1478 (IC base=-0.202)

- **PATRÓN** `ibs_15` > `0.9231` → IC=+0.380 (n=23)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9231 (IC base=-0.202)

- **PATRÓN** `dist_vwap_pct` < `0.4298` → IC=+0.158 (n=77)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.4298 (IC base=-0.202)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.194 (n=34)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 37.0 (IC base=-0.202)

- **PATRÓN** `ibs_15` < `0.381` → IC=+0.295 (n=894)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.381 (IC base=-0.027)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1177` → IC=-0.263 (n=796)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1177
  - _Potencial_: sin este filtro IC_bueno=-0.178 (n=797)

- **FILTRO** `sigma_h` > `0.0155` → IC=-0.248 (n=1067)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0155
  - _Potencial_: sin este filtro IC_bueno=-0.165 (n=526)

- **FILTRO** `drift_15min` |x|> `1.2816` → IC=-0.280 (n=398)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.2816
  - _Potencial_: sin este filtro IC_bueno=-0.201 (n=1195)

- **FILTRO** `libro_spread` > `0.04` → IC=-0.273 (n=20)

  - _Acción_: SKIP cuando `libro_spread` > 0.04
  - _Potencial_: sin este filtro IC_bueno=-0.220 (n=1573)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.221)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.221)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0719` → IC=+0.281 (n=1110)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0719 (IC base=-0.012)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1185` → IC=+0.299 (n=540)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1185 (IC base=-0.012)

- **PATRÓN** `ibs_15` < `0.1385` → IC=+0.313 (n=828)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.1385 (IC base=-0.012)

- **PATRÓN** `dist_vwap_pct` > `0.7684` → IC=+0.340 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7684 (IC base=-0.012)

### UPDOWN_GBM_ETH_15M_HORA7
- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.149 (n=55)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0067 (IC base=+0.087)

- **PATRÓN** `drift_60min` |x|≤ `0.1094` → IC=+0.141 (n=37)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.1094 (IC base=+0.087)

- **PATRÓN** `drift_15min` |x|≤ `0.7315` → IC=+0.149 (n=55)

  - _Acción_: Kelly boost +0.75€ cuando `drift_15min` |x|≤ 0.7315 (IC base=+0.087)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.15` → IC=+0.180 (n=23)

  - _Acción_: Kelly boost +0.90€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.15 (IC base=+0.087)

- **PATRÓN** `ibs_15` > `0.8407` → IC=+0.315 (n=25)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8407 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` < `0.0949` → IC=+0.206 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0949 (IC base=+0.087)

- **PATRÓN** `ballena_activa_n` < `116.0` → IC=+0.130 (n=52)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 116.0 (IC base=+0.087)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.149 (n=55)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0067 (IC base=+0.087)

- **PATRÓN** `drift_60min` |x|≤ `0.1094` → IC=+0.141 (n=37)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.1094 (IC base=+0.087)

- **PATRÓN** `drift_15min` |x|≤ `0.7315` → IC=+0.149 (n=55)

  - _Acción_: Kelly boost +0.75€ cuando `drift_15min` |x|≤ 0.7315 (IC base=+0.087)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.15` → IC=+0.180 (n=23)

  - _Acción_: Kelly boost +0.90€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.15 (IC base=+0.087)

- **PATRÓN** `ibs_15` > `0.8407` → IC=+0.315 (n=25)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8407 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` < `0.0949` → IC=+0.206 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0949 (IC base=+0.087)

- **PATRÓN** `ballena_activa_n` < `116.0` → IC=+0.130 (n=52)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 116.0 (IC base=+0.087)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.297 (n=466)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0033 (IC base=+0.281)

- **PATRÓN** `drift_60min` |x|≤ `0.0712` → IC=+0.309 (n=615)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0712 (IC base=+0.281)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1515` → IC=+0.283 (n=930)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1515 (IC base=+0.281)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2214` → IC=+0.289 (n=853)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2214 (IC base=+0.281)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.293 (n=1451)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.281)

- **PATRÓN** `ibs_15` > `0.8379` → IC=+0.310 (n=1396)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8379 (IC base=+0.281)

- **PATRÓN** `dist_vwap_pct` > `0.2676` → IC=+0.309 (n=601)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2676 (IC base=+0.281)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.916` → IC=+0.386 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.916 (IC base=+0.281)

- **PATRÓN** `libro_liquidez` > `13134.4548` → IC=+0.301 (n=466)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13134.4548 (IC base=+0.281)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.304 (n=325)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.274)

- **PATRÓN** `drift_60min` |x|≤ `0.0763` → IC=+0.302 (n=326)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0763 (IC base=+0.274)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2694` → IC=+0.282 (n=246)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2694 (IC base=+0.274)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2298` → IC=+0.280 (n=444)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2298 (IC base=+0.274)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.292 (n=777)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.274)

- **PATRÓN** `ibs_15` > `0.9198` → IC=+0.326 (n=492)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9198 (IC base=+0.274)

- **PATRÓN** `dist_vwap_pct` > `0.2546` → IC=+0.309 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2546 (IC base=+0.274)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.738` → IC=+0.391 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.738 (IC base=+0.274)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.275 (n=955)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.274)

- **PATRÓN** `libro_liquidez` > `15709.5063` → IC=+0.315 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15709.5063 (IC base=+0.274)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.007` → IC=+0.294 (n=658)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.007 (IC base=+0.288)

- **PATRÓN** `sigma_h` > `0.0054` → IC=+0.291 (n=439)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0054 (IC base=+0.288)

- **PATRÓN** `drift_60min` |x|≤ `0.109` → IC=+0.309 (n=439)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.109 (IC base=+0.288)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0654` → IC=+0.291 (n=658)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0654 (IC base=+0.288)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1008` → IC=+0.312 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1008 (IC base=+0.288)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.298 (n=633)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.288)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.288 (n=466)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.288)

- **PATRÓN** `ibs_15` > `0.8466` → IC=+0.318 (n=658)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8466 (IC base=+0.288)

- **PATRÓN** `dist_vwap_pct` > `0.2788` → IC=+0.315 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2788 (IC base=+0.288)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.243` → IC=+0.374 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.243 (IC base=+0.288)

### UPDOWN_OU_5M
- **FILTRO** `delta_ratio_macro` |x|≤ `0.126` → IC=-0.156 (n=94)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.126
  - _Potencial_: sin este filtro IC_bueno=-0.102 (n=287)

- **FILTRO** `ballena_activa_n` > `47.0` → IC=-0.138 (n=233)

  - _Acción_: SKIP cuando `ballena_activa_n` > 47.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=116)

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
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.0773` → IC=-0.243 (n=33)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.0773
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=17)

- **FILTRO** `ballena_activa_n` > `42.0` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `ballena_activa_n` > 42.0
  - _Potencial_: sin este filtro IC_bueno=-0.105 (n=36)

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

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5714 sube el IC de +0.136 a +0.217 en UPDOWN_GBM#15min (n=5112). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7082 sube el IC de +0.201 a +0.271 en UPDOWN_GBM#BTC#15min (n=822). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.4915 sube el IC de +0.132 a +0.218 en UPDOWN_GBM#ETH#15min (n=1028). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5333 sube el IC de +0.147 a +0.218 en UPDOWN_GBM#XRP#15min (n=1300). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6314 sube el IC de -0.085 a +0.274 en UPDOWN_GBM_15M_TARDIO (n=1257). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3705 sube el IC de -0.002 a +0.286 en UPDOWN_GBM_15M_TARDIO (n=5202). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7639 sube el IC de +0.068 a +0.314 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=445). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.6255 sube el IC de -0.184 a +0.289 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=74). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.5684 sube el IC de +0.145 a +0.238 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=628). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3849 sube el IC de +0.244 a +0.273 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=2044). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.9231 sube el IC de -0.202 a +0.380 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=23). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.381 sube el IC de -0.027 a +0.295 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=894). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.221 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.1385 sube el IC de -0.012 a +0.313 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=828). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_YES, IBS > 0.8407 sube el IC de +0.087 a +0.315 en UPDOWN_GBM_ETH_15M_HORA7 (n=25). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_YES, IBS > 0.8407 sube el IC de +0.087 a +0.315 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=25). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8379 sube el IC de +0.281 a +0.310 en UPDOWN_GBM_IBS_ALTO (n=1396). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.9198 sube el IC de +0.274 a +0.326 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=492). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8466 sube el IC de +0.288 a +0.318 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=658). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7904 sube el IC de +0.365 a +0.394 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=763). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8078 sube el IC de +0.362 a +0.384 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=369). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.764 sube el IC de +0.365 a +0.394 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=395). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 2213 | +0.082 | +216.46€ | 1 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 2213 | +0.082 | +216.46€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1803 | +0.082 | +177.92€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1803 | +0.082 | +177.92€ | 1 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 285 | +0.068 | +10.79€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 285 | +0.068 | +10.79€ | 5 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 94 | +0.125 | +28.08€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 94 | +0.125 | +28.08€ | 1 | 9 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 1205 | -0.015 | +76.31€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 1205 | -0.015 | +76.31€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE | 7 | +0.019 | +3.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE#15min | 7 | +0.019 | +3.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 918 | -0.032 | +55.38€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 918 | -0.032 | +55.38€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 195 | +0.064 | +24.17€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 195 | +0.064 | +24.17€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 85 | -0.017 | -6.49€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 85 | -0.017 | -6.49€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 48790 | -0.084 | -6254.53€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 3075 | +0.080 | -304.52€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 45715 | -0.095 | -5950.01€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4885 | -0.111 | -818.96€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4885 | -0.111 | -818.96€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 3075 | +0.080 | -304.52€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 3075 | +0.080 | -304.52€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 4962 | -0.103 | -923.28€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 4962 | -0.103 | -923.28€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 13381 | -0.042 | -1316.66€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 13381 | -0.042 | -1316.66€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 13291 | -0.112 | -1365.72€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 13291 | -0.112 | -1365.72€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 9196 | -0.136 | -1525.39€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 9196 | -0.136 | -1525.39€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 51534 | -0.012 | +2796.98€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 13302 | +0.004 | +1486.94€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 38232 | -0.018 | +1310.04€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 51534 | -0.012 | +2796.98€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 13302 | +0.004 | +1486.94€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 38232 | -0.018 | +1310.04€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 195621 | +0.112 | -8202.26€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#15min | 22252 | +0.180 | -702.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 901 | +0.015 | -72.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 161332 | +0.105 | -7021.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 11136 | +0.094 | -406.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 26736 | +0.102 | -1909.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 80 | -0.171 | +14.55€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 26641 | +0.103 | -1911.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 36912 | +0.123 | -652.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5625 | +0.178 | -235.00€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 26705 | +0.119 | -227.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 4540 | +0.080 | -168.47€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 26784 | +0.098 | -1948.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 90 | -0.109 | +14.44€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 26679 | +0.099 | -1952.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 41808 | +0.123 | -890.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 10476 | +0.178 | -257.58€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 27131 | +0.105 | -559.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 4189 | +0.103 | -64.68€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#SOL | 36616 | +0.111 | -1645.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 5888 | +0.198 | -253.40€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 804 | +0.041 | -18.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 27517 | +0.095 | -1200.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 2407 | +0.104 | -172.98€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO#XRP | 26765 | +0.107 | -1155.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 93 | -0.121 | +14.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 26659 | +0.108 | -1169.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 31731 | +0.191 | -2264.81€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 31731 | +0.191 | -2264.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 7188 | +0.167 | -773.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 7188 | +0.167 | -773.79€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 4644 | +0.196 | -182.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 4644 | +0.196 | -182.66€ | 3 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 7041 | +0.173 | -636.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 7041 | +0.173 | -636.19€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 5869 | +0.252 | -201.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 5869 | +0.252 | -201.80€ | 0 | 4 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 6910 | +0.184 | -484.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 6910 | +0.184 | -484.12€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 1273 | +0.425 | -47.05€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 1273 | +0.425 | -47.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 528 | +0.440 | -4.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 528 | +0.440 | -4.15€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE#15min | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 518 | +0.423 | -20.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 518 | +0.423 | -20.66€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 213 | +0.398 | -18.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 213 | +0.398 | -18.37€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 112281 | +0.199 | -8323.15€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 112281 | +0.199 | -8323.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 19437 | +0.177 | -2262.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 19437 | +0.177 | -2262.39€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 18103 | +0.223 | -621.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 18103 | +0.223 | -621.34€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 19276 | +0.180 | -2043.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 19276 | +0.180 | -2043.57€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 18255 | +0.217 | -739.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 18255 | +0.217 | -739.06€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 18532 | +0.204 | -1149.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 18532 | +0.204 | -1149.10€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 18678 | +0.196 | -1507.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 18678 | +0.196 | -1507.69€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 43466 | +0.116 | +346.06€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 43466 | +0.116 | +346.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 21642 | +0.117 | +199.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 21642 | +0.117 | +199.12€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 21824 | +0.116 | +146.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 21824 | +0.116 | +146.95€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 2663 | +0.292 | -18.79€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 2663 | +0.292 | -18.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 1215 | +0.281 | -30.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 1215 | +0.281 | -30.59€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 1306 | +0.295 | +5.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 1306 | +0.295 | +5.08€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 142 | +0.347 | +6.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 142 | +0.347 | +6.73€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 1228 | +0.437 | -7.04€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 1228 | +0.437 | -7.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 586 | +0.434 | -9.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 586 | +0.434 | -9.01€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 590 | +0.441 | +0.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 590 | +0.441 | +0.56€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 52 | +0.407 | +1.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 52 | +0.407 | +1.41€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1972 | +0.066 | -92.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 725 | +0.046 | -64.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 1247 | +0.078 | -27.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1538 | +0.073 | -46.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 291 | +0.053 | -19.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 1247 | +0.078 | -27.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 88332 | +0.100 | -2042.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 7136 | +0.097 | +162.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 81196 | +0.101 | -2204.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 48260 | +0.105 | -467.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 7136 | +0.097 | +162.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 41124 | +0.106 | -630.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 18854 | +0.109 | -83.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 18854 | +0.109 | -83.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 21218 | +0.082 | -1491.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 21218 | +0.082 | -1491.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 914 | +0.186 | -109.27€ | 5 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 914 | +0.186 | -109.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 914 | +0.186 | -109.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 914 | +0.186 | -109.27€ | 5 | 4 |
| ✅ GBM_LATE_15M | 59974 | +0.101 | +33630.85€ | 0 | 18 |
| ✅ GBM_LATE_15M#15min | 59974 | +0.101 | +33630.85€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 9932 | +0.225 | +8569.89€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 9932 | +0.225 | +8569.89€ | 0 | 22 |
| ✅ GBM_LATE_15M#BTC | 9257 | +0.177 | +7344.93€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 9257 | +0.177 | +7344.93€ | 0 | 20 |
| ✅ GBM_LATE_15M#DOGE | 10743 | +0.208 | +8512.57€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 10743 | +0.208 | +8512.57€ | 0 | 20 |
| ✅ GBM_LATE_15M#ETH | 8010 | +0.058 | +2647.44€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 8010 | +0.058 | +2647.44€ | 1 | 15 |
| ✅ GBM_LATE_15M#SOL | 8349 | -0.028 | +2178.21€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 8349 | -0.028 | +2178.21€ | 4 | 13 |
| ✅ GBM_LATE_15M#XRP | 13683 | -0.020 | +4377.82€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 13683 | -0.020 | +4377.82€ | 3 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 63444 | +0.086 | +36927.93€ | 0 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 63444 | +0.086 | +36927.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 12277 | -0.002 | +6519.23€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 12277 | -0.002 | +6519.23€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 13645 | +0.005 | +3694.59€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 13645 | +0.005 | +3694.59€ | 0 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 8595 | +0.295 | +9843.43€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 8595 | +0.295 | +9843.43€ | 0 | 21 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 12091 | +0.015 | +3795.14€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 12091 | +0.015 | +3795.14€ | 1 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 9718 | +0.045 | +4361.40€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 9718 | +0.045 | +4361.40€ | 3 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 7118 | +0.315 | +8714.14€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 7118 | +0.315 | +8714.14€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 47326 | +0.179 | +39277.50€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 47326 | +0.179 | +39277.50€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 7131 | +0.240 | +6660.62€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 7131 | +0.240 | +6660.62€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 7509 | +0.141 | +5603.73€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 7509 | +0.141 | +5603.73€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 7610 | +0.225 | +6631.96€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 7610 | +0.225 | +6631.96€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 8116 | +0.130 | +6300.91€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 8116 | +0.130 | +6300.91€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 8944 | +0.121 | +6790.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 8944 | +0.121 | +6790.93€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 8016 | +0.234 | +7289.36€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 8016 | +0.234 | +7289.36€ | 0 | 26 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 12975 | +0.126 | +6560.19€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 12975 | +0.126 | +6560.19€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 669 | +0.162 | +439.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 669 | +0.162 | +439.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 3461 | +0.126 | +1880.82€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 3461 | +0.126 | +1880.82€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 507 | +0.158 | +290.79€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 507 | +0.158 | +290.79€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 3733 | +0.125 | +1822.17€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 3733 | +0.125 | +1822.17€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 3375 | +0.100 | +1357.96€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 3375 | +0.100 | +1357.96€ | 0 | 12 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 1230 | +0.167 | +768.64€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 1230 | +0.167 | +768.64€ | 0 | 26 |
| ✅ GBM_LATE_15M_TARDIO | 60186 | +0.189 | +49826.30€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#15min | 60186 | +0.189 | +49826.30€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 9497 | +0.250 | +9183.53€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 9497 | +0.250 | +9183.53€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 9610 | +0.140 | +6775.05€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 9610 | +0.140 | +6775.05€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 10211 | +0.235 | +9248.07€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 10211 | +0.235 | +9248.07€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 9969 | +0.143 | +7431.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 9969 | +0.143 | +7431.08€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 10655 | +0.125 | +7630.96€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 10655 | +0.125 | +7630.96€ | 0 | 18 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 10244 | +0.242 | +9557.60€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 10244 | +0.242 | +9557.60€ | 0 | 21 |
| ✅ GBM_LATE_5M | 15509 | +0.216 | +12889.46€ | 0 | 27 |
| ✅ GBM_LATE_5M#5min | 15509 | +0.216 | +12889.46€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 1690 | +0.248 | +1614.53€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 1690 | +0.248 | +1614.53€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 3286 | +0.211 | +2831.05€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 3286 | +0.211 | +2831.05€ | 0 | 25 |
| ✅ GBM_LATE_5M#DOGE | 1453 | +0.210 | +1160.11€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1453 | +0.210 | +1160.11€ | 0 | 19 |
| ✅ GBM_LATE_5M#ETH | 4359 | +0.204 | +3295.25€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 4359 | +0.204 | +3295.25€ | 0 | 25 |
| ✅ GBM_LATE_5M#SOL | 2705 | +0.226 | +2399.09€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 2705 | +0.226 | +2399.09€ | 0 | 25 |
| ✅ GBM_LATE_5M#XRP | 2016 | +0.209 | +1589.43€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 2016 | +0.209 | +1589.43€ | 0 | 0 |
| ✅ GBM_LATE_60M | 5391 | +0.055 | +1464.05€ | 0 | 6 |
| ✅ GBM_LATE_60M#60min | 5391 | +0.055 | +1464.05€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 1861 | +0.059 | +550.74€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 1861 | +0.059 | +550.74€ | 1 | 6 |
| ✅ GBM_LATE_60M#ETH | 1718 | +0.055 | +545.81€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 1718 | +0.055 | +545.81€ | 1 | 7 |
| ✅ GBM_LATE_60M#SOL | 1812 | +0.051 | +367.49€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 1812 | +0.051 | +367.49€ | 0 | 9 |
| 🚫 GBM_LATE_60M_FADE | 724 | -0.249 | -35.03€ | 8 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 724 | -0.249 | -35.03€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 261 | -0.253 | -19.53€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 261 | -0.253 | -19.53€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 262 | -0.242 | -6.68€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 262 | -0.242 | -6.68€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 201 | -0.249 | -8.83€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 201 | -0.249 | -8.83€ | 7 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 2219 | +0.084 | +556.31€ | 1 | 9 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 2219 | +0.084 | +556.31€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 854 | +0.069 | +190.29€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 854 | +0.069 | +190.29€ | 1 | 5 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 763 | +0.054 | +147.51€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 763 | +0.054 | +147.51€ | 2 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 602 | +0.141 | +218.51€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 602 | +0.141 | +218.51€ | 1 | 10 |
| ✅ LATE_WINDOW_5MIN | 309 | +0.310 | +369.09€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 309 | +0.310 | +369.09€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 309 | +0.310 | +369.09€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 309 | +0.310 | +369.09€ | 1 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 4470 | +0.096 | +1004.50€ | 0 | 1 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 4470 | +0.096 | +1004.50€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 4470 | +0.096 | +1004.50€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 4470 | +0.096 | +1004.50€ | 0 | 1 |
| ✅ LIQUIDACIONES_15M | 1383 | +0.011 | +58.27€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 1383 | +0.011 | +58.27€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 137 | +0.068 | +20.82€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 137 | +0.068 | +20.82€ | 0 | 4 |
| ✅ LIQUIDACIONES_15M#BTC | 290 | +0.000 | +10.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 290 | +0.000 | +10.46€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 87 | -0.006 | +2.77€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 87 | -0.006 | +2.77€ | 2 | 1 |
| ✅ LIQUIDACIONES_15M#ETH | 331 | +0.025 | +21.42€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 331 | +0.025 | +21.42€ | 2 | 1 |
| ✅ LIQUIDACIONES_15M#SOL | 331 | -0.011 | +3.10€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 331 | -0.011 | +3.10€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 207 | +0.007 | -0.30€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 207 | +0.007 | -0.30€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 4356 | +0.016 | +148.57€ | 5 | 1 |
| ✅ LIQUIDACIONES_5M#5min | 4356 | +0.016 | +148.57€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 239 | +0.006 | -5.14€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 239 | +0.006 | -5.14€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 827 | +0.015 | +40.58€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 827 | +0.015 | +40.58€ | 2 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 290 | +0.048 | +54.27€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 290 | +0.048 | +54.27€ | 0 | 5 |
| ✅ LIQUIDACIONES_5M#ETH | 1672 | +0.018 | +28.21€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1672 | +0.018 | +28.21€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 776 | +0.013 | +3.99€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 776 | +0.013 | +3.99€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 552 | +0.002 | +26.67€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 552 | +0.002 | +26.67€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 2516 | -0.032 | -3.09€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 2516 | -0.032 | -3.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 766 | -0.029 | -9.55€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 766 | -0.029 | -9.55€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 901 | -0.008 | +22.01€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 901 | -0.008 | +22.01€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 849 | -0.059 | -15.56€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 849 | -0.059 | -15.56€ | 5 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 17593 | -0.034 | -241.20€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 8467 | -0.035 | -130.22€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 9126 | -0.032 | -110.98€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 630 | -0.059 | -43.68€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 321 | -0.039 | -6.92€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 309 | -0.079 | -36.77€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 4622 | -0.029 | -50.36€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 2188 | -0.025 | -1.73€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 2434 | -0.032 | -48.63€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 1681 | -0.033 | -3.76€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 855 | -0.044 | -25.37€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 826 | -0.022 | +21.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 3983 | -0.034 | -66.19€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 1907 | -0.032 | -20.95€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 2076 | -0.035 | -45.24€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 3365 | -0.024 | +39.52€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 1630 | -0.029 | -1.63€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 1735 | -0.018 | +41.15€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 3312 | -0.046 | -116.73€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 1566 | -0.052 | -73.63€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 1746 | -0.041 | -43.10€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 70994 | +0.000 | +3859.60€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 70994 | +0.000 | +3859.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 12884 | +0.027 | +1794.40€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 12884 | +0.027 | +1794.40€ | 2 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 9875 | -0.038 | -153.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 9875 | -0.038 | -153.75€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 13024 | +0.026 | +1468.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 13024 | +0.026 | +1468.56€ | 1 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 9851 | -0.052 | -248.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 9851 | -0.052 | -248.97€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 12112 | -0.004 | +339.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 12112 | -0.004 | +339.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 13248 | +0.019 | +659.48€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 13248 | +0.019 | +659.48€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 7263 | -0.053 | -108.59€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 7263 | -0.053 | -108.59€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1269 | -0.001 | -13.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1269 | -0.001 | -13.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 2016 | -0.060 | -20.28€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 2016 | -0.060 | -20.28€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 93 | -0.016 | +0.13€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 93 | -0.016 | +0.13€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 811 | -0.119 | -34.68€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 811 | -0.119 | -34.68€ | 5 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 2207 | -0.067 | -12.58€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 2207 | -0.067 | -12.58€ | 2 | 0 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 174053 | -0.077 | +2516.53€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 174053 | -0.077 | +2516.53€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 30570 | -0.077 | +1818.01€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 30570 | -0.077 | +1818.01€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 25925 | -0.100 | -1203.41€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 25925 | -0.100 | -1203.41€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 30991 | -0.067 | +1530.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 30991 | -0.067 | +1530.71€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 25477 | -0.099 | -839.14€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 25477 | -0.099 | -839.14€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 31070 | -0.059 | +275.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 31070 | -0.059 | +275.31€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 30020 | -0.068 | +935.06€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 30020 | -0.068 | +935.06€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 9154 | -0.035 | -178.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 9154 | -0.035 | -178.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 1008 | -0.017 | -19.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 1008 | -0.017 | -19.32€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 2126 | -0.046 | -27.33€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 2126 | -0.046 | -27.33€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2669 | -0.024 | -33.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2669 | -0.024 | -33.87€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1280 | -0.063 | -30.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1280 | -0.063 | -30.88€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 1062 | -0.034 | -35.44€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 1062 | -0.034 | -35.44€ | 0 | 0 |
| ✅ ORDER_FLOW_5M | 2219 | +0.121 | +892.57€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#5min | 2083 | +0.125 | +879.97€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 490 | +0.136 | +243.21€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 490 | +0.136 | +243.21€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#DOGE | 432 | +0.120 | +155.22€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 432 | +0.120 | +155.22€ | 0 | 2 |
| ✅ ORDER_FLOW_5M#ETH | 390 | +0.130 | +182.02€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 390 | +0.130 | +182.02€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 350 | +0.139 | +176.88€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 350 | +0.139 | +176.88€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#XRP | 421 | +0.098 | +122.63€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 421 | +0.098 | +122.63€ | 0 | 2 |
| ✅ ORDER_FLOW_5M_REACTIVO | 2303 | -0.018 | -22.48€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 2303 | -0.018 | -22.48€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 415 | +0.011 | +22.53€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 415 | +0.011 | +22.53€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 425 | -0.043 | -23.62€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 425 | -0.043 | -23.62€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 569 | -0.043 | -37.02€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 569 | -0.043 | -37.02€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 468 | +0.006 | +11.31€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 468 | +0.006 | +11.31€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 426 | -0.014 | +4.31€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 426 | -0.014 | +4.31€ | 0 | 0 |
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
| ✅ PRICE_TARGET_GBM_FADE | 1522 | -0.198 | -68.41€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 598 | -0.192 | -32.30€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 528 | -0.189 | -27.85€ | 5 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#reach | 70 | -0.208 | -4.45€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 509 | -0.204 | -36.81€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 447 | -0.215 | -43.96€ | 4 | 1 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 62 | -0.125 | +7.14€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 415 | -0.195 | +0.71€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 385 | -0.193 | -1.44€ | 6 | 0 |
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
| ✅ STREAK_FADE_15M | 988 | +0.036 | +77.48€ | 2 | 2 |
| ✅ STREAK_FADE_15M#15min | 988 | +0.036 | +77.48€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 359 | +0.015 | +2.34€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 359 | +0.015 | +2.34€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 76 | +0.013 | +0.02€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 76 | +0.013 | +0.02€ | 1 | 0 |
| ✅ STREAK_FADE_15M#SOL | 84 | +0.023 | +7.13€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 84 | +0.023 | +7.13€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 469 | +0.058 | +67.99€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 469 | +0.058 | +67.99€ | 1 | 4 |
| ✅ STREAK_FADE_5M | 3611 | -0.023 | -142.21€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3611 | -0.023 | -142.21€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 1127 | -0.023 | -40.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 1127 | -0.023 | -40.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 620 | -0.027 | -26.54€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 620 | -0.027 | -26.54€ | 1 | 0 |
| ✅ STREAK_FADE_5M#SOL | 173 | -0.043 | -14.79€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 173 | -0.043 | -14.79€ | 4 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1691 | -0.019 | -60.68€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1691 | -0.019 | -60.68€ | 1 | 0 |
| ✅ STREAK_FADE_60M | 125 | -0.035 | -12.61€ | 3 | 0 |
| ✅ STREAK_FADE_60M#60min | 125 | -0.035 | -12.61€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 46 | -0.062 | -3.71€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 46 | -0.062 | -3.71€ | 4 | 0 |
| ✅ STREAK_FADE_60M#SOL | 79 | -0.018 | -8.89€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 79 | -0.018 | -8.89€ | 0 | 1 |
| ✅ STREAK_MOM_5M | 11573 | +0.014 | +72.34€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 11573 | +0.014 | +72.34€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2995 | +0.018 | +24.38€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2995 | +0.018 | +24.38€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 3050 | +0.015 | +31.69€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 3050 | +0.015 | +31.69€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2935 | +0.008 | -3.04€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2935 | +0.008 | -3.04€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2593 | +0.014 | +19.31€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2593 | +0.014 | +19.31€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 12503 | +0.018 | -0.60€ | 4 | 0 |
| ✅ STRUCT_NO_15M#15min | 12503 | +0.018 | -0.60€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 5142 | +0.021 | +4.44€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 5142 | +0.021 | +4.44€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 4363 | +0.018 | -1.39€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 4363 | +0.018 | -1.39€ | 4 | 0 |
| ✅ STRUCT_NO_15M#SOL | 2998 | +0.014 | -3.65€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 2998 | +0.014 | -3.65€ | 1 | 0 |
| ✅ UPDOWN_GBM | 113428 | +0.060 | +10771.94€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 27632 | +0.078 | +5472.32€ | 0 | 9 |
| ✅ UPDOWN_GBM#240min | 3293 | -0.001 | +35.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 75364 | +0.062 | +5154.28€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 6756 | -0.002 | +119.31€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 9726 | +0.103 | +1749.57€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1782 | +0.163 | +818.90€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 90 | -0.011 | -2.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 7854 | +0.091 | +932.67€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 25747 | +0.058 | +2291.23€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 3714 | +0.080 | +832.14€ | 0 | 11 |
| ✅ UPDOWN_GBM#BTC#240min | 950 | -0.001 | +18.76€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 17937 | +0.068 | +1361.25€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 3007 | -0.005 | +76.54€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 139 | -0.067 | +2.53€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 12417 | +0.076 | +1355.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1763 | +0.154 | +737.64€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 86 | +0.023 | -0.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 10568 | +0.063 | +618.91€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 26752 | +0.050 | +1892.33€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 6513 | +0.072 | +1005.51€ | 0 | 8 |
| ✅ UPDOWN_GBM#ETH#240min | 918 | +0.005 | +16.04€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 16699 | +0.052 | +829.52€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 2494 | +0.000 | +40.77€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 128 | -0.108 | +0.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 23893 | +0.040 | +1357.92€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 7495 | +0.032 | +452.12€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#240min | 852 | -0.011 | +4.67€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 14177 | +0.053 | +909.30€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 1255 | -0.001 | +2.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#daily | 114 | -0.147 | -10.16€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 14891 | +0.074 | +2127.04€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 6365 | +0.093 | +1626.02€ | 0 | 11 |
| ✅ UPDOWN_GBM#XRP#240min | 397 | +0.006 | -1.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 8129 | +0.062 | +502.63€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 381 | -0.106 | -7.15€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 1017 | +0.365 | +378.94€ | 0 | 9 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 1017 | +0.365 | +378.94€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 491 | +0.362 | +172.01€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 491 | +0.362 | +172.01€ | 0 | 10 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 526 | +0.365 | +206.93€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 526 | +0.365 | +206.93€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO | 26669 | -0.019 | +6655.90€ | 2 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 26669 | -0.019 | +6655.90€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1981 | -0.051 | +561.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1981 | -0.051 | +561.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 4972 | -0.115 | +279.14€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 4972 | -0.115 | +279.14€ | 2 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 1072 | +0.223 | +901.85€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 1072 | +0.223 | +901.85€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 3561 | +0.221 | +2295.60€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 3561 | +0.221 | +2295.60€ | 1 | 18 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 7599 | -0.058 | +1128.84€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 7599 | -0.058 | +1128.84€ | 4 | 5 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 7484 | -0.056 | +1489.31€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 7484 | -0.056 | +1489.31€ | 4 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 332 | +0.060 | +30.94€ | 0 | 7 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 332 | +0.060 | +30.94€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 332 | +0.060 | +30.94€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 332 | +0.060 | +30.94€ | 0 | 7 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1861 | +0.281 | +1559.86€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1861 | +0.281 | +1559.86€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 984 | +0.274 | +771.86€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 984 | +0.274 | +771.86€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 877 | +0.288 | +788.00€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 877 | +0.288 | +788.00€ | 0 | 10 |
| ✅ UPDOWN_OU_5M | 875 | -0.115 | -88.25€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 875 | -0.115 | -88.25€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 277 | -0.081 | -20.93€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 277 | -0.081 | -20.93€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 99 | -0.183 | -12.98€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 99 | -0.183 | -12.98€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 116 | -0.178 | -4.99€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 116 | -0.178 | -4.99€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 4885 | +0.299 | +2192.82€ | 0 | 3 |
| ✅ WEEKLY_PRICE#BTC | 1868 | +0.256 | +248.75€ | 0 | 3 |
| ✅ WEEKLY_PRICE#ETH | 1889 | +0.293 | +803.62€ | 0 | 3 |
| ✅ WEEKLY_PRICE#SOL | 1128 | +0.381 | +1140.45€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**✅ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: n≥15 y IC<-0.05
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: IC=+0.022 n=1386 — no justifica filtro, seguir monitorizando
  - _Datos_: n=1386 IC=+0.022 PNL=+68.62€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 841 celda(s) pasan gate riguroso completo de 2965 evaluadas (n>=40) y 4077 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.032 < 0.08 — monitorear
  - _Datos_: n=7489 IC=+0.032 PNL=+449.50€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=1889/15 IC=+0.293 PNL=+803.62€ | BTC: n=1868/15 IC=+0.256 PNL=+248.75€ | SOL: n=1128/15 IC=+0.381 PNL=+1140.45€

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
  - _Estado_: alineada_con_outcome_prev IC=+0.138 n=1085/60 | contraria IC=+0.182 n=1143 | gap=-0.045 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=607, boost estimado=+0.010. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 0/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=2492/40 IC=+0.000 PNL=+40.75€ | BTC#60min: n=3005/40 IC=-0.005 PNL=+76.63€ | SOL#60min: n=1253/40 IC=-0.001 PNL=+1.98€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.045 n=766599 | tras_1loss IC=+0.101 n=580713 | tras_2loss IC=+0.072 n=231697/40 | gap=-0.027 (umbral 0.05)

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.158 > 0.08 con n=1138 PNL=+671.32€
  - _Datos_: n=1138 IC=+0.158 PNL=+671.32€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.134 > 0.08 con n=1339 PNL=+635.74€
  - _Datos_: n=1339 IC=+0.134 PNL=+635.74€

**🟡 H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: n≥25 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.126 > 0.08 con n=89 PNL=+36.54€
  - _Datos_: n=89 IC=+0.126 PNL=+36.54€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.336 > 0.1 con n=3981 PNL=+2244.65€
  - _Datos_: n=3981 IC=+0.336 PNL=+2244.65€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=1144 IC=+0.065 PNL=+113.51€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1144 IC=+0.065 PNL=+113.51€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=108 IC=+0.173 PNL=+68.06€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=108 IC=+0.173 PNL=+68.06€

**⏳ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: 30
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-OF-02H-BTCSOL** — ORDER_FLOW H=02h UTC — BTC+SOL solamente (revisar blacklist)
  - _Hipótesis_: La hora 02h está en el blacklist basado en TODOS los pares. Con BTC+SOL solo, el historial muestra 4/5 (80%) IC=+0.054. ¿Se confirma la señal positiva con más datos?
  - _Umbral_: 15
  - _Acción_: Si IC>0.05 con n≥20 → proponer eliminar 02h del blacklist ORDER_FLOW
  - _Estado_: 7/15 ops en el filtro definido (IC actual=+0.097 PNL=+9.02€)
  - _Datos_: n=7 IC=+0.097 PNL=+9.02€

**⏳ H-CUSTOM-OF-07H-BTCSOL** — ORDER_FLOW H=07h UTC — BTC+SOL solamente (revisar blacklist)
  - _Hipótesis_: La hora 07h está en el blacklist. Con BTC+SOL solo, el historial muestra 7/12 (58%) IC=+0.043. El blacklist puede estar basado en pares negativos que ya están excluidos.
  - _Umbral_: 20
  - _Acción_: Si IC>0.05 con n≥20 → proponer eliminar 07h del blacklist ORDER_FLOW
  - _Estado_: 3/20 ops en el filtro definido (IC actual=-0.015 PNL=-2.12€)
  - _Datos_: n=3 IC=-0.015 PNL=-2.12€
  - _Bloqueante_: FILTRO_YA_IMPLEMENTADO: 07h sigue en ORDER_FLOW_BLACKLIST_HOURS -- mientras siga ahí, nunca genera fila para volver a evaluarse (26-Ago, triage candidatas estancadas)

**〰️ H-CUSTOM-GBM-60MIN-BUYYES** — GBM 60min BUY_YES — ¿edge superior al BUY_NO?
  - _Hipótesis_: Análisis actual muestra BUY_YES 60min: 22/36 (61%) IC=+0.105 vs BUY_NO 60min: 8/14 (57%) IC=+0.044. En 60min parece que BUY_YES es la dirección dominante, al contrario que en 15min.
  - _Umbral_: n≥30 y IC>+0.08
  - _Acción_: Si BUY_YES 60min confirma IC≥0.10 n≥40 → prioridad live por encima de BUY_NO
  - _Estado_: n=4456 IC=-0.004 PNL=-41.64€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=4456 IC=-0.004 PNL=-41.64€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=2294 IC=+0.002 PNL=+161.00€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=2294 IC=+0.002 PNL=+161.00€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=1386 IC=+0.022 PNL=+68.62€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=1386 IC=+0.022 PNL=+68.62€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.136 > 0.1 con n=7608 PNL=+3696.94€
  - _Datos_: n=7608 IC=+0.136 PNL=+3696.94€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=3710 IC=+0.080 PNL=+829.32€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=3710 IC=+0.080 PNL=+829.32€

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
  - _Estado_: n=1495 IC=+0.042 PNL=+126.37€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=1495 IC=+0.042 PNL=+126.37€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=189 IC=-0.029 PNL=-6.25€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=189 IC=-0.029 PNL=-6.25€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.310 n=309) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=309 IC=+0.310 PNL=+369.09€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.118 > 0.02 con n=1293 PNL=+520.97€
  - _Datos_: n=1293 IC=+0.118 PNL=+520.97€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=263 IC=-0.115 PNL=+6.39€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=263 IC=-0.115 PNL=+6.39€

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
  - _Estado_: n=46527 IC=+0.071 PNL=+6250.92€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=46527 IC=+0.071 PNL=+6250.92€

**⏳ H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: 120
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: 0/120 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.136 < -0.1 con n=784 PNL=+115.28€
  - _Datos_: n=784 IC=-0.136 PNL=+115.28€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=4427 IC=+0.069 PNL=+563.85€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=4427 IC=+0.069 PNL=+563.85€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=195 IC=-0.084 PNL=+1.76€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=195 IC=-0.084 PNL=+1.76€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.101 > 0.1 con n=1182 PNL=+299.02€
  - _Datos_: n=1182 IC=+0.101 PNL=+299.02€

**⏳ H-CUSTOM-ETH15-BUYNO-PRECIO-ALTO** — ETH#15min BUY_NO con precio_yes>0.55 pierde (NO longshot contra favorito)
  - _Hipótesis_: Detectado 2026-07-02: ult.60 shadow ETH15 BUY_NO — py_mkt~0.5 wr=0.67 PNL=+29.3 (n=49); py_mkt 0.6-0.8 wr 0.33-0 PNL=-5.75 (n=9). Filtro RETURN NONE (no SKIP) aplicado en shadow_predict.py (PY_MKT_MAX_BUY_NO_ETH15=0.55) el mismo dia -- bloquea la GENERACIÓN de la fila, no solo la decisión. Esta hipotesis trackea la zona filtrada: si las ops que HABRIAN caido aqui siguen apareciendo en otras estrategias o el IC forward de la zona se vuelve positivo, revisar el filtro. CAVEAT: n=9, muestra chica — el filtro se aplico por asimetria de riesgo (afecta a dinero live), no por significancia. ⚠️ 05-Ago (fix): la clave del filtro decía 'py_mkt', que NUNCA existió ni en features de UPDOWN_GBM (T_h/delta_ratio_macro/drift_15min/drift_60min/pct_spot_vs_ref/sigma_h) ni como columna top-level de results.csv -- corregida a 'precio_yes_mercado' (columna real). Aun así, con la clave correcta esta hipótesis NUNCA podrá acumular n mientras el filtro RETURN NONE siga activo -- es el mismo patrón 'frozen by design' que H-CUSTOM-LATE15-PHOTO-FINISH (más abajo): la propia protección impide generar los datos necesarios para volver a evaluarla. Para monitorearla de verdad haría falta un logger separado que capture la señal SIN aplicar el filtro (mismo patrón que gate_bucket_propio con data/markets histórico) -- no construido, pendiente decisión.
  - _Umbral_: 20
  - _Acción_: Si IC forward de la zona >0 con n>=20 → retirar filtro; si confirma negativo → considerar extender a BTC/SOL 15min
  - _Estado_: 7/20 ops en el filtro definido (IC actual=-0.058 PNL=-1.16€)
  - _Datos_: n=7 IC=-0.058 PNL=-1.16€
  - _Bloqueante_: FILTRO_YA_IMPLEMENTADO: PY_MKT_MAX_BUY_NO_ETH15=0.55 en shadow_predict.py hace RETURN NONE (bloquea generación, no solo decisión) -- nunca podrá acumular n mientras siga activo. Haría falta un logger separado sin el filtro para monitorear de verdad (no construido, 26-Ago)

**〰️ H-PRECIO-YES-BARATO** — BUY_YES con precio de mercado 0.30-0.40 — mercado infravalora YES
  - _Hipótesis_: Detectado 2026-07-03 en benchmark de calibración del mercado (7d, estrategias GBM): en el bucket precio_yes_mercado [0.3-0.4) la frecuencia real de YES fue 0.45 vs 0.35 implícito (+0.10, n=38). Posible sesgo favorito-longshot suave en binarios de 15min (complemento del LONGSHOT ya activo para BUY_NO con py<0.20). Si se confirma, BUY_YES comprado en esa banda lleva viento de cola estructural del propio mercado, independiente del modelo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → kelly_boost ×1.1 para BUY_YES con precio_yes_mercado en [0.30,0.40), simétrico al longshot BUY_NO existente
  - _Estado_: n=45554 IC=-0.138 PNL=+2756.72€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=45554 IC=-0.138 PNL=+2756.72€

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
  - _Estado_: n=4809 IC=+0.134 PNL=+3272.73€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=4809 IC=+0.134 PNL=+3272.73€

**⏳ H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: 40
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=11824 IC=+0.057 PNL=+1008.05€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=11824 IC=+0.057 PNL=+1008.05€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.101 > 0.08 con n=4928 PNL=+2771.83€
  - _Datos_: n=4928 IC=+0.101 PNL=+2771.83€

**⏳ H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: 80
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: 0/80 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.221 < -0.1 con n=4955 PNL=-432.24€
  - _Datos_: n=4955 IC=-0.221 PNL=-432.24€

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
  - _Estado_: n=118 IC=+0.058 PNL=+23.22€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=118 IC=+0.058 PNL=+23.22€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.095 n=2266) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=2266 IC=+0.095 PNL=+449.17€

**⏳ H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.415 n=689) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=689 IC=+0.415 PNL=+1008.56€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=19426 IC=+0.177 PNL=-2259.89€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=19426 IC=+0.177 PNL=-2259.89€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.236 > 0.1 con n=312 PNL=+220.98€
  - _Datos_: n=312 IC=+0.236 PNL=+220.98€
