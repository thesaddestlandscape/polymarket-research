# Hipótesis automáticas — 2026-11-07 07:43 UTC
_Generado por shadow_postmortem.py sobre 1229635 resoluciones (PNL=+167486.37€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.5` → IC=-0.317 (n=195)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.119 (n=691)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.198 (n=1003)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` > 0.505 (IC base=+0.129)

- **PATRÓN** `n_total_lado` > `63.0` → IC=+0.184 (n=315)

  - _Acción_: Kelly boost +0.92€ cuando `n_total_lado` > 63.0 (IC base=+0.129)

- **PATRÓN** `banda_hit_calibrado` > `0.6142` → IC=+0.245 (n=629)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6142 (IC base=+0.129)

- **PATRÓN** `banda_z` > `8.63` → IC=+0.203 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 8.63 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.149 (n=348)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 17.0 (IC base=+0.129)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=1027)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.129)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.293 (n=167)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.113 (n=489)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.195 (n=868)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` > 0.505 (IC base=+0.132)

- **PATRÓN** `n_total_lado` > `66.0` → IC=+0.187 (n=273)

  - _Acción_: Kelly boost +0.94€ cuando `n_total_lado` > 66.0 (IC base=+0.132)

- **PATRÓN** `banda_hit_calibrado` > `0.8131` → IC=+0.270 (n=368)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8131 (IC base=+0.132)

- **PATRÓN** `banda_z` > `9.008` → IC=+0.211 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.008 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.154 (n=296)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 17.0 (IC base=+0.132)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.139 (n=927)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.132)

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
- **FILTRO** `ballenas_wallet_edge_medio` < `2.833` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `ballenas_wallet_edge_medio` < 2.833
  - _Potencial_: sin este filtro IC_bueno=+0.375 (n=6)

- **PATRÓN** `py_entrada` > `0.495` → IC=+0.167 (n=46)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` > 0.495 (IC base=+0.162)

- **PATRÓN** `n_ballena_banda` > `26.0` → IC=+0.231 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `n_ballena_banda` > 26.0 (IC base=+0.162)

- **PATRÓN** `n_total_lado` > `43.0` → IC=+0.300 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 43.0 (IC base=+0.162)

- **PATRÓN** `banda_hit_calibrado` > `0.6068` → IC=+0.180 (n=23)

  - _Acción_: Kelly boost +0.90€ cuando `banda_hit_calibrado` > 0.6068 (IC base=+0.162)

- **PATRÓN** `banda_z` > `2.495` → IC=+0.231 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 2.495 (IC base=+0.162)

- **PATRÓN** `ballenas_wallet_edge_medio` > `0.729` → IC=+0.159 (n=42)

  - _Acción_: Kelly boost +0.80€ cuando `ballenas_wallet_edge_medio` > 0.729 (IC base=+0.162)

- **PATRÓN** `hora_utc` > `13.0` → IC=+0.269 (n=24)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 13.0 (IC base=+0.162)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.167 (n=22)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 7.0 (IC base=+0.162)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.214 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.162)

- **PATRÓN** `libro_liquidez` > `2453.7234` → IC=+0.202 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2453.7234 (IC base=+0.162)

### BALLENAS_TARDIAS
- **FILTRO** `restante_s_al_confirmar` < `133.27` → IC=-0.221 (n=11544)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 133.27
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=34634)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `125.38` → IC=-0.257 (n=1189)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 125.38
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=3568)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `116.68` → IC=-0.296 (n=1195)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 116.68
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=3590)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `restante_s_al_confirmar` < `117.63` → IC=-0.166 (n=3153)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 117.63
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=9464)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `154.84` → IC=-0.239 (n=3123)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 154.84
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=9370)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `129.19` → IC=-0.263 (n=2192)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 129.19
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=6576)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.210 (n=26521)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.104)

- **PATRÓN** `libro_liquidez` > `8439.9904` → IC=+0.160 (n=2277)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 8439.9904 (IC base=+0.104)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.128 (n=22851)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 17.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.130 (n=27835)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.124)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.223 (n=20999)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.142 (n=8103)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `6696.732` → IC=+0.147 (n=3127)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 6696.732 (IC base=+0.124)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.185 (n=2083)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 6.0 (IC base=+0.178)

- **PATRÓN** `py_entrada` > `0.765` → IC=+0.364 (n=696)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.765 (IC base=+0.178)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.181 (n=2674)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.01 (IC base=+0.178)

- **PATRÓN** `libro_liquidez` > `9416.0594` → IC=+0.181 (n=1860)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 9416.0594 (IC base=+0.178)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.187 (n=1903)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 7.0 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.183 (n=2127)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 17.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` < `0.295` → IC=+0.312 (n=981)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.295 (IC base=+0.180)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.183 (n=2726)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.01 (IC base=+0.180)

- **PATRÓN** `libro_liquidez` > `16089.4675` → IC=+0.184 (n=703)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 16089.4675 (IC base=+0.180)

### FAVORITO_CONFIRMADO#BTC#60min
- **FILTRO** `py_entrada` < `0.55` → IC=-0.335 (n=95)

  - _Acción_: SKIP cuando `py_entrada` < 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.094 (n=2127)

- **PATRÓN** `py_entrada` > `0.61` → IC=+0.173 (n=579)

  - _Acción_: Kelly boost +0.86€ cuando `py_entrada` > 0.61 (IC base=+0.075)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.143 (n=1357)

  - _Acción_: Kelly boost +0.72€ cuando `py_entrada` < 0.44 (IC base=+0.082)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.168 (n=5090)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.164)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.168 (n=4306)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` < 15.0 (IC base=+0.164)

- **PATRÓN** `py_entrada` > `0.77` → IC=+0.377 (n=1636)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.77 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.214 (n=2294)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.204)

- **PATRÓN** `py_entrada` < `0.275` → IC=+0.329 (n=928)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.275 (IC base=+0.204)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.207 (n=2668)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.204)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.142 (n=1301)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 5.0 (IC base=+0.142)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.147 (n=1110)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 15.0 (IC base=+0.142)

- **PATRÓN** `py_entrada` > `0.675` → IC=+0.255 (n=419)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.675 (IC base=+0.142)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.141 (n=1058)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.156 (n=155)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.072)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.255 (n=934)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.227)

- **PATRÓN** `py_entrada` > `0.83` → IC=+0.420 (n=1294)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.83 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.148 (n=1394)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 7.0 (IC base=+0.147)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.156 (n=721)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 7.0 (IC base=+0.147)

- **PATRÓN** `py_entrada` < `0.34` → IC=+0.286 (n=670)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.34 (IC base=+0.147)

### FAVORITO_CONFIRMADO#SOL#60min
- **FILTRO** `libro_liquidez` < `950.557` → IC=-0.131 (n=155)

  - _Acción_: SKIP cuando `libro_liquidez` < 950.557
  - _Potencial_: sin este filtro IC_bueno=+0.072 (n=316)

- **PATRÓN** `py_entrada` > `0.55` → IC=+0.160 (n=457)

  - _Acción_: Kelly boost +0.80€ cuando `py_entrada` > 0.55 (IC base=+0.047)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.148 (n=467)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 17.0 (IC base=+0.122)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.242 (n=421)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.122)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `10.0` → IC=-0.297 (n=72)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.232 (n=151)

- **FILTRO** `libro_liquidez` < `9614.35` → IC=-0.263 (n=167)

  - _Acción_: SKIP cuando `libro_liquidez` < 9614.35
  - _Potencial_: sin este filtro IC_bueno=-0.224 (n=56)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.201 (n=22835)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.199 (n=19338)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.197)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.227 (n=9504)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.197)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=360)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.197)

- **PATRÓN** `libro_liquidez` > `4915.142` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4915.142 (IC base=+0.197)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.177 (n=5205)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 5.0 (IC base=+0.174)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.174 (n=5190)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 18.0 (IC base=+0.174)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.182 (n=5275)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` < 0.74 (IC base=+0.174)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.174 (n=4370)

  - _Acción_: Kelly boost +0.87€ cuando `py_entrada` > 0.71 (IC base=+0.174)

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

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.214 (n=3016)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.211)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.215 (n=2020)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.211)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.255 (n=1523)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.211)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.183 (n=5109)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 5.0 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.180 (n=4343)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 15.0 (IC base=+0.177)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.178 (n=5292)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` < 0.73 (IC base=+0.177)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.185 (n=3992)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` > 0.71 (IC base=+0.177)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.256 (n=4323)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.249)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.250 (n=3669)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.249)

- **PATRÓN** `py_entrada` > `0.8` → IC=+0.366 (n=1369)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.8 (IC base=+0.249)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.306 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.249)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.190 (n=5025)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.187)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.191 (n=4269)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.187)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.191 (n=3744)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.71 (IC base=+0.187)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.429 (n=936)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.426)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.428 (n=831)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.426)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.439 (n=949)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.426)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.432 (n=992)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.426)

- **PATRÓN** `libro_liquidez` > `3182.2307` → IC=+0.437 (n=809)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3182.2307 (IC base=+0.426)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` < `11.0` → IC=+0.450 (n=256)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.439)

- **PATRÓN** `py_entrada` > `0.935` → IC=+0.455 (n=219)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.935 (IC base=+0.439)

- **PATRÓN** `libro_liquidez` > `12430.0394` → IC=+0.446 (n=331)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12430.0394 (IC base=+0.439)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.430 (n=370)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.424)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.427 (n=369)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.424)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.436 (n=373)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.424)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.430 (n=414)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.424)

- **PATRÓN** `libro_liquidez` > `4712.9023` → IC=+0.435 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4712.9023 (IC base=+0.424)

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
  - _Potencial_: sin este filtro IC_bueno=-0.257 (n=35)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=34)

- **FILTRO** `libro_liquidez` < `6112.397` → IC=-0.300 (n=33)

  - _Acción_: SKIP cuando `libro_liquidez` < 6112.397
  - _Potencial_: sin este filtro IC_bueno=-0.237 (n=17)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.205 (n=29929)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.241 (n=30073)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.200)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.189 (n=4457)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 18.0 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.182 (n=9543)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 12.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.192 (n=13633)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.71 (IC base=+0.180)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.228 (n=6209)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.225)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.287 (n=4248)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.225)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.183 (n=12526)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 7.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.198 (n=10591)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` > 0.72 (IC base=+0.180)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.835` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.835
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.228 (n=4192)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.219)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.224 (n=4804)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.219)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.269 (n=4183)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.219)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **FILTRO** `hora_utc` > `3.0` → IC=-0.278 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **FILTRO** `libro_liquidez` < `3176.5987` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `libro_liquidez` < 3176.5987
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.212 (n=4260)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.258 (n=4366)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.202 (n=4982)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.198 (n=4974)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 6.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.243 (n=5188)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.196)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.191 (n=10744)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.139 (n=11194)

  - _Acción_: Kelly boost +0.69€ cuando `restante_min` > 4.96 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `3.49` → IC=+0.137 (n=13090)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 3.49 (IC base=+0.116)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.193 (n=5249)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.142 (n=5071)

  - _Acción_: Kelly boost +0.71€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.126 (n=6590)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 7.0 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `2.6` → IC=+0.141 (n=4944)

  - _Acción_: Kelly boost +0.70€ cuando `lag_apertura_s` < 2.6 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.190 (n=5495)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.136 (n=6813)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.95 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `2.23` → IC=+0.139 (n=5012)

  - _Acción_: Kelly boost +0.70€ cuando `lag_apertura_s` < 2.23 (IC base=+0.116)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.305 (n=1334)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.292)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.388 (n=687)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.292)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.284 (n=899)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.280)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.367 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.280)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.318 (n=647)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.297)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.300 (n=949)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.297)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.396 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.297)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.297 (n=797)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.297)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` < `16.0` → IC=+0.362 (n=92)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.341)

- **PATRÓN** `py_entrada` > `0.805` → IC=+0.430 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.805 (IC base=+0.341)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.372 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.341)

- **PATRÓN** `libro_liquidez` > `720.8183` → IC=+0.372 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 720.8183 (IC base=+0.341)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.444 (n=909)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.440)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.446 (n=879)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.440)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.440 (n=1055)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.440)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.437 (n=425)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.433)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.436 (n=295)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.433)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.432 (n=439)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.433)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.439 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.433)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.466 (n=144)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.447)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.449 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.447)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.448 (n=499)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.447)

- **PATRÓN** `libro_liquidez` > `2346.1445` → IC=+0.457 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2346.1445 (IC base=+0.447)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.419 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.406)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.417 (n=34)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.406)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.447 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.406)

- **PATRÓN** `libro_liquidez` > `779.6536` → IC=+0.392 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 779.6536 (IC base=+0.406)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION
- **FILTRO** `hora_utc` < `5.0` → IC=-0.269 (n=24)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=109)

- **FILTRO** `py_entrada` > `0.715` → IC=-0.351 (n=65)

  - _Acción_: SKIP cuando `py_entrada` > 0.715
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=68)

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

- **FILTRO** `py_entrada` > `0.715` → IC=-0.351 (n=65)

  - _Acción_: SKIP cuando `py_entrada` > 0.715
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=68)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4766` → IC=+0.139 (n=16884)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.4766 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.127 (n=17052)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 6.0 (IC base=+0.123)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.127 (n=11765)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 12.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` > `0.3727` → IC=+0.165 (n=16884)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.3727 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` > `0.8013` → IC=+0.282 (n=958)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8013 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.529` → IC=+0.185 (n=8435)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 3.529 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` > `0.6251` → IC=+0.264 (n=5021)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6251 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` > `0.3035` → IC=+0.250 (n=1742)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3035 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` > `2.7399` → IC=+0.235 (n=4039)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7399 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.134 (n=8437)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.123)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.121 (n=10544)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0061 (IC base=+0.081)

- **PATRÓN** `ibs_20min` < `0.6782` → IC=+0.132 (n=23917)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.6782 (IC base=+0.081)

- **PATRÓN** `dist_vwap_pct` > `0.6184` → IC=+0.190 (n=1433)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.6184 (IC base=+0.081)

- **PATRÓN** `dist_vwap_pct` < `0.1627` → IC=+0.188 (n=8262)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` < 0.1627 (IC base=+0.081)

- **PATRÓN** `volumen_regimen` < `0.6955` → IC=+0.195 (n=3761)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 0.6955 (IC base=+0.081)

- **PATRÓN** `volumen_pendiente_norm` > `0.2955` → IC=+0.228 (n=2106)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2955 (IC base=+0.081)

- **PATRÓN** `volumen_spike_ratio` > `2.6732` → IC=+0.209 (n=4840)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6732 (IC base=+0.081)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.225 (n=14425)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 100.0 (IC base=+0.081)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `drift_60min` |x|≤ `0.3653` → IC=+0.212 (n=3610)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3653 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.224 (n=1751)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.211)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.213 (n=2424)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` > `0.9855` → IC=+0.280 (n=1636)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9855 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.534` → IC=+0.279 (n=1603)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.534 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.2826` → IC=+0.267 (n=470)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2826 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `1.4352` → IC=+0.214 (n=3456)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4352 (IC base=+0.211)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.224 (n=3962)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `2051.72` → IC=+0.211 (n=1203)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2051.72 (IC base=+0.211)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.225 (n=2199)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.211)

- **PATRÓN** `sigma_h` < `0.0101` → IC=+0.242 (n=3164)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0101 (IC base=+0.240)

- **PATRÓN** `sigma_h` > `0.009` → IC=+0.240 (n=1437)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.009 (IC base=+0.240)

- **PATRÓN** `drift_60min` |x|≤ `0.09` → IC=+0.278 (n=1055)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.09 (IC base=+0.240)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.250 (n=1179)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.240)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.243 (n=1466)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.240)

- **PATRÓN** `ibs_20min` < `0.5588` → IC=+0.258 (n=3165)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5588 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` < `0.0941` → IC=+0.244 (n=2862)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0941 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` > `0.2878` → IC=+0.249 (n=429)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2878 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` < `1.4444` → IC=+0.246 (n=1006)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4444 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` > `1.8557` → IC=+0.242 (n=2009)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8557 (IC base=+0.240)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.242 (n=3631)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.240)

- **PATRÓN** `libro_liquidez` > `1785.9` → IC=+0.245 (n=2109)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1785.9 (IC base=+0.240)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.234 (n=1018)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.223)

- **PATRÓN** `drift_60min` |x|≤ `0.1096` → IC=+0.255 (n=1328)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1096 (IC base=+0.223)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.234 (n=3156)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.223)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.226 (n=2146)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.223)

- **PATRÓN** `ibs_20min` > `0.9098` → IC=+0.261 (n=1006)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9098 (IC base=+0.223)

- **PATRÓN** `dist_vwap_pct` > `0.186` → IC=+0.234 (n=1396)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.186 (IC base=+0.223)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.987` → IC=+0.264 (n=442)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.987 (IC base=+0.223)

- **PATRÓN** `volumen_regimen` < `1.2254` → IC=+0.224 (n=3019)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2254 (IC base=+0.223)

- **PATRÓN** `volumen_regimen` > `0.6287` → IC=+0.228 (n=3018)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6287 (IC base=+0.223)

- **PATRÓN** `volumen_pendiente_norm` > `0.2785` → IC=+0.268 (n=425)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2785 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` > `2.4308` → IC=+0.254 (n=993)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4308 (IC base=+0.223)

- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.149 (n=3208)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0064 (IC base=+0.127)

- **PATRÓN** `drift_60min` |x|≤ `0.0778` → IC=+0.151 (n=1069)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.0778 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.142 (n=2278)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 11.0 (IC base=+0.127)

- **PATRÓN** `ibs_20min` < `0.7095` → IC=+0.167 (n=3207)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.7095 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.973` → IC=+0.135 (n=2935)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 3.973 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` < `1.0545` → IC=+0.136 (n=2822)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 1.0545 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` > `0.0719` → IC=+0.152 (n=1300)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` > 0.0719 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` < `2.4323` → IC=+0.137 (n=3082)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 2.4323 (IC base=+0.127)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.128 (n=4161)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.01 (IC base=+0.127)

- **PATRÓN** `ballena_activa_n` < `204.0` → IC=+0.165 (n=1337)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 204.0 (IC base=+0.127)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0114` → IC=+0.215 (n=1734)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0114 (IC base=+0.195)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.201 (n=4007)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.195)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.195 (n=3420)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 15.0 (IC base=+0.195)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.263 (n=1486)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.195)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.063` → IC=+0.277 (n=835)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.063 (IC base=+0.195)

- **PATRÓN** `volumen_pendiente_norm` < `0.0975` → IC=+0.197 (n=3423)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` < 0.0975 (IC base=+0.195)

- **PATRÓN** `volumen_pendiente_norm` > `0.3522` → IC=+0.223 (n=492)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3522 (IC base=+0.195)

- **PATRÓN** `volumen_spike_ratio` > `2.7274` → IC=+0.213 (n=1691)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7274 (IC base=+0.195)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.200 (n=4613)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.195)

- **PATRÓN** `libro_liquidez` > `2031.6` → IC=+0.204 (n=1273)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2031.6 (IC base=+0.195)

- **PATRÓN** `sigma_h` < `0.0111` → IC=+0.224 (n=3084)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0111 (IC base=+0.218)

- **PATRÓN** `drift_60min` |x|≤ `0.1765` → IC=+0.234 (n=1542)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1765 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.241 (n=1332)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.220 (n=1599)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.218)

- **PATRÓN** `ibs_20min` < `0.0419` → IC=+0.270 (n=1169)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0419 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.976` → IC=+0.263 (n=386)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.976 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` > `0.3488` → IC=+0.254 (n=505)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3488 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` < `1.7631` → IC=+0.221 (n=1481)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7631 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` > `2.1534` → IC=+0.226 (n=2244)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1534 (IC base=+0.218)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.223 (n=1770)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.218)

- **PATRÓN** `libro_liquidez` > `1911.7298` → IC=+0.225 (n=1589)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1911.7298 (IC base=+0.218)

- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.221 (n=3310)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 25.0 (IC base=+0.218)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.162 (n=190)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=4603)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.155 (n=644)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0038 (IC base=+0.058)

- **PATRÓN** `ibs_20min` > `0.9436` → IC=+0.232 (n=644)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9436 (IC base=+0.058)

- **PATRÓN** `dist_vwap_pct` > `0.14` → IC=+0.340 (n=453)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.14 (IC base=+0.058)

- **PATRÓN** `dist_vwap_pct` < `0.5452` → IC=+0.333 (n=800)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5452 (IC base=+0.058)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.078` → IC=+0.202 (n=1406)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.078 (IC base=+0.058)

- **PATRÓN** `volumen_regimen` > `0.7027` → IC=+0.339 (n=679)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7027 (IC base=+0.058)

- **PATRÓN** `volumen_pendiente_norm` < `0.1669` → IC=+0.335 (n=617)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1669 (IC base=+0.058)

- **PATRÓN** `volumen_pendiente_norm` > `0.3014` → IC=+0.333 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3014 (IC base=+0.058)

- **PATRÓN** `volumen_spike_ratio` < `1.4169` → IC=+0.343 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4169 (IC base=+0.058)

- **PATRÓN** `volumen_spike_ratio` > `2.2694` → IC=+0.337 (n=336)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2694 (IC base=+0.058)

- **PATRÓN** `ballena_activa_n` < `142.0` → IC=+0.337 (n=748)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 142.0 (IC base=+0.058)

- **PATRÓN** `ibs_20min` < `0.0903` → IC=+0.184 (n=1199)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.0903 (IC base=+0.049)

- **PATRÓN** `dist_vwap_pct` > `0.3361` → IC=+0.159 (n=593)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.3361 (IC base=+0.049)

- **PATRÓN** `dist_vwap_pct` < `0.1393` → IC=+0.148 (n=2127)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.1393 (IC base=+0.049)

- **PATRÓN** `volumen_regimen` < `0.8329` → IC=+0.157 (n=1516)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.8329 (IC base=+0.049)

- **PATRÓN** `volumen_pendiente_norm` > `0.2799` → IC=+0.203 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2799 (IC base=+0.049)

- **PATRÓN** `volumen_spike_ratio` < `1.77` → IC=+0.151 (n=1459)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.77 (IC base=+0.049)

- **PATRÓN** `volumen_spike_ratio` > `1.5112` → IC=+0.151 (n=1954)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.5112 (IC base=+0.049)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.186 (n=135)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=721)

- **FILTRO** `ibs_20min` < `0.2647` → IC=-0.171 (n=214)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2647
  - _Potencial_: sin este filtro IC_bueno=+0.078 (n=642)

- **FILTRO** `ibs_20min` > `0.2` → IC=-0.132 (n=4514)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2
  - _Potencial_: sin este filtro IC_bueno=+0.156 (n=2225)

- **FILTRO** `sigma_ewma_delta_pct` > `8.347` → IC=-0.225 (n=726)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.347
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=6013)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.178 (n=293)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.75 (IC base=+0.015)

- **PATRÓN** `dist_vwap_pct` > `0.9754` → IC=+0.275 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9754 (IC base=+0.015)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.043` → IC=+0.158 (n=200)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 5.043 (IC base=+0.015)

