# Hipótesis automáticas — 2026-10-18 12:56 UTC
_Generado por shadow_postmortem.py sobre 951341 resoluciones (PNL=+123052.63€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **PATRÓN** `py_entrada` > `0.515` → IC=+0.241 (n=764)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.515 (IC base=+0.140)

- **PATRÓN** `n_total_lado` > `66.0` → IC=+0.188 (n=274)

  - _Acción_: Kelly boost +0.94€ cuando `n_total_lado` > 66.0 (IC base=+0.140)

- **PATRÓN** `banda_hit_calibrado` > `0.802` → IC=+0.273 (n=540)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.802 (IC base=+0.140)

- **PATRÓN** `banda_z` > `9.307` → IC=+0.200 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.307 (IC base=+0.140)

- **PATRÓN** `ballenas_wallet_edge_medio` > `0.727` → IC=+0.139 (n=726)

  - _Acción_: Kelly boost +0.69€ cuando `ballenas_wallet_edge_medio` > 0.727 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.178 (n=293)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 17.0 (IC base=+0.140)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.141 (n=542)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 11.0 (IC base=+0.140)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.157 (n=880)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.01 (IC base=+0.140)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **PATRÓN** `py_entrada` > `0.555` → IC=+0.275 (n=456)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.555 (IC base=+0.146)

- **PATRÓN** `n_total_lado` > `47.0` → IC=+0.187 (n=455)

  - _Acción_: Kelly boost +0.94€ cuando `n_total_lado` > 47.0 (IC base=+0.146)

- **PATRÓN** `banda_hit_calibrado` > `0.624` → IC=+0.276 (n=454)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.624 (IC base=+0.146)

- **PATRÓN** `banda_z` > `9.736` → IC=+0.221 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.736 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.193 (n=242)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 17.0 (IC base=+0.146)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.154 (n=781)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `101.0` → IC=+0.154 (n=406)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 101.0 (IC base=+0.146)

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
  - _Potencial_: sin este filtro IC_bueno=+0.113 (n=104)

- **FILTRO** `hora_utc` < `10.0` → IC=-0.157 (n=33)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=103)

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
- **PATRÓN** `n_ballena_banda` > `25.0` → IC=+0.167 (n=19)

  - _Acción_: Kelly boost +0.83€ cuando `n_ballena_banda` > 25.0 (IC base=+0.141)

- **PATRÓN** `n_total_lado` > `38.0` → IC=+0.224 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 38.0 (IC base=+0.141)

- **PATRÓN** `banda_z` > `2.495` → IC=+0.230 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 2.495 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.200 (n=28)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.141)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.184 (n=36)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.02 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `2518.5859` → IC=+0.230 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2518.5859 (IC base=+0.141)

### BALLENAS_TARDIAS
- **FILTRO** `restante_s_al_confirmar` < `142.84` → IC=-0.206 (n=9839)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 142.84
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=29517)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `129.85` → IC=-0.264 (n=1112)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 129.85
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=3339)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `121.42` → IC=-0.287 (n=1074)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 121.42
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=3223)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `167.54` → IC=-0.208 (n=2589)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 167.54
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=7769)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `133.42` → IC=-0.282 (n=1909)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 133.42
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=5730)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.212 (n=21065)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.107)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.136 (n=4258)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `9189.8912` → IC=+0.177 (n=1917)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 9189.8912 (IC base=+0.107)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.130 (n=17801)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.130 (n=21707)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.125)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.226 (n=16552)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=7076)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `7150.8964` → IC=+0.159 (n=2733)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 7150.8964 (IC base=+0.125)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.200 (n=2006)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.194)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.195 (n=1962)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 17.0 (IC base=+0.194)

- **PATRÓN** `py_entrada` > `0.775` → IC=+0.364 (n=644)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.775 (IC base=+0.194)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.196 (n=2462)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.01 (IC base=+0.194)

- **PATRÓN** `libro_liquidez` > `16322.4619` → IC=+0.202 (n=639)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16322.4619 (IC base=+0.194)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.192 (n=1762)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 7.0 (IC base=+0.186)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.190 (n=1968)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 17.0 (IC base=+0.186)

- **PATRÓN** `py_entrada` < `0.245` → IC=+0.340 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.245 (IC base=+0.186)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.188 (n=2520)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.01 (IC base=+0.186)

- **PATRÓN** `libro_liquidez` > `16115.8854` → IC=+0.196 (n=650)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 16115.8854 (IC base=+0.186)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.61` → IC=+0.168 (n=462)

  - _Acción_: Kelly boost +0.84€ cuando `py_entrada` > 0.61 (IC base=+0.080)

- **PATRÓN** `libro_liquidez` > `6860.5651` → IC=+0.169 (n=122)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 6860.5651 (IC base=+0.080)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.139 (n=1090)

  - _Acción_: Kelly boost +0.70€ cuando `py_entrada` < 0.44 (IC base=+0.088)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.166 (n=4093)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.160)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.160 (n=2799)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 12.0 (IC base=+0.160)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.370 (n=1323)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.160)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.222 (n=1809)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.213)

- **PATRÓN** `py_entrada` < `0.255` → IC=+0.360 (n=656)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.255 (IC base=+0.213)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.217 (n=2123)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.213)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.144 (n=1028)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.140)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.145 (n=879)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 15.0 (IC base=+0.140)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.258 (n=328)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `1868.6989` → IC=+0.153 (n=655)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 1868.6989 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.162 (n=152)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.070)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.246 (n=957)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.223)

- **PATRÓN** `py_entrada` > `0.82` → IC=+0.411 (n=1172)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.82 (IC base=+0.223)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.149 (n=1281)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 7.0 (IC base=+0.148)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.158 (n=674)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 7.0 (IC base=+0.148)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.285 (n=646)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.148)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.154 (n=849)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.148)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.172 (n=339)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 7.0 (IC base=+0.160)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.355 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.160)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.153 (n=194)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.02 (IC base=+0.160)

- **PATRÓN** `libro_liquidez` > `1131.3588` → IC=+0.147 (n=242)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 1131.3588 (IC base=+0.160)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.154 (n=434)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 17.0 (IC base=+0.126)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.253 (n=402)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.126)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `11.0` → IC=-0.297 (n=62)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=148)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.205 (n=17731)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.201)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.202 (n=15072)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.201)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.234 (n=7334)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.201)

- **PATRÓN** `libro_liquidez` > `4837.3339` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4837.3339 (IC base=+0.201)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.179 (n=4098)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 5.0 (IC base=+0.178)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.181 (n=3878)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 17.0 (IC base=+0.178)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.182 (n=3992)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` < 0.73 (IC base=+0.178)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.380 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.247 (n=89)

- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=90)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.225 (n=2047)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.233 (n=1370)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.224)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.310 (n=724)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.224)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.188 (n=4028)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.184 (n=3434)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 15.0 (IC base=+0.182)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.187 (n=3167)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` > 0.71 (IC base=+0.182)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.257 (n=3502)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.248)

- **PATRÓN** `py_entrada` > `0.785` → IC=+0.361 (n=1112)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.785 (IC base=+0.248)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.192 (n=3953)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 5.0 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.193 (n=2535)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 11.0 (IC base=+0.188)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.192 (n=2910)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.71 (IC base=+0.188)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.431 (n=756)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.427)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.441 (n=783)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.427)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.431 (n=798)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.427)

- **PATRÓN** `libro_liquidez` > `12834.5263` → IC=+0.444 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12834.5263 (IC base=+0.427)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` < `7.0` → IC=+0.450 (n=138)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.436)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.448 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.436)

- **PATRÓN** `libro_liquidez` > `18380.2021` → IC=+0.441 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 18380.2021 (IC base=+0.436)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.447 (n=204)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.431)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.442 (n=306)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.431)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.434 (n=330)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.431)

- **PATRÓN** `libro_liquidez` > `4389.547` → IC=+0.439 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4389.547 (IC base=+0.431)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.407 (n=138)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.402)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.400 (n=138)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.402)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.415 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.402)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.77` → IC=-0.318 (n=31)

  - _Acción_: SKIP cuando `py_entrada` > 0.77
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=11)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=26)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.207 (n=22917)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.201)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.247 (n=23216)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.201)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.187 (n=10773)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.185)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.188 (n=7364)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 12.0 (IC base=+0.185)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.201 (n=10284)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.71 (IC base=+0.185)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.227 (n=4785)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.227 (n=4724)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.224)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.286 (n=3371)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.224)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.189 (n=3921)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 17.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.211 (n=5246)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.181)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.835` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.835
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.231 (n=4821)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.221)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.222 (n=3691)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.221)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.278 (n=3276)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.221)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.205 (n=8811)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.202)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.260 (n=3414)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.202)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.206 (n=3807)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.199 (n=3860)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 6.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.247 (n=4002)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.196)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.190 (n=8308)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.139 (n=8190)

  - _Acción_: Kelly boost +0.69€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `2.41` → IC=+0.137 (n=7586)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 2.41 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.193 (n=4108)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.38 (IC base=+0.119)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.143 (n=4159)

  - _Acción_: Kelly boost +0.71€ cuando `restante_min` > 4.95 (IC base=+0.119)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.129 (n=5023)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 7.0 (IC base=+0.119)

- **PATRÓN** `lag_apertura_s` < `2.78` → IC=+0.146 (n=3775)

  - _Acción_: Kelly boost +0.73€ cuando `lag_apertura_s` < 2.78 (IC base=+0.119)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.187 (n=4200)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` < 0.38 (IC base=+0.114)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.134 (n=4468)

  - _Acción_: Kelly boost +0.67€ cuando `restante_min` > 4.96 (IC base=+0.114)

- **PATRÓN** `lag_apertura_s` < `2.26` → IC=+0.135 (n=3829)

  - _Acción_: Kelly boost +0.67€ cuando `lag_apertura_s` < 2.26 (IC base=+0.114)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.300 (n=1612)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.292)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.293 (n=1596)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.292)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.378 (n=557)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.292)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.287 (n=730)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.279)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.280 (n=629)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.279)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.350 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.279)

- **PATRÓN** `libro_liquidez` > `5400.2534` → IC=+0.286 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5400.2534 (IC base=+0.279)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.321 (n=518)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.296)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.300 (n=768)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.296)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.389 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.296)

- **PATRÓN** `libro_liquidez` > `2108.9504` → IC=+0.310 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2108.9504 (IC base=+0.296)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.445 (n=748)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.441)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.441 (n=486)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.441)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.442 (n=740)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.441)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.446 (n=512)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.441)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.442 (n=846)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.441)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.439 (n=356)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.436)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.443 (n=242)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.436)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.438 (n=367)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.436)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.443 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.436)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.452 (n=352)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.448)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.453 (n=295)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.448)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.449 (n=388)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.448)

- **PATRÓN** `libro_liquidez` > `2158.1237` → IC=+0.455 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2158.1237 (IC base=+0.448)

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
  - _Potencial_: sin este filtro IC_bueno=-0.223 (n=92)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.340 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.206 (n=90)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.250 (n=58)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.219 (n=55)

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
  - _Potencial_: sin este filtro IC_bueno=-0.223 (n=92)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.340 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.206 (n=90)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.250 (n=58)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.219 (n=55)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4767` → IC=+0.137 (n=12832)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.4767 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.123 (n=12968)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 6.0 (IC base=+0.120)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.121 (n=13437)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` < 18.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` > `0.9818` → IC=+0.247 (n=4279)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9818 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` > `0.7872` → IC=+0.266 (n=724)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7872 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` < `0.3692` → IC=+0.256 (n=3554)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3692 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.929` → IC=+0.190 (n=4851)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 5.929 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` < `1.2036` → IC=+0.256 (n=3700)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2036 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` > `0.6183` → IC=+0.262 (n=3699)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6183 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` > `0.3023` → IC=+0.238 (n=1306)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3023 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` > `2.343` → IC=+0.228 (n=4131)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.343 (IC base=+0.120)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.121 (n=15773)

  - _Acción_: Kelly boost +0.60€ cuando `libro_spread` < 0.04 (IC base=+0.120)

- **PATRÓN** `ibs_20min` < `0.5679` → IC=+0.141 (n=15842)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` < 0.5679 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` < `0.1534` → IC=+0.184 (n=5759)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` < 0.1534 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` < `0.6961` → IC=+0.181 (n=2700)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 0.6961 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` > `1.0503` → IC=+0.179 (n=2780)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` > 1.0503 (IC base=+0.074)

- **PATRÓN** `volumen_pendiente_norm` > `0.2949` → IC=+0.230 (n=1530)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2949 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` > `2.6769` → IC=+0.205 (n=3479)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6769 (IC base=+0.074)

- **PATRÓN** `ballena_activa_n` < `107.0` → IC=+0.219 (n=10284)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 107.0 (IC base=+0.074)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.214 (n=934)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.197)

- **PATRÓN** `drift_60min` |x|≤ `0.3472` → IC=+0.201 (n=2802)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3472 (IC base=+0.197)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.207 (n=1353)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.203 (n=1884)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.197)

- **PATRÓN** `ibs_20min` > `0.9781` → IC=+0.278 (n=1270)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9781 (IC base=+0.197)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.977` → IC=+0.283 (n=1226)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.977 (IC base=+0.197)

- **PATRÓN** `volumen_pendiente_norm` > `0.2321` → IC=+0.247 (n=496)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2321 (IC base=+0.197)

- **PATRÓN** `volumen_spike_ratio` > `1.4363` → IC=+0.199 (n=2667)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 1.4363 (IC base=+0.197)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.211 (n=2980)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.197)

- **PATRÓN** `libro_liquidez` > `2085.6796` → IC=+0.210 (n=934)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2085.6796 (IC base=+0.197)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.210 (n=2173)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 24.0 (IC base=+0.197)

- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.239 (n=2347)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0084 (IC base=+0.236)

- **PATRÓN** `sigma_h` > `0.0076` → IC=+0.238 (n=1064)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0076 (IC base=+0.236)

- **PATRÓN** `drift_60min` |x|≤ `0.0873` → IC=+0.271 (n=783)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0873 (IC base=+0.236)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.256 (n=856)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.236)

- **PATRÓN** `ibs_20min` < `0.5215` → IC=+0.257 (n=2347)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5215 (IC base=+0.236)

- **PATRÓN** `volumen_pendiente_norm` < `0.0932` → IC=+0.239 (n=2096)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0932 (IC base=+0.236)

- **PATRÓN** `volumen_pendiente_norm` > `0.2847` → IC=+0.247 (n=314)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2847 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` < `1.4369` → IC=+0.240 (n=737)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4369 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` > `2.6424` → IC=+0.242 (n=738)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6424 (IC base=+0.236)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.239 (n=2623)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.236)

- **PATRÓN** `libro_liquidez` > `1673.3648` → IC=+0.244 (n=2097)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1673.3648 (IC base=+0.236)

- **PATRÓN** `ballena_activa_n` < `7.0` → IC=+0.240 (n=764)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 7.0 (IC base=+0.236)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.240 (n=1007)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.226)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.229 (n=1037)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.226)

- **PATRÓN** `drift_60min` |x|≤ `0.106` → IC=+0.261 (n=1006)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.106 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.237 (n=2398)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.226)

- **PATRÓN** `ibs_20min` > `0.9553` → IC=+0.275 (n=762)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9553 (IC base=+0.226)

- **PATRÓN** `dist_vwap_pct` > `0.1279` → IC=+0.233 (n=1247)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1279 (IC base=+0.226)

- **PATRÓN** `dist_vwap_pct` < `0.3397` → IC=+0.228 (n=2198)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3397 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.408` → IC=+0.267 (n=346)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.408 (IC base=+0.226)

- **PATRÓN** `volumen_regimen` < `1.2316` → IC=+0.228 (n=2285)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2316 (IC base=+0.226)

- **PATRÓN** `volumen_regimen` > `0.6211` → IC=+0.231 (n=2286)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6211 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` > `0.2778` → IC=+0.258 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2778 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` < `1.5146` → IC=+0.227 (n=992)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5146 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` > `2.4423` → IC=+0.253 (n=751)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4423 (IC base=+0.226)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.150 (n=2332)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0057 (IC base=+0.131)

- **PATRÓN** `drift_60min` |x|≤ `0.0749` → IC=+0.168 (n=777)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.0749 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.152 (n=887)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 17.0 (IC base=+0.131)

- **PATRÓN** `ibs_20min` < `0.7296` → IC=+0.175 (n=2331)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.7296 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` < `0.1327` → IC=+0.153 (n=2171)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.1327 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.077` → IC=+0.151 (n=379)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 11.077 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.207` → IC=+0.139 (n=2132)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` < 4.207 (IC base=+0.131)

- **PATRÓN** `volumen_regimen` < `1.1995` → IC=+0.139 (n=2331)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 1.1995 (IC base=+0.131)

- **PATRÓN** `volumen_pendiente_norm` > `0.0967` → IC=+0.159 (n=852)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.0967 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` < `2.4573` → IC=+0.141 (n=2212)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 2.4573 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` > `1.4152` → IC=+0.135 (n=2211)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 1.4152 (IC base=+0.131)

- **PATRÓN** `ballena_activa_n` < `219.0` → IC=+0.169 (n=944)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 219.0 (IC base=+0.131)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.012` → IC=+0.214 (n=973)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.012 (IC base=+0.194)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.198 (n=3055)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 5.0 (IC base=+0.194)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.195 (n=2609)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 15.0 (IC base=+0.194)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.272 (n=1119)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.194)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.287` → IC=+0.269 (n=609)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.287 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` < `0.0975` → IC=+0.198 (n=2572)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` < 0.0975 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` > `0.3511` → IC=+0.211 (n=379)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3511 (IC base=+0.194)

- **PATRÓN** `volumen_spike_ratio` > `2.6928` → IC=+0.211 (n=1279)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6928 (IC base=+0.194)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.201 (n=3466)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.194)

- **PATRÓN** `libro_liquidez` > `1983.6434` → IC=+0.200 (n=1320)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1983.6434 (IC base=+0.194)

- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.223 (n=2291)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0106 (IC base=+0.217)

- **PATRÓN** `drift_60min` |x|≤ `0.4639` → IC=+0.223 (n=2291)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4639 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.244 (n=971)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.217)

- **PATRÓN** `ibs_20min` < `0.0148` → IC=+0.275 (n=868)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0148 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.44` → IC=+0.249 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.44 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` > `0.3474` → IC=+0.258 (n=370)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3474 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` < `1.7274` → IC=+0.214 (n=1086)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7274 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` > `2.7276` → IC=+0.228 (n=1119)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7276 (IC base=+0.217)

- **PATRÓN** `libro_liquidez` > `2060.32` → IC=+0.226 (n=868)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2060.32 (IC base=+0.217)

- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.219 (n=2148)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 25.0 (IC base=+0.217)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.142 (n=146)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=3522)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.160 (n=519)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0036 (IC base=+0.052)

- **PATRÓN** `ibs_20min` > `0.9547` → IC=+0.226 (n=517)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9547 (IC base=+0.052)

- **PATRÓN** `dist_vwap_pct` > `0.1359` → IC=+0.326 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1359 (IC base=+0.052)

- **PATRÓN** `dist_vwap_pct` < `0.7505` → IC=+0.332 (n=642)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.7505 (IC base=+0.052)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.086` → IC=+0.187 (n=1114)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 5.086 (IC base=+0.052)

- **PATRÓN** `volumen_regimen` < `0.8546` → IC=+0.335 (n=385)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8546 (IC base=+0.052)

- **PATRÓN** `volumen_regimen` > `1.2247` → IC=+0.350 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2247 (IC base=+0.052)

- **PATRÓN** `volumen_pendiente_norm` < `0.1688` → IC=+0.325 (n=473)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1688 (IC base=+0.052)

- **PATRÓN** `volumen_pendiente_norm` > `0.2986` → IC=+0.343 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2986 (IC base=+0.052)

- **PATRÓN** `volumen_spike_ratio` < `1.4088` → IC=+0.341 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4088 (IC base=+0.052)

- **PATRÓN** `volumen_spike_ratio` > `2.2467` → IC=+0.324 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2467 (IC base=+0.052)

- **PATRÓN** `ballena_activa_n` < `133.0` → IC=+0.336 (n=503)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 133.0 (IC base=+0.052)

- **PATRÓN** `ibs_20min` < `0.0951` → IC=+0.170 (n=919)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.0951 (IC base=+0.034)

- **PATRÓN** `dist_vwap_pct` > `0.322` → IC=+0.140 (n=445)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` > 0.322 (IC base=+0.034)

- **PATRÓN** `dist_vwap_pct` < `0.1306` → IC=+0.133 (n=1479)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.1306 (IC base=+0.034)

- **PATRÓN** `volumen_regimen` < `0.8471` → IC=+0.143 (n=1079)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 0.8471 (IC base=+0.034)

- **PATRÓN** `volumen_regimen` > `1.1684` → IC=+0.130 (n=539)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` > 1.1684 (IC base=+0.034)

- **PATRÓN** `volumen_pendiente_norm` > `0.2852` → IC=+0.198 (n=213)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2852 (IC base=+0.034)

- **PATRÓN** `volumen_spike_ratio` > `2.1533` → IC=+0.150 (n=703)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 2.1533 (IC base=+0.034)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.163 (n=96)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.073 (n=534)

- **FILTRO** `ibs_20min` < `0.2791` → IC=-0.192 (n=157)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2791
  - _Potencial_: sin este filtro IC_bueno=+0.113 (n=473)

- **FILTRO** `ibs_20min` > `0.2187` → IC=-0.132 (n=3467)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2187
  - _Potencial_: sin este filtro IC_bueno=+0.148 (n=1708)

- **FILTRO** `sigma_ewma_delta_pct` > `8.651` → IC=-0.230 (n=543)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.651
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=4632)

- **PATRÓN** `ibs_20min` > `0.7913` → IC=+0.196 (n=215)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.7913 (IC base=+0.036)

- **PATRÓN** `dist_vwap_pct` > `1.0167` → IC=+0.270 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0167 (IC base=+0.036)

- **PATRÓN** `dist_vwap_pct` < `0.6236` → IC=+0.264 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6236 (IC base=+0.036)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.1` → IC=+0.153 (n=200)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 3.1 (IC base=+0.036)

