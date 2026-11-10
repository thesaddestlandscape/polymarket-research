# Hipótesis automáticas — 2026-11-10 11:37 UTC
_Generado por shadow_postmortem.py sobre 1273427 resoluciones (PNL=+173995.73€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.5` → IC=-0.317 (n=195)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.118 (n=697)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.196 (n=1020)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` > 0.505 (IC base=+0.127)

- **PATRÓN** `n_total_lado` > `62.0` → IC=+0.186 (n=323)

  - _Acción_: Kelly boost +0.93€ cuando `n_total_lado` > 62.0 (IC base=+0.127)

- **PATRÓN** `banda_hit_calibrado` > `0.813` → IC=+0.272 (n=436)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.813 (IC base=+0.127)

- **PATRÓN** `banda_z` > `8.579` → IC=+0.199 (n=320)

  - _Acción_: Kelly boost +0.99€ cuando `banda_z` > 8.579 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.143 (n=359)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 17.0 (IC base=+0.127)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.128 (n=689)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 12.0 (IC base=+0.127)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.141 (n=1046)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.127)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.302 (n=165)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.113 (n=497)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.193 (n=885)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.505 (IC base=+0.130)

- **PATRÓN** `n_total_lado` > `65.0` → IC=+0.184 (n=280)

  - _Acción_: Kelly boost +0.92€ cuando `n_total_lado` > 65.0 (IC base=+0.130)

- **PATRÓN** `banda_hit_calibrado` > `0.8126` → IC=+0.274 (n=378)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8126 (IC base=+0.130)

- **PATRÓN** `banda_z` > `8.854` → IC=+0.210 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 8.854 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.138 (n=750)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 8.0 (IC base=+0.130)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.130 (n=587)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 12.0 (IC base=+0.130)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.137 (n=946)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.130)

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
- **FILTRO** `restante_s_al_confirmar` < `132.48` → IC=-0.221 (n=11747)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 132.48
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=35246)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `125.14` → IC=-0.259 (n=1198)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 125.14
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=3594)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `116.47` → IC=-0.288 (n=1217)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 116.47
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=3655)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `restante_s_al_confirmar` < `117.17` → IC=-0.164 (n=3208)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 117.17
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=9625)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `151.8` → IC=-0.244 (n=3196)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 151.8
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=9590)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `128.77` → IC=-0.263 (n=2204)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 128.77
  - _Potencial_: sin este filtro IC_bueno=-0.084 (n=6613)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.210 (n=27466)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.104)

- **PATRÓN** `libro_liquidez` > `8331.6086` → IC=+0.159 (n=2314)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 8331.6086 (IC base=+0.104)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.129 (n=23556)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 17.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.130 (n=28704)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.124)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.224 (n=21638)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.140 (n=8251)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `6578.5422` → IC=+0.145 (n=3184)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 6578.5422 (IC base=+0.124)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.185 (n=2091)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 6.0 (IC base=+0.177)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.363 (n=697)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.177)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.180 (n=2686)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.01 (IC base=+0.177)

- **PATRÓN** `libro_liquidez` > `9413.2764` → IC=+0.180 (n=1868)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 9413.2764 (IC base=+0.177)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.186 (n=1905)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 7.0 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.182 (n=2134)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 17.0 (IC base=+0.179)

- **PATRÓN** `py_entrada` < `0.295` → IC=+0.312 (n=981)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.295 (IC base=+0.179)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.181 (n=2732)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.01 (IC base=+0.179)

- **PATRÓN** `libro_liquidez` > `16076.7957` → IC=+0.183 (n=705)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 16076.7957 (IC base=+0.179)

### FAVORITO_CONFIRMADO#BTC#60min
- **FILTRO** `py_entrada` < `0.55` → IC=-0.335 (n=95)

  - _Acción_: SKIP cuando `py_entrada` < 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.095 (n=2180)

- **PATRÓN** `py_entrada` > `0.61` → IC=+0.168 (n=598)

  - _Acción_: Kelly boost +0.84€ cuando `py_entrada` > 0.61 (IC base=+0.077)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.144 (n=1406)

  - _Acción_: Kelly boost +0.72€ cuando `py_entrada` < 0.44 (IC base=+0.083)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.170 (n=5240)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 5.0 (IC base=+0.166)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.171 (n=4427)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 15.0 (IC base=+0.166)

- **PATRÓN** `py_entrada` > `0.77` → IC=+0.375 (n=1715)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.77 (IC base=+0.166)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.209 (n=2370)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.201)

- **PATRÓN** `py_entrada` < `0.275` → IC=+0.330 (n=943)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.275 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.204 (n=2762)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.201)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.144 (n=633)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 15.0 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.146 (n=1142)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 15.0 (IC base=+0.141)

- **PATRÓN** `py_entrada` > `0.675` → IC=+0.255 (n=434)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.675 (IC base=+0.141)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=1085)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.156 (n=155)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.075)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.253 (n=941)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.227)

- **PATRÓN** `py_entrada` > `0.83` → IC=+0.421 (n=1309)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.83 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.146 (n=1414)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 7.0 (IC base=+0.145)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.153 (n=727)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 7.0 (IC base=+0.145)

- **PATRÓN** `py_entrada` < `0.345` → IC=+0.278 (n=717)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.345 (IC base=+0.145)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `py_entrada` > `0.55` → IC=+0.162 (n=459)

  - _Acción_: Kelly boost +0.81€ cuando `py_entrada` > 0.55 (IC base=+0.045)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.147 (n=468)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 17.0 (IC base=+0.122)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.243 (n=423)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.122)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `10.0` → IC=-0.297 (n=72)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.232 (n=151)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.202 (n=23623)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.199 (n=19998)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 15.0 (IC base=+0.197)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.226 (n=9900)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.197)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.338 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.197)

- **PATRÓN** `libro_liquidez` > `4915.142` → IC=+0.338 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4915.142 (IC base=+0.197)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.175 (n=5390)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 5.0 (IC base=+0.171)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.172 (n=5378)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 18.0 (IC base=+0.171)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.181 (n=5394)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` < 0.74 (IC base=+0.171)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.380 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.247 (n=89)

- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=90)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.215 (n=3172)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.211)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.216 (n=2117)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.211)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.253 (n=1586)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.211)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.183 (n=5274)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.179 (n=4484)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 15.0 (IC base=+0.177)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.178 (n=5434)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` < 0.73 (IC base=+0.177)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.185 (n=4130)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` > 0.71 (IC base=+0.177)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.258 (n=4447)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.251)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.252 (n=3769)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.251)

- **PATRÓN** `py_entrada` > `0.8` → IC=+0.366 (n=1420)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.190 (n=5177)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.187)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.191 (n=4398)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 15.0 (IC base=+0.187)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.193 (n=3850)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.71 (IC base=+0.187)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.429 (n=954)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.425)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.426 (n=951)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.425)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.438 (n=964)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.425)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.431 (n=1014)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.425)

- **PATRÓN** `libro_liquidez` > `4577.7327` → IC=+0.443 (n=615)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4577.7327 (IC base=+0.425)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.438 (n=387)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.439)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.442 (n=396)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.439)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.449 (n=425)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.439)

- **PATRÓN** `libro_liquidez` > `12430.0394` → IC=+0.444 (n=340)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12430.0394 (IC base=+0.439)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.431 (n=375)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.423)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.426 (n=376)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.423)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.434 (n=379)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.423)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.429 (n=422)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.423)

- **PATRÓN** `libro_liquidez` > `4758.7803` → IC=+0.429 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4758.7803 (IC base=+0.423)

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

- **FILTRO** `py_entrada` > `0.76` → IC=-0.295 (n=37)

  - _Acción_: SKIP cuando `py_entrada` > 0.76
  - _Potencial_: sin este filtro IC_bueno=-0.233 (n=13)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=34)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.205 (n=30929)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.240 (n=31310)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.200)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.188 (n=4615)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 18.0 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.180 (n=9925)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 12.0 (IC base=+0.179)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.190 (n=14204)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.71 (IC base=+0.179)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.228 (n=6418)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.224)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.287 (n=4403)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.224)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.182 (n=12987)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 7.0 (IC base=+0.179)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.197 (n=10992)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` > 0.72 (IC base=+0.179)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.835` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.835
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.228 (n=4336)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.222 (n=4970)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.218)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.269 (n=4327)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.218)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **FILTRO** `hora_utc` > `3.0` → IC=-0.278 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.205 (n=11796)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.256 (n=4528)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.202 (n=5140)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.199 (n=5138)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 6.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.245 (n=5377)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.196)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.193 (n=11146)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.140 (n=11659)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `3.46` → IC=+0.138 (n=13571)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 3.46 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.195 (n=5430)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.144 (n=5256)

  - _Acción_: Kelly boost +0.72€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.126 (n=6822)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 7.0 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `2.59` → IC=+0.143 (n=5113)

  - _Acción_: Kelly boost +0.72€ cuando `lag_apertura_s` < 2.59 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.192 (n=5716)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.138 (n=7116)

  - _Acción_: Kelly boost +0.69€ cuando `restante_min` > 4.95 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `3.14` → IC=+0.138 (n=6806)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 3.14 (IC base=+0.117)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.307 (n=1370)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.292)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.387 (n=705)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.292)

- **PATRÓN** `libro_liquidez` > `3959.4948` → IC=+0.292 (n=869)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3959.4948 (IC base=+0.292)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.285 (n=921)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.281)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.364 (n=306)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.281)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.318 (n=664)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.296)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.300 (n=973)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.296)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.395 (n=332)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.296)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` < `16.0` → IC=+0.366 (n=95)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.344)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.391 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.344)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.378 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.344)

- **PATRÓN** `libro_liquidez` > `745.0217` → IC=+0.375 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 745.0217 (IC base=+0.344)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.442 (n=934)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.438)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.444 (n=903)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.438)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.439 (n=1087)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.438)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.436 (n=436)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.431)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.435 (n=305)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.431)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.436 (n=452)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.431)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.460 (n=148)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.445)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.445 (n=381)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.445)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.447 (n=415)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.445)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.446 (n=516)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.445)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4775` → IC=+0.140 (n=17479)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.4775 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.127 (n=17663)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 6.0 (IC base=+0.123)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.127 (n=12202)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 12.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` > `0.9776` → IC=+0.246 (n=5827)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9776 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` > `0.7915` → IC=+0.284 (n=975)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7915 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.493` → IC=+0.185 (n=8737)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 3.493 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` > `0.626` → IC=+0.266 (n=5214)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.626 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` > `0.3046` → IC=+0.250 (n=1808)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3046 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` > `2.7529` → IC=+0.235 (n=4185)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7529 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.135 (n=8676)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.123)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.122 (n=10935)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0062 (IC base=+0.083)

- **PATRÓN** `ibs_20min` < `0.5652` → IC=+0.143 (n=21839)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.5652 (IC base=+0.083)

- **PATRÓN** `dist_vwap_pct` > `0.6112` → IC=+0.191 (n=1455)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.6112 (IC base=+0.083)

- **PATRÓN** `dist_vwap_pct` < `0.1612` → IC=+0.191 (n=8702)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` < 0.1612 (IC base=+0.083)

- **PATRÓN** `volumen_regimen` < `0.697` → IC=+0.197 (n=3923)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_regimen` < 0.697 (IC base=+0.083)

- **PATRÓN** `volumen_pendiente_norm` > `0.2968` → IC=+0.232 (n=2190)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2968 (IC base=+0.083)

- **PATRÓN** `volumen_spike_ratio` > `1.4571` → IC=+0.207 (n=15120)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4571 (IC base=+0.083)

- **PATRÓN** `ballena_activa_n` < `99.0` → IC=+0.229 (n=15023)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 99.0 (IC base=+0.083)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `drift_60min` |x|≤ `0.3643` → IC=+0.213 (n=3727)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3643 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.226 (n=1807)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.212)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.212 (n=2506)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` > `0.9866` → IC=+0.278 (n=1691)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9866 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.475` → IC=+0.279 (n=1657)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.475 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` > `0.2342` → IC=+0.255 (n=660)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2342 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `1.4375` → IC=+0.214 (n=3571)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4375 (IC base=+0.212)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.225 (n=4101)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.212)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.226 (n=2328)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.212)

- **PATRÓN** `sigma_h` > `0.0092` → IC=+0.246 (n=1485)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0092 (IC base=+0.244)

- **PATRÓN** `drift_60min` |x|≤ `0.0892` → IC=+0.280 (n=1091)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0892 (IC base=+0.244)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.252 (n=1222)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.244)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.247 (n=1512)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.244)

- **PATRÓN** `ibs_20min` < `0.5639` → IC=+0.260 (n=3271)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5639 (IC base=+0.244)

- **PATRÓN** `volumen_pendiente_norm` < `0.0952` → IC=+0.247 (n=2963)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0952 (IC base=+0.244)

- **PATRÓN** `volumen_pendiente_norm` > `0.2908` → IC=+0.251 (n=440)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2908 (IC base=+0.244)

- **PATRÓN** `volumen_spike_ratio` < `1.447` → IC=+0.247 (n=1040)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.447 (IC base=+0.244)

- **PATRÓN** `volumen_spike_ratio` > `1.8593` → IC=+0.247 (n=2080)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8593 (IC base=+0.244)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.246 (n=3759)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.244)

- **PATRÓN** `libro_liquidez` > `1775.6172` → IC=+0.249 (n=2181)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1775.6172 (IC base=+0.244)

- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.245 (n=1486)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 8.0 (IC base=+0.244)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.235 (n=1049)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.226)

- **PATRÓN** `drift_60min` |x|≤ `0.1094` → IC=+0.256 (n=1376)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1094 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.236 (n=3270)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.226)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.229 (n=2224)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.226)

- **PATRÓN** `ibs_20min` > `0.9055` → IC=+0.258 (n=1041)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9055 (IC base=+0.226)

- **PATRÓN** `dist_vwap_pct` > `0.1844` → IC=+0.233 (n=1427)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1844 (IC base=+0.226)

- **PATRÓN** `dist_vwap_pct` < `0.5244` → IC=+0.228 (n=3413)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5244 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.84` → IC=+0.263 (n=458)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.84 (IC base=+0.226)

- **PATRÓN** `volumen_regimen` > `0.6297` → IC=+0.231 (n=3123)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6297 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` > `0.2788` → IC=+0.269 (n=439)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2788 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` > `2.4452` → IC=+0.252 (n=1028)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4452 (IC base=+0.226)

- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.152 (n=3342)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0064 (IC base=+0.129)

- **PATRÓN** `drift_60min` |x|≤ `0.077` → IC=+0.153 (n=1114)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.077 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.152 (n=1246)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 17.0 (IC base=+0.129)

- **PATRÓN** `ibs_20min` < `0.3514` → IC=+0.201 (n=2228)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3514 (IC base=+0.129)

- **PATRÓN** `dist_vwap_pct` < `0.1373` → IC=+0.145 (n=3236)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.1373 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.974` → IC=+0.137 (n=3051)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 3.974 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` < `0.635` → IC=+0.151 (n=1114)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.635 (IC base=+0.129)

- **PATRÓN** `volumen_pendiente_norm` > `0.0717` → IC=+0.155 (n=1363)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` > 0.0717 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` < `2.4421` → IC=+0.140 (n=3214)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 2.4421 (IC base=+0.129)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.130 (n=4338)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.01 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `202.0` → IC=+0.175 (n=1393)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 202.0 (IC base=+0.129)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0114` → IC=+0.214 (n=1794)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0114 (IC base=+0.196)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.203 (n=4144)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.196)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.261 (n=1537)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.196)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.981` → IC=+0.281 (n=865)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.981 (IC base=+0.196)

- **PATRÓN** `volumen_pendiente_norm` < `0.0977` → IC=+0.198 (n=3535)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` < 0.0977 (IC base=+0.196)

- **PATRÓN** `volumen_pendiente_norm` > `0.3528` → IC=+0.225 (n=511)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3528 (IC base=+0.196)

- **PATRÓN** `volumen_spike_ratio` > `2.7305` → IC=+0.214 (n=1749)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7305 (IC base=+0.196)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.200 (n=4769)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.196)

- **PATRÓN** `libro_liquidez` > `1913.1432` → IC=+0.204 (n=1791)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1913.1432 (IC base=+0.196)

- **PATRÓN** `sigma_h` < `0.0111` → IC=+0.225 (n=3203)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0111 (IC base=+0.221)

- **PATRÓN** `drift_60min` |x|≤ `0.2922` → IC=+0.234 (n=2425)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2922 (IC base=+0.221)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.244 (n=1381)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.221)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.224 (n=1655)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.221)

- **PATRÓN** `ibs_20min` < `0.0455` → IC=+0.268 (n=1214)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0455 (IC base=+0.221)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.832` → IC=+0.268 (n=395)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.832 (IC base=+0.221)

- **PATRÓN** `volumen_pendiente_norm` > `0.3492` → IC=+0.257 (n=524)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3492 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` < `1.7683` → IC=+0.220 (n=1539)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7683 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` > `2.1618` → IC=+0.230 (n=2331)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1618 (IC base=+0.221)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.225 (n=1841)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.221)

- **PATRÓN** `libro_liquidez` > `1899.8184` → IC=+0.225 (n=1649)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1899.8184 (IC base=+0.221)

- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.225 (n=3484)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 25.0 (IC base=+0.221)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.170 (n=207)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=4750)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.150 (n=659)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0039 (IC base=+0.058)

- **PATRÓN** `ibs_20min` > `0.9428` → IC=+0.233 (n=656)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9428 (IC base=+0.058)

- **PATRÓN** `dist_vwap_pct` > `0.1397` → IC=+0.339 (n=458)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1397 (IC base=+0.058)

- **PATRÓN** `dist_vwap_pct` < `0.776` → IC=+0.333 (n=873)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.776 (IC base=+0.058)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.085` → IC=+0.202 (n=1436)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.085 (IC base=+0.058)

- **PATRÓN** `volumen_regimen` > `1.1051` → IC=+0.348 (n=353)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1051 (IC base=+0.058)

- **PATRÓN** `volumen_pendiente_norm` < `0.1672` → IC=+0.336 (n=631)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1672 (IC base=+0.058)

- **PATRÓN** `volumen_pendiente_norm` > `0.3037` → IC=+0.338 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3037 (IC base=+0.058)

- **PATRÓN** `volumen_spike_ratio` < `1.5405` → IC=+0.345 (n=334)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5405 (IC base=+0.058)

- **PATRÓN** `volumen_spike_ratio` > `2.2812` → IC=+0.338 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2812 (IC base=+0.058)

- **PATRÓN** `ballena_activa_n` < `142.0` → IC=+0.338 (n=769)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 142.0 (IC base=+0.058)

- **PATRÓN** `ibs_20min` < `0.0884` → IC=+0.190 (n=1241)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.0884 (IC base=+0.052)

- **PATRÓN** `dist_vwap_pct` > `0.3334` → IC=+0.163 (n=603)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 0.3334 (IC base=+0.052)

- **PATRÓN** `dist_vwap_pct` < `0.1384` → IC=+0.153 (n=2234)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.1384 (IC base=+0.052)

- **PATRÓN** `volumen_regimen` < `0.8329` → IC=+0.162 (n=1577)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8329 (IC base=+0.052)

- **PATRÓN** `volumen_pendiente_norm` > `0.2821` → IC=+0.212 (n=297)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2821 (IC base=+0.052)

- **PATRÓN** `volumen_spike_ratio` < `1.7747` → IC=+0.155 (n=1516)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 1.7747 (IC base=+0.052)

- **PATRÓN** `volumen_spike_ratio` > `1.5127` → IC=+0.157 (n=2031)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.5127 (IC base=+0.052)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.192 (n=141)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=752)

- **FILTRO** `ibs_20min` < `0.2581` → IC=-0.174 (n=222)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2581
  - _Potencial_: sin este filtro IC_bueno=+0.078 (n=671)

- **FILTRO** `ibs_20min` > `0.2` → IC=-0.132 (n=4671)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2
  - _Potencial_: sin este filtro IC_bueno=+0.154 (n=2310)

- **FILTRO** `sigma_ewma_delta_pct` > `8.28` → IC=-0.225 (n=750)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.28
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=6231)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.176 (n=304)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` > 0.75 (IC base=+0.015)

- **PATRÓN** `dist_vwap_pct` > `0.9554` → IC=+0.278 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9554 (IC base=+0.015)

- **PATRÓN** `dist_vwap_pct` < `0.4558` → IC=+0.271 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4558 (IC base=+0.015)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.939` → IC=+0.159 (n=209)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 4.939 (IC base=+0.015)

- **PATRÓN** `volumen_regimen` > `1.0155` → IC=+0.306 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0155 (IC base=+0.015)

- **PATRÓN** `volumen_pendiente_norm` < `0.0791` → IC=+0.286 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0791 (IC base=+0.015)

- **PATRÓN** `volumen_spike_ratio` < `2.1931` → IC=+0.290 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1931 (IC base=+0.015)

- **PATRÓN** `volumen_spike_ratio` > `1.544` → IC=+0.273 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.544 (IC base=+0.015)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.286 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.015)

- **PATRÓN** `ibs_20min` < `0.2` → IC=+0.154 (n=2310)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.2 (IC base=-0.037)

- **PATRÓN** `dist_vwap_pct` > `0.222` → IC=+0.289 (n=306)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.222 (IC base=-0.037)

