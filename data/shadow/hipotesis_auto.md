# Hipótesis automáticas — 2026-11-09 04:07 UTC
_Generado por shadow_postmortem.py sobre 1254579 resoluciones (PNL=+170911.88€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.5` → IC=-0.317 (n=195)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.118 (n=697)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.197 (n=1015)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` > 0.505 (IC base=+0.128)

- **PATRÓN** `n_total_lado` > `62.0` → IC=+0.186 (n=323)

  - _Acción_: Kelly boost +0.93€ cuando `n_total_lado` > 62.0 (IC base=+0.128)

- **PATRÓN** `banda_hit_calibrado` > `0.6121` → IC=+0.238 (n=639)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6121 (IC base=+0.128)

- **PATRÓN** `banda_z` > `8.618` → IC=+0.201 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 8.618 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.143 (n=357)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 17.0 (IC base=+0.128)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.129 (n=686)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 12.0 (IC base=+0.128)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.142 (n=1041)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.128)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.302 (n=165)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.113 (n=497)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.195 (n=880)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` > 0.505 (IC base=+0.131)

- **PATRÓN** `n_total_lado` > `66.0` → IC=+0.187 (n=276)

  - _Acción_: Kelly boost +0.94€ cuando `n_total_lado` > 66.0 (IC base=+0.131)

- **PATRÓN** `banda_hit_calibrado` > `0.8128` → IC=+0.274 (n=374)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8128 (IC base=+0.131)

- **PATRÓN** `banda_z` > `8.901` → IC=+0.208 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 8.901 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.148 (n=305)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 17.0 (IC base=+0.131)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.131 (n=584)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 12.0 (IC base=+0.131)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.138 (n=941)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.131)

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
- **FILTRO** `restante_s_al_confirmar` < `132.6` → IC=-0.222 (n=11650)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 132.6
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=34951)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `125.12` → IC=-0.259 (n=1193)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 125.12
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=3582)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `116.46` → IC=-0.289 (n=1209)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 116.46
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=3627)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `restante_s_al_confirmar` < `117.36` → IC=-0.165 (n=3174)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 117.36
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=9522)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `152.06` → IC=-0.247 (n=3169)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 152.06
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=9509)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `129.15` → IC=-0.263 (n=2192)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 129.15
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=6581)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.210 (n=27186)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.104)

- **PATRÓN** `libro_liquidez` > `8357.347` → IC=+0.159 (n=2300)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 8357.347 (IC base=+0.104)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.128 (n=23309)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 17.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.130 (n=28228)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.124)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.223 (n=21346)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.141 (n=8193)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `6596.2331` → IC=+0.146 (n=3165)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 6596.2331 (IC base=+0.124)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.185 (n=2191)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.177)

- **PATRÓN** `py_entrada` > `0.765` → IC=+0.364 (n=696)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.765 (IC base=+0.177)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.180 (n=2682)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.01 (IC base=+0.177)

- **PATRÓN** `libro_liquidez` > `9392.7207` → IC=+0.180 (n=1866)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 9392.7207 (IC base=+0.177)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.186 (n=1904)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 7.0 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.183 (n=2130)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 17.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` < `0.295` → IC=+0.312 (n=981)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.295 (IC base=+0.180)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.182 (n=2729)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.01 (IC base=+0.180)

- **PATRÓN** `libro_liquidez` > `16078.4757` → IC=+0.184 (n=704)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 16078.4757 (IC base=+0.180)

### FAVORITO_CONFIRMADO#BTC#60min
- **FILTRO** `py_entrada` < `0.55` → IC=-0.335 (n=95)

  - _Acción_: SKIP cuando `py_entrada` < 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.095 (n=2161)

- **PATRÓN** `py_entrada` > `0.61` → IC=+0.171 (n=593)

  - _Acción_: Kelly boost +0.85€ cuando `py_entrada` > 0.61 (IC base=+0.076)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.144 (n=1387)

  - _Acción_: Kelly boost +0.72€ cuando `py_entrada` < 0.44 (IC base=+0.082)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.169 (n=5179)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.165)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.169 (n=4374)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 15.0 (IC base=+0.165)

- **PATRÓN** `py_entrada` > `0.77` → IC=+0.375 (n=1680)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.77 (IC base=+0.165)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.212 (n=2340)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.202)

- **PATRÓN** `py_entrada` < `0.275` → IC=+0.330 (n=940)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.275 (IC base=+0.202)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.205 (n=2725)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.202)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.142 (n=627)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 15.0 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.147 (n=1128)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 15.0 (IC base=+0.141)

- **PATRÓN** `py_entrada` > `0.675` → IC=+0.253 (n=431)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.675 (IC base=+0.141)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.142 (n=1475)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.02 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.156 (n=155)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.074)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.254 (n=938)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.228)

- **PATRÓN** `py_entrada` > `0.83` → IC=+0.420 (n=1306)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.83 (IC base=+0.228)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.147 (n=1410)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 7.0 (IC base=+0.145)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.154 (n=726)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 7.0 (IC base=+0.145)

- **PATRÓN** `py_entrada` < `0.345` → IC=+0.278 (n=717)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.345 (IC base=+0.145)

### FAVORITO_CONFIRMADO#SOL#60min
- **FILTRO** `libro_liquidez` < `951.9496` → IC=-0.127 (n=156)

  - _Acción_: SKIP cuando `libro_liquidez` < 951.9496
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=318)

- **PATRÓN** `py_entrada` > `0.55` → IC=+0.160 (n=457)

  - _Acción_: Kelly boost +0.80€ cuando `py_entrada` > 0.55 (IC base=+0.046)

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

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.201 (n=23306)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.199 (n=19713)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 15.0 (IC base=+0.197)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.226 (n=9766)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.197)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=360)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.197)

- **PATRÓN** `libro_liquidez` > `4915.142` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4915.142 (IC base=+0.197)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.176 (n=5314)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 5.0 (IC base=+0.172)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.173 (n=5301)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 18.0 (IC base=+0.172)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.181 (n=5345)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` < 0.74 (IC base=+0.172)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.172 (n=4482)

  - _Acción_: Kelly boost +0.86€ cuando `py_entrada` > 0.71 (IC base=+0.172)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.380 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.247 (n=89)

- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=90)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.213 (n=3112)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.210)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.216 (n=2073)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.210)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.253 (n=1567)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.210)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.183 (n=5208)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.180 (n=4422)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 15.0 (IC base=+0.177)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.179 (n=5369)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` < 0.73 (IC base=+0.177)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.185 (n=4080)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` > 0.71 (IC base=+0.177)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.257 (n=4398)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.250)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.251 (n=3724)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.250)

- **PATRÓN** `py_entrada` > `0.8` → IC=+0.366 (n=1397)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.8 (IC base=+0.250)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.306 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.250)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.190 (n=5115)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.186)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.190 (n=4343)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 15.0 (IC base=+0.186)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.192 (n=3808)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.71 (IC base=+0.186)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.429 (n=944)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.425)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.427 (n=839)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.425)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.438 (n=956)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.425)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.431 (n=1002)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.425)

- **PATRÓN** `libro_liquidez` > `4484.2424` → IC=+0.443 (n=609)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4484.2424 (IC base=+0.425)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.437 (n=381)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.438)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.446 (n=259)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.438)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.454 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.438)

- **PATRÓN** `libro_liquidez` > `12295.9377` → IC=+0.444 (n=335)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12295.9377 (IC base=+0.438)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.431 (n=373)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.425)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.426 (n=337)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.425)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.436 (n=376)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.425)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.431 (n=418)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.425)

- **PATRÓN** `libro_liquidez` > `4712.9023` → IC=+0.436 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4712.9023 (IC base=+0.425)

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

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.208 (n=26290)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.240 (n=30933)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.200)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.187 (n=4567)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 18.0 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.181 (n=9747)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 12.0 (IC base=+0.179)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.190 (n=13985)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.71 (IC base=+0.179)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.228 (n=6346)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.224)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.287 (n=4361)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.224)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.192 (n=4513)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 18.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.198 (n=10834)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` > 0.72 (IC base=+0.180)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.835` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.835
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.227 (n=4289)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.219)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.223 (n=4892)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.219)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.268 (n=4290)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.219)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **FILTRO** `hora_utc` > `3.0` → IC=-0.278 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.212 (n=4352)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.257 (n=4479)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.202 (n=5088)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.199 (n=5061)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 6.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.244 (n=5325)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.196)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.192 (n=10978)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.140 (n=11427)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `3.49` → IC=+0.137 (n=13377)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 3.49 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.193 (n=5339)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.143 (n=5149)

  - _Acción_: Kelly boost +0.72€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.125 (n=6702)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 7.0 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `2.61` → IC=+0.143 (n=5037)

  - _Acción_: Kelly boost +0.71€ cuando `lag_apertura_s` < 2.61 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.191 (n=5639)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.137 (n=6979)

  - _Acción_: Kelly boost +0.69€ cuando `restante_min` > 4.95 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `3.16` → IC=+0.137 (n=6704)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 3.16 (IC base=+0.116)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.306 (n=1358)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.292)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.387 (n=694)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.292)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.284 (n=913)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.280)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.365 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.280)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.318 (n=658)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.298)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.301 (n=964)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.298)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.393 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.298)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` < `16.0` → IC=+0.365 (n=94)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.343)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.390 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.343)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.375 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.343)

- **PATRÓN** `libro_liquidez` > `745.0217` → IC=+0.374 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 745.0217 (IC base=+0.343)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.443 (n=922)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.439)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.444 (n=892)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.439)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.440 (n=1073)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.439)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.435 (n=432)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.432)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.437 (n=301)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.432)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.431 (n=448)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.432)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.438 (n=449)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.432)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.449 (n=445)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.446)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.447 (n=375)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.446)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.446 (n=407)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.446)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.447 (n=507)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.446)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4757` → IC=+0.139 (n=17218)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.4757 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.127 (n=17396)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 6.0 (IC base=+0.123)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.127 (n=11976)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 12.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` > `0.978` → IC=+0.246 (n=5740)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.978 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` > `0.7962` → IC=+0.284 (n=969)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7962 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.498` → IC=+0.184 (n=8610)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 3.498 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` > `0.6247` → IC=+0.264 (n=5123)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6247 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` > `0.3041` → IC=+0.249 (n=1774)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3041 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` > `2.7506` → IC=+0.235 (n=4120)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7506 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.134 (n=8554)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.123)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.122 (n=10759)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0062 (IC base=+0.081)

- **PATRÓN** `ibs_20min` < `0.5664` → IC=+0.143 (n=21482)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` < 0.5664 (IC base=+0.081)

- **PATRÓN** `dist_vwap_pct` > `0.6096` → IC=+0.192 (n=1452)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.6096 (IC base=+0.081)

- **PATRÓN** `dist_vwap_pct` < `0.1607` → IC=+0.190 (n=8486)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` < 0.1607 (IC base=+0.081)

- **PATRÓN** `volumen_regimen` < `0.6955` → IC=+0.195 (n=3844)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 0.6955 (IC base=+0.081)

- **PATRÓN** `volumen_pendiente_norm` > `0.2967` → IC=+0.229 (n=2151)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2967 (IC base=+0.081)

- **PATRÓN** `volumen_spike_ratio` > `1.4573` → IC=+0.206 (n=14836)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4573 (IC base=+0.081)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.227 (n=14757)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 100.0 (IC base=+0.081)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `drift_60min` |x|≤ `0.3627` → IC=+0.213 (n=3673)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3627 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.225 (n=1786)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.211)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.213 (n=2463)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` > `0.9868` → IC=+0.278 (n=1665)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9868 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.488` → IC=+0.279 (n=1632)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.488 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.2828` → IC=+0.266 (n=480)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2828 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `1.4361` → IC=+0.213 (n=3519)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4361 (IC base=+0.211)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.225 (n=4046)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.211)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.225 (n=2266)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.211)

- **PATRÓN** `sigma_h` < `0.0102` → IC=+0.243 (n=3221)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0102 (IC base=+0.242)

- **PATRÓN** `sigma_h` > `0.0091` → IC=+0.243 (n=1460)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0091 (IC base=+0.242)

- **PATRÓN** `drift_60min` |x|≤ `0.0893` → IC=+0.280 (n=1075)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0893 (IC base=+0.242)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.251 (n=1206)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.242)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.244 (n=1484)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.242)

- **PATRÓN** `ibs_20min` < `0.5616` → IC=+0.259 (n=3220)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5616 (IC base=+0.242)

- **PATRÓN** `volumen_pendiente_norm` < `0.0948` → IC=+0.246 (n=2919)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0948 (IC base=+0.242)

- **PATRÓN** `volumen_pendiente_norm` > `0.289` → IC=+0.249 (n=436)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.289 (IC base=+0.242)

- **PATRÓN** `volumen_spike_ratio` < `1.446` → IC=+0.245 (n=1024)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.446 (IC base=+0.242)

- **PATRÓN** `volumen_spike_ratio` > `1.855` → IC=+0.244 (n=2046)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.855 (IC base=+0.242)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.244 (n=3704)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.242)

- **PATRÓN** `libro_liquidez` > `1779.0666` → IC=+0.247 (n=2147)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1779.0666 (IC base=+0.242)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0055` → IC=+0.229 (n=2704)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0055 (IC base=+0.224)

- **PATRÓN** `drift_60min` |x|≤ `0.081` → IC=+0.262 (n=1024)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.081 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.235 (n=3212)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.227 (n=2179)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` > `0.9085` → IC=+0.259 (n=1024)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9085 (IC base=+0.224)

- **PATRÓN** `dist_vwap_pct` > `0.1841` → IC=+0.232 (n=1412)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1841 (IC base=+0.224)

- **PATRÓN** `dist_vwap_pct` < `0.5247` → IC=+0.227 (n=3350)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5247 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.906` → IC=+0.264 (n=452)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.906 (IC base=+0.224)

- **PATRÓN** `volumen_regimen` < `1.2254` → IC=+0.224 (n=3073)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2254 (IC base=+0.224)

- **PATRÓN** `volumen_regimen` > `0.6277` → IC=+0.229 (n=3072)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6277 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` > `0.2788` → IC=+0.267 (n=432)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2788 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` > `2.4415` → IC=+0.249 (n=1011)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4415 (IC base=+0.224)

- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.152 (n=3275)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0064 (IC base=+0.129)

- **PATRÓN** `drift_60min` |x|≤ `0.0761` → IC=+0.154 (n=1092)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.0761 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.152 (n=1226)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 17.0 (IC base=+0.129)

- **PATRÓN** `ibs_20min` < `0.3504` → IC=+0.199 (n=2183)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.3504 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.942` → IC=+0.137 (n=2991)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 3.942 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` < `1.199` → IC=+0.136 (n=3274)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 1.199 (IC base=+0.129)

- **PATRÓN** `volumen_pendiente_norm` > `0.0717` → IC=+0.156 (n=1331)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` > 0.0717 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` < `2.4394` → IC=+0.139 (n=3148)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 2.4394 (IC base=+0.129)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.129 (n=4250)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.01 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `179.0` → IC=+0.174 (n=1036)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 179.0 (IC base=+0.129)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0114` → IC=+0.213 (n=1768)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0114 (IC base=+0.196)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.203 (n=4085)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.196)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.263 (n=1515)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.196)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.987` → IC=+0.280 (n=852)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.987 (IC base=+0.196)

- **PATRÓN** `volumen_pendiente_norm` < `0.0977` → IC=+0.198 (n=3490)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` < 0.0977 (IC base=+0.196)

- **PATRÓN** `volumen_pendiente_norm` > `0.3522` → IC=+0.223 (n=503)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3522 (IC base=+0.196)

- **PATRÓN** `volumen_spike_ratio` > `2.73` → IC=+0.214 (n=1724)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.73 (IC base=+0.196)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.201 (n=4711)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.196)

- **PATRÓN** `libro_liquidez` > `1917.4584` → IC=+0.204 (n=1766)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1917.4584 (IC base=+0.196)

- **PATRÓN** `sigma_h` < `0.011` → IC=+0.226 (n=3155)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.011 (IC base=+0.219)

- **PATRÓN** `drift_60min` |x|≤ `0.2928` → IC=+0.231 (n=2388)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2928 (IC base=+0.219)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.243 (n=1363)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.219)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.220 (n=1625)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.219)

- **PATRÓN** `ibs_20min` < `0.0441` → IC=+0.269 (n=1194)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0441 (IC base=+0.219)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.875` → IC=+0.266 (n=391)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.875 (IC base=+0.219)

- **PATRÓN** `volumen_pendiente_norm` > `0.3488` → IC=+0.251 (n=517)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3488 (IC base=+0.219)

- **PATRÓN** `volumen_spike_ratio` < `1.768` → IC=+0.218 (n=1515)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.768 (IC base=+0.219)

- **PATRÓN** `volumen_spike_ratio` > `2.1616` → IC=+0.228 (n=2294)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1616 (IC base=+0.219)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.225 (n=1814)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.219)

- **PATRÓN** `libro_liquidez` > `1904.8952` → IC=+0.226 (n=1624)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1904.8952 (IC base=+0.219)

- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.222 (n=3411)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 25.0 (IC base=+0.219)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.163 (n=203)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=4683)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.157 (n=651)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0038 (IC base=+0.057)

- **PATRÓN** `ibs_20min` > `0.9436` → IC=+0.232 (n=651)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9436 (IC base=+0.057)

- **PATRÓN** `dist_vwap_pct` > `0.14` → IC=+0.338 (n=454)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.14 (IC base=+0.057)

- **PATRÓN** `dist_vwap_pct` < `0.776` → IC=+0.332 (n=861)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.776 (IC base=+0.057)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.077` → IC=+0.201 (n=1424)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.077 (IC base=+0.057)

- **PATRÓN** `volumen_regimen` > `1.0968` → IC=+0.346 (n=349)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0968 (IC base=+0.057)

- **PATRÓN** `volumen_pendiente_norm` < `0.1669` → IC=+0.334 (n=624)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1669 (IC base=+0.057)

- **PATRÓN** `volumen_pendiente_norm` > `0.3024` → IC=+0.334 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3024 (IC base=+0.057)

- **PATRÓN** `volumen_spike_ratio` < `1.4175` → IC=+0.345 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4175 (IC base=+0.057)

- **PATRÓN** `volumen_spike_ratio` > `2.2749` → IC=+0.336 (n=340)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2749 (IC base=+0.057)

- **PATRÓN** `ballena_activa_n` < `142.0` → IC=+0.337 (n=758)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 142.0 (IC base=+0.057)

- **PATRÓN** `ibs_20min` < `0.0897` → IC=+0.188 (n=1222)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.0897 (IC base=+0.050)

- **PATRÓN** `dist_vwap_pct` > `0.3333` → IC=+0.160 (n=598)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.3333 (IC base=+0.050)

- **PATRÓN** `dist_vwap_pct` < `0.1384` → IC=+0.150 (n=2181)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.1384 (IC base=+0.050)

- **PATRÓN** `volumen_regimen` < `1.0043` → IC=+0.156 (n=2039)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.0043 (IC base=+0.050)

- **PATRÓN** `volumen_pendiente_norm` > `0.2815` → IC=+0.213 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2815 (IC base=+0.050)

- **PATRÓN** `volumen_spike_ratio` < `1.7755` → IC=+0.151 (n=1487)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 1.7755 (IC base=+0.050)

- **PATRÓN** `volumen_spike_ratio` > `2.1484` → IC=+0.160 (n=1011)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 2.1484 (IC base=+0.050)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.188 (n=139)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=742)

- **FILTRO** `ibs_20min` < `0.2609` → IC=-0.176 (n=220)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2609
  - _Potencial_: sin este filtro IC_bueno=+0.082 (n=661)

- **FILTRO** `ibs_20min` > `0.2` → IC=-0.133 (n=4605)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2
  - _Potencial_: sin este filtro IC_bueno=+0.154 (n=2273)

- **FILTRO** `sigma_ewma_delta_pct` > `8.287` → IC=-0.225 (n=737)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.287
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=6141)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.178 (n=302)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.75 (IC base=+0.018)

- **PATRÓN** `dist_vwap_pct` > `0.9612` → IC=+0.275 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9612 (IC base=+0.018)

- **PATRÓN** `dist_vwap_pct` < `1.3132` → IC=+0.272 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 1.3132 (IC base=+0.018)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.987` → IC=+0.157 (n=208)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 4.987 (IC base=+0.018)

- **PATRÓN** `volumen_regimen` > `1.0233` → IC=+0.304 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0233 (IC base=+0.018)

- **PATRÓN** `volumen_pendiente_norm` < `0.0791` → IC=+0.285 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0791 (IC base=+0.018)

- **PATRÓN** `volumen_spike_ratio` < `2.1915` → IC=+0.289 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1915 (IC base=+0.018)

- **PATRÓN** `volumen_spike_ratio` > `1.544` → IC=+0.271 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.544 (IC base=+0.018)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.282 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.018)

- **PATRÓN** `ibs_20min` < `0.2` → IC=+0.154 (n=2273)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.2 (IC base=-0.038)

- **PATRÓN** `dist_vwap_pct` > `0.218` → IC=+0.286 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.218 (IC base=-0.038)

- **PATRÓN** `dist_vwap_pct` < `0.4836` → IC=+0.280 (n=1154)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4836 (IC base=-0.038)

- **PATRÓN** `volumen_regimen` < `0.7017` → IC=+0.302 (n=443)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7017 (IC base=-0.038)

- **PATRÓN** `volumen_pendiente_norm` > `0.0793` → IC=+0.302 (n=452)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0793 (IC base=-0.038)

- **PATRÓN** `volumen_spike_ratio` < `2.4762` → IC=+0.302 (n=938)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4762 (IC base=-0.038)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `ibs_20min` < `0.7818` → IC=-0.153 (n=3490)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7818
  - _Potencial_: sin este filtro IC_bueno=+0.123 (n=1799)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.171 (n=1161)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=4128)

- **FILTRO** `ibs_20min` > `0.7422` → IC=-0.193 (n=1837)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7422
  - _Potencial_: sin este filtro IC_bueno=+0.068 (n=5514)

- **PATRÓN** `ibs_20min` > `0.7818` → IC=+0.123 (n=1799)

  - _Acción_: Kelly boost +0.62€ cuando `ibs_20min` > 0.7818 (IC base=-0.059)

- **PATRÓN** `dist_vwap_pct` > `1.0267` → IC=+0.360 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0267 (IC base=-0.059)

- **PATRÓN** `dist_vwap_pct` < `0.2496` → IC=+0.302 (n=901)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2496 (IC base=-0.059)

- **PATRÓN** `volumen_regimen` > `0.7043` → IC=+0.316 (n=907)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7043 (IC base=-0.059)

- **PATRÓN** `volumen_pendiente_norm` < `0.1078` → IC=+0.304 (n=966)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1078 (IC base=-0.059)

- **PATRÓN** `volumen_pendiente_norm` > `0.1692` → IC=+0.303 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1692 (IC base=-0.059)

- **PATRÓN** `volumen_spike_ratio` < `1.5875` → IC=+0.306 (n=436)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5875 (IC base=-0.059)

- **PATRÓN** `volumen_spike_ratio` > `2.5309` → IC=+0.326 (n=331)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5309 (IC base=-0.059)

- **PATRÓN** `dist_vwap_pct` > `0.8075` → IC=+0.275 (n=363)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8075 (IC base=+0.003)

- **PATRÓN** `dist_vwap_pct` < `0.2222` → IC=+0.262 (n=2122)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2222 (IC base=+0.003)

- **PATRÓN** `volumen_regimen` < `0.7188` → IC=+0.269 (n=941)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7188 (IC base=+0.003)

- **PATRÓN** `volumen_regimen` > `1.0635` → IC=+0.282 (n=970)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0635 (IC base=+0.003)

- **PATRÓN** `volumen_pendiente_norm` > `0.1071` → IC=+0.280 (n=763)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1071 (IC base=+0.003)

- **PATRÓN** `volumen_spike_ratio` < `2.1787` → IC=+0.265 (n=1771)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1787 (IC base=+0.003)

- **PATRÓN** `volumen_spike_ratio` > `1.4426` → IC=+0.269 (n=2012)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4426 (IC base=+0.003)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0106` → IC=+0.196 (n=7454)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` > 0.0106 (IC base=+0.088)

- **PATRÓN** `ibs_20min` > `0.8696` → IC=+0.286 (n=10117)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8696 (IC base=+0.088)

- **PATRÓN** `dist_vwap_pct` > `0.9381` → IC=+0.301 (n=1594)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9381 (IC base=+0.088)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.479` → IC=+0.168 (n=9978)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 3.479 (IC base=+0.088)

- **PATRÓN** `volumen_regimen` < `1.1746` → IC=+0.269 (n=8191)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1746 (IC base=+0.088)

- **PATRÓN** `volumen_regimen` > `0.6924` → IC=+0.276 (n=7319)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6924 (IC base=+0.088)

- **PATRÓN** `volumen_pendiente_norm` > `0.2943` → IC=+0.291 (n=1853)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2943 (IC base=+0.088)

- **PATRÓN** `volumen_spike_ratio` > `2.6532` → IC=+0.286 (n=4315)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6532 (IC base=+0.088)

- **PATRÓN** `ballena_activa_n` < `90.0` → IC=+0.308 (n=12558)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 90.0 (IC base=+0.088)

- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.157 (n=7173)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0101 (IC base=+0.081)

- **PATRÓN** `ibs_20min` < `0.641` → IC=+0.154 (n=21484)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.641 (IC base=+0.081)

- **PATRÓN** `dist_vwap_pct` < `0.2546` → IC=+0.278 (n=7251)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2546 (IC base=+0.081)

- **PATRÓN** `volumen_regimen` < `0.6986` → IC=+0.279 (n=3112)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6986 (IC base=+0.081)

