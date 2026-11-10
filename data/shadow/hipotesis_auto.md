# Hipótesis automáticas — 2026-11-10 20:22 UTC
_Generado por shadow_postmortem.py sobre 1278658 resoluciones (PNL=+174820.78€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.5` → IC=-0.317 (n=195)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.118 (n=697)

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
- **FILTRO** `restante_s_al_confirmar` < `132.48` → IC=-0.220 (n=11782)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 132.48
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=35352)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `125.14` → IC=-0.259 (n=1200)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 125.14
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=3603)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `116.46` → IC=-0.288 (n=1218)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 116.46
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=3656)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `restante_s_al_confirmar` < `117.22` → IC=-0.163 (n=3221)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 117.22
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=9663)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `151.72` → IC=-0.242 (n=3207)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 151.72
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=9624)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `128.77` → IC=-0.264 (n=2209)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 128.77
  - _Potencial_: sin este filtro IC_bueno=-0.084 (n=6628)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.210 (n=27566)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.104)

- **PATRÓN** `libro_liquidez` > `8325.3306` → IC=+0.159 (n=2318)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 8325.3306 (IC base=+0.104)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.128 (n=23672)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 17.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.130 (n=28704)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.124)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.224 (n=21690)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.140 (n=8265)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `6565.9782` → IC=+0.145 (n=3190)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 6565.9782 (IC base=+0.124)

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
  - _Potencial_: sin este filtro IC_bueno=+0.095 (n=2188)

- **PATRÓN** `py_entrada` > `0.61` → IC=+0.167 (n=601)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` > 0.61 (IC base=+0.076)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.144 (n=1410)

  - _Acción_: Kelly boost +0.72€ cuando `py_entrada` < 0.44 (IC base=+0.083)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.169 (n=4985)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 6.0 (IC base=+0.166)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.171 (n=4438)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 15.0 (IC base=+0.166)

- **PATRÓN** `py_entrada` > `0.77` → IC=+0.375 (n=1722)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.77 (IC base=+0.166)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.210 (n=2379)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.201)

- **PATRÓN** `py_entrada` < `0.275` → IC=+0.330 (n=946)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.275 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.204 (n=2769)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.201)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.142 (n=1348)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 5.0 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.145 (n=1146)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 15.0 (IC base=+0.141)

- **PATRÓN** `py_entrada` > `0.675` → IC=+0.255 (n=434)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.675 (IC base=+0.141)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.144 (n=1090)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.156 (n=155)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.074)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.253 (n=941)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.227)

- **PATRÓN** `py_entrada` > `0.83` → IC=+0.420 (n=1312)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.83 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.146 (n=1416)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 7.0 (IC base=+0.144)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.153 (n=727)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 7.0 (IC base=+0.144)

- **PATRÓN** `py_entrada` < `0.345` → IC=+0.278 (n=717)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.345 (IC base=+0.144)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `py_entrada` > `0.55` → IC=+0.162 (n=460)

  - _Acción_: Kelly boost +0.81€ cuando `py_entrada` > 0.55 (IC base=+0.045)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.146 (n=470)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 17.0 (IC base=+0.122)

- **PATRÓN** `py_entrada` < `0.33` → IC=+0.235 (n=454)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.33 (IC base=+0.122)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `10.0` → IC=-0.297 (n=72)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.232 (n=151)

- **FILTRO** `libro_liquidez` < `9614.35` → IC=-0.263 (n=167)

  - _Acción_: SKIP cuando `libro_liquidez` < 9614.35
  - _Potencial_: sin este filtro IC_bueno=-0.224 (n=56)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.201 (n=23736)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.198 (n=20056)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 15.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.226 (n=9933)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.196)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.338 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.196)

- **PATRÓN** `libro_liquidez` > `4915.142` → IC=+0.338 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4915.142 (IC base=+0.196)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.175 (n=5416)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 5.0 (IC base=+0.171)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.171 (n=5401)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 18.0 (IC base=+0.171)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.181 (n=5414)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` < 0.74 (IC base=+0.171)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.380 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.247 (n=89)

- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=90)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.214 (n=3196)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.211)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.216 (n=2119)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.211)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.253 (n=1590)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.211)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.184 (n=5296)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.179 (n=4495)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 15.0 (IC base=+0.177)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.178 (n=5451)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` < 0.73 (IC base=+0.177)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.185 (n=4143)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` > 0.71 (IC base=+0.177)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.257 (n=4464)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.250)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.251 (n=3779)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.250)

- **PATRÓN** `py_entrada` > `0.8` → IC=+0.366 (n=1426)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.190 (n=5201)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.186)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.190 (n=4409)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 15.0 (IC base=+0.186)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.192 (n=3865)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.71 (IC base=+0.186)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.429 (n=957)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.425)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.427 (n=953)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.425)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.438 (n=967)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.425)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.431 (n=1017)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.425)

- **PATRÓN** `libro_liquidez` > `4600.3711` → IC=+0.443 (n=616)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4600.3711 (IC base=+0.425)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.438 (n=387)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.439)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.447 (n=263)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.439)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.449 (n=425)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.439)

- **PATRÓN** `libro_liquidez` > `12430.0394` → IC=+0.444 (n=340)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12430.0394 (IC base=+0.439)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.432 (n=378)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.424)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.425 (n=343)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.424)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.435 (n=382)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.424)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.430 (n=425)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.424)

- **PATRÓN** `libro_liquidez` > `4774.0338` → IC=+0.429 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4774.0338 (IC base=+0.424)

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

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.205 (n=31076)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.240 (n=31396)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.200)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.188 (n=4633)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 18.0 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.180 (n=9934)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 12.0 (IC base=+0.179)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.190 (n=14253)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.71 (IC base=+0.179)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.226 (n=13017)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.225)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.287 (n=4412)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.225)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.182 (n=13050)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 7.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.197 (n=11033)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` > 0.72 (IC base=+0.180)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.835` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.835
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.228 (n=4349)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.219)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.222 (n=4970)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.219)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.254 (n=7230)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.219)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **FILTRO** `hora_utc` > `3.0` → IC=-0.278 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.206 (n=11857)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.257 (n=4537)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.202 (n=5165)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.199 (n=5138)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 6.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.245 (n=5389)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.196)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.194 (n=11184)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.140 (n=11715)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `3.45` → IC=+0.139 (n=13613)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 3.45 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.195 (n=5451)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.144 (n=5282)

  - _Acción_: Kelly boost +0.72€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.126 (n=6822)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 7.0 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `2.59` → IC=+0.143 (n=5139)

  - _Acción_: Kelly boost +0.72€ cuando `lag_apertura_s` < 2.59 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.192 (n=5733)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.138 (n=7150)

  - _Acción_: Kelly boost +0.69€ cuando `restante_min` > 4.95 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `3.14` → IC=+0.138 (n=6839)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 3.14 (IC base=+0.117)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.307 (n=1380)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.292)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.387 (n=708)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.292)

- **PATRÓN** `libro_liquidez` > `3962.0865` → IC=+0.293 (n=873)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3962.0865 (IC base=+0.292)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.286 (n=926)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.281)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.364 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.281)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.318 (n=669)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.296)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.300 (n=978)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.296)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.396 (n=334)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.443 (n=938)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.438)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.444 (n=906)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.438)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.436 (n=439)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.431)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.435 (n=305)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.431)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.440 (n=333)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.431)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.460 (n=148)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.445)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.445 (n=381)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.445)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.447 (n=416)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.445)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.444 (n=357)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.445)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4787` → IC=+0.140 (n=17561)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.4787 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.127 (n=17772)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 6.0 (IC base=+0.123)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.127 (n=12218)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 12.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` > `0.9776` → IC=+0.246 (n=5855)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9776 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` > `0.7995` → IC=+0.283 (n=967)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7995 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.492` → IC=+0.185 (n=8781)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 3.492 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` > `0.6249` → IC=+0.266 (n=5249)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6249 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` > `0.3046` → IC=+0.250 (n=1815)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3046 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` > `2.7521` → IC=+0.235 (n=4207)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7521 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.135 (n=8711)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.123)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.122 (n=10966)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0062 (IC base=+0.083)

- **PATRÓN** `ibs_20min` < `0.5652` → IC=+0.144 (n=21943)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.5652 (IC base=+0.083)

- **PATRÓN** `dist_vwap_pct` > `0.6181` → IC=+0.191 (n=1443)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.6181 (IC base=+0.083)

- **PATRÓN** `volumen_regimen` < `0.8608` → IC=+0.195 (n=5975)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` < 0.8608 (IC base=+0.083)

- **PATRÓN** `volumen_pendiente_norm` > `0.2967` → IC=+0.233 (n=2202)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2967 (IC base=+0.083)

- **PATRÓN** `volumen_spike_ratio` > `2.6769` → IC=+0.211 (n=5068)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6769 (IC base=+0.083)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.229 (n=15128)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 100.0 (IC base=+0.083)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `drift_60min` |x|≤ `0.3654` → IC=+0.213 (n=3745)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3654 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.226 (n=1822)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.212)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.212 (n=2508)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` > `0.9869` → IC=+0.278 (n=1697)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9869 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.469` → IC=+0.279 (n=1664)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.469 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` > `0.2339` → IC=+0.257 (n=664)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2339 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `1.4363` → IC=+0.214 (n=3588)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4363 (IC base=+0.212)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.225 (n=4124)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.212)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.225 (n=2343)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.212)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.244 (n=3290)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0103 (IC base=+0.244)

- **PATRÓN** `sigma_h` > `0.0092` → IC=+0.246 (n=1492)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0092 (IC base=+0.244)

- **PATRÓN** `drift_60min` |x|≤ `0.0892` → IC=+0.281 (n=1097)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0892 (IC base=+0.244)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.251 (n=1229)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.244)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.247 (n=1512)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.244)

- **PATRÓN** `ibs_20min` < `0.564` → IC=+0.260 (n=3290)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.564 (IC base=+0.244)

- **PATRÓN** `volumen_pendiente_norm` < `0.0952` → IC=+0.247 (n=2980)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0952 (IC base=+0.244)

- **PATRÓN** `volumen_pendiente_norm` > `0.2904` → IC=+0.252 (n=442)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2904 (IC base=+0.244)

- **PATRÓN** `volumen_spike_ratio` < `1.447` → IC=+0.247 (n=1046)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.447 (IC base=+0.244)

- **PATRÓN** `volumen_spike_ratio` > `1.8601` → IC=+0.247 (n=2091)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8601 (IC base=+0.244)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.246 (n=3781)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.244)

- **PATRÓN** `libro_liquidez` > `1776.2196` → IC=+0.249 (n=2192)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1776.2196 (IC base=+0.244)

- **PATRÓN** `ballena_activa_n` < `6.0` → IC=+0.246 (n=1103)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 6.0 (IC base=+0.244)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.235 (n=1049)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.225)

- **PATRÓN** `drift_60min` |x|≤ `0.1096` → IC=+0.257 (n=1382)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1096 (IC base=+0.225)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.236 (n=3293)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.229 (n=2227)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.225)

- **PATRÓN** `ibs_20min` > `0.9054` → IC=+0.256 (n=1047)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9054 (IC base=+0.225)

- **PATRÓN** `dist_vwap_pct` > `0.1857` → IC=+0.235 (n=1424)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1857 (IC base=+0.225)

- **PATRÓN** `dist_vwap_pct` < `0.3338` → IC=+0.226 (n=3123)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3338 (IC base=+0.225)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.849` → IC=+0.264 (n=460)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.849 (IC base=+0.225)

- **PATRÓN** `volumen_regimen` > `0.6287` → IC=+0.231 (n=3141)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6287 (IC base=+0.225)

- **PATRÓN** `volumen_pendiente_norm` > `0.2788` → IC=+0.269 (n=440)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2788 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` > `2.4455` → IC=+0.252 (n=1034)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4455 (IC base=+0.225)

- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.152 (n=3361)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0064 (IC base=+0.129)

- **PATRÓN** `drift_60min` |x|≤ `0.0775` → IC=+0.153 (n=1123)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.0775 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.152 (n=1255)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 17.0 (IC base=+0.129)

- **PATRÓN** `ibs_20min` < `0.3527` → IC=+0.201 (n=2241)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3527 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.62` → IC=+0.130 (n=544)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` > 10.62 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.981` → IC=+0.137 (n=3071)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 3.981 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` < `1.1954` → IC=+0.137 (n=3361)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 1.1954 (IC base=+0.129)

- **PATRÓN** `volumen_pendiente_norm` > `0.0717` → IC=+0.157 (n=1372)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` > 0.0717 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` < `2.4421` → IC=+0.140 (n=3234)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 2.4421 (IC base=+0.129)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.130 (n=4364)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.01 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `176.0` → IC=+0.181 (n=1060)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 176.0 (IC base=+0.129)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0114` → IC=+0.214 (n=1801)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0114 (IC base=+0.196)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.204 (n=4163)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.196)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.261 (n=1541)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.196)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.981` → IC=+0.280 (n=869)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.981 (IC base=+0.196)

- **PATRÓN** `volumen_pendiente_norm` < `0.0976` → IC=+0.198 (n=3549)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` < 0.0976 (IC base=+0.196)

- **PATRÓN** `volumen_pendiente_norm` > `0.3525` → IC=+0.226 (n=513)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3525 (IC base=+0.196)

- **PATRÓN** `volumen_spike_ratio` > `2.7298` → IC=+0.214 (n=1755)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7298 (IC base=+0.196)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.201 (n=4787)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.196)

- **PATRÓN** `libro_liquidez` > `1912.1779` → IC=+0.204 (n=1797)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1912.1779 (IC base=+0.196)

- **PATRÓN** `sigma_h` < `0.0111` → IC=+0.225 (n=3218)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0111 (IC base=+0.221)

- **PATRÓN** `drift_60min` |x|≤ `0.2926` → IC=+0.234 (n=2437)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2926 (IC base=+0.221)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.243 (n=1388)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.221)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.224 (n=1655)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.221)

- **PATRÓN** `ibs_20min` < `0.0458` → IC=+0.267 (n=1219)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0458 (IC base=+0.221)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.832` → IC=+0.269 (n=396)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.832 (IC base=+0.221)

- **PATRÓN** `volumen_pendiente_norm` > `0.3488` → IC=+0.257 (n=529)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3488 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` < `1.7683` → IC=+0.219 (n=1547)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7683 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` > `2.1594` → IC=+0.230 (n=2343)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1594 (IC base=+0.221)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.225 (n=1850)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.221)

- **PATRÓN** `libro_liquidez` > `1897.5376` → IC=+0.226 (n=1657)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1897.5376 (IC base=+0.221)

- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.224 (n=3506)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 25.0 (IC base=+0.221)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.171 (n=208)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=4765)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.150 (n=659)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0039 (IC base=+0.059)

- **PATRÓN** `ibs_20min` > `0.9428` → IC=+0.233 (n=658)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9428 (IC base=+0.059)

- **PATRÓN** `dist_vwap_pct` > `0.14` → IC=+0.339 (n=457)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.14 (IC base=+0.059)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.086` → IC=+0.201 (n=1441)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.086 (IC base=+0.059)

- **PATRÓN** `volumen_regimen` > `1.0993` → IC=+0.349 (n=355)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0993 (IC base=+0.059)

- **PATRÓN** `volumen_pendiente_norm` < `0.1678` → IC=+0.337 (n=634)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1678 (IC base=+0.059)

- **PATRÓN** `volumen_pendiente_norm` > `0.3054` → IC=+0.333 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3054 (IC base=+0.059)

- **PATRÓN** `volumen_spike_ratio` < `1.421` → IC=+0.348 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.421 (IC base=+0.059)

- **PATRÓN** `volumen_spike_ratio` > `2.2842` → IC=+0.336 (n=346)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2842 (IC base=+0.059)

- **PATRÓN** `ballena_activa_n` < `142.0` → IC=+0.338 (n=774)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 142.0 (IC base=+0.059)

- **PATRÓN** `ibs_20min` < `0.0884` → IC=+0.191 (n=1245)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.0884 (IC base=+0.053)

- **PATRÓN** `dist_vwap_pct` > `0.3354` → IC=+0.163 (n=601)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.3354 (IC base=+0.053)

- **PATRÓN** `dist_vwap_pct` < `0.1387` → IC=+0.155 (n=2247)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.1387 (IC base=+0.053)

- **PATRÓN** `volumen_regimen` < `1.0049` → IC=+0.160 (n=2089)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.0049 (IC base=+0.053)

- **PATRÓN** `volumen_pendiente_norm` > `0.2812` → IC=+0.213 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2812 (IC base=+0.053)

- **PATRÓN** `volumen_spike_ratio` < `1.7716` → IC=+0.157 (n=1523)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.7716 (IC base=+0.053)

- **PATRÓN** `volumen_spike_ratio` > `1.5111` → IC=+0.158 (n=2040)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.5111 (IC base=+0.053)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.183 (n=143)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=760)

- **FILTRO** `ibs_20min` < `0.2609` → IC=-0.174 (n=225)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2609
  - _Potencial_: sin este filtro IC_bueno=+0.079 (n=678)

- **FILTRO** `ibs_20min` > `0.2` → IC=-0.132 (n=4688)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2
  - _Potencial_: sin este filtro IC_bueno=+0.154 (n=2320)

- **FILTRO** `sigma_ewma_delta_pct` > `8.287` → IC=-0.226 (n=752)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.287
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=6256)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.178 (n=309)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.75 (IC base=+0.016)

- **PATRÓN** `dist_vwap_pct` > `0.9668` → IC=+0.275 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9668 (IC base=+0.016)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.917` → IC=+0.159 (n=212)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 4.917 (IC base=+0.016)

- **PATRÓN** `volumen_regimen` > `0.6233` → IC=+0.287 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6233 (IC base=+0.016)

- **PATRÓN** `volumen_pendiente_norm` < `0.0791` → IC=+0.279 (n=269)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0791 (IC base=+0.016)