- **PATRÓN** `volumen_regimen` > `0.6262` → IC=+0.279 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6262 (IC base=+0.015)

- **PATRÓN** `volumen_spike_ratio` < `2.4484` → IC=+0.277 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4484 (IC base=+0.015)

- **PATRÓN** `volumen_spike_ratio` > `1.5387` → IC=+0.263 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5387 (IC base=+0.015)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.268 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.015)

- **PATRÓN** `ibs_20min` < `0.2` → IC=+0.156 (n=2225)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.2 (IC base=-0.037)

- **PATRÓN** `dist_vwap_pct` > `0.218` → IC=+0.286 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.218 (IC base=-0.037)

- **PATRÓN** `volumen_regimen` < `0.695` → IC=+0.303 (n=435)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.695 (IC base=-0.037)

- **PATRÓN** `volumen_pendiente_norm` > `0.1613` → IC=+0.300 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1613 (IC base=-0.037)

- **PATRÓN** `volumen_spike_ratio` < `2.456` → IC=+0.301 (n=919)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.456 (IC base=-0.037)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `ibs_20min` < `0.7813` → IC=-0.153 (n=3400)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7813
  - _Potencial_: sin este filtro IC_bueno=+0.122 (n=1756)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.167 (n=1145)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=4011)

- **FILTRO** `ibs_20min` > `0.7442` → IC=-0.196 (n=1797)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7442
  - _Potencial_: sin este filtro IC_bueno=+0.067 (n=5395)

- **PATRÓN** `ibs_20min` > `0.7813` → IC=+0.122 (n=1756)

  - _Acción_: Kelly boost +0.61€ cuando `ibs_20min` > 0.7813 (IC base=-0.059)

- **PATRÓN** `dist_vwap_pct` > `1.0473` → IC=+0.357 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0473 (IC base=-0.059)

- **PATRÓN** `volumen_regimen` > `0.7048` → IC=+0.317 (n=878)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7048 (IC base=-0.059)

- **PATRÓN** `volumen_pendiente_norm` < `0.1068` → IC=+0.306 (n=934)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1068 (IC base=-0.059)

- **PATRÓN** `volumen_spike_ratio` < `1.5796` → IC=+0.307 (n=423)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5796 (IC base=-0.059)

- **PATRÓN** `volumen_spike_ratio` > `2.5191` → IC=+0.320 (n=320)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5191 (IC base=-0.059)

- **PATRÓN** `dist_vwap_pct` > `0.8149` → IC=+0.279 (n=360)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8149 (IC base=+0.001)

- **PATRÓN** `dist_vwap_pct` < `0.223` → IC=+0.262 (n=2055)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.223 (IC base=+0.001)

- **PATRÓN** `volumen_regimen` < `0.6419` → IC=+0.272 (n=694)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6419 (IC base=+0.001)

- **PATRÓN** `volumen_regimen` > `1.0622` → IC=+0.281 (n=944)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0622 (IC base=+0.001)

- **PATRÓN** `volumen_pendiente_norm` > `0.1065` → IC=+0.280 (n=735)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1065 (IC base=+0.001)

- **PATRÓN** `volumen_spike_ratio` < `2.1776` → IC=+0.265 (n=1722)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1776 (IC base=+0.001)

- **PATRÓN** `volumen_spike_ratio` > `1.442` → IC=+0.269 (n=1956)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.442 (IC base=+0.001)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0106` → IC=+0.198 (n=7310)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0106 (IC base=+0.089)

- **PATRÓN** `ibs_20min` > `0.8712` → IC=+0.287 (n=9931)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8712 (IC base=+0.089)

- **PATRÓN** `dist_vwap_pct` > `0.6785` → IC=+0.300 (n=2083)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6785 (IC base=+0.089)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.505` → IC=+0.168 (n=9805)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 3.505 (IC base=+0.089)

- **PATRÓN** `volumen_regimen` > `0.6927` → IC=+0.276 (n=7185)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6927 (IC base=+0.089)

- **PATRÓN** `volumen_pendiente_norm` > `0.2942` → IC=+0.292 (n=1822)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2942 (IC base=+0.089)

- **PATRÓN** `volumen_spike_ratio` > `2.6493` → IC=+0.285 (n=4244)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6493 (IC base=+0.089)

- **PATRÓN** `ballena_activa_n` < `90.0` → IC=+0.308 (n=12354)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 90.0 (IC base=+0.089)

- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.157 (n=7048)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0101 (IC base=+0.081)

- **PATRÓN** `ibs_20min` < `0.6423` → IC=+0.153 (n=21118)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` < 0.6423 (IC base=+0.081)

- **PATRÓN** `dist_vwap_pct` < `0.2567` → IC=+0.277 (n=7064)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2567 (IC base=+0.081)

- **PATRÓN** `volumen_regimen` < `0.6989` → IC=+0.279 (n=3045)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6989 (IC base=+0.081)

- **PATRÓN** `volumen_regimen` > `1.1913` → IC=+0.277 (n=2307)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1913 (IC base=+0.081)

- **PATRÓN** `volumen_pendiente_norm` > `0.294` → IC=+0.324 (n=1529)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.294 (IC base=+0.081)

- **PATRÓN** `volumen_spike_ratio` < `1.4542` → IC=+0.301 (n=3398)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4542 (IC base=+0.081)

- **PATRÓN** `volumen_spike_ratio` > `2.2774` → IC=+0.298 (n=4617)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2774 (IC base=+0.081)

- **PATRÓN** `ballena_activa_n` < `73.0` → IC=+0.307 (n=10160)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 73.0 (IC base=+0.081)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.8018` → IC=-0.124 (n=3921)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8018
  - _Potencial_: sin este filtro IC_bueno=+0.296 (n=2022)

- **FILTRO** `ibs_20min` > `0.72` → IC=-0.233 (n=1303)

  - _Acción_: SKIP cuando `ibs_20min` > 0.72
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=3912)

- **FILTRO** `sigma_ewma_delta_pct` > `4.151` → IC=-0.232 (n=1123)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.151
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=4092)

- **PATRÓN** `ibs_20min` > `0.9348` → IC=+0.337 (n=1486)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9348 (IC base=+0.019)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.025` → IC=+0.189 (n=1987)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 3.025 (IC base=+0.019)

- **PATRÓN** `volumen_pendiente_norm` > `0.2294` → IC=+0.327 (n=385)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2294 (IC base=+0.019)

- **PATRÓN** `volumen_spike_ratio` < `1.4472` → IC=+0.279 (n=637)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4472 (IC base=+0.019)

- **PATRÓN** `volumen_spike_ratio` > `2.2427` → IC=+0.300 (n=865)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2427 (IC base=+0.019)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.316 (n=1291)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.019)

- **PATRÓN** `ibs_20min` < `0.1723` → IC=+0.164 (n=1304)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` < 0.1723 (IC base=-0.025)

- **PATRÓN** `volumen_pendiente_norm` < `0.1519` → IC=+0.399 (n=961)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1519 (IC base=-0.025)

- **PATRÓN** `volumen_spike_ratio` < `1.4225` → IC=+0.423 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4225 (IC base=-0.025)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.395 (n=953)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 23.0 (IC base=-0.025)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.3003` → IC=+0.225 (n=726)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3003 (IC base=+0.013)

- **PATRÓN** `volumen_regimen` < `1.1951` → IC=+0.207 (n=2138)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1951 (IC base=+0.013)

- **PATRÓN** `volumen_regimen` > `0.6949` → IC=+0.213 (n=1911)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6949 (IC base=+0.013)

- **PATRÓN** `volumen_pendiente_norm` > `0.277` → IC=+0.247 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.277 (IC base=+0.013)

- **PATRÓN** `volumen_spike_ratio` < `1.417` → IC=+0.229 (n=706)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.417 (IC base=+0.013)

- **PATRÓN** `volumen_spike_ratio` > `2.4477` → IC=+0.208 (n=704)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4477 (IC base=+0.013)

- **PATRÓN** `ballena_activa_n` < `263.0` → IC=+0.244 (n=1406)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 263.0 (IC base=+0.013)

- **PATRÓN** `dist_vwap_pct` < `0.1332` → IC=+0.252 (n=1500)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1332 (IC base=-0.004)

- **PATRÓN** `volumen_regimen` > `0.6194` → IC=+0.249 (n=1470)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6194 (IC base=-0.004)

- **PATRÓN** `volumen_pendiente_norm` > `0.2697` → IC=+0.301 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2697 (IC base=-0.004)

- **PATRÓN** `volumen_spike_ratio` < `1.5272` → IC=+0.252 (n=624)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5272 (IC base=-0.004)

- **PATRÓN** `volumen_spike_ratio` > `2.1427` → IC=+0.258 (n=643)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1427 (IC base=-0.004)

- **PATRÓN** `ballena_activa_n` < `190.0` → IC=+0.264 (n=476)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 190.0 (IC base=-0.004)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0093` → IC=+0.318 (n=2062)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0093 (IC base=+0.282)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.290 (n=3247)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.282)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.323 (n=1682)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.282)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.646` → IC=+0.313 (n=1037)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.646 (IC base=+0.282)

- **PATRÓN** `volumen_pendiente_norm` < `0.0976` → IC=+0.295 (n=2711)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0976 (IC base=+0.282)

- **PATRÓN** `volumen_spike_ratio` > `1.6063` → IC=+0.289 (n=3003)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6063 (IC base=+0.282)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.291 (n=3705)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.282)

- **PATRÓN** `libro_liquidez` > `2031.7184` → IC=+0.297 (n=1031)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2031.7184 (IC base=+0.282)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.307 (n=1865)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.282)

- **PATRÓN** `sigma_h` > `0.0074` → IC=+0.322 (n=2486)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0074 (IC base=+0.303)

- **PATRÓN** `drift_60min` |x|≤ `0.1781` → IC=+0.322 (n=1227)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1781 (IC base=+0.303)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.325 (n=1072)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.303)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.306 (n=1262)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.303)

- **PATRÓN** `ibs_20min` < `0.0148` → IC=+0.304 (n=1225)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0148 (IC base=+0.303)

- **PATRÓN** `ibs_20min` > `0.139` → IC=+0.313 (n=1855)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.139 (IC base=+0.303)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.242` → IC=+0.313 (n=341)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.242 (IC base=+0.303)

- **PATRÓN** `volumen_pendiente_norm` < `0.1987` → IC=+0.303 (n=2740)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1987 (IC base=+0.303)

- **PATRÓN** `volumen_pendiente_norm` > `0.3447` → IC=+0.310 (n=450)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3447 (IC base=+0.303)

- **PATRÓN** `volumen_spike_ratio` < `1.5923` → IC=+0.304 (n=894)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5923 (IC base=+0.303)

- **PATRÓN** `volumen_spike_ratio` > `2.7258` → IC=+0.319 (n=1216)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7258 (IC base=+0.303)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.305 (n=1412)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.303)

- **PATRÓN** `libro_liquidez` > `1912.76` → IC=+0.313 (n=1262)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1912.76 (IC base=+0.303)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.309 (n=2365)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 24.0 (IC base=+0.303)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7279` → IC=-0.182 (n=1370)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7279
  - _Potencial_: sin este filtro IC_bueno=+0.068 (n=4111)

- **PATRÓN** `ibs_20min` > `0.85` → IC=+0.161 (n=1344)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` > 0.85 (IC base=+0.022)

- **PATRÓN** `dist_vwap_pct` > `0.1447` → IC=+0.235 (n=1016)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1447 (IC base=+0.022)

- **PATRÓN** `dist_vwap_pct` < `0.3599` → IC=+0.233 (n=1888)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3599 (IC base=+0.022)

- **PATRÓN** `volumen_regimen` < `1.1596` → IC=+0.232 (n=1933)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1596 (IC base=+0.022)

- **PATRÓN** `volumen_regimen` > `0.6714` → IC=+0.231 (n=1726)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6714 (IC base=+0.022)

- **PATRÓN** `volumen_pendiente_norm` < `0.1626` → IC=+0.234 (n=2028)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1626 (IC base=+0.022)

- **PATRÓN** `volumen_pendiente_norm` > `0.103` → IC=+0.238 (n=628)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.103 (IC base=+0.022)

- **PATRÓN** `volumen_spike_ratio` < `2.4563` → IC=+0.235 (n=1873)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4563 (IC base=+0.022)

- **PATRÓN** `volumen_spike_ratio` > `1.5053` → IC=+0.232 (n=1673)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5053 (IC base=+0.022)

- **PATRÓN** `ballena_activa_n` < `115.0` → IC=+0.253 (n=1915)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 115.0 (IC base=+0.022)

- **PATRÓN** `dist_vwap_pct` > `0.7361` → IC=+0.253 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7361 (IC base=+0.005)

- **PATRÓN** `dist_vwap_pct` < `0.3522` → IC=+0.248 (n=1531)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3522 (IC base=+0.005)

- **PATRÓN** `volumen_regimen` < `1.1951` → IC=+0.253 (n=1381)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1951 (IC base=+0.005)

- **PATRÓN** `volumen_pendiente_norm` > `0.2812` → IC=+0.313 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2812 (IC base=+0.005)

- **PATRÓN** `volumen_spike_ratio` < `1.7888` → IC=+0.282 (n=883)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7888 (IC base=+0.005)

- **PATRÓN** `volumen_spike_ratio` > `2.4256` → IC=+0.273 (n=442)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4256 (IC base=+0.005)

- **PATRÓN** `ballena_activa_n` < `99.0` → IC=+0.278 (n=1184)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 99.0 (IC base=+0.005)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7431` → IC=-0.241 (n=2270)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7431
  - _Potencial_: sin este filtro IC_bueno=+0.312 (n=2270)

- **FILTRO** `ibs_20min` > `0.625` → IC=-0.230 (n=1078)

  - _Acción_: SKIP cuando `ibs_20min` > 0.625
  - _Potencial_: sin este filtro IC_bueno=+0.149 (n=3253)

- **FILTRO** `sigma_ewma_delta_pct` > `8.298` → IC=-0.253 (n=495)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.298
  - _Potencial_: sin este filtro IC_bueno=+0.094 (n=3836)

- **PATRÓN** `ibs_20min` > `0.7431` → IC=+0.312 (n=2270)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7431 (IC base=+0.036)

- **PATRÓN** `dist_vwap_pct` > `1.0495` → IC=+0.355 (n=337)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0495 (IC base=+0.036)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.469` → IC=+0.154 (n=1838)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 2.469 (IC base=+0.036)

- **PATRÓN** `volumen_regimen` < `0.8471` → IC=+0.342 (n=1107)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8471 (IC base=+0.036)

- **PATRÓN** `volumen_regimen` > `0.6986` → IC=+0.335 (n=1481)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6986 (IC base=+0.036)

- **PATRÓN** `volumen_pendiente_norm` < `0.1562` → IC=+0.335 (n=1714)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1562 (IC base=+0.036)

- **PATRÓN** `volumen_pendiente_norm` > `0.2747` → IC=+0.360 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2747 (IC base=+0.036)

- **PATRÓN** `volumen_spike_ratio` < `1.4268` → IC=+0.361 (n=537)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4268 (IC base=+0.036)

- **PATRÓN** `ballena_activa_n` < `45.0` → IC=+0.355 (n=1430)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 45.0 (IC base=+0.036)

- **PATRÓN** `ibs_20min` < `0.625` → IC=+0.149 (n=3253)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` < 0.625 (IC base=+0.055)

- **PATRÓN** `dist_vwap_pct` < `0.3042` → IC=+0.262 (n=1629)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3042 (IC base=+0.055)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.014` → IC=+0.128 (n=3054)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` < 3.014 (IC base=+0.055)

- **PATRÓN** `volumen_regimen` < `0.6914` → IC=+0.282 (n=705)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6914 (IC base=+0.055)

- **PATRÓN** `volumen_pendiente_norm` > `0.0706` → IC=+0.281 (n=634)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0706 (IC base=+0.055)

- **PATRÓN** `volumen_spike_ratio` < `2.4388` → IC=+0.268 (n=1549)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4388 (IC base=+0.055)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.282 (n=1578)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 47.0 (IC base=+0.055)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.358 (n=2067)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.315)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.317 (n=2339)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.315)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.318 (n=1101)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.315)

- **PATRÓN** `ibs_20min` > `0.6667` → IC=+0.344 (n=2318)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6667 (IC base=+0.315)

- **PATRÓN** `dist_vwap_pct` > `0.2114` → IC=+0.340 (n=1276)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2114 (IC base=+0.315)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.813` → IC=+0.333 (n=1117)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.813 (IC base=+0.315)

- **PATRÓN** `volumen_regimen` > `0.8714` → IC=+0.334 (n=1543)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8714 (IC base=+0.315)

- **PATRÓN** `volumen_pendiente_norm` > `0.2804` → IC=+0.346 (n=343)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2804 (IC base=+0.315)

- **PATRÓN** `volumen_spike_ratio` > `1.43` → IC=+0.327 (n=2228)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.43 (IC base=+0.315)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.344 (n=2068)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 40.0 (IC base=+0.315)

- **PATRÓN** `sigma_h` > `0.0154` → IC=+0.347 (n=1644)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0154 (IC base=+0.316)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.322 (n=1251)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.316)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.317 (n=1201)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.316)

- **PATRÓN** `ibs_20min` < `0.38` → IC=+0.335 (n=2466)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.38 (IC base=+0.316)

- **PATRÓN** `dist_vwap_pct` < `0.2414` → IC=+0.321 (n=2385)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2414 (IC base=+0.316)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.64` → IC=+0.329 (n=918)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.64 (IC base=+0.316)

- **PATRÓN** `volumen_regimen` < `0.7186` → IC=+0.321 (n=1085)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7186 (IC base=+0.316)

- **PATRÓN** `volumen_regimen` > `1.2096` → IC=+0.343 (n=822)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2096 (IC base=+0.316)

- **PATRÓN** `volumen_pendiente_norm` > `0.2295` → IC=+0.362 (n=461)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2295 (IC base=+0.316)

- **PATRÓN** `volumen_spike_ratio` < `1.4118` → IC=+0.323 (n=762)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4118 (IC base=+0.316)

- **PATRÓN** `volumen_spike_ratio` > `2.1375` → IC=+0.317 (n=1035)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1375 (IC base=+0.316)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0124` → IC=+0.224 (n=5453)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0124 (IC base=+0.175)

- **PATRÓN** `drift_60min` |x|≤ `0.0876` → IC=+0.194 (n=5448)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.0876 (IC base=+0.175)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.184 (n=16930)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.175)

- **PATRÓN** `ibs_20min` > `0.5392` → IC=+0.231 (n=16340)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5392 (IC base=+0.175)