- **PATRÓN** `volumen_regimen` > `1.1913` → IC=+0.279 (n=2358)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1913 (IC base=+0.081)

- **PATRÓN** `volumen_pendiente_norm` > `0.295` → IC=+0.325 (n=1578)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.295 (IC base=+0.081)

- **PATRÓN** `volumen_spike_ratio` < `1.5758` → IC=+0.302 (n=4586)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5758 (IC base=+0.081)

- **PATRÓN** `volumen_spike_ratio` > `2.2833` → IC=+0.301 (n=4723)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2833 (IC base=+0.081)

- **PATRÓN** `ballena_activa_n` < `73.0` → IC=+0.309 (n=10395)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 73.0 (IC base=+0.081)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.8011` → IC=-0.127 (n=3970)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8011
  - _Potencial_: sin este filtro IC_bueno=+0.296 (n=2046)

- **FILTRO** `ibs_20min` > `0.7195` → IC=-0.234 (n=1319)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7195
  - _Potencial_: sin este filtro IC_bueno=+0.046 (n=3958)

- **FILTRO** `sigma_ewma_delta_pct` > `4.115` → IC=-0.232 (n=1137)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.115
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=4140)

- **PATRÓN** `ibs_20min` > `0.934` → IC=+0.335 (n=1504)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.934 (IC base=+0.017)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.979` → IC=+0.188 (n=2010)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 2.979 (IC base=+0.017)

- **PATRÓN** `volumen_pendiente_norm` > `0.2292` → IC=+0.326 (n=388)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2292 (IC base=+0.017)

- **PATRÓN** `volumen_spike_ratio` < `1.4467` → IC=+0.279 (n=641)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4467 (IC base=+0.017)

- **PATRÓN** `volumen_spike_ratio` > `2.2415` → IC=+0.301 (n=872)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2415 (IC base=+0.017)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.316 (n=1305)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.017)

- **PATRÓN** `ibs_20min` < `0.1727` → IC=+0.166 (n=1321)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.1727 (IC base=-0.024)

- **PATRÓN** `volumen_pendiente_norm` < `0.1519` → IC=+0.401 (n=989)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1519 (IC base=-0.024)

- **PATRÓN** `volumen_spike_ratio` < `2.6658` → IC=+0.403 (n=958)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.6658 (IC base=-0.024)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.398 (n=983)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 23.0 (IC base=-0.024)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.2967` → IC=+0.224 (n=733)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2967 (IC base=+0.012)

- **PATRÓN** `volumen_regimen` < `1.1944` → IC=+0.209 (n=2180)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1944 (IC base=+0.012)

- **PATRÓN** `volumen_regimen` > `0.694` → IC=+0.215 (n=1949)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.694 (IC base=+0.012)

- **PATRÓN** `volumen_pendiente_norm` > `0.2781` → IC=+0.242 (n=297)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2781 (IC base=+0.012)

- **PATRÓN** `volumen_spike_ratio` < `1.4202` → IC=+0.232 (n=718)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4202 (IC base=+0.012)

- **PATRÓN** `ballena_activa_n` < `263.0` → IC=+0.245 (n=1436)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 263.0 (IC base=+0.012)

- **PATRÓN** `dist_vwap_pct` < `0.1305` → IC=+0.256 (n=1552)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1305 (IC base=-0.004)

- **PATRÓN** `volumen_regimen` > `0.618` → IC=+0.251 (n=1512)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.618 (IC base=-0.004)

- **PATRÓN** `volumen_pendiente_norm` > `0.2701` → IC=+0.311 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2701 (IC base=-0.004)

- **PATRÓN** `volumen_spike_ratio` < `1.5272` → IC=+0.255 (n=642)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5272 (IC base=-0.004)

- **PATRÓN** `volumen_spike_ratio` > `2.1503` → IC=+0.262 (n=661)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1503 (IC base=-0.004)

- **PATRÓN** `ballena_activa_n` < `212.0` → IC=+0.267 (n=647)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 212.0 (IC base=-0.004)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0093` → IC=+0.318 (n=2096)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0093 (IC base=+0.283)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.292 (n=3299)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.283)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.324 (n=1715)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.283)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.582` → IC=+0.305 (n=2100)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.582 (IC base=+0.283)

- **PATRÓN** `volumen_pendiente_norm` < `0.0977` → IC=+0.297 (n=2757)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0977 (IC base=+0.283)

- **PATRÓN** `volumen_spike_ratio` > `1.6063` → IC=+0.290 (n=3052)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6063 (IC base=+0.283)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.293 (n=3770)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.283)

- **PATRÓN** `libro_liquidez` > `2025.081` → IC=+0.296 (n=1048)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2025.081 (IC base=+0.283)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.308 (n=1914)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.283)

- **PATRÓN** `sigma_h` > `0.0074` → IC=+0.324 (n=2536)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0074 (IC base=+0.305)

- **PATRÓN** `drift_60min` |x|≤ `0.1772` → IC=+0.325 (n=1249)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1772 (IC base=+0.305)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.328 (n=1094)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.305)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.306 (n=1283)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.305)

- **PATRÓN** `ibs_20min` > `0.1429` → IC=+0.316 (n=1897)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1429 (IC base=+0.305)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.173` → IC=+0.312 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.173 (IC base=+0.305)

- **PATRÓN** `volumen_pendiente_norm` < `0.1999` → IC=+0.306 (n=2789)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1999 (IC base=+0.305)

- **PATRÓN** `volumen_pendiente_norm` > `0.3455` → IC=+0.311 (n=459)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3455 (IC base=+0.305)

- **PATRÓN** `volumen_spike_ratio` < `1.5954` → IC=+0.304 (n=913)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5954 (IC base=+0.305)

- **PATRÓN** `volumen_spike_ratio` > `2.7414` → IC=+0.321 (n=1241)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7414 (IC base=+0.305)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.308 (n=1443)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.305)

- **PATRÓN** `libro_liquidez` > `1908.66` → IC=+0.315 (n=1287)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1908.66 (IC base=+0.305)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.312 (n=2382)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 23.0 (IC base=+0.305)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7262` → IC=-0.183 (n=1400)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7262
  - _Potencial_: sin este filtro IC_bueno=+0.068 (n=4202)

- **PATRÓN** `ibs_20min` > `0.8479` → IC=+0.158 (n=1376)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` > 0.8479 (IC base=+0.021)

- **PATRÓN** `dist_vwap_pct` > `0.142` → IC=+0.234 (n=1025)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.142 (IC base=+0.021)

- **PATRÓN** `dist_vwap_pct` < `0.3574` → IC=+0.234 (n=1948)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3574 (IC base=+0.021)

- **PATRÓN** `volumen_regimen` < `1.1603` → IC=+0.234 (n=1981)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1603 (IC base=+0.021)

- **PATRÓN** `volumen_regimen` > `0.673` → IC=+0.230 (n=1770)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.673 (IC base=+0.021)

- **PATRÓN** `volumen_pendiente_norm` < `0.1628` → IC=+0.234 (n=2081)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1628 (IC base=+0.021)

- **PATRÓN** `volumen_pendiente_norm` > `0.0761` → IC=+0.237 (n=733)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0761 (IC base=+0.021)

- **PATRÓN** `volumen_spike_ratio` < `2.4586` → IC=+0.238 (n=1921)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4586 (IC base=+0.021)

- **PATRÓN** `ballena_activa_n` < `115.0` → IC=+0.254 (n=1960)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 115.0 (IC base=+0.021)

- **PATRÓN** `dist_vwap_pct` < `0.3486` → IC=+0.251 (n=1582)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3486 (IC base=+0.005)

- **PATRÓN** `volumen_regimen` < `1.0168` → IC=+0.258 (n=1253)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0168 (IC base=+0.005)

- **PATRÓN** `volumen_pendiente_norm` > `0.2817` → IC=+0.310 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2817 (IC base=+0.005)

- **PATRÓN** `volumen_spike_ratio` < `1.5218` → IC=+0.294 (n=601)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5218 (IC base=+0.005)

- **PATRÓN** `volumen_spike_ratio` > `2.426` → IC=+0.277 (n=455)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.426 (IC base=+0.005)

- **PATRÓN** `ballena_activa_n` < `99.0` → IC=+0.282 (n=1226)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 99.0 (IC base=+0.005)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7407` → IC=-0.247 (n=2306)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7407
  - _Potencial_: sin este filtro IC_bueno=+0.312 (n=2313)

- **FILTRO** `ibs_20min` > `0.6216` → IC=-0.230 (n=1094)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6216
  - _Potencial_: sin este filtro IC_bueno=+0.149 (n=3288)

- **FILTRO** `sigma_ewma_delta_pct` > `8.266` → IC=-0.253 (n=500)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.266
  - _Potencial_: sin este filtro IC_bueno=+0.094 (n=3882)

- **PATRÓN** `ibs_20min` > `0.7407` → IC=+0.312 (n=2313)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7407 (IC base=+0.033)

- **PATRÓN** `dist_vwap_pct` > `1.045` → IC=+0.356 (n=339)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.045 (IC base=+0.033)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.438` → IC=+0.154 (n=1871)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 2.438 (IC base=+0.033)

- **PATRÓN** `volumen_regimen` < `0.8453` → IC=+0.341 (n=1122)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8453 (IC base=+0.033)

- **PATRÓN** `volumen_regimen` > `0.6975` → IC=+0.334 (n=1503)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6975 (IC base=+0.033)

- **PATRÓN** `volumen_pendiente_norm` < `0.1563` → IC=+0.334 (n=1739)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1563 (IC base=+0.033)

- **PATRÓN** `volumen_pendiente_norm` > `0.2747` → IC=+0.362 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2747 (IC base=+0.033)

- **PATRÓN** `volumen_spike_ratio` < `1.427` → IC=+0.363 (n=545)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.427 (IC base=+0.033)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.350 (n=1118)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=+0.033)

- **PATRÓN** `ibs_20min` < `0.6216` → IC=+0.149 (n=3288)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.6216 (IC base=+0.054)

- **PATRÓN** `dist_vwap_pct` < `0.3042` → IC=+0.261 (n=1664)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3042 (IC base=+0.054)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.014` → IC=+0.129 (n=3089)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` < 3.014 (IC base=+0.054)

- **PATRÓN** `volumen_regimen` < `0.6945` → IC=+0.281 (n=718)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6945 (IC base=+0.054)

- **PATRÓN** `volumen_pendiente_norm` > `0.0703` → IC=+0.282 (n=649)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0703 (IC base=+0.054)

- **PATRÓN** `volumen_spike_ratio` < `1.807` → IC=+0.276 (n=1052)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.807 (IC base=+0.054)

- **PATRÓN** `ballena_activa_n` < `39.0` → IC=+0.280 (n=1418)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 39.0 (IC base=+0.054)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.359 (n=2098)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.316)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.318 (n=2370)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.316)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.317 (n=1118)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.316)

- **PATRÓN** `ibs_20min` > `0.6667` → IC=+0.345 (n=2348)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6667 (IC base=+0.316)

- **PATRÓN** `dist_vwap_pct` > `0.2114` → IC=+0.338 (n=1287)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2114 (IC base=+0.316)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.802` → IC=+0.332 (n=1131)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.802 (IC base=+0.316)

- **PATRÓN** `volumen_regimen` > `0.8704` → IC=+0.335 (n=1565)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8704 (IC base=+0.316)

- **PATRÓN** `volumen_pendiente_norm` > `0.281` → IC=+0.348 (n=346)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.281 (IC base=+0.316)

- **PATRÓN** `volumen_spike_ratio` > `1.4315` → IC=+0.328 (n=2262)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4315 (IC base=+0.316)

- **PATRÓN** `libro_liquidez` > `2978.4963` → IC=+0.327 (n=783)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2978.4963 (IC base=+0.316)

- **PATRÓN** `ballena_activa_n` < `39.0` → IC=+0.345 (n=2071)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 39.0 (IC base=+0.316)

- **PATRÓN** `sigma_h` > `0.0154` → IC=+0.348 (n=1671)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0154 (IC base=+0.317)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.324 (n=1277)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.317)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.317 (n=1214)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.317)

- **PATRÓN** `ibs_20min` < `0.38` → IC=+0.335 (n=2507)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.38 (IC base=+0.317)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.628` → IC=+0.329 (n=934)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.628 (IC base=+0.317)

- **PATRÓN** `volumen_regimen` < `0.7185` → IC=+0.320 (n=1105)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7185 (IC base=+0.317)

- **PATRÓN** `volumen_regimen` > `1.212` → IC=+0.346 (n=836)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.212 (IC base=+0.317)

- **PATRÓN** `volumen_pendiente_norm` > `0.2309` → IC=+0.364 (n=475)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2309 (IC base=+0.317)

- **PATRÓN** `volumen_spike_ratio` < `1.4117` → IC=+0.325 (n=775)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4117 (IC base=+0.317)

- **PATRÓN** `volumen_spike_ratio` > `2.139` → IC=+0.317 (n=1054)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.139 (IC base=+0.317)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0124` → IC=+0.224 (n=5555)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0124 (IC base=+0.174)

- **PATRÓN** `drift_60min` |x|≤ `0.1219` → IC=+0.191 (n=7329)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.1219 (IC base=+0.174)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.184 (n=17239)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.174)

- **PATRÓN** `ibs_20min` > `0.5391` → IC=+0.231 (n=16646)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5391 (IC base=+0.174)

- **PATRÓN** `dist_vwap_pct` > `0.1612` → IC=+0.205 (n=6403)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1612 (IC base=+0.174)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.796` → IC=+0.257 (n=3242)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.796 (IC base=+0.174)

- **PATRÓN** `volumen_regimen` < `1.1814` → IC=+0.154 (n=11080)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 1.1814 (IC base=+0.174)

- **PATRÓN** `volumen_regimen` > `0.6249` → IC=+0.153 (n=11079)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 0.6249 (IC base=+0.174)

- **PATRÓN** `volumen_pendiente_norm` > `0.2941` → IC=+0.204 (n=2417)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2941 (IC base=+0.174)

- **PATRÓN** `volumen_spike_ratio` > `2.6096` → IC=+0.188 (n=5395)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.6096 (IC base=+0.174)

- **PATRÓN** `ballena_activa_n` < `88.0` → IC=+0.193 (n=15590)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 88.0 (IC base=+0.174)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.191 (n=7194)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0058 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.0802` → IC=+0.220 (n=5444)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0802 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.211 (n=6194)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` < `0.5253` → IC=+0.238 (n=16329)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5253 (IC base=+0.182)

- **PATRÓN** `dist_vwap_pct` < `0.1805` → IC=+0.176 (n=11825)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.1805 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.557` → IC=+0.192 (n=2603)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 9.557 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.518` → IC=+0.189 (n=14530)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` < 2.518 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` < `1.1813` → IC=+0.163 (n=11629)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.1813 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.2942` → IC=+0.217 (n=2440)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2942 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `2.6341` → IC=+0.192 (n=5174)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.6341 (IC base=+0.182)

- **PATRÓN** `ballena_activa_n` < `92.0` → IC=+0.197 (n=15327)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 92.0 (IC base=+0.182)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.228 (n=916)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0056 (IC base=+0.228)

- **PATRÓN** `drift_60min` |x|≤ `0.1043` → IC=+0.258 (n=1206)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1043 (IC base=+0.228)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.233 (n=2848)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.228)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.230 (n=1862)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.228)

- **PATRÓN** `ibs_20min` > `0.9421` → IC=+0.297 (n=1828)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9421 (IC base=+0.228)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.517` → IC=+0.331 (n=890)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.517 (IC base=+0.228)

- **PATRÓN** `volumen_pendiente_norm` > `0.2807` → IC=+0.293 (n=414)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2807 (IC base=+0.228)

- **PATRÓN** `volumen_spike_ratio` < `1.8326` → IC=+0.225 (n=1742)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8326 (IC base=+0.228)

- **PATRÓN** `volumen_spike_ratio` > `1.4336` → IC=+0.228 (n=2613)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4336 (IC base=+0.228)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.238 (n=3041)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.228)

- **PATRÓN** `sigma_h` < `0.0097` → IC=+0.258 (n=2218)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0097 (IC base=+0.255)

- **PATRÓN** `drift_60min` |x|≤ `0.0973` → IC=+0.311 (n=976)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0973 (IC base=+0.255)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.260 (n=2286)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.255)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.257 (n=2018)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.255)

- **PATRÓN** `ibs_20min` < `0.0499` → IC=+0.301 (n=976)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0499 (IC base=+0.255)

- **PATRÓN** `volumen_pendiente_norm` < `0.0993` → IC=+0.258 (n=1949)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0993 (IC base=+0.255)

- **PATRÓN** `volumen_pendiente_norm` > `0.3017` → IC=+0.272 (n=336)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3017 (IC base=+0.255)

- **PATRÓN** `volumen_spike_ratio` < `1.4466` → IC=+0.275 (n=708)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4466 (IC base=+0.255)

- **PATRÓN** `volumen_spike_ratio` > `2.6989` → IC=+0.257 (n=707)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6989 (IC base=+0.255)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.258 (n=2561)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.255)

- **PATRÓN** `libro_liquidez` > `1779.5665` → IC=+0.262 (n=1479)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1779.5665 (IC base=+0.255)

- **PATRÓN** `ballena_activa_n` < `9.0` → IC=+0.256 (n=1023)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 9.0 (IC base=+0.255)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.199 (n=849)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.131)

- **PATRÓN** `drift_60min` |x|≤ `0.0647` → IC=+0.179 (n=845)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.0647 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.146 (n=2648)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.131)

- **PATRÓN** `ibs_20min` > `0.2641` → IC=+0.208 (n=2533)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2641 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` > `0.183` → IC=+0.211 (n=1279)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.183 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.71` → IC=+0.209 (n=466)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.71 (IC base=+0.131)

- **PATRÓN** `volumen_regimen` < `0.6943` → IC=+0.137 (n=1115)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 0.6943 (IC base=+0.131)

- **PATRÓN** `volumen_regimen` > `1.0569` → IC=+0.135 (n=1149)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` > 1.0569 (IC base=+0.131)

- **PATRÓN** `volumen_pendiente_norm` > `0.2801` → IC=+0.173 (n=396)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.2801 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` < `1.5049` → IC=+0.140 (n=1095)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.5049 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` > `2.4689` → IC=+0.147 (n=830)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 2.4689 (IC base=+0.131)

- **PATRÓN** `ballena_activa_n` < `401.0` → IC=+0.136 (n=2459)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 401.0 (IC base=+0.131)

- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.173 (n=2686)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0064 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.237` → IC=+0.170 (n=2364)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.237 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.181 (n=1286)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 15.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` < `0.6102` → IC=+0.208 (n=2684)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6102 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.885` → IC=+0.175 (n=502)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 10.885 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.998` → IC=+0.151 (n=2340)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` < 3.998 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `1.1994` → IC=+0.159 (n=2684)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.1994 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` < `0.0937` → IC=+0.149 (n=2321)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` < 0.0937 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `2.4589` → IC=+0.151 (n=2559)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.4589 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `212.0` → IC=+0.186 (n=1103)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 212.0 (IC base=+0.146)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.227 (n=1885)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0098 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.2471` → IC=+0.233 (n=1885)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2471 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.218 (n=2938)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.293 (n=1499)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.064` → IC=+0.303 (n=668)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.064 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` < `0.0991` → IC=+0.211 (n=2457)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0991 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` > `0.3522` → IC=+0.234 (n=401)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3522 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `2.7141` → IC=+0.226 (n=1251)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7141 (IC base=+0.212)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.216 (n=3419)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `1912.7172` → IC=+0.221 (n=1282)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1912.7172 (IC base=+0.212)

- **PATRÓN** `sigma_h` < `0.0107` → IC=+0.249 (n=2185)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0107 (IC base=+0.238)

- **PATRÓN** `drift_60min` |x|≤ `0.4117` → IC=+0.261 (n=2184)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4117 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.280 (n=958)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.238)

- **PATRÓN** `ibs_20min` < `0.037` → IC=+0.289 (n=1094)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.037 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.028` → IC=+0.281 (n=331)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.028 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` > `0.3581` → IC=+0.284 (n=414)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3581 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` < `1.7757` → IC=+0.238 (n=1054)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7757 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` > `2.189` → IC=+0.250 (n=1596)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.189 (IC base=+0.238)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.238 (n=1273)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.238)

- **PATRÓN** `libro_liquidez` > `1894.4532` → IC=+0.250 (n=1126)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1894.4532 (IC base=+0.238)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.242 (n=1610)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.238)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.204 (n=916)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.130)

- **PATRÓN** `drift_60min` |x|≤ `0.0779` → IC=+0.182 (n=915)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.0779 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.140 (n=2826)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 5.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` > `0.2535` → IC=+0.192 (n=2737)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.2535 (IC base=+0.130)

- **PATRÓN** `dist_vwap_pct` > `0.1379` → IC=+0.185 (n=1592)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1379 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.265` → IC=+0.200 (n=472)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.265 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` < `0.843` → IC=+0.137 (n=1825)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 0.843 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` > `1.182` → IC=+0.131 (n=913)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` > 1.182 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` > `0.2885` → IC=+0.170 (n=413)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.2885 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` < `1.8237` → IC=+0.129 (n=1788)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 1.8237 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` > `2.5146` → IC=+0.147 (n=894)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 2.5146 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `6802.938` → IC=+0.196 (n=1241)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 6802.938 (IC base=+0.130)

- **PATRÓN** `ballena_activa_n` < `128.0` → IC=+0.134 (n=2683)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 128.0 (IC base=+0.130)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.164 (n=2569)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0066 (IC base=+0.128)

- **PATRÓN** `drift_60min` |x|≤ `0.3939` → IC=+0.145 (n=2917)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.3939 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.165 (n=1408)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 15.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` < `0.6789` → IC=+0.184 (n=2917)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.6789 (IC base=+0.128)

- **PATRÓN** `dist_vwap_pct` < `0.1594` → IC=+0.156 (n=2945)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1594 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.258` → IC=+0.141 (n=698)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 9.258 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` < `0.8509` → IC=+0.150 (n=1946)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.8509 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` > `0.2952` → IC=+0.178 (n=433)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.2952 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` < `1.801` → IC=+0.131 (n=1843)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 1.801 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` > `2.5352` → IC=+0.133 (n=921)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 2.5352 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `6244.4779` → IC=+0.190 (n=1323)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 6244.4779 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.148 (n=924)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 49.0 (IC base=+0.128)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **FILTRO** `ibs_20min` > `0.65` → IC=-0.187 (n=1061)

  - _Acción_: SKIP cuando `ibs_20min` > 0.65
  - _Potencial_: sin este filtro IC_bueno=+0.218 (n=3190)

- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.167 (n=1384)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` > 0.0112 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.159 (n=1451)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 15.0 (IC base=+0.121)

- **PATRÓN** `ibs_20min` > `0.4727` → IC=+0.206 (n=3050)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4727 (IC base=+0.121)

- **PATRÓN** `dist_vwap_pct` > `0.1947` → IC=+0.187 (n=1667)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1947 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.0` → IC=+0.288 (n=644)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.0 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` < `1.1718` → IC=+0.132 (n=3050)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 1.1718 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` > `0.6294` → IC=+0.121 (n=3050)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` > 0.6294 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` < `0.1632` → IC=+0.127 (n=3107)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` < 0.1632 (IC base=+0.121)

- **PATRÓN** `volumen_spike_ratio` < `1.5429` → IC=+0.130 (n=1302)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 1.5429 (IC base=+0.121)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.122 (n=3190)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.02 (IC base=+0.121)

- **PATRÓN** `libro_liquidez` > `2654.1703` → IC=+0.197 (n=1383)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 2654.1703 (IC base=+0.121)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.143 (n=1312)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 20.0 (IC base=+0.121)

- **PATRÓN** `sigma_h` < `0.0118` → IC=+0.141 (n=3189)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0118 (IC base=+0.117)

- **PATRÓN** `drift_60min` |x|≤ `0.111` → IC=+0.162 (n=1063)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.111 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.133 (n=3256)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 5.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` < `0.65` → IC=+0.218 (n=3190)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.65 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` < `0.211` → IC=+0.142 (n=3116)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.211 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.258` → IC=+0.137 (n=2821)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 2.258 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` < `1.1725` → IC=+0.125 (n=3189)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` < 1.1725 (IC base=+0.117)

- **PATRÓN** `volumen_pendiente_norm` > `0.2743` → IC=+0.141 (n=438)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_pendiente_norm` > 0.2743 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` < `1.4337` → IC=+0.131 (n=1004)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 1.4337 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `2536.4746` → IC=+0.183 (n=1446)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 2536.4746 (IC base=+0.117)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.123 (n=1992)

  - _Acción_: Kelly boost +0.61€ cuando `ballena_activa_n` < 27.0 (IC base=+0.117)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0131` → IC=+0.247 (n=2465)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0131 (IC base=+0.225)

- **PATRÓN** `drift_60min` |x|≤ `0.1667` → IC=+0.238 (n=1215)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1667 (IC base=+0.225)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.230 (n=2863)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.228 (n=2487)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.225)

- **PATRÓN** `ibs_20min` > `0.6667` → IC=+0.256 (n=2761)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6667 (IC base=+0.225)

- **PATRÓN** `dist_vwap_pct` > `0.1805` → IC=+0.232 (n=1713)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1805 (IC base=+0.225)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.588` → IC=+0.254 (n=1242)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.588 (IC base=+0.225)

- **PATRÓN** `volumen_regimen` > `0.6229` → IC=+0.234 (n=2759)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6229 (IC base=+0.225)

- **PATRÓN** `volumen_pendiente_norm` > `0.2353` → IC=+0.267 (n=514)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2353 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` < `2.4732` → IC=+0.228 (n=2691)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4732 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` > `1.8151` → IC=+0.232 (n=1794)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8151 (IC base=+0.225)

