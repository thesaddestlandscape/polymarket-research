# Hipótesis automáticas — 2026-11-14 08:48 UTC
_Generado por shadow_postmortem.py sobre 1330167 resoluciones (PNL=+183665.94€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.5` → IC=-0.317 (n=195)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.116 (n=704)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.196 (n=1023)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` > 0.505 (IC base=+0.126)

- **PATRÓN** `n_total_lado` > `62.0` → IC=+0.187 (n=324)

  - _Acción_: Kelly boost +0.94€ cuando `n_total_lado` > 62.0 (IC base=+0.126)

- **PATRÓN** `banda_hit_calibrado` > `0.8129` → IC=+0.273 (n=438)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8129 (IC base=+0.126)

- **PATRÓN** `banda_z` > `8.513` → IC=+0.198 (n=322)

  - _Acción_: Kelly boost +0.99€ cuando `banda_z` > 8.513 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.143 (n=359)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 17.0 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.126 (n=693)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 12.0 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.140 (n=1052)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.126)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.302 (n=165)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.113 (n=499)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.193 (n=888)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.505 (IC base=+0.128)

- **PATRÓN** `n_total_lado` > `65.0` → IC=+0.185 (n=281)

  - _Acción_: Kelly boost +0.93€ cuando `n_total_lado` > 65.0 (IC base=+0.128)

- **PATRÓN** `banda_hit_calibrado` > `0.8126` → IC=+0.274 (n=378)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8126 (IC base=+0.128)

- **PATRÓN** `banda_z` > `8.841` → IC=+0.207 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 8.841 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.138 (n=753)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 8.0 (IC base=+0.128)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.135 (n=952)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.128)

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
- **FILTRO** `restante_s_al_confirmar` < `131.82` → IC=-0.217 (n=12070)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 131.82
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=36215)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `125.07` → IC=-0.257 (n=1213)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 125.07
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=3641)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `115.68` → IC=-0.279 (n=1231)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 115.68
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=3694)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `restante_s_al_confirmar` < `116.45` → IC=-0.165 (n=3306)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 116.45
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=9919)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `151.93` → IC=-0.238 (n=3291)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 151.93
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=9874)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `127.97` → IC=-0.266 (n=2269)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 127.97
  - _Potencial_: sin este filtro IC_bueno=-0.089 (n=6810)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.209 (n=28415)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.103)

- **PATRÓN** `libro_liquidez` > `8197.8863` → IC=+0.157 (n=2354)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 8197.8863 (IC base=+0.103)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.128 (n=24582)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 17.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.131 (n=29958)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.124)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.225 (n=22455)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.139 (n=8421)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `6458.3039` → IC=+0.143 (n=3263)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 6458.3039 (IC base=+0.124)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.185 (n=2198)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.177)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.358 (n=751)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.177)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.180 (n=2690)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.01 (IC base=+0.177)

- **PATRÓN** `libro_liquidez` > `16321.0855` → IC=+0.180 (n=698)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 16321.0855 (IC base=+0.177)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.185 (n=1912)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 7.0 (IC base=+0.178)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.181 (n=2141)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 17.0 (IC base=+0.178)

- **PATRÓN** `py_entrada` < `0.295` → IC=+0.312 (n=981)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.295 (IC base=+0.178)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.181 (n=2742)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.01 (IC base=+0.178)

- **PATRÓN** `libro_liquidez` > `16073.2055` → IC=+0.184 (n=708)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 16073.2055 (IC base=+0.178)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.61` → IC=+0.168 (n=619)

  - _Acción_: Kelly boost +0.84€ cuando `py_entrada` > 0.61 (IC base=+0.076)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.146 (n=1454)

  - _Acción_: Kelly boost +0.73€ cuando `py_entrada` < 0.44 (IC base=+0.084)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.170 (n=5140)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 6.0 (IC base=+0.167)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.172 (n=4576)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 15.0 (IC base=+0.167)

- **PATRÓN** `py_entrada` > `0.77` → IC=+0.375 (n=1792)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.77 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.207 (n=2450)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` < `0.275` → IC=+0.332 (n=956)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.275 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.204 (n=2859)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.200)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.141 (n=659)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 15.0 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.143 (n=1186)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 15.0 (IC base=+0.139)

- **PATRÓN** `py_entrada` > `0.675` → IC=+0.254 (n=453)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.675 (IC base=+0.139)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.141 (n=1129)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.156 (n=155)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.074)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.251 (n=957)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.228)

- **PATRÓN** `py_entrada` > `0.83` → IC=+0.420 (n=1339)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.83 (IC base=+0.228)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.157 (n=738)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 7.0 (IC base=+0.145)

- **PATRÓN** `py_entrada` < `0.345` → IC=+0.278 (n=717)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.345 (IC base=+0.145)

### FAVORITO_CONFIRMADO#SOL#60min
- **FILTRO** `libro_liquidez` < `955.8819` → IC=-0.121 (n=159)

  - _Acción_: SKIP cuando `libro_liquidez` < 955.8819
  - _Potencial_: sin este filtro IC_bueno=+0.066 (n=325)

- **PATRÓN** `py_entrada` > `0.55` → IC=+0.165 (n=467)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` > 0.55 (IC base=+0.048)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.142 (n=490)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 17.0 (IC base=+0.122)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.252 (n=446)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.122)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` < `7.0` → IC=-0.257 (n=113)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.254 (n=116)

- **FILTRO** `py_entrada` > `0.755` → IC=-0.299 (n=152)

  - _Acción_: SKIP cuando `py_entrada` > 0.755
  - _Potencial_: sin este filtro IC_bueno=-0.171 (n=77)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.201 (n=24610)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.195)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.197 (n=20780)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 15.0 (IC base=+0.195)

- **PATRÓN** `py_entrada` > `0.738` → IC=+0.229 (n=7785)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.738 (IC base=+0.195)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.338 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.195)

- **PATRÓN** `libro_liquidez` > `4915.142` → IC=+0.338 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4915.142 (IC base=+0.195)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.173 (n=5609)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 5.0 (IC base=+0.168)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.179 (n=5573)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` < 0.74 (IC base=+0.168)

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

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.212 (n=3360)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.208)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.211 (n=2240)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.208)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.248 (n=1659)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.208)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.183 (n=5487)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.175)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.177 (n=4653)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 15.0 (IC base=+0.175)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.176 (n=5636)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` < 0.73 (IC base=+0.175)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.184 (n=4303)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` > 0.71 (IC base=+0.175)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.258 (n=4603)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.251)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.253 (n=3887)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.251)

- **PATRÓN** `py_entrada` > `0.8` → IC=+0.364 (n=1481)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.190 (n=5375)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.186)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.189 (n=4551)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 15.0 (IC base=+0.186)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.197 (n=1798)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` > 0.73 (IC base=+0.186)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.430 (n=980)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.426)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.427 (n=974)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.426)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.437 (n=989)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.426)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.431 (n=1047)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.426)

- **PATRÓN** `libro_liquidez` > `4644.67` → IC=+0.442 (n=631)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4644.67 (IC base=+0.426)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.440 (n=397)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.439)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.446 (n=274)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.439)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.448 (n=438)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.439)

- **PATRÓN** `libro_liquidez` > `12497.2329` → IC=+0.444 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12497.2329 (IC base=+0.439)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.431 (n=389)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.424)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.428 (n=386)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.424)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.443 (n=296)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.424)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.429 (n=438)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.424)

- **PATRÓN** `libro_liquidez` > `4814.8438` → IC=+0.431 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4814.8438 (IC base=+0.424)

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

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.205 (n=32258)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.239 (n=32388)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.199)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.186 (n=4820)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 18.0 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.178 (n=10328)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 12.0 (IC base=+0.177)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.206 (n=6885)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.177)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.226 (n=13465)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.224)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.285 (n=4516)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.224)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.183 (n=13491)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 7.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.197 (n=11452)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` > 0.72 (IC base=+0.180)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.855` → IC=-0.357 (n=19)

  - _Acción_: SKIP cuando `py_entrada` < 0.855
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.228 (n=4516)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.219)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.221 (n=5190)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.219)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.254 (n=7439)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.219)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **FILTRO** `hora_utc` > `3.0` → IC=-0.278 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.214 (n=4575)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.204)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.256 (n=4670)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.204)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.202 (n=5370)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.197 (n=5360)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 6.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.245 (n=5539)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.196)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.194 (n=11625)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.141 (n=12324)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `3.41` → IC=+0.139 (n=14157)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 3.41 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.194 (n=5667)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.144 (n=5572)

  - _Acción_: Kelly boost +0.72€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.124 (n=7147)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 7.0 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `4.03` → IC=+0.141 (n=7048)

  - _Acción_: Kelly boost +0.71€ cuando `lag_apertura_s` < 4.03 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.195 (n=5958)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.138 (n=7486)

  - _Acción_: Kelly boost +0.69€ cuando `restante_min` > 4.95 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `3.09` → IC=+0.138 (n=7108)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 3.09 (IC base=+0.117)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.305 (n=1416)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.292)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.292 (n=1758)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.292)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.386 (n=728)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.292)

- **PATRÓN** `libro_liquidez` > `3977.0508` → IC=+0.292 (n=898)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3977.0508 (IC base=+0.292)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.285 (n=951)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.281)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.367 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.281)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.315 (n=690)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.295)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.300 (n=1011)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.295)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.391 (n=347)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.440 (n=964)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.437)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.443 (n=928)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.437)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.438 (n=449)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.433)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.437 (n=314)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.433)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.442 (n=340)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.433)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.449 (n=311)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.440)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.439 (n=393)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.440)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.444 (n=429)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.440)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.439 (n=374)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.440)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4847` → IC=+0.139 (n=18302)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.4847 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.129 (n=18497)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 6.0 (IC base=+0.123)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.125 (n=12758)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 12.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` > `0.9767` → IC=+0.246 (n=6102)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9767 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` > `0.8014` → IC=+0.282 (n=983)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8014 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.479` → IC=+0.188 (n=9169)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 3.479 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` > `0.6957` → IC=+0.268 (n=4931)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6957 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` > `0.3041` → IC=+0.250 (n=1884)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3041 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` > `2.7479` → IC=+0.235 (n=4399)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7479 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.137 (n=9018)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `4684.3506` → IC=+0.150 (n=6100)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 4684.3506 (IC base=+0.123)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.123 (n=11465)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0063 (IC base=+0.085)

- **PATRÓN** `ibs_20min` < `0.5642` → IC=+0.144 (n=22928)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.5642 (IC base=+0.085)

- **PATRÓN** `dist_vwap_pct` > `0.6258` → IC=+0.191 (n=1489)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.6258 (IC base=+0.085)

- **PATRÓN** `volumen_regimen` < `0.8592` → IC=+0.195 (n=6292)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` < 0.8592 (IC base=+0.085)

- **PATRÓN** `volumen_pendiente_norm` > `0.2958` → IC=+0.234 (n=2313)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2958 (IC base=+0.085)

- **PATRÓN** `volumen_spike_ratio` > `2.6625` → IC=+0.214 (n=5332)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6625 (IC base=+0.085)

- **PATRÓN** `ballena_activa_n` < `99.0` → IC=+0.230 (n=15913)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 99.0 (IC base=+0.085)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `drift_60min` |x|≤ `0.3706` → IC=+0.213 (n=3894)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3706 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.228 (n=1888)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` > `0.9851` → IC=+0.276 (n=1765)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9851 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.441` → IC=+0.278 (n=1736)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.441 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.2341` → IC=+0.254 (n=686)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2341 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `1.4382` → IC=+0.212 (n=3733)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4382 (IC base=+0.211)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.223 (n=4322)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `2030.82` → IC=+0.211 (n=1298)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2030.82 (IC base=+0.211)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.222 (n=2493)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.211)

- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.248 (n=1564)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0094 (IC base=+0.243)

- **PATRÓN** `drift_60min` |x|≤ `0.1971` → IC=+0.265 (n=2299)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1971 (IC base=+0.243)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.247 (n=1289)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.243)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.251 (n=1595)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.243)

- **PATRÓN** `ibs_20min` < `0.5669` → IC=+0.259 (n=3448)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5669 (IC base=+0.243)

- **PATRÓN** `volumen_pendiente_norm` < `0.095` → IC=+0.245 (n=3121)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.095 (IC base=+0.243)

- **PATRÓN** `volumen_pendiente_norm` > `0.2892` → IC=+0.251 (n=463)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2892 (IC base=+0.243)

- **PATRÓN** `volumen_spike_ratio` < `1.4471` → IC=+0.246 (n=1099)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4471 (IC base=+0.243)

- **PATRÓN** `volumen_spike_ratio` > `1.8604` → IC=+0.247 (n=2196)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8604 (IC base=+0.243)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.245 (n=3991)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.243)

- **PATRÓN** `libro_liquidez` > `1775.17` → IC=+0.249 (n=2298)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1775.17 (IC base=+0.243)

- **PATRÓN** `ballena_activa_n` < `6.0` → IC=+0.244 (n=1184)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 6.0 (IC base=+0.243)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.237 (n=1099)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.224)

- **PATRÓN** `drift_60min` |x|≤ `0.1108` → IC=+0.251 (n=1449)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1108 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.236 (n=3447)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.225 (n=2347)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` > `0.8994` → IC=+0.257 (n=1097)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8994 (IC base=+0.224)

- **PATRÓN** `dist_vwap_pct` > `0.1869` → IC=+0.234 (n=1445)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1869 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.835` → IC=+0.263 (n=483)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.835 (IC base=+0.224)

- **PATRÓN** `volumen_regimen` > `0.6977` → IC=+0.232 (n=2941)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6977 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` > `0.2784` → IC=+0.270 (n=454)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2784 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` > `2.4472` → IC=+0.249 (n=1083)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4472 (IC base=+0.224)

- **PATRÓN** `libro_liquidez` > `15928.6386` → IC=+0.223 (n=1097)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15928.6386 (IC base=+0.224)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.153 (n=3540)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0065 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.0785` → IC=+0.159 (n=1181)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.0785 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.155 (n=1322)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 17.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` < `0.7053` → IC=+0.171 (n=3540)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.7053 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.974` → IC=+0.141 (n=3233)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` < 3.974 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `0.629` → IC=+0.155 (n=1180)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.629 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` > `0.0973` → IC=+0.156 (n=1302)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` > 0.0973 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` < `2.442` → IC=+0.142 (n=3413)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.442 (IC base=+0.133)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.133 (n=4600)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.01 (IC base=+0.133)

- **PATRÓN** `ballena_activa_n` < `174.0` → IC=+0.188 (n=1131)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 174.0 (IC base=+0.133)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.207 (n=2757)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0098 (IC base=+0.194)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.203 (n=4338)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.194)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.259 (n=1606)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.194)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.966` → IC=+0.282 (n=910)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.966 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` < `0.097` → IC=+0.196 (n=3703)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` < 0.097 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` > `0.3512` → IC=+0.226 (n=534)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3512 (IC base=+0.194)

- **PATRÓN** `volumen_spike_ratio` > `2.7279` → IC=+0.212 (n=1829)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7279 (IC base=+0.194)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.199 (n=5005)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.04 (IC base=+0.194)

- **PATRÓN** `libro_liquidez` > `2006.8956` → IC=+0.204 (n=1377)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2006.8956 (IC base=+0.194)

- **PATRÓN** `sigma_h` < `0.0122` → IC=+0.224 (n=3820)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0122 (IC base=+0.222)

- **PATRÓN** `drift_60min` |x|≤ `0.1771` → IC=+0.236 (n=1683)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1771 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.243 (n=1452)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.227 (n=1742)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` < `0.0486` → IC=+0.269 (n=1274)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0486 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.754` → IC=+0.258 (n=411)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.754 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` > `0.3473` → IC=+0.256 (n=556)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3473 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` > `2.156` → IC=+0.231 (n=2453)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.156 (IC base=+0.222)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.224 (n=1922)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.222)

- **PATRÓN** `libro_liquidez` > `1986.95` → IC=+0.227 (n=1274)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1986.95 (IC base=+0.222)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.226 (n=3668)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 24.0 (IC base=+0.222)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.177 (n=215)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.066 (n=4981)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.150 (n=678)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0039 (IC base=+0.063)

- **PATRÓN** `ibs_20min` > `0.9435` → IC=+0.237 (n=676)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9435 (IC base=+0.063)

- **PATRÓN** `dist_vwap_pct` > `0.1404` → IC=+0.341 (n=462)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1404 (IC base=+0.063)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.12` → IC=+0.208 (n=1487)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.12 (IC base=+0.063)

- **PATRÓN** `volumen_regimen` > `1.1075` → IC=+0.357 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1075 (IC base=+0.063)

- **PATRÓN** `volumen_pendiente_norm` < `0.1669` → IC=+0.340 (n=656)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1669 (IC base=+0.063)

- **PATRÓN** `volumen_pendiente_norm` > `0.3052` → IC=+0.340 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3052 (IC base=+0.063)

- **PATRÓN** `volumen_spike_ratio` < `1.5458` → IC=+0.352 (n=349)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5458 (IC base=+0.063)

- **PATRÓN** `volumen_spike_ratio` > `2.2842` → IC=+0.342 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2842 (IC base=+0.063)

- **PATRÓN** `ballena_activa_n` < `142.0` → IC=+0.343 (n=807)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 142.0 (IC base=+0.063)

- **PATRÓN** `ibs_20min` < `0.0868` → IC=+0.186 (n=1300)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.0868 (IC base=+0.055)

- **PATRÓN** `dist_vwap_pct` > `0.539` → IC=+0.164 (n=424)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.539 (IC base=+0.055)

- **PATRÓN** `volumen_regimen` < `1.0033` → IC=+0.163 (n=2210)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.0033 (IC base=+0.055)

- **PATRÓN** `volumen_pendiente_norm` > `0.2799` → IC=+0.212 (n=317)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2799 (IC base=+0.055)

- **PATRÓN** `volumen_spike_ratio` < `1.7655` → IC=+0.156 (n=1612)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.7655 (IC base=+0.055)

- **PATRÓN** `volumen_spike_ratio` > `1.5059` → IC=+0.163 (n=2160)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.5059 (IC base=+0.055)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.180 (n=148)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=793)

- **FILTRO** `ibs_20min` < `0.2667` → IC=-0.174 (n=234)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2667
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=707)

- **FILTRO** `ibs_20min` > `0.2` → IC=-0.131 (n=4859)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2
  - _Potencial_: sin este filtro IC_bueno=+0.155 (n=2442)

- **FILTRO** `sigma_ewma_delta_pct` > `8.302` → IC=-0.231 (n=789)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.302
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=6512)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.180 (n=320)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.75 (IC base=+0.023)

- **PATRÓN** `dist_vwap_pct` > `0.9668` → IC=+0.283 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9668 (IC base=+0.023)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.266` → IC=+0.141 (n=321)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 2.266 (IC base=+0.023)

- **PATRÓN** `volumen_regimen` < `0.8516` → IC=+0.267 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8516 (IC base=+0.023)

- **PATRÓN** `volumen_regimen` > `0.6233` → IC=+0.290 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6233 (IC base=+0.023)

- **PATRÓN** `volumen_pendiente_norm` < `0.0791` → IC=+0.283 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0791 (IC base=+0.023)

- **PATRÓN** `volumen_spike_ratio` < `2.1989` → IC=+0.290 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1989 (IC base=+0.023)