- **PATRÓN** `dist_vwap_pct` > `0.1624` → IC=+0.206 (n=6342)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1624 (IC base=+0.175)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.852` → IC=+0.259 (n=3187)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.852 (IC base=+0.175)

- **PATRÓN** `volumen_regimen` < `1.1837` → IC=+0.155 (n=10882)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.1837 (IC base=+0.175)

- **PATRÓN** `volumen_regimen` > `0.6257` → IC=+0.154 (n=10883)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 0.6257 (IC base=+0.175)

- **PATRÓN** `volumen_pendiente_norm` > `0.2942` → IC=+0.207 (n=2367)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2942 (IC base=+0.175)

- **PATRÓN** `volumen_spike_ratio` > `2.6084` → IC=+0.189 (n=5295)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 2.6084 (IC base=+0.175)

- **PATRÓN** `ballena_activa_n` < `88.0` → IC=+0.194 (n=15255)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 88.0 (IC base=+0.175)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.191 (n=7059)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0058 (IC base=+0.181)

- **PATRÓN** `drift_60min` |x|≤ `0.0806` → IC=+0.219 (n=5332)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0806 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.210 (n=6051)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` < `0.523` → IC=+0.238 (n=15986)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.523 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` < `0.1819` → IC=+0.176 (n=11529)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.1819 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.615` → IC=+0.190 (n=2549)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 9.615 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.542` → IC=+0.188 (n=14222)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` < 2.542 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `1.181` → IC=+0.163 (n=11386)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.181 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.2934` → IC=+0.216 (n=2391)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2934 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `2.6297` → IC=+0.189 (n=5063)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 2.6297 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `92.0` → IC=+0.196 (n=14953)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 92.0 (IC base=+0.181)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.227 (n=900)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0056 (IC base=+0.227)

- **PATRÓN** `drift_60min` |x|≤ `0.1047` → IC=+0.257 (n=1184)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1047 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.232 (n=2795)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.227)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.230 (n=1828)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.227)

- **PATRÓN** `ibs_20min` > `0.8113` → IC=+0.273 (n=2402)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8113 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.568` → IC=+0.331 (n=873)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.568 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` > `0.2807` → IC=+0.296 (n=405)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2807 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` < `1.834` → IC=+0.223 (n=1708)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.834 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` > `1.4341` → IC=+0.228 (n=2562)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4341 (IC base=+0.227)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.238 (n=2975)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.227)

- **PATRÓN** `sigma_h` < `0.0095` → IC=+0.257 (n=2177)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0095 (IC base=+0.253)

- **PATRÓN** `drift_60min` |x|≤ `0.0973` → IC=+0.307 (n=958)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0973 (IC base=+0.253)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.258 (n=2245)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.253)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.260 (n=1038)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.253)

- **PATRÓN** `ibs_20min` < `0.0486` → IC=+0.299 (n=958)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0486 (IC base=+0.253)

- **PATRÓN** `volumen_pendiente_norm` < `0.0993` → IC=+0.256 (n=1911)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0993 (IC base=+0.253)

- **PATRÓN** `volumen_pendiente_norm` > `0.3015` → IC=+0.272 (n=331)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3015 (IC base=+0.253)

- **PATRÓN** `volumen_spike_ratio` < `1.4456` → IC=+0.276 (n=694)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4456 (IC base=+0.253)

- **PATRÓN** `volumen_spike_ratio` > `2.7028` → IC=+0.257 (n=693)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7028 (IC base=+0.253)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.256 (n=2506)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.253)

- **PATRÓN** `libro_liquidez` > `1927.5038` → IC=+0.259 (n=986)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1927.5038 (IC base=+0.253)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.199 (n=834)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0031 (IC base=+0.132)

- **PATRÓN** `drift_60min` |x|≤ `0.0657` → IC=+0.177 (n=831)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.0657 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.148 (n=2606)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 5.0 (IC base=+0.132)

- **PATRÓN** `ibs_20min` > `0.2644` → IC=+0.208 (n=2493)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2644 (IC base=+0.132)

- **PATRÓN** `dist_vwap_pct` > `0.1844` → IC=+0.212 (n=1269)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1844 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.762` → IC=+0.207 (n=455)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.762 (IC base=+0.132)

- **PATRÓN** `volumen_regimen` < `0.6953` → IC=+0.140 (n=1097)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 0.6953 (IC base=+0.132)

- **PATRÓN** `volumen_regimen` > `1.0601` → IC=+0.137 (n=1130)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` > 1.0601 (IC base=+0.132)

- **PATRÓN** `volumen_pendiente_norm` > `0.2807` → IC=+0.179 (n=387)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.2807 (IC base=+0.132)

- **PATRÓN** `volumen_spike_ratio` < `1.5028` → IC=+0.140 (n=1078)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.5028 (IC base=+0.132)

- **PATRÓN** `volumen_spike_ratio` > `2.4677` → IC=+0.149 (n=816)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 2.4677 (IC base=+0.132)

- **PATRÓN** `ballena_activa_n` < `402.0` → IC=+0.137 (n=2416)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 402.0 (IC base=+0.132)

- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.171 (n=2636)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0064 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.2383` → IC=+0.168 (n=2320)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.2383 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.182 (n=1000)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 17.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` < `0.6109` → IC=+0.206 (n=2636)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6109 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.972` → IC=+0.175 (n=494)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 10.972 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.03` → IC=+0.149 (n=2304)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 4.03 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` < `1.2024` → IC=+0.159 (n=2636)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.2024 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` < `0.0934` → IC=+0.147 (n=2283)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` < 0.0934 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `2.452` → IC=+0.149 (n=2512)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 2.452 (IC base=+0.145)

- **PATRÓN** `ballena_activa_n` < `212.0` → IC=+0.182 (n=1081)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 212.0 (IC base=+0.145)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0115` → IC=+0.232 (n=1259)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0115 (IC base=+0.211)

- **PATRÓN** `drift_60min` |x|≤ `0.3954` → IC=+0.225 (n=2437)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3954 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.217 (n=2879)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.293 (n=1467)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.139` → IC=+0.304 (n=656)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.139 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.353` → IC=+0.237 (n=393)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.353 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `2.7154` → IC=+0.225 (n=1225)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7154 (IC base=+0.211)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.216 (n=3344)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `1917.81` → IC=+0.223 (n=1256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1917.81 (IC base=+0.211)

- **PATRÓN** `sigma_h` < `0.0107` → IC=+0.247 (n=2135)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0107 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.4161` → IC=+0.260 (n=2134)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4161 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.280 (n=933)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` < `0.0323` → IC=+0.289 (n=1067)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0323 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.126` → IC=+0.282 (n=328)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.126 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.3584` → IC=+0.286 (n=405)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3584 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` < `1.7668` → IC=+0.241 (n=1029)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7668 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `2.1795` → IC=+0.247 (n=1559)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1795 (IC base=+0.237)

- **PATRÓN** `libro_liquidez` > `1904.2932` → IC=+0.251 (n=1100)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1904.2932 (IC base=+0.237)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.241 (n=1553)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.237)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.208 (n=901)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.132)

- **PATRÓN** `drift_60min` |x|≤ `0.0786` → IC=+0.189 (n=897)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.0786 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.141 (n=2781)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 5.0 (IC base=+0.132)

- **PATRÓN** `ibs_20min` > `0.256` → IC=+0.193 (n=2688)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.256 (IC base=+0.132)

- **PATRÓN** `dist_vwap_pct` > `0.1399` → IC=+0.186 (n=1580)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1399 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.367` → IC=+0.197 (n=463)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 11.367 (IC base=+0.132)

- **PATRÓN** `volumen_regimen` < `0.8447` → IC=+0.137 (n=1793)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 0.8447 (IC base=+0.132)

- **PATRÓN** `volumen_regimen` > `1.1837` → IC=+0.134 (n=896)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` > 1.1837 (IC base=+0.132)

- **PATRÓN** `volumen_pendiente_norm` > `0.2887` → IC=+0.175 (n=404)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.2887 (IC base=+0.132)

- **PATRÓN** `volumen_spike_ratio` < `1.8232` → IC=+0.131 (n=1755)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 1.8232 (IC base=+0.132)

- **PATRÓN** `volumen_spike_ratio` > `2.516` → IC=+0.152 (n=878)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 2.516 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `6915.1659` → IC=+0.195 (n=1219)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 6915.1659 (IC base=+0.132)

- **PATRÓN** `ballena_activa_n` < `128.0` → IC=+0.137 (n=2627)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 128.0 (IC base=+0.132)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.164 (n=2511)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0066 (IC base=+0.127)

- **PATRÓN** `drift_60min` |x|≤ `0.3957` → IC=+0.143 (n=2851)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.3957 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.161 (n=1367)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 15.0 (IC base=+0.127)

- **PATRÓN** `ibs_20min` < `0.6774` → IC=+0.184 (n=2851)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.6774 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` < `0.1602` → IC=+0.155 (n=2865)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1602 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.312` → IC=+0.142 (n=682)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 9.312 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` < `0.8509` → IC=+0.151 (n=1902)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.8509 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` > `0.2942` → IC=+0.173 (n=423)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.2942 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` < `2.2` → IC=+0.130 (n=2377)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 2.2 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` > `1.4171` → IC=+0.127 (n=2701)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` > 1.4171 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `6344.3973` → IC=+0.189 (n=1293)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 6344.3973 (IC base=+0.127)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.147 (n=891)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 49.0 (IC base=+0.127)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.166 (n=1358)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.0112 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.158 (n=1428)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 15.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` > `0.4737` → IC=+0.207 (n=2993)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4737 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` > `0.1961` → IC=+0.190 (n=1650)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.1961 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.085` → IC=+0.290 (n=630)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.085 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` < `1.1736` → IC=+0.133 (n=2992)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 1.1736 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` > `0.7037` → IC=+0.123 (n=2673)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` > 0.7037 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` < `0.1633` → IC=+0.128 (n=3049)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` < 0.1633 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` < `1.5416` → IC=+0.131 (n=1278)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 1.5416 (IC base=+0.122)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.125 (n=3128)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.02 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `2667.5823` → IC=+0.199 (n=1357)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2667.5823 (IC base=+0.122)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.146 (n=1263)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 20.0 (IC base=+0.122)

- **PATRÓN** `sigma_h` < `0.0119` → IC=+0.141 (n=3124)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.0119 (IC base=+0.118)

- **PATRÓN** `drift_60min` |x|≤ `0.1119` → IC=+0.161 (n=1040)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.1119 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.134 (n=3185)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 5.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` < `0.65` → IC=+0.219 (n=3122)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.65 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` < `0.2101` → IC=+0.144 (n=3031)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.2101 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.279` → IC=+0.139 (n=2754)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 2.279 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` < `1.1736` → IC=+0.128 (n=3118)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 1.1736 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` > `0.2739` → IC=+0.138 (n=426)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_pendiente_norm` > 0.2739 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` < `1.432` → IC=+0.132 (n=981)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 1.432 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` > `2.4248` → IC=+0.126 (n=981)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` > 2.4248 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `2910.8784` → IC=+0.192 (n=1040)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 2910.8784 (IC base=+0.118)

- **PATRÓN** `ballena_activa_n` < `45.0` → IC=+0.124 (n=2922)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 45.0 (IC base=+0.118)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.247 (n=2710)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0107 (IC base=+0.225)

- **PATRÓN** `drift_60min` |x|≤ `0.1665` → IC=+0.239 (n=1192)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1665 (IC base=+0.225)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.229 (n=2811)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.229 (n=2447)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.225)

- **PATRÓN** `ibs_20min` > `0.6667` → IC=+0.258 (n=2714)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6667 (IC base=+0.225)

- **PATRÓN** `dist_vwap_pct` > `0.1809` → IC=+0.234 (n=1692)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1809 (IC base=+0.225)

- **PATRÓN** `dist_vwap_pct` < `0.8208` → IC=+0.226 (n=2787)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.8208 (IC base=+0.225)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.65` → IC=+0.252 (n=1365)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.65 (IC base=+0.225)

- **PATRÓN** `volumen_regimen` > `0.6249` → IC=+0.233 (n=2710)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6249 (IC base=+0.225)

- **PATRÓN** `volumen_pendiente_norm` > `0.2353` → IC=+0.270 (n=506)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2353 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` < `2.47` → IC=+0.228 (n=2641)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.47 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` > `1.8145` → IC=+0.233 (n=1761)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8145 (IC base=+0.225)

- **PATRÓN** `sigma_h` < `0.0128` → IC=+0.241 (n=1224)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0128 (IC base=+0.238)

- **PATRÓN** `sigma_h` > `0.0179` → IC=+0.245 (n=1855)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0179 (IC base=+0.238)

- **PATRÓN** `drift_60min` |x|≤ `0.5735` → IC=+0.246 (n=2782)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5735 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.251 (n=1371)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.238)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.244 (n=1246)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.238)

- **PATRÓN** `ibs_20min` < `0.44` → IC=+0.263 (n=2794)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.44 (IC base=+0.238)

- **PATRÓN** `dist_vwap_pct` > `1.1432` → IC=+0.258 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1432 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.021` → IC=+0.264 (n=388)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.021 (IC base=+0.238)

- **PATRÓN** `volumen_regimen` < `0.864` → IC=+0.244 (n=1855)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.864 (IC base=+0.238)

- **PATRÓN** `volumen_regimen` > `0.6401` → IC=+0.241 (n=2782)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6401 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` > `0.2804` → IC=+0.287 (n=383)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2804 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` < `2.527` → IC=+0.235 (n=2617)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.527 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` > `1.436` → IC=+0.239 (n=2617)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.436 (IC base=+0.238)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.211 (n=1415)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.162)

- **PATRÓN** `drift_60min` |x|≤ `0.1327` → IC=+0.176 (n=1858)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.1327 (IC base=+0.162)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.173 (n=4421)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 5.0 (IC base=+0.162)

- **PATRÓN** `ibs_20min` > `0.31` → IC=+0.197 (n=4222)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.31 (IC base=+0.162)

- **PATRÓN** `dist_vwap_pct` > `0.2206` → IC=+0.185 (n=1656)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.2206 (IC base=+0.162)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.645` → IC=+0.208 (n=691)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.645 (IC base=+0.162)

- **PATRÓN** `volumen_regimen` < `0.8616` → IC=+0.172 (n=2566)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` < 0.8616 (IC base=+0.162)

- **PATRÓN** `volumen_regimen` > `1.1928` → IC=+0.171 (n=1283)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` > 1.1928 (IC base=+0.162)

- **PATRÓN** `volumen_pendiente_norm` > `0.0739` → IC=+0.173 (n=1698)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.0739 (IC base=+0.162)

- **PATRÓN** `volumen_spike_ratio` < `1.5284` → IC=+0.168 (n=1810)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 1.5284 (IC base=+0.162)

- **PATRÓN** `volumen_spike_ratio` > `2.4779` → IC=+0.164 (n=1371)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 2.4779 (IC base=+0.162)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.164 (n=4725)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.02 (IC base=+0.162)

- **PATRÓN** `libro_liquidez` > `2663.9798` → IC=+0.173 (n=3771)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 2663.9798 (IC base=+0.162)

- **PATRÓN** `ibs_20min` < `0.3846` → IC=+0.170 (n=3029)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.3846 (IC base=+0.092)

- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.136 (n=1938)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 25.0 (IC base=+0.092)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.195 (n=1126)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0061 (IC base=+0.179)

- **PATRÓN** `drift_60min` |x|≤ `0.3283` → IC=+0.197 (n=1124)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.3283 (IC base=+0.179)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.213 (n=1015)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.179)

- **PATRÓN** `ibs_20min` > `0.2144` → IC=+0.212 (n=1124)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2144 (IC base=+0.179)

- **PATRÓN** `dist_vwap_pct` > `0.3087` → IC=+0.213 (n=340)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3087 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.949` → IC=+0.206 (n=492)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.949 (IC base=+0.179)

- **PATRÓN** `volumen_regimen` < `0.8803` → IC=+0.192 (n=752)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 0.8803 (IC base=+0.179)

- **PATRÓN** `volumen_pendiente_norm` < `0.1499` → IC=+0.181 (n=1183)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` < 0.1499 (IC base=+0.179)

- **PATRÓN** `volumen_pendiente_norm` > `0.0703` → IC=+0.191 (n=442)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.0703 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` < `2.1675` → IC=+0.194 (n=970)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 2.1675 (IC base=+0.179)

- **PATRÓN** `libro_liquidez` > `15815.8495` → IC=+0.191 (n=510)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 15815.8495 (IC base=+0.179)

- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.165 (n=463)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0031 (IC base=+0.092)

- **PATRÓN** `ibs_20min` < `0.1959` → IC=+0.201 (n=607)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1959 (IC base=+0.092)

- **PATRÓN** `volumen_pendiente_norm` > `0.1604` → IC=+0.138 (n=360)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_pendiente_norm` > 0.1604 (IC base=+0.092)

- **PATRÓN** `ballena_activa_n` < `162.0` → IC=+0.179 (n=599)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 162.0 (IC base=+0.092)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.243 (n=577)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.170)

- **PATRÓN** `drift_60min` |x|≤ `0.2101` → IC=+0.174 (n=873)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.2101 (IC base=+0.170)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.186 (n=1363)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.170)

- **PATRÓN** `ibs_20min` > `0.8071` → IC=+0.266 (n=593)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8071 (IC base=+0.170)

- **PATRÓN** `dist_vwap_pct` > `0.8227` → IC=+0.191 (n=221)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.8227 (IC base=+0.170)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.882` → IC=+0.213 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.882 (IC base=+0.170)

- **PATRÓN** `volumen_regimen` < `0.8313` → IC=+0.179 (n=873)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` < 0.8313 (IC base=+0.170)

- **PATRÓN** `volumen_regimen` > `1.156` → IC=+0.171 (n=436)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` > 1.156 (IC base=+0.170)

- **PATRÓN** `volumen_pendiente_norm` > `0.2202` → IC=+0.209 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2202 (IC base=+0.170)

- **PATRÓN** `volumen_spike_ratio` > `2.4761` → IC=+0.192 (n=430)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.4761 (IC base=+0.170)

- **PATRÓN** `libro_liquidez` > `8299.7653` → IC=+0.174 (n=593)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 8299.7653 (IC base=+0.170)

- **PATRÓN** `ibs_20min` < `0.0929` → IC=+0.190 (n=427)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.0929 (IC base=+0.081)

- **PATRÓN** `libro_liquidez` > `5163.6795` → IC=+0.136 (n=853)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 5163.6795 (IC base=+0.081)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.123 (n=544)

  - _Acción_: Kelly boost +0.61€ cuando `ballena_activa_n` < 42.0 (IC base=+0.081)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` < `0.0073` → IC=+0.153 (n=462)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0073 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.167 (n=737)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 11.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` > `0.4595` → IC=+0.183 (n=1047)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.4595 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` > `0.9532` → IC=+0.196 (n=179)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.9532 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.915` → IC=+0.231 (n=415)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.915 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` < `1.0475` → IC=+0.134 (n=922)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 1.0475 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` > `0.7037` → IC=+0.137 (n=937)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` > 0.7037 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` > `0.2259` → IC=+0.156 (n=193)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` > 0.2259 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` < `2.4099` → IC=+0.130 (n=1013)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 2.4099 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` > `1.8035` → IC=+0.125 (n=675)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` > 1.8035 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.129 (n=1098)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.02 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `2733.5431` → IC=+0.165 (n=475)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 2733.5431 (IC base=+0.125)

- **PATRÓN** `ibs_20min` < `0.3667` → IC=+0.183 (n=758)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.3667 (IC base=+0.063)

- **PATRÓN** `libro_liquidez` > `2620.5349` → IC=+0.151 (n=514)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 2620.5349 (IC base=+0.063)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0118` → IC=+0.227 (n=328)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0118 (IC base=+0.195)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.240 (n=171)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.195)

- **PATRÓN** `ibs_20min` > `0.5524` → IC=+0.218 (n=328)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5524 (IC base=+0.195)

- **PATRÓN** `dist_vwap_pct` > `0.2223` → IC=+0.217 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2223 (IC base=+0.195)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.732` → IC=+0.215 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.732 (IC base=+0.195)

- **PATRÓN** `volumen_regimen` > `1.1874` → IC=+0.268 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1874 (IC base=+0.195)

- **PATRÓN** `volumen_pendiente_norm` < `0.1036` → IC=+0.206 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1036 (IC base=+0.195)

- **PATRÓN** `volumen_spike_ratio` < `1.8284` → IC=+0.219 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8284 (IC base=+0.195)

- **PATRÓN** `volumen_spike_ratio` > `1.5387` → IC=+0.205 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5387 (IC base=+0.195)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.203 (n=402)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.195)

- **PATRÓN** `libro_liquidez` > `3014.8723` → IC=+0.204 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3014.8723 (IC base=+0.195)

- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.161 (n=399)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0113 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.3039` → IC=+0.151 (n=267)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.3039 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.196 (n=192)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 15.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.162 (n=353)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` < 0.5 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` > `1.2295` → IC=+0.300 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2295 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.17` → IC=+0.167 (n=106)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 5.17 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.238` → IC=+0.147 (n=358)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 2.238 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `0.8805` → IC=+0.188 (n=267)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 0.8805 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` < `0.1134` → IC=+0.162 (n=368)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` < 0.1134 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` > `0.2302` → IC=+0.184 (n=74)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.2302 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `1.5142` → IC=+0.208 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5142 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `2.6761` → IC=+0.162 (n=128)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 2.6761 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.159 (n=382)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 20.0 (IC base=+0.144)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0124` → IC=+0.230 (n=7126)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0124 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.189 (n=22274)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` > `0.432` → IC=+0.228 (n=21381)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.432 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` > `0.8904` → IC=+0.214 (n=2576)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8904 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.99` → IC=+0.255 (n=5233)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.99 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` < `1.2161` → IC=+0.160 (n=14385)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2161 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.2413` → IC=+0.207 (n=3841)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2413 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `2.6186` → IC=+0.194 (n=6955)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.6186 (IC base=+0.180)

- **PATRÓN** `ballena_activa_n` < `104.0` → IC=+0.202 (n=20018)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 104.0 (IC base=+0.180)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.198 (n=8636)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.006 (IC base=+0.193)

- **PATRÓN** `sigma_h` > `0.0122` → IC=+0.201 (n=6532)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0122 (IC base=+0.193)

- **PATRÓN** `drift_60min` |x|≤ `0.4821` → IC=+0.196 (n=19590)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.4821 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.214 (n=7337)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.193)

- **PATRÓN** `ibs_20min` < `0.5911` → IC=+0.243 (n=19590)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5911 (IC base=+0.193)

- **PATRÓN** `dist_vwap_pct` < `0.1793` → IC=+0.175 (n=12252)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.1793 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.474` → IC=+0.195 (n=2650)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 9.474 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.416` → IC=+0.198 (n=19082)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` < 3.416 (IC base=+0.193)

- **PATRÓN** `volumen_regimen` < `0.7016` → IC=+0.174 (n=5791)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.7016 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` > `0.2916` → IC=+0.249 (n=2684)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2916 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` > `2.6244` → IC=+0.204 (n=6241)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6244 (IC base=+0.193)

- **PATRÓN** `ballena_activa_n` < `92.0` → IC=+0.209 (n=18478)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 92.0 (IC base=+0.193)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.249 (n=1662)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.235)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.236 (n=2313)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.235)

- **PATRÓN** `ibs_20min` > `0.8634` → IC=+0.300 (n=2286)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8634 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.591` → IC=+0.337 (n=1120)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.591 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` > `0.2325` → IC=+0.298 (n=613)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2325 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` > `2.2901` → IC=+0.242 (n=1500)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2901 (IC base=+0.235)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.251 (n=3750)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.235)