- **PATRÓN** `volumen_regimen` < `0.7536` → IC=+0.261 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7536 (IC base=+0.036)

- **PATRÓN** `volumen_regimen` > `0.992` → IC=+0.300 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.992 (IC base=+0.036)

- **PATRÓN** `volumen_pendiente_norm` < `0.0778` → IC=+0.281 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0778 (IC base=+0.036)

- **PATRÓN** `volumen_spike_ratio` < `2.1915` → IC=+0.282 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1915 (IC base=+0.036)

- **PATRÓN** `volumen_spike_ratio` > `1.5401` → IC=+0.258 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5401 (IC base=+0.036)

- **PATRÓN** `ibs_20min` < `0.2187` → IC=+0.148 (n=1708)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` < 0.2187 (IC base=-0.039)

- **PATRÓN** `dist_vwap_pct` > `0.2659` → IC=+0.275 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2659 (IC base=-0.039)

- **PATRÓN** `dist_vwap_pct` < `0.4351` → IC=+0.274 (n=785)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4351 (IC base=-0.039)

- **PATRÓN** `volumen_regimen` < `0.7007` → IC=+0.298 (n=310)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7007 (IC base=-0.039)

- **PATRÓN** `volumen_pendiente_norm` > `0.08` → IC=+0.303 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.08 (IC base=-0.039)

- **PATRÓN** `volumen_spike_ratio` < `2.4196` → IC=+0.301 (n=640)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4196 (IC base=-0.039)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6194` → IC=-0.176 (n=937)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6194
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=2813)

- **FILTRO** `ibs_20min` < `0.7431` → IC=-0.148 (n=2475)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7431
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=1275)

- **FILTRO** `ibs_20min` > `0.7547` → IC=-0.204 (n=1362)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7547
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=4089)

- **PATRÓN** `dist_vwap_pct` > `0.7356` → IC=+0.332 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7356 (IC base=-0.068)

- **PATRÓN** `dist_vwap_pct` < `0.2576` → IC=+0.299 (n=545)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2576 (IC base=-0.068)

- **PATRÓN** `volumen_regimen` < `1.1457` → IC=+0.295 (n=636)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1457 (IC base=-0.068)

- **PATRÓN** `volumen_regimen` > `0.7047` → IC=+0.310 (n=568)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7047 (IC base=-0.068)

- **PATRÓN** `volumen_pendiente_norm` < `0.1006` → IC=+0.298 (n=597)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1006 (IC base=-0.068)

- **PATRÓN** `volumen_pendiente_norm` > `0.0737` → IC=+0.298 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0737 (IC base=-0.068)

- **PATRÓN** `volumen_spike_ratio` < `1.4138` → IC=+0.321 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4138 (IC base=-0.068)

- **PATRÓN** `volumen_spike_ratio` > `1.8376` → IC=+0.298 (n=410)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8376 (IC base=-0.068)

- **PATRÓN** `dist_vwap_pct` > `0.8102` → IC=+0.273 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8102 (IC base=-0.006)

- **PATRÓN** `volumen_regimen` > `1.0696` → IC=+0.280 (n=672)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0696 (IC base=-0.006)

- **PATRÓN** `volumen_pendiente_norm` > `0.1023` → IC=+0.277 (n=518)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1023 (IC base=-0.006)

- **PATRÓN** `volumen_spike_ratio` < `2.1859` → IC=+0.260 (n=1197)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1859 (IC base=-0.006)

- **PATRÓN** `volumen_spike_ratio` > `1.4281` → IC=+0.261 (n=1360)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4281 (IC base=-0.006)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.206 (n=5644)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0097 (IC base=+0.096)

- **PATRÓN** `ibs_20min` > `0.3241` → IC=+0.168 (n=16914)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` > 0.3241 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` > `0.9563` → IC=+0.298 (n=1254)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9563 (IC base=+0.096)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.608` → IC=+0.160 (n=7579)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 3.608 (IC base=+0.096)

- **PATRÓN** `volumen_regimen` < `1.1722` → IC=+0.261 (n=6221)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1722 (IC base=+0.096)

- **PATRÓN** `volumen_regimen` > `0.6884` → IC=+0.266 (n=5557)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6884 (IC base=+0.096)

- **PATRÓN** `volumen_pendiente_norm` > `0.2397` → IC=+0.275 (n=1855)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2397 (IC base=+0.096)

- **PATRÓN** `volumen_spike_ratio` > `2.6418` → IC=+0.269 (n=3315)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6418 (IC base=+0.096)

- **PATRÓN** `ballena_activa_n` < `92.0` → IC=+0.292 (n=9527)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 92.0 (IC base=+0.096)

- **PATRÓN** `sigma_h` > `0.0092` → IC=+0.161 (n=5435)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` > 0.0092 (IC base=+0.074)

- **PATRÓN** `ibs_20min` < `0.6606` → IC=+0.144 (n=16305)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.6606 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` < `0.2398` → IC=+0.261 (n=5080)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2398 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` > `1.1942` → IC=+0.265 (n=1710)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1942 (IC base=+0.074)

- **PATRÓN** `volumen_pendiente_norm` > `0.2934` → IC=+0.317 (n=1083)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2934 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` < `1.5781` → IC=+0.286 (n=3224)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5781 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` > `2.2648` → IC=+0.282 (n=3322)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2648 (IC base=+0.074)

- **PATRÓN** `ballena_activa_n` < `77.0` → IC=+0.292 (n=7259)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 77.0 (IC base=+0.074)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.3703` → IC=-0.176 (n=1537)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3703
  - _Potencial_: sin este filtro IC_bueno=+0.133 (n=3121)

- **FILTRO** `ibs_20min` > `0.7448` → IC=-0.211 (n=973)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7448
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=2921)

- **FILTRO** `sigma_ewma_delta_pct` > `4.472` → IC=-0.203 (n=857)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.472
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=3037)

- **PATRÓN** `ibs_20min` > `0.9145` → IC=+0.306 (n=1167)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9145 (IC base=+0.031)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.041` → IC=+0.212 (n=827)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.041 (IC base=+0.031)

- **PATRÓN** `volumen_pendiente_norm` > `0.2287` → IC=+0.298 (n=295)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2287 (IC base=+0.031)

- **PATRÓN** `volumen_spike_ratio` < `1.4427` → IC=+0.244 (n=506)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4427 (IC base=+0.031)

- **PATRÓN** `volumen_spike_ratio` > `2.2415` → IC=+0.270 (n=688)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2415 (IC base=+0.031)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.274 (n=1032)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.031)

- **PATRÓN** `ibs_20min` < `0.1618` → IC=+0.162 (n=974)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` < 0.1618 (IC base=-0.028)

- **PATRÓN** `volumen_pendiente_norm` < `0.0719` → IC=+0.415 (n=432)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0719 (IC base=-0.028)

- **PATRÓN** `volumen_spike_ratio` < `2.4765` → IC=+0.405 (n=484)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4765 (IC base=-0.028)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.398 (n=441)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 21.0 (IC base=-0.028)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.1122` → IC=+0.210 (n=846)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1122 (IC base=+0.023)

- **PATRÓN** `volumen_regimen` < `1.1951` → IC=+0.188 (n=1642)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 1.1951 (IC base=+0.023)

- **PATRÓN** `volumen_regimen` > `0.6821` → IC=+0.198 (n=1466)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_regimen` > 0.6821 (IC base=+0.023)

- **PATRÓN** `volumen_pendiente_norm` > `0.2752` → IC=+0.220 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2752 (IC base=+0.023)

- **PATRÓN** `volumen_spike_ratio` < `1.4286` → IC=+0.208 (n=540)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4286 (IC base=+0.023)

- **PATRÓN** `volumen_spike_ratio` > `2.4911` → IC=+0.190 (n=539)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 2.4911 (IC base=+0.023)

- **PATRÓN** `ballena_activa_n` < `221.0` → IC=+0.237 (n=709)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 221.0 (IC base=+0.023)

- **PATRÓN** `dist_vwap_pct` < `0.1132` → IC=+0.231 (n=1048)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1132 (IC base=-0.002)

- **PATRÓN** `volumen_regimen` > `0.6201` → IC=+0.233 (n=1048)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6201 (IC base=-0.002)

- **PATRÓN** `volumen_pendiente_norm` > `0.273` → IC=+0.293 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.273 (IC base=-0.002)

- **PATRÓN** `volumen_spike_ratio` < `1.5357` → IC=+0.232 (n=439)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5357 (IC base=-0.002)

- **PATRÓN** `volumen_spike_ratio` > `2.1658` → IC=+0.245 (n=453)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1658 (IC base=-0.002)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0118` → IC=+0.306 (n=827)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0118 (IC base=+0.265)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.271 (n=2601)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.265)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.310 (n=1305)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.265)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.692` → IC=+0.295 (n=789)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.692 (IC base=+0.265)

- **PATRÓN** `volumen_pendiente_norm` < `0.0979` → IC=+0.277 (n=2152)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0979 (IC base=+0.265)

- **PATRÓN** `volumen_spike_ratio` > `1.6106` → IC=+0.271 (n=2392)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6106 (IC base=+0.265)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.276 (n=2935)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.265)

- **PATRÓN** `libro_liquidez` > `1977.5784` → IC=+0.283 (n=1125)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1977.5784 (IC base=+0.265)

- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.328 (n=969)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0101 (IC base=+0.291)

- **PATRÓN** `drift_60min` |x|≤ `0.1832` → IC=+0.309 (n=940)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1832 (IC base=+0.291)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.321 (n=817)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.291)

- **PATRÓN** `ibs_20min` < `0.3696` → IC=+0.294 (n=2135)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3696 (IC base=+0.291)

- **PATRÓN** `ibs_20min` > `0.2581` → IC=+0.300 (n=969)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2581 (IC base=+0.291)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.611` → IC=+0.316 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.611 (IC base=+0.291)

- **PATRÓN** `volumen_pendiente_norm` < `0.1968` → IC=+0.289 (n=2084)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1968 (IC base=+0.291)

- **PATRÓN** `volumen_pendiente_norm` > `0.3414` → IC=+0.311 (n=337)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3414 (IC base=+0.291)

- **PATRÓN** `volumen_spike_ratio` < `1.7251` → IC=+0.298 (n=896)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7251 (IC base=+0.291)

- **PATRÓN** `volumen_spike_ratio` > `2.6617` → IC=+0.303 (n=923)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6617 (IC base=+0.291)

- **PATRÓN** `libro_liquidez` > `2055.2962` → IC=+0.311 (n=712)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2055.2962 (IC base=+0.291)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.292 (n=1333)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 19.0 (IC base=+0.291)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.738` → IC=-0.185 (n=1021)

  - _Acción_: SKIP cuando `ibs_20min` > 0.738
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=3065)

- **PATRÓN** `ibs_20min` > `0.8806` → IC=+0.171 (n=963)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` > 0.8806 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` > `0.1494` → IC=+0.230 (n=724)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1494 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` < `0.3636` → IC=+0.232 (n=1298)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3636 (IC base=+0.029)

- **PATRÓN** `volumen_regimen` < `1.0103` → IC=+0.246 (n=1178)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0103 (IC base=+0.029)

- **PATRÓN** `volumen_pendiente_norm` > `0.1026` → IC=+0.252 (n=422)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1026 (IC base=+0.029)

- **PATRÓN** `volumen_spike_ratio` < `1.3994` → IC=+0.246 (n=432)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3994 (IC base=+0.029)

- **PATRÓN** `ballena_activa_n` < `103.0` → IC=+0.265 (n=1157)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 103.0 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` < `0.3277` → IC=+0.228 (n=1005)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3277 (IC base=-0.003)

- **PATRÓN** `volumen_regimen` < `1.0331` → IC=+0.233 (n=813)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0331 (IC base=-0.003)

- **PATRÓN** `volumen_pendiente_norm` < `0.1037` → IC=+0.244 (n=856)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1037 (IC base=-0.003)

- **PATRÓN** `volumen_pendiente_norm` > `0.2882` → IC=+0.298 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2882 (IC base=-0.003)

- **PATRÓN** `volumen_spike_ratio` < `1.8034` → IC=+0.266 (n=583)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8034 (IC base=-0.003)

- **PATRÓN** `volumen_spike_ratio` > `2.4526` → IC=+0.251 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4526 (IC base=-0.003)

- **PATRÓN** `ballena_activa_n` < `125.0` → IC=+0.254 (n=888)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 125.0 (IC base=-0.003)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7619` → IC=-0.209 (n=1786)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7619
  - _Potencial_: sin este filtro IC_bueno=+0.304 (n=1786)

- **FILTRO** `ibs_20min` > `0.65` → IC=-0.238 (n=876)

  - _Acción_: SKIP cuando `ibs_20min` > 0.65
  - _Potencial_: sin este filtro IC_bueno=+0.119 (n=2631)

- **FILTRO** `sigma_ewma_delta_pct` > `8.538` → IC=-0.236 (n=403)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.538
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=3104)

- **PATRÓN** `ibs_20min` > `0.7619` → IC=+0.304 (n=1786)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7619 (IC base=+0.047)

- **PATRÓN** `dist_vwap_pct` > `0.2143` → IC=+0.337 (n=797)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2143 (IC base=+0.047)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.58` → IC=+0.177 (n=555)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 9.58 (IC base=+0.047)

- **PATRÓN** `volumen_regimen` < `0.8453` → IC=+0.333 (n=895)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8453 (IC base=+0.047)

- **PATRÓN** `volumen_regimen` > `0.7033` → IC=+0.322 (n=1199)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7033 (IC base=+0.047)

- **PATRÓN** `volumen_pendiente_norm` < `0.1583` → IC=+0.321 (n=1392)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1583 (IC base=+0.047)

- **PATRÓN** `volumen_pendiente_norm` > `0.2752` → IC=+0.357 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2752 (IC base=+0.047)

- **PATRÓN** `volumen_spike_ratio` < `1.4421` → IC=+0.342 (n=435)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4421 (IC base=+0.047)

- **PATRÓN** `ballena_activa_n` < `57.0` → IC=+0.337 (n=1309)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 57.0 (IC base=+0.047)

- **PATRÓN** `ibs_20min` < `0.55` → IC=+0.142 (n=2318)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` < 0.55 (IC base=+0.030)

- **PATRÓN** `dist_vwap_pct` < `0.4547` → IC=+0.248 (n=1232)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4547 (IC base=+0.030)

- **PATRÓN** `volumen_regimen` < `0.7047` → IC=+0.261 (n=504)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7047 (IC base=+0.030)

- **PATRÓN** `volumen_pendiente_norm` < `0.2195` → IC=+0.241 (n=1288)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2195 (IC base=+0.030)

- **PATRÓN** `volumen_pendiente_norm` > `0.0756` → IC=+0.254 (n=432)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0756 (IC base=+0.030)

- **PATRÓN** `volumen_spike_ratio` < `2.4232` → IC=+0.251 (n=1100)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4232 (IC base=+0.030)

- **PATRÓN** `ballena_activa_n` < `53.0` → IC=+0.268 (n=1125)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 53.0 (IC base=+0.030)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0108` → IC=+0.343 (n=1697)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0108 (IC base=+0.299)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.300 (n=733)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.299)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.311 (n=910)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.299)

- **PATRÓN** `ibs_20min` > `0.7561` → IC=+0.338 (n=1697)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7561 (IC base=+0.299)

- **PATRÓN** `dist_vwap_pct` > `0.2081` → IC=+0.326 (n=1074)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2081 (IC base=+0.299)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.778` → IC=+0.318 (n=921)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.778 (IC base=+0.299)

- **PATRÓN** `volumen_regimen` > `0.6275` → IC=+0.308 (n=1899)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6275 (IC base=+0.299)

- **PATRÓN** `volumen_pendiente_norm` > `0.2799` → IC=+0.341 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2799 (IC base=+0.299)

- **PATRÓN** `volumen_spike_ratio` > `1.4247` → IC=+0.310 (n=1819)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4247 (IC base=+0.299)

- **PATRÓN** `libro_liquidez` > `2464.8952` → IC=+0.309 (n=1697)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2464.8952 (IC base=+0.299)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.332 (n=1632)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 42.0 (IC base=+0.299)

- **PATRÓN** `sigma_h` > `0.0151` → IC=+0.332 (n=1345)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0151 (IC base=+0.301)

- **PATRÓN** `drift_60min` |x|≤ `0.1875` → IC=+0.304 (n=887)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1875 (IC base=+0.301)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.312 (n=782)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.301)

- **PATRÓN** `ibs_20min` < `0.37` → IC=+0.326 (n=2015)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.37 (IC base=+0.301)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.549` → IC=+0.315 (n=748)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.549 (IC base=+0.301)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.079` → IC=+0.302 (n=2393)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 10.079 (IC base=+0.301)

- **PATRÓN** `volumen_regimen` < `0.7186` → IC=+0.305 (n=887)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7186 (IC base=+0.301)

- **PATRÓN** `volumen_regimen` > `1.224` → IC=+0.331 (n=672)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.224 (IC base=+0.301)

- **PATRÓN** `volumen_pendiente_norm` > `0.2824` → IC=+0.352 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2824 (IC base=+0.301)

- **PATRÓN** `volumen_spike_ratio` < `1.4133` → IC=+0.308 (n=614)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4133 (IC base=+0.301)

- **PATRÓN** `volumen_spike_ratio` > `2.1346` → IC=+0.305 (n=834)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1346 (IC base=+0.301)

- **PATRÓN** `libro_liquidez` > `2638.1002` → IC=+0.302 (n=1343)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2638.1002 (IC base=+0.301)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.182 (n=4172)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0048 (IC base=+0.180)

- **PATRÓN** `sigma_h` > `0.0115` → IC=+0.223 (n=4157)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0115 (IC base=+0.180)

- **PATRÓN** `drift_60min` |x|≤ `0.0868` → IC=+0.202 (n=4154)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0868 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.189 (n=12938)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` > `0.5576` → IC=+0.234 (n=12458)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5576 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` > `0.1637` → IC=+0.207 (n=5084)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1637 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.432` → IC=+0.252 (n=3276)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.432 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` < `1.1897` → IC=+0.169 (n=8263)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.1897 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` > `0.6243` → IC=+0.165 (n=8262)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 0.6243 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.2931` → IC=+0.205 (n=1818)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2931 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `2.6068` → IC=+0.191 (n=4024)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.6068 (IC base=+0.180)

- **PATRÓN** `libro_liquidez` > `1992.1632` → IC=+0.182 (n=11129)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 1992.1632 (IC base=+0.180)

- **PATRÓN** `ballena_activa_n` < `95.0` → IC=+0.198 (n=11365)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 95.0 (IC base=+0.180)

- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.185 (n=8025)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0069 (IC base=+0.178)

- **PATRÓN** `drift_60min` |x|≤ `0.0798` → IC=+0.224 (n=4010)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0798 (IC base=+0.178)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.212 (n=4500)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.178)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.235 (n=12068)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5 (IC base=+0.178)

- **PATRÓN** `dist_vwap_pct` < `0.1738` → IC=+0.173 (n=8531)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` < 0.1738 (IC base=+0.178)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.049` → IC=+0.197 (n=1977)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 10.049 (IC base=+0.178)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.699` → IC=+0.179 (n=10595)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` < 2.699 (IC base=+0.178)

- **PATRÓN** `volumen_regimen` < `1.1809` → IC=+0.162 (n=8586)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.1809 (IC base=+0.178)

- **PATRÓN** `volumen_pendiente_norm` > `0.2929` → IC=+0.225 (n=1773)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2929 (IC base=+0.178)

- **PATRÓN** `volumen_spike_ratio` > `2.6319` → IC=+0.186 (n=3760)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.6319 (IC base=+0.178)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.191 (n=10990)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 100.0 (IC base=+0.178)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.231 (n=698)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.213)

- **PATRÓN** `drift_60min` |x|≤ `0.3313` → IC=+0.230 (n=2086)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3313 (IC base=+0.213)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.216 (n=2185)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.213)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.222 (n=1413)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.213)

- **PATRÓN** `ibs_20min` > `0.9275` → IC=+0.292 (n=1390)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9275 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.018` → IC=+0.331 (n=656)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.018 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` > `0.2804` → IC=+0.270 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2804 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` < `1.8388` → IC=+0.206 (n=1313)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8388 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` > `1.4374` → IC=+0.213 (n=1969)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4374 (IC base=+0.213)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.225 (n=2239)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.213)

- **PATRÓN** `libro_liquidez` > `2087.345` → IC=+0.219 (n=695)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2087.345 (IC base=+0.213)

- **PATRÓN** `sigma_h` < `0.0081` → IC=+0.249 (n=1630)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0081 (IC base=+0.247)

- **PATRÓN** `sigma_h` > `0.0072` → IC=+0.257 (n=739)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0072 (IC base=+0.247)

- **PATRÓN** `drift_60min` |x|≤ `0.0955` → IC=+0.301 (n=718)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0955 (IC base=+0.247)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.253 (n=1475)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.247)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.250 (n=795)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.247)

- **PATRÓN** `ibs_20min` < `0.3916` → IC=+0.264 (n=1631)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3916 (IC base=+0.247)

- **PATRÓN** `volumen_pendiente_norm` < `0.0993` → IC=+0.248 (n=1420)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0993 (IC base=+0.247)

- **PATRÓN** `volumen_pendiente_norm` > `0.2954` → IC=+0.282 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2954 (IC base=+0.247)

- **PATRÓN** `volumen_spike_ratio` < `2.2595` → IC=+0.255 (n=1356)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.2595 (IC base=+0.247)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.252 (n=1827)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.247)

- **PATRÓN** `libro_liquidez` > `1541.32` → IC=+0.257 (n=1630)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1541.32 (IC base=+0.247)

- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.252 (n=579)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 8.0 (IC base=+0.247)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.220 (n=629)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.155)