- **PATRÓN** `volumen_spike_ratio` > `1.449` → IC=+0.267 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.449 (IC base=+0.023)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.276 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 40.0 (IC base=+0.023)

- **PATRÓN** `ibs_20min` < `0.2` → IC=+0.155 (n=2442)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.2 (IC base=-0.035)

- **PATRÓN** `dist_vwap_pct` > `0.23` → IC=+0.286 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.23 (IC base=-0.035)

- **PATRÓN** `volumen_regimen` < `0.6993` → IC=+0.296 (n=478)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6993 (IC base=-0.035)

- **PATRÓN** `volumen_regimen` > `1.0553` → IC=+0.286 (n=493)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0553 (IC base=-0.035)

- **PATRÓN** `volumen_pendiente_norm` > `0.0787` → IC=+0.309 (n=490)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0787 (IC base=-0.035)

- **PATRÓN** `volumen_spike_ratio` < `2.4493` → IC=+0.297 (n=1018)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4493 (IC base=-0.035)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `ibs_20min` < `0.79` → IC=-0.157 (n=3736)

  - _Acción_: SKIP cuando `ibs_20min` < 0.79
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=1935)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.173 (n=1196)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=4475)

- **FILTRO** `ibs_20min` > `0.7353` → IC=-0.190 (n=1955)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7353
  - _Potencial_: sin este filtro IC_bueno=+0.070 (n=5879)

- **PATRÓN** `ibs_20min` > `0.79` → IC=+0.136 (n=1935)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` > 0.79 (IC base=-0.057)

- **PATRÓN** `dist_vwap_pct` > `1.001` → IC=+0.351 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.001 (IC base=-0.057)

- **PATRÓN** `dist_vwap_pct` < `0.2513` → IC=+0.298 (n=1020)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2513 (IC base=-0.057)

- **PATRÓN** `volumen_regimen` > `0.7043` → IC=+0.318 (n=1007)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7043 (IC base=-0.057)

- **PATRÓN** `volumen_pendiente_norm` < `0.1074` → IC=+0.301 (n=1073)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1074 (IC base=-0.057)

- **PATRÓN** `volumen_pendiente_norm` > `0.17` → IC=+0.301 (n=295)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.17 (IC base=-0.057)

- **PATRÓN** `volumen_spike_ratio` < `1.5796` → IC=+0.303 (n=486)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5796 (IC base=-0.057)

- **PATRÓN** `volumen_spike_ratio` > `2.5185` → IC=+0.314 (n=368)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5185 (IC base=-0.057)

- **PATRÓN** `dist_vwap_pct` > `1.0624` → IC=+0.280 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0624 (IC base=+0.005)

- **PATRÓN** `volumen_regimen` < `0.6409` → IC=+0.273 (n=768)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6409 (IC base=+0.005)

- **PATRÓN** `volumen_regimen` > `1.2067` → IC=+0.287 (n=768)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2067 (IC base=+0.005)

- **PATRÓN** `volumen_pendiente_norm` > `0.2844` → IC=+0.289 (n=320)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2844 (IC base=+0.005)

- **PATRÓN** `volumen_spike_ratio` < `2.4675` → IC=+0.265 (n=2176)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4675 (IC base=+0.005)

- **PATRÓN** `volumen_spike_ratio` > `1.4346` → IC=+0.271 (n=2176)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4346 (IC base=+0.005)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0108` → IC=+0.196 (n=7947)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` > 0.0108 (IC base=+0.087)

- **PATRÓN** `ibs_20min` > `0.8667` → IC=+0.285 (n=10806)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8667 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` > `0.9348` → IC=+0.301 (n=1638)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9348 (IC base=+0.087)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.469` → IC=+0.169 (n=10687)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 3.469 (IC base=+0.087)

- **PATRÓN** `volumen_regimen` > `0.6921` → IC=+0.279 (n=7862)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6921 (IC base=+0.087)

- **PATRÓN** `volumen_pendiente_norm` > `0.2928` → IC=+0.296 (n=1961)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2928 (IC base=+0.087)

- **PATRÓN** `volumen_spike_ratio` > `2.6446` → IC=+0.287 (n=4609)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6446 (IC base=+0.087)

- **PATRÓN** `ballena_activa_n` < `89.0` → IC=+0.309 (n=13464)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 89.0 (IC base=+0.087)

- **PATRÓN** `sigma_h` > `0.0103` → IC=+0.157 (n=7689)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0103 (IC base=+0.084)

- **PATRÓN** `ibs_20min` < `0.5192` → IC=+0.172 (n=20285)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.5192 (IC base=+0.084)

- **PATRÓN** `volumen_regimen` < `0.6971` → IC=+0.281 (n=3394)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6971 (IC base=+0.084)

- **PATRÓN** `volumen_regimen` > `1.1877` → IC=+0.285 (n=2572)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1877 (IC base=+0.084)

- **PATRÓN** `volumen_pendiente_norm` > `0.2944` → IC=+0.328 (n=1715)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2944 (IC base=+0.084)

- **PATRÓN** `volumen_spike_ratio` < `1.4517` → IC=+0.305 (n=3801)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4517 (IC base=+0.084)

- **PATRÓN** `volumen_spike_ratio` > `2.2745` → IC=+0.304 (n=5169)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2745 (IC base=+0.084)

- **PATRÓN** `ballena_activa_n` < `72.0` → IC=+0.311 (n=11381)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 72.0 (IC base=+0.084)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.8037` → IC=-0.136 (n=4229)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8037
  - _Potencial_: sin este filtro IC_bueno=+0.303 (n=2179)

- **FILTRO** `ibs_20min` > `0.7128` → IC=-0.237 (n=1417)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7128
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=4255)

- **FILTRO** `sigma_ewma_delta_pct` > `4.079` → IC=-0.238 (n=1219)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.079
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=4453)

- **PATRÓN** `ibs_20min` > `0.8037` → IC=+0.303 (n=2179)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8037 (IC base=+0.013)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.964` → IC=+0.190 (n=2132)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 2.964 (IC base=+0.013)

- **PATRÓN** `volumen_pendiente_norm` > `0.2286` → IC=+0.331 (n=407)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2286 (IC base=+0.013)

- **PATRÓN** `volumen_spike_ratio` < `1.4475` → IC=+0.284 (n=678)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4475 (IC base=+0.013)

- **PATRÓN** `volumen_spike_ratio` > `2.2415` → IC=+0.305 (n=922)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2415 (IC base=+0.013)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.318 (n=1415)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.013)

- **PATRÓN** `ibs_20min` < `0.1733` → IC=+0.173 (n=1419)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.1733 (IC base=-0.020)

- **PATRÓN** `volumen_pendiente_norm` < `0.1512` → IC=+0.397 (n=1145)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1512 (IC base=-0.020)

- **PATRÓN** `volumen_spike_ratio` < `1.4257` → IC=+0.422 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4257 (IC base=-0.020)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.395 (n=1135)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 22.0 (IC base=-0.020)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.3014` → IC=+0.226 (n=747)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3014 (IC base=+0.011)

- **PATRÓN** `volumen_regimen` < `1.1952` → IC=+0.211 (n=2330)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1952 (IC base=+0.011)

- **PATRÓN** `volumen_regimen` > `0.6948` → IC=+0.221 (n=2082)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6948 (IC base=+0.011)

- **PATRÓN** `volumen_pendiente_norm` > `0.275` → IC=+0.247 (n=310)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.275 (IC base=+0.011)

- **PATRÓN** `volumen_spike_ratio` < `1.417` → IC=+0.231 (n=770)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.417 (IC base=+0.011)

- **PATRÓN** `volumen_spike_ratio` > `2.4708` → IC=+0.216 (n=768)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4708 (IC base=+0.011)

- **PATRÓN** `ballena_activa_n` < `257.0` → IC=+0.245 (n=1533)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 257.0 (IC base=+0.011)

- **PATRÓN** `volumen_regimen` > `1.0179` → IC=+0.265 (n=759)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0179 (IC base=-0.001)

- **PATRÓN** `volumen_pendiente_norm` > `0.2697` → IC=+0.304 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2697 (IC base=-0.001)

- **PATRÓN** `volumen_spike_ratio` < `1.5257` → IC=+0.263 (n=714)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5257 (IC base=-0.001)

- **PATRÓN** `volumen_spike_ratio` > `2.1487` → IC=+0.263 (n=735)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1487 (IC base=-0.001)

- **PATRÓN** `ballena_activa_n` < `183.0` → IC=+0.280 (n=544)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 183.0 (IC base=-0.001)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.323 (n=1508)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0113 (IC base=+0.284)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.295 (n=3323)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.284)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.326 (n=1802)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.284)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.584` → IC=+0.306 (n=2240)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.584 (IC base=+0.284)

- **PATRÓN** `volumen_pendiente_norm` < `0.0974` → IC=+0.296 (n=2925)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0974 (IC base=+0.284)

- **PATRÓN** `volumen_spike_ratio` > `3.2547` → IC=+0.298 (n=1077)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.2547 (IC base=+0.284)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.293 (n=3997)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.284)

- **PATRÓN** `libro_liquidez` > `2009.4584` → IC=+0.295 (n=1108)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2009.4584 (IC base=+0.284)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.306 (n=2036)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 14.0 (IC base=+0.284)

- **PATRÓN** `sigma_h` > `0.0091` → IC=+0.331 (n=2022)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0091 (IC base=+0.307)

- **PATRÓN** `drift_60min` |x|≤ `0.179` → IC=+0.325 (n=1336)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.179 (IC base=+0.307)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.327 (n=1164)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.307)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.310 (n=1380)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.307)

- **PATRÓN** `ibs_20min` > `0.1489` → IC=+0.318 (n=2022)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1489 (IC base=+0.307)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.098` → IC=+0.312 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.098 (IC base=+0.307)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.414` → IC=+0.308 (n=3143)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.414 (IC base=+0.307)

- **PATRÓN** `volumen_pendiente_norm` < `0.1989` → IC=+0.307 (n=2994)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1989 (IC base=+0.307)

- **PATRÓN** `volumen_pendiente_norm` > `0.3448` → IC=+0.316 (n=493)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3448 (IC base=+0.307)

- **PATRÓN** `volumen_spike_ratio` > `2.7396` → IC=+0.323 (n=1329)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7396 (IC base=+0.307)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.308 (n=1531)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.307)

- **PATRÓN** `libro_liquidez` > `1987.5384` → IC=+0.314 (n=1011)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1987.5384 (IC base=+0.307)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.312 (n=2569)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 22.0 (IC base=+0.307)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7183` → IC=-0.178 (n=1503)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7183
  - _Potencial_: sin este filtro IC_bueno=+0.070 (n=4511)

- **PATRÓN** `dist_vwap_pct` > `0.1465` → IC=+0.237 (n=1065)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1465 (IC base=+0.022)

- **PATRÓN** `volumen_regimen` < `1.1591` → IC=+0.238 (n=2146)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1591 (IC base=+0.022)

- **PATRÓN** `volumen_pendiente_norm` < `0.1618` → IC=+0.237 (n=2249)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1618 (IC base=+0.022)

- **PATRÓN** `volumen_pendiente_norm` > `0.1024` → IC=+0.243 (n=702)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1024 (IC base=+0.022)

- **PATRÓN** `volumen_spike_ratio` < `2.4283` → IC=+0.241 (n=2083)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4283 (IC base=+0.022)

- **PATRÓN** `ballena_activa_n` < `113.0` → IC=+0.255 (n=2120)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 113.0 (IC base=+0.022)

- **PATRÓN** `dist_vwap_pct` > `0.7363` → IC=+0.262 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7363 (IC base=+0.008)

- **PATRÓN** `volumen_regimen` < `1.1877` → IC=+0.263 (n=1553)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1877 (IC base=+0.008)

- **PATRÓN** `volumen_regimen` > `0.6165` → IC=+0.256 (n=1553)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6165 (IC base=+0.008)

- **PATRÓN** `volumen_pendiente_norm` > `0.2826` → IC=+0.307 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2826 (IC base=+0.008)

- **PATRÓN** `volumen_spike_ratio` < `1.7856` → IC=+0.290 (n=996)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7856 (IC base=+0.008)

- **PATRÓN** `volumen_spike_ratio` > `2.4276` → IC=+0.280 (n=498)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4276 (IC base=+0.008)

- **PATRÓN** `ballena_activa_n` < `115.0` → IC=+0.284 (n=1516)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 115.0 (IC base=+0.008)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7429` → IC=-0.248 (n=2456)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7429
  - _Potencial_: sin este filtro IC_bueno=+0.312 (n=2460)

- **FILTRO** `ibs_20min` > `0.6154` → IC=-0.235 (n=1161)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6154
  - _Potencial_: sin este filtro IC_bueno=+0.156 (n=3498)

- **FILTRO** `sigma_ewma_delta_pct` > `8.287` → IC=-0.267 (n=531)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.287
  - _Potencial_: sin este filtro IC_bueno=+0.101 (n=4128)

- **PATRÓN** `ibs_20min` > `0.7429` → IC=+0.312 (n=2460)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7429 (IC base=+0.033)

- **PATRÓN** `dist_vwap_pct` > `1.0473` → IC=+0.354 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0473 (IC base=+0.033)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.448` → IC=+0.157 (n=1993)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 2.448 (IC base=+0.033)

- **PATRÓN** `volumen_regimen` < `0.8382` → IC=+0.345 (n=1195)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8382 (IC base=+0.033)

- **PATRÓN** `volumen_regimen` > `0.6911` → IC=+0.336 (n=1601)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6911 (IC base=+0.033)

- **PATRÓN** `volumen_pendiente_norm` < `0.1575` → IC=+0.335 (n=1847)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1575 (IC base=+0.033)

- **PATRÓN** `volumen_pendiente_norm` > `0.2752` → IC=+0.370 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2752 (IC base=+0.033)

- **PATRÓN** `volumen_spike_ratio` < `1.4268` → IC=+0.363 (n=581)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4268 (IC base=+0.033)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.355 (n=1555)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=+0.033)

- **PATRÓN** `ibs_20min` < `0.6154` → IC=+0.156 (n=3498)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.6154 (IC base=+0.059)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.052` → IC=+0.134 (n=3282)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` < 3.052 (IC base=+0.059)

- **PATRÓN** `volumen_regimen` < `0.6916` → IC=+0.279 (n=780)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6916 (IC base=+0.059)

- **PATRÓN** `volumen_pendiente_norm` > `0.0705` → IC=+0.297 (n=711)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0705 (IC base=+0.059)

- **PATRÓN** `volumen_spike_ratio` < `1.8006` → IC=+0.281 (n=1146)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8006 (IC base=+0.059)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.287 (n=1749)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 46.0 (IC base=+0.059)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.359 (n=2263)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.316)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.318 (n=2553)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.316)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.318 (n=2659)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.316)

- **PATRÓN** `ibs_20min` > `0.6571` → IC=+0.344 (n=2534)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6571 (IC base=+0.316)

- **PATRÓN** `dist_vwap_pct` > `0.2123` → IC=+0.335 (n=1344)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2123 (IC base=+0.316)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.731` → IC=+0.334 (n=1247)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.731 (IC base=+0.316)

- **PATRÓN** `volumen_regimen` > `0.6291` → IC=+0.326 (n=2532)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6291 (IC base=+0.316)

- **PATRÓN** `volumen_pendiente_norm` > `0.2816` → IC=+0.349 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2816 (IC base=+0.316)

- **PATRÓN** `volumen_spike_ratio` > `1.5289` → IC=+0.328 (n=2181)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5289 (IC base=+0.316)

- **PATRÓN** `libro_liquidez` > `2995.3274` → IC=+0.329 (n=844)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2995.3274 (IC base=+0.316)

- **PATRÓN** `ballena_activa_n` < `39.0` → IC=+0.342 (n=2283)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 39.0 (IC base=+0.316)

- **PATRÓN** `sigma_h` > `0.0147` → IC=+0.351 (n=1812)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0147 (IC base=+0.315)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.319 (n=1372)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.315)

- **PATRÓN** `ibs_20min` < `0.3828` → IC=+0.331 (n=2716)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3828 (IC base=+0.315)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.299` → IC=+0.327 (n=502)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.299 (IC base=+0.315)

- **PATRÓN** `volumen_regimen` < `0.7185` → IC=+0.319 (n=1196)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7185 (IC base=+0.315)

- **PATRÓN** `volumen_regimen` > `1.2055` → IC=+0.343 (n=906)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2055 (IC base=+0.315)

- **PATRÓN** `volumen_pendiente_norm` > `0.2833` → IC=+0.368 (n=384)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2833 (IC base=+0.315)

- **PATRÓN** `volumen_spike_ratio` < `1.4127` → IC=+0.322 (n=845)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4127 (IC base=+0.315)

- **PATRÓN** `volumen_spike_ratio` > `2.1403` → IC=+0.317 (n=1149)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1403 (IC base=+0.315)

- **PATRÓN** `libro_liquidez` > `2982.1479` → IC=+0.317 (n=906)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2982.1479 (IC base=+0.315)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.222 (n=5874)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0125 (IC base=+0.172)

- **PATRÓN** `drift_60min` |x|≤ `0.1231` → IC=+0.191 (n=7752)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.1231 (IC base=+0.172)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.184 (n=18290)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.172)

- **PATRÓN** `ibs_20min` > `0.5378` → IC=+0.229 (n=17613)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5378 (IC base=+0.172)

- **PATRÓN** `dist_vwap_pct` > `0.1626` → IC=+0.204 (n=6601)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1626 (IC base=+0.172)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.75` → IC=+0.259 (n=3440)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.75 (IC base=+0.172)

- **PATRÓN** `volumen_regimen` < `1.1752` → IC=+0.152 (n=11735)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.1752 (IC base=+0.172)

- **PATRÓN** `volumen_regimen` > `0.6228` → IC=+0.152 (n=11736)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.6228 (IC base=+0.172)

- **PATRÓN** `volumen_pendiente_norm` > `0.293` → IC=+0.203 (n=2539)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.293 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` > `2.6003` → IC=+0.185 (n=5712)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.6003 (IC base=+0.172)

- **PATRÓN** `ballena_activa_n` < `86.0` → IC=+0.191 (n=16535)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 86.0 (IC base=+0.172)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.192 (n=7668)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0059 (IC base=+0.185)

- **PATRÓN** `sigma_h` > `0.0079` → IC=+0.186 (n=11606)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0079 (IC base=+0.185)

- **PATRÓN** `drift_60min` |x|≤ `0.0817` → IC=+0.223 (n=5804)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0817 (IC base=+0.185)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.212 (n=6537)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.185)

- **PATRÓN** `ibs_20min` < `0.5261` → IC=+0.239 (n=17394)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5261 (IC base=+0.185)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.496` → IC=+0.189 (n=2757)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 9.496 (IC base=+0.185)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.506` → IC=+0.192 (n=15508)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` < 2.506 (IC base=+0.185)

- **PATRÓN** `volumen_regimen` < `1.1836` → IC=+0.165 (n=12367)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.1836 (IC base=+0.185)

- **PATRÓN** `volumen_pendiente_norm` > `0.2939` → IC=+0.220 (n=2609)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2939 (IC base=+0.185)

- **PATRÓN** `volumen_spike_ratio` > `2.6274` → IC=+0.196 (n=5527)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.6274 (IC base=+0.185)

- **PATRÓN** `ballena_activa_n` < `91.0` → IC=+0.200 (n=16396)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 91.0 (IC base=+0.185)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` > `0.0108` → IC=+0.263 (n=968)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0108 (IC base=+0.226)