- **PATRÓN** `dist_vwap_pct` < `0.4903` → IC=+0.280 (n=1183)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4903 (IC base=-0.037)

- **PATRÓN** `volumen_regimen` < `0.7051` → IC=+0.302 (n=452)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7051 (IC base=-0.037)

- **PATRÓN** `volumen_pendiente_norm` > `0.0793` → IC=+0.304 (n=462)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0793 (IC base=-0.037)

- **PATRÓN** `volumen_spike_ratio` < `2.4676` → IC=+0.300 (n=958)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4676 (IC base=-0.037)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `ibs_20min` < `0.7833` → IC=-0.156 (n=3558)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7833
  - _Potencial_: sin este filtro IC_bueno=+0.129 (n=1833)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.171 (n=1172)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=4219)

- **FILTRO** `ibs_20min` > `0.74` → IC=-0.194 (n=1863)

  - _Acción_: SKIP cuando `ibs_20min` > 0.74
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=5613)

- **PATRÓN** `ibs_20min` > `0.7833` → IC=+0.129 (n=1833)

  - _Acción_: Kelly boost +0.64€ cuando `ibs_20min` > 0.7833 (IC base=-0.059)

- **PATRÓN** `dist_vwap_pct` > `1.001` → IC=+0.362 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.001 (IC base=-0.059)

- **PATRÓN** `dist_vwap_pct` < `0.2507` → IC=+0.301 (n=932)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2507 (IC base=-0.059)

- **PATRÓN** `volumen_regimen` > `0.7048` → IC=+0.318 (n=930)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7048 (IC base=-0.059)

- **PATRÓN** `volumen_pendiente_norm` > `0.1692` → IC=+0.305 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1692 (IC base=-0.059)

- **PATRÓN** `volumen_spike_ratio` < `1.5797` → IC=+0.304 (n=448)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5797 (IC base=-0.059)

- **PATRÓN** `volumen_spike_ratio` > `2.5272` → IC=+0.324 (n=339)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5272 (IC base=-0.059)

- **PATRÓN** `dist_vwap_pct` > `0.8106` → IC=+0.278 (n=362)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8106 (IC base=+0.003)

- **PATRÓN** `volumen_regimen` < `0.6413` → IC=+0.274 (n=729)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6413 (IC base=+0.003)

- **PATRÓN** `volumen_regimen` > `1.0661` → IC=+0.287 (n=992)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0661 (IC base=+0.003)

- **PATRÓN** `volumen_pendiente_norm` > `0.1064` → IC=+0.280 (n=779)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1064 (IC base=+0.003)

- **PATRÓN** `volumen_spike_ratio` < `2.1776` → IC=+0.265 (n=1814)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1776 (IC base=+0.003)

- **PATRÓN** `volumen_spike_ratio` > `1.4419` → IC=+0.270 (n=2061)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4419 (IC base=+0.003)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0106` → IC=+0.196 (n=7568)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` > 0.0106 (IC base=+0.088)

- **PATRÓN** `ibs_20min` > `0.97` → IC=+0.313 (n=7560)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.97 (IC base=+0.088)

- **PATRÓN** `dist_vwap_pct` > `0.9308` → IC=+0.302 (n=1606)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9308 (IC base=+0.088)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.478` → IC=+0.168 (n=10161)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 3.478 (IC base=+0.088)

- **PATRÓN** `volumen_regimen` > `0.6932` → IC=+0.277 (n=7450)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6932 (IC base=+0.088)

- **PATRÓN** `volumen_pendiente_norm` > `0.2943` → IC=+0.294 (n=1890)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2943 (IC base=+0.088)

- **PATRÓN** `volumen_spike_ratio` > `2.6561` → IC=+0.287 (n=4387)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6561 (IC base=+0.088)

- **PATRÓN** `ballena_activa_n` < `90.0` → IC=+0.309 (n=12791)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 90.0 (IC base=+0.088)

- **PATRÓN** `sigma_h` > `0.0102` → IC=+0.157 (n=7291)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0102 (IC base=+0.082)

- **PATRÓN** `ibs_20min` < `0.64` → IC=+0.155 (n=21871)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.64 (IC base=+0.082)

- **PATRÓN** `dist_vwap_pct` < `0.2564` → IC=+0.280 (n=7455)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2564 (IC base=+0.082)

- **PATRÓN** `volumen_regimen` < `0.6997` → IC=+0.282 (n=3180)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6997 (IC base=+0.082)

- **PATRÓN** `volumen_regimen` > `1.1889` → IC=+0.280 (n=2410)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1889 (IC base=+0.082)

- **PATRÓN** `volumen_pendiente_norm` > `0.2946` → IC=+0.328 (n=1608)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2946 (IC base=+0.082)

- **PATRÓN** `volumen_spike_ratio` < `1.5758` → IC=+0.304 (n=4687)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5758 (IC base=+0.082)

- **PATRÓN** `volumen_spike_ratio` > `2.2821` → IC=+0.303 (n=4827)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2821 (IC base=+0.082)

- **PATRÓN** `ballena_activa_n` < `72.0` → IC=+0.311 (n=10608)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 72.0 (IC base=+0.082)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.8021` → IC=-0.130 (n=4032)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8021
  - _Potencial_: sin este filtro IC_bueno=+0.300 (n=2080)

- **FILTRO** `ibs_20min` > `0.7179` → IC=-0.234 (n=1342)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7179
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=4029)

- **FILTRO** `sigma_ewma_delta_pct` > `4.087` → IC=-0.234 (n=1161)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.087
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=4210)

- **PATRÓN** `ibs_20min` > `0.8021` → IC=+0.300 (n=2080)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8021 (IC base=+0.016)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.966` → IC=+0.190 (n=2044)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 2.966 (IC base=+0.016)

- **PATRÓN** `volumen_pendiente_norm` > `0.2295` → IC=+0.328 (n=394)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2295 (IC base=+0.016)

- **PATRÓN** `volumen_spike_ratio` < `1.449` → IC=+0.280 (n=651)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.449 (IC base=+0.016)

- **PATRÓN** `volumen_spike_ratio` > `2.2427` → IC=+0.304 (n=886)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2427 (IC base=+0.016)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.303 (n=1944)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 27.0 (IC base=+0.016)

- **PATRÓN** `ibs_20min` < `0.1743` → IC=+0.168 (n=1343)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` < 0.1743 (IC base=-0.023)

- **PATRÓN** `volumen_pendiente_norm` < `0.1528` → IC=+0.404 (n=1025)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1528 (IC base=-0.023)

- **PATRÓN** `volumen_spike_ratio` < `1.4225` → IC=+0.425 (n=331)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4225 (IC base=-0.023)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.401 (n=1027)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 23.0 (IC base=-0.023)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.1691` → IC=+0.224 (n=980)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1691 (IC base=+0.012)

- **PATRÓN** `volumen_regimen` < `1.195` → IC=+0.211 (n=2221)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.195 (IC base=+0.012)

- **PATRÓN** `volumen_regimen` > `0.6955` → IC=+0.217 (n=1985)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6955 (IC base=+0.012)

- **PATRÓN** `volumen_pendiente_norm` > `0.2781` → IC=+0.247 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2781 (IC base=+0.012)

- **PATRÓN** `volumen_spike_ratio` < `1.4174` → IC=+0.229 (n=732)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4174 (IC base=+0.012)

- **PATRÓN** `ballena_activa_n` < `262.0` → IC=+0.247 (n=1464)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 262.0 (IC base=+0.012)

- **PATRÓN** `dist_vwap_pct` < `0.1327` → IC=+0.259 (n=1595)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1327 (IC base=-0.004)

- **PATRÓN** `volumen_regimen` > `0.619` → IC=+0.254 (n=1547)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.619 (IC base=-0.004)

- **PATRÓN** `volumen_pendiente_norm` > `0.2701` → IC=+0.314 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2701 (IC base=-0.004)

- **PATRÓN** `volumen_spike_ratio` < `1.5263` → IC=+0.259 (n=658)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5263 (IC base=-0.004)

- **PATRÓN** `volumen_spike_ratio` > `2.1487` → IC=+0.264 (n=677)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1487 (IC base=-0.004)

- **PATRÓN** `ballena_activa_n` < `210.0` → IC=+0.274 (n=666)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 210.0 (IC base=-0.004)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.321 (n=2126)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0094 (IC base=+0.284)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.293 (n=3345)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.284)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.324 (n=1735)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.284)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.586` → IC=+0.305 (n=2133)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.586 (IC base=+0.284)

- **PATRÓN** `volumen_pendiente_norm` < `0.0981` → IC=+0.296 (n=2794)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0981 (IC base=+0.284)

- **PATRÓN** `volumen_spike_ratio` > `1.6104` → IC=+0.290 (n=3093)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6104 (IC base=+0.284)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.292 (n=3814)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.284)

- **PATRÓN** `libro_liquidez` > `2022.0197` → IC=+0.293 (n=1061)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2022.0197 (IC base=+0.284)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.309 (n=1964)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.284)

- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.333 (n=1921)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0089 (IC base=+0.307)

- **PATRÓN** `drift_60min` |x|≤ `0.1771` → IC=+0.327 (n=1269)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1771 (IC base=+0.307)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.329 (n=1108)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.307)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.309 (n=1305)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.307)

- **PATRÓN** `ibs_20min` > `0.1429` → IC=+0.319 (n=1926)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1429 (IC base=+0.307)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.151` → IC=+0.310 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.151 (IC base=+0.307)

- **PATRÓN** `volumen_pendiente_norm` < `0.2005` → IC=+0.308 (n=2830)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2005 (IC base=+0.307)

- **PATRÓN** `volumen_pendiente_norm` > `0.3455` → IC=+0.314 (n=466)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3455 (IC base=+0.307)

- **PATRÓN** `volumen_spike_ratio` < `1.597` → IC=+0.306 (n=927)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.597 (IC base=+0.307)

- **PATRÓN** `volumen_spike_ratio` > `2.7414` → IC=+0.323 (n=1260)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7414 (IC base=+0.307)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.309 (n=1463)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.307)

- **PATRÓN** `libro_liquidez` > `1903.9584` → IC=+0.314 (n=1307)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1903.9584 (IC base=+0.307)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.314 (n=2433)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 23.0 (IC base=+0.307)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7237` → IC=-0.181 (n=1427)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7237
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=4283)

- **PATRÓN** `ibs_20min` > `0.8473` → IC=+0.157 (n=1402)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` > 0.8473 (IC base=+0.021)

- **PATRÓN** `dist_vwap_pct` > `0.1424` → IC=+0.237 (n=1043)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1424 (IC base=+0.021)

- **PATRÓN** `dist_vwap_pct` < `0.3559` → IC=+0.236 (n=1991)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3559 (IC base=+0.021)

- **PATRÓN** `volumen_regimen` < `1.1654` → IC=+0.236 (n=2024)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1654 (IC base=+0.021)

- **PATRÓN** `volumen_regimen` > `0.6738` → IC=+0.232 (n=1809)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6738 (IC base=+0.021)

- **PATRÓN** `volumen_pendiente_norm` < `0.1626` → IC=+0.236 (n=2126)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1626 (IC base=+0.021)

- **PATRÓN** `volumen_pendiente_norm` > `0.1031` → IC=+0.243 (n=660)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1031 (IC base=+0.021)

- **PATRÓN** `volumen_spike_ratio` < `2.4521` → IC=+0.240 (n=1963)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4521 (IC base=+0.021)

- **PATRÓN** `ballena_activa_n` < `115.0` → IC=+0.255 (n=2011)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 115.0 (IC base=+0.021)

- **PATRÓN** `ibs_20min` < `0.0918` → IC=+0.157 (n=1429)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.0918 (IC base=+0.006)

- **PATRÓN** `dist_vwap_pct` < `0.3464` → IC=+0.257 (n=1626)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3464 (IC base=+0.006)

- **PATRÓN** `volumen_regimen` < `1.1913` → IC=+0.260 (n=1459)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1913 (IC base=+0.006)

- **PATRÓN** `volumen_pendiente_norm` > `0.2815` → IC=+0.315 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2815 (IC base=+0.006)

- **PATRÓN** `volumen_spike_ratio` < `1.7888` → IC=+0.289 (n=934)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7888 (IC base=+0.006)

- **PATRÓN** `volumen_spike_ratio` > `2.4311` → IC=+0.278 (n=467)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4311 (IC base=+0.006)

- **PATRÓN** `ballena_activa_n` < `98.0` → IC=+0.287 (n=1256)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 98.0 (IC base=+0.006)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7407` → IC=-0.248 (n=2343)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7407
  - _Potencial_: sin este filtro IC_bueno=+0.311 (n=2347)

- **FILTRO** `ibs_20min` > `0.6207` → IC=-0.231 (n=1107)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6207
  - _Potencial_: sin este filtro IC_bueno=+0.150 (n=3340)

- **FILTRO** `sigma_ewma_delta_pct` > `8.241` → IC=-0.253 (n=507)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.241
  - _Potencial_: sin este filtro IC_bueno=+0.095 (n=3940)

- **PATRÓN** `ibs_20min` > `0.7407` → IC=+0.311 (n=2347)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7407 (IC base=+0.032)

- **PATRÓN** `dist_vwap_pct` > `1.0387` → IC=+0.358 (n=342)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0387 (IC base=+0.032)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.43` → IC=+0.154 (n=1905)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 2.43 (IC base=+0.032)

- **PATRÓN** `volumen_regimen` < `0.8453` → IC=+0.341 (n=1138)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8453 (IC base=+0.032)

- **PATRÓN** `volumen_regimen` > `0.6974` → IC=+0.334 (n=1524)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6974 (IC base=+0.032)

- **PATRÓN** `volumen_pendiente_norm` < `0.1558` → IC=+0.334 (n=1761)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1558 (IC base=+0.032)

- **PATRÓN** `volumen_pendiente_norm` > `0.274` → IC=+0.360 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.274 (IC base=+0.032)

- **PATRÓN** `volumen_spike_ratio` < `1.4223` → IC=+0.358 (n=553)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4223 (IC base=+0.032)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.349 (n=1141)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=+0.032)

- **PATRÓN** `ibs_20min` < `0.6207` → IC=+0.150 (n=3340)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.6207 (IC base=+0.055)

- **PATRÓN** `dist_vwap_pct` < `0.3052` → IC=+0.261 (n=1710)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3052 (IC base=+0.055)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.71` → IC=+0.122 (n=3490)

  - _Acción_: Kelly boost +0.61€ cuando `sigma_ewma_delta_pct` < 4.71 (IC base=+0.055)

- **PATRÓN** `volumen_regimen` < `0.6951` → IC=+0.281 (n=733)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6951 (IC base=+0.055)

- **PATRÓN** `volumen_pendiente_norm` > `0.0706` → IC=+0.288 (n=668)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0706 (IC base=+0.055)

- **PATRÓN** `volumen_spike_ratio` < `1.8024` → IC=+0.278 (n=1075)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8024 (IC base=+0.055)

- **PATRÓN** `ballena_activa_n` < `39.0` → IC=+0.279 (n=1457)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 39.0 (IC base=+0.055)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0159` → IC=+0.359 (n=1593)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0159 (IC base=+0.317)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.319 (n=2412)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.317)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.318 (n=1142)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.317)

- **PATRÓN** `ibs_20min` > `0.661` → IC=+0.345 (n=2391)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.661 (IC base=+0.317)

- **PATRÓN** `dist_vwap_pct` > `0.2123` → IC=+0.339 (n=1296)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2123 (IC base=+0.317)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.806` → IC=+0.334 (n=1157)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.806 (IC base=+0.317)

- **PATRÓN** `volumen_regimen` > `0.6307` → IC=+0.327 (n=2390)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6307 (IC base=+0.317)

- **PATRÓN** `volumen_pendiente_norm` > `0.28` → IC=+0.350 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.28 (IC base=+0.317)

- **PATRÓN** `volumen_spike_ratio` > `1.4315` → IC=+0.328 (n=2303)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4315 (IC base=+0.317)

- **PATRÓN** `libro_liquidez` > `2984.8754` → IC=+0.326 (n=797)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2984.8754 (IC base=+0.317)

- **PATRÓN** `ballena_activa_n` < `33.0` → IC=+0.345 (n=1862)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 33.0 (IC base=+0.317)

- **PATRÓN** `sigma_h` > `0.0152` → IC=+0.349 (n=1704)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0152 (IC base=+0.317)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.324 (n=1297)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.317)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.317 (n=1239)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.317)

- **PATRÓN** `ibs_20min` < `0.3804` → IC=+0.335 (n=2556)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3804 (IC base=+0.317)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.621` → IC=+0.328 (n=945)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.621 (IC base=+0.317)

- **PATRÓN** `volumen_regimen` < `0.7189` → IC=+0.323 (n=1125)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7189 (IC base=+0.317)

- **PATRÓN** `volumen_regimen` > `1.2104` → IC=+0.344 (n=853)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2104 (IC base=+0.317)

- **PATRÓN** `volumen_pendiente_norm` > `0.23` → IC=+0.364 (n=482)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.23 (IC base=+0.317)

- **PATRÓN** `volumen_spike_ratio` < `1.4127` → IC=+0.325 (n=793)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4127 (IC base=+0.317)

- **PATRÓN** `volumen_spike_ratio` > `2.1396` → IC=+0.317 (n=1077)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1396 (IC base=+0.317)

- **PATRÓN** `libro_liquidez` > `2963.501` → IC=+0.317 (n=852)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2963.501 (IC base=+0.317)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.224 (n=5631)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0125 (IC base=+0.173)

- **PATRÓN** `drift_60min` |x|≤ `0.1221` → IC=+0.191 (n=7433)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.1221 (IC base=+0.173)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.183 (n=17499)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.173)

- **PATRÓN** `ibs_20min` > `0.5378` → IC=+0.231 (n=16890)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5378 (IC base=+0.173)

- **PATRÓN** `dist_vwap_pct` > `0.1615` → IC=+0.205 (n=6452)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1615 (IC base=+0.173)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.784` → IC=+0.258 (n=3289)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.784 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` < `1.1817` → IC=+0.153 (n=11242)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.1817 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` > `0.6264` → IC=+0.152 (n=11242)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.6264 (IC base=+0.173)

- **PATRÓN** `volumen_pendiente_norm` > `0.2943` → IC=+0.204 (n=2459)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2943 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` > `2.6095` → IC=+0.188 (n=5476)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.6095 (IC base=+0.173)

- **PATRÓN** `ballena_activa_n` < `87.0` → IC=+0.192 (n=15803)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 87.0 (IC base=+0.173)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.192 (n=7311)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0058 (IC base=+0.183)

- **PATRÓN** `drift_60min` |x|≤ `0.0803` → IC=+0.222 (n=5536)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0803 (IC base=+0.183)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.211 (n=6266)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.183)

- **PATRÓN** `ibs_20min` < `0.5262` → IC=+0.239 (n=16608)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5262 (IC base=+0.183)

- **PATRÓN** `dist_vwap_pct` < `0.1818` → IC=+0.177 (n=12076)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.1818 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.536` → IC=+0.193 (n=2649)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 9.536 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.512` → IC=+0.190 (n=14777)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` < 2.512 (IC base=+0.183)

- **PATRÓN** `volumen_regimen` < `1.1821` → IC=+0.164 (n=11827)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.1821 (IC base=+0.183)

- **PATRÓN** `volumen_pendiente_norm` > `0.294` → IC=+0.219 (n=2485)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.294 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` < `1.5598` → IC=+0.182 (n=6953)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 1.5598 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` > `2.6324` → IC=+0.192 (n=5266)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.6324 (IC base=+0.183)

- **PATRÓN** `ballena_activa_n` < `91.0` → IC=+0.198 (n=15584)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 91.0 (IC base=+0.183)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `drift_60min` |x|≤ `0.1044` → IC=+0.257 (n=1225)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1044 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.234 (n=2892)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.227)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.228 (n=1895)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.227)

- **PATRÓN** `ibs_20min` > `0.9427` → IC=+0.296 (n=1855)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9427 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.491` → IC=+0.329 (n=906)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.491 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` > `0.2814` → IC=+0.284 (n=425)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2814 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` < `1.8357` → IC=+0.225 (n=1769)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8357 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` > `1.4363` → IC=+0.229 (n=2653)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4363 (IC base=+0.227)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.238 (n=3084)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.227)

- **PATRÓN** `sigma_h` < `0.0098` → IC=+0.258 (n=2261)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0098 (IC base=+0.257)

- **PATRÓN** `sigma_h` > `0.0088` → IC=+0.257 (n=1024)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0088 (IC base=+0.257)

- **PATRÓN** `drift_60min` |x|≤ `0.0967` → IC=+0.314 (n=993)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0967 (IC base=+0.257)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.261 (n=2327)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.257)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.260 (n=2055)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.257)

- **PATRÓN** `ibs_20min` < `0.0526` → IC=+0.301 (n=994)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0526 (IC base=+0.257)

- **PATRÓN** `volumen_pendiente_norm` < `0.0995` → IC=+0.259 (n=1980)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0995 (IC base=+0.257)

- **PATRÓN** `volumen_pendiente_norm` > `0.3015` → IC=+0.271 (n=339)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3015 (IC base=+0.257)

- **PATRÓN** `volumen_spike_ratio` < `1.4466` → IC=+0.277 (n=720)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4466 (IC base=+0.257)

- **PATRÓN** `volumen_spike_ratio` > `2.6927` → IC=+0.256 (n=720)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6927 (IC base=+0.257)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.259 (n=2602)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.257)

