# Hipótesis automáticas — 2026-11-11 19:35 UTC
_Generado por shadow_postmortem.py sobre 1292672 resoluciones (PNL=+177148.13€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.5` → IC=-0.317 (n=195)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=698)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.196 (n=1023)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` > 0.505 (IC base=+0.127)

- **PATRÓN** `n_total_lado` > `62.0` → IC=+0.187 (n=324)

  - _Acción_: Kelly boost +0.94€ cuando `n_total_lado` > 62.0 (IC base=+0.127)

- **PATRÓN** `banda_hit_calibrado` > `0.8129` → IC=+0.273 (n=438)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8129 (IC base=+0.127)

- **PATRÓN** `banda_z` > `8.555` → IC=+0.197 (n=321)

  - _Acción_: Kelly boost +0.98€ cuando `banda_z` > 8.555 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.143 (n=359)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 17.0 (IC base=+0.127)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.129 (n=690)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 12.0 (IC base=+0.127)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.141 (n=1049)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.127)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.302 (n=165)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.113 (n=497)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.193 (n=888)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.505 (IC base=+0.130)

- **PATRÓN** `n_total_lado` > `66.0` → IC=+0.188 (n=277)

  - _Acción_: Kelly boost +0.94€ cuando `n_total_lado` > 66.0 (IC base=+0.130)

- **PATRÓN** `banda_hit_calibrado` > `0.8126` → IC=+0.274 (n=378)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8126 (IC base=+0.130)

- **PATRÓN** `banda_z` > `8.854` → IC=+0.210 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 8.854 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.138 (n=753)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 8.0 (IC base=+0.130)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.131 (n=588)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 12.0 (IC base=+0.130)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.137 (n=949)

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
- **FILTRO** `restante_s_al_confirmar` < `132.48` → IC=-0.220 (n=11857)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 132.48
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=35576)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `125.13` → IC=-0.258 (n=1202)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 125.13
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=3609)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `116.46` → IC=-0.287 (n=1219)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 116.46
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=3658)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `restante_s_al_confirmar` < `117.21` → IC=-0.164 (n=3250)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 117.21
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=9750)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `152.07` → IC=-0.242 (n=3234)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 152.07
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=9702)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `129.04` → IC=-0.263 (n=2216)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 129.04
  - _Potencial_: sin este filtro IC_bueno=-0.084 (n=6648)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.210 (n=27785)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.104)

- **PATRÓN** `libro_liquidez` > `8289.2002` → IC=+0.158 (n=2328)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 8289.2002 (IC base=+0.104)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.128 (n=23927)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 17.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.130 (n=29019)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.124)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.225 (n=21899)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.140 (n=8310)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `6518.7605` → IC=+0.143 (n=3211)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 6518.7605 (IC base=+0.124)

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

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.185 (n=1909)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 7.0 (IC base=+0.178)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.181 (n=2136)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 17.0 (IC base=+0.178)

- **PATRÓN** `py_entrada` < `0.295` → IC=+0.312 (n=981)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.295 (IC base=+0.178)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.181 (n=2736)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.01 (IC base=+0.178)

- **PATRÓN** `libro_liquidez` > `16075.8828` → IC=+0.184 (n=706)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 16075.8828 (IC base=+0.178)

### FAVORITO_CONFIRMADO#BTC#60min
- **FILTRO** `py_entrada` < `0.55` → IC=-0.335 (n=95)

  - _Acción_: SKIP cuando `py_entrada` < 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.095 (n=2209)

- **PATRÓN** `py_entrada` > `0.61` → IC=+0.167 (n=607)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` > 0.61 (IC base=+0.077)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.145 (n=1419)

  - _Acción_: Kelly boost +0.72€ cuando `py_entrada` < 0.44 (IC base=+0.082)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.169 (n=5032)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 6.0 (IC base=+0.166)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.170 (n=4481)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 15.0 (IC base=+0.166)

- **PATRÓN** `py_entrada` > `0.77` → IC=+0.375 (n=1741)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.77 (IC base=+0.166)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.209 (n=2398)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.201)

- **PATRÓN** `py_entrada` < `0.275` → IC=+0.331 (n=950)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.275 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.205 (n=2793)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.201)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.144 (n=644)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 15.0 (IC base=+0.142)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.147 (n=1158)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 15.0 (IC base=+0.142)

- **PATRÓN** `py_entrada` > `0.675` → IC=+0.254 (n=441)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.675 (IC base=+0.142)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.145 (n=1103)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.01 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.156 (n=155)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.072)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.252 (n=944)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.227)

- **PATRÓN** `py_entrada` > `0.83` → IC=+0.420 (n=1319)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.83 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.145 (n=1422)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 7.0 (IC base=+0.144)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.154 (n=729)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 7.0 (IC base=+0.144)

- **PATRÓN** `py_entrada` < `0.345` → IC=+0.278 (n=717)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.345 (IC base=+0.144)

### FAVORITO_CONFIRMADO#SOL#60min
- **FILTRO** `libro_liquidez` < `952.1685` → IC=-0.125 (n=158)

  - _Acción_: SKIP cuando `libro_liquidez` < 952.1685
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=322)

- **PATRÓN** `py_entrada` > `0.55` → IC=+0.163 (n=461)

  - _Acción_: Kelly boost +0.82€ cuando `py_entrada` > 0.55 (IC base=+0.045)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.145 (n=474)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 17.0 (IC base=+0.120)

- **PATRÓN** `py_entrada` < `0.33` → IC=+0.236 (n=457)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.33 (IC base=+0.120)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `10.0` → IC=-0.297 (n=72)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.232 (n=151)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.201 (n=23988)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.198 (n=20262)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 15.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` > `0.735` → IC=+0.230 (n=7590)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.735 (IC base=+0.196)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.338 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.196)

- **PATRÓN** `libro_liquidez` > `4915.142` → IC=+0.338 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4915.142 (IC base=+0.196)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.174 (n=5471)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 5.0 (IC base=+0.170)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.170 (n=5459)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 18.0 (IC base=+0.170)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.181 (n=5454)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` < 0.74 (IC base=+0.170)

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

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.213 (n=3248)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.209)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.214 (n=2153)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.209)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.251 (n=1615)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.209)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.184 (n=5350)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.179 (n=4537)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 15.0 (IC base=+0.177)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.178 (n=5500)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` < 0.73 (IC base=+0.177)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.185 (n=4188)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` > 0.71 (IC base=+0.177)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.257 (n=4504)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.251)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.251 (n=3811)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.251)

- **PATRÓN** `py_entrada` > `0.8` → IC=+0.364 (n=1444)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.190 (n=5248)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.186)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.191 (n=4444)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 15.0 (IC base=+0.186)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.196 (n=1760)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` > 0.73 (IC base=+0.186)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.429 (n=966)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.425)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.427 (n=958)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.425)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.438 (n=976)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.425)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.431 (n=1028)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.425)

- **PATRÓN** `libro_liquidez` > `4621.8886` → IC=+0.442 (n=622)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4621.8886 (IC base=+0.425)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.439 (n=392)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.440)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.443 (n=401)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.440)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.449 (n=431)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.440)

- **PATRÓN** `libro_liquidez` > `12447.5813` → IC=+0.445 (n=346)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12447.5813 (IC base=+0.440)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.429 (n=381)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.422)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.426 (n=378)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.422)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.433 (n=385)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.422)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.428 (n=428)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.422)

- **PATRÓN** `libro_liquidez` > `4792.7768` → IC=+0.422 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4792.7768 (IC base=+0.422)

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

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.205 (n=31371)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.240 (n=31683)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.200)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.188 (n=4679)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 18.0 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.180 (n=10040)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 12.0 (IC base=+0.179)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.189 (n=14417)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.71 (IC base=+0.179)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.229 (n=6513)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.225)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.286 (n=4446)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.225)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.182 (n=13177)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 7.0 (IC base=+0.179)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.197 (n=11138)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` > 0.72 (IC base=+0.179)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.835` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.835
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.228 (n=4389)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.219)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.221 (n=5029)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.219)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.254 (n=7291)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.219)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **FILTRO** `hora_utc` > `3.0` → IC=-0.278 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.206 (n=11974)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.204)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.256 (n=4581)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.204)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.202 (n=5213)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.199 (n=5195)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 6.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.240 (n=6587)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.196)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.194 (n=11318)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.141 (n=11897)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `3.43` → IC=+0.139 (n=13766)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 3.43 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.195 (n=5518)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.118)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.145 (n=5366)

  - _Acción_: Kelly boost +0.72€ cuando `restante_min` > 4.96 (IC base=+0.118)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.126 (n=6898)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 7.0 (IC base=+0.118)

- **PATRÓN** `lag_apertura_s` < `4.15` → IC=+0.141 (n=6847)

  - _Acción_: Kelly boost +0.71€ cuando `lag_apertura_s` < 4.15 (IC base=+0.118)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.193 (n=5800)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.138 (n=7255)

  - _Acción_: Kelly boost +0.69€ cuando `restante_min` > 4.95 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `3.12` → IC=+0.138 (n=6914)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 3.12 (IC base=+0.116)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.308 (n=1391)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.294)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.388 (n=715)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.294)

- **PATRÓN** `libro_liquidez` > `3976.0278` → IC=+0.295 (n=880)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3976.0278 (IC base=+0.294)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.287 (n=934)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.283)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.365 (n=309)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.283)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.320 (n=675)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.299)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.302 (n=989)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.299)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.397 (n=339)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.299)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.443 (n=947)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.439)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.444 (n=914)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.439)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.437 (n=445)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.432)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.435 (n=308)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.432)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.437 (n=459)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.432)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.460 (n=149)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.446)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.446 (n=384)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.446)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.448 (n=419)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.446)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.445 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.446)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4788` → IC=+0.140 (n=17774)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.4788 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.127 (n=17986)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 6.0 (IC base=+0.123)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.126 (n=12370)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 12.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` > `0.977` → IC=+0.246 (n=5927)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.977 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` > `0.7975` → IC=+0.285 (n=978)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7975 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.488` → IC=+0.186 (n=8896)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 3.488 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` > `0.6258` → IC=+0.265 (n=5328)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6258 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` > `0.3045` → IC=+0.251 (n=1836)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3045 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` > `2.7521` → IC=+0.235 (n=4261)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7521 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.135 (n=8811)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `4652.9231` → IC=+0.149 (n=5925)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 4652.9231 (IC base=+0.123)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.122 (n=11101)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0062 (IC base=+0.083)

- **PATRÓN** `ibs_20min` < `0.5652` → IC=+0.144 (n=22209)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.5652 (IC base=+0.083)

- **PATRÓN** `dist_vwap_pct` > `0.6168` → IC=+0.191 (n=1472)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.6168 (IC base=+0.083)

- **PATRÓN** `volumen_regimen` < `0.697` → IC=+0.199 (n=4000)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.697 (IC base=+0.083)

- **PATRÓN** `volumen_pendiente_norm` > `0.2966` → IC=+0.234 (n=2231)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2966 (IC base=+0.083)

- **PATRÓN** `volumen_spike_ratio` > `2.6742` → IC=+0.212 (n=5139)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6742 (IC base=+0.083)

- **PATRÓN** `ballena_activa_n` < `99.0` → IC=+0.229 (n=15322)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 99.0 (IC base=+0.083)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `drift_60min` |x|≤ `0.3654` → IC=+0.213 (n=3787)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3654 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.227 (n=1841)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.211)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.212 (n=2537)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` > `0.9859` → IC=+0.278 (n=1717)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9859 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.45` → IC=+0.279 (n=1686)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.45 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.2333` → IC=+0.259 (n=674)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2333 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `1.4363` → IC=+0.213 (n=3630)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4363 (IC base=+0.211)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.224 (n=4180)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `2038.52` → IC=+0.213 (n=1262)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2038.52 (IC base=+0.211)

- **PATRÓN** `ballena_activa_n` < `26.0` → IC=+0.224 (n=3442)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 26.0 (IC base=+0.211)

- **PATRÓN** `sigma_h` > `0.0093` → IC=+0.245 (n=1514)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0093 (IC base=+0.243)

- **PATRÓN** `drift_60min` |x|≤ `0.0891` → IC=+0.282 (n=1112)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0891 (IC base=+0.243)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.251 (n=1243)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.243)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.249 (n=1531)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.243)

- **PATRÓN** `ibs_20min` < `0.5657` → IC=+0.260 (n=3333)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5657 (IC base=+0.243)

- **PATRÓN** `volumen_pendiente_norm` < `0.0952` → IC=+0.246 (n=3020)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0952 (IC base=+0.243)

- **PATRÓN** `volumen_pendiente_norm` > `0.2902` → IC=+0.253 (n=447)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2902 (IC base=+0.243)

- **PATRÓN** `volumen_spike_ratio` < `1.4472` → IC=+0.246 (n=1061)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4472 (IC base=+0.243)

- **PATRÓN** `volumen_spike_ratio` > `1.8593` → IC=+0.247 (n=2120)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8593 (IC base=+0.243)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.245 (n=3838)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.243)

- **PATRÓN** `libro_liquidez` > `1775.22` → IC=+0.250 (n=2221)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1775.22 (IC base=+0.243)

- **PATRÓN** `ballena_activa_n` < `6.0` → IC=+0.245 (n=1131)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 6.0 (IC base=+0.243)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.232 (n=2129)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.224)

- **PATRÓN** `drift_60min` |x|≤ `0.1096` → IC=+0.254 (n=1403)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1096 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.235 (n=3339)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.227 (n=2261)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` > `0.9028` → IC=+0.257 (n=1062)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9028 (IC base=+0.224)

- **PATRÓN** `dist_vwap_pct` > `0.1851` → IC=+0.235 (n=1445)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1851 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.802` → IC=+0.264 (n=468)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.802 (IC base=+0.224)

- **PATRÓN** `volumen_regimen` > `0.6287` → IC=+0.231 (n=3185)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6287 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` > `0.2788` → IC=+0.269 (n=443)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2788 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` > `2.4482` → IC=+0.249 (n=1048)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4482 (IC base=+0.224)

- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.152 (n=3405)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0064 (IC base=+0.130)

- **PATRÓN** `drift_60min` |x|≤ `0.0775` → IC=+0.154 (n=1137)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.0775 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.152 (n=1270)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 17.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` < `0.707` → IC=+0.170 (n=3405)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.707 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.97` → IC=+0.138 (n=3110)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 3.97 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` < `0.6343` → IC=+0.154 (n=1136)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.6343 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` > `0.0717` → IC=+0.156 (n=1394)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` > 0.0717 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` < `2.442` → IC=+0.141 (n=3278)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 2.442 (IC base=+0.130)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.130 (n=4421)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.01 (IC base=+0.130)

- **PATRÓN** `ballena_activa_n` < `176.0` → IC=+0.182 (n=1081)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 176.0 (IC base=+0.130)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0114` → IC=+0.214 (n=1820)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0114 (IC base=+0.196)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.204 (n=4208)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.196)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.262 (n=1557)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.196)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.004` → IC=+0.281 (n=878)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.004 (IC base=+0.196)

- **PATRÓN** `volumen_pendiente_norm` < `0.0974` → IC=+0.198 (n=3588)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` < 0.0974 (IC base=+0.196)

- **PATRÓN** `volumen_pendiente_norm` > `0.3525` → IC=+0.228 (n=517)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3525 (IC base=+0.196)

- **PATRÓN** `volumen_spike_ratio` > `2.7293` → IC=+0.213 (n=1774)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7293 (IC base=+0.196)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.201 (n=4842)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.196)

- **PATRÓN** `libro_liquidez` > `1910.6984` → IC=+0.202 (n=1816)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1910.6984 (IC base=+0.196)

- **PATRÓN** `sigma_h` < `0.0111` → IC=+0.225 (n=3256)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0111 (IC base=+0.221)

- **PATRÓN** `drift_60min` |x|≤ `0.292` → IC=+0.234 (n=2467)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.292 (IC base=+0.221)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.241 (n=1405)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.221)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.226 (n=1676)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.221)

- **PATRÓN** `ibs_20min` < `0.0476` → IC=+0.269 (n=1238)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0476 (IC base=+0.221)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.791` → IC=+0.262 (n=401)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.791 (IC base=+0.221)

- **PATRÓN** `volumen_pendiente_norm` > `0.3484` → IC=+0.258 (n=536)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3484 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` < `1.7663` → IC=+0.219 (n=1567)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7663 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` > `2.1588` → IC=+0.229 (n=2373)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1588 (IC base=+0.221)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.223 (n=1884)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.221)

- **PATRÓN** `libro_liquidez` > `1891.307` → IC=+0.226 (n=1678)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1891.307 (IC base=+0.221)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.225 (n=3512)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 24.0 (IC base=+0.221)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.176 (n=211)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.063 (n=4818)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.150 (n=666)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0039 (IC base=+0.060)

- **PATRÓN** `ibs_20min` > `0.9416` → IC=+0.232 (n=663)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9416 (IC base=+0.060)

- **PATRÓN** `dist_vwap_pct` > `0.14` → IC=+0.340 (n=461)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.14 (IC base=+0.060)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.087` → IC=+0.203 (n=1454)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.087 (IC base=+0.060)

- **PATRÓN** `volumen_regimen` > `1.0993` → IC=+0.350 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0993 (IC base=+0.060)

- **PATRÓN** `volumen_pendiente_norm` < `0.1682` → IC=+0.336 (n=640)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1682 (IC base=+0.060)

- **PATRÓN** `volumen_pendiente_norm` > `0.3064` → IC=+0.336 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3064 (IC base=+0.060)

- **PATRÓN** `volumen_spike_ratio` < `1.5415` → IC=+0.347 (n=339)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5415 (IC base=+0.060)

- **PATRÓN** `volumen_spike_ratio` > `2.2887` → IC=+0.338 (n=350)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2887 (IC base=+0.060)

- **PATRÓN** `ballena_activa_n` < `142.0` → IC=+0.338 (n=784)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 142.0 (IC base=+0.060)

- **PATRÓN** `ibs_20min` < `0.0868` → IC=+0.189 (n=1258)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.0868 (IC base=+0.053)

- **PATRÓN** `dist_vwap_pct` > `0.337` → IC=+0.163 (n=609)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 0.337 (IC base=+0.053)

- **PATRÓN** `volumen_regimen` < `0.833` → IC=+0.165 (n=1607)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.833 (IC base=+0.053)

- **PATRÓN** `volumen_pendiente_norm` > `0.2804` → IC=+0.212 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2804 (IC base=+0.053)

- **PATRÓN** `volumen_spike_ratio` < `1.7674` → IC=+0.157 (n=1547)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.7674 (IC base=+0.053)

- **PATRÓN** `volumen_spike_ratio` > `1.5087` → IC=+0.160 (n=2072)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.5087 (IC base=+0.053)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.176 (n=146)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=768)

- **FILTRO** `ibs_20min` < `0.2615` → IC=-0.178 (n=228)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2615
  - _Potencial_: sin este filtro IC_bueno=+0.081 (n=686)

- **FILTRO** `ibs_20min` > `0.2` → IC=-0.132 (n=4734)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2
  - _Potencial_: sin este filtro IC_bueno=+0.154 (n=2353)

- **FILTRO** `sigma_ewma_delta_pct` > `8.309` → IC=-0.228 (n=763)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.309
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=6324)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.179 (n=313)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.75 (IC base=+0.016)

- **PATRÓN** `dist_vwap_pct` > `0.9754` → IC=+0.278 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9754 (IC base=+0.016)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.917` → IC=+0.154 (n=215)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 4.917 (IC base=+0.016)

- **PATRÓN** `volumen_regimen` > `0.624` → IC=+0.285 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.624 (IC base=+0.016)

- **PATRÓN** `volumen_pendiente_norm` < `0.0797` → IC=+0.279 (n=270)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0797 (IC base=+0.016)

- **PATRÓN** `volumen_spike_ratio` < `2.1931` → IC=+0.286 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1931 (IC base=+0.016)

- **PATRÓN** `volumen_spike_ratio` > `1.4523` → IC=+0.264 (n=273)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4523 (IC base=+0.016)

- **PATRÓN** `ballena_activa_n` < `41.0` → IC=+0.269 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 41.0 (IC base=+0.016)