- **PATRÓN** `libro_liquidez` > `2841.1464` → IC=+0.228 (n=1251)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2841.1464 (IC base=+0.225)

- **PATRÓN** `sigma_h` < `0.0129` → IC=+0.241 (n=1250)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0129 (IC base=+0.239)

- **PATRÓN** `sigma_h` > `0.023` → IC=+0.249 (n=1288)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.023 (IC base=+0.239)

- **PATRÓN** `drift_60min` |x|≤ `0.5725` → IC=+0.247 (n=2841)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5725 (IC base=+0.239)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.253 (n=1404)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.239)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.244 (n=1268)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.239)

- **PATRÓN** `ibs_20min` < `0.44` → IC=+0.264 (n=2847)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.44 (IC base=+0.239)

- **PATRÓN** `dist_vwap_pct` > `1.1261` → IC=+0.255 (n=276)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1261 (IC base=+0.239)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.043` → IC=+0.265 (n=398)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.043 (IC base=+0.239)

- **PATRÓN** `volumen_regimen` < `0.8632` → IC=+0.244 (n=1894)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8632 (IC base=+0.239)

- **PATRÓN** `volumen_regimen` > `0.6394` → IC=+0.243 (n=2841)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6394 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` > `0.2811` → IC=+0.290 (n=394)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2811 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` < `2.527` → IC=+0.237 (n=2675)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.527 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` > `1.4358` → IC=+0.240 (n=2675)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4358 (IC base=+0.239)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.208 (n=1429)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.161)

- **PATRÓN** `drift_60min` |x|≤ `0.1325` → IC=+0.175 (n=1888)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.1325 (IC base=+0.161)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.173 (n=4480)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 5.0 (IC base=+0.161)

- **PATRÓN** `ibs_20min` > `0.3087` → IC=+0.197 (n=4284)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.3087 (IC base=+0.161)

- **PATRÓN** `dist_vwap_pct` > `0.2194` → IC=+0.182 (n=1672)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.2194 (IC base=+0.161)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.63` → IC=+0.209 (n=700)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.63 (IC base=+0.161)

- **PATRÓN** `volumen_regimen` < `0.8606` → IC=+0.171 (n=2607)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` < 0.8606 (IC base=+0.161)

- **PATRÓN** `volumen_regimen` > `1.1918` → IC=+0.171 (n=1303)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` > 1.1918 (IC base=+0.161)

- **PATRÓN** `volumen_pendiente_norm` > `0.1574` → IC=+0.174 (n=1132)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.1574 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` < `1.528` → IC=+0.166 (n=1838)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 1.528 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` > `1.8094` → IC=+0.163 (n=2784)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 1.8094 (IC base=+0.161)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.162 (n=4797)

  - _Acción_: Kelly boost +0.81€ cuando `libro_spread` < 0.02 (IC base=+0.161)

- **PATRÓN** `libro_liquidez` > `7946.3404` → IC=+0.184 (n=1943)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 7946.3404 (IC base=+0.161)

- **PATRÓN** `ibs_20min` < `0.3846` → IC=+0.170 (n=3089)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.3846 (IC base=+0.091)

- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.134 (n=2005)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 25.0 (IC base=+0.091)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.196 (n=1128)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0061 (IC base=+0.180)

- **PATRÓN** `drift_60min` |x|≤ `0.3283` → IC=+0.198 (n=1126)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.3283 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.213 (n=1017)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` > `0.6075` → IC=+0.236 (n=752)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6075 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` > `0.3086` → IC=+0.214 (n=341)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3086 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.949` → IC=+0.206 (n=492)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.949 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.356` → IC=+0.180 (n=1185)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` < 6.356 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` < `0.8799` → IC=+0.193 (n=751)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` < 0.8799 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.0705` → IC=+0.192 (n=443)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.0705 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` < `2.1671` → IC=+0.195 (n=972)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 2.1671 (IC base=+0.180)

- **PATRÓN** `libro_liquidez` > `15801.9297` → IC=+0.190 (n=511)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 15801.9297 (IC base=+0.180)

- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.162 (n=465)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0031 (IC base=+0.088)

- **PATRÓN** `ibs_20min` < `0.1986` → IC=+0.202 (n=613)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1986 (IC base=+0.088)

- **PATRÓN** `volumen_pendiente_norm` > `0.1612` → IC=+0.135 (n=365)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` > 0.1612 (IC base=+0.088)

- **PATRÓN** `ballena_activa_n` < `162.0` → IC=+0.179 (n=599)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 162.0 (IC base=+0.088)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.235 (n=586)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.163)

- **PATRÓN** `drift_60min` |x|≤ `0.2084` → IC=+0.164 (n=886)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.2084 (IC base=+0.163)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.181 (n=1380)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 5.0 (IC base=+0.163)

- **PATRÓN** `ibs_20min` > `0.801` → IC=+0.264 (n=604)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.801 (IC base=+0.163)

- **PATRÓN** `dist_vwap_pct` > `0.8169` → IC=+0.190 (n=224)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.8169 (IC base=+0.163)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.864` → IC=+0.216 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.864 (IC base=+0.163)

- **PATRÓN** `volumen_regimen` < `0.8293` → IC=+0.172 (n=886)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` < 0.8293 (IC base=+0.163)

- **PATRÓN** `volumen_regimen` > `1.1537` → IC=+0.163 (n=443)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 1.1537 (IC base=+0.163)

- **PATRÓN** `volumen_pendiente_norm` > `0.2183` → IC=+0.209 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2183 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` > `2.4744` → IC=+0.186 (n=437)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.4744 (IC base=+0.163)

- **PATRÓN** `libro_liquidez` > `8209.8692` → IC=+0.173 (n=603)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 8209.8692 (IC base=+0.163)

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.120 (n=867)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.60€ cuando `sigma_h` < 0.0052 (IC base=+0.085)

- **PATRÓN** `ibs_20min` < `0.0882` → IC=+0.198 (n=432)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.0882 (IC base=+0.085)

- **PATRÓN** `libro_liquidez` > `5148.7656` → IC=+0.135 (n=863)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 5148.7656 (IC base=+0.085)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.128 (n=423)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 34.0 (IC base=+0.085)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.143 (n=953)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.0106 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.171 (n=761)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 11.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` > `0.4571` → IC=+0.184 (n=1084)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.4571 (IC base=+0.130)

- **PATRÓN** `dist_vwap_pct` > `0.932` → IC=+0.183 (n=184)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.932 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.857` → IC=+0.230 (n=432)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.857 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` < `1.0464` → IC=+0.138 (n=953)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 1.0464 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` > `0.7008` → IC=+0.142 (n=967)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 0.7008 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` > `0.2253` → IC=+0.162 (n=196)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.2253 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` < `2.4087` → IC=+0.135 (n=1048)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 2.4087 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` > `1.8035` → IC=+0.130 (n=698)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 1.8035 (IC base=+0.130)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.133 (n=1137)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.02 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `2727.3504` → IC=+0.169 (n=491)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 2727.3504 (IC base=+0.130)

- **PATRÓN** `ibs_20min` < `0.3684` → IC=+0.178 (n=796)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.3684 (IC base=+0.064)

- **PATRÓN** `libro_liquidez` > `2871.2614` → IC=+0.157 (n=397)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 2871.2614 (IC base=+0.064)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0175` → IC=+0.236 (n=248)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0175 (IC base=+0.192)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.232 (n=177)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.192)

- **PATRÓN** `ibs_20min` > `0.5522` → IC=+0.213 (n=332)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5522 (IC base=+0.192)

- **PATRÓN** `dist_vwap_pct` > `0.2222` → IC=+0.210 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2222 (IC base=+0.192)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.789` → IC=+0.213 (n=364)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.789 (IC base=+0.192)

- **PATRÓN** `volumen_regimen` > `1.1848` → IC=+0.270 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1848 (IC base=+0.192)

- **PATRÓN** `volumen_pendiente_norm` < `0.1035` → IC=+0.203 (n=331)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1035 (IC base=+0.192)

- **PATRÓN** `volumen_pendiente_norm` > `0.0785` → IC=+0.202 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0785 (IC base=+0.192)

- **PATRÓN** `volumen_spike_ratio` < `2.1609` → IC=+0.207 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1609 (IC base=+0.192)

- **PATRÓN** `volumen_spike_ratio` > `1.4242` → IC=+0.201 (n=343)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4242 (IC base=+0.192)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.203 (n=405)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.192)

- **PATRÓN** `libro_liquidez` > `3014.8723` → IC=+0.198 (n=124)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 3014.8723 (IC base=+0.192)

- **PATRÓN** `sigma_h` > `0.0243` → IC=+0.176 (n=183)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.0243 (IC base=+0.142)

- **PATRÓN** `drift_60min` |x|≤ `0.3053` → IC=+0.153 (n=269)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.3053 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.196 (n=192)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 15.0 (IC base=+0.142)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.160 (n=357)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.5 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` > `1.2224` → IC=+0.290 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2224 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.232` → IC=+0.176 (n=106)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 5.232 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.661` → IC=+0.142 (n=464)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 7.661 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` < `0.8755` → IC=+0.190 (n=269)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` < 0.8755 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` < `0.113` → IC=+0.160 (n=371)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` < 0.113 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` > `0.2295` → IC=+0.167 (n=76)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.2295 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` < `1.508` → IC=+0.195 (n=129)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 1.508 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` > `2.6761` → IC=+0.157 (n=129)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 2.6761 (IC base=+0.142)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.159 (n=385)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 20.0 (IC base=+0.142)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0124` → IC=+0.230 (n=7270)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0124 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.189 (n=22692)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` > `0.4312` → IC=+0.228 (n=21791)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4312 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` > `0.879` → IC=+0.211 (n=2618)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.879 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.949` → IC=+0.256 (n=5329)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.949 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` < `1.2153` → IC=+0.159 (n=14669)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2153 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.2414` → IC=+0.207 (n=3915)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2414 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `2.6212` → IC=+0.194 (n=7090)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.6212 (IC base=+0.180)

- **PATRÓN** `ballena_activa_n` < `103.0` → IC=+0.202 (n=20418)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 103.0 (IC base=+0.180)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.198 (n=8802)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.006 (IC base=+0.194)

- **PATRÓN** `sigma_h` > `0.0122` → IC=+0.203 (n=6669)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0122 (IC base=+0.194)

- **PATRÓN** `drift_60min` |x|≤ `0.4802` → IC=+0.197 (n=19985)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.4802 (IC base=+0.194)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.216 (n=7505)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.194)

- **PATRÓN** `ibs_20min` < `0.5916` → IC=+0.243 (n=19984)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5916 (IC base=+0.194)

- **PATRÓN** `dist_vwap_pct` < `0.1778` → IC=+0.176 (n=12569)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.1778 (IC base=+0.194)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.42` → IC=+0.195 (n=2704)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 9.42 (IC base=+0.194)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.533` → IC=+0.199 (n=18524)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.533 (IC base=+0.194)

- **PATRÓN** `volumen_regimen` < `0.7017` → IC=+0.174 (n=5907)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.7017 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` > `0.2929` → IC=+0.251 (n=2751)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2929 (IC base=+0.194)

- **PATRÓN** `volumen_spike_ratio` > `2.6321` → IC=+0.205 (n=6372)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6321 (IC base=+0.194)

- **PATRÓN** `ballena_activa_n` < `92.0` → IC=+0.210 (n=18904)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 92.0 (IC base=+0.194)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.250 (n=1693)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.236)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.236 (n=2351)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.236)

- **PATRÓN** `ibs_20min` > `0.8656` → IC=+0.301 (n=2326)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8656 (IC base=+0.236)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.518` → IC=+0.336 (n=1136)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.518 (IC base=+0.236)

- **PATRÓN** `volumen_pendiente_norm` > `0.2323` → IC=+0.299 (n=625)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2323 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` > `2.288` → IC=+0.242 (n=1527)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.288 (IC base=+0.236)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.251 (n=3829)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.236)

- **PATRÓN** `libro_liquidez` > `2045.1302` → IC=+0.237 (n=1163)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2045.1302 (IC base=+0.236)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.253 (n=2212)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.236)

- **PATRÓN** `sigma_h` < `0.0101` → IC=+0.269 (n=3098)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0101 (IC base=+0.267)

- **PATRÓN** `drift_60min` |x|≤ `0.1214` → IC=+0.294 (n=1363)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1214 (IC base=+0.267)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.270 (n=2859)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.267)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.269 (n=2800)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.267)

- **PATRÓN** `ibs_20min` < `0.545` → IC=+0.285 (n=3097)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.545 (IC base=+0.267)

- **PATRÓN** `volumen_pendiente_norm` < `0.0975` → IC=+0.271 (n=2819)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0975 (IC base=+0.267)

- **PATRÓN** `volumen_pendiente_norm` > `0.2905` → IC=+0.282 (n=433)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2905 (IC base=+0.267)

- **PATRÓN** `volumen_spike_ratio` < `1.5594` → IC=+0.269 (n=1306)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5594 (IC base=+0.267)

- **PATRÓN** `volumen_spike_ratio` > `2.6495` → IC=+0.276 (n=990)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6495 (IC base=+0.267)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.269 (n=3566)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.267)

- **PATRÓN** `libro_liquidez` > `1779.0666` → IC=+0.275 (n=2065)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1779.0666 (IC base=+0.267)

- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.278 (n=1070)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 8.0 (IC base=+0.267)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.179 (n=1188)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0031 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.0783` → IC=+0.151 (n=1188)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.0783 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.147 (n=3710)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 5.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` > `0.1988` → IC=+0.189 (n=3564)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.1988 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.3177` → IC=+0.200 (n=1178)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3177 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.316` → IC=+0.162 (n=747)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 9.316 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `0.6348` → IC=+0.155 (n=1188)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.6348 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` > `1.0679` → IC=+0.141 (n=1616)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` > 1.0679 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.2717` → IC=+0.177 (n=506)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.2717 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `2.166` → IC=+0.141 (n=3078)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 2.166 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `1.5203` → IC=+0.141 (n=3125)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.5203 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `221.0` → IC=+0.159 (n=1147)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 221.0 (IC base=+0.136)

- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.163 (n=3059)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0064 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.078` → IC=+0.165 (n=1020)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.078 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.168 (n=1129)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 17.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` < `0.6801` → IC=+0.186 (n=3059)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.6801 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.981` → IC=+0.139 (n=2765)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 3.981 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `1.0483` → IC=+0.149 (n=2691)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 1.0483 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.2196` → IC=+0.196 (n=567)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2196 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `2.4295` → IC=+0.142 (n=2948)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.4295 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `1.7707` → IC=+0.142 (n=1965)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.7707 (IC base=+0.137)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.138 (n=3972)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `226.0` → IC=+0.154 (n=964)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 226.0 (IC base=+0.137)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.243 (n=2424)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0099 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.236 (n=3802)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.227)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.229 (n=3252)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.227)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.302 (n=1365)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.001` → IC=+0.323 (n=807)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.001 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` < `0.1319` → IC=+0.229 (n=3440)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1319 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` > `0.3501` → IC=+0.227 (n=478)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3501 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` > `2.7369` → IC=+0.241 (n=1611)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7369 (IC base=+0.227)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.234 (n=4388)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.227)

- **PATRÓN** `libro_liquidez` > `1917.1432` → IC=+0.240 (n=1648)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1917.1432 (IC base=+0.227)

- **PATRÓN** `sigma_h` < `0.0109` → IC=+0.250 (n=3048)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0109 (IC base=+0.243)

- **PATRÓN** `drift_60min` |x|≤ `0.1777` → IC=+0.264 (n=1524)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1777 (IC base=+0.243)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.264 (n=1323)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.243)

- **PATRÓN** `ibs_20min` < `0.0588` → IC=+0.302 (n=1158)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0588 (IC base=+0.243)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.104` → IC=+0.302 (n=371)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.104 (IC base=+0.243)

- **PATRÓN** `volumen_pendiente_norm` > `0.3492` → IC=+0.303 (n=521)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3492 (IC base=+0.243)

- **PATRÓN** `volumen_spike_ratio` > `2.1786` → IC=+0.254 (n=2223)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1786 (IC base=+0.243)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.250 (n=1769)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.243)

- **PATRÓN** `libro_liquidez` > `2004.3184` → IC=+0.254 (n=1155)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2004.3184 (IC base=+0.243)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.251 (n=2173)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.243)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.194 (n=1264)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0037 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.4293` → IC=+0.144 (n=3769)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.4293 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.148 (n=3905)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 5.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` > `0.8897` → IC=+0.271 (n=1257)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8897 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.1935` → IC=+0.166 (n=1721)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1935 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.948` → IC=+0.155 (n=1672)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 2.948 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `0.8593` → IC=+0.151 (n=2514)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.8593 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.2332` → IC=+0.186 (n=670)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.2332 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `1.5199` → IC=+0.150 (n=1624)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.5199 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `2.1788` → IC=+0.143 (n=1671)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 2.1788 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `5516.8147` → IC=+0.226 (n=1709)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5516.8147 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `88.0` → IC=+0.142 (n=2436)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 88.0 (IC base=+0.136)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.169 (n=2774)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0067 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.4355` → IC=+0.154 (n=3151)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.4355 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.174 (n=1166)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 17.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` < `0.5762` → IC=+0.210 (n=2773)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5762 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` < `0.1518` → IC=+0.158 (n=2945)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.1518 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.857` → IC=+0.154 (n=464)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 10.857 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.044` → IC=+0.148 (n=2750)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 3.044 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `0.6886` → IC=+0.161 (n=1387)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.6886 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` > `0.2939` → IC=+0.212 (n=401)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2939 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `1.5337` → IC=+0.153 (n=2717)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.5337 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `6325.8714` → IC=+0.218 (n=1051)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6325.8714 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `91.0` → IC=+0.157 (n=2049)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 91.0 (IC base=+0.144)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.149 (n=1735)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` > 0.0112 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.147 (n=2701)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 11.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` > `0.4286` → IC=+0.189 (n=3840)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.4286 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` > `1.0026` → IC=+0.202 (n=628)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0026 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.242` → IC=+0.269 (n=972)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.242 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` < `0.8767` → IC=+0.131 (n=2549)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 0.8767 (IC base=+0.117)

- **PATRÓN** `volumen_pendiente_norm` < `0.1017` → IC=+0.121 (n=3624)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_pendiente_norm` < 0.1017 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` < `2.489` → IC=+0.121 (n=3734)

  - _Acción_: Kelly boost +0.60€ cuando `volumen_spike_ratio` < 2.489 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `2710.4123` → IC=+0.240 (n=1274)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2710.4123 (IC base=+0.117)

- **PATRÓN** `sigma_h` < `0.0108` → IC=+0.152 (n=3168)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0108 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.1366` → IC=+0.153 (n=1200)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.1366 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.163 (n=1697)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 15.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` < `0.6667` → IC=+0.215 (n=3610)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6667 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` < `0.2159` → IC=+0.141 (n=3252)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.2159 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.039` → IC=+0.147 (n=3479)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 3.039 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `1.1918` → IC=+0.134 (n=3597)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 1.1918 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` > `0.2277` → IC=+0.179 (n=627)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.2277 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `1.4363` → IC=+0.157 (n=1138)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.4363 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `2605.7243` → IC=+0.208 (n=1199)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2605.7243 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.138 (n=3073)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 43.0 (IC base=+0.126)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0139` → IC=+0.259 (n=3140)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0139 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.243 (n=3669)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.237)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.243 (n=2345)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` > `0.615` → IC=+0.271 (n=3139)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.615 (IC base=+0.237)

- **PATRÓN** `dist_vwap_pct` > `0.1935` → IC=+0.251 (n=1828)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1935 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.219` → IC=+0.286 (n=605)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.219 (IC base=+0.237)

- **PATRÓN** `volumen_regimen` < `1.2201` → IC=+0.239 (n=3513)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2201 (IC base=+0.237)

- **PATRÓN** `volumen_regimen` > `0.6419` → IC=+0.242 (n=3513)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6419 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.2391` → IC=+0.255 (n=606)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2391 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `2.5042` → IC=+0.259 (n=1145)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5042 (IC base=+0.237)

- **PATRÓN** `libro_liquidez` > `2969.1926` → IC=+0.242 (n=1171)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2969.1926 (IC base=+0.237)

- **PATRÓN** `sigma_h` > `0.026` → IC=+0.268 (n=1208)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.026 (IC base=+0.242)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.248 (n=3413)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.242)

- **PATRÓN** `ibs_20min` < `0.5206` → IC=+0.272 (n=3620)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5206 (IC base=+0.242)

- **PATRÓN** `dist_vwap_pct` < `0.2982` → IC=+0.248 (n=3574)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2982 (IC base=+0.242)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.148` → IC=+0.279 (n=705)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.148 (IC base=+0.242)

- **PATRÓN** `volumen_regimen` > `1.2193` → IC=+0.263 (n=1207)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2193 (IC base=+0.242)

- **PATRÓN** `volumen_pendiente_norm` > `0.2863` → IC=+0.304 (n=499)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2863 (IC base=+0.242)

- **PATRÓN** `volumen_spike_ratio` > `1.4355` → IC=+0.246 (n=3410)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4355 (IC base=+0.242)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.200 (n=5804)

- **PATRÓN** `sigma_h` < `0.005` → IC=+0.246 (n=2017)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.218)

- **PATRÓN** `drift_60min` |x|≤ `0.5055` → IC=+0.227 (n=6020)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5055 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.232 (n=2176)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.218)

- **PATRÓN** `ibs_20min` > `0.9346` → IC=+0.256 (n=2008)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9346 (IC base=+0.218)

- **PATRÓN** `dist_vwap_pct` < `0.4266` → IC=+0.221 (n=4385)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4266 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.549` → IC=+0.227 (n=1976)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.549 (IC base=+0.218)

- **PATRÓN** `volumen_regimen` < `0.7081` → IC=+0.230 (n=1953)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7081 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` < `0.105` → IC=+0.219 (n=5619)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.105 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` > `0.1652` → IC=+0.225 (n=1691)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1652 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` < `2.2557` → IC=+0.223 (n=5215)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.2557 (IC base=+0.218)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.224 (n=4666)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.218)

- **PATRÓN** `libro_liquidez` > `2884.9951` → IC=+0.224 (n=5377)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2884.9951 (IC base=+0.218)

- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.237 (n=1460)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.199)

- **PATRÓN** `drift_60min` |x|≤ `0.4924` → IC=+0.211 (n=4365)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4924 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.212 (n=1473)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.213 (n=1931)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.199)

- **PATRÓN** `ibs_20min` < `0.0878` → IC=+0.212 (n=1455)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0878 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` > `0.6576` → IC=+0.209 (n=747)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6576 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.778` → IC=+0.210 (n=3918)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.778 (IC base=+0.199)

- **PATRÓN** `volumen_regimen` < `1.0945` → IC=+0.205 (n=3663)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0945 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` < `0.0978` → IC=+0.200 (n=4022)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0978 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` > `0.0735` → IC=+0.201 (n=1945)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0735 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` < `1.5315` → IC=+0.203 (n=1893)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5315 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` > `2.1849` → IC=+0.206 (n=1951)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1849 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.200 (n=5804)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

- **PATRÓN** `ballena_activa_n` < `65.0` → IC=+0.214 (n=2870)

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

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.185 (n=566)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 5.0 (IC base=+0.176)

- **PATRÓN** `ibs_20min` < `0.1382` → IC=+0.198 (n=670)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.1382 (IC base=+0.176)

- **PATRÓN** `dist_vwap_pct` > `0.6926` → IC=+0.199 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6926 (IC base=+0.176)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.86` → IC=+0.188 (n=1755)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` < 10.86 (IC base=+0.176)

- **PATRÓN** `volumen_regimen` < `1.0915` → IC=+0.189 (n=1337)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 1.0915 (IC base=+0.176)

- **PATRÓN** `volumen_pendiente_norm` > `0.1521` → IC=+0.195 (n=463)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.1521 (IC base=+0.176)

- **PATRÓN** `volumen_spike_ratio` < `1.4126` → IC=+0.194 (n=504)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 1.4126 (IC base=+0.176)

- **PATRÓN** `volumen_spike_ratio` > `2.1703` → IC=+0.180 (n=685)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 2.1703 (IC base=+0.176)

- **PATRÓN** `libro_liquidez` > `14605.0565` → IC=+0.179 (n=689)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 14605.0565 (IC base=+0.176)

- **PATRÓN** `ballena_activa_n` < `687.0` → IC=+0.187 (n=1474)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 687.0 (IC base=+0.176)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` > `0.009` → IC=+0.225 (n=623)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.009 (IC base=+0.202)

- **PATRÓN** `drift_60min` |x|≤ `0.5907` → IC=+0.210 (n=933)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5907 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.222 (n=846)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.202)

- **PATRÓN** `ibs_20min` < `0.3929` → IC=+0.203 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3929 (IC base=+0.202)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.249 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.202)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.412` → IC=+0.248 (n=340)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.412 (IC base=+0.202)

- **PATRÓN** `volumen_pendiente_norm` > `0.2054` → IC=+0.236 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2054 (IC base=+0.202)

- **PATRÓN** `volumen_spike_ratio` < `3.3613` → IC=+0.202 (n=931)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 3.3613 (IC base=+0.202)

- **PATRÓN** `volumen_spike_ratio` > `1.7981` → IC=+0.209 (n=831)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7981 (IC base=+0.202)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.203 (n=1224)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `2775.94` → IC=+0.239 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2775.94 (IC base=+0.202)

- **PATRÓN** `ballena_activa_n` < `9.0` → IC=+0.209 (n=662)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 9.0 (IC base=+0.202)

- **PATRÓN** `sigma_h` < `0.0116` → IC=+0.242 (n=60)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0116 (IC base=+0.228)