- **PATRÓN** `drift_60min` |x|≤ `0.1042` → IC=+0.257 (n=1274)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1042 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.233 (n=3013)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.226)

- **PATRÓN** `ibs_20min` > `0.9426` → IC=+0.292 (n=1929)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9426 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.458` → IC=+0.327 (n=947)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.458 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` > `0.2811` → IC=+0.283 (n=436)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2811 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` < `1.8356` → IC=+0.225 (n=1842)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8356 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` > `1.4355` → IC=+0.225 (n=2762)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4355 (IC base=+0.226)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.236 (n=3230)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.226)

- **PATRÓN** `libro_liquidez` > `2035.4848` → IC=+0.226 (n=965)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2035.4848 (IC base=+0.226)

- **PATRÓN** `sigma_h` < `0.01` → IC=+0.258 (n=2382)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.01 (IC base=+0.256)

- **PATRÓN** `sigma_h` > `0.009` → IC=+0.258 (n=1080)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.009 (IC base=+0.256)

- **PATRÓN** `drift_60min` |x|≤ `0.0973` → IC=+0.311 (n=1048)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0973 (IC base=+0.256)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.260 (n=2449)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.256)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.261 (n=2169)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.256)

- **PATRÓN** `ibs_20min` < `0.4408` → IC=+0.274 (n=2379)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4408 (IC base=+0.256)

- **PATRÓN** `volumen_pendiente_norm` < `0.0993` → IC=+0.258 (n=2091)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0993 (IC base=+0.256)

- **PATRÓN** `volumen_pendiente_norm` > `0.3016` → IC=+0.272 (n=358)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3016 (IC base=+0.256)

- **PATRÓN** `volumen_spike_ratio` < `1.4456` → IC=+0.276 (n=761)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4456 (IC base=+0.256)

- **PATRÓN** `volumen_spike_ratio` > `2.6807` → IC=+0.256 (n=761)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6807 (IC base=+0.256)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.266 (n=1713)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.256)

- **PATRÓN** `libro_liquidez` > `1774.3736` → IC=+0.266 (n=1586)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1774.3736 (IC base=+0.256)

- **PATRÓN** `ballena_activa_n` < `7.0` → IC=+0.256 (n=898)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 7.0 (IC base=+0.256)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.196 (n=894)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0032 (IC base=+0.128)

- **PATRÓN** `drift_60min` |x|≤ `0.0648` → IC=+0.177 (n=895)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.0648 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.146 (n=2804)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` > `0.2602` → IC=+0.205 (n=2679)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2602 (IC base=+0.128)

- **PATRÓN** `dist_vwap_pct` > `0.1843` → IC=+0.213 (n=1310)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1843 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.646` → IC=+0.211 (n=490)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.646 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` < `0.6259` → IC=+0.133 (n=895)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 0.6259 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` > `1.0504` → IC=+0.134 (n=1215)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` > 1.0504 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` > `0.279` → IC=+0.167 (n=412)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.279 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` < `1.4059` → IC=+0.134 (n=878)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 1.4059 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` > `2.4602` → IC=+0.147 (n=878)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 2.4602 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `396.0` → IC=+0.132 (n=2606)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 396.0 (IC base=+0.128)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.171 (n=2870)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0066 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.2421` → IC=+0.175 (n=2524)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.2421 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.184 (n=1361)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 15.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` < `0.6093` → IC=+0.210 (n=2868)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6093 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.904` → IC=+0.175 (n=536)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 10.904 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.028` → IC=+0.156 (n=2500)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 4.028 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` < `1.2004` → IC=+0.162 (n=2868)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2004 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` < `0.2281` → IC=+0.154 (n=3043)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` < 0.2281 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `2.4684` → IC=+0.155 (n=2743)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.4684 (IC base=+0.151)

- **PATRÓN** `ballena_activa_n` < `207.0` → IC=+0.198 (n=1177)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 207.0 (IC base=+0.151)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.01` → IC=+0.224 (n=1991)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.01 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.2509` → IC=+0.232 (n=1991)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2509 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.218 (n=3110)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.290 (n=1590)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.04` → IC=+0.306 (n=709)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.04 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` < `0.0983` → IC=+0.210 (n=2604)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0983 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.3511` → IC=+0.241 (n=422)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3511 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `2.7105` → IC=+0.225 (n=1321)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7105 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.214 (n=3613)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `1997.475` → IC=+0.223 (n=995)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1997.475 (IC base=+0.210)

- **PATRÓN** `sigma_h` < `0.0119` → IC=+0.247 (n=2651)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0119 (IC base=+0.240)

- **PATRÓN** `drift_60min` |x|≤ `0.4171` → IC=+0.262 (n=2332)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4171 (IC base=+0.240)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.279 (n=1017)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.240)

- **PATRÓN** `ibs_20min` < `0.0419` → IC=+0.291 (n=1168)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0419 (IC base=+0.240)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.89` → IC=+0.276 (n=346)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.89 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` > `0.3545` → IC=+0.286 (n=443)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3545 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` < `1.7663` → IC=+0.241 (n=1127)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7663 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` > `2.1782` → IC=+0.252 (n=1708)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1782 (IC base=+0.240)

- **PATRÓN** `libro_liquidez` > `1873.0676` → IC=+0.249 (n=1201)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1873.0676 (IC base=+0.240)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.240 (n=1708)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.240)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.197 (n=975)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0038 (IC base=+0.127)

- **PATRÓN** `drift_60min` |x|≤ `0.0787` → IC=+0.182 (n=971)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.0787 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.138 (n=3011)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.127)

- **PATRÓN** `ibs_20min` > `0.2458` → IC=+0.188 (n=2908)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.2458 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` > `0.1399` → IC=+0.184 (n=1643)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.1399 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.231` → IC=+0.200 (n=498)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.231 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` < `0.839` → IC=+0.137 (n=1939)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.839 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` > `0.2874` → IC=+0.168 (n=438)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` > 0.2874 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` < `1.8067` → IC=+0.126 (n=1899)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 1.8067 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` > `2.5066` → IC=+0.138 (n=950)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 2.5066 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `6871.072` → IC=+0.197 (n=1319)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 6871.072 (IC base=+0.127)

- **PATRÓN** `ballena_activa_n` < `125.0` → IC=+0.127 (n=2853)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 125.0 (IC base=+0.127)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.164 (n=2726)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0067 (IC base=+0.131)

- **PATRÓN** `drift_60min` |x|≤ `0.4037` → IC=+0.148 (n=3095)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.4037 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.167 (n=1477)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 15.0 (IC base=+0.131)

- **PATRÓN** `ibs_20min` < `0.6727` → IC=+0.187 (n=3095)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.6727 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.201` → IC=+0.141 (n=738)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 9.201 (IC base=+0.131)

- **PATRÓN** `volumen_regimen` < `0.852` → IC=+0.151 (n=2064)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.852 (IC base=+0.131)

- **PATRÓN** `volumen_pendiente_norm` > `0.2942` → IC=+0.174 (n=458)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.2942 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` < `2.2001` → IC=+0.132 (n=2587)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 2.2001 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` > `1.5162` → IC=+0.133 (n=2626)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 1.5162 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `6363.9352` → IC=+0.192 (n=1403)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 6363.9352 (IC base=+0.131)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.158 (n=978)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 48.0 (IC base=+0.131)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0127` → IC=+0.164 (n=1080)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` > 0.0127 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.134 (n=3325)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 5.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` > `0.4719` → IC=+0.205 (n=3237)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4719 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` > `0.2007` → IC=+0.188 (n=1716)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.2007 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.96` → IC=+0.286 (n=682)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.96 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` < `1.164` → IC=+0.130 (n=3238)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.164 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` < `0.1621` → IC=+0.123 (n=3301)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_pendiente_norm` < 0.1621 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` < `1.7791` → IC=+0.124 (n=2094)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 1.7791 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `2674.0244` → IC=+0.199 (n=1468)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 2674.0244 (IC base=+0.118)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.132 (n=1078)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 16.0 (IC base=+0.118)

- **PATRÓN** `sigma_h` < `0.0119` → IC=+0.144 (n=3388)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0119 (IC base=+0.121)

- **PATRÓN** `drift_60min` |x|≤ `0.1142` → IC=+0.163 (n=1129)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.1142 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.136 (n=3452)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 5.0 (IC base=+0.121)

- **PATRÓN** `ibs_20min` < `0.6489` → IC=+0.220 (n=3386)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6489 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.237` → IC=+0.142 (n=2998)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 2.237 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` < `1.1765` → IC=+0.127 (n=3386)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` < 1.1765 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` > `0.859` → IC=+0.125 (n=2257)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` > 0.859 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` < `0.162` → IC=+0.124 (n=3336)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.162 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` > `0.275` → IC=+0.153 (n=473)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` > 0.275 (IC base=+0.121)

- **PATRÓN** `volumen_spike_ratio` < `1.4338` → IC=+0.139 (n=1069)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.4338 (IC base=+0.121)

- **PATRÓN** `volumen_spike_ratio` > `2.4431` → IC=+0.135 (n=1068)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 2.4431 (IC base=+0.121)

- **PATRÓN** `libro_liquidez` > `2564.2045` → IC=+0.188 (n=1535)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 2564.2045 (IC base=+0.121)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.128 (n=3200)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 44.0 (IC base=+0.121)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0108` → IC=+0.249 (n=2911)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0108 (IC base=+0.227)

- **PATRÓN** `drift_60min` |x|≤ `0.1651` → IC=+0.244 (n=1281)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1651 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.233 (n=3027)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.227)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.230 (n=2623)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.227)

- **PATRÓN** `ibs_20min` > `0.6667` → IC=+0.258 (n=2914)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6667 (IC base=+0.227)

- **PATRÓN** `dist_vwap_pct` > `1.1299` → IC=+0.237 (n=641)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1299 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.529` → IC=+0.257 (n=1335)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.529 (IC base=+0.227)

- **PATRÓN** `volumen_regimen` > `0.6219` → IC=+0.237 (n=2911)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6219 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` > `0.2341` → IC=+0.267 (n=542)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2341 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` < `2.4668` → IC=+0.230 (n=2841)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4668 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` > `1.4318` → IC=+0.232 (n=2841)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4318 (IC base=+0.227)

- **PATRÓN** `libro_liquidez` > `2595.188` → IC=+0.231 (n=1941)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2595.188 (IC base=+0.227)

- **PATRÓN** `sigma_h` < `0.0124` → IC=+0.243 (n=1329)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0124 (IC base=+0.241)

- **PATRÓN** `sigma_h` > `0.0173` → IC=+0.244 (n=2013)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0173 (IC base=+0.241)

- **PATRÓN** `drift_60min` |x|≤ `0.5892` → IC=+0.250 (n=3019)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5892 (IC base=+0.241)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.252 (n=1476)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.241)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.247 (n=1357)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.241)

- **PATRÓN** `ibs_20min` < `0.0385` → IC=+0.300 (n=1331)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0385 (IC base=+0.241)

- **PATRÓN** `dist_vwap_pct` > `1.1322` → IC=+0.263 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1322 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.119` → IC=+0.269 (n=578)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.119 (IC base=+0.241)

- **PATRÓN** `volumen_regimen` < `0.869` → IC=+0.243 (n=2013)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.869 (IC base=+0.241)

- **PATRÓN** `volumen_regimen` > `0.6411` → IC=+0.242 (n=3019)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6411 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` > `0.2811` → IC=+0.293 (n=418)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2811 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` < `2.5149` → IC=+0.239 (n=2854)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5149 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` > `1.5489` → IC=+0.242 (n=2549)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5489 (IC base=+0.241)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.210 (n=1526)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.157)

- **PATRÓN** `drift_60min` |x|≤ `0.1355` → IC=+0.171 (n=2011)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.1355 (IC base=+0.157)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.170 (n=4760)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 5.0 (IC base=+0.157)

- **PATRÓN** `ibs_20min` > `0.425` → IC=+0.203 (n=4085)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.425 (IC base=+0.157)

- **PATRÓN** `dist_vwap_pct` > `0.223` → IC=+0.177 (n=1708)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.223 (IC base=+0.157)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.516` → IC=+0.209 (n=752)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.516 (IC base=+0.157)

- **PATRÓN** `volumen_regimen` < `0.8606` → IC=+0.167 (n=2751)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.8606 (IC base=+0.157)

- **PATRÓN** `volumen_regimen` > `1.1957` → IC=+0.164 (n=1375)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 1.1957 (IC base=+0.157)

- **PATRÓN** `volumen_pendiente_norm` > `0.1569` → IC=+0.174 (n=1202)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.1569 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` < `1.5279` → IC=+0.161 (n=1962)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 1.5279 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` > `1.8094` → IC=+0.161 (n=2972)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.8094 (IC base=+0.157)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.158 (n=3921)

  - _Acción_: Kelly boost +0.79€ cuando `libro_spread` < 0.01 (IC base=+0.157)

- **PATRÓN** `libro_liquidez` > `7408.8356` → IC=+0.186 (n=2072)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 7408.8356 (IC base=+0.157)

- **PATRÓN** `ibs_20min` < `0.3824` → IC=+0.176 (n=3327)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.3824 (IC base=+0.098)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.139 (n=2178)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 23.0 (IC base=+0.098)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.197 (n=1148)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0061 (IC base=+0.184)

- **PATRÓN** `drift_60min` |x|≤ `0.3302` → IC=+0.199 (n=1149)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3302 (IC base=+0.184)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.217 (n=1035)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.184)

- **PATRÓN** `ibs_20min` > `0.7998` → IC=+0.236 (n=521)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7998 (IC base=+0.184)

- **PATRÓN** `dist_vwap_pct` > `0.3093` → IC=+0.218 (n=346)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3093 (IC base=+0.184)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.946` → IC=+0.213 (n=506)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.946 (IC base=+0.184)

- **PATRÓN** `volumen_regimen` < `0.6292` → IC=+0.207 (n=384)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6292 (IC base=+0.184)

- **PATRÓN** `volumen_pendiente_norm` < `0.2153` → IC=+0.188 (n=1292)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` < 0.2153 (IC base=+0.184)

- **PATRÓN** `volumen_pendiente_norm` > `0.0913` → IC=+0.200 (n=398)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0913 (IC base=+0.184)

- **PATRÓN** `volumen_spike_ratio` < `2.1675` → IC=+0.198 (n=991)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 2.1675 (IC base=+0.184)

- **PATRÓN** `libro_liquidez` > `13750.9538` → IC=+0.192 (n=765)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 13750.9538 (IC base=+0.184)

- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.161 (n=481)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0031 (IC base=+0.080)

- **PATRÓN** `ibs_20min` < `0.2085` → IC=+0.197 (n=632)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.2085 (IC base=+0.080)

- **PATRÓN** `ballena_activa_n` < `165.0` → IC=+0.174 (n=618)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 165.0 (IC base=+0.080)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.233 (n=608)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.154)

- **PATRÓN** `drift_60min` |x|≤ `0.2106` → IC=+0.157 (n=919)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.2106 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.174 (n=1426)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 5.0 (IC base=+0.154)

- **PATRÓN** `ibs_20min` > `0.7838` → IC=+0.267 (n=625)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7838 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` > `0.821` → IC=+0.193 (n=223)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.821 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.907` → IC=+0.206 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.907 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` < `0.8322` → IC=+0.165 (n=919)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8322 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` > `0.2192` → IC=+0.198 (n=250)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2192 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` > `1.7829` → IC=+0.172 (n=906)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 1.7829 (IC base=+0.154)

- **PATRÓN** `libro_liquidez` > `7992.687` → IC=+0.178 (n=625)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 7992.687 (IC base=+0.154)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.127 (n=901)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.63€ cuando `sigma_h` < 0.0053 (IC base=+0.095)

- **PATRÓN** `ibs_20min` < `0.0867` → IC=+0.213 (n=451)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0867 (IC base=+0.095)

- **PATRÓN** `volumen_regimen` < `0.6774` → IC=+0.132 (n=595)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 0.6774 (IC base=+0.095)

- **PATRÓN** `libro_liquidez` > `7883.4537` → IC=+0.153 (n=612)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 7883.4537 (IC base=+0.095)

- **PATRÓN** `ballena_activa_n` < `61.0` → IC=+0.122 (n=871)

  - _Acción_: Kelly boost +0.61€ cuando `ballena_activa_n` < 61.0 (IC base=+0.095)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` < `0.0093` → IC=+0.144 (n=784)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0093 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.161 (n=820)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 11.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` > `0.5385` → IC=+0.190 (n=1049)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.5385 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` > `0.936` → IC=+0.163 (n=191)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.936 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.857` → IC=+0.223 (n=457)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.857 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` < `1.0461` → IC=+0.133 (n=1033)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 1.0461 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` > `0.6997` → IC=+0.127 (n=1049)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` > 0.6997 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` > `0.224` → IC=+0.149 (n=206)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.224 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` < `1.4125` → IC=+0.147 (n=380)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.4125 (IC base=+0.120)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.120 (n=1236)

  - _Acción_: Kelly boost +0.60€ cuando `libro_spread` < 0.02 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `2751.7394` → IC=+0.162 (n=533)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 2751.7394 (IC base=+0.120)

- **PATRÓN** `ibs_20min` < `0.55` → IC=+0.163 (n=1152)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` < 0.55 (IC base=+0.081)

- **PATRÓN** `libro_liquidez` > `2631.0579` → IC=+0.166 (n=594)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2631.0579 (IC base=+0.081)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0157` → IC=+0.241 (n=284)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0157 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.224 (n=201)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.188)

- **PATRÓN** `ibs_20min` > `0.9524` → IC=+0.208 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9524 (IC base=+0.188)

- **PATRÓN** `dist_vwap_pct` > `0.2434` → IC=+0.196 (n=218)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.2434 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.53` → IC=+0.202 (n=424)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.53 (IC base=+0.188)

- **PATRÓN** `volumen_regimen` > `1.224` → IC=+0.264 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.224 (IC base=+0.188)

- **PATRÓN** `volumen_pendiente_norm` > `0.0802` → IC=+0.219 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0802 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` < `2.1265` → IC=+0.199 (n=350)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 2.1265 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` > `1.4093` → IC=+0.203 (n=398)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4093 (IC base=+0.188)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.201 (n=449)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.188)

- **PATRÓN** `libro_liquidez` > `2724.4103` → IC=+0.217 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2724.4103 (IC base=+0.188)

- **PATRÓN** `sigma_h` > `0.0105` → IC=+0.172 (n=471)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0105 (IC base=+0.152)

- **PATRÓN** `drift_60min` |x|≤ `0.5234` → IC=+0.159 (n=414)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.5234 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.194 (n=230)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 15.0 (IC base=+0.152)

- **PATRÓN** `ibs_20min` < `0.3404` → IC=+0.158 (n=314)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.3404 (IC base=+0.152)

- **PATRÓN** `ibs_20min` > `0.0991` → IC=+0.158 (n=471)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` > 0.0991 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` > `1.1744` → IC=+0.275 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1744 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.969` → IC=+0.153 (n=119)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 4.969 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.987` → IC=+0.153 (n=453)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` < 2.987 (IC base=+0.152)

- **PATRÓN** `volumen_regimen` < `1.2424` → IC=+0.172 (n=471)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` < 1.2424 (IC base=+0.152)