- **PATRÓN** `libro_liquidez` > `1774.0108` → IC=+0.264 (n=1504)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1774.0108 (IC base=+0.257)

- **PATRÓN** `ballena_activa_n` < `7.0` → IC=+0.258 (n=841)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 7.0 (IC base=+0.257)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.200 (n=859)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.129)

- **PATRÓN** `drift_60min` |x|≤ `0.0648` → IC=+0.176 (n=860)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.0648 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.146 (n=2693)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.129)

- **PATRÓN** `ibs_20min` > `0.2604` → IC=+0.208 (n=2577)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2604 (IC base=+0.129)

- **PATRÓN** `dist_vwap_pct` > `0.1838` → IC=+0.213 (n=1293)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1838 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.65` → IC=+0.207 (n=472)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.65 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` < `0.63` → IC=+0.134 (n=859)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 0.63 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` > `1.0589` → IC=+0.137 (n=1168)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` > 1.0589 (IC base=+0.129)

- **PATRÓN** `volumen_pendiente_norm` > `0.2807` → IC=+0.171 (n=402)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.2807 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` < `1.5049` → IC=+0.135 (n=1114)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.5049 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` > `2.4674` → IC=+0.150 (n=845)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 2.4674 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `215.0` → IC=+0.144 (n=1112)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 215.0 (IC base=+0.129)

- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.172 (n=2733)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0064 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.3037` → IC=+0.166 (n=2731)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.3037 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.185 (n=1029)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 17.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` < `0.6102` → IC=+0.209 (n=2731)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6102 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` < `0.1462` → IC=+0.174 (n=2863)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` < 0.1462 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.877` → IC=+0.180 (n=513)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 10.877 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.03` → IC=+0.151 (n=2381)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` < 4.03 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `1.199` → IC=+0.162 (n=2731)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.199 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` < `0.0938` → IC=+0.151 (n=2362)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` < 0.0938 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `2.4667` → IC=+0.153 (n=2605)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.4667 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `210.0` → IC=+0.191 (n=1120)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 210.0 (IC base=+0.148)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0115` → IC=+0.231 (n=1301)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0115 (IC base=+0.211)

- **PATRÓN** `drift_60min` |x|≤ `0.2482` → IC=+0.233 (n=1911)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2482 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.219 (n=2978)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.291 (n=1523)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.09` → IC=+0.306 (n=679)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.09 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` < `0.0991` → IC=+0.211 (n=2489)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0991 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.3532` → IC=+0.240 (n=409)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3532 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `2.7157` → IC=+0.225 (n=1268)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7157 (IC base=+0.211)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.215 (n=3457)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `2010.7034` → IC=+0.223 (n=955)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2010.7034 (IC base=+0.211)

- **PATRÓN** `sigma_h` < `0.0107` → IC=+0.248 (n=2222)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0107 (IC base=+0.239)

- **PATRÓN** `drift_60min` |x|≤ `0.4112` → IC=+0.262 (n=2221)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4112 (IC base=+0.239)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.281 (n=971)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.239)

- **PATRÓN** `ibs_20min` < `0.0385` → IC=+0.289 (n=1112)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0385 (IC base=+0.239)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.915` → IC=+0.279 (n=333)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.915 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` > `0.3581` → IC=+0.288 (n=422)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3581 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` < `1.7742` → IC=+0.241 (n=1072)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7742 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` > `2.1845` → IC=+0.251 (n=1624)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1845 (IC base=+0.239)

- **PATRÓN** `libro_liquidez` > `1888.2915` → IC=+0.251 (n=1145)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1888.2915 (IC base=+0.239)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.245 (n=1659)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.239)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.204 (n=931)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.129)

- **PATRÓN** `drift_60min` |x|≤ `0.0779` → IC=+0.180 (n=929)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.0779 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.139 (n=2872)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 5.0 (IC base=+0.129)

- **PATRÓN** `ibs_20min` > `0.25` → IC=+0.191 (n=2780)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.25 (IC base=+0.129)

- **PATRÓN** `dist_vwap_pct` > `0.1385` → IC=+0.185 (n=1611)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1385 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.272` → IC=+0.198 (n=478)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 11.272 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` < `0.8446` → IC=+0.136 (n=1854)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.8446 (IC base=+0.129)

- **PATRÓN** `volumen_pendiente_norm` > `0.2885` → IC=+0.171 (n=418)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.2885 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` > `2.5113` → IC=+0.145 (n=908)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 2.5113 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `6802.938` → IC=+0.196 (n=1261)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 6802.938 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `127.0` → IC=+0.130 (n=2726)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 127.0 (IC base=+0.129)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.164 (n=2610)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0067 (IC base=+0.129)

- **PATRÓN** `drift_60min` |x|≤ `0.3953` → IC=+0.146 (n=2965)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.3953 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.164 (n=1419)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 15.0 (IC base=+0.129)

- **PATRÓN** `ibs_20min` < `0.6789` → IC=+0.185 (n=2965)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.6789 (IC base=+0.129)

- **PATRÓN** `dist_vwap_pct` < `0.1593` → IC=+0.155 (n=3002)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1593 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.254` → IC=+0.141 (n=708)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 9.254 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` < `0.8521` → IC=+0.150 (n=1978)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.8521 (IC base=+0.129)

- **PATRÓN** `volumen_pendiente_norm` > `0.2942` → IC=+0.176 (n=440)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.2942 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` < `1.8007` → IC=+0.131 (n=1874)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 1.8007 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` > `1.5196` → IC=+0.131 (n=2511)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 1.5196 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `6266.4711` → IC=+0.191 (n=1344)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 6266.4711 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.151 (n=959)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 49.0 (IC base=+0.129)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.163 (n=1408)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` > 0.0113 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.157 (n=1468)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 15.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` > `0.4706` → IC=+0.205 (n=3102)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4706 (IC base=+0.119)

- **PATRÓN** `dist_vwap_pct` > `0.1947` → IC=+0.186 (n=1672)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1947 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.972` → IC=+0.287 (n=651)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.972 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` < `1.1709` → IC=+0.130 (n=3094)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.1709 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` < `0.1632` → IC=+0.124 (n=3152)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.1632 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` < `1.7825` → IC=+0.126 (n=2001)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 1.7825 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `2655.3249` → IC=+0.193 (n=1403)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 2655.3249 (IC base=+0.119)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.139 (n=1348)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 20.0 (IC base=+0.119)

- **PATRÓN** `sigma_h` < `0.0118` → IC=+0.141 (n=3248)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.0118 (IC base=+0.118)

- **PATRÓN** `drift_60min` |x|≤ `0.1119` → IC=+0.163 (n=1082)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.1119 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.134 (n=3317)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 5.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` < `0.65` → IC=+0.219 (n=3246)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.65 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` < `0.2138` → IC=+0.143 (n=3196)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.2138 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.243` → IC=+0.139 (n=2873)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 2.243 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` < `1.1712` → IC=+0.127 (n=3246)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` < 1.1712 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` > `0.2739` → IC=+0.143 (n=446)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` > 0.2739 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` < `1.4337` → IC=+0.136 (n=1023)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.4337 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `2897.4067` → IC=+0.195 (n=1082)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 2897.4067 (IC base=+0.118)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.125 (n=2053)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 27.0 (IC base=+0.118)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0132` → IC=+0.249 (n=2496)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0132 (IC base=+0.226)

- **PATRÓN** `drift_60min` |x|≤ `0.1655` → IC=+0.240 (n=1229)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1655 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.231 (n=2899)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.226)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.230 (n=2523)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.226)

- **PATRÓN** `ibs_20min` > `0.6667` → IC=+0.258 (n=2795)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6667 (IC base=+0.226)

- **PATRÓN** `dist_vwap_pct` > `0.1809` → IC=+0.234 (n=1723)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1809 (IC base=+0.226)

- **PATRÓN** `dist_vwap_pct` < `0.797` → IC=+0.226 (n=2881)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.797 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.594` → IC=+0.257 (n=1264)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.594 (IC base=+0.226)

- **PATRÓN** `volumen_regimen` > `0.6237` → IC=+0.236 (n=2794)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6237 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` > `0.2348` → IC=+0.265 (n=522)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2348 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` < `2.4722` → IC=+0.229 (n=2725)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4722 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` > `1.8145` → IC=+0.233 (n=1816)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8145 (IC base=+0.226)

- **PATRÓN** `libro_liquidez` > `2576.372` → IC=+0.232 (n=1862)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2576.372 (IC base=+0.226)

- **PATRÓN** `sigma_h` > `0.0228` → IC=+0.248 (n=1309)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0228 (IC base=+0.240)

- **PATRÓN** `drift_60min` |x|≤ `0.576` → IC=+0.248 (n=2888)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.576 (IC base=+0.240)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.252 (n=1419)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.240)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.245 (n=1294)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.240)

- **PATRÓN** `ibs_20min` < `0.44` → IC=+0.264 (n=2896)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.44 (IC base=+0.240)

- **PATRÓN** `dist_vwap_pct` > `1.1311` → IC=+0.260 (n=273)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1311 (IC base=+0.240)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.021` → IC=+0.266 (n=404)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.021 (IC base=+0.240)

- **PATRÓN** `volumen_regimen` < `0.8653` → IC=+0.242 (n=1927)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8653 (IC base=+0.240)

- **PATRÓN** `volumen_regimen` > `0.6409` → IC=+0.243 (n=2889)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6409 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` > `0.2812` → IC=+0.291 (n=400)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2812 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` < `1.8377` → IC=+0.238 (n=1815)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8377 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` > `1.5489` → IC=+0.241 (n=2431)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5489 (IC base=+0.240)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.208 (n=1455)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.161)

- **PATRÓN** `drift_60min` |x|≤ `0.1329` → IC=+0.174 (n=1920)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.1329 (IC base=+0.161)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.173 (n=4548)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 5.0 (IC base=+0.161)

- **PATRÓN** `ibs_20min` > `0.3077` → IC=+0.197 (n=4362)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.3077 (IC base=+0.161)

- **PATRÓN** `dist_vwap_pct` > `0.2202` → IC=+0.183 (n=1676)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.2202 (IC base=+0.161)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.601` → IC=+0.209 (n=712)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.601 (IC base=+0.161)

- **PATRÓN** `volumen_regimen` < `0.8606` → IC=+0.172 (n=2651)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` < 0.8606 (IC base=+0.161)

- **PATRÓN** `volumen_regimen` > `1.1929` → IC=+0.168 (n=1325)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` > 1.1929 (IC base=+0.161)

- **PATRÓN** `volumen_pendiente_norm` > `0.1569` → IC=+0.174 (n=1150)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.1569 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` < `1.5264` → IC=+0.166 (n=1872)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 1.5264 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` > `2.4729` → IC=+0.163 (n=1417)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 2.4729 (IC base=+0.161)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.161 (n=4877)

  - _Acción_: Kelly boost +0.81€ cuando `libro_spread` < 0.02 (IC base=+0.161)

- **PATRÓN** `libro_liquidez` > `7842.7274` → IC=+0.186 (n=1977)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 7842.7274 (IC base=+0.161)

- **PATRÓN** `ibs_20min` < `0.3846` → IC=+0.172 (n=3151)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.3846 (IC base=+0.092)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.134 (n=2020)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 24.0 (IC base=+0.092)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.197 (n=1138)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0061 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.3291` → IC=+0.197 (n=1138)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.3291 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.215 (n=1026)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` > `0.6089` → IC=+0.238 (n=758)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6089 (IC base=+0.182)

- **PATRÓN** `dist_vwap_pct` > `0.3087` → IC=+0.218 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3087 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.928` → IC=+0.211 (n=500)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.928 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` < `0.6313` → IC=+0.202 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6313 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.0911` → IC=+0.196 (n=393)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.0911 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` < `2.1671` → IC=+0.196 (n=982)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 2.1671 (IC base=+0.182)

- **PATRÓN** `libro_liquidez` > `15755.8578` → IC=+0.191 (n=516)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 15755.8578 (IC base=+0.182)

- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.160 (n=472)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0031 (IC base=+0.083)

- **PATRÓN** `ibs_20min` < `0.2031` → IC=+0.202 (n=622)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2031 (IC base=+0.083)

- **PATRÓN** `ballena_activa_n` < `164.0` → IC=+0.176 (n=613)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 164.0 (IC base=+0.083)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.236 (n=593)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.157)

- **PATRÓN** `drift_60min` |x|≤ `0.2091` → IC=+0.158 (n=899)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.2091 (IC base=+0.157)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.177 (n=1393)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 5.0 (IC base=+0.157)

- **PATRÓN** `ibs_20min` > `0.7967` → IC=+0.266 (n=610)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7967 (IC base=+0.157)

- **PATRÓN** `dist_vwap_pct` > `0.3567` → IC=+0.186 (n=422)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.3567 (IC base=+0.157)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.884` → IC=+0.208 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.884 (IC base=+0.157)

- **PATRÓN** `volumen_regimen` < `0.8331` → IC=+0.171 (n=898)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` < 0.8331 (IC base=+0.157)

- **PATRÓN** `volumen_pendiente_norm` > `0.2193` → IC=+0.204 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2193 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` > `2.4744` → IC=+0.182 (n=442)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 2.4744 (IC base=+0.157)

- **PATRÓN** `libro_liquidez` > `8108.4175` → IC=+0.175 (n=610)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 8108.4175 (IC base=+0.157)

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.123 (n=873)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0052 (IC base=+0.090)

- **PATRÓN** `ibs_20min` < `0.0866` → IC=+0.208 (n=437)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0866 (IC base=+0.090)

- **PATRÓN** `libro_liquidez` > `8030.3267` → IC=+0.149 (n=594)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 8030.3267 (IC base=+0.090)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.126 (n=567)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 43.0 (IC base=+0.090)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` < `0.009` → IC=+0.151 (n=748)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.009 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.174 (n=784)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 11.0 (IC base=+0.131)

- **PATRÓN** `ibs_20min` > `0.5517` → IC=+0.198 (n=1001)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.5517 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` > `0.9192` → IC=+0.172 (n=187)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.9192 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.848` → IC=+0.232 (n=446)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.848 (IC base=+0.131)

- **PATRÓN** `volumen_regimen` < `1.0462` → IC=+0.141 (n=987)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 1.0462 (IC base=+0.131)

- **PATRÓN** `volumen_regimen` > `0.704` → IC=+0.140 (n=1001)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` > 0.704 (IC base=+0.131)

- **PATRÓN** `volumen_pendiente_norm` > `0.2246` → IC=+0.158 (n=200)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` > 0.2246 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` < `1.4128` → IC=+0.157 (n=362)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.4128 (IC base=+0.131)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.133 (n=1171)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.02 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `2751.7394` → IC=+0.169 (n=508)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 2751.7394 (IC base=+0.131)

- **PATRÓN** `ibs_20min` < `0.5616` → IC=+0.149 (n=1089)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` < 0.5616 (IC base=+0.069)

- **PATRÓN** `libro_liquidez` > `2635.7469` → IC=+0.163 (n=561)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 2635.7469 (IC base=+0.069)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0178` → IC=+0.237 (n=249)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0178 (IC base=+0.194)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.236 (n=180)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.194)

- **PATRÓN** `ibs_20min` > `0.5522` → IC=+0.214 (n=334)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5522 (IC base=+0.194)

- **PATRÓN** `dist_vwap_pct` > `0.2223` → IC=+0.210 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2223 (IC base=+0.194)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.845` → IC=+0.215 (n=367)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.845 (IC base=+0.194)

- **PATRÓN** `volumen_regimen` > `1.1874` → IC=+0.272 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1874 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` < `0.1024` → IC=+0.204 (n=333)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1024 (IC base=+0.194)

- **PATRÓN** `volumen_spike_ratio` < `1.8262` → IC=+0.212 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8262 (IC base=+0.194)

- **PATRÓN** `volumen_spike_ratio` > `1.4242` → IC=+0.203 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4242 (IC base=+0.194)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.204 (n=407)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.194)

- **PATRÓN** `libro_liquidez` > `3017.6749` → IC=+0.201 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3017.6749 (IC base=+0.194)

- **PATRÓN** `sigma_h` > `0.0244` → IC=+0.177 (n=184)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` > 0.0244 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.6449` → IC=+0.146 (n=405)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.6449 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.196 (n=192)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 15.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` < `0.4984` → IC=+0.159 (n=356)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.4984 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` > `1.2224` → IC=+0.290 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2224 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.232` → IC=+0.179 (n=107)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 5.232 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.525` → IC=+0.144 (n=487)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 9.525 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` < `0.8805` → IC=+0.188 (n=270)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 0.8805 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` < `0.1134` → IC=+0.160 (n=372)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` < 0.1134 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` > `0.2295` → IC=+0.167 (n=76)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.2295 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` < `1.508` → IC=+0.197 (n=130)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 1.508 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` > `2.6713` → IC=+0.159 (n=130)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 2.6713 (IC base=+0.141)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.160 (n=386)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 20.0 (IC base=+0.141)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.230 (n=7376)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0125 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.190 (n=23040)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` > `0.4301` → IC=+0.228 (n=22119)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4301 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` > `0.8744` → IC=+0.210 (n=2639)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8744 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.947` → IC=+0.257 (n=5408)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.947 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `1.2155` → IC=+0.159 (n=14893)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2155 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.2412` → IC=+0.208 (n=3983)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2412 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `2.6236` → IC=+0.194 (n=7199)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.6236 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `103.0` → IC=+0.202 (n=20765)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 103.0 (IC base=+0.181)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.198 (n=8953)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.006 (IC base=+0.195)

- **PATRÓN** `sigma_h` > `0.0122` → IC=+0.205 (n=6770)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0122 (IC base=+0.195)

- **PATRÓN** `drift_60min` |x|≤ `0.4806` → IC=+0.198 (n=20309)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.4806 (IC base=+0.195)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.216 (n=7595)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.195)

- **PATRÓN** `ibs_20min` < `0.5918` → IC=+0.244 (n=20312)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5918 (IC base=+0.195)

- **PATRÓN** `dist_vwap_pct` < `0.1784` → IC=+0.177 (n=12840)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.1784 (IC base=+0.195)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.393` → IC=+0.195 (n=2746)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 9.393 (IC base=+0.195)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.529` → IC=+0.201 (n=18829)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.529 (IC base=+0.195)

- **PATRÓN** `volumen_regimen` < `0.6322` → IC=+0.177 (n=4553)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.6322 (IC base=+0.195)

- **PATRÓN** `volumen_pendiente_norm` > `0.2932` → IC=+0.253 (n=2787)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2932 (IC base=+0.195)

- **PATRÓN** `volumen_spike_ratio` > `2.6321` → IC=+0.206 (n=6478)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6321 (IC base=+0.195)

- **PATRÓN** `ballena_activa_n` < `91.0` → IC=+0.211 (n=19194)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 91.0 (IC base=+0.195)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.252 (n=1713)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.236)

- **PATRÓN** `ibs_20min` > `0.9736` → IC=+0.320 (n=1606)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9736 (IC base=+0.236)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.828` → IC=+0.344 (n=843)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.828 (IC base=+0.236)

- **PATRÓN** `volumen_pendiente_norm` > `0.2328` → IC=+0.293 (n=640)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2328 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` > `2.2913` → IC=+0.243 (n=1550)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2913 (IC base=+0.236)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.251 (n=3884)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.236)

- **PATRÓN** `libro_liquidez` > `2042.27` → IC=+0.238 (n=1180)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2042.27 (IC base=+0.236)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.254 (n=2148)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 14.0 (IC base=+0.236)

- **PATRÓN** `sigma_h` < `0.0102` → IC=+0.270 (n=3150)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0102 (IC base=+0.269)

- **PATRÓN** `drift_60min` |x|≤ `0.1212` → IC=+0.295 (n=1385)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1212 (IC base=+0.269)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.272 (n=2901)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.269)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.271 (n=2849)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.269)

- **PATRÓN** `ibs_20min` < `0.5478` → IC=+0.286 (n=3148)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5478 (IC base=+0.269)

- **PATRÓN** `volumen_pendiente_norm` < `0.0979` → IC=+0.273 (n=2864)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0979 (IC base=+0.269)

- **PATRÓN** `volumen_pendiente_norm` > `0.2907` → IC=+0.285 (n=436)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2907 (IC base=+0.269)

- **PATRÓN** `volumen_spike_ratio` < `1.562` → IC=+0.271 (n=1328)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.562 (IC base=+0.269)

- **PATRÓN** `volumen_spike_ratio` > `2.6528` → IC=+0.278 (n=1006)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6528 (IC base=+0.269)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.275 (n=2207)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.269)

- **PATRÓN** `libro_liquidez` > `1775.5` → IC=+0.277 (n=2098)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1775.5 (IC base=+0.269)

- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.283 (n=1109)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 8.0 (IC base=+0.269)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.181 (n=1213)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0031 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.0785` → IC=+0.149 (n=1209)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.0785 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.148 (n=3775)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 5.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` > `0.1959` → IC=+0.189 (n=3625)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.1959 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.3196` → IC=+0.199 (n=1189)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3196 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.333` → IC=+0.165 (n=758)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 9.333 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `0.6362` → IC=+0.156 (n=1209)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.6362 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` > `1.0696` → IC=+0.142 (n=1644)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 1.0696 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` < `0.0713` → IC=+0.138 (n=3248)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_pendiente_norm` < 0.0713 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.2706` → IC=+0.179 (n=512)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.2706 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `2.1654` → IC=+0.140 (n=3132)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 2.1654 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `1.5192` → IC=+0.142 (n=3180)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.5192 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `220.0` → IC=+0.162 (n=1169)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 220.0 (IC base=+0.136)

- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.162 (n=3122)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0064 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.3258` → IC=+0.146 (n=3119)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.3258 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.168 (n=1144)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 17.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` < `0.6801` → IC=+0.185 (n=3120)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.6801 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` < `0.1391` → IC=+0.151 (n=3030)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.1391 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.001` → IC=+0.137 (n=1493)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` > 3.001 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.002` → IC=+0.138 (n=2818)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 4.002 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `1.0486` → IC=+0.150 (n=2745)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 1.0486 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.2205` → IC=+0.193 (n=578)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2205 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `2.437` → IC=+0.141 (n=3010)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.437 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `1.7752` → IC=+0.142 (n=2006)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.7752 (IC base=+0.137)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.137 (n=4052)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `225.0` → IC=+0.156 (n=990)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 225.0 (IC base=+0.137)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.240 (n=2463)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0099 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.237 (n=3856)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.227)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.228 (n=3306)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.227)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.302 (n=1380)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.994` → IC=+0.324 (n=820)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.994 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` < `0.132` → IC=+0.229 (n=3487)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.132 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` > `0.3509` → IC=+0.230 (n=483)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3509 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` > `2.7432` → IC=+0.243 (n=1634)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7432 (IC base=+0.227)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.233 (n=4442)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.227)