- **PATRÓN** `libro_liquidez` > `2050.02` → IC=+0.236 (n=1143)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2050.02 (IC base=+0.235)

- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.258 (n=1175)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 8.0 (IC base=+0.235)

- **PATRÓN** `sigma_h` < `0.01` → IC=+0.268 (n=3044)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.01 (IC base=+0.266)

- **PATRÓN** `drift_60min` |x|≤ `0.1223` → IC=+0.290 (n=1338)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1223 (IC base=+0.266)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.269 (n=2801)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.266)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.267 (n=2755)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.266)

- **PATRÓN** `ibs_20min` < `0.5404` → IC=+0.284 (n=3041)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5404 (IC base=+0.266)

- **PATRÓN** `volumen_pendiente_norm` < `0.0975` → IC=+0.269 (n=2765)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0975 (IC base=+0.266)

- **PATRÓN** `volumen_pendiente_norm` > `0.289` → IC=+0.282 (n=429)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.289 (IC base=+0.266)

- **PATRÓN** `volumen_spike_ratio` < `1.5594` → IC=+0.267 (n=1282)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5594 (IC base=+0.266)

- **PATRÓN** `volumen_spike_ratio` > `2.6495` → IC=+0.275 (n=971)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6495 (IC base=+0.266)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.271 (n=2111)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.266)

- **PATRÓN** `libro_liquidez` > `1785.4165` → IC=+0.273 (n=2027)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1785.4165 (IC base=+0.266)

- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.273 (n=1037)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 8.0 (IC base=+0.266)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.178 (n=1170)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0031 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.0787` → IC=+0.148 (n=1168)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.0787 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.147 (n=3647)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 5.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` > `0.203` → IC=+0.188 (n=3502)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.203 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.1804` → IC=+0.192 (n=1525)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.1804 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.221` → IC=+0.163 (n=561)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 11.221 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `0.6358` → IC=+0.155 (n=1168)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.6358 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` > `1.0696` → IC=+0.139 (n=1588)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` > 1.0696 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.2707` → IC=+0.178 (n=498)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.2707 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `2.1536` → IC=+0.141 (n=3025)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 2.1536 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `1.5154` → IC=+0.141 (n=3070)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 1.5154 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `303.0` → IC=+0.151 (n=2253)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 303.0 (IC base=+0.136)

- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.162 (n=2997)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0064 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.3258` → IC=+0.145 (n=2995)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.3258 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.165 (n=1102)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 17.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` < `0.6816` → IC=+0.184 (n=2995)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.6816 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.045` → IC=+0.136 (n=1429)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` > 3.045 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.024` → IC=+0.137 (n=2712)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 4.024 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `1.0503` → IC=+0.149 (n=2636)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 1.0503 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.2189` → IC=+0.192 (n=554)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2189 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `2.42` → IC=+0.140 (n=2886)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 2.42 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `1.767` → IC=+0.140 (n=1924)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 1.767 (IC base=+0.136)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.137 (n=3890)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `226.0` → IC=+0.150 (n=936)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 226.0 (IC base=+0.136)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.013` → IC=+0.250 (n=1188)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.013 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.234 (n=3730)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.226)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.228 (n=3191)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.226)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.303 (n=1338)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.085` → IC=+0.325 (n=790)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.085 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` < `0.0974` → IC=+0.228 (n=3189)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0974 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` > `2.732` → IC=+0.241 (n=1579)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.732 (IC base=+0.226)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.233 (n=4297)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.226)

- **PATRÓN** `libro_liquidez` > `2031.6` → IC=+0.239 (n=1188)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2031.6 (IC base=+0.226)

- **PATRÓN** `sigma_h` < `0.011` → IC=+0.248 (n=2982)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.011 (IC base=+0.242)

- **PATRÓN** `drift_60min` |x|≤ `0.179` → IC=+0.263 (n=1492)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.179 (IC base=+0.242)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.263 (n=1292)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.242)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.242 (n=1551)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.242)

- **PATRÓN** `ibs_20min` < `0.0566` → IC=+0.303 (n=1131)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0566 (IC base=+0.242)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.216` → IC=+0.303 (n=363)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.216 (IC base=+0.242)

- **PATRÓN** `volumen_pendiente_norm` > `0.3487` → IC=+0.303 (n=506)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3487 (IC base=+0.242)

- **PATRÓN** `volumen_spike_ratio` > `2.1698` → IC=+0.254 (n=2173)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1698 (IC base=+0.242)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.248 (n=1726)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.242)

- **PATRÓN** `libro_liquidez` > `1909.8776` → IC=+0.254 (n=1537)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1909.8776 (IC base=+0.242)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.247 (n=2835)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 23.0 (IC base=+0.242)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.194 (n=1235)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0037 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.4327` → IC=+0.145 (n=3694)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.4327 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.147 (n=3831)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 5.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` > `0.8908` → IC=+0.272 (n=1232)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8908 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` > `0.1961` → IC=+0.167 (n=1705)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1961 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.986` → IC=+0.156 (n=1641)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 2.986 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `0.8601` → IC=+0.149 (n=2463)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.8601 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.2329` → IC=+0.184 (n=656)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.2329 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `1.5176` → IC=+0.149 (n=1589)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.5176 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `2.1727` → IC=+0.145 (n=1637)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 2.1727 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `5516.8147` → IC=+0.227 (n=1675)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5516.8147 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `89.0` → IC=+0.144 (n=2387)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 89.0 (IC base=+0.137)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.166 (n=2727)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0067 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.4377` → IC=+0.151 (n=3099)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.4377 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.168 (n=1143)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 17.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` < `0.5809` → IC=+0.209 (n=2727)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5809 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` < `0.1525` → IC=+0.156 (n=2879)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1525 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.877` → IC=+0.151 (n=459)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 10.877 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.059` → IC=+0.145 (n=2699)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 3.059 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` < `0.6885` → IC=+0.160 (n=1364)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.6885 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` > `0.2916` → IC=+0.210 (n=391)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2916 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` < `2.2078` → IC=+0.145 (n=2632)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.2078 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` > `1.5326` → IC=+0.150 (n=2672)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.5326 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `6390.1468` → IC=+0.216 (n=1033)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6390.1468 (IC base=+0.141)

- **PATRÓN** `ballena_activa_n` < `92.0` → IC=+0.153 (n=2032)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 92.0 (IC base=+0.141)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.148 (n=1698)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` > 0.0113 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.149 (n=2639)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 11.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` > `0.4324` → IC=+0.191 (n=3741)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.4324 (IC base=+0.119)

- **PATRÓN** `dist_vwap_pct` > `1.0143` → IC=+0.204 (n=619)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0143 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.312` → IC=+0.269 (n=951)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.312 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` < `1.2133` → IC=+0.126 (n=3741)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` < 1.2133 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` < `0.1011` → IC=+0.122 (n=3554)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_pendiente_norm` < 0.1011 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` < `2.491` → IC=+0.122 (n=3655)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` < 2.491 (IC base=+0.119)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.121 (n=3922)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.02 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `2721.3768` → IC=+0.241 (n=1247)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2721.3768 (IC base=+0.119)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.132 (n=1231)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 20.0 (IC base=+0.119)

- **PATRÓN** `sigma_h` < `0.0108` → IC=+0.154 (n=3102)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0108 (IC base=+0.127)

- **PATRÓN** `drift_60min` |x|≤ `0.1373` → IC=+0.155 (n=1175)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.1373 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.164 (n=1659)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 15.0 (IC base=+0.127)

- **PATRÓN** `ibs_20min` < `0.6667` → IC=+0.215 (n=3545)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6667 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` < `0.217` → IC=+0.143 (n=3167)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.217 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.072` → IC=+0.151 (n=3412)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 3.072 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` < `0.6369` → IC=+0.155 (n=1175)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.6369 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` > `0.2253` → IC=+0.176 (n=613)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.2253 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` < `1.4331` → IC=+0.156 (n=1114)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.4331 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `2628.0169` → IC=+0.209 (n=1175)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2628.0169 (IC base=+0.127)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.141 (n=2985)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 43.0 (IC base=+0.127)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0114` → IC=+0.258 (n=3451)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0114 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.242 (n=3603)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.237)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.243 (n=2307)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` > `0.6152` → IC=+0.272 (n=3081)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6152 (IC base=+0.237)

- **PATRÓN** `dist_vwap_pct` > `0.1944` → IC=+0.253 (n=1810)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1944 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.208` → IC=+0.286 (n=595)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.208 (IC base=+0.237)

- **PATRÓN** `volumen_regimen` < `1.2203` → IC=+0.239 (n=3449)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2203 (IC base=+0.237)

- **PATRÓN** `volumen_regimen` > `0.6436` → IC=+0.241 (n=3449)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6436 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.2388` → IC=+0.258 (n=596)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2388 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `2.4962` → IC=+0.257 (n=1124)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4962 (IC base=+0.237)

- **PATRÓN** `sigma_h` > `0.0259` → IC=+0.267 (n=1182)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0259 (IC base=+0.241)

- **PATRÓN** `drift_60min` |x|≤ `0.6292` → IC=+0.241 (n=3545)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6292 (IC base=+0.241)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.246 (n=3338)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.241)

- **PATRÓN** `ibs_20min` < `0.52` → IC=+0.272 (n=3544)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.52 (IC base=+0.241)

- **PATRÓN** `dist_vwap_pct` < `0.2194` → IC=+0.247 (n=3349)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2194 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.141` → IC=+0.278 (n=683)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.141 (IC base=+0.241)

- **PATRÓN** `volumen_regimen` < `0.7157` → IC=+0.241 (n=1560)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7157 (IC base=+0.241)

- **PATRÓN** `volumen_regimen` > `1.2151` → IC=+0.261 (n=1182)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2151 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` > `0.2849` → IC=+0.298 (n=488)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2849 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` > `1.4345` → IC=+0.244 (n=3334)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4345 (IC base=+0.241)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.200 (n=5777)

- **PATRÓN** `sigma_h` < `0.005` → IC=+0.244 (n=1986)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.218)

- **PATRÓN** `drift_60min` |x|≤ `0.5053` → IC=+0.226 (n=5942)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5053 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.232 (n=2149)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.218)

- **PATRÓN** `ibs_20min` > `0.9347` → IC=+0.256 (n=1980)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9347 (IC base=+0.218)

- **PATRÓN** `dist_vwap_pct` < `0.4291` → IC=+0.221 (n=4332)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4291 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.629` → IC=+0.224 (n=2938)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.629 (IC base=+0.218)

- **PATRÓN** `volumen_regimen` < `0.7088` → IC=+0.228 (n=1930)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7088 (IC base=+0.218)

- **PATRÓN** `volumen_regimen` > `0.8843` → IC=+0.219 (n=2924)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8843 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` < `0.105` → IC=+0.218 (n=5539)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.105 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` > `0.1652` → IC=+0.224 (n=1678)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1652 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` < `2.256` → IC=+0.222 (n=5147)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.256 (IC base=+0.218)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.224 (n=4643)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.218)

- **PATRÓN** `libro_liquidez` > `3755.0982` → IC=+0.226 (n=3960)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3755.0982 (IC base=+0.218)

- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.237 (n=1450)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.199)

- **PATRÓN** `drift_60min` |x|≤ `0.4908` → IC=+0.211 (n=4345)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4908 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.213 (n=1464)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.214 (n=1922)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.199)

- **PATRÓN** `ibs_20min` < `0.7304` → IC=+0.207 (n=4346)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7304 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` > `0.6584` → IC=+0.209 (n=745)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6584 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.779` → IC=+0.210 (n=3899)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.779 (IC base=+0.199)

- **PATRÓN** `volumen_regimen` < `1.0952` → IC=+0.205 (n=3645)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0952 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` < `0.0978` → IC=+0.200 (n=4002)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0978 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` > `0.0735` → IC=+0.200 (n=1937)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0735 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` < `1.5315` → IC=+0.203 (n=1885)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5315 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` > `2.1857` → IC=+0.206 (n=1942)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1857 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.200 (n=5777)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

- **PATRÓN** `ballena_activa_n` < `65.0` → IC=+0.213 (n=2853)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 65.0 (IC base=+0.199)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.276 (n=814)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0057 (IC base=+0.269)

- **PATRÓN** `drift_60min` |x|≤ `0.0846` → IC=+0.297 (n=309)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0846 (IC base=+0.269)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.279 (n=925)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.269)

- **PATRÓN** `ibs_20min` < `0.8328` → IC=+0.278 (n=925)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.8328 (IC base=+0.269)

- **PATRÓN** `dist_vwap_pct` < `0.6679` → IC=+0.277 (n=1076)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6679 (IC base=+0.269)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.118` → IC=+0.300 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.118 (IC base=+0.269)

- **PATRÓN** `volumen_regimen` < `1.2212` → IC=+0.271 (n=925)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2212 (IC base=+0.269)

- **PATRÓN** `volumen_regimen` > `0.8749` → IC=+0.288 (n=617)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8749 (IC base=+0.269)

- **PATRÓN** `volumen_pendiente_norm` > `0.2881` → IC=+0.351 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2881 (IC base=+0.269)

- **PATRÓN** `volumen_spike_ratio` < `2.4907` → IC=+0.276 (n=921)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4907 (IC base=+0.269)

- **PATRÓN** `volumen_spike_ratio` > `2.1895` → IC=+0.269 (n=418)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1895 (IC base=+0.269)

- **PATRÓN** `libro_liquidez` > `12909.5134` → IC=+0.279 (n=617)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12909.5134 (IC base=+0.269)

- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.263 (n=509)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0032 (IC base=+0.176)

- **PATRÓN** `drift_60min` |x|≤ `0.3854` → IC=+0.189 (n=1519)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.3854 (IC base=+0.176)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.216 (n=557)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.184 (n=565)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 5.0 (IC base=+0.176)

- **PATRÓN** `ibs_20min` < `0.138` → IC=+0.197 (n=668)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.138 (IC base=+0.176)

- **PATRÓN** `dist_vwap_pct` > `0.6955` → IC=+0.197 (n=140)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.6955 (IC base=+0.176)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.315` → IC=+0.198 (n=1488)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` < 6.315 (IC base=+0.176)

- **PATRÓN** `volumen_regimen` < `1.0915` → IC=+0.188 (n=1336)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 1.0915 (IC base=+0.176)

- **PATRÓN** `volumen_pendiente_norm` > `0.1519` → IC=+0.195 (n=463)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.1519 (IC base=+0.176)

- **PATRÓN** `volumen_spike_ratio` < `1.4126` → IC=+0.194 (n=504)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 1.4126 (IC base=+0.176)

- **PATRÓN** `volumen_spike_ratio` > `2.1703` → IC=+0.180 (n=685)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 2.1703 (IC base=+0.176)

- **PATRÓN** `libro_liquidez` > `14605.0565` → IC=+0.179 (n=689)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 14605.0565 (IC base=+0.176)

- **PATRÓN** `ballena_activa_n` < `686.0` → IC=+0.188 (n=1473)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 686.0 (IC base=+0.176)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.226 (n=604)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0089 (IC base=+0.201)

- **PATRÓN** `drift_60min` |x|≤ `0.5896` → IC=+0.207 (n=906)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5896 (IC base=+0.201)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.233 (n=418)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.201)

- **PATRÓN** `ibs_20min` < `0.3913` → IC=+0.201 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3913 (IC base=+0.201)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.245 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.201)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.444` → IC=+0.249 (n=329)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.444 (IC base=+0.201)

- **PATRÓN** `volumen_pendiente_norm` > `0.2062` → IC=+0.233 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2062 (IC base=+0.201)

- **PATRÓN** `volumen_spike_ratio` > `1.8037` → IC=+0.208 (n=807)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8037 (IC base=+0.201)

- **PATRÓN** `ballena_activa_n` < `9.0` → IC=+0.209 (n=630)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 9.0 (IC base=+0.201)

- **PATRÓN** `sigma_h` < `0.0116` → IC=+0.242 (n=60)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0116 (IC base=+0.228)

- **PATRÓN** `sigma_h` > `0.009` → IC=+0.286 (n=40)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.009 (IC base=+0.228)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.233 (n=28)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.228)

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

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.0081` → IC=+0.218 (n=1628)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0081 (IC base=+0.203)

- **PATRÓN** `drift_60min` |x|≤ `0.4542` → IC=+0.212 (n=1627)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4542 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.221 (n=572)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.203)

- **PATRÓN** `ibs_20min` < `0.5006` → IC=+0.216 (n=1085)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5006 (IC base=+0.203)

- **PATRÓN** `ibs_20min` > `0.8555` → IC=+0.206 (n=543)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8555 (IC base=+0.203)

- **PATRÓN** `dist_vwap_pct` < `0.3955` → IC=+0.214 (n=1630)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3955 (IC base=+0.203)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.521` → IC=+0.209 (n=1652)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 6.521 (IC base=+0.203)

- **PATRÓN** `volumen_regimen` < `0.7054` → IC=+0.209 (n=716)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7054 (IC base=+0.203)

- **PATRÓN** `volumen_regimen` > `1.2249` → IC=+0.205 (n=543)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2249 (IC base=+0.203)

- **PATRÓN** `volumen_pendiente_norm` < `0.1025` → IC=+0.208 (n=1498)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1025 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` < `2.1597` → IC=+0.214 (n=1402)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1597 (IC base=+0.203)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.241 (n=454)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.201)

- **PATRÓN** `drift_60min` |x|≤ `0.4841` → IC=+0.221 (n=1354)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4841 (IC base=+0.201)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.210 (n=512)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.201)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.218 (n=917)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.201)

- **PATRÓN** `ibs_20min` < `0.7466` → IC=+0.203 (n=1355)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7466 (IC base=+0.201)

- **PATRÓN** `ibs_20min` > `0.0937` → IC=+0.205 (n=1353)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.0937 (IC base=+0.201)

- **PATRÓN** `dist_vwap_pct` > `0.6225` → IC=+0.219 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6225 (IC base=+0.201)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.351` → IC=+0.205 (n=1234)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.351 (IC base=+0.201)

- **PATRÓN** `volumen_regimen` < `0.6391` → IC=+0.227 (n=452)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6391 (IC base=+0.201)

- **PATRÓN** `volumen_pendiente_norm` > `0.074` → IC=+0.229 (n=552)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.074 (IC base=+0.201)

- **PATRÓN** `volumen_spike_ratio` < `2.1876` → IC=+0.207 (n=1167)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1876 (IC base=+0.201)

- **PATRÓN** `libro_liquidez` > `6428.6136` → IC=+0.206 (n=1209)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6428.6136 (IC base=+0.201)

- **PATRÓN** `ballena_activa_n` < `98.0` → IC=+0.202 (n=1344)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 98.0 (IC base=+0.201)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0098` → IC=+0.224 (n=632)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0098 (IC base=+0.198)

- **PATRÓN** `hora_utc` > `9.0` → IC=+0.235 (n=662)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 9.0 (IC base=+0.198)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.272 (n=323)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.198)

- **PATRÓN** `dist_vwap_pct` > `0.7686` → IC=+0.238 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7686 (IC base=+0.198)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.208` → IC=+0.224 (n=519)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.208 (IC base=+0.198)

- **PATRÓN** `volumen_regimen` < `0.6428` → IC=+0.245 (n=316)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6428 (IC base=+0.198)

- **PATRÓN** `volumen_pendiente_norm` < `0.1056` → IC=+0.206 (n=853)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1056 (IC base=+0.198)

- **PATRÓN** `volumen_pendiente_norm` > `0.079` → IC=+0.204 (n=421)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.079 (IC base=+0.198)

- **PATRÓN** `volumen_spike_ratio` < `2.1444` → IC=+0.203 (n=810)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1444 (IC base=+0.198)

- **PATRÓN** `volumen_spike_ratio` > `1.4746` → IC=+0.204 (n=921)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4746 (IC base=+0.198)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.207 (n=1119)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.198)

- **PATRÓN** `libro_liquidez` > `4325.8202` → IC=+0.245 (n=316)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4325.8202 (IC base=+0.198)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.203 (n=821)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 40.0 (IC base=+0.198)

- **PATRÓN** `sigma_h` > `0.01` → IC=+0.234 (n=461)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.01 (IC base=+0.218)

- **PATRÓN** `drift_60min` |x|≤ `0.5949` → IC=+0.234 (n=691)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5949 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.248 (n=479)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.218)

- **PATRÓN** `ibs_20min` < `0.6522` → IC=+0.250 (n=609)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6522 (IC base=+0.218)

- **PATRÓN** `dist_vwap_pct` > `0.5326` → IC=+0.221 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5326 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.791` → IC=+0.233 (n=639)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.791 (IC base=+0.218)

- **PATRÓN** `volumen_regimen` < `0.7541` → IC=+0.226 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7541 (IC base=+0.218)

- **PATRÓN** `volumen_regimen` > `1.2794` → IC=+0.225 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2794 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` < `0.0838` → IC=+0.235 (n=582)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0838 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` > `2.1859` → IC=+0.249 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1859 (IC base=+0.218)

- **PATRÓN** `libro_liquidez` > `3788.9662` → IC=+0.234 (n=461)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3788.9662 (IC base=+0.218)

- **PATRÓN** `ballena_activa_n` < `36.0` → IC=+0.255 (n=602)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 36.0 (IC base=+0.218)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.149 (n=714)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0038 (IC base=+0.052)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.186 (n=1375)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.75 (IC base=+0.052)