- **PATRÓN** `volumen_pendiente_norm` < `0.1126` → IC=+0.167 (n=433)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` < 0.1126 (IC base=+0.152)

- **PATRÓN** `volumen_pendiente_norm` > `0.2348` → IC=+0.193 (n=86)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2348 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` < `1.4819` → IC=+0.201 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4819 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` > `2.6321` → IC=+0.160 (n=151)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 2.6321 (IC base=+0.152)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.167 (n=455)

  - _Acción_: Kelly boost +0.84€ cuando `ballena_activa_n` < 20.0 (IC base=+0.152)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.229 (n=7726)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0125 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.191 (n=24144)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 5.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` > `0.4286` → IC=+0.227 (n=23159)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4286 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` > `0.8853` → IC=+0.213 (n=2666)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8853 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.933` → IC=+0.259 (n=5684)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.933 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `1.2127` → IC=+0.160 (n=15595)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2127 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.2406` → IC=+0.209 (n=4154)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2406 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `2.6236` → IC=+0.193 (n=7539)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.6236 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `102.0` → IC=+0.201 (n=21812)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 102.0 (IC base=+0.181)

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.199 (n=7125)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.197)

- **PATRÓN** `sigma_h` > `0.0122` → IC=+0.207 (n=7120)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0122 (IC base=+0.197)

- **PATRÓN** `drift_60min` |x|≤ `0.147` → IC=+0.203 (n=9395)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.147 (IC base=+0.197)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.216 (n=7997)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.197)

- **PATRÓN** `ibs_20min` < `0.5928` → IC=+0.244 (n=21348)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5928 (IC base=+0.197)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.521` → IC=+0.203 (n=19847)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.521 (IC base=+0.197)

- **PATRÓN** `volumen_regimen` < `0.7006` → IC=+0.176 (n=6308)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.7006 (IC base=+0.197)

- **PATRÓN** `volumen_pendiente_norm` > `0.2929` → IC=+0.255 (n=2933)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2929 (IC base=+0.197)

- **PATRÓN** `volumen_spike_ratio` > `2.6247` → IC=+0.211 (n=6824)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6247 (IC base=+0.197)

- **PATRÓN** `ballena_activa_n` < `90.0` → IC=+0.213 (n=20223)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 90.0 (IC base=+0.197)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` > `0.0109` → IC=+0.276 (n=1234)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0109 (IC base=+0.235)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.253 (n=1791)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.235)

- **PATRÓN** `ibs_20min` > `0.8632` → IC=+0.296 (n=2467)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8632 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.828` → IC=+0.342 (n=883)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.828 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` > `0.2325` → IC=+0.287 (n=661)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2325 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` > `2.2913` → IC=+0.242 (n=1621)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2913 (IC base=+0.235)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.249 (n=4095)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.235)

- **PATRÓN** `libro_liquidez` > `2028.3148` → IC=+0.238 (n=1233)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2028.3148 (IC base=+0.235)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.250 (n=2294)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 14.0 (IC base=+0.235)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.269 (n=3321)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0103 (IC base=+0.268)

- **PATRÓN** `sigma_h` > `0.0093` → IC=+0.269 (n=1510)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0093 (IC base=+0.268)

- **PATRÓN** `drift_60min` |x|≤ `0.1233` → IC=+0.295 (n=1461)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1233 (IC base=+0.268)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.269 (n=3442)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.268)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.271 (n=2998)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.268)

- **PATRÓN** `ibs_20min` < `0.5508` → IC=+0.286 (n=3319)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5508 (IC base=+0.268)

- **PATRÓN** `volumen_pendiente_norm` < `0.0977` → IC=+0.270 (n=3020)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0977 (IC base=+0.268)

- **PATRÓN** `volumen_pendiente_norm` > `0.2898` → IC=+0.289 (n=457)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2898 (IC base=+0.268)

- **PATRÓN** `volumen_spike_ratio` < `1.5653` → IC=+0.272 (n=1403)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5653 (IC base=+0.268)

- **PATRÓN** `volumen_spike_ratio` > `2.6442` → IC=+0.280 (n=1063)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6442 (IC base=+0.268)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.274 (n=2378)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.268)

- **PATRÓN** `libro_liquidez` > `1774.82` → IC=+0.276 (n=2212)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1774.82 (IC base=+0.268)

- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.278 (n=1206)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 8.0 (IC base=+0.268)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.177 (n=1273)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0032 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.0794` → IC=+0.147 (n=1267)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.0794 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.151 (n=3956)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 5.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` > `0.1948` → IC=+0.187 (n=3796)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.1948 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` > `0.3231` → IC=+0.199 (n=1193)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.3231 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.333` → IC=+0.168 (n=792)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 9.333 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `0.6354` → IC=+0.155 (n=1266)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.6354 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` > `1.0679` → IC=+0.144 (n=1721)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 1.0679 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.2712` → IC=+0.185 (n=535)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.2712 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `2.1695` → IC=+0.142 (n=3282)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.1695 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `1.5162` → IC=+0.144 (n=3332)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.5162 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `296.0` → IC=+0.153 (n=2453)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 296.0 (IC base=+0.138)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.163 (n=3302)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0065 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.0803` → IC=+0.169 (n=1102)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.0803 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.171 (n=1214)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` < `0.678` → IC=+0.187 (n=3301)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.678 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.005` → IC=+0.143 (n=2985)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 4.005 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `1.0421` → IC=+0.153 (n=2905)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.0421 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.2202` → IC=+0.193 (n=610)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2202 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `2.4301` → IC=+0.146 (n=3191)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 2.4301 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `1.769` → IC=+0.145 (n=2127)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.769 (IC base=+0.140)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.141 (n=4291)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `220.0` → IC=+0.164 (n=1047)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 220.0 (IC base=+0.140)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0132` → IC=+0.244 (n=1287)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0132 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.236 (n=4043)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.226)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.226 (n=3452)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.226)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.301 (n=1439)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.981` → IC=+0.320 (n=861)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.981 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` < `0.1319` → IC=+0.227 (n=3662)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1319 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` > `0.3503` → IC=+0.232 (n=506)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3503 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` > `2.7506` → IC=+0.243 (n=1712)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7506 (IC base=+0.226)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.232 (n=4668)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.226)

- **PATRÓN** `libro_liquidez` > `2006.7416` → IC=+0.240 (n=1286)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2006.7416 (IC base=+0.226)

- **PATRÓN** `sigma_h` < `0.0111` → IC=+0.250 (n=3257)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0111 (IC base=+0.245)

- **PATRÓN** `drift_60min` |x|≤ `0.1797` → IC=+0.262 (n=1627)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1797 (IC base=+0.245)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.264 (n=1410)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.245)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.248 (n=1691)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.245)

- **PATRÓN** `ibs_20min` < `0.0625` → IC=+0.303 (n=1238)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0625 (IC base=+0.245)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.023` → IC=+0.304 (n=386)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.023 (IC base=+0.245)

- **PATRÓN** `volumen_pendiente_norm` > `0.3484` → IC=+0.303 (n=557)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3484 (IC base=+0.245)

- **PATRÓN** `volumen_spike_ratio` > `2.1737` → IC=+0.257 (n=2377)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1737 (IC base=+0.245)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.250 (n=1871)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.245)

- **PATRÓN** `libro_liquidez` > `1981.9661` → IC=+0.257 (n=1232)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1981.9661 (IC base=+0.245)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.250 (n=3098)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 21.0 (IC base=+0.245)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.194 (n=1339)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0038 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.3382` → IC=+0.148 (n=3528)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.3382 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.151 (n=4157)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 5.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` > `0.8826` → IC=+0.270 (n=1337)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8826 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` > `0.1967` → IC=+0.168 (n=1770)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.1967 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.069` → IC=+0.168 (n=606)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 11.069 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `0.8574` → IC=+0.155 (n=2673)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.8574 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.2323` → IC=+0.190 (n=708)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.2323 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `1.5155` → IC=+0.154 (n=1725)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 1.5155 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `2.1602` → IC=+0.142 (n=1777)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 2.1602 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `7295.1819` → IC=+0.241 (n=1336)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7295.1819 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `86.0` → IC=+0.146 (n=2588)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 86.0 (IC base=+0.138)

- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.171 (n=2963)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0068 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.4435` → IC=+0.159 (n=3367)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.4435 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.175 (n=1243)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 17.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` < `0.7057` → IC=+0.199 (n=3368)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.7057 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.007` → IC=+0.151 (n=665)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 9.007 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.029` → IC=+0.153 (n=2942)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` < 3.029 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `0.8558` → IC=+0.160 (n=2245)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.8558 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` > `0.2941` → IC=+0.213 (n=426)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2941 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `2.2041` → IC=+0.152 (n=2864)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.2041 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` > `1.5255` → IC=+0.155 (n=2908)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.5255 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `6575.9455` → IC=+0.222 (n=1122)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6575.9455 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `57.0` → IC=+0.173 (n=1101)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 57.0 (IC base=+0.148)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0127` → IC=+0.153 (n=1362)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` > 0.0127 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.148 (n=2873)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 11.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` > `0.4286` → IC=+0.188 (n=4081)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.4286 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` > `1.0102` → IC=+0.201 (n=654)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0102 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.234` → IC=+0.273 (n=1034)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.234 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` < `0.8739` → IC=+0.133 (n=2717)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 0.8739 (IC base=+0.117)

- **PATRÓN** `volumen_pendiente_norm` < `0.1006` → IC=+0.121 (n=3867)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_pendiente_norm` < 0.1006 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` < `2.4914` → IC=+0.121 (n=3975)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` < 2.4914 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `2724.2301` → IC=+0.242 (n=1357)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2724.2301 (IC base=+0.117)

- **PATRÓN** `sigma_h` < `0.0109` → IC=+0.156 (n=3365)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0109 (IC base=+0.132)

- **PATRÓN** `drift_60min` |x|≤ `0.1396` → IC=+0.155 (n=1273)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.1396 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.167 (n=1801)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 15.0 (IC base=+0.132)

- **PATRÓN** `ibs_20min` < `0.6667` → IC=+0.219 (n=3835)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6667 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.042` → IC=+0.154 (n=3698)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 3.042 (IC base=+0.132)

- **PATRÓN** `volumen_regimen` < `0.6385` → IC=+0.151 (n=1272)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.6385 (IC base=+0.132)

- **PATRÓN** `volumen_pendiente_norm` > `0.2291` → IC=+0.196 (n=673)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2291 (IC base=+0.132)

- **PATRÓN** `volumen_spike_ratio` < `1.4377` → IC=+0.162 (n=1211)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 1.4377 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `2623.7268` → IC=+0.215 (n=1272)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2623.7268 (IC base=+0.132)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.144 (n=3644)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 49.0 (IC base=+0.132)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.260 (n=3722)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0113 (IC base=+0.239)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.246 (n=3890)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.239)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.242 (n=3334)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.239)

- **PATRÓN** `ibs_20min` > `0.6142` → IC=+0.272 (n=3324)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6142 (IC base=+0.239)

- **PATRÓN** `dist_vwap_pct` > `0.1962` → IC=+0.253 (n=1882)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1962 (IC base=+0.239)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.11` → IC=+0.288 (n=654)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.11 (IC base=+0.239)

- **PATRÓN** `volumen_regimen` < `1.2171` → IC=+0.240 (n=3721)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2171 (IC base=+0.239)

- **PATRÓN** `volumen_regimen` > `0.6435` → IC=+0.245 (n=3721)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6435 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` > `0.2393` → IC=+0.255 (n=646)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2393 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` > `2.5001` → IC=+0.257 (n=1214)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5001 (IC base=+0.239)

- **PATRÓN** `libro_liquidez` > `2986.2232` → IC=+0.247 (n=1241)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2986.2232 (IC base=+0.239)

- **PATRÓN** `sigma_h` > `0.0255` → IC=+0.268 (n=1286)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0255 (IC base=+0.244)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.249 (n=3624)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.244)

- **PATRÓN** `ibs_20min` < `0.1398` → IC=+0.308 (n=1697)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1398 (IC base=+0.244)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.066` → IC=+0.277 (n=733)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.066 (IC base=+0.244)

- **PATRÓN** `volumen_regimen` < `0.7156` → IC=+0.247 (n=1697)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7156 (IC base=+0.244)

- **PATRÓN** `volumen_regimen` > `1.2134` → IC=+0.264 (n=1285)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2134 (IC base=+0.244)

- **PATRÓN** `volumen_pendiente_norm` > `0.2859` → IC=+0.310 (n=530)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2859 (IC base=+0.244)

- **PATRÓN** `volumen_spike_ratio` > `1.4328` → IC=+0.248 (n=3643)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4328 (IC base=+0.244)

- **PATRÓN** `libro_liquidez` > `2974.2994` → IC=+0.248 (n=1285)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2974.2994 (IC base=+0.244)

### GBM_LATE_5M
- **PATRÓN** `sigma_h` < `0.0105` → IC=+0.231 (n=5959)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0105 (IC base=+0.223)

- **PATRÓN** `drift_60min` |x|≤ `0.5209` → IC=+0.232 (n=6772)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5209 (IC base=+0.223)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.230 (n=6822)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.223)

- **PATRÓN** `ibs_20min` > `0.9286` → IC=+0.259 (n=2257)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9286 (IC base=+0.223)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.577` → IC=+0.229 (n=3375)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.577 (IC base=+0.223)

- **PATRÓN** `volumen_regimen` < `0.7035` → IC=+0.232 (n=2131)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7035 (IC base=+0.223)

- **PATRÓN** `volumen_regimen` > `0.8773` → IC=+0.223 (n=3227)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8773 (IC base=+0.223)

- **PATRÓN** `volumen_pendiente_norm` < `0.1043` → IC=+0.224 (n=6334)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1043 (IC base=+0.223)

- **PATRÓN** `volumen_pendiente_norm` > `0.1649` → IC=+0.231 (n=1906)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1649 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` < `2.2575` → IC=+0.228 (n=5865)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.2575 (IC base=+0.223)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.227 (n=4895)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.223)

- **PATRÓN** `libro_liquidez` > `3703.1952` → IC=+0.230 (n=4514)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3703.1952 (IC base=+0.223)

- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.239 (n=1531)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.202)

- **PATRÓN** `drift_60min` |x|≤ `0.5018` → IC=+0.214 (n=4575)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5018 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.209 (n=1765)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.202)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.215 (n=2066)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.202)

- **PATRÓN** `ibs_20min` < `0.1842` → IC=+0.214 (n=2013)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1842 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` > `0.6725` → IC=+0.212 (n=752)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6725 (IC base=+0.202)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.758` → IC=+0.215 (n=4124)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.758 (IC base=+0.202)

- **PATRÓN** `volumen_regimen` < `1.0964` → IC=+0.208 (n=3815)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0964 (IC base=+0.202)

- **PATRÓN** `volumen_pendiente_norm` < `0.0979` → IC=+0.203 (n=4219)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0979 (IC base=+0.202)

- **PATRÓN** `volumen_pendiente_norm` > `0.0733` → IC=+0.205 (n=2039)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0733 (IC base=+0.202)

- **PATRÓN** `volumen_spike_ratio` < `1.5329` → IC=+0.206 (n=1985)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5329 (IC base=+0.202)

- **PATRÓN** `volumen_spike_ratio` > `2.1931` → IC=+0.211 (n=2046)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1931 (IC base=+0.202)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.203 (n=6030)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.202)

- **PATRÓN** `ballena_activa_n` < `30.0` → IC=+0.227 (n=1989)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 30.0 (IC base=+0.202)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.277 (n=817)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0057 (IC base=+0.270)

- **PATRÓN** `sigma_h` > `0.0033` → IC=+0.272 (n=928)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0033 (IC base=+0.270)

- **PATRÓN** `drift_60min` |x|≤ `0.0849` → IC=+0.298 (n=310)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0849 (IC base=+0.270)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.277 (n=985)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.270)

- **PATRÓN** `ibs_20min` < `0.8318` → IC=+0.279 (n=928)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.8318 (IC base=+0.270)

- **PATRÓN** `dist_vwap_pct` < `0.6688` → IC=+0.278 (n=1079)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6688 (IC base=+0.270)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.118` → IC=+0.300 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.118 (IC base=+0.270)

- **PATRÓN** `volumen_regimen` < `1.2246` → IC=+0.272 (n=928)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2246 (IC base=+0.270)

- **PATRÓN** `volumen_regimen` > `0.8769` → IC=+0.291 (n=619)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8769 (IC base=+0.270)

- **PATRÓN** `volumen_pendiente_norm` > `0.2881` → IC=+0.351 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2881 (IC base=+0.270)

- **PATRÓN** `volumen_spike_ratio` < `2.4871` → IC=+0.277 (n=924)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4871 (IC base=+0.270)

- **PATRÓN** `volumen_spike_ratio` > `2.189` → IC=+0.270 (n=419)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.189 (IC base=+0.270)

- **PATRÓN** `libro_liquidez` > `12915.1097` → IC=+0.279 (n=619)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12915.1097 (IC base=+0.270)

- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.263 (n=509)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0032 (IC base=+0.175)

- **PATRÓN** `drift_60min` |x|≤ `0.3854` → IC=+0.188 (n=1523)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.3854 (IC base=+0.175)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.216 (n=557)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.175)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.180 (n=570)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 5.0 (IC base=+0.175)

- **PATRÓN** `ibs_20min` < `0.1382` → IC=+0.197 (n=671)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.1382 (IC base=+0.175)

- **PATRÓN** `dist_vwap_pct` > `0.6955` → IC=+0.197 (n=140)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.6955 (IC base=+0.175)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.86` → IC=+0.187 (n=1760)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` < 10.86 (IC base=+0.175)

- **PATRÓN** `volumen_regimen` < `1.091` → IC=+0.188 (n=1340)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 1.091 (IC base=+0.175)

- **PATRÓN** `volumen_pendiente_norm` < `0.2705` → IC=+0.177 (n=1798)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` < 0.2705 (IC base=+0.175)

- **PATRÓN** `volumen_pendiente_norm` > `0.1518` → IC=+0.194 (n=466)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.1518 (IC base=+0.175)

- **PATRÓN** `volumen_spike_ratio` < `1.4122` → IC=+0.194 (n=505)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 1.4122 (IC base=+0.175)

- **PATRÓN** `volumen_spike_ratio` > `1.8038` → IC=+0.179 (n=1010)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` > 1.8038 (IC base=+0.175)

- **PATRÓN** `libro_liquidez` > `14605.0565` → IC=+0.177 (n=691)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 14605.0565 (IC base=+0.175)

- **PATRÓN** `ballena_activa_n` < `691.0` → IC=+0.187 (n=1479)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 691.0 (IC base=+0.175)

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
- **PATRÓN** `sigma_h` < `0.0083` → IC=+0.221 (n=1826)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0083 (IC base=+0.208)

- **PATRÓN** `drift_60min` |x|≤ `0.4578` → IC=+0.216 (n=1826)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4578 (IC base=+0.208)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.233 (n=638)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.208)

- **PATRÓN** `ibs_20min` < `0.4751` → IC=+0.218 (n=1219)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4751 (IC base=+0.208)

- **PATRÓN** `ibs_20min` > `0.1447` → IC=+0.211 (n=1826)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1447 (IC base=+0.208)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.379` → IC=+0.215 (n=1851)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 6.379 (IC base=+0.208)

- **PATRÓN** `volumen_regimen` < `0.8664` → IC=+0.217 (n=1218)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8664 (IC base=+0.208)