- **PATRÓN** `libro_liquidez` > `1912.76` → IC=+0.239 (n=1672)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1912.76 (IC base=+0.227)

- **PATRÓN** `sigma_h` < `0.011` → IC=+0.250 (n=3095)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.011 (IC base=+0.245)

- **PATRÓN** `drift_60min` |x|≤ `0.1776` → IC=+0.267 (n=1548)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1776 (IC base=+0.245)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.265 (n=1340)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.245)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.245 (n=1605)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.245)

- **PATRÓN** `ibs_20min` < `0.0595` → IC=+0.303 (n=1173)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0595 (IC base=+0.245)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.065` → IC=+0.301 (n=375)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.065 (IC base=+0.245)

- **PATRÓN** `volumen_pendiente_norm` > `0.3501` → IC=+0.308 (n=530)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3501 (IC base=+0.245)

- **PATRÓN** `volumen_spike_ratio` > `2.1787` → IC=+0.256 (n=2258)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1787 (IC base=+0.245)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.250 (n=1795)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.245)

- **PATRÓN** `libro_liquidez` > `1996.9432` → IC=+0.255 (n=1172)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1996.9432 (IC base=+0.245)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.255 (n=2230)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.245)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.193 (n=1282)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0037 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.4307` → IC=+0.145 (n=3827)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.4307 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.150 (n=3965)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 5.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` > `0.8874` → IC=+0.272 (n=1276)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8874 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` > `0.1946` → IC=+0.169 (n=1740)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.1946 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.106` → IC=+0.163 (n=582)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 11.106 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `0.8609` → IC=+0.152 (n=2552)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.8609 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.2333` → IC=+0.189 (n=679)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.2333 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `1.5179` → IC=+0.151 (n=1647)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 1.5179 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `2.1755` → IC=+0.143 (n=1697)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 2.1755 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `5516.8147` → IC=+0.226 (n=1735)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5516.8147 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `87.0` → IC=+0.147 (n=2467)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 87.0 (IC base=+0.138)

- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.169 (n=2813)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0068 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.4356` → IC=+0.157 (n=3197)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.4356 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.174 (n=1177)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 17.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` < `0.5743` → IC=+0.212 (n=2812)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5743 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` < `0.1518` → IC=+0.161 (n=2996)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 0.1518 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.877` → IC=+0.155 (n=471)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 10.877 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.052` → IC=+0.150 (n=2790)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 3.052 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `0.6903` → IC=+0.162 (n=1406)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.6903 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.2942` → IC=+0.215 (n=405)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2942 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `2.2126` → IC=+0.149 (n=2714)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 2.2126 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` > `1.5324` → IC=+0.155 (n=2756)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.5324 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `6400.6695` → IC=+0.222 (n=1065)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6400.6695 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `90.0` → IC=+0.160 (n=2078)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 90.0 (IC base=+0.146)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0127` → IC=+0.150 (n=1295)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` > 0.0127 (IC base=+0.116)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.146 (n=2737)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 11.0 (IC base=+0.116)

- **PATRÓN** `ibs_20min` > `0.4286` → IC=+0.186 (n=3897)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.4286 (IC base=+0.116)

- **PATRÓN** `dist_vwap_pct` > `0.9949` → IC=+0.202 (n=638)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9949 (IC base=+0.116)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.242` → IC=+0.270 (n=984)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.242 (IC base=+0.116)

- **PATRÓN** `volumen_regimen` < `0.8759` → IC=+0.129 (n=2588)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 0.8759 (IC base=+0.116)

- **PATRÓN** `volumen_spike_ratio` < `1.8241` → IC=+0.122 (n=2529)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` < 1.8241 (IC base=+0.116)

- **PATRÓN** `libro_liquidez` > `2709.074` → IC=+0.237 (n=1294)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2709.074 (IC base=+0.116)

- **PATRÓN** `sigma_h` < `0.0109` → IC=+0.152 (n=3217)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0109 (IC base=+0.127)

- **PATRÓN** `drift_60min` |x|≤ `0.1373` → IC=+0.152 (n=1218)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.1373 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.163 (n=1713)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 15.0 (IC base=+0.127)

- **PATRÓN** `ibs_20min` < `0.6667` → IC=+0.216 (n=3660)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6667 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` < `0.2163` → IC=+0.142 (n=3327)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.2163 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.033` → IC=+0.148 (n=3534)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 3.033 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` < `1.1909` → IC=+0.134 (n=3654)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 1.1909 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` > `0.2279` → IC=+0.181 (n=641)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.2279 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` < `1.4357` → IC=+0.160 (n=1157)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 1.4357 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `2602.1348` → IC=+0.209 (n=1218)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2602.1348 (IC base=+0.127)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.140 (n=3065)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 42.0 (IC base=+0.127)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0139` → IC=+0.261 (n=3181)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0139 (IC base=+0.239)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.245 (n=3718)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.239)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.242 (n=3197)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.239)

- **PATRÓN** `ibs_20min` > `0.615` → IC=+0.272 (n=3181)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.615 (IC base=+0.239)

- **PATRÓN** `dist_vwap_pct` > `0.1942` → IC=+0.253 (n=1837)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1942 (IC base=+0.239)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.208` → IC=+0.289 (n=618)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.208 (IC base=+0.239)

- **PATRÓN** `volumen_regimen` < `1.2201` → IC=+0.241 (n=3560)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2201 (IC base=+0.239)

- **PATRÓN** `volumen_regimen` > `0.6435` → IC=+0.244 (n=3561)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6435 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` > `0.2388` → IC=+0.257 (n=614)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2388 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` > `2.4995` → IC=+0.261 (n=1161)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4995 (IC base=+0.239)

- **PATRÓN** `libro_liquidez` > `2975.6214` → IC=+0.246 (n=1187)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2975.6214 (IC base=+0.239)

- **PATRÓN** `sigma_h` > `0.0259` → IC=+0.270 (n=1227)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0259 (IC base=+0.243)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.248 (n=3466)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.243)

- **PATRÓN** `ibs_20min` < `0.5207` → IC=+0.273 (n=3679)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5207 (IC base=+0.243)

- **PATRÓN** `dist_vwap_pct` < `0.2197` → IC=+0.249 (n=3519)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2197 (IC base=+0.243)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.121` → IC=+0.277 (n=715)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.121 (IC base=+0.243)

- **PATRÓN** `volumen_regimen` < `0.7155` → IC=+0.245 (n=1621)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7155 (IC base=+0.243)

- **PATRÓN** `volumen_regimen` > `1.2193` → IC=+0.264 (n=1226)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2193 (IC base=+0.243)

- **PATRÓN** `volumen_pendiente_norm` > `0.2861` → IC=+0.305 (n=506)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2861 (IC base=+0.243)

- **PATRÓN** `volumen_spike_ratio` > `1.4346` → IC=+0.247 (n=3468)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4346 (IC base=+0.243)

- **PATRÓN** `libro_liquidez` > `2960.6154` → IC=+0.243 (n=1226)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2960.6154 (IC base=+0.243)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.200 (n=5877)

- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.244 (n=2107)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.220)

- **PATRÓN** `drift_60min` |x|≤ `0.513` → IC=+0.228 (n=6305)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.513 (IC base=+0.220)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.227 (n=5684)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.220)

- **PATRÓN** `ibs_20min` > `0.93` → IC=+0.256 (n=2104)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.93 (IC base=+0.220)

- **PATRÓN** `dist_vwap_pct` < `0.2442` → IC=+0.223 (n=4097)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2442 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.499` → IC=+0.224 (n=2084)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.499 (IC base=+0.220)

- **PATRÓN** `volumen_regimen` < `0.7085` → IC=+0.230 (n=2030)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7085 (IC base=+0.220)

- **PATRÓN** `volumen_pendiente_norm` < `0.1053` → IC=+0.221 (n=5886)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1053 (IC base=+0.220)

- **PATRÓN** `volumen_pendiente_norm` > `0.1652` → IC=+0.226 (n=1781)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1652 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` < `2.2533` → IC=+0.223 (n=5463)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.2533 (IC base=+0.220)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.225 (n=4758)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.220)

- **PATRÓN** `libro_liquidez` > `2872.2242` → IC=+0.224 (n=5633)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2872.2242 (IC base=+0.220)

- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.239 (n=1479)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.199)

- **PATRÓN** `drift_60min` |x|≤ `0.4932` → IC=+0.211 (n=4420)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4932 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.213 (n=1481)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.211 (n=1959)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.199)

- **PATRÓN** `ibs_20min` < `0.0867` → IC=+0.212 (n=1475)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0867 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` > `0.6569` → IC=+0.209 (n=747)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6569 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.758` → IC=+0.210 (n=3973)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.758 (IC base=+0.199)

- **PATRÓN** `volumen_regimen` < `1.0954` → IC=+0.205 (n=3711)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0954 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` < `0.0976` → IC=+0.200 (n=4074)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0976 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` > `0.0732` → IC=+0.201 (n=1971)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0732 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` < `1.5315` → IC=+0.204 (n=1918)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5315 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` > `2.183` → IC=+0.208 (n=1975)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.183 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.200 (n=5877)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

- **PATRÓN** `ballena_activa_n` < `32.0` → IC=+0.220 (n=1920)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 32.0 (IC base=+0.199)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.276 (n=816)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0057 (IC base=+0.270)

- **PATRÓN** `drift_60min` |x|≤ `0.0849` → IC=+0.298 (n=310)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0849 (IC base=+0.270)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.277 (n=984)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.270)

- **PATRÓN** `ibs_20min` < `0.8328` → IC=+0.279 (n=928)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.8328 (IC base=+0.270)

- **PATRÓN** `dist_vwap_pct` < `0.6688` → IC=+0.278 (n=1079)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6688 (IC base=+0.270)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.118` → IC=+0.300 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.118 (IC base=+0.270)

- **PATRÓN** `volumen_regimen` < `1.2246` → IC=+0.272 (n=928)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2246 (IC base=+0.270)

- **PATRÓN** `volumen_regimen` > `0.8769` → IC=+0.290 (n=618)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8769 (IC base=+0.270)

- **PATRÓN** `volumen_pendiente_norm` > `0.2881` → IC=+0.351 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2881 (IC base=+0.270)

- **PATRÓN** `volumen_spike_ratio` < `1.8118` → IC=+0.272 (n=616)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8118 (IC base=+0.270)

- **PATRÓN** `volumen_spike_ratio` > `2.189` → IC=+0.270 (n=419)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.189 (IC base=+0.270)

- **PATRÓN** `libro_liquidez` > `12915.1097` → IC=+0.279 (n=618)

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

- **PATRÓN** `sigma_ewma_delta_pct` < `4.105` → IC=+0.200 (n=1330)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.105 (IC base=+0.175)

- **PATRÓN** `volumen_regimen` < `0.644` → IC=+0.202 (n=508)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.644 (IC base=+0.175)

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
- **PATRÓN** `sigma_h` > `0.0123` → IC=+0.236 (n=343)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0123 (IC base=+0.208)

- **PATRÓN** `drift_60min` |x|≤ `0.6006` → IC=+0.212 (n=1028)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6006 (IC base=+0.208)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.230 (n=939)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.208)

- **PATRÓN** `ibs_20min` < `0.7122` → IC=+0.211 (n=686)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7122 (IC base=+0.208)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.251 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.208)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.281` → IC=+0.245 (n=379)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.281 (IC base=+0.208)

- **PATRÓN** `volumen_pendiente_norm` > `0.2044` → IC=+0.244 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2044 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` > `1.7946` → IC=+0.215 (n=915)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7946 (IC base=+0.208)

- **PATRÓN** `libro_liquidez` > `2777.94` → IC=+0.239 (n=343)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2777.94 (IC base=+0.208)

- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.220 (n=729)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 8.0 (IC base=+0.208)

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

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.0083` → IC=+0.217 (n=1771)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0083 (IC base=+0.204)

- **PATRÓN** `drift_60min` |x|≤ `0.458` → IC=+0.211 (n=1768)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.458 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.227 (n=617)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.204)

- **PATRÓN** `ibs_20min` < `0.476` → IC=+0.214 (n=1179)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.476 (IC base=+0.204)

- **PATRÓN** `ibs_20min` > `0.1477` → IC=+0.206 (n=1768)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1477 (IC base=+0.204)

- **PATRÓN** `dist_vwap_pct` < `0.2061` → IC=+0.215 (n=1587)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2061 (IC base=+0.204)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.363` → IC=+0.210 (n=1795)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 6.363 (IC base=+0.204)

- **PATRÓN** `volumen_regimen` < `0.8762` → IC=+0.210 (n=1179)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8762 (IC base=+0.204)

- **PATRÓN** `volumen_pendiente_norm` < `0.102` → IC=+0.207 (n=1629)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.102 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` < `2.1427` → IC=+0.211 (n=1523)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1427 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` > `1.4939` → IC=+0.205 (n=1547)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4939 (IC base=+0.204)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.204 (n=1774)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.204)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.241 (n=469)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.200)

- **PATRÓN** `drift_60min` |x|≤ `0.4873` → IC=+0.219 (n=1402)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4873 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.207 (n=527)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.200)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.217 (n=956)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.200)

- **PATRÓN** `ibs_20min` < `0.3937` → IC=+0.201 (n=935)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3937 (IC base=+0.200)

- **PATRÓN** `ibs_20min` > `0.612` → IC=+0.205 (n=636)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.612 (IC base=+0.200)

- **PATRÓN** `dist_vwap_pct` > `0.6225` → IC=+0.219 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6225 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.284` → IC=+0.203 (n=1279)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.284 (IC base=+0.200)

- **PATRÓN** `volumen_regimen` < `1.2492` → IC=+0.209 (n=1402)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2492 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` > `0.0731` → IC=+0.228 (n=572)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0731 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` < `1.412` → IC=+0.209 (n=459)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.412 (IC base=+0.200)

- **PATRÓN** `libro_liquidez` > `6540.7204` → IC=+0.205 (n=1253)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6540.7204 (IC base=+0.200)

- **PATRÓN** `ballena_activa_n` < `98.0` → IC=+0.200 (n=1397)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 98.0 (IC base=+0.200)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0082` → IC=+0.233 (n=447)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0082 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `10.0` → IC=+0.242 (n=684)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.204)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.280 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.204)

- **PATRÓN** `dist_vwap_pct` > `0.7569` → IC=+0.240 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7569 (IC base=+0.204)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.173` → IC=+0.230 (n=558)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.173 (IC base=+0.204)

- **PATRÓN** `volumen_regimen` < `0.6434` → IC=+0.248 (n=339)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6434 (IC base=+0.204)

- **PATRÓN** `volumen_pendiente_norm` < `0.1058` → IC=+0.213 (n=919)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1058 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` < `2.1404` → IC=+0.214 (n=870)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1404 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` > `1.468` → IC=+0.208 (n=990)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.468 (IC base=+0.204)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.213 (n=1194)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.204)

- **PATRÓN** `libro_liquidez` > `4315.5868` → IC=+0.248 (n=339)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4315.5868 (IC base=+0.204)

- **PATRÓN** `ballena_activa_n` < `39.0` → IC=+0.210 (n=882)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 39.0 (IC base=+0.204)

- **PATRÓN** `sigma_h` < `0.0118` → IC=+0.223 (n=626)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0118 (IC base=+0.222)

- **PATRÓN** `sigma_h` > `0.01` → IC=+0.238 (n=476)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.01 (IC base=+0.222)

- **PATRÓN** `drift_60min` |x|≤ `0.5949` → IC=+0.239 (n=712)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5949 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.224 (n=662)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.248 (n=494)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` < `0.6444` → IC=+0.252 (n=626)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6444 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.753` → IC=+0.238 (n=658)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.753 (IC base=+0.222)

- **PATRÓN** `volumen_regimen` < `0.7541` → IC=+0.230 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7541 (IC base=+0.222)

- **PATRÓN** `volumen_regimen` > `1.2667` → IC=+0.224 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2667 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` < `0.0838` → IC=+0.236 (n=600)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0838 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` > `2.1886` → IC=+0.260 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1886 (IC base=+0.222)

- **PATRÓN** `libro_liquidez` > `3782.8762` → IC=+0.235 (n=474)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3782.8762 (IC base=+0.222)

- **PATRÓN** `ballena_activa_n` < `26.0` → IC=+0.261 (n=484)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 26.0 (IC base=+0.222)

### GBM_LATE_60M
- **FILTRO** `ibs_20min` > `0.4861` → IC=-0.122 (n=664)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4861
  - _Potencial_: sin este filtro IC_bueno=+0.161 (n=1291)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.148 (n=737)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0038 (IC base=+0.053)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.184 (n=1417)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.75 (IC base=+0.053)

- **PATRÓN** `dist_vwap_pct` > `0.1427` → IC=+0.142 (n=1052)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.1427 (IC base=+0.053)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.425` → IC=+0.150 (n=469)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 10.425 (IC base=+0.053)

- **PATRÓN** `ibs_20min` < `0.0621` → IC=+0.269 (n=646)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0621 (IC base=+0.049)

- **PATRÓN** `volumen_pendiente_norm` > `0.1474` → IC=+0.136 (n=402)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` > 0.1474 (IC base=+0.049)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.124 (n=613)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0052 (IC base=+0.070)

- **PATRÓN** `ibs_20min` > `0.5456` → IC=+0.164 (n=593)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` > 0.5456 (IC base=+0.070)

- **PATRÓN** `dist_vwap_pct` > `0.119` → IC=+0.171 (n=320)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.119 (IC base=+0.070)

- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.132 (n=267)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.66€ cuando `sigma_h` < 0.0035 (IC base=+0.047)

- **PATRÓN** `ibs_20min` < `0.0674` → IC=+0.274 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0674 (IC base=+0.047)

- **PATRÓN** `volumen_pendiente_norm` > `0.2187` → IC=+0.147 (n=114)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` > 0.2187 (IC base=+0.047)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` > `0.6792` → IC=-0.158 (n=156)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6792
  - _Potencial_: sin este filtro IC_bueno=+0.107 (n=471)

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.129 (n=475)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.64€ cuando `sigma_h` < 0.0052 (IC base=+0.071)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.126 (n=351)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 15.0 (IC base=+0.071)

- **PATRÓN** `ibs_20min` > `0.7783` → IC=+0.219 (n=453)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7783 (IC base=+0.071)

- **PATRÓN** `dist_vwap_pct` > `0.1264` → IC=+0.172 (n=333)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.1264 (IC base=+0.071)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.646` → IC=+0.203 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.646 (IC base=+0.071)

- **PATRÓN** `ibs_20min` < `0.1112` → IC=+0.251 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1112 (IC base=+0.024)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.59` → IC=+0.195 (n=80)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 10.59 (IC base=+0.024)

### GBM_LATE_60M#SOL#60min
- **PATRÓN** `ibs_20min` > `0.7241` → IC=+0.135 (n=507)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` > 0.7241 (IC base=+0.021)

- **PATRÓN** `dist_vwap_pct` > `0.7051` → IC=+0.133 (n=175)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` > 0.7051 (IC base=+0.021)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.652` → IC=+0.133 (n=167)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` > 8.652 (IC base=+0.021)

- **PATRÓN** `sigma_h` < `0.0096` → IC=+0.184 (n=299)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0096 (IC base=+0.079)

- **PATRÓN** `ibs_20min` < `0.4857` → IC=+0.181 (n=418)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.4857 (IC base=+0.079)

- **PATRÓN** `dist_vwap_pct` < `0.1829` → IC=+0.141 (n=405)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.1829 (IC base=+0.079)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.779` → IC=+0.287 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.779 (IC base=+0.079)

- **PATRÓN** `volumen_regimen` > `1.0831` → IC=+0.181 (n=139)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` > 1.0831 (IC base=+0.079)

- **PATRÓN** `volumen_pendiente_norm` > `0.084` → IC=+0.161 (n=181)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.084 (IC base=+0.079)