- **PATRÓN** `dist_vwap_pct` > `0.1458` → IC=+0.139 (n=1027)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` > 0.1458 (IC base=+0.052)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.469` → IC=+0.146 (n=456)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 10.469 (IC base=+0.052)

- **PATRÓN** `ibs_20min` < `0.0588` → IC=+0.263 (n=610)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0588 (IC base=+0.046)

- **PATRÓN** `volumen_pendiente_norm` > `0.1449` → IC=+0.136 (n=380)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` > 0.1449 (IC base=+0.046)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `ibs_20min` < `0.5358` → IC=-0.124 (n=285)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5358
  - _Potencial_: sin este filtro IC_bueno=+0.165 (n=580)

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.125 (n=598)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0052 (IC base=+0.069)

- **PATRÓN** `ibs_20min` > `0.5358` → IC=+0.165 (n=580)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` > 0.5358 (IC base=+0.069)

- **PATRÓN** `dist_vwap_pct` > `0.1195` → IC=+0.165 (n=314)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.1195 (IC base=+0.069)

- **PATRÓN** `ibs_20min` < `0.0755` → IC=+0.270 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0755 (IC base=+0.047)

- **PATRÓN** `volumen_pendiente_norm` > `0.2172` → IC=+0.173 (n=111)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.2172 (IC base=+0.047)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` < `0.5412` → IC=-0.125 (n=291)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5412
  - _Potencial_: sin este filtro IC_bueno=+0.171 (n=593)

- **FILTRO** `ibs_20min` > `0.6905` → IC=-0.180 (n=148)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6905
  - _Potencial_: sin este filtro IC_bueno=+0.113 (n=447)

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.126 (n=463)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.63€ cuando `sigma_h` < 0.0052 (IC base=+0.070)

- **PATRÓN** `ibs_20min` > `0.5412` → IC=+0.171 (n=593)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` > 0.5412 (IC base=+0.070)

- **PATRÓN** `dist_vwap_pct` > `0.1269` → IC=+0.173 (n=328)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.1269 (IC base=+0.070)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.717` → IC=+0.200 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.717 (IC base=+0.070)

- **PATRÓN** `ibs_20min` < `0.0296` → IC=+0.262 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0296 (IC base=+0.022)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.686` → IC=+0.218 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.686 (IC base=+0.022)

### GBM_LATE_60M#SOL#60min
- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.199 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.021)

- **PATRÓN** `dist_vwap_pct` > `0.7192` → IC=+0.130 (n=171)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` > 0.7192 (IC base=+0.021)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.697` → IC=+0.140 (n=159)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 8.697 (IC base=+0.021)

- **PATRÓN** `sigma_h` < `0.0095` → IC=+0.183 (n=276)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0095 (IC base=+0.072)

- **PATRÓN** `ibs_20min` < `0.3415` → IC=+0.201 (n=336)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3415 (IC base=+0.072)

- **PATRÓN** `dist_vwap_pct` < `0.1869` → IC=+0.133 (n=363)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.1869 (IC base=+0.072)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.903` → IC=+0.295 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.903 (IC base=+0.072)

- **PATRÓN** `volumen_regimen` > `1.0862` → IC=+0.167 (n=127)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 1.0862 (IC base=+0.072)

- **PATRÓN** `volumen_pendiente_norm` > `0.1522` → IC=+0.173 (n=108)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.1522 (IC base=+0.072)

- **PATRÓN** `volumen_spike_ratio` > `1.8478` → IC=+0.143 (n=236)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.8478 (IC base=+0.072)

### GBM_LATE_60M_FADE
- **FILTRO** `drift_60min` |x|> `0.1829` → IC=-0.304 (n=90)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1829
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=274)

- **FILTRO** `dist_vwap_pct` > `0.2381` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2381
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=351)

- **FILTRO** `volumen_regimen` < `0.7761` → IC=-0.306 (n=91)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7761
  - _Potencial_: sin este filtro IC_bueno=-0.190 (n=275)

- **FILTRO** `hora_utc` > `11.0` → IC=-0.309 (n=150)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.257 (n=175)

- **FILTRO** `dist_vwap_pct` > `0.4614` → IC=-0.405 (n=19)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4614
  - _Potencial_: sin este filtro IC_bueno=-0.273 (n=306)

- **FILTRO** `sigma_ewma_delta_pct` > `9.697` → IC=-0.328 (n=27)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 9.697
  - _Potencial_: sin este filtro IC_bueno=-0.277 (n=298)

- **FILTRO** `volumen_pendiente_norm` > `0.0453` → IC=-0.375 (n=30)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0453
  - _Potencial_: sin este filtro IC_bueno=-0.269 (n=206)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.280 (n=48)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.205 (n=59)

- **FILTRO** `volumen_regimen` < `0.8856` → IC=-0.321 (n=26)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.8856
  - _Potencial_: sin este filtro IC_bueno=-0.211 (n=81)

- **FILTRO** `sigma_h` < `0.0033` → IC=-0.257 (n=72)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0033
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=74)

- **FILTRO** `hora_utc` < `13.0` → IC=-0.300 (n=73)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.207 (n=73)

- **FILTRO** `ibs_20min` > `0.7502` → IC=-0.265 (n=49)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7502
  - _Potencial_: sin este filtro IC_bueno=-0.247 (n=97)

- **FILTRO** `volumen_regimen` > `0.805` → IC=-0.316 (n=36)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.232 (n=110)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.5857` → IC=-0.471 (n=32)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5857
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=96)

- **FILTRO** `volumen_regimen` < `0.7435` → IC=-0.265 (n=32)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7435
  - _Potencial_: sin este filtro IC_bueno=-0.143 (n=96)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.368 (n=36)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.272 (n=90)

- **FILTRO** `ibs_20min` > `0.6926` → IC=-0.409 (n=42)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6926
  - _Potencial_: sin este filtro IC_bueno=-0.244 (n=84)

- **FILTRO** `volumen_spike_ratio` < `1.7371` → IC=-0.372 (n=45)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.7371
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=46)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.296 (n=111)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `sigma_h` < `0.0074` → IC=-0.322 (n=43)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0074
  - _Potencial_: sin este filtro IC_bueno=-0.189 (n=88)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.400 (n=18)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.204 (n=113)

- **FILTRO** `volumen_pendiente_norm` > `0.1329` → IC=-0.258 (n=31)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1329
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=75)

- **FILTRO** `libro_spread` > `0.06` → IC=-0.250 (n=30)

  - _Acción_: SKIP cuando `libro_spread` > 0.06
  - _Potencial_: sin este filtro IC_bueno=-0.228 (n=101)

- **FILTRO** `sigma_h` < `0.0107` → IC=-0.329 (n=39)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0107
  - _Potencial_: sin este filtro IC_bueno=-0.125 (n=14)

- **FILTRO** `sigma_ewma_delta_pct` > `2.412` → IC=-0.326 (n=21)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 2.412
  - _Potencial_: sin este filtro IC_bueno=-0.235 (n=32)

- **FILTRO** `volumen_regimen` < `0.9051` → IC=-0.447 (n=17)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9051
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=36)

### GBM_LATE_60M_PYCONFIRMADO
- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.241 (n=226)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0083 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.196 (n=307)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 16.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` > `0.6786` → IC=+0.178 (n=676)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.6786 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` > `0.8184` → IC=+0.284 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8184 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.643` → IC=+0.153 (n=373)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 3.643 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` < `8.618` → IC=+0.142 (n=688)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 8.618 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` < `0.6249` → IC=+0.180 (n=226)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 0.6249 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` < `0.0702` → IC=+0.177 (n=496)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` < 0.0702 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` < `1.388` → IC=+0.188 (n=190)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 1.388 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.619` → IC=+0.158 (n=185)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 10.619 (IC base=+0.036)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.7797` → IC=-0.133 (n=88)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7797
  - _Potencial_: sin este filtro IC_bueno=+0.123 (n=181)

- **PATRÓN** `ibs_20min` > `0.7797` → IC=+0.123 (n=181)

  - _Acción_: Kelly boost +0.61€ cuando `ibs_20min` > 0.7797 (IC base=+0.039)

- **PATRÓN** `dist_vwap_pct` > `0.6135` → IC=+0.207 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6135 (IC base=+0.039)

- **PATRÓN** `ibs_20min` < `0.2076` → IC=+0.151 (n=376)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.2076 (IC base=+0.090)

- **PATRÓN** `volumen_pendiente_norm` > `0.2723` → IC=+0.135 (n=61)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` > 0.2723 (IC base=+0.090)

- **PATRÓN** `volumen_spike_ratio` > `1.7602` → IC=+0.125 (n=230)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` > 1.7602 (IC base=+0.090)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `volumen_pendiente_norm` > `0.1879` → IC=-0.167 (n=25)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1879
  - _Potencial_: sin este filtro IC_bueno=+0.147 (n=233)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.138 (n=150)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` < 0.0042 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.167 (n=79)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 18.0 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.124 (n=107)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 8.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` > `0.7964` → IC=+0.157 (n=199)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` > 0.7964 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` < `0.1019` → IC=+0.150 (n=181)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.1019 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.539` → IC=+0.144 (n=231)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 9.539 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` < `0.6249` → IC=+0.162 (n=75)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.6249 (IC base=+0.117)

- **PATRÓN** `volumen_pendiente_norm` < `0.1248` → IC=+0.156 (n=222)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` < 0.1248 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` < `2.1053` → IC=+0.147 (n=171)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 2.1053 (IC base=+0.117)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.128 (n=189)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.01 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.619` → IC=+0.203 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.619 (IC base=+0.017)

- **PATRÓN** `volumen_pendiente_norm` > `0.2823` → IC=+0.144 (n=43)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_pendiente_norm` > 0.2823 (IC base=+0.017)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.2` → IC=-0.233 (n=58)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=123)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.296 (n=179)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.243)

- **PATRÓN** `ibs_20min` > `0.6` → IC=+0.280 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6 (IC base=+0.243)

- **PATRÓN** `dist_vwap_pct` > `0.6973` → IC=+0.385 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6973 (IC base=+0.243)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.903` → IC=+0.354 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.903 (IC base=+0.243)

- **PATRÓN** `volumen_regimen` < `0.5849` → IC=+0.293 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.5849 (IC base=+0.243)

- **PATRÓN** `volumen_pendiente_norm` > `0.0966` → IC=+0.315 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0966 (IC base=+0.243)

- **PATRÓN** `volumen_spike_ratio` < `1.4721` → IC=+0.332 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4721 (IC base=+0.243)

- **PATRÓN** `volumen_spike_ratio` > `2.3425` → IC=+0.294 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3425 (IC base=+0.243)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.962` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.962 (IC base=-0.074)

### LATE_WINDOW_5MIN
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.319 (n=103)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3975` → IC=+0.336 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3975 (IC base=+0.332)

- **PATRÓN** `elapsed_s` > `207.7` → IC=+0.391 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 207.7 (IC base=+0.332)

- **PATRÓN** `drift_15min` |x|≤ `1.0104` → IC=+0.431 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0104 (IC base=+0.332)

- **PATRÓN** `drift_60min` |x|≤ `0.969` → IC=+0.377 (n=79)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.969 (IC base=+0.332)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.400 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.332)

- **PATRÓN** `ballena_activa_n` < `1208.0` → IC=+0.365 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1208.0 (IC base=+0.332)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3474` → IC=+0.295 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3474 (IC base=+0.254)

- **PATRÓN** `elapsed_s` > `185.6` → IC=+0.283 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 185.6 (IC base=+0.254)

- **PATRÓN** `elapsed_s` < `203.0` → IC=+0.262 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 203.0 (IC base=+0.254)

- **PATRÓN** `drift_15min` |x|≤ `2.3044` → IC=+0.305 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3044 (IC base=+0.254)

- **PATRÓN** `drift_60min` |x|≤ `0.6365` → IC=+0.294 (n=61)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6365 (IC base=+0.254)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.319 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.254)

- **PATRÓN** `ballena_activa_n` < `1750.0` → IC=+0.306 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1750.0 (IC base=+0.254)

### LATE_WINDOW_5MIN#BTC#5min
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.319 (n=103)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3975` → IC=+0.336 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3975 (IC base=+0.332)

- **PATRÓN** `elapsed_s` > `207.7` → IC=+0.391 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 207.7 (IC base=+0.332)

- **PATRÓN** `drift_15min` |x|≤ `1.0104` → IC=+0.431 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0104 (IC base=+0.332)

- **PATRÓN** `drift_60min` |x|≤ `0.969` → IC=+0.377 (n=79)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.969 (IC base=+0.332)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.400 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.332)

- **PATRÓN** `ballena_activa_n` < `1208.0` → IC=+0.365 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1208.0 (IC base=+0.332)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3474` → IC=+0.295 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3474 (IC base=+0.254)

- **PATRÓN** `elapsed_s` > `185.6` → IC=+0.283 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 185.6 (IC base=+0.254)

- **PATRÓN** `elapsed_s` < `203.0` → IC=+0.262 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 203.0 (IC base=+0.254)

- **PATRÓN** `drift_15min` |x|≤ `2.3044` → IC=+0.305 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3044 (IC base=+0.254)

- **PATRÓN** `drift_60min` |x|≤ `0.6365` → IC=+0.294 (n=61)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6365 (IC base=+0.254)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.319 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.254)

- **PATRÓN** `ballena_activa_n` < `1750.0` → IC=+0.306 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1750.0 (IC base=+0.254)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.120 (n=1429)

  - _Acción_: Kelly boost +0.60€ cuando `py_entrada` > 0.5 (IC base=+0.099)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.120 (n=1429)

  - _Acción_: Kelly boost +0.60€ cuando `py_entrada` > 0.5 (IC base=+0.099)

### LIQUIDACIONES_15M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=243)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=243)

- **FILTRO** `libro_liquidez` < `6868.5329` → IC=-0.149 (n=129)

  - _Acción_: SKIP cuando `libro_liquidez` < 6868.5329
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=130)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=680)

### LIQUIDACIONES_15M#BNB#15min
- **PATRÓN** `hora_utc` < `5.0` → IC=+0.132 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 5.0 (IC base=+0.009)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `libro_liquidez` < `12112.4745` → IC=-0.159 (n=42)

  - _Acción_: SKIP cuando `libro_liquidez` < 12112.4745
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=87)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `liq_usd_total` < `4006.09` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `liq_usd_total` < 4006.09
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=28)

- **FILTRO** `hora_utc` < `10.0` → IC=-0.184 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=38)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.127 (n=73)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 7.0 (IC base=+0.056)

### LIQUIDACIONES_15M#SOL#15min
- **FILTRO** `hora_utc` > `4.0` → IC=-0.180 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 4.0
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=14)

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
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=3897)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=136)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=93)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.278 (n=34)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=123)

- **FILTRO** `ballena_activa_n` > `21.0` → IC=-0.160 (n=92)

  - _Acción_: SKIP cuando `ballena_activa_n` > 21.0
  - _Potencial_: sin este filtro IC_bueno=+0.258 (n=31)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.258 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 21.0 (IC base=-0.091)

### LIQUIDACIONES_5M#BNB#5min
- **FILTRO** `hora_utc` > `14.0` → IC=-0.141 (n=51)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=143)

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

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.124 (n=272)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` < 0.495 (IC base=+0.023)

### LIQUIDACIONES_5M#DOGE#5min
- **PATRÓN** `py_entrada` < `0.5` → IC=+0.239 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.5 (IC base=+0.250)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=1590)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=1544)

- **FILTRO** `liq_n` < `3.0` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `liq_n` < 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **FILTRO** `liq_usd_total` < `6520.36` → IC=-0.220 (n=23)

  - _Acción_: SKIP cuando `liq_usd_total` < 6520.36
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=13)

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
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=726)

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
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=441)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=422)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.149 (n=186)

  - _Acción_: Kelly boost +0.74€ cuando `py_entrada` < 0.495 (IC base=+0.023)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=971)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=971)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=1185)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=1185)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=269)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=269)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.146 (n=63)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=333)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=381)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=297)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=390)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=390)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.120 (n=185)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=235)

- **FILTRO** `libro_liquidez` < `659.869` → IC=-0.136 (n=138)

  - _Acción_: SKIP cuando `libro_liquidez` < 659.869
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=282)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=337)

### LIQUIDACIONES_DEPTH_FASE0#BNB#15min
- **FILTRO** `py_entrada` > `0.59` → IC=-0.158 (n=36)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=71)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.192 (n=76)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=90)

- **FILTRO** `hora_utc` > `14.0` → IC=-0.179 (n=76)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=90)

- **FILTRO** `py_entrada` > `0.58` → IC=-0.159 (n=39)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=43)

- **FILTRO** `hora_utc` < `10.0` → IC=-0.241 (n=25)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=57)

### LIQUIDACIONES_DEPTH_FASE0#BTC#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.126 (n=260)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=659)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **FILTRO** `py_entrada` > `0.6` → IC=-0.152 (n=231)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=652)

- **PATRÓN** `py_entrada` < `0.47` → IC=+0.150 (n=241)

  - _Acción_: Kelly boost +0.75€ cuando `py_entrada` < 0.47 (IC base=-0.011)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **FILTRO** `py_entrada` < `0.41` → IC=-0.160 (n=157)

  - _Acción_: SKIP cuando `py_entrada` < 0.41
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=331)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.120 (n=164)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=672)

- **FILTRO** `profundidad_ratio` < `63.9` → IC=-0.124 (n=275)

  - _Acción_: SKIP cuando `profundidad_ratio` < 63.9
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=561)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.122 (n=331)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.063 (n=348)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.120 (n=488)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=510)

- **FILTRO** `py_entrada` > `0.58` → IC=-0.125 (n=326)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=386)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.174 (n=142)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=616)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.126 (n=236)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=545)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.135 (n=113)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=345)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.44` → IC=-0.138 (n=459)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=463)

### MOMENTUM_IBS_15M
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=1073)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=5550)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.126 (n=241)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=7798)

### MOMENTUM_IBS_15M#BNB#15min
- **FILTRO** `libro_liquidez` < `2151.302` → IC=-0.153 (n=47)

  - _Acción_: SKIP cuando `libro_liquidez` < 2151.302
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=143)

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
- **FILTRO** `py_entrada` < `0.46` → IC=-0.172 (n=7544)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=24102)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.174 (n=8019)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=24595)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.182 (n=1451)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=4393)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.147 (n=1932)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.092 (n=3854)

- **PATRÓN** `py_entrada` < `0.505` → IC=+0.123 (n=2966)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` < 0.505 (IC base=+0.012)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` < `0.44` → IC=-0.171 (n=1042)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=3389)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.180 (n=1144)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=3461)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` > `0.62` → IC=-0.203 (n=1433)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.085 (n=4487)

- **PATRÓN** `ibs_20min` > `0.9632` → IC=+0.133 (n=1989)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` > 0.9632 (IC base=+0.035)

- **PATRÓN** `libro_liquidez` > `1755.5984` → IC=+0.122 (n=1988)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 1755.5984 (IC base=+0.035)

### MOMENTUM_IBS_15M_BALLENA#ETH#15min
- **FILTRO** `py_entrada` > `0.58` → IC=-0.182 (n=1089)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=3565)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.485` → IC=-0.158 (n=1450)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=+0.085 (n=4428)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=2432)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.162 (n=772)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=2356)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.180 (n=973)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=2986)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=3938)

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
- **FILTRO** `py_entrada` < `0.395` → IC=-0.230 (n=72)

  - _Acción_: SKIP cuando `py_entrada` < 0.395
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=262)

- **FILTRO** `ibs_20min` < `0.1975` → IC=-0.223 (n=110)

  - _Acción_: SKIP cuando `ibs_20min` < 0.1975
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=224)

- **FILTRO** `hora_utc` < `7.0` → IC=-0.204 (n=113)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.097 (n=355)

- **FILTRO** `ballena_activa_n` > `85.0` → IC=-0.186 (n=154)

  - _Acción_: SKIP cuando `ballena_activa_n` > 85.0
  - _Potencial_: sin este filtro IC_bueno=-0.094 (n=306)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=968)

- **FILTRO** `ballena_activa_n` > `23.0` → IC=-0.191 (n=390)

  - _Acción_: SKIP cuando `ballena_activa_n` > 23.0
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=772)

### MOMENTUM_IBS_15M_FADE#XRP#15min
- **FILTRO** `hora_utc` < `13.0` → IC=-0.238 (n=59)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 13.0
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=237)

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
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=91)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.156 (n=30)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 15.0 (IC base=+0.024)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.133 (n=21667)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.089 (n=48489)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.296 (n=16742)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=53414)

- **FILTRO** `ibs_7min` < `0.2195` → IC=-0.232 (n=17538)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2195
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=52618)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.152 (n=23084)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=47072)

- **FILTRO** `py_entrada` > `0.68` → IC=-0.250 (n=20438)

  - _Acción_: SKIP cuando `py_entrada` > 0.68
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=67378)

- **FILTRO** `ibs_7min` > `0.283` → IC=-0.183 (n=21953)

  - _Acción_: SKIP cuando `ibs_7min` > 0.283
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=65863)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.155 (n=3042)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=9407)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.319 (n=3059)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=9390)

- **FILTRO** `ibs_7min` < `0.7097` → IC=-0.251 (n=4103)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7097
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=8346)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.152 (n=2756)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=9693)

- **FILTRO** `py_entrada` > `0.72` → IC=-0.276 (n=3665)

  - _Acción_: SKIP cuando `py_entrada` > 0.72
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=11515)

- **FILTRO** `ibs_7min` > `0.775` → IC=-0.212 (n=3794)

  - _Acción_: SKIP cuando `ibs_7min` > 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=11386)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.261 (n=2802)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=8898)

- **FILTRO** `ibs_7min` < `0.7152` → IC=-0.207 (n=2925)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7152
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=8775)