- **PATRÓN** `drift_60min` |x|≤ `0.1597` → IC=+0.183 (n=1248)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.1597 (IC base=+0.155)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.171 (n=1972)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 5.0 (IC base=+0.155)

- **PATRÓN** `ibs_20min` > `0.3425` → IC=+0.224 (n=1871)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3425 (IC base=+0.155)

- **PATRÓN** `dist_vwap_pct` > `0.1342` → IC=+0.215 (n=1135)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1342 (IC base=+0.155)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.393` → IC=+0.224 (n=353)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.393 (IC base=+0.155)

- **PATRÓN** `volumen_regimen` < `0.6892` → IC=+0.164 (n=825)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.6892 (IC base=+0.155)

- **PATRÓN** `volumen_pendiente_norm` > `0.2823` → IC=+0.187 (n=298)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.2823 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` < `1.414` → IC=+0.180 (n=611)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 1.414 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` > `2.5048` → IC=+0.161 (n=611)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 2.5048 (IC base=+0.155)

- **PATRÓN** `ballena_activa_n` < `423.0` → IC=+0.159 (n=1794)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 423.0 (IC base=+0.155)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.169 (n=1973)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0058 (IC base=+0.143)

- **PATRÓN** `drift_60min` |x|≤ `0.2342` → IC=+0.172 (n=1734)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.2342 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.182 (n=944)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 15.0 (IC base=+0.143)

- **PATRÓN** `ibs_20min` < `0.6182` → IC=+0.203 (n=1970)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6182 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.539` → IC=+0.196 (n=376)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 11.539 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` < `1.204` → IC=+0.158 (n=1970)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.204 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` < `0.0938` → IC=+0.145 (n=1665)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` < 0.0938 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` > `0.1586` → IC=+0.144 (n=605)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_pendiente_norm` > 0.1586 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` < `2.5035` → IC=+0.151 (n=1850)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.5035 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` > `1.4236` → IC=+0.146 (n=1850)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.4236 (IC base=+0.143)

- **PATRÓN** `ballena_activa_n` < `202.0` → IC=+0.176 (n=593)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 202.0 (IC base=+0.143)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.234 (n=960)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0107 (IC base=+0.213)

- **PATRÓN** `drift_60min` |x|≤ `0.3956` → IC=+0.225 (n=1858)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3956 (IC base=+0.213)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.231 (n=768)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.213)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.303 (n=1098)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.442` → IC=+0.293 (n=487)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.442 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` < `0.0994` → IC=+0.213 (n=1800)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0994 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` > `0.353` → IC=+0.227 (n=306)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.353 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` < `1.766` → IC=+0.212 (n=899)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.766 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` > `2.7084` → IC=+0.230 (n=927)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7084 (IC base=+0.213)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.221 (n=2510)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.213)

- **PATRÓN** `libro_liquidez` > `1973.887` → IC=+0.226 (n=957)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1973.887 (IC base=+0.213)

- **PATRÓN** `sigma_h` < `0.0087` → IC=+0.252 (n=1210)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0087 (IC base=+0.235)

- **PATRÓN** `drift_60min` |x|≤ `0.1429` → IC=+0.273 (n=798)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1429 (IC base=+0.235)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.281 (n=691)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.235)

- **PATRÓN** `ibs_20min` < `0.0058` → IC=+0.298 (n=797)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0058 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.533` → IC=+0.278 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.533 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` > `0.3534` → IC=+0.279 (n=296)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3534 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` < `1.7408` → IC=+0.235 (n=760)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7408 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` > `2.1502` → IC=+0.239 (n=1152)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1502 (IC base=+0.235)

- **PATRÓN** `libro_liquidez` > `2055.5584` → IC=+0.244 (n=604)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2055.5584 (IC base=+0.235)

- **PATRÓN** `ballena_activa_n` < `10.0` → IC=+0.232 (n=805)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 10.0 (IC base=+0.235)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.183 (n=1780)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0064 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.4031` → IC=+0.168 (n=2022)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.4031 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.163 (n=2100)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` > `0.3118` → IC=+0.213 (n=2022)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3118 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` > `0.1399` → IC=+0.197 (n=1244)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.1399 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.774` → IC=+0.197 (n=351)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 11.774 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` < `1.028` → IC=+0.159 (n=1779)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.028 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.1028` → IC=+0.178 (n=831)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.1028 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `1.5369` → IC=+0.152 (n=875)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 1.5369 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` > `2.5072` → IC=+0.165 (n=661)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 2.5072 (IC base=+0.151)

- **PATRÓN** `libro_liquidez` > `4648.9712` → IC=+0.190 (n=1348)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 4648.9712 (IC base=+0.151)

- **PATRÓN** `ballena_activa_n` < `141.0` → IC=+0.159 (n=1959)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 141.0 (IC base=+0.151)

- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.153 (n=2132)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0071 (IC base=+0.125)

- **PATRÓN** `drift_60min` |x|≤ `0.3948` → IC=+0.144 (n=2131)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.3948 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.165 (n=1012)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 15.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` < `0.6837` → IC=+0.185 (n=2131)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.6837 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` < `0.1526` → IC=+0.155 (n=2123)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1526 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.826` → IC=+0.154 (n=746)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 6.826 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` < `0.857` → IC=+0.158 (n=1421)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.857 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` > `0.2982` → IC=+0.199 (n=320)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2982 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` < `1.808` → IC=+0.134 (n=1330)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 1.808 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` > `1.4232` → IC=+0.127 (n=1994)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` > 1.4232 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `7630.6935` → IC=+0.189 (n=966)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 7630.6935 (IC base=+0.125)

- **PATRÓN** `ballena_activa_n` < `68.0` → IC=+0.145 (n=857)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 68.0 (IC base=+0.125)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0103` → IC=+0.178 (n=1031)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` > 0.0103 (IC base=+0.128)

- **PATRÓN** `drift_60min` |x|≤ `0.4388` → IC=+0.131 (n=2001)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.65€ cuando `drift_60min` |x|≤ 0.4388 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.143 (n=2318)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` > `0.4872` → IC=+0.216 (n=2276)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4872 (IC base=+0.128)

- **PATRÓN** `dist_vwap_pct` > `0.1947` → IC=+0.189 (n=1331)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.1947 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.644` → IC=+0.273 (n=486)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.644 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` < `1.179` → IC=+0.143 (n=2274)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 1.179 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` < `0.1609` → IC=+0.135 (n=2307)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` < 0.1609 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` > `0.2785` → IC=+0.128 (n=315)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` > 0.2785 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` < `1.5438` → IC=+0.144 (n=970)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.5438 (IC base=+0.128)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.129 (n=2375)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.02 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `2812.8978` → IC=+0.207 (n=1031)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2812.8978 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.163 (n=719)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 20.0 (IC base=+0.128)

- **PATRÓN** `sigma_h` < `0.0108` → IC=+0.136 (n=2334)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` < 0.0108 (IC base=+0.118)

- **PATRÓN** `drift_60min` |x|≤ `0.1079` → IC=+0.169 (n=778)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.1079 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.138 (n=2371)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` < `0.5932` → IC=+0.217 (n=2332)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5932 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` < `0.2001` → IC=+0.146 (n=2200)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.2001 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.392` → IC=+0.127 (n=470)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` > 7.392 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.478` → IC=+0.127 (n=2062)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` < 2.478 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` < `1.1736` → IC=+0.129 (n=2332)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 1.1736 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` > `0.2754` → IC=+0.148 (n=308)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.2754 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` < `1.4479` → IC=+0.131 (n=724)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 1.4479 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` > `2.4313` → IC=+0.136 (n=723)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 2.4313 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `2657.9934` → IC=+0.190 (n=1058)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 2657.9934 (IC base=+0.118)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.128 (n=1877)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 42.0 (IC base=+0.118)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0129` → IC=+0.246 (n=1874)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0129 (IC base=+0.221)

- **PATRÓN** `drift_60min` |x|≤ `0.1746` → IC=+0.236 (n=923)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1746 (IC base=+0.221)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.224 (n=2176)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.221)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.228 (n=1423)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.221)

- **PATRÓN** `ibs_20min` > `0.74` → IC=+0.267 (n=1876)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.74 (IC base=+0.221)

- **PATRÓN** `dist_vwap_pct` > `0.1858` → IC=+0.226 (n=1366)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1858 (IC base=+0.221)

- **PATRÓN** `dist_vwap_pct` < `0.48` → IC=+0.223 (n=1869)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.48 (IC base=+0.221)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.61` → IC=+0.250 (n=953)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.61 (IC base=+0.221)

- **PATRÓN** `volumen_regimen` < `1.1768` → IC=+0.224 (n=2098)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1768 (IC base=+0.221)

- **PATRÓN** `volumen_regimen` > `0.6195` → IC=+0.229 (n=2097)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6195 (IC base=+0.221)

- **PATRÓN** `volumen_pendiente_norm` > `0.2825` → IC=+0.271 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2825 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` < `2.4628` → IC=+0.226 (n=2041)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4628 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` > `1.8052` → IC=+0.229 (n=1361)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8052 (IC base=+0.221)

- **PATRÓN** `libro_liquidez` > `2631.2954` → IC=+0.226 (n=1398)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2631.2954 (IC base=+0.221)

- **PATRÓN** `sigma_h` < `0.0124` → IC=+0.236 (n=948)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0124 (IC base=+0.228)

- **PATRÓN** `sigma_h` > `0.0225` → IC=+0.238 (n=977)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0225 (IC base=+0.228)

- **PATRÓN** `drift_60min` |x|≤ `0.089` → IC=+0.260 (n=718)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.089 (IC base=+0.228)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.247 (n=1050)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.228)

- **PATRÓN** `ibs_20min` < `0.4259` → IC=+0.256 (n=2154)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4259 (IC base=+0.228)

- **PATRÓN** `dist_vwap_pct` > `0.2942` → IC=+0.234 (n=577)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2942 (IC base=+0.228)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.355` → IC=+0.255 (n=410)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.355 (IC base=+0.228)

- **PATRÓN** `volumen_regimen` > `0.7072` → IC=+0.234 (n=1924)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7072 (IC base=+0.228)

- **PATRÓN** `volumen_pendiente_norm` > `0.28` → IC=+0.284 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.28 (IC base=+0.228)

- **PATRÓN** `volumen_spike_ratio` > `1.4388` → IC=+0.231 (n=2000)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4388 (IC base=+0.228)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.228 (n=2784)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.228)

- **PATRÓN** `libro_liquidez` > `2374.1526` → IC=+0.230 (n=1924)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2374.1526 (IC base=+0.228)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.208 (n=1395)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.180)

- **PATRÓN** `sigma_h` > `0.0088` → IC=+0.192 (n=1058)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` > 0.0088 (IC base=+0.180)

- **PATRÓN** `drift_60min` |x|≤ `0.1292` → IC=+0.200 (n=1396)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1292 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.215 (n=1551)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` > `0.7275` → IC=+0.231 (n=2114)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7275 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` > `0.7834` → IC=+0.201 (n=489)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7834 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.66` → IC=+0.210 (n=1370)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.66 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` < `0.863` → IC=+0.202 (n=1899)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.863 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` > `0.6967` → IC=+0.184 (n=2544)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` > 0.6967 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.0999` → IC=+0.192 (n=1145)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.0999 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` < `1.4352` → IC=+0.195 (n=1028)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 1.4352 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `2.5135` → IC=+0.189 (n=1028)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 2.5135 (IC base=+0.180)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.186 (n=3588)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.02 (IC base=+0.180)

- **PATRÓN** `libro_liquidez` > `2704.1228` → IC=+0.187 (n=2833)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 2704.1228 (IC base=+0.180)

- **PATRÓN** `ballena_activa_n` < `150.0` → IC=+0.192 (n=2951)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 150.0 (IC base=+0.180)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.133 (n=1132)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` < 0.0037 (IC base=+0.090)

- **PATRÓN** `ibs_20min` < `0.3802` → IC=+0.161 (n=2257)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` < 0.3802 (IC base=+0.090)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.130 (n=1096)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 19.0 (IC base=+0.090)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.211 (n=393)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.174)

- **PATRÓN** `drift_60min` |x|≤ `0.3259` → IC=+0.197 (n=892)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.3259 (IC base=+0.174)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.202 (n=807)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.174)

- **PATRÓN** `ibs_20min` > `0.6473` → IC=+0.232 (n=594)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6473 (IC base=+0.174)

- **PATRÓN** `dist_vwap_pct` > `0.2987` → IC=+0.193 (n=278)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.2987 (IC base=+0.174)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.109` → IC=+0.192 (n=381)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 3.109 (IC base=+0.174)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.775` → IC=+0.176 (n=945)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` < 6.775 (IC base=+0.174)

- **PATRÓN** `volumen_regimen` < `0.8739` → IC=+0.200 (n=595)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8739 (IC base=+0.174)

- **PATRÓN** `volumen_pendiente_norm` > `0.0716` → IC=+0.177 (n=354)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.0716 (IC base=+0.174)

- **PATRÓN** `volumen_spike_ratio` < `2.2086` → IC=+0.183 (n=769)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` < 2.2086 (IC base=+0.174)

- **PATRÓN** `volumen_spike_ratio` > `1.4162` → IC=+0.175 (n=873)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 1.4162 (IC base=+0.174)

- **PATRÓN** `libro_liquidez` > `14721.2123` → IC=+0.186 (n=594)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 14721.2123 (IC base=+0.174)

- **PATRÓN** `ballena_activa_n` < `158.0` → IC=+0.200 (n=381)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 158.0 (IC base=+0.174)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.142 (n=1053)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.0056 (IC base=+0.118)

- **PATRÓN** `drift_60min` |x|≤ `0.3403` → IC=+0.136 (n=1052)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.68€ cuando `drift_60min` |x|≤ 0.3403 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.127 (n=944)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 7.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` < `0.6403` → IC=+0.166 (n=926)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.6403 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` < `0.1841` → IC=+0.141 (n=1067)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.1841 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.715` → IC=+0.131 (n=204)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` > 8.715 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` > `1.0611` → IC=+0.149 (n=477)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 1.0611 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` > `0.1595` → IC=+0.164 (n=278)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` > 0.1595 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` < `2.1169` → IC=+0.130 (n=915)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 2.1169 (IC base=+0.118)

- **PATRÓN** `ballena_activa_n` < `308.0` → IC=+0.146 (n=898)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 308.0 (IC base=+0.118)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.248 (n=650)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.215)

- **PATRÓN** `drift_60min` |x|≤ `0.0944` → IC=+0.240 (n=325)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0944 (IC base=+0.215)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.231 (n=1021)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.215)

- **PATRÓN** `ibs_20min` > `0.6864` → IC=+0.274 (n=649)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6864 (IC base=+0.215)

- **PATRÓN** `dist_vwap_pct` > `0.3552` → IC=+0.222 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3552 (IC base=+0.215)

- **PATRÓN** `dist_vwap_pct` < `0.2032` → IC=+0.220 (n=875)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2032 (IC base=+0.215)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.884` → IC=+0.242 (n=394)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.884 (IC base=+0.215)

- **PATRÓN** `volumen_regimen` < `0.8344` → IC=+0.224 (n=650)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8344 (IC base=+0.215)

- **PATRÓN** `volumen_regimen` > `1.1666` → IC=+0.225 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1666 (IC base=+0.215)

- **PATRÓN** `volumen_pendiente_norm` > `0.1551` → IC=+0.247 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1551 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` < `1.4185` → IC=+0.249 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4185 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` > `2.4608` → IC=+0.234 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4608 (IC base=+0.215)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.215 (n=1088)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.215)

- **PATRÓN** `ibs_20min` < `0.104` → IC=+0.167 (n=328)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.104 (IC base=+0.063)

- **PATRÓN** `libro_liquidez` > `6737.5602` → IC=+0.132 (n=656)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 6737.5602 (IC base=+0.063)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.174 (n=354)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` > 0.0097 (IC base=+0.161)

- **PATRÓN** `drift_60min` |x|≤ `0.5315` → IC=+0.162 (n=780)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.5315 (IC base=+0.161)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.217 (n=373)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.161)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.273 (n=364)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.161)

- **PATRÓN** `dist_vwap_pct` > `0.9916` → IC=+0.238 (n=143)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9916 (IC base=+0.161)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.1` → IC=+0.227 (n=328)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.1 (IC base=+0.161)

- **PATRÓN** `volumen_regimen` < `1.0604` → IC=+0.177 (n=686)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` < 1.0604 (IC base=+0.161)

- **PATRÓN** `volumen_regimen` > `0.7177` → IC=+0.168 (n=697)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` > 0.7177 (IC base=+0.161)

- **PATRÓN** `volumen_pendiente_norm` > `0.1642` → IC=+0.182 (n=218)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.1642 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` < `1.454` → IC=+0.164 (n=251)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.454 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` > `2.1801` → IC=+0.176 (n=341)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 2.1801 (IC base=+0.161)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.168 (n=805)

  - _Acción_: Kelly boost +0.84€ cuando `libro_spread` < 0.02 (IC base=+0.161)

- **PATRÓN** `libro_liquidez` > `3054.254` → IC=+0.191 (n=260)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 3054.254 (IC base=+0.161)

- **PATRÓN** `ibs_20min` < `0.6667` → IC=+0.121 (n=826)

  - _Acción_: Kelly boost +0.60€ cuando `ibs_20min` < 0.6667 (IC base=+0.058)

- **PATRÓN** `libro_liquidez` > `2725.786` → IC=+0.148 (n=373)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 2725.786 (IC base=+0.058)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.131 (n=529)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 21.0 (IC base=+0.058)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` < `0.0239` → IC=+0.157 (n=205)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0239 (IC base=+0.153)

- **PATRÓN** `sigma_h` > `0.0211` → IC=+0.174 (n=93)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` > 0.0211 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.254` → IC=+0.176 (n=137)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.254 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.183 (n=77)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 15.0 (IC base=+0.153)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.202 (n=92)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` > `0.56` → IC=+0.188 (n=184)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.56 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` > `0.301` → IC=+0.167 (n=106)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.301 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.301` → IC=+0.182 (n=174)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` < 3.301 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` > `1.0169` → IC=+0.174 (n=93)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` > 1.0169 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` < `0.2493` → IC=+0.178 (n=203)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` < 0.2493 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` > `0.1876` → IC=+0.173 (n=50)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.1876 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `1.4605` → IC=+0.226 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4605 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` > `2.6057` → IC=+0.194 (n=60)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.6057 (IC base=+0.153)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.173 (n=246)

  - _Acción_: Kelly boost +0.87€ cuando `libro_spread` < 0.03 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `2731.7891` → IC=+0.174 (n=93)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 2731.7891 (IC base=+0.153)

- **PATRÓN** `sigma_h` > `0.012` → IC=+0.152 (n=208)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` > 0.012 (IC base=+0.115)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.167 (n=79)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 17.0 (IC base=+0.115)

- **PATRÓN** `ibs_20min` < `0.6` → IC=+0.130 (n=233)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` < 0.6 (IC base=+0.115)

- **PATRÓN** `dist_vwap_pct` > `1.1142` → IC=+0.255 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1142 (IC base=+0.115)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.064` → IC=+0.151 (n=61)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 5.064 (IC base=+0.115)

- **PATRÓN** `volumen_regimen` > `1.064` → IC=+0.130 (n=106)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` > 1.064 (IC base=+0.115)

- **PATRÓN** `volumen_pendiente_norm` > `0.2302` → IC=+0.167 (n=43)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.2302 (IC base=+0.115)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.136 (n=193)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 17.0 (IC base=+0.115)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.183 (n=5416)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0047 (IC base=+0.182)

- **PATRÓN** `sigma_h` > `0.0115` → IC=+0.225 (n=5418)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0115 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.191 (n=16904)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 5.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` > `0.4483` → IC=+0.230 (n=16225)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4483 (IC base=+0.182)

- **PATRÓN** `dist_vwap_pct` > `0.901` → IC=+0.210 (n=2019)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.901 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.294` → IC=+0.253 (n=3967)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.294 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` < `1.2214` → IC=+0.170 (n=10875)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 1.2214 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.2905` → IC=+0.207 (n=2158)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2905 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `2.6119` → IC=+0.197 (n=5257)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 2.6119 (IC base=+0.182)

- **PATRÓN** `libro_liquidez` > `1807.7032` → IC=+0.185 (n=16224)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 1807.7032 (IC base=+0.182)

- **PATRÓN** `ballena_activa_n` < `114.0` → IC=+0.203 (n=14874)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 114.0 (IC base=+0.182)

- **PATRÓN** `sigma_h` < `0.0055` → IC=+0.193 (n=6511)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0055 (IC base=+0.187)

- **PATRÓN** `drift_60min` |x|≤ `0.3803` → IC=+0.191 (n=12995)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.3803 (IC base=+0.187)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.209 (n=5501)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.187)

- **PATRÓN** `ibs_20min` < `0.5817` → IC=+0.241 (n=14768)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5817 (IC base=+0.187)

- **PATRÓN** `dist_vwap_pct` < `0.1752` → IC=+0.170 (n=8985)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` < 0.1752 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.858` → IC=+0.204 (n=2054)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.858 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.595` → IC=+0.189 (n=14264)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` < 3.595 (IC base=+0.187)

- **PATRÓN** `volumen_regimen` < `0.705` → IC=+0.160 (n=4386)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.705 (IC base=+0.187)

- **PATRÓN** `volumen_pendiente_norm` > `0.2898` → IC=+0.252 (n=1993)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2898 (IC base=+0.187)

- **PATRÓN** `volumen_spike_ratio` > `2.2587` → IC=+0.196 (n=6322)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.2587 (IC base=+0.187)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.215 (n=9130)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 40.0 (IC base=+0.187)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.236 (n=889)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.223)

- **PATRÓN** `drift_60min` |x|≤ `0.3478` → IC=+0.226 (n=2650)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3478 (IC base=+0.223)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.235 (n=1276)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.223)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.227 (n=1792)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.223)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.329 (n=1036)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.223)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.577` → IC=+0.352 (n=618)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.577 (IC base=+0.223)

- **PATRÓN** `volumen_pendiente_norm` > `0.279` → IC=+0.284 (n=346)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.279 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` > `2.2722` → IC=+0.236 (n=1153)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2722 (IC base=+0.223)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.240 (n=2803)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.223)