- **PATRÓN** `volumen_spike_ratio` > `1.451` → IC=+0.128 (n=390)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` > 1.451 (IC base=+0.079)

### GBM_LATE_60M_FADE
- **FILTRO** `hora_utc` > `7.0` → IC=-0.300 (n=93)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.194 (n=286)

- **FILTRO** `dist_vwap_pct` > `0.2352` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2352
  - _Potencial_: sin este filtro IC_bueno=-0.215 (n=363)

- **FILTRO** `volumen_regimen` < `0.8567` → IC=-0.303 (n=125)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.8567
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=254)

- **FILTRO** `hora_utc` > `11.0` → IC=-0.309 (n=150)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.251 (n=179)

- **FILTRO** `dist_vwap_pct` > `0.4497` → IC=-0.405 (n=19)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4497
  - _Potencial_: sin este filtro IC_bueno=-0.269 (n=310)

- **FILTRO** `sigma_ewma_delta_pct` > `9.697` → IC=-0.328 (n=27)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 9.697
  - _Potencial_: sin este filtro IC_bueno=-0.273 (n=302)

- **FILTRO** `volumen_pendiente_norm` > `0.0448` → IC=-0.379 (n=31)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0448
  - _Potencial_: sin este filtro IC_bueno=-0.263 (n=209)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.280 (n=48)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.208 (n=63)

- **FILTRO** `volumen_regimen` < `0.89` → IC=-0.328 (n=27)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.89
  - _Potencial_: sin este filtro IC_bueno=-0.209 (n=84)

- **FILTRO** `volumen_regimen` > `0.805` → IC=-0.316 (n=36)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.226 (n=111)

- **FILTRO** `volumen_spike_ratio` > `1.4782` → IC=-0.310 (n=56)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.4782
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=58)

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
  - _Potencial_: sin este filtro IC_bueno=-0.277 (n=92)

- **FILTRO** `ibs_20min` > `0.681` → IC=-0.389 (n=43)

  - _Acción_: SKIP cuando `ibs_20min` > 0.681
  - _Potencial_: sin este filtro IC_bueno=-0.259 (n=85)

- **FILTRO** `volumen_spike_ratio` < `1.4324` → IC=-0.380 (n=23)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.4324
  - _Potencial_: sin este filtro IC_bueno=-0.292 (n=70)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.300 (n=113)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `sigma_h` < `0.0064` → IC=-0.333 (n=34)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0064
  - _Potencial_: sin este filtro IC_bueno=-0.202 (n=102)

- **FILTRO** `drift_60min` |x|> `0.2366` → IC=-0.357 (n=33)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2366
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=102)

- **FILTRO** `volumen_pendiente_norm` > `0.1196` → IC=-0.258 (n=31)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1196
  - _Potencial_: sin este filtro IC_bueno=-0.232 (n=80)

- **FILTRO** `volumen_spike_ratio` > `2.3401` → IC=-0.269 (n=37)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.3401
  - _Potencial_: sin este filtro IC_bueno=-0.224 (n=74)

- **FILTRO** `libro_spread` > `0.06` → IC=-0.250 (n=30)

  - _Acción_: SKIP cuando `libro_spread` > 0.06
  - _Potencial_: sin este filtro IC_bueno=-0.232 (n=106)

- **FILTRO** `sigma_h` < `0.0107` → IC=-0.333 (n=40)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0107
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=14)

- **FILTRO** `sigma_ewma_delta_pct` > `4.698` → IC=-0.382 (n=15)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.698
  - _Potencial_: sin este filtro IC_bueno=-0.207 (n=39)

- **FILTRO** `volumen_regimen` < `0.9051` → IC=-0.447 (n=17)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9051
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=37)

- **FILTRO** `libro_spread` > `0.04` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.04
  - _Potencial_: sin este filtro IC_bueno=-0.243 (n=33)

### GBM_LATE_60M_PYCONFIRMADO
- **PATRÓN** `sigma_h` > `0.0086` → IC=+0.249 (n=237)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0086 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.189 (n=368)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 15.0 (IC base=+0.142)

- **PATRÓN** `ibs_20min` > `0.6774` → IC=+0.179 (n=712)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.6774 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` > `0.7967` → IC=+0.285 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7967 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.614` → IC=+0.157 (n=389)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 3.614 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` < `8.522` → IC=+0.143 (n=726)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 8.522 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` < `0.6249` → IC=+0.179 (n=238)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 0.6249 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` > `1.2146` → IC=+0.144 (n=237)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 1.2146 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` < `0.0701` → IC=+0.174 (n=528)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` < 0.0701 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` < `1.3956` → IC=+0.196 (n=202)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 1.3956 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.489` → IC=+0.155 (n=195)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 10.489 (IC base=+0.036)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.7234` → IC=-0.148 (n=69)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7234
  - _Potencial_: sin este filtro IC_bueno=+0.093 (n=207)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.126 (n=105)

  - _Acción_: Kelly boost +0.63€ cuando `ibs_20min` > 1.0 (IC base=+0.032)

- **PATRÓN** `dist_vwap_pct` > `0.6135` → IC=+0.207 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6135 (IC base=+0.032)

- **PATRÓN** `ibs_20min` < `0.2162` → IC=+0.150 (n=392)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.2162 (IC base=+0.095)

- **PATRÓN** `volumen_spike_ratio` > `2.1144` → IC=+0.145 (n=164)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 2.1144 (IC base=+0.095)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `volumen_pendiente_norm` > `0.1814` → IC=-0.167 (n=25)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1814
  - _Potencial_: sin este filtro IC_bueno=+0.142 (n=258)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.155 (n=85)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 18.0 (IC base=+0.116)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.133 (n=118)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 8.0 (IC base=+0.116)

- **PATRÓN** `ibs_20min` > `0.7163` → IC=+0.146 (n=241)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` > 0.7163 (IC base=+0.116)

- **PATRÓN** `dist_vwap_pct` < `0.0973` → IC=+0.147 (n=199)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.0973 (IC base=+0.116)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.217` → IC=+0.139 (n=250)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 9.217 (IC base=+0.116)

- **PATRÓN** `volumen_regimen` > `1.1915` → IC=+0.163 (n=81)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 1.1915 (IC base=+0.116)

- **PATRÓN** `volumen_pendiente_norm` < `0.1814` → IC=+0.142 (n=258)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` < 0.1814 (IC base=+0.116)

- **PATRÓN** `volumen_spike_ratio` < `2.0546` → IC=+0.156 (n=187)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.0546 (IC base=+0.116)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.126 (n=209)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.01 (IC base=+0.116)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.619` → IC=+0.205 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.619 (IC base=+0.014)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.2` → IC=-0.233 (n=58)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=130)

- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.287 (n=120)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0099 (IC base=+0.251)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.299 (n=187)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.251)

- **PATRÓN** `ibs_20min` > `0.5882` → IC=+0.280 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5882 (IC base=+0.251)

- **PATRÓN** `dist_vwap_pct` > `0.6943` → IC=+0.392 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6943 (IC base=+0.251)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.832` → IC=+0.359 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.832 (IC base=+0.251)

- **PATRÓN** `volumen_regimen` < `0.5991` → IC=+0.300 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.5991 (IC base=+0.251)

- **PATRÓN** `volumen_pendiente_norm` > `0.0973` → IC=+0.327 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0973 (IC base=+0.251)

- **PATRÓN** `volumen_spike_ratio` < `1.4812` → IC=+0.330 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4812 (IC base=+0.251)

- **PATRÓN** `volumen_spike_ratio` > `2.3741` → IC=+0.303 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3741 (IC base=+0.251)

### LATE_WINDOW_5MIN
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.323 (n=111)

- **PATRÓN** `drift_ventana_pct` |x|> `0.349` → IC=+0.339 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.349 (IC base=+0.326)

- **PATRÓN** `elapsed_s` > `204.5` → IC=+0.398 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 204.5 (IC base=+0.326)

- **PATRÓN** `drift_15min` |x|≤ `1.0295` → IC=+0.435 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0295 (IC base=+0.326)

- **PATRÓN** `drift_60min` |x|≤ `0.9647` → IC=+0.374 (n=85)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9647 (IC base=+0.326)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.396 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.326)

- **PATRÓN** `ballena_activa_n` < `1220.0` → IC=+0.350 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1220.0 (IC base=+0.326)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3488` → IC=+0.295 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3488 (IC base=+0.262)

- **PATRÓN** `elapsed_s` > `230.1` → IC=+0.353 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 230.1 (IC base=+0.262)

- **PATRÓN** `drift_15min` |x|≤ `2.2537` → IC=+0.305 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.2537 (IC base=+0.262)

- **PATRÓN** `drift_60min` |x|≤ `0.6365` → IC=+0.306 (n=65)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6365 (IC base=+0.262)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.323 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.262)

- **PATRÓN** `ballena_activa_n` < `1330.0` → IC=+0.351 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1330.0 (IC base=+0.262)

### LATE_WINDOW_5MIN#BTC#5min
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.323 (n=111)

- **PATRÓN** `drift_ventana_pct` |x|> `0.349` → IC=+0.339 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.349 (IC base=+0.326)

- **PATRÓN** `elapsed_s` > `204.5` → IC=+0.398 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 204.5 (IC base=+0.326)

- **PATRÓN** `drift_15min` |x|≤ `1.0295` → IC=+0.435 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0295 (IC base=+0.326)

- **PATRÓN** `drift_60min` |x|≤ `0.9647` → IC=+0.374 (n=85)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9647 (IC base=+0.326)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.396 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.326)

- **PATRÓN** `ballena_activa_n` < `1220.0` → IC=+0.350 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1220.0 (IC base=+0.326)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3488` → IC=+0.295 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3488 (IC base=+0.262)

- **PATRÓN** `elapsed_s` > `230.1` → IC=+0.353 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 230.1 (IC base=+0.262)

- **PATRÓN** `drift_15min` |x|≤ `2.2537` → IC=+0.305 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.2537 (IC base=+0.262)

- **PATRÓN** `drift_60min` |x|≤ `0.6365` → IC=+0.306 (n=65)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6365 (IC base=+0.262)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.323 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.262)

- **PATRÓN** `ballena_activa_n` < `1330.0` → IC=+0.351 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1330.0 (IC base=+0.262)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.123 (n=1460)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` > 0.5 (IC base=+0.098)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.123 (n=1460)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` > 0.5 (IC base=+0.098)

### LIQUIDACIONES_15M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=247)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=247)

- **FILTRO** `libro_liquidez` < `3436.0985` → IC=-0.171 (n=86)

  - _Acción_: SKIP cuando `libro_liquidez` < 3436.0985
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=177)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=819)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `libro_liquidez` < `12112.4745` → IC=-0.167 (n=43)

  - _Acción_: SKIP cuando `libro_liquidez` < 12112.4745
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=90)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `liq_usd_total` < `4006.09` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `liq_usd_total` < 4006.09
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=28)

- **FILTRO** `hora_utc` < `10.0` → IC=-0.184 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=38)

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
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=3929)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=150)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=107)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.278 (n=34)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=137)

- **FILTRO** `ballena_activa_n` > `25.0` → IC=-0.156 (n=91)

  - _Acción_: SKIP cuando `ballena_activa_n` > 25.0
  - _Potencial_: sin este filtro IC_bueno=+0.188 (n=46)

- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.188 (n=46)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 25.0 (IC base=-0.078)

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

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.123 (n=274)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` < 0.495 (IC base=+0.023)

### LIQUIDACIONES_5M#DOGE#5min
- **PATRÓN** `liq_n` > `3.0` → IC=+0.333 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `liq_n` > 3.0 (IC base=+0.204)

- **PATRÓN** `liq_usd_total` > `2129.85` → IC=+0.321 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `liq_usd_total` > 2129.85 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.237 (n=36)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.204)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.203 (n=35)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.204)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.227 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.505 (IC base=+0.204)

- **PATRÓN** `libro_liquidez` > `2323.928` → IC=+0.230 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2323.928 (IC base=+0.204)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=1602)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=1556)

- **FILTRO** `hora_utc` > `5.0` → IC=-0.286 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=10)

### LIQUIDACIONES_5M#SOL#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=728)

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
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=446)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=427)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.137 (n=191)

  - _Acción_: Kelly boost +0.69€ cuando `py_entrada` < 0.495 (IC base=+0.019)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=1001)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=1001)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=1251)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=1251)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=284)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=284)

- **FILTRO** `py_entrada` < `0.42` → IC=-0.132 (n=74)

  - _Acción_: SKIP cuando `py_entrada` < 0.42
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=225)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.136 (n=64)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=347)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=396)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=301)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=401)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=401)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.120 (n=185)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=246)

- **FILTRO** `libro_liquidez` < `550.4778` → IC=-0.142 (n=107)

  - _Acción_: SKIP cuando `libro_liquidez` < 550.4778
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=324)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=358)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.188 (n=78)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=97)

- **FILTRO** `hora_utc` > `14.0` → IC=-0.159 (n=80)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=95)

- **FILTRO** `hora_utc` < `17.0` → IC=-0.125 (n=62)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=23)

### LIQUIDACIONES_DEPTH_FASE0#BTC#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.130 (n=282)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=706)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **FILTRO** `py_entrada` > `0.57` → IC=-0.121 (n=423)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.085 (n=499)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.142 (n=305)

  - _Acción_: Kelly boost +0.71€ cuando `py_entrada` < 0.5 (IC base=-0.010)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` > `0.57` → IC=-0.123 (n=351)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.068 (n=359)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` > `0.58` → IC=-0.122 (n=342)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=402)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.156 (n=158)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=670)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` > `0.61` → IC=-0.141 (n=115)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=358)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.41` → IC=-0.158 (n=317)

  - _Acción_: SKIP cuando `py_entrada` < 0.41
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=678)

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
- **FILTRO** `py_entrada` < `0.46` → IC=-0.174 (n=7865)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=25084)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.175 (n=8346)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=25642)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.186 (n=1521)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.118 (n=4581)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.149 (n=2032)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.094 (n=3994)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.133 (n=1578)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` > 1.0 (IC base=+0.042)

- **PATRÓN** `py_entrada` < `0.505` → IC=+0.125 (n=3057)

  - _Acción_: Kelly boost +0.63€ cuando `py_entrada` < 0.505 (IC base=+0.012)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` < `0.44` → IC=-0.173 (n=1090)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=3495)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.181 (n=1191)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=3587)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` > `0.62` → IC=-0.201 (n=1501)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.086 (n=4669)

- **PATRÓN** `ibs_20min` > `0.9626` → IC=+0.132 (n=2071)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` > 0.9626 (IC base=+0.034)

- **PATRÓN** `libro_liquidez` > `1742.2963` → IC=+0.120 (n=2071)

  - _Acción_: Kelly boost +0.60€ cuando `libro_liquidez` > 1742.2963 (IC base=+0.034)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.485` → IC=-0.160 (n=1521)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=4614)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=2432)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.162 (n=772)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=2356)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.180 (n=973)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=3054)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=4006)

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
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=1077)

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
  - _Potencial_: sin este filtro IC_bueno=-0.101 (n=361)

- **FILTRO** `ballena_activa_n` > `84.0` → IC=-0.179 (n=157)

  - _Acción_: SKIP cuando `ballena_activa_n` > 84.0
  - _Potencial_: sin este filtro IC_bueno=-0.101 (n=309)

- **FILTRO** `libro_liquidez` < `3222.056` → IC=-0.183 (n=156)

  - _Acción_: SKIP cuando `libro_liquidez` < 3222.056
  - _Potencial_: sin este filtro IC_bueno=-0.097 (n=318)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=968)

- **FILTRO** `ballena_activa_n` > `23.0` → IC=-0.191 (n=390)

  - _Acción_: SKIP cuando `ballena_activa_n` > 23.0
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=791)

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
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=92)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.135 (n=22461)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.090 (n=50433)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.297 (n=17472)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=55422)

- **FILTRO** `ibs_7min` < `0.2172` → IC=-0.233 (n=18222)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2172
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=54672)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.152 (n=23801)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=49093)

- **FILTRO** `py_entrada` > `0.68` → IC=-0.252 (n=21322)

  - _Acción_: SKIP cuando `py_entrada` > 0.68
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=69822)

- **FILTRO** `ibs_7min` > `0.2826` → IC=-0.184 (n=22770)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2826
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=68374)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.155 (n=3153)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=9834)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.316 (n=3206)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=9781)

- **FILTRO** `ibs_7min` < `0.7105` → IC=-0.250 (n=4281)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7105
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=8706)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.152 (n=2777)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=10210)

- **FILTRO** `py_entrada` > `0.72` → IC=-0.277 (n=3843)

  - _Acción_: SKIP cuando `py_entrada` > 0.72
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=11901)

- **FILTRO** `ibs_7min` > `0.7778` → IC=-0.211 (n=3931)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7778
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=11813)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.123 (n=2932)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.101 (n=9208)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.264 (n=2929)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=9211)

- **FILTRO** `ibs_7min` < `0.7143` → IC=-0.208 (n=3034)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7143
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=9106)

- **FILTRO** `ballena_activa_n` > `155.0` → IC=-0.200 (n=3025)

  - _Acción_: SKIP cuando `ballena_activa_n` > 155.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=9115)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.268 (n=2839)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=9542)

- **FILTRO** `ibs_7min` > `0.2664` → IC=-0.195 (n=3093)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2664
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=9288)

- **FILTRO** `ballena_activa_n` > `153.0` → IC=-0.182 (n=3094)

  - _Acción_: SKIP cuando `ballena_activa_n` > 153.0
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=9287)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.165 (n=3011)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=9412)

- **FILTRO** `py_entrada` < `0.3` → IC=-0.324 (n=2951)

  - _Acción_: SKIP cuando `py_entrada` < 0.3
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=9472)

- **FILTRO** `ibs_7min` < `0.2857` → IC=-0.250 (n=4083)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2857
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=8340)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.201 (n=2492)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=9931)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.259 (n=4043)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=12627)

- **FILTRO** `ibs_7min` > `0.7316` → IC=-0.182 (n=4167)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7316
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=12503)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.262 (n=2922)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=8875)

- **FILTRO** `ibs_7min` < `0.7143` → IC=-0.196 (n=2943)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7143
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=8854)

- **FILTRO** `ballena_activa_n` > `25.0` → IC=-0.190 (n=2869)

  - _Acción_: SKIP cuando `ballena_activa_n` > 25.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=8928)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.259 (n=2843)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=9425)

- **FILTRO** `ibs_7min` > `0.2737` → IC=-0.176 (n=3066)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2737
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=9202)

- **FILTRO** `ballena_activa_n` > `24.0` → IC=-0.172 (n=2984)

  - _Acción_: SKIP cuando `ballena_activa_n` > 24.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=9284)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.32` → IC=-0.298 (n=2761)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=8912)

- **FILTRO** `ibs_7min` < `0.7` → IC=-0.234 (n=3777)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=7896)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.216 (n=2877)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=8796)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.198 (n=4278)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=13365)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.132 (n=3828)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.107 (n=8046)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.308 (n=2830)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=9044)

- **FILTRO** `ibs_7min` < `0.1563` → IC=-0.231 (n=2968)

  - _Acción_: SKIP cuando `ibs_7min` < 0.1563
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=8906)

- **FILTRO** `ballena_activa_n` > `9.0` → IC=-0.205 (n=2636)

  - _Acción_: SKIP cuando `ballena_activa_n` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.090 (n=9238)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.234 (n=3819)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=12619)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1046` → IC=-0.135 (n=61)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1046
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=121)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `py_entrada` < `0.455` → IC=-0.163 (n=304)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=1012)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=1301)

- **FILTRO** `py_entrada` > `0.545` → IC=-0.157 (n=170)

  - _Acción_: SKIP cuando `py_entrada` > 0.545
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=625)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=1458)

- **FILTRO** `py_entrada` > `0.565` → IC=-0.172 (n=260)

  - _Acción_: SKIP cuando `py_entrada` > 0.565
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=892)

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
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=578)

- **FILTRO** `libro_liquidez` < `3302.3462` → IC=-0.155 (n=192)

  - _Acción_: SKIP cuando `libro_liquidez` < 3302.3462
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=578)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=395)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.4307` → IC=+0.148 (n=683)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.74€ cuando `delta_ratio` |x|> 0.4307 (IC base=+0.123)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.127 (n=1359)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 14.0 (IC base=+0.123)

- **PATRÓN** `total_vol_5m` < `418.1326` → IC=+0.161 (n=502)

  - _Acción_: Kelly boost +0.80€ cuando `total_vol_5m` < 418.1326 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `2322.369` → IC=+0.130 (n=1345)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 2322.369 (IC base=+0.123)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `14.0` → IC=+0.179 (n=182)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 14.0 (IC base=+0.133)

- **PATRÓN** `total_vol_5m` < `371.804` → IC=+0.155 (n=317)

  - _Acción_: Kelly boost +0.78€ cuando `total_vol_5m` < 371.804 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `2506.369` → IC=+0.240 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2506.369 (IC base=+0.133)