- **PATRÓN** `sigma_h` > `0.009` → IC=+0.286 (n=40)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.009 (IC base=+0.228)

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

- **PATRÓN** `libro_liquidez` > `2388.306` → IC=+0.259 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2388.306 (IC base=+0.228)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.0081` → IC=+0.219 (n=1673)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0081 (IC base=+0.205)

- **PATRÓN** `drift_60min` |x|≤ `0.1456` → IC=+0.217 (n=736)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1456 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.224 (n=588)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.205)

- **PATRÓN** `ibs_20min` < `0.4957` → IC=+0.219 (n=1114)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4957 (IC base=+0.205)

- **PATRÓN** `ibs_20min` > `0.8536` → IC=+0.208 (n=557)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8536 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` < `0.2061` → IC=+0.216 (n=1485)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2061 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.45` → IC=+0.210 (n=1695)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 6.45 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` < `0.8733` → IC=+0.211 (n=1114)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8733 (IC base=+0.205)

- **PATRÓN** `volumen_pendiente_norm` < `0.1023` → IC=+0.210 (n=1539)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1023 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` < `2.4495` → IC=+0.213 (n=1634)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4495 (IC base=+0.205)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.241 (n=458)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.200)

- **PATRÓN** `drift_60min` |x|≤ `0.4873` → IC=+0.220 (n=1367)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4873 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.207 (n=521)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.200)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.217 (n=922)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.200)

- **PATRÓN** `ibs_20min` < `0.3991` → IC=+0.201 (n=912)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3991 (IC base=+0.200)

- **PATRÓN** `ibs_20min` > `0.6178` → IC=+0.207 (n=620)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6178 (IC base=+0.200)

- **PATRÓN** `dist_vwap_pct` > `0.6243` → IC=+0.218 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6243 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.834` → IC=+0.202 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.834 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.351` → IC=+0.204 (n=1245)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.351 (IC base=+0.200)

- **PATRÓN** `volumen_regimen` < `0.6378` → IC=+0.227 (n=456)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6378 (IC base=+0.200)

- **PATRÓN** `volumen_regimen` > `0.7208` → IC=+0.200 (n=1221)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7208 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` > `0.0735` → IC=+0.228 (n=557)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0735 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` < `2.1843` → IC=+0.206 (n=1179)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1843 (IC base=+0.200)

- **PATRÓN** `libro_liquidez` > `6428.6136` → IC=+0.207 (n=1221)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6428.6136 (IC base=+0.200)

- **PATRÓN** `ballena_activa_n` < `98.0` → IC=+0.201 (n=1356)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 98.0 (IC base=+0.200)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0098` → IC=+0.223 (n=638)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0098 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `9.0` → IC=+0.235 (n=671)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 9.0 (IC base=+0.199)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.273 (n=332)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` > `0.7677` → IC=+0.240 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7677 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.202` → IC=+0.225 (n=526)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.202 (IC base=+0.199)

- **PATRÓN** `volumen_regimen` < `0.6408` → IC=+0.248 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6408 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` < `0.1056` → IC=+0.208 (n=862)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1056 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` > `0.0795` → IC=+0.206 (n=423)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0795 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` < `2.1486` → IC=+0.206 (n=818)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1486 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` > `1.4745` → IC=+0.205 (n=930)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4745 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.209 (n=1127)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `4320.729` → IC=+0.244 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4320.729 (IC base=+0.199)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.205 (n=830)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 40.0 (IC base=+0.199)

- **PATRÓN** `sigma_h` < `0.013` → IC=+0.220 (n=697)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.013 (IC base=+0.220)

- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.232 (n=465)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0099 (IC base=+0.220)

- **PATRÓN** `drift_60min` |x|≤ `0.5947` → IC=+0.237 (n=697)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5947 (IC base=+0.220)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.248 (n=483)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.220)

- **PATRÓN** `ibs_20min` < `0.6522` → IC=+0.250 (n=615)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6522 (IC base=+0.220)

- **PATRÓN** `dist_vwap_pct` > `0.5279` → IC=+0.219 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5279 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.776` → IC=+0.234 (n=644)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.776 (IC base=+0.220)

- **PATRÓN** `volumen_regimen` < `0.7541` → IC=+0.225 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7541 (IC base=+0.220)

- **PATRÓN** `volumen_regimen` > `1.2681` → IC=+0.228 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2681 (IC base=+0.220)

- **PATRÓN** `volumen_pendiente_norm` < `0.0838` → IC=+0.235 (n=587)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0838 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` > `2.593` → IC=+0.260 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.593 (IC base=+0.220)

- **PATRÓN** `libro_liquidez` > `3779.7004` → IC=+0.234 (n=465)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3779.7004 (IC base=+0.220)

- **PATRÓN** `ballena_activa_n` < `36.0` → IC=+0.256 (n=605)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 36.0 (IC base=+0.220)

### GBM_LATE_60M
- **FILTRO** `ibs_20min` > `0.5` → IC=-0.121 (n=648)

  - _Acción_: SKIP cuando `ibs_20min` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.154 (n=1263)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.149 (n=725)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0038 (IC base=+0.052)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.184 (n=1398)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.75 (IC base=+0.052)

- **PATRÓN** `dist_vwap_pct` > `0.1432` → IC=+0.140 (n=1038)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` > 0.1432 (IC base=+0.052)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.44` → IC=+0.147 (n=463)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 10.44 (IC base=+0.052)

- **PATRÓN** `ibs_20min` < `0.0617` → IC=+0.268 (n=631)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0617 (IC base=+0.045)

- **PATRÓN** `volumen_pendiente_norm` > `0.147` → IC=+0.139 (n=394)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_pendiente_norm` > 0.147 (IC base=+0.045)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `ibs_20min` < `0.5385` → IC=-0.125 (n=289)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5385
  - _Potencial_: sin este filtro IC_bueno=+0.164 (n=588)

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.125 (n=606)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0052 (IC base=+0.069)

- **PATRÓN** `ibs_20min` > `0.5385` → IC=+0.164 (n=588)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` > 0.5385 (IC base=+0.069)

- **PATRÓN** `dist_vwap_pct` > `0.119` → IC=+0.168 (n=317)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.119 (IC base=+0.069)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.129 (n=262)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.64€ cuando `sigma_h` < 0.0034 (IC base=+0.045)

- **PATRÓN** `ibs_20min` < `0.0742` → IC=+0.272 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0742 (IC base=+0.045)

- **PATRÓN** `volumen_pendiente_norm` > `0.2172` → IC=+0.161 (n=113)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.2172 (IC base=+0.045)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` > `0.6807` → IC=-0.171 (n=153)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6807
  - _Potencial_: sin este filtro IC_bueno=+0.110 (n=462)

- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.126 (n=469)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.63€ cuando `sigma_h` < 0.0051 (IC base=+0.070)

- **PATRÓN** `ibs_20min` > `0.7783` → IC=+0.218 (n=448)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7783 (IC base=+0.070)

- **PATRÓN** `dist_vwap_pct` > `0.1265` → IC=+0.173 (n=328)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.1265 (IC base=+0.070)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.65` → IC=+0.197 (n=150)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 11.65 (IC base=+0.070)

- **PATRÓN** `ibs_20min` < `0.0289` → IC=+0.276 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0289 (IC base=+0.023)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.592` → IC=+0.200 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.592 (IC base=+0.023)

### GBM_LATE_60M#SOL#60min
- **PATRÓN** `ibs_20min` > `0.7222` → IC=+0.136 (n=500)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` > 0.7222 (IC base=+0.021)

- **PATRÓN** `dist_vwap_pct` > `0.4645` → IC=+0.124 (n=251)

  - _Acción_: Kelly boost +0.62€ cuando `dist_vwap_pct` > 0.4645 (IC base=+0.021)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.667` → IC=+0.139 (n=164)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 8.667 (IC base=+0.021)

- **PATRÓN** `sigma_h` < `0.0112` → IC=+0.147 (n=381)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0112 (IC base=+0.071)

- **PATRÓN** `ibs_20min` < `0.3415` → IC=+0.199 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3415 (IC base=+0.071)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.838` → IC=+0.283 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.838 (IC base=+0.071)

- **PATRÓN** `volumen_regimen` > `1.0818` → IC=+0.162 (n=134)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 1.0818 (IC base=+0.071)

- **PATRÓN** `volumen_pendiente_norm` > `0.1557` → IC=+0.170 (n=113)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.1557 (IC base=+0.071)

- **PATRÓN** `volumen_spike_ratio` > `2.5569` → IC=+0.153 (n=125)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 2.5569 (IC base=+0.071)

### GBM_LATE_60M_FADE
- **FILTRO** `sigma_h` < `0.0058` → IC=-0.241 (n=187)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0058
  - _Potencial_: sin este filtro IC_bueno=-0.193 (n=187)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.300 (n=93)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.189 (n=281)

- **FILTRO** `dist_vwap_pct` > `0.2351` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2351
  - _Potencial_: sin este filtro IC_bueno=-0.211 (n=358)

- **FILTRO** `hora_utc` > `11.0` → IC=-0.309 (n=150)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.258 (n=176)

- **FILTRO** `dist_vwap_pct` > `0.4614` → IC=-0.405 (n=19)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4614
  - _Potencial_: sin este filtro IC_bueno=-0.274 (n=307)

- **FILTRO** `sigma_ewma_delta_pct` > `9.697` → IC=-0.328 (n=27)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 9.697
  - _Potencial_: sin este filtro IC_bueno=-0.277 (n=299)

- **FILTRO** `volumen_pendiente_norm` > `0.0448` → IC=-0.379 (n=31)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0448
  - _Potencial_: sin este filtro IC_bueno=-0.269 (n=206)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.280 (n=48)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.198 (n=61)

- **FILTRO** `sigma_ewma_delta_pct` > `9.679` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 9.679
  - _Potencial_: sin este filtro IC_bueno=-0.234 (n=92)

- **FILTRO** `volumen_regimen` < `0.89` → IC=-0.328 (n=27)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.89
  - _Potencial_: sin este filtro IC_bueno=-0.202 (n=82)

- **FILTRO** `drift_60min` |x|> `0.0922` → IC=-0.308 (n=71)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.0922
  - _Potencial_: sin este filtro IC_bueno=-0.193 (n=73)

- **FILTRO** `ibs_20min` > `0.7502` → IC=-0.265 (n=49)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7502
  - _Potencial_: sin este filtro IC_bueno=-0.247 (n=97)

- **FILTRO** `volumen_regimen` > `0.805` → IC=-0.316 (n=36)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.232 (n=110)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `sigma_h` < `0.0034` → IC=-0.233 (n=43)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.144 (n=88)

- **FILTRO** `hora_utc` < `2.0` → IC=-0.179 (n=26)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 2.0
  - _Potencial_: sin este filtro IC_bueno=-0.173 (n=105)

- **FILTRO** `ibs_20min` < `0.5857` → IC=-0.471 (n=32)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5857
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=99)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.368 (n=36)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.274 (n=91)

- **FILTRO** `ibs_20min` > `0.681` → IC=-0.389 (n=43)

  - _Acción_: SKIP cuando `ibs_20min` > 0.681
  - _Potencial_: sin este filtro IC_bueno=-0.256 (n=84)

- **FILTRO** `volumen_spike_ratio` < `1.4324` → IC=-0.380 (n=23)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.4324
  - _Potencial_: sin este filtro IC_bueno=-0.289 (n=69)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.298 (n=112)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `hora_utc` > `5.0` → IC=-0.344 (n=43)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=91)

- **FILTRO** `volumen_spike_ratio` > `2.3401` → IC=-0.269 (n=37)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.3401
  - _Potencial_: sin este filtro IC_bueno=-0.216 (n=72)

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
- **PATRÓN** `sigma_h` > `0.0084` → IC=+0.243 (n=235)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0084 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.188 (n=363)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 15.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` > `0.6774` → IC=+0.179 (n=700)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.6774 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` > `0.7991` → IC=+0.283 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7991 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.614` → IC=+0.153 (n=384)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 3.614 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` < `8.528` → IC=+0.142 (n=715)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 8.528 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` < `0.6243` → IC=+0.182 (n=234)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 0.6243 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` < `0.0701` → IC=+0.175 (n=518)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` < 0.0701 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` < `1.3944` → IC=+0.190 (n=198)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` < 1.3944 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.53` → IC=+0.158 (n=191)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 10.53 (IC base=+0.032)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.7831` → IC=-0.130 (n=90)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7831
  - _Potencial_: sin este filtro IC_bueno=+0.116 (n=183)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.126 (n=105)

  - _Acción_: Kelly boost +0.63€ cuando `ibs_20min` > 1.0 (IC base=+0.035)

- **PATRÓN** `dist_vwap_pct` > `0.5957` → IC=+0.214 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5957 (IC base=+0.035)

- **PATRÓN** `ibs_20min` < `0.215` → IC=+0.147 (n=383)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.215 (IC base=+0.088)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.339` → IC=+0.133 (n=88)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` > 11.339 (IC base=+0.088)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `volumen_pendiente_norm` > `0.1814` → IC=-0.167 (n=25)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1814
  - _Potencial_: sin este filtro IC_bueno=+0.142 (n=252)

- **FILTRO** `ibs_20min` > `0.2338` → IC=-0.141 (n=101)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2338
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=306)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.124 (n=208)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0057 (IC base=+0.115)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.151 (n=84)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 18.0 (IC base=+0.115)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.129 (n=114)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 8.0 (IC base=+0.115)

- **PATRÓN** `ibs_20min` > `0.8879` → IC=+0.175 (n=158)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` > 0.8879 (IC base=+0.115)

- **PATRÓN** `dist_vwap_pct` < `0.0967` → IC=+0.141 (n=196)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.0967 (IC base=+0.115)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.217` → IC=+0.141 (n=246)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 9.217 (IC base=+0.115)

- **PATRÓN** `volumen_regimen` < `0.6242` → IC=+0.167 (n=79)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.6242 (IC base=+0.115)

- **PATRÓN** `volumen_pendiente_norm` < `0.1814` → IC=+0.142 (n=252)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` < 0.1814 (IC base=+0.115)

- **PATRÓN** `volumen_spike_ratio` < `1.7318` → IC=+0.174 (n=139)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 1.7318 (IC base=+0.115)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.126 (n=204)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.01 (IC base=+0.115)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.584` → IC=+0.214 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.584 (IC base=+0.011)

- **PATRÓN** `volumen_pendiente_norm` > `0.2863` → IC=+0.130 (n=44)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` > 0.2863 (IC base=+0.011)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.2` → IC=-0.233 (n=58)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=128)

- **PATRÓN** `sigma_h` > `0.0109` → IC=+0.286 (n=87)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0109 (IC base=+0.246)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.295 (n=183)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.246)

- **PATRÓN** `ibs_20min` > `0.6` → IC=+0.282 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6 (IC base=+0.246)

- **PATRÓN** `dist_vwap_pct` > `0.6947` → IC=+0.391 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6947 (IC base=+0.246)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.832` → IC=+0.357 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.832 (IC base=+0.246)

- **PATRÓN** `volumen_regimen` < `0.5849` → IC=+0.298 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.5849 (IC base=+0.246)

- **PATRÓN** `volumen_pendiente_norm` > `0.0966` → IC=+0.312 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0966 (IC base=+0.246)

- **PATRÓN** `volumen_spike_ratio` < `1.48` → IC=+0.337 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.48 (IC base=+0.246)

- **PATRÓN** `volumen_spike_ratio` > `2.309` → IC=+0.300 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.309 (IC base=+0.246)

### LATE_WINDOW_5MIN
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.318 (n=108)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3975` → IC=+0.342 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3975 (IC base=+0.329)

- **PATRÓN** `elapsed_s` > `207.7` → IC=+0.395 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 207.7 (IC base=+0.329)

- **PATRÓN** `drift_15min` |x|≤ `1.0295` → IC=+0.433 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0295 (IC base=+0.329)

- **PATRÓN** `drift_60min` |x|≤ `0.969` → IC=+0.369 (n=82)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.969 (IC base=+0.329)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.403 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.329)

- **PATRÓN** `ballena_activa_n` < `1071.0` → IC=+0.367 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1071.0 (IC base=+0.329)

- **PATRÓN** `drift_ventana_pct` |x|> `0.4356` → IC=+0.294 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.4356 (IC base=+0.256)

- **PATRÓN** `elapsed_s` > `229.9` → IC=+0.324 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 229.9 (IC base=+0.256)

- **PATRÓN** `elapsed_s` < `203.6` → IC=+0.254 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 203.6 (IC base=+0.256)

- **PATRÓN** `drift_15min` |x|≤ `2.2537` → IC=+0.300 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.2537 (IC base=+0.256)

- **PATRÓN** `drift_60min` |x|≤ `0.6365` → IC=+0.300 (n=63)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6365 (IC base=+0.256)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.318 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.256)

- **PATRÓN** `ballena_activa_n` < `1330.0` → IC=+0.346 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1330.0 (IC base=+0.256)

### LATE_WINDOW_5MIN#BTC#5min
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.318 (n=108)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3975` → IC=+0.342 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3975 (IC base=+0.329)

- **PATRÓN** `elapsed_s` > `207.7` → IC=+0.395 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 207.7 (IC base=+0.329)

- **PATRÓN** `drift_15min` |x|≤ `1.0295` → IC=+0.433 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0295 (IC base=+0.329)

- **PATRÓN** `drift_60min` |x|≤ `0.969` → IC=+0.369 (n=82)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.969 (IC base=+0.329)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.403 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.329)

- **PATRÓN** `ballena_activa_n` < `1071.0` → IC=+0.367 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1071.0 (IC base=+0.329)

- **PATRÓN** `drift_ventana_pct` |x|> `0.4356` → IC=+0.294 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.4356 (IC base=+0.256)

- **PATRÓN** `elapsed_s` > `229.9` → IC=+0.324 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 229.9 (IC base=+0.256)

- **PATRÓN** `elapsed_s` < `203.6` → IC=+0.254 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 203.6 (IC base=+0.256)

- **PATRÓN** `drift_15min` |x|≤ `2.2537` → IC=+0.300 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.2537 (IC base=+0.256)

- **PATRÓN** `drift_60min` |x|≤ `0.6365` → IC=+0.300 (n=63)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6365 (IC base=+0.256)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.318 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.256)

- **PATRÓN** `ballena_activa_n` < `1330.0` → IC=+0.346 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1330.0 (IC base=+0.256)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.121 (n=1438)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` > 0.5 (IC base=+0.098)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.121 (n=1438)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` > 0.5 (IC base=+0.098)

### LIQUIDACIONES_15M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=244)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=244)

- **FILTRO** `libro_liquidez` < `6904.0159` → IC=-0.151 (n=130)

  - _Acción_: SKIP cuando `libro_liquidez` < 6904.0159
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=130)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=745)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `libro_liquidez` < `12112.4745` → IC=-0.159 (n=42)

  - _Acción_: SKIP cuando `libro_liquidez` < 12112.4745
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=88)

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
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=3913)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=141)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=98)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.278 (n=34)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=128)

- **FILTRO** `ballena_activa_n` > `33.0` → IC=-0.178 (n=85)

  - _Acción_: SKIP cuando `ballena_activa_n` > 33.0
  - _Potencial_: sin este filtro IC_bueno=+0.211 (n=43)

- **PATRÓN** `ballena_activa_n` < `33.0` → IC=+0.211 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 33.0 (IC base=-0.085)

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

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.122 (n=273)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` < 0.495 (IC base=+0.023)

### LIQUIDACIONES_5M#DOGE#5min
- **PATRÓN** `liq_usd_total` > `4933.63` → IC=+0.324 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `liq_usd_total` > 4933.63 (IC base=+0.233)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.333 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.233)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.505 (IC base=+0.233)

- **PATRÓN** `libro_liquidez` > `2699.3605` → IC=+0.265 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2699.3605 (IC base=+0.233)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=1596)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=1550)

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
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=443)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=424)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.142 (n=188)

  - _Acción_: Kelly boost +0.71€ cuando `py_entrada` < 0.495 (IC base=+0.021)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=986)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=986)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=1215)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=1215)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=276)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=276)

- **FILTRO** `hora_utc` > `12.0` → IC=-0.139 (n=81)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=210)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.146 (n=63)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=338)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=386)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=298)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=397)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=397)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.120 (n=185)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=242)

- **FILTRO** `libro_liquidez` < `659.869` → IC=-0.134 (n=140)

  - _Acción_: SKIP cuando `libro_liquidez` < 659.869
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=287)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=348)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.188 (n=78)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=95)

- **FILTRO** `hora_utc` > `14.0` → IC=-0.159 (n=80)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=93)

- **FILTRO** `hora_utc` < `17.0` → IC=-0.125 (n=62)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=23)

### LIQUIDACIONES_DEPTH_FASE0#BTC#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.131 (n=269)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=692)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **FILTRO** `py_entrada` > `0.57` → IC=-0.120 (n=414)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.081 (n=487)

- **PATRÓN** `py_entrada` < `0.51` → IC=+0.131 (n=318)

  - _Acción_: Kelly boost +0.66€ cuando `py_entrada` < 0.51 (IC base=-0.012)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **FILTRO** `py_entrada` < `0.41` → IC=-0.148 (n=160)

  - _Acción_: SKIP cuando `py_entrada` < 0.41
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=340)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` > `0.57` → IC=-0.122 (n=342)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.067 (n=354)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` > `0.58` → IC=-0.122 (n=334)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=392)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.162 (n=149)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=650)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.122 (n=538)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=284)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.141 (n=115)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=354)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.41` → IC=-0.162 (n=303)

  - _Acción_: SKIP cuando `py_entrada` < 0.41
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=653)

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
- **FILTRO** `py_entrada` < `0.46` → IC=-0.172 (n=7710)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=24702)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.175 (n=8222)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=25199)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.182 (n=1485)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.116 (n=4510)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.149 (n=1994)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.094 (n=3930)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.133 (n=1549)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` > 1.0 (IC base=+0.042)

- **PATRÓN** `py_entrada` < `0.505` → IC=+0.125 (n=3014)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` < 0.505 (IC base=+0.012)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` < `0.44` → IC=-0.170 (n=1065)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=3454)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.183 (n=1151)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=3561)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` > `0.62` → IC=-0.202 (n=1474)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.085 (n=4589)

- **PATRÓN** `ibs_20min` > `0.963` → IC=+0.133 (n=2037)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` > 0.963 (IC base=+0.035)

- **PATRÓN** `libro_liquidez` > `1745.7954` → IC=+0.122 (n=2038)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 1745.7954 (IC base=+0.035)

### MOMENTUM_IBS_15M_BALLENA#ETH#15min
- **FILTRO** `py_entrada` > `0.58` → IC=-0.181 (n=1113)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=3657)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.485` → IC=-0.159 (n=1492)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=4536)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=2432)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.162 (n=772)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=2356)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.180 (n=973)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=3030)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=3982)

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
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=1067)

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
  - _Potencial_: sin este filtro IC_bueno=-0.099 (n=360)

- **FILTRO** `ballena_activa_n` > `84.0` → IC=-0.179 (n=157)

  - _Acción_: SKIP cuando `ballena_activa_n` > 84.0
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=308)

- **FILTRO** `libro_liquidez` < `3222.056` → IC=-0.183 (n=156)

  - _Acción_: SKIP cuando `libro_liquidez` < 3222.056
  - _Potencial_: sin este filtro IC_bueno=-0.096 (n=317)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=968)

- **FILTRO** `ballena_activa_n` > `23.0` → IC=-0.191 (n=390)

  - _Acción_: SKIP cuando `ballena_activa_n` > 23.0
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=783)

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
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=91)

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

### MOMENTUM_IBS_5M#SOL#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=631)

### MOMENTUM_IBS_5M_BALLENA
- **FILTRO** `hora_utc` < `8.0` → IC=-0.133 (n=22069)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.089 (n=49674)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.297 (n=17149)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=54594)

- **FILTRO** `ibs_7min` < `0.2187` → IC=-0.232 (n=17932)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2187
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=53811)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.152 (n=23495)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=48248)

- **FILTRO** `py_entrada` > `0.68` → IC=-0.251 (n=20979)

  - _Acción_: SKIP cuando `py_entrada` > 0.68
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=68795)

- **FILTRO** `ibs_7min` > `0.283` → IC=-0.184 (n=22428)

  - _Acción_: SKIP cuando `ibs_7min` > 0.283
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=67346)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.155 (n=3098)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=9668)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.318 (n=3144)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=9622)

- **FILTRO** `ibs_7min` < `0.7113` → IC=-0.250 (n=4212)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7113
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=8554)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.152 (n=2768)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=9998)

- **FILTRO** `py_entrada` > `0.72` → IC=-0.276 (n=3780)

  - _Acción_: SKIP cuando `py_entrada` > 0.72
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=11726)

- **FILTRO** `ibs_7min` > `0.7768` → IC=-0.211 (n=3876)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7768
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=11630)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.262 (n=2877)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=9068)

- **FILTRO** `ibs_7min` < `0.7149` → IC=-0.207 (n=2986)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7149
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=8959)

- **FILTRO** `ballena_activa_n` > `155.0` → IC=-0.199 (n=2971)

  - _Acción_: SKIP cuando `ballena_activa_n` > 155.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=8974)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.269 (n=2805)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9408)

- **FILTRO** `ibs_7min` > `0.2665` → IC=-0.195 (n=3051)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2665
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=9162)

- **FILTRO** `ballena_activa_n` > `153.0` → IC=-0.182 (n=3047)

  - _Acción_: SKIP cuando `ballena_activa_n` > 153.0
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=9166)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.164 (n=2955)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=9252)

- **FILTRO** `py_entrada` < `0.3` → IC=-0.324 (n=2896)

  - _Acción_: SKIP cuando `py_entrada` < 0.3
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=9311)