- **PATRÓN** `libro_liquidez` > `2085.52` → IC=+0.233 (n=883)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2085.52 (IC base=+0.223)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.244 (n=1568)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 17.0 (IC base=+0.223)

- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.265 (n=2264)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0084 (IC base=+0.261)

- **PATRÓN** `drift_60min` |x|≤ `0.1205` → IC=+0.281 (n=998)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1205 (IC base=+0.261)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.269 (n=2067)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.261)

- **PATRÓN** `ibs_20min` < `0.5069` → IC=+0.288 (n=2263)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5069 (IC base=+0.261)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.354` → IC=+0.264 (n=700)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.354 (IC base=+0.261)

- **PATRÓN** `volumen_pendiente_norm` < `0.0703` → IC=+0.262 (n=1921)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0703 (IC base=+0.261)

- **PATRÓN** `volumen_pendiente_norm` > `0.2832` → IC=+0.281 (n=318)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2832 (IC base=+0.261)

- **PATRÓN** `volumen_spike_ratio` < `1.4411` → IC=+0.261 (n=714)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4411 (IC base=+0.261)

- **PATRÓN** `volumen_spike_ratio` > `2.6396` → IC=+0.271 (n=714)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6396 (IC base=+0.261)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.263 (n=2536)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.261)

- **PATRÓN** `libro_liquidez` > `1671.94` → IC=+0.269 (n=2022)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1671.94 (IC base=+0.261)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.267 (n=1002)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.261)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.200 (n=874)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.1045` → IC=+0.168 (n=1153)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.1045 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.163 (n=2731)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` > `0.376` → IC=+0.226 (n=2340)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.376 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.1243` → IC=+0.196 (n=1374)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.1243 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.602` → IC=+0.164 (n=432)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 11.602 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.159` → IC=+0.155 (n=2404)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 4.159 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `0.6282` → IC=+0.172 (n=874)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` < 0.6282 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` < `0.0723` → IC=+0.154 (n=2332)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` < 0.0723 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.272` → IC=+0.179 (n=375)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.272 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `2.1856` → IC=+0.160 (n=2252)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.1856 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `1.5327` → IC=+0.154 (n=2287)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.5327 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `267.0` → IC=+0.183 (n=1109)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 267.0 (IC base=+0.150)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.163 (n=2195)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0058 (IC base=+0.143)

- **PATRÓN** `drift_60min` |x|≤ `0.2576` → IC=+0.162 (n=1932)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.2576 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.170 (n=830)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.143)

- **PATRÓN** `ibs_20min` < `0.7028` → IC=+0.197 (n=2195)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.7028 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` < `0.1347` → IC=+0.164 (n=2053)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.1347 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.204` → IC=+0.157 (n=365)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 11.204 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.456` → IC=+0.143 (n=2212)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 6.456 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` < `1.186` → IC=+0.152 (n=2195)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.186 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` > `0.2172` → IC=+0.196 (n=412)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2172 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` < `2.4323` → IC=+0.148 (n=2091)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 2.4323 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` > `1.7755` → IC=+0.155 (n=1394)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.7755 (IC base=+0.143)

- **PATRÓN** `ballena_activa_n` < `276.0` → IC=+0.155 (n=882)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 276.0 (IC base=+0.143)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0123` → IC=+0.258 (n=904)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0123 (IC base=+0.225)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.232 (n=2823)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.227 (n=2423)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.225)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.303 (n=1008)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.225)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.31` → IC=+0.319 (n=573)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.31 (IC base=+0.225)

- **PATRÓN** `volumen_pendiente_norm` < `0.0977` → IC=+0.228 (n=2384)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0977 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` > `2.7011` → IC=+0.238 (n=1188)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7011 (IC base=+0.225)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.233 (n=3209)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.225)

- **PATRÓN** `libro_liquidez` > `1842.4048` → IC=+0.237 (n=1801)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1842.4048 (IC base=+0.225)

- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.244 (n=2233)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0106 (IC base=+0.240)

- **PATRÓN** `drift_60min` |x|≤ `0.1818` → IC=+0.256 (n=1116)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1818 (IC base=+0.240)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.262 (n=952)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.240)

- **PATRÓN** `ibs_20min` < `0.0288` → IC=+0.303 (n=846)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0288 (IC base=+0.240)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.0` → IC=+0.292 (n=407)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.0 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` > `0.3452` → IC=+0.300 (n=373)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3452 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` > `2.1315` → IC=+0.251 (n=1606)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1315 (IC base=+0.240)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.241 (n=1344)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.240)

- **PATRÓN** `libro_liquidez` > `2054.9584` → IC=+0.258 (n=846)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2054.9584 (IC base=+0.240)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.247 (n=1554)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 19.0 (IC base=+0.240)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.199 (n=1230)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0038 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.4176` → IC=+0.158 (n=2791)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.4176 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.161 (n=2899)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 5.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` > `0.2506` → IC=+0.195 (n=2790)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 0.2506 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.1406` → IC=+0.170 (n=1493)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.1406 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.153` → IC=+0.162 (n=1136)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 4.153 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `0.8682` → IC=+0.167 (n=1861)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.8682 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.281` → IC=+0.189 (n=365)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.281 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `1.5231` → IC=+0.166 (n=1198)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 1.5231 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` > `2.1683` → IC=+0.158 (n=1235)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 2.1683 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `6546.3895` → IC=+0.244 (n=1265)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6546.3895 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `74.0` → IC=+0.173 (n=1174)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 74.0 (IC base=+0.146)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.189 (n=774)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0033 (IC base=+0.127)

- **PATRÓN** `drift_60min` |x|≤ `0.4388` → IC=+0.138 (n=2318)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.4388 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.150 (n=846)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 17.0 (IC base=+0.127)

- **PATRÓN** `ibs_20min` < `0.7395` → IC=+0.182 (n=2318)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.7395 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` < `0.1476` → IC=+0.143 (n=2097)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.1476 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.137` → IC=+0.166 (n=354)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 11.137 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` < `0.8715` → IC=+0.138 (n=1546)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 0.8715 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` > `0.2964` → IC=+0.228 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2964 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` > `1.4314` → IC=+0.137 (n=2229)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.4314 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `7319.7397` → IC=+0.211 (n=773)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7319.7397 (IC base=+0.127)

- **PATRÓN** `ballena_activa_n` < `67.0` → IC=+0.128 (n=753)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 67.0 (IC base=+0.127)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0102` → IC=+0.155 (n=1273)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` > 0.0102 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.177 (n=1027)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` > `0.4432` → IC=+0.200 (n=2808)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4432 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` > `1.064` → IC=+0.208 (n=498)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.064 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.764` → IC=+0.268 (n=709)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.764 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` < `1.2221` → IC=+0.136 (n=2809)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 1.2221 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` < `0.0984` → IC=+0.125 (n=2650)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.0984 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` > `0.2785` → IC=+0.142 (n=361)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` > 0.2785 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` < `1.8314` → IC=+0.127 (n=1829)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 1.8314 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` > `2.1924` → IC=+0.132 (n=1243)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 2.1924 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.130 (n=2905)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.02 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `2504.2715` → IC=+0.234 (n=1273)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2504.2715 (IC base=+0.125)

- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.140 (n=908)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 25.0 (IC base=+0.125)

- **PATRÓN** `sigma_h` < `0.0099` → IC=+0.148 (n=2360)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0099 (IC base=+0.117)

- **PATRÓN** `drift_60min` |x|≤ `0.1341` → IC=+0.154 (n=894)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.1341 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.130 (n=2766)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 5.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` < `0.6463` → IC=+0.210 (n=2681)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6463 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` < `0.2143` → IC=+0.136 (n=2302)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.2143 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.298` → IC=+0.134 (n=2583)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` < 3.298 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` < `0.7113` → IC=+0.135 (n=1180)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 0.7113 (IC base=+0.117)

- **PATRÓN** `volumen_pendiente_norm` > `0.2242` → IC=+0.167 (n=455)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` > 0.2242 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` < `1.44` → IC=+0.152 (n=836)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 1.44 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `2679.9048` → IC=+0.211 (n=894)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2679.9048 (IC base=+0.117)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.133 (n=2195)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 47.0 (IC base=+0.117)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0136` → IC=+0.247 (n=2374)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0136 (IC base=+0.228)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.233 (n=2775)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.228)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.237 (n=1777)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.228)

- **PATRÓN** `ibs_20min` > `0.6098` → IC=+0.271 (n=2375)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6098 (IC base=+0.228)

- **PATRÓN** `dist_vwap_pct` > `0.1918` → IC=+0.244 (n=1451)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1918 (IC base=+0.228)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.761` → IC=+0.269 (n=888)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.761 (IC base=+0.228)

- **PATRÓN** `volumen_regimen` < `1.2245` → IC=+0.236 (n=2658)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2245 (IC base=+0.228)

- **PATRÓN** `volumen_regimen` > `0.6411` → IC=+0.231 (n=2658)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6411 (IC base=+0.228)

- **PATRÓN** `volumen_pendiente_norm` > `0.2873` → IC=+0.252 (n=333)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2873 (IC base=+0.228)

- **PATRÓN** `volumen_spike_ratio` > `1.549` → IC=+0.236 (n=2309)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.549 (IC base=+0.228)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.230 (n=3450)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.228)

- **PATRÓN** `libro_liquidez` > `2635.0196` → IC=+0.237 (n=1772)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2635.0196 (IC base=+0.228)

- **PATRÓN** `sigma_h` > `0.0229` → IC=+0.248 (n=1258)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0229 (IC base=+0.229)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.236 (n=2608)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.229)

- **PATRÓN** `ibs_20min` < `0.5129` → IC=+0.265 (n=2775)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5129 (IC base=+0.229)

- **PATRÓN** `dist_vwap_pct` < `0.2911` → IC=+0.233 (n=2671)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2911 (IC base=+0.229)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.219` → IC=+0.265 (n=533)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.219 (IC base=+0.229)

- **PATRÓN** `volumen_regimen` > `1.227` → IC=+0.257 (n=925)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.227 (IC base=+0.229)

- **PATRÓN** `volumen_pendiente_norm` > `0.2805` → IC=+0.299 (n=371)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2805 (IC base=+0.229)

- **PATRÓN** `volumen_spike_ratio` > `1.432` → IC=+0.232 (n=2573)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.432 (IC base=+0.229)

- **PATRÓN** `libro_liquidez` > `2385.8449` → IC=+0.229 (n=2479)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2385.8449 (IC base=+0.229)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.192 (n=4835)

- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.243 (n=1654)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=+0.205)

- **PATRÓN** `drift_60min` |x|≤ `0.5051` → IC=+0.215 (n=4944)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5051 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.221 (n=1784)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.205)

- **PATRÓN** `ibs_20min` > `0.9401` → IC=+0.247 (n=1650)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9401 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` > `0.1707` → IC=+0.209 (n=1855)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1707 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` < `0.4314` → IC=+0.210 (n=3572)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4314 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.725` → IC=+0.213 (n=1610)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.725 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.629` → IC=+0.206 (n=4406)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.629 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` < `0.7044` → IC=+0.219 (n=1594)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7044 (IC base=+0.205)

- **PATRÓN** `volumen_pendiente_norm` > `0.1668` → IC=+0.220 (n=1388)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1668 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` < `1.4551` → IC=+0.210 (n=1623)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4551 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` > `1.8456` → IC=+0.207 (n=3244)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8456 (IC base=+0.205)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.211 (n=3830)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.205)

- **PATRÓN** `libro_liquidez` > `2945.7901` → IC=+0.214 (n=4416)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2945.7901 (IC base=+0.205)

- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.238 (n=1214)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.190)

- **PATRÓN** `drift_60min` |x|≤ `0.4913` → IC=+0.206 (n=3638)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4913 (IC base=+0.190)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.209 (n=1221)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.208 (n=1636)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.190)

- **PATRÓN** `ibs_20min` < `0.7333` → IC=+0.197 (n=3639)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.7333 (IC base=+0.190)

- **PATRÓN** `dist_vwap_pct` > `0.6714` → IC=+0.200 (n=627)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6714 (IC base=+0.190)

- **PATRÓN** `dist_vwap_pct` < `0.4174` → IC=+0.188 (n=3651)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` < 0.4174 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.118` → IC=+0.198 (n=3653)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` < 6.118 (IC base=+0.190)

- **PATRÓN** `volumen_regimen` < `1.0986` → IC=+0.200 (n=3031)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0986 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` < `0.0975` → IC=+0.194 (n=3334)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` < 0.0975 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` > `0.2229` → IC=+0.194 (n=739)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2229 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` < `1.5329` → IC=+0.195 (n=1579)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 1.5329 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` > `1.8131` → IC=+0.198 (n=2392)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 1.8131 (IC base=+0.190)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.192 (n=4835)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.01 (IC base=+0.190)

- **PATRÓN** `ballena_activa_n` < `169.0` → IC=+0.201 (n=3144)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 169.0 (IC base=+0.190)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.266 (n=643)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.252)

- **PATRÓN** `drift_60min` |x|≤ `0.0855` → IC=+0.293 (n=244)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0855 (IC base=+0.252)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.256 (n=767)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.252)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.258 (n=333)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.252)

- **PATRÓN** `ibs_20min` < `0.4896` → IC=+0.275 (n=486)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4896 (IC base=+0.252)

- **PATRÓN** `dist_vwap_pct` < `0.3275` → IC=+0.267 (n=722)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3275 (IC base=+0.252)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.071` → IC=+0.269 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.071 (IC base=+0.252)

- **PATRÓN** `volumen_regimen` < `1.2117` → IC=+0.259 (n=729)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2117 (IC base=+0.252)

- **PATRÓN** `volumen_regimen` > `0.6018` → IC=+0.258 (n=729)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6018 (IC base=+0.252)

- **PATRÓN** `volumen_pendiente_norm` > `0.2881` → IC=+0.350 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2881 (IC base=+0.252)

- **PATRÓN** `volumen_spike_ratio` < `1.8249` → IC=+0.260 (n=485)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8249 (IC base=+0.252)

- **PATRÓN** `volumen_spike_ratio` > `1.4398` → IC=+0.251 (n=726)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4398 (IC base=+0.252)

- **PATRÓN** `libro_liquidez` > `16374.9374` → IC=+0.271 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16374.9374 (IC base=+0.252)

- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.229 (n=850)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.173)

- **PATRÓN** `drift_60min` |x|≤ `0.3699` → IC=+0.187 (n=1271)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.3699 (IC base=+0.173)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.212 (n=453)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.173)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.201 (n=476)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.173)

- **PATRÓN** `ibs_20min` < `0.1385` → IC=+0.206 (n=560)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1385 (IC base=+0.173)

- **PATRÓN** `ibs_20min` > `0.6084` → IC=+0.173 (n=576)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` > 0.6084 (IC base=+0.173)

- **PATRÓN** `dist_vwap_pct` > `0.6858` → IC=+0.202 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6858 (IC base=+0.173)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.377` → IC=+0.191 (n=1257)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` < 6.377 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` < `1.2232` → IC=+0.188 (n=1271)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 1.2232 (IC base=+0.173)

- **PATRÓN** `volumen_pendiente_norm` > `0.2166` → IC=+0.197 (n=259)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2166 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` < `1.4018` → IC=+0.189 (n=422)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 1.4018 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` > `2.1667` → IC=+0.186 (n=574)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.1667 (IC base=+0.173)

- **PATRÓN** `libro_liquidez` > `14952.5633` → IC=+0.187 (n=576)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 14952.5633 (IC base=+0.173)

- **PATRÓN** `ballena_activa_n` < `698.0` → IC=+0.185 (n=1225)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 698.0 (IC base=+0.173)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.193 (n=252)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0062 (IC base=+0.184)

- **PATRÓN** `sigma_h` > `0.0103` → IC=+0.214 (n=344)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0103 (IC base=+0.184)

- **PATRÓN** `drift_60min` |x|≤ `0.5868` → IC=+0.196 (n=755)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.5868 (IC base=+0.184)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.242 (n=266)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.184)

- **PATRÓN** `ibs_20min` < `0.3897` → IC=+0.185 (n=252)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.3897 (IC base=+0.184)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.237 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.184)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.492` → IC=+0.227 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.492 (IC base=+0.184)

- **PATRÓN** `volumen_pendiente_norm` > `0.211` → IC=+0.237 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.211 (IC base=+0.184)

- **PATRÓN** `volumen_spike_ratio` > `2.2523` → IC=+0.194 (n=502)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.2523 (IC base=+0.184)

- **PATRÓN** `libro_liquidez` > `2474.4708` → IC=+0.222 (n=343)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2474.4708 (IC base=+0.184)

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
- **PATRÓN** `sigma_h` < `0.008` → IC=+0.213 (n=1373)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.008 (IC base=+0.196)

- **PATRÓN** `drift_60min` |x|≤ `0.4596` → IC=+0.204 (n=1373)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4596 (IC base=+0.196)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.214 (n=498)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.196)

- **PATRÓN** `ibs_20min` < `0.5189` → IC=+0.209 (n=916)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5189 (IC base=+0.196)

- **PATRÓN** `ibs_20min` > `0.7596` → IC=+0.198 (n=623)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.7596 (IC base=+0.196)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.114` → IC=+0.205 (n=1235)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.114 (IC base=+0.196)

- **PATRÓN** `volumen_regimen` < `0.8782` → IC=+0.199 (n=916)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8782 (IC base=+0.196)

- **PATRÓN** `volumen_regimen` > `1.2326` → IC=+0.204 (n=458)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2326 (IC base=+0.196)

- **PATRÓN** `volumen_pendiente_norm` < `0.1051` → IC=+0.200 (n=1263)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1051 (IC base=+0.196)

- **PATRÓN** `volumen_pendiente_norm` > `0.164` → IC=+0.196 (n=409)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.164 (IC base=+0.196)

- **PATRÓN** `volumen_spike_ratio` < `2.4559` → IC=+0.204 (n=1344)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4559 (IC base=+0.196)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.197 (n=1409)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.01 (IC base=+0.196)

- **PATRÓN** `sigma_h` < `0.008` → IC=+0.206 (n=1120)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.008 (IC base=+0.188)

- **PATRÓN** `drift_60min` |x|≤ `0.4933` → IC=+0.212 (n=1120)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4933 (IC base=+0.188)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.204 (n=437)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.200 (n=750)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.188)

- **PATRÓN** `ibs_20min` < `0.3984` → IC=+0.197 (n=747)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.3984 (IC base=+0.188)

- **PATRÓN** `ibs_20min` > `0.0864` → IC=+0.191 (n=1119)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.0864 (IC base=+0.188)

- **PATRÓN** `dist_vwap_pct` > `0.6674` → IC=+0.199 (n=197)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.6674 (IC base=+0.188)

- **PATRÓN** `dist_vwap_pct` < `0.2251` → IC=+0.190 (n=1081)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` < 0.2251 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.719` → IC=+0.193 (n=1145)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` < 6.719 (IC base=+0.188)

- **PATRÓN** `volumen_regimen` < `0.6394` → IC=+0.226 (n=374)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6394 (IC base=+0.188)

- **PATRÓN** `volumen_pendiente_norm` > `0.0744` → IC=+0.210 (n=470)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0744 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` < `2.1931` → IC=+0.199 (n=964)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 2.1931 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` > `1.7867` → IC=+0.190 (n=730)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 1.7867 (IC base=+0.188)

- **PATRÓN** `libro_liquidez` > `6849.7278` → IC=+0.195 (n=1119)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 6849.7278 (IC base=+0.188)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0107` → IC=+0.201 (n=643)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0107 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.201 (n=751)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 3.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` > `0.925` → IC=+0.245 (n=332)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.925 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` > `0.743` → IC=+0.238 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.743 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.204` → IC=+0.210 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.204 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` < `0.6978` → IC=+0.228 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6978 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` < `0.1064` → IC=+0.191 (n=658)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` < 0.1064 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.0795` → IC=+0.192 (n=326)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.0795 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` < `1.5679` → IC=+0.195 (n=313)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 1.5679 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `2.4918` → IC=+0.203 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4918 (IC base=+0.180)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.186 (n=851)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.02 (IC base=+0.180)

- **PATRÓN** `libro_liquidez` > `3551.9496` → IC=+0.212 (n=487)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3551.9496 (IC base=+0.180)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.198 (n=713)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 52.0 (IC base=+0.180)

- **PATRÓN** `sigma_h` < `0.0091` → IC=+0.202 (n=354)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0091 (IC base=+0.201)

- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.209 (n=177)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0125 (IC base=+0.201)

- **PATRÓN** `drift_60min` |x|≤ `0.6119` → IC=+0.224 (n=530)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6119 (IC base=+0.201)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.238 (n=360)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 9.0 (IC base=+0.201)

- **PATRÓN** `ibs_20min` < `0.7249` → IC=+0.224 (n=530)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7249 (IC base=+0.201)

- **PATRÓN** `dist_vwap_pct` > `0.5232` → IC=+0.222 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5232 (IC base=+0.201)

- **PATRÓN** `dist_vwap_pct` < `1.2157` → IC=+0.204 (n=590)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 1.2157 (IC base=+0.201)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.868` → IC=+0.210 (n=474)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.868 (IC base=+0.201)

- **PATRÓN** `volumen_regimen` < `1.3392` → IC=+0.205 (n=531)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.3392 (IC base=+0.201)

- **PATRÓN** `volumen_regimen` > `0.9381` → IC=+0.210 (n=353)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.9381 (IC base=+0.201)

- **PATRÓN** `volumen_pendiente_norm` < `0.1072` → IC=+0.223 (n=457)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1072 (IC base=+0.201)

- **PATRÓN** `volumen_spike_ratio` > `2.2044` → IC=+0.243 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2044 (IC base=+0.201)