- **PATRÓN** `ibs_20min` < `0.2` → IC=+0.154 (n=2353)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.2 (IC base=-0.037)

- **PATRÓN** `dist_vwap_pct` > `0.223` → IC=+0.286 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.223 (IC base=-0.037)

- **PATRÓN** `volumen_regimen` < `0.7052` → IC=+0.303 (n=460)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7052 (IC base=-0.037)

- **PATRÓN** `volumen_pendiente_norm` > `0.08` → IC=+0.305 (n=470)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.08 (IC base=-0.037)

- **PATRÓN** `volumen_spike_ratio` < `2.4729` → IC=+0.299 (n=976)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4729 (IC base=-0.037)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `ibs_20min` < `0.7874` → IC=-0.156 (n=3629)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7874
  - _Potencial_: sin este filtro IC_bueno=+0.131 (n=1871)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.172 (n=1179)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=4321)

- **FILTRO** `ibs_20min` > `0.7385` → IC=-0.191 (n=1899)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7385
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=5698)

- **PATRÓN** `ibs_20min` > `0.7874` → IC=+0.131 (n=1871)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` > 0.7874 (IC base=-0.058)

- **PATRÓN** `dist_vwap_pct` > `1.0296` → IC=+0.354 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0296 (IC base=-0.058)

- **PATRÓN** `dist_vwap_pct` < `0.2507` → IC=+0.299 (n=968)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2507 (IC base=-0.058)

- **PATRÓN** `volumen_regimen` > `0.704` → IC=+0.318 (n=960)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.704 (IC base=-0.058)

- **PATRÓN** `volumen_pendiente_norm` < `0.1074` → IC=+0.301 (n=1020)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1074 (IC base=-0.058)

- **PATRÓN** `volumen_pendiente_norm` > `0.1715` → IC=+0.301 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1715 (IC base=-0.058)

- **PATRÓN** `volumen_spike_ratio` < `1.5853` → IC=+0.306 (n=463)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5853 (IC base=-0.058)

- **PATRÓN** `volumen_spike_ratio` > `2.5237` → IC=+0.321 (n=350)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5237 (IC base=-0.058)

- **PATRÓN** `dist_vwap_pct` > `0.8133` → IC=+0.275 (n=367)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8133 (IC base=+0.004)

- **PATRÓN** `volumen_regimen` < `0.6418` → IC=+0.274 (n=744)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6418 (IC base=+0.004)

- **PATRÓN** `volumen_regimen` > `1.0669` → IC=+0.285 (n=1011)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0669 (IC base=+0.004)

- **PATRÓN** `volumen_pendiente_norm` > `0.1694` → IC=+0.285 (n=594)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1694 (IC base=+0.004)

- **PATRÓN** `volumen_spike_ratio` < `2.1776` → IC=+0.265 (n=1852)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1776 (IC base=+0.004)

- **PATRÓN** `volumen_spike_ratio` > `1.4393` → IC=+0.270 (n=2104)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4393 (IC base=+0.004)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.196 (n=7706)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` > 0.0107 (IC base=+0.087)

- **PATRÓN** `ibs_20min` > `0.9695` → IC=+0.312 (n=7690)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9695 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` > `0.9348` → IC=+0.302 (n=1616)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9348 (IC base=+0.087)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.474` → IC=+0.169 (n=10347)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 3.474 (IC base=+0.087)

- **PATRÓN** `volumen_regimen` > `0.693` → IC=+0.278 (n=7599)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.693 (IC base=+0.087)

- **PATRÓN** `volumen_pendiente_norm` > `0.294` → IC=+0.294 (n=1920)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.294 (IC base=+0.087)

- **PATRÓN** `volumen_spike_ratio` > `2.6525` → IC=+0.286 (n=4465)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6525 (IC base=+0.087)

- **PATRÓN** `ballena_activa_n` < `90.0` → IC=+0.309 (n=13041)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 90.0 (IC base=+0.087)

- **PATRÓN** `sigma_h` > `0.0102` → IC=+0.156 (n=7430)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0102 (IC base=+0.082)

- **PATRÓN** `ibs_20min` < `0.5207` → IC=+0.171 (n=19593)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.5207 (IC base=+0.082)

- **PATRÓN** `volumen_regimen` < `0.6989` → IC=+0.282 (n=3250)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6989 (IC base=+0.082)

- **PATRÓN** `volumen_regimen` > `1.1874` → IC=+0.280 (n=2462)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1874 (IC base=+0.082)

- **PATRÓN** `volumen_pendiente_norm` > `0.2942` → IC=+0.328 (n=1645)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2942 (IC base=+0.082)

- **PATRÓN** `volumen_spike_ratio` < `1.4529` → IC=+0.305 (n=3633)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4529 (IC base=+0.082)

- **PATRÓN** `volumen_spike_ratio` > `2.2756` → IC=+0.302 (n=4940)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2756 (IC base=+0.082)

- **PATRÓN** `ballena_activa_n` < `72.0` → IC=+0.311 (n=10872)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 72.0 (IC base=+0.082)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.8028` → IC=-0.133 (n=4097)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8028
  - _Potencial_: sin este filtro IC_bueno=+0.302 (n=2112)

- **FILTRO** `ibs_20min` > `0.7153` → IC=-0.235 (n=1368)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7153
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=4107)

- **FILTRO** `sigma_ewma_delta_pct` > `4.085` → IC=-0.236 (n=1187)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.085
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=4288)

- **PATRÓN** `ibs_20min` > `0.8028` → IC=+0.302 (n=2112)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8028 (IC base=+0.015)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.962` → IC=+0.190 (n=2076)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 2.962 (IC base=+0.015)

- **PATRÓN** `volumen_pendiente_norm` > `0.2294` → IC=+0.331 (n=400)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2294 (IC base=+0.015)

- **PATRÓN** `volumen_spike_ratio` < `1.4491` → IC=+0.281 (n=660)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4491 (IC base=+0.015)

- **PATRÓN** `volumen_spike_ratio` > `2.2443` → IC=+0.304 (n=898)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2443 (IC base=+0.015)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.304 (n=1980)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 27.0 (IC base=+0.015)

- **PATRÓN** `ibs_20min` < `0.1746` → IC=+0.170 (n=1369)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.1746 (IC base=-0.022)

- **PATRÓN** `volumen_pendiente_norm` < `0.1515` → IC=+0.404 (n=1065)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1515 (IC base=-0.022)

- **PATRÓN** `volumen_spike_ratio` < `1.5277` → IC=+0.423 (n=453)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5277 (IC base=-0.022)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.402 (n=1051)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 22.0 (IC base=-0.022)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.1691` → IC=+0.225 (n=993)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1691 (IC base=+0.011)

- **PATRÓN** `volumen_regimen` < `1.195` → IC=+0.211 (n=2261)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.195 (IC base=+0.011)

- **PATRÓN** `volumen_regimen` > `0.6955` → IC=+0.218 (n=2020)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6955 (IC base=+0.011)

- **PATRÓN** `volumen_pendiente_norm` > `0.2774` → IC=+0.247 (n=306)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2774 (IC base=+0.011)

- **PATRÓN** `volumen_spike_ratio` < `1.4202` → IC=+0.228 (n=745)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4202 (IC base=+0.011)

- **PATRÓN** `ballena_activa_n` < `260.0` → IC=+0.246 (n=1492)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 260.0 (IC base=+0.011)

- **PATRÓN** `volumen_regimen` < `0.6867` → IC=+0.249 (n=699)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6867 (IC base=-0.004)

- **PATRÓN** `volumen_regimen` > `0.6187` → IC=+0.253 (n=1587)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6187 (IC base=-0.004)

- **PATRÓN** `volumen_pendiente_norm` > `0.2697` → IC=+0.306 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2697 (IC base=-0.004)

- **PATRÓN** `volumen_spike_ratio` < `1.5256` → IC=+0.258 (n=675)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5256 (IC base=-0.004)

- **PATRÓN** `volumen_spike_ratio` > `2.148` → IC=+0.261 (n=696)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.148 (IC base=-0.004)

- **PATRÓN** `ballena_activa_n` < `186.0` → IC=+0.275 (n=517)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 186.0 (IC base=-0.004)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.322 (n=2153)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0094 (IC base=+0.284)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.293 (n=3231)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.284)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.325 (n=1758)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.284)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.586` → IC=+0.305 (n=2172)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.586 (IC base=+0.284)

- **PATRÓN** `volumen_pendiente_norm` < `0.0979` → IC=+0.296 (n=2837)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0979 (IC base=+0.284)

- **PATRÓN** `volumen_spike_ratio` > `1.6099` → IC=+0.290 (n=3139)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6099 (IC base=+0.284)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.293 (n=3875)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.284)

- **PATRÓN** `libro_liquidez` > `2017.0956` → IC=+0.292 (n=1077)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2017.0956 (IC base=+0.284)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.308 (n=2018)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.284)

- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.331 (n=1961)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0089 (IC base=+0.307)

- **PATRÓN** `drift_60min` |x|≤ `0.1763` → IC=+0.326 (n=1291)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1763 (IC base=+0.307)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.326 (n=1127)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.307)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.311 (n=1324)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.307)

- **PATRÓN** `ibs_20min` > `0.1471` → IC=+0.318 (n=1956)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1471 (IC base=+0.307)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.125` → IC=+0.308 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.125 (IC base=+0.307)

- **PATRÓN** `volumen_pendiente_norm` < `0.1997` → IC=+0.307 (n=2886)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1997 (IC base=+0.307)

- **PATRÓN** `volumen_pendiente_norm` > `0.3452` → IC=+0.316 (n=476)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3452 (IC base=+0.307)

- **PATRÓN** `volumen_spike_ratio` > `2.7347` → IC=+0.324 (n=1284)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7347 (IC base=+0.307)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.307 (n=1498)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.307)

- **PATRÓN** `libro_liquidez` > `1896.567` → IC=+0.312 (n=1330)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1896.567 (IC base=+0.307)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.314 (n=2500)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 23.0 (IC base=+0.307)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7233` → IC=-0.180 (n=1454)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7233
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=4364)

- **PATRÓN** `dist_vwap_pct` > `0.144` → IC=+0.238 (n=1056)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.144 (IC base=+0.021)

- **PATRÓN** `volumen_regimen` < `1.1593` → IC=+0.237 (n=2069)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1593 (IC base=+0.021)

- **PATRÓN** `volumen_pendiente_norm` < `0.1628` → IC=+0.236 (n=2171)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1628 (IC base=+0.021)

- **PATRÓN** `volumen_pendiente_norm` > `0.1032` → IC=+0.244 (n=678)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1032 (IC base=+0.021)

- **PATRÓN** `volumen_spike_ratio` < `2.4511` → IC=+0.240 (n=2008)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4511 (IC base=+0.021)

- **PATRÓN** `ballena_activa_n` < `114.0` → IC=+0.255 (n=2048)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 114.0 (IC base=+0.021)

- **PATRÓN** `dist_vwap_pct` > `0.7358` → IC=+0.259 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7358 (IC base=+0.006)

- **PATRÓN** `volumen_regimen` < `1.1824` → IC=+0.262 (n=1492)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1824 (IC base=+0.006)

- **PATRÓN** `volumen_pendiente_norm` > `0.2808` → IC=+0.315 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2808 (IC base=+0.006)

- **PATRÓN** `volumen_spike_ratio` < `1.7847` → IC=+0.291 (n=955)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7847 (IC base=+0.006)

- **PATRÓN** `volumen_spike_ratio` > `2.4256` → IC=+0.280 (n=479)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4256 (IC base=+0.006)

- **PATRÓN** `ballena_activa_n` < `115.0` → IC=+0.283 (n=1456)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 115.0 (IC base=+0.006)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7407` → IC=-0.248 (n=2380)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7407
  - _Potencial_: sin este filtro IC_bueno=+0.312 (n=2388)

- **FILTRO** `ibs_20min` > `0.6203` → IC=-0.235 (n=1126)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6203
  - _Potencial_: sin este filtro IC_bueno=+0.152 (n=3381)

- **FILTRO** `sigma_ewma_delta_pct` > `8.282` → IC=-0.262 (n=515)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.282
  - _Potencial_: sin este filtro IC_bueno=+0.096 (n=3992)

- **PATRÓN** `ibs_20min` > `0.7407` → IC=+0.312 (n=2388)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7407 (IC base=+0.032)

- **PATRÓN** `dist_vwap_pct` > `1.043` → IC=+0.356 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.043 (IC base=+0.032)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.461` → IC=+0.154 (n=1936)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 2.461 (IC base=+0.032)

- **PATRÓN** `volumen_regimen` < `0.8445` → IC=+0.342 (n=1157)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8445 (IC base=+0.032)

- **PATRÓN** `volumen_regimen` > `0.6967` → IC=+0.335 (n=1550)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6967 (IC base=+0.032)

- **PATRÓN** `volumen_pendiente_norm` < `0.1562` → IC=+0.335 (n=1787)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1562 (IC base=+0.032)

- **PATRÓN** `volumen_pendiente_norm` > `0.274` → IC=+0.363 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.274 (IC base=+0.032)

- **PATRÓN** `volumen_spike_ratio` < `1.4239` → IC=+0.358 (n=562)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4239 (IC base=+0.032)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.354 (n=1498)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=+0.032)

- **PATRÓN** `ibs_20min` < `0.6203` → IC=+0.152 (n=3381)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` < 0.6203 (IC base=+0.055)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.034` → IC=+0.130 (n=3175)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` < 3.034 (IC base=+0.055)

- **PATRÓN** `volumen_regimen` < `0.6951` → IC=+0.281 (n=746)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6951 (IC base=+0.055)

- **PATRÓN** `volumen_pendiente_norm` > `0.0714` → IC=+0.291 (n=681)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0714 (IC base=+0.055)

- **PATRÓN** `volumen_spike_ratio` < `1.802` → IC=+0.278 (n=1094)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.802 (IC base=+0.055)

- **PATRÓN** `ballena_activa_n` < `39.0` → IC=+0.280 (n=1490)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 39.0 (IC base=+0.055)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0157` → IC=+0.359 (n=1627)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0157 (IC base=+0.315)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.317 (n=2466)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.315)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.317 (n=1159)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.315)

- **PATRÓN** `ibs_20min` > `0.66` → IC=+0.343 (n=2442)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.66 (IC base=+0.315)

- **PATRÓN** `dist_vwap_pct` > `0.294` → IC=+0.339 (n=1191)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.294 (IC base=+0.315)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.781` → IC=+0.334 (n=1191)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.781 (IC base=+0.315)

- **PATRÓN** `volumen_regimen` > `0.6293` → IC=+0.326 (n=2440)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6293 (IC base=+0.315)

- **PATRÓN** `volumen_pendiente_norm` > `0.2809` → IC=+0.345 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2809 (IC base=+0.315)

- **PATRÓN** `volumen_spike_ratio` > `1.4315` → IC=+0.326 (n=2353)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4315 (IC base=+0.315)

- **PATRÓN** `libro_liquidez` > `2992.9424` → IC=+0.327 (n=814)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2992.9424 (IC base=+0.315)

- **PATRÓN** `ballena_activa_n` < `33.0` → IC=+0.342 (n=1923)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 33.0 (IC base=+0.315)

- **PATRÓN** `sigma_h` > `0.015` → IC=+0.350 (n=1744)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.015 (IC base=+0.316)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.320 (n=1326)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.316)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.318 (n=1260)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.316)

- **PATRÓN** `ibs_20min` < `0.381` → IC=+0.334 (n=2614)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.381 (IC base=+0.316)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.619` → IC=+0.328 (n=962)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.619 (IC base=+0.316)

- **PATRÓN** `volumen_regimen` < `0.7189` → IC=+0.322 (n=1151)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7189 (IC base=+0.316)

- **PATRÓN** `volumen_regimen` > `1.2085` → IC=+0.342 (n=871)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2085 (IC base=+0.316)

- **PATRÓN** `volumen_pendiente_norm` > `0.2299` → IC=+0.366 (n=491)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2299 (IC base=+0.316)

- **PATRÓN** `volumen_spike_ratio` < `1.4118` → IC=+0.323 (n=811)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4118 (IC base=+0.316)

- **PATRÓN** `volumen_spike_ratio` > `2.139` → IC=+0.316 (n=1102)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.139 (IC base=+0.316)

- **PATRÓN** `libro_liquidez` > `2973.5854` → IC=+0.316 (n=871)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2973.5854 (IC base=+0.316)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.223 (n=5728)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0125 (IC base=+0.173)

- **PATRÓN** `drift_60min` |x|≤ `0.1222` → IC=+0.191 (n=7555)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.1222 (IC base=+0.173)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.183 (n=17809)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.173)

- **PATRÓN** `ibs_20min` > `0.5374` → IC=+0.230 (n=17167)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5374 (IC base=+0.173)

- **PATRÓN** `dist_vwap_pct` > `0.1624` → IC=+0.205 (n=6515)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1624 (IC base=+0.173)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.765` → IC=+0.258 (n=3344)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.765 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` < `1.1796` → IC=+0.152 (n=11431)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.1796 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` > `0.6256` → IC=+0.152 (n=11430)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.6256 (IC base=+0.173)

- **PATRÓN** `volumen_pendiente_norm` > `0.2942` → IC=+0.203 (n=2488)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2942 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` > `2.6086` → IC=+0.187 (n=5566)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.6086 (IC base=+0.173)

- **PATRÓN** `ballena_activa_n` < `87.0` → IC=+0.192 (n=16091)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 87.0 (IC base=+0.173)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.193 (n=7430)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0058 (IC base=+0.184)

- **PATRÓN** `drift_60min` |x|≤ `0.0804` → IC=+0.222 (n=5621)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0804 (IC base=+0.184)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.211 (n=6342)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.184)

- **PATRÓN** `ibs_20min` < `0.526` → IC=+0.239 (n=16857)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.526 (IC base=+0.184)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.522` → IC=+0.190 (n=2684)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 9.522 (IC base=+0.184)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.511` → IC=+0.190 (n=15016)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` < 2.511 (IC base=+0.184)

- **PATRÓN** `volumen_regimen` < `1.182` → IC=+0.165 (n=11999)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.182 (IC base=+0.184)

- **PATRÓN** `volumen_pendiente_norm` > `0.2939` → IC=+0.219 (n=2526)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2939 (IC base=+0.184)

- **PATRÓN** `volumen_spike_ratio` < `1.5593` → IC=+0.183 (n=7061)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 1.5593 (IC base=+0.184)

- **PATRÓN** `volumen_spike_ratio` > `2.6296` → IC=+0.193 (n=5349)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.6296 (IC base=+0.184)

- **PATRÓN** `ballena_activa_n` < `91.0` → IC=+0.198 (n=15842)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 91.0 (IC base=+0.184)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` > `0.0108` → IC=+0.266 (n=944)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0108 (IC base=+0.227)

- **PATRÓN** `drift_60min` |x|≤ `0.1043` → IC=+0.256 (n=1246)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1043 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.233 (n=2945)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.227)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.227 (n=1920)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.227)

- **PATRÓN** `ibs_20min` > `0.9423` → IC=+0.295 (n=1887)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9423 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.46` → IC=+0.329 (n=923)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.46 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` > `0.2811` → IC=+0.287 (n=431)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2811 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` < `1.8383` → IC=+0.226 (n=1802)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8383 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` > `1.4363` → IC=+0.227 (n=2700)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4363 (IC base=+0.227)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.237 (n=3146)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.227)

- **PATRÓN** `sigma_h` < `0.0099` → IC=+0.258 (n=2296)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0099 (IC base=+0.257)

- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.259 (n=1046)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0089 (IC base=+0.257)

- **PATRÓN** `drift_60min` |x|≤ `0.0962` → IC=+0.314 (n=1009)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0962 (IC base=+0.257)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.261 (n=2370)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.257)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.261 (n=2091)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.257)

- **PATRÓN** `ibs_20min` < `0.055` → IC=+0.302 (n=1009)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.055 (IC base=+0.257)

- **PATRÓN** `volumen_pendiente_norm` < `0.0993` → IC=+0.260 (n=2016)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0993 (IC base=+0.257)

- **PATRÓN** `volumen_pendiente_norm` > `0.3015` → IC=+0.272 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3015 (IC base=+0.257)