- **PATRÓN** `ballena_activa_n` < `6.0` → IC=+0.136 (n=174)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 6.0 (IC base=+0.133)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `delta_ratio` |x|> `0.4378` → IC=+0.151 (n=104)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.75€ cuando `delta_ratio` |x|> 0.4378 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.140 (n=287)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 15.0 (IC base=+0.117)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.123 (n=372)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.04 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `2389.574` → IC=+0.141 (n=204)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 2389.574 (IC base=+0.117)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4165` → IC=+0.175 (n=189)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.88€ cuando `delta_ratio` |x|> 0.4165 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.148 (n=262)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 5.0 (IC base=+0.125)

- **PATRÓN** `total_vol_5m` < `852.6939` → IC=+0.153 (n=283)

  - _Acción_: Kelly boost +0.76€ cuando `total_vol_5m` < 852.6939 (IC base=+0.125)

- **PATRÓN** `ballena_activa_n` < `59.0` → IC=+0.173 (n=96)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 59.0 (IC base=+0.125)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.3978` → IC=+0.165 (n=258)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.83€ cuando `delta_ratio` |x|> 0.3978 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.170 (n=186)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 12.0 (IC base=+0.141)

- **PATRÓN** `total_vol_5m` < `4608.276` → IC=+0.178 (n=172)

  - _Acción_: Kelly boost +0.89€ cuando `total_vol_5m` < 4608.276 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `3712.2533` → IC=+0.161 (n=172)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 3712.2533 (IC base=+0.141)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `hora_utc` < `14.0` → IC=+0.126 (n=276)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 14.0 (IC base=+0.096)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.137 (n=202)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.096)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `4.8182` → IC=-0.203 (n=116)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.8182
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=118)

- **FILTRO** `sigma_h` > `0.0068` → IC=-0.240 (n=287)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0068
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=558)

- **FILTRO** `T_h` > `129.6211` → IC=-0.179 (n=210)

  - _Acción_: SKIP cuando `T_h` > 129.6211
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=635)

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.148 (n=279)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0045 (IC base=-0.071)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `T_h` > `88.1766` → IC=-0.234 (n=62)

  - _Acción_: SKIP cuando `T_h` > 88.1766
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=190)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.279 (n=84)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=-0.028)

- **PATRÓN** `pct_vs_K` |x|≤ `1.73` → IC=+0.174 (n=84)

  - _Acción_: Kelly boost +0.87€ cuando `pct_vs_K` |x|≤ 1.73 (IC base=-0.028)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `sigma_h` > `0.0107` → IC=-0.136 (n=20)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0107
  - _Potencial_: sin este filtro IC_bueno=-0.121 (n=64)

- **FILTRO** `pct_vs_K` |x|> `6.6759` → IC=-0.267 (n=28)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 6.6759
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=56)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0129` → IC=-0.161 (n=54)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0129
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=107)

- **FILTRO** `T_h` < `66.2576` → IC=-0.191 (n=53)

  - _Acción_: SKIP cuando `T_h` < 66.2576
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=108)

### PRICE_TARGET_GBM#SOL#reach
- **FILTRO** `T_h` < `146.0708` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `T_h` < 146.0708
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=16)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0112` → IC=-0.230 (n=579)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0112
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=193)

- **FILTRO** `T_h` > `70.1154` → IC=-0.230 (n=516)

  - _Acción_: SKIP cuando `T_h` > 70.1154
  - _Potencial_: sin este filtro IC_bueno=-0.194 (n=256)

- **FILTRO** `pct_vs_K` |x|> `2.0709` → IC=-0.336 (n=333)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.0709
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=341)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `sigma_h` < `0.0083` → IC=-0.208 (n=166)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0083
  - _Potencial_: sin este filtro IC_bueno=-0.163 (n=87)

- **FILTRO** `T_h` > `143.1632` → IC=-0.262 (n=61)

  - _Acción_: SKIP cuando `T_h` > 143.1632
  - _Potencial_: sin este filtro IC_bueno=-0.186 (n=186)

- **FILTRO** `pct_vs_K` |x|> `2.5079` → IC=-0.371 (n=83)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.5079
  - _Potencial_: sin este filtro IC_bueno=-0.120 (n=164)

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
- **FILTRO** `sigma_h` < `0.01` → IC=-0.307 (n=143)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=75)

- **FILTRO** `T_h` > `60.9471` → IC=-0.282 (n=163)

  - _Acción_: SKIP cuando `T_h` > 60.9471
  - _Potencial_: sin este filtro IC_bueno=-0.254 (n=55)

- **FILTRO** `pct_vs_K` |x|> `2.8988` → IC=-0.415 (n=69)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.8988
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=134)

- **PATRÓN** `pct_vs_K` |x|≤ `0.8095` → IC=+0.198 (n=51)

  - _Acción_: Kelly boost +0.99€ cuando `pct_vs_K` |x|≤ 0.8095 (IC base=-0.159)

### PRICE_TARGET_GBM_FADE#ETH#reach
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
- **FILTRO** `sigma_h` < `0.0083` → IC=-0.268 (n=54)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0083
  - _Potencial_: sin este filtro IC_bueno=-0.159 (n=162)

- **FILTRO** `T_h` > `66.1685` → IC=-0.224 (n=161)

  - _Acción_: SKIP cuando `T_h` > 66.1685
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=55)

- **FILTRO** `sigma_h` > `0.0142` → IC=-0.304 (n=49)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0142
  - _Potencial_: sin este filtro IC_bueno=-0.160 (n=98)

- **FILTRO** `sigma_h` < `0.0099` → IC=-0.260 (n=48)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0099
  - _Potencial_: sin este filtro IC_bueno=-0.183 (n=99)

- **FILTRO** `T_h` > `33.9175` → IC=-0.232 (n=110)

  - _Acción_: SKIP cuando `T_h` > 33.9175
  - _Potencial_: sin este filtro IC_bueno=-0.141 (n=37)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1195` → IC=+0.461 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1195 (IC base=+0.333)

- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.383 (n=75)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0104 (IC base=+0.333)

- **PATRÓN** `T_h` < `0.3261` → IC=+0.400 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.3261 (IC base=+0.333)

- **PATRÓN** `T_h` > `0.8789` → IC=+0.368 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.8789 (IC base=+0.333)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.481 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.333)

- **PATRÓN** `edge` > `0.1005` → IC=+0.429 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1005 (IC base=+0.394)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.401 (n=89)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0075 (IC base=+0.394)

- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.410 (n=176)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0097 (IC base=+0.394)

- **PATRÓN** `T_h` < `0.7258` → IC=+0.433 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.7258 (IC base=+0.394)

- **PATRÓN** `T_h` > `1.4832` → IC=+0.400 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4832 (IC base=+0.394)

- **PATRÓN** `dist_50` > `0.3717` → IC=+0.444 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3717 (IC base=+0.394)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.412 (n=327)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.394)

### RESOLUTION_SNIPER#BTC#sniper
- **PATRÓN** `edge` > `0.1235` → IC=+0.268 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1235 (IC base=+0.179)

- **PATRÓN** `sigma_h` < `0.0077` → IC=+0.269 (n=37)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0077 (IC base=+0.179)

- **PATRÓN** `T_h` > `1.484` → IC=+0.210 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.484 (IC base=+0.179)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.263 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.219 (n=55)
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

- **PATRÓN** `edge` > `0.2005` → IC=+0.471 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.2005 (IC base=+0.463)

- **PATRÓN** `sigma_h` < `0.0156` → IC=+0.474 (n=151)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0156 (IC base=+0.463)

- **PATRÓN** `T_h` < `0.8072` → IC=+0.457 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.8072 (IC base=+0.463)

- **PATRÓN** `T_h` > `1.4857` → IC=+0.481 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4857 (IC base=+0.463)

- **PATRÓN** `dist_50` > `0.4593` → IC=+0.493 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4593 (IC base=+0.463)

- **PATRÓN** `hora_utc` < `2.0` → IC=+0.485 (n=63)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 2.0 (IC base=+0.463)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=420)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.074 (n=477)

- **PATRÓN** `streak_estiramiento` < `0.8196` → IC=+0.127 (n=328)

  - _Acción_: Kelly boost +0.64€ cuando `streak_estiramiento` < 0.8196 (IC base=+0.062)

- **PATRÓN** `ballena_activa_n` < `30.0` → IC=+0.129 (n=246)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 30.0 (IC base=+0.062)

### STREAK_FADE_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=17)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` < 0.495 (IC base=+0.081)

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
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=165)

- **PATRÓN** `streak_estiramiento` < `0.2236` → IC=+0.125 (n=62)

  - _Acción_: Kelly boost +0.62€ cuando `streak_estiramiento` < 0.2236 (IC base=+0.031)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.150 (n=118)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 11.0 (IC base=+0.098)

- **PATRÓN** `streak_estiramiento` < `0.437` → IC=+0.186 (n=138)

  - _Acción_: Kelly boost +0.93€ cuando `streak_estiramiento` < 0.437 (IC base=+0.098)

- **PATRÓN** `ballena_activa_n` < `31.0` → IC=+0.165 (n=150)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 31.0 (IC base=+0.098)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `9.0` → IC=-0.197 (n=31)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=103)

- **FILTRO** `streak_len` > `5.0` → IC=-0.250 (n=22)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=112)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=71)

- **FILTRO** `libro_liquidez` < `3678.6572` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 3678.6572
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=78)

- **FILTRO** `streak_len` > `3.0` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=51)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.136 (n=31)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=36)

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

  - _Acción_: Kelly boost +0.76€ cuando `regimen_ma_toques` > 4.0 (IC base=+0.026)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=1067)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=1341)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=1244)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=1295)

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
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=4915)

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
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=2822)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.188 (n=1760)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0053 (IC base=+0.143)

- **PATRÓN** `drift_60min` |x|≤ `0.2199` → IC=+0.159 (n=5279)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.2199 (IC base=+0.143)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3558` → IC=+0.150 (n=4927)

  - _Acción_: Kelly boost +0.75€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3558 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.153 (n=4864)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 6.0 (IC base=+0.143)

- **PATRÓN** `ibs_15` > `0.5806` → IC=+0.227 (n=4716)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5806 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` > `0.1329` → IC=+0.133 (n=2500)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` > 0.1329 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` < `0.6811` → IC=+0.128 (n=5254)

  - _Acción_: Kelly boost +0.64€ cuando `dist_vwap_pct` < 0.6811 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.295` → IC=+0.250 (n=998)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.295 (IC base=+0.143)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=3037)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `4556.2087` → IC=+0.169 (n=1760)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 4556.2087 (IC base=+0.143)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=2015)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.221 (n=786)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0057 (IC base=+0.201)

- **PATRÓN** `drift_60min` |x|≤ `0.0593` → IC=+0.254 (n=262)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0593 (IC base=+0.201)

- **PATRÓN** `delta_ratio_macro` |x|> `0.269` → IC=+0.224 (n=262)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.269 (IC base=+0.201)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.227 (n=723)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.201)

- **PATRÓN** `ibs_15` > `0.7082` → IC=+0.273 (n=786)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7082 (IC base=+0.201)

- **PATRÓN** `dist_vwap_pct` > `0.3735` → IC=+0.227 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3735 (IC base=+0.201)

- **PATRÓN** `dist_vwap_pct` < `0.5105` → IC=+0.203 (n=885)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5105 (IC base=+0.201)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.43` → IC=+0.309 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.43 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.204 (n=1017)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.201)

- **PATRÓN** `libro_liquidez` > `15745.2501` → IC=+0.224 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15745.2501 (IC base=+0.201)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.007` → IC=+0.148 (n=973)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.007 (IC base=+0.132)

- **PATRÓN** `drift_60min` |x|≤ `0.1094` → IC=+0.147 (n=649)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.1094 (IC base=+0.132)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1407` → IC=+0.133 (n=649)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.66€ cuando `delta_ratio_macro` |x|> 0.1407 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.139 (n=888)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 6.0 (IC base=+0.132)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.132 (n=974)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 16.0 (IC base=+0.132)

- **PATRÓN** `ibs_15` > `0.4932` → IC=+0.218 (n=972)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.4932 (IC base=+0.132)

- **PATRÓN** `dist_vwap_pct` > `0.1169` → IC=+0.152 (n=613)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.1169 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.81` → IC=+0.284 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.81 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `5944.0797` → IC=+0.168 (n=441)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 5944.0797 (IC base=+0.132)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `ibs_15` > `0.2564` → IC=-0.122 (n=207)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.2564
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=404)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `ibs_15` > `0.5917` → IC=+0.131 (n=976)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.65€ cuando `ibs_15` > 0.5917 (IC base=+0.057)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` < `0.0256` → IC=+0.168 (n=1313)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0256 (IC base=+0.156)

- **PATRÓN** `drift_60min` |x|≤ `0.2241` → IC=+0.178 (n=1313)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.2241 (IC base=+0.156)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0986` → IC=+0.217 (n=404)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0986 (IC base=+0.156)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.163 (n=1197)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 6.0 (IC base=+0.156)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.162 (n=1164)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 14.0 (IC base=+0.156)

- **PATRÓN** `ibs_15` > `0.5455` → IC=+0.230 (n=1173)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5455 (IC base=+0.156)

- **PATRÓN** `dist_vwap_pct` > `0.5234` → IC=+0.196 (n=314)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.5234 (IC base=+0.156)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.093` → IC=+0.205 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.093 (IC base=+0.156)

- **PATRÓN** `libro_liquidez` > `2734.8592` → IC=+0.188 (n=875)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 2734.8592 (IC base=+0.156)

- **PATRÓN** `ibs_15` < `0.1091` → IC=+0.156 (n=1007)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.78€ cuando `ibs_15` < 0.1091 (IC base=+0.068)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` > `0.006` → IC=+0.388 (n=249)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.006 (IC base=+0.364)

- **PATRÓN** `drift_60min` |x|≤ `0.1117` → IC=+0.364 (n=498)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1117 (IC base=+0.364)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1505` → IC=+0.378 (n=497)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1505 (IC base=+0.364)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1351` → IC=+0.380 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1351 (IC base=+0.364)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.371 (n=789)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.364)

- **PATRÓN** `ibs_15` > `0.7883` → IC=+0.392 (n=747)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7883 (IC base=+0.364)

- **PATRÓN** `dist_vwap_pct` > `0.1529` → IC=+0.381 (n=442)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1529 (IC base=+0.364)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.84` → IC=+0.400 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.84 (IC base=+0.364)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.367 (n=909)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.364)

- **PATRÓN** `libro_liquidez` > `9681.5596` → IC=+0.380 (n=339)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9681.5596 (IC base=+0.364)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `drift_60min` |x|≤ `0.0547` → IC=+0.364 (n=123)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0547 (IC base=+0.361)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2197` → IC=+0.375 (n=166)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2197 (IC base=+0.361)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1441` → IC=+0.399 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1441 (IC base=+0.361)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.380 (n=340)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.361)

- **PATRÓN** `ibs_15` > `0.8112` → IC=+0.384 (n=367)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8112 (IC base=+0.361)

- **PATRÓN** `dist_vwap_pct` > `0.3743` → IC=+0.392 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3743 (IC base=+0.361)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.117` → IC=+0.382 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.117 (IC base=+0.361)

- **PATRÓN** `libro_liquidez` > `8119.484` → IC=+0.384 (n=367)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8119.484 (IC base=+0.361)

- **PATRÓN** `ballena_activa_n` < `487.0` → IC=+0.401 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 487.0 (IC base=+0.361)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.369 (n=380)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.364)

- **PATRÓN** `sigma_h` > `0.006` → IC=+0.380 (n=173)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.006 (IC base=+0.364)

- **PATRÓN** `drift_60min` |x|≤ `0.1078` → IC=+0.367 (n=254)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1078 (IC base=+0.364)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1294` → IC=+0.378 (n=253)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1294 (IC base=+0.364)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2969` → IC=+0.375 (n=310)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2969 (IC base=+0.364)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.367 (n=382)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.364)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.376 (n=175)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.364)

- **PATRÓN** `ibs_15` > `0.762` → IC=+0.393 (n=380)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.762 (IC base=+0.364)

- **PATRÓN** `dist_vwap_pct` > `0.1215` → IC=+0.372 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1215 (IC base=+0.364)

- **PATRÓN** `dist_vwap_pct` < `0.6315` → IC=+0.367 (n=433)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6315 (IC base=+0.364)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.889` → IC=+0.404 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.889 (IC base=+0.364)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.368 (n=430)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.364)

- **PATRÓN** `libro_liquidez` > `4142.643` → IC=+0.380 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4142.643 (IC base=+0.364)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0075` → IC=-0.195 (n=2691)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0075
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=2692)

- **FILTRO** `drift_15min` |x|> `0.9116` → IC=-0.147 (n=1345)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.9116
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=4037)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.218 (n=2265)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=3118)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1404` → IC=+0.220 (n=462)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1404 (IC base=-0.082)

- **PATRÓN** `ibs_15` > `0.6296` → IC=+0.278 (n=1220)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6296 (IC base=-0.082)

- **PATRÓN** `dist_vwap_pct` > `0.1092` → IC=+0.202 (n=715)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1092 (IC base=-0.082)

- **PATRÓN** `dist_vwap_pct` < `0.5539` → IC=+0.198 (n=1290)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` < 0.5539 (IC base=-0.082)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2351` → IC=+0.267 (n=1630)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2351 (IC base=-0.005)

- **PATRÓN** `ibs_15` < `0.3696` → IC=+0.284 (n=4892)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3696 (IC base=-0.005)

- **PATRÓN** `dist_vwap_pct` > `0.6425` → IC=+0.279 (n=682)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6425 (IC base=-0.005)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0317` → IC=-0.223 (n=2543)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0317
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=849)

- **FILTRO** `sigma_h` < `0.0038` → IC=-0.216 (n=848)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0038
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=2544)

- **FILTRO** `sigma_ewma_delta_pct` > `22.185` → IC=-0.259 (n=479)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 22.185
  - _Potencial_: sin este filtro IC_bueno=-0.175 (n=2913)

- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.157 (n=327)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0031 (IC base=+0.070)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2674` → IC=+0.285 (n=142)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2674 (IC base=+0.070)

- **PATRÓN** `ibs_15` > `0.7593` → IC=+0.322 (n=425)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7593 (IC base=+0.070)

- **PATRÓN** `dist_vwap_pct` > `0.102` → IC=+0.277 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.102 (IC base=+0.070)

- **PATRÓN** `dist_vwap_pct` < `0.4912` → IC=+0.283 (n=473)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4912 (IC base=+0.070)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.257` → IC=+0.145 (n=218)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 22.257 (IC base=+0.070)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0742` → IC=+0.224 (n=74)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0742 (IC base=-0.187)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0866` → IC=+0.308 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0866 (IC base=-0.187)

- **PATRÓN** `ibs_15` < `0.6255` → IC=+0.289 (n=74)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.6255 (IC base=-0.187)

- **PATRÓN** `dist_vwap_pct` < `0.0453` → IC=+0.303 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0453 (IC base=-0.187)

- **PATRÓN** `ballena_activa_n` < `393.0` → IC=+0.300 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 393.0 (IC base=-0.187)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.152 (n=798)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.161 (n=538)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0059 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.0721` → IC=+0.179 (n=269)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.0721 (IC base=+0.146)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3021` → IC=+0.196 (n=478)

  - _Acción_: Kelly boost +0.98€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3021 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.167 (n=283)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 15.0 (IC base=+0.146)

- **PATRÓN** `ibs_15` > `0.5659` → IC=+0.241 (n=612)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5659 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.6245` → IC=+0.158 (n=112)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.6245 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` < `0.2672` → IC=+0.149 (n=571)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.2672 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.973` → IC=+0.265 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.973 (IC base=+0.146)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=798)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `8982.7122` → IC=+0.160 (n=204)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 8982.7122 (IC base=+0.146)

- **PATRÓN** `sigma_h` < `0.0082` → IC=+0.249 (n=1867)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0082 (IC base=+0.243)

- **PATRÓN** `drift_60min` |x|≤ `0.3545` → IC=+0.248 (n=1643)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3545 (IC base=+0.243)

- **PATRÓN** `drift_15min` |x|≤ `0.7787` → IC=+0.258 (n=1643)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7787 (IC base=+0.243)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2152` → IC=+0.259 (n=846)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2152 (IC base=+0.243)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.254 (n=690)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.243)

- **PATRÓN** `ibs_15` < `0.1842` → IC=+0.303 (n=1245)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.1842 (IC base=+0.243)

- **PATRÓN** `dist_vwap_pct` > `0.3756` → IC=+0.271 (n=469)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3756 (IC base=+0.243)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.23` → IC=+0.248 (n=821)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.23 (IC base=+0.243)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.153` → IC=+0.248 (n=1947)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.153 (IC base=+0.243)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1844` → IC=-0.265 (n=313)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1844
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=940)

- **FILTRO** `sigma_h` > `0.0105` → IC=-0.234 (n=426)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0105
  - _Potencial_: sin este filtro IC_bueno=-0.181 (n=827)

- **FILTRO** `drift_60min` |x|> `0.1724` → IC=-0.264 (n=426)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1724
  - _Potencial_: sin este filtro IC_bueno=-0.166 (n=827)

- **FILTRO** `drift_15min` |x|> `0.9086` → IC=-0.284 (n=313)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.9086
  - _Potencial_: sin este filtro IC_bueno=-0.171 (n=940)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1455` → IC=+0.188 (n=46)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.94€ cuando `delta_ratio_macro` |x|> 0.1455 (IC base=-0.200)

- **PATRÓN** `ibs_15` > `0.5625` → IC=+0.234 (n=62)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5625 (IC base=-0.200)

- **PATRÓN** `dist_vwap_pct` > `0.2752` → IC=+0.143 (n=26)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.2752 (IC base=-0.200)

- **PATRÓN** `dist_vwap_pct` < `0.4298` → IC=+0.154 (n=76)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.4298 (IC base=-0.200)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0642` → IC=+0.236 (n=835)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0642 (IC base=-0.031)