- **PATRÓN** `libro_liquidez` > `2981.5842` → IC=+0.220 (n=530)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2981.5842 (IC base=+0.201)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.231 (n=519)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 46.0 (IC base=+0.201)

### GBM_LATE_60M
- **FILTRO** `ibs_20min` < `0.5412` → IC=-0.120 (n=667)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5412
  - _Potencial_: sin este filtro IC_bueno=+0.166 (n=1359)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.157 (n=709)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0039 (IC base=+0.068)

- **PATRÓN** `ibs_20min` > `0.5412` → IC=+0.166 (n=1359)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.5412 (IC base=+0.068)

- **PATRÓN** `dist_vwap_pct` > `0.3558` → IC=+0.157 (n=537)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.3558 (IC base=+0.068)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.019` → IC=+0.160 (n=442)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 9.019 (IC base=+0.068)

- **PATRÓN** `ibs_20min` < `0.2` → IC=+0.247 (n=539)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2 (IC base=+0.065)

- **PATRÓN** `dist_vwap_pct` < `0.1008` → IC=+0.130 (n=792)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` < 0.1008 (IC base=+0.065)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.374` → IC=+0.185 (n=128)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 10.374 (IC base=+0.065)

- **PATRÓN** `volumen_pendiente_norm` > `0.147` → IC=+0.191 (n=221)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.147 (IC base=+0.065)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `ibs_20min` < `0.5022` → IC=-0.122 (n=223)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5022
  - _Potencial_: sin este filtro IC_bueno=+0.186 (n=454)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.129 (n=539)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.64€ cuando `sigma_h` < 0.0056 (IC base=+0.083)

- **PATRÓN** `ibs_20min` > `0.5022` → IC=+0.186 (n=454)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.5022 (IC base=+0.083)

- **PATRÓN** `dist_vwap_pct` > `0.1215` → IC=+0.155 (n=256)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.1215 (IC base=+0.083)

- **PATRÓN** `ibs_20min` < `0.0468` → IC=+0.284 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0468 (IC base=+0.081)

- **PATRÓN** `dist_vwap_pct` < `0.1153` → IC=+0.131 (n=375)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.1153 (IC base=+0.081)

- **PATRÓN** `volumen_pendiente_norm` > `0.2165` → IC=+0.194 (n=70)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2165 (IC base=+0.081)

- **PATRÓN** `volumen_spike_ratio` < `1.3896` → IC=+0.126 (n=113)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 1.3896 (IC base=+0.081)

### GBM_LATE_60M#ETH#60min
- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.131 (n=464)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.65€ cuando `sigma_h` < 0.0059 (IC base=+0.093)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.148 (n=265)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 15.0 (IC base=+0.093)

- **PATRÓN** `ibs_20min` > `0.6355` → IC=+0.206 (n=443)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6355 (IC base=+0.093)

- **PATRÓN** `dist_vwap_pct` > `0.1247` → IC=+0.196 (n=258)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.1247 (IC base=+0.093)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.194` → IC=+0.257 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.194 (IC base=+0.093)

- **PATRÓN** `volumen_regimen` < `0.8144` → IC=+0.125 (n=331)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` < 0.8144 (IC base=+0.093)

- **PATRÓN** `volumen_pendiente_norm` > `0.2854` → IC=+0.162 (n=69)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.2854 (IC base=+0.093)

- **PATRÓN** `ibs_20min` < `0.0279` → IC=+0.307 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0279 (IC base=+0.026)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.722` → IC=+0.262 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.722 (IC base=+0.026)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `ibs_20min` < `0.5161` → IC=-0.120 (n=227)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5161
  - _Potencial_: sin este filtro IC_bueno=+0.108 (n=462)

- **FILTRO** `ibs_20min` > `0.1429` → IC=-0.219 (n=62)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1429
  - _Potencial_: sin este filtro IC_bueno=+0.244 (n=193)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.165 (n=347)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` > 0.75 (IC base=+0.028)

- **PATRÓN** `dist_vwap_pct` > `0.7377` → IC=+0.134 (n=129)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` > 0.7377 (IC base=+0.028)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.483` → IC=+0.158 (n=109)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 9.483 (IC base=+0.028)

- **PATRÓN** `volumen_pendiente_norm` > `0.2318` → IC=+0.144 (n=99)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_pendiente_norm` > 0.2318 (IC base=+0.028)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.167 (n=223)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0103 (IC base=+0.084)

- **PATRÓN** `ibs_20min` < `0.1429` → IC=+0.244 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1429 (IC base=+0.084)

- **PATRÓN** `dist_vwap_pct` < `0.6699` → IC=+0.153 (n=223)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.6699 (IC base=+0.084)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.803` → IC=+0.300 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.803 (IC base=+0.084)

- **PATRÓN** `volumen_regimen` > `1.0818` → IC=+0.227 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0818 (IC base=+0.084)

- **PATRÓN** `volumen_pendiente_norm` > `0.1517` → IC=+0.263 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1517 (IC base=+0.084)

- **PATRÓN** `volumen_spike_ratio` > `1.4109` → IC=+0.184 (n=169)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 1.4109 (IC base=+0.084)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.177 (n=162)

  - _Acción_: Kelly boost +0.88€ cuando `libro_spread` < 0.06 (IC base=+0.084)

### GBM_LATE_60M_FADE
- **FILTRO** `hora_utc` > `8.0` → IC=-0.333 (n=64)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=237)

- **FILTRO** `dist_vwap_pct` > `0.2334` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2334
  - _Potencial_: sin este filtro IC_bueno=-0.206 (n=284)

- **FILTRO** `volumen_spike_ratio` > `2.5112` → IC=-0.222 (n=77)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.5112
  - _Potencial_: sin este filtro IC_bueno=-0.158 (n=150)

- **FILTRO** `ibs_20min` > `0.5714` → IC=-0.327 (n=125)

  - _Acción_: SKIP cuando `ibs_20min` > 0.5714
  - _Potencial_: sin este filtro IC_bueno=-0.234 (n=126)

- **FILTRO** `dist_vwap_pct` > `0.4319` → IC=-0.409 (n=20)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4319
  - _Potencial_: sin este filtro IC_bueno=-0.268 (n=231)

- **FILTRO** `sigma_ewma_delta_pct` > `10.458` → IC=-0.315 (n=25)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 10.458
  - _Potencial_: sin este filtro IC_bueno=-0.276 (n=226)

- **FILTRO** `volumen_pendiente_norm` > `0.0519` → IC=-0.362 (n=27)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0519
  - _Potencial_: sin este filtro IC_bueno=-0.264 (n=138)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `drift_60min` |x|> `0.1744` → IC=-0.260 (n=23)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1744
  - _Potencial_: sin este filtro IC_bueno=-0.207 (n=73)

- **FILTRO** `hora_utc` < `6.0` → IC=-0.271 (n=46)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=51)

- **FILTRO** `volumen_spike_ratio` > `2.3966` → IC=-0.237 (n=36)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.3966
  - _Potencial_: sin este filtro IC_bueno=-0.175 (n=38)

- **FILTRO** `sigma_h` < `0.0021` → IC=-0.259 (n=27)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0021
  - _Potencial_: sin este filtro IC_bueno=-0.241 (n=83)

- **FILTRO** `ibs_20min` > `0.3962` → IC=-0.273 (n=73)

  - _Acción_: SKIP cuando `ibs_20min` > 0.3962
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=37)

- **FILTRO** `volumen_regimen` > `0.807` → IC=-0.328 (n=27)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.807
  - _Potencial_: sin este filtro IC_bueno=-0.218 (n=83)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.6568` → IC=-0.441 (n=32)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6568
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=67)

- **FILTRO** `hora_utc` < `6.0` → IC=-0.375 (n=22)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=74)

- **FILTRO** `ibs_20min` > `0.538` → IC=-0.378 (n=47)

  - _Acción_: SKIP cuando `ibs_20min` > 0.538
  - _Potencial_: sin este filtro IC_bueno=-0.186 (n=49)

- **FILTRO** `volumen_spike_ratio` < `1.442` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.442
  - _Potencial_: sin este filtro IC_bueno=-0.260 (n=48)

- **PATRÓN** `ibs_20min` > `0.9464` → IC=+0.167 (n=34)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.9464 (IC base=-0.173)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `sigma_h` < `0.0064` → IC=-0.333 (n=34)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0064
  - _Potencial_: sin este filtro IC_bueno=-0.185 (n=71)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.395 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=88)

- **FILTRO** `hora_utc` > `11.0` → IC=-0.441 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=30)

- **FILTRO** `volumen_regimen` < `0.9792` → IC=-0.458 (n=22)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9792
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=23)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` > `0.1628` → IC=-0.122 (n=273)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1628
  - _Potencial_: sin este filtro IC_bueno=+0.154 (n=530)

- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.190 (n=169)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.0071 (IC base=+0.109)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.168 (n=194)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 17.0 (IC base=+0.109)

- **PATRÓN** `ibs_20min` > `0.6842` → IC=+0.147 (n=508)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` > 0.6842 (IC base=+0.109)

- **PATRÓN** `dist_vwap_pct` > `0.737` → IC=+0.211 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.737 (IC base=+0.109)

- **PATRÓN** `volumen_regimen` < `0.6288` → IC=+0.163 (n=170)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.6288 (IC base=+0.109)

- **PATRÓN** `volumen_pendiente_norm` < `0.2267` → IC=+0.139 (n=452)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_pendiente_norm` < 0.2267 (IC base=+0.109)

- **PATRÓN** `volumen_spike_ratio` < `1.7943` → IC=+0.150 (n=272)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.7943 (IC base=+0.109)

- **PATRÓN** `ibs_20min` < `0.1628` → IC=+0.154 (n=530)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.1628 (IC base=+0.060)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.104` → IC=+0.181 (n=180)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 9.104 (IC base=+0.060)

- **PATRÓN** `libro_liquidez` > `3239.2397` → IC=+0.139 (n=402)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 3239.2397 (IC base=+0.060)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.6781` → IC=-0.222 (n=52)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6781
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=157)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.208 (n=94)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.158 (n=191)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 12.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.148 (n=106)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 6.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` < `0.1761` → IC=+0.199 (n=280)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.1761 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.158` → IC=+0.164 (n=120)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 7.158 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` > `1.0363` → IC=+0.182 (n=127)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 1.0363 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` < `0.0701` → IC=+0.154 (n=218)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` < 0.0701 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.2726` → IC=+0.173 (n=47)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.2726 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `2.5202` → IC=+0.173 (n=249)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 2.5202 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `1.5564` → IC=+0.143 (n=222)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.5564 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `5957.7943` → IC=+0.151 (n=127)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 5957.7943 (IC base=+0.137)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `volumen_pendiente_norm` > `0.1263` → IC=-0.149 (n=35)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1263
  - _Potencial_: sin este filtro IC_bueno=+0.135 (n=165)

- **FILTRO** `ibs_20min` > `0.1906` → IC=-0.134 (n=99)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1906
  - _Potencial_: sin este filtro IC_bueno=+0.114 (n=195)

- **PATRÓN** `sigma_h` < `0.005` → IC=+0.123 (n=157)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.005 (IC base=+0.090)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.182 (n=64)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 18.0 (IC base=+0.090)

- **PATRÓN** `ibs_20min` > `0.8022` → IC=+0.134 (n=159)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` > 0.8022 (IC base=+0.090)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.217` → IC=+0.122 (n=183)

  - _Acción_: Kelly boost +0.61€ cuando `sigma_ewma_delta_pct` < 9.217 (IC base=+0.090)

- **PATRÓN** `volumen_regimen` < `1.0006` → IC=+0.123 (n=157)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` < 1.0006 (IC base=+0.090)

- **PATRÓN** `volumen_pendiente_norm` < `0.1263` → IC=+0.135 (n=165)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` < 0.1263 (IC base=+0.090)

- **PATRÓN** `volumen_spike_ratio` < `1.7926` → IC=+0.160 (n=101)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 1.7926 (IC base=+0.090)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.059` → IC=+0.232 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.059 (IC base=+0.030)

- **PATRÓN** `volumen_pendiente_norm` > `0.275` → IC=+0.136 (n=31)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` > 0.275 (IC base=+0.030)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.4118` → IC=-0.271 (n=33)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4118
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=103)

- **FILTRO** `dist_vwap_pct` > `0.1687` → IC=-0.175 (n=38)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1687
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=98)

- **PATRÓN** `hora_utc` > `13.0` → IC=+0.303 (n=115)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 13.0 (IC base=+0.246)

- **PATRÓN** `ibs_20min` > `0.6667` → IC=+0.266 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6667 (IC base=+0.246)

- **PATRÓN** `dist_vwap_pct` > `0.6475` → IC=+0.384 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6475 (IC base=+0.246)

- **PATRÓN** `dist_vwap_pct` < `0.2189` → IC=+0.246 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2189 (IC base=+0.246)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.318` → IC=+0.317 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.318 (IC base=+0.246)

- **PATRÓN** `volumen_regimen` < `0.5821` → IC=+0.317 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.5821 (IC base=+0.246)

- **PATRÓN** `volumen_pendiente_norm` > `0.1057` → IC=+0.325 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1057 (IC base=+0.246)

- **PATRÓN** `volumen_spike_ratio` < `1.4907` → IC=+0.391 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4907 (IC base=+0.246)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.245 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.246)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.418` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.418 (IC base=-0.087)

### LATE_WINDOW_5MIN
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.326 (n=67)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3349` → IC=+0.317 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3349 (IC base=+0.310)

- **PATRÓN** `elapsed_s` > `184.3` → IC=+0.383 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 184.3 (IC base=+0.310)

- **PATRÓN** `drift_15min` |x|≤ `1.0295` → IC=+0.455 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0295 (IC base=+0.310)

- **PATRÓN** `drift_60min` |x|≤ `0.969` → IC=+0.367 (n=58)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.969 (IC base=+0.310)

- **PATRÓN** `ballena_activa_n` < `1114.0` → IC=+0.364 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1114.0 (IC base=+0.310)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3488` → IC=+0.263 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3488 (IC base=+0.233)

- **PATRÓN** `elapsed_s` > `185.9` → IC=+0.246 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 185.9 (IC base=+0.233)

- **PATRÓN** `elapsed_s` < `202.5` → IC=+0.278 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 202.5 (IC base=+0.233)

- **PATRÓN** `drift_15min` |x|≤ `1.4315` → IC=+0.333 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.4315 (IC base=+0.233)

- **PATRÓN** `drift_60min` |x|≤ `0.9999` → IC=+0.273 (n=64)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9999 (IC base=+0.233)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.326 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.233)

- **PATRÓN** `ballena_activa_n` < `1862.0` → IC=+0.288 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1862.0 (IC base=+0.233)

### LATE_WINDOW_5MIN#BTC#5min
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.326 (n=67)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3349` → IC=+0.317 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3349 (IC base=+0.310)

- **PATRÓN** `elapsed_s` > `184.3` → IC=+0.383 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 184.3 (IC base=+0.310)

- **PATRÓN** `drift_15min` |x|≤ `1.0295` → IC=+0.455 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0295 (IC base=+0.310)

- **PATRÓN** `drift_60min` |x|≤ `0.969` → IC=+0.367 (n=58)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.969 (IC base=+0.310)

- **PATRÓN** `ballena_activa_n` < `1114.0` → IC=+0.364 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1114.0 (IC base=+0.310)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3488` → IC=+0.263 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3488 (IC base=+0.233)

- **PATRÓN** `elapsed_s` > `185.9` → IC=+0.246 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 185.9 (IC base=+0.233)

- **PATRÓN** `elapsed_s` < `202.5` → IC=+0.278 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 202.5 (IC base=+0.233)

- **PATRÓN** `drift_15min` |x|≤ `1.4315` → IC=+0.333 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.4315 (IC base=+0.233)

- **PATRÓN** `drift_60min` |x|≤ `0.9999` → IC=+0.273 (n=64)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9999 (IC base=+0.233)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.326 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.233)

- **PATRÓN** `ballena_activa_n` < `1862.0` → IC=+0.288 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1862.0 (IC base=+0.233)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `libro_liquidez` > `2852.6244` → IC=+0.133 (n=557)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 2852.6244 (IC base=+0.099)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `libro_liquidez` > `2852.6244` → IC=+0.133 (n=557)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 2852.6244 (IC base=+0.099)

### LIQUIDACIONES_15M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=185)

- **FILTRO** `libro_liquidez` < `2764.5849` → IC=-0.192 (n=50)

  - _Acción_: SKIP cuando `libro_liquidez` < 2764.5849
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=151)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=279)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `libro_liquidez` < `10724.0239` → IC=-0.196 (n=21)

  - _Acción_: SKIP cuando `libro_liquidez` < 10724.0239
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=66)

- **FILTRO** `liq_n` < `5.0` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `liq_n` < 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.147 (n=15)

- **FILTRO** `py_entrada` < `0.515` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=26)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `liq_usd_total` < `3561.53` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `liq_usd_total` < 3561.53
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=23)

- **FILTRO** `py_entrada` < `0.445` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=31)

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
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=3439)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.170 (n=101)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.170 (n=101)

- **FILTRO** `ballena_activa_n` > `118.0` → IC=-0.217 (n=58)

  - _Acción_: SKIP cuando `ballena_activa_n` > 118.0
  - _Potencial_: sin este filtro IC_bueno=-0.094 (n=30)

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
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=1260)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=1214)

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
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=412)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=393)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.136 (n=171)

  - _Acción_: Kelly boost +0.68€ cuando `py_entrada` < 0.495 (IC base=+0.019)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=834)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=834)

- **FILTRO** `py_entrada` < `0.44` → IC=-0.133 (n=257)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=657)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=782)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=782)

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
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=217)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=241)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=254)

- **FILTRO** `py_entrada` > `0.545` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `py_entrada` > 0.545
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=215)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=253)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=344)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=344)

- **FILTRO** `libro_liquidez` < `611.7268` → IC=-0.132 (n=123)

  - _Acción_: SKIP cuando `libro_liquidez` < 611.7268
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=251)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=251)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.129 (n=87)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=179)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.4` → IC=-0.121 (n=1280)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=3388)

### LIQUIDACIONES_DEPTH_FASE0#BNB#15min
- **FILTRO** `py_entrada` > `0.57` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=26)

- **FILTRO** `hora_utc` > `11.0` → IC=-0.227 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=23)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.144 (n=43)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=45)

- **FILTRO** `hora_utc` < `13.0` → IC=-0.265 (n=15)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 13.0
  - _Potencial_: sin este filtro IC_bueno=+0.111 (n=16)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.46` → IC=+0.159 (n=136)

  - _Acción_: Kelly boost +0.80€ cuando `py_entrada` < 0.46 (IC base=+0.010)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.204 (n=52)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=239)

- **FILTRO** `restante_min` < `10.43` → IC=-0.122 (n=96)

  - _Acción_: SKIP cuando `restante_min` < 10.43
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=195)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.155 (n=140)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=163)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.141 (n=37)

  - _Acción_: Kelly boost +0.71€ cuando `py_entrada` < 0.5 (IC base=+0.054)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.54` → IC=-0.125 (n=326)

  - _Acción_: SKIP cuando `py_entrada` < 0.54
  - _Potencial_: sin este filtro IC_bueno=+0.131 (n=109)

- **FILTRO** `profundidad_ratio` < `56.1` → IC=-0.148 (n=143)

  - _Acción_: SKIP cuando `profundidad_ratio` < 56.1
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=292)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.208 (n=70)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=316)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `profundidad_ratio` < `20.5` → IC=-0.150 (n=135)

  - _Acción_: SKIP cuando `profundidad_ratio` < 20.5
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=276)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.175 (n=78)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=341)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.129 (n=270)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=291)

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
- **FILTRO** `py_entrada` < `0.47` → IC=-0.163 (n=5766)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.063 (n=17992)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.172 (n=5886)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=18566)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.194 (n=1056)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=3250)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.172 (n=1016)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=3358)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.143 (n=1134)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` > 1.0 (IC base=+0.040)

- **PATRÓN** `libro_liquidez` > `1364.7185` → IC=+0.137 (n=2153)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 1364.7185 (IC base=+0.040)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.129 (n=2035)

  - _Acción_: Kelly boost +0.64€ cuando `py_entrada` < 0.5 (IC base=+0.013)

- **PATRÓN** `libro_liquidez` > `1513.7991` → IC=+0.153 (n=1488)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 1513.7991 (IC base=+0.013)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.156 (n=801)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=2695)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.175 (n=851)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=2625)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.173 (n=1059)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.106 (n=3269)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.199 (n=1036)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.075 (n=3419)

- **PATRÓN** `ibs_20min` > `0.9643` → IC=+0.129 (n=1474)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` > 0.9643 (IC base=+0.038)

- **PATRÓN** `libro_liquidez` > `1833.5848` → IC=+0.127 (n=1472)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 1833.5848 (IC base=+0.038)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.154 (n=1040)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.080 (n=3271)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=2344)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.162 (n=758)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=2282)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.208 (n=761)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=2762)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=3502)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` > `20.0` → IC=-0.146 (n=125)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 20.0
  - _Potencial_: sin este filtro IC_bueno=-0.094 (n=436)

- **FILTRO** `py_entrada` < `0.445` → IC=-0.264 (n=138)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=423)

- **FILTRO** `py_entrada` > `0.595` → IC=-0.234 (n=273)

  - _Acción_: SKIP cuando `py_entrada` > 0.595
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=862)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `py_entrada` < `0.395` → IC=-0.230 (n=72)

  - _Acción_: SKIP cuando `py_entrada` < 0.395
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=262)

- **FILTRO** `libro_liquidez` < `3613.7014` → IC=-0.152 (n=110)

  - _Acción_: SKIP cuando `libro_liquidez` < 3613.7014
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=224)

- **FILTRO** `py_entrada` > `0.615` → IC=-0.216 (n=86)

  - _Acción_: SKIP cuando `py_entrada` > 0.615
  - _Potencial_: sin este filtro IC_bueno=-0.101 (n=351)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=891)