- **PATRÓN** `volumen_spike_ratio` < `1.4462` → IC=+0.277 (n=733)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4462 (IC base=+0.257)

- **PATRÓN** `volumen_spike_ratio` > `2.6922` → IC=+0.259 (n=732)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6922 (IC base=+0.257)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.267 (n=1638)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.257)

- **PATRÓN** `libro_liquidez` > `1774.727` → IC=+0.265 (n=1529)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1774.727 (IC base=+0.257)

- **PATRÓN** `ballena_activa_n` < `7.0` → IC=+0.258 (n=857)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 7.0 (IC base=+0.257)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.201 (n=876)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.128)

- **PATRÓN** `drift_60min` |x|≤ `0.0657` → IC=+0.175 (n=875)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.0657 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.145 (n=2743)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` > `0.2602` → IC=+0.206 (n=2621)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2602 (IC base=+0.128)

- **PATRÓN** `dist_vwap_pct` > `0.1842` → IC=+0.212 (n=1307)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1842 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.646` → IC=+0.209 (n=480)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.646 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` < `0.6275` → IC=+0.131 (n=874)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 0.6275 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` > `1.0568` → IC=+0.135 (n=1188)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` > 1.0568 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` > `0.281` → IC=+0.169 (n=406)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.281 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` < `1.5076` → IC=+0.132 (n=1133)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 1.5076 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` > `2.4711` → IC=+0.148 (n=859)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 2.4711 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `398.0` → IC=+0.132 (n=2548)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 398.0 (IC base=+0.128)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.171 (n=2777)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0065 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.2375` → IC=+0.173 (n=2440)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.2375 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.180 (n=1318)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 15.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` < `0.6109` → IC=+0.209 (n=2773)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6109 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.86` → IC=+0.178 (n=523)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 10.86 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.023` → IC=+0.152 (n=2420)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` < 4.023 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `1.1952` → IC=+0.161 (n=2773)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.1952 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` < `0.0941` → IC=+0.150 (n=2396)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` < 0.0941 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `2.4589` → IC=+0.153 (n=2647)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.4589 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `210.0` → IC=+0.191 (n=1146)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 210.0 (IC base=+0.148)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0115` → IC=+0.231 (n=1319)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0115 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.2478` → IC=+0.233 (n=1938)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2478 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.219 (n=3024)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.293 (n=1543)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.096` → IC=+0.305 (n=691)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.096 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` < `0.0988` → IC=+0.211 (n=2530)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0988 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` > `0.353` → IC=+0.241 (n=412)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.353 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `2.7129` → IC=+0.225 (n=1287)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7129 (IC base=+0.212)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.215 (n=3512)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `2006.3984` → IC=+0.223 (n=969)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2006.3984 (IC base=+0.212)

- **PATRÓN** `sigma_h` < `0.0118` → IC=+0.245 (n=2567)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0118 (IC base=+0.239)

- **PATRÓN** `drift_60min` |x|≤ `0.4107` → IC=+0.263 (n=2259)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4107 (IC base=+0.239)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.278 (n=985)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.239)

- **PATRÓN** `ibs_20min` < `0.0409` → IC=+0.290 (n=1130)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0409 (IC base=+0.239)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.906` → IC=+0.277 (n=339)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.906 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` > `0.3557` → IC=+0.289 (n=429)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3557 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` < `1.7719` → IC=+0.240 (n=1091)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7719 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` > `2.1802` → IC=+0.251 (n=1653)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1802 (IC base=+0.239)

- **PATRÓN** `libro_liquidez` > `1880.7482` → IC=+0.251 (n=1164)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1880.7482 (IC base=+0.239)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.244 (n=1703)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.239)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.205 (n=946)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0038 (IC base=+0.129)

- **PATRÓN** `drift_60min` |x|≤ `0.0775` → IC=+0.184 (n=942)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.0775 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.139 (n=2923)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.129)

- **PATRÓN** `ibs_20min` > `0.2467` → IC=+0.191 (n=2825)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.2467 (IC base=+0.129)

- **PATRÓN** `dist_vwap_pct` > `0.1398` → IC=+0.186 (n=1624)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1398 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.255` → IC=+0.200 (n=485)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.255 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` < `0.8431` → IC=+0.136 (n=1884)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.8431 (IC base=+0.129)

- **PATRÓN** `volumen_pendiente_norm` > `0.2882` → IC=+0.170 (n=425)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.2882 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` > `2.5111` → IC=+0.145 (n=922)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 2.5111 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `6839.7566` → IC=+0.196 (n=1281)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 6839.7566 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `126.0` → IC=+0.128 (n=2763)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 126.0 (IC base=+0.129)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.165 (n=2648)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0067 (IC base=+0.130)

- **PATRÓN** `drift_60min` |x|≤ `0.3955` → IC=+0.146 (n=3007)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.3955 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.165 (n=1438)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 15.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` < `0.6789` → IC=+0.185 (n=3007)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.6789 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.209` → IC=+0.138 (n=717)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 9.209 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` < `0.852` → IC=+0.151 (n=2005)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.852 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` > `0.2939` → IC=+0.173 (n=450)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.2939 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` < `1.8002` → IC=+0.133 (n=1902)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 1.8002 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` > `1.4148` → IC=+0.131 (n=2853)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 1.4148 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `6321.4176` → IC=+0.189 (n=1363)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 6321.4176 (IC base=+0.130)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.153 (n=977)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 49.0 (IC base=+0.130)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.160 (n=1429)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0113 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.133 (n=3230)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 5.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` > `0.4706` → IC=+0.204 (n=3159)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4706 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` > `0.1966` → IC=+0.188 (n=1688)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1966 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.996` → IC=+0.287 (n=665)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.996 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` < `1.1689` → IC=+0.130 (n=3152)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.1689 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` < `0.163` → IC=+0.123 (n=3210)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.163 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` < `1.7799` → IC=+0.125 (n=2038)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 1.7799 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `2665.4023` → IC=+0.194 (n=1429)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 2665.4023 (IC base=+0.118)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.133 (n=1041)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 16.0 (IC base=+0.118)

- **PATRÓN** `sigma_h` < `0.0119` → IC=+0.142 (n=3292)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.0119 (IC base=+0.119)

- **PATRÓN** `drift_60min` |x|≤ `0.1121` → IC=+0.165 (n=1096)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.1121 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.134 (n=3361)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 5.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` < `0.65` → IC=+0.219 (n=3288)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.65 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.253` → IC=+0.139 (n=2912)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` < 2.253 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` < `1.1736` → IC=+0.127 (n=3287)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` < 1.1736 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` > `0.275` → IC=+0.147 (n=454)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` > 0.275 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` < `1.4337` → IC=+0.138 (n=1036)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.4337 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `2902.3615` → IC=+0.194 (n=1096)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 2902.3615 (IC base=+0.119)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.124 (n=2090)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 27.0 (IC base=+0.119)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0131` → IC=+0.250 (n=2532)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0131 (IC base=+0.226)

- **PATRÓN** `drift_60min` |x|≤ `0.1653` → IC=+0.242 (n=1248)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1653 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.232 (n=2944)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.226)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.229 (n=2558)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.226)

- **PATRÓN** `ibs_20min` > `0.6667` → IC=+0.257 (n=2834)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6667 (IC base=+0.226)

- **PATRÓN** `dist_vwap_pct` > `0.1809` → IC=+0.233 (n=1738)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1809 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.576` → IC=+0.257 (n=1289)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.576 (IC base=+0.226)

- **PATRÓN** `volumen_regimen` > `0.6237` → IC=+0.235 (n=2835)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6237 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` > `0.2352` → IC=+0.268 (n=527)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2352 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` < `2.472` → IC=+0.229 (n=2764)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.472 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` > `1.4338` → IC=+0.230 (n=2764)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4338 (IC base=+0.226)

- **PATRÓN** `libro_liquidez` > `2585.5589` → IC=+0.232 (n=1889)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2585.5589 (IC base=+0.226)

- **PATRÓN** `sigma_h` > `0.0227` → IC=+0.249 (n=1330)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0227 (IC base=+0.240)

- **PATRÓN** `drift_60min` |x|≤ `0.5783` → IC=+0.249 (n=2933)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5783 (IC base=+0.240)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.252 (n=1440)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.240)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.246 (n=1306)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.240)

- **PATRÓN** `ibs_20min` < `0.44` → IC=+0.263 (n=2942)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.44 (IC base=+0.240)

- **PATRÓN** `dist_vwap_pct` > `1.1432` → IC=+0.259 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1432 (IC base=+0.240)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.0` → IC=+0.268 (n=407)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.0 (IC base=+0.240)

- **PATRÓN** `volumen_regimen` < `0.8662` → IC=+0.242 (n=1956)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8662 (IC base=+0.240)

- **PATRÓN** `volumen_regimen` > `0.6408` → IC=+0.243 (n=2933)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6408 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` > `0.2812` → IC=+0.294 (n=406)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2812 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` < `1.8375` → IC=+0.238 (n=1845)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8375 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` > `1.549` → IC=+0.240 (n=2471)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.549 (IC base=+0.240)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.209 (n=1484)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.159)

- **PATRÓN** `drift_60min` |x|≤ `0.1332` → IC=+0.174 (n=1950)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.1332 (IC base=+0.159)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.195 (n=2163)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 15.0 (IC base=+0.159)

- **PATRÓN** `ibs_20min` > `0.3077` → IC=+0.196 (n=4433)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.3077 (IC base=+0.159)

- **PATRÓN** `dist_vwap_pct` > `0.2208` → IC=+0.183 (n=1684)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.2208 (IC base=+0.159)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.557` → IC=+0.209 (n=723)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.557 (IC base=+0.159)

- **PATRÓN** `volumen_regimen` < `0.8605` → IC=+0.170 (n=2684)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 0.8605 (IC base=+0.159)

- **PATRÓN** `volumen_regimen` > `1.1935` → IC=+0.164 (n=1342)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 1.1935 (IC base=+0.159)

- **PATRÓN** `volumen_pendiente_norm` > `0.1571` → IC=+0.174 (n=1166)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.1571 (IC base=+0.159)

- **PATRÓN** `volumen_spike_ratio` < `1.527` → IC=+0.165 (n=1901)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.527 (IC base=+0.159)

- **PATRÓN** `volumen_spike_ratio` > `1.809` → IC=+0.161 (n=2881)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.809 (IC base=+0.159)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.160 (n=4961)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.02 (IC base=+0.159)

- **PATRÓN** `libro_liquidez` > `7688.5419` → IC=+0.186 (n=2009)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 7688.5419 (IC base=+0.159)

- **PATRÓN** `ibs_20min` < `0.3836` → IC=+0.173 (n=3210)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.3836 (IC base=+0.094)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.134 (n=2050)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 23.0 (IC base=+0.094)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.197 (n=1141)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0061 (IC base=+0.183)

- **PATRÓN** `drift_60min` |x|≤ `0.3292` → IC=+0.198 (n=1141)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.3292 (IC base=+0.183)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.216 (n=1029)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.183)

- **PATRÓN** `ibs_20min` > `0.6177` → IC=+0.239 (n=760)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6177 (IC base=+0.183)

- **PATRÓN** `dist_vwap_pct` > `0.3087` → IC=+0.218 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3087 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.927` → IC=+0.212 (n=502)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.927 (IC base=+0.183)

- **PATRÓN** `volumen_regimen` < `0.8791` → IC=+0.196 (n=761)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 0.8791 (IC base=+0.183)

- **PATRÓN** `volumen_pendiente_norm` > `0.0913` → IC=+0.197 (n=394)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.0913 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` < `2.1675` → IC=+0.197 (n=985)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 2.1675 (IC base=+0.183)

- **PATRÓN** `libro_liquidez` > `15745.686` → IC=+0.192 (n=517)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 15745.686 (IC base=+0.183)

- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.160 (n=474)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0031 (IC base=+0.083)

- **PATRÓN** `ibs_20min` < `0.2049` → IC=+0.200 (n=625)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2049 (IC base=+0.083)

- **PATRÓN** `ballena_activa_n` < `164.0` → IC=+0.177 (n=614)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 164.0 (IC base=+0.083)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.235 (n=598)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.2092` → IC=+0.156 (n=907)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.2092 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.172 (n=1410)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 5.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` > `0.7914` → IC=+0.266 (n=617)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7914 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` > `0.821` → IC=+0.192 (n=222)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.821 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.882` → IC=+0.206 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.882 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` < `0.8322` → IC=+0.165 (n=907)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8322 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` > `0.2193` → IC=+0.199 (n=247)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2193 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` > `1.7764` → IC=+0.170 (n=894)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 1.7764 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `8031.121` → IC=+0.175 (n=617)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 8031.121 (IC base=+0.153)

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.124 (n=883)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0052 (IC base=+0.093)

- **PATRÓN** `ibs_20min` < `0.0847` → IC=+0.212 (n=442)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0847 (IC base=+0.093)

- **PATRÓN** `volumen_regimen` < `0.6781` → IC=+0.126 (n=583)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` < 0.6781 (IC base=+0.093)

- **PATRÓN** `libro_liquidez` > `7971.353` → IC=+0.152 (n=601)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 7971.353 (IC base=+0.093)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.131 (n=437)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 35.0 (IC base=+0.093)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` < `0.0092` → IC=+0.148 (n=765)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0092 (IC base=+0.129)

- **PATRÓN** `drift_60min` |x|≤ `0.5372` → IC=+0.128 (n=1147)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.64€ cuando `drift_60min` |x|≤ 0.5372 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.171 (n=800)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 11.0 (IC base=+0.129)

- **PATRÓN** `ibs_20min` > `0.5455` → IC=+0.197 (n=1024)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.5455 (IC base=+0.129)

- **PATRÓN** `dist_vwap_pct` > `0.9272` → IC=+0.175 (n=186)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.9272 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.857` → IC=+0.229 (n=452)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.857 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` < `1.0445` → IC=+0.141 (n=1008)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 1.0445 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` > `0.7005` → IC=+0.137 (n=1024)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` > 0.7005 (IC base=+0.129)

- **PATRÓN** `volumen_pendiente_norm` > `0.2253` → IC=+0.155 (n=201)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` > 0.2253 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` < `1.4112` → IC=+0.156 (n=370)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.4112 (IC base=+0.129)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.131 (n=1200)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.02 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `2765.9275` → IC=+0.169 (n=520)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 2765.9275 (IC base=+0.129)

- **PATRÓN** `ibs_20min` < `0.5556` → IC=+0.150 (n=1121)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.5556 (IC base=+0.073)

- **PATRÓN** `libro_liquidez` > `2641.0193` → IC=+0.165 (n=577)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 2641.0193 (IC base=+0.073)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0173` → IC=+0.242 (n=254)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0173 (IC base=+0.194)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.236 (n=180)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.194)

- **PATRÓN** `ibs_20min` > `0.7222` → IC=+0.211 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7222 (IC base=+0.194)

- **PATRÓN** `dist_vwap_pct` > `0.3129` → IC=+0.213 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3129 (IC base=+0.194)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.492` → IC=+0.221 (n=338)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.492 (IC base=+0.194)

- **PATRÓN** `volumen_regimen` > `1.1939` → IC=+0.260 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1939 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` > `0.078` → IC=+0.206 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.078 (IC base=+0.194)

- **PATRÓN** `volumen_spike_ratio` < `2.1565` → IC=+0.209 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1565 (IC base=+0.194)

- **PATRÓN** `volumen_spike_ratio` > `2.3975` → IC=+0.208 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3975 (IC base=+0.194)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.203 (n=415)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.194)

- **PATRÓN** `libro_liquidez` > `3017.6749` → IC=+0.205 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3017.6749 (IC base=+0.194)

- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.157 (n=418)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0112 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.3231` → IC=+0.155 (n=279)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.3231 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.188 (n=200)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 15.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.158 (n=369)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.5 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `1.2011` → IC=+0.269 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2011 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.225` → IC=+0.176 (n=109)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 5.225 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.521` → IC=+0.142 (n=504)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 9.521 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `0.889` → IC=+0.188 (n=280)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 0.889 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` < `0.1106` → IC=+0.156 (n=385)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` < 0.1106 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.2293` → IC=+0.171 (n=77)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.2293 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `1.4819` → IC=+0.191 (n=134)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 1.4819 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `2.6395` → IC=+0.162 (n=134)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 2.6395 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.158 (n=404)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 20.0 (IC base=+0.140)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.229 (n=7502)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0125 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.190 (n=23449)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` > `0.4292` → IC=+0.227 (n=22480)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4292 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` > `0.882` → IC=+0.213 (n=2643)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.882 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.949` → IC=+0.258 (n=5505)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.949 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` < `1.2141` → IC=+0.159 (n=15141)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2141 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.2411` → IC=+0.209 (n=4038)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2411 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `2.6236` → IC=+0.194 (n=7317)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.6236 (IC base=+0.180)

- **PATRÓN** `ballena_activa_n` < `103.0` → IC=+0.201 (n=21148)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 103.0 (IC base=+0.180)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.199 (n=9101)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0061 (IC base=+0.195)

- **PATRÓN** `sigma_h` > `0.0122` → IC=+0.205 (n=6886)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0122 (IC base=+0.195)

- **PATRÓN** `drift_60min` |x|≤ `0.4819` → IC=+0.199 (n=20649)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.4819 (IC base=+0.195)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.215 (n=7721)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.195)

- **PATRÓN** `ibs_20min` < `0.5926` → IC=+0.244 (n=20649)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5926 (IC base=+0.195)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.528` → IC=+0.202 (n=19170)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.528 (IC base=+0.195)

- **PATRÓN** `volumen_regimen` < `0.6319` → IC=+0.178 (n=4626)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` < 0.6319 (IC base=+0.195)

- **PATRÓN** `volumen_pendiente_norm` > `0.2931` → IC=+0.253 (n=2835)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2931 (IC base=+0.195)

- **PATRÓN** `volumen_spike_ratio` > `2.6293` → IC=+0.207 (n=6591)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6293 (IC base=+0.195)

- **PATRÓN** `ballena_activa_n` < `91.0` → IC=+0.212 (n=19549)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 91.0 (IC base=+0.195)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` > `0.0108` → IC=+0.283 (n=1200)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0108 (IC base=+0.236)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.252 (n=1746)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.236)

- **PATRÓN** `ibs_20min` > `0.8644` → IC=+0.297 (n=2400)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8644 (IC base=+0.236)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.827` → IC=+0.342 (n=859)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.827 (IC base=+0.236)

- **PATRÓN** `volumen_pendiente_norm` > `0.2323` → IC=+0.293 (n=649)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2323 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` < `1.4504` → IC=+0.234 (n=1159)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4504 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` > `2.2901` → IC=+0.241 (n=1576)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2901 (IC base=+0.236)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.250 (n=3962)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.236)

- **PATRÓN** `libro_liquidez` > `2037.1587` → IC=+0.239 (n=1200)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2037.1587 (IC base=+0.236)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.253 (n=2202)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 14.0 (IC base=+0.236)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.270 (n=3207)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0103 (IC base=+0.269)

- **PATRÓN** `sigma_h` > `0.0092` → IC=+0.269 (n=1459)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0092 (IC base=+0.269)

- **PATRÓN** `drift_60min` |x|≤ `0.1215` → IC=+0.295 (n=1411)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1215 (IC base=+0.269)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.270 (n=3335)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.269)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.271 (n=2898)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.269)

- **PATRÓN** `ibs_20min` < `0.5496` → IC=+0.286 (n=3206)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5496 (IC base=+0.269)

- **PATRÓN** `volumen_pendiente_norm` < `0.1608` → IC=+0.271 (n=3233)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1608 (IC base=+0.269)

- **PATRÓN** `volumen_pendiente_norm` > `0.2905` → IC=+0.285 (n=444)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2905 (IC base=+0.269)

- **PATRÓN** `volumen_spike_ratio` < `1.5629` → IC=+0.273 (n=1354)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5629 (IC base=+0.269)

- **PATRÓN** `volumen_spike_ratio` > `2.6459` → IC=+0.278 (n=1026)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6459 (IC base=+0.269)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.274 (n=2279)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.269)