- **PATRÓN** `volumen_spike_ratio` < `2.1915` → IC=+0.284 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1915 (IC base=+0.016)

- **PATRÓN** `volumen_spike_ratio` > `1.449` → IC=+0.266 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.449 (IC base=+0.016)

- **PATRÓN** `ballena_activa_n` < `41.0` → IC=+0.270 (n=276)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 41.0 (IC base=+0.016)

- **PATRÓN** `ibs_20min` < `0.2` → IC=+0.154 (n=2320)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.2 (IC base=-0.037)

- **PATRÓN** `dist_vwap_pct` > `0.2227` → IC=+0.288 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2227 (IC base=-0.037)

- **PATRÓN** `dist_vwap_pct` < `0.3063` → IC=+0.280 (n=1108)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3063 (IC base=-0.037)

- **PATRÓN** `volumen_regimen` < `0.704` → IC=+0.303 (n=454)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.704 (IC base=-0.037)

- **PATRÓN** `volumen_pendiente_norm` > `0.0797` → IC=+0.305 (n=465)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0797 (IC base=-0.037)

- **PATRÓN** `volumen_spike_ratio` < `2.456` → IC=+0.300 (n=963)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.456 (IC base=-0.037)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `ibs_20min` < `0.7838` → IC=-0.155 (n=3574)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7838
  - _Potencial_: sin este filtro IC_bueno=+0.129 (n=1844)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.171 (n=1172)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=4246)

- **FILTRO** `ibs_20min` > `0.74` → IC=-0.194 (n=1869)

  - _Acción_: SKIP cuando `ibs_20min` > 0.74
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=5640)

- **PATRÓN** `ibs_20min` > `0.7838` → IC=+0.129 (n=1844)

  - _Acción_: Kelly boost +0.64€ cuando `ibs_20min` > 0.7838 (IC base=-0.059)

- **PATRÓN** `dist_vwap_pct` > `1.0308` → IC=+0.359 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0308 (IC base=-0.059)

- **PATRÓN** `volumen_regimen` > `0.7043` → IC=+0.317 (n=939)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7043 (IC base=-0.059)

- **PATRÓN** `volumen_pendiente_norm` > `0.1712` → IC=+0.303 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1712 (IC base=-0.059)

- **PATRÓN** `volumen_spike_ratio` < `1.5808` → IC=+0.306 (n=452)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5808 (IC base=-0.059)

- **PATRÓN** `volumen_spike_ratio` > `2.5248` → IC=+0.317 (n=343)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5248 (IC base=-0.059)

- **PATRÓN** `dist_vwap_pct` > `0.817` → IC=+0.278 (n=358)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.817 (IC base=+0.003)

- **PATRÓN** `volumen_regimen` < `0.7204` → IC=+0.273 (n=967)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7204 (IC base=+0.003)

- **PATRÓN** `volumen_regimen` > `1.0661` → IC=+0.286 (n=996)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0661 (IC base=+0.003)

- **PATRÓN** `volumen_pendiente_norm` > `0.2335` → IC=+0.284 (n=397)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2335 (IC base=+0.003)

- **PATRÓN** `volumen_spike_ratio` < `2.1777` → IC=+0.265 (n=1822)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1777 (IC base=+0.003)

- **PATRÓN** `volumen_spike_ratio` > `1.4419` → IC=+0.269 (n=2070)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4419 (IC base=+0.003)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.197 (n=7598)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` > 0.0107 (IC base=+0.088)

- **PATRÓN** `ibs_20min` > `0.9697` → IC=+0.312 (n=7605)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9697 (IC base=+0.088)

- **PATRÓN** `dist_vwap_pct` > `0.9396` → IC=+0.301 (n=1593)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9396 (IC base=+0.088)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.477` → IC=+0.168 (n=10210)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 3.477 (IC base=+0.088)

- **PATRÓN** `volumen_regimen` > `0.6927` → IC=+0.278 (n=7489)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6927 (IC base=+0.088)

- **PATRÓN** `volumen_pendiente_norm` > `0.2942` → IC=+0.294 (n=1898)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2942 (IC base=+0.088)

- **PATRÓN** `volumen_spike_ratio` > `2.6527` → IC=+0.287 (n=4407)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6527 (IC base=+0.088)

- **PATRÓN** `ballena_activa_n` < `90.0` → IC=+0.309 (n=12858)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 90.0 (IC base=+0.088)

- **PATRÓN** `sigma_h` > `0.0102` → IC=+0.157 (n=7331)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0102 (IC base=+0.082)

- **PATRÓN** `ibs_20min` < `0.64` → IC=+0.155 (n=21983)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.64 (IC base=+0.082)

- **PATRÓN** `volumen_regimen` < `0.6989` → IC=+0.281 (n=3199)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6989 (IC base=+0.082)

- **PATRÓN** `volumen_regimen` > `1.1879` → IC=+0.280 (n=2424)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1879 (IC base=+0.082)

- **PATRÓN** `volumen_pendiente_norm` > `0.2946` → IC=+0.328 (n=1618)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2946 (IC base=+0.082)

- **PATRÓN** `volumen_spike_ratio` < `1.5755` → IC=+0.305 (n=4716)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5755 (IC base=+0.082)

- **PATRÓN** `volumen_spike_ratio` > `2.2808` → IC=+0.302 (n=4858)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2808 (IC base=+0.082)

- **PATRÓN** `ballena_activa_n` < `72.0` → IC=+0.311 (n=10681)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 72.0 (IC base=+0.082)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.8022` → IC=-0.131 (n=4050)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8022
  - _Potencial_: sin este filtro IC_bueno=+0.300 (n=2087)

- **FILTRO** `ibs_20min` > `0.7176` → IC=-0.235 (n=1348)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7176
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=4050)

- **FILTRO** `sigma_ewma_delta_pct` > `4.093` → IC=-0.234 (n=1168)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.093
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=4230)

- **PATRÓN** `ibs_20min` > `0.8022` → IC=+0.300 (n=2087)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8022 (IC base=+0.016)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.964` → IC=+0.190 (n=2051)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 2.964 (IC base=+0.016)

- **PATRÓN** `volumen_pendiente_norm` > `0.2295` → IC=+0.329 (n=395)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2295 (IC base=+0.016)

- **PATRÓN** `volumen_spike_ratio` < `1.4491` → IC=+0.279 (n=653)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4491 (IC base=+0.016)

- **PATRÓN** `volumen_spike_ratio` > `2.2427` → IC=+0.304 (n=888)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2427 (IC base=+0.016)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.303 (n=1952)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 27.0 (IC base=+0.016)

- **PATRÓN** `ibs_20min` < `0.1743` → IC=+0.166 (n=1350)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.1743 (IC base=-0.023)

- **PATRÓN** `volumen_pendiente_norm` < `0.1519` → IC=+0.405 (n=1035)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1519 (IC base=-0.023)

- **PATRÓN** `volumen_spike_ratio` < `1.4203` → IC=+0.426 (n=334)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4203 (IC base=-0.023)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.402 (n=1038)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 23.0 (IC base=-0.023)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.1694` → IC=+0.225 (n=980)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1694 (IC base=+0.011)

- **PATRÓN** `volumen_regimen` < `1.195` → IC=+0.211 (n=2231)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.195 (IC base=+0.011)

- **PATRÓN** `volumen_regimen` > `0.6955` → IC=+0.217 (n=1994)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6955 (IC base=+0.011)

- **PATRÓN** `volumen_pendiente_norm` > `0.2774` → IC=+0.247 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2774 (IC base=+0.011)

- **PATRÓN** `volumen_spike_ratio` < `1.4174` → IC=+0.229 (n=735)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4174 (IC base=+0.011)

- **PATRÓN** `ballena_activa_n` < `261.0` → IC=+0.247 (n=1467)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 261.0 (IC base=+0.011)

- **PATRÓN** `volumen_regimen` > `0.6194` → IC=+0.254 (n=1558)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6194 (IC base=-0.004)

- **PATRÓN** `volumen_pendiente_norm` > `0.2697` → IC=+0.312 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2697 (IC base=-0.004)

- **PATRÓN** `volumen_spike_ratio` < `1.5262` → IC=+0.261 (n=662)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5262 (IC base=-0.004)

- **PATRÓN** `volumen_spike_ratio` > `2.1503` → IC=+0.264 (n=683)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1503 (IC base=-0.004)

- **PATRÓN** `ballena_activa_n` < `187.0` → IC=+0.274 (n=512)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 187.0 (IC base=-0.004)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.322 (n=2135)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0094 (IC base=+0.284)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.293 (n=3198)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.284)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.324 (n=1740)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.284)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.582` → IC=+0.305 (n=2144)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.582 (IC base=+0.284)

- **PATRÓN** `volumen_pendiente_norm` < `0.0979` → IC=+0.296 (n=2806)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0979 (IC base=+0.284)

- **PATRÓN** `volumen_spike_ratio` > `1.6099` → IC=+0.290 (n=3105)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6099 (IC base=+0.284)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.293 (n=3830)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.284)

- **PATRÓN** `libro_liquidez` > `2020.3434` → IC=+0.294 (n=1066)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2020.3434 (IC base=+0.284)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.309 (n=1979)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.284)

- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.332 (n=1930)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0089 (IC base=+0.308)

- **PATRÓN** `drift_60min` |x|≤ `0.1771` → IC=+0.327 (n=1276)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1771 (IC base=+0.308)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.328 (n=1114)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.308)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.309 (n=1305)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.308)

- **PATRÓN** `ibs_20min` > `0.1439` → IC=+0.319 (n=1930)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1439 (IC base=+0.308)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.151` → IC=+0.311 (n=347)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.151 (IC base=+0.308)

- **PATRÓN** `volumen_pendiente_norm` < `0.2004` → IC=+0.308 (n=2844)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2004 (IC base=+0.308)

- **PATRÓN** `volumen_pendiente_norm` > `0.3455` → IC=+0.315 (n=468)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3455 (IC base=+0.308)

- **PATRÓN** `volumen_spike_ratio` < `1.5947` → IC=+0.307 (n=931)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5947 (IC base=+0.308)

- **PATRÓN** `volumen_spike_ratio` > `2.7396` → IC=+0.323 (n=1266)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7396 (IC base=+0.308)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.309 (n=1470)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.308)

- **PATRÓN** `libro_liquidez` > `1902.41` → IC=+0.312 (n=1313)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1902.41 (IC base=+0.308)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.314 (n=2449)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 23.0 (IC base=+0.308)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7236` → IC=-0.180 (n=1434)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7236
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=4305)

- **PATRÓN** `ibs_20min` > `0.8465` → IC=+0.154 (n=1411)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` > 0.8465 (IC base=+0.021)

- **PATRÓN** `dist_vwap_pct` > `0.1437` → IC=+0.236 (n=1041)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1437 (IC base=+0.021)

- **PATRÓN** `volumen_regimen` < `1.1635` → IC=+0.235 (n=2036)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1635 (IC base=+0.021)

- **PATRÓN** `volumen_regimen` > `0.6733` → IC=+0.232 (n=1819)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6733 (IC base=+0.021)

- **PATRÓN** `volumen_pendiente_norm` < `0.1632` → IC=+0.236 (n=2139)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1632 (IC base=+0.021)

- **PATRÓN** `volumen_pendiente_norm` > `0.1031` → IC=+0.244 (n=665)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1031 (IC base=+0.021)

- **PATRÓN** `volumen_spike_ratio` < `2.4504` → IC=+0.240 (n=1975)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4504 (IC base=+0.021)

- **PATRÓN** `ballena_activa_n` < `114.0` → IC=+0.255 (n=2013)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 114.0 (IC base=+0.021)

- **PATRÓN** `ibs_20min` < `0.0918` → IC=+0.157 (n=1436)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.0918 (IC base=+0.006)

- **PATRÓN** `dist_vwap_pct` > `0.7333` → IC=+0.255 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7333 (IC base=+0.006)

- **PATRÓN** `dist_vwap_pct` < `0.1543` → IC=+0.257 (n=1465)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1543 (IC base=+0.006)

- **PATRÓN** `volumen_regimen` < `1.1877` → IC=+0.261 (n=1469)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1877 (IC base=+0.006)

- **PATRÓN** `volumen_pendiente_norm` > `0.2815` → IC=+0.315 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2815 (IC base=+0.006)

- **PATRÓN** `volumen_spike_ratio` < `1.787` → IC=+0.292 (n=940)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.787 (IC base=+0.006)

- **PATRÓN** `volumen_spike_ratio` > `2.4311` → IC=+0.278 (n=470)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4311 (IC base=+0.006)

- **PATRÓN** `ballena_activa_n` < `97.0` → IC=+0.288 (n=1257)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 97.0 (IC base=+0.006)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7407` → IC=-0.249 (n=2353)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7407
  - _Potencial_: sin este filtro IC_bueno=+0.311 (n=2357)

- **FILTRO** `ibs_20min` > `0.62` → IC=-0.234 (n=1116)

  - _Acción_: SKIP cuando `ibs_20min` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.151 (n=3350)

- **FILTRO** `sigma_ewma_delta_pct` > `8.256` → IC=-0.254 (n=510)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.256
  - _Potencial_: sin este filtro IC_bueno=+0.095 (n=3956)

- **PATRÓN** `ibs_20min` > `0.7407` → IC=+0.311 (n=2357)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7407 (IC base=+0.032)

- **PATRÓN** `dist_vwap_pct` > `1.0425` → IC=+0.357 (n=340)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0425 (IC base=+0.032)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.439` → IC=+0.153 (n=1911)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 2.439 (IC base=+0.032)

- **PATRÓN** `volumen_regimen` < `0.8444` → IC=+0.343 (n=1142)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8444 (IC base=+0.032)

- **PATRÓN** `volumen_regimen` > `0.696` → IC=+0.334 (n=1530)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.696 (IC base=+0.032)

- **PATRÓN** `volumen_pendiente_norm` < `0.155` → IC=+0.335 (n=1768)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.155 (IC base=+0.032)

- **PATRÓN** `volumen_pendiente_norm` > `0.274` → IC=+0.360 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.274 (IC base=+0.032)

- **PATRÓN** `volumen_spike_ratio` < `1.4223` → IC=+0.358 (n=555)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4223 (IC base=+0.032)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.354 (n=1473)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=+0.032)

- **PATRÓN** `ibs_20min` < `0.62` → IC=+0.151 (n=3350)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.62 (IC base=+0.055)

- **PATRÓN** `dist_vwap_pct` < `0.3066` → IC=+0.261 (n=1727)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3066 (IC base=+0.055)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.014` → IC=+0.129 (n=3149)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` < 3.014 (IC base=+0.055)

- **PATRÓN** `volumen_regimen` < `0.6945` → IC=+0.279 (n=737)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6945 (IC base=+0.055)

- **PATRÓN** `volumen_pendiente_norm` > `0.071` → IC=+0.289 (n=672)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.071 (IC base=+0.055)

- **PATRÓN** `volumen_spike_ratio` < `1.8024` → IC=+0.278 (n=1081)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8024 (IC base=+0.055)

- **PATRÓN** `ballena_activa_n` < `39.0` → IC=+0.278 (n=1468)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 39.0 (IC base=+0.055)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0159` → IC=+0.358 (n=1603)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0159 (IC base=+0.316)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.319 (n=2431)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.316)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.318 (n=1142)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.316)

- **PATRÓN** `ibs_20min` > `0.661` → IC=+0.345 (n=2404)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.661 (IC base=+0.316)

- **PATRÓN** `dist_vwap_pct` > `0.2129` → IC=+0.340 (n=1294)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2129 (IC base=+0.316)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.798` → IC=+0.333 (n=1168)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.798 (IC base=+0.316)

- **PATRÓN** `volumen_regimen` > `0.8673` → IC=+0.337 (n=1603)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8673 (IC base=+0.316)

- **PATRÓN** `volumen_pendiente_norm` > `0.2804` → IC=+0.348 (n=353)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2804 (IC base=+0.316)

- **PATRÓN** `volumen_spike_ratio` > `1.4314` → IC=+0.328 (n=2317)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4314 (IC base=+0.316)

- **PATRÓN** `libro_liquidez` > `2988.0754` → IC=+0.326 (n=802)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2988.0754 (IC base=+0.316)

- **PATRÓN** `ballena_activa_n` < `33.0` → IC=+0.345 (n=1879)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 33.0 (IC base=+0.316)

- **PATRÓN** `sigma_h` > `0.0152` → IC=+0.349 (n=1716)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0152 (IC base=+0.316)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.322 (n=1307)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.316)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.317 (n=1239)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.316)

- **PATRÓN** `ibs_20min` < `0.3806` → IC=+0.334 (n=2571)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3806 (IC base=+0.316)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.624` → IC=+0.329 (n=950)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.624 (IC base=+0.316)

- **PATRÓN** `volumen_regimen` < `0.7189` → IC=+0.323 (n=1132)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7189 (IC base=+0.316)

- **PATRÓN** `volumen_regimen` > `1.2104` → IC=+0.344 (n=857)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2104 (IC base=+0.316)

- **PATRÓN** `volumen_pendiente_norm` > `0.2306` → IC=+0.364 (n=485)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2306 (IC base=+0.316)

- **PATRÓN** `volumen_spike_ratio` < `1.4127` → IC=+0.325 (n=797)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4127 (IC base=+0.316)

- **PATRÓN** `volumen_spike_ratio` > `2.1399` → IC=+0.316 (n=1083)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1399 (IC base=+0.316)

- **PATRÓN** `libro_liquidez` > `2969.0068` → IC=+0.316 (n=857)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2969.0068 (IC base=+0.316)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.224 (n=5662)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0125 (IC base=+0.173)

- **PATRÓN** `drift_60min` |x|≤ `0.1223` → IC=+0.191 (n=7468)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.1223 (IC base=+0.173)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.183 (n=17596)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 5.0 (IC base=+0.173)

- **PATRÓN** `ibs_20min` > `0.5377` → IC=+0.230 (n=16962)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5377 (IC base=+0.173)