- **FILTRO** `libro_liquidez` < `2083.4373` → IC=-0.168 (n=347)

  - _Acción_: SKIP cuando `libro_liquidez` < 2083.4373
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=705)

### MOMENTUM_IBS_15M_FADE#XRP#15min
- **FILTRO** `hora_utc` < `13.0` → IC=-0.238 (n=59)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 13.0
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=232)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.128 (n=16425)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=36536)

- **FILTRO** `py_entrada` < `0.33` → IC=-0.284 (n=12950)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=40011)

- **FILTRO** `ibs_7min` < `0.2415` → IC=-0.229 (n=13239)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2415
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=39722)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.152 (n=17769)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=35192)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.240 (n=16335)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=50519)

- **FILTRO** `ibs_7min` > `0.2857` → IC=-0.181 (n=16547)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2857
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=50307)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.146 (n=2649)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=6568)

- **FILTRO** `py_entrada` < `0.46` → IC=-0.235 (n=4561)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=4656)

- **FILTRO** `ibs_7min` < `0.7121` → IC=-0.245 (n=3040)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7121
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=6177)

- **FILTRO** `ballena_activa_n` > `6.0` → IC=-0.178 (n=2004)

  - _Acción_: SKIP cuando `ballena_activa_n` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=7213)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.270 (n=2870)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=8724)

- **FILTRO** `ibs_7min` > `0.7714` → IC=-0.212 (n=2897)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7714
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=8697)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.263 (n=2072)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=6886)

- **FILTRO** `ibs_7min` < `0.728` → IC=-0.198 (n=2239)

  - _Acción_: SKIP cuando `ibs_7min` < 0.728
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=6719)

- **FILTRO** `ballena_activa_n` > `153.0` → IC=-0.190 (n=2234)

  - _Acción_: SKIP cuando `ballena_activa_n` > 153.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=6724)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.263 (n=2240)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=6859)

- **FILTRO** `ibs_7min` > `0.2682` → IC=-0.198 (n=2273)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2682
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=6826)

- **FILTRO** `ballena_activa_n` > `150.0` → IC=-0.186 (n=2269)

  - _Acción_: SKIP cuando `ballena_activa_n` > 150.0
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=6830)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.157 (n=2162)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.084 (n=6603)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.315 (n=2150)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=6615)

- **FILTRO** `ibs_7min` < `0.3` → IC=-0.247 (n=2884)

  - _Acción_: SKIP cuando `ibs_7min` < 0.3
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=5881)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.194 (n=2109)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=6656)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.252 (n=2861)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=9468)

- **FILTRO** `ibs_7min` > `0.7341` → IC=-0.176 (n=3082)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7341
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=9247)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.261 (n=2011)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=6616)

- **FILTRO** `ibs_7min` < `0.7307` → IC=-0.188 (n=2156)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7307
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=6471)

- **FILTRO** `ballena_activa_n` > `27.0` → IC=-0.188 (n=2154)

  - _Acción_: SKIP cuando `ballena_activa_n` > 27.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=6473)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.270 (n=2009)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=6964)

- **FILTRO** `ibs_7min` > `0.2751` → IC=-0.182 (n=2243)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2751
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=6730)

- **FILTRO** `ballena_activa_n` > `26.0` → IC=-0.175 (n=2234)

  - _Acción_: SKIP cuando `ballena_activa_n` > 26.0
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=6739)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.283 (n=2068)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=6639)

- **FILTRO** `ibs_7min` < `0.2174` → IC=-0.232 (n=2174)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2174
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=6533)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.219 (n=2101)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=6606)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.187 (n=3064)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=9711)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.32` → IC=-0.290 (n=2028)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=6659)

- **FILTRO** `ibs_7min` < `0.2162` → IC=-0.221 (n=2170)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2162
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=6517)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.199 (n=1960)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=6727)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.213 (n=2934)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=9150)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1046` → IC=-0.135 (n=61)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1046
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=120)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `py_entrada` < `0.455` → IC=-0.158 (n=299)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=982)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=1266)

- **FILTRO** `py_entrada` > `0.545` → IC=-0.152 (n=156)

  - _Acción_: SKIP cuando `py_entrada` > 0.545
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=537)

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
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=833)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `py_entrada` < `0.475` → IC=-0.122 (n=162)

  - _Acción_: SKIP cuando `py_entrada` < 0.475
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=329)

- **FILTRO** `ballena_activa_n` > `3.0` → IC=-0.143 (n=166)

  - _Acción_: SKIP cuando `ballena_activa_n` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=324)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.231 (n=50)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=441)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.129 (n=68)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=630)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=387)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.3982` → IC=+0.144 (n=1126)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.72€ cuando `delta_ratio` |x|> 0.3982 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.139 (n=521)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 14.0 (IC base=+0.131)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.133 (n=428)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 4.0 (IC base=+0.131)

- **PATRÓN** `total_vol_5m` < `3732.187` → IC=+0.151 (n=751)

  - _Acción_: Kelly boost +0.75€ cuando `total_vol_5m` < 3732.187 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `3656.7944` → IC=+0.145 (n=511)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 3656.7944 (IC base=+0.131)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.148 (n=379)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 12.0 (IC base=+0.131)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.4367` → IC=+0.167 (n=88)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.83€ cuando `delta_ratio` |x|> 0.4367 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.219 (n=126)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `2585.3133` → IC=+0.222 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2585.3133 (IC base=+0.146)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `delta_ratio` |x|> `0.3992` → IC=+0.134 (n=230)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.67€ cuando `delta_ratio` |x|> 0.3992 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.127 (n=207)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 14.0 (IC base=+0.117)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.127 (n=274)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.04 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `2090.589` → IC=+0.125 (n=206)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 2090.589 (IC base=+0.117)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.416` → IC=+0.184 (n=150)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.92€ cuando `delta_ratio` |x|> 0.416 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.157 (n=231)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 4.0 (IC base=+0.138)

- **PATRÓN** `total_vol_5m` < `388.5476` → IC=+0.223 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 388.5476 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `7829.679` → IC=+0.145 (n=150)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 7829.679 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `71.0` → IC=+0.211 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 71.0 (IC base=+0.138)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.4324` → IC=+0.253 (n=91)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio` |x|> 0.4324 (IC base=+0.152)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.225 (n=67)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.152)

- **PATRÓN** `total_vol_5m` < `7882.091` → IC=+0.167 (n=199)

  - _Acción_: Kelly boost +0.83€ cuando `total_vol_5m` < 7882.091 (IC base=+0.152)

- **PATRÓN** `libro_liquidez` > `3267.081` → IC=+0.167 (n=178)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 3267.081 (IC base=+0.152)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `hora_utc` < `10.0` → IC=+0.132 (n=142)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 10.0 (IC base=+0.096)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.185 (n=128)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.01 (IC base=+0.096)

- **PATRÓN** `libro_liquidez` > `3589.6144` → IC=+0.163 (n=96)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 3589.6144 (IC base=+0.096)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `8.4547` → IC=-0.256 (n=43)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 8.4547
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=130)

- **FILTRO** `sigma_h` > `0.0051` → IC=-0.267 (n=315)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0051
  - _Potencial_: sin este filtro IC_bueno=+0.108 (n=317)

- **FILTRO** `T_h` > `129.6211` → IC=-0.203 (n=156)

  - _Acción_: SKIP cuando `T_h` > 129.6211
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=476)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.183 (n=159)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0034 (IC base=-0.079)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `T_h` > `87.9957` → IC=-0.276 (n=47)

  - _Acción_: SKIP cuando `T_h` > 87.9957
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=143)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.300 (n=48)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=-0.036)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `sigma_h` > `0.0055` → IC=-0.152 (n=44)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0055
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=16)

- **FILTRO** `pct_vs_K` |x|> `7.7861` → IC=-0.273 (n=20)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 7.7861
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=40)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0102` → IC=-0.237 (n=36)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0102
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=72)

- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.233 (n=28)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0054 (IC base=-0.082)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0101` → IC=-0.217 (n=444)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0101
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=148)

- **FILTRO** `T_h` > `70.6078` → IC=-0.194 (n=443)

  - _Acción_: SKIP cuando `T_h` > 70.6078
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=149)

- **FILTRO** `sigma_h` > `0.0083` → IC=-0.272 (n=169)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0083
  - _Potencial_: sin este filtro IC_bueno=-0.221 (n=331)

- **FILTRO** `T_h` > `54.3929` → IC=-0.279 (n=374)

  - _Acción_: SKIP cuando `T_h` > 54.3929
  - _Potencial_: sin este filtro IC_bueno=-0.117 (n=126)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `T_h` > `71.43` → IC=-0.182 (n=130)

  - _Acción_: SKIP cuando `T_h` > 71.43
  - _Potencial_: sin este filtro IC_bueno=-0.097 (n=65)

- **FILTRO** `pct_vs_K` |x|> `2.7902` → IC=-0.396 (n=46)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.7902
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=149)

- **FILTRO** `T_h` > `72.749` → IC=-0.279 (n=134)

  - _Acción_: SKIP cuando `T_h` > 72.749
  - _Potencial_: sin este filtro IC_bueno=-0.245 (n=45)

- **FILTRO** `pct_vs_K` |x|> `3.0008` → IC=-0.432 (n=42)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.0008
  - _Potencial_: sin este filtro IC_bueno=-0.219 (n=137)

### PRICE_TARGET_GBM_FADE#BTC#reach
- **FILTRO** `T_h` < `139.5329` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `T_h` < 139.5329
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

- **FILTRO** `sigma_h` < `0.0085` → IC=-0.239 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0085
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=7)

- **FILTRO** `T_h` > `144.5457` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `T_h` > 144.5457
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `sigma_h` < `0.0091` → IC=-0.316 (n=112)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0091
  - _Potencial_: sin este filtro IC_bueno=-0.117 (n=58)

- **FILTRO** `T_h` > `78.4593` → IC=-0.260 (n=127)

  - _Acción_: SKIP cuando `T_h` > 78.4593
  - _Potencial_: sin este filtro IC_bueno=-0.211 (n=43)

- **FILTRO** `pct_vs_K` |x|> `3.1129` → IC=-0.444 (n=52)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.1129
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=103)

### PRICE_TARGET_GBM_FADE#ETH#reach
- **FILTRO** `sigma_h` > `0.006` → IC=-0.167 (n=16)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.006
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

- **FILTRO** `T_h` < `145.7969` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `T_h` < 145.7969
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=6)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` < `0.0083` → IC=-0.245 (n=53)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0083
  - _Potencial_: sin este filtro IC_bueno=-0.095 (n=109)

- **FILTRO** `T_h` > `94.1391` → IC=-0.218 (n=108)

  - _Acción_: SKIP cuando `T_h` > 94.1391
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=54)

- **FILTRO** `sigma_h` > `0.0153` → IC=-0.362 (n=27)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0153
  - _Potencial_: sin este filtro IC_bueno=-0.206 (n=83)

- **FILTRO** `sigma_h` < `0.0085` → IC=-0.263 (n=36)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0085
  - _Potencial_: sin este filtro IC_bueno=-0.237 (n=74)

- **FILTRO** `T_h` > `46.6251` → IC=-0.313 (n=73)

  - _Acción_: SKIP cuando `T_h` > 46.6251
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=37)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1221` → IC=+0.464 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1221 (IC base=+0.333)

- **PATRÓN** `sigma_h` < `0.0135` → IC=+0.349 (n=91)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0135 (IC base=+0.333)

- **PATRÓN** `sigma_h` > `0.0073` → IC=+0.370 (n=90)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0073 (IC base=+0.333)

- **PATRÓN** `T_h` > `0.7719` → IC=+0.387 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.7719 (IC base=+0.333)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.477 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.333)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.347 (n=83)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.333)

- **PATRÓN** `edge` > `0.097` → IC=+0.444 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.097 (IC base=+0.416)

- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.432 (n=190)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0082 (IC base=+0.416)

- **PATRÓN** `T_h` < `0.5922` → IC=+0.431 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.5922 (IC base=+0.416)

- **PATRÓN** `T_h` > `1.4829` → IC=+0.431 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4829 (IC base=+0.416)

- **PATRÓN** `dist_50` > `0.3772` → IC=+0.458 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3772 (IC base=+0.416)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.478 (n=135)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.416)

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
- **PATRÓN** `edge` > `0.1885` → IC=+0.482 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1885 (IC base=+0.435)

- **PATRÓN** `sigma_h` < `0.016` → IC=+0.465 (n=55)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.016 (IC base=+0.435)

- **PATRÓN** `T_h` > `0.4307` → IC=+0.447 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.4307 (IC base=+0.435)

- **PATRÓN** `dist_50` > `0.3326` → IC=+0.465 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3326 (IC base=+0.435)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.435 (n=29)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.435)

- **PATRÓN** `edge` > `0.177` → IC=+0.478 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.177 (IC base=+0.464)

- **PATRÓN** `sigma_h` < `0.0156` → IC=+0.478 (n=136)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0156 (IC base=+0.464)

- **PATRÓN** `T_h` > `1.1543` → IC=+0.478 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.1543 (IC base=+0.464)

- **PATRÓN** `dist_50` > `0.4373` → IC=+0.485 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4373 (IC base=+0.464)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.472 (n=141)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.464)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=300)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=379)

- **FILTRO** `streak_estiramiento` > `0.8382` → IC=-0.174 (n=84)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.8382
  - _Potencial_: sin este filtro IC_bueno=+0.121 (n=254)

- **PATRÓN** `streak_estiramiento` < `0.8382` → IC=+0.121 (n=254)

  - _Acción_: Kelly boost +0.61€ cuando `streak_estiramiento` < 0.8382 (IC base=+0.045)

- **PATRÓN** `libro_liquidez` > `2756.3002` → IC=+0.150 (n=101)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2756.3002 (IC base=+0.045)

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

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.122 (n=133)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 5.0 (IC base=+0.088)

- **PATRÓN** `streak_estiramiento` < `0.4503` → IC=+0.184 (n=96)

  - _Acción_: Kelly boost +0.92€ cuando `streak_estiramiento` < 0.4503 (IC base=+0.088)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.148 (n=106)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 35.0 (IC base=+0.088)

- **PATRÓN** `libro_liquidez` > `2229.7597` → IC=+0.141 (n=126)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 2229.7597 (IC base=+0.088)

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
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=45)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=30)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=820)

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

### STREAK_FADE_60M#ETH#60min
- **FILTRO** `hora_utc` > `5.0` → IC=-0.147 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=10)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=10)

### STREAK_FADE_60M#SOL#60min
- **PATRÓN** `regimen_ma_toques` > `4.0` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `regimen_ma_toques` > 4.0 (IC base=+0.024)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=970)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=1330)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=1119)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=1156)

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
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=3931)

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
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=2153)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.198 (n=1523)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0053 (IC base=+0.180)

- **PATRÓN** `sigma_h` > `0.0119` → IC=+0.196 (n=1154)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` > 0.0119 (IC base=+0.180)

- **PATRÓN** `drift_60min` |x|≤ `0.1735` → IC=+0.194 (n=3048)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.1735 (IC base=+0.180)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1333` → IC=+0.192 (n=1376)

  - _Acción_: Kelly boost +0.96€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1333 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.188 (n=3206)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 6.0 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.183 (n=3185)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 15.0 (IC base=+0.180)

- **PATRÓN** `ibs_15` > `0.5632` → IC=+0.257 (n=3461)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5632 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` > `0.1251` → IC=+0.172 (n=1652)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.1251 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` < `0.6708` → IC=+0.167 (n=3275)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` < 0.6708 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.56` → IC=+0.253 (n=904)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.56 (IC base=+0.180)

- **PATRÓN** `libro_liquidez` > `4866.2545` → IC=+0.200 (n=1154)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4866.2545 (IC base=+0.180)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=1366)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.232 (n=595)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.220)

- **PATRÓN** `drift_60min` |x|≤ `0.0585` → IC=+0.267 (n=200)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0585 (IC base=+0.220)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2517` → IC=+0.245 (n=198)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2517 (IC base=+0.220)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.242 (n=594)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.220)

- **PATRÓN** `ibs_15` > `0.7199` → IC=+0.285 (n=594)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7199 (IC base=+0.220)

- **PATRÓN** `dist_vwap_pct` > `0.1352` → IC=+0.242 (n=347)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1352 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.108` → IC=+0.303 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.108 (IC base=+0.220)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.222 (n=771)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.220)

- **PATRÓN** `libro_liquidez` > `16217.9862` → IC=+0.250 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16217.9862 (IC base=+0.220)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.197 (n=229)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0034 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.0491` → IC=+0.155 (n=230)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.0491 (IC base=+0.145)

- **PATRÓN** `drift_15min` |x|≤ `0.3963` → IC=+0.149 (n=229)

  - _Acción_: Kelly boost +0.75€ cuando `drift_15min` |x|≤ 0.3963 (IC base=+0.145)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1438` → IC=+0.151 (n=457)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.76€ cuando `delta_ratio_macro` |x|> 0.1438 (IC base=+0.145)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1354` → IC=+0.164 (n=269)

  - _Acción_: Kelly boost +0.82€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1354 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.155 (n=624)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 6.0 (IC base=+0.145)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.150 (n=715)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 17.0 (IC base=+0.145)

- **PATRÓN** `ibs_15` > `0.5467` → IC=+0.244 (n=685)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5467 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` > `0.1154` → IC=+0.155 (n=430)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.1154 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` < `0.6071` → IC=+0.146 (n=783)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.6071 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.851` → IC=+0.279 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.851 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `3209.7303` → IC=+0.152 (n=685)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 3209.7303 (IC base=+0.145)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `sigma_ewma_delta_pct` > `18.005` → IC=-0.184 (n=36)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 18.005
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=312)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.139 (n=247)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` < 0.0061 (IC base=+0.099)

- **PATRÓN** `drift_60min` |x|≤ `0.3048` → IC=+0.121 (n=739)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.60€ cuando `drift_60min` |x|≤ 0.3048 (IC base=+0.099)

- **PATRÓN** `ibs_15` > `0.9` → IC=+0.247 (n=247)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9 (IC base=+0.099)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.137 (n=408)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.099)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `8.407` → IC=+0.149 (n=72)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 8.407 (IC base=+0.013)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0238` → IC=+0.247 (n=267)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0238 (IC base=+0.202)

- **PATRÓN** `drift_60min` |x|≤ `0.0851` → IC=+0.237 (n=352)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0851 (IC base=+0.202)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3374` → IC=+0.233 (n=703)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3374 (IC base=+0.202)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.217 (n=709)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.202)

- **PATRÓN** `ibs_15` > `0.5429` → IC=+0.282 (n=800)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5429 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` > `0.1887` → IC=+0.211 (n=406)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1887 (IC base=+0.202)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.825` → IC=+0.225 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.825 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `2969.9944` → IC=+0.299 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2969.9944 (IC base=+0.202)

- **PATRÓN** `ibs_15` < `0.1111` → IC=+0.157 (n=768)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.79€ cuando `ibs_15` < 0.1111 (IC base=+0.066)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.369 (n=410)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.365)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.379 (n=279)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.365)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1505` → IC=+0.384 (n=410)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1505 (IC base=+0.365)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2299` → IC=+0.384 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2299 (IC base=+0.365)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.378 (n=614)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.365)

- **PATRÓN** `ibs_15` > `0.788` → IC=+0.401 (n=614)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.788 (IC base=+0.365)

- **PATRÓN** `dist_vwap_pct` > `0.1433` → IC=+0.381 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1433 (IC base=+0.365)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.679` → IC=+0.387 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.679 (IC base=+0.365)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.369 (n=748)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.365)

- **PATRÓN** `libro_liquidez` > `3837.2318` → IC=+0.375 (n=549)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3837.2318 (IC base=+0.365)

- **PATRÓN** `ballena_activa_n` < `423.0` → IC=+0.380 (n=541)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 423.0 (IC base=+0.365)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.366 (n=282)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.364)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.391 (n=108)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.364)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2146` → IC=+0.384 (n=145)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2146 (IC base=+0.364)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1413` → IC=+0.397 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1413 (IC base=+0.364)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.384 (n=299)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.364)

- **PATRÓN** `ibs_15` > `0.8057` → IC=+0.391 (n=320)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8057 (IC base=+0.364)

- **PATRÓN** `dist_vwap_pct` > `0.2448` → IC=+0.396 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2448 (IC base=+0.364)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.859` → IC=+0.385 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.859 (IC base=+0.364)

- **PATRÓN** `libro_liquidez` > `15286.8558` → IC=+0.391 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15286.8558 (IC base=+0.364)

- **PATRÓN** `ballena_activa_n` < `497.0` → IC=+0.409 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 497.0 (IC base=+0.364)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.364 (n=130)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.363)

- **PATRÓN** `sigma_h` > `0.0057` → IC=+0.382 (n=134)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0057 (IC base=+0.363)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0904` → IC=+0.376 (n=263)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0904 (IC base=+0.363)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2995` → IC=+0.381 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2995 (IC base=+0.363)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.388 (n=141)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.363)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.370 (n=137)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.363)

- **PATRÓN** `ibs_15` > `0.7504` → IC=+0.412 (n=294)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7504 (IC base=+0.363)

- **PATRÓN** `dist_vwap_pct` > `0.4534` → IC=+0.381 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4534 (IC base=+0.363)

- **PATRÓN** `dist_vwap_pct` < `0.2797` → IC=+0.365 (n=273)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2797 (IC base=+0.363)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.973` → IC=+0.386 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.973 (IC base=+0.363)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.367 (n=330)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.363)

- **PATRÓN** `libro_liquidez` > `3939.9229` → IC=+0.390 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3939.9229 (IC base=+0.363)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0123` → IC=-0.225 (n=1058)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0123
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=3178)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.210 (n=1652)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=2584)

- **FILTRO** `libro_liquidez` < `4171.7267` → IC=-0.152 (n=2795)

  - _Acción_: SKIP cuando `libro_liquidez` < 4171.7267
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=1441)

- **PATRÓN** `ibs_15` > `0.6341` → IC=+0.285 (n=1025)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6341 (IC base=-0.067)