- **PATRÓN** `libro_liquidez` > `1774.927` → IC=+0.277 (n=2137)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1774.927 (IC base=+0.269)

- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.280 (n=1142)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 8.0 (IC base=+0.269)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.178 (n=1234)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0032 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.0787` → IC=+0.147 (n=1229)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.0787 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.148 (n=3844)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 5.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` > `0.1969` → IC=+0.188 (n=3686)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.1969 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` > `0.3199` → IC=+0.199 (n=1198)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3199 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.338` → IC=+0.167 (n=770)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 9.338 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `0.6362` → IC=+0.153 (n=1230)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.6362 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` > `1.0691` → IC=+0.141 (n=1672)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` > 1.0691 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.2716` → IC=+0.181 (n=519)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.2716 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `2.1676` → IC=+0.141 (n=3184)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 2.1676 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `1.5212` → IC=+0.143 (n=3234)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.5212 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `218.0` → IC=+0.161 (n=1187)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 218.0 (IC base=+0.137)

- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.163 (n=3176)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0064 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.3265` → IC=+0.147 (n=3175)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.3265 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.167 (n=1166)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 17.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` < `0.6808` → IC=+0.185 (n=3175)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.6808 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.001` → IC=+0.139 (n=2870)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 4.001 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `1.0456` → IC=+0.151 (n=2794)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.0456 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.2196` → IC=+0.191 (n=591)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2196 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `2.4321` → IC=+0.143 (n=3066)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.4321 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `1.7707` → IC=+0.142 (n=2044)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.7707 (IC base=+0.137)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.138 (n=4125)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `223.0` → IC=+0.154 (n=997)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 223.0 (IC base=+0.137)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.242 (n=2495)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0099 (IC base=+0.228)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.237 (n=3918)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.228)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.228 (n=3350)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.228)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.303 (n=1398)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.228)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.017` → IC=+0.324 (n=834)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.017 (IC base=+0.228)

- **PATRÓN** `volumen_pendiente_norm` < `0.132` → IC=+0.229 (n=3542)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.132 (IC base=+0.228)

- **PATRÓN** `volumen_pendiente_norm` > `0.351` → IC=+0.233 (n=488)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.351 (IC base=+0.228)

- **PATRÓN** `volumen_spike_ratio` > `2.7431` → IC=+0.242 (n=1658)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7431 (IC base=+0.228)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.234 (n=4512)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.228)

- **PATRÓN** `libro_liquidez` > `1909.72` → IC=+0.238 (n=1696)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1909.72 (IC base=+0.228)

- **PATRÓN** `sigma_h` < `0.011` → IC=+0.250 (n=3147)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.011 (IC base=+0.245)

- **PATRÓN** `drift_60min` |x|≤ `0.1768` → IC=+0.265 (n=1574)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1768 (IC base=+0.245)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.263 (n=1363)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.245)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.248 (n=1625)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.245)

- **PATRÓN** `ibs_20min` < `0.0608` → IC=+0.303 (n=1194)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0608 (IC base=+0.245)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.054` → IC=+0.304 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.054 (IC base=+0.245)

- **PATRÓN** `volumen_pendiente_norm` > `0.3489` → IC=+0.308 (n=539)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3489 (IC base=+0.245)

- **PATRÓN** `volumen_spike_ratio` > `2.1769` → IC=+0.256 (n=2298)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1769 (IC base=+0.245)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.249 (n=1834)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.245)

- **PATRÓN** `libro_liquidez` > `1991.8648` → IC=+0.258 (n=1192)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1991.8648 (IC base=+0.245)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.250 (n=3031)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 22.0 (IC base=+0.245)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.194 (n=1297)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0037 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.4315` → IC=+0.146 (n=3889)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.4315 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.150 (n=4035)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 5.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` > `0.8855` → IC=+0.271 (n=1296)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8855 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` > `0.1961` → IC=+0.170 (n=1753)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.1961 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.968` → IC=+0.158 (n=1726)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 2.968 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `0.86` → IC=+0.152 (n=2593)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.86 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.2333` → IC=+0.191 (n=690)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.2333 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `1.5176` → IC=+0.154 (n=1673)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 1.5176 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `2.1723` → IC=+0.143 (n=1724)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 2.1723 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `7287.1688` → IC=+0.238 (n=1296)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7287.1688 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `87.0` → IC=+0.146 (n=2519)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 87.0 (IC base=+0.138)

- **PATRÓN** `sigma_h` < `0.0078` → IC=+0.164 (n=3252)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0078 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.4369` → IC=+0.157 (n=3247)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.4369 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.174 (n=1196)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 17.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` < `0.5743` → IC=+0.212 (n=2859)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5743 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.014` → IC=+0.154 (n=642)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 9.014 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.039` → IC=+0.150 (n=2835)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 3.039 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` < `0.69` → IC=+0.165 (n=1429)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.69 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` > `0.2937` → IC=+0.211 (n=413)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2937 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `2.2064` → IC=+0.151 (n=2760)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.2064 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` > `1.5286` → IC=+0.155 (n=2802)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.5286 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `6468.2131` → IC=+0.221 (n=1083)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6468.2131 (IC base=+0.147)

- **PATRÓN** `ballena_activa_n` < `90.0` → IC=+0.162 (n=2127)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 90.0 (IC base=+0.147)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0127` → IC=+0.152 (n=1322)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` > 0.0127 (IC base=+0.115)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.147 (n=2797)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 11.0 (IC base=+0.115)

- **PATRÓN** `ibs_20min` > `0.4286` → IC=+0.185 (n=3966)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.4286 (IC base=+0.115)

- **PATRÓN** `dist_vwap_pct` > `1.0064` → IC=+0.204 (n=639)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0064 (IC base=+0.115)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.246` → IC=+0.270 (n=1004)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.246 (IC base=+0.115)

- **PATRÓN** `volumen_regimen` < `0.8763` → IC=+0.128 (n=2636)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 0.8763 (IC base=+0.115)

- **PATRÓN** `volumen_spike_ratio` < `1.824` → IC=+0.122 (n=2574)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` < 1.824 (IC base=+0.115)

- **PATRÓN** `libro_liquidez` > `2714.0997` → IC=+0.237 (n=1318)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2714.0997 (IC base=+0.115)

- **PATRÓN** `sigma_h` < `0.0109` → IC=+0.154 (n=3266)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0109 (IC base=+0.128)

- **PATRÓN** `drift_60min` |x|≤ `0.1376` → IC=+0.153 (n=1235)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.1376 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.164 (n=1743)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 15.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` < `0.6667` → IC=+0.217 (n=3714)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6667 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.039` → IC=+0.150 (n=3586)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 3.039 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` < `0.6401` → IC=+0.151 (n=1236)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.6401 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` > `0.2296` → IC=+0.185 (n=649)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.2296 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` < `1.437` → IC=+0.162 (n=1174)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 1.437 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `2602.1348` → IC=+0.210 (n=1235)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2602.1348 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.142 (n=3126)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 42.0 (IC base=+0.128)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0138` → IC=+0.260 (n=3229)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0138 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.244 (n=3780)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.238)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.243 (n=2411)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.238)

- **PATRÓN** `ibs_20min` > `0.6142` → IC=+0.272 (n=3229)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6142 (IC base=+0.238)

- **PATRÓN** `dist_vwap_pct` > `0.1931` → IC=+0.252 (n=1852)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1931 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.164` → IC=+0.288 (n=631)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.164 (IC base=+0.238)

- **PATRÓN** `volumen_regimen` < `1.2171` → IC=+0.239 (n=3615)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2171 (IC base=+0.238)

- **PATRÓN** `volumen_regimen` > `0.6434` → IC=+0.243 (n=3616)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6434 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` > `0.2393` → IC=+0.254 (n=625)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2393 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` > `2.4984` → IC=+0.258 (n=1179)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4984 (IC base=+0.238)

- **PATRÓN** `libro_liquidez` > `2982.5368` → IC=+0.244 (n=1205)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2982.5368 (IC base=+0.238)

- **PATRÓN** `sigma_h` > `0.0258` → IC=+0.268 (n=1247)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0258 (IC base=+0.244)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.248 (n=3532)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.244)

- **PATRÓN** `ibs_20min` < `0.1388` → IC=+0.308 (n=1646)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1388 (IC base=+0.244)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.09` → IC=+0.276 (n=721)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.09 (IC base=+0.244)

- **PATRÓN** `volumen_regimen` < `0.7155` → IC=+0.245 (n=1646)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7155 (IC base=+0.244)

- **PATRÓN** `volumen_regimen` > `1.2151` → IC=+0.263 (n=1247)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2151 (IC base=+0.244)

- **PATRÓN** `volumen_pendiente_norm` > `0.2861` → IC=+0.307 (n=515)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2861 (IC base=+0.244)

- **PATRÓN** `volumen_spike_ratio` > `1.432` → IC=+0.247 (n=3531)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.432 (IC base=+0.244)

- **PATRÓN** `libro_liquidez` > `2968.6954` → IC=+0.245 (n=1247)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2968.6954 (IC base=+0.244)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.201 (n=5947)

- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.244 (n=2151)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.221)

- **PATRÓN** `drift_60min` |x|≤ `0.5136` → IC=+0.230 (n=6433)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5136 (IC base=+0.221)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.229 (n=5833)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.221)

- **PATRÓN** `ibs_20min` > `0.9291` → IC=+0.257 (n=2147)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9291 (IC base=+0.221)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.506` → IC=+0.226 (n=2137)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.506 (IC base=+0.221)

- **PATRÓN** `volumen_regimen` < `0.7061` → IC=+0.231 (n=2071)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7061 (IC base=+0.221)

- **PATRÓN** `volumen_regimen` > `0.8808` → IC=+0.221 (n=3138)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8808 (IC base=+0.221)

- **PATRÓN** `volumen_pendiente_norm` < `0.105` → IC=+0.222 (n=6007)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.105 (IC base=+0.221)

- **PATRÓN** `volumen_pendiente_norm` > `0.165` → IC=+0.229 (n=1815)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.165 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` < `2.2548` → IC=+0.225 (n=5572)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.2548 (IC base=+0.221)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.226 (n=4816)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.221)

- **PATRÓN** `libro_liquidez` > `2588.138` → IC=+0.225 (n=6434)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2588.138 (IC base=+0.221)

- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.239 (n=1492)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.200)

- **PATRÓN** `drift_60min` |x|≤ `0.4977` → IC=+0.212 (n=4473)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4977 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.214 (n=1496)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.200)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.212 (n=1970)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.200)

- **PATRÓN** `ibs_20min` < `0.1849` → IC=+0.212 (n=1968)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1849 (IC base=+0.200)

- **PATRÓN** `dist_vwap_pct` > `0.6648` → IC=+0.210 (n=756)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6648 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.762` → IC=+0.212 (n=4026)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.762 (IC base=+0.200)

- **PATRÓN** `volumen_regimen` < `1.0965` → IC=+0.206 (n=3757)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0965 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` < `0.0976` → IC=+0.201 (n=4116)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0976 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` > `0.0733` → IC=+0.204 (n=1997)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0733 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` < `1.5315` → IC=+0.206 (n=1941)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5315 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` > `2.1859` → IC=+0.210 (n=1999)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1859 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.201 (n=5947)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.200)

- **PATRÓN** `ballena_activa_n` < `32.0` → IC=+0.223 (n=1966)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 32.0 (IC base=+0.200)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.276 (n=816)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0057 (IC base=+0.270)

- **PATRÓN** `sigma_h` > `0.0033` → IC=+0.272 (n=927)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0033 (IC base=+0.270)

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

- **PATRÓN** `volumen_spike_ratio` < `2.4871` → IC=+0.276 (n=923)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4871 (IC base=+0.270)

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
- **PATRÓN** `sigma_h` < `0.0083` → IC=+0.219 (n=1811)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0083 (IC base=+0.206)

- **PATRÓN** `drift_60min` |x|≤ `0.458` → IC=+0.214 (n=1811)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.458 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.232 (n=636)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.206)

- **PATRÓN** `ibs_20min` < `0.4728` → IC=+0.217 (n=1208)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4728 (IC base=+0.206)

- **PATRÓN** `ibs_20min` > `0.1444` → IC=+0.209 (n=1811)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1444 (IC base=+0.206)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.379` → IC=+0.213 (n=1837)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 6.379 (IC base=+0.206)

- **PATRÓN** `volumen_regimen` < `0.8685` → IC=+0.213 (n=1208)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8685 (IC base=+0.206)

- **PATRÓN** `volumen_pendiente_norm` < `0.102` → IC=+0.210 (n=1671)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.102 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` < `2.4261` → IC=+0.212 (n=1773)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4261 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` > `1.4939` → IC=+0.208 (n=1584)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4939 (IC base=+0.206)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.243 (n=477)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.201)

- **PATRÓN** `drift_60min` |x|≤ `0.4894` → IC=+0.221 (n=1420)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4894 (IC base=+0.201)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.205 (n=533)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.201)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.217 (n=959)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.201)

- **PATRÓN** `ibs_20min` < `0.1702` → IC=+0.205 (n=625)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1702 (IC base=+0.201)

- **PATRÓN** `ibs_20min` > `0.612` → IC=+0.207 (n=644)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.612 (IC base=+0.201)

- **PATRÓN** `dist_vwap_pct` > `0.6286` → IC=+0.218 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6286 (IC base=+0.201)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.281` → IC=+0.206 (n=1297)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.281 (IC base=+0.201)

- **PATRÓN** `volumen_regimen` < `1.2516` → IC=+0.210 (n=1420)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2516 (IC base=+0.201)

- **PATRÓN** `volumen_pendiente_norm` > `0.0728` → IC=+0.230 (n=584)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0728 (IC base=+0.201)

- **PATRÓN** `volumen_spike_ratio` < `1.4106` → IC=+0.210 (n=464)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4106 (IC base=+0.201)

- **PATRÓN** `volumen_spike_ratio` > `1.7842` → IC=+0.202 (n=928)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7842 (IC base=+0.201)

- **PATRÓN** `libro_liquidez` > `6555.044` → IC=+0.207 (n=1268)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6555.044 (IC base=+0.201)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0083` → IC=+0.236 (n=467)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0083 (IC base=+0.207)

- **PATRÓN** `hora_utc` > `10.0` → IC=+0.242 (n=726)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.207)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.286 (n=362)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.207)

- **PATRÓN** `dist_vwap_pct` > `0.7792` → IC=+0.235 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7792 (IC base=+0.207)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.202` → IC=+0.236 (n=581)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.202 (IC base=+0.207)

- **PATRÓN** `volumen_regimen` < `0.7088` → IC=+0.242 (n=467)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7088 (IC base=+0.207)

- **PATRÓN** `volumen_pendiente_norm` < `0.1062` → IC=+0.214 (n=960)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1062 (IC base=+0.207)

- **PATRÓN** `volumen_pendiente_norm` > `0.0799` → IC=+0.214 (n=466)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0799 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` < `2.1532` → IC=+0.216 (n=908)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1532 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` > `1.47` → IC=+0.212 (n=1032)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.47 (IC base=+0.207)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.215 (n=1239)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.207)

- **PATRÓN** `libro_liquidez` > `4106.249` → IC=+0.241 (n=481)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4106.249 (IC base=+0.207)

- **PATRÓN** `ballena_activa_n` < `38.0` → IC=+0.211 (n=924)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 38.0 (IC base=+0.207)

- **PATRÓN** `sigma_h` < `0.0132` → IC=+0.226 (n=742)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0132 (IC base=+0.226)

- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.245 (n=496)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0101 (IC base=+0.226)

- **PATRÓN** `drift_60min` |x|≤ `0.6042` → IC=+0.244 (n=741)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6042 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.227 (n=694)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.226)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.251 (n=512)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.226)

- **PATRÓN** `ibs_20min` < `0.7341` → IC=+0.252 (n=741)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7341 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.816` → IC=+0.240 (n=691)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.816 (IC base=+0.226)

- **PATRÓN** `volumen_regimen` < `0.756` → IC=+0.232 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.756 (IC base=+0.226)

- **PATRÓN** `volumen_regimen` > `1.2794` → IC=+0.235 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2794 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` < `0.0825` → IC=+0.238 (n=624)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0825 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` > `2.1932` → IC=+0.261 (n=328)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1932 (IC base=+0.226)

- **PATRÓN** `libro_liquidez` > `3814.5709` → IC=+0.240 (n=494)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3814.5709 (IC base=+0.226)

- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.263 (n=496)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 25.0 (IC base=+0.226)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.150 (n=752)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0038 (IC base=+0.055)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.185 (n=1444)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.75 (IC base=+0.055)

- **PATRÓN** `dist_vwap_pct` > `0.1434` → IC=+0.143 (n=1062)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.1434 (IC base=+0.055)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.365` → IC=+0.144 (n=479)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 10.365 (IC base=+0.055)

- **PATRÓN** `ibs_20min` < `0.0639` → IC=+0.263 (n=661)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0639 (IC base=+0.048)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `ibs_20min` < `0.5412` → IC=-0.121 (n=299)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5412
  - _Potencial_: sin este filtro IC_bueno=+0.165 (n=609)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.129 (n=628)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.64€ cuando `sigma_h` < 0.0053 (IC base=+0.070)

- **PATRÓN** `ibs_20min` > `0.5412` → IC=+0.165 (n=609)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` > 0.5412 (IC base=+0.070)

- **PATRÓN** `dist_vwap_pct` > `0.1215` → IC=+0.171 (n=323)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.1215 (IC base=+0.070)

- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.131 (n=272)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.66€ cuando `sigma_h` < 0.0035 (IC base=+0.044)

- **PATRÓN** `ibs_20min` < `0.0659` → IC=+0.264 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0659 (IC base=+0.044)

- **PATRÓN** `volumen_pendiente_norm` > `0.07` → IC=+0.124 (n=256)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` > 0.07 (IC base=+0.044)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` > `0.6751` → IC=-0.158 (n=159)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6751
  - _Potencial_: sin este filtro IC_bueno=+0.105 (n=479)

- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.151 (n=319)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0041 (IC base=+0.072)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.126 (n=359)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 15.0 (IC base=+0.072)

- **PATRÓN** `ibs_20min` > `0.5355` → IC=+0.169 (n=620)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` > 0.5355 (IC base=+0.072)

- **PATRÓN** `dist_vwap_pct` > `0.1272` → IC=+0.173 (n=337)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.1272 (IC base=+0.072)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.646` → IC=+0.205 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.646 (IC base=+0.072)

- **PATRÓN** `ibs_20min` < `0.1087` → IC=+0.251 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1087 (IC base=+0.023)

### GBM_LATE_60M#SOL#60min
- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.192 (n=261)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 1.0 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` > `0.4663` → IC=+0.127 (n=261)

  - _Acción_: Kelly boost +0.64€ cuando `dist_vwap_pct` > 0.4663 (IC base=+0.025)

- **PATRÓN** `sigma_h` < `0.0096` → IC=+0.185 (n=309)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0096 (IC base=+0.078)

- **PATRÓN** `ibs_20min` < `0.4857` → IC=+0.176 (n=433)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.4857 (IC base=+0.078)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.827` → IC=+0.276 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.827 (IC base=+0.078)

- **PATRÓN** `volumen_regimen` > `1.0831` → IC=+0.185 (n=144)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` > 1.0831 (IC base=+0.078)

- **PATRÓN** `volumen_pendiente_norm` > `0.1089` → IC=+0.161 (n=163)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.1089 (IC base=+0.078)