- **PATRÓN** `ibs_15` < `0.3814` → IC=+0.294 (n=835)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3814 (IC base=-0.031)

- **PATRÓN** `dist_vwap_pct` > `0.6712` → IC=+0.241 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6712 (IC base=-0.031)

- **PATRÓN** `dist_vwap_pct` < `0.4491` → IC=+0.242 (n=893)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4491 (IC base=-0.031)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.016` → IC=-0.247 (n=1025)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.016
  - _Potencial_: sin este filtro IC_bueno=-0.153 (n=506)

- **FILTRO** `libro_spread` > `0.04` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.04
  - _Potencial_: sin este filtro IC_bueno=-0.215 (n=1512)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.216)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.216)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1185` → IC=+0.299 (n=506)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1185 (IC base=-0.017)

- **PATRÓN** `ibs_15` < `0.1358` → IC=+0.310 (n=776)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.1358 (IC base=-0.017)

- **PATRÓN** `dist_vwap_pct` > `0.7569` → IC=+0.339 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7569 (IC base=-0.017)

### UPDOWN_GBM_ETH_15M_HORA7
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.160 (n=51)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0065 (IC base=+0.109)

- **PATRÓN** `drift_60min` |x|≤ `0.1564` → IC=+0.160 (n=45)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.1564 (IC base=+0.109)

- **PATRÓN** `drift_15min` |x|≤ `0.3763` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3763 (IC base=+0.109)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.235` → IC=+0.206 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.235 (IC base=+0.109)

- **PATRÓN** `ibs_15` > `0.8434` → IC=+0.340 (n=23)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8434 (IC base=+0.109)

- **PATRÓN** `dist_vwap_pct` > `0.4735` → IC=+0.167 (n=16)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.4735 (IC base=+0.109)

- **PATRÓN** `dist_vwap_pct` < `0.0917` → IC=+0.224 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0917 (IC base=+0.109)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.861` → IC=+0.167 (n=16)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 11.861 (IC base=+0.109)

- **PATRÓN** `libro_liquidez` > `3887.0921` → IC=+0.138 (n=45)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 3887.0921 (IC base=+0.109)

- **PATRÓN** `ballena_activa_n` < `116.0` → IC=+0.153 (n=47)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 116.0 (IC base=+0.109)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.160 (n=51)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0065 (IC base=+0.109)

- **PATRÓN** `drift_60min` |x|≤ `0.1564` → IC=+0.160 (n=45)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.1564 (IC base=+0.109)

- **PATRÓN** `drift_15min` |x|≤ `0.3763` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3763 (IC base=+0.109)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.235` → IC=+0.206 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.235 (IC base=+0.109)

- **PATRÓN** `ibs_15` > `0.8434` → IC=+0.340 (n=23)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8434 (IC base=+0.109)

- **PATRÓN** `dist_vwap_pct` > `0.4735` → IC=+0.167 (n=16)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.4735 (IC base=+0.109)

- **PATRÓN** `dist_vwap_pct` < `0.0917` → IC=+0.224 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0917 (IC base=+0.109)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.861` → IC=+0.167 (n=16)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 11.861 (IC base=+0.109)

- **PATRÓN** `libro_liquidez` > `3887.0921` → IC=+0.138 (n=45)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 3887.0921 (IC base=+0.109)

- **PATRÓN** `ballena_activa_n` < `116.0` → IC=+0.153 (n=47)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 116.0 (IC base=+0.109)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.302 (n=447)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0033 (IC base=+0.283)

- **PATRÓN** `drift_60min` |x|≤ `0.0721` → IC=+0.311 (n=590)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0721 (IC base=+0.283)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1533` → IC=+0.284 (n=893)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1533 (IC base=+0.283)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2228` → IC=+0.292 (n=816)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2228 (IC base=+0.283)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.296 (n=1385)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.283)

- **PATRÓN** `ibs_15` > `0.838` → IC=+0.312 (n=1342)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.838 (IC base=+0.283)

- **PATRÓN** `dist_vwap_pct` > `0.2619` → IC=+0.315 (n=582)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2619 (IC base=+0.283)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.915` → IC=+0.389 (n=296)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.915 (IC base=+0.283)

- **PATRÓN** `libro_liquidez` > `13285.6042` → IC=+0.302 (n=447)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13285.6042 (IC base=+0.283)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.303 (n=237)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.275)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.275 (n=322)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.275)

- **PATRÓN** `drift_60min` |x|≤ `0.0587` → IC=+0.307 (n=237)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0587 (IC base=+0.275)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2702` → IC=+0.277 (n=236)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2702 (IC base=+0.275)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3948` → IC=+0.279 (n=636)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3948 (IC base=+0.275)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.293 (n=742)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.275)

- **PATRÓN** `ibs_15` > `0.8287` → IC=+0.300 (n=709)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8287 (IC base=+0.275)

- **PATRÓN** `dist_vwap_pct` > `0.2467` → IC=+0.308 (n=306)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2467 (IC base=+0.275)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.742` → IC=+0.393 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.742 (IC base=+0.275)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.277 (n=916)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.275)

- **PATRÓN** `libro_liquidez` > `15821.8878` → IC=+0.312 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15821.8878 (IC base=+0.275)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.299 (n=631)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0069 (IC base=+0.291)

- **PATRÓN** `drift_60min` |x|≤ `0.0506` → IC=+0.317 (n=211)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0506 (IC base=+0.291)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0654` → IC=+0.291 (n=631)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0654 (IC base=+0.291)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1007` → IC=+0.329 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1007 (IC base=+0.291)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.304 (n=605)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.291)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.294 (n=445)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.291)

- **PATRÓN** `ibs_15` > `0.8486` → IC=+0.320 (n=631)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8486 (IC base=+0.291)

- **PATRÓN** `dist_vwap_pct` > `0.2788` → IC=+0.318 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2788 (IC base=+0.291)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.12` → IC=+0.381 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.12 (IC base=+0.291)

### UPDOWN_OU_5M
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1157` → IC=-0.153 (n=223)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1157
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=111)

- **FILTRO** `ballena_activa_n` > `34.0` → IC=-0.131 (n=253)

  - _Acción_: SKIP cuando `ballena_activa_n` > 34.0
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=91)

- **FILTRO** `sigma_h` < `0.0051` → IC=-0.177 (n=122)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0051
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=367)

- **FILTRO** `ballena_activa_n` > `24.0` → IC=-0.204 (n=113)

  - _Acción_: SKIP cuando `ballena_activa_n` > 24.0
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=115)

### UPDOWN_OU_5M#BNB#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1682` → IC=-0.191 (n=40)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1682
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=41)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.160 (n=48)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=54)

### UPDOWN_OU_5M#BTC#5min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.2127` → IC=-0.233 (n=28)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2127
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=29)

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