- **PATRÓN** `dist_vwap_pct` > `0.1092` → IC=+0.209 (n=589)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1092 (IC base=-0.067)

- **PATRÓN** `dist_vwap_pct` < `0.424` → IC=+0.202 (n=999)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.424 (IC base=-0.067)

- **PATRÓN** `delta_ratio_macro` |x|> `0.23` → IC=+0.269 (n=1165)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.23 (IC base=-0.013)

- **PATRÓN** `ibs_15` < `0.359` → IC=+0.282 (n=3492)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.359 (IC base=-0.013)

- **PATRÓN** `dist_vwap_pct` > `0.6607` → IC=+0.280 (n=453)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6607 (IC base=-0.013)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0341` → IC=-0.220 (n=1828)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0341
  - _Potencial_: sin este filtro IC_bueno=-0.117 (n=615)

- **FILTRO** `sigma_h` < `0.0034` → IC=-0.230 (n=609)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=1834)

- **FILTRO** `sigma_ewma_delta_pct` > `23.379` → IC=-0.268 (n=351)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 23.379
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=2092)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.212 (n=64)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.194 (n=2379)

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.123 (n=733)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0052 (IC base=+0.098)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2033` → IC=+0.296 (n=150)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2033 (IC base=+0.098)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.137 (n=356)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 15.0 (IC base=+0.098)

- **PATRÓN** `ibs_15` > `0.7572` → IC=+0.337 (n=330)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7572 (IC base=+0.098)

- **PATRÓN** `dist_vwap_pct` > `0.1039` → IC=+0.295 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1039 (IC base=+0.098)

- **PATRÓN** `dist_vwap_pct` < `0.3639` → IC=+0.290 (n=336)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3639 (IC base=+0.098)

- **PATRÓN** `sigma_ewma_delta_pct` > `24.371` → IC=+0.145 (n=170)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 24.371 (IC base=+0.098)

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
  - _Potencial_: sin este filtro IC_bueno=+0.162 (n=666)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.165 (n=452)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0058 (IC base=+0.154)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.163 (n=342)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` > 0.0048 (IC base=+0.154)

- **PATRÓN** `drift_60min` |x|≤ `0.0709` → IC=+0.193 (n=226)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.0709 (IC base=+0.154)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3006` → IC=+0.192 (n=391)

  - _Acción_: Kelly boost +0.96€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3006 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.166 (n=513)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.154)

- **PATRÓN** `ibs_15` > `0.6187` → IC=+0.255 (n=513)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6187 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` > `0.4589` → IC=+0.164 (n=135)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.4589 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` < `0.2815` → IC=+0.154 (n=481)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.2815 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.508` → IC=+0.260 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.508 (IC base=+0.154)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.162 (n=666)

  - _Acción_: Kelly boost +0.81€ cuando `libro_spread` < 0.01 (IC base=+0.154)

- **PATRÓN** `libro_liquidez` > `10015.5876` → IC=+0.165 (n=171)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 10015.5876 (IC base=+0.154)

- **PATRÓN** `sigma_h` < `0.0077` → IC=+0.250 (n=1240)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0077 (IC base=+0.244)

- **PATRÓN** `drift_60min` |x|≤ `0.3575` → IC=+0.244 (n=1091)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3575 (IC base=+0.244)

- **PATRÓN** `drift_15min` |x|≤ `0.7686` → IC=+0.258 (n=1091)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7686 (IC base=+0.244)

- **PATRÓN** `delta_ratio_macro` |x|> `0.158` → IC=+0.258 (n=827)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.158 (IC base=+0.244)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.252 (n=453)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.244)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.247 (n=480)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.244)

- **PATRÓN** `ibs_15` < `0.3684` → IC=+0.274 (n=1240)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3684 (IC base=+0.244)

- **PATRÓN** `dist_vwap_pct` > `0.5987` → IC=+0.268 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5987 (IC base=+0.244)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.449` → IC=+0.254 (n=551)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.449 (IC base=+0.244)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.476` → IC=+0.249 (n=1296)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.476 (IC base=+0.244)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `drift_60min` |x|> `0.1726` → IC=-0.257 (n=331)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1726
  - _Potencial_: sin este filtro IC_bueno=-0.154 (n=643)

- **FILTRO** `drift_15min` |x|> `0.89` → IC=-0.280 (n=243)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.89
  - _Potencial_: sin este filtro IC_bueno=-0.159 (n=731)

- **FILTRO** `sigma_ewma_delta_pct` > `6.602` → IC=-0.199 (n=227)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.602
  - _Potencial_: sin este filtro IC_bueno=-0.186 (n=747)

- **FILTRO** `sigma_ewma_delta_pct` > `17.996` → IC=-0.146 (n=509)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 17.996
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=4050)

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

- **PATRÓN** `delta_ratio_macro` |x|> `0.0642` → IC=+0.238 (n=548)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0642 (IC base=-0.040)

- **PATRÓN** `ibs_15` < `0.3529` → IC=+0.289 (n=548)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3529 (IC base=-0.040)

- **PATRÓN** `dist_vwap_pct` < `0.4499` → IC=+0.243 (n=574)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4499 (IC base=-0.040)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0197` → IC=-0.250 (n=585)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0197
  - _Potencial_: sin este filtro IC_bueno=-0.162 (n=586)

- **FILTRO** `sigma_ewma_delta_pct` > `7.379` → IC=-0.208 (n=364)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 7.379
  - _Potencial_: sin este filtro IC_bueno=-0.205 (n=807)

- **FILTRO** `libro_spread` > `0.04` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.04
  - _Potencial_: sin este filtro IC_bueno=-0.204 (n=1152)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.206)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.206)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0678` → IC=+0.273 (n=754)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0678 (IC base=-0.025)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1154` → IC=+0.296 (n=366)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1154 (IC base=-0.025)

- **PATRÓN** `ibs_15` < `0.3333` → IC=+0.293 (n=845)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3333 (IC base=-0.025)

- **PATRÓN** `dist_vwap_pct` > `0.7764` → IC=+0.350 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7764 (IC base=-0.025)

### UPDOWN_GBM_ETH_15M_HORA7
- **PATRÓN** `ibs_15` > `0.8434` → IC=+0.324 (n=15)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8434 (IC base=+0.068)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **PATRÓN** `ibs_15` > `0.8434` → IC=+0.324 (n=15)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8434 (IC base=+0.068)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.298 (n=919)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.291)

- **PATRÓN** `drift_60min` |x|≤ `0.053` → IC=+0.321 (n=349)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.053 (IC base=+0.291)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2402` → IC=+0.303 (n=348)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2402 (IC base=+0.291)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2248` → IC=+0.308 (n=619)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2248 (IC base=+0.291)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.308 (n=1088)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.291)

- **PATRÓN** `ibs_15` > `0.8389` → IC=+0.321 (n=1044)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8389 (IC base=+0.291)

- **PATRÓN** `dist_vwap_pct` > `0.2631` → IC=+0.323 (n=449)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2631 (IC base=+0.291)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.638` → IC=+0.376 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.638 (IC base=+0.291)

- **PATRÓN** `libro_liquidez` > `14141.7548` → IC=+0.314 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14141.7548 (IC base=+0.291)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.315 (n=247)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.289)

- **PATRÓN** `drift_60min` |x|≤ `0.0571` → IC=+0.316 (n=188)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0571 (IC base=+0.289)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2575` → IC=+0.309 (n=187)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2575 (IC base=+0.289)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.308 (n=561)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.289)

- **PATRÓN** `ibs_15` > `0.8279` → IC=+0.317 (n=561)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8279 (IC base=+0.289)

- **PATRÓN** `dist_vwap_pct` > `0.2516` → IC=+0.324 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2516 (IC base=+0.289)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.701` → IC=+0.382 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.701 (IC base=+0.289)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.289 (n=727)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.289)

- **PATRÓN** `libro_liquidez` > `16217.9862` → IC=+0.331 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16217.9862 (IC base=+0.289)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.304 (n=484)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.293)

- **PATRÓN** `drift_60min` |x|≤ `0.0515` → IC=+0.317 (n=162)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0515 (IC base=+0.293)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1466` → IC=+0.296 (n=322)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1466 (IC base=+0.293)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1057` → IC=+0.332 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1057 (IC base=+0.293)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.314 (n=466)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.293)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.294 (n=436)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.293)

- **PATRÓN** `ibs_15` > `0.8527` → IC=+0.323 (n=483)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8527 (IC base=+0.293)

- **PATRÓN** `dist_vwap_pct` > `0.4679` → IC=+0.331 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4679 (IC base=+0.293)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.638` → IC=+0.361 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.638 (IC base=+0.293)

### UPDOWN_OU_5M
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1226` → IC=-0.151 (n=84)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1226
  - _Potencial_: sin este filtro IC_bueno=-0.098 (n=252)

- **FILTRO** `ballena_activa_n` > `47.0` → IC=-0.136 (n=226)

  - _Acción_: SKIP cuando `ballena_activa_n` > 47.0
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=78)

- **FILTRO** `sigma_h` < `0.0051` → IC=-0.169 (n=119)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0051
  - _Potencial_: sin este filtro IC_bueno=-0.089 (n=358)

- **FILTRO** `ballena_activa_n` > `23.0` → IC=-0.206 (n=107)

  - _Acción_: SKIP cuando `ballena_activa_n` > 23.0
  - _Potencial_: sin este filtro IC_bueno=-0.113 (n=109)

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

- **FILTRO** `drift_60min` |x|> `0.2244` → IC=-0.222 (n=16)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2244
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=34)

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
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.0775` → IC=-0.260 (n=23)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.0775
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=12)

- **FILTRO** `sigma_h` < `0.0063` → IC=-0.222 (n=34)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0063
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=19)

- **FILTRO** `ballena_activa_n` > `18.0` → IC=-0.196 (n=21)

  - _Acción_: SKIP cuando `ballena_activa_n` > 18.0
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### WEEKLY_PRICE
- **PATRÓN** `T_h` > `85.7585` → IC=+0.195 (n=463)

  - _Acción_: Kelly boost +0.97€ cuando `T_h` > 85.7585 (IC base=+0.190)

- **PATRÓN** `ratio` < `0.973` → IC=+0.423 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.973 (IC base=+0.190)

- **PATRÓN** `T_h` > `111.9997` → IC=+0.354 (n=2106)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9997 (IC base=+0.338)

- **PATRÓN** `ratio` > `1.0236` → IC=+0.374 (n=332)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0236 (IC base=+0.338)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `105.6124` → IC=+0.179 (n=191)

  - _Acción_: Kelly boost +0.89€ cuando `T_h` > 105.6124 (IC base=+0.161)

- **PATRÓN** `ratio` < `0.9701` → IC=+0.384 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9701 (IC base=+0.161)

- **PATRÓN** `T_h` > `110.3225` → IC=+0.308 (n=722)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 110.3225 (IC base=+0.296)

- **PATRÓN** `ratio` > `1.0464` → IC=+0.399 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0464 (IC base=+0.296)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `83.3501` → IC=+0.236 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 83.3501 (IC base=+0.229)

- **PATRÓN** `ratio` < `0.9849` → IC=+0.432 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9849 (IC base=+0.229)

- **PATRÓN** `T_h` > `111.9838` → IC=+0.353 (n=759)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9838 (IC base=+0.325)