- **FILTRO** `ibs_7min` < `0.2886` → IC=-0.249 (n=4028)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2886
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=8179)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.200 (n=2469)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=9738)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.258 (n=3975)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=12450)

- **FILTRO** `ibs_7min` > `0.7321` → IC=-0.183 (n=4106)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7321
  - _Potencial_: sin este filtro IC_bueno=-0.000 (n=12319)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.261 (n=2866)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=8742)

- **FILTRO** `ibs_7min` < `0.7159` → IC=-0.196 (n=2900)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7159
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=8708)

- **FILTRO** `ballena_activa_n` > `25.0` → IC=-0.189 (n=2831)

  - _Acción_: SKIP cuando `ballena_activa_n` > 25.0
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=8777)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.259 (n=2793)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=9298)

- **FILTRO** `ibs_7min` > `0.2743` → IC=-0.178 (n=3022)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2743
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=9069)

- **FILTRO** `ballena_activa_n` > `24.0` → IC=-0.170 (n=2951)

  - _Acción_: SKIP cuando `ballena_activa_n` > 24.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=9140)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.32` → IC=-0.297 (n=2708)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=8806)

- **FILTRO** `ibs_7min` < `0.7027` → IC=-0.230 (n=3796)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7027
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=7718)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.216 (n=2847)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=8667)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.198 (n=4209)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=13161)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.130 (n=3764)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.106 (n=7939)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.307 (n=2780)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=8923)

- **FILTRO** `ibs_7min` < `0.1626` → IC=-0.229 (n=2925)

  - _Acción_: SKIP cuando `ibs_7min` < 0.1626
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=8778)

- **FILTRO** `ballena_activa_n` > `9.0` → IC=-0.204 (n=2607)

  - _Acción_: SKIP cuando `ballena_activa_n` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=9096)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.233 (n=3758)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=12411)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1046` → IC=-0.135 (n=61)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1046
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=121)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `py_entrada` < `0.455` → IC=-0.161 (n=302)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=1011)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=1298)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=1458)

- **FILTRO** `py_entrada` > `0.565` → IC=-0.172 (n=260)

  - _Acción_: SKIP cuando `py_entrada` > 0.565
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=888)

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
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=394)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.4307` → IC=+0.152 (n=673)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.76€ cuando `delta_ratio` |x|> 0.4307 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.130 (n=760)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 6.0 (IC base=+0.124)

- **PATRÓN** `total_vol_5m` < `418.1817` → IC=+0.164 (n=495)

  - _Acción_: Kelly boost +0.82€ cuando `total_vol_5m` < 418.1817 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `2321.735` → IC=+0.132 (n=1325)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 2321.735 (IC base=+0.124)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `14.0` → IC=+0.181 (n=180)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 14.0 (IC base=+0.135)

- **PATRÓN** `total_vol_5m` < `498.39` → IC=+0.154 (n=356)

  - _Acción_: Kelly boost +0.77€ cuando `total_vol_5m` < 498.39 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `2507.387` → IC=+0.244 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2507.387 (IC base=+0.135)

- **PATRÓN** `ballena_activa_n` < `6.0` → IC=+0.140 (n=170)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 6.0 (IC base=+0.135)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `delta_ratio` |x|> `0.4378` → IC=+0.154 (n=102)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.77€ cuando `delta_ratio` |x|> 0.4378 (IC base=+0.118)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.140 (n=281)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 15.0 (IC base=+0.118)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.125 (n=366)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.04 (IC base=+0.118)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4168` → IC=+0.179 (n=185)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.90€ cuando `delta_ratio` |x|> 0.4168 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.177 (n=97)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 15.0 (IC base=+0.126)

- **PATRÓN** `total_vol_5m` < `824.3104` → IC=+0.157 (n=278)

  - _Acción_: Kelly boost +0.79€ cuando `total_vol_5m` < 824.3104 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `59.0` → IC=+0.180 (n=95)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 59.0 (IC base=+0.126)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.4317` → IC=+0.212 (n=116)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio` |x|> 0.4317 (IC base=+0.142)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.174 (n=182)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 12.0 (IC base=+0.142)

- **PATRÓN** `total_vol_5m` < `4608.276` → IC=+0.180 (n=170)

  - _Acción_: Kelly boost +0.90€ cuando `total_vol_5m` < 4608.276 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `3709.6192` → IC=+0.163 (n=170)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 3709.6192 (IC base=+0.142)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.144 (n=116)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 27.0 (IC base=+0.142)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `hora_utc` < `13.0` → IC=+0.126 (n=260)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 13.0 (IC base=+0.098)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.140 (n=201)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.098)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `7.4417` → IC=-0.272 (n=55)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 7.4417
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=167)

- **FILTRO** `T_h` > `129.6211` → IC=-0.186 (n=208)

  - _Acción_: SKIP cuando `T_h` > 129.6211
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=625)

- **FILTRO** `pct_vs_K` |x|> `3.4135` → IC=-0.195 (n=283)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.4135
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=550)

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.150 (n=275)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0045 (IC base=-0.075)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `T_h` > `88.1766` → IC=-0.234 (n=62)

  - _Acción_: SKIP cuando `T_h` > 88.1766
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=187)

- **FILTRO** `pct_vs_K` |x|> `4.2538` → IC=-0.250 (n=62)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.2538
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=187)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.277 (n=83)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=-0.030)

- **PATRÓN** `pct_vs_K` |x|≤ `1.7112` → IC=+0.171 (n=83)

  - _Acción_: Kelly boost +0.85€ cuando `pct_vs_K` |x|≤ 1.7112 (IC base=-0.030)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `sigma_h` > `0.01` → IC=-0.155 (n=27)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.125 (n=54)

- **FILTRO** `pct_vs_K` |x|> `6.9241` → IC=-0.259 (n=27)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 6.9241
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=54)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0151` → IC=-0.207 (n=39)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0151
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=119)

### PRICE_TARGET_GBM#SOL#reach
- **FILTRO** `sigma_h` < `0.0164` → IC=-0.192 (n=24)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0164
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

- **FILTRO** `T_h` < `146.0708` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `T_h` < 146.0708
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=16)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0102` → IC=-0.235 (n=504)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0102
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=260)

- **FILTRO** `T_h` > `70.1154` → IC=-0.227 (n=511)

  - _Acción_: SKIP cuando `T_h` > 70.1154
  - _Potencial_: sin este filtro IC_bueno=-0.194 (n=253)

- **FILTRO** `pct_vs_K` |x|> `3.0893` → IC=-0.410 (n=164)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.0893
  - _Potencial_: sin este filtro IC_bueno=-0.122 (n=493)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `sigma_h` < `0.0095` → IC=-0.205 (n=188)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0095
  - _Potencial_: sin este filtro IC_bueno=-0.146 (n=63)

- **FILTRO** `T_h` < `61.882` → IC=-0.202 (n=82)

  - _Acción_: SKIP cuando `T_h` < 61.882
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=169)

- **FILTRO** `sigma_h` < `0.0044` → IC=-0.226 (n=60)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0044
  - _Potencial_: sin este filtro IC_bueno=-0.208 (n=183)

- **FILTRO** `T_h` > `143.4358` → IC=-0.258 (n=60)

  - _Acción_: SKIP cuando `T_h` > 143.4358
  - _Potencial_: sin este filtro IC_bueno=-0.197 (n=183)

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
- **FILTRO** `sigma_h` < `0.0097` → IC=-0.310 (n=140)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0097
  - _Potencial_: sin este filtro IC_bueno=-0.210 (n=74)

- **FILTRO** `T_h` > `95.4524` → IC=-0.287 (n=106)

  - _Acción_: SKIP cuando `T_h` > 95.4524
  - _Potencial_: sin este filtro IC_bueno=-0.264 (n=108)

- **FILTRO** `sigma_h` > `0.0091` → IC=-0.365 (n=50)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0091
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=151)

- **FILTRO** `sigma_h` < `0.0055` → IC=-0.211 (n=50)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0055
  - _Potencial_: sin este filtro IC_bueno=-0.141 (n=151)

- **FILTRO** `T_h` > `57.2198` → IC=-0.235 (n=134)

  - _Acción_: SKIP cuando `T_h` > 57.2198
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=67)

- **PATRÓN** `pct_vs_K` |x|≤ `0.8095` → IC=+0.198 (n=51)

  - _Acción_: Kelly boost +0.99€ cuando `pct_vs_K` |x|≤ 0.8095 (IC base=-0.160)

### PRICE_TARGET_GBM_FADE#ETH#reach
- **FILTRO** `sigma_h` < `0.0095` → IC=-0.152 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0095
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **FILTRO** `T_h` < `132.3532` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `T_h` < 132.3532
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=10)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` < `0.0083` → IC=-0.264 (n=53)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0083
  - _Potencial_: sin este filtro IC_bueno=-0.159 (n=162)

- **FILTRO** `T_h` > `66.1685` → IC=-0.224 (n=161)

  - _Acción_: SKIP cuando `T_h` > 66.1685
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=54)

- **FILTRO** `sigma_h` > `0.0142` → IC=-0.304 (n=49)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0142
  - _Potencial_: sin este filtro IC_bueno=-0.163 (n=96)

- **FILTRO** `sigma_h` < `0.0085` → IC=-0.263 (n=36)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0085
  - _Potencial_: sin este filtro IC_bueno=-0.194 (n=109)

- **FILTRO** `T_h` > `34.5323` → IC=-0.245 (n=108)

  - _Acción_: SKIP cuando `T_h` > 34.5323
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=37)

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

- **PATRÓN** `edge` > `0.1` → IC=+0.429 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1 (IC base=+0.394)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.400 (n=88)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0075 (IC base=+0.394)

- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.410 (n=176)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0097 (IC base=+0.394)

- **PATRÓN** `T_h` > `1.4832` → IC=+0.400 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4832 (IC base=+0.394)

- **PATRÓN** `dist_50` > `0.3717` → IC=+0.444 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3717 (IC base=+0.394)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.412 (n=326)
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

- **PATRÓN** `edge` > `0.2008` → IC=+0.471 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.2008 (IC base=+0.463)

- **PATRÓN** `sigma_h` < `0.0157` → IC=+0.474 (n=151)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0157 (IC base=+0.463)

- **PATRÓN** `T_h` < `0.8102` → IC=+0.457 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.8102 (IC base=+0.463)

- **PATRÓN** `T_h` > `1.486` → IC=+0.481 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.486 (IC base=+0.463)

- **PATRÓN** `dist_50` > `0.4597` → IC=+0.493 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4597 (IC base=+0.463)

- **PATRÓN** `hora_utc` < `2.0` → IC=+0.485 (n=63)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 2.0 (IC base=+0.463)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=409)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.072 (n=475)

- **PATRÓN** `streak_estiramiento` < `0.5379` → IC=+0.182 (n=218)

  - _Acción_: Kelly boost +0.91€ cuando `streak_estiramiento` < 0.5379 (IC base=+0.060)

- **PATRÓN** `ballena_activa_n` < `30.0` → IC=+0.128 (n=245)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 30.0 (IC base=+0.060)

### STREAK_FADE_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=17)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` < 0.495 (IC base=+0.071)

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
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=162)

- **PATRÓN** `streak_estiramiento` < `0.2206` → IC=+0.135 (n=61)

  - _Acción_: Kelly boost +0.67€ cuando `streak_estiramiento` < 0.2206 (IC base=+0.034)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.147 (n=117)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 11.0 (IC base=+0.097)

- **PATRÓN** `streak_estiramiento` < `0.4354` → IC=+0.183 (n=137)

  - _Acción_: Kelly boost +0.92€ cuando `streak_estiramiento` < 0.4354 (IC base=+0.097)

- **PATRÓN** `ballena_activa_n` < `31.0` → IC=+0.162 (n=149)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 31.0 (IC base=+0.097)

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

  - _Acción_: Kelly boost +0.76€ cuando `regimen_ma_toques` > 4.0 (IC base=+0.036)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=1062)

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
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=1294)

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
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=4818)

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
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=2789)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.190 (n=1724)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0053 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.2188` → IC=+0.160 (n=5172)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.2188 (IC base=+0.144)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3569` → IC=+0.152 (n=4819)

  - _Acción_: Kelly boost +0.76€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3569 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.153 (n=4771)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 6.0 (IC base=+0.144)

- **PATRÓN** `ibs_15` > `0.5833` → IC=+0.230 (n=4625)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5833 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` > `0.1329` → IC=+0.134 (n=2464)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` > 0.1329 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` < `0.4987` → IC=+0.130 (n=4829)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` < 0.4987 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.327` → IC=+0.255 (n=980)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.327 (IC base=+0.144)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=2993)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `4594.254` → IC=+0.168 (n=1723)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 4594.254 (IC base=+0.144)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=1966)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.221 (n=775)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0056 (IC base=+0.202)

- **PATRÓN** `drift_60min` |x|≤ `0.0598` → IC=+0.259 (n=259)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0598 (IC base=+0.202)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2676` → IC=+0.219 (n=258)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2676 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.220 (n=808)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.202)

- **PATRÓN** `ibs_15` > `0.7103` → IC=+0.276 (n=774)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7103 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` > `0.3722` → IC=+0.228 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3722 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` < `0.5105` → IC=+0.206 (n=873)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5105 (IC base=+0.202)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.54` → IC=+0.307 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.54 (IC base=+0.202)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.205 (n=1002)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `8194.7858` → IC=+0.210 (n=774)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8194.7858 (IC base=+0.202)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.007` → IC=+0.148 (n=958)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.007 (IC base=+0.131)

- **PATRÓN** `drift_60min` |x|≤ `0.1093` → IC=+0.144 (n=639)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.1093 (IC base=+0.131)

- **PATRÓN** `delta_ratio_macro` |x|> `0.141` → IC=+0.136 (n=638)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.68€ cuando `delta_ratio_macro` |x|> 0.141 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.136 (n=874)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 6.0 (IC base=+0.131)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.132 (n=958)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 16.0 (IC base=+0.131)

- **PATRÓN** `ibs_15` > `0.4934` → IC=+0.217 (n=957)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.4934 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` > `0.1169` → IC=+0.150 (n=601)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.1169 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` < `0.4255` → IC=+0.131 (n=1014)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` < 0.4255 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.76` → IC=+0.278 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.76 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `5907.3848` → IC=+0.163 (n=434)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 5907.3848 (IC base=+0.131)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `ibs_15` > `0.2506` → IC=-0.121 (n=201)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.2506
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=393)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `ibs_15` > `0.6` → IC=+0.136 (n=945)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.68€ cuando `ibs_15` > 0.6 (IC base=+0.060)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` < `0.0256` → IC=+0.166 (n=1280)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0256 (IC base=+0.156)

- **PATRÓN** `drift_60min` |x|≤ `0.2222` → IC=+0.175 (n=1280)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.2222 (IC base=+0.156)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0989` → IC=+0.219 (n=393)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0989 (IC base=+0.156)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.162 (n=1171)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 6.0 (IC base=+0.156)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.163 (n=1132)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 14.0 (IC base=+0.156)

- **PATRÓN** `ibs_15` > `0.5455` → IC=+0.233 (n=1146)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5455 (IC base=+0.156)

- **PATRÓN** `dist_vwap_pct` > `0.5229` → IC=+0.197 (n=311)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.5229 (IC base=+0.156)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.093` → IC=+0.210 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.093 (IC base=+0.156)

- **PATRÓN** `libro_liquidez` > `2717.8831` → IC=+0.186 (n=854)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 2717.8831 (IC base=+0.156)

- **PATRÓN** `ibs_15` < `0.1111` → IC=+0.156 (n=994)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.78€ cuando `ibs_15` < 0.1111 (IC base=+0.068)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.388 (n=247)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.363)

- **PATRÓN** `drift_60min` |x|≤ `0.1119` → IC=+0.365 (n=494)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1119 (IC base=+0.363)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1501` → IC=+0.377 (n=494)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1501 (IC base=+0.363)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1074` → IC=+0.377 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1074 (IC base=+0.363)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.371 (n=781)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.363)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.364 (n=498)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.363)

- **PATRÓN** `ibs_15` > `0.7883` → IC=+0.392 (n=741)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7883 (IC base=+0.363)

- **PATRÓN** `dist_vwap_pct` > `0.1523` → IC=+0.380 (n=438)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1523 (IC base=+0.363)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.922` → IC=+0.399 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.922 (IC base=+0.363)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.367 (n=901)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.363)

- **PATRÓN** `libro_liquidez` > `9681.5596` → IC=+0.382 (n=336)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9681.5596 (IC base=+0.363)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `drift_60min` |x|≤ `0.0553` → IC=+0.371 (n=122)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0553 (IC base=+0.363)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2196` → IC=+0.374 (n=165)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2196 (IC base=+0.363)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1441` → IC=+0.398 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1441 (IC base=+0.363)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.379 (n=338)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.363)

- **PATRÓN** `ibs_15` > `0.8078` → IC=+0.386 (n=365)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8078 (IC base=+0.363)

- **PATRÓN** `dist_vwap_pct` > `0.3736` → IC=+0.391 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3736 (IC base=+0.363)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.98` → IC=+0.389 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.98 (IC base=+0.363)

- **PATRÓN** `libro_liquidez` > `8065.6565` → IC=+0.386 (n=365)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8065.6565 (IC base=+0.363)

- **PATRÓN** `ballena_activa_n` < `489.0` → IC=+0.404 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 489.0 (IC base=+0.363)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.368 (n=376)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.363)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.379 (n=171)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.363)

- **PATRÓN** `drift_60min` |x|≤ `0.1078` → IC=+0.366 (n=251)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1078 (IC base=+0.363)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0824` → IC=+0.373 (n=336)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0824 (IC base=+0.363)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2969` → IC=+0.373 (n=306)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2969 (IC base=+0.363)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.365 (n=377)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.363)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.375 (n=174)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.363)

- **PATRÓN** `ibs_15` > `0.762` → IC=+0.392 (n=376)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.762 (IC base=+0.363)

- **PATRÓN** `dist_vwap_pct` > `0.1215` → IC=+0.370 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1215 (IC base=+0.363)

- **PATRÓN** `dist_vwap_pct` < `0.2796` → IC=+0.365 (n=347)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2796 (IC base=+0.363)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.973` → IC=+0.403 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.973 (IC base=+0.363)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.366 (n=425)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.363)

- **PATRÓN** `libro_liquidez` > `4142.643` → IC=+0.379 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4142.643 (IC base=+0.363)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0074` → IC=-0.193 (n=2660)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0074
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=2662)

- **FILTRO** `drift_15min` |x|> `0.9097` → IC=-0.144 (n=1329)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.9097
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=3992)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.217 (n=2233)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=3089)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1404` → IC=+0.221 (n=457)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1404 (IC base=-0.080)

- **PATRÓN** `ibs_15` > `0.6288` → IC=+0.280 (n=1209)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6288 (IC base=-0.080)

- **PATRÓN** `dist_vwap_pct` > `0.1102` → IC=+0.203 (n=708)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1102 (IC base=-0.080)

- **PATRÓN** `dist_vwap_pct` < `0.5564` → IC=+0.199 (n=1278)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5564 (IC base=-0.080)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2354` → IC=+0.270 (n=1604)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2354 (IC base=-0.005)

- **PATRÓN** `ibs_15` < `0.3684` → IC=+0.284 (n=4811)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3684 (IC base=-0.005)

- **PATRÓN** `dist_vwap_pct` > `0.649` → IC=+0.281 (n=677)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.649 (IC base=-0.005)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0316` → IC=-0.222 (n=2498)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0316
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=834)

- **FILTRO** `sigma_h` < `0.0037` → IC=-0.219 (n=833)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0037
  - _Potencial_: sin este filtro IC_bueno=-0.175 (n=2499)

- **FILTRO** `sigma_ewma_delta_pct` > `22.231` → IC=-0.257 (n=475)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 22.231
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=2857)

- **PATRÓN** `sigma_h` < `0.003` → IC=+0.155 (n=323)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.003 (IC base=+0.072)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2673` → IC=+0.282 (n=140)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2673 (IC base=+0.072)

- **PATRÓN** `ibs_15` > `0.7593` → IC=+0.326 (n=418)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7593 (IC base=+0.072)

- **PATRÓN** `dist_vwap_pct` > `0.1023` → IC=+0.277 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1023 (IC base=+0.072)

- **PATRÓN** `dist_vwap_pct` < `0.4912` → IC=+0.286 (n=466)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4912 (IC base=+0.072)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.337` → IC=+0.148 (n=217)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 22.337 (IC base=+0.072)

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
  - _Potencial_: sin este filtro IC_bueno=+0.152 (n=792)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.159 (n=607)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0065 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.0722` → IC=+0.177 (n=267)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.0722 (IC base=+0.146)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3048` → IC=+0.195 (n=474)

  - _Acción_: Kelly boost +0.98€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3048 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.161 (n=435)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 11.0 (IC base=+0.146)

- **PATRÓN** `ibs_15` > `0.5671` → IC=+0.242 (n=607)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5671 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.6301` → IC=+0.158 (n=112)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.6301 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` < `0.2675` → IC=+0.150 (n=567)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.2675 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.914` → IC=+0.265 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.914 (IC base=+0.146)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=792)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `8984.1415` → IC=+0.159 (n=203)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 8984.1415 (IC base=+0.146)

- **PATRÓN** `sigma_h` < `0.0081` → IC=+0.250 (n=1831)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0081 (IC base=+0.242)

- **PATRÓN** `drift_60min` |x|≤ `0.356` → IC=+0.247 (n=1612)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.356 (IC base=+0.242)

- **PATRÓN** `drift_15min` |x|≤ `0.7762` → IC=+0.258 (n=1612)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7762 (IC base=+0.242)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2152` → IC=+0.261 (n=831)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2152 (IC base=+0.242)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.254 (n=681)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.242)

- **PATRÓN** `ibs_15` < `0.3811` → IC=+0.273 (n=1831)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3811 (IC base=+0.242)

- **PATRÓN** `dist_vwap_pct` > `0.3785` → IC=+0.268 (n=460)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3785 (IC base=+0.242)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.253` → IC=+0.247 (n=714)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.253 (IC base=+0.242)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1827` → IC=-0.261 (n=308)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1827
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=928)

- **FILTRO** `drift_60min` |x|> `0.1722` → IC=-0.261 (n=420)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1722
  - _Potencial_: sin este filtro IC_bueno=-0.163 (n=816)

- **FILTRO** `drift_15min` |x|> `0.9082` → IC=-0.284 (n=308)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.9082
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=928)

- **FILTRO** `sigma_ewma_delta_pct` > `6.141` → IC=-0.203 (n=284)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.141
  - _Potencial_: sin este filtro IC_bueno=-0.194 (n=952)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.214 (n=246)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=990)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1455` → IC=+0.188 (n=46)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.94€ cuando `delta_ratio_macro` |x|> 0.1455 (IC base=-0.196)

- **PATRÓN** `ibs_15` > `0.5625` → IC=+0.234 (n=62)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5625 (IC base=-0.196)

- **PATRÓN** `dist_vwap_pct` > `0.2752` → IC=+0.143 (n=26)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.2752 (IC base=-0.196)

- **PATRÓN** `dist_vwap_pct` < `0.4298` → IC=+0.154 (n=76)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.4298 (IC base=-0.196)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0639` → IC=+0.234 (n=819)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0639 (IC base=-0.032)

- **PATRÓN** `ibs_15` < `0.3824` → IC=+0.295 (n=819)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3824 (IC base=-0.032)

- **PATRÓN** `dist_vwap_pct` > `0.6758` → IC=+0.241 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6758 (IC base=-0.032)

- **PATRÓN** `dist_vwap_pct` < `0.451` → IC=+0.241 (n=874)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.451 (IC base=-0.032)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0133` → IC=-0.241 (n=1131)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0133
  - _Potencial_: sin este filtro IC_bueno=-0.140 (n=378)

- **FILTRO** `libro_spread` > `0.04` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.04
  - _Potencial_: sin este filtro IC_bueno=-0.215 (n=1490)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.216)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.216)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1189` → IC=+0.296 (n=494)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1189 (IC base=-0.017)

- **PATRÓN** `ibs_15` < `0.1346` → IC=+0.309 (n=759)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.1346 (IC base=-0.017)

- **PATRÓN** `dist_vwap_pct` > `0.7632` → IC=+0.337 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7632 (IC base=-0.017)

### UPDOWN_GBM_ETH_15M_HORA7
- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.167 (n=43)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0061 (IC base=+0.097)

- **PATRÓN** `drift_60min` |x|≤ `0.1564` → IC=+0.144 (n=43)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.1564 (IC base=+0.097)

- **PATRÓN** `drift_15min` |x|≤ `0.3763` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3763 (IC base=+0.097)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2386` → IC=+0.197 (n=31)

  - _Acción_: Kelly boost +0.98€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2386 (IC base=+0.097)

- **PATRÓN** `ibs_15` > `0.8434` → IC=+0.340 (n=23)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8434 (IC base=+0.097)

- **PATRÓN** `dist_vwap_pct` > `0.4735` → IC=+0.167 (n=16)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.4735 (IC base=+0.097)

- **PATRÓN** `dist_vwap_pct` < `0.1207` → IC=+0.177 (n=29)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` < 0.1207 (IC base=+0.097)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.167 (n=43)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0061 (IC base=+0.097)

- **PATRÓN** `drift_60min` |x|≤ `0.1564` → IC=+0.144 (n=43)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.1564 (IC base=+0.097)

- **PATRÓN** `drift_15min` |x|≤ `0.3763` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3763 (IC base=+0.097)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2386` → IC=+0.197 (n=31)

  - _Acción_: Kelly boost +0.98€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2386 (IC base=+0.097)

- **PATRÓN** `ibs_15` > `0.8434` → IC=+0.340 (n=23)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8434 (IC base=+0.097)

- **PATRÓN** `dist_vwap_pct` > `0.4735` → IC=+0.167 (n=16)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.4735 (IC base=+0.097)

- **PATRÓN** `dist_vwap_pct` < `0.1207` → IC=+0.177 (n=29)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` < 0.1207 (IC base=+0.097)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.299 (n=441)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0033 (IC base=+0.284)