- **FILTRO** `sigma_h` < `0.0047` → IC=-0.326 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0047
  - _Potencial_: sin este filtro IC_bueno=-0.286 (n=12)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.306` → IC=-0.385 (n=24)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.306
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `drift_60min` |x|> `0.2521` → IC=-0.200 (n=18)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2521
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=37)

- **FILTRO** `ballena_activa_n` > `42.0` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `ballena_activa_n` > 42.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=34)

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
- **PATRÓN** `ratio` < `0.9703` → IC=+0.393 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9703 (IC base=+0.172)

- **PATRÓN** `T_h` > `118.7731` → IC=+0.353 (n=2808)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 118.7731 (IC base=+0.335)

- **PATRÓN** `ratio` > `1.0211` → IC=+0.387 (n=486)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0211 (IC base=+0.335)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `111.9957` → IC=+0.139 (n=267)

  - _Acción_: Kelly boost +0.70€ cuando `T_h` > 111.9957 (IC base=+0.130)

- **PATRÓN** `ratio` < `0.9933` → IC=+0.261 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9933 (IC base=+0.130)

- **PATRÓN** `T_h` > `111.9824` → IC=+0.316 (n=1012)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9824 (IC base=+0.299)

- **PATRÓN** `ratio` > `1.0177` → IC=+0.366 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0177 (IC base=+0.299)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `87.7391` → IC=+0.223 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 87.7391 (IC base=+0.220)

- **PATRÓN** `ratio` < `0.9854` → IC=+0.403 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9854 (IC base=+0.220)

- **PATRÓN** `T_h` > `111.996` → IC=+0.352 (n=1020)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.996 (IC base=+0.322)

- **PATRÓN** `ratio` > `1.0082` → IC=+0.342 (n=308)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0082 (IC base=+0.322)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.0625` → IC=+0.418 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.0625 (IC base=+0.397)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5806 sube el IC de +0.143 a +0.227 en UPDOWN_GBM#15min (n=4716). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7082 sube el IC de +0.201 a +0.273 en UPDOWN_GBM#BTC#15min (n=786). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.4932 sube el IC de +0.132 a +0.218 en UPDOWN_GBM#ETH#15min (n=972). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5455 sube el IC de +0.156 a +0.230 en UPDOWN_GBM#XRP#15min (n=1173). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1091 sube el IC de +0.068 a +0.156 en UPDOWN_GBM#XRP#15min (n=1007). Ya aplicado como kelly_boost=+0.78€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6296 sube el IC de -0.082 a +0.278 en UPDOWN_GBM_15M_TARDIO (n=1220). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3696 sube el IC de -0.005 a +0.284 en UPDOWN_GBM_15M_TARDIO (n=4892). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7593 sube el IC de +0.070 a +0.322 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=425). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.6255 sube el IC de -0.187 a +0.289 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=74). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.5659 sube el IC de +0.146 a +0.241 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=612). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.1842 sube el IC de +0.243 a +0.303 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=1245). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de -0.200 a +0.234 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=62). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3814 sube el IC de -0.031 a +0.294 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=835). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.216 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.1358 sube el IC de -0.017 a +0.310 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=776). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_YES, IBS > 0.8434 sube el IC de +0.109 a +0.340 en UPDOWN_GBM_ETH_15M_HORA7 (n=23). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_YES, IBS > 0.8434 sube el IC de +0.109 a +0.340 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=23). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.838 sube el IC de +0.283 a +0.312 en UPDOWN_GBM_IBS_ALTO (n=1342). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8287 sube el IC de +0.275 a +0.300 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=709). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8486 sube el IC de +0.291 a +0.320 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=631). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7883 sube el IC de +0.364 a +0.392 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=747). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8112 sube el IC de +0.361 a +0.384 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=367). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.762 sube el IC de +0.364 a +0.393 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=380). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 2172 | +0.084 | +233.24€ | 1 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 2172 | +0.084 | +233.24€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1767 | +0.085 | +193.96€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1767 | +0.085 | +193.96€ | 1 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 284 | +0.070 | +11.30€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 284 | +0.070 | +11.30€ | 5 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 90 | +0.130 | +28.32€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 90 | +0.130 | +28.32€ | 1 | 10 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 1129 | -0.022 | +70.10€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 1129 | -0.022 | +70.10€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE | 7 | +0.019 | +3.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE#15min | 7 | +0.019 | +3.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 872 | -0.039 | +54.47€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 872 | -0.039 | +54.47€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 173 | +0.060 | +18.55€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 173 | +0.060 | +18.55€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 77 | -0.032 | -6.17€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 77 | -0.032 | -6.17€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 46993 | -0.084 | -5993.59€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 2893 | +0.069 | -297.56€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 44100 | -0.095 | -5696.03€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4792 | -0.112 | -805.61€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4792 | -0.112 | -805.61€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 2893 | +0.069 | -297.56€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 2893 | +0.069 | -297.56€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 4872 | -0.106 | -939.11€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 4872 | -0.106 | -939.11€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 12833 | -0.042 | -1182.49€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 12833 | -0.042 | -1182.49€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 12786 | -0.112 | -1322.21€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 12786 | -0.112 | -1322.21€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 8817 | -0.129 | -1446.60€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 8817 | -0.129 | -1446.60€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 48361 | -0.012 | +2863.10€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 12512 | +0.004 | +1526.79€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 35849 | -0.018 | +1336.31€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 48361 | -0.012 | +2863.10€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 12512 | +0.004 | +1526.79€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 35849 | -0.018 | +1336.31€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 186045 | +0.113 | -7746.43€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#15min | 21636 | +0.180 | -715.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 853 | +0.008 | -75.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 152932 | +0.105 | -6576.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 10624 | +0.093 | -379.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 25343 | +0.103 | -1777.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 76 | -0.179 | +10.07€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 25252 | +0.104 | -1775.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 35301 | +0.124 | -585.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5607 | +0.178 | -233.50€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 25318 | +0.120 | -176.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 4334 | +0.080 | -153.61€ | 1 | 2 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 25394 | +0.098 | -1854.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 86 | -0.114 | +7.00€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 25293 | +0.099 | -1850.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 39733 | +0.123 | -854.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 10014 | +0.178 | -252.22€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 25719 | +0.105 | -542.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 3988 | +0.103 | -50.68€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#SOL | 34903 | +0.112 | -1560.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 5765 | +0.198 | -255.09€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 756 | +0.034 | -21.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 26080 | +0.096 | -1108.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 2302 | +0.102 | -174.80€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO#XRP | 25371 | +0.107 | -1113.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 88 | -0.122 | +8.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 25270 | +0.108 | -1121.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 30136 | +0.193 | -2051.39€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 30136 | +0.193 | -2051.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 6824 | +0.171 | -687.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 6824 | +0.171 | -687.02€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 4324 | +0.199 | -149.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 4324 | +0.199 | -149.59€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 6696 | +0.176 | -580.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 6696 | +0.176 | -580.74€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 5622 | +0.251 | -199.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 5622 | +0.251 | -199.74€ | 0 | 4 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 6591 | +0.186 | -448.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 6591 | +0.186 | -448.06€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 1229 | +0.425 | -46.25€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 1229 | +0.425 | -46.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 507 | +0.439 | -4.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 507 | +0.439 | -4.72€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE#15min | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 495 | +0.423 | -19.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 495 | +0.423 | -19.29€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 213 | +0.398 | -18.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 213 | +0.398 | -18.37€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 106615 | +0.199 | -7902.82€ | 3 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 106615 | +0.199 | -7902.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 18429 | +0.179 | -2093.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 18429 | +0.179 | -2093.22€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 17189 | +0.224 | -579.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 17189 | +0.224 | -579.61€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 18306 | +0.179 | -1965.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 18306 | +0.179 | -1965.43€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 17332 | +0.218 | -699.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 17332 | +0.218 | -699.50€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 17623 | +0.203 | -1123.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 17623 | +0.203 | -1123.57€ | 1 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 17736 | +0.196 | -1441.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 17736 | +0.196 | -1441.48€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 41061 | +0.117 | +349.23€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 41061 | +0.117 | +349.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 20445 | +0.117 | +202.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 20445 | +0.117 | +202.99€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 20616 | +0.117 | +146.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 20616 | +0.117 | +146.24€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 2555 | +0.292 | -14.95€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 2555 | +0.292 | -14.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 1170 | +0.281 | -30.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 1170 | +0.281 | -30.80€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 1246 | +0.296 | +10.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 1246 | +0.296 | +10.60€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 139 | +0.344 | +5.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 139 | +0.344 | +5.25€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 1179 | +0.438 | -4.60€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 1179 | +0.438 | -4.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 564 | +0.431 | -11.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 564 | +0.431 | -11.90€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 564 | +0.445 | +6.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 564 | +0.445 | +6.04€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 51 | +0.406 | +1.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 51 | +0.406 | +1.25€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1931 | +0.068 | -86.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 725 | +0.046 | -64.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 1206 | +0.080 | -21.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1497 | +0.075 | -41.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 291 | +0.053 | -19.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 1206 | +0.080 | -21.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 83147 | +0.101 | -1962.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 6700 | +0.096 | +141.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 76447 | +0.101 | -2103.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 45454 | +0.106 | -441.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 6700 | +0.096 | +141.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 38754 | +0.107 | -582.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 17647 | +0.109 | -105.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 17647 | +0.109 | -105.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 20046 | +0.082 | -1415.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 20046 | +0.082 | -1415.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 914 | +0.186 | -109.27€ | 5 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 914 | +0.186 | -109.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 914 | +0.186 | -109.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 914 | +0.186 | -109.27€ | 5 | 4 |
| ✅ GBM_LATE_15M | 56383 | +0.099 | +31397.03€ | 0 | 18 |
| ✅ GBM_LATE_15M#15min | 56383 | +0.099 | +31397.03€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 9329 | +0.227 | +8100.59€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 9329 | +0.227 | +8100.59€ | 0 | 21 |
| ✅ GBM_LATE_15M#BTC | 8618 | +0.176 | +6763.98€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 8618 | +0.176 | +6763.98€ | 0 | 22 |
| ✅ GBM_LATE_15M#DOGE | 10115 | +0.208 | +8009.12€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 10115 | +0.208 | +8009.12€ | 0 | 21 |
| ✅ GBM_LATE_15M#ETH | 7580 | +0.054 | +2404.20€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 7580 | +0.054 | +2404.20€ | 1 | 18 |
| ✅ GBM_LATE_15M#SOL | 7874 | -0.031 | +2026.88€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 7874 | -0.031 | +2026.88€ | 4 | 15 |
| ✅ GBM_LATE_15M#XRP | 12867 | -0.023 | +4092.26€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 12867 | -0.023 | +4092.26€ | 3 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 59384 | +0.085 | +34376.25€ | 0 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 59384 | +0.085 | +34376.25€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 11483 | -0.002 | +6116.43€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 11483 | -0.002 | +6116.43€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 12769 | +0.004 | +3365.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 12769 | +0.004 | +3365.76€ | 0 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 8084 | +0.295 | +9243.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 8084 | +0.295 | +9243.87€ | 0 | 22 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 11318 | +0.013 | +3493.35€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 11318 | +0.013 | +3493.35€ | 1 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 9137 | +0.043 | +4052.30€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 9137 | +0.043 | +4052.30€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 6593 | +0.317 | +8104.53€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 6593 | +0.317 | +8104.53€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 44661 | +0.178 | +36827.25€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 44661 | +0.178 | +36827.25€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 6718 | +0.240 | +6279.78€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 6718 | +0.240 | +6279.78€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 7075 | +0.139 | +5207.10€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 7075 | +0.139 | +5207.10€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 7185 | +0.225 | +6242.26€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 7185 | +0.225 | +6242.26€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 7658 | +0.129 | +5920.65€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 7658 | +0.129 | +5920.65€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 8451 | +0.119 | +6311.41€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 8451 | +0.119 | +6311.41€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 7574 | +0.233 | +6866.05€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 7574 | +0.233 | +6866.05€ | 0 | 25 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 12111 | +0.125 | +6029.03€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 12111 | +0.125 | +6029.03€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 489 | +0.160 | +325.89€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 489 | +0.160 | +325.89€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 3400 | +0.127 | +1847.55€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 3400 | +0.127 | +1847.55€ | 0 | 13 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 505 | +0.159 | +279.48€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 505 | +0.159 | +279.48€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 3537 | +0.124 | +1675.92€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 3537 | +0.124 | +1675.92€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 3143 | +0.098 | +1256.89€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 3143 | +0.098 | +1256.89€ | 0 | 13 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 1037 | +0.167 | +643.30€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 1037 | +0.167 | +643.30€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO | 56568 | +0.188 | +46527.25€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#15min | 56568 | +0.188 | +46527.25€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 8916 | +0.252 | +8684.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 8916 | +0.252 | +8684.76€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 8991 | +0.137 | +6182.35€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 8991 | +0.137 | +6182.35€ | 0 | 26 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 9603 | +0.236 | +8718.31€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 9603 | +0.236 | +8718.31€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 9362 | +0.141 | +6917.36€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 9362 | +0.141 | +6917.36€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 10046 | +0.121 | +7052.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 10046 | +0.121 | +7052.83€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 9650 | +0.241 | +8971.66€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 9650 | +0.241 | +8971.66€ | 0 | 21 |
| ✅ GBM_LATE_5M | 14298 | +0.211 | +11625.45€ | 1 | 26 |
| ✅ GBM_LATE_5M#5min | 14298 | +0.211 | +11625.45€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 1078 | +0.247 | +1027.08€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 1078 | +0.247 | +1027.08€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 3266 | +0.211 | +2814.84€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 3266 | +0.211 | +2814.84€ | 0 | 25 |
| ✅ GBM_LATE_5M#DOGE | 1449 | +0.209 | +1152.27€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1449 | +0.209 | +1152.27€ | 0 | 18 |
| ✅ GBM_LATE_5M#ETH | 4225 | +0.202 | +3148.73€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 4225 | +0.202 | +3148.73€ | 0 | 25 |
| ✅ GBM_LATE_5M#SOL | 2302 | +0.212 | +1928.24€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 2302 | +0.212 | +1928.24€ | 0 | 25 |
| ✅ GBM_LATE_5M#XRP | 1978 | +0.210 | +1554.29€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1978 | +0.210 | +1554.29€ | 0 | 0 |
| ✅ GBM_LATE_60M | 4983 | +0.051 | +1376.00€ | 1 | 6 |
| ✅ GBM_LATE_60M#60min | 4983 | +0.051 | +1376.00€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 1730 | +0.059 | +531.36€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 1730 | +0.059 | +531.36€ | 0 | 6 |
| ✅ GBM_LATE_60M#ETH | 1603 | +0.052 | +513.94€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 1603 | +0.052 | +513.94€ | 1 | 7 |
| ✅ GBM_LATE_60M#SOL | 1650 | +0.042 | +330.71€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 1650 | +0.042 | +330.71€ | 0 | 10 |
| 🚫 GBM_LATE_60M_FADE | 708 | -0.249 | -34.26€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 708 | -0.249 | -34.26€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 258 | -0.250 | -18.00€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 258 | -0.250 | -18.00€ | 4 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 260 | -0.244 | -7.05€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 260 | -0.244 | -7.05€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 190 | -0.250 | -9.21€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 190 | -0.250 | -9.21€ | 9 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 2086 | +0.084 | +538.40€ | 0 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 2086 | +0.084 | +538.40€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 798 | +0.074 | +193.93€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 798 | +0.074 | +193.93€ | 1 | 4 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 749 | +0.058 | +145.65€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 749 | +0.058 | +145.65€ | 1 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 539 | +0.136 | +198.82€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 539 | +0.136 | +198.82€ | 1 | 9 |
| ✅ LATE_WINDOW_5MIN | 241 | +0.294 | +271.50€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 241 | +0.294 | +271.50€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 241 | +0.294 | +271.50€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 241 | +0.294 | +271.50€ | 1 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 4375 | +0.096 | +988.94€ | 0 | 1 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 4375 | +0.096 | +988.94€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 4375 | +0.096 | +988.94€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 4375 | +0.096 | +988.94€ | 0 | 1 |
| ✅ LIQUIDACIONES_15M | 1103 | -0.009 | +14.71€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 1103 | -0.009 | +14.71€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 66 | +0.000 | -1.21€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 66 | +0.000 | -1.21€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 278 | -0.011 | +6.41€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 278 | -0.011 | +6.41€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 42 | -0.091 | -4.06€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 42 | -0.091 | -4.06€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 291 | +0.019 | +18.01€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 291 | +0.019 | +18.01€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 313 | -0.014 | +1.05€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 313 | -0.014 | +1.05€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 113 | -0.039 | -5.48€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 113 | -0.039 | -5.48€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 4185 | +0.017 | +122.37€ | 5 | 1 |
| ✅ LIQUIDACIONES_5M#5min | 4185 | +0.017 | +122.37€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 211 | +0.021 | -1.84€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 211 | +0.021 | -1.84€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 826 | +0.016 | +41.72€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 826 | +0.016 | +41.72€ | 4 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 249 | +0.026 | +25.95€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 249 | +0.026 | +25.95€ | 0 | 6 |
| ✅ LIQUIDACIONES_5M#ETH | 1654 | +0.019 | +27.57€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1654 | +0.019 | +27.57€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 769 | +0.011 | +1.89€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 769 | +0.011 | +1.89€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 476 | +0.013 | +27.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 476 | +0.013 | +27.09€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 2347 | -0.031 | -4.56€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 2347 | -0.031 | -4.56€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 710 | -0.029 | -10.19€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 710 | -0.029 | -10.19€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 833 | -0.008 | +19.47€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 833 | -0.008 | +19.47€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 804 | -0.057 | -13.83€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 804 | -0.057 | -13.83€ | 5 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 15178 | -0.031 | -86.98€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 7284 | -0.032 | -59.26€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 7894 | -0.029 | -27.71€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 533 | -0.051 | -28.66€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 273 | -0.024 | +2.85€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 260 | -0.080 | -31.51€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 3968 | -0.024 | +0.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 1881 | -0.023 | +8.18€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 2087 | -0.025 | -8.08€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 1485 | -0.027 | +20.01€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 762 | -0.031 | +3.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 723 | -0.023 | +16.67€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 3431 | -0.034 | -53.53€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 1617 | -0.036 | -34.94€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 1814 | -0.032 | -18.60€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 2921 | -0.023 | +43.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 1412 | -0.026 | +9.30€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 1509 | -0.019 | +33.79€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 2840 | -0.042 | -67.98€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 1339 | -0.049 | -47.98€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 1501 | -0.035 | -20.00€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 66937 | -0.000 | +3563.51€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 66937 | -0.000 | +3563.51€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 12128 | +0.027 | +1657.40€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 12128 | +0.027 | +1657.40€ | 2 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 9363 | -0.037 | -152.33€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 9363 | -0.037 | -152.33€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 12261 | +0.025 | +1365.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 12261 | +0.025 | +1365.46€ | 1 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 9296 | -0.052 | -237.12€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 9296 | -0.052 | -237.12€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 11412 | -0.004 | +314.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 11412 | -0.004 | +314.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 12477 | +0.017 | +615.40€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 12477 | +0.017 | +615.40€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 7156 | -0.054 | -116.08€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 7156 | -0.054 | -116.08€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1246 | -0.002 | -15.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1246 | -0.002 | -15.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1985 | -0.063 | -24.58€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1985 | -0.063 | -24.58€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 77 | -0.019 | -0.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 77 | -0.019 | -0.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 808 | -0.120 | -35.47€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 808 | -0.120 | -35.47€ | 5 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 2177 | -0.068 | -12.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 2177 | -0.068 | -12.56€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 863 | -0.018 | -27.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 863 | -0.018 | -27.52€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3378 | +0.004 | -1.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3378 | +0.004 | -1.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 133 | -0.033 | -0.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 133 | -0.033 | -0.70€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 196 | +0.010 | -1.25€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 196 | +0.010 | -1.25€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 139 | -0.004 | -2.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 139 | -0.004 | -2.34€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1326 | +0.006 | +6.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1326 | +0.006 | +6.37€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1391 | +0.007 | -0.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1391 | +0.007 | -0.19€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 193 | -0.013 | -3.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 193 | -0.013 | -3.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 164038 | -0.078 | +2222.20€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 164038 | -0.078 | +2222.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 28731 | -0.078 | +1702.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 28731 | -0.078 | +1702.94€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 24521 | -0.102 | -1259.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 24521 | -0.102 | -1259.52€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 29093 | -0.069 | +1413.35€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 29093 | -0.069 | +1413.35€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 24065 | -0.099 | -755.40€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 24065 | -0.099 | -755.40€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 29316 | -0.059 | +311.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 29316 | -0.059 | +311.54€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 28312 | -0.070 | +809.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 28312 | -0.070 | +809.29€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 9049 | -0.035 | -184.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 9049 | -0.035 | -184.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 1003 | -0.016 | -18.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 1003 | -0.016 | -18.88€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 2111 | -0.047 | -28.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 2111 | -0.047 | -28.20€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2643 | -0.025 | -38.51€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2643 | -0.025 | -38.51€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1270 | -0.065 | -32.51€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1270 | -0.065 | -32.51€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 1013 | -0.032 | -34.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 1013 | -0.032 | -34.02€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 2143 | +0.119 | +843.08€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#5min | 2007 | +0.123 | +830.48€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 480 | +0.133 | +231.61€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 480 | +0.133 | +231.61€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#DOGE | 408 | +0.117 | +141.00€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 408 | +0.117 | +141.00€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#ETH | 377 | +0.125 | +169.62€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 377 | +0.125 | +169.62€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 343 | +0.141 | +175.20€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 343 | +0.141 | +175.20€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#XRP | 399 | +0.096 | +113.05€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 399 | +0.096 | +113.05€ | 0 | 2 |
| ✅ ORDER_FLOW_5M_REACTIVO | 2155 | -0.015 | -12.43€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 2155 | -0.015 | -12.43€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 397 | +0.016 | +27.88€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 397 | +0.016 | +27.88€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 397 | -0.044 | -25.17€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 397 | -0.044 | -25.17€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 544 | -0.033 | -23.83€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 544 | -0.033 | -23.83€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 436 | -0.002 | -0.56€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 436 | -0.002 | -0.56€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 381 | -0.006 | +9.24€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 381 | -0.006 | +9.24€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 1146 | -0.072 | -40.12€ | 3 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 530 | -0.107 | -77.78€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 409 | -0.120 | -57.23€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 121 | -0.061 | -20.55€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 401 | -0.031 | +27.25€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 286 | -0.017 | +35.25€ | 1 | 2 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 115 | -0.064 | -8.00€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 215 | -0.062 | +10.41€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 179 | -0.058 | +8.57€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 36 | -0.079 | +1.84€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 874 | -0.074 | -13.41€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 272 | -0.066 | -26.71€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 1446 | -0.205 | -89.25€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC | 570 | -0.203 | -49.08€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#atexpiry | 500 | -0.201 | -44.63€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#reach | 70 | -0.208 | -4.45€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 483 | -0.209 | -38.50€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 421 | -0.221 | -45.64€ | 3 | 1 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 62 | -0.125 | +7.14€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL | 393 | -0.201 | -1.66€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 363 | -0.199 | -3.81€ | 5 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 30 | -0.219 | +2.15€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 1284 | -0.208 | -94.09€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 162 | -0.183 | +4.84€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 536 | +0.377 | +504.10€ | 0 | 12 |
| ✅ RESOLUTION_SNIPER#BTC | 107 | +0.151 | +88.66€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 107 | +0.151 | +88.66€ | 0 | 5 |
| ✅ RESOLUTION_SNIPER#ETH | 123 | +0.364 | +103.53€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 123 | +0.364 | +103.53€ | 0 | 5 |
| ✅ RESOLUTION_SNIPER#SOL | 306 | +0.458 | +311.91€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 306 | +0.458 | +311.91€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#sniper | 536 | +0.377 | +504.10€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 935 | +0.042 | +81.90€ | 2 | 2 |
| ✅ STREAK_FADE_15M#15min | 935 | +0.042 | +81.90€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 355 | +0.021 | +4.48€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 355 | +0.021 | +4.48€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 73 | +0.020 | +1.57€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 73 | +0.020 | +1.57€ | 1 | 1 |
| ✅ STREAK_FADE_15M#SOL | 83 | +0.018 | +6.06€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 83 | +0.018 | +6.06€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 424 | +0.068 | +69.79€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 424 | +0.068 | +69.79€ | 1 | 4 |
| ✅ STREAK_FADE_5M | 3570 | -0.023 | -143.07€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3570 | -0.023 | -143.07€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 1127 | -0.023 | -40.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 1127 | -0.023 | -40.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 612 | -0.029 | -27.74€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 612 | -0.029 | -27.74€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 171 | -0.043 | -14.80€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 171 | -0.043 | -14.80€ | 4 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1660 | -0.019 | -60.32€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1660 | -0.019 | -60.32€ | 2 | 0 |
| ✅ STREAK_FADE_60M | 118 | -0.050 | -12.20€ | 5 | 0 |
| ✅ STREAK_FADE_60M#60min | 118 | -0.050 | -12.20€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 44 | -0.087 | -4.62€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 44 | -0.087 | -4.62€ | 4 | 0 |
| ✅ STREAK_FADE_60M#SOL | 74 | -0.026 | -7.58€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 74 | -0.026 | -7.58€ | 0 | 1 |
| ✅ STREAK_MOM_5M | 11504 | +0.014 | +73.23€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 11504 | +0.014 | +73.23€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2995 | +0.018 | +24.38€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2995 | +0.018 | +24.38€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 3006 | +0.017 | +34.36€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 3006 | +0.017 | +34.36€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2922 | +0.008 | -3.73€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2922 | +0.008 | -3.73€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2581 | +0.014 | +18.23€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2581 | +0.014 | +18.23€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 11864 | +0.018 | -8.94€ | 4 | 0 |
| ✅ STRUCT_NO_15M#15min | 11864 | +0.018 | -8.94€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 4934 | +0.021 | +4.95€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 4934 | +0.021 | +4.95€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 4074 | +0.016 | -11.37€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 4074 | +0.016 | -11.37€ | 4 | 0 |
| ✅ STRUCT_NO_15M#SOL | 2856 | +0.014 | -2.52€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 2856 | +0.014 | -2.52€ | 1 | 0 |
| ✅ UPDOWN_GBM | 105393 | +0.060 | +10067.74€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 25693 | +0.079 | +5223.92€ | 0 | 10 |
| ✅ UPDOWN_GBM#240min | 3132 | +0.000 | +35.16€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 69966 | +0.062 | +4697.90€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 6242 | -0.001 | +115.71€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 8660 | +0.105 | +1601.50€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1781 | +0.164 | +820.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 90 | -0.011 | -2.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 6789 | +0.091 | +783.30€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 24068 | +0.057 | +2125.29€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 3442 | +0.078 | +767.01€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 891 | +0.001 | +18.29€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 16813 | +0.067 | +1262.25€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 2791 | -0.004 | +73.60€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 131 | -0.064 | +4.14€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 11459 | +0.079 | +1324.01€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1761 | +0.154 | +738.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 86 | +0.023 | -0.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 9612 | +0.066 | +586.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 25068 | +0.050 | +1755.48€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 6066 | +0.071 | +925.40€ | 0 | 9 |
| ✅ UPDOWN_GBM#ETH#240min | 860 | +0.005 | +16.23€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 15728 | +0.052 | +776.42€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 2294 | +0.001 | +36.23€ | 1 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 120 | -0.107 | +1.20€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 22446 | +0.040 | +1274.01€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 6867 | +0.032 | +431.20€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#240min | 808 | -0.010 | +5.12€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 13507 | +0.051 | +840.26€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 1157 | +0.002 | +5.88€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#daily | 107 | -0.142 | -8.45€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 13690 | +0.073 | +1989.29€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 5776 | +0.095 | +1541.69€ | 0 | 10 |
| ✅ UPDOWN_GBM#XRP#240min | 397 | +0.006 | -1.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 7517 | +0.061 | +449.23€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 358 | -0.103 | -3.11€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 995 | +0.364 | +363.53€ | 0 | 10 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 995 | +0.364 | +363.53€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 489 | +0.361 | +170.29€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 489 | +0.361 | +170.29€ | 0 | 9 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 506 | +0.364 | +193.24€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 506 | +0.364 | +193.24€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO | 25198 | -0.021 | +6208.03€ | 3 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 25198 | -0.021 | +6208.03€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1981 | -0.051 | +561.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1981 | -0.051 | +561.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 4696 | -0.116 | +221.41€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 4696 | -0.116 | +221.41€ | 3 | 11 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 1071 | +0.222 | +899.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 1071 | +0.222 | +899.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 3303 | +0.219 | +2111.27€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 3303 | +0.219 | +2111.27€ | 1 | 19 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 7144 | -0.061 | +1050.35€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 7144 | -0.061 | +1050.35€ | 4 | 8 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 7003 | -0.061 | +1363.95€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 7003 | -0.061 | +1363.95€ | 2 | 5 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 309 | +0.059 | +27.08€ | 0 | 10 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 309 | +0.059 | +27.08€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 309 | +0.059 | +27.08€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 309 | +0.059 | +27.08€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1786 | +0.283 | +1494.60€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1786 | +0.283 | +1494.60€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 945 | +0.275 | +736.93€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 945 | +0.275 | +736.93€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 841 | +0.291 | +757.67€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 841 | +0.291 | +757.67€ | 0 | 9 |
| ✅ UPDOWN_OU_5M | 865 | -0.114 | -86.28€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 865 | -0.114 | -86.28€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 273 | -0.082 | -20.87€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 273 | -0.082 | -20.87€ | 1 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 97 | -0.177 | -11.96€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 97 | -0.177 | -11.96€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 112 | -0.175 | -4.10€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 112 | -0.175 | -4.10€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 38 | -0.175 | -6.61€ | 2 | 0 |
| ✅ WEEKLY_PRICE | 4651 | +0.300 | +2096.35€ | 0 | 3 |
| ✅ WEEKLY_PRICE#BTC | 1776 | +0.256 | +221.13€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 1792 | +0.295 | +762.27€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 1083 | +0.381 | +1112.94€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**✅ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: n≥15 y IC<-0.05
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: IC=+0.022 n=1294 — no justifica filtro, seguir monitorizando
  - _Datos_: n=1294 IC=+0.022 PNL=+63.34€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 813 celda(s) pasan gate riguroso completo de 2895 evaluadas (n>=40) y 4010 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.032 < 0.08 — monitorear
  - _Datos_: n=6865 IC=+0.032 PNL=+431.22€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=1792/15 IC=+0.295 PNL=+762.27€ | BTC: n=1776/15 IC=+0.256 PNL=+221.13€ | SOL: n=1083/15 IC=+0.381 PNL=+1112.94€

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
  - _Estado_: alineada_con_outcome_prev IC=+0.140 n=1054/60 | contraria IC=+0.184 n=1110 | gap=-0.044 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=587, boost estimado=+0.012. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 0/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=2294/40 IC=+0.001 PNL=+36.23€ | BTC#60min: n=2791/40 IC=-0.004 PNL=+73.60€ | SOL#60min: n=1157/40 IC=+0.002 PNL=+5.88€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.045 n=723647 | tras_1loss IC=+0.100 n=548921 | tras_2loss IC=+0.070 n=219711/40 | gap=-0.025 (umbral 0.05)

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.164 > 0.08 con n=1048 PNL=+645.27€
  - _Datos_: n=1048 IC=+0.164 PNL=+645.27€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.136 > 0.08 con n=1235 PNL=+598.01€
  - _Datos_: n=1235 IC=+0.136 PNL=+598.01€

**🟡 H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: n≥25 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.140 > 0.08 con n=84 PNL=+37.51€
  - _Datos_: n=84 IC=+0.140 PNL=+37.51€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.333 > 0.1 con n=3788 PNL=+2087.18€
  - _Datos_: n=3788 IC=+0.333 PNL=+2087.18€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=1057 IC=+0.066 PNL=+103.66€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1057 IC=+0.066 PNL=+103.66€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=106 IC=+0.167 PNL=+64.18€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=106 IC=+0.167 PNL=+64.18€

**⏳ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: 30
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-OF-02H-BTCSOL** — ORDER_FLOW H=02h UTC — BTC+SOL solamente (revisar blacklist)
  - _Hipótesis_: La hora 02h está en el blacklist basado en TODOS los pares. Con BTC+SOL solo, el historial muestra 4/5 (80%) IC=+0.054. ¿Se confirma la señal positiva con más datos?
  - _Umbral_: 15
  - _Acción_: Si IC>0.05 con n≥20 → proponer eliminar 02h del blacklist ORDER_FLOW
  - _Estado_: 6/15 ops en el filtro definido (IC actual=+0.075 PNL=+7.10€)
  - _Datos_: n=6 IC=+0.075 PNL=+7.10€

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
  - _Estado_: n=4173 IC=+0.001 PNL=-20.49€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=4173 IC=+0.001 PNL=-20.49€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=2069 IC=-0.004 PNL=+136.20€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=2069 IC=-0.004 PNL=+136.20€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=1294 IC=+0.022 PNL=+63.34€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=1294 IC=+0.022 PNL=+63.34€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.143 > 0.1 con n=7037 PNL=+3576.67€
  - _Datos_: n=7037 IC=+0.143 PNL=+3576.67€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=3440 IC=+0.078 PNL=+767.04€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=3440 IC=+0.078 PNL=+767.04€

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
  - _Estado_: n=1369 IC=+0.038 PNL=+107.98€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=1369 IC=+0.038 PNL=+107.98€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=175 IC=-0.031 PNL=-6.20€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=175 IC=-0.031 PNL=-6.20€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.294 n=241) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=241 IC=+0.294 PNL=+271.50€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.117 > 0.02 con n=1255 PNL=+495.84€
  - _Datos_: n=1255 IC=+0.117 PNL=+495.84€

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
  - _Estado_: n=43264 IC=+0.073 PNL=+6011.86€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=43264 IC=+0.073 PNL=+6011.86€

**⏳ H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: 120
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: 0/120 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.139 < -0.1 con n=749 PNL=+99.16€
  - _Datos_: n=749 IC=-0.139 PNL=+99.16€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=4025 IC=+0.068 PNL=+515.69€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=4025 IC=+0.068 PNL=+515.69€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=184 IC=-0.102 PNL=-0.48€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=184 IC=-0.102 PNL=-0.48€

**〰️ H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: n=1093 IC=+0.099 PNL=+270.65€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=1093 IC=+0.099 PNL=+270.65€

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
  - _Estado_: n=42899 IC=-0.137 PNL=+2733.14€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=42899 IC=-0.137 PNL=+2733.14€

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
  - _Estado_: n=4450 IC=+0.129 PNL=+2915.49€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=4450 IC=+0.129 PNL=+2915.49€

**⏳ H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: 40
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=10924 IC=+0.058 PNL=+952.90€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=10924 IC=+0.058 PNL=+952.90€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.103 > 0.08 con n=4618 PNL=+2621.63€
  - _Datos_: n=4618 IC=+0.103 PNL=+2621.63€

**⏳ H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: 80
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: 0/80 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.220 < -0.1 con n=4687 PNL=-394.90€
  - _Datos_: n=4687 IC=-0.220 PNL=-394.90€

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
  - _Estado_: n=104 IC=+0.047 PNL=+17.67€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=104 IC=+0.047 PNL=+17.67€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.094 n=2221) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=2221 IC=+0.094 PNL=+438.02€

**⏳ H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.414 n=681) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=681 IC=+0.414 PNL=+992.85€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=18419 IC=+0.179 PNL=-2091.33€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=18419 IC=+0.179 PNL=-2091.33€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.233 > 0.1 con n=286 PNL=+201.05€
  - _Datos_: n=286 IC=+0.233 PNL=+201.05€