- **FILTRO** `ballena_activa_n` > `155.0` → IC=-0.198 (n=2919)

  - _Acción_: SKIP cuando `ballena_activa_n` > 155.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=8781)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.268 (n=2730)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9214)

- **FILTRO** `ibs_7min` > `0.2655` → IC=-0.196 (n=2983)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2655
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=8961)

- **FILTRO** `ballena_activa_n` > `153.0` → IC=-0.181 (n=2978)

  - _Acción_: SKIP cuando `ballena_activa_n` > 153.0
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=8966)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.164 (n=2894)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=9022)

- **FILTRO** `py_entrada` < `0.3` → IC=-0.323 (n=2840)

  - _Acción_: SKIP cuando `py_entrada` < 0.3
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=9076)

- **FILTRO** `ibs_7min` < `0.2857` → IC=-0.249 (n=3923)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2857
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=7993)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.200 (n=2444)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=9472)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.257 (n=3873)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=12197)

- **FILTRO** `ibs_7min` > `0.7317` → IC=-0.182 (n=4017)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7317
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=12053)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.262 (n=2801)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=8553)

- **FILTRO** `ibs_7min` < `0.7176` → IC=-0.193 (n=2838)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7176
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=8516)

- **FILTRO** `ballena_activa_n` > `25.0` → IC=-0.188 (n=2786)

  - _Acción_: SKIP cuando `ballena_activa_n` > 25.0
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=8568)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.258 (n=2720)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=9108)

- **FILTRO** `ibs_7min` > `0.2744` → IC=-0.175 (n=2954)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2744
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=8874)

- **FILTRO** `ballena_activa_n` > `24.0` → IC=-0.170 (n=2901)

  - _Acción_: SKIP cuando `ballena_activa_n` > 24.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=8927)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.32` → IC=-0.296 (n=2654)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=8628)

- **FILTRO** `ibs_7min` < `0.7037` → IC=-0.229 (n=3716)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7037
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=7566)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.216 (n=2806)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=8476)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.197 (n=4114)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=12868)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.130 (n=3694)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.104 (n=7761)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.307 (n=2704)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=8751)

- **FILTRO** `ibs_7min` < `0.1695` → IC=-0.230 (n=2863)

  - _Acción_: SKIP cuando `ibs_7min` < 0.1695
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=8592)

- **FILTRO** `ballena_activa_n` > `9.0` → IC=-0.203 (n=2565)

  - _Acción_: SKIP cuando `ballena_activa_n` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=8890)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.233 (n=3661)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=12151)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1046` → IC=-0.135 (n=61)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1046
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=121)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `py_entrada` < `0.455` → IC=-0.160 (n=301)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=1007)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=1293)

- **FILTRO** `py_entrada` > `0.54` → IC=-0.142 (n=191)

  - _Acción_: SKIP cuando `py_entrada` > 0.54
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=576)

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
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=884)

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

- **FILTRO** `libro_spread` > `0.01` → IC=-0.140 (n=98)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=671)

- **FILTRO** `libro_liquidez` < `3302.3462` → IC=-0.155 (n=192)

  - _Acción_: SKIP cuando `libro_liquidez` < 3302.3462
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=577)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=394)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.4305` → IC=+0.150 (n=659)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.75€ cuando `delta_ratio` |x|> 0.4305 (IC base=+0.123)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.130 (n=750)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 6.0 (IC base=+0.123)

- **PATRÓN** `total_vol_5m` < `421.6695` → IC=+0.161 (n=484)

  - _Acción_: Kelly boost +0.80€ cuando `total_vol_5m` < 421.6695 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `3557.0392` → IC=+0.141 (n=658)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 3557.0392 (IC base=+0.123)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `14.0` → IC=+0.178 (n=172)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 14.0 (IC base=+0.130)

- **PATRÓN** `total_vol_5m` < `504.262` → IC=+0.149 (n=348)

  - _Acción_: Kelly boost +0.74€ cuando `total_vol_5m` < 504.262 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `2522.0946` → IC=+0.237 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2522.0946 (IC base=+0.130)

- **PATRÓN** `ballena_activa_n` < `6.0` → IC=+0.128 (n=162)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 6.0 (IC base=+0.130)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `delta_ratio` |x|> `0.4378` → IC=+0.160 (n=101)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.80€ cuando `delta_ratio` |x|> 0.4378 (IC base=+0.118)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.140 (n=262)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 14.0 (IC base=+0.118)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4162` → IC=+0.190 (n=182)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.95€ cuando `delta_ratio` |x|> 0.4162 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.170 (n=95)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 15.0 (IC base=+0.128)

- **PATRÓN** `total_vol_5m` < `502.4124` → IC=+0.170 (n=183)

  - _Acción_: Kelly boost +0.85€ cuando `total_vol_5m` < 502.4124 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `59.0` → IC=+0.180 (n=95)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 59.0 (IC base=+0.128)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.3978` → IC=+0.165 (n=249)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.83€ cuando `delta_ratio` |x|> 0.3978 (IC base=+0.142)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.176 (n=177)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 12.0 (IC base=+0.142)

- **PATRÓN** `total_vol_5m` < `4679.172` → IC=+0.179 (n=166)

  - _Acción_: Kelly boost +0.89€ cuando `total_vol_5m` < 4679.172 (IC base=+0.142)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `hora_utc` < `13.0` → IC=+0.123 (n=253)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 13.0 (IC base=+0.094)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.140 (n=201)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.094)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `7.4417` → IC=-0.272 (n=55)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 7.4417
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=167)

- **FILTRO** `sigma_h` > `0.0067` → IC=-0.270 (n=276)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0067
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=537)

- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.153 (n=269)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0044 (IC base=-0.082)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0056` → IC=-0.232 (n=121)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0056
  - _Potencial_: sin este filtro IC_bueno=+0.161 (n=122)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.271 (n=81)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=-0.035)

- **PATRÓN** `pct_vs_K` |x|≤ `1.7112` → IC=+0.163 (n=81)

  - _Acción_: Kelly boost +0.81€ cuando `pct_vs_K` |x|≤ 1.7112 (IC base=-0.035)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `sigma_h` > `0.0062` → IC=-0.196 (n=54)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0062
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=27)

- **FILTRO** `T_h` < `251.7955` → IC=-0.210 (n=60)

  - _Acción_: SKIP cuando `T_h` < 251.7955
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=21)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0109` → IC=-0.192 (n=76)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0109
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=78)

- **FILTRO** `T_h` < `64.4744` → IC=-0.192 (n=50)

  - _Acción_: SKIP cuando `T_h` < 64.4744
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=104)

### PRICE_TARGET_GBM#SOL#reach
- **FILTRO** `T_h` < `146.0708` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `T_h` < 146.0708
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=16)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0101` → IC=-0.239 (n=493)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0101
  - _Potencial_: sin este filtro IC_bueno=-0.154 (n=255)

- **FILTRO** `T_h` > `70.3179` → IC=-0.223 (n=500)

  - _Acción_: SKIP cuando `T_h` > 70.3179
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=248)

- **FILTRO** `sigma_h` > `0.0103` → IC=-0.241 (n=160)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0103
  - _Potencial_: sin este filtro IC_bueno=-0.191 (n=483)

- **FILTRO** `pct_vs_K` |x|> `3.0996` → IC=-0.413 (n=159)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.0996
  - _Potencial_: sin este filtro IC_bueno=-0.134 (n=484)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `sigma_h` < `0.0095` → IC=-0.208 (n=183)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0095
  - _Potencial_: sin este filtro IC_bueno=-0.109 (n=62)

- **FILTRO** `sigma_h` > `0.006` → IC=-0.290 (n=117)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.006
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=118)

- **FILTRO** `T_h` > `143.6682` → IC=-0.250 (n=58)

  - _Acción_: SKIP cuando `T_h` > 143.6682
  - _Potencial_: sin este filtro IC_bueno=-0.221 (n=177)

### PRICE_TARGET_GBM_FADE#BTC#reach
- **FILTRO** `T_h` < `139.5329` → IC=-0.340 (n=23)

  - _Acción_: SKIP cuando `T_h` < 139.5329
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=13)

- **FILTRO** `sigma_h` < `0.0066` → IC=-0.265 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0066
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=16)

- **FILTRO** `T_h` > `148.7378` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `T_h` > 148.7378
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=16)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `sigma_h` < `0.0097` → IC=-0.306 (n=137)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0097
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=72)

- **FILTRO** `T_h` > `95.5599` → IC=-0.283 (n=104)

  - _Acción_: SKIP cuando `T_h` > 95.5599
  - _Potencial_: sin este filtro IC_bueno=-0.257 (n=105)

- **FILTRO** `sigma_h` > `0.0091` → IC=-0.363 (n=49)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0091
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=148)

- **FILTRO** `sigma_h` < `0.0054` → IC=-0.206 (n=49)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0054
  - _Potencial_: sin este filtro IC_bueno=-0.147 (n=148)

- **FILTRO** `T_h` > `57.2198` → IC=-0.237 (n=131)

  - _Acción_: SKIP cuando `T_h` > 57.2198
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=66)

- **PATRÓN** `pct_vs_K` |x|≤ `0.8012` → IC=+0.192 (n=50)

  - _Acción_: Kelly boost +0.96€ cuando `pct_vs_K` |x|≤ 0.8012 (IC base=-0.163)

### PRICE_TARGET_GBM_FADE#ETH#reach
- **FILTRO** `T_h` < `132.3532` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `T_h` < 132.3532
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=10)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` < `0.0083` → IC=-0.278 (n=52)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0083
  - _Potencial_: sin este filtro IC_bueno=-0.144 (n=158)

- **FILTRO** `T_h` > `69.35` → IC=-0.217 (n=157)

  - _Acción_: SKIP cuando `T_h` > 69.35
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=53)

- **FILTRO** `sigma_h` > `0.0158` → IC=-0.311 (n=35)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0158
  - _Potencial_: sin este filtro IC_bueno=-0.191 (n=108)

- **FILTRO** `sigma_h` < `0.0097` → IC=-0.255 (n=47)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0097
  - _Potencial_: sin este filtro IC_bueno=-0.204 (n=96)

- **FILTRO** `T_h` > `33.9175` → IC=-0.252 (n=107)

  - _Acción_: SKIP cuando `T_h` > 33.9175
  - _Potencial_: sin este filtro IC_bueno=-0.132 (n=36)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1195` → IC=+0.461 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1195 (IC base=+0.338)

- **PATRÓN** `sigma_h` < `0.0147` → IC=+0.351 (n=112)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0147 (IC base=+0.338)

- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.382 (n=74)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0104 (IC base=+0.338)

- **PATRÓN** `T_h` < `0.3261` → IC=+0.400 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.3261 (IC base=+0.338)

- **PATRÓN** `T_h` > `0.8774` → IC=+0.387 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.8774 (IC base=+0.338)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.481 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.338)

- **PATRÓN** `edge` > `0.1` → IC=+0.427 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1 (IC base=+0.395)

- **PATRÓN** `sigma_h` < `0.0076` → IC=+0.399 (n=87)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0076 (IC base=+0.395)

- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.409 (n=173)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0097 (IC base=+0.395)

- **PATRÓN** `T_h` < `0.6127` → IC=+0.422 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.6127 (IC base=+0.395)

- **PATRÓN** `T_h` > `1.484` → IC=+0.398 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.484 (IC base=+0.395)

- **PATRÓN** `dist_50` > `0.3756` → IC=+0.442 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3756 (IC base=+0.395)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.414 (n=325)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.395)

### RESOLUTION_SNIPER#BTC#sniper
- **PATRÓN** `edge` > `0.1235` → IC=+0.259 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1235 (IC base=+0.179)

- **PATRÓN** `sigma_h` < `0.0077` → IC=+0.257 (n=35)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0077 (IC base=+0.179)

- **PATRÓN** `T_h` > `1.3612` → IC=+0.203 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.3612 (IC base=+0.179)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.263 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.232 (n=54)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.179)

### RESOLUTION_SNIPER#ETH#sniper
- **PATRÓN** `edge` > `0.1023` → IC=+0.464 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1023 (IC base=+0.406)

- **PATRÓN** `sigma_h` < `0.0102` → IC=+0.419 (n=60)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0102 (IC base=+0.406)

- **PATRÓN** `T_h` < `1.2415` → IC=+0.435 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 1.2415 (IC base=+0.406)

- **PATRÓN** `dist_50` > `0.4084` → IC=+0.482 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4084 (IC base=+0.406)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.444 (n=34)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.406)

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

- **PATRÓN** `edge` > `0.2005` → IC=+0.470 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.2005 (IC base=+0.462)

- **PATRÓN** `sigma_h` < `0.0162` → IC=+0.473 (n=148)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0162 (IC base=+0.462)

- **PATRÓN** `T_h` < `0.8229` → IC=+0.455 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.8229 (IC base=+0.462)

- **PATRÓN** `T_h` > `1.486` → IC=+0.481 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.486 (IC base=+0.462)

- **PATRÓN** `dist_50` > `0.4597` → IC=+0.492 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4597 (IC base=+0.462)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.467 (n=148)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.462)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=391)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.072 (n=472)

- **PATRÓN** `streak_estiramiento` < `0.293` → IC=+0.163 (n=99)

  - _Acción_: Kelly boost +0.82€ cuando `streak_estiramiento` < 0.293 (IC base=+0.029)

- **PATRÓN** `streak_estiramiento` < `0.5379` → IC=+0.183 (n=216)

  - _Acción_: Kelly boost +0.92€ cuando `streak_estiramiento` < 0.5379 (IC base=+0.059)

- **PATRÓN** `ballena_activa_n` < `30.0` → IC=+0.129 (n=243)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 30.0 (IC base=+0.059)

### STREAK_FADE_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=17)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.167 (n=16)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` < 0.495 (IC base=+0.061)

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
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=151)

- **PATRÓN** `streak_estiramiento` < `0.2244` → IC=+0.161 (n=57)

  - _Acción_: Kelly boost +0.81€ cuando `streak_estiramiento` < 0.2244 (IC base=+0.039)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.150 (n=115)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 11.0 (IC base=+0.097)

- **PATRÓN** `streak_estiramiento` < `0.2929` → IC=+0.214 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `streak_estiramiento` < 0.2929 (IC base=+0.097)

- **PATRÓN** `ballena_activa_n` < `31.0` → IC=+0.164 (n=147)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 31.0 (IC base=+0.097)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `streak_len` > `5.0` → IC=-0.250 (n=22)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=111)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.196 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=112)

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
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=37)

- **FILTRO** `streak_len` > `3.0` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=51)

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
- **PATRÓN** `regimen_ma_toques` > `4.0` → IC=+0.152 (n=21)

  - _Acción_: Kelly boost +0.76€ cuando `regimen_ma_toques` > 4.0 (IC base=+0.045)

- **PATRÓN** `volumen_racha` < `16919.513` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_racha` < 16919.513 (IC base=+0.045)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=1059)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=1338)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=1244)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=1293)

### STRUCT_NO_15M
- **FILTRO** `py_entrada` < `0.455` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.105 (n=36)

- **FILTRO** `libro_liquidez` < `6744.0765` → IC=-0.175 (n=38)

  - _Acción_: SKIP cuando `libro_liquidez` < 6744.0765
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=13)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=4734)

### STRUCT_NO_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.455` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.105 (n=36)

- **FILTRO** `libro_liquidez` < `6744.0765` → IC=-0.175 (n=38)

  - _Acción_: SKIP cuando `libro_liquidez` < 6744.0765
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=13)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=2729)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.191 (n=1664)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0052 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.2172` → IC=+0.162 (n=4992)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.2172 (IC base=+0.148)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3547` → IC=+0.156 (n=4640)

  - _Acción_: Kelly boost +0.78€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3547 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.157 (n=4599)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 6.0 (IC base=+0.148)

- **PATRÓN** `ibs_15` > `0.5906` → IC=+0.234 (n=4457)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5906 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` > `0.1318` → IC=+0.140 (n=2391)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` > 0.1318 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` < `0.5098` → IC=+0.135 (n=4623)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.5098 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.394` → IC=+0.260 (n=952)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.394 (IC base=+0.148)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.151 (n=2947)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `4681.5356` → IC=+0.172 (n=1663)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 4681.5356 (IC base=+0.148)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=1927)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.223 (n=763)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0057 (IC base=+0.202)

- **PATRÓN** `drift_60min` |x|≤ `0.06` → IC=+0.259 (n=255)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.06 (IC base=+0.202)

- **PATRÓN** `drift_15min` |x|≤ `0.3811` → IC=+0.208 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3811 (IC base=+0.202)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2675` → IC=+0.223 (n=254)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2675 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.221 (n=794)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.202)

- **PATRÓN** `ibs_15` > `0.7086` → IC=+0.278 (n=762)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7086 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` > `0.376` → IC=+0.223 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.376 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` < `0.5198` → IC=+0.206 (n=859)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5198 (IC base=+0.202)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.598` → IC=+0.307 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.598 (IC base=+0.202)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.205 (n=987)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `11986.2969` → IC=+0.220 (n=508)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11986.2969 (IC base=+0.202)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.007` → IC=+0.149 (n=940)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.007 (IC base=+0.131)

- **PATRÓN** `drift_60min` |x|≤ `0.1094` → IC=+0.144 (n=628)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.1094 (IC base=+0.131)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1407` → IC=+0.134 (n=626)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.67€ cuando `delta_ratio_macro` |x|> 0.1407 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.135 (n=858)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 6.0 (IC base=+0.131)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.134 (n=989)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 17.0 (IC base=+0.131)

- **PATRÓN** `ibs_15` > `0.4963` → IC=+0.217 (n=939)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.4963 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` > `0.1183` → IC=+0.149 (n=591)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.1183 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` < `0.4301` → IC=+0.132 (n=994)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.4301 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.889` → IC=+0.280 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.889 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `5881.5817` → IC=+0.161 (n=426)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 5881.5817 (IC base=+0.131)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `ibs_15` > `0.6038` → IC=+0.135 (n=894)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.68€ cuando `ibs_15` > 0.6038 (IC base=+0.061)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` < `0.0254` → IC=+0.176 (n=1203)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0254 (IC base=+0.167)

- **PATRÓN** `drift_60min` |x|≤ `0.2189` → IC=+0.180 (n=1203)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.2189 (IC base=+0.167)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0982` → IC=+0.224 (n=367)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0982 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.172 (n=1097)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 6.0 (IC base=+0.167)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.174 (n=1073)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 14.0 (IC base=+0.167)

- **PATRÓN** `ibs_15` > `0.5593` → IC=+0.250 (n=1075)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5593 (IC base=+0.167)

- **PATRÓN** `dist_vwap_pct` > `0.13` → IC=+0.192 (n=661)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.13 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.892` → IC=+0.223 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.892 (IC base=+0.167)

- **PATRÓN** `libro_liquidez` > `2954.4444` → IC=+0.197 (n=546)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 2954.4444 (IC base=+0.167)

- **PATRÓN** `ibs_15` < `0.1111` → IC=+0.156 (n=960)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.78€ cuando `ibs_15` < 0.1111 (IC base=+0.067)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.387 (n=245)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.362)

- **PATRÓN** `drift_60min` |x|≤ `0.1122` → IC=+0.364 (n=490)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1122 (IC base=+0.362)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1501` → IC=+0.376 (n=489)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1501 (IC base=+0.362)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.107` → IC=+0.376 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.107 (IC base=+0.362)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.370 (n=776)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.362)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.363 (n=493)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.362)

- **PATRÓN** `ibs_15` > `0.7883` → IC=+0.392 (n=735)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7883 (IC base=+0.362)

- **PATRÓN** `dist_vwap_pct` > `0.1523` → IC=+0.378 (n=434)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1523 (IC base=+0.362)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.976` → IC=+0.398 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.976 (IC base=+0.362)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.366 (n=893)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.362)

- **PATRÓN** `libro_liquidez` > `9875.3038` → IC=+0.381 (n=333)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9875.3038 (IC base=+0.362)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `drift_60min` |x|≤ `0.0553` → IC=+0.371 (n=122)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0553 (IC base=+0.362)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2175` → IC=+0.374 (n=165)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2175 (IC base=+0.362)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1441` → IC=+0.397 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1441 (IC base=+0.362)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.379 (n=338)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.362)

- **PATRÓN** `ibs_15` > `0.8112` → IC=+0.385 (n=363)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8112 (IC base=+0.362)

- **PATRÓN** `dist_vwap_pct` > `0.3743` → IC=+0.391 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3743 (IC base=+0.362)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.114` → IC=+0.389 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.114 (IC base=+0.362)

- **PATRÓN** `libro_liquidez` > `9173.8264` → IC=+0.378 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9173.8264 (IC base=+0.362)

- **PATRÓN** `ballena_activa_n` < `489.0` → IC=+0.403 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 489.0 (IC base=+0.362)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.366 (n=372)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.361)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.377 (n=169)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.361)

- **PATRÓN** `drift_60min` |x|≤ `0.108` → IC=+0.364 (n=249)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.108 (IC base=+0.361)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0824` → IC=+0.371 (n=332)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0824 (IC base=+0.361)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2951` → IC=+0.372 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2951 (IC base=+0.361)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.364 (n=373)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.361)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.374 (n=172)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.361)

- **PATRÓN** `ibs_15` > `0.7604` → IC=+0.390 (n=372)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7604 (IC base=+0.361)

- **PATRÓN** `dist_vwap_pct` > `0.1202` → IC=+0.370 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1202 (IC base=+0.361)