- **PATRÓN** `ratio` > `1.0372` → IC=+0.402 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0372 (IC base=+0.325)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.1003` → IC=+0.445 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1003 (IC base=+0.399)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5632 sube el IC de +0.180 a +0.257 en UPDOWN_GBM#15min (n=3461). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7199 sube el IC de +0.220 a +0.285 en UPDOWN_GBM#BTC#15min (n=594). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.5467 sube el IC de +0.145 a +0.244 en UPDOWN_GBM#ETH#15min (n=685). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.9 sube el IC de +0.099 a +0.247 en UPDOWN_GBM#SOL#15min (n=247). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5429 sube el IC de +0.202 a +0.282 en UPDOWN_GBM#XRP#15min (n=800). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1111 sube el IC de +0.066 a +0.157 en UPDOWN_GBM#XRP#15min (n=768). Ya aplicado como kelly_boost=+0.79€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6341 sube el IC de -0.067 a +0.285 en UPDOWN_GBM_15M_TARDIO (n=1025). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.359 sube el IC de -0.013 a +0.282 en UPDOWN_GBM_15M_TARDIO (n=3492). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7572 sube el IC de +0.098 a +0.337 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=330). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.6255 sube el IC de -0.195 a +0.300 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=58). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6187 sube el IC de +0.154 a +0.255 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=513). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3684 sube el IC de +0.244 a +0.274 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=1240). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de -0.190 a +0.234 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=62). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3529 sube el IC de -0.040 a +0.289 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=548). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.206 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3333 sube el IC de -0.025 a +0.293 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=845). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_YES, IBS > 0.8434 sube el IC de +0.068 a +0.324 en UPDOWN_GBM_ETH_15M_HORA7 (n=15). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_YES, IBS > 0.8434 sube el IC de +0.068 a +0.324 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=15). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8389 sube el IC de +0.291 a +0.321 en UPDOWN_GBM_IBS_ALTO (n=1044). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8279 sube el IC de +0.289 a +0.317 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=561). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8527 sube el IC de +0.293 a +0.323 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=483). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.788 sube el IC de +0.365 a +0.401 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=614). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8057 sube el IC de +0.364 a +0.391 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=320). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7504 sube el IC de +0.363 a +0.412 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=294). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1874 | +0.091 | +205.88€ | 0 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1874 | +0.091 | +205.88€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1490 | +0.096 | +181.43€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1490 | +0.096 | +181.43€ | 0 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 280 | +0.067 | +10.78€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 280 | +0.067 | +10.78€ | 5 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 73 | +0.100 | +14.01€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 73 | +0.100 | +14.01€ | 0 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 566 | -0.016 | +60.51€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 566 | -0.016 | +60.51€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 411 | -0.040 | +32.29€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 411 | -0.040 | +32.29€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 124 | +0.056 | +20.72€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 124 | +0.056 | +20.72€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 28 | +0.000 | +4.14€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 28 | +0.000 | +4.14€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 39356 | -0.083 | -4947.26€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 2154 | +0.030 | -247.23€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 37202 | -0.089 | -4700.04€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4451 | -0.116 | -769.56€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4451 | -0.116 | -769.56€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 2154 | +0.030 | -247.23€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 2154 | +0.030 | -247.23€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 4297 | -0.105 | -876.21€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 4297 | -0.105 | -876.21€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 10457 | -0.021 | -934.13€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 10457 | -0.021 | -934.13€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 10358 | -0.105 | -812.16€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 10358 | -0.105 | -812.16€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 7639 | -0.137 | -1307.98€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 7639 | -0.137 | -1307.98€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 33790 | -0.016 | +3470.20€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 8741 | +0.004 | +1693.85€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 25049 | -0.023 | +1776.35€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 33790 | -0.016 | +3470.20€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 8741 | +0.004 | +1693.85€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 25049 | -0.023 | +1776.35€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 141252 | +0.115 | -5731.97€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 18304 | +0.183 | -540.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 619 | -0.020 | -67.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 113832 | +0.106 | -4818.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 8497 | +0.101 | -305.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 18880 | +0.108 | -1149.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 61 | -0.151 | +10.95€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 18804 | +0.109 | -1149.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 27423 | +0.129 | -373.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5150 | +0.190 | -162.85€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 18864 | +0.120 | -95.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 3367 | +0.084 | -92.16€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 18933 | +0.098 | -1351.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 72 | -0.122 | -6.14€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 18846 | +0.099 | -1334.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 30036 | +0.124 | -555.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 7801 | +0.178 | -134.29€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 19112 | +0.107 | -355.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 3111 | +0.099 | -57.07€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#SOL | 27079 | +0.115 | -1359.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 5154 | +0.196 | -251.96€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 522 | +0.013 | -13.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 19384 | +0.095 | -937.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 2019 | +0.133 | -156.75€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#XRP | 18901 | +0.104 | -942.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 66 | -0.088 | +4.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 18822 | +0.105 | -946.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 22697 | +0.196 | -1373.48€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 22697 | +0.196 | -1373.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 5175 | +0.178 | -445.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 5175 | +0.178 | -445.21€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 2831 | +0.204 | -57.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 2831 | +0.204 | -57.57€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 5116 | +0.181 | -406.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 5116 | +0.181 | -406.60€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 4448 | +0.248 | -145.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 4448 | +0.248 | -145.03€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 5048 | +0.187 | -332.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 5048 | +0.187 | -332.83€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 991 | +0.427 | -32.82€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 991 | +0.427 | -32.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 390 | +0.436 | -5.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 390 | +0.436 | -5.47€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE#15min | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 387 | +0.431 | -9.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 387 | +0.431 | -9.50€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 201 | +0.402 | -15.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 201 | +0.402 | -15.52€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 79361 | +0.201 | -5714.38€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 79361 | +0.201 | -5714.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 13627 | +0.185 | -1401.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 13627 | +0.185 | -1401.96€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 12818 | +0.224 | -444.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 12818 | +0.224 | -444.32€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 13593 | +0.181 | -1436.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 13593 | +0.181 | -1436.60€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 12892 | +0.220 | -484.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 12892 | +0.220 | -484.48€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 13164 | +0.201 | -877.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 13164 | +0.201 | -877.05€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 13267 | +0.196 | -1069.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 13267 | +0.196 | -1069.97€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 30339 | +0.117 | +206.62€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 30339 | +0.117 | +206.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 15080 | +0.119 | +176.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 15080 | +0.119 | +176.24€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 15259 | +0.114 | +30.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 15259 | +0.114 | +30.38€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 2029 | +0.292 | -11.11€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 2029 | +0.292 | -11.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 928 | +0.279 | -26.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 928 | +0.279 | -26.38€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 982 | +0.296 | +9.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 982 | +0.296 | +9.96€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 119 | +0.351 | +5.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 119 | +0.351 | +5.31€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 935 | +0.441 | +4.05€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 935 | +0.441 | +4.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 453 | +0.436 | -3.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 453 | +0.436 | -3.66€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 436 | +0.448 | +7.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 436 | +0.448 | +7.17€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 46 | +0.396 | +0.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 46 | +0.396 | +0.55€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1598 | +0.072 | -60.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 616 | +0.053 | -48.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 982 | +0.083 | -12.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 72 | +0.108 | +2.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 72 | +0.108 | +2.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1229 | +0.080 | -22.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 247 | +0.066 | -10.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 982 | +0.083 | -12.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 297 | +0.028 | -41.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 297 | +0.028 | -41.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 59714 | +0.100 | -1525.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 4830 | +0.091 | +49.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 54884 | +0.101 | -1574.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 32884 | +0.105 | -366.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 4830 | +0.091 | +49.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 28054 | +0.108 | -415.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 12215 | +0.109 | -57.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 12215 | +0.109 | -57.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 14615 | +0.081 | -1100.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 14615 | +0.081 | -1100.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 894 | +0.192 | -112.64€ | 3 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 894 | +0.192 | -112.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 894 | +0.192 | -112.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 894 | +0.192 | -112.64€ | 3 | 4 |
| ✅ GBM_LATE_15M | 41109 | +0.093 | +21314.43€ | 0 | 19 |
| ✅ GBM_LATE_15M#15min | 41109 | +0.093 | +21314.43€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 6864 | +0.214 | +5611.09€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 6864 | +0.214 | +5611.09€ | 0 | 23 |
| ✅ GBM_LATE_15M#BTC | 6153 | +0.178 | +4629.97€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 6153 | +0.178 | +4629.97€ | 0 | 25 |
| ✅ GBM_LATE_15M#DOGE | 7351 | +0.205 | +5703.40€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 7351 | +0.205 | +5703.40€ | 0 | 20 |
| ✅ GBM_LATE_15M#ETH | 5735 | +0.040 | +1572.47€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 5735 | +0.040 | +1572.47€ | 1 | 19 |
| ✅ GBM_LATE_15M#SOL | 5805 | -0.031 | +1233.05€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 5805 | -0.031 | +1233.05€ | 4 | 15 |
| ✅ GBM_LATE_15M#XRP | 9201 | -0.031 | +2564.45€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 9201 | -0.031 | +2564.45€ | 3 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 44290 | +0.085 | +24005.54€ | 0 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 44290 | +0.085 | +24005.54€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 8552 | +0.004 | +4303.73€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 8552 | +0.004 | +4303.73€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 9357 | +0.010 | +2193.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 9357 | +0.010 | +2193.76€ | 0 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 6152 | +0.277 | +6577.35€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 6152 | +0.277 | +6577.35€ | 0 | 20 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 7933 | +0.013 | +1951.78€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 7933 | +0.013 | +1951.78€ | 1 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 7079 | +0.039 | +2915.55€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 7079 | +0.039 | +2915.55€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 5217 | +0.300 | +6063.37€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 5217 | +0.300 | +6063.37€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 32645 | +0.179 | +26321.63€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 32645 | +0.179 | +26321.63€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 4953 | +0.228 | +4367.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 4953 | +0.228 | +4367.94€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 5120 | +0.149 | +3766.09€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 5120 | +0.149 | +3766.09€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 5229 | +0.223 | +4499.51€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 5229 | +0.223 | +4499.51€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 5536 | +0.138 | +4195.14€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 5536 | +0.138 | +4195.14€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 6140 | +0.123 | +4559.34€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 6140 | +0.123 | +4559.34€ | 0 | 26 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 5667 | +0.224 | +4933.61€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 5667 | +0.224 | +4933.61€ | 0 | 26 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 8739 | +0.134 | +4258.20€ | 0 | 18 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 8739 | +0.134 | +4258.20€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 405 | +0.154 | +252.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 405 | +0.154 | +252.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 2590 | +0.144 | +1479.34€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 2590 | +0.144 | +1479.34€ | 0 | 23 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 418 | +0.148 | +207.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 418 | +0.148 | +207.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 2609 | +0.139 | +1236.13€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 2609 | +0.139 | +1236.13€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 2135 | +0.108 | +822.25€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 2135 | +0.108 | +822.25€ | 0 | 16 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 582 | +0.134 | +260.21€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 582 | +0.134 | +260.21€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO | 41319 | +0.184 | +32883.47€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#15min | 41319 | +0.184 | +32883.47€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 6549 | +0.240 | +6077.54€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 6549 | +0.240 | +6077.54€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 6418 | +0.147 | +4349.96€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 6418 | +0.147 | +4349.96€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 6982 | +0.232 | +6219.58€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 6982 | +0.232 | +6219.58€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 6810 | +0.138 | +4837.65€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 6810 | +0.138 | +4837.65€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 7318 | +0.121 | +5037.65€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 7318 | +0.121 | +5037.65€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 7242 | +0.229 | +6361.10€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 7242 | +0.229 | +6361.10€ | 0 | 21 |
| ✅ GBM_LATE_5M | 11441 | +0.199 | +8763.21€ | 1 | 29 |
| ✅ GBM_LATE_5M#5min | 11441 | +0.199 | +8763.21€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 940 | +0.237 | +852.08€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 940 | +0.237 | +852.08€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 2665 | +0.202 | +2231.39€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 2665 | +0.202 | +2231.39€ | 0 | 27 |
| ✅ GBM_LATE_5M#DOGE | 1081 | +0.188 | +762.64€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1081 | +0.188 | +762.64€ | 0 | 18 |
| ✅ GBM_LATE_5M#ETH | 3322 | +0.193 | +2339.10€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 3322 | +0.193 | +2339.10€ | 0 | 26 |
| ✅ GBM_LATE_5M#SOL | 1680 | +0.189 | +1265.42€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 1680 | +0.189 | +1265.42€ | 0 | 27 |
| ✅ GBM_LATE_5M#XRP | 1753 | +0.201 | +1312.57€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1753 | +0.201 | +1312.57€ | 0 | 0 |
| ✅ GBM_LATE_60M | 3327 | +0.067 | +1111.91€ | 1 | 8 |
| ✅ GBM_LATE_60M#60min | 3327 | +0.067 | +1111.91€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 1232 | +0.083 | +466.21€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 1232 | +0.083 | +466.21€ | 1 | 7 |
| ✅ GBM_LATE_60M#ETH | 1070 | +0.070 | +384.67€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 1070 | +0.070 | +384.67€ | 0 | 9 |
| ✅ GBM_LATE_60M#SOL | 1025 | +0.044 | +261.03€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 1025 | +0.044 | +261.03€ | 2 | 12 |
| 🚫 GBM_LATE_60M_FADE | 552 | -0.247 | -25.96€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 552 | -0.247 | -25.96€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 207 | -0.242 | -12.51€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 207 | -0.242 | -12.51€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 195 | -0.231 | -4.04€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 195 | -0.231 | -4.04€ | 4 | 1 |
| 🚫 GBM_LATE_60M_FADE#SOL | 150 | -0.270 | -9.41€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 150 | -0.270 | -9.41€ | 4 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 1479 | +0.083 | +387.86€ | 1 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 1479 | +0.083 | +387.86€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 582 | +0.081 | +144.90€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 582 | +0.081 | +144.90€ | 1 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 531 | +0.057 | +83.11€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 531 | +0.057 | +83.11€ | 2 | 9 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 366 | +0.122 | +159.85€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 366 | +0.122 | +159.85€ | 2 | 10 |
| ✅ LATE_WINDOW_5MIN | 161 | +0.273 | +154.25€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 161 | +0.273 | +154.25€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 161 | +0.273 | +154.25€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 161 | +0.273 | +154.25€ | 1 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 3326 | +0.101 | +821.86€ | 0 | 1 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 3326 | +0.101 | +821.86€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 3326 | +0.101 | +821.86€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 3326 | +0.101 | +821.86€ | 0 | 1 |
| ✅ LIQUIDACIONES_15M | 501 | -0.053 | -24.48€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 501 | -0.053 | -24.48€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 137 | -0.018 | +1.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 137 | -0.018 | +1.11€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 92 | -0.074 | -7.43€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 92 | -0.074 | -7.43€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 191 | -0.008 | -1.30€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 191 | -0.008 | -1.30€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M | 3646 | +0.017 | +84.54€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 3646 | +0.017 | +84.54€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 175 | +0.025 | -1.76€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 175 | +0.025 | -1.76€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 760 | +0.014 | +34.81€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 760 | +0.014 | +34.81€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE | 204 | -0.015 | -4.58€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 204 | -0.015 | -4.58€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 1310 | +0.027 | +33.06€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1310 | +0.027 | +33.06€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 755 | +0.011 | +1.37€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 755 | +0.011 | +1.37€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 442 | +0.011 | +21.64€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 442 | +0.011 | +21.64€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 1711 | -0.040 | -27.49€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1711 | -0.040 | -27.49€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 492 | -0.028 | -10.05€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 492 | -0.028 | -10.05€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 579 | -0.015 | +6.05€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 579 | -0.015 | +6.05€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 640 | -0.072 | -23.49€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 640 | -0.072 | -23.49€ | 5 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 8192 | -0.029 | -28.77€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 3888 | -0.037 | -96.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 4304 | -0.020 | +67.39€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 243 | -0.039 | -7.99€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 124 | -0.024 | -0.52€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 119 | -0.054 | -7.47€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 2043 | -0.019 | +17.14€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 972 | -0.025 | -7.18€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 1071 | -0.013 | +24.32€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 903 | -0.027 | +6.29€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 454 | -0.046 | -15.82€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 449 | -0.008 | +22.12€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 1768 | -0.042 | -65.84€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 821 | -0.053 | -56.31€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 947 | -0.033 | -9.52€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 1601 | -0.025 | +6.88€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 763 | -0.039 | -18.03€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 838 | -0.013 | +24.91€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 1634 | -0.028 | +14.75€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 754 | -0.033 | +1.71€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 880 | -0.024 | +13.04€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 48210 | -0.001 | +2431.32€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 48210 | -0.001 | +2431.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 8680 | +0.026 | +1106.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 8680 | +0.026 | +1106.72€ | 2 | 4 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 6972 | -0.033 | -92.04€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 6972 | -0.033 | -92.04€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 8783 | +0.024 | +914.11€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 8783 | +0.024 | +914.11€ | 2 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 6813 | -0.047 | -135.82€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 6813 | -0.047 | -135.82€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 8150 | -0.005 | +234.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 8150 | -0.005 | +234.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 8812 | +0.015 | +403.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 8812 | +0.015 | +403.80€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 6564 | -0.060 | -161.85€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 6564 | -0.060 | -161.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1225 | -0.000 | -15.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1225 | -0.000 | -15.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1696 | -0.080 | -45.39€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1696 | -0.080 | -45.39€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 54 | -0.054 | -2.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 54 | -0.054 | -2.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 771 | -0.118 | -31.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 771 | -0.118 | -31.93€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1962 | -0.076 | -41.86€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1962 | -0.076 | -41.86€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 856 | -0.015 | -25.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 856 | -0.015 | -25.00€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 119815 | -0.076 | +1790.41€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 119815 | -0.076 | +1790.41€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 20811 | -0.076 | +1114.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 20811 | -0.076 | +1114.87€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 18057 | -0.100 | -972.18€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 18057 | -0.100 | -972.18€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 21094 | -0.068 | +1154.06€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 21094 | -0.068 | +1154.06€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 17600 | -0.097 | -596.59€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 17600 | -0.097 | -596.59€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 21482 | -0.056 | +352.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 21482 | -0.056 | +352.79€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 20771 | -0.065 | +737.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 20771 | -0.065 | +737.46€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 8722 | -0.033 | -179.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 8722 | -0.033 | -179.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 1001 | -0.017 | -18.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 1001 | -0.017 | -18.91€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1974 | -0.045 | -22.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1974 | -0.045 | -22.34€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1008 | -0.022 | -32.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1008 | -0.022 | -32.80€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2584 | -0.026 | -41.92€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2584 | -0.026 | -41.92€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1189 | -0.055 | -28.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1189 | -0.055 | -28.38€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 966 | -0.031 | -35.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 966 | -0.031 | -35.50€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1637 | +0.125 | +676.19€ | 0 | 6 |
| ✅ ORDER_FLOW_5M#5min | 1501 | +0.131 | +663.60€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 351 | +0.146 | +188.29€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 351 | +0.146 | +188.29€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#DOGE | 306 | +0.117 | +104.35€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 306 | +0.117 | +104.35€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#ETH | 299 | +0.138 | +146.82€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 299 | +0.138 | +146.82€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#SOL | 265 | +0.152 | +146.10€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 265 | +0.152 | +146.10€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#XRP | 280 | +0.096 | +78.04€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 280 | +0.096 | +78.04€ | 0 | 3 |
| ✅ ORDER_FLOW_5M_REACTIVO | 1381 | -0.011 | -3.96€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 1381 | -0.011 | -3.96€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 270 | +0.000 | +10.83€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 270 | +0.000 | +10.83€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 236 | -0.008 | +2.00€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 236 | -0.008 | +2.00€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 359 | -0.035 | -20.73€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 359 | -0.035 | -20.73€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 291 | +0.009 | +2.56€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 291 | +0.009 | +2.56€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 225 | -0.011 | +1.37€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 225 | -0.011 | +1.37€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 872 | -0.068 | -36.38€ | 3 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 406 | -0.110 | -73.97€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 317 | -0.140 | -64.18€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 89 | -0.005 | -9.80€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 310 | -0.029 | +26.51€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 224 | -0.022 | +27.01€ | 1 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 86 | -0.045 | -0.50€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 156 | -0.032 | +11.09€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 126 | -0.039 | +6.19€ | 1 | 1 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 30 | +0.000 | +4.90€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 667 | -0.082 | -30.97€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 205 | -0.022 | -5.40€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 1092 | -0.207 | -65.69€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC | 430 | -0.208 | -40.61€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#atexpiry | 374 | -0.213 | -40.89€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 56 | -0.172 | +0.28€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 371 | -0.216 | -34.19€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 325 | -0.225 | -39.89€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 46 | -0.146 | +5.69€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 291 | -0.193 | +9.12€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 272 | -0.190 | +5.98€ | 5 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 19 | -0.204 | +3.14€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 971 | -0.211 | -74.80€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 121 | -0.175 | +9.11€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 437 | +0.393 | +407.43€ | 0 | 12 |
| ✅ RESOLUTION_SNIPER#BTC | 61 | +0.135 | +49.67€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 61 | +0.135 | +49.67€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 107 | +0.362 | +89.61€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 107 | +0.362 | +89.61€ | 0 | 8 |
| ✅ RESOLUTION_SNIPER#SOL | 269 | +0.459 | +268.15€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 269 | +0.459 | +268.15€ | 0 | 10 |
| ✅ RESOLUTION_SNIPER#sniper | 437 | +0.393 | +407.43€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 717 | +0.029 | +34.44€ | 3 | 2 |
| ✅ STREAK_FADE_15M#15min | 717 | +0.029 | +34.44€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 300 | +0.023 | +3.36€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 300 | +0.023 | +3.36€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 59 | -0.008 | -1.64€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 59 | -0.008 | -1.64€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 73 | -0.007 | +0.78€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 73 | -0.007 | +0.78€ | 3 | 1 |
| ✅ STREAK_FADE_15M#XRP | 285 | +0.051 | +31.95€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 285 | +0.051 | +31.95€ | 0 | 5 |
| ✅ STREAK_FADE_5M | 3434 | -0.022 | -134.82€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3434 | -0.022 | -134.82€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 1052 | -0.022 | -37.01€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 1052 | -0.022 | -37.01€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 590 | -0.027 | -26.08€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 590 | -0.027 | -26.08€ | 1 | 0 |
| ✅ STREAK_FADE_5M#SOL | 164 | -0.036 | -13.29€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 164 | -0.036 | -13.29€ | 4 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1628 | -0.018 | -58.44€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1628 | -0.018 | -58.44€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 98 | -0.060 | -10.46€ | 4 | 0 |
| ✅ STREAK_FADE_60M#60min | 98 | -0.060 | -10.46€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 41 | -0.081 | -4.05€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 41 | -0.081 | -4.05€ | 2 | 0 |
| ✅ STREAK_FADE_60M#SOL | 57 | -0.042 | -6.41€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 57 | -0.042 | -6.41€ | 0 | 1 |
| ✅ STREAK_MOM_5M | 10714 | +0.017 | +96.03€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 10714 | +0.017 | +96.03€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2726 | +0.020 | +26.92€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2726 | +0.020 | +26.92€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2783 | +0.021 | +41.26€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2783 | +0.021 | +41.26€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2888 | +0.009 | -0.95€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2888 | +0.009 | -0.95€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2317 | +0.019 | +28.80€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2317 | +0.019 | +28.80€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 9750 | +0.013 | -50.39€ | 2 | 0 |
| ✅ STRUCT_NO_15M#15min | 9750 | +0.013 | -50.39€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 3950 | +0.017 | -8.94€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 3950 | +0.017 | -8.94€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3613 | +0.011 | -26.65€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3613 | +0.011 | -26.65€ | 2 | 0 |
| ✅ STRUCT_NO_15M#SOL | 2187 | +0.009 | -14.80€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 2187 | +0.009 | -14.80€ | 1 | 0 |
| ✅ UPDOWN_GBM | 74341 | +0.053 | +6543.26€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 18546 | +0.083 | +4092.60€ | 0 | 11 |
| ✅ UPDOWN_GBM#240min | 2402 | +0.004 | +23.24€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 48789 | +0.049 | +2343.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 4347 | +0.008 | +84.68€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 6851 | +0.089 | +1075.72€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1576 | +0.156 | +698.08€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 77 | -0.006 | -0.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 5198 | +0.070 | +378.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 15769 | +0.056 | +1356.20€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 2372 | +0.090 | +583.87€ | 0 | 9 |
| ✅ UPDOWN_GBM#BTC#240min | 640 | +0.011 | +11.02€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 10727 | +0.061 | +701.63€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 1937 | +0.004 | +56.43€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 93 | -0.068 | +3.26€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 8267 | +0.067 | +867.25€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1555 | +0.147 | +610.96€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 78 | +0.013 | -1.79€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 6634 | +0.049 | +258.08€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 16935 | +0.044 | +1089.77€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 4358 | +0.064 | +630.51€ | 0 | 12 |
| ✅ UPDOWN_GBM#ETH#240min | 625 | +0.006 | +16.23€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 10349 | +0.043 | +419.34€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 1517 | +0.013 | +21.04€ | 1 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 86 | -0.102 | +2.66€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 16281 | +0.032 | +776.34€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 4562 | +0.034 | +382.27€ | 0 | 4 |
| ✅ UPDOWN_GBM#SOL#240min | 594 | -0.008 | -1.31€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 10156 | +0.036 | +392.90€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 893 | +0.007 | +7.21€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 76 | -0.128 | -4.73€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 10236 | +0.063 | +1379.81€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 4123 | +0.101 | +1186.91€ | 0 | 9 |
| ✅ UPDOWN_GBM#XRP#240min | 388 | +0.010 | -0.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 5725 | +0.040 | +192.97€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 255 | -0.099 | +1.19€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 818 | +0.365 | +300.90€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 818 | +0.365 | +300.90€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 426 | +0.364 | +148.55€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 426 | +0.364 | +148.55€ | 0 | 10 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 392 | +0.363 | +152.35€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 392 | +0.363 | +152.35€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO | 19443 | -0.025 | +4603.24€ | 3 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 19443 | -0.025 | +4603.24€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1718 | -0.056 | +502.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1718 | -0.056 | +502.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 3419 | -0.111 | +149.66€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 3419 | -0.111 | +149.66€ | 4 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 948 | +0.216 | +770.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 948 | +0.216 | +770.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 2336 | +0.218 | +1527.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 2336 | +0.218 | +1527.16€ | 1 | 21 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 5533 | -0.066 | +662.51€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 5533 | -0.066 | +662.51€ | 4 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 5489 | -0.064 | +990.64€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 5489 | -0.064 | +990.64€ | 3 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 221 | +0.034 | +7.42€ | 0 | 1 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 221 | +0.034 | +7.42€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 221 | +0.034 | +7.42€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 221 | +0.034 | +7.42€ | 0 | 1 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1392 | +0.291 | +1185.22€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1392 | +0.291 | +1185.22€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 748 | +0.289 | +605.65€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 748 | +0.289 | +605.65€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 644 | +0.293 | +579.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 644 | +0.293 | +579.57€ | 0 | 9 |
| ✅ UPDOWN_OU_5M | 813 | -0.111 | -82.14€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 813 | -0.111 | -82.14€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 248 | -0.080 | -18.10€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 248 | -0.080 | -18.10€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 87 | -0.163 | -9.15€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 87 | -0.163 | -9.15€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 95 | -0.180 | -5.53€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 95 | -0.180 | -5.53€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 3492 | +0.305 | +1688.36€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 1275 | +0.259 | +171.66€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 1341 | +0.299 | +608.27€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 876 | +0.379 | +908.42€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**✅ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: n≥15 y IC<-0.05
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: IC=+0.021 n=923 — no justifica filtro, seguir monitorizando
  - _Datos_: n=923 IC=+0.021 PNL=+36.00€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 705 celda(s) pasan gate riguroso completo de 2664 evaluadas (n>=40) y 3703 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.034 < 0.08 — monitorear
  - _Datos_: n=4561 IC=+0.034 PNL=+380.41€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=1341/15 IC=+0.299 PNL=+608.27€ | BTC: n=1275/15 IC=+0.259 PNL=+171.66€ | SOL: n=876/15 IC=+0.379 PNL=+908.42€

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
  - _Estado_: alineada_con_outcome_prev IC=+0.137 n=769/60 | contraria IC=+0.191 n=796 | gap=-0.054 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=452, boost estimado=+0.016. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 0/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=1516/40 IC=+0.014 PNL=+21.55€ | BTC#60min: n=1936/40 IC=+0.004 PNL=+56.94€ | SOL#60min: n=893/40 IC=+0.007 PNL=+7.21€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.048 n=539659 | tras_1loss IC=+0.094 n=410846 | tras_2loss IC=+0.063 n=166658/40 | gap=-0.016 (umbral 0.05)

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.205 > 0.08 con n=717 PNL=+560.67€
  - _Datos_: n=717 IC=+0.205 PNL=+560.67€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.176 > 0.08 con n=803 PNL=+477.13€
  - _Datos_: n=803 IC=+0.176 PNL=+477.13€

**🟡 H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: n≥25 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.177 > 0.08 con n=60 PNL=+33.31€
  - _Datos_: n=60 IC=+0.177 PNL=+33.31€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.335 > 0.1 con n=2851 PNL=+1610.74€
  - _Datos_: n=2851 IC=+0.335 PNL=+1610.74€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=650 IC=+0.075 PNL=+75.95€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=650 IC=+0.075 PNL=+75.95€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=83 IC=+0.194 PNL=+59.09€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=83 IC=+0.194 PNL=+59.09€

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
  - _Estado_: n=2925 IC=+0.008 PNL=+3.45€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2925 IC=+0.008 PNL=+3.45€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=1420 IC=+0.009 PNL=+82.26€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=1420 IC=+0.009 PNL=+82.26€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=923 IC=+0.021 PNL=+36.00€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=923 IC=+0.021 PNL=+36.00€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.180 > 0.1 con n=4612 PNL=+2942.39€
  - _Datos_: n=4612 IC=+0.180 PNL=+2942.39€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=2371 IC=+0.089 PNL=+583.37€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=2371 IC=+0.089 PNL=+583.37€

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
  - _Estado_: n=956 IC=+0.036 PNL=+92.92€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=956 IC=+0.036 PNL=+92.92€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=115 IC=+0.021 PNL=+2.50€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=115 IC=+0.021 PNL=+2.50€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.273 n=161) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=161 IC=+0.273 PNL=+154.25€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.130 > 0.02 con n=940 PNL=+409.52€
  - _Datos_: n=940 IC=+0.130 PNL=+409.52€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=202 IC=-0.083 PNL=+23.24€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=202 IC=-0.083 PNL=+23.24€

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
  - _Estado_: n=29010 IC=+0.073 PNL=+4217.51€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=29010 IC=+0.073 PNL=+4217.51€

**⏳ H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: 120
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: 0/120 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.137 < -0.1 con n=461 PNL=+54.58€
  - _Datos_: n=461 IC=-0.137 PNL=+54.58€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=3057 IC=+0.066 PNL=+372.70€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=3057 IC=+0.066 PNL=+372.70€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=136 IC=-0.094 PNL=+5.06€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=136 IC=-0.094 PNL=+5.06€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.111 > 0.1 con n=770 PNL=+212.52€
  - _Datos_: n=770 IC=+0.111 PNL=+212.52€

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
  - _Estado_: n=30911 IC=-0.134 PNL=+2487.15€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=30911 IC=-0.134 PNL=+2487.15€

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
  - _Estado_: n=3107 IC=+0.131 PNL=+1863.32€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=3107 IC=+0.131 PNL=+1863.32€

**⏳ H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: 40
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=7646 IC=+0.049 PNL=+592.37€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=7646 IC=+0.049 PNL=+592.37€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.093 > 0.08 con n=3359 PNL=+1811.52€
  - _Datos_: n=3359 IC=+0.093 PNL=+1811.52€

**⏳ H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: 80
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: 0/80 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.222 < -0.1 con n=3188 PNL=-246.21€
  - _Datos_: n=3188 IC=-0.222 PNL=-246.21€

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
  - _Estado_: n=66 IC=+0.000 PNL=+4.12€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=66 IC=+0.000 PNL=+4.12€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.103 n=1687) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=1687 IC=+0.103 PNL=+375.73€

**⏳ H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.415 n=560) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=560 IC=+0.415 PNL=+809.80€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=13619 IC=+0.185 PNL=-1402.88€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=13619 IC=+0.185 PNL=-1402.88€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.217 > 0.1 con n=224 PNL=+146.18€
  - _Datos_: n=224 IC=+0.217 PNL=+146.18€