- **PATRÓN** `drift_60min` |x|≤ `0.0725` → IC=+0.312 (n=582)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0725 (IC base=+0.284)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1533` → IC=+0.286 (n=881)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1533 (IC base=+0.284)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2236` → IC=+0.290 (n=804)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2236 (IC base=+0.284)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.297 (n=1364)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.284)

- **PATRÓN** `ibs_15` > `0.8382` → IC=+0.312 (n=1323)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8382 (IC base=+0.284)

- **PATRÓN** `dist_vwap_pct` > `0.262` → IC=+0.314 (n=573)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.262 (IC base=+0.284)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.916` → IC=+0.389 (n=295)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.916 (IC base=+0.284)

- **PATRÓN** `libro_liquidez` > `13286.7566` → IC=+0.306 (n=441)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13286.7566 (IC base=+0.284)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.305 (n=234)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.277)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.278 (n=318)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.277)

- **PATRÓN** `drift_60min` |x|≤ `0.0593` → IC=+0.318 (n=234)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0593 (IC base=+0.277)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3948` → IC=+0.282 (n=628)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3948 (IC base=+0.277)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.296 (n=733)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.277)

- **PATRÓN** `ibs_15` > `0.829` → IC=+0.303 (n=702)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.829 (IC base=+0.277)

- **PATRÓN** `dist_vwap_pct` > `0.2467` → IC=+0.310 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2467 (IC base=+0.277)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.806` → IC=+0.392 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.806 (IC base=+0.277)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.279 (n=906)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.277)

- **PATRÓN** `libro_liquidez` > `14783.8555` → IC=+0.306 (n=318)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14783.8555 (IC base=+0.277)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.301 (n=622)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0069 (IC base=+0.290)

- **PATRÓN** `drift_60min` |x|≤ `0.0506` → IC=+0.314 (n=208)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0506 (IC base=+0.290)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1412` → IC=+0.293 (n=414)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1412 (IC base=+0.290)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1009` → IC=+0.326 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1009 (IC base=+0.290)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.302 (n=594)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.290)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.296 (n=571)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.290)

- **PATRÓN** `ibs_15` > `0.8489` → IC=+0.319 (n=621)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8489 (IC base=+0.290)

- **PATRÓN** `dist_vwap_pct` > `0.1241` → IC=+0.307 (n=417)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1241 (IC base=+0.290)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.164` → IC=+0.379 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.164 (IC base=+0.290)

### UPDOWN_OU_5M
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.0825` → IC=-0.155 (n=247)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.0825
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=83)

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
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=48)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.306` → IC=-0.385 (n=24)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.306
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `sigma_h` < `0.0072` → IC=-0.155 (n=27)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0072
  - _Potencial_: sin este filtro IC_bueno=-0.121 (n=27)

- **FILTRO** `ballena_activa_n` > `42.0` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `ballena_activa_n` > 42.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=33)

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
- **PATRÓN** `ratio` < `0.9704` → IC=+0.398 (n=371)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9704 (IC base=+0.175)

- **PATRÓN** `T_h` > `120.2753` → IC=+0.355 (n=2753)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 120.2753 (IC base=+0.337)

- **PATRÓN** `ratio` > `1.0221` → IC=+0.390 (n=462)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0221 (IC base=+0.337)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `111.9936` → IC=+0.145 (n=260)

  - _Acción_: Kelly boost +0.73€ cuando `T_h` > 111.9936 (IC base=+0.133)

- **PATRÓN** `ratio` < `0.9933` → IC=+0.268 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9933 (IC base=+0.133)

- **PATRÓN** `T_h` > `111.9836` → IC=+0.318 (n=990)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9836 (IC base=+0.303)

- **PATRÓN** `ratio` > `1.0187` → IC=+0.361 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0187 (IC base=+0.303)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `85.7585` → IC=+0.225 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 85.7585 (IC base=+0.223)

- **PATRÓN** `ratio` < `0.9854` → IC=+0.405 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9854 (IC base=+0.223)

- **PATRÓN** `T_h` > `111.9969` → IC=+0.356 (n=997)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9969 (IC base=+0.324)