- **PATRÓN** `volumen_pendiente_norm` < `0.1019` → IC=+0.212 (n=1684)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1019 (IC base=+0.208)

- **PATRÓN** `volumen_pendiente_norm` > `0.1614` → IC=+0.209 (n=528)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1614 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` < `1.403` → IC=+0.227 (n=596)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.403 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` > `1.4939` → IC=+0.210 (n=1596)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4939 (IC base=+0.208)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.208 (n=1812)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.208)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.242 (n=479)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.200)

- **PATRÓN** `drift_60min` |x|≤ `0.49` → IC=+0.220 (n=1431)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.49 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.205 (n=533)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.200)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.214 (n=974)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.200)

- **PATRÓN** `ibs_20min` < `0.3937` → IC=+0.201 (n=954)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3937 (IC base=+0.200)

- **PATRÓN** `ibs_20min` > `0.612` → IC=+0.208 (n=649)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.612 (IC base=+0.200)

- **PATRÓN** `dist_vwap_pct` > `0.6286` → IC=+0.218 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6286 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.266` → IC=+0.204 (n=1307)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.266 (IC base=+0.200)

- **PATRÓN** `volumen_regimen` < `1.2516` → IC=+0.208 (n=1431)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2516 (IC base=+0.200)

- **PATRÓN** `volumen_regimen` > `0.7214` → IC=+0.200 (n=1278)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7214 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` > `0.0733` → IC=+0.225 (n=588)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0733 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` < `2.1859` → IC=+0.203 (n=1235)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1859 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` > `1.7864` → IC=+0.203 (n=935)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7864 (IC base=+0.200)

- **PATRÓN** `libro_liquidez` > `6544.3683` → IC=+0.208 (n=1278)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6544.3683 (IC base=+0.200)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.240 (n=513)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0084 (IC base=+0.214)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.245 (n=1043)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.214)

- **PATRÓN** `ibs_20min` > `0.9855` → IC=+0.290 (n=388)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9855 (IC base=+0.214)

- **PATRÓN** `dist_vwap_pct` > `0.8142` → IC=+0.238 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8142 (IC base=+0.214)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.173` → IC=+0.244 (n=632)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.173 (IC base=+0.214)

- **PATRÓN** `volumen_regimen` < `0.7016` → IC=+0.246 (n=513)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7016 (IC base=+0.214)

- **PATRÓN** `volumen_pendiente_norm` < `0.1039` → IC=+0.219 (n=1062)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1039 (IC base=+0.214)

- **PATRÓN** `volumen_pendiente_norm` > `0.273` → IC=+0.228 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.273 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` < `2.1734` → IC=+0.225 (n=998)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1734 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` > `1.4699` → IC=+0.216 (n=1134)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4699 (IC base=+0.214)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.224 (n=1370)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.214)

- **PATRÓN** `libro_liquidez` > `4364.3329` → IC=+0.254 (n=388)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4364.3329 (IC base=+0.214)

- **PATRÓN** `sigma_h` > `0.0102` → IC=+0.253 (n=529)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0102 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.6329` → IC=+0.247 (n=794)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6329 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.234 (n=732)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.234)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.259 (n=559)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` < `0.64` → IC=+0.259 (n=700)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.64 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.913` → IC=+0.253 (n=742)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.913 (IC base=+0.234)

- **PATRÓN** `volumen_regimen` < `0.7544` → IC=+0.239 (n=350)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7544 (IC base=+0.234)

- **PATRÓN** `volumen_regimen` > `1.2815` → IC=+0.242 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2815 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` < `0.0816` → IC=+0.246 (n=674)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0816 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.2075` → IC=+0.263 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2075 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `3861.429` → IC=+0.253 (n=529)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3861.429 (IC base=+0.234)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.270 (n=693)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 34.0 (IC base=+0.234)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.150 (n=778)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0038 (IC base=+0.054)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.185 (n=1485)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.75 (IC base=+0.054)

- **PATRÓN** `dist_vwap_pct` > `0.1469` → IC=+0.142 (n=1077)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.1469 (IC base=+0.054)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.347` → IC=+0.142 (n=493)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 10.347 (IC base=+0.054)

- **PATRÓN** `ibs_20min` < `0.0659` → IC=+0.259 (n=695)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0659 (IC base=+0.052)

- **PATRÓN** `volumen_pendiente_norm` > `0.1474` → IC=+0.137 (n=428)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_pendiente_norm` > 0.1474 (IC base=+0.052)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.128 (n=646)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.64€ cuando `sigma_h` < 0.0054 (IC base=+0.070)

- **PATRÓN** `ibs_20min` > `0.5427` → IC=+0.164 (n=628)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` > 0.5427 (IC base=+0.070)

- **PATRÓN** `dist_vwap_pct` > `0.1218` → IC=+0.169 (n=324)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.1218 (IC base=+0.070)

- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.132 (n=283)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.66€ cuando `sigma_h` < 0.0035 (IC base=+0.044)

- **PATRÓN** `ibs_20min` < `0.0659` → IC=+0.248 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0659 (IC base=+0.044)

- **PATRÓN** `volumen_pendiente_norm` > `0.2172` → IC=+0.148 (n=126)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.2172 (IC base=+0.044)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` > `0.6649` → IC=-0.153 (n=165)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6649
  - _Potencial_: sin este filtro IC_bueno=+0.111 (n=497)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.152 (n=331)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0042 (IC base=+0.068)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.122 (n=376)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 15.0 (IC base=+0.068)

- **PATRÓN** `ibs_20min` > `0.5241` → IC=+0.166 (n=644)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.5241 (IC base=+0.068)

- **PATRÓN** `dist_vwap_pct` > `0.129` → IC=+0.169 (n=342)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.129 (IC base=+0.068)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.613` → IC=+0.203 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.613 (IC base=+0.068)

- **PATRÓN** `volumen_pendiente_norm` > `0.2815` → IC=+0.150 (n=101)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.2815 (IC base=+0.068)

- **PATRÓN** `ibs_20min` < `0.1087` → IC=+0.260 (n=219)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1087 (IC base=+0.030)

### GBM_LATE_60M#SOL#60min
- **PATRÓN** `ibs_20min` > `0.72` → IC=+0.138 (n=537)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` > 0.72 (IC base=+0.027)

- **PATRÓN** `dist_vwap_pct` > `0.728` → IC=+0.142 (n=185)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.728 (IC base=+0.027)

- **PATRÓN** `sigma_h` < `0.0097` → IC=+0.183 (n=332)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0097 (IC base=+0.085)

- **PATRÓN** `ibs_20min` < `0.4857` → IC=+0.188 (n=466)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.4857 (IC base=+0.085)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.841` → IC=+0.304 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.841 (IC base=+0.085)

- **PATRÓN** `volumen_regimen` > `1.1082` → IC=+0.194 (n=155)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` > 1.1082 (IC base=+0.085)

- **PATRÓN** `volumen_pendiente_norm` > `0.0818` → IC=+0.160 (n=198)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.0818 (IC base=+0.085)

- **PATRÓN** `volumen_spike_ratio` > `2.5569` → IC=+0.153 (n=145)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 2.5569 (IC base=+0.085)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.127 (n=218)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.03 (IC base=+0.085)

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

- **FILTRO** `libro_liquidez` < `903.3651` → IC=-0.235 (n=96)

  - _Acción_: SKIP cuando `libro_liquidez` < 903.3651
  - _Potencial_: sin este filtro IC_bueno=-0.223 (n=290)

- **FILTRO** `hora_utc` > `11.0` → IC=-0.309 (n=150)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=186)

- **FILTRO** `ibs_20min` > `0.6985` → IC=-0.310 (n=114)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6985
  - _Potencial_: sin este filtro IC_bueno=-0.259 (n=222)

- **FILTRO** `dist_vwap_pct` > `0.4428` → IC=-0.409 (n=20)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4428
  - _Potencial_: sin este filtro IC_bueno=-0.267 (n=316)

- **FILTRO** `sigma_ewma_delta_pct` > `9.697` → IC=-0.328 (n=27)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 9.697
  - _Potencial_: sin este filtro IC_bueno=-0.272 (n=309)

- **FILTRO** `volumen_pendiente_norm` > `0.0453` → IC=-0.375 (n=30)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0453
  - _Potencial_: sin este filtro IC_bueno=-0.260 (n=215)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `hora_utc` > `9.0` → IC=-0.293 (n=27)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.230 (n=87)

- **FILTRO** `sigma_ewma_delta_pct` > `9.679` → IC=-0.250 (n=18)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 9.679
  - _Potencial_: sin este filtro IC_bueno=-0.245 (n=96)

- **FILTRO** `volumen_spike_ratio` < `1.6757` → IC=-0.292 (n=22)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.6757
  - _Potencial_: sin este filtro IC_bueno=-0.218 (n=69)

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

- **FILTRO** `ibs_20min` < `0.5872` → IC=-0.471 (n=33)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5872
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=99)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.368 (n=36)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.279 (n=93)

- **FILTRO** `ibs_20min` > `0.681` → IC=-0.389 (n=43)

  - _Acción_: SKIP cuando `ibs_20min` > 0.681
  - _Potencial_: sin este filtro IC_bueno=-0.261 (n=86)

- **FILTRO** `volumen_spike_ratio` < `1.4324` → IC=-0.380 (n=23)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.4324
  - _Potencial_: sin este filtro IC_bueno=-0.294 (n=71)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.302 (n=114)

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

- **FILTRO** `sigma_ewma_delta_pct` > `4.698` → IC=-0.382 (n=15)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.698
  - _Potencial_: sin este filtro IC_bueno=-0.202 (n=45)

- **FILTRO** `volumen_regimen` < `0.914` → IC=-0.452 (n=19)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.914
  - _Potencial_: sin este filtro IC_bueno=-0.151 (n=41)

- **FILTRO** `libro_spread` > `0.05` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.05
  - _Potencial_: sin este filtro IC_bueno=-0.244 (n=41)

### GBM_LATE_60M_PYCONFIRMADO
- **PATRÓN** `sigma_h` > `0.0088` → IC=+0.249 (n=249)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0088 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.191 (n=338)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 16.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` > `0.6774` → IC=+0.185 (n=744)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.6774 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` > `0.8184` → IC=+0.294 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8184 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.59` → IC=+0.158 (n=404)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 3.59 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` < `0.6242` → IC=+0.185 (n=249)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 0.6242 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` < `0.0701` → IC=+0.181 (n=556)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` < 0.0701 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `1.3986` → IC=+0.207 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3986 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.749` → IC=+0.143 (n=261)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 8.749 (IC base=+0.031)

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

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.2413 (IC base=+0.087)

- **PATRÓN** `volumen_pendiente_norm` > `0.2735` → IC=+0.144 (n=71)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_pendiente_norm` > 0.2735 (IC base=+0.087)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `volumen_pendiente_norm` > `0.1814` → IC=-0.167 (n=25)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1814
  - _Potencial_: sin este filtro IC_bueno=+0.144 (n=259)

- **FILTRO** `ibs_20min` > `0.15` → IC=-0.122 (n=146)

  - _Acción_: SKIP cuando `ibs_20min` > 0.15
  - _Potencial_: sin este filtro IC_bueno=+0.082 (n=285)

- **PATRÓN** `drift_60min` |x|≤ `0.1025` → IC=+0.133 (n=107)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.67€ cuando `drift_60min` |x|≤ 0.1025 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.155 (n=85)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 18.0 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.136 (n=119)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 8.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` > `0.7163` → IC=+0.147 (n=242)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` > 0.7163 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.217` → IC=+0.140 (n=251)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` < 9.217 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` < `0.6244` → IC=+0.175 (n=81)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.6244 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` > `1.1915` → IC=+0.163 (n=81)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 1.1915 (IC base=+0.117)

- **PATRÓN** `volumen_pendiente_norm` < `0.1814` → IC=+0.144 (n=259)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_pendiente_norm` < 0.1814 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` < `2.0546` → IC=+0.158 (n=188)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.0546 (IC base=+0.117)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.126 (n=209)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.01 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.619` → IC=+0.205 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.619 (IC base=+0.013)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.0811` → IC=-0.228 (n=101)

  - _Acción_: SKIP cuando `ibs_20min` > 0.0811
  - _Potencial_: sin este filtro IC_bueno=+0.067 (n=102)

- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.285 (n=128)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0101 (IC base=+0.253)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.296 (n=199)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.253)

- **PATRÓN** `ibs_20min` > `0.5882` → IC=+0.279 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5882 (IC base=+0.253)

- **PATRÓN** `dist_vwap_pct` > `0.7189` → IC=+0.397 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7189 (IC base=+0.253)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.797` → IC=+0.339 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.797 (IC base=+0.253)

- **PATRÓN** `volumen_regimen` < `0.5849` → IC=+0.312 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.5849 (IC base=+0.253)

- **PATRÓN** `volumen_pendiente_norm` > `0.0951` → IC=+0.300 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0951 (IC base=+0.253)

- **PATRÓN** `volumen_spike_ratio` < `1.3961` → IC=+0.344 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3961 (IC base=+0.253)

- **PATRÓN** `volumen_spike_ratio` > `2.3472` → IC=+0.292 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3472 (IC base=+0.253)

### LATE_WINDOW_5MIN
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.323 (n=128)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3645` → IC=+0.337 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3645 (IC base=+0.327)

- **PATRÓN** `elapsed_s` > `207.7` → IC=+0.392 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 207.7 (IC base=+0.327)

- **PATRÓN** `drift_15min` |x|≤ `1.0295` → IC=+0.412 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0295 (IC base=+0.327)

- **PATRÓN** `drift_60min` |x|≤ `0.7805` → IC=+0.382 (n=83)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.7805 (IC base=+0.327)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.389 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.327)

- **PATRÓN** `ballena_activa_n` < `1107.0` → IC=+0.353 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1107.0 (IC base=+0.327)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3495` → IC=+0.290 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3495 (IC base=+0.269)

- **PATRÓN** `elapsed_s` > `227.0` → IC=+0.346 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 227.0 (IC base=+0.269)

- **PATRÓN** `drift_15min` |x|≤ `2.2146` → IC=+0.327 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.2146 (IC base=+0.269)

- **PATRÓN** `drift_60min` |x|≤ `0.6484` → IC=+0.313 (n=73)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6484 (IC base=+0.269)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.323 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.269)

- **PATRÓN** `ballena_activa_n` < `1342.0` → IC=+0.368 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1342.0 (IC base=+0.269)

### LATE_WINDOW_5MIN#BTC#5min
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.323 (n=128)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3645` → IC=+0.337 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3645 (IC base=+0.327)

- **PATRÓN** `elapsed_s` > `207.7` → IC=+0.392 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 207.7 (IC base=+0.327)

- **PATRÓN** `drift_15min` |x|≤ `1.0295` → IC=+0.412 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0295 (IC base=+0.327)

- **PATRÓN** `drift_60min` |x|≤ `0.7805` → IC=+0.382 (n=83)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.7805 (IC base=+0.327)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.389 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.327)

- **PATRÓN** `ballena_activa_n` < `1107.0` → IC=+0.353 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1107.0 (IC base=+0.327)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3495` → IC=+0.290 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3495 (IC base=+0.269)

- **PATRÓN** `elapsed_s` > `227.0` → IC=+0.346 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 227.0 (IC base=+0.269)

- **PATRÓN** `drift_15min` |x|≤ `2.2146` → IC=+0.327 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.2146 (IC base=+0.269)

- **PATRÓN** `drift_60min` |x|≤ `0.6484` → IC=+0.313 (n=73)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6484 (IC base=+0.269)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.323 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.269)

- **PATRÓN** `ballena_activa_n` < `1342.0` → IC=+0.368 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1342.0 (IC base=+0.269)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.125 (n=1474)

  - _Acción_: Kelly boost +0.63€ cuando `py_entrada` > 0.5 (IC base=+0.098)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.125 (n=1474)

  - _Acción_: Kelly boost +0.63€ cuando `py_entrada` > 0.5 (IC base=+0.098)

### LIQUIDACIONES_15M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=253)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=253)

- **FILTRO** `libro_liquidez` < `6919.5202` → IC=-0.147 (n=134)

  - _Acción_: SKIP cuando `libro_liquidez` < 6919.5202
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=135)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=1033)

### LIQUIDACIONES_15M#BNB#15min
- **PATRÓN** `liq_n` > `2.0` → IC=+0.207 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `liq_n` > 2.0 (IC base=+0.071)

- **PATRÓN** `liq_usd_total` > `2417.8` → IC=+0.233 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `liq_usd_total` > 2417.8 (IC base=+0.071)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.188 (n=30)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 5.0 (IC base=+0.071)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.131 (n=63)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.03 (IC base=+0.071)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `libro_liquidez` < `12324.2702` → IC=-0.152 (n=44)

  - _Acción_: SKIP cuando `libro_liquidez` < 12324.2702
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=92)

### LIQUIDACIONES_15M#DOGE#15min
- **FILTRO** `hora_utc` > `9.0` → IC=-0.121 (n=27)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=+0.143 (n=40)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.300 (n=18)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.036)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `hora_utc` < `10.0` → IC=-0.184 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=40)

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
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=4001)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=173)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.091 (n=130)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.278 (n=34)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=160)

- **FILTRO** `ballena_activa_n` > `60.0` → IC=-0.188 (n=78)

  - _Acción_: SKIP cuando `ballena_activa_n` > 60.0
  - _Potencial_: sin este filtro IC_bueno=+0.202 (n=82)

- **PATRÓN** `ballena_activa_n` < `60.0` → IC=+0.202 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 60.0 (IC base=-0.031)

### LIQUIDACIONES_5M#BTC#5min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=22)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.167 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=15)

- **FILTRO** `libro_liquidez` < `13988.6712` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `libro_liquidez` < 13988.6712
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=19)

- **FILTRO** `ballena_activa_n` > `558.0` → IC=-0.227 (n=20)

  - _Acción_: SKIP cuando `ballena_activa_n` > 558.0
  - _Potencial_: sin este filtro IC_bueno=+0.200 (n=8)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.121 (n=275)

  - _Acción_: Kelly boost +0.60€ cuando `py_entrada` < 0.495 (IC base=+0.023)

### LIQUIDACIONES_5M#DOGE#5min
- **PATRÓN** `liq_n` > `3.0` → IC=+0.333 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `liq_n` > 3.0 (IC base=+0.240)

- **PATRÓN** `liq_usd_total` > `2217.29` → IC=+0.350 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `liq_usd_total` > 2217.29 (IC base=+0.240)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.278 (n=43)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.240)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.237 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.5 (IC base=+0.240)

- **PATRÓN** `libro_liquidez` > `2529.728` → IC=+0.274 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2529.728 (IC base=+0.240)

- **PATRÓN** `ballena_activa_n` < `6.0` → IC=+0.260 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 6.0 (IC base=+0.240)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=1615)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=1569)

- **FILTRO** `hora_utc` > `5.0` → IC=-0.286 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=10)

- **FILTRO** `ballena_activa_n` > `133.0` → IC=-0.250 (n=18)

  - _Acción_: SKIP cuando `ballena_activa_n` > 133.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

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
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=470)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=451)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.142 (n=202)

  - _Acción_: Kelly boost +0.71€ cuando `py_entrada` < 0.495 (IC base=+0.018)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=1040)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=1040)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=1346)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=1346)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=303)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=303)

- **FILTRO** `py_entrada` < `0.43` → IC=-0.132 (n=104)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=214)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.136 (n=64)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=370)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=419)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=310)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=412)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=412)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.120 (n=185)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=257)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=386)

### LIQUIDACIONES_DEPTH_FASE0#BNB#15min
- **FILTRO** `py_entrada` > `0.6` → IC=-0.141 (n=37)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=80)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.185 (n=90)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=110)

- **FILTRO** `hora_utc` > `14.0` → IC=-0.159 (n=86)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=114)

- **FILTRO** `py_entrada` > `0.52` → IC=-0.127 (n=57)

  - _Acción_: SKIP cuando `py_entrada` > 0.52
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=31)

- **FILTRO** `hora_utc` < `17.0` → IC=-0.142 (n=65)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=23)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **FILTRO** `py_entrada` > `0.6` → IC=-0.168 (n=257)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=738)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.148 (n=330)

  - _Acción_: Kelly boost +0.74€ cuando `py_entrada` < 0.5 (IC base=-0.011)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.121 (n=571)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=613)

- **FILTRO** `py_entrada` > `0.58` → IC=-0.126 (n=359)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=431)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.135 (n=288)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=632)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.122 (n=631)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.075 (n=337)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.120 (n=728)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=392)

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
- **FILTRO** `py_entrada` < `0.46` → IC=-0.174 (n=8245)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=26172)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.172 (n=8695)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=26919)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.194 (n=1538)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=4855)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.145 (n=2121)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.093 (n=4187)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.138 (n=1640)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` > 1.0 (IC base=+0.041)