- **PATRÓN** `volumen_spike_ratio` > `1.4557` → IC=+0.125 (n=403)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` > 1.4557 (IC base=+0.078)

### GBM_LATE_60M_FADE
- **FILTRO** `hora_utc` > `7.0` → IC=-0.300 (n=93)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=287)

- **FILTRO** `dist_vwap_pct` > `0.2351` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2351
  - _Potencial_: sin este filtro IC_bueno=-0.216 (n=364)

- **FILTRO** `volumen_regimen` < `0.8567` → IC=-0.303 (n=125)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.8567
  - _Potencial_: sin este filtro IC_bueno=-0.181 (n=255)

- **FILTRO** `hora_utc` > `11.0` → IC=-0.309 (n=150)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.251 (n=183)

- **FILTRO** `dist_vwap_pct` > `0.4428` → IC=-0.409 (n=20)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4428
  - _Potencial_: sin este filtro IC_bueno=-0.268 (n=313)

- **FILTRO** `sigma_ewma_delta_pct` > `9.697` → IC=-0.328 (n=27)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 9.697
  - _Potencial_: sin este filtro IC_bueno=-0.273 (n=306)

- **FILTRO** `volumen_pendiente_norm` > `0.0453` → IC=-0.375 (n=30)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0453
  - _Potencial_: sin este filtro IC_bueno=-0.264 (n=214)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `sigma_h` > `0.0054` → IC=-0.269 (n=37)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0054
  - _Potencial_: sin este filtro IC_bueno=-0.224 (n=74)

- **FILTRO** `hora_utc` > `9.0` → IC=-0.286 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.224 (n=85)

- **FILTRO** `sigma_h` < `0.0033` → IC=-0.257 (n=72)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0033
  - _Potencial_: sin este filtro IC_bueno=-0.240 (n=75)

- **FILTRO** `hora_utc` < `12.0` → IC=-0.278 (n=70)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.222 (n=77)

- **FILTRO** `ibs_20min` > `0.7502` → IC=-0.265 (n=49)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7502
  - _Potencial_: sin este filtro IC_bueno=-0.240 (n=98)

- **FILTRO** `volumen_regimen` > `0.805` → IC=-0.316 (n=36)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.226 (n=111)

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

- **FILTRO** `dist_vwap_pct` > `0.1281` → IC=-0.353 (n=32)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1281
  - _Potencial_: sin este filtro IC_bueno=-0.288 (n=97)

- **FILTRO** `volumen_spike_ratio` < `1.4324` → IC=-0.380 (n=23)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.4324
  - _Potencial_: sin este filtro IC_bueno=-0.294 (n=71)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.302 (n=114)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `drift_60min` |x|> `0.2366` → IC=-0.357 (n=33)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2366
  - _Potencial_: sin este filtro IC_bueno=-0.195 (n=103)

- **FILTRO** `dist_vwap_pct` > `0.0767` → IC=-0.242 (n=29)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.0767
  - _Potencial_: sin este filtro IC_bueno=-0.236 (n=108)

- **FILTRO** `volumen_pendiente_norm` > `0.1196` → IC=-0.258 (n=31)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1196
  - _Potencial_: sin este filtro IC_bueno=-0.235 (n=81)

- **FILTRO** `volumen_spike_ratio` > `2.3386` → IC=-0.275 (n=38)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.3386
  - _Potencial_: sin este filtro IC_bueno=-0.224 (n=74)

- **FILTRO** `libro_spread` > `0.06` → IC=-0.250 (n=30)

  - _Acción_: SKIP cuando `libro_spread` > 0.06
  - _Potencial_: sin este filtro IC_bueno=-0.234 (n=107)

- **FILTRO** `sigma_h` < `0.0112` → IC=-0.341 (n=42)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0112
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=15)

- **FILTRO** `sigma_ewma_delta_pct` > `4.698` → IC=-0.382 (n=15)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.698
  - _Potencial_: sin este filtro IC_bueno=-0.204 (n=42)

- **FILTRO** `volumen_regimen` < `0.9051` → IC=-0.450 (n=18)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9051
  - _Potencial_: sin este filtro IC_bueno=-0.159 (n=39)

### GBM_LATE_60M_PYCONFIRMADO
- **PATRÓN** `sigma_h` > `0.0086` → IC=+0.265 (n=241)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0086 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.195 (n=375)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 15.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` > `0.6774` → IC=+0.183 (n=723)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` > 0.6774 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` > `0.8064` → IC=+0.287 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8064 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.4` → IC=+0.169 (n=167)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 10.4 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` < `0.6244` → IC=+0.183 (n=241)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 0.6244 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` > `1.2146` → IC=+0.150 (n=241)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 1.2146 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` < `0.0701` → IC=+0.180 (n=538)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` < 0.0701 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `1.3986` → IC=+0.202 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3986 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.489` → IC=+0.155 (n=198)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 10.489 (IC base=+0.032)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.725` → IC=-0.153 (n=70)

  - _Acción_: SKIP cuando `ibs_20min` < 0.725
  - _Potencial_: sin este filtro IC_bueno=+0.105 (n=213)

- **PATRÓN** `sigma_h` > `0.0065` → IC=+0.149 (n=72)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` > 0.0065 (IC base=+0.040)

- **PATRÓN** `ibs_20min` > `0.9138` → IC=+0.132 (n=142)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` > 0.9138 (IC base=+0.040)

- **PATRÓN** `dist_vwap_pct` > `0.6135` → IC=+0.207 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6135 (IC base=+0.040)

- **PATRÓN** `ibs_20min` < `0.2365` → IC=+0.145 (n=404)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.2365 (IC base=+0.087)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.347` → IC=+0.122 (n=125)

  - _Acción_: Kelly boost +0.61€ cuando `sigma_ewma_delta_pct` > 9.347 (IC base=+0.087)

- **PATRÓN** `volumen_pendiente_norm` > `0.273` → IC=+0.143 (n=68)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` > 0.273 (IC base=+0.087)

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

- **PATRÓN** `volumen_regimen` < `0.6244` → IC=+0.175 (n=81)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.6244 (IC base=+0.116)

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
- **FILTRO** `ibs_20min` > `0.1875` → IC=-0.231 (n=65)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1875
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=127)

- **FILTRO** `dist_vwap_pct` > `0.1816` → IC=-0.167 (n=37)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1816
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=155)

- **PATRÓN** `sigma_h` > `0.01` → IC=+0.300 (n=123)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.01 (IC base=+0.256)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.302 (n=190)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.256)

- **PATRÓN** `ibs_20min` > `0.5882` → IC=+0.284 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5882 (IC base=+0.256)

- **PATRÓN** `dist_vwap_pct` > `0.6973` → IC=+0.394 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6973 (IC base=+0.256)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.832` → IC=+0.359 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.832 (IC base=+0.256)

- **PATRÓN** `volumen_regimen` < `0.5991` → IC=+0.304 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.5991 (IC base=+0.256)

- **PATRÓN** `volumen_pendiente_norm` > `0.0973` → IC=+0.327 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0973 (IC base=+0.256)

- **PATRÓN** `volumen_spike_ratio` < `1.396` → IC=+0.336 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.396 (IC base=+0.256)

- **PATRÓN** `volumen_spike_ratio` > `2.3741` → IC=+0.308 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3741 (IC base=+0.256)

### LATE_WINDOW_5MIN
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.328 (n=114)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3645` → IC=+0.338 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3645 (IC base=+0.322)

- **PATRÓN** `elapsed_s` > `207.0` → IC=+0.400 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 207.0 (IC base=+0.322)

- **PATRÓN** `drift_15min` |x|≤ `1.0295` → IC=+0.406 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0295 (IC base=+0.322)

- **PATRÓN** `drift_60min` |x|≤ `0.7805` → IC=+0.373 (n=77)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.7805 (IC base=+0.322)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.389 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.322)

- **PATRÓN** `ballena_activa_n` < `1114.0` → IC=+0.344 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1114.0 (IC base=+0.322)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3488` → IC=+0.300 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3488 (IC base=+0.267)

- **PATRÓN** `elapsed_s` > `229.9` → IC=+0.329 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 229.9 (IC base=+0.267)

- **PATRÓN** `elapsed_s` < `203.6` → IC=+0.265 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 203.6 (IC base=+0.267)

- **PATRÓN** `drift_15min` |x|≤ `2.3044` → IC=+0.309 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3044 (IC base=+0.267)

- **PATRÓN** `drift_60min` |x|≤ `0.6365` → IC=+0.309 (n=66)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6365 (IC base=+0.267)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.328 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.267)

- **PATRÓN** `ballena_activa_n` < `1768.0` → IC=+0.312 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1768.0 (IC base=+0.267)

### LATE_WINDOW_5MIN#BTC#5min
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.328 (n=114)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3645` → IC=+0.338 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3645 (IC base=+0.322)

- **PATRÓN** `elapsed_s` > `207.0` → IC=+0.400 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 207.0 (IC base=+0.322)

- **PATRÓN** `drift_15min` |x|≤ `1.0295` → IC=+0.406 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0295 (IC base=+0.322)

- **PATRÓN** `drift_60min` |x|≤ `0.7805` → IC=+0.373 (n=77)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.7805 (IC base=+0.322)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.389 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.322)

- **PATRÓN** `ballena_activa_n` < `1114.0` → IC=+0.344 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1114.0 (IC base=+0.322)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3488` → IC=+0.300 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3488 (IC base=+0.267)

- **PATRÓN** `elapsed_s` > `229.9` → IC=+0.329 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 229.9 (IC base=+0.267)

- **PATRÓN** `elapsed_s` < `203.6` → IC=+0.265 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 203.6 (IC base=+0.267)

- **PATRÓN** `drift_15min` |x|≤ `2.3044` → IC=+0.309 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3044 (IC base=+0.267)

- **PATRÓN** `drift_60min` |x|≤ `0.6365` → IC=+0.309 (n=66)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6365 (IC base=+0.267)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.328 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.267)

- **PATRÓN** `ballena_activa_n` < `1768.0` → IC=+0.312 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1768.0 (IC base=+0.267)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.124 (n=1463)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` > 0.5 (IC base=+0.098)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.124 (n=1463)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` > 0.5 (IC base=+0.098)

### LIQUIDACIONES_15M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=248)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=248)

- **FILTRO** `libro_liquidez` < `3490.7365` → IC=-0.174 (n=87)

  - _Acción_: SKIP cuando `libro_liquidez` < 3490.7365
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=177)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=877)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `libro_liquidez` < `12324.2702` → IC=-0.152 (n=44)

  - _Acción_: SKIP cuando `libro_liquidez` < 12324.2702
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=90)

### LIQUIDACIONES_15M#DOGE#15min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.152 (n=21)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.154 (n=24)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.154 (n=24)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 10.0 (IC base=+0.011)

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
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=3942)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=152)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=109)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.278 (n=34)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=139)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.188 (n=46)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 21.0 (IC base=-0.077)

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
- **PATRÓN** `liq_n` > `3.0` → IC=+0.333 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `liq_n` > 3.0 (IC base=+0.196)

- **PATRÓN** `liq_usd_total` > `1930.81` → IC=+0.328 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `liq_usd_total` > 1930.81 (IC base=+0.196)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.258 (n=31)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.210 (n=36)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.227 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.505 (IC base=+0.196)

- **PATRÓN** `libro_liquidez` > `2323.928` → IC=+0.218 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2323.928 (IC base=+0.196)

- **PATRÓN** `ballena_activa_n` < `6.0` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 6.0 (IC base=+0.196)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=1607)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=1561)

- **FILTRO** `liq_n` < `3.0` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `liq_n` < 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **FILTRO** `liq_usd_total` < `6520.36` → IC=-0.220 (n=23)

  - _Acción_: SKIP cuando `liq_usd_total` < 6520.36
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=13)

- **FILTRO** `ballena_activa_n` > `133.0` → IC=-0.250 (n=18)

  - _Acción_: SKIP cuando `ballena_activa_n` > 133.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

### LIQUIDACIONES_5M#SOL#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=729)

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
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=448)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=429)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.141 (n=193)

  - _Acción_: Kelly boost +0.71€ cuando `py_entrada` < 0.495 (IC base=+0.021)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=1013)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=1013)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=1280)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=1280)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=293)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=293)

- **FILTRO** `py_entrada` < `0.42` → IC=-0.141 (n=76)

  - _Acción_: SKIP cuando `py_entrada` < 0.42
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=232)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.136 (n=64)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=352)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=401)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=301)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=404)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=404)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.120 (n=185)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=249)

- **FILTRO** `libro_liquidez` < `553.1995` → IC=-0.145 (n=108)

  - _Acción_: SKIP cuando `libro_liquidez` < 553.1995
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=326)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=366)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.188 (n=78)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=99)

- **FILTRO** `hora_utc` > `14.0` → IC=-0.155 (n=82)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=95)

- **FILTRO** `py_entrada` > `0.52` → IC=-0.121 (n=56)

  - _Acción_: SKIP cuando `py_entrada` > 0.52
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=30)

- **FILTRO** `hora_utc` < `17.0` → IC=-0.131 (n=63)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=23)

### LIQUIDACIONES_DEPTH_FASE0#BTC#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.131 (n=296)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=733)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **FILTRO** `py_entrada` > `0.57` → IC=-0.128 (n=434)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.086 (n=515)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.145 (n=316)

  - _Acción_: Kelly boost +0.72€ cuando `py_entrada` < 0.5 (IC base=-0.012)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` > `0.57` → IC=-0.123 (n=364)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=373)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` > `0.58` → IC=-0.128 (n=347)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=411)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.131 (n=272)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=588)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.44` → IC=-0.137 (n=516)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=519)

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
- **FILTRO** `py_entrada` < `0.46` → IC=-0.175 (n=7993)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=25476)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.174 (n=8483)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=26065)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.188 (n=1550)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.118 (n=4659)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.149 (n=2065)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.094 (n=4055)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.135 (n=1603)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` > 1.0 (IC base=+0.041)

- **PATRÓN** `py_entrada` < `0.505` → IC=+0.126 (n=3108)

  - _Acción_: Kelly boost +0.63€ cuando `py_entrada` < 0.505 (IC base=+0.012)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` < `0.44` → IC=-0.173 (n=1110)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=3532)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.179 (n=1188)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=3666)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` > `0.62` → IC=-0.203 (n=1539)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.087 (n=4741)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.137 (n=1910)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` > 1.0 (IC base=+0.034)

- **PATRÓN** `libro_liquidez` > `1738.668` → IC=+0.120 (n=2105)

  - _Acción_: Kelly boost +0.60€ cuando `libro_liquidez` > 1738.668 (IC base=+0.034)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.485` → IC=-0.161 (n=1545)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=4684)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=2439)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.162 (n=772)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=2363)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.180 (n=973)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=3066)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=4018)

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
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=1080)

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
  - _Potencial_: sin este filtro IC_bueno=-0.102 (n=362)

- **FILTRO** `ballena_activa_n` > `84.0` → IC=-0.179 (n=157)

  - _Acción_: SKIP cuando `ballena_activa_n` > 84.0
  - _Potencial_: sin este filtro IC_bueno=-0.103 (n=310)

- **FILTRO** `libro_liquidez` < `3222.056` → IC=-0.183 (n=156)

  - _Acción_: SKIP cuando `libro_liquidez` < 3222.056
  - _Potencial_: sin este filtro IC_bueno=-0.098 (n=319)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_liquidez` < `1823.8789` → IC=-0.168 (n=248)

  - _Acción_: SKIP cuando `libro_liquidez` < 1823.8789
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=746)

- **FILTRO** `ballena_activa_n` > `23.0` → IC=-0.191 (n=390)

  - _Acción_: SKIP cuando `ballena_activa_n` > 23.0
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=796)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.135 (n=22738)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.090 (n=51330)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.298 (n=17796)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=56272)

- **FILTRO** `ibs_7min` < `0.2158` → IC=-0.234 (n=18515)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2158
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=55553)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.152 (n=25163)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=48905)

- **FILTRO** `py_entrada` > `0.68` → IC=-0.252 (n=21630)

  - _Acción_: SKIP cuando `py_entrada` > 0.68
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=70898)

- **FILTRO** `ibs_7min` > `0.2821` → IC=-0.184 (n=23127)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2821
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=69401)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.157 (n=3189)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=10019)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.317 (n=3263)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=9945)

- **FILTRO** `ibs_7min` < `0.7105` → IC=-0.251 (n=4357)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7105
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=8851)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.153 (n=2787)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=10421)

- **FILTRO** `py_entrada` > `0.72` → IC=-0.277 (n=3908)

  - _Acción_: SKIP cuando `py_entrada` > 0.72
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=12068)

- **FILTRO** `ibs_7min` > `0.7778` → IC=-0.211 (n=3990)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7778
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=11986)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.264 (n=2977)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=9348)

- **FILTRO** `ibs_7min` < `0.7139` → IC=-0.209 (n=3080)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7139
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=9245)

- **FILTRO** `ballena_activa_n` > `156.0` → IC=-0.202 (n=3063)

  - _Acción_: SKIP cuando `ballena_activa_n` > 156.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=9262)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.267 (n=2879)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=9686)

- **FILTRO** `ibs_7min` > `0.2664` → IC=-0.193 (n=3139)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2664
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=9426)

- **FILTRO** `ballena_activa_n` > `153.0` → IC=-0.181 (n=3135)

  - _Acción_: SKIP cuando `ballena_activa_n` > 153.0
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=9430)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.166 (n=3051)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=9594)

- **FILTRO** `py_entrada` < `0.3` → IC=-0.325 (n=3011)

  - _Acción_: SKIP cuando `py_entrada` < 0.3
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=9634)

- **FILTRO** `ibs_7min` < `0.2857` → IC=-0.251 (n=4165)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2857
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=8480)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.202 (n=2514)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=10131)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.260 (n=4099)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=12822)

- **FILTRO** `ibs_7min` > `0.7308` → IC=-0.183 (n=4230)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7308
  - _Potencial_: sin este filtro IC_bueno=-0.000 (n=12691)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.263 (n=2976)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=9005)

- **FILTRO** `ibs_7min` < `0.7143` → IC=-0.196 (n=2995)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7143
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=8986)

- **FILTRO** `ballena_activa_n` > `25.0` → IC=-0.191 (n=2906)

  - _Acción_: SKIP cuando `ballena_activa_n` > 25.0
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=9075)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.260 (n=2892)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=9564)

- **FILTRO** `ibs_7min` > `0.2732` → IC=-0.178 (n=3112)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2732
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=9344)

- **FILTRO** `ballena_activa_n` > `24.0` → IC=-0.173 (n=3022)

  - _Acción_: SKIP cuando `ballena_activa_n` > 24.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=9434)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.32` → IC=-0.300 (n=2818)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=9039)

- **FILTRO** `ibs_7min` < `0.7` → IC=-0.235 (n=3856)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=8001)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.218 (n=2914)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=8943)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.199 (n=4351)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=13552)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.131 (n=3879)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.108 (n=8173)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.309 (n=2885)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=9167)

- **FILTRO** `ibs_7min` < `0.7353` → IC=-0.220 (n=3973)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7353
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=8079)

- **FILTRO** `ballena_activa_n` > `9.0` → IC=-0.205 (n=2668)

  - _Acción_: SKIP cuando `ballena_activa_n` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.090 (n=9384)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.234 (n=3867)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=12840)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1046` → IC=-0.135 (n=61)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1046
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=121)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `py_entrada` < `0.455` → IC=-0.163 (n=304)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=1013)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=1302)

- **FILTRO** `py_entrada` > `0.545` → IC=-0.157 (n=170)

  - _Acción_: SKIP cuando `py_entrada` > 0.545
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=625)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=1458)

- **FILTRO** `py_entrada` > `0.565` → IC=-0.172 (n=260)

  - _Acción_: SKIP cuando `py_entrada` > 0.565
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=898)

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
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=580)

- **FILTRO** `libro_liquidez` < `3304.2295` → IC=-0.151 (n=193)

  - _Acción_: SKIP cuando `libro_liquidez` < 3304.2295
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=579)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=396)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.4308` → IC=+0.149 (n=691)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.75€ cuando `delta_ratio` |x|> 0.4308 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.128 (n=1370)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 14.0 (IC base=+0.124)

- **PATRÓN** `total_vol_5m` < `421.686` → IC=+0.161 (n=508)

  - _Acción_: Kelly boost +0.80€ cuando `total_vol_5m` < 421.686 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `3557.0392` → IC=+0.138 (n=691)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 3557.0392 (IC base=+0.124)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `14.0` → IC=+0.181 (n=183)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 14.0 (IC base=+0.134)

- **PATRÓN** `total_vol_5m` < `371.804` → IC=+0.156 (n=318)

  - _Acción_: Kelly boost +0.78€ cuando `total_vol_5m` < 371.804 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `2506.369` → IC=+0.240 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2506.369 (IC base=+0.134)