- **PATRÓN** `dist_vwap_pct` > `0.1624` → IC=+0.205 (n=6442)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1624 (IC base=+0.173)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.784` → IC=+0.257 (n=3304)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.784 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` < `1.1803` → IC=+0.152 (n=11296)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.1803 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` > `0.6255` → IC=+0.152 (n=11296)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.6255 (IC base=+0.173)

- **PATRÓN** `volumen_pendiente_norm` > `0.2941` → IC=+0.203 (n=2466)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2941 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` > `2.6076` → IC=+0.187 (n=5500)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.6076 (IC base=+0.173)

- **PATRÓN** `ballena_activa_n` < `87.0` → IC=+0.192 (n=15877)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 87.0 (IC base=+0.173)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.192 (n=7339)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0058 (IC base=+0.183)

- **PATRÓN** `drift_60min` |x|≤ `0.2085` → IC=+0.209 (n=11122)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2085 (IC base=+0.183)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.211 (n=6287)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.183)

- **PATRÓN** `ibs_20min` < `0.5263` → IC=+0.239 (n=16683)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5263 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.533` → IC=+0.193 (n=2660)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 9.533 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.513` → IC=+0.190 (n=14847)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` < 2.513 (IC base=+0.183)

- **PATRÓN** `volumen_regimen` < `1.1819` → IC=+0.164 (n=11874)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.1819 (IC base=+0.183)

- **PATRÓN** `volumen_pendiente_norm` > `0.294` → IC=+0.220 (n=2498)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.294 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` < `1.5597` → IC=+0.183 (n=6984)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 1.5597 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` > `2.6319` → IC=+0.193 (n=5291)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.6319 (IC base=+0.183)

- **PATRÓN** `ballena_activa_n` < `91.0` → IC=+0.198 (n=15656)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 91.0 (IC base=+0.183)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `drift_60min` |x|≤ `0.1043` → IC=+0.258 (n=1229)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1043 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.233 (n=2906)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.227)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.228 (n=1897)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.227)

- **PATRÓN** `ibs_20min` > `0.8138` → IC=+0.273 (n=2496)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8138 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.479` → IC=+0.329 (n=910)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.479 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` > `0.2814` → IC=+0.285 (n=426)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2814 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` < `1.8357` → IC=+0.226 (n=1776)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8357 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` > `1.4361` → IC=+0.228 (n=2664)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4361 (IC base=+0.227)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.238 (n=3098)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.227)

- **PATRÓN** `sigma_h` < `0.0098` → IC=+0.259 (n=2271)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0098 (IC base=+0.256)

- **PATRÓN** `sigma_h` > `0.0088` → IC=+0.257 (n=1033)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0088 (IC base=+0.256)

- **PATRÓN** `drift_60min` |x|≤ `0.0967` → IC=+0.314 (n=999)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0967 (IC base=+0.256)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.261 (n=2345)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.256)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.260 (n=2064)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.256)

- **PATRÓN** `ibs_20min` < `0.0534` → IC=+0.301 (n=999)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0534 (IC base=+0.256)

- **PATRÓN** `volumen_pendiente_norm` < `0.0993` → IC=+0.259 (n=1995)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0993 (IC base=+0.256)

- **PATRÓN** `volumen_pendiente_norm` > `0.301` → IC=+0.273 (n=341)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.301 (IC base=+0.256)

- **PATRÓN** `volumen_spike_ratio` < `1.4457` → IC=+0.279 (n=725)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4457 (IC base=+0.256)

- **PATRÓN** `volumen_spike_ratio` > `2.6917` → IC=+0.257 (n=725)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6917 (IC base=+0.256)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.266 (n=1609)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.256)

- **PATRÓN** `libro_liquidez` > `1774.897` → IC=+0.264 (n=1513)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1774.897 (IC base=+0.256)

- **PATRÓN** `ballena_activa_n` < `7.0` → IC=+0.257 (n=843)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 7.0 (IC base=+0.256)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.201 (n=864)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.128)

- **PATRÓN** `drift_60min` |x|≤ `0.0652` → IC=+0.175 (n=864)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.0652 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.145 (n=2711)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` > `0.2602` → IC=+0.206 (n=2591)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2602 (IC base=+0.128)

- **PATRÓN** `dist_vwap_pct` > `0.1844` → IC=+0.212 (n=1291)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1844 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.65` → IC=+0.208 (n=474)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.65 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` < `0.6286` → IC=+0.132 (n=864)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 0.6286 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` > `1.0569` → IC=+0.136 (n=1175)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` > 1.0569 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` > `0.2804` → IC=+0.172 (n=403)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.2804 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` < `1.5047` → IC=+0.133 (n=1120)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 1.5047 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` > `2.4677` → IC=+0.151 (n=849)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 2.4677 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `399.0` → IC=+0.132 (n=2515)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 399.0 (IC base=+0.128)

- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.172 (n=2743)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0064 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.238` → IC=+0.172 (n=2414)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.238 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.180 (n=1308)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 15.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` < `0.6112` → IC=+0.209 (n=2743)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6112 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.857` → IC=+0.180 (n=517)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 10.857 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.025` → IC=+0.151 (n=2393)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` < 4.025 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` < `1.1958` → IC=+0.161 (n=2743)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.1958 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` < `0.0939` → IC=+0.150 (n=2373)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` < 0.0939 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `2.4679` → IC=+0.153 (n=2618)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.4679 (IC base=+0.147)

- **PATRÓN** `ballena_activa_n` < `210.0` → IC=+0.189 (n=1129)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 210.0 (IC base=+0.147)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0115` → IC=+0.231 (n=1303)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0115 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.2483` → IC=+0.234 (n=1916)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2483 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.220 (n=2989)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.291 (n=1526)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.541` → IC=+0.297 (n=893)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.541 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` < `0.099` → IC=+0.211 (n=2497)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.099 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` > `0.353` → IC=+0.240 (n=409)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.353 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `2.7137` → IC=+0.225 (n=1272)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7137 (IC base=+0.212)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.216 (n=3468)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `2009.87` → IC=+0.224 (n=958)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2009.87 (IC base=+0.212)

- **PATRÓN** `sigma_h` < `0.0118` → IC=+0.246 (n=2538)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0118 (IC base=+0.240)

- **PATRÓN** `drift_60min` |x|≤ `0.4117` → IC=+0.262 (n=2233)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4117 (IC base=+0.240)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.281 (n=975)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.240)

- **PATRÓN** `ibs_20min` < `0.039` → IC=+0.290 (n=1117)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.039 (IC base=+0.240)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.908` → IC=+0.280 (n=335)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.908 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` > `0.3576` → IC=+0.289 (n=424)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3576 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` < `1.7747` → IC=+0.242 (n=1078)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7747 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` > `2.1823` → IC=+0.251 (n=1633)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1823 (IC base=+0.240)

- **PATRÓN** `libro_liquidez` > `1886.9572` → IC=+0.251 (n=1150)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1886.9572 (IC base=+0.240)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.245 (n=1672)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.240)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.204 (n=931)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.128)

- **PATRÓN** `drift_60min` |x|≤ `0.0775` → IC=+0.183 (n=931)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.0775 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.138 (n=2888)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` > `0.2502` → IC=+0.191 (n=2792)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.2502 (IC base=+0.128)

- **PATRÓN** `dist_vwap_pct` > `0.1389` → IC=+0.185 (n=1609)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1389 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.265` → IC=+0.199 (n=480)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.265 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` < `0.8426` → IC=+0.136 (n=1862)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.8426 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` > `0.2885` → IC=+0.170 (n=419)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.2885 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` > `2.5111` → IC=+0.145 (n=912)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 2.5111 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `6810.9354` → IC=+0.196 (n=1266)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 6810.9354 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `126.0` → IC=+0.128 (n=2728)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 126.0 (IC base=+0.128)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.164 (n=2621)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0067 (IC base=+0.129)

- **PATRÓN** `drift_60min` |x|≤ `0.3967` → IC=+0.146 (n=2975)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.3967 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.164 (n=1428)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 15.0 (IC base=+0.129)

- **PATRÓN** `ibs_20min` < `0.6789` → IC=+0.186 (n=2975)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.6789 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.249` → IC=+0.141 (n=711)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 9.249 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` < `0.851` → IC=+0.151 (n=1985)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.851 (IC base=+0.129)

- **PATRÓN** `volumen_pendiente_norm` > `0.2939` → IC=+0.179 (n=443)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.2939 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` < `1.8002` → IC=+0.133 (n=1881)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 1.8002 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` > `1.4149` → IC=+0.131 (n=2821)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 1.4149 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `6255.5047` → IC=+0.191 (n=1349)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 6255.5047 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.152 (n=961)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 49.0 (IC base=+0.129)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.161 (n=1411)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` > 0.0113 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.157 (n=1481)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 15.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` > `0.4706` → IC=+0.204 (n=3117)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4706 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` > `0.1959` → IC=+0.187 (n=1667)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1959 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.996` → IC=+0.286 (n=657)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.996 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` < `1.1689` → IC=+0.129 (n=3109)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.1689 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` < `0.1626` → IC=+0.123 (n=3167)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.1626 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` < `1.7798` → IC=+0.125 (n=2011)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 1.7798 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `2656.4463` → IC=+0.193 (n=1410)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 2656.4463 (IC base=+0.118)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.134 (n=1018)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 16.0 (IC base=+0.118)

- **PATRÓN** `sigma_h` < `0.0118` → IC=+0.141 (n=3256)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0118 (IC base=+0.118)

- **PATRÓN** `drift_60min` |x|≤ `0.1127` → IC=+0.164 (n=1086)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.1127 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.134 (n=3331)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 5.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` < `0.65` → IC=+0.219 (n=3258)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.65 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` < `0.2144` → IC=+0.143 (n=3212)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.2144 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.253` → IC=+0.138 (n=2882)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 2.253 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` < `1.1712` → IC=+0.127 (n=3256)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` < 1.1712 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` > `0.2743` → IC=+0.142 (n=448)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` > 0.2743 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` < `1.4336` → IC=+0.136 (n=1027)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.4336 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `2900.261` → IC=+0.195 (n=1086)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 2900.261 (IC base=+0.118)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.125 (n=2064)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 27.0 (IC base=+0.118)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0132` → IC=+0.249 (n=2507)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0132 (IC base=+0.226)

- **PATRÓN** `drift_60min` |x|≤ `0.1656` → IC=+0.240 (n=1235)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1656 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.231 (n=2916)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.226)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.229 (n=2529)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.226)

- **PATRÓN** `ibs_20min` > `0.6667` → IC=+0.257 (n=2808)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6667 (IC base=+0.226)

- **PATRÓN** `dist_vwap_pct` > `0.1817` → IC=+0.234 (n=1721)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1817 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.58` → IC=+0.255 (n=1272)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.58 (IC base=+0.226)

- **PATRÓN** `volumen_regimen` > `0.6237` → IC=+0.235 (n=2807)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6237 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` > `0.2348` → IC=+0.266 (n=523)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2348 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` < `2.4722` → IC=+0.229 (n=2737)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4722 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` > `1.4333` → IC=+0.231 (n=2736)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4333 (IC base=+0.226)

- **PATRÓN** `libro_liquidez` > `2580.1216` → IC=+0.231 (n=1871)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2580.1216 (IC base=+0.226)

- **PATRÓN** `sigma_h` > `0.0228` → IC=+0.249 (n=1317)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0228 (IC base=+0.239)

- **PATRÓN** `drift_60min` |x|≤ `0.5795` → IC=+0.248 (n=2901)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5795 (IC base=+0.239)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.252 (n=1425)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.239)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.245 (n=1294)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.239)

- **PATRÓN** `ibs_20min` < `0.44` → IC=+0.263 (n=2909)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.44 (IC base=+0.239)

- **PATRÓN** `dist_vwap_pct` > `1.1483` → IC=+0.257 (n=270)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1483 (IC base=+0.239)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.016` → IC=+0.267 (n=405)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.016 (IC base=+0.239)

- **PATRÓN** `volumen_regimen` < `0.8647` → IC=+0.243 (n=1934)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8647 (IC base=+0.239)

- **PATRÓN** `volumen_regimen` > `0.6409` → IC=+0.243 (n=2901)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6409 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` > `0.2813` → IC=+0.293 (n=403)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2813 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` < `1.8377` → IC=+0.237 (n=1823)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8377 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` > `1.5489` → IC=+0.240 (n=2443)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5489 (IC base=+0.239)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.207 (n=1461)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.160)

- **PATRÓN** `drift_60min` |x|≤ `0.1331` → IC=+0.173 (n=1929)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.1331 (IC base=+0.160)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.172 (n=4577)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 5.0 (IC base=+0.160)

- **PATRÓN** `ibs_20min` > `0.3077` → IC=+0.196 (n=4386)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.3077 (IC base=+0.160)

- **PATRÓN** `dist_vwap_pct` > `0.2206` → IC=+0.184 (n=1673)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.2206 (IC base=+0.160)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.595` → IC=+0.208 (n=715)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.595 (IC base=+0.160)

- **PATRÓN** `volumen_regimen` < `0.8601` → IC=+0.170 (n=2661)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 0.8601 (IC base=+0.160)

- **PATRÓN** `volumen_regimen` > `1.1921` → IC=+0.167 (n=1330)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 1.1921 (IC base=+0.160)

- **PATRÓN** `volumen_pendiente_norm` > `0.1569` → IC=+0.173 (n=1154)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.1569 (IC base=+0.160)

- **PATRÓN** `volumen_spike_ratio` < `1.5262` → IC=+0.164 (n=1880)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.5262 (IC base=+0.160)

- **PATRÓN** `volumen_spike_ratio` > `2.4729` → IC=+0.163 (n=1424)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 2.4729 (IC base=+0.160)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.160 (n=4904)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.02 (IC base=+0.160)

- **PATRÓN** `libro_liquidez` > `7790.3095` → IC=+0.185 (n=1987)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 7790.3095 (IC base=+0.160)

- **PATRÓN** `ibs_20min` < `0.3846` → IC=+0.173 (n=3165)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.3846 (IC base=+0.093)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.134 (n=2035)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 24.0 (IC base=+0.093)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.197 (n=1138)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0061 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.103` → IC=+0.224 (n=501)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.103 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.215 (n=1027)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` > `0.6089` → IC=+0.238 (n=759)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6089 (IC base=+0.182)

- **PATRÓN** `dist_vwap_pct` > `0.3087` → IC=+0.218 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3087 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.927` → IC=+0.211 (n=500)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.927 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` < `0.8791` → IC=+0.195 (n=759)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 0.8791 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.0912` → IC=+0.196 (n=393)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.0912 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` < `2.1671` → IC=+0.196 (n=983)

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
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.235 (n=597)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.155)

- **PATRÓN** `drift_60min` |x|≤ `0.2091` → IC=+0.157 (n=902)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.2091 (IC base=+0.155)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.174 (n=1401)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 5.0 (IC base=+0.155)

- **PATRÓN** `ibs_20min` > `0.7966` → IC=+0.266 (n=612)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7966 (IC base=+0.155)

- **PATRÓN** `dist_vwap_pct` > `0.821` → IC=+0.192 (n=222)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.821 (IC base=+0.155)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.884` → IC=+0.205 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.884 (IC base=+0.155)

- **PATRÓN** `volumen_regimen` < `0.8313` → IC=+0.167 (n=901)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.8313 (IC base=+0.155)

- **PATRÓN** `volumen_pendiente_norm` > `0.2202` → IC=+0.204 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2202 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` > `1.776` → IC=+0.173 (n=888)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 1.776 (IC base=+0.155)

- **PATRÓN** `libro_liquidez` > `8101.5764` → IC=+0.176 (n=612)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 8101.5764 (IC base=+0.155)

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.123 (n=877)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0052 (IC base=+0.091)

- **PATRÓN** `ibs_20min` < `0.0847` → IC=+0.210 (n=439)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0847 (IC base=+0.091)

- **PATRÓN** `libro_liquidez` > `8021.1459` → IC=+0.151 (n=597)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 8021.1459 (IC base=+0.091)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.126 (n=567)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 43.0 (IC base=+0.091)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` < `0.0091` → IC=+0.149 (n=753)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0091 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.171 (n=795)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 11.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` > `0.5513` → IC=+0.196 (n=1009)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.5513 (IC base=+0.130)

- **PATRÓN** `dist_vwap_pct` > `0.9339` → IC=+0.183 (n=184)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.9339 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.829` → IC=+0.229 (n=448)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.829 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` < `1.0445` → IC=+0.141 (n=994)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 1.0445 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` > `0.7037` → IC=+0.139 (n=1009)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` > 0.7037 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` < `0.0776` → IC=+0.128 (n=992)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` < 0.0776 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` > `0.223` → IC=+0.155 (n=201)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` > 0.223 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` < `1.4125` → IC=+0.151 (n=365)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 1.4125 (IC base=+0.130)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.132 (n=1181)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.02 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `2758.0268` → IC=+0.171 (n=512)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 2758.0268 (IC base=+0.130)

- **PATRÓN** `ibs_20min` < `0.5616` → IC=+0.150 (n=1097)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.5616 (IC base=+0.070)

- **PATRÓN** `libro_liquidez` > `2636.7224` → IC=+0.161 (n=565)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 2636.7224 (IC base=+0.070)

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
- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.229 (n=7409)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0125 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.190 (n=23180)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` > `0.4301` → IC=+0.228 (n=22224)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4301 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` > `0.8828` → IC=+0.212 (n=2615)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8828 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.936` → IC=+0.257 (n=5434)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.936 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` < `1.2141` → IC=+0.159 (n=14966)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.2141 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.2411` → IC=+0.208 (n=3997)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2411 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `2.6218` → IC=+0.194 (n=7234)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.6218 (IC base=+0.180)

- **PATRÓN** `ballena_activa_n` < `103.0` → IC=+0.201 (n=20876)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 103.0 (IC base=+0.180)

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.199 (n=6814)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0052 (IC base=+0.195)