- **PATRÓN** `py_entrada` < `0.505` → IC=+0.125 (n=3216)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` < 0.505 (IC base=+0.013)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` < `0.44` → IC=-0.174 (n=1150)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=3604)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.181 (n=1227)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=3776)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` > `0.62` → IC=-0.198 (n=1579)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.086 (n=4888)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.135 (n=1962)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` > 1.0 (IC base=+0.034)

- **PATRÓN** `libro_liquidez` > `1737.5454` → IC=+0.121 (n=2168)

  - _Acción_: Kelly boost +0.60€ cuando `libro_liquidez` > 1737.5454 (IC base=+0.034)

### MOMENTUM_IBS_15M_BALLENA#ETH#15min
- **FILTRO** `py_entrada` > `0.575` → IC=-0.177 (n=1251)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=3831)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.485` → IC=-0.160 (n=1585)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=4830)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=2446)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.162 (n=772)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=2370)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.180 (n=973)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=3119)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=4071)

- **FILTRO** `ballena_activa_n` > `32.0` → IC=-0.127 (n=1366)

  - _Acción_: SKIP cuando `ballena_activa_n` > 32.0
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=2693)

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
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=1098)

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
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=363)

- **FILTRO** `drift_20min_pct` |x|> `0.2038` → IC=-0.142 (n=118)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.2038
  - _Potencial_: sin este filtro IC_bueno=-0.119 (n=358)

- **FILTRO** `libro_liquidez` < `3239.0468` → IC=-0.185 (n=157)

  - _Acción_: SKIP cuando `libro_liquidez` < 3239.0468
  - _Potencial_: sin este filtro IC_bueno=-0.095 (n=319)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=978)

- **FILTRO** `libro_liquidez` < `1989.4319` → IC=-0.141 (n=396)

  - _Acción_: SKIP cuando `libro_liquidez` < 1989.4319
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=806)

### MOMENTUM_IBS_15M_FADE#XRP#15min
- **FILTRO** `hora_utc` < `13.0` → IC=-0.238 (n=59)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 13.0
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=239)

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
  - _Potencial_: sin este filtro IC_bueno=-0.091 (n=52812)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.299 (n=18407)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=57874)

- **FILTRO** `ibs_7min` < `0.2143` → IC=-0.235 (n=19019)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2143
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=57262)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.153 (n=25764)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=50517)

- **FILTRO** `py_entrada` > `0.68` → IC=-0.253 (n=22189)

  - _Acción_: SKIP cuando `py_entrada` > 0.68
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=73181)

- **FILTRO** `ibs_7min` > `0.2807` → IC=-0.183 (n=23841)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2807
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=71529)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.160 (n=3291)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=10347)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.319 (n=3374)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=10264)

- **FILTRO** `ibs_7min` < `0.7099` → IC=-0.253 (n=4498)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7099
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=9140)

- **FILTRO** `py_entrada` > `0.72` → IC=-0.279 (n=4009)

  - _Acción_: SKIP cuando `py_entrada` > 0.72
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=12468)

- **FILTRO** `ibs_7min` > `0.7727` → IC=-0.210 (n=4117)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7727
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=12360)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.263 (n=3072)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=9588)

- **FILTRO** `ibs_7min` < `0.7137` → IC=-0.210 (n=3165)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7137
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=9495)

- **FILTRO** `ballena_activa_n` > `156.0` → IC=-0.201 (n=3153)

  - _Acción_: SKIP cuando `ballena_activa_n` > 156.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=9507)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.268 (n=2965)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=9968)

- **FILTRO** `ibs_7min` > `0.2659` → IC=-0.194 (n=3232)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2659
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=9701)

- **FILTRO** `ballena_activa_n` > `152.0` → IC=-0.180 (n=3230)

  - _Acción_: SKIP cuando `ballena_activa_n` > 152.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=9703)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.167 (n=3146)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=9935)

- **FILTRO** `py_entrada` < `0.3` → IC=-0.324 (n=3120)

  - _Acción_: SKIP cuando `py_entrada` < 0.3
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=9961)

- **FILTRO** `ibs_7min` < `0.2883` → IC=-0.250 (n=4316)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2883
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=8765)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.201 (n=2550)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=10531)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.260 (n=4217)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=13246)

- **FILTRO** `ibs_7min` > `0.7273` → IC=-0.183 (n=4363)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7273
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=13100)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.264 (n=3059)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=9265)

- **FILTRO** `ibs_7min` < `0.7136` → IC=-0.199 (n=3080)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7136
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=9244)

- **FILTRO** `ballena_activa_n` > `24.0` → IC=-0.190 (n=3076)

  - _Acción_: SKIP cuando `ballena_activa_n` > 24.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=9248)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.261 (n=2985)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=9836)

- **FILTRO** `ibs_7min` > `0.2727` → IC=-0.179 (n=3202)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2727
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=9619)

- **FILTRO** `ballena_activa_n` > `23.0` → IC=-0.169 (n=3199)

  - _Acción_: SKIP cuando `ballena_activa_n` > 23.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=9622)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.32` → IC=-0.302 (n=2927)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=9271)

- **FILTRO** `ibs_7min` < `0.7` → IC=-0.236 (n=4003)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=8195)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.218 (n=2992)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=9206)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.199 (n=4455)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=13991)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.133 (n=4008)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.110 (n=8372)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.311 (n=2985)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=9395)

- **FILTRO** `ibs_7min` < `0.7308` → IC=-0.223 (n=4082)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7308
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=8298)

- **FILTRO** `ballena_activa_n` > `9.0` → IC=-0.207 (n=2735)

  - _Acción_: SKIP cuando `ballena_activa_n` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.092 (n=9645)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.228 (n=4274)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=12956)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1046` → IC=-0.135 (n=61)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1046
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=121)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `py_entrada` < `0.455` → IC=-0.163 (n=304)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=1014)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=1303)

- **FILTRO** `py_entrada` > `0.545` → IC=-0.159 (n=171)

  - _Acción_: SKIP cuando `py_entrada` > 0.545
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=630)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=1458)

- **FILTRO** `py_entrada` > `0.565` → IC=-0.172 (n=260)

  - _Acción_: SKIP cuando `py_entrada` > 0.565
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=910)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.123 (n=221)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=279)

- **FILTRO** `ballena_activa_n` > `3.0` → IC=-0.143 (n=166)

  - _Acción_: SKIP cuando `ballena_activa_n` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=333)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.231 (n=50)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=450)

- **FILTRO** `py_entrada` > `0.58` → IC=-0.216 (n=192)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=583)

- **FILTRO** `libro_liquidez` < `3304.2295` → IC=-0.151 (n=193)

  - _Acción_: SKIP cuando `libro_liquidez` < 3304.2295
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=582)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.4307` → IC=+0.148 (n=705)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.74€ cuando `delta_ratio` |x|> 0.4307 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.129 (n=1398)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 14.0 (IC base=+0.125)

- **PATRÓN** `total_vol_5m` < `422.506` → IC=+0.157 (n=517)

  - _Acción_: Kelly boost +0.79€ cuando `total_vol_5m` < 422.506 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `3557.6032` → IC=+0.138 (n=703)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 3557.6032 (IC base=+0.125)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `14.0` → IC=+0.177 (n=184)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 14.0 (IC base=+0.134)

- **PATRÓN** `total_vol_5m` < `287.685` → IC=+0.163 (n=244)

  - _Acción_: Kelly boost +0.81€ cuando `total_vol_5m` < 287.685 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `2517.123` → IC=+0.234 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2517.123 (IC base=+0.134)

- **PATRÓN** `ballena_activa_n` < `6.0` → IC=+0.137 (n=180)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 6.0 (IC base=+0.134)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `delta_ratio` |x|> `0.3994` → IC=+0.135 (n=321)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.67€ cuando `delta_ratio` |x|> 0.3994 (IC base=+0.121)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.139 (n=300)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 15.0 (IC base=+0.121)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.127 (n=389)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.04 (IC base=+0.121)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4164` → IC=+0.173 (n=194)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.87€ cuando `delta_ratio` |x|> 0.4164 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.149 (n=269)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 5.0 (IC base=+0.128)

- **PATRÓN** `total_vol_5m` < `857.788` → IC=+0.153 (n=292)

  - _Acción_: Kelly boost +0.77€ cuando `total_vol_5m` < 857.788 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `59.0` → IC=+0.173 (n=99)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 59.0 (IC base=+0.128)

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
- **PATRÓN** `hora_utc` < `14.0` → IC=+0.129 (n=286)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 14.0 (IC base=+0.098)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.134 (n=203)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.098)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `7.3154` → IC=-0.250 (n=58)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 7.3154
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=176)

- **FILTRO** `pct_vs_K` |x|> `2.7579` → IC=-0.149 (n=445)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.7579
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=446)

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.150 (n=295)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0045 (IC base=-0.052)

### PRICE_TARGET_GBM#ETH#atexpiry
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.293 (n=90)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=-0.007)

- **PATRÓN** `pct_vs_K` |x|≤ `1.7678` → IC=+0.196 (n=90)

  - _Acción_: Kelly boost +0.98€ cuando `pct_vs_K` |x|≤ 1.7678 (IC base=-0.007)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `pct_vs_K` |x|> `6.6759` → IC=-0.267 (n=28)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 6.6759
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=56)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `T_h` < `68.0124` → IC=-0.155 (n=56)

  - _Acción_: SKIP cuando `T_h` < 68.0124
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=115)

### PRICE_TARGET_GBM#SOL#reach
- **FILTRO** `T_h` < `146.0708` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `T_h` < 146.0708
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=16)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0115` → IC=-0.239 (n=603)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0115
  - _Potencial_: sin este filtro IC_bueno=-0.190 (n=201)

- **FILTRO** `T_h` > `66.9347` → IC=-0.231 (n=537)

  - _Acción_: SKIP cuando `T_h` > 66.9347
  - _Potencial_: sin este filtro IC_bueno=-0.217 (n=267)

- **FILTRO** `sigma_h` < `0.0076` → IC=-0.191 (n=351)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0076
  - _Potencial_: sin este filtro IC_bueno=-0.152 (n=351)

- **FILTRO** `T_h` > `143.0075` → IC=-0.229 (n=175)

  - _Acción_: SKIP cuando `T_h` > 143.0075
  - _Potencial_: sin este filtro IC_bueno=-0.152 (n=527)

- **FILTRO** `pct_vs_K` |x|> `3.014` → IC=-0.398 (n=174)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.014
  - _Potencial_: sin este filtro IC_bueno=-0.096 (n=528)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `sigma_h` < `0.009` → IC=-0.207 (n=172)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.009
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=92)

- **FILTRO** `T_h` < `60.8769` → IC=-0.219 (n=87)

  - _Acción_: SKIP cuando `T_h` < 60.8769
  - _Potencial_: sin este filtro IC_bueno=-0.193 (n=177)

- **FILTRO** `sigma_h` < `0.0072` → IC=-0.208 (n=169)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0072
  - _Potencial_: sin este filtro IC_bueno=-0.141 (n=90)

- **FILTRO** `T_h` > `143.4358` → IC=-0.227 (n=64)

  - _Acción_: SKIP cuando `T_h` > 143.4358
  - _Potencial_: sin este filtro IC_bueno=-0.170 (n=195)

- **FILTRO** `pct_vs_K` |x|> `1.9121` → IC=-0.317 (n=129)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 1.9121
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=130)

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
- **FILTRO** `sigma_h` < `0.0089` → IC=-0.319 (n=114)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0089
  - _Potencial_: sin este filtro IC_bueno=-0.244 (n=115)

- **FILTRO** `T_h` < `69.3259` → IC=-0.292 (n=75)

  - _Acción_: SKIP cuando `T_h` < 69.3259
  - _Potencial_: sin este filtro IC_bueno=-0.276 (n=154)

- **FILTRO** `sigma_h` < `0.0055` → IC=-0.209 (n=53)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0055
  - _Potencial_: sin este filtro IC_bueno=-0.121 (n=159)

- **FILTRO** `pct_vs_K` |x|> `2.0709` → IC=-0.386 (n=103)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.0709
  - _Potencial_: sin este filtro IC_bueno=+0.086 (n=109)

- **PATRÓN** `pct_vs_K` |x|≤ `0.9248` → IC=+0.196 (n=54)

  - _Acción_: Kelly boost +0.98€ cuando `pct_vs_K` |x|≤ 0.9248 (IC base=-0.145)

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
- **FILTRO** `sigma_h` < `0.0084` → IC=-0.241 (n=56)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0084
  - _Potencial_: sin este filtro IC_bueno=-0.186 (n=170)

- **FILTRO** `T_h` > `64.3086` → IC=-0.219 (n=169)

  - _Acción_: SKIP cuando `T_h` > 64.3086
  - _Potencial_: sin este filtro IC_bueno=-0.144 (n=57)

- **FILTRO** `sigma_h` > `0.0139` → IC=-0.315 (n=52)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0139
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=102)

- **FILTRO** `sigma_h` < `0.0104` → IC=-0.269 (n=50)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0104
  - _Potencial_: sin este filtro IC_bueno=-0.141 (n=104)

- **FILTRO** `T_h` < `89.2641` → IC=-0.209 (n=101)

  - _Acción_: SKIP cuando `T_h` < 89.2641
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=53)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1186` → IC=+0.452 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1186 (IC base=+0.330)

- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.386 (n=77)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0104 (IC base=+0.330)

- **PATRÓN** `T_h` < `0.3392` → IC=+0.402 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.3392 (IC base=+0.330)

- **PATRÓN** `T_h` > `0.4307` → IC=+0.357 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.4307 (IC base=+0.330)

- **PATRÓN** `dist_50` > `0.4692` → IC=+0.482 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4692 (IC base=+0.330)

- **PATRÓN** `edge` > `0.1005` → IC=+0.427 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1005 (IC base=+0.389)

- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.408 (n=183)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0097 (IC base=+0.389)

- **PATRÓN** `T_h` < `0.7218` → IC=+0.418 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.7218 (IC base=+0.389)

- **PATRÓN** `T_h` > `1.4833` → IC=+0.393 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4833 (IC base=+0.389)

- **PATRÓN** `dist_50` > `0.366` → IC=+0.441 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.366 (IC base=+0.389)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.410 (n=333)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.389)

### RESOLUTION_SNIPER#BTC#sniper
- **PATRÓN** `edge` > `0.1161` → IC=+0.274 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1161 (IC base=+0.171)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.259 (n=27)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.171)

- **PATRÓN** `sigma_h` > `0.0092` → IC=+0.200 (n=28)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0092 (IC base=+0.171)

- **PATRÓN** `T_h` > `1.4847` → IC=+0.200 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4847 (IC base=+0.171)

- **PATRÓN** `dist_50` > `0.322` → IC=+0.294 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.322 (IC base=+0.171)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.226 (n=60)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.171)

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
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=447)

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
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=188)

- **PATRÓN** `streak_estiramiento` < `0.2384` → IC=+0.134 (n=69)

  - _Acción_: Kelly boost +0.67€ cuando `streak_estiramiento` < 0.2384 (IC base=+0.030)

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
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=52)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.136 (n=31)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=37)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=820)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=826)

### STREAK_FADE_60M
- **FILTRO** `hora_utc` < `11.0` → IC=-0.184 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=19)

- **FILTRO** `py_entrada` < `0.515` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=21)

- **FILTRO** `volumen_racha` > `3677.1957` → IC=-0.143 (n=26)

  - _Acción_: SKIP cuando `volumen_racha` > 3677.1957
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=10)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=21)

- **FILTRO** `libro_liquidez` < `3449.8988` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `libro_liquidez` < 3449.8988
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

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
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=1081)

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
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=1300)

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
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=5076)

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
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=2942)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0055` → IC=+0.184 (n=1878)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0055 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.2232` → IC=+0.159 (n=5631)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.2232 (IC base=+0.139)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3551` → IC=+0.147 (n=5276)

  - _Acción_: Kelly boost +0.73€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3551 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.146 (n=5942)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 4.0 (IC base=+0.139)

- **PATRÓN** `ibs_15` > `0.5718` → IC=+0.221 (n=5030)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5718 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.1365` → IC=+0.129 (n=2607)

  - _Acción_: Kelly boost +0.64€ cuando `dist_vwap_pct` > 0.1365 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.26` → IC=+0.242 (n=1063)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.26 (IC base=+0.139)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=3172)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `4496.9297` → IC=+0.170 (n=1877)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 4496.9297 (IC base=+0.139)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=2185)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.218 (n=818)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.202)

- **PATRÓN** `drift_60min` |x|≤ `0.0763` → IC=+0.249 (n=360)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0763 (IC base=+0.202)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2675` → IC=+0.227 (n=273)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2675 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.229 (n=753)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.202)

- **PATRÓN** `ibs_15` > `0.7077` → IC=+0.272 (n=818)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7077 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` > `0.3751` → IC=+0.225 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3751 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` < `0.1104` → IC=+0.204 (n=558)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1104 (IC base=+0.202)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.371` → IC=+0.310 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.371 (IC base=+0.202)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.204 (n=1060)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `11835.8417` → IC=+0.220 (n=545)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11835.8417 (IC base=+0.202)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.145 (n=1021)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0071 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.1093` → IC=+0.150 (n=681)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.1093 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.139 (n=933)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 6.0 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.133 (n=1023)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 16.0 (IC base=+0.133)

- **PATRÓN** `ibs_15` > `0.4915` → IC=+0.219 (n=1020)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.4915 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` > `0.1194` → IC=+0.151 (n=631)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.1194 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.066` → IC=+0.283 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.066 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `6017.9372` → IC=+0.173 (n=463)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 6017.9372 (IC base=+0.133)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `ibs_15` > `0.7632` → IC=+0.133 (n=736)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.66€ cuando `ibs_15` > 0.7632 (IC base=+0.053)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` < `0.0193` → IC=+0.168 (n=950)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0193 (IC base=+0.152)