- **PATRÓN** `ballena_activa_n` < `6.0` → IC=+0.136 (n=174)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 6.0 (IC base=+0.134)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `delta_ratio` |x|> `0.4378` → IC=+0.157 (n=106)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.79€ cuando `delta_ratio` |x|> 0.4378 (IC base=+0.119)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.138 (n=291)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 15.0 (IC base=+0.119)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.124 (n=378)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.04 (IC base=+0.119)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4165` → IC=+0.174 (n=191)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.87€ cuando `delta_ratio` |x|> 0.4165 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.145 (n=266)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.125)

- **PATRÓN** `total_vol_5m` < `857.788` → IC=+0.150 (n=287)

  - _Acción_: Kelly boost +0.75€ cuando `total_vol_5m` < 857.788 (IC base=+0.125)

- **PATRÓN** `ballena_activa_n` < `59.0` → IC=+0.173 (n=96)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 59.0 (IC base=+0.125)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.4317` → IC=+0.208 (n=118)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio` |x|> 0.4317 (IC base=+0.143)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.174 (n=188)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 12.0 (IC base=+0.143)

- **PATRÓN** `total_vol_5m` < `4621.455` → IC=+0.180 (n=173)

  - _Acción_: Kelly boost +0.90€ cuando `total_vol_5m` < 4621.455 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `3712.2533` → IC=+0.163 (n=173)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 3712.2533 (IC base=+0.143)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `hora_utc` < `14.0` → IC=+0.130 (n=279)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 14.0 (IC base=+0.099)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.134 (n=203)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.099)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `4.8182` → IC=-0.203 (n=116)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.8182
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=118)

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.147 (n=287)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0045 (IC base=-0.062)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `T_h` > `88.1766` → IC=-0.212 (n=64)

  - _Acción_: SKIP cuando `T_h` > 88.1766
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=196)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.286 (n=87)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=-0.015)

- **PATRÓN** `pct_vs_K` |x|≤ `1.73` → IC=+0.182 (n=86)

  - _Acción_: Kelly boost +0.91€ cuando `pct_vs_K` |x|≤ 1.73 (IC base=-0.015)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `sigma_h` > `0.0107` → IC=-0.136 (n=20)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0107
  - _Potencial_: sin este filtro IC_bueno=-0.121 (n=64)

- **FILTRO** `pct_vs_K` |x|> `6.6759` → IC=-0.267 (n=28)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 6.6759
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=56)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0153` → IC=-0.151 (n=41)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0153
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=125)

- **FILTRO** `T_h` < `95.4178` → IC=-0.171 (n=83)

  - _Acción_: SKIP cuando `T_h` < 95.4178
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=83)

### PRICE_TARGET_GBM#SOL#reach
- **FILTRO** `T_h` < `146.0708` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `T_h` < 146.0708
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=16)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0114` → IC=-0.234 (n=591)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0114
  - _Potencial_: sin este filtro IC_bueno=-0.190 (n=198)

- **FILTRO** `T_h` > `68.7654` → IC=-0.228 (n=528)

  - _Acción_: SKIP cuando `T_h` > 68.7654
  - _Potencial_: sin este filtro IC_bueno=-0.211 (n=261)

- **FILTRO** `pct_vs_K` |x|> `3.0379` → IC=-0.395 (n=170)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.0379
  - _Potencial_: sin este filtro IC_bueno=-0.109 (n=517)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `sigma_h` < `0.0086` → IC=-0.209 (n=170)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0086
  - _Potencial_: sin este filtro IC_bueno=-0.170 (n=89)

- **FILTRO** `T_h` > `143.4358` → IC=-0.238 (n=63)

  - _Acción_: SKIP cuando `T_h` > 143.4358
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=190)

- **FILTRO** `T_h` < `90.3399` → IC=-0.253 (n=83)

  - _Acción_: SKIP cuando `T_h` < 90.3399
  - _Potencial_: sin este filtro IC_bueno=-0.169 (n=170)

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
- **FILTRO** `sigma_h` < `0.0111` → IC=-0.300 (n=168)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0111
  - _Potencial_: sin este filtro IC_bueno=-0.224 (n=56)

- **FILTRO** `sigma_h` > `0.0091` → IC=-0.368 (n=51)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0091
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=156)

- **FILTRO** `T_h` > `56.8566` → IC=-0.221 (n=138)

  - _Acción_: SKIP cuando `T_h` > 56.8566
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=69)

- **PATRÓN** `pct_vs_K` |x|≤ `0.8096` → IC=+0.204 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `pct_vs_K` |x|≤ 0.8096 (IC base=-0.151)

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
- **FILTRO** `sigma_h` < `0.0083` → IC=-0.254 (n=55)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0083
  - _Potencial_: sin este filtro IC_bueno=-0.173 (n=166)

- **FILTRO** `T_h` > `65.6683` → IC=-0.225 (n=165)

  - _Acción_: SKIP cuando `T_h` > 65.6683
  - _Potencial_: sin este filtro IC_bueno=-0.103 (n=56)

- **FILTRO** `sigma_h` > `0.014` → IC=-0.308 (n=50)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.014
  - _Potencial_: sin este filtro IC_bueno=-0.137 (n=100)

- **FILTRO** `sigma_h` < `0.0103` → IC=-0.265 (n=49)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0103
  - _Potencial_: sin este filtro IC_bueno=-0.160 (n=101)

- **FILTRO** `T_h` < `111.9918` → IC=-0.219 (n=112)

  - _Acción_: SKIP cuando `T_h` < 111.9918
  - _Potencial_: sin este filtro IC_bueno=-0.125 (n=38)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1186` → IC=+0.452 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1186 (IC base=+0.328)

- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.385 (n=76)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0104 (IC base=+0.328)

- **PATRÓN** `T_h` < `0.3261` → IC=+0.400 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.3261 (IC base=+0.328)

- **PATRÓN** `T_h` > `0.4292` → IC=+0.356 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.4292 (IC base=+0.328)

- **PATRÓN** `dist_50` > `0.3298` → IC=+0.433 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3298 (IC base=+0.328)

- **PATRÓN** `edge` > `0.0997` → IC=+0.429 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.0997 (IC base=+0.390)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.401 (n=89)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0075 (IC base=+0.390)

- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.411 (n=177)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0097 (IC base=+0.390)

- **PATRÓN** `T_h` < `0.7119` → IC=+0.416 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.7119 (IC base=+0.390)

- **PATRÓN** `T_h` > `1.4829` → IC=+0.401 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4829 (IC base=+0.390)

- **PATRÓN** `dist_50` > `0.366` → IC=+0.444 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.366 (IC base=+0.390)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.412 (n=327)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.390)

### RESOLUTION_SNIPER#BTC#sniper
- **PATRÓN** `edge` > `0.1021` → IC=+0.276 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1021 (IC base=+0.163)

- **PATRÓN** `sigma_h` < `0.0077` → IC=+0.250 (n=38)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0077 (IC base=+0.163)

- **PATRÓN** `T_h` < `0.5574` → IC=+0.214 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.5574 (IC base=+0.163)

- **PATRÓN** `T_h` > `1.484` → IC=+0.210 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.484 (IC base=+0.163)

- **PATRÓN** `dist_50` > `0.322` → IC=+0.297 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.322 (IC base=+0.163)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.219 (n=55)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.163)

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
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=430)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.073 (n=481)

- **PATRÓN** `streak_estiramiento` < `0.8196` → IC=+0.128 (n=331)

  - _Acción_: Kelly boost +0.64€ cuando `streak_estiramiento` < 0.8196 (IC base=+0.061)

- **PATRÓN** `ballena_activa_n` < `30.0` → IC=+0.124 (n=248)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 30.0 (IC base=+0.061)

### STREAK_FADE_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=17)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` < 0.495 (IC base=+0.091)

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
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=173)

- **PATRÓN** `streak_estiramiento` < `0.228` → IC=+0.127 (n=65)

  - _Acción_: Kelly boost +0.63€ cuando `streak_estiramiento` < 0.228 (IC base=+0.035)

- **PATRÓN** `streak_estiramiento` < `0.555` → IC=+0.165 (n=159)

  - _Acción_: Kelly boost +0.82€ cuando `streak_estiramiento` < 0.555 (IC base=+0.095)

- **PATRÓN** `ballena_activa_n` < `31.0` → IC=+0.158 (n=153)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 31.0 (IC base=+0.095)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `streak_len` > `5.0` → IC=-0.250 (n=22)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=114)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.208 (n=22)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=114)

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
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=1070)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=1344)

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
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=5001)

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
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=2866)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.189 (n=1803)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0054 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.221` → IC=+0.159 (n=5407)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.221 (IC base=+0.141)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1345` → IC=+0.154 (n=2224)

  - _Acción_: Kelly boost +0.77€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1345 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.150 (n=4992)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 6.0 (IC base=+0.141)

- **PATRÓN** `ibs_15` > `0.5789` → IC=+0.224 (n=4833)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5789 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` > `0.1346` → IC=+0.132 (n=2554)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` > 0.1346 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` < `0.3254` → IC=+0.125 (n=4563)

  - _Acción_: Kelly boost +0.63€ cuando `dist_vwap_pct` < 0.3254 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.322` → IC=+0.246 (n=1026)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.322 (IC base=+0.141)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=3089)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `4537.2825` → IC=+0.169 (n=1803)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 4537.2825 (IC base=+0.141)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=2068)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.221 (n=796)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0057 (IC base=+0.201)

- **PATRÓN** `drift_60min` |x|≤ `0.0593` → IC=+0.254 (n=266)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0593 (IC base=+0.201)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2678` → IC=+0.223 (n=265)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2678 (IC base=+0.201)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.226 (n=731)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.201)

- **PATRÓN** `ibs_15` > `0.7077` → IC=+0.273 (n=795)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7077 (IC base=+0.201)

- **PATRÓN** `dist_vwap_pct` > `0.3735` → IC=+0.225 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3735 (IC base=+0.201)

- **PATRÓN** `dist_vwap_pct` < `0.1104` → IC=+0.202 (n=534)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1104 (IC base=+0.201)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.43` → IC=+0.312 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.43 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.203 (n=1030)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.201)

- **PATRÓN** `libro_liquidez` > `11862.3083` → IC=+0.218 (n=530)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11862.3083 (IC base=+0.201)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.149 (n=993)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0071 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.1094` → IC=+0.154 (n=662)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.1094 (IC base=+0.133)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1407` → IC=+0.134 (n=662)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.67€ cuando `delta_ratio_macro` |x|> 0.1407 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.139 (n=906)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 6.0 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.134 (n=995)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 16.0 (IC base=+0.133)

- **PATRÓN** `ibs_15` > `0.4963` → IC=+0.220 (n=993)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.4963 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` > `0.1187` → IC=+0.151 (n=623)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.1187 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.945` → IC=+0.282 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.945 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `5973.6174` → IC=+0.173 (n=450)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 5973.6174 (IC base=+0.133)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `ibs_15` > `0.2568` → IC=-0.125 (n=214)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.2568
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=417)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `ibs_15` > `0.5909` → IC=+0.122 (n=1020)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.61€ cuando `ibs_15` > 0.5909 (IC base=+0.053)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` < `0.0254` → IC=+0.166 (n=1350)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0254 (IC base=+0.153)

- **PATRÓN** `sigma_h` > `0.0133` → IC=+0.155 (n=1350)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` > 0.0133 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.225` → IC=+0.177 (n=1350)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.225 (IC base=+0.153)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0978` → IC=+0.220 (n=416)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0978 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.159 (n=1235)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 6.0 (IC base=+0.153)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.159 (n=1194)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 14.0 (IC base=+0.153)

- **PATRÓN** `ibs_15` > `0.5429` → IC=+0.227 (n=1206)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5429 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` > `0.5304` → IC=+0.186 (n=317)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.5304 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.029` → IC=+0.199 (n=300)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 18.029 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `2945.8249` → IC=+0.199 (n=612)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 2945.8249 (IC base=+0.153)

- **PATRÓN** `ibs_15` < `0.1094` → IC=+0.153 (n=1034)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.77€ cuando `ibs_15` < 0.1094 (IC base=+0.068)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` > `0.0054` → IC=+0.392 (n=342)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0054 (IC base=+0.364)

- **PATRÓN** `drift_60min` |x|≤ `0.1117` → IC=+0.365 (n=503)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1117 (IC base=+0.364)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1503` → IC=+0.379 (n=502)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1503 (IC base=+0.364)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1351` → IC=+0.382 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1351 (IC base=+0.364)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.372 (n=796)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.364)

- **PATRÓN** `ibs_15` > `0.7903` → IC=+0.393 (n=754)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7903 (IC base=+0.364)

- **PATRÓN** `dist_vwap_pct` > `0.1534` → IC=+0.380 (n=448)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1534 (IC base=+0.364)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.085` → IC=+0.397 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.085 (IC base=+0.364)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.367 (n=919)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.364)

- **PATRÓN** `libro_liquidez` > `9641.0136` → IC=+0.381 (n=342)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9641.0136 (IC base=+0.364)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
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

- **PATRÓN** `ballena_activa_n` < `413.0` → IC=+0.389 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 413.0 (IC base=+0.362)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.369 (n=386)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.364)

- **PATRÓN** `sigma_h` > `0.006` → IC=+0.381 (n=175)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.006 (IC base=+0.364)

- **PATRÓN** `drift_60min` |x|≤ `0.1078` → IC=+0.369 (n=258)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1078 (IC base=+0.364)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1293` → IC=+0.381 (n=258)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1293 (IC base=+0.364)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2969` → IC=+0.374 (n=316)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2969 (IC base=+0.364)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.369 (n=387)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.364)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.373 (n=179)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.364)

- **PATRÓN** `ibs_15` > `0.7632` → IC=+0.392 (n=386)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7632 (IC base=+0.364)

- **PATRÓN** `dist_vwap_pct` > `0.159` → IC=+0.373 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.159 (IC base=+0.364)

- **PATRÓN** `dist_vwap_pct` < `0.2798` → IC=+0.365 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2798 (IC base=+0.364)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.991` → IC=+0.393 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.991 (IC base=+0.364)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.368 (n=438)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.364)

- **PATRÓN** `libro_liquidez` > `4150.4977` → IC=+0.376 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4150.4977 (IC base=+0.364)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0075` → IC=-0.197 (n=2721)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0075
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=2722)

- **FILTRO** `drift_15min` |x|> `0.9123` → IC=-0.147 (n=1360)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.9123
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=4082)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.219 (n=2297)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=3146)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1411` → IC=+0.215 (n=468)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1411 (IC base=-0.082)

- **PATRÓN** `ibs_15` > `0.6306` → IC=+0.278 (n=1234)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6306 (IC base=-0.082)

- **PATRÓN** `dist_vwap_pct` > `0.1103` → IC=+0.201 (n=724)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1103 (IC base=-0.082)

- **PATRÓN** `dist_vwap_pct` < `0.2596` → IC=+0.198 (n=1055)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` < 0.2596 (IC base=-0.082)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2344` → IC=+0.270 (n=1661)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2344 (IC base=-0.004)

- **PATRÓN** `ibs_15` < `0.3704` → IC=+0.284 (n=4983)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3704 (IC base=-0.004)

- **PATRÓN** `dist_vwap_pct` > `0.6509` → IC=+0.279 (n=689)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6509 (IC base=-0.004)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0321` → IC=-0.220 (n=2588)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0321
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=864)

- **FILTRO** `sigma_h` < `0.0038` → IC=-0.216 (n=863)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0038
  - _Potencial_: sin este filtro IC_bueno=-0.175 (n=2589)

- **FILTRO** `sigma_ewma_delta_pct` > `22.185` → IC=-0.254 (n=489)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 22.185
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=2963)

- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.154 (n=330)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0031 (IC base=+0.071)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2673` → IC=+0.288 (n=144)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2673 (IC base=+0.071)

- **PATRÓN** `ibs_15` > `0.7593` → IC=+0.320 (n=431)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7593 (IC base=+0.071)

- **PATRÓN** `dist_vwap_pct` > `0.1039` → IC=+0.276 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1039 (IC base=+0.071)

- **PATRÓN** `dist_vwap_pct` < `0.2429` → IC=+0.278 (n=386)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2429 (IC base=+0.071)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.251` → IC=+0.150 (n=221)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 22.251 (IC base=+0.071)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0742` → IC=+0.224 (n=74)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0742 (IC base=-0.186)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0866` → IC=+0.308 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0866 (IC base=-0.186)

- **PATRÓN** `ibs_15` < `0.6255` → IC=+0.289 (n=74)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.6255 (IC base=-0.186)

- **PATRÓN** `dist_vwap_pct` < `0.0453` → IC=+0.303 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0453 (IC base=-0.186)

- **PATRÓN** `ballena_activa_n` < `393.0` → IC=+0.300 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 393.0 (IC base=-0.186)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.154 (n=807)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.161 (n=544)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0059 (IC base=+0.148)

- **PATRÓN** `sigma_h` > `0.0052` → IC=+0.150 (n=412)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` > 0.0052 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.0721` → IC=+0.182 (n=272)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.0721 (IC base=+0.148)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2995` → IC=+0.196 (n=484)

  - _Acción_: Kelly boost +0.98€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2995 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.163 (n=443)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 11.0 (IC base=+0.148)

- **PATRÓN** `ibs_15` > `0.5684` → IC=+0.242 (n=618)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5684 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` > `0.6301` → IC=+0.164 (n=114)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.6301 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` < `0.2675` → IC=+0.149 (n=577)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.2675 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.028` → IC=+0.258 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.028 (IC base=+0.148)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.154 (n=807)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `8872.332` → IC=+0.159 (n=206)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 8872.332 (IC base=+0.148)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.253 (n=1276)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0061 (IC base=+0.242)

- **PATRÓN** `drift_60min` |x|≤ `0.3558` → IC=+0.247 (n=1684)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3558 (IC base=+0.242)

- **PATRÓN** `drift_15min` |x|≤ `0.782` → IC=+0.257 (n=1684)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.782 (IC base=+0.242)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2142` → IC=+0.263 (n=867)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2142 (IC base=+0.242)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.251 (n=704)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.242)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.242 (n=1308)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.242)

- **PATRÓN** `ibs_15` < `0.1856` → IC=+0.301 (n=1276)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.1856 (IC base=+0.242)

- **PATRÓN** `dist_vwap_pct` > `0.3774` → IC=+0.272 (n=475)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3774 (IC base=+0.242)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.323` → IC=+0.246 (n=841)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.323 (IC base=+0.242)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.189` → IC=+0.247 (n=2000)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.189 (IC base=+0.242)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1869` → IC=-0.267 (n=316)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1869
  - _Potencial_: sin este filtro IC_bueno=-0.178 (n=952)

- **FILTRO** `sigma_h` > `0.0105` → IC=-0.237 (n=431)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0105
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=837)

- **FILTRO** `drift_60min` |x|> `0.1722` → IC=-0.267 (n=431)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1722
  - _Potencial_: sin este filtro IC_bueno=-0.166 (n=837)

- **FILTRO** `drift_15min` |x|> `0.9102` → IC=-0.286 (n=316)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.9102
  - _Potencial_: sin este filtro IC_bueno=-0.172 (n=952)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1455` → IC=+0.188 (n=46)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.94€ cuando `delta_ratio_macro` |x|> 0.1455 (IC base=-0.201)

- **PATRÓN** `ibs_15` > `0.5625` → IC=+0.234 (n=62)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5625 (IC base=-0.201)

- **PATRÓN** `dist_vwap_pct` > `0.2752` → IC=+0.143 (n=26)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.2752 (IC base=-0.201)

- **PATRÓN** `dist_vwap_pct` < `0.4298` → IC=+0.154 (n=76)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.4298 (IC base=-0.201)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0642` → IC=+0.236 (n=850)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0642 (IC base=-0.030)

- **PATRÓN** `ibs_15` < `0.381` → IC=+0.294 (n=852)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.381 (IC base=-0.030)