- **PATRÓN** `sigma_h` > `0.0122` → IC=+0.205 (n=6800)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0122 (IC base=+0.195)

- **PATRÓN** `drift_60min` |x|≤ `0.4818` → IC=+0.198 (n=20401)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.4818 (IC base=+0.195)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.215 (n=7633)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.195)

- **PATRÓN** `ibs_20min` < `0.5918` → IC=+0.245 (n=20403)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5918 (IC base=+0.195)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.393` → IC=+0.196 (n=2757)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 9.393 (IC base=+0.195)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.528` → IC=+0.201 (n=18916)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.528 (IC base=+0.195)

- **PATRÓN** `volumen_regimen` < `0.7026` → IC=+0.175 (n=6030)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.7026 (IC base=+0.195)

- **PATRÓN** `volumen_pendiente_norm` > `0.2932` → IC=+0.254 (n=2800)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2932 (IC base=+0.195)

- **PATRÓN** `volumen_spike_ratio` > `2.6312` → IC=+0.206 (n=6508)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6312 (IC base=+0.195)

- **PATRÓN** `ballena_activa_n` < `91.0` → IC=+0.211 (n=19285)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 91.0 (IC base=+0.195)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.251 (n=1728)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.236)

- **PATRÓN** `ibs_20min` > `0.9736` → IC=+0.320 (n=1613)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9736 (IC base=+0.236)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.827` → IC=+0.343 (n=847)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.827 (IC base=+0.236)

- **PATRÓN** `volumen_pendiente_norm` > `0.2327` → IC=+0.292 (n=642)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2327 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` < `1.4494` → IC=+0.234 (n=1145)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4494 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` > `2.2913` → IC=+0.243 (n=1557)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2913 (IC base=+0.236)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.251 (n=3907)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.236)

- **PATRÓN** `libro_liquidez` > `2040.64` → IC=+0.238 (n=1186)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2040.64 (IC base=+0.236)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.254 (n=2162)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 14.0 (IC base=+0.236)

- **PATRÓN** `sigma_h` < `0.0102` → IC=+0.270 (n=3165)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0102 (IC base=+0.269)

- **PATRÓN** `sigma_h` > `0.0092` → IC=+0.269 (n=1439)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0092 (IC base=+0.269)

- **PATRÓN** `drift_60min` |x|≤ `0.1214` → IC=+0.296 (n=1392)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1214 (IC base=+0.269)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.272 (n=2923)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.269)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.271 (n=2860)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.269)

- **PATRÓN** `ibs_20min` < `0.5479` → IC=+0.286 (n=3164)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5479 (IC base=+0.269)

- **PATRÓN** `volumen_pendiente_norm` < `0.0977` → IC=+0.272 (n=2881)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0977 (IC base=+0.269)

- **PATRÓN** `volumen_pendiente_norm` > `0.2907` → IC=+0.287 (n=439)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2907 (IC base=+0.269)

- **PATRÓN** `volumen_spike_ratio` < `1.5617` → IC=+0.271 (n=1335)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5617 (IC base=+0.269)

- **PATRÓN** `volumen_spike_ratio` > `2.6495` → IC=+0.279 (n=1012)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6495 (IC base=+0.269)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.275 (n=2227)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.269)

- **PATRÓN** `libro_liquidez` > `1775.5` → IC=+0.276 (n=2109)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1775.5 (IC base=+0.269)

- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.282 (n=1112)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 8.0 (IC base=+0.269)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.179 (n=1224)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0031 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.0787` → IC=+0.149 (n=1217)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.0787 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.148 (n=3800)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 5.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` > `0.1959` → IC=+0.188 (n=3644)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.1959 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.181` → IC=+0.192 (n=1554)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.181 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.329` → IC=+0.165 (n=761)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 9.329 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `0.6358` → IC=+0.155 (n=1215)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.6358 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` > `1.0681` → IC=+0.142 (n=1653)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 1.0681 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.2705` → IC=+0.180 (n=513)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.2705 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `2.166` → IC=+0.140 (n=3149)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 2.166 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `1.5193` → IC=+0.142 (n=3196)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.5193 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `220.0` → IC=+0.161 (n=1183)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 220.0 (IC base=+0.136)

- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.162 (n=3135)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0064 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.0793` → IC=+0.164 (n=1045)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.0793 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.166 (n=1152)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 17.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` < `0.6801` → IC=+0.186 (n=3135)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.6801 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.014` → IC=+0.137 (n=1501)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` > 3.014 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.221` → IC=+0.140 (n=3175)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` < 6.221 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `1.1895` → IC=+0.147 (n=3135)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 1.1895 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.2202` → IC=+0.193 (n=581)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2202 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `2.4323` → IC=+0.142 (n=3025)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.4323 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `1.7717` → IC=+0.141 (n=2017)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.7717 (IC base=+0.137)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.137 (n=4073)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `224.0` → IC=+0.153 (n=981)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 224.0 (IC base=+0.137)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.241 (n=2469)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0099 (IC base=+0.228)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.237 (n=3875)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.228)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.228 (n=3315)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.228)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.302 (n=1382)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.228)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.988` → IC=+0.322 (n=823)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.988 (IC base=+0.228)

- **PATRÓN** `volumen_pendiente_norm` < `0.132` → IC=+0.229 (n=3505)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.132 (IC base=+0.228)

- **PATRÓN** `volumen_pendiente_norm` > `0.3507` → IC=+0.228 (n=484)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3507 (IC base=+0.228)

- **PATRÓN** `volumen_spike_ratio` > `2.7413` → IC=+0.242 (n=1641)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7413 (IC base=+0.228)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.234 (n=4460)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.228)

- **PATRÓN** `libro_liquidez` > `1911.8434` → IC=+0.239 (n=1678)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1911.8434 (IC base=+0.228)

- **PATRÓN** `sigma_h` < `0.011` → IC=+0.249 (n=3113)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.011 (IC base=+0.245)

- **PATRÓN** `drift_60min` |x|≤ `0.1778` → IC=+0.267 (n=1555)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1778 (IC base=+0.245)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.264 (n=1347)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.245)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.245 (n=1605)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.245)

- **PATRÓN** `ibs_20min` < `0.0598` → IC=+0.304 (n=1178)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0598 (IC base=+0.245)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.065` → IC=+0.303 (n=378)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.065 (IC base=+0.245)

- **PATRÓN** `volumen_pendiente_norm` > `0.3492` → IC=+0.307 (n=533)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3492 (IC base=+0.245)

- **PATRÓN** `volumen_spike_ratio` > `2.1769` → IC=+0.255 (n=2269)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1769 (IC base=+0.245)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.250 (n=1803)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.245)

- **PATRÓN** `libro_liquidez` > `1994.3897` → IC=+0.255 (n=1178)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1994.3897 (IC base=+0.245)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.254 (n=2246)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.245)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.193 (n=1282)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0037 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.1296` → IC=+0.156 (n=1692)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.1296 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.149 (n=3990)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 5.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` > `0.8868` → IC=+0.273 (n=1282)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8868 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` > `0.1958` → IC=+0.169 (n=1736)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.1958 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.114` → IC=+0.163 (n=586)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 11.114 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `0.86` → IC=+0.150 (n=2564)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.86 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.2336` → IC=+0.188 (n=681)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.2336 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `1.5176` → IC=+0.151 (n=1655)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 1.5176 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `2.1727` → IC=+0.143 (n=1705)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 2.1727 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `5529.6254` → IC=+0.226 (n=1744)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5529.6254 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `87.0` → IC=+0.146 (n=2484)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 87.0 (IC base=+0.137)

- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.169 (n=2824)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0068 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.4362` → IC=+0.157 (n=3208)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.4362 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.173 (n=1183)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 17.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` < `0.5737` → IC=+0.213 (n=2823)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5737 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.873` → IC=+0.155 (n=473)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 10.873 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.043` → IC=+0.150 (n=2800)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 3.043 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` < `0.8573` → IC=+0.158 (n=2139)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.8573 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` > `0.2941` → IC=+0.216 (n=406)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2941 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `2.2105` → IC=+0.150 (n=2726)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.2105 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` > `1.5315` → IC=+0.155 (n=2767)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.5315 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `6394.3222` → IC=+0.221 (n=1070)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6394.3222 (IC base=+0.147)

- **PATRÓN** `ballena_activa_n` < `90.0` → IC=+0.161 (n=2090)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 90.0 (IC base=+0.147)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0127` → IC=+0.151 (n=1303)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` > 0.0127 (IC base=+0.116)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.146 (n=2764)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 11.0 (IC base=+0.116)

- **PATRÓN** `ibs_20min` > `0.4286` → IC=+0.185 (n=3919)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.4286 (IC base=+0.116)

- **PATRÓN** `dist_vwap_pct` > `1.0039` → IC=+0.203 (n=627)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0039 (IC base=+0.116)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.24` → IC=+0.268 (n=990)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.24 (IC base=+0.116)

- **PATRÓN** `volumen_regimen` < `0.8756` → IC=+0.128 (n=2603)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 0.8756 (IC base=+0.116)

- **PATRÓN** `volumen_spike_ratio` < `1.8238` → IC=+0.123 (n=2542)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` < 1.8238 (IC base=+0.116)

- **PATRÓN** `libro_liquidez` > `2710.4123` → IC=+0.237 (n=1301)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2710.4123 (IC base=+0.116)

- **PATRÓN** `sigma_h` < `0.0109` → IC=+0.152 (n=3231)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0109 (IC base=+0.127)

- **PATRÓN** `drift_60min` |x|≤ `0.1375` → IC=+0.152 (n=1223)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.1375 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.163 (n=1723)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 15.0 (IC base=+0.127)

- **PATRÓN** `ibs_20min` < `0.6667` → IC=+0.216 (n=3675)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6667 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` < `0.217` → IC=+0.142 (n=3345)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.217 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.032` → IC=+0.149 (n=3548)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 3.032 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` < `1.1905` → IC=+0.135 (n=3667)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 1.1905 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` > `0.228` → IC=+0.182 (n=643)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.228 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` < `1.4358` → IC=+0.160 (n=1161)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 1.4358 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `2601.4356` → IC=+0.209 (n=1222)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2601.4356 (IC base=+0.127)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.141 (n=3079)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 42.0 (IC base=+0.127)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0139` → IC=+0.261 (n=3194)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0139 (IC base=+0.239)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.244 (n=3739)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.239)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.244 (n=2386)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.239)

- **PATRÓN** `ibs_20min` > `0.6152` → IC=+0.272 (n=3194)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6152 (IC base=+0.239)

- **PATRÓN** `dist_vwap_pct` > `0.196` → IC=+0.254 (n=1833)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.196 (IC base=+0.239)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.171` → IC=+0.286 (n=621)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.171 (IC base=+0.239)

- **PATRÓN** `volumen_regimen` < `1.2177` → IC=+0.240 (n=3576)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2177 (IC base=+0.239)

- **PATRÓN** `volumen_regimen` > `0.6435` → IC=+0.244 (n=3576)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6435 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` > `0.2391` → IC=+0.256 (n=616)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2391 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` > `2.4984` → IC=+0.260 (n=1166)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4984 (IC base=+0.239)

- **PATRÓN** `libro_liquidez` > `2978.3521` → IC=+0.245 (n=1192)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2978.3521 (IC base=+0.239)

- **PATRÓN** `sigma_h` > `0.0259` → IC=+0.270 (n=1232)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0259 (IC base=+0.243)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.248 (n=3487)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.243)

- **PATRÓN** `ibs_20min` < `0.5206` → IC=+0.273 (n=3694)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5206 (IC base=+0.243)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.116` → IC=+0.277 (n=716)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.116 (IC base=+0.243)

- **PATRÓN** `volumen_regimen` < `0.7155` → IC=+0.245 (n=1627)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7155 (IC base=+0.243)

- **PATRÓN** `volumen_regimen` > `1.2178` → IC=+0.264 (n=1232)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2178 (IC base=+0.243)

- **PATRÓN** `volumen_pendiente_norm` > `0.2862` → IC=+0.306 (n=508)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2862 (IC base=+0.243)

- **PATRÓN** `volumen_spike_ratio` > `1.4351` → IC=+0.248 (n=3484)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4351 (IC base=+0.243)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.200 (n=5900)

- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.245 (n=2121)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.220)

- **PATRÓN** `drift_60min` |x|≤ `0.5136` → IC=+0.229 (n=6356)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5136 (IC base=+0.220)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.228 (n=5751)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.220)

- **PATRÓN** `ibs_20min` > `0.9294` → IC=+0.256 (n=2120)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9294 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.507` → IC=+0.224 (n=2104)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.507 (IC base=+0.220)

- **PATRÓN** `volumen_regimen` < `0.7054` → IC=+0.231 (n=2050)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7054 (IC base=+0.220)

- **PATRÓN** `volumen_regimen` > `0.8813` → IC=+0.220 (n=3105)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8813 (IC base=+0.220)

- **PATRÓN** `volumen_pendiente_norm` < `0.1051` → IC=+0.221 (n=5935)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1051 (IC base=+0.220)

- **PATRÓN** `volumen_pendiente_norm` > `0.1652` → IC=+0.228 (n=1793)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1652 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` < `2.2531` → IC=+0.223 (n=5506)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.2531 (IC base=+0.220)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.225 (n=4776)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.220)

- **PATRÓN** `libro_liquidez` > `2879.8591` → IC=+0.225 (n=5677)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2879.8591 (IC base=+0.220)

- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.239 (n=1479)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.199)

- **PATRÓN** `drift_60min` |x|≤ `0.4952` → IC=+0.212 (n=4437)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4952 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.213 (n=1486)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.211 (n=1959)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.199)

- **PATRÓN** `ibs_20min` < `0.1841` → IC=+0.210 (n=1952)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1841 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` > `0.6637` → IC=+0.208 (n=742)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6637 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.756` → IC=+0.211 (n=3990)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.756 (IC base=+0.199)

- **PATRÓN** `volumen_regimen` < `1.095` → IC=+0.206 (n=3726)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.095 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` < `0.0976` → IC=+0.200 (n=4087)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0976 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` > `0.0733` → IC=+0.203 (n=1980)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0733 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` < `1.5304` → IC=+0.205 (n=1924)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5304 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` > `2.1824` → IC=+0.209 (n=1983)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1824 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.200 (n=5900)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

- **PATRÓN** `ballena_activa_n` < `32.0` → IC=+0.221 (n=1930)

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
- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.217 (n=1786)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0084 (IC base=+0.204)

- **PATRÓN** `drift_60min` |x|≤ `0.4605` → IC=+0.211 (n=1786)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4605 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.229 (n=630)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.204)

- **PATRÓN** `ibs_20min` < `0.4751` → IC=+0.214 (n=1192)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4751 (IC base=+0.204)

- **PATRÓN** `ibs_20min` > `0.1477` → IC=+0.207 (n=1786)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1477 (IC base=+0.204)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.379` → IC=+0.211 (n=1814)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 6.379 (IC base=+0.204)

- **PATRÓN** `volumen_regimen` < `0.8733` → IC=+0.210 (n=1191)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8733 (IC base=+0.204)

- **PATRÓN** `volumen_pendiente_norm` < `0.102` → IC=+0.208 (n=1647)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.102 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` < `1.403` → IC=+0.223 (n=583)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.403 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` > `1.4937` → IC=+0.206 (n=1562)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4937 (IC base=+0.204)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.205 (n=1784)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.204)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.243 (n=472)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.200)

- **PATRÓN** `drift_60min` |x|≤ `0.4897` → IC=+0.220 (n=1414)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4897 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.205 (n=533)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.200)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.217 (n=956)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.200)

- **PATRÓN** `ibs_20min` < `0.1702` → IC=+0.203 (n=622)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1702 (IC base=+0.200)

- **PATRÓN** `ibs_20min` > `0.612` → IC=+0.208 (n=641)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.612 (IC base=+0.200)

- **PATRÓN** `dist_vwap_pct` > `0.633` → IC=+0.217 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.633 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.266` → IC=+0.204 (n=1290)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.266 (IC base=+0.200)

- **PATRÓN** `volumen_regimen` < `1.2516` → IC=+0.209 (n=1414)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2516 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` > `0.0733` → IC=+0.230 (n=580)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0733 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` < `1.4106` → IC=+0.209 (n=462)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4106 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` > `1.7842` → IC=+0.202 (n=924)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7842 (IC base=+0.200)

- **PATRÓN** `libro_liquidez` > `6544.4636` → IC=+0.205 (n=1263)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6544.4636 (IC base=+0.200)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0083` → IC=+0.237 (n=459)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0083 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `10.0` → IC=+0.244 (n=713)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.206)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.280 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.206)

- **PATRÓN** `dist_vwap_pct` > `0.7792` → IC=+0.236 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7792 (IC base=+0.206)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.193` → IC=+0.231 (n=570)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.193 (IC base=+0.206)

- **PATRÓN** `volumen_regimen` < `0.7061` → IC=+0.243 (n=457)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7061 (IC base=+0.206)

- **PATRÓN** `volumen_pendiente_norm` < `0.1058` → IC=+0.214 (n=939)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1058 (IC base=+0.206)

- **PATRÓN** `volumen_pendiente_norm` > `0.0788` → IC=+0.209 (n=458)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0788 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` < `2.1407` → IC=+0.215 (n=889)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1407 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` > `1.4694` → IC=+0.209 (n=1010)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4694 (IC base=+0.206)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.214 (n=1209)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.206)

- **PATRÓN** `libro_liquidez` > `4306.9276` → IC=+0.250 (n=346)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4306.9276 (IC base=+0.206)

- **PATRÓN** `ballena_activa_n` < `38.0` → IC=+0.211 (n=899)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 38.0 (IC base=+0.206)

- **PATRÓN** `sigma_h` < `0.0131` → IC=+0.223 (n=715)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0131 (IC base=+0.222)

- **PATRÓN** `sigma_h` > `0.01` → IC=+0.238 (n=476)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.01 (IC base=+0.222)

- **PATRÓN** `drift_60min` |x|≤ `0.5987` → IC=+0.241 (n=715)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5987 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.225 (n=666)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.248 (n=494)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` < `0.7308` → IC=+0.252 (n=715)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7308 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.774` → IC=+0.236 (n=662)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.774 (IC base=+0.222)

- **PATRÓN** `volumen_regimen` < `1.0964` → IC=+0.226 (n=629)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0964 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` < `0.0825` → IC=+0.237 (n=602)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0825 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` > `2.1876` → IC=+0.258 (n=316)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1876 (IC base=+0.222)

- **PATRÓN** `libro_liquidez` > `3792.9162` → IC=+0.236 (n=476)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3792.9162 (IC base=+0.222)

- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.262 (n=469)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 25.0 (IC base=+0.222)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.148 (n=737)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0038 (IC base=+0.054)

- **PATRÓN** `ibs_20min` > `0.7505` → IC=+0.187 (n=1412)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.7505 (IC base=+0.054)

- **PATRÓN** `dist_vwap_pct` > `0.1435` → IC=+0.142 (n=1048)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.1435 (IC base=+0.054)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.432` → IC=+0.149 (n=474)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 10.432 (IC base=+0.054)