- **PATRÓN** `dist_vwap_pct` < `0.2797` → IC=+0.363 (n=342)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2797 (IC base=+0.361)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.577` → IC=+0.402 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.577 (IC base=+0.361)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.365 (n=419)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.361)

- **PATRÓN** `libro_liquidez` > `4132.469` → IC=+0.377 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4132.469 (IC base=+0.361)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `libro_spread` > `0.01` → IC=-0.214 (n=2158)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=3040)

- **FILTRO** `libro_liquidez` < `4433.059` → IC=-0.159 (n=3430)

  - _Acción_: SKIP cuando `libro_liquidez` < 4433.059
  - _Potencial_: sin este filtro IC_bueno=+0.078 (n=1768)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1393` → IC=+0.218 (n=449)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1393 (IC base=-0.078)

- **PATRÓN** `ibs_15` > `0.6288` → IC=+0.280 (n=1192)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6288 (IC base=-0.078)

- **PATRÓN** `dist_vwap_pct` > `0.1107` → IC=+0.201 (n=697)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1107 (IC base=-0.078)

- **PATRÓN** `dist_vwap_pct` < `0.4198` → IC=+0.198 (n=1172)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` < 0.4198 (IC base=-0.078)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2353` → IC=+0.270 (n=1569)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2353 (IC base=-0.005)

- **PATRÓN** `ibs_15` < `0.3684` → IC=+0.284 (n=4708)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3684 (IC base=-0.005)

- **PATRÓN** `dist_vwap_pct` > `0.6601` → IC=+0.281 (n=668)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6601 (IC base=-0.005)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0322` → IC=-0.222 (n=2455)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0322
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=820)

- **FILTRO** `sigma_h` < `0.0037` → IC=-0.218 (n=818)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0037
  - _Potencial_: sin este filtro IC_bueno=-0.175 (n=2457)

- **FILTRO** `sigma_ewma_delta_pct` > `22.34` → IC=-0.256 (n=469)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 22.34
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=2806)

- **PATRÓN** `sigma_h` < `0.003` → IC=+0.151 (n=316)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.003 (IC base=+0.071)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2673` → IC=+0.284 (n=137)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2673 (IC base=+0.071)

- **PATRÓN** `ibs_15` > `0.7593` → IC=+0.328 (n=410)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7593 (IC base=+0.071)

- **PATRÓN** `dist_vwap_pct` > `0.1039` → IC=+0.277 (n=276)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1039 (IC base=+0.071)

- **PATRÓN** `dist_vwap_pct` < `0.4954` → IC=+0.288 (n=456)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4954 (IC base=+0.071)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.513` → IC=+0.145 (n=215)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 22.513 (IC base=+0.071)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0742` → IC=+0.233 (n=73)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0742 (IC base=-0.186)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0866` → IC=+0.308 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0866 (IC base=-0.186)

- **PATRÓN** `ibs_15` < `0.6255` → IC=+0.300 (n=73)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.6255 (IC base=-0.186)

- **PATRÓN** `dist_vwap_pct` < `0.0453` → IC=+0.303 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0453 (IC base=-0.186)

- **PATRÓN** `ballena_activa_n` < `393.0` → IC=+0.300 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 393.0 (IC base=-0.186)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.151 (n=781)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.158 (n=527)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0059 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.0735` → IC=+0.180 (n=264)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.0735 (IC base=+0.145)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2995` → IC=+0.193 (n=467)

  - _Acción_: Kelly boost +0.96€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2995 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.158 (n=428)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 11.0 (IC base=+0.145)

- **PATRÓN** `ibs_15` > `0.5679` → IC=+0.240 (n=599)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5679 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` > `0.115` → IC=+0.152 (n=374)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.115 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` < `0.2759` → IC=+0.147 (n=559)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.2759 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.049` → IC=+0.261 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.049 (IC base=+0.145)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.151 (n=781)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `9030.0177` → IC=+0.158 (n=200)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 9030.0177 (IC base=+0.145)

- **PATRÓN** `sigma_h` < `0.0082` → IC=+0.251 (n=1792)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0082 (IC base=+0.244)

- **PATRÓN** `drift_60min` |x|≤ `0.3575` → IC=+0.248 (n=1577)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3575 (IC base=+0.244)

- **PATRÓN** `drift_15min` |x|≤ `0.7796` → IC=+0.260 (n=1577)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7796 (IC base=+0.244)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2144` → IC=+0.267 (n=814)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2144 (IC base=+0.244)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.252 (n=666)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.244)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.246 (n=1218)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.244)

- **PATRÓN** `ibs_15` < `0.3798` → IC=+0.275 (n=1792)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3798 (IC base=+0.244)

- **PATRÓN** `dist_vwap_pct` > `0.6088` → IC=+0.271 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6088 (IC base=+0.244)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.267` → IC=+0.248 (n=696)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.267 (IC base=+0.244)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1844` → IC=-0.255 (n=300)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1844
  - _Potencial_: sin este filtro IC_bueno=-0.172 (n=902)

- **FILTRO** `drift_60min` |x|> `0.1722` → IC=-0.258 (n=407)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1722
  - _Potencial_: sin este filtro IC_bueno=-0.159 (n=795)

- **FILTRO** `drift_15min` |x|> `0.9084` → IC=-0.278 (n=300)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.9084
  - _Potencial_: sin este filtro IC_bueno=-0.164 (n=902)

- **FILTRO** `sigma_ewma_delta_pct` > `6.265` → IC=-0.199 (n=277)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.265
  - _Potencial_: sin este filtro IC_bueno=-0.190 (n=925)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.214 (n=229)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.187 (n=973)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1455` → IC=+0.188 (n=46)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.94€ cuando `delta_ratio_macro` |x|> 0.1455 (IC base=-0.193)

- **PATRÓN** `ibs_15` > `0.5625` → IC=+0.234 (n=62)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5625 (IC base=-0.193)

- **PATRÓN** `dist_vwap_pct` > `0.2752` → IC=+0.143 (n=26)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.2752 (IC base=-0.193)

- **PATRÓN** `dist_vwap_pct` < `0.4298` → IC=+0.154 (n=76)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.4298 (IC base=-0.193)

- **PATRÓN** `ibs_15` < `0.3846` → IC=+0.294 (n=800)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3846 (IC base=-0.031)

- **PATRÓN** `dist_vwap_pct` > `0.6797` → IC=+0.236 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6797 (IC base=-0.031)

- **PATRÓN** `dist_vwap_pct` < `0.1942` → IC=+0.244 (n=722)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1942 (IC base=-0.031)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.239 (n=721)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=734)

- **FILTRO** `libro_liquidez` < `2918.2419` → IC=-0.220 (n=960)

  - _Acción_: SKIP cuando `libro_liquidez` < 2918.2419
  - _Potencial_: sin este filtro IC_bueno=-0.198 (n=495)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.213)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.213)

- **PATRÓN** `delta_ratio_macro` |x|> `0.119` → IC=+0.275 (n=726)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.119 (IC base=-0.019)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0947` → IC=+0.295 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0947 (IC base=-0.019)

- **PATRÓN** `ibs_15` < `0.1346` → IC=+0.309 (n=727)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.1346 (IC base=-0.019)

- **PATRÓN** `dist_vwap_pct` > `0.7785` → IC=+0.338 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7785 (IC base=-0.019)

### UPDOWN_GBM_ETH_15M_HORA7
- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.147 (n=49)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0067 (IC base=+0.091)

- **PATRÓN** `drift_60min` |x|≤ `0.1919` → IC=+0.128 (n=49)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.64€ cuando `drift_60min` |x|≤ 0.1919 (IC base=+0.091)

- **PATRÓN** `drift_15min` |x|≤ `0.3763` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3763 (IC base=+0.091)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.235` → IC=+0.188 (n=30)

  - _Acción_: Kelly boost +0.94€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.235 (IC base=+0.091)

- **PATRÓN** `ibs_15` > `0.8489` → IC=+0.333 (n=22)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8489 (IC base=+0.091)

- **PATRÓN** `dist_vwap_pct` > `0.4193` → IC=+0.182 (n=20)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.4193 (IC base=+0.091)

- **PATRÓN** `dist_vwap_pct` < `0.0949` → IC=+0.179 (n=26)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` < 0.0949 (IC base=+0.091)

- **PATRÓN** `drift_60min` |x|≤ `0.082` → IC=+0.183 (n=58)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.082 (IC base=+0.060)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.147 (n=49)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0067 (IC base=+0.091)

- **PATRÓN** `drift_60min` |x|≤ `0.1919` → IC=+0.128 (n=49)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.64€ cuando `drift_60min` |x|≤ 0.1919 (IC base=+0.091)

- **PATRÓN** `drift_15min` |x|≤ `0.3763` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3763 (IC base=+0.091)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.235` → IC=+0.188 (n=30)

  - _Acción_: Kelly boost +0.94€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.235 (IC base=+0.091)

- **PATRÓN** `ibs_15` > `0.8489` → IC=+0.333 (n=22)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8489 (IC base=+0.091)

- **PATRÓN** `dist_vwap_pct` > `0.4193` → IC=+0.182 (n=20)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.4193 (IC base=+0.091)

- **PATRÓN** `dist_vwap_pct` < `0.0949` → IC=+0.179 (n=26)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` < 0.0949 (IC base=+0.091)

- **PATRÓN** `drift_60min` |x|≤ `0.082` → IC=+0.183 (n=58)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.082 (IC base=+0.060)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.296 (n=435)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0033 (IC base=+0.284)

- **PATRÓN** `drift_60min` |x|≤ `0.0722` → IC=+0.312 (n=574)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0722 (IC base=+0.284)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1516` → IC=+0.287 (n=868)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1516 (IC base=+0.284)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2227` → IC=+0.292 (n=792)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2227 (IC base=+0.284)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.298 (n=1343)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.284)

- **PATRÓN** `ibs_15` > `0.8385` → IC=+0.312 (n=1303)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8385 (IC base=+0.284)

- **PATRÓN** `dist_vwap_pct` > `0.266` → IC=+0.314 (n=567)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.266 (IC base=+0.284)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.101` → IC=+0.388 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.101 (IC base=+0.284)

- **PATRÓN** `libro_liquidez` > `13331.6544` → IC=+0.308 (n=435)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13331.6544 (IC base=+0.284)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.307 (n=231)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.278)

- **PATRÓN** `drift_60min` |x|≤ `0.0596` → IC=+0.316 (n=231)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0596 (IC base=+0.278)

- **PATRÓN** `drift_15min` |x|≤ `0.3847` → IC=+0.285 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3847 (IC base=+0.278)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3931` → IC=+0.284 (n=618)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3931 (IC base=+0.278)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.298 (n=721)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.278)

- **PATRÓN** `ibs_15` > `0.8292` → IC=+0.304 (n=691)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8292 (IC base=+0.278)

- **PATRÓN** `dist_vwap_pct` > `0.2504` → IC=+0.314 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2504 (IC base=+0.278)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.916` → IC=+0.391 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.916 (IC base=+0.278)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.279 (n=893)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.278)

- **PATRÓN** `libro_liquidez` > `15901.5027` → IC=+0.311 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15901.5027 (IC base=+0.278)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.302 (n=613)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0069 (IC base=+0.290)

- **PATRÓN** `drift_60min` |x|≤ `0.1093` → IC=+0.305 (n=409)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1093 (IC base=+0.290)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1409` → IC=+0.295 (n=408)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1409 (IC base=+0.290)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1007` → IC=+0.328 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1007 (IC base=+0.290)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.302 (n=585)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.290)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.294 (n=435)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.290)

- **PATRÓN** `ibs_15` > `0.8489` → IC=+0.318 (n=612)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8489 (IC base=+0.290)

- **PATRÓN** `dist_vwap_pct` > `0.2815` → IC=+0.315 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2815 (IC base=+0.290)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.379` → IC=+0.384 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.379 (IC base=+0.290)

### UPDOWN_OU_5M
- **FILTRO** `delta_ratio_macro` |x|≤ `0.126` → IC=-0.156 (n=91)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.126
  - _Potencial_: sin este filtro IC_bueno=-0.101 (n=279)

- **FILTRO** `ballena_activa_n` > `34.0` → IC=-0.129 (n=251)

  - _Acción_: SKIP cuando `ballena_activa_n` > 34.0
  - _Potencial_: sin este filtro IC_bueno=-0.084 (n=87)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.1228` → IC=-0.211 (n=119)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1228
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=369)

- **FILTRO** `sigma_h` > `0.007` → IC=-0.183 (n=121)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.007
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=367)

### UPDOWN_OU_5M#BNB#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1682` → IC=-0.191 (n=40)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1682
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=41)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.160 (n=48)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=54)

### UPDOWN_OU_5M#BTC#5min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1387` → IC=-0.136 (n=53)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1387
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=161)

- **FILTRO** `sigma_h` < `0.0053` → IC=-0.184 (n=36)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0053
  - _Potencial_: sin este filtro IC_bueno=-0.091 (n=20)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.2127` → IC=-0.233 (n=28)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2127
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=28)

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
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=47)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.306` → IC=-0.385 (n=24)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.306
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `sigma_h` < `0.0094` → IC=-0.167 (n=34)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0094
  - _Potencial_: sin este filtro IC_bueno=-0.119 (n=19)

- **FILTRO** `ballena_activa_n` > `42.0` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `ballena_activa_n` > 42.0
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=32)

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
- **PATRÓN** `T_h` > `87.9936` → IC=+0.180 (n=604)

  - _Acción_: Kelly boost +0.90€ cuando `T_h` > 87.9936 (IC base=+0.179)

- **PATRÓN** `ratio` < `0.9703` → IC=+0.396 (n=362)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9703 (IC base=+0.179)

- **PATRÓN** `T_h` > `119.8535` → IC=+0.355 (n=2703)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 119.8535 (IC base=+0.336)

- **PATRÓN** `ratio` > `1.0213` → IC=+0.386 (n=454)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0213 (IC base=+0.336)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `111.9936` → IC=+0.150 (n=255)

  - _Acción_: Kelly boost +0.75€ cuando `T_h` > 111.9936 (IC base=+0.141)

- **PATRÓN** `ratio` < `0.9933` → IC=+0.273 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9933 (IC base=+0.141)

- **PATRÓN** `T_h` > `111.9838` → IC=+0.315 (n=967)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9838 (IC base=+0.301)

- **PATRÓN** `ratio` > `1.0182` → IC=+0.358 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0182 (IC base=+0.301)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `85.7585` → IC=+0.228 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 85.7585 (IC base=+0.225)

- **PATRÓN** `ratio` < `0.9854` → IC=+0.402 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9854 (IC base=+0.225)

- **PATRÓN** `T_h` > `111.9969` → IC=+0.355 (n=977)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9969 (IC base=+0.322)