- **PATRÓN** `dist_vwap_pct` > `0.6795` → IC=+0.236 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6795 (IC base=-0.030)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.1522` → IC=-0.243 (n=387)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1522
  - _Potencial_: sin este filtro IC_bueno=-0.209 (n=1165)

- **FILTRO** `libro_spread` > `0.04` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.04
  - _Potencial_: sin este filtro IC_bueno=-0.217 (n=1533)

- **FILTRO** `libro_liquidez` < `2917.696` → IC=-0.225 (n=1024)

  - _Acción_: SKIP cuando `libro_liquidez` < 2917.696
  - _Potencial_: sin este filtro IC_bueno=-0.202 (n=528)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.217)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.217)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1185` → IC=+0.302 (n=518)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1185 (IC base=-0.016)

- **PATRÓN** `ibs_15` < `0.3256` → IC=+0.293 (n=1190)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3256 (IC base=-0.016)

- **PATRÓN** `dist_vwap_pct` > `0.768` → IC=+0.332 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.768 (IC base=-0.016)

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
- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.298 (n=454)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0033 (IC base=+0.283)

- **PATRÓN** `drift_60min` |x|≤ `0.0721` → IC=+0.312 (n=598)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0721 (IC base=+0.283)

- **PATRÓN** `delta_ratio_macro` |x|> `0.152` → IC=+0.285 (n=905)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.152 (IC base=+0.283)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2224` → IC=+0.289 (n=828)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2224 (IC base=+0.283)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.295 (n=1405)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.283)

- **PATRÓN** `ibs_15` > `0.838` → IC=+0.311 (n=1358)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.838 (IC base=+0.283)

- **PATRÓN** `dist_vwap_pct` > `0.2631` → IC=+0.312 (n=588)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2631 (IC base=+0.283)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.964` → IC=+0.387 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.964 (IC base=+0.283)

- **PATRÓN** `libro_liquidez` > `13167.3452` → IC=+0.302 (n=453)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13167.3452 (IC base=+0.283)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.305 (n=239)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.275)

- **PATRÓN** `drift_60min` |x|≤ `0.0778` → IC=+0.302 (n=316)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0778 (IC base=+0.275)

- **PATRÓN** `drift_15min` |x|≤ `0.3843` → IC=+0.276 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3843 (IC base=+0.275)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2695` → IC=+0.280 (n=239)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2695 (IC base=+0.275)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3931` → IC=+0.280 (n=643)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3931 (IC base=+0.275)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.293 (n=751)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.275)

- **PATRÓN** `ibs_15` > `0.8279` → IC=+0.301 (n=717)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8279 (IC base=+0.275)

- **PATRÓN** `dist_vwap_pct` > `0.2516` → IC=+0.310 (n=308)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2516 (IC base=+0.275)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.806` → IC=+0.395 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.806 (IC base=+0.275)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.277 (n=926)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.275)

- **PATRÓN** `libro_liquidez` > `15796.8084` → IC=+0.313 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15796.8084 (IC base=+0.275)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.297 (n=643)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0069 (IC base=+0.290)

- **PATRÓN** `drift_60min` |x|≤ `0.0504` → IC=+0.319 (n=214)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0504 (IC base=+0.290)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1009` → IC=+0.322 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1009 (IC base=+0.290)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.302 (n=614)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.290)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.291 (n=453)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.290)

- **PATRÓN** `ibs_15` > `0.8475` → IC=+0.318 (n=642)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8475 (IC base=+0.290)

- **PATRÓN** `dist_vwap_pct` > `0.2797` → IC=+0.317 (n=276)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2797 (IC base=+0.290)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.34` → IC=+0.372 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.34 (IC base=+0.290)

### UPDOWN_OU_5M
- **FILTRO** `delta_ratio_macro` |x|≤ `0.126` → IC=-0.156 (n=94)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.126
  - _Potencial_: sin este filtro IC_bueno=-0.099 (n=285)

- **FILTRO** `ballena_activa_n` > `32.0` → IC=-0.130 (n=260)

  - _Acción_: SKIP cuando `ballena_activa_n` > 32.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=87)

- **FILTRO** `sigma_h` < `0.0051` → IC=-0.177 (n=122)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0051
  - _Potencial_: sin este filtro IC_bueno=-0.090 (n=369)

- **FILTRO** `ballena_activa_n` > `60.0` → IC=-0.229 (n=57)

  - _Acción_: SKIP cuando `ballena_activa_n` > 60.0
  - _Potencial_: sin este filtro IC_bueno=-0.140 (n=173)

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

- **FILTRO** `sigma_h` < `0.0047` → IC=-0.326 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0047
  - _Potencial_: sin este filtro IC_bueno=-0.286 (n=12)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.2685` → IC=-0.370 (n=21)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2685
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=12)

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
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=29)

- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.0863` → IC=-0.214 (n=26)

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
- **PATRÓN** `ratio` < `0.9701` → IC=+0.380 (n=388)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9701 (IC base=+0.165)

- **PATRÓN** `T_h` > `119.8535` → IC=+0.354 (n=2862)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 119.8535 (IC base=+0.336)

- **PATRÓN** `ratio` > `1.021` → IC=+0.388 (n=497)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.021 (IC base=+0.336)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `111.9974` → IC=+0.129 (n=273)

  - _Acción_: Kelly boost +0.65€ cuando `T_h` > 111.9974 (IC base=+0.125)

- **PATRÓN** `ratio` < `0.9933` → IC=+0.255 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9933 (IC base=+0.125)

- **PATRÓN** `T_h` > `111.9836` → IC=+0.317 (n=1031)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9836 (IC base=+0.300)

- **PATRÓN** `ratio` > `1.0177` → IC=+0.368 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0177 (IC base=+0.300)

### WEEKLY_PRICE#ETH
- **PATRÓN** `ratio` < `0.9849` → IC=+0.403 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9849 (IC base=+0.211)

- **PATRÓN** `T_h` > `111.9966` → IC=+0.355 (n=1040)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9966 (IC base=+0.324)

- **PATRÓN** `ratio` > `1.0082` → IC=+0.346 (n=317)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0082 (IC base=+0.324)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.0625` → IC=+0.418 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.0625 (IC base=+0.397)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5789 sube el IC de +0.141 a +0.224 en UPDOWN_GBM#15min (n=4833). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7077 sube el IC de +0.201 a +0.273 en UPDOWN_GBM#BTC#15min (n=795). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.4963 sube el IC de +0.133 a +0.220 en UPDOWN_GBM#ETH#15min (n=993). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5429 sube el IC de +0.153 a +0.227 en UPDOWN_GBM#XRP#15min (n=1206). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1094 sube el IC de +0.068 a +0.153 en UPDOWN_GBM#XRP#15min (n=1034). Ya aplicado como kelly_boost=+0.77€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6306 sube el IC de -0.082 a +0.278 en UPDOWN_GBM_15M_TARDIO (n=1234). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3704 sube el IC de -0.004 a +0.284 en UPDOWN_GBM_15M_TARDIO (n=4983). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7593 sube el IC de +0.071 a +0.320 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=431). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.6255 sube el IC de -0.186 a +0.289 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=74). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.5684 sube el IC de +0.148 a +0.242 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=618). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.1856 sube el IC de +0.242 a +0.301 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=1276). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de -0.201 a +0.234 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=62). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.381 sube el IC de -0.030 a +0.294 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=852). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.217 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3256 sube el IC de -0.016 a +0.293 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=1190). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_YES, IBS > 0.8434 sube el IC de +0.109 a +0.340 en UPDOWN_GBM_ETH_15M_HORA7 (n=23). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_YES, IBS > 0.8434 sube el IC de +0.109 a +0.340 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=23). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.838 sube el IC de +0.283 a +0.311 en UPDOWN_GBM_IBS_ALTO (n=1358). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8279 sube el IC de +0.275 a +0.301 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=717). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8475 sube el IC de +0.290 a +0.318 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=642). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7903 sube el IC de +0.364 a +0.393 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=754). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8078 sube el IC de +0.362 a +0.384 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=369). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7632 sube el IC de +0.364 a +0.392 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=386). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 2176 | +0.084 | +234.09€ | 1 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 2176 | +0.084 | +234.09€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1770 | +0.085 | +195.31€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1770 | +0.085 | +195.31€ | 1 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 285 | +0.068 | +10.79€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 285 | +0.068 | +10.79€ | 5 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 90 | +0.130 | +28.32€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 90 | +0.130 | +28.32€ | 1 | 10 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 1145 | -0.021 | +72.79€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 1145 | -0.021 | +72.79€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE | 7 | +0.019 | +3.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE#15min | 7 | +0.019 | +3.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 879 | -0.038 | +57.42€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 879 | -0.038 | +57.42€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 181 | +0.063 | +19.36€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 181 | +0.063 | +19.36€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 78 | -0.037 | -7.24€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 78 | -0.037 | -7.24€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 47433 | -0.084 | -6044.46€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 2945 | +0.072 | -301.71€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 44488 | -0.094 | -5742.75€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4811 | -0.113 | -804.95€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4811 | -0.113 | -804.95€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 2945 | +0.072 | -301.71€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 2945 | +0.072 | -301.71€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 4877 | -0.106 | -938.87€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 4877 | -0.106 | -938.87€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 13000 | -0.042 | -1210.70€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 13000 | -0.042 | -1210.70€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 12936 | -0.112 | -1349.50€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 12936 | -0.112 | -1349.50€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 8864 | -0.129 | -1438.73€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 8864 | -0.129 | -1438.73€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 49205 | -0.012 | +2848.20€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 12729 | +0.004 | +1517.69€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 36476 | -0.018 | +1330.51€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 49205 | -0.012 | +2848.20€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 12729 | +0.004 | +1517.69€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 36476 | -0.018 | +1330.51€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 188543 | +0.113 | -7822.36€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#15min | 21797 | +0.180 | -716.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 865 | +0.010 | -74.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 155116 | +0.105 | -6626.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 10765 | +0.093 | -404.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 25702 | +0.103 | -1809.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 76 | -0.179 | +10.07€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 25611 | +0.104 | -1807.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 35724 | +0.124 | -610.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5611 | +0.178 | -238.12€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 25679 | +0.120 | -187.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 4392 | +0.079 | -162.43€ | 1 | 2 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 25754 | +0.099 | -1852.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 87 | -0.118 | +5.83€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 25652 | +0.100 | -1847.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 40278 | +0.123 | -857.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 10136 | +0.178 | -253.99€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 26086 | +0.105 | -537.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 4044 | +0.102 | -56.92€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#SOL | 35353 | +0.112 | -1581.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 5798 | +0.198 | -255.37€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 768 | +0.036 | -20.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 26458 | +0.096 | -1120.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 2329 | +0.100 | -185.58€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO#XRP | 25732 | +0.107 | -1110.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 89 | -0.115 | +15.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 25630 | +0.108 | -1125.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 30558 | +0.193 | -2102.80€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 30558 | +0.193 | -2102.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 6921 | +0.170 | -709.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 6921 | +0.170 | -709.77€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 4417 | +0.197 | -163.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 4417 | +0.197 | -163.99€ | 3 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 6782 | +0.176 | -587.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 6782 | +0.176 | -587.18€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 5688 | +0.251 | -201.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 5688 | +0.251 | -201.45€ | 0 | 4 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 6671 | +0.185 | -454.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 6671 | +0.185 | -454.16€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 1243 | +0.425 | -46.72€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 1243 | +0.425 | -46.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 515 | +0.440 | -3.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 515 | +0.440 | -3.67€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE#15min | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 501 | +0.422 | -20.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 501 | +0.422 | -20.81€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 213 | +0.398 | -18.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 213 | +0.398 | -18.37€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 108091 | +0.200 | -7966.72€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 108091 | +0.200 | -7966.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 18691 | +0.179 | -2125.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 18691 | +0.179 | -2125.48€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 17430 | +0.225 | -574.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 17430 | +0.225 | -574.51€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 18554 | +0.179 | -1985.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 18554 | +0.179 | -1985.12€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 17575 | +0.218 | -702.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 17575 | +0.218 | -702.47€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 17861 | +0.203 | -1126.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 17861 | +0.203 | -1126.11€ | 1 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 17980 | +0.196 | -1453.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 17980 | +0.196 | -1453.05€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 41680 | +0.117 | +352.20€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 41680 | +0.117 | +352.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 20746 | +0.118 | +215.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 20746 | +0.118 | +215.09€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 20934 | +0.116 | +137.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 20934 | +0.116 | +137.11€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 2588 | +0.294 | -2.91€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 2588 | +0.294 | -2.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 1185 | +0.283 | -25.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 1185 | +0.283 | -25.34€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 1264 | +0.299 | +17.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 1264 | +0.299 | +17.18€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 139 | +0.344 | +5.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 139 | +0.344 | +5.25€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 1194 | +0.439 | -2.74€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 1194 | +0.439 | -2.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 574 | +0.432 | -10.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 574 | +0.432 | -10.65€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 569 | +0.446 | +6.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 569 | +0.446 | +6.65€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 51 | +0.406 | +1.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 51 | +0.406 | +1.25€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1943 | +0.068 | -84.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 725 | +0.046 | -64.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 1218 | +0.081 | -19.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1509 | +0.076 | -38.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 291 | +0.053 | -19.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 1218 | +0.081 | -19.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 84474 | +0.101 | -1976.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 6813 | +0.096 | +141.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 77661 | +0.101 | -2118.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 46172 | +0.106 | -440.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 6813 | +0.096 | +141.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 39359 | +0.107 | -582.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 17959 | +0.109 | -112.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 17959 | +0.109 | -112.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 20343 | +0.082 | -1423.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 20343 | +0.082 | -1423.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 914 | +0.186 | -109.27€ | 5 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 914 | +0.186 | -109.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 914 | +0.186 | -109.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 914 | +0.186 | -109.27€ | 5 | 4 |
| ✅ GBM_LATE_15M | 57325 | +0.100 | +31970.33€ | 0 | 18 |
| ✅ GBM_LATE_15M#15min | 57325 | +0.100 | +31970.33€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 9490 | +0.227 | +8228.57€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 9490 | +0.227 | +8228.57€ | 0 | 22 |
| ✅ GBM_LATE_15M#BTC | 8785 | +0.175 | +6901.96€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 8785 | +0.175 | +6901.96€ | 0 | 20 |
| ✅ GBM_LATE_15M#DOGE | 10273 | +0.208 | +8139.16€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 10273 | +0.208 | +8139.16€ | 0 | 21 |
| ✅ GBM_LATE_15M#ETH | 7679 | +0.056 | +2459.93€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 7679 | +0.056 | +2459.93€ | 1 | 16 |
| ✅ GBM_LATE_15M#SOL | 8001 | -0.031 | +2054.24€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 8001 | -0.031 | +2054.24€ | 4 | 13 |
| ✅ GBM_LATE_15M#XRP | 13097 | -0.022 | +4186.46€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 13097 | -0.022 | +4186.46€ | 3 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 60443 | +0.085 | +35008.93€ | 0 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 60443 | +0.085 | +35008.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 11684 | -0.002 | +6209.73€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 11684 | -0.002 | +6209.73€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 12998 | +0.004 | +3448.63€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 12998 | +0.004 | +3448.63€ | 0 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 8217 | +0.295 | +9400.80€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 8217 | +0.295 | +9400.80€ | 0 | 21 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 11533 | +0.013 | +3577.23€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 11533 | +0.013 | +3577.23€ | 1 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 9275 | +0.043 | +4122.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 9275 | +0.043 | +4122.12€ | 3 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 6736 | +0.315 | +8250.43€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 6736 | +0.315 | +8250.43€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 45363 | +0.178 | +37422.42€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 45363 | +0.178 | +37422.42€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 6830 | +0.240 | +6377.22€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 6830 | +0.240 | +6377.22€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 7190 | +0.138 | +5279.11€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 7190 | +0.138 | +5279.11€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 7297 | +0.225 | +6339.42€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 7297 | +0.225 | +6339.42€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 7774 | +0.129 | +6040.43€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 7774 | +0.129 | +6040.43€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 8584 | +0.119 | +6417.90€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 8584 | +0.119 | +6417.90€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 7688 | +0.233 | +6968.35€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 7688 | +0.233 | +6968.35€ | 0 | 24 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 12326 | +0.125 | +6163.99€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 12326 | +0.125 | +6163.99€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 543 | +0.166 | +371.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 543 | +0.166 | +371.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 3412 | +0.127 | +1861.39€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 3412 | +0.127 | +1861.39€ | 0 | 13 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 506 | +0.158 | +277.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 506 | +0.158 | +277.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 3577 | +0.123 | +1703.89€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 3577 | +0.123 | +1703.89€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 3223 | +0.099 | +1291.34€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 3223 | +0.099 | +1291.34€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 1065 | +0.166 | +658.18€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 1065 | +0.166 | +658.18€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO | 57501 | +0.188 | +47312.71€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#15min | 57501 | +0.188 | +47312.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 9072 | +0.251 | +8819.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 9072 | +0.251 | +8819.93€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 9146 | +0.137 | +6309.88€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 9146 | +0.137 | +6309.88€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 9754 | +0.236 | +8860.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 9754 | +0.236 | +8860.87€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 9513 | +0.142 | +7037.34€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 9513 | +0.142 | +7037.34€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 10210 | +0.121 | +7165.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 10210 | +0.121 | +7165.76€ | 0 | 18 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 9806 | +0.241 | +9118.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 9806 | +0.241 | +9118.93€ | 0 | 20 |
| ✅ GBM_LATE_5M | 14539 | +0.213 | +11908.46€ | 1 | 26 |
| ✅ GBM_LATE_5M#5min | 14539 | +0.213 | +11908.46€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 1118 | +0.250 | +1077.52€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 1118 | +0.250 | +1077.52€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 3266 | +0.211 | +2814.84€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 3266 | +0.211 | +2814.84€ | 0 | 27 |
| ✅ GBM_LATE_5M#DOGE | 1453 | +0.210 | +1160.11€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1453 | +0.210 | +1160.11€ | 0 | 19 |
| ✅ GBM_LATE_5M#ETH | 4306 | +0.204 | +3244.18€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 4306 | +0.204 | +3244.18€ | 0 | 23 |
| ✅ GBM_LATE_5M#SOL | 2401 | +0.215 | +2036.11€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 2401 | +0.215 | +2036.11€ | 0 | 26 |
| ✅ GBM_LATE_5M#XRP | 1995 | +0.211 | +1575.70€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1995 | +0.211 | +1575.70€ | 0 | 0 |
| ✅ GBM_LATE_60M | 5097 | +0.052 | +1391.46€ | 0 | 5 |
| ✅ GBM_LATE_60M#60min | 5097 | +0.052 | +1391.46€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 1770 | +0.058 | +536.75€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 1770 | +0.058 | +536.75€ | 1 | 6 |
| ✅ GBM_LATE_60M#ETH | 1633 | +0.052 | +521.37€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 1633 | +0.052 | +521.37€ | 1 | 6 |
| ✅ GBM_LATE_60M#SOL | 1694 | +0.044 | +333.34€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 1694 | +0.044 | +333.34€ | 0 | 8 |
| 🚫 GBM_LATE_60M_FADE | 713 | -0.250 | -34.37€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 713 | -0.250 | -34.37€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 258 | -0.250 | -18.00€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 258 | -0.250 | -18.00€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 261 | -0.245 | -7.56€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 261 | -0.245 | -7.56€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 194 | -0.250 | -8.81€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 194 | -0.250 | -8.81€ | 8 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 2121 | +0.084 | +541.12€ | 0 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 2121 | +0.084 | +541.12€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 821 | +0.071 | +192.58€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 821 | +0.071 | +192.58€ | 1 | 6 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 749 | +0.058 | +145.65€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 749 | +0.058 | +145.65€ | 1 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 551 | +0.138 | +202.88€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 551 | +0.138 | +202.88€ | 2 | 9 |
| ✅ LATE_WINDOW_5MIN | 247 | +0.295 | +279.38€ | 1 | 13 |
| ✅ LATE_WINDOW_5MIN#5min | 247 | +0.295 | +279.38€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 247 | +0.295 | +279.38€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 247 | +0.295 | +279.38€ | 1 | 13 |
| ✅ LEADLAG_BTC_XRP_15M | 4399 | +0.098 | +1004.85€ | 0 | 1 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 4399 | +0.098 | +1004.85€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 4399 | +0.098 | +1004.85€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 4399 | +0.098 | +1004.85€ | 0 | 1 |
| ✅ LIQUIDACIONES_15M | 1162 | -0.005 | +18.12€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 1162 | -0.005 | +18.12€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 75 | -0.006 | -1.82€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 75 | -0.006 | -1.82€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 281 | -0.009 | +7.18€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 281 | -0.009 | +7.18€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 55 | -0.061 | -4.61€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 55 | -0.061 | -4.61€ | 1 | 1 |
| ✅ LIQUIDACIONES_15M#ETH | 299 | +0.022 | +19.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 299 | +0.022 | +19.09€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 317 | -0.017 | +0.08€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 317 | -0.017 | +0.08€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 135 | -0.004 | -1.80€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 135 | -0.004 | -1.80€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 4200 | +0.017 | +125.99€ | 4 | 1 |
| ✅ LIQUIDACIONES_5M#5min | 4200 | +0.017 | +125.99€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 215 | +0.025 | -0.90€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 215 | +0.025 | -0.90€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 827 | +0.015 | +40.58€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 827 | +0.015 | +40.58€ | 4 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 251 | +0.026 | +25.87€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 251 | +0.026 | +25.87€ | 0 | 7 |
| ✅ LIQUIDACIONES_5M#ETH | 1659 | +0.020 | +29.48€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1659 | +0.020 | +29.48€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 770 | +0.010 | +1.38€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 770 | +0.010 | +1.38€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 478 | +0.015 | +29.59€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 478 | +0.015 | +29.59€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 2388 | -0.034 | -9.62€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 2388 | -0.034 | -9.62€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 724 | -0.032 | -11.67€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 724 | -0.032 | -11.67€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 849 | -0.012 | +15.58€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 849 | -0.012 | +15.58€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 815 | -0.057 | -13.53€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 815 | -0.057 | -13.53€ | 5 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 15674 | -0.031 | -97.38€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 7542 | -0.032 | -61.66€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 8132 | -0.029 | -35.72€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 543 | -0.056 | -34.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 280 | -0.032 | -1.89€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 263 | -0.081 | -32.28€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 4103 | -0.024 | -1.49€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 1949 | -0.022 | +11.52€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 2154 | -0.026 | -13.01€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 1520 | -0.027 | +21.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 779 | -0.033 | +0.26€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 741 | -0.021 | +21.35€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 3540 | -0.033 | -54.12€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 1680 | -0.035 | -31.19€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 1860 | -0.032 | -22.93€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 3025 | -0.021 | +52.54€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 1465 | -0.026 | +10.05€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 1560 | -0.017 | +42.49€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 2943 | -0.043 | -81.75€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 1389 | -0.049 | -50.41€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 1554 | -0.037 | -31.34€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 68017 | -0.000 | +3612.04€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 68017 | -0.000 | +3612.04€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 12329 | +0.027 | +1675.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 12329 | +0.027 | +1675.78€ | 2 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 9496 | -0.037 | -130.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 9496 | -0.037 | -130.27€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 12471 | +0.025 | +1381.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 12471 | +0.025 | +1381.02€ | 1 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 9438 | -0.052 | -248.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 9438 | -0.052 | -248.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 11604 | -0.004 | +323.39€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 11604 | -0.004 | +323.39€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 12679 | +0.017 | +610.39€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 12679 | +0.017 | +610.39€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 7175 | -0.055 | -119.43€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 7175 | -0.055 | -119.43€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1247 | -0.002 | -15.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1247 | -0.002 | -15.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1988 | -0.064 | -26.11€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1988 | -0.064 | -26.11€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 79 | -0.018 | -0.18€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 79 | -0.018 | -0.18€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 809 | -0.120 | -35.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 809 | -0.120 | -35.98€ | 5 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 2189 | -0.068 | -14.44€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 2189 | -0.068 | -14.44€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 863 | -0.018 | -27.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 863 | -0.018 | -27.52€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3379 | +0.003 | -2.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3379 | +0.003 | -2.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 133 | -0.033 | -0.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 133 | -0.033 | -0.70€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 197 | +0.007 | -1.76€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 197 | +0.007 | -1.76€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 139 | -0.004 | -2.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 139 | -0.004 | -2.34€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1326 | +0.006 | +6.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1326 | +0.006 | +6.37€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1391 | +0.007 | -0.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1391 | +0.007 | -0.19€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 193 | -0.013 | -3.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 193 | -0.013 | -3.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 166596 | -0.078 | +2147.19€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 166596 | -0.078 | +2147.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 29184 | -0.078 | +1769.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 29184 | -0.078 | +1769.19€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 24890 | -0.102 | -1287.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 24890 | -0.102 | -1287.91€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 29566 | -0.069 | +1388.45€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 29566 | -0.069 | +1388.45€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 24437 | -0.099 | -767.68€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 24437 | -0.099 | -767.68€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 29760 | -0.059 | +258.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 29760 | -0.059 | +258.36€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 28759 | -0.070 | +786.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 28759 | -0.070 | +786.78€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 9064 | -0.035 | -182.95€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 9064 | -0.035 | -182.95€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 1008 | -0.017 | -19.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 1008 | -0.017 | -19.32€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 2112 | -0.047 | -28.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 2112 | -0.047 | -28.71€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2649 | -0.025 | -37.10€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2649 | -0.025 | -37.10€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1272 | -0.064 | -32.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1272 | -0.064 | -32.38€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 1014 | -0.032 | -33.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 1014 | -0.032 | -33.50€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 2166 | +0.120 | +861.76€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#5min | 2030 | +0.124 | +849.17€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 481 | +0.134 | +233.57€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 481 | +0.134 | +233.57€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#DOGE | 415 | +0.119 | +146.47€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 415 | +0.119 | +146.47€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#ETH | 382 | +0.125 | +170.48€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 382 | +0.125 | +170.48€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 345 | +0.143 | +179.09€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 345 | +0.143 | +179.09€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#XRP | 407 | +0.099 | +119.57€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 407 | +0.099 | +119.57€ | 0 | 2 |
| ✅ ORDER_FLOW_5M_REACTIVO | 2195 | -0.016 | -15.86€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 2195 | -0.016 | -15.86€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 398 | +0.015 | +26.81€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 398 | +0.015 | +26.81€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 405 | -0.041 | -21.91€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 405 | -0.041 | -21.91€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 553 | -0.037 | -29.12€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 553 | -0.037 | -29.12€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 444 | +0.002 | +4.26€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 444 | +0.002 | +4.26€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 395 | -0.011 | +4.09€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 395 | -0.011 | +4.09€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 1168 | -0.065 | -18.16€ | 1 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 539 | -0.103 | -68.40€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 418 | -0.114 | -47.85€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 121 | -0.061 | -20.55€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 409 | -0.023 | +34.22€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 294 | -0.007 | +42.23€ | 1 | 2 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 115 | -0.064 | -8.00€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 220 | -0.050 | +16.02€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 184 | -0.043 | +14.18€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 36 | -0.079 | +1.84€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 896 | -0.065 | +8.55€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 272 | -0.066 | -26.71€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 1476 | -0.204 | -88.27€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC | 582 | -0.200 | -47.65€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 512 | -0.198 | -43.20€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#reach | 70 | -0.208 | -4.45€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 493 | -0.209 | -38.69€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 431 | -0.221 | -45.83€ | 3 | 1 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 62 | -0.125 | +7.14€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 401 | -0.200 | -1.94€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 371 | -0.197 | -4.09€ | 5 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 30 | -0.219 | +2.15€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 1314 | -0.206 | -93.11€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 162 | -0.183 | +4.84€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 539 | +0.372 | +499.33€ | 0 | 12 |
| ✅ RESOLUTION_SNIPER#BTC | 110 | +0.134 | +83.90€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 110 | +0.134 | +83.90€ | 0 | 6 |
| ✅ RESOLUTION_SNIPER#ETH | 123 | +0.364 | +103.53€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 123 | +0.364 | +103.53€ | 0 | 5 |
| ✅ RESOLUTION_SNIPER#SOL | 306 | +0.458 | +311.91€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 306 | +0.458 | +311.91€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#sniper | 539 | +0.372 | +499.33€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 949 | +0.042 | +81.09€ | 2 | 2 |
| ✅ STREAK_FADE_15M#15min | 949 | +0.042 | +81.09€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 357 | +0.018 | +3.41€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 357 | +0.018 | +3.41€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 74 | +0.026 | +3.13€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 74 | +0.026 | +3.13€ | 1 | 1 |
| ✅ STREAK_FADE_15M#SOL | 83 | +0.018 | +6.06€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 83 | +0.018 | +6.06€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 435 | +0.068 | +68.50€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 435 | +0.068 | +68.50€ | 1 | 3 |
| ✅ STREAK_FADE_5M | 3577 | -0.024 | -144.53€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3577 | -0.024 | -144.53€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 1127 | -0.023 | -40.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 1127 | -0.023 | -40.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 616 | -0.031 | -28.72€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 616 | -0.031 | -28.72€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 171 | -0.043 | -14.80€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 171 | -0.043 | -14.80€ | 4 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1663 | -0.019 | -60.80€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1663 | -0.019 | -60.80€ | 2 | 0 |
| ✅ STREAK_FADE_60M | 118 | -0.050 | -12.20€ | 5 | 0 |
| ✅ STREAK_FADE_60M#60min | 118 | -0.050 | -12.20€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 44 | -0.087 | -4.62€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 44 | -0.087 | -4.62€ | 4 | 0 |
| ✅ STREAK_FADE_60M#SOL | 74 | -0.026 | -7.58€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 74 | -0.026 | -7.58€ | 0 | 1 |
| ✅ STREAK_MOM_5M | 11517 | +0.014 | +72.91€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 11517 | +0.014 | +72.91€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2995 | +0.018 | +24.38€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2995 | +0.018 | +24.38€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 3014 | +0.016 | +32.39€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 3014 | +0.016 | +32.39€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2927 | +0.009 | -2.09€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2927 | +0.009 | -2.09€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2581 | +0.014 | +18.23€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2581 | +0.014 | +18.23€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 12086 | +0.018 | -5.65€ | 4 | 0 |
| ✅ STRUCT_NO_15M#15min | 12086 | +0.018 | -5.65€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 5020 | +0.021 | +5.59€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 5020 | +0.021 | +5.59€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 4166 | +0.016 | -10.04€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 4166 | +0.016 | -10.04€ | 4 | 0 |
| ✅ STRUCT_NO_15M#SOL | 2900 | +0.015 | -1.20€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 2900 | +0.015 | -1.20€ | 1 | 0 |
| ✅ UPDOWN_GBM | 107464 | +0.060 | +10234.75€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 26206 | +0.079 | +5282.25€ | 0 | 10 |
| ✅ UPDOWN_GBM#240min | 3171 | -0.000 | +34.91€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 71341 | +0.062 | +4810.76€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 6377 | -0.002 | +113.39€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 8907 | +0.105 | +1639.22€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1781 | +0.164 | +820.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 90 | -0.011 | -2.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 7036 | +0.091 | +821.03€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 24518 | +0.057 | +2161.71€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 3506 | +0.078 | +779.37€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 906 | +0.000 | +17.76€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 17124 | +0.067 | +1287.35€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 2848 | -0.004 | +73.50€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 134 | -0.066 | +3.73€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 11684 | +0.078 | +1332.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1761 | +0.154 | +738.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 86 | +0.023 | -0.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 9837 | +0.065 | +594.81€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 25536 | +0.050 | +1810.26€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 6184 | +0.072 | +956.22€ | 0 | 9 |
| ✅ UPDOWN_GBM#ETH#240min | 875 | +0.005 | +16.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 16009 | +0.052 | +800.23€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 2345 | +0.001 | +36.48€ | 1 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 123 | -0.108 | +0.71€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 22817 | +0.039 | +1281.20€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 7041 | +0.031 | +427.68€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#240min | 817 | -0.010 | +5.01€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 13665 | +0.051 | +854.26€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 1184 | +0.000 | +3.42€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#daily | 110 | -0.143 | -9.17€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 14000 | +0.073 | +2011.81€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 5933 | +0.094 | +1560.34€ | 0 | 11 |
| ✅ UPDOWN_GBM#XRP#240min | 397 | +0.006 | -1.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 7670 | +0.060 | +453.08€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 367 | -0.104 | -4.72€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 1005 | +0.364 | +370.75€ | 0 | 10 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 1005 | +0.364 | +370.75€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 491 | +0.362 | +172.01€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 491 | +0.362 | +172.01€ | 0 | 9 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 514 | +0.364 | +198.73€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 514 | +0.364 | +198.73€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO | 25588 | -0.021 | +6327.33€ | 3 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 25588 | -0.021 | +6327.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1981 | -0.051 | +561.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1981 | -0.051 | +561.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 4771 | -0.115 | +252.74€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 4771 | -0.115 | +252.74€ | 3 | 11 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 1071 | +0.222 | +899.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 1071 | +0.222 | +899.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 3374 | +0.219 | +2150.78€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 3374 | +0.219 | +2150.78€ | 1 | 21 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 7260 | -0.060 | +1061.81€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 7260 | -0.060 | +1061.81€ | 4 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 7131 | -0.060 | +1400.95€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 7131 | -0.060 | +1400.95€ | 3 | 5 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 312 | +0.060 | +27.61€ | 0 | 10 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 312 | +0.060 | +27.61€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 312 | +0.060 | +27.61€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 312 | +0.060 | +27.61€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1810 | +0.283 | +1520.67€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1810 | +0.283 | +1520.67€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 955 | +0.275 | +747.56€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 955 | +0.275 | +747.56€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 855 | +0.290 | +773.11€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 855 | +0.290 | +773.11€ | 0 | 8 |
| ✅ UPDOWN_OU_5M | 870 | -0.114 | -86.85€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 870 | -0.114 | -86.85€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 277 | -0.081 | -20.93€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 277 | -0.081 | -20.93€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 97 | -0.177 | -11.96€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 97 | -0.177 | -11.96€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 113 | -0.178 | -4.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 113 | -0.178 | -4.61€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 38 | -0.175 | -6.61€ | 2 | 0 |
| ✅ WEEKLY_PRICE | 4739 | +0.300 | +2135.68€ | 0 | 3 |
| ✅ WEEKLY_PRICE#BTC | 1807 | +0.256 | +225.35€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 1831 | +0.295 | +782.33€ | 0 | 3 |
| ✅ WEEKLY_PRICE#SOL | 1101 | +0.381 | +1127.99€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**✅ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: n≥15 y IC<-0.05
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: IC=+0.022 n=1331 — no justifica filtro, seguir monitorizando
  - _Datos_: n=1331 IC=+0.022 PNL=+64.61€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 815 celda(s) pasan gate riguroso completo de 2908 evaluadas (n>=40) y 4027 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.031 < 0.08 — monitorear
  - _Datos_: n=7039 IC=+0.031 PNL=+427.70€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=1831/15 IC=+0.295 PNL=+782.33€ | BTC: n=1807/15 IC=+0.256 PNL=+225.35€ | SOL: n=1101/15 IC=+0.381 PNL=+1127.99€

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
  - _Estado_: alineada_con_outcome_prev IC=+0.141 n=1065/60 | contraria IC=+0.184 n=1117 | gap=-0.043 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=594, boost estimado=+0.012. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 0/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=2344/40 IC=+0.001 PNL=+36.99€ | BTC#60min: n=2847/40 IC=-0.004 PNL=+74.01€ | SOL#60min: n=1183/40 IC=+0.000 PNL=+3.93€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.045 n=734763 | tras_1loss IC=+0.100 n=557048 | tras_2loss IC=+0.071 n=222641/40 | gap=-0.026 (umbral 0.05)

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.161 > 0.08 con n=1067 PNL=+648.82€
  - _Datos_: n=1067 IC=+0.161 PNL=+648.82€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.132 > 0.08 con n=1281 PNL=+599.12€
  - _Datos_: n=1281 IC=+0.132 PNL=+599.12€