- **PATRÓN** `ibs_20min` < `0.0617` → IC=+0.264 (n=651)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0617 (IC base=+0.049)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.123 (n=616)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0053 (IC base=+0.070)

- **PATRÓN** `ibs_20min` > `0.5459` → IC=+0.163 (n=598)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` > 0.5459 (IC base=+0.070)

- **PATRÓN** `dist_vwap_pct` > `0.1215` → IC=+0.170 (n=319)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.1215 (IC base=+0.070)

- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.130 (n=268)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.65€ cuando `sigma_h` < 0.0035 (IC base=+0.047)

- **PATRÓN** `ibs_20min` < `0.0659` → IC=+0.269 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0659 (IC base=+0.047)

- **PATRÓN** `volumen_pendiente_norm` > `0.0693` → IC=+0.126 (n=252)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` > 0.0693 (IC base=+0.047)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` > `0.679` → IC=-0.160 (n=157)

  - _Acción_: SKIP cuando `ibs_20min` > 0.679
  - _Potencial_: sin este filtro IC_bueno=+0.106 (n=473)

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.128 (n=477)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.64€ cuando `sigma_h` < 0.0052 (IC base=+0.072)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.126 (n=354)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 15.0 (IC base=+0.072)

- **PATRÓN** `ibs_20min` > `0.7783` → IC=+0.221 (n=456)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7783 (IC base=+0.072)

- **PATRÓN** `dist_vwap_pct` > `0.1265` → IC=+0.172 (n=333)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.1265 (IC base=+0.072)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.65` → IC=+0.203 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.65 (IC base=+0.072)

- **PATRÓN** `ibs_20min` < `0.1087` → IC=+0.248 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1087 (IC base=+0.023)

### GBM_LATE_60M#SOL#60min
- **PATRÓN** `ibs_20min` > `0.7241` → IC=+0.137 (n=510)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` > 0.7241 (IC base=+0.023)

- **PATRÓN** `dist_vwap_pct` > `0.4644` → IC=+0.125 (n=254)

  - _Acción_: Kelly boost +0.62€ cuando `dist_vwap_pct` > 0.4644 (IC base=+0.023)

- **PATRÓN** `sigma_h` < `0.0096` → IC=+0.188 (n=302)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0096 (IC base=+0.079)

- **PATRÓN** `ibs_20min` < `0.4857` → IC=+0.178 (n=424)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.4857 (IC base=+0.079)

- **PATRÓN** `dist_vwap_pct` < `0.1839` → IC=+0.141 (n=413)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.1839 (IC base=+0.079)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.779` → IC=+0.271 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.779 (IC base=+0.079)

- **PATRÓN** `volumen_regimen` > `1.0831` → IC=+0.178 (n=141)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` > 1.0831 (IC base=+0.079)

- **PATRÓN** `volumen_pendiente_norm` > `0.1089` → IC=+0.161 (n=163)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.1089 (IC base=+0.079)

- **PATRÓN** `volumen_spike_ratio` > `1.4547` → IC=+0.126 (n=394)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` > 1.4547 (IC base=+0.079)

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

- **FILTRO** `volumen_regimen` > `0.805` → IC=-0.316 (n=36)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.226 (n=111)

- **FILTRO** `libro_liquidez` < `5528.1887` → IC=-0.259 (n=110)

  - _Acción_: SKIP cuando `libro_liquidez` < 5528.1887
  - _Potencial_: sin este filtro IC_bueno=-0.218 (n=37)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `sigma_h` < `0.0063` → IC=-0.208 (n=87)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0063
  - _Potencial_: sin este filtro IC_bueno=-0.117 (n=45)

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
- **PATRÓN** `sigma_h` > `0.0086` → IC=+0.252 (n=240)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0086 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.192 (n=371)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 15.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` > `0.6774` → IC=+0.181 (n=715)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.6774 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` > `0.8064` → IC=+0.283 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8064 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.608` → IC=+0.157 (n=389)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 3.608 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `0.6243` → IC=+0.185 (n=239)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 0.6243 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` > `1.2135` → IC=+0.146 (n=238)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 1.2135 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` < `0.0701` → IC=+0.175 (n=530)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` < 0.0701 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `1.396` → IC=+0.198 (n=203)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.396 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.489` → IC=+0.151 (n=196)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 10.489 (IC base=+0.035)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.7234` → IC=-0.148 (n=69)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7234
  - _Potencial_: sin este filtro IC_bueno=+0.097 (n=209)

- **PATRÓN** `ibs_20min` > `0.9081` → IC=+0.124 (n=139)

  - _Acción_: Kelly boost +0.62€ cuando `ibs_20min` > 0.9081 (IC base=+0.036)

- **PATRÓN** `dist_vwap_pct` > `0.6267` → IC=+0.207 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6267 (IC base=+0.036)

- **PATRÓN** `ibs_20min` < `0.2162` → IC=+0.147 (n=395)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` < 0.2162 (IC base=+0.093)

- **PATRÓN** `volumen_spike_ratio` > `2.1239` → IC=+0.135 (n=165)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 2.1239 (IC base=+0.093)

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
- **FILTRO** `ibs_20min` > `0.1951` → IC=-0.227 (n=64)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1951
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=125)

- **PATRÓN** `sigma_h` > `0.0109` → IC=+0.302 (n=89)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0109 (IC base=+0.252)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.300 (n=188)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.252)

- **PATRÓN** `ibs_20min` > `0.5882` → IC=+0.281 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5882 (IC base=+0.252)

- **PATRÓN** `dist_vwap_pct` > `0.6947` → IC=+0.392 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6947 (IC base=+0.252)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.824` → IC=+0.349 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.824 (IC base=+0.252)

- **PATRÓN** `volumen_regimen` < `0.5849` → IC=+0.302 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.5849 (IC base=+0.252)

- **PATRÓN** `volumen_pendiente_norm` > `0.0973` → IC=+0.327 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0973 (IC base=+0.252)

- **PATRÓN** `volumen_spike_ratio` < `1.4812` → IC=+0.330 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4812 (IC base=+0.252)

- **PATRÓN** `volumen_spike_ratio` > `2.3425` → IC=+0.306 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3425 (IC base=+0.252)

### LATE_WINDOW_5MIN
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.326 (n=113)

- **PATRÓN** `drift_ventana_pct` |x|> `0.349` → IC=+0.341 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.349 (IC base=+0.328)

- **PATRÓN** `elapsed_s` > `207.0` → IC=+0.398 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 207.0 (IC base=+0.328)

- **PATRÓN** `drift_15min` |x|≤ `1.0295` → IC=+0.435 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0295 (IC base=+0.328)

- **PATRÓN** `drift_60min` |x|≤ `0.9647` → IC=+0.375 (n=86)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9647 (IC base=+0.328)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.397 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.328)

- **PATRÓN** `ballena_activa_n` < `1220.0` → IC=+0.350 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1220.0 (IC base=+0.328)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3488` → IC=+0.300 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3488 (IC base=+0.265)

- **PATRÓN** `elapsed_s` > `229.9` → IC=+0.329 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 229.9 (IC base=+0.265)

- **PATRÓN** `drift_15min` |x|≤ `2.3044` → IC=+0.307 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3044 (IC base=+0.265)

- **PATRÓN** `drift_60min` |x|≤ `0.6421` → IC=+0.309 (n=66)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6421 (IC base=+0.265)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.326 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.265)

- **PATRÓN** `ballena_activa_n` < `1750.0` → IC=+0.310 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1750.0 (IC base=+0.265)

### LATE_WINDOW_5MIN#BTC#5min
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.326 (n=113)

- **PATRÓN** `drift_ventana_pct` |x|> `0.349` → IC=+0.341 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.349 (IC base=+0.328)

- **PATRÓN** `elapsed_s` > `207.0` → IC=+0.398 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 207.0 (IC base=+0.328)

- **PATRÓN** `drift_15min` |x|≤ `1.0295` → IC=+0.435 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0295 (IC base=+0.328)

- **PATRÓN** `drift_60min` |x|≤ `0.9647` → IC=+0.375 (n=86)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9647 (IC base=+0.328)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.397 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.328)

- **PATRÓN** `ballena_activa_n` < `1220.0` → IC=+0.350 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1220.0 (IC base=+0.328)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3488` → IC=+0.300 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3488 (IC base=+0.265)

- **PATRÓN** `elapsed_s` > `229.9` → IC=+0.329 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 229.9 (IC base=+0.265)

- **PATRÓN** `drift_15min` |x|≤ `2.3044` → IC=+0.307 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3044 (IC base=+0.265)

- **PATRÓN** `drift_60min` |x|≤ `0.6421` → IC=+0.309 (n=66)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6421 (IC base=+0.265)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.326 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.265)

- **PATRÓN** `ballena_activa_n` < `1750.0` → IC=+0.310 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1750.0 (IC base=+0.265)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.123 (n=1460)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` > 0.5 (IC base=+0.098)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.123 (n=1460)

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
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=828)

### LIQUIDACIONES_15M#BNB#15min
- **PATRÓN** `liq_usd_total` > `1412.54` → IC=+0.200 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `liq_usd_total` > 1412.54 (IC base=+0.028)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `libro_liquidez` < `12324.2702` → IC=-0.152 (n=44)

  - _Acción_: SKIP cuando `libro_liquidez` < 12324.2702
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
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=3934)

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
- **FILTRO** `libro_liquidez` < `13988.6712` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `libro_liquidez` < 13988.6712
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=19)

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
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=1603)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=1557)

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
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=448)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=429)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.141 (n=193)

  - _Acción_: Kelly boost +0.71€ cuando `py_entrada` < 0.495 (IC base=+0.021)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=1006)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=1006)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=1259)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=1259)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=288)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=288)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.136 (n=64)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=348)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=397)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=301)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=402)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=402)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.120 (n=185)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=247)

- **FILTRO** `libro_liquidez` < `553.1995` → IC=-0.145 (n=108)

  - _Acción_: SKIP cuando `libro_liquidez` < 553.1995
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=324)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=360)

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

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **FILTRO** `py_entrada` > `0.57` → IC=-0.126 (n=428)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.082 (n=503)

- **PATRÓN** `py_entrada` < `0.51` → IC=+0.136 (n=328)

  - _Acción_: Kelly boost +0.68€ cuando `py_entrada` < 0.51 (IC base=-0.013)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` > `0.57` → IC=-0.122 (n=358)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.068 (n=361)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` > `0.58` → IC=-0.123 (n=343)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=405)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.134 (n=266)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=572)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.44` → IC=-0.140 (n=506)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=506)

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
- **FILTRO** `py_entrada` < `0.46` → IC=-0.175 (n=7904)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=25181)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.174 (n=8387)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=25757)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.187 (n=1530)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.118 (n=4599)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.150 (n=2039)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.095 (n=4013)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.134 (n=1584)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` > 1.0 (IC base=+0.042)

- **PATRÓN** `py_entrada` < `0.505` → IC=+0.126 (n=3073)

  - _Acción_: Kelly boost +0.63€ cuando `py_entrada` < 0.505 (IC base=+0.012)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` < `0.44` → IC=-0.172 (n=1097)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=3502)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.181 (n=1197)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=3603)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` > `0.62` → IC=-0.201 (n=1513)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.086 (n=4688)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.136 (n=1888)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` > 1.0 (IC base=+0.034)

- **PATRÓN** `libro_liquidez` > `1741.4156` → IC=+0.121 (n=2081)

  - _Acción_: Kelly boost +0.60€ cuando `libro_liquidez` > 1741.4156 (IC base=+0.034)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.485` → IC=-0.160 (n=1525)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=4635)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=2433)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.162 (n=772)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=2357)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.180 (n=973)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=3058)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=4010)

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
  - _Potencial_: sin este filtro IC_bueno=-0.102 (n=362)

- **FILTRO** `ballena_activa_n` > `84.0` → IC=-0.179 (n=157)

  - _Acción_: SKIP cuando `ballena_activa_n` > 84.0
  - _Potencial_: sin este filtro IC_bueno=-0.103 (n=310)

- **FILTRO** `libro_liquidez` < `3222.056` → IC=-0.183 (n=156)

  - _Acción_: SKIP cuando `libro_liquidez` < 3222.056
  - _Potencial_: sin este filtro IC_bueno=-0.098 (n=319)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=969)

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
  - _Potencial_: sin este filtro IC_bueno=-0.090 (n=50723)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.298 (n=17558)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=55626)

- **FILTRO** `ibs_7min` < `0.2172` → IC=-0.234 (n=18296)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2172
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=54888)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.153 (n=23884)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=49300)

- **FILTRO** `py_entrada` > `0.68` → IC=-0.252 (n=21413)

  - _Acción_: SKIP cuando `py_entrada` > 0.68
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=70133)

- **FILTRO** `ibs_7min` > `0.2824` → IC=-0.184 (n=22877)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2824
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=68669)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.155 (n=3153)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=9893)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.316 (n=3221)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=9825)

- **FILTRO** `ibs_7min` < `0.7107` → IC=-0.250 (n=4305)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7107
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=8741)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.152 (n=2780)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=10266)

- **FILTRO** `py_entrada` > `0.72` → IC=-0.277 (n=3859)

  - _Acción_: SKIP cuando `py_entrada` > 0.72
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=11950)

- **FILTRO** `ibs_7min` > `0.7768` → IC=-0.211 (n=3952)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7768
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=11857)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.123 (n=2932)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.101 (n=9253)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.264 (n=2941)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=9244)

- **FILTRO** `ibs_7min` < `0.7141` → IC=-0.209 (n=3046)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7141
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=9139)

- **FILTRO** `ballena_activa_n` > `155.0` → IC=-0.201 (n=3044)

  - _Acción_: SKIP cuando `ballena_activa_n` > 155.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=9141)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.268 (n=2852)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=9584)

- **FILTRO** `ibs_7min` > `0.2661` → IC=-0.195 (n=3108)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2661
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=9328)

- **FILTRO** `ballena_activa_n` > `154.0` → IC=-0.182 (n=3090)

  - _Acción_: SKIP cuando `ballena_activa_n` > 154.0
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=9346)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.165 (n=3011)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=9473)

- **FILTRO** `py_entrada` < `0.3` → IC=-0.324 (n=2967)

  - _Acción_: SKIP cuando `py_entrada` < 0.3
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=9517)

- **FILTRO** `ibs_7min` < `0.2857` → IC=-0.250 (n=4102)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2857
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=8382)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.201 (n=2497)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=9987)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.259 (n=4064)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=12677)

- **FILTRO** `ibs_7min` > `0.7315` → IC=-0.182 (n=4185)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7315
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=12556)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.262 (n=2937)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=8897)

- **FILTRO** `ibs_7min` < `0.7143` → IC=-0.197 (n=2954)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7143
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=8880)

- **FILTRO** `ballena_activa_n` > `25.0` → IC=-0.190 (n=2879)

  - _Acción_: SKIP cuando `ballena_activa_n` > 25.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=8955)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.258 (n=2866)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=9465)

- **FILTRO** `ibs_7min` > `0.2737` → IC=-0.177 (n=3081)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2737
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=9250)

- **FILTRO** `ballena_activa_n` > `24.0` → IC=-0.172 (n=3000)

  - _Acción_: SKIP cuando `ballena_activa_n` > 24.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=9331)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.32` → IC=-0.299 (n=2776)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=8945)

- **FILTRO** `ibs_7min` < `0.7` → IC=-0.235 (n=3797)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=7924)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.217 (n=2891)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=8830)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.199 (n=4295)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=13421)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.132 (n=3828)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.108 (n=8086)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.308 (n=2842)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=9072)

- **FILTRO** `ibs_7min` < `0.1556` → IC=-0.231 (n=2978)

  - _Acción_: SKIP cuando `ibs_7min` < 0.1556
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=8936)

- **FILTRO** `ballena_activa_n` > `9.0` → IC=-0.205 (n=2641)

  - _Acción_: SKIP cuando `ballena_activa_n` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.090 (n=9273)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.233 (n=3832)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=12681)

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
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=894)

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
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=579)

- **FILTRO** `libro_liquidez` < `3302.3462` → IC=-0.155 (n=192)

  - _Acción_: SKIP cuando `libro_liquidez` < 3302.3462
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=579)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=396)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.4307` → IC=+0.149 (n=688)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.75€ cuando `delta_ratio` |x|> 0.4307 (IC base=+0.123)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.127 (n=1360)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 14.0 (IC base=+0.123)

- **PATRÓN** `total_vol_5m` < `418.5531` → IC=+0.161 (n=505)

  - _Acción_: Kelly boost +0.80€ cuando `total_vol_5m` < 418.5531 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `2323.571` → IC=+0.129 (n=1352)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 2323.571 (IC base=+0.123)

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
- **PATRÓN** `delta_ratio` |x|> `0.4378` → IC=+0.154 (n=105)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.77€ cuando `delta_ratio` |x|> 0.4378 (IC base=+0.119)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.140 (n=287)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 15.0 (IC base=+0.119)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.124 (n=373)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.04 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `2392.1732` → IC=+0.142 (n=205)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 2392.1732 (IC base=+0.119)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4165` → IC=+0.172 (n=190)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.86€ cuando `delta_ratio` |x|> 0.4165 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.144 (n=265)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.123)