- **PATRÓN** `sigma_h` > `0.0127` → IC=+0.155 (n=1424)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` > 0.0127 (IC base=+0.152)

- **PATRÓN** `drift_60min` |x|≤ `0.2279` → IC=+0.179 (n=1424)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.2279 (IC base=+0.152)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0962` → IC=+0.213 (n=441)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0962 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.158 (n=1306)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 6.0 (IC base=+0.152)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.157 (n=1253)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 14.0 (IC base=+0.152)

- **PATRÓN** `ibs_15` > `0.537` → IC=+0.224 (n=1272)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.537 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` > `0.1984` → IC=+0.168 (n=646)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.1984 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.676` → IC=+0.191 (n=234)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 21.676 (IC base=+0.152)

- **PATRÓN** `libro_liquidez` > `2507.6219` → IC=+0.173 (n=1272)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 2507.6219 (IC base=+0.152)

- **PATRÓN** `ibs_15` < `0.1111` → IC=+0.150 (n=1088)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.75€ cuando `ibs_15` < 0.1111 (IC base=+0.067)

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
- **FILTRO** `sigma_h` > `0.0075` → IC=-0.200 (n=2776)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0075
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=2777)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.220 (n=2353)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=3200)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1411` → IC=+0.214 (n=477)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1411 (IC base=-0.084)

- **PATRÓN** `ibs_15` > `0.6307` → IC=+0.275 (n=1254)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6307 (IC base=-0.084)

- **PATRÓN** `dist_vwap_pct` > `0.1115` → IC=+0.198 (n=730)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.1115 (IC base=-0.084)

- **PATRÓN** `dist_vwap_pct` < `0.2602` → IC=+0.196 (n=1080)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` < 0.2602 (IC base=-0.084)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2328` → IC=+0.272 (n=1715)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2328 (IC base=-0.003)

- **PATRÓN** `ibs_15` < `0.3704` → IC=+0.286 (n=5136)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3704 (IC base=-0.003)

- **PATRÓN** `dist_vwap_pct` > `0.6602` → IC=+0.283 (n=708)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6602 (IC base=-0.003)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0323` → IC=-0.219 (n=2671)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0323
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=891)

- **FILTRO** `sigma_ewma_delta_pct` > `22.182` → IC=-0.245 (n=501)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 22.182
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=3061)

- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.151 (n=339)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0031 (IC base=+0.067)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2673` → IC=+0.287 (n=148)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2673 (IC base=+0.067)

- **PATRÓN** `ibs_15` > `0.7639` → IC=+0.314 (n=443)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7639 (IC base=+0.067)

- **PATRÓN** `dist_vwap_pct` > `0.1043` → IC=+0.272 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1043 (IC base=+0.067)

- **PATRÓN** `dist_vwap_pct` < `0.2443` → IC=+0.274 (n=400)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2443 (IC base=+0.067)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.133` → IC=+0.148 (n=225)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 22.133 (IC base=+0.067)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0742` → IC=+0.224 (n=74)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0742 (IC base=-0.185)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0866` → IC=+0.308 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0866 (IC base=-0.185)

- **PATRÓN** `ibs_15` < `0.6255` → IC=+0.289 (n=74)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.6255 (IC base=-0.185)

- **PATRÓN** `dist_vwap_pct` < `0.0453` → IC=+0.303 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0453 (IC base=-0.185)

- **PATRÓN** `ballena_activa_n` < `393.0` → IC=+0.300 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 393.0 (IC base=-0.185)

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

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.255 (n=1335)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0061 (IC base=+0.244)

- **PATRÓN** `drift_60min` |x|≤ `0.3589` → IC=+0.246 (n=1761)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3589 (IC base=+0.244)

- **PATRÓN** `drift_15min` |x|≤ `0.7869` → IC=+0.258 (n=1761)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7869 (IC base=+0.244)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2104` → IC=+0.267 (n=908)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2104 (IC base=+0.244)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.256 (n=735)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.244)

- **PATRÓN** `ibs_15` < `0.3849` → IC=+0.273 (n=2002)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3849 (IC base=+0.244)

- **PATRÓN** `dist_vwap_pct` > `0.3806` → IC=+0.275 (n=486)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3806 (IC base=+0.244)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.409` → IC=+0.249 (n=774)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.409 (IC base=+0.244)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.254` → IC=+0.248 (n=2097)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.254 (IC base=+0.244)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1877` → IC=-0.270 (n=324)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1877
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=976)

- **FILTRO** `sigma_h` > `0.0105` → IC=-0.236 (n=441)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0105
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=859)

- **FILTRO** `drift_60min` |x|> `0.1726` → IC=-0.270 (n=441)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1726
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=859)

- **FILTRO** `drift_15min` |x|> `0.9147` → IC=-0.285 (n=324)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.9147
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=976)

- **FILTRO** `sigma_ewma_delta_pct` > `16.923` → IC=-0.135 (n=689)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 16.923
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=5508)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1478` → IC=+0.188 (n=46)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.94€ cuando `delta_ratio_macro` |x|> 0.1478 (IC base=-0.202)

- **PATRÓN** `ibs_15` > `0.9231` → IC=+0.380 (n=23)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9231 (IC base=-0.202)

- **PATRÓN** `dist_vwap_pct` < `0.1327` → IC=+0.167 (n=55)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.1327 (IC base=-0.202)

- **PATRÓN** `ibs_15` < `0.381` → IC=+0.297 (n=881)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.381 (IC base=-0.029)

- **PATRÓN** `dist_vwap_pct` > `0.6926` → IC=+0.245 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6926 (IC base=-0.029)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0156` → IC=-0.248 (n=1059)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0156
  - _Potencial_: sin este filtro IC_bueno=-0.161 (n=523)

- **FILTRO** `drift_60min` |x|> `0.1534` → IC=-0.248 (n=395)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1534
  - _Potencial_: sin este filtro IC_bueno=-0.210 (n=1187)

- **FILTRO** `drift_15min` |x|> `1.2687` → IC=-0.281 (n=395)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.2687
  - _Potencial_: sin este filtro IC_bueno=-0.199 (n=1187)

- **FILTRO** `libro_spread` > `0.04` → IC=-0.273 (n=20)

  - _Acción_: SKIP cuando `libro_spread` > 0.04
  - _Potencial_: sin este filtro IC_bueno=-0.219 (n=1562)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.220)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.220)

- **PATRÓN** `delta_ratio_macro` |x|> `0.168` → IC=+0.282 (n=557)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.168 (IC base=-0.014)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1183` → IC=+0.299 (n=535)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1183 (IC base=-0.014)

- **PATRÓN** `ibs_15` < `0.3273` → IC=+0.295 (n=1229)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3273 (IC base=-0.014)

- **PATRÓN** `dist_vwap_pct` > `0.7632` → IC=+0.336 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7632 (IC base=-0.014)

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

- **PATRÓN** `sigma_h` > `0.0064` → IC=+0.283 (n=463)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0064 (IC base=+0.282)

- **PATRÓN** `drift_60min` |x|≤ `0.0714` → IC=+0.309 (n=612)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0714 (IC base=+0.282)

- **PATRÓN** `delta_ratio_macro` |x|> `0.152` → IC=+0.283 (n=926)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.152 (IC base=+0.282)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2216` → IC=+0.290 (n=849)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2216 (IC base=+0.282)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.294 (n=1442)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.282)

- **PATRÓN** `ibs_15` > `0.838` → IC=+0.309 (n=1389)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.838 (IC base=+0.282)

- **PATRÓN** `dist_vwap_pct` > `0.2659` → IC=+0.311 (n=595)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2659 (IC base=+0.282)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.944` → IC=+0.386 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.944 (IC base=+0.282)

- **PATRÓN** `libro_liquidez` > `13140.1865` → IC=+0.300 (n=463)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13140.1865 (IC base=+0.282)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.304 (n=324)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.275)

- **PATRÓN** `drift_60min` |x|≤ `0.0764` → IC=+0.304 (n=324)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0764 (IC base=+0.275)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2694` → IC=+0.282 (n=246)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2694 (IC base=+0.275)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3917` → IC=+0.281 (n=661)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3917 (IC base=+0.275)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.293 (n=772)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.275)

- **PATRÓN** `ibs_15` > `0.9195` → IC=+0.325 (n=490)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9195 (IC base=+0.275)

- **PATRÓN** `dist_vwap_pct` > `0.2534` → IC=+0.314 (n=309)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2534 (IC base=+0.275)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.742` → IC=+0.390 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.742 (IC base=+0.275)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.276 (n=950)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.275)

- **PATRÓN** `libro_liquidez` > `15745.2501` → IC=+0.314 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15745.2501 (IC base=+0.275)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.293 (n=655)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0069 (IC base=+0.289)

- **PATRÓN** `sigma_h` > `0.0053` → IC=+0.290 (n=437)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0053 (IC base=+0.289)

- **PATRÓN** `drift_60min` |x|≤ `0.1093` → IC=+0.309 (n=437)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1093 (IC base=+0.289)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0654` → IC=+0.290 (n=655)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0654 (IC base=+0.289)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1007` → IC=+0.316 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1007 (IC base=+0.289)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.299 (n=629)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.289)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.290 (n=464)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.289)

- **PATRÓN** `ibs_15` > `0.8466` → IC=+0.317 (n=655)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8466 (IC base=+0.289)

- **PATRÓN** `dist_vwap_pct` > `0.2774` → IC=+0.318 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2774 (IC base=+0.289)

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
- **FILTRO** `delta_ratio_macro` |x|≤ `0.2529` → IC=-0.147 (n=32)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2529
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=32)

- **FILTRO** `sigma_h` < `0.0054` → IC=-0.321 (n=26)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0054
  - _Potencial_: sin este filtro IC_bueno=-0.318 (n=9)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `drift_60min` |x|> `0.2521` → IC=-0.200 (n=18)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2521
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=37)

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
- **PATRÓN** `ratio` < `0.9701` → IC=+0.367 (n=397)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9701 (IC base=+0.158)

- **PATRÓN** `T_h` > `117.6267` → IC=+0.356 (n=2921)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 117.6267 (IC base=+0.337)

- **PATRÓN** `ratio` > `1.0204` → IC=+0.389 (n=509)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0204 (IC base=+0.337)

### WEEKLY_PRICE#BTC
- **PATRÓN** `ratio` < `0.9933` → IC=+0.241 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9933 (IC base=+0.115)

- **PATRÓN** `T_h` > `111.9558` → IC=+0.320 (n=1054)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9558 (IC base=+0.302)

- **PATRÓN** `ratio` > `1.0177` → IC=+0.370 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0177 (IC base=+0.302)

### WEEKLY_PRICE#ETH
- **PATRÓN** `ratio` < `0.9841` → IC=+0.394 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9841 (IC base=+0.205)

- **PATRÓN** `T_h` > `111.9965` → IC=+0.356 (n=1062)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9965 (IC base=+0.325)