**🟡 H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: n≥25 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.129 > 0.08 con n=87 PNL=+35.62€
  - _Datos_: n=87 IC=+0.129 PNL=+35.62€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.334 > 0.1 con n=3860 PNL=+2146.24€
  - _Datos_: n=3860 IC=+0.334 PNL=+2146.24€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=1091 IC=+0.065 PNL=+106.94€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1091 IC=+0.065 PNL=+106.94€

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
  - _Estado_: 2/20 ops en el filtro definido (IC actual=+0.000 PNL=-0.08€)
  - _Datos_: n=2 IC=+0.000 PNL=-0.08€
  - _Bloqueante_: FILTRO_YA_IMPLEMENTADO: 07h sigue en ORDER_FLOW_BLACKLIST_HOURS -- mientras siga ahí, nunca genera fila para volver a evaluarse (26-Ago, triage candidatas estancadas)

**〰️ H-CUSTOM-GBM-60MIN-BUYYES** — GBM 60min BUY_YES — ¿edge superior al BUY_NO?
  - _Hipótesis_: Análisis actual muestra BUY_YES 60min: 22/36 (61%) IC=+0.105 vs BUY_NO 60min: 8/14 (57%) IC=+0.044. En 60min parece que BUY_YES es la dirección dominante, al contrario que en 15min.
  - _Umbral_: n≥30 y IC>+0.08
  - _Acción_: Si BUY_YES 60min confirma IC≥0.10 n≥40 → prioridad live por encima de BUY_NO
  - _Estado_: n=4252 IC=+0.002 PNL=-15.90€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=4252 IC=+0.002 PNL=-15.90€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=2122 IC=-0.007 PNL=+130.82€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=2122 IC=-0.007 PNL=+130.82€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=1331 IC=+0.022 PNL=+64.61€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=1331 IC=+0.022 PNL=+64.61€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.141 > 0.1 con n=7209 PNL=+3616.14€
  - _Datos_: n=7209 IC=+0.141 PNL=+3616.14€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=3506 IC=+0.078 PNL=+779.37€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=3506 IC=+0.078 PNL=+779.37€

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
  - _Estado_: n=1391 IC=+0.038 PNL=+108.94€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=1391 IC=+0.038 PNL=+108.94€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=178 IC=-0.033 PNL=-6.69€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=178 IC=-0.033 PNL=-6.69€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.295 n=247) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=247 IC=+0.295 PNL=+279.38€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.118 > 0.02 con n=1270 PNL=+508.16€
  - _Datos_: n=1270 IC=+0.118 PNL=+508.16€

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
  - _Estado_: n=44195 IC=+0.073 PNL=+6111.95€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=44195 IC=+0.073 PNL=+6111.95€

**⏳ H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: 120
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: 0/120 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.138 < -0.1 con n=760 PNL=+101.08€
  - _Datos_: n=760 IC=-0.138 PNL=+101.08€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=4132 IC=+0.068 PNL=+525.26€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=4132 IC=+0.068 PNL=+525.26€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=190 IC=-0.099 PNL=-0.56€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=190 IC=-0.099 PNL=-0.56€

**〰️ H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: n=1118 IC=+0.098 PNL=+277.11€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=1118 IC=+0.098 PNL=+277.11€

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
  - _Estado_: n=43583 IC=-0.137 PNL=+2760.13€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=43583 IC=-0.137 PNL=+2760.13€

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
  - _Estado_: n=4536 IC=+0.130 PNL=+2992.65€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=4536 IC=+0.130 PNL=+2992.65€

**⏳ H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: 40
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=11120 IC=+0.058 PNL=+973.48€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=11120 IC=+0.058 PNL=+973.48€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.103 > 0.08 con n=4679 PNL=+2661.37€
  - _Datos_: n=4679 IC=+0.103 PNL=+2661.37€

**⏳ H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: 80
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: 0/80 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.219 < -0.1 con n=4770 PNL=-386.59€
  - _Datos_: n=4770 IC=-0.219 PNL=-386.59€

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
  - _Estado_: n=109 IC=+0.050 PNL=+18.22€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=109 IC=+0.050 PNL=+18.22€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.097 n=2234) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=2234 IC=+0.097 PNL=+450.12€

**⏳ H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.414 n=687) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=687 IC=+0.414 PNL=+1004.93€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=18683 IC=+0.179 PNL=-2123.24€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=18683 IC=+0.179 PNL=-2123.24€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.229 > 0.1 con n=297 PNL=+204.59€
  - _Datos_: n=297 IC=+0.229 PNL=+204.59€