- **PATRÓN** `total_vol_5m` < `865.1327` → IC=+0.146 (n=286)

  - _Acción_: Kelly boost +0.73€ cuando `total_vol_5m` < 865.1327 (IC base=+0.123)

- **PATRÓN** `ballena_activa_n` < `59.0` → IC=+0.173 (n=96)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 59.0 (IC base=+0.123)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.3978` → IC=+0.165 (n=258)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.83€ cuando `delta_ratio` |x|> 0.3978 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.170 (n=186)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 12.0 (IC base=+0.141)

- **PATRÓN** `total_vol_5m` < `5917.212` → IC=+0.168 (n=227)

  - _Acción_: Kelly boost +0.84€ cuando `total_vol_5m` < 5917.212 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `3712.2533` → IC=+0.161 (n=172)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 3712.2533 (IC base=+0.141)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `hora_utc` < `14.0` → IC=+0.127 (n=277)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 14.0 (IC base=+0.098)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.134 (n=203)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.098)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `4.8182` → IC=-0.203 (n=116)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.8182
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=118)

- **FILTRO** `T_h` > `129.6211` → IC=-0.170 (n=213)

  - _Acción_: SKIP cuando `T_h` > 129.6211
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=643)

- **FILTRO** `pct_vs_K` |x|> `3.395` → IC=-0.183 (n=291)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.395
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=565)

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.146 (n=283)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0045 (IC base=-0.065)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `pct_vs_K` |x|> `4.2515` → IC=-0.254 (n=63)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.2515
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=192)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.282 (n=85)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=-0.021)

- **PATRÓN** `pct_vs_K` |x|≤ `1.73` → IC=+0.178 (n=85)

  - _Acción_: Kelly boost +0.89€ cuando `pct_vs_K` |x|≤ 1.73 (IC base=-0.021)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `T_h` < `251.7955` → IC=-0.192 (n=63)

  - _Acción_: SKIP cuando `T_h` < 251.7955
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=21)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `T_h` < `66.2576` → IC=-0.179 (n=54)

  - _Acción_: SKIP cuando `T_h` < 66.2576
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=110)

### PRICE_TARGET_GBM#SOL#reach
- **FILTRO** `T_h` < `146.0708` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `T_h` < 146.0708
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=16)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0113` → IC=-0.231 (n=585)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0113
  - _Potencial_: sin este filtro IC_bueno=-0.190 (n=195)

- **FILTRO** `T_h` > `69.35` → IC=-0.227 (n=522)

  - _Acción_: SKIP cuando `T_h` > 69.35
  - _Potencial_: sin este filtro IC_bueno=-0.208 (n=258)

- **FILTRO** `pct_vs_K` |x|> `3.0379` → IC=-0.395 (n=170)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.0379
  - _Potencial_: sin este filtro IC_bueno=-0.110 (n=511)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `sigma_h` > `0.0065` → IC=-0.205 (n=127)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0065
  - _Potencial_: sin este filtro IC_bueno=-0.187 (n=129)

- **FILTRO** `T_h` > `49.2217` → IC=-0.210 (n=191)

  - _Acción_: SKIP cuando `T_h` > 49.2217
  - _Potencial_: sin este filtro IC_bueno=-0.157 (n=65)

- **FILTRO** `T_h` > `143.4358` → IC=-0.234 (n=62)

  - _Acción_: SKIP cuando `T_h` > 143.4358
  - _Potencial_: sin este filtro IC_bueno=-0.181 (n=189)

- **FILTRO** `pct_vs_K` |x|> `2.4904` → IC=-0.362 (n=85)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.4904
  - _Potencial_: sin este filtro IC_bueno=-0.107 (n=166)

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
- **FILTRO** `sigma_h` < `0.011` → IC=-0.296 (n=165)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.011
  - _Potencial_: sin este filtro IC_bueno=-0.224 (n=56)

- **FILTRO** `T_h` > `70.3263` → IC=-0.280 (n=148)

  - _Acción_: SKIP cuando `T_h` > 70.3263
  - _Potencial_: sin este filtro IC_bueno=-0.273 (n=73)

- **FILTRO** `sigma_h` < `0.0055` → IC=-0.198 (n=51)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0055
  - _Potencial_: sin este filtro IC_bueno=-0.135 (n=154)

- **FILTRO** `pct_vs_K` |x|> `2.8988` → IC=-0.415 (n=69)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.8988
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=136)

- **PATRÓN** `pct_vs_K` |x|≤ `0.8096` → IC=+0.204 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `pct_vs_K` |x|≤ 0.8096 (IC base=-0.152)

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
- **FILTRO** `sigma_h` < `0.0083` → IC=-0.268 (n=54)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0083
  - _Potencial_: sin este filtro IC_bueno=-0.163 (n=164)

- **FILTRO** `T_h` > `65.7668` → IC=-0.221 (n=163)

  - _Acción_: SKIP cuando `T_h` > 65.7668
  - _Potencial_: sin este filtro IC_bueno=-0.097 (n=55)

- **FILTRO** `sigma_h` > `0.014` → IC=-0.308 (n=50)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.014
  - _Potencial_: sin este filtro IC_bueno=-0.150 (n=98)

- **FILTRO** `sigma_h` < `0.0085` → IC=-0.269 (n=37)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0085
  - _Potencial_: sin este filtro IC_bueno=-0.181 (n=111)

- **FILTRO** `T_h` > `34.5304` → IC=-0.232 (n=110)

  - _Acción_: SKIP cuando `T_h` > 34.5304
  - _Potencial_: sin este filtro IC_bueno=-0.125 (n=38)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1195` → IC=+0.461 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1195 (IC base=+0.333)

- **PATRÓN** `sigma_h` > `0.0146` → IC=+0.350 (n=38)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0146 (IC base=+0.333)

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
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=422)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.072 (n=479)

- **PATRÓN** `streak_estiramiento` < `0.8196` → IC=+0.125 (n=329)

  - _Acción_: Kelly boost +0.63€ cuando `streak_estiramiento` < 0.8196 (IC base=+0.059)

- **PATRÓN** `ballena_activa_n` < `29.0` → IC=+0.124 (n=243)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 29.0 (IC base=+0.059)

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
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=167)

- **PATRÓN** `streak_estiramiento` < `0.4376` → IC=+0.188 (n=139)

  - _Acción_: Kelly boost +0.94€ cuando `streak_estiramiento` < 0.4376 (IC base=+0.093)

- **PATRÓN** `ballena_activa_n` < `31.0` → IC=+0.156 (n=152)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 31.0 (IC base=+0.093)

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
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=1068)

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
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=4941)

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
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=2836)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.188 (n=1771)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0054 (IC base=+0.142)

- **PATRÓN** `drift_60min` |x|≤ `0.22` → IC=+0.159 (n=5314)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.22 (IC base=+0.142)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1351` → IC=+0.157 (n=2184)

  - _Acción_: Kelly boost +0.78€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1351 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.152 (n=4909)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 6.0 (IC base=+0.142)

- **PATRÓN** `ibs_15` > `0.5801` → IC=+0.226 (n=4746)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5801 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` > `0.1339` → IC=+0.133 (n=2494)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` > 0.1339 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` < `0.3239` → IC=+0.126 (n=4479)

  - _Acción_: Kelly boost +0.63€ cuando `dist_vwap_pct` < 0.3239 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.283` → IC=+0.247 (n=1005)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.283 (IC base=+0.142)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=3051)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `4551.8044` → IC=+0.169 (n=1771)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 4551.8044 (IC base=+0.142)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=2030)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.222 (n=788)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0057 (IC base=+0.202)

- **PATRÓN** `drift_60min` |x|≤ `0.0596` → IC=+0.251 (n=263)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0596 (IC base=+0.202)

- **PATRÓN** `delta_ratio_macro` |x|> `0.269` → IC=+0.225 (n=263)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.269 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.228 (n=726)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.202)

- **PATRÓN** `ibs_15` > `0.7086` → IC=+0.275 (n=788)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7086 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` > `0.3743` → IC=+0.227 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3743 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` < `0.5108` → IC=+0.205 (n=889)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5108 (IC base=+0.202)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.41` → IC=+0.310 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.41 (IC base=+0.202)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.204 (n=1020)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `14493.8191` → IC=+0.221 (n=357)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14493.8191 (IC base=+0.202)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.007` → IC=+0.149 (n=978)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.007 (IC base=+0.131)

- **PATRÓN** `drift_60min` |x|≤ `0.1106` → IC=+0.147 (n=652)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.1106 (IC base=+0.131)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1407` → IC=+0.132 (n=652)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.66€ cuando `delta_ratio_macro` |x|> 0.1407 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.138 (n=895)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 6.0 (IC base=+0.131)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.132 (n=1031)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 17.0 (IC base=+0.131)

- **PATRÓN** `ibs_15` > `0.4932` → IC=+0.216 (n=978)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.4932 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` > `0.1175` → IC=+0.152 (n=613)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.1175 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.845` → IC=+0.280 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.845 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `5960.612` → IC=+0.168 (n=444)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 5960.612 (IC base=+0.131)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `ibs_15` > `0.5926` → IC=+0.128 (n=986)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.64€ cuando `ibs_15` > 0.5926 (IC base=+0.056)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` < `0.0255` → IC=+0.166 (n=1324)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0255 (IC base=+0.154)

- **PATRÓN** `drift_60min` |x|≤ `0.2241` → IC=+0.176 (n=1324)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.2241 (IC base=+0.154)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0992` → IC=+0.216 (n=407)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0992 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.160 (n=1212)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 6.0 (IC base=+0.154)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.159 (n=1172)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 14.0 (IC base=+0.154)

- **PATRÓN** `ibs_15` > `0.5455` → IC=+0.228 (n=1183)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5455 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` > `0.5298` → IC=+0.193 (n=311)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.5298 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.989` → IC=+0.193 (n=291)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 17.989 (IC base=+0.154)

- **PATRÓN** `libro_liquidez` > `2944.0982` → IC=+0.195 (n=601)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 2944.0982 (IC base=+0.154)

- **PATRÓN** `ibs_15` < `0.1089` → IC=+0.157 (n=1014)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.78€ cuando `ibs_15` < 0.1089 (IC base=+0.068)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` > `0.006` → IC=+0.389 (n=250)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.006 (IC base=+0.364)

- **PATRÓN** `drift_60min` |x|≤ `0.1119` → IC=+0.364 (n=499)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1119 (IC base=+0.364)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1505` → IC=+0.378 (n=498)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1505 (IC base=+0.364)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1351` → IC=+0.381 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1351 (IC base=+0.364)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.371 (n=790)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.364)

- **PATRÓN** `ibs_15` > `0.7903` → IC=+0.393 (n=747)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7903 (IC base=+0.364)

- **PATRÓN** `dist_vwap_pct` > `0.1529` → IC=+0.381 (n=442)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1529 (IC base=+0.364)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.899` → IC=+0.399 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.899 (IC base=+0.364)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.367 (n=910)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.364)

- **PATRÓN** `libro_liquidez` > `3882.1799` → IC=+0.372 (n=668)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3882.1799 (IC base=+0.364)

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

- **PATRÓN** `ballena_activa_n` < `413.0` → IC=+0.388 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 413.0 (IC base=+0.361)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.369 (n=381)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.364)

- **PATRÓN** `sigma_h` > `0.006` → IC=+0.380 (n=173)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.006 (IC base=+0.364)

- **PATRÓN** `drift_60min` |x|≤ `0.1078` → IC=+0.367 (n=254)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1078 (IC base=+0.364)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0824` → IC=+0.374 (n=340)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0824 (IC base=+0.364)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2969` → IC=+0.375 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2969 (IC base=+0.364)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.367 (n=383)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.364)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.376 (n=175)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.364)

- **PATRÓN** `ibs_15` > `0.762` → IC=+0.393 (n=381)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.762 (IC base=+0.364)

- **PATRÓN** `dist_vwap_pct` > `0.1215` → IC=+0.372 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1215 (IC base=+0.364)

- **PATRÓN** `dist_vwap_pct` < `0.2797` → IC=+0.367 (n=351)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2797 (IC base=+0.364)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.889` → IC=+0.404 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.889 (IC base=+0.364)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.368 (n=431)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.364)

- **PATRÓN** `libro_liquidez` > `4142.643` → IC=+0.380 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4142.643 (IC base=+0.364)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0075` → IC=-0.196 (n=2700)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0075
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=2701)

- **FILTRO** `drift_15min` |x|> `0.9124` → IC=-0.145 (n=1349)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.9124
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=4051)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.218 (n=2274)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=3127)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1404` → IC=+0.220 (n=463)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1404 (IC base=-0.082)

- **PATRÓN** `ibs_15` > `0.6306` → IC=+0.279 (n=1222)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6306 (IC base=-0.082)

- **PATRÓN** `dist_vwap_pct` > `0.1099` → IC=+0.203 (n=714)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1099 (IC base=-0.082)

- **PATRÓN** `dist_vwap_pct` < `0.4172` → IC=+0.200 (n=1204)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4172 (IC base=-0.082)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2348` → IC=+0.268 (n=1639)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2348 (IC base=-0.005)

- **PATRÓN** `ibs_15` < `0.3703` → IC=+0.285 (n=4918)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3703 (IC base=-0.005)

- **PATRÓN** `dist_vwap_pct` > `0.6504` → IC=+0.280 (n=676)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6504 (IC base=-0.005)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0318` → IC=-0.222 (n=2555)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0318
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=852)

- **FILTRO** `sigma_ewma_delta_pct` > `22.158` → IC=-0.258 (n=481)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 22.158
  - _Potencial_: sin este filtro IC_bueno=-0.175 (n=2926)

- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.158 (n=328)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0031 (IC base=+0.071)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2675` → IC=+0.285 (n=142)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2675 (IC base=+0.071)

- **PATRÓN** `ibs_15` > `0.7609` → IC=+0.322 (n=426)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7609 (IC base=+0.071)

- **PATRÓN** `dist_vwap_pct` > `0.1023` → IC=+0.276 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1023 (IC base=+0.071)

- **PATRÓN** `dist_vwap_pct` < `0.4914` → IC=+0.284 (n=476)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4914 (IC base=+0.071)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.257` → IC=+0.149 (n=220)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 22.257 (IC base=+0.071)

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
  - _Potencial_: sin este filtro IC_bueno=+0.153 (n=799)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.162 (n=539)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0059 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.0722` → IC=+0.180 (n=270)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.0722 (IC base=+0.147)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3021` → IC=+0.197 (n=479)

  - _Acción_: Kelly boost +0.98€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3021 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.161 (n=438)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 11.0 (IC base=+0.147)

- **PATRÓN** `ibs_15` > `0.5671` → IC=+0.243 (n=612)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5671 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` > `0.6301` → IC=+0.158 (n=112)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.6301 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` < `0.2675` → IC=+0.150 (n=573)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.2675 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.973` → IC=+0.265 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.973 (IC base=+0.147)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=799)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `5033.9699` → IC=+0.156 (n=408)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 5033.9699 (IC base=+0.147)

- **PATRÓN** `sigma_h` < `0.0082` → IC=+0.249 (n=1881)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0082 (IC base=+0.243)

- **PATRÓN** `drift_60min` |x|≤ `0.3548` → IC=+0.249 (n=1655)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3548 (IC base=+0.243)

- **PATRÓN** `drift_15min` |x|≤ `0.7801` → IC=+0.257 (n=1655)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7801 (IC base=+0.243)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2145` → IC=+0.261 (n=853)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2145 (IC base=+0.243)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.254 (n=693)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.243)

- **PATRÓN** `ibs_15` < `0.1851` → IC=+0.305 (n=1254)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.1851 (IC base=+0.243)

- **PATRÓN** `dist_vwap_pct` > `0.3785` → IC=+0.271 (n=465)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3785 (IC base=+0.243)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.267` → IC=+0.248 (n=733)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.267 (IC base=+0.243)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.186` → IC=+0.249 (n=1965)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.186 (IC base=+0.243)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1043` → IC=-0.245 (n=629)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1043
  - _Potencial_: sin este filtro IC_bueno=-0.155 (n=630)

- **FILTRO** `drift_60min` |x|> `0.1723` → IC=-0.265 (n=428)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1723
  - _Potencial_: sin este filtro IC_bueno=-0.166 (n=831)

- **FILTRO** `drift_15min` |x|> `0.9101` → IC=-0.285 (n=314)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.9101
  - _Potencial_: sin este filtro IC_bueno=-0.172 (n=945)

- **FILTRO** `sigma_ewma_delta_pct` > `6.129` → IC=-0.203 (n=288)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.129
  - _Potencial_: sin este filtro IC_bueno=-0.199 (n=971)

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

- **PATRÓN** `delta_ratio_macro` |x|> `0.0642` → IC=+0.236 (n=840)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0642 (IC base=-0.031)

- **PATRÓN** `ibs_15` < `0.3814` → IC=+0.295 (n=841)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3814 (IC base=-0.031)

- **PATRÓN** `dist_vwap_pct` > `0.6765` → IC=+0.240 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6765 (IC base=-0.031)

- **PATRÓN** `dist_vwap_pct` < `0.1942` → IC=+0.247 (n=770)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1942 (IC base=-0.031)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.016` → IC=-0.247 (n=1029)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.016
  - _Potencial_: sin este filtro IC_bueno=-0.153 (n=508)