- **PATRÓN** `ratio` > `1.0314` → IC=+0.401 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0314 (IC base=+0.324)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.0788` → IC=+0.419 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.0788 (IC base=+0.397)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5833 sube el IC de +0.144 a +0.230 en UPDOWN_GBM#15min (n=4625). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7103 sube el IC de +0.202 a +0.276 en UPDOWN_GBM#BTC#15min (n=774). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.4934 sube el IC de +0.131 a +0.217 en UPDOWN_GBM#ETH#15min (n=957). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5455 sube el IC de +0.156 a +0.233 en UPDOWN_GBM#XRP#15min (n=1146). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1111 sube el IC de +0.068 a +0.156 en UPDOWN_GBM#XRP#15min (n=994). Ya aplicado como kelly_boost=+0.78€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6288 sube el IC de -0.080 a +0.280 en UPDOWN_GBM_15M_TARDIO (n=1209). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3684 sube el IC de -0.005 a +0.284 en UPDOWN_GBM_15M_TARDIO (n=4811). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7593 sube el IC de +0.072 a +0.326 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=418). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.6255 sube el IC de -0.186 a +0.289 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=74). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.5671 sube el IC de +0.146 a +0.242 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=607). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3811 sube el IC de +0.242 a +0.273 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=1831). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de -0.196 a +0.234 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=62). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3824 sube el IC de -0.032 a +0.295 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=819). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.216 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.1346 sube el IC de -0.017 a +0.309 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=759). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_YES, IBS > 0.8434 sube el IC de +0.097 a +0.340 en UPDOWN_GBM_ETH_15M_HORA7 (n=23). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_YES, IBS > 0.8434 sube el IC de +0.097 a +0.340 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=23). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8382 sube el IC de +0.284 a +0.312 en UPDOWN_GBM_IBS_ALTO (n=1323). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.829 sube el IC de +0.277 a +0.303 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=702). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8489 sube el IC de +0.290 a +0.319 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=621). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7883 sube el IC de +0.363 a +0.392 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=741). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8078 sube el IC de +0.363 a +0.386 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=365). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.762 sube el IC de +0.363 a +0.392 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=376). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 2167 | +0.085 | +236.20€ | 1 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 2167 | +0.085 | +236.20€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1762 | +0.085 | +196.91€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1762 | +0.085 | +196.91€ | 1 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 284 | +0.070 | +11.30€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 284 | +0.070 | +11.30€ | 5 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 90 | +0.130 | +28.32€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 90 | +0.130 | +28.32€ | 1 | 10 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 1114 | -0.021 | +72.31€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 1114 | -0.021 | +72.31€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE | 7 | +0.019 | +3.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE#15min | 7 | +0.019 | +3.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 861 | -0.036 | +57.43€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 861 | -0.036 | +57.43€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 169 | +0.056 | +17.79€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 169 | +0.056 | +17.79€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 77 | -0.032 | -6.17€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 77 | -0.032 | -6.17€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 46601 | -0.086 | -5962.76€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 2843 | +0.065 | -295.62€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 43758 | -0.095 | -5667.13€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4775 | -0.113 | -805.43€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4775 | -0.113 | -805.43€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 2843 | +0.065 | -295.62€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 2843 | +0.065 | -295.62€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 4836 | -0.107 | -933.11€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 4836 | -0.107 | -933.11€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 12696 | -0.043 | -1169.87€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 12696 | -0.043 | -1169.87€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 12678 | -0.115 | -1332.23€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 12678 | -0.115 | -1332.23€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 8773 | -0.128 | -1426.49€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 8773 | -0.128 | -1426.49€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 47580 | -0.012 | +2931.24€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 12302 | +0.005 | +1536.00€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 35278 | -0.018 | +1395.24€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 47580 | -0.012 | +2931.24€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 12302 | +0.005 | +1536.00€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 35278 | -0.018 | +1395.24€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 183610 | +0.113 | -7689.53€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#15min | 21499 | +0.180 | -700.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 840 | +0.006 | -78.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 150752 | +0.105 | -6530.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 10519 | +0.093 | -379.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 24982 | +0.102 | -1768.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 75 | -0.175 | +11.25€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 24892 | +0.104 | -1767.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 34886 | +0.124 | -589.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5599 | +0.179 | -227.87€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 24959 | +0.120 | -184.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 4286 | +0.079 | -154.86€ | 1 | 2 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 25032 | +0.097 | -1851.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 86 | -0.114 | +7.00€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 24931 | +0.098 | -1847.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 39203 | +0.123 | -830.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 9901 | +0.177 | -251.93€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 25352 | +0.105 | -517.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 3938 | +0.103 | -52.01€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#SOL | 34499 | +0.112 | -1535.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 5751 | +0.198 | -248.79€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 743 | +0.033 | -24.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 25710 | +0.096 | -1089.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 2295 | +0.102 | -172.97€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO#XRP | 25008 | +0.106 | -1114.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 87 | -0.118 | +9.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 24908 | +0.107 | -1123.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 29753 | +0.193 | -2023.43€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 29753 | +0.193 | -2023.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 6731 | +0.172 | -664.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 6731 | +0.172 | -664.79€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 4248 | +0.197 | -153.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 4248 | +0.197 | -153.39€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 6615 | +0.176 | -569.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 6615 | +0.176 | -569.48€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 5565 | +0.250 | -202.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 5565 | +0.250 | -202.18€ | 0 | 4 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 6515 | +0.185 | -447.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 6515 | +0.185 | -447.34€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 1217 | +0.425 | -45.72€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 1217 | +0.425 | -45.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 499 | +0.438 | -5.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 499 | +0.438 | -5.84€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE#15min | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 491 | +0.425 | -17.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 491 | +0.425 | -17.64€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 213 | +0.398 | -18.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 213 | +0.398 | -18.37€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 105114 | +0.200 | -7765.58€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 105114 | +0.200 | -7765.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 18158 | +0.179 | -2052.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 18158 | +0.179 | -2052.46€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 16948 | +0.224 | -565.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 16948 | +0.224 | -565.37€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 18048 | +0.180 | -1928.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 18048 | +0.180 | -1928.04€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 17086 | +0.218 | -685.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 17086 | +0.218 | -685.01€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 17375 | +0.202 | -1115.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 17375 | +0.202 | -1115.02€ | 1 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 17499 | +0.196 | -1419.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 17499 | +0.196 | -1419.69€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 40440 | +0.117 | +326.58€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 40440 | +0.117 | +326.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 20135 | +0.117 | +195.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 20135 | +0.117 | +195.99€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 20305 | +0.116 | +130.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 20305 | +0.116 | +130.59€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 2532 | +0.292 | -11.58€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 2532 | +0.292 | -11.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 1160 | +0.280 | -32.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 1160 | +0.280 | -32.76€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 1234 | +0.298 | +16.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 1234 | +0.298 | +16.12€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 138 | +0.343 | +5.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 138 | +0.343 | +5.05€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 1165 | +0.439 | -1.99€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 1165 | +0.439 | -1.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 559 | +0.432 | -10.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 559 | +0.432 | -10.37€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 555 | +0.446 | +7.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 555 | +0.446 | +7.12€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 51 | +0.406 | +1.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 51 | +0.406 | +1.25€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1919 | +0.067 | -86.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 725 | +0.046 | -64.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 1194 | +0.080 | -22.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1485 | +0.075 | -41.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 291 | +0.053 | -19.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 1194 | +0.080 | -22.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 81826 | +0.101 | -1961.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 6594 | +0.096 | +135.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 75232 | +0.101 | -2097.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 44750 | +0.105 | -449.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 6594 | +0.096 | +135.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 38156 | +0.107 | -584.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 17335 | +0.108 | -107.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 17335 | +0.108 | -107.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 19741 | +0.082 | -1404.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 19741 | +0.082 | -1404.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 914 | +0.186 | -109.27€ | 5 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 914 | +0.186 | -109.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 914 | +0.186 | -109.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 914 | +0.186 | -109.27€ | 5 | 4 |
| ✅ GBM_LATE_15M | 55503 | +0.099 | +30754.12€ | 0 | 18 |
| ✅ GBM_LATE_15M#15min | 55503 | +0.099 | +30754.12€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 9190 | +0.226 | +7936.79€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 9190 | +0.226 | +7936.79€ | 0 | 21 |
| ✅ GBM_LATE_15M#BTC | 8460 | +0.175 | +6598.49€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 8460 | +0.175 | +6598.49€ | 0 | 22 |
| ✅ GBM_LATE_15M#DOGE | 9967 | +0.207 | +7858.07€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 9967 | +0.207 | +7858.07€ | 0 | 21 |
| ✅ GBM_LATE_15M#ETH | 7487 | +0.052 | +2344.16€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 7487 | +0.052 | +2344.16€ | 1 | 18 |
| ✅ GBM_LATE_15M#SOL | 7759 | -0.032 | +1999.38€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 7759 | -0.032 | +1999.38€ | 4 | 15 |
| ✅ GBM_LATE_15M#XRP | 12640 | -0.023 | +4017.23€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 12640 | -0.023 | +4017.23€ | 3 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 58382 | +0.085 | +33806.73€ | 0 | 18 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 58382 | +0.085 | +33806.73€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 11293 | -0.002 | +6047.56€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 11293 | -0.002 | +6047.56€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 12542 | +0.004 | +3308.20€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 12542 | +0.004 | +3308.20€ | 0 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 7973 | +0.294 | +9077.68€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 7973 | +0.294 | +9077.68€ | 0 | 22 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 11102 | +0.013 | +3424.24€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 11102 | +0.013 | +3424.24€ | 1 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 9001 | +0.043 | +4007.03€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 9001 | +0.043 | +4007.03€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 6471 | +0.316 | +7942.02€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 6471 | +0.316 | +7942.02€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 43962 | +0.178 | +36213.54€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 43962 | +0.178 | +36213.54€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 6610 | +0.240 | +6160.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 6610 | +0.240 | +6160.28€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 6955 | +0.139 | +5118.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 6955 | +0.139 | +5118.83€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 7077 | +0.224 | +6128.75€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 7077 | +0.224 | +6128.75€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 7538 | +0.129 | +5846.69€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 7538 | +0.129 | +5846.69€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 8317 | +0.119 | +6218.92€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 8317 | +0.119 | +6218.92€ | 1 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 7465 | +0.232 | +6740.07€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 7465 | +0.232 | +6740.07€ | 0 | 25 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 11889 | +0.125 | +5922.93€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 11889 | +0.125 | +5922.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 468 | +0.157 | +308.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 468 | +0.157 | +308.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 3358 | +0.129 | +1824.78€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 3358 | +0.129 | +1824.78€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 505 | +0.159 | +279.48€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 505 | +0.159 | +279.48€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 3497 | +0.124 | +1676.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 3497 | +0.124 | +1676.81€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 3029 | +0.096 | +1195.56€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 3029 | +0.096 | +1195.56€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 1032 | +0.166 | +637.57€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 1032 | +0.166 | +637.57€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO | 55698 | +0.187 | +45676.47€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#15min | 55698 | +0.187 | +45676.47€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 8780 | +0.251 | +8514.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 8780 | +0.251 | +8514.87€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 8827 | +0.137 | +6052.19€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 8827 | +0.137 | +6052.19€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 9465 | +0.235 | +8551.17€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 9465 | +0.235 | +8551.17€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 9226 | +0.140 | +6789.86€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 9226 | +0.140 | +6789.86€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 9891 | +0.121 | +6962.85€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 9891 | +0.121 | +6962.85€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 9509 | +0.240 | +8805.53€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 9509 | +0.240 | +8805.53€ | 0 | 19 |
| ✅ GBM_LATE_5M | 13844 | +0.210 | +11222.37€ | 1 | 26 |
| ✅ GBM_LATE_5M#5min | 13844 | +0.210 | +11222.37€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 1054 | +0.246 | +1000.28€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 1054 | +0.246 | +1000.28€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 3258 | +0.211 | +2815.67€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 3258 | +0.211 | +2815.67€ | 0 | 25 |
| ✅ GBM_LATE_5M#DOGE | 1322 | +0.204 | +1023.94€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1322 | +0.204 | +1023.94€ | 0 | 21 |
| ✅ GBM_LATE_5M#ETH | 4048 | +0.203 | +3027.03€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 4048 | +0.203 | +3027.03€ | 0 | 25 |
| ✅ GBM_LATE_5M#SOL | 2203 | +0.208 | +1818.33€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 2203 | +0.208 | +1818.33€ | 0 | 26 |
| ✅ GBM_LATE_5M#XRP | 1959 | +0.209 | +1537.13€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1959 | +0.209 | +1537.13€ | 0 | 0 |
| ✅ GBM_LATE_60M | 4906 | +0.049 | +1340.40€ | 1 | 6 |
| ✅ GBM_LATE_60M#60min | 4906 | +0.049 | +1340.40€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 1711 | +0.058 | +523.82€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 1711 | +0.058 | +523.82€ | 1 | 6 |
| ✅ GBM_LATE_60M#ETH | 1580 | +0.051 | +497.93€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 1580 | +0.051 | +497.93€ | 1 | 6 |
| ✅ GBM_LATE_60M#SOL | 1615 | +0.039 | +318.65€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 1615 | +0.039 | +318.65€ | 0 | 9 |
| 🚫 GBM_LATE_60M_FADE | 700 | -0.249 | -36.16€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 700 | -0.249 | -36.16€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 255 | -0.251 | -20.81€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 255 | -0.251 | -20.81€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 258 | -0.242 | -6.03€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 258 | -0.242 | -6.03€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 187 | -0.251 | -9.32€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 187 | -0.251 | -9.32€ | 5 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 2036 | +0.082 | +527.92€ | 0 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 2036 | +0.082 | +527.92€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 783 | +0.069 | +189.48€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 783 | +0.069 | +189.48€ | 1 | 4 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 722 | +0.057 | +141.22€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 722 | +0.057 | +141.22€ | 2 | 12 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 531 | +0.134 | +197.22€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 531 | +0.134 | +197.22€ | 1 | 9 |
| ✅ LATE_WINDOW_5MIN | 234 | +0.292 | +262.43€ | 1 | 13 |
| ✅ LATE_WINDOW_5MIN#5min | 234 | +0.292 | +262.43€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 234 | +0.292 | +262.43€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 234 | +0.292 | +262.43€ | 1 | 13 |
| ✅ LEADLAG_BTC_XRP_15M | 4293 | +0.097 | +973.33€ | 0 | 1 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 4293 | +0.097 | +973.33€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 4293 | +0.097 | +973.33€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 4293 | +0.097 | +973.33€ | 0 | 1 |
| ✅ LIQUIDACIONES_15M | 1026 | -0.012 | +13.51€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 1026 | -0.012 | +13.51€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 56 | +0.017 | +0.59€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 56 | +0.017 | +0.59€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 272 | -0.007 | +7.15€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 272 | -0.007 | +7.15€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 35 | -0.149 | -5.62€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 35 | -0.149 | -5.62€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 275 | +0.020 | +17.85€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 275 | +0.020 | +17.85€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 306 | -0.013 | +1.32€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 306 | -0.013 | +1.32€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 82 | -0.083 | -7.78€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 82 | -0.083 | -7.78€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 4160 | +0.017 | +120.50€ | 5 | 1 |
| ✅ LIQUIDACIONES_5M#5min | 4160 | +0.017 | +120.50€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 205 | +0.022 | -1.78€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 205 | +0.022 | -1.78€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 825 | +0.015 | +40.47€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 825 | +0.015 | +40.47€ | 4 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 240 | +0.025 | +24.23€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 240 | +0.025 | +24.23€ | 0 | 4 |
| ✅ LIQUIDACIONES_5M#ETH | 1648 | +0.019 | +27.42€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1648 | +0.019 | +27.42€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 769 | +0.011 | +1.89€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 769 | +0.011 | +1.89€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 473 | +0.014 | +28.29€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 473 | +0.014 | +28.29€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 2296 | -0.033 | -9.93€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 2296 | -0.033 | -9.93€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 692 | -0.033 | -13.43€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 692 | -0.033 | -13.43€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 814 | -0.007 | +19.30€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 814 | -0.007 | +19.30€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 790 | -0.059 | -15.81€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 790 | -0.059 | -15.81€ | 5 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 14752 | -0.031 | -106.55€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 7088 | -0.033 | -83.86€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 7664 | -0.029 | -22.69€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 526 | -0.049 | -25.67€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 268 | -0.022 | +3.69€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 258 | -0.077 | -29.36€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 3860 | -0.025 | -5.97€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 1838 | -0.024 | +0.72€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 2022 | -0.026 | -6.69€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 1454 | -0.028 | +14.54€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 745 | -0.033 | +0.38€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 709 | -0.023 | +14.16€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 3335 | -0.034 | -51.75€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 1572 | -0.037 | -39.88€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 1763 | -0.030 | -11.88€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 2836 | -0.023 | +38.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 1374 | -0.028 | +2.93€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 1462 | -0.018 | +35.24€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 2741 | -0.043 | -75.86€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 1291 | -0.051 | -51.71€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 1450 | -0.036 | -24.16€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 65833 | -0.000 | +3552.40€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 65833 | -0.000 | +3552.40€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 11919 | +0.027 | +1633.13€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 11919 | +0.027 | +1633.13€ | 2 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 9231 | -0.036 | -115.57€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 9231 | -0.036 | -115.57€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 12054 | +0.025 | +1320.74€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 12054 | +0.025 | +1320.74€ | 1 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 9149 | -0.051 | -203.01€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 9149 | -0.051 | -203.01€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 11218 | -0.004 | +316.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 11218 | -0.004 | +316.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 12262 | +0.017 | +600.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 12262 | +0.017 | +600.34€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 7132 | -0.055 | -119.15€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 7132 | -0.055 | -119.15€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1245 | -0.003 | -16.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1245 | -0.003 | -16.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1975 | -0.065 | -27.06€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1975 | -0.065 | -27.06€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 73 | -0.020 | -0.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 73 | -0.020 | -0.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 807 | -0.119 | -34.96€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 807 | -0.119 | -34.96€ | 5 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 2169 | -0.068 | -13.03€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 2169 | -0.068 | -13.03€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 863 | -0.018 | -27.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 863 | -0.018 | -27.52€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 161517 | -0.078 | +2405.32€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 161517 | -0.078 | +2405.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 28272 | -0.078 | +1670.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 28272 | -0.078 | +1670.75€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 24158 | -0.101 | -1199.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 24158 | -0.101 | -1199.42€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 28632 | -0.068 | +1462.83€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 28632 | -0.068 | +1462.83€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 23699 | -0.098 | -700.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 23699 | -0.098 | -700.93€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 28884 | -0.058 | +335.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 28884 | -0.058 | +335.32€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 27872 | -0.069 | +836.76€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 27872 | -0.069 | +836.76€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 9027 | -0.035 | -182.01€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 9027 | -0.035 | -182.01€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 1003 | -0.016 | -18.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 1003 | -0.016 | -18.88€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 2095 | -0.046 | -26.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 2095 | -0.046 | -26.97€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2639 | -0.026 | -38.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2639 | -0.026 | -38.71€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1270 | -0.065 | -32.51€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1270 | -0.065 | -32.51€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 1011 | -0.031 | -33.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 1011 | -0.031 | -33.00€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 2113 | +0.120 | +839.95€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#5min | 1977 | +0.124 | +827.35€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 474 | +0.135 | +231.88€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 474 | +0.135 | +231.88€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#DOGE | 401 | +0.118 | +139.50€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 401 | +0.118 | +139.50€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#ETH | 370 | +0.126 | +167.71€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 370 | +0.126 | +167.71€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 339 | +0.142 | +175.06€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 339 | +0.142 | +175.06€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#XRP | 393 | +0.098 | +113.20€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 393 | +0.098 | +113.20€ | 0 | 2 |
| ✅ ORDER_FLOW_5M_REACTIVO | 2116 | -0.016 | -16.73€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 2116 | -0.016 | -16.73€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 393 | +0.014 | +25.01€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 393 | +0.014 | +25.01€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 387 | -0.048 | -27.15€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 387 | -0.048 | -27.15€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 534 | -0.034 | -23.72€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 534 | -0.034 | -23.72€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 432 | -0.002 | -0.65€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 432 | -0.002 | -0.65€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 370 | -0.005 | +9.77€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 370 | -0.005 | +9.77€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 1122 | -0.075 | -43.18€ | 3 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 516 | -0.108 | -77.10€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 404 | -0.123 | -58.64€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 112 | -0.053 | -18.46€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 394 | -0.035 | +25.03€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 283 | -0.019 | +34.47€ | 2 | 2 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 111 | -0.075 | -9.44€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 212 | -0.065 | +8.89€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 176 | -0.062 | +7.05€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 36 | -0.079 | +1.84€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 863 | -0.077 | -17.11€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 259 | -0.067 | -26.07€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 1421 | -0.207 | -90.14€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC | 561 | -0.205 | -49.85€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#atexpiry | 494 | -0.204 | -45.54€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#reach | 67 | -0.210 | -4.31€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 473 | -0.212 | -39.07€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 415 | -0.222 | -45.98€ | 5 | 1 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 58 | -0.133 | +6.91€ | 2 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL | 387 | -0.202 | -1.22€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 360 | -0.199 | -3.62€ | 5 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 27 | -0.224 | +2.40€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 1269 | -0.209 | -95.14€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 152 | -0.188 | +5.00€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 535 | +0.377 | +503.19€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#BTC | 107 | +0.151 | +88.66€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 107 | +0.151 | +88.66€ | 0 | 5 |
| ✅ RESOLUTION_SNIPER#ETH | 123 | +0.364 | +103.53€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 123 | +0.364 | +103.53€ | 0 | 5 |
| ✅ RESOLUTION_SNIPER#SOL | 305 | +0.458 | +311.00€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 305 | +0.458 | +311.00€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#sniper | 535 | +0.377 | +503.19€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 922 | +0.044 | +83.60€ | 2 | 2 |
| ✅ STREAK_FADE_15M#15min | 922 | +0.044 | +83.60€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 347 | +0.027 | +8.12€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 347 | +0.027 | +8.12€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 72 | +0.013 | +0.80€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 72 | +0.013 | +0.80€ | 1 | 1 |
| ✅ STREAK_FADE_15M#SOL | 83 | +0.018 | +6.06€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 83 | +0.018 | +6.06€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 420 | +0.069 | +68.62€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 420 | +0.069 | +68.62€ | 1 | 4 |
| ✅ STREAK_FADE_5M | 3565 | -0.023 | -141.58€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3565 | -0.023 | -141.58€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 1127 | -0.023 | -40.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 1127 | -0.023 | -40.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 610 | -0.028 | -26.72€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 610 | -0.028 | -26.72€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 171 | -0.043 | -14.80€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 171 | -0.043 | -14.80€ | 4 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1657 | -0.019 | -59.85€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1657 | -0.019 | -59.85€ | 2 | 0 |
| ✅ STREAK_FADE_60M | 117 | -0.046 | -11.69€ | 5 | 0 |
| ✅ STREAK_FADE_60M#60min | 117 | -0.046 | -11.69€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 44 | -0.087 | -4.62€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 44 | -0.087 | -4.62€ | 4 | 0 |
| ✅ STREAK_FADE_60M#SOL | 73 | -0.020 | -7.07€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 73 | -0.020 | -7.07€ | 0 | 1 |
| ✅ STREAK_MOM_5M | 11485 | +0.014 | +74.59€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 11485 | +0.014 | +74.59€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2994 | +0.018 | +23.87€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2994 | +0.018 | +23.87€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2994 | +0.017 | +36.32€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2994 | +0.017 | +36.32€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2917 | +0.008 | -3.28€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2917 | +0.008 | -3.28€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2580 | +0.014 | +17.68€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2580 | +0.014 | +17.68€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 11666 | +0.017 | -18.31€ | 4 | 0 |
| ✅ STRUCT_NO_15M#15min | 11666 | +0.017 | -18.31€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 4837 | +0.021 | +5.11€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 4837 | +0.021 | +5.11€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 4006 | +0.015 | -12.97€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 4006 | +0.015 | -12.97€ | 4 | 0 |
| ✅ STRUCT_NO_15M#SOL | 2823 | +0.011 | -10.44€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 2823 | +0.011 | -10.44€ | 1 | 0 |
| ✅ UPDOWN_GBM | 103522 | +0.060 | +9900.26€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 25225 | +0.080 | +5176.34€ | 0 | 10 |
| ✅ UPDOWN_GBM#240min | 3090 | +0.000 | +33.27€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 68734 | +0.062 | +4577.75€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 6116 | -0.000 | +116.26€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 8521 | +0.105 | +1569.43€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1781 | +0.164 | +820.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 90 | -0.011 | -2.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 6650 | +0.091 | +751.23€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 23616 | +0.057 | +2086.12€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 3372 | +0.080 | +765.77€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 876 | +0.001 | +15.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 16500 | +0.067 | +1225.64€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 2738 | -0.003 | +74.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 130 | -0.061 | +4.65€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 11256 | +0.079 | +1310.15€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1761 | +0.154 | +738.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 86 | +0.023 | -0.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 9409 | +0.066 | +572.57€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 24616 | +0.050 | +1723.06€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 5961 | +0.072 | +905.20€ | 0 | 10 |
| ✅ UPDOWN_GBM#ETH#240min | 844 | +0.005 | +16.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 15445 | +0.052 | +763.80€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 2247 | +0.002 | +35.91€ | 1 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 119 | -0.103 | +1.76€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 22084 | +0.040 | +1269.37€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 6706 | +0.032 | +438.79€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#240min | 797 | -0.009 | +5.75€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 13344 | +0.051 | +826.86€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 1131 | +0.002 | +5.91€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#daily | 106 | -0.139 | -7.94€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 13427 | +0.073 | +1943.98€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 5644 | +0.095 | +1507.95€ | 0 | 10 |
| ✅ UPDOWN_GBM#XRP#240min | 397 | +0.006 | -1.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 7386 | +0.060 | +437.65€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 355 | -0.099 | -1.53€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 987 | +0.363 | +359.02€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 987 | +0.363 | +359.02€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 486 | +0.363 | +171.22€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 486 | +0.363 | +171.22€ | 0 | 9 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 501 | +0.363 | +187.80€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 501 | +0.363 | +187.80€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO | 24831 | -0.021 | +6131.92€ | 3 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 24831 | -0.021 | +6131.92€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1981 | -0.051 | +561.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1981 | -0.051 | +561.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 4620 | -0.114 | +234.48€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 4620 | -0.114 | +234.48€ | 3 | 11 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 1071 | +0.222 | +899.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 1071 | +0.222 | +899.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 3250 | +0.218 | +2067.78€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 3250 | +0.218 | +2067.78€ | 1 | 18 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 7031 | -0.060 | +1044.60€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 7031 | -0.060 | +1044.60€ | 5 | 8 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 6878 | -0.061 | +1324.00€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 6878 | -0.061 | +1324.00€ | 2 | 5 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 299 | +0.061 | +23.77€ | 0 | 7 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 299 | +0.061 | +23.77€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 299 | +0.061 | +23.77€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 299 | +0.061 | +23.77€ | 0 | 7 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1763 | +0.284 | +1479.95€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1763 | +0.284 | +1479.95€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 935 | +0.277 | +735.83€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 935 | +0.277 | +735.83€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 828 | +0.290 | +744.12€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 828 | +0.290 | +744.12€ | 0 | 9 |
| ✅ UPDOWN_OU_5M | 860 | -0.113 | -84.72€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#5min | 860 | -0.113 | -84.72€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 270 | -0.081 | -20.33€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 270 | -0.081 | -20.33€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 96 | -0.173 | -11.45€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 96 | -0.173 | -11.45€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 111 | -0.173 | -3.59€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 111 | -0.173 | -3.59€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 38 | -0.175 | -6.61€ | 2 | 0 |
| ✅ WEEKLY_PRICE | 4560 | +0.303 | +2099.95€ | 0 | 3 |
| ✅ WEEKLY_PRICE#BTC | 1730 | +0.260 | +234.76€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 1756 | +0.297 | +758.75€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 1074 | +0.381 | +1106.43€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**〰️ H-IBS-15** — IBS-15 como señal de mean-reversion
  - _Umbral_: n≥40 ops con ibs_15 en features y spread_IC>0.15 entre buckets
  - _Acción_: Añadir ibs_15 como boost/filtro en FEATURE_RULES de shadow_postmortem.py
  - _Estado_: Spread bajo (0.037) — sin ventaja clara. oversold(IBS<0.3): IC=+0.071 n=36016 | neutral: IC=+0.062 n=38132 | overbought(IBS>0.7): IC=+0.099 n=35861
  - _Datos_: n=114525 IC=+0.079 PNL=+17480.59€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 797 celda(s) pasan gate riguroso completo de 2869 evaluadas (n>=40) y 3990 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.032 < 0.08 — monitorear
  - _Datos_: n=6706 IC=+0.032 PNL=+438.79€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=1756/15 IC=+0.297 PNL=+758.75€ | BTC: n=1730/15 IC=+0.260 PNL=+234.76€ | SOL: n=1074/15 IC=+0.381 PNL=+1106.43€

**🟡 H-KALMAN** — Kalman filter para drift adaptativo
  - _Umbral_: n≥200 por subtipo para calibrar parámetros Q/R del KF
  - _Acción_: Sustituir DRIFT_DAMPING por KalmanDrift en fetch_binance_klines.py
  - _Estado_: 31 subtypes con n≥200: UPDOWN_GBM, UPDOWN_GBM#ETH#60min, UPDOWN_GBM#ETH, UPDOWN_GBM#60min, UPDOWN_GBM#BTC#60min
  - _Bloqueante_: N_INSUFICIENTE


### ⏳ Acumulando datos

**⏳ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: 15
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: Falta 11 ops más en GBM@18h (IC actual=-0.067)
  - _Datos_: n=4 IC=-0.067 PNL=-3.02€

**⏳ H-HORA-GBM** — hora_utc causal automático en GBM (forward)
  - _Umbral_: n≥20 forward con hora_utc + alguna hora con n≥15 IC<-0.10 o >+0.10
  - _Acción_: El sistema lo aplica automáticamente vía FEATURE_RULES. Verificar en strategy_params.json.
  - _Estado_: 103460 ops, 22 horas distintas. Sin hora con n≥15 y IC extremo aún.

**⏳ H-WINDOW-MOMENTUM** — Momentum de outcome entre ventanas 15min contiguas
  - _Umbral_: n≥60 alineadas y gap IC≥0.08 vs contrarias — y descartar que sea proxy de drift_15min/60min
  - _Acción_: Si confirma e independiente de drift → capturar prev_window_outcome como feature en shadow_predict y boost ×1.1-1.2 en señales alineadas
  - _Estado_: alineada_con_outcome_prev IC=+0.141 n=1045/60 | contraria IC=+0.184 n=1099 | gap=-0.043 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=578, boost estimado=+0.013. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 339 ops con delta_ratio

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=2247/40 IC=+0.002 PNL=+35.91€ | BTC#60min: n=2738/40 IC=-0.003 PNL=+74.44€ | SOL#60min: n=1131/40 IC=+0.002 PNL=+5.91€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.045 n=713068 | tras_1loss IC=+0.099 n=541210 | tras_2loss IC=+0.069 n=216839/40 | gap=-0.024 (umbral 0.05)

**⏳ H-BTC-LEADS-ETH** — ETH/SOL GBM contrario al drift_15min de BTC del mismo ciclo
  - _Umbral_: n≥40 en contrario_BTC y gap≥0.08 — y descartar confound con drift propio antes de actuar
  - _Acción_: Si se confirma y no es confound → boost en ETH/SOL cuando decisión contraria a drift_15min BTC
  - _Estado_: alineado_BTC IC=+0.043 n=15400 | contrario_BTC IC=+0.054 n=13520/40 | gap=+0.011 (umbral 0.08) — SIN CONFIRMAR independencia de filtros propios de ETH


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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.167 > 0.08 con n=1020 PNL=+641.76€
  - _Datos_: n=1020 IC=+0.167 PNL=+641.76€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.137 > 0.08 con n=1220 PNL=+592.17€
  - _Datos_: n=1220 IC=+0.137 PNL=+592.17€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.335 > 0.1 con n=3714 PNL=+2080.44€
  - _Datos_: n=3714 IC=+0.335 PNL=+2080.44€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=1043 IC=+0.064 PNL=+99.80€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1043 IC=+0.064 PNL=+99.80€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=105 IC=+0.173 PNL=+66.22€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=105 IC=+0.173 PNL=+66.22€

**〰️ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: n=99459 IC=+0.060 PNL=+9600.14€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=99459 IC=+0.060 PNL=+9600.14€

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
  - _Estado_: n=4096 IC=+0.002 PNL=-14.51€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=4096 IC=+0.002 PNL=-14.51€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=2020 IC=-0.005 PNL=+130.77€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=2020 IC=-0.005 PNL=+130.77€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=1274 IC=+0.021 PNL=+62.00€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=1274 IC=+0.021 PNL=+62.00€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.144 > 0.1 con n=6892 PNL=+3545.17€
  - _Datos_: n=6892 IC=+0.144 PNL=+3545.17€

**〰️ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: n=2934 IC=+0.068 PNL=+221.39€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=2934 IC=+0.068 PNL=+221.39€

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=3372 IC=+0.080 PNL=+765.77€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=3372 IC=+0.080 PNL=+765.77€

**⏳ H-CUSTOM-DRIFT15-ZONA-MUERTA** — GBM#15min drift_15min ∈ [-0.3,+0.3] — zona muerta de señal
  - _Hipótesis_: Análisis n=127 GBM#15min: cuando drift_15min está entre -0.3 y +0.3 (mercado sin dirección clara) el IC es negativo (-0.043). Cuando drift>0.3 IC=+0.100 (n=28). Cuando drift<-1 IC=+0.048 (reversión). La señal requiere mercado con dirección clara.
  - _Umbral_: 50
  - _Acción_: Filtrar señales GBM#15min cuando drift_15min ∈ [-0.3, +0.3] — validar con n≥50 antes de implementar
  - _Estado_: 1/50 ops en el filtro definido (IC actual=+0.008 PNL=+1.17€)
  - _Datos_: n=1 IC=+0.008 PNL=+1.17€
  - _Bloqueante_: FILTRO_YA_IMPLEMENTADO: confirmada 2026-07-01 (IC=-0.037 n=52) e implementada en shadow_predict.py (skip si drift_15min∈[-0.3,0.3)) -- verificado 26-Ago con 2177 filas post-TWAP reales, 0 caen en la zona filtrada. Frozen by design, no falta n

**🟡 H-CUSTOM-DRIFT15-MOMENTUM** — GBM#15min drift_15min > 0.3 — zona de momentum (señal fuerte)
  - _Hipótesis_: Cuando drift_15min > 0.3%/h el GBM captura bien la dirección: IC=+0.100 n=28 en todos GBM#15min; IC=+0.152 n=13 solo BTC. El mercado tiene dirección clara y el GBM la sigue. Hipótesis: este rango es donde la señal es real.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma IC>0.10 con n≥40 → boost ×1.2 en GBM#15min cuando drift_15min>0.3
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.092 > 0.08 con n=14620 PNL=+3721.51€
  - _Datos_: n=14620 IC=+0.092 PNL=+3721.51€

**〰️ H-CUSTOM-LONGSHOT-BIAS** — Longshot bias — ¿mejor IC cuando py_mkt < 0.20 o > 0.80?
  - _Hipótesis_: Jon-Becker repo documenta formalmente: contratos a 1-20 cents tienen win_rate < precio implícito (compradores pierden sistemáticamente en longshots). En nuestro sistema: cuando py_mkt<0.20 el GBM predice BUY_NO con edge estructural adicional al del modelo. ¿Se confirma en nuestros datos? Buscar en feature pct_spot_vs_ref si los mercados extremos tienen mejor IC en BUY_NO.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 en mercados extremos → boost ×1.2 en BUY_NO cuando py_mkt<0.20
  - _Estado_: n=691 IC=-0.219 PNL=+10.72€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=691 IC=-0.219 PNL=+10.72€

**〰️ H-CUSTOM-ETH15-REVERSION** — ETH#15min con drift_15min < -1 — ¿mean reversion?
  - _Hipótesis_: ETH y BTC tienen patrones opuestos: BTC funciona con momentum (drift>0.3). ETH funciona con reversión (drift<-1): 9/14 (64%) IC=+0.087. La hipótesis es que ETH tiene más mean-reversion que BTC en 15min.
  - _Umbral_: n≥20 y IC>+0.08
  - _Acción_: Si ETH drift<-1 confirma IC>0.08 con n≥20 → boost ×1.1 en ETH#15min cuando drift_15min<-1
  - _Estado_: n=589 IC=-0.014 PNL=+4.87€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=589 IC=-0.014 PNL=+4.87€

**〰️ H-CUSTOM-GBM-09H** — GBM a las 09h UTC — bloqueada 2026-06-29
  - _Hipótesis_: IC=-0.158 n=19 PNL=-11.62€. Bloqueada manualmente el 2026-06-29 añadiendo hora 9 a meta.gbm_blacklist_hours_auto. Esta hipótesis monitorea que el IC siga siendo negativo para justificar el bloqueo.
  - _Umbral_: n≥25 para confirmar el bloqueo es necesario
  - _Acción_: Si IC sube a >-0.05 con n≥30 → evaluar desbloquear. Si se mantiene <-0.10 → confirmar bloqueo permanente.
  - _Estado_: n=1321 IC=+0.036 PNL=+102.06€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=1321 IC=+0.036 PNL=+102.06€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=169 IC=-0.021 PNL=-4.14€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=169 IC=-0.021 PNL=-4.14€

**〰️ H-FUNDING-HIGH-BUYNO** — Funding rate alto (>p90 real ≈0.009%/8h) → BUY_NO tiene más edge
  - _Hipótesis_: Cuando funding perps Binance está en el decil superior real (>0.009%/8h, ver recalibración 06-Ago), los longs están sobrecargados y pagan por mantener. Hipótesis: BUY_NO GBM tiene IC superior en este régimen vs funding neutral. RECALIBRADO 06-Ago: el umbral original (0.03) era FÍSICAMENTE IMPOSIBLE -- el máximo real observado en 5428 filas de UPDOWN_GBM (feature funding_rate_8h = round(fr*100,5), fr=lastFundingRate crudo de Binance) es 0.01, y nunca lo cruzaba -- n=0 desde que se creó, atrapada sin poder acumular ni una fila. Recalibrado a p90 real (percentiles: p50=0.00368, p75=0.00651, p90=0.00943, p95=p99=p100=0.01 -- el feature satura en 0.01 en el 8.4% de las filas, sin evidencia de que sea un bug de captura, no de que sea funding genuinamente extremo). n=332 BUY_NO ya disponibles con el umbral nuevo (>>umbral_n=40), frente a n=0 con el original.
  - _Umbral_: n≥40 y IC>+0.05 diferencial vs baseline
  - _Acción_: Si IC_funding_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en BUY_NO cuando funding_rate_8h > 0.009
  - _Estado_: n=13746 IC=+0.042 PNL=+729.22€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=13746 IC=+0.042 PNL=+729.22€

**🟡 H-FUNDING-NEGATIVE-BUYYES** — Funding rate negativo (<-0.01%/8h) → BUY_YES tiene más edge (short squeeze)
  - _Hipótesis_: Cuando funding < -0.01%/8h, los shorts están pagando por mantener la posición. Históricamente precede squeezes en cripto. Hipótesis: BUY_YES GBM tiene IC superior en régimen de funding negativo.
  - _Umbral_: n≥30 y IC>+0.05
  - _Acción_: Si se confirma → boost ×1.1 en BUY_YES cuando funding_rate_8h < -0.01
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.108 > 0.08 con n=480 PNL=+92.46€
  - _Datos_: n=480 IC=+0.108 PNL=+92.46€

**🔶 H-LATE-WINDOW-5MIN** — Late-window BTC 5min — arbitraje timing vs Polymarket
  - _Hipótesis_: Inspirado en VyvanseWithMarijuana (36.5% ROI, $42k vol). A T+160-270s dentro de una ventana BTC 5min, si BTC ya se movió >0.3%, Polymarket no ha actualizado precio → edge estructural. Estrategia LATE_WINDOW_5MIN en shadow hasta n≥30. FIX 2026-07-02: la estrategia llevaba 0 predicciones desde su creacion porque HORIZONTE_MIN_HORAS=0.05 (3min) descartaba todo mercado a <3min de expirar — y su zona de entrada (160-270s de una ventana de 5min) deja 30-140s restantes, siempre bajo el suelo. Corregido en shadow_predict (zona late-window marcada _solo_late, 30s-3min, solo evaluada por esta estrategia). El reloj de acumulacion empieza de verdad hoy. Contexto extra: el estudio de ballenas de hoy confirma que comprar el lado ganador a mitad/final de ventana es el playbook comun de los 3 mayores ganadores verificados de estos mercados (Bonereaper +$19.9k/mes, wowitsamazing +$10k/mes, zhangfan151 +$8.7k/mes).
  - _Umbral_: n≥30 y IC>+0.05
  - _Acción_: Si IC≥0.08 con n≥30 → proponer pasar a live con stake mínimo (0.50€). Si IC<0 con n≥30 → el lag de Polymarket en BTC es insuficiente.
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.292 n=234) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=234 IC=+0.292 PNL=+262.43€

**〰️ H-DVOL-SPIKE-BUYNO** — DVOL spike (sigma_h alto) → BUY_NO tiene más edge (panic regime)
  - _Hipótesis_: Inspirado en 'The Volatility Edge' (Concretum Research, 2025): en equities, VIX spikes identifican regímenes de pánico donde los moves están sobreamplificados por feedback loops (deleveraging, hedgers, etc). En cripto el análogo es DVOL (Deribit BTC IV). Sin acceso a DVOL, usamos sigma_h como proxy (vol realizada 1h). Hipótesis: cuando sigma_h > 0.004/h (≈ vol diaria >9.6%), los mercados de predicción exageran la bajada en 15min → BUY_NO tiene IC superior porque el pánico se revierte intraday. Activar cuando n≥200 en BUY_NO #15min para tener potencia suficiente para subdividir por régimen.
  - _Umbral_: n≥200 BUY_NO #15min total, luego n≥40 en subconjunto sigma_h>0.004 y IC>+0.10
  - _Acción_: Si IC_sigma_alto > IC_baseline + 0.08 con n≥40 → boost ×1.2 en BUY_NO cuando sigma_h>0.004. Pendiente integrar DVOL real (Deribit API) cuando n≥500.
  - _Estado_: n=16594 IC=+0.055 PNL=+1496.14€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=16594 IC=+0.055 PNL=+1496.14€

**〰️ H-CUSTOM-POLY-DRIFT-CONFIRM** — poly_drift_5obs: ¿el precio YES interno de Polymarket confirma nuestra señal?
  - _Hipótesis_: Feature nueva 2026-06-27: drift del precio YES en Polymarket en últimas 5 obs (~5min). Si poly_drift<0 y decidimos BUY_NO (o poly_drift>0 y BUY_YES) → confluencia. Si diverge → reducción de stake. Hipótesis: confluencia Binance+Polymarket mejora IC; divergencia empeora.
  - _Umbral_: n≥40 en confluencia vs divergencia para validar el boost ×1.1
  - _Acción_: Si IC_confluencia>IC_divergencia con n≥40 → mantener el boost. Si no → retirar.
  - _Estado_: n=6209 IC=+0.059 PNL=+930.73€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=6209 IC=+0.059 PNL=+930.73€

**🟡 H-CUSTOM-OF-VOLUMEN-ALTO** — ORDER_FLOW_5M con total_vol_5m alto — ¿volumen extremo mejora el IC?
  - _Hipótesis_: Inspirado en un artículo sobre 'volume trading strategy' (mean-reversion en SPY): la idea es que un mismo movimiento de precio con volumen inusualmente alto refleja pánico/liquidación forzada y tiene más probabilidad de revertir que el mismo movimiento con volumen normal. No es transplantable tal cual (esa estrategia opera en barras diarias de SPY, nosotros en ventanas de 15-60min de cripto), pero el feature total_vol_5m ya se captura en cada predicción de ORDER_FLOW_5M (shadow_predict.py) y nunca se ha usado como filtro independiente — solo sirve de denominador para calcular delta_ratio. Hipótesis: dentro de las señales que ya pasan el filtro de delta_ratio, un total_vol_5m alto (volumen real, no solo desequilibrio) mejora el IC. Distribución real en predictions_*.csv (n=843): mediana=1696, p75=108522 (muy asimétrica) — se usa p75 como umbral de 'volumen alto'.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC_volumen_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en ORDER_FLOW_5M cuando total_vol_5m>100000
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.113 > 0.08 con n=704 PNL=+235.52€
  - _Datos_: n=704 IC=+0.113 PNL=+235.52€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-POS** — GBM 15min/60min: spread positivo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Inspirado en un artículo sobre bots de Polymarket: mercados de distinta duración del mismo activo (ej. BTC#15min vs BTC#60min) no repriciician a la misma velocidad — uno puede quedarse rezagado tras un movimiento. Si el spread entre ambos se sale de lo normal, puede indicar que uno de los dos aún no ha incorporado la información que el otro ya tiene. No es transplantable tal cual (el artículo lo usa para arbitraje comprando ambos lados a la vez, algo que no hacemos — ver idea_bidirectional_accumulation aparcada), pero el feature cross_window_spread (precio_yes propio menos precio_yes de la ventana relacionada, sin normalizar aún por z-score) ya se captura para GBM#15min (contra 60min) y GBM#60min (contra 15min) desde el 2026-07-01, sin cambiar ninguna decisión. Esta hipótesis cubre el lado positivo (mercado propio más caro que el relacionado); ver H-CUSTOM-CROSS-WINDOW-SPREAD-NEG para el lado negativo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread, y evaluar si merece la pena normalizar a z-score con más histórico
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.126 > 0.08 con n=1585 PNL=+426.16€
  - _Datos_: n=1585 IC=+0.126 PNL=+426.16€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-NEG** — GBM 15min/60min: spread negativo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Lado negativo de H-CUSTOM-CROSS-WINDOW-SPREAD-POS (mercado propio más barato que el relacionado). Mismo feature cross_window_spread, mismo origen (artículo sobre bots de Polymarket), umbral simétrico.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.090 > 0.08 con n=1278 PNL=+548.14€
  - _Datos_: n=1278 IC=+0.090 PNL=+548.14€

**〰️ H-CUSTOM-MOON-LLENA** — Fase lunar: ¿rendimiento peor cerca de luna llena?
  - _Hipótesis_: Inspirado en el paper de Fornero (2023, 43 Jornadas SADAF) sobre astrología financiera: 5 estudios peer-review (Dichev & Janes 2003, Yuan et al. 2006, Keef & Khaled 2011, Floros & Tan 2013, Liu & Tseng 2009) en 25-62 mercados bursátiles encuentran rendimientos 5-10%/año más bajos cerca de luna llena que de luna nueva. El propio paper es escéptico de la astrología como tal, pero el mecanismo que documenta no es místico: sesgo de humor de inversores minoristas (más fuerte en acciones con dominancia retail, casi nulo en institucional). Polymarket es un mercado muy retail/cripto — hipótesis: si el mecanismo transfiere, debería verse peor IC cerca de luna llena (moon_phase≈0.5) que en el resto del ciclo.
  - _Umbral_: n≥200 PERO ADEMÁS necesita cubrir al menos 3 ciclos lunares completos (~90 días de calendario) — no evaluar solo por n, aunque el volumen diario ya lo cruce en horas
  - _Acción_: Si IC cerca de luna llena < IC resto del ciclo con margen ≥0.05 y ≥3 ciclos lunares cubiertos → considerar boost/filtro por moon_phase. No implementar con menos de 3 ciclos aunque n sea alto — el efecto es de calendario lento, no de volumen.
  - _Estado_: n=94243 IC=+0.125 PNL=+38045.26€ — sin señal clara aún (umbral IC: min=None max=-0.03)
  - _Datos_: n=94243 IC=+0.125 PNL=+38045.26€

**〰️ H-CUSTOM-MERCURY-RETROGRADO** — Mercurio retrógrado: ¿rendimiento peor durante la ventana?
  - _Hipótesis_: Mismo origen que H-CUSTOM-MOON-LLENA (paper de Fornero, 43 Jornadas SADAF 2023). Qi, Wang & Zhang (2022, 48 mercados, 1973-2019): rendimientos 3.33%/año más bajos durante Mercurio retrógrado. Kou & Ma (2022) en China (99.8% cuentas retail): hasta -31% anualizado. Ambos estudios confirman que el mecanismo es la creencia/superstición de inversores retail (mayor efecto cuanto más retail y más supersticioso el mercado), no un efecto astral literal — Polymarket encaja en ese perfil. Ventanas 2026 (fuente pública, actualizar cada año): 26-feb a 20-mar, 29-jun a 23-jul, 24-oct a 13-nov.
  - _Umbral_: n≥100 PERO ADEMÁS necesita cubrir al menos 2-3 ventanas de retrogradación distintas (no solo la de jun-jul 2026) — esperar mínimo hasta después de la ventana de oct-nov 2026
  - _Acción_: Si IC en mercury_retrogrado=1 < IC en mercury_retrogrado=0 con margen ≥0.05 y ≥2 ventanas distintas cubiertas → considerar boost/filtro. No implementar tras una sola ventana (jun-jul 2026) por more que n sea alto — sería solo un evento, no un patrón.
  - _Estado_: n=86130 IC=+0.141 PNL=+39313.49€ — sin señal clara aún (umbral IC: min=None max=-0.03)
  - _Datos_: n=86130 IC=+0.141 PNL=+39313.49€

**〰️ H-CUSTOM-SMART-MONEY-CONSENSUS** — Consenso de wallets 'smart money' — ¿confirma nuestra dirección?
  - _Hipótesis_: Javi propuso estudiar bots/wallets que operan bien en nuestros mismos mercados. En vez de creer artículos (ya verificamos 2 veces esta semana que las narrativas no aguantan el cruce con datos reales), smart_money_tracker.py mide el track record REAL de wallets activas en BTC/ETH/SOL/XRP Up-or-Down 5/15/60min vía data-api.polymarket.com/positions, filtrado a posiciones 'Up or Down'. Clasifica como 'smart' las wallets con n>=10 posiciones, win_rate>=0.55 y pnl_total>0. smart_money_consensus es el sesgo direccional reciente (Up-Down)/(Up+Down) de esas wallets 'smart' por activo. Hipótesis: si nuestra decisión (BUY_YES/BUY_NO) coincide con el consenso smart money, mejor IC que cuando diverge. RESET METODOLOGICO 2026-07-02: la clasificacion 'smart' original via /positions estaba INVERTIDA para wallets de alta frecuencia (el endpoint solo retiene el residuo perdedor sin redimir; verificado: 'wowitsamazing' figuraba como -$478k y es +$10k/mes en el leaderboard oficial). Desde 2026-07-02T06:12Z el consenso se construye solo con wallets verificadas en el leaderboard oficial (pnl_mes>=$1000, 24 wallets). Los valores de smart_money_consensus capturados en features ANTES de esa fecha provienen de la clasificacion rota — descontar ese tramo al evaluar.
  - _Umbral_: n≥40 y IC>+0.08 — además necesita que existan wallets 'smart' acumuladas (0 al empezar, se van descubriendo cada ciclo)
  - _Acción_: Si IC en confluencia (decisión coincide con signo de smart_money_consensus) supera en >=0.05 al IC en divergencia, con n≥40 en cada lado → boost ×1.1-1.2 cuando coincide, considerar reducir stake cuando diverge fuerte.
  - _Estado_: n=15928 IC=+0.062 PNL=+1650.91€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=15928 IC=+0.062 PNL=+1650.91€

**🟡 H-CUSTOM-OF-EDGE-ALTO** — ORDER_FLOW_5M: edge alto (>0.20) rinde mejor que edge cerca del suelo
  - _Hipótesis_: Analizado 2026-07-01 sobre 794 resoluciones de ORDER_FLOW_5M: edge_neto en [0.025,0.198) -> IC=-0.009 (n=397, PNL=-10.49€) vs edge_neto en [0.198,0.385] -> IC=+0.029 (n=397, PNL=+16.43€). Comprobado que NO es un efecto general: en UPDOWN_GBM el patrón se invierte (edge bajo IC=-0.002 vs edge alto IC=-0.033), así que este filtro debe quedar scoped solo a ORDER_FLOW_5M, no aplicarse a otras estrategias. CORREGIDO 2026-07-01 (mismo día, encontrado por auditoría): el filtro original usaba 'edge_neto' con solo feature_lo, pero edge_neto está firmado por dirección (negativo en BUY_NO, positivo en BUY_YES) y ORDER_FLOW_5M solo genera BUY_NO desde 2026-06-25 — el filtro nunca podía matchear ningún BUY_NO real, solo el remanente BUY_YES histórico de antes del 25-jun (n=151, datos muertos, no crecen hacia adelante). Cambiado a 'edge_direccional' (siempre positivo, = abs(edge_neto)) + decision=BUY_NO explícito. Con el fix: n=227, IC=+0.0502, PNL=+19.15€ — señal real y viva.
  - _Umbral_: n≥80 en cada mitad (bajo/alto) para confirmar con más margen que el análisis inicial
  - _Acción_: Si se confirma con n≥80 y el gap se mantiene ≥0.03 → subir EDGE_MINIMO solo para ORDER_FLOW_5M a ~0.20 (o escalar Kelly con la magnitud del edge)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.119 > 0.02 con n=1237 PNL=+499.99€
  - _Datos_: n=1237 IC=+0.119 PNL=+499.99€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=251 IC=-0.117 PNL=+7.41€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=251 IC=-0.117 PNL=+7.41€

**〰️ H-CUSTOM-WEEKLY-INRANGE-BUYYES** — WEEKLY_PRICE BUY_YES con in_range=1 — ¿estructuralmente sobrevalorado?
  - _Hipótesis_: Analizado 2026-07-01, n=10 (evidencia mínima): BUY_YES cuando in_range=1 fue 0/3 (todo pérdida). Mecanismo propuesto: acertar un rango de precio estrecho al vencimiento es intrínsecamente poco probable, el mercado puede estar sobrevalorando el 'sí'. Ver H-CUSTOM-WEEKLY-PCTDIST-BUYNO para el lado complementario (BUY_NO con pct_dist alto).
  - _Umbral_: n≥25 y IC<-0.10 para confirmar (evidencia inicial es de solo 3 ops)
  - _Acción_: Si se confirma con n≥25 → filtro causal in_range==1 + BUY_YES → skip en WEEKLY_PRICE
  - _Estado_: n=81 IC=-0.030 PNL=+3.88€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=81 IC=-0.030 PNL=+3.88€

**🟡 H-CUSTOM-WEEKLY-PCTDIST-BUYNO** — WEEKLY_PRICE BUY_NO con pct_dist alto — cuanto más lejos del rango, más seguro
  - _Hipótesis_: Analizado 2026-07-01, n=10 (evidencia mínima): BUY_NO con pct_dist>=2.09% fue 4/4 victorias (rango 2.09%-23.4%); BUY_NO con pct_dist<8% (pero fuera del corte anterior) tuvo derrotas. Patrón: cuanto más lejos está el spot del rango objetivo al momento de la predicción, más fiable el BUY_NO. Complementa H-CUSTOM-WEEKLY-INRANGE-BUYYES.
  - _Umbral_: n≥25 y IC>+0.10 para confirmar
  - _Acción_: Si se confirma con n≥25 → boost ×1.2 en WEEKLY_PRICE BUY_NO cuando pct_dist≥2
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.451 > 0.1 con n=2074 PNL=+2017.25€
  - _Datos_: n=2074 IC=+0.451 PNL=+2017.25€

**〰️ H-CUSTOM-GBM-BUYYES-GLOBAL-MALO** — UPDOWN_GBM BUY_YES global — ¿estructuralmente peor que BUY_NO en todas las estrategias activas?
  - _Hipótesis_: Analizado 2026-07-01: patrón cross-estrategia consistente en las 4 estrategias activas — BUY_NO gana a BUY_YES sin excepción (UPDOWN_GBM IC=+0.058 n=154 vs -0.046 n=412; ORDER_FLOW_5M +0.053 n=439 vs -0.043 n=355; PRICE_TARGET_GBM +0.011 n=45 vs -0.267 n=28; WEEKLY_PRICE +0.115 n=50 vs -0.315 n=25). Mecanismo propuesto: sesgo retail comprando 'Up'/'YES' en cripto infla el precio de YES por encima de su valor justo en Polymarket — consistente con la sobreconfianza del modelo en probabilidades altas de YES detectada en la calibración Platt (ver idea_calibracion_platt). ORDER_FLOW_5M (solo genera BUY_NO desde 2026-06-25) y WEEKLY_PRICE (H-WEEKLY-BUYNO) ya actúan sobre este mismo patrón; UPDOWN_GBM y PRICE_TARGET_GBM (ver H-CUSTOM-PRICETARGET-BUYYES-MALO) todavía no tienen un tratamiento sistemático equivalente, solo filtros puntuales por hora/subtipo.
  - _Umbral_: n≥50 y IC<-0.05 para confirmar bloqueo global (a día de hoy ya está en n=412, IC=-0.046 — muy cerca)
  - _Acción_: Si se confirma con n≥50 → exigir evidencia direccional más fuerte por subtipo antes de permitir BUY_YES en live (barra asimétrica frente a BUY_NO), en vez de auto-desactivar de golpe todo BUY_YES de GBM
  - _Estado_: n=42418 IC=+0.074 PNL=+5933.28€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=42418 IC=+0.074 PNL=+5933.28€

**🟡 H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: n≥120 y IC>+0.10 (el n=61 del descubrimiento está incluido — exigir ~doble para confirmar forward)
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.198 > 0.1 con n=8739 PNL=+4990.00€
  - _Datos_: n=8739 IC=+0.198 PNL=+4990.00€

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.136 < -0.1 con n=737 PNL=+101.82€
  - _Datos_: n=737 IC=-0.136 PNL=+101.82€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=3938 IC=+0.068 PNL=+506.82€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=3938 IC=+0.068 PNL=+506.82€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=184 IC=-0.102 PNL=-0.48€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=184 IC=-0.102 PNL=-0.48€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.101 > 0.1 con n=1074 PNL=+272.20€
  - _Datos_: n=1074 IC=+0.101 PNL=+272.20€

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
  - _Estado_: n=42267 IC=-0.136 PNL=+2763.11€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=42267 IC=-0.136 PNL=+2763.11€

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
  - _Estado_: n=4365 IC=+0.129 PNL=+2830.28€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=4365 IC=+0.129 PNL=+2830.28€

**🟡 H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: n≥40 forward y IC>+0.08 (barra live estándar)
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.191 > 0.08 con n=5261 PNL=+3642.94€
  - _Datos_: n=5261 IC=+0.191 PNL=+3642.94€

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=10616 IC=+0.059 PNL=+945.15€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=10616 IC=+0.059 PNL=+945.15€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.101 > 0.08 con n=4509 PNL=+2551.18€
  - _Datos_: n=4509 IC=+0.101 PNL=+2551.18€

**🟡 H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: n≥80 (elevado desde el estándar 40, por ser recorte post-hoc) y IC>+0.08 en BTC específicamente
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.202 > 0.08 con n=1029 PNL=+577.45€
  - _Datos_: n=1029 IC=+0.202 PNL=+577.45€

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.219 < -0.1 con n=4610 PNL=-369.12€
  - _Datos_: n=4610 IC=-0.219 PNL=-369.12€

**🟡 H-CUSTOM-GBMLATE-ANCHURA-MERCADO** — GBM_LATE_15M BUY_YES — anchura de mercado (retorno concurrente de los otros 3 majors) como modificador secundario
  - _Hipótesis_: Detectado 2026-07-09 buscando explicar por qué varias pérdidas de la racha=4 comparten ventana de 15min. Con precios reales (05-09jul, ~20k muestras BTC) se calculó el retorno concurrente de los OTROS 3 majors desde el inicio de la ventana hasta el momento exacto de la decisión (sin fuga de datos, nunca el precio de cierre) y se cruzó con resultados reales de GBM_LATE_15M BUY_YES: n=802, magnitud media de los otros 3 en deciles limpios y monótonos (decil1 IC=-0.146 hit 35% → decil6-9 IC≈+0.20/+0.29 hit 70-80%). NO es redundante con drift_ventana_pct propio del par (correlación solo 0.26); controlando por el drift propio, la anchura sigue añadiendo información (dentro de drift propio>=0, que es el 90% de los casos: IC=0.127 si anchura baja vs IC=0.211 si anchura alta). Funciona en espejo para BUY_NO (shadow, n=685, anchura negativa 0/3→3/3: hit 47.4%→70.3%). CAVEAT importante: NO explica los clusters concretos de racha=4 en vivo — 6 de los 8 eventos históricos tienen anchura ALTA en al menos 2 de las 4 pérdidas (ver notas de sesión 09-Jul), y el backtest directo sobre trades.csv real (n=105-116) es inconcluso/contradictorio (gate anchura>=3 empeora el PnL real, -2.11€ vs +32.32€ sin filtro — probablemente confusión por mezcla de pares en una muestra pequeña, SOL domina ese bucket y SOL es el par MENOS sensible a esta señal: IC 0.132→0.143 apenas cambia, vs ETH 0.038→0.192). Tratar como MODIFICADOR del filtro primario H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT, no como filtro independiente — ver esa hipótesis para la tabla cruzada. Feature `mercado_anchura_pct` añadida 2026-07-09 en shadow_predict.py (_s_gbm_late), puro logging, no cambia ninguna decisión — empieza a acumular desde cero en predicciones nuevas. ACTUALIZACIÓN 12-Jul (desagregación por activo, n fresco): BTC n=35 ic=+0.392 z=+4.90, ETH n=32 ic=+0.353 z=+4.24, XRP n=31 ic=+0.288 z=+3.41 -- los 3 MUY fuertes y consistentes. SOL sigue siendo el único débil (n=30 ic=+0.094 z=+1.10), confirma el caveat ya escrito arriba (SOL insensible). Con XRP incluido, el patrón deja de ser '3 activos + SOL raro' para ser una regla casi universal salvo SOL -- candidato fuerte para boost Kelly restringido a BTC/ETH/XRP (excluir SOL explícitamente) en vez de aplicar a las 4 monedas por igual.
  - _Umbral_: n≥100 forward (feature nueva, sin histórico) e IC>+0.20 en la zona alta (mercado_anchura_pct≥0.056, el decil superior observado)
  - _Acción_: Si confirma con n≥100 IC≥0.20 → boost Kelly cuando mercado_anchura_pct≥0.056 Y prob_yes_modelo≥0.53 (la celda 'doble buena', hit 72.7% retrospectivo). No usar como filtro solo — ver CAVEAT de los clusters de racha en la descripción, y el análisis por-par (SOL insensible) antes de aplicar a las 4 monedas por igual.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.220 > 0.2 con n=11353 PNL=+9348.76€
  - _Datos_: n=11353 IC=+0.220 PNL=+9348.76€

**🟡 H-CUSTOM-OF5M-SMARTMONEY-CONTRARIO** — ORDER_FLOW_5M SOL BUY_NO — smart money EN CONTRA del flujo CEX, no a favor, predice mejor
  - _Hipótesis_: Detectado 11-Jul revisando el backlog quant-desk (reencuadre de ORDER_FLOW_5M). ORDER_FLOW_5M solo dispara BUY_NO (presión vendedora en Binance). Split retrospectivo SOL#5min por smart_money_consensus (ya logueado, nunca cruzado con esta estrategia): cuando el consenso on-chain es BAJISTA (smart_money_consensus<0, 'confirma' la señal CEX) el hit cae a 47.1% (ic_bayes=-0.026, n=17); cuando el consenso es ALCISTA/neutro (smart_money_consensus>=0, CONTRARIO a la señal CEX) el hit sube a 65.0% (ic_bayes=+0.136, n=20, pnl/trade+0.294). Contraintuitivo: la 'confirmación' de dos fuentes empeora, la divergencia mejora. Hipótesis mecánica: el flujo de Binance ya captura la información rápida de 5min; smart money on-chain se mueve más lento (posiciones ya tomadas), así que cuando coincide con el flujo CEX puede ser la MISMA información ya vista dos veces sin dar nada nuevo (o incluso momentum ya agotado), mientras que la divergencia indica que el flujo CEX es el que se está moviendo AHORA sobre información fresca que smart money aún no reflejó. Distinto del cierre 08-Jul del consenso poblacional plano (n=2494, ruido puro) — aquello era agregado sobre TODAS las estrategias; esto es específico del mecanismo de ORDER_FLOW_5M. n=17/20 insuficiente para concluir (regla del proyecto n≥15 es el mínimo absoluto, no un veredicto) — vigilar forward.
  - _Umbral_: n≥40 en cada rama (contrario y alineado) para separar señal de ruido
  - _Acción_: Si confirma con n≥40 e ic_bayes contrario≥+0.08 (con alineado claramente peor) → boost Kelly en ORDER_FLOW_5M BUY_NO cuando smart_money_consensus>=0; considerar filtro/veto cuando smart_money_consensus<0 y muy negativo (posible señal 'ya vista', sin ventaja).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.114 > 0.08 con n=151 PNL=+62.62€
  - _Datos_: n=151 IC=+0.114 PNL=+62.62€

**🟡 H-CUSTOM-ETH15-SIGMA-ACCEL** — GBM_LATE_15M ETH — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: sigma_ewma_delta_pct = (sigma_h_ewma10-sigma_h)/sigma_h. Verificado ad-hoc n=47: cuando la vol reciente (EWMA half-life 10min) supera la ventana plana, hit sube de 59.5% (agregado ETH) a 66.0%, ic_bayes=+0.153. Efecto NO uniforme entre activos (ver hermanas BTC/XRP) -- desagregar por activo es obligatorio, el agregado GBM_LATE_15M diluye esto a ruido.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en ETH#15min
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.087 > 0.08 con n=4022 PNL=+1503.10€
  - _Datos_: n=4022 IC=+0.087 PNL=+1503.10€

**🟡 H-CUSTOM-BTC15-SIGMA-ACCEL** — GBM_LATE_15M BTC — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: mismo mecanismo que ETH (ver H-CUSTOM-ETH15-SIGMA-ACCEL). Verificado ad-hoc n=35: hit sube de 63.6% (agregado BTC) a 68.6%, ic_bayes=+0.176.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en BTC#15min
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.171 > 0.08 con n=3918 PNL=+2994.48€
  - _Datos_: n=3918 IC=+0.171 PNL=+2994.48€

**〰️ H-CUSTOM-XRP15-SIGMA-DECEL** — GBM_LATE_15M XRP — vol DESacelerando (EWMA10<=flat) mejora la señal (signo opuesto a ETH/BTC)
  - _Hipótesis_: 12-Jul: XRP muestra el signo CONTRARIO a ETH/BTC -- cuando la vol reciente cae por debajo de la ventana plana, hit sube de 63.9% (agregado XRP) a 68.8%, ic_bayes=+0.180 (n=48). Cuando acelera, hit CAE a 57.1%. Confirma que este feature no puede tratarse con un umbral global -- cada activo necesita su propio signo. REFUTADA 13-Jul: recalculado con n=61 (más del doble del n original) usando el mismo método riguroso (percentiles + permutación 20k) que confirmó BTC/SOL/ETH -- el signo se INVIRTIÓ: decel (sigma<0) da IC=-0.065 n=21 (malo), accel (sigma>=0) da IC=+0.071 n=40 (bueno). XRP en realidad tiene el MISMO signo que BTC/ETH (sigma alto=bueno), solo que más débil -- coherente con el patrón ganador ya auto-descubierto por postmortem (sigma_ewma_delta_pct>5.563, ic_patron=+0.20 n=18, mismo signo). El hallazgo ad-hoc del 12-Jul con n=48 no replicó con más datos -- probable ruido de una muestra menor/distinta. Ver idea_estrategia_mercado_bajista... no, ver project_sigma_filtro_sol_xrp_no_promociona_13jul (memoria) para el detalle completo.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: REFUTADA -- no implementar kelly_boost por sigma<0 en XRP. El signo correcto es el opuesto (sigma alto=bueno), ya cubierto por el patron_ganador automático de postmortem sobre GBM_LATE_15M#XRP#15min -- no hace falta ninguna acción manual adicional.
  - _Estado_: n=6602 IC=-0.020 PNL=+2024.17€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=6602 IC=-0.020 PNL=+2024.17€

**〰️ H-CUSTOM-SMARTMONEY-FAVORITO-SOL** — FAVORITO_CONFIRMADO SOL — alineado con smart_money_consensus bate ir en contra (REABRE hallazgo cerrado 08-Jul)
  - _Hipótesis_: 12-Jul: el cierre 08-Jul (n=2494, sin desagregar por estrategia/activo) encontro ruido puro. Desagregando por estrategia+activo (mecanismo nuevo): FAVORITO_CONFIRMADO#SOL alineado con smart_money_consensus (|consenso|>0.1, n_wallets>=3) hit=78.4% (n=37) vs contrario hit=52.4% (n=42), z=+2.41. GBM_LATE_15M tambien muestra el mismo signo en BTC/ETH/XRP (z=0.86-1.61, mas debil) pero SOL plano ahi -- inconsistencia entre estrategias que hay que entender antes de actuar.
  - _Umbral_: n>=40 por lado y z>=2
  - _Acción_: Si confirma con n>=40 y z>=2 -> considerar boost condicionado a alineacion con smart_money_consensus en FAVORITO_CONFIRMADO#SOL
  - _Estado_: n=741 IC=+0.075 PNL=-23.19€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=741 IC=+0.075 PNL=-23.19€

**🟡 H-CUSTOM-FAVORITO-SOL-ALTACONVICCION** — FAVORITO_CONFIRMADO SOL BUY_YES alta conviccion (py_entrada alto) — UNICO caso positivo en fill-ability de hoy
  - _Hipótesis_: 12-Jul: auditoria de fill-ability de las 8 candidatas encontro las 8 negativas en agregado. Pero desagregando FAVORITO_CONFIRMADO por activo (mecanismo nuevo, no mirado hasta hoy): SOL#BUY_YES con py_entrada>=0.665-0.695 da pnl/trade POSITIVO en el subconjunto fillable real (+0.12 a +0.41 EUR/trade, n=6-17 segun el corte exacto) -- unico resultado positivo de toda la auditoria de candidatas. n todavia bajo, necesita mas dato antes de proponer nada.
  - _Umbral_: n>=40 y pnl/trade fillable > 0 sostenido
  - _Acción_: Seguir acumulando snapshots candidato_evaluacion para SOL#15min#BUY_YES en FAVORITO_CONFIRMADO; re-evaluar fill-ability con n>=40 antes de proponer whitelist
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.241 > 0.08 con n=5687 PNL=-440.51€
  - _Datos_: n=5687 IC=+0.241 PNL=-440.51€

**〰️ H-CUSTOM-GBM18H-XRP-EXCEPCION** — UPDOWN_GBM XRP a las 18h UTC -- puede estar mal incluida en el blacklist horario global
  - _Hipótesis_: 12-Jul: gbm_blacklist_hours_auto=[9,10,18] bloquea GBM en las 4 monedas a las 18h. Desagregando por activo (h9/h10 no tienen dato retrospectivo -- el propio blacklist impide que se genere): BTC ic=-0.140 (n=48), ETH ic=-0.136 (n=42), SOL ic=-0.167 (n=22) consistentes con el bloqueo, pero XRP ic=+0.100 (n=23) -- signo OPUESTO. El bloqueo agregado puede estar sobre-bloqueando XRP especificamente.
  - _Umbral_: n>=40 y IC>0.08
  - _Acción_: Si confirma con n>=40 IC>0.08 -> considerar excepcion de XRP en gbm_blacklist_hours_auto para la hora 18 (shadow puro, UPDOWN_GBM no esta live)
  - _Estado_: n=102 IC=+0.038 PNL=+16.32€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=102 IC=+0.038 PNL=+16.32€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.095 n=2178) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=2178 IC=+0.095 PNL=+436.05€

**🟡 H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: n>=40 y IC>=0.08
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.307 > 0.08 con n=651 PNL=+172.19€
  - _Datos_: n=651 IC=+0.307 PNL=+172.19€

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.413 n=678) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=678 IC=+0.413 PNL=+987.06€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=18157 IC=+0.179 PNL=-2050.61€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=18157 IC=+0.179 PNL=-2050.61€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.232 > 0.1 con n=285 PNL=+199.63€
  - _Datos_: n=285 IC=+0.232 PNL=+199.63€