- **PATRÓN** `ratio` > `1.0289` → IC=+0.406 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0289 (IC base=+0.325)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.0624` → IC=+0.417 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.0624 (IC base=+0.397)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5718 sube el IC de +0.139 a +0.221 en UPDOWN_GBM#15min (n=5030). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7077 sube el IC de +0.202 a +0.272 en UPDOWN_GBM#BTC#15min (n=818). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.4915 sube el IC de +0.133 a +0.219 en UPDOWN_GBM#ETH#15min (n=1020). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.537 sube el IC de +0.152 a +0.224 en UPDOWN_GBM#XRP#15min (n=1272). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1111 sube el IC de +0.067 a +0.150 en UPDOWN_GBM#XRP#15min (n=1088). Ya aplicado como kelly_boost=+0.75€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6307 sube el IC de -0.084 a +0.275 en UPDOWN_GBM_15M_TARDIO (n=1254). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3704 sube el IC de -0.003 a +0.286 en UPDOWN_GBM_15M_TARDIO (n=5136). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7639 sube el IC de +0.067 a +0.314 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=443). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.6255 sube el IC de -0.185 a +0.289 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=74). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.5684 sube el IC de +0.146 a +0.239 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=627). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3849 sube el IC de +0.244 a +0.273 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=2002). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.9231 sube el IC de -0.202 a +0.380 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=23). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.381 sube el IC de -0.029 a +0.297 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=881). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.220 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3273 sube el IC de -0.014 a +0.295 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=1229). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_YES, IBS > 0.8407 sube el IC de +0.103 a +0.315 en UPDOWN_GBM_ETH_15M_HORA7 (n=25). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_YES, IBS > 0.8407 sube el IC de +0.103 a +0.315 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=25). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.838 sube el IC de +0.282 a +0.309 en UPDOWN_GBM_IBS_ALTO (n=1389). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.9195 sube el IC de +0.275 a +0.325 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=490). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8466 sube el IC de +0.289 a +0.317 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=655). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7903 sube el IC de +0.364 a +0.394 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=762). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8078 sube el IC de +0.362 a +0.384 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=369). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.764 sube el IC de +0.365 a +0.394 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=393). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 2185 | +0.083 | +227.83€ | 1 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 2185 | +0.083 | +227.83€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1775 | +0.084 | +189.30€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1775 | +0.084 | +189.30€ | 1 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 285 | +0.068 | +10.79€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 285 | +0.068 | +10.79€ | 5 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 94 | +0.125 | +28.08€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 94 | +0.125 | +28.08€ | 1 | 9 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 1156 | -0.020 | +72.69€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 1156 | -0.020 | +72.69€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE | 7 | +0.019 | +3.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE#15min | 7 | +0.019 | +3.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 883 | -0.037 | +57.87€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 883 | -0.037 | +57.87€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 183 | +0.062 | +18.96€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 183 | +0.062 | +18.96€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 83 | -0.029 | -7.39€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 83 | -0.029 | -7.39€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 48285 | -0.084 | -6230.40€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 3037 | +0.077 | -306.38€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 45248 | -0.095 | -5924.02€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4854 | -0.112 | -813.96€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4854 | -0.112 | -813.96€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 3037 | +0.077 | -306.38€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 3037 | +0.077 | -306.38€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 4925 | -0.103 | -943.35€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 4925 | -0.103 | -943.35€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 13225 | -0.042 | -1293.99€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 13225 | -0.042 | -1293.99€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 13165 | -0.112 | -1379.92€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 13165 | -0.112 | -1379.92€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 9079 | -0.134 | -1492.80€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 9079 | -0.134 | -1492.80€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 50785 | -0.012 | +2820.42€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 13122 | +0.004 | +1501.38€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 37663 | -0.018 | +1319.04€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 50785 | -0.012 | +2820.42€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 13122 | +0.004 | +1501.38€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 37663 | -0.018 | +1319.04€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 193350 | +0.113 | -8031.56€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#15min | 22105 | +0.180 | -705.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 888 | +0.013 | -73.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 159333 | +0.105 | -6838.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 11024 | +0.093 | -414.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 26405 | +0.103 | -1875.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 79 | -0.179 | +10.89€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 26311 | +0.104 | -1874.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 36531 | +0.124 | -617.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5621 | +0.178 | -240.88€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 26374 | +0.120 | -186.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 4494 | +0.080 | -168.20€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 26454 | +0.098 | -1912.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 90 | -0.109 | +14.44€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 26349 | +0.099 | -1915.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 41316 | +0.123 | -875.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 10364 | +0.179 | -257.55€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 26794 | +0.106 | -540.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 4146 | +0.102 | -68.74€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#SOL | 36209 | +0.112 | -1618.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 5859 | +0.199 | -247.71€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 791 | +0.040 | -19.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 27175 | +0.096 | -1174.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 2384 | +0.103 | -177.79€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO#XRP | 26435 | +0.107 | -1131.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 92 | -0.117 | +15.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 26330 | +0.108 | -1147.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 31368 | +0.192 | -2208.40€ | 2 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 31368 | +0.192 | -2208.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 7102 | +0.168 | -751.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 7102 | +0.168 | -751.85€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 4576 | +0.196 | -180.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 4576 | +0.196 | -180.76€ | 3 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 6963 | +0.174 | -617.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 6963 | +0.174 | -617.28€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 5811 | +0.251 | -201.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 5811 | +0.251 | -201.50€ | 0 | 4 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 6837 | +0.185 | -470.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 6837 | +0.185 | -470.76€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 1262 | +0.426 | -46.40€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 1262 | +0.426 | -46.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 524 | +0.439 | -4.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 524 | +0.439 | -4.68€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE#15min | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 511 | +0.424 | -19.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 511 | +0.424 | -19.48€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 213 | +0.398 | -18.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 213 | +0.398 | -18.37€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 110928 | +0.199 | -8227.51€ | 3 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 110928 | +0.199 | -8227.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 19199 | +0.177 | -2231.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 19199 | +0.177 | -2231.12€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 17889 | +0.224 | -604.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 17889 | +0.224 | -604.43€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 19046 | +0.180 | -2027.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 19046 | +0.180 | -2027.96€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 18028 | +0.218 | -712.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 18028 | +0.218 | -712.38€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 18309 | +0.203 | -1152.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 18309 | +0.203 | -1152.89€ | 1 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 18457 | +0.196 | -1498.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 18457 | +0.196 | -1498.72€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 42885 | +0.117 | +359.78€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 42885 | +0.117 | +359.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 21351 | +0.117 | +206.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 21351 | +0.117 | +206.52€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 21534 | +0.117 | +153.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 21534 | +0.117 | +153.26€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 2639 | +0.292 | -17.58€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 2639 | +0.292 | -17.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 1204 | +0.281 | -30.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 1204 | +0.281 | -30.62€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 1293 | +0.295 | +6.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 1293 | +0.295 | +6.31€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 142 | +0.347 | +6.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 142 | +0.347 | +6.73€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 1215 | +0.437 | -8.74€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 1215 | +0.437 | -8.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 580 | +0.433 | -9.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 580 | +0.433 | -9.85€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 583 | +0.440 | -0.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 583 | +0.440 | -0.30€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 52 | +0.407 | +1.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 52 | +0.407 | +1.41€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1965 | +0.067 | -89.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 725 | +0.046 | -64.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 1240 | +0.079 | -25.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1531 | +0.074 | -44.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 291 | +0.053 | -19.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 1240 | +0.079 | -25.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 87065 | +0.101 | -2030.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 7030 | +0.097 | +155.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 80035 | +0.101 | -2186.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 47570 | +0.105 | -449.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 7030 | +0.097 | +155.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 40540 | +0.107 | -605.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 18560 | +0.109 | -96.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 18560 | +0.109 | -96.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 20935 | +0.082 | -1485.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 20935 | +0.082 | -1485.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 914 | +0.186 | -109.27€ | 5 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 914 | +0.186 | -109.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 914 | +0.186 | -109.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 914 | +0.186 | -109.27€ | 5 | 4 |
| ✅ GBM_LATE_15M | 59139 | +0.101 | +33116.91€ | 0 | 18 |
| ✅ GBM_LATE_15M#15min | 59139 | +0.101 | +33116.91€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 9787 | +0.226 | +8461.38€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 9787 | +0.226 | +8461.38€ | 0 | 21 |
| ✅ GBM_LATE_15M#BTC | 9107 | +0.176 | +7197.63€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 9107 | +0.176 | +7197.63€ | 0 | 21 |
| ✅ GBM_LATE_15M#DOGE | 10599 | +0.207 | +8394.69€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 10599 | +0.207 | +8394.69€ | 0 | 20 |
| ✅ GBM_LATE_15M#ETH | 7899 | +0.058 | +2594.72€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 7899 | +0.058 | +2594.72€ | 1 | 16 |
| ✅ GBM_LATE_15M#SOL | 8242 | -0.028 | +2153.18€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 8242 | -0.028 | +2153.18€ | 4 | 15 |
| ✅ GBM_LATE_15M#XRP | 13505 | -0.021 | +4315.31€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 13505 | -0.021 | +4315.31€ | 3 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 62494 | +0.086 | +36353.09€ | 0 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 62494 | +0.086 | +36353.09€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 12080 | -0.002 | +6423.89€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 12080 | -0.002 | +6423.89€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 13443 | +0.005 | +3616.89€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 13443 | +0.005 | +3616.89€ | 0 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 8474 | +0.295 | +9706.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 8474 | +0.295 | +9706.76€ | 0 | 22 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 11926 | +0.015 | +3733.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 11926 | +0.015 | +3733.87€ | 1 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 9575 | +0.045 | +4304.73€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 9575 | +0.045 | +4304.73€ | 3 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 6996 | +0.315 | +8566.95€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 6996 | +0.315 | +8566.95€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 46674 | +0.179 | +38631.87€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 46674 | +0.179 | +38631.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 7029 | +0.240 | +6548.06€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 7029 | +0.240 | +6548.06€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 7395 | +0.140 | +5493.06€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 7395 | +0.140 | +5493.06€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 7511 | +0.224 | +6529.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 7511 | +0.224 | +6529.77€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 8003 | +0.129 | +6182.37€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 8003 | +0.129 | +6182.37€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 8830 | +0.120 | +6677.99€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 8830 | +0.120 | +6677.99€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 7906 | +0.234 | +7200.61€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 7906 | +0.234 | +7200.61€ | 0 | 25 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 12745 | +0.126 | +6433.99€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 12745 | +0.126 | +6433.99€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 651 | +0.163 | +432.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 651 | +0.163 | +432.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 3445 | +0.126 | +1869.80€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 3445 | +0.126 | +1869.80€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 507 | +0.158 | +290.79€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 507 | +0.158 | +290.79€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 3637 | +0.125 | +1772.31€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 3637 | +0.125 | +1772.31€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 3310 | +0.099 | +1311.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 3310 | +0.099 | +1311.44€ | 0 | 13 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 1195 | +0.169 | +757.33€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 1195 | +0.169 | +757.33€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO | 59331 | +0.189 | +49060.52€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#15min | 59331 | +0.189 | +49060.52€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 9356 | +0.251 | +9071.17€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 9356 | +0.251 | +9071.17€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 9461 | +0.139 | +6620.27€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 9461 | +0.139 | +6620.27€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 10070 | +0.235 | +9128.07€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 10070 | +0.235 | +9128.07€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 9831 | +0.143 | +7301.78€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 9831 | +0.143 | +7301.78€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 10515 | +0.124 | +7504.60€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 10515 | +0.124 | +7504.60€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 10098 | +0.242 | +9434.63€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 10098 | +0.242 | +9434.63€ | 0 | 20 |
| ✅ GBM_LATE_5M | 15126 | +0.214 | +12494.37€ | 0 | 26 |
| ✅ GBM_LATE_5M#5min | 15126 | +0.214 | +12494.37€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 1439 | +0.247 | +1366.68€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 1439 | +0.247 | +1366.68€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 3267 | +0.211 | +2815.48€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 3267 | +0.211 | +2815.48€ | 0 | 27 |
| ✅ GBM_LATE_5M#DOGE | 1453 | +0.210 | +1160.11€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1453 | +0.210 | +1160.11€ | 0 | 19 |
| ✅ GBM_LATE_5M#ETH | 4341 | +0.205 | +3277.60€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 4341 | +0.205 | +3277.60€ | 0 | 26 |
| ✅ GBM_LATE_5M#SOL | 2610 | +0.222 | +2285.06€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 2610 | +0.222 | +2285.06€ | 0 | 24 |
| ✅ GBM_LATE_5M#XRP | 2016 | +0.209 | +1589.43€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 2016 | +0.209 | +1589.43€ | 0 | 0 |
| ✅ GBM_LATE_60M | 5298 | +0.053 | +1447.25€ | 0 | 6 |
| ✅ GBM_LATE_60M#60min | 5298 | +0.053 | +1447.25€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 1832 | +0.058 | +551.21€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 1832 | +0.058 | +551.21€ | 0 | 6 |
| ✅ GBM_LATE_60M#ETH | 1692 | +0.052 | +538.65€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 1692 | +0.052 | +538.65€ | 1 | 7 |
| ✅ GBM_LATE_60M#SOL | 1774 | +0.049 | +357.38€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 1774 | +0.049 | +357.38€ | 0 | 9 |
| 🚫 GBM_LATE_60M_FADE | 722 | -0.251 | -36.39€ | 9 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 722 | -0.251 | -36.39€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 261 | -0.253 | -19.53€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 261 | -0.253 | -19.53€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 261 | -0.245 | -7.56€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 261 | -0.245 | -7.56€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 200 | -0.253 | -9.31€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 200 | -0.253 | -9.31€ | 7 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 2178 | +0.084 | +544.65€ | 0 | 9 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 2178 | +0.084 | +544.65€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 847 | +0.071 | +192.82€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 847 | +0.071 | +192.82€ | 1 | 5 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 753 | +0.058 | +146.75€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 753 | +0.058 | +146.75€ | 2 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 578 | +0.136 | +205.08€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 578 | +0.136 | +205.08€ | 1 | 9 |
| ✅ LATE_WINDOW_5MIN | 270 | +0.298 | +308.59€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 270 | +0.298 | +308.59€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 270 | +0.298 | +308.59€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 270 | +0.298 | +308.59€ | 1 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 4437 | +0.097 | +1013.55€ | 0 | 1 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 4437 | +0.097 | +1013.55€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 4437 | +0.097 | +1013.55€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 4437 | +0.097 | +1013.55€ | 0 | 1 |
| ✅ LIQUIDACIONES_15M | 1323 | +0.009 | +49.66€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 1323 | +0.009 | +49.66€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 111 | +0.066 | +13.99€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 111 | +0.066 | +13.99€ | 0 | 4 |
| ✅ LIQUIDACIONES_15M#BTC | 289 | +0.002 | +10.97€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 289 | +0.002 | +10.97€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 77 | -0.019 | +0.97€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 77 | -0.019 | +0.97€ | 1 | 1 |
| ✅ LIQUIDACIONES_15M#ETH | 323 | +0.026 | +21.35€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 323 | +0.026 | +21.35€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 330 | -0.009 | +3.61€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 330 | -0.009 | +3.61€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 193 | +0.003 | -1.22€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 193 | +0.003 | -1.22€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 4280 | +0.018 | +153.14€ | 5 | 1 |
| ✅ LIQUIDACIONES_5M#5min | 4280 | +0.018 | +153.14€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 239 | +0.006 | -5.14€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 239 | +0.006 | -5.14€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 827 | +0.015 | +40.58€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 827 | +0.015 | +40.58€ | 4 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 272 | +0.051 | +55.03€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 272 | +0.051 | +55.03€ | 0 | 6 |
| ✅ LIQUIDACIONES_5M#ETH | 1667 | +0.019 | +28.62€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1667 | +0.019 | +28.62€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 775 | +0.012 | +3.41€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 775 | +0.012 | +3.41€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 500 | +0.012 | +30.64€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 500 | +0.012 | +30.64€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 2481 | -0.032 | -4.87€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 2481 | -0.032 | -4.87€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 752 | -0.032 | -12.05€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 752 | -0.032 | -12.05€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 886 | -0.010 | +19.68€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 886 | -0.010 | +19.68€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 843 | -0.056 | -12.50€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 843 | -0.056 | -12.50€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 16737 | -0.032 | -192.78€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 8073 | -0.034 | -104.85€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 8664 | -0.031 | -87.93€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 590 | -0.056 | -37.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 302 | -0.033 | -2.81€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 288 | -0.079 | -34.35€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 4394 | -0.027 | -28.96€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 2095 | -0.024 | +4.27€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 2299 | -0.029 | -33.23€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 1604 | -0.030 | +7.61€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 819 | -0.037 | -9.18€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 785 | -0.024 | +16.79€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 3787 | -0.033 | -62.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 1813 | -0.033 | -26.88€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 1974 | -0.033 | -35.19€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 3218 | -0.022 | +48.17€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 1558 | -0.029 | -2.26€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 1660 | -0.015 | +50.43€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 3144 | -0.047 | -120.37€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 1486 | -0.052 | -67.98€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 1658 | -0.042 | -52.38€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 70031 | -0.000 | +3761.40€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 70031 | -0.000 | +3761.40€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 12701 | +0.027 | +1736.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 12701 | +0.027 | +1736.87€ | 2 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 9757 | -0.038 | -152.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 9757 | -0.038 | -152.78€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 12841 | +0.025 | +1443.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 12841 | +0.025 | +1443.78€ | 1 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 9718 | -0.053 | -253.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 9718 | -0.053 | -253.37€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 11946 | -0.004 | +342.99€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 11946 | -0.004 | +342.99€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 13068 | +0.018 | +643.90€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 13068 | +0.018 | +643.90€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 7235 | -0.054 | -112.53€ | 5 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 7235 | -0.054 | -112.53€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1260 | -0.002 | -15.47€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1260 | -0.002 | -15.47€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 2006 | -0.061 | -21.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 2006 | -0.061 | -21.54€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 93 | -0.016 | +0.13€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 93 | -0.016 | +0.13€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 810 | -0.119 | -35.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 810 | -0.119 | -35.34€ | 5 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 2203 | -0.067 | -12.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 2203 | -0.067 | -12.79€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 863 | -0.018 | -27.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 863 | -0.018 | -27.52€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 171651 | -0.078 | +2249.96€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 171651 | -0.078 | +2249.96€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 30115 | -0.077 | +1727.57€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 30115 | -0.077 | +1727.57€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 25593 | -0.101 | -1262.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 25593 | -0.101 | -1262.34€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 30544 | -0.068 | +1516.81€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 30544 | -0.068 | +1516.81€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 25145 | -0.100 | -853.03€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 25145 | -0.100 | -853.03€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 30644 | -0.059 | +257.16€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 30644 | -0.059 | +257.16€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 29610 | -0.069 | +863.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 29610 | -0.069 | +863.80€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 9110 | -0.035 | -181.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 9110 | -0.035 | -181.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 1008 | -0.017 | -19.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 1008 | -0.017 | -19.32€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 2119 | -0.046 | -28.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 2119 | -0.046 | -28.02€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2661 | -0.025 | -35.39€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2661 | -0.025 | -35.39€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1275 | -0.064 | -31.66€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1275 | -0.064 | -31.66€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 1038 | -0.035 | -35.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 1038 | -0.035 | -35.56€ | 0 | 0 |
| ✅ ORDER_FLOW_5M | 2202 | +0.121 | +883.84€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#5min | 2066 | +0.125 | +871.24€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 487 | +0.134 | +237.33€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 487 | +0.134 | +237.33€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#DOGE | 426 | +0.121 | +155.30€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 426 | +0.121 | +155.30€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#ETH | 388 | +0.128 | +178.25€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 388 | +0.128 | +178.25€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 349 | +0.141 | +178.93€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 349 | +0.141 | +178.93€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#XRP | 416 | +0.098 | +121.43€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 416 | +0.098 | +121.43€ | 0 | 2 |
| ✅ ORDER_FLOW_5M_REACTIVO | 2271 | -0.016 | -10.33€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 2271 | -0.016 | -10.33€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 409 | +0.011 | +23.62€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 409 | +0.011 | +23.62€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 420 | -0.040 | -20.76€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 420 | -0.040 | -20.76€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 564 | -0.041 | -34.17€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 564 | -0.041 | -34.17€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 460 | +0.009 | +12.82€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 460 | +0.009 | +12.82€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 418 | -0.009 | +8.16€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 418 | -0.009 | +8.16€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 1192 | -0.058 | +15.92€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 550 | -0.094 | -50.44€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 429 | -0.103 | -29.89€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 121 | -0.061 | -20.55€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 417 | -0.018 | +43.32€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 302 | +0.000 | +51.32€ | 0 | 2 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 115 | -0.064 | -8.00€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 225 | -0.042 | +23.05€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 189 | -0.034 | +21.21€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 36 | -0.079 | +1.84€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 920 | -0.055 | +42.64€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 272 | -0.066 | -26.71€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 1506 | -0.202 | -80.95€ | 5 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 593 | -0.198 | -41.43€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 523 | -0.195 | -36.98€ | 5 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#reach | 70 | -0.208 | -4.45€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 503 | -0.207 | -38.60€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 441 | -0.218 | -45.74€ | 4 | 1 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 62 | -0.125 | +7.14€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 410 | -0.199 | -0.92€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 380 | -0.196 | -3.07€ | 5 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 30 | -0.219 | +2.15€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 1344 | -0.204 | -85.79€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 162 | -0.183 | +4.84€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 548 | +0.373 | +506.59€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#BTC | 116 | +0.144 | +89.63€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 116 | +0.144 | +89.63€ | 0 | 6 |
| ✅ RESOLUTION_SNIPER#ETH | 125 | +0.366 | +104.29€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 125 | +0.366 | +104.29€ | 0 | 5 |
| ✅ RESOLUTION_SNIPER#SOL | 307 | +0.458 | +312.67€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 307 | +0.458 | +312.67€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#sniper | 548 | +0.373 | +506.59€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 976 | +0.039 | +80.61€ | 2 | 2 |
| ✅ STREAK_FADE_15M#15min | 976 | +0.039 | +80.61€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 359 | +0.015 | +2.34€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 359 | +0.015 | +2.34€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 75 | +0.019 | +1.57€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 75 | +0.019 | +1.57€ | 1 | 1 |
| ✅ STREAK_FADE_15M#SOL | 83 | +0.018 | +6.06€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 83 | +0.018 | +6.06€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 459 | +0.064 | +70.64€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 459 | +0.064 | +70.64€ | 1 | 4 |
| ✅ STREAK_FADE_5M | 3594 | -0.023 | -142.81€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3594 | -0.023 | -142.81€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 1127 | -0.023 | -40.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 1127 | -0.023 | -40.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 619 | -0.028 | -27.08€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 619 | -0.028 | -27.08€ | 1 | 0 |
| ✅ STREAK_FADE_5M#SOL | 172 | -0.046 | -15.31€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 172 | -0.046 | -15.31€ | 4 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1676 | -0.019 | -60.21€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1676 | -0.019 | -60.21€ | 2 | 0 |
| ✅ STREAK_FADE_60M | 121 | -0.053 | -14.40€ | 6 | 0 |
| ✅ STREAK_FADE_60M#60min | 121 | -0.053 | -14.40€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 44 | -0.087 | -4.62€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 44 | -0.087 | -4.62€ | 4 | 0 |
| ✅ STREAK_FADE_60M#SOL | 77 | -0.032 | -9.78€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 77 | -0.032 | -9.78€ | 0 | 1 |
| ✅ STREAK_MOM_5M | 11558 | +0.014 | +74.82€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 11558 | +0.014 | +74.82€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2995 | +0.018 | +24.38€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2995 | +0.018 | +24.38€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 3043 | +0.016 | +33.19€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 3043 | +0.016 | +33.19€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2934 | +0.009 | -2.53€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2934 | +0.009 | -2.53€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2586 | +0.014 | +19.79€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2586 | +0.014 | +19.79€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 12370 | +0.018 | -5.75€ | 4 | 0 |
| ✅ STRUCT_NO_15M#15min | 12370 | +0.018 | -5.75€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 5095 | +0.021 | +3.81€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 5095 | +0.021 | +3.81€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 4299 | +0.018 | -4.25€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 4299 | +0.018 | -4.25€ | 4 | 0 |
| ✅ STRUCT_NO_15M#SOL | 2976 | +0.013 | -5.31€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 2976 | +0.013 | -5.31€ | 1 | 0 |
| ✅ UPDOWN_GBM | 111759 | +0.060 | +10611.23€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 27226 | +0.078 | +5435.69€ | 0 | 9 |
| ✅ UPDOWN_GBM#240min | 3251 | -0.001 | +32.24€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 74266 | +0.062 | +5035.41€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 6637 | -0.002 | +115.90€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 9479 | +0.104 | +1713.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1782 | +0.163 | +818.90€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 90 | -0.011 | -2.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 7607 | +0.091 | +896.93€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 25413 | +0.058 | +2261.95€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 3657 | +0.079 | +821.00€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 934 | -0.001 | +16.09€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 17727 | +0.068 | +1346.60€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 2957 | -0.005 | +75.22€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 138 | -0.064 | +3.04€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 12204 | +0.076 | +1339.40€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1761 | +0.154 | +738.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 86 | +0.023 | -0.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 10357 | +0.063 | +601.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 26435 | +0.050 | +1866.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 6415 | +0.071 | +988.02€ | 0 | 8 |
| ✅ UPDOWN_GBM#ETH#240min | 904 | +0.004 | +15.64€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 16544 | +0.052 | +822.76€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 2446 | +0.000 | +39.33€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 126 | -0.109 | +0.43€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 23600 | +0.040 | +1333.85€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 7366 | +0.032 | +451.62€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#240min | 840 | -0.011 | +5.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 14047 | +0.052 | +885.54€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 1234 | -0.002 | +1.35€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#daily | 113 | -0.143 | -9.65€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 14626 | +0.073 | +2097.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 6245 | +0.093 | +1617.71€ | 0 | 11 |
| ✅ UPDOWN_GBM#XRP#240min | 397 | +0.006 | -1.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 7984 | +0.061 | +481.76€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 377 | -0.104 | -6.18€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 1015 | +0.364 | +377.14€ | 0 | 10 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 1015 | +0.364 | +377.14€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 491 | +0.362 | +172.01€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 491 | +0.362 | +172.01€ | 0 | 10 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 524 | +0.365 | +205.13€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 524 | +0.365 | +205.13€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO | 26349 | -0.020 | +6560.24€ | 2 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 26349 | -0.020 | +6560.24€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1981 | -0.051 | +561.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1981 | -0.051 | +561.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 4917 | -0.115 | +274.63€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 4917 | -0.115 | +274.63€ | 2 | 11 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 1071 | +0.222 | +899.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 1071 | +0.222 | +899.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 3504 | +0.221 | +2250.12€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 3504 | +0.221 | +2250.12€ | 1 | 20 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 7497 | -0.059 | +1114.56€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 7497 | -0.059 | +1114.56€ | 5 | 5 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 7379 | -0.058 | +1459.88€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 7379 | -0.058 | +1459.88€ | 4 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 326 | +0.061 | +33.64€ | 0 | 8 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 326 | +0.061 | +33.64€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 326 | +0.061 | +33.64€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 326 | +0.061 | +33.64€ | 0 | 8 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1852 | +0.282 | +1556.21€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1852 | +0.282 | +1556.21€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 979 | +0.275 | +770.32€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 979 | +0.275 | +770.32€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 873 | +0.289 | +785.88€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 873 | +0.289 | +785.88€ | 0 | 10 |
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
| ✅ WEEKLY_PRICE | 4833 | +0.300 | +2158.68€ | 0 | 3 |
| ✅ WEEKLY_PRICE#BTC | 1845 | +0.255 | +236.16€ | 0 | 3 |
| ✅ WEEKLY_PRICE#ETH | 1869 | +0.294 | +788.42€ | 0 | 3 |
| ✅ WEEKLY_PRICE#SOL | 1119 | +0.381 | +1134.11€ | 0 | 1 |