- **FILTRO** `libro_spread` > `0.04` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.04
  - _Potencial_: sin este filtro IC_bueno=-0.215 (n=1518)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.216)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.216)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1189` → IC=+0.300 (n=509)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1189 (IC base=-0.017)

- **PATRÓN** `ibs_15` < `0.1364` → IC=+0.309 (n=782)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.1364 (IC base=-0.017)

- **PATRÓN** `dist_vwap_pct` > `0.768` → IC=+0.337 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.768 (IC base=-0.017)

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
- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.303 (n=449)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0033 (IC base=+0.283)

- **PATRÓN** `drift_60min` |x|≤ `0.0725` → IC=+0.310 (n=592)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0725 (IC base=+0.283)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1533` → IC=+0.285 (n=896)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1533 (IC base=+0.283)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2227` → IC=+0.293 (n=819)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2227 (IC base=+0.283)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.296 (n=1391)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.283)

- **PATRÓN** `ibs_15` > `0.838` → IC=+0.312 (n=1345)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.838 (IC base=+0.283)

- **PATRÓN** `dist_vwap_pct` > `0.263` → IC=+0.314 (n=580)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.263 (IC base=+0.283)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.915` → IC=+0.389 (n=296)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.915 (IC base=+0.283)

- **PATRÓN** `libro_liquidez` > `13267.5913` → IC=+0.302 (n=448)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13267.5913 (IC base=+0.283)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.304 (n=238)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.276)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.275 (n=323)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.276)

- **PATRÓN** `drift_60min` |x|≤ `0.0588` → IC=+0.308 (n=238)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0588 (IC base=+0.276)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2702` → IC=+0.278 (n=237)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2702 (IC base=+0.276)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3948` → IC=+0.280 (n=638)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3948 (IC base=+0.276)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.294 (n=745)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.276)

- **PATRÓN** `ibs_15` > `0.829` → IC=+0.301 (n=711)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.829 (IC base=+0.276)

- **PATRÓN** `dist_vwap_pct` > `0.2502` → IC=+0.311 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2502 (IC base=+0.276)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.742` → IC=+0.393 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.742 (IC base=+0.276)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.277 (n=919)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.276)

- **PATRÓN** `libro_liquidez` > `15821.8878` → IC=+0.312 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15821.8878 (IC base=+0.276)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.299 (n=634)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0069 (IC base=+0.291)

- **PATRÓN** `drift_60min` |x|≤ `0.0515` → IC=+0.318 (n=212)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0515 (IC base=+0.291)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1408` → IC=+0.292 (n=422)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1408 (IC base=+0.291)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1007` → IC=+0.329 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1007 (IC base=+0.291)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.303 (n=608)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.291)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.296 (n=581)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.291)

- **PATRÓN** `ibs_15` > `0.8478` → IC=+0.321 (n=633)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8478 (IC base=+0.291)

- **PATRÓN** `dist_vwap_pct` > `0.2798` → IC=+0.316 (n=270)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2798 (IC base=+0.291)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.128` → IC=+0.380 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.128 (IC base=+0.291)

### UPDOWN_OU_5M
- **FILTRO** `delta_ratio_macro` |x|≤ `0.126` → IC=-0.156 (n=94)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.126
  - _Potencial_: sin este filtro IC_bueno=-0.103 (n=283)

- **FILTRO** `ballena_activa_n` > `33.0` → IC=-0.135 (n=258)

  - _Acción_: SKIP cuando `ballena_activa_n` > 33.0
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
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=163)

- **FILTRO** `drift_60min` |x|> `0.2379` → IC=-0.214 (n=19)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2379
  - _Potencial_: sin este filtro IC_bueno=-0.134 (n=39)

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
- **PATRÓN** `ratio` < `0.9702` → IC=+0.384 (n=386)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9702 (IC base=+0.166)

- **PATRÓN** `T_h` > `119.191` → IC=+0.354 (n=2839)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 119.191 (IC base=+0.336)

- **PATRÓN** `ratio` > `1.021` → IC=+0.387 (n=493)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.021 (IC base=+0.336)

### WEEKLY_PRICE#BTC
- **PATRÓN** `ratio` < `0.9933` → IC=+0.253 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9933 (IC base=+0.125)

- **PATRÓN** `T_h` > `111.9836` → IC=+0.317 (n=1024)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9836 (IC base=+0.300)

- **PATRÓN** `ratio` > `1.0177` → IC=+0.367 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0177 (IC base=+0.300)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `87.7391` → IC=+0.214 (n=316)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 87.7391 (IC base=+0.214)

- **PATRÓN** `ratio` < `0.9849` → IC=+0.410 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9849 (IC base=+0.214)

- **PATRÓN** `T_h` > `111.9969` → IC=+0.354 (n=1029)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9969 (IC base=+0.323)