- **PATRÓN** `ratio` > `1.0312` → IC=+0.400 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0312 (IC base=+0.322)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.0788` → IC=+0.422 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.0788 (IC base=+0.398)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5906 sube el IC de +0.148 a +0.234 en UPDOWN_GBM#15min (n=4457). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7086 sube el IC de +0.202 a +0.278 en UPDOWN_GBM#BTC#15min (n=762). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.4963 sube el IC de +0.131 a +0.217 en UPDOWN_GBM#ETH#15min (n=939). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5593 sube el IC de +0.167 a +0.250 en UPDOWN_GBM#XRP#15min (n=1075). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1111 sube el IC de +0.067 a +0.156 en UPDOWN_GBM#XRP#15min (n=960). Ya aplicado como kelly_boost=+0.78€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6288 sube el IC de -0.078 a +0.280 en UPDOWN_GBM_15M_TARDIO (n=1192). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3684 sube el IC de -0.005 a +0.284 en UPDOWN_GBM_15M_TARDIO (n=4708). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7593 sube el IC de +0.071 a +0.328 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=410). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.6255 sube el IC de -0.186 a +0.300 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=73). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.5679 sube el IC de +0.145 a +0.240 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=599). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3798 sube el IC de +0.244 a +0.275 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=1792). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de -0.193 a +0.234 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=62). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3846 sube el IC de -0.031 a +0.294 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=800). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.213 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.1346 sube el IC de -0.019 a +0.309 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=727). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_YES, IBS > 0.8489 sube el IC de +0.091 a +0.333 en UPDOWN_GBM_ETH_15M_HORA7 (n=22). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_YES, IBS > 0.8489 sube el IC de +0.091 a +0.333 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=22). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8385 sube el IC de +0.284 a +0.312 en UPDOWN_GBM_IBS_ALTO (n=1303). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8292 sube el IC de +0.278 a +0.304 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=691). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8489 sube el IC de +0.290 a +0.318 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=612). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7883 sube el IC de +0.362 a +0.392 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=735). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8112 sube el IC de +0.362 a +0.385 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=363). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7604 sube el IC de +0.361 a +0.390 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=372). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 2143 | +0.085 | +230.91€ | 1 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 2143 | +0.085 | +230.91€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1738 | +0.086 | +191.63€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1738 | +0.086 | +191.63€ | 1 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 284 | +0.070 | +11.30€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 284 | +0.070 | +11.30€ | 5 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 90 | +0.130 | +28.32€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 90 | +0.130 | +28.32€ | 1 | 10 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 1059 | -0.023 | +72.10€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 1059 | -0.023 | +72.10€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE | 7 | +0.019 | +3.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE#15min | 7 | +0.019 | +3.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 812 | -0.038 | +57.76€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 812 | -0.038 | +57.76€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 163 | +0.051 | +17.26€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 163 | +0.051 | +17.26€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 77 | -0.032 | -6.17€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 77 | -0.032 | -6.17€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 46178 | -0.086 | -5868.47€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 2758 | +0.059 | -291.84€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 43420 | -0.095 | -5576.63€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4757 | -0.112 | -793.45€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4757 | -0.112 | -793.45€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 2758 | +0.059 | -291.84€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 2758 | +0.059 | -291.84€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 4785 | -0.109 | -921.30€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 4785 | -0.109 | -921.30€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 12617 | -0.043 | -1178.54€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 12617 | -0.043 | -1178.54€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 12493 | -0.113 | -1250.20€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 12493 | -0.113 | -1250.20€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 8768 | -0.128 | -1433.14€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 8768 | -0.128 | -1433.14€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 46535 | -0.012 | +2983.04€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 12005 | +0.005 | +1562.53€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 34530 | -0.018 | +1420.51€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 46535 | -0.012 | +2983.04€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 12005 | +0.005 | +1562.53€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 34530 | -0.018 | +1420.51€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 180125 | +0.113 | -7483.85€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#15min | 21264 | +0.180 | -669.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 823 | +0.003 | -78.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 147673 | +0.105 | -6355.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 10365 | +0.093 | -381.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 24474 | +0.103 | -1678.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 74 | -0.171 | +12.42€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 24385 | +0.104 | -1678.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 34295 | +0.124 | -583.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5588 | +0.179 | -219.53€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 24453 | +0.120 | -190.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 4212 | +0.079 | -150.87€ | 1 | 2 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 24523 | +0.098 | -1786.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 84 | -0.116 | +5.91€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 24424 | +0.099 | -1781.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 38436 | +0.123 | -806.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 9726 | +0.177 | -230.67€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 24827 | +0.105 | -511.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 3871 | +0.102 | -56.03€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#SOL | 33899 | +0.112 | -1544.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 5707 | +0.199 | -244.95€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 726 | +0.030 | -24.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 25184 | +0.096 | -1101.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 2282 | +0.102 | -174.10€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO#XRP | 24498 | +0.107 | -1084.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 85 | -0.121 | +7.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 24400 | +0.107 | -1092.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 29167 | +0.193 | -1962.36€ | 2 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 29167 | +0.193 | -1962.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 6592 | +0.174 | -629.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 6592 | +0.174 | -629.54€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 4128 | +0.197 | -149.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 4128 | +0.197 | -149.09€ | 3 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 6492 | +0.176 | -558.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 6492 | +0.176 | -558.89€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 5477 | +0.249 | -203.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 5477 | +0.249 | -203.23€ | 0 | 4 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 6399 | +0.185 | -435.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 6399 | +0.185 | -435.36€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 1207 | +0.426 | -44.86€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 1207 | +0.426 | -44.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 493 | +0.439 | -4.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 493 | +0.439 | -4.49€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE#15min | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 487 | +0.424 | -18.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 487 | +0.424 | -18.13€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 213 | +0.398 | -18.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 213 | +0.398 | -18.37€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 102906 | +0.200 | -7511.84€ | 3 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 102906 | +0.200 | -7511.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 17746 | +0.180 | -1962.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 17746 | +0.180 | -1962.98€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 16594 | +0.225 | -547.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 16594 | +0.225 | -547.14€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 17668 | +0.180 | -1872.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 17668 | +0.180 | -1872.76€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 16725 | +0.218 | -661.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 16725 | +0.218 | -661.04€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 17022 | +0.203 | -1080.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 17022 | +0.203 | -1080.91€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 17151 | +0.196 | -1387.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 17151 | +0.196 | -1387.02€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 39611 | +0.116 | +291.85€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 39611 | +0.116 | +291.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 19724 | +0.117 | +174.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 19724 | +0.117 | +174.98€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 19887 | +0.116 | +116.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 19887 | +0.116 | +116.87€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 2494 | +0.292 | -16.33€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 2494 | +0.292 | -16.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 1142 | +0.280 | -32.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 1142 | +0.280 | -32.72€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 1216 | +0.297 | +12.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 1216 | +0.297 | +12.40€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 136 | +0.341 | +3.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 136 | +0.341 | +3.99€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 1147 | +0.440 | -0.04€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 1147 | +0.440 | -0.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 549 | +0.433 | -9.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 549 | +0.433 | -9.48€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 547 | +0.447 | +8.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 547 | +0.447 | +8.19€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 51 | +0.406 | +1.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 51 | +0.406 | +1.25€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1899 | +0.068 | -83.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 725 | +0.046 | -64.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 1174 | +0.082 | -19.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1465 | +0.076 | -38.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 291 | +0.053 | -19.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 1174 | +0.082 | -19.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 80002 | +0.100 | -1921.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 6450 | +0.095 | +125.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 73552 | +0.101 | -2046.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 43777 | +0.105 | -454.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 6450 | +0.095 | +125.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 37327 | +0.107 | -579.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 16907 | +0.109 | -95.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 16907 | +0.109 | -95.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 19318 | +0.082 | -1371.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 19318 | +0.082 | -1371.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 914 | +0.186 | -109.27€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 914 | +0.186 | -109.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 914 | +0.186 | -109.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 914 | +0.186 | -109.27€ | 2 | 4 |
| ✅ GBM_LATE_15M | 54399 | +0.098 | +29996.97€ | 0 | 18 |
| ✅ GBM_LATE_15M#15min | 54399 | +0.098 | +29996.97€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 9029 | +0.224 | +7752.33€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 9029 | +0.224 | +7752.33€ | 0 | 22 |
| ✅ GBM_LATE_15M#BTC | 8299 | +0.174 | +6436.79€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 8299 | +0.174 | +6436.79€ | 0 | 21 |
| ✅ GBM_LATE_15M#DOGE | 9762 | +0.206 | +7653.09€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 9762 | +0.206 | +7653.09€ | 0 | 22 |
| ✅ GBM_LATE_15M#ETH | 7366 | +0.052 | +2302.66€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 7366 | +0.052 | +2302.66€ | 1 | 18 |
| ✅ GBM_LATE_15M#SOL | 7595 | -0.031 | +1956.02€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 7595 | -0.031 | +1956.02€ | 4 | 12 |
| ✅ GBM_LATE_15M#XRP | 12348 | -0.024 | +3896.08€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 12348 | -0.024 | +3896.08€ | 3 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 57363 | +0.085 | +33131.95€ | 0 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 57363 | +0.085 | +33131.95€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 11158 | -0.002 | +5932.59€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 11158 | -0.002 | +5932.59€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 12286 | +0.005 | +3232.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 12286 | +0.005 | +3232.12€ | 0 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 7832 | +0.292 | +8858.04€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 7832 | +0.292 | +8858.04€ | 0 | 23 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 10845 | +0.014 | +3337.95€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 10845 | +0.014 | +3337.95€ | 1 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 8871 | +0.045 | +3982.38€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 8871 | +0.045 | +3982.38€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 6371 | +0.316 | +7788.88€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 6371 | +0.316 | +7788.88€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 43099 | +0.178 | +35469.90€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 43099 | +0.178 | +35469.90€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 6485 | +0.239 | +6014.11€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 6485 | +0.239 | +6014.11€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 6837 | +0.139 | +5031.10€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 6837 | +0.139 | +5031.10€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 6925 | +0.223 | +5970.01€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 6925 | +0.223 | +5970.01€ | 0 | 19 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 7385 | +0.130 | +5728.29€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 7385 | +0.130 | +5728.29€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 8146 | +0.120 | +6136.03€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 8146 | +0.120 | +6136.03€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 7321 | +0.232 | +6590.37€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 7321 | +0.232 | +6590.37€ | 0 | 25 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 11683 | +0.126 | +5841.22€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 11683 | +0.126 | +5841.22€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 468 | +0.157 | +308.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 468 | +0.157 | +308.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 3336 | +0.131 | +1826.61€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 3336 | +0.131 | +1826.61€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 503 | +0.157 | +275.36€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 503 | +0.157 | +275.36€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 3449 | +0.126 | +1684.78€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 3449 | +0.126 | +1684.78€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 2906 | +0.093 | +1115.54€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 2906 | +0.093 | +1115.54€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 1021 | +0.169 | +630.22€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 1021 | +0.169 | +630.22€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO | 54621 | +0.186 | +44717.08€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#15min | 54621 | +0.186 | +44717.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 8625 | +0.249 | +8327.22€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 8625 | +0.249 | +8327.22€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 8662 | +0.136 | +5932.65€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 8662 | +0.136 | +5932.65€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 9270 | +0.234 | +8325.78€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 9270 | +0.234 | +8325.78€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 9056 | +0.139 | +6659.51€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 9056 | +0.139 | +6659.51€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 9685 | +0.123 | +6880.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 9685 | +0.123 | +6880.44€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 9323 | +0.239 | +8591.48€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 9323 | +0.239 | +8591.48€ | 0 | 20 |
| ✅ GBM_LATE_5M | 13712 | +0.210 | +11081.36€ | 1 | 27 |
| ✅ GBM_LATE_5M#5min | 13712 | +0.210 | +11081.36€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 1054 | +0.246 | +1000.28€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 1054 | +0.246 | +1000.28€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 3257 | +0.211 | +2804.80€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 3257 | +0.211 | +2804.80€ | 0 | 25 |
| ✅ GBM_LATE_5M#DOGE | 1286 | +0.203 | +988.61€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1286 | +0.203 | +988.61€ | 0 | 17 |
| ✅ GBM_LATE_5M#ETH | 3973 | +0.202 | +2964.68€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 3973 | +0.202 | +2964.68€ | 0 | 24 |
| ✅ GBM_LATE_5M#SOL | 2183 | +0.207 | +1785.87€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 2183 | +0.207 | +1785.87€ | 0 | 25 |
| ✅ GBM_LATE_5M#XRP | 1959 | +0.209 | +1537.13€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1959 | +0.209 | +1537.13€ | 0 | 0 |
| ✅ GBM_LATE_60M | 4793 | +0.050 | +1304.06€ | 0 | 6 |
| ✅ GBM_LATE_60M#60min | 4793 | +0.050 | +1304.06€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 1681 | +0.059 | +527.20€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 1681 | +0.059 | +527.20€ | 1 | 5 |
| ✅ GBM_LATE_60M#ETH | 1549 | +0.051 | +461.06€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 1549 | +0.051 | +461.06€ | 2 | 6 |
| ✅ GBM_LATE_60M#SOL | 1563 | +0.039 | +315.80€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 1563 | +0.039 | +315.80€ | 0 | 10 |
| 🚫 GBM_LATE_60M_FADE | 691 | -0.250 | -36.66€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 691 | -0.250 | -36.66€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 253 | -0.253 | -21.29€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 253 | -0.253 | -21.29€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 254 | -0.242 | -5.91€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 254 | -0.242 | -5.91€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 184 | -0.253 | -9.46€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 184 | -0.253 | -9.46€ | 7 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 1976 | +0.084 | +511.84€ | 0 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 1976 | +0.084 | +511.84€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 770 | +0.072 | +194.29€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 770 | +0.072 | +194.29€ | 1 | 5 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 689 | +0.060 | +123.82€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 689 | +0.060 | +123.82€ | 1 | 12 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 517 | +0.132 | +193.73€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 517 | +0.132 | +193.73€ | 1 | 9 |
| ✅ LATE_WINDOW_5MIN | 225 | +0.293 | +252.39€ | 1 | 13 |
| ✅ LATE_WINDOW_5MIN#5min | 225 | +0.293 | +252.39€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 225 | +0.293 | +252.39€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 225 | +0.293 | +252.39€ | 1 | 13 |
| ✅ LEADLAG_BTC_XRP_15M | 4253 | +0.098 | +974.95€ | 0 | 1 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 4253 | +0.098 | +974.95€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 4253 | +0.098 | +974.95€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 4253 | +0.098 | +974.95€ | 0 | 1 |
| ✅ LIQUIDACIONES_15M | 960 | -0.013 | +12.21€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 960 | -0.013 | +12.21€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 52 | +0.000 | -0.43€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 52 | +0.000 | -0.43€ | 0 | 1 |
| ✅ LIQUIDACIONES_15M#BTC | 261 | -0.021 | +3.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 261 | -0.021 | +3.07€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 33 | -0.157 | -5.64€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 33 | -0.157 | -5.64€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 260 | +0.027 | +20.08€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 260 | +0.027 | +20.08€ | 2 | 1 |
| ✅ LIQUIDACIONES_15M#SOL | 288 | -0.003 | +3.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 288 | -0.003 | +3.92€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 66 | -0.118 | -8.79€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 66 | -0.118 | -8.79€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 4139 | +0.017 | +123.93€ | 5 | 1 |
| ✅ LIQUIDACIONES_5M#5min | 4139 | +0.017 | +123.93€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 200 | +0.025 | -1.25€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 200 | +0.025 | -1.25€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 824 | +0.016 | +41.61€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 824 | +0.016 | +41.61€ | 4 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 235 | +0.023 | +22.50€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 235 | +0.023 | +22.50€ | 0 | 1 |
| ✅ LIQUIDACIONES_5M#ETH | 1642 | +0.019 | +28.38€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1642 | +0.019 | +28.38€ | 6 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 767 | +0.011 | +1.87€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 767 | +0.011 | +1.87€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 471 | +0.016 | +30.81€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 471 | +0.016 | +30.81€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 2251 | -0.034 | -12.09€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 2251 | -0.034 | -12.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 680 | -0.032 | -12.81€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 680 | -0.032 | -12.81€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 799 | -0.008 | +17.86€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 799 | -0.008 | +17.86€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 772 | -0.061 | -17.14€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 772 | -0.061 | -17.14€ | 5 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 14271 | -0.032 | -142.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 6837 | -0.035 | -94.79€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 7434 | -0.030 | -47.28€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 507 | -0.050 | -25.69€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 259 | -0.017 | +6.09€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 248 | -0.084 | -31.78€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 3734 | -0.026 | -14.86€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 1776 | -0.024 | +0.73€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 1958 | -0.028 | -15.59€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 1419 | -0.029 | +11.73€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 725 | -0.034 | -1.18€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 694 | -0.023 | +12.91€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 3225 | -0.036 | -67.67€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 1515 | -0.039 | -45.34€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 1710 | -0.033 | -22.33€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 2741 | -0.027 | +16.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 1323 | -0.034 | -14.40€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 1418 | -0.020 | +31.32€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 2645 | -0.041 | -62.50€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 1239 | -0.048 | -40.70€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 1406 | -0.035 | -21.80€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M | 14662 | -0.012 | -218.19€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 14662 | -0.012 | -218.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 578 | -0.010 | -0.50€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 64260 | +0.000 | +3501.36€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 64260 | +0.000 | +3501.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 11630 | +0.027 | +1587.61€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 11630 | +0.027 | +1587.61€ | 2 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 9036 | -0.035 | -88.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 9036 | -0.035 | -88.88€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 11765 | +0.025 | +1290.45€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 11765 | +0.025 | +1290.45€ | 1 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 8943 | -0.050 | -193.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 8943 | -0.050 | -193.80€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 10928 | -0.004 | +300.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 10928 | -0.004 | +300.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 11958 | +0.018 | +605.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 11958 | +0.018 | +605.42€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 7088 | -0.055 | -118.67€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 7088 | -0.055 | -118.67€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1244 | -0.002 | -15.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1244 | -0.002 | -15.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1952 | -0.066 | -29.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1952 | -0.066 | -29.34€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 71 | -0.007 | +0.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 71 | -0.007 | +0.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 802 | -0.118 | -33.59€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 802 | -0.118 | -33.59€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 2158 | -0.069 | -14.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 2158 | -0.069 | -14.19€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 861 | -0.017 | -26.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 861 | -0.017 | -26.50€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3376 | +0.004 | -1.92€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3376 | +0.004 | -1.92€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 133 | -0.033 | -0.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 133 | -0.033 | -0.70€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 195 | +0.008 | -2.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 195 | +0.008 | -2.19€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 139 | -0.004 | -2.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 139 | -0.004 | -2.34€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1326 | +0.006 | +6.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1326 | +0.006 | +6.37€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1391 | +0.007 | -0.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1391 | +0.007 | -0.19€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 192 | -0.010 | -2.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 192 | -0.010 | -2.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 157972 | -0.077 | +2371.57€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 157972 | -0.077 | +2371.57€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 27629 | -0.078 | +1565.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 27629 | -0.078 | +1565.27€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 23644 | -0.101 | -1148.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 23644 | -0.101 | -1148.20€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 27986 | -0.068 | +1419.08€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 27986 | -0.068 | +1419.08€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 23182 | -0.097 | -644.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 23182 | -0.097 | -644.30€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 28264 | -0.058 | +348.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 28264 | -0.058 | +348.22€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 27267 | -0.069 | +831.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 27267 | -0.069 | +831.49€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 9000 | -0.035 | -184.95€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 9000 | -0.035 | -184.95€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 1002 | -0.017 | -19.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 1002 | -0.017 | -19.42€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 2075 | -0.047 | -29.92€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 2075 | -0.047 | -29.92€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1009 | -0.021 | -31.94€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2635 | -0.025 | -37.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2635 | -0.025 | -37.79€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1269 | -0.065 | -33.39€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1269 | -0.065 | -33.39€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 1010 | -0.031 | -32.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 1010 | -0.031 | -32.49€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 2071 | +0.118 | +812.12€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#5min | 1935 | +0.123 | +799.52€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 463 | +0.130 | +218.28€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 463 | +0.130 | +218.28€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#DOGE | 396 | +0.118 | +138.59€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 396 | +0.118 | +138.59€ | 0 | 2 |
| ✅ ORDER_FLOW_5M#ETH | 364 | +0.128 | +168.35€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 364 | +0.128 | +168.35€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 330 | +0.142 | +169.50€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 330 | +0.142 | +169.50€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#XRP | 382 | +0.094 | +104.80€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 382 | +0.094 | +104.80€ | 0 | 2 |
| ✅ ORDER_FLOW_5M_REACTIVO | 2033 | -0.017 | -15.12€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 2033 | -0.017 | -15.12€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 383 | +0.017 | +27.81€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 383 | +0.017 | +27.81€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 375 | -0.049 | -27.08€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 375 | -0.049 | -27.08€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 506 | -0.041 | -32.23€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 506 | -0.041 | -32.23€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 410 | +0.000 | +2.34€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 410 | +0.000 | +2.34€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 359 | -0.001 | +14.04€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 359 | -0.001 | +14.04€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 1102 | -0.080 | -57.10€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 506 | -0.112 | -80.05€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 394 | -0.129 | -61.59€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 112 | -0.053 | -18.46€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 388 | -0.038 | +18.02€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 277 | -0.023 | +27.46€ | 1 | 2 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 111 | -0.075 | -9.44€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 208 | -0.076 | +4.94€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 172 | -0.075 | +3.10€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 36 | -0.079 | +1.84€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 843 | -0.083 | -31.03€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 259 | -0.067 | -26.07€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 1391 | -0.208 | -90.18€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC | 547 | -0.209 | -50.21€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#atexpiry | 480 | -0.207 | -45.90€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#reach | 67 | -0.210 | -4.31€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 464 | -0.210 | -39.61€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 406 | -0.221 | -46.51€ | 5 | 1 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 58 | -0.133 | +6.91€ | 1 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL | 380 | -0.202 | -0.37€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 353 | -0.199 | -2.77€ | 5 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 27 | -0.224 | +2.40€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 1239 | -0.210 | -95.18€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 152 | -0.188 | +5.00€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 526 | +0.379 | +488.57€ | 0 | 13 |
| ✅ RESOLUTION_SNIPER#BTC | 102 | +0.154 | +77.00€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 102 | +0.154 | +77.00€ | 0 | 5 |
| ✅ RESOLUTION_SNIPER#ETH | 123 | +0.364 | +103.53€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 123 | +0.364 | +103.53€ | 0 | 5 |
| ✅ RESOLUTION_SNIPER#SOL | 301 | +0.457 | +308.04€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 301 | +0.457 | +308.04€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#sniper | 526 | +0.379 | +488.57€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 901 | +0.046 | +86.50€ | 2 | 3 |
| ✅ STREAK_FADE_15M#15min | 901 | +0.046 | +86.50€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 340 | +0.029 | +8.64€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 340 | +0.029 | +8.64€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 71 | +0.007 | +0.21€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 71 | +0.007 | +0.21€ | 1 | 1 |
| ✅ STREAK_FADE_15M#SOL | 83 | +0.018 | +6.06€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 83 | +0.018 | +6.06€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 407 | +0.072 | +71.60€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 407 | +0.072 | +71.60€ | 1 | 4 |
| ✅ STREAK_FADE_5M | 3560 | -0.023 | -143.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3560 | -0.023 | -143.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 1127 | -0.023 | -40.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 1127 | -0.023 | -40.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 609 | -0.029 | -27.28€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 609 | -0.029 | -27.28€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 170 | -0.041 | -14.29€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 170 | -0.041 | -14.29€ | 4 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1654 | -0.020 | -61.43€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1654 | -0.020 | -61.43€ | 2 | 0 |
| ✅ STREAK_FADE_60M | 116 | -0.042 | -10.16€ | 5 | 0 |
| ✅ STREAK_FADE_60M#60min | 116 | -0.042 | -10.16€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 44 | -0.087 | -4.62€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 44 | -0.087 | -4.62€ | 4 | 0 |
| ✅ STREAK_FADE_60M#SOL | 72 | -0.013 | -5.54€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 72 | -0.013 | -5.54€ | 0 | 2 |
| ✅ STREAK_MOM_5M | 11463 | +0.014 | +72.34€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 11463 | +0.014 | +72.34€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2986 | +0.017 | +22.84€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2986 | +0.017 | +22.84€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2983 | +0.017 | +35.66€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2983 | +0.017 | +35.66€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2915 | +0.008 | -3.30€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2915 | +0.008 | -3.30€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2579 | +0.013 | +17.14€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2579 | +0.013 | +17.14€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 11425 | +0.017 | -18.08€ | 2 | 0 |
| ✅ STRUCT_NO_15M#15min | 11425 | +0.017 | -18.08€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 4753 | +0.021 | +6.61€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 4753 | +0.021 | +6.61€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3909 | +0.015 | -12.17€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3909 | +0.015 | -12.17€ | 2 | 0 |
| ✅ STRUCT_NO_15M#SOL | 2763 | +0.011 | -12.52€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 2763 | +0.011 | -12.52€ | 1 | 0 |
| ✅ UPDOWN_GBM | 100685 | +0.059 | +9556.15€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 24578 | +0.080 | +5111.19€ | 0 | 10 |
| ✅ UPDOWN_GBM#240min | 3033 | +0.001 | +29.92€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 66765 | +0.060 | +4307.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 5962 | +0.001 | +109.64€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 8441 | +0.104 | +1546.53€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1781 | +0.164 | +820.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 90 | -0.011 | -2.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 6570 | +0.090 | +728.33€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 22957 | +0.057 | +2002.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 3310 | +0.080 | +753.55€ | 0 | 11 |
| ✅ UPDOWN_GBM#BTC#240min | 855 | +0.002 | +14.06€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 15994 | +0.065 | +1160.81€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 2672 | -0.003 | +69.67€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 126 | -0.062 | +4.75€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 10902 | +0.077 | +1253.34€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1761 | +0.154 | +738.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 86 | +0.023 | -0.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 9055 | +0.063 | +515.77€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 23883 | +0.049 | +1654.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 5839 | +0.072 | +887.66€ | 0 | 10 |
| ✅ UPDOWN_GBM#ETH#240min | 826 | +0.005 | +16.04€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 14909 | +0.051 | +718.26€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 2193 | +0.003 | +30.64€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 116 | -0.102 | +2.28€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 21482 | +0.039 | +1205.88€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 6476 | +0.032 | +423.49€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#240min | 779 | -0.010 | +4.30€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 13027 | +0.049 | +775.93€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 1097 | +0.005 | +9.34€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#daily | 103 | -0.138 | -7.17€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 13018 | +0.073 | +1894.53€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 5411 | +0.096 | +1487.86€ | 0 | 10 |
| ✅ UPDOWN_GBM#XRP#240min | 397 | +0.006 | -1.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 7210 | +0.059 | +408.29€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 345 | -0.099 | -0.14€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 979 | +0.362 | +350.46€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 979 | +0.362 | +350.46€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 484 | +0.362 | +168.39€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 484 | +0.362 | +168.39€ | 0 | 9 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 495 | +0.361 | +182.07€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 495 | +0.361 | +182.07€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO | 24324 | -0.021 | +6037.24€ | 2 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 24324 | -0.021 | +6037.24€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1981 | -0.051 | +561.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1981 | -0.051 | +561.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 4538 | -0.114 | +236.88€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 4538 | -0.114 | +236.88€ | 3 | 11 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 1071 | +0.222 | +899.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 1071 | +0.222 | +899.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 3187 | +0.219 | +2039.88€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 3187 | +0.219 | +2039.88€ | 1 | 19 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 6872 | -0.059 | +1031.91€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 6872 | -0.059 | +1031.91€ | 5 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 6675 | -0.062 | +1267.53€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 6675 | -0.062 | +1267.53€ | 2 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 294 | +0.068 | +27.03€ | 0 | 8 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 294 | +0.068 | +27.03€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 294 | +0.068 | +27.03€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 294 | +0.068 | +27.03€ | 0 | 8 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1737 | +0.284 | +1459.14€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1737 | +0.284 | +1459.14€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 921 | +0.278 | +725.24€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 921 | +0.278 | +725.24€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 816 | +0.290 | +733.91€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 816 | +0.290 | +733.91€ | 0 | 9 |
| ✅ UPDOWN_OU_5M | 858 | -0.113 | -84.85€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 858 | -0.113 | -84.85€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 270 | -0.081 | -20.33€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 270 | -0.081 | -20.33€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 95 | -0.170 | -10.94€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 95 | -0.170 | -10.94€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 110 | -0.179 | -4.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 110 | -0.179 | -4.23€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 38 | -0.175 | -6.61€ | 2 | 0 |
| ✅ WEEKLY_PRICE | 4474 | +0.303 | +2066.85€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 1697 | +0.260 | +231.35€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 1721 | +0.296 | +747.11€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 1056 | +0.381 | +1088.39€ | 0 | 1 |