- **PATRÓN** `ratio` > `1.0298` → IC=+0.403 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0298 (IC base=+0.323)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.0625` → IC=+0.418 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.0625 (IC base=+0.397)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5801 sube el IC de +0.142 a +0.226 en UPDOWN_GBM#15min (n=4746). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7086 sube el IC de +0.202 a +0.275 en UPDOWN_GBM#BTC#15min (n=788). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.4932 sube el IC de +0.131 a +0.216 en UPDOWN_GBM#ETH#15min (n=978). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5455 sube el IC de +0.154 a +0.228 en UPDOWN_GBM#XRP#15min (n=1183). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1089 sube el IC de +0.068 a +0.157 en UPDOWN_GBM#XRP#15min (n=1014). Ya aplicado como kelly_boost=+0.78€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6306 sube el IC de -0.082 a +0.279 en UPDOWN_GBM_15M_TARDIO (n=1222). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3703 sube el IC de -0.005 a +0.285 en UPDOWN_GBM_15M_TARDIO (n=4918). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7609 sube el IC de +0.071 a +0.322 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=426). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.6255 sube el IC de -0.187 a +0.289 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=74). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.5671 sube el IC de +0.147 a +0.243 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=612). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.1851 sube el IC de +0.243 a +0.305 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=1254). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de -0.200 a +0.234 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=62). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3814 sube el IC de -0.031 a +0.295 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=841). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.216 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.1364 sube el IC de -0.017 a +0.309 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=782). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_YES, IBS > 0.8434 sube el IC de +0.109 a +0.340 en UPDOWN_GBM_ETH_15M_HORA7 (n=23). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_YES, IBS > 0.8434 sube el IC de +0.109 a +0.340 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=23). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.838 sube el IC de +0.283 a +0.312 en UPDOWN_GBM_IBS_ALTO (n=1345). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.829 sube el IC de +0.276 a +0.301 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=711). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8478 sube el IC de +0.291 a +0.321 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=633). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7903 sube el IC de +0.364 a +0.393 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=747). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8112 sube el IC de +0.361 a +0.384 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=367). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.762 sube el IC de +0.364 a +0.393 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=381). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 2175 | +0.084 | +234.60€ | 1 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 2175 | +0.084 | +234.60€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1770 | +0.085 | +195.31€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1770 | +0.085 | +195.31€ | 1 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 284 | +0.070 | +11.30€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 284 | +0.070 | +11.30€ | 5 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 90 | +0.130 | +28.32€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 90 | +0.130 | +28.32€ | 1 | 10 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 1139 | -0.021 | +73.45€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 1139 | -0.021 | +73.45€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE | 7 | +0.019 | +3.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE#15min | 7 | +0.019 | +3.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 879 | -0.038 | +57.42€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 879 | -0.038 | +57.42€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 176 | +0.062 | +18.94€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 176 | +0.062 | +18.94€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 77 | -0.032 | -6.17€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 77 | -0.032 | -6.17€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 47134 | -0.084 | -5986.99€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 2905 | +0.070 | -297.27€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 44229 | -0.094 | -5689.73€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4803 | -0.113 | -801.56€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4803 | -0.113 | -801.56€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 2905 | +0.070 | -297.27€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 2905 | +0.070 | -297.27€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 4874 | -0.106 | -938.42€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 4874 | -0.106 | -938.42€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 12884 | -0.042 | -1184.02€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 12884 | -0.042 | -1184.02€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 12831 | -0.111 | -1320.89€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 12831 | -0.111 | -1320.89€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 8837 | -0.129 | -1444.84€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 8837 | -0.129 | -1444.84€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 48595 | -0.012 | +2845.67€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 12571 | +0.004 | +1517.69€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 36024 | -0.018 | +1327.97€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 48595 | -0.012 | +2845.67€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 12571 | +0.004 | +1517.69€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 36024 | -0.018 | +1327.97€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 186707 | +0.113 | -7752.27€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#15min | 21675 | +0.180 | -717.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 855 | +0.009 | -74.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 153514 | +0.105 | -6577.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 10663 | +0.093 | -382.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 25438 | +0.103 | -1793.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 76 | -0.179 | +10.07€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 25347 | +0.104 | -1791.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 35415 | +0.124 | -586.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5607 | +0.178 | -233.50€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 25415 | +0.120 | -175.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 4351 | +0.080 | -155.44€ | 1 | 2 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 25489 | +0.098 | -1846.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 86 | -0.114 | +7.00€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 25388 | +0.099 | -1842.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 39876 | +0.123 | -849.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 10044 | +0.178 | -251.78€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 25817 | +0.105 | -536.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 4003 | +0.103 | -53.03€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#SOL | 35023 | +0.112 | -1563.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 5774 | +0.198 | -257.48€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 758 | +0.035 | -20.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 26182 | +0.096 | -1111.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 2309 | +0.102 | -174.52€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO#XRP | 25466 | +0.107 | -1112.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 88 | -0.122 | +8.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 25365 | +0.108 | -1120.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 30249 | +0.193 | -2065.19€ | 2 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 30249 | +0.193 | -2065.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 6850 | +0.171 | -692.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 6850 | +0.171 | -692.96€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 4348 | +0.198 | -151.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 4348 | +0.198 | -151.56€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 6718 | +0.176 | -580.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 6718 | +0.176 | -580.88€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 5639 | +0.250 | -201.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 5639 | +0.250 | -201.84€ | 0 | 4 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 6615 | +0.185 | -451.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 6615 | +0.185 | -451.71€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 1232 | +0.425 | -45.93€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 1232 | +0.425 | -45.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 507 | +0.439 | -4.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 507 | +0.439 | -4.72€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE#15min | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 498 | +0.424 | -18.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 498 | +0.424 | -18.97€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 213 | +0.398 | -18.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 213 | +0.398 | -18.37€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 106991 | +0.200 | -7881.96€ | 3 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 106991 | +0.200 | -7881.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 18495 | +0.179 | -2095.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 18495 | +0.179 | -2095.34€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 17252 | +0.225 | -570.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 17252 | +0.225 | -570.03€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 18369 | +0.180 | -1963.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 18369 | +0.180 | -1963.41€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 17389 | +0.218 | -692.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 17389 | +0.218 | -692.52€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 17684 | +0.203 | -1119.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 17684 | +0.203 | -1119.24€ | 1 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 17802 | +0.196 | -1441.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 17802 | +0.196 | -1441.43€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 41220 | +0.117 | +347.49€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 41220 | +0.117 | +347.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 20523 | +0.117 | +203.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 20523 | +0.117 | +203.38€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 20697 | +0.117 | +144.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 20697 | +0.117 | +144.11€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 2565 | +0.292 | -14.76€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 2565 | +0.292 | -14.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 1175 | +0.281 | -30.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 1175 | +0.281 | -30.54€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 1251 | +0.296 | +10.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 1251 | +0.296 | +10.53€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 139 | +0.344 | +5.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 139 | +0.344 | +5.25€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 1183 | +0.438 | -4.13€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 1183 | +0.438 | -4.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 567 | +0.431 | -11.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 567 | +0.431 | -11.53€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 565 | +0.445 | +6.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 565 | +0.445 | +6.14€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 51 | +0.406 | +1.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 51 | +0.406 | +1.25€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1934 | +0.068 | -85.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 725 | +0.046 | -64.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 1209 | +0.081 | -21.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1500 | +0.075 | -40.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 291 | +0.053 | -19.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 1209 | +0.081 | -21.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 83501 | +0.101 | -1962.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 6729 | +0.096 | +141.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 76772 | +0.101 | -2103.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 45649 | +0.106 | -441.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 6729 | +0.096 | +141.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 38920 | +0.107 | -582.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 17727 | +0.109 | -104.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 17727 | +0.109 | -104.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 20125 | +0.082 | -1417.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 20125 | +0.082 | -1417.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 914 | +0.186 | -109.27€ | 5 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 914 | +0.186 | -109.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 914 | +0.186 | -109.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 914 | +0.186 | -109.27€ | 5 | 4 |
| ✅ GBM_LATE_15M | 56640 | +0.100 | +31560.58€ | 0 | 17 |
| ✅ GBM_LATE_15M#15min | 56640 | +0.100 | +31560.58€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 9375 | +0.227 | +8138.94€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 9375 | +0.227 | +8138.94€ | 0 | 22 |
| ✅ GBM_LATE_15M#BTC | 8667 | +0.176 | +6793.42€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 8667 | +0.176 | +6793.42€ | 0 | 22 |
| ✅ GBM_LATE_15M#DOGE | 10157 | +0.208 | +8047.53€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 10157 | +0.208 | +8047.53€ | 0 | 21 |
| ✅ GBM_LATE_15M#ETH | 7603 | +0.055 | +2421.65€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 7603 | +0.055 | +2421.65€ | 1 | 17 |
| ✅ GBM_LATE_15M#SOL | 7911 | -0.031 | +2034.18€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 7911 | -0.031 | +2034.18€ | 4 | 14 |
| ✅ GBM_LATE_15M#XRP | 12927 | -0.023 | +4124.86€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 12927 | -0.023 | +4124.86€ | 3 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 59671 | +0.085 | +34527.83€ | 0 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 59671 | +0.085 | +34527.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 11535 | -0.002 | +6130.73€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 11535 | -0.002 | +6130.73€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 12831 | +0.004 | +3391.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 12831 | +0.004 | +3391.76€ | 0 | 11 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 8120 | +0.295 | +9294.52€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 8120 | +0.295 | +9294.52€ | 0 | 22 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 11377 | +0.013 | +3506.85€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 11377 | +0.013 | +3506.85€ | 1 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 9176 | +0.043 | +4066.91€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 9176 | +0.043 | +4066.91€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 6632 | +0.316 | +8137.06€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 6632 | +0.316 | +8137.06€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 44855 | +0.178 | +36953.97€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 44855 | +0.178 | +36953.97€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 6750 | +0.240 | +6302.73€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 6750 | +0.240 | +6302.73€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 7110 | +0.138 | +5211.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 7110 | +0.138 | +5211.71€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 7213 | +0.225 | +6273.34€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 7213 | +0.225 | +6273.34€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 7688 | +0.129 | +5941.51€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 7688 | +0.129 | +5941.51€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 8486 | +0.118 | +6335.40€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 8486 | +0.118 | +6335.40€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 7608 | +0.233 | +6889.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 7608 | +0.233 | +6889.28€ | 0 | 24 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 12167 | +0.125 | +6046.43€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 12167 | +0.125 | +6046.43€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 505 | +0.163 | +341.50€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 505 | +0.163 | +341.50€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 3401 | +0.127 | +1847.75€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 3401 | +0.127 | +1847.75€ | 0 | 13 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 505 | +0.159 | +279.48€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 505 | +0.159 | +279.48€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 3553 | +0.124 | +1671.90€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 3553 | +0.124 | +1671.90€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 3166 | +0.099 | +1262.50€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 3166 | +0.099 | +1262.50€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 1037 | +0.167 | +643.30€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 1037 | +0.167 | +643.30€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO | 56828 | +0.188 | +46713.94€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#15min | 56828 | +0.188 | +46713.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 8961 | +0.252 | +8721.18€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 8961 | +0.252 | +8721.18€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 9037 | +0.136 | +6201.85€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 9037 | +0.136 | +6201.85€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 9644 | +0.236 | +8758.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 9644 | +0.236 | +8758.76€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 9404 | +0.141 | +6936.95€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 9404 | +0.141 | +6936.95€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 10090 | +0.121 | +7085.20€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 10090 | +0.121 | +7085.20€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 9692 | +0.241 | +9010.00€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 9692 | +0.241 | +9010.00€ | 0 | 19 |
| ✅ GBM_LATE_5M | 14388 | +0.211 | +11720.93€ | 1 | 26 |
| ✅ GBM_LATE_5M#5min | 14388 | +0.211 | +11720.93€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 1078 | +0.247 | +1027.08€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 1078 | +0.247 | +1027.08€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 3266 | +0.211 | +2814.84€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 3266 | +0.211 | +2814.84€ | 0 | 24 |
| ✅ GBM_LATE_5M#DOGE | 1453 | +0.210 | +1160.11€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1453 | +0.210 | +1160.11€ | 0 | 19 |
| ✅ GBM_LATE_5M#ETH | 4265 | +0.203 | +3188.08€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 4265 | +0.203 | +3188.08€ | 0 | 24 |
| ✅ GBM_LATE_5M#SOL | 2335 | +0.213 | +1962.88€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 2335 | +0.213 | +1962.88€ | 0 | 25 |
| ✅ GBM_LATE_5M#XRP | 1991 | +0.210 | +1567.94€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1991 | +0.210 | +1567.94€ | 0 | 0 |
| ✅ GBM_LATE_60M | 5017 | +0.052 | +1381.27€ | 0 | 5 |
| ✅ GBM_LATE_60M#60min | 5017 | +0.052 | +1381.27€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 1743 | +0.059 | +528.28€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 1743 | +0.059 | +528.28€ | 0 | 6 |
| ✅ GBM_LATE_60M#ETH | 1611 | +0.052 | +521.72€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 1611 | +0.052 | +521.72€ | 1 | 6 |
| ✅ GBM_LATE_60M#SOL | 1663 | +0.043 | +331.27€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 1663 | +0.043 | +331.27€ | 0 | 9 |
| 🚫 GBM_LATE_60M_FADE | 708 | -0.249 | -34.26€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 708 | -0.249 | -34.26€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 258 | -0.250 | -18.00€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 258 | -0.250 | -18.00€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 260 | -0.244 | -7.05€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 260 | -0.244 | -7.05€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 190 | -0.250 | -9.21€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 190 | -0.250 | -9.21€ | 8 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 2095 | +0.084 | +535.24€ | 0 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 2095 | +0.084 | +535.24€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 804 | +0.073 | +190.37€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 804 | +0.073 | +190.37€ | 1 | 4 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 749 | +0.058 | +145.65€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 749 | +0.058 | +145.65€ | 1 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 542 | +0.136 | +199.22€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 542 | +0.136 | +199.22€ | 1 | 9 |
| ✅ LATE_WINDOW_5MIN | 244 | +0.297 | +277.58€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 244 | +0.297 | +277.58€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 244 | +0.297 | +277.58€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 244 | +0.297 | +277.58€ | 1 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 4381 | +0.096 | +990.54€ | 0 | 1 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 4381 | +0.096 | +990.54€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 4381 | +0.096 | +990.54€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 4381 | +0.096 | +990.54€ | 0 | 1 |
| ✅ LIQUIDACIONES_15M | 1113 | -0.009 | +15.87€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 1113 | -0.009 | +15.87€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 71 | +0.021 | +0.22€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 71 | +0.021 | +0.22€ | 0 | 1 |
| ✅ LIQUIDACIONES_15M#BTC | 279 | -0.009 | +7.17€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 279 | -0.009 | +7.17€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 44 | -0.087 | -4.08€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 44 | -0.087 | -4.08€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 291 | +0.019 | +18.01€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 291 | +0.019 | +18.01€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 313 | -0.014 | +1.05€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 313 | -0.014 | +1.05€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 115 | -0.047 | -6.50€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 115 | -0.047 | -6.50€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 4190 | +0.017 | +125.59€ | 5 | 1 |
| ✅ LIQUIDACIONES_5M#5min | 4190 | +0.017 | +125.59€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 213 | +0.021 | -1.88€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 213 | +0.021 | -1.88€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 826 | +0.016 | +41.72€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 826 | +0.016 | +41.72€ | 1 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 249 | +0.026 | +25.95€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 249 | +0.026 | +25.95€ | 0 | 6 |
| ✅ LIQUIDACIONES_5M#ETH | 1655 | +0.019 | +28.33€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1655 | +0.019 | +28.33€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 769 | +0.011 | +1.89€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 769 | +0.011 | +1.89€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 478 | +0.015 | +29.59€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 478 | +0.015 | +29.59€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 2360 | -0.033 | -7.73€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 2360 | -0.033 | -7.73€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 715 | -0.030 | -10.38€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 715 | -0.030 | -10.38€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 838 | -0.009 | +18.00€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 838 | -0.009 | +18.00€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 807 | -0.059 | -15.36€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 807 | -0.059 | -15.36€ | 5 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 15372 | -0.031 | -102.20€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 7387 | -0.033 | -63.94€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 7985 | -0.030 | -38.26€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 541 | -0.054 | -32.02€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 278 | -0.029 | +0.26€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 263 | -0.081 | -32.28€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 4020 | -0.025 | -3.27€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 1907 | -0.023 | +9.30€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 2113 | -0.026 | -12.57€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 1502 | -0.029 | +16.90€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 771 | -0.033 | +0.84€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 731 | -0.024 | +16.06€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 3470 | -0.034 | -57.05€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 1640 | -0.038 | -40.36€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 1830 | -0.031 | -16.69€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 2954 | -0.022 | +51.58€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 1431 | -0.025 | +14.97€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 1523 | -0.019 | +36.61€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 2885 | -0.043 | -78.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 1360 | -0.049 | -48.95€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 1525 | -0.037 | -29.39€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 67229 | -0.001 | +3580.03€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 67229 | -0.001 | +3580.03€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 12181 | +0.027 | +1656.40€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 12181 | +0.027 | +1656.40€ | 2 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 9399 | -0.037 | -141.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 9399 | -0.037 | -141.54€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 12320 | +0.025 | +1374.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 12320 | +0.025 | +1374.80€ | 1 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 9334 | -0.052 | -240.57€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 9334 | -0.052 | -240.57€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 11463 | -0.004 | +315.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 11463 | -0.004 | +315.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 12532 | +0.017 | +615.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 12532 | +0.017 | +615.19€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 7161 | -0.054 | -116.58€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 7161 | -0.054 | -116.58€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1247 | -0.002 | -15.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1247 | -0.002 | -15.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1985 | -0.063 | -24.58€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1985 | -0.063 | -24.58€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 79 | -0.018 | -0.18€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 79 | -0.018 | -0.18€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 809 | -0.120 | -35.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 809 | -0.120 | -35.98€ | 5 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 2178 | -0.068 | -13.12€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 2178 | -0.068 | -13.12€ | 2 | 0 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 164730 | -0.078 | +2178.20€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 164730 | -0.078 | +2178.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 28855 | -0.078 | +1709.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 28855 | -0.078 | +1709.05€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 24621 | -0.102 | -1279.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 24621 | -0.102 | -1279.49€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 29225 | -0.068 | +1430.48€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 29225 | -0.068 | +1430.48€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 24165 | -0.099 | -760.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 24165 | -0.099 | -760.89€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 29437 | -0.059 | +277.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 29437 | -0.059 | +277.50€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 28427 | -0.070 | +801.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 28427 | -0.070 | +801.55€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 9058 | -0.035 | -182.13€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 9058 | -0.035 | -182.13€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 1008 | -0.017 | -19.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 1008 | -0.017 | -19.32€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 2111 | -0.047 | -28.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 2111 | -0.047 | -28.20€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2645 | -0.025 | -37.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2645 | -0.025 | -37.30€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1271 | -0.064 | -31.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1271 | -0.064 | -31.87€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 1014 | -0.032 | -33.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 1014 | -0.032 | -33.50€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 2153 | +0.119 | +850.08€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#5min | 2017 | +0.123 | +837.49€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 481 | +0.134 | +233.57€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 481 | +0.134 | +233.57€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#DOGE | 410 | +0.119 | +144.62€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 410 | +0.119 | +144.62€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#ETH | 380 | +0.123 | +167.50€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 380 | +0.123 | +167.50€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 343 | +0.141 | +175.20€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 343 | +0.141 | +175.20€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#XRP | 403 | +0.098 | +116.59€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 403 | +0.098 | +116.59€ | 0 | 2 |
| ✅ ORDER_FLOW_5M_REACTIVO | 2171 | -0.016 | -19.00€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 2171 | -0.016 | -19.00€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 398 | +0.015 | +26.81€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 398 | +0.015 | +26.81€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 399 | -0.044 | -25.67€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 399 | -0.044 | -25.67€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 548 | -0.035 | -25.49€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 548 | -0.035 | -25.49€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 438 | -0.004 | -2.70€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 438 | -0.004 | -2.70€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 388 | -0.008 | +8.04€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 388 | -0.008 | +8.04€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 1157 | -0.068 | -24.76€ | 3 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 535 | -0.103 | -69.04€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 414 | -0.115 | -48.49€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 121 | -0.061 | -20.55€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 404 | -0.027 | +30.89€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 289 | -0.012 | +38.89€ | 1 | 2 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 115 | -0.064 | -8.00€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 218 | -0.054 | +13.39€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 182 | -0.049 | +11.56€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 36 | -0.079 | +1.84€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 885 | -0.068 | +1.96€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 272 | -0.066 | -26.71€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 1461 | -0.203 | -85.53€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 577 | -0.200 | -46.21€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 507 | -0.197 | -41.75€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#reach | 70 | -0.208 | -4.45€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 488 | -0.208 | -37.50€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 426 | -0.220 | -44.65€ | 4 | 1 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 62 | -0.125 | +7.14€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL | 396 | -0.201 | -1.82€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 366 | -0.198 | -3.97€ | 5 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 30 | -0.219 | +2.15€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 1299 | -0.206 | -90.37€ | 0 | 0 |
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
| ✅ STREAK_FADE_15M | 939 | +0.041 | +78.21€ | 2 | 2 |
| ✅ STREAK_FADE_15M#15min | 939 | +0.041 | +78.21€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 355 | +0.021 | +4.48€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 355 | +0.021 | +4.48€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 73 | +0.020 | +1.57€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 73 | +0.020 | +1.57€ | 1 | 1 |
| ✅ STREAK_FADE_15M#SOL | 83 | +0.018 | +6.06€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 83 | +0.018 | +6.06€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 428 | +0.065 | +66.10€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 428 | +0.065 | +66.10€ | 1 | 2 |
| ✅ STREAK_FADE_5M | 3572 | -0.023 | -143.04€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3572 | -0.023 | -143.04€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 1127 | -0.023 | -40.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 1127 | -0.023 | -40.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 612 | -0.029 | -27.74€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 612 | -0.029 | -27.74€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 171 | -0.043 | -14.80€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 171 | -0.043 | -14.80€ | 4 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1662 | -0.019 | -60.29€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1662 | -0.019 | -60.29€ | 2 | 0 |
| ✅ STREAK_FADE_60M | 118 | -0.050 | -12.20€ | 5 | 0 |
| ✅ STREAK_FADE_60M#60min | 118 | -0.050 | -12.20€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 44 | -0.087 | -4.62€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 44 | -0.087 | -4.62€ | 4 | 0 |
| ✅ STREAK_FADE_60M#SOL | 74 | -0.026 | -7.58€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 74 | -0.026 | -7.58€ | 0 | 1 |
| ✅ STREAK_MOM_5M | 11512 | +0.014 | +73.34€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 11512 | +0.014 | +73.34€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2995 | +0.018 | +24.38€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2995 | +0.018 | +24.38€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 3009 | +0.016 | +32.83€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 3009 | +0.016 | +32.83€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2927 | +0.009 | -2.09€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2927 | +0.009 | -2.09€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2581 | +0.014 | +18.23€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2581 | +0.014 | +18.23€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 11922 | +0.018 | -6.92€ | 4 | 0 |
| ✅ STRUCT_NO_15M#15min | 11922 | +0.018 | -6.92€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 4960 | +0.020 | +2.59€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 4960 | +0.020 | +2.59€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 4092 | +0.016 | -8.76€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 4092 | +0.016 | -8.76€ | 4 | 0 |
| ✅ STRUCT_NO_15M#SOL | 2870 | +0.015 | -0.75€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 2870 | +0.015 | -0.75€ | 1 | 0 |
| ✅ UPDOWN_GBM | 105842 | +0.060 | +10094.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 25827 | +0.079 | +5231.86€ | 0 | 10 |
| ✅ UPDOWN_GBM#240min | 3140 | -0.000 | +34.04€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 70229 | +0.062 | +4719.31€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 6280 | -0.001 | +114.69€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 8705 | +0.105 | +1608.71€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1781 | +0.164 | +820.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 90 | -0.011 | -2.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 6834 | +0.091 | +790.51€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 24175 | +0.057 | +2137.64€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 3461 | +0.078 | +773.99€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 894 | +0.000 | +17.77€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 16879 | +0.067 | +1267.34€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 2808 | -0.004 | +74.30€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 133 | -0.063 | +4.24€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 11497 | +0.079 | +1320.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1761 | +0.154 | +738.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 86 | +0.023 | -0.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 9650 | +0.065 | +583.26€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 25176 | +0.050 | +1760.89€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 6097 | +0.072 | +925.97€ | 0 | 9 |
| ✅ UPDOWN_GBM#ETH#240min | 864 | +0.005 | +16.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 15785 | +0.052 | +780.34€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 2308 | +0.002 | +37.17€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 122 | -0.105 | +1.22€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 22528 | +0.040 | +1280.12€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 6909 | +0.032 | +431.99€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#240min | 809 | -0.011 | +4.56€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 13537 | +0.051 | +849.01€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 1164 | +0.000 | +3.22€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#daily | 109 | -0.140 | -8.66€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 13759 | +0.073 | +1988.50€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 5818 | +0.094 | +1541.28€ | 0 | 10 |
| ✅ UPDOWN_GBM#XRP#240min | 397 | +0.006 | -1.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 7544 | +0.061 | +448.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 364 | -0.101 | -3.19€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 996 | +0.364 | +364.33€ | 0 | 10 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 996 | +0.364 | +364.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 489 | +0.361 | +170.29€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 489 | +0.361 | +170.29€ | 0 | 9 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 507 | +0.364 | +194.04€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 507 | +0.364 | +194.04€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO | 25307 | -0.021 | +6257.83€ | 3 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 25307 | -0.021 | +6257.83€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1981 | -0.051 | +561.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1981 | -0.051 | +561.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 4716 | -0.115 | +228.01€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 4716 | -0.115 | +228.01€ | 2 | 11 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 1071 | +0.222 | +899.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 1071 | +0.222 | +899.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 3323 | +0.220 | +2131.79€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 3323 | +0.220 | +2131.79€ | 1 | 19 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 7178 | -0.061 | +1053.75€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 7178 | -0.061 | +1053.75€ | 4 | 8 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 7038 | -0.060 | +1383.23€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 7038 | -0.060 | +1383.23€ | 2 | 5 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 309 | +0.059 | +27.08€ | 0 | 10 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 309 | +0.059 | +27.08€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 309 | +0.059 | +27.08€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 309 | +0.059 | +27.08€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1792 | +0.283 | +1502.40€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1792 | +0.283 | +1502.40€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 948 | +0.276 | +742.93€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 948 | +0.276 | +742.93€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 844 | +0.291 | +759.47€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 844 | +0.291 | +759.47€ | 0 | 9 |
| ✅ UPDOWN_OU_5M | 868 | -0.115 | -87.81€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 868 | -0.115 | -87.81€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 275 | -0.085 | -21.89€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 275 | -0.085 | -21.89€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 97 | -0.177 | -11.96€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 97 | -0.177 | -11.96€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 113 | -0.178 | -4.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 113 | -0.178 | -4.61€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 38 | -0.175 | -6.61€ | 2 | 0 |
| ✅ WEEKLY_PRICE | 4702 | +0.300 | +2113.75€ | 0 | 3 |
| ✅ WEEKLY_PRICE#BTC | 1796 | +0.256 | +226.16€ | 0 | 3 |
| ✅ WEEKLY_PRICE#ETH | 1814 | +0.295 | +770.40€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 1092 | +0.381 | +1117.20€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**✅ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: n≥15 y IC<-0.05
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: IC=+0.023 n=1310 — no justifica filtro, seguir monitorizando
  - _Datos_: n=1310 IC=+0.023 PNL=+69.26€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 810 celda(s) pasan gate riguroso completo de 2898 evaluadas (n>=40) y 4017 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.032 < 0.08 — monitorear
  - _Datos_: n=6906 IC=+0.032 PNL=+431.33€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=1814/15 IC=+0.295 PNL=+770.40€ | BTC: n=1796/15 IC=+0.256 PNL=+226.16€ | SOL: n=1092/15 IC=+0.381 PNL=+1117.20€

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
  - _Estado_: alineada_con_outcome_prev IC=+0.141 n=1056/60 | contraria IC=+0.184 n=1111 | gap=-0.043 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=590, boost estimado=+0.012. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 0/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=2306/40 IC=+0.002 PNL=+37.22€ | BTC#60min: n=2806/40 IC=-0.004 PNL=+74.28€ | SOL#60min: n=1163/40 IC=+0.000 PNL=+3.78€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.045 n=726740 | tras_1loss IC=+0.100 n=551119 | tras_2loss IC=+0.070 n=220509/40 | gap=-0.025 (umbral 0.05)

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.134 > 0.08 con n=1254 PNL=+595.52€
  - _Datos_: n=1254 IC=+0.134 PNL=+595.52€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.334 > 0.1 con n=3829 PNL=+2119.52€
  - _Datos_: n=3829 IC=+0.334 PNL=+2119.52€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=1074 IC=+0.067 PNL=+107.03€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1074 IC=+0.067 PNL=+107.03€

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
  - _Estado_: n=4193 IC=+0.001 PNL=-20.92€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=4193 IC=+0.001 PNL=-20.92€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=2082 IC=-0.004 PNL=+136.20€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=2082 IC=-0.004 PNL=+136.20€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=1310 IC=+0.023 PNL=+69.26€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=1310 IC=+0.023 PNL=+69.26€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.142 > 0.1 con n=7076 PNL=+3573.53€
  - _Datos_: n=7076 IC=+0.142 PNL=+3573.53€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=3459 IC=+0.078 PNL=+772.50€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=3459 IC=+0.078 PNL=+772.50€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.297 n=244) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=244 IC=+0.297 PNL=+277.58€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.117 > 0.02 con n=1263 PNL=+502.92€
  - _Datos_: n=1263 IC=+0.117 PNL=+502.92€

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
  - _Estado_: n=43422 IC=+0.073 PNL=+6010.81€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=43422 IC=+0.073 PNL=+6010.81€

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
  - _Estado_: n=4051 IC=+0.068 PNL=+521.05€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=4051 IC=+0.068 PNL=+521.05€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=187 IC=-0.093 PNL=+0.97€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=187 IC=-0.093 PNL=+0.97€

**〰️ H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: n=1100 IC=+0.100 PNL=+273.61€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=1100 IC=+0.100 PNL=+273.61€

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
  - _Estado_: n=43078 IC=-0.137 PNL=+2762.45€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=43078 IC=-0.137 PNL=+2762.45€

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
  - _Estado_: n=4477 IC=+0.130 PNL=+2932.78€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=4477 IC=+0.130 PNL=+2932.78€

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
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.220 < -0.1 con n=4712 PNL=-382.08€
  - _Datos_: n=4712 IC=-0.220 PNL=-382.08€

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
  - _Estado_: n=106 IC=+0.046 PNL=+18.93€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=106 IC=+0.046 PNL=+18.93€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.095 n=2225) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=2225 IC=+0.095 PNL=+441.72€

**⏳ H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.414 n=683) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=683 IC=+0.414 PNL=+997.20€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=18487 IC=+0.179 PNL=-2094.43€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=18487 IC=+0.179 PNL=-2094.43€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.233 > 0.1 con n=290 PNL=+203.84€
  - _Datos_: n=290 IC=+0.233 PNL=+203.84€
