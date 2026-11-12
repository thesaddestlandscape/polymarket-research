# Hipótesis automáticas — 2026-11-12 09:40 UTC
_Generado por shadow_postmortem.py sobre 1301317 resoluciones (PNL=+178234.90€)_

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
- **FILTRO** `restante_s_al_confirmar` < `132.2` → IC=-0.220 (n=11899)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 132.2
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=35704)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `125.1` → IC=-0.259 (n=1205)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 125.1
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=3615)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `116.46` → IC=-0.287 (n=1219)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 116.46
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=3658)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `restante_s_al_confirmar` < `116.78` → IC=-0.168 (n=3267)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 116.78
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=9804)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `152.07` → IC=-0.241 (n=3240)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 152.07
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=9720)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `128.75` → IC=-0.263 (n=2227)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 128.75
  - _Potencial_: sin este filtro IC_bueno=-0.084 (n=6682)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.210 (n=27935)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.104)

- **PATRÓN** `libro_liquidez` > `8278.0847` → IC=+0.158 (n=2333)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 8278.0847 (IC base=+0.104)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.128 (n=24102)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 17.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.130 (n=29348)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.124)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.225 (n=22029)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.140 (n=8330)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `6504.5601` → IC=+0.143 (n=3223)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 6504.5601 (IC base=+0.124)

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
  - _Potencial_: sin este filtro IC_bueno=+0.095 (n=2219)

- **PATRÓN** `py_entrada` > `0.61` → IC=+0.166 (n=611)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` > 0.61 (IC base=+0.077)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.145 (n=1426)

  - _Acción_: Kelly boost +0.72€ cuando `py_entrada` < 0.44 (IC base=+0.083)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.170 (n=5332)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 5.0 (IC base=+0.166)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.170 (n=4503)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 15.0 (IC base=+0.166)

- **PATRÓN** `py_entrada` > `0.77` → IC=+0.374 (n=1755)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.77 (IC base=+0.166)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.209 (n=2406)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.202)

- **PATRÓN** `py_entrada` < `0.275` → IC=+0.331 (n=951)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.275 (IC base=+0.202)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.205 (n=2807)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.202)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.142 (n=647)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 15.0 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.146 (n=1164)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 15.0 (IC base=+0.141)

- **PATRÓN** `py_entrada` > `0.675` → IC=+0.255 (n=442)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.675 (IC base=+0.141)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.145 (n=1110)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.156 (n=155)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.073)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.250 (n=949)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.227)

- **PATRÓN** `py_entrada` > `0.83` → IC=+0.420 (n=1324)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.83 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.146 (n=1426)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 7.0 (IC base=+0.145)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.156 (n=733)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 7.0 (IC base=+0.145)

- **PATRÓN** `py_entrada` < `0.345` → IC=+0.278 (n=717)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.345 (IC base=+0.145)

### FAVORITO_CONFIRMADO#SOL#60min
- **FILTRO** `libro_liquidez` < `952.1685` → IC=-0.125 (n=158)

  - _Acción_: SKIP cuando `libro_liquidez` < 952.1685
  - _Potencial_: sin este filtro IC_bueno=+0.066 (n=323)

- **PATRÓN** `py_entrada` > `0.55` → IC=+0.164 (n=462)

  - _Acción_: Kelly boost +0.82€ cuando `py_entrada` > 0.55 (IC base=+0.046)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.148 (n=478)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 17.0 (IC base=+0.122)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.249 (n=432)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.122)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `10.0` → IC=-0.297 (n=72)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.232 (n=151)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.201 (n=24110)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.195)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.197 (n=20395)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 15.0 (IC base=+0.195)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.229 (n=7644)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.195)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.338 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.195)

- **PATRÓN** `libro_liquidez` > `4915.142` → IC=+0.338 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4915.142 (IC base=+0.195)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.174 (n=5501)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 5.0 (IC base=+0.169)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.169 (n=5489)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 18.0 (IC base=+0.169)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.180 (n=5477)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` < 0.74 (IC base=+0.169)

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

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.212 (n=3270)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.209)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.212 (n=2181)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.209)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.250 (n=1629)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.209)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.184 (n=5374)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.178 (n=4568)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 15.0 (IC base=+0.176)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.177 (n=5531)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` < 0.73 (IC base=+0.176)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.184 (n=4214)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` > 0.71 (IC base=+0.176)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.257 (n=4522)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.251)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.251 (n=3827)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.251)

- **PATRÓN** `py_entrada` > `0.8` → IC=+0.363 (n=1455)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.190 (n=5273)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.186)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.190 (n=4472)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 15.0 (IC base=+0.186)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.196 (n=1768)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` > 0.73 (IC base=+0.186)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.429 (n=971)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.425)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.426 (n=962)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.425)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.437 (n=980)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.425)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.431 (n=1035)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.425)

- **PATRÓN** `libro_liquidez` > `4626.5104` → IC=+0.441 (n=625)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4626.5104 (IC base=+0.425)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.439 (n=393)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.439)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.441 (n=403)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.439)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.447 (n=433)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.439)

- **PATRÓN** `libro_liquidez` > `12485.1016` → IC=+0.443 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12485.1016 (IC base=+0.439)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.430 (n=384)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.423)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.427 (n=380)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.423)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.442 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.423)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.429 (n=432)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.423)

- **PATRÓN** `libro_liquidez` > `4792.7768` → IC=+0.422 (n=127)

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
- **FILTRO** `hora_utc` > `14.0` → IC=-0.324 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.257 (n=35)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=34)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.205 (n=31591)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.239 (n=31880)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.200)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.187 (n=4719)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 18.0 (IC base=+0.178)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.179 (n=10121)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 12.0 (IC base=+0.178)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.188 (n=14521)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` > 0.71 (IC base=+0.178)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.226 (n=13202)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.224)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.285 (n=4468)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.224)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.183 (n=13231)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 7.0 (IC base=+0.179)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.197 (n=11210)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` > 0.72 (IC base=+0.179)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.835` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.835
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.227 (n=4425)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.219)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.222 (n=5087)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.219)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.254 (n=7324)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.219)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **FILTRO** `hora_utc` > `3.0` → IC=-0.278 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.205 (n=12758)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.256 (n=4607)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.202 (n=5252)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.198 (n=5253)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 6.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.240 (n=6626)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.196)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.194 (n=11385)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.141 (n=12002)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `3.42` → IC=+0.139 (n=13852)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 3.42 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.194 (n=5549)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.145 (n=5415)

  - _Acción_: Kelly boost +0.72€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.125 (n=6983)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 7.0 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `4.14` → IC=+0.141 (n=6897)

  - _Acción_: Kelly boost +0.71€ cuando `lag_apertura_s` < 4.14 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.193 (n=5836)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.138 (n=7315)

  - _Acción_: Kelly boost +0.69€ cuando `restante_min` > 4.95 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `3.11` → IC=+0.138 (n=6959)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 3.11 (IC base=+0.116)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.307 (n=1395)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.293)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.387 (n=717)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.293)

- **PATRÓN** `libro_liquidez` > `3976.0278` → IC=+0.293 (n=884)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3976.0278 (IC base=+0.293)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.286 (n=937)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.282)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.365 (n=309)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.282)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.319 (n=677)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.298)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.302 (n=993)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.298)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.395 (n=341)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.298)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` < `16.0` → IC=+0.367 (n=96)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.345)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.388 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.345)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.381 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.345)

- **PATRÓN** `libro_liquidez` > `761.0655` → IC=+0.375 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 761.0655 (IC base=+0.345)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.441 (n=950)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.438)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.443 (n=921)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.438)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.437 (n=445)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.432)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.436 (n=310)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.432)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.437 (n=461)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.432)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.451 (n=305)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.443)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.443 (n=387)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.443)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.444 (n=424)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.443)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4787` → IC=+0.140 (n=17896)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.4787 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.128 (n=18082)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 6.0 (IC base=+0.123)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.126 (n=12479)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 12.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` > `0.9767` → IC=+0.246 (n=5965)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9767 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` > `0.7954` → IC=+0.285 (n=988)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7954 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.484` → IC=+0.187 (n=8960)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 3.484 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` > `0.626` → IC=+0.265 (n=5376)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.626 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` > `0.3043` → IC=+0.251 (n=1849)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3043 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` > `2.7521` → IC=+0.235 (n=4294)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7521 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.136 (n=8867)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `4662.5332` → IC=+0.149 (n=5965)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 4662.5332 (IC base=+0.123)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.123 (n=11215)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0062 (IC base=+0.084)

- **PATRÓN** `ibs_20min` < `0.565` → IC=+0.144 (n=22362)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.565 (IC base=+0.084)

- **PATRÓN** `dist_vwap_pct` > `0.6154` → IC=+0.191 (n=1491)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.6154 (IC base=+0.084)

- **PATRÓN** `volumen_regimen` < `0.6968` → IC=+0.199 (n=4033)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_regimen` < 0.6968 (IC base=+0.084)

- **PATRÓN** `volumen_pendiente_norm` > `0.2964` → IC=+0.233 (n=2247)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2964 (IC base=+0.084)

- **PATRÓN** `volumen_spike_ratio` > `2.6719` → IC=+0.213 (n=5182)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6719 (IC base=+0.084)

- **PATRÓN** `ballena_activa_n` < `99.0` → IC=+0.230 (n=15451)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 99.0 (IC base=+0.084)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `drift_60min` |x|≤ `0.3657` → IC=+0.213 (n=3811)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3657 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.227 (n=1850)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.211)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.211 (n=2560)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` > `0.9857` → IC=+0.278 (n=1729)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9857 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.441` → IC=+0.279 (n=1698)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.441 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.2333` → IC=+0.260 (n=680)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2333 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `1.4374` → IC=+0.213 (n=3654)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4374 (IC base=+0.211)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.224 (n=4212)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `2037.07` → IC=+0.212 (n=1270)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2037.07 (IC base=+0.211)

- **PATRÓN** `ballena_activa_n` < `26.0` → IC=+0.224 (n=3473)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 26.0 (IC base=+0.211)

- **PATRÓN** `sigma_h` > `0.0093` → IC=+0.246 (n=1523)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0093 (IC base=+0.244)

- **PATRÓN** `drift_60min` |x|≤ `0.0893` → IC=+0.281 (n=1121)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0893 (IC base=+0.244)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.250 (n=1255)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.244)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.250 (n=1553)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.244)

- **PATRÓN** `ibs_20min` < `0.5663` → IC=+0.261 (n=3359)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5663 (IC base=+0.244)

- **PATRÓN** `volumen_pendiente_norm` < `0.0722` → IC=+0.248 (n=2887)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0722 (IC base=+0.244)

- **PATRÓN** `volumen_pendiente_norm` > `0.2892` → IC=+0.252 (n=450)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2892 (IC base=+0.244)

- **PATRÓN** `volumen_spike_ratio` < `1.4468` → IC=+0.245 (n=1070)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4468 (IC base=+0.244)

- **PATRÓN** `volumen_spike_ratio` > `1.8593` → IC=+0.248 (n=2138)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8593 (IC base=+0.244)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.246 (n=3874)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.244)

- **PATRÓN** `libro_liquidez` > `1774.3788` → IC=+0.250 (n=2239)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1774.3788 (IC base=+0.244)

- **PATRÓN** `ballena_activa_n` < `6.0` → IC=+0.246 (n=1140)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 6.0 (IC base=+0.244)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.235 (n=1073)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.224)

- **PATRÓN** `drift_60min` |x|≤ `0.1096` → IC=+0.252 (n=1415)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1096 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.235 (n=3362)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.226 (n=2285)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` > `0.9018` → IC=+0.257 (n=1071)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9018 (IC base=+0.224)

- **PATRÓN** `dist_vwap_pct` > `0.1851` → IC=+0.234 (n=1452)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1851 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.787` → IC=+0.265 (n=471)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.787 (IC base=+0.224)

- **PATRÓN** `volumen_regimen` > `0.629` → IC=+0.230 (n=3212)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.629 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` > `0.2787` → IC=+0.269 (n=444)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2787 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` > `2.4491` → IC=+0.248 (n=1057)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4491 (IC base=+0.224)

- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.153 (n=3434)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0064 (IC base=+0.131)

- **PATRÓN** `drift_60min` |x|≤ `0.0777` → IC=+0.156 (n=1146)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.0777 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.152 (n=1282)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 17.0 (IC base=+0.131)

- **PATRÓN** `ibs_20min` < `0.3536` → IC=+0.202 (n=2289)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3536 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.981` → IC=+0.138 (n=3137)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 3.981 (IC base=+0.131)

- **PATRÓN** `volumen_regimen` < `0.6337` → IC=+0.154 (n=1146)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.6337 (IC base=+0.131)

- **PATRÓN** `volumen_pendiente_norm` > `0.0719` → IC=+0.155 (n=1405)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` > 0.0719 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` < `2.4423` → IC=+0.142 (n=3307)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.4423 (IC base=+0.131)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.131 (n=4459)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.01 (IC base=+0.131)

- **PATRÓN** `ballena_activa_n` < `175.0` → IC=+0.184 (n=1082)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 175.0 (IC base=+0.131)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.208 (n=2690)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0097 (IC base=+0.196)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.203 (n=4233)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.196)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.261 (n=1567)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.196)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.975` → IC=+0.281 (n=885)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.975 (IC base=+0.196)

- **PATRÓN** `volumen_pendiente_norm` < `0.0975` → IC=+0.198 (n=3615)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` < 0.0975 (IC base=+0.196)

- **PATRÓN** `volumen_pendiente_norm` > `0.3524` → IC=+0.230 (n=523)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3524 (IC base=+0.196)

- **PATRÓN** `volumen_spike_ratio` > `2.7284` → IC=+0.214 (n=1787)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7284 (IC base=+0.196)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.200 (n=4878)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.196)

- **PATRÓN** `libro_liquidez` > `2014.5584` → IC=+0.202 (n=1345)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2014.5584 (IC base=+0.196)

- **PATRÓN** `sigma_h` < `0.0111` → IC=+0.225 (n=3281)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0111 (IC base=+0.221)

- **PATRÓN** `drift_60min` |x|≤ `0.2922` → IC=+0.234 (n=2487)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2922 (IC base=+0.221)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.242 (n=1416)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.221)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.226 (n=1699)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.221)

- **PATRÓN** `ibs_20min` < `0.0476` → IC=+0.270 (n=1243)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0476 (IC base=+0.221)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.771` → IC=+0.261 (n=403)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.771 (IC base=+0.221)

- **PATRÓN** `volumen_pendiente_norm` > `0.3479` → IC=+0.257 (n=540)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3479 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` < `1.7653` → IC=+0.218 (n=1579)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7653 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` > `2.1586` → IC=+0.230 (n=2392)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1586 (IC base=+0.221)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.222 (n=1892)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.221)

- **PATRÓN** `libro_liquidez` > `1887.0196` → IC=+0.225 (n=1691)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1887.0196 (IC base=+0.221)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.226 (n=3549)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 24.0 (IC base=+0.221)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.178 (n=212)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=4856)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.150 (n=666)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0039 (IC base=+0.060)

- **PATRÓN** `ibs_20min` > `0.9414` → IC=+0.234 (n=666)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9414 (IC base=+0.060)

- **PATRÓN** `dist_vwap_pct` > `0.1402` → IC=+0.340 (n=461)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1402 (IC base=+0.060)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.086` → IC=+0.204 (n=1463)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.086 (IC base=+0.060)

- **PATRÓN** `volumen_regimen` > `1.1051` → IC=+0.351 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1051 (IC base=+0.060)

- **PATRÓN** `volumen_pendiente_norm` < `0.1678` → IC=+0.338 (n=644)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1678 (IC base=+0.060)

- **PATRÓN** `volumen_pendiente_norm` > `0.3054` → IC=+0.336 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3054 (IC base=+0.060)

- **PATRÓN** `volumen_spike_ratio` < `1.421` → IC=+0.351 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.421 (IC base=+0.060)

- **PATRÓN** `volumen_spike_ratio` > `2.2934` → IC=+0.342 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2934 (IC base=+0.060)

- **PATRÓN** `ballena_activa_n` < `142.0` → IC=+0.339 (n=789)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 142.0 (IC base=+0.060)

- **PATRÓN** `ibs_20min` < `0.0868` → IC=+0.188 (n=1268)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.0868 (IC base=+0.054)

- **PATRÓN** `dist_vwap_pct` > `0.3367` → IC=+0.163 (n=618)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 0.3367 (IC base=+0.054)

- **PATRÓN** `volumen_regimen` < `1.0062` → IC=+0.161 (n=2142)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.0062 (IC base=+0.054)

- **PATRÓN** `volumen_pendiente_norm` > `0.2807` → IC=+0.209 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2807 (IC base=+0.054)

- **PATRÓN** `volumen_spike_ratio` < `1.77` → IC=+0.157 (n=1564)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.77 (IC base=+0.054)

- **PATRÓN** `volumen_spike_ratio` > `1.5089` → IC=+0.160 (n=2094)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.5089 (IC base=+0.054)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.176 (n=146)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.055 (n=773)

- **FILTRO** `ibs_20min` < `0.2647` → IC=-0.175 (n=229)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2647
  - _Potencial_: sin este filtro IC_bueno=+0.082 (n=690)

- **FILTRO** `ibs_20min` > `0.2` → IC=-0.131 (n=4765)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2
  - _Potencial_: sin este filtro IC_bueno=+0.154 (n=2371)

- **FILTRO** `sigma_ewma_delta_pct` > `8.302` → IC=-0.231 (n=770)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.302
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=6366)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.177 (n=314)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.75 (IC base=+0.018)

- **PATRÓN** `dist_vwap_pct` > `0.9797` → IC=+0.283 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9797 (IC base=+0.018)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.888` → IC=+0.158 (n=217)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 4.888 (IC base=+0.018)

- **PATRÓN** `volumen_regimen` < `0.856` → IC=+0.264 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.856 (IC base=+0.018)

- **PATRÓN** `volumen_regimen` > `0.624` → IC=+0.283 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.624 (IC base=+0.018)

- **PATRÓN** `volumen_pendiente_norm` < `0.0797` → IC=+0.280 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0797 (IC base=+0.018)

- **PATRÓN** `volumen_spike_ratio` < `2.1931` → IC=+0.288 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1931 (IC base=+0.018)

- **PATRÓN** `volumen_spike_ratio` > `1.4523` → IC=+0.263 (n=276)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4523 (IC base=+0.018)

- **PATRÓN** `ballena_activa_n` < `41.0` → IC=+0.270 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 41.0 (IC base=+0.018)

- **PATRÓN** `ibs_20min` < `0.2` → IC=+0.154 (n=2371)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.2 (IC base=-0.036)

- **PATRÓN** `dist_vwap_pct` > `0.5007` → IC=+0.289 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5007 (IC base=-0.036)

- **PATRÓN** `volumen_regimen` < `0.7058` → IC=+0.304 (n=463)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7058 (IC base=-0.036)

- **PATRÓN** `volumen_pendiente_norm` > `0.08` → IC=+0.307 (n=474)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.08 (IC base=-0.036)

- **PATRÓN** `volumen_spike_ratio` < `2.4762` → IC=+0.299 (n=982)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4762 (IC base=-0.036)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `ibs_20min` < `0.7882` → IC=-0.156 (n=3656)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7882
  - _Potencial_: sin este filtro IC_bueno=+0.132 (n=1884)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.173 (n=1183)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=4357)

- **FILTRO** `ibs_20min` > `0.7372` → IC=-0.190 (n=1912)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7372
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=5739)

- **PATRÓN** `ibs_20min` > `0.7882` → IC=+0.132 (n=1884)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` > 0.7882 (IC base=-0.058)

- **PATRÓN** `dist_vwap_pct` > `1.0036` → IC=+0.356 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0036 (IC base=-0.058)

- **PATRÓN** `volumen_regimen` > `0.7043` → IC=+0.318 (n=971)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7043 (IC base=-0.058)

- **PATRÓN** `volumen_pendiente_norm` < `0.1064` → IC=+0.301 (n=1032)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1064 (IC base=-0.058)

- **PATRÓN** `volumen_pendiente_norm` > `0.1706` → IC=+0.300 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1706 (IC base=-0.058)

- **PATRÓN** `volumen_spike_ratio` < `1.5808` → IC=+0.304 (n=468)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5808 (IC base=-0.058)

- **PATRÓN** `volumen_spike_ratio` > `2.5248` → IC=+0.318 (n=355)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5248 (IC base=-0.058)

- **PATRÓN** `dist_vwap_pct` > `1.064` → IC=+0.275 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.064 (IC base=+0.004)

- **PATRÓN** `volumen_regimen` < `0.6419` → IC=+0.274 (n=749)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6419 (IC base=+0.004)

- **PATRÓN** `volumen_regimen` > `1.0657` → IC=+0.282 (n=1018)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0657 (IC base=+0.004)

- **PATRÓN** `volumen_pendiente_norm` > `0.1694` → IC=+0.286 (n=597)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1694 (IC base=+0.004)

- **PATRÓN** `volumen_spike_ratio` < `2.1753` → IC=+0.265 (n=1865)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1753 (IC base=+0.004)

- **PATRÓN** `volumen_spike_ratio` > `1.4374` → IC=+0.270 (n=2119)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4374 (IC base=+0.004)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.196 (n=7749)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` > 0.0107 (IC base=+0.087)

- **PATRÓN** `ibs_20min` > `0.9688` → IC=+0.312 (n=7745)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9688 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` > `0.9308` → IC=+0.302 (n=1624)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9308 (IC base=+0.087)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.472` → IC=+0.169 (n=10420)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 3.472 (IC base=+0.087)

- **PATRÓN** `volumen_regimen` > `0.693` → IC=+0.278 (n=7657)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.693 (IC base=+0.087)

- **PATRÓN** `volumen_pendiente_norm` > `0.2935` → IC=+0.295 (n=1932)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2935 (IC base=+0.087)

- **PATRÓN** `volumen_spike_ratio` > `2.6493` → IC=+0.286 (n=4496)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6493 (IC base=+0.087)

- **PATRÓN** `ballena_activa_n` < `89.0` → IC=+0.309 (n=13100)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 89.0 (IC base=+0.087)

- **PATRÓN** `sigma_h` > `0.0102` → IC=+0.156 (n=7482)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0102 (IC base=+0.083)

- **PATRÓN** `ibs_20min` < `0.5203` → IC=+0.172 (n=19746)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.5203 (IC base=+0.083)

- **PATRÓN** `volumen_regimen` < `0.6986` → IC=+0.281 (n=3283)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6986 (IC base=+0.083)

- **PATRÓN** `volumen_regimen` > `1.186` → IC=+0.281 (n=2485)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.186 (IC base=+0.083)

- **PATRÓN** `volumen_pendiente_norm` > `0.2942` → IC=+0.328 (n=1660)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2942 (IC base=+0.083)

- **PATRÓN** `volumen_spike_ratio` < `1.4529` → IC=+0.306 (n=3671)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4529 (IC base=+0.083)

- **PATRÓN** `volumen_spike_ratio` > `2.2761` → IC=+0.303 (n=4990)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2761 (IC base=+0.083)

- **PATRÓN** `ballena_activa_n` < `72.0` → IC=+0.312 (n=10985)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 72.0 (IC base=+0.083)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.8028` → IC=-0.134 (n=4125)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8028
  - _Potencial_: sin este filtro IC_bueno=+0.302 (n=2125)

- **FILTRO** `ibs_20min` > `0.7152` → IC=-0.237 (n=1377)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7152
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=4138)

- **FILTRO** `sigma_ewma_delta_pct` > `4.087` → IC=-0.237 (n=1193)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.087
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=4322)

- **PATRÓN** `ibs_20min` > `0.8028` → IC=+0.302 (n=2125)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8028 (IC base=+0.014)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.955` → IC=+0.190 (n=2088)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 2.955 (IC base=+0.014)

- **PATRÓN** `volumen_pendiente_norm` > `0.2292` → IC=+0.331 (n=400)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2292 (IC base=+0.014)

- **PATRÓN** `volumen_spike_ratio` < `1.449` → IC=+0.284 (n=664)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.449 (IC base=+0.014)

- **PATRÓN** `volumen_spike_ratio` > `2.2443` → IC=+0.304 (n=902)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2443 (IC base=+0.014)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.305 (n=1991)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 27.0 (IC base=+0.014)

- **PATRÓN** `ibs_20min` < `0.1744` → IC=+0.171 (n=1379)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.1744 (IC base=-0.021)

- **PATRÓN** `volumen_pendiente_norm` < `0.1512` → IC=+0.405 (n=1083)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1512 (IC base=-0.021)

- **PATRÓN** `volumen_spike_ratio` < `1.4203` → IC=+0.426 (n=349)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4203 (IC base=-0.021)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.403 (n=1087)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 23.0 (IC base=-0.021)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.1693` → IC=+0.225 (n=995)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1693 (IC base=+0.011)

- **PATRÓN** `volumen_regimen` < `1.195` → IC=+0.210 (n=2278)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.195 (IC base=+0.011)

- **PATRÓN** `volumen_regimen` > `0.6956` → IC=+0.218 (n=2035)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6956 (IC base=+0.011)

- **PATRÓN** `volumen_pendiente_norm` > `0.2769` → IC=+0.244 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2769 (IC base=+0.011)

- **PATRÓN** `volumen_spike_ratio` < `1.4206` → IC=+0.228 (n=751)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4206 (IC base=+0.011)

- **PATRÓN** `ballena_activa_n` < `259.0` → IC=+0.244 (n=1500)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 259.0 (IC base=+0.011)

- **PATRÓN** `volumen_regimen` > `0.6162` → IC=+0.254 (n=1605)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6162 (IC base=-0.003)

- **PATRÓN** `volumen_pendiente_norm` > `0.2697` → IC=+0.300 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2697 (IC base=-0.003)

- **PATRÓN** `volumen_spike_ratio` < `1.5222` → IC=+0.262 (n=683)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5222 (IC base=-0.003)

- **PATRÓN** `volumen_spike_ratio` > `2.1427` → IC=+0.259 (n=704)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1427 (IC base=-0.003)

- **PATRÓN** `ballena_activa_n` < `207.0` → IC=+0.273 (n=693)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 207.0 (IC base=-0.003)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0095` → IC=+0.322 (n=2166)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0095 (IC base=+0.284)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.293 (n=3249)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.284)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.325 (n=1767)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.284)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.59` → IC=+0.305 (n=2186)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.59 (IC base=+0.284)

- **PATRÓN** `volumen_pendiente_norm` < `0.0978` → IC=+0.297 (n=2854)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0978 (IC base=+0.284)

- **PATRÓN** `volumen_spike_ratio` > `1.6071` → IC=+0.290 (n=3159)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6071 (IC base=+0.284)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.293 (n=3900)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.284)

- **PATRÓN** `libro_liquidez` > `2015.541` → IC=+0.293 (n=1083)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2015.541 (IC base=+0.284)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.308 (n=2041)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.284)

- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.331 (n=1976)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0089 (IC base=+0.307)

- **PATRÓN** `drift_60min` |x|≤ `0.1771` → IC=+0.326 (n=1304)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1771 (IC base=+0.307)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.328 (n=1134)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.307)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.310 (n=1344)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.307)

- **PATRÓN** `ibs_20min` > `0.1473` → IC=+0.318 (n=1974)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1473 (IC base=+0.307)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.114` → IC=+0.309 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.114 (IC base=+0.307)

- **PATRÓN** `volumen_pendiente_norm` < `0.1991` → IC=+0.307 (n=2911)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1991 (IC base=+0.307)

- **PATRÓN** `volumen_pendiente_norm` > `0.3448` → IC=+0.315 (n=480)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3448 (IC base=+0.307)

- **PATRÓN** `volumen_spike_ratio` > `2.7291` → IC=+0.325 (n=1294)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7291 (IC base=+0.307)

- **PATRÓN** `libro_liquidez` > `1892.3232` → IC=+0.311 (n=1340)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1892.3232 (IC base=+0.307)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.314 (n=2528)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 23.0 (IC base=+0.307)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7221` → IC=-0.178 (n=1465)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7221
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=4397)

- **PATRÓN** `dist_vwap_pct` > `0.1447` → IC=+0.238 (n=1058)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1447 (IC base=+0.021)

- **PATRÓN** `volumen_regimen` < `1.1591` → IC=+0.236 (n=2086)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1591 (IC base=+0.021)

- **PATRÓN** `volumen_pendiente_norm` < `0.1628` → IC=+0.236 (n=2187)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1628 (IC base=+0.021)

- **PATRÓN** `volumen_pendiente_norm` > `0.103` → IC=+0.243 (n=684)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.103 (IC base=+0.021)

- **PATRÓN** `volumen_spike_ratio` < `2.4363` → IC=+0.240 (n=2024)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4363 (IC base=+0.021)

- **PATRÓN** `ballena_activa_n` < `114.0` → IC=+0.254 (n=2067)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 114.0 (IC base=+0.021)

- **PATRÓN** `ibs_20min` < `0.0918` → IC=+0.156 (n=1467)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.0918 (IC base=+0.007)

- **PATRÓN** `dist_vwap_pct` > `0.7318` → IC=+0.256 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7318 (IC base=+0.007)

- **PATRÓN** `volumen_regimen` < `1.1812` → IC=+0.264 (n=1504)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1812 (IC base=+0.007)

- **PATRÓN** `volumen_pendiente_norm` > `0.2815` → IC=+0.316 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2815 (IC base=+0.007)

- **PATRÓN** `volumen_spike_ratio` < `1.7847` → IC=+0.292 (n=964)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7847 (IC base=+0.007)

- **PATRÓN** `volumen_spike_ratio` > `2.4256` → IC=+0.279 (n=483)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4256 (IC base=+0.007)

- **PATRÓN** `ballena_activa_n` < `115.0` → IC=+0.283 (n=1469)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 115.0 (IC base=+0.007)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7407` → IC=-0.249 (n=2393)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7407
  - _Potencial_: sin este filtro IC_bueno=+0.312 (n=2402)

- **FILTRO** `ibs_20min` > `0.619` → IC=-0.235 (n=1135)

  - _Acción_: SKIP cuando `ibs_20min` > 0.619
  - _Potencial_: sin este filtro IC_bueno=+0.153 (n=3406)

- **FILTRO** `sigma_ewma_delta_pct` > `8.282` → IC=-0.264 (n=520)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.282
  - _Potencial_: sin este filtro IC_bueno=+0.098 (n=4021)

- **PATRÓN** `ibs_20min` > `0.7407` → IC=+0.312 (n=2402)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7407 (IC base=+0.032)

- **PATRÓN** `dist_vwap_pct` > `1.0425` → IC=+0.357 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0425 (IC base=+0.032)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.461` → IC=+0.155 (n=1947)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 2.461 (IC base=+0.032)

- **PATRÓN** `volumen_regimen` < `0.842` → IC=+0.344 (n=1164)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.842 (IC base=+0.032)

- **PATRÓN** `volumen_regimen` > `0.696` → IC=+0.336 (n=1560)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.696 (IC base=+0.032)

- **PATRÓN** `volumen_pendiente_norm` < `0.1563` → IC=+0.335 (n=1794)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1563 (IC base=+0.032)

- **PATRÓN** `volumen_pendiente_norm` > `0.274` → IC=+0.364 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.274 (IC base=+0.032)

- **PATRÓN** `volumen_spike_ratio` < `1.4223` → IC=+0.359 (n=565)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4223 (IC base=+0.032)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.355 (n=1507)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=+0.032)

- **PATRÓN** `ibs_20min` < `0.619` → IC=+0.153 (n=3406)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.619 (IC base=+0.056)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.044` → IC=+0.131 (n=3197)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` < 3.044 (IC base=+0.056)

- **PATRÓN** `volumen_regimen` < `0.6945` → IC=+0.280 (n=753)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6945 (IC base=+0.056)

- **PATRÓN** `volumen_pendiente_norm` > `0.071` → IC=+0.292 (n=689)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.071 (IC base=+0.056)

- **PATRÓN** `volumen_spike_ratio` < `1.8044` → IC=+0.278 (n=1107)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8044 (IC base=+0.056)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.285 (n=1685)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 46.0 (IC base=+0.056)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0157` → IC=+0.360 (n=1640)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0157 (IC base=+0.315)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.317 (n=2483)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.315)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.317 (n=1175)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.315)

- **PATRÓN** `ibs_20min` > `0.66` → IC=+0.344 (n=2461)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.66 (IC base=+0.315)

- **PATRÓN** `dist_vwap_pct` > `0.294` → IC=+0.339 (n=1192)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.294 (IC base=+0.315)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.776` → IC=+0.335 (n=1203)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.776 (IC base=+0.315)

- **PATRÓN** `volumen_regimen` > `0.6293` → IC=+0.327 (n=2461)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6293 (IC base=+0.315)

- **PATRÓN** `volumen_pendiente_norm` > `0.2811` → IC=+0.346 (n=362)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2811 (IC base=+0.315)

- **PATRÓN** `volumen_spike_ratio` > `1.4315` → IC=+0.327 (n=2373)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4315 (IC base=+0.315)

- **PATRÓN** `libro_liquidez` > `2994.1526` → IC=+0.329 (n=820)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2994.1526 (IC base=+0.315)

- **PATRÓN** `ballena_activa_n` < `33.0` → IC=+0.342 (n=1945)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 33.0 (IC base=+0.315)

- **PATRÓN** `sigma_h` > `0.015` → IC=+0.350 (n=1757)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.015 (IC base=+0.316)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.321 (n=1335)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.316)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.318 (n=1281)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.316)

- **PATRÓN** `ibs_20min` < `0.381` → IC=+0.334 (n=2636)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.381 (IC base=+0.316)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.613` → IC=+0.328 (n=966)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.613 (IC base=+0.316)

- **PATRÓN** `volumen_regimen` < `0.7189` → IC=+0.322 (n=1161)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7189 (IC base=+0.316)

- **PATRÓN** `volumen_regimen` > `1.2061` → IC=+0.343 (n=879)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2061 (IC base=+0.316)

- **PATRÓN** `volumen_pendiente_norm` > `0.23` → IC=+0.365 (n=494)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.23 (IC base=+0.316)

- **PATRÓN** `volumen_spike_ratio` < `1.4124` → IC=+0.321 (n=819)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4124 (IC base=+0.316)

- **PATRÓN** `volumen_spike_ratio` > `2.1399` → IC=+0.316 (n=1113)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1399 (IC base=+0.316)

- **PATRÓN** `libro_liquidez` > `2977.6478` → IC=+0.316 (n=879)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2977.6478 (IC base=+0.316)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.223 (n=5762)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0125 (IC base=+0.172)

- **PATRÓN** `drift_60min` |x|≤ `0.122` → IC=+0.191 (n=7597)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.122 (IC base=+0.172)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.183 (n=17884)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.172)

- **PATRÓN** `ibs_20min` > `0.5374` → IC=+0.230 (n=17263)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5374 (IC base=+0.172)

- **PATRÓN** `dist_vwap_pct` > `0.162` → IC=+0.205 (n=6535)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.162 (IC base=+0.172)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.757` → IC=+0.259 (n=3363)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.757 (IC base=+0.172)

- **PATRÓN** `volumen_regimen` < `1.1782` → IC=+0.152 (n=11498)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.1782 (IC base=+0.172)

- **PATRÓN** `volumen_regimen` > `0.6257` → IC=+0.151 (n=11499)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.6257 (IC base=+0.172)

- **PATRÓN** `volumen_pendiente_norm` > `0.2938` → IC=+0.204 (n=2499)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2938 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` > `2.6059` → IC=+0.186 (n=5598)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.6059 (IC base=+0.172)

- **PATRÓN** `ballena_activa_n` < `87.0` → IC=+0.191 (n=16201)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 87.0 (IC base=+0.172)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.192 (n=7482)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0059 (IC base=+0.184)

- **PATRÓN** `sigma_h` > `0.0078` → IC=+0.185 (n=11324)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` > 0.0078 (IC base=+0.184)

- **PATRÓN** `drift_60min` |x|≤ `0.2085` → IC=+0.210 (n=11322)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2085 (IC base=+0.184)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.212 (n=6389)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.184)

- **PATRÓN** `ibs_20min` < `0.5257` → IC=+0.240 (n=16981)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5257 (IC base=+0.184)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.505` → IC=+0.187 (n=2704)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 9.505 (IC base=+0.184)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.508` → IC=+0.192 (n=15127)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` < 2.508 (IC base=+0.184)

- **PATRÓN** `volumen_regimen` < `1.182` → IC=+0.165 (n=12080)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.182 (IC base=+0.184)

- **PATRÓN** `volumen_pendiente_norm` > `0.2938` → IC=+0.219 (n=2542)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2938 (IC base=+0.184)

- **PATRÓN** `volumen_spike_ratio` > `2.6288` → IC=+0.194 (n=5390)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.6288 (IC base=+0.184)

- **PATRÓN** `ballena_activa_n` < `91.0` → IC=+0.199 (n=15973)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 91.0 (IC base=+0.184)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `drift_60min` |x|≤ `0.1042` → IC=+0.257 (n=1251)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1042 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.233 (n=2953)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.226)

- **PATRÓN** `ibs_20min` > `0.9423` → IC=+0.295 (n=1894)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9423 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.458` → IC=+0.330 (n=928)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.458 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` > `0.2808` → IC=+0.288 (n=432)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2808 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` < `1.8355` → IC=+0.224 (n=1808)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8355 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` > `1.4352` → IC=+0.226 (n=2712)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4352 (IC base=+0.226)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.237 (n=3161)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.226)

- **PATRÓN** `sigma_h` < `0.0099` → IC=+0.259 (n=2318)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0099 (IC base=+0.258)

- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.259 (n=1049)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0089 (IC base=+0.258)

- **PATRÓN** `drift_60min` |x|≤ `0.0965` → IC=+0.316 (n=1018)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0965 (IC base=+0.258)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.263 (n=2385)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.258)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.264 (n=1573)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.258)

- **PATRÓN** `ibs_20min` < `0.4403` → IC=+0.274 (n=2314)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4403 (IC base=+0.258)

- **PATRÓN** `volumen_pendiente_norm` < `0.0993` → IC=+0.261 (n=2033)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0993 (IC base=+0.258)

- **PATRÓN** `volumen_pendiente_norm` > `0.3012` → IC=+0.270 (n=346)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3012 (IC base=+0.258)

- **PATRÓN** `volumen_spike_ratio` < `1.4451` → IC=+0.276 (n=739)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4451 (IC base=+0.258)

- **PATRÓN** `volumen_spike_ratio` > `2.6807` → IC=+0.257 (n=739)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6807 (IC base=+0.258)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.268 (n=1660)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.258)

- **PATRÓN** `libro_liquidez` > `1773.334` → IC=+0.267 (n=1542)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1773.334 (IC base=+0.258)

- **PATRÓN** `ballena_activa_n` < `7.0` → IC=+0.258 (n=862)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 7.0 (IC base=+0.258)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.199 (n=879)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.128)

- **PATRÓN** `drift_60min` |x|≤ `0.0648` → IC=+0.176 (n=877)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.0648 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.145 (n=2748)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` > `0.2604` → IC=+0.206 (n=2630)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2604 (IC base=+0.128)

- **PATRÓN** `dist_vwap_pct` > `0.1836` → IC=+0.212 (n=1312)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1836 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.624` → IC=+0.209 (n=480)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.624 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` < `0.6275` → IC=+0.131 (n=877)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 0.6275 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` > `1.0555` → IC=+0.135 (n=1193)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` > 1.0555 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` > `0.2804` → IC=+0.169 (n=406)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.2804 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` < `1.5076` → IC=+0.132 (n=1137)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 1.5076 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` > `2.4689` → IC=+0.148 (n=862)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 2.4689 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `398.0` → IC=+0.132 (n=2560)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 398.0 (IC base=+0.128)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.172 (n=2794)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0065 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.2376` → IC=+0.175 (n=2456)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.2376 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.181 (n=1325)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 15.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` < `0.6109` → IC=+0.210 (n=2791)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6109 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.87` → IC=+0.176 (n=526)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 10.87 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.028` → IC=+0.153 (n=2434)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 4.028 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `1.1958` → IC=+0.161 (n=2791)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.1958 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` < `0.2279` → IC=+0.153 (n=2958)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` < 0.2279 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `2.4631` → IC=+0.154 (n=2665)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.4631 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `209.0` → IC=+0.195 (n=1147)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 209.0 (IC base=+0.149)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0115` → IC=+0.231 (n=1330)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0115 (IC base=+0.211)

- **PATRÓN** `drift_60min` |x|≤ `0.2476` → IC=+0.232 (n=1950)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2476 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.219 (n=3039)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.292 (n=1555)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.064` → IC=+0.304 (n=693)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.064 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.3519` → IC=+0.243 (n=414)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3519 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `2.71` → IC=+0.226 (n=1295)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.71 (IC base=+0.211)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.215 (n=3534)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `2004.2354` → IC=+0.223 (n=975)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2004.2354 (IC base=+0.211)

- **PATRÓN** `sigma_h` < `0.0118` → IC=+0.246 (n=2590)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0118 (IC base=+0.240)

- **PATRÓN** `drift_60min` |x|≤ `0.41` → IC=+0.264 (n=2278)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.41 (IC base=+0.240)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.280 (n=993)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.240)

- **PATRÓN** `ibs_20min` < `0.0419` → IC=+0.290 (n=1139)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0419 (IC base=+0.240)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.874` → IC=+0.279 (n=342)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.874 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` > `0.3556` → IC=+0.288 (n=432)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3556 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` < `1.7742` → IC=+0.242 (n=1101)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7742 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` > `2.1818` → IC=+0.252 (n=1667)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1818 (IC base=+0.240)

- **PATRÓN** `libro_liquidez` > `1877.7172` → IC=+0.250 (n=1174)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1877.7172 (IC base=+0.240)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.246 (n=1722)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.240)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.203 (n=949)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0038 (IC base=+0.127)

- **PATRÓN** `drift_60min` |x|≤ `0.0775` → IC=+0.185 (n=948)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.0775 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.138 (n=2936)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.127)

- **PATRÓN** `ibs_20min` > `0.2458` → IC=+0.190 (n=2842)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.2458 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` > `0.1398` → IC=+0.186 (n=1628)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1398 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.243` → IC=+0.201 (n=489)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.243 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` < `0.8417` → IC=+0.135 (n=1896)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.8417 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` > `0.2879` → IC=+0.168 (n=429)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` > 0.2879 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` > `2.5103` → IC=+0.142 (n=928)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 2.5103 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `6805.3231` → IC=+0.197 (n=1289)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 6805.3231 (IC base=+0.127)

- **PATRÓN** `ballena_activa_n` < `126.0` → IC=+0.127 (n=2783)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 126.0 (IC base=+0.127)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.164 (n=2667)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0067 (IC base=+0.130)

- **PATRÓN** `drift_60min` |x|≤ `0.3967` → IC=+0.146 (n=3028)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.3967 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.166 (n=1447)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 15.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` < `0.6774` → IC=+0.185 (n=3028)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.6774 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.195` → IC=+0.138 (n=724)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 9.195 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` < `0.852` → IC=+0.151 (n=2019)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.852 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` > `0.2939` → IC=+0.174 (n=452)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.2939 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` < `1.8013` → IC=+0.132 (n=1916)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 1.8013 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` > `1.5196` → IC=+0.131 (n=2567)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 1.5196 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `6326.2918` → IC=+0.190 (n=1373)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 6326.2918 (IC base=+0.130)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.158 (n=950)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 48.0 (IC base=+0.130)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0126` → IC=+0.164 (n=1059)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` > 0.0126 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.132 (n=3248)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 5.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` > `0.4706` → IC=+0.205 (n=3180)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4706 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` > `0.197` → IC=+0.187 (n=1695)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.197 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.996` → IC=+0.287 (n=669)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.996 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` < `1.1682` → IC=+0.128 (n=3175)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 1.1682 (IC base=+0.117)

- **PATRÓN** `volumen_pendiente_norm` < `0.163` → IC=+0.122 (n=3232)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_pendiente_norm` < 0.163 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` < `1.7791` → IC=+0.124 (n=2053)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 1.7791 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `2663.0195` → IC=+0.195 (n=1439)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 2663.0195 (IC base=+0.117)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.133 (n=1046)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 16.0 (IC base=+0.117)

- **PATRÓN** `sigma_h` < `0.0119` → IC=+0.142 (n=3312)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.0119 (IC base=+0.119)

- **PATRÓN** `drift_60min` |x|≤ `0.1126` → IC=+0.166 (n=1104)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.1126 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.135 (n=3379)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 5.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` < `0.65` → IC=+0.220 (n=3311)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.65 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.253` → IC=+0.141 (n=2932)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` < 2.253 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` < `1.1736` → IC=+0.127 (n=3310)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` < 1.1736 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` > `0.275` → IC=+0.146 (n=459)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` > 0.275 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` < `1.4348` → IC=+0.137 (n=1044)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.4348 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` > `2.4425` → IC=+0.130 (n=1044)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 2.4425 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `2900.261` → IC=+0.194 (n=1104)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 2900.261 (IC base=+0.119)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.125 (n=1453)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 19.0 (IC base=+0.119)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0131` → IC=+0.250 (n=2549)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0131 (IC base=+0.226)

- **PATRÓN** `drift_60min` |x|≤ `0.1651` → IC=+0.242 (n=1255)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1651 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.232 (n=2960)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.226)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.228 (n=2578)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.226)

- **PATRÓN** `ibs_20min` > `0.6667` → IC=+0.258 (n=2853)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6667 (IC base=+0.226)

- **PATRÓN** `dist_vwap_pct` > `0.1805` → IC=+0.233 (n=1743)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1805 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.543` → IC=+0.258 (n=1299)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.543 (IC base=+0.226)

- **PATRÓN** `volumen_regimen` > `0.624` → IC=+0.235 (n=2853)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.624 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` > `0.2349` → IC=+0.266 (n=532)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2349 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` < `2.4722` → IC=+0.229 (n=2783)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4722 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` > `1.4338` → IC=+0.230 (n=2783)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4338 (IC base=+0.226)

- **PATRÓN** `libro_liquidez` > `2587.5715` → IC=+0.230 (n=1902)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2587.5715 (IC base=+0.226)

- **PATRÓN** `sigma_h` < `0.0125` → IC=+0.242 (n=1299)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0125 (IC base=+0.241)

- **PATRÓN** `sigma_h` > `0.0226` → IC=+0.248 (n=1339)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0226 (IC base=+0.241)

- **PATRÓN** `drift_60min` |x|≤ `0.5795` → IC=+0.250 (n=2951)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5795 (IC base=+0.241)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.253 (n=1446)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.241)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.248 (n=1322)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.241)

- **PATRÓN** `ibs_20min` < `0.44` → IC=+0.264 (n=2961)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.44 (IC base=+0.241)

- **PATRÓN** `dist_vwap_pct` > `1.1333` → IC=+0.261 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1333 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.14` → IC=+0.268 (n=566)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.14 (IC base=+0.241)

- **PATRÓN** `volumen_regimen` < `0.8667` → IC=+0.243 (n=1968)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8667 (IC base=+0.241)

- **PATRÓN** `volumen_regimen` > `0.6408` → IC=+0.244 (n=2952)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6408 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` > `0.2811` → IC=+0.292 (n=407)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2811 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` < `2.5149` → IC=+0.239 (n=2786)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5149 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` > `1.549` → IC=+0.242 (n=2488)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.549 (IC base=+0.241)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.208 (n=1490)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.158)

- **PATRÓN** `drift_60min` |x|≤ `0.1337` → IC=+0.172 (n=1964)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.1337 (IC base=+0.158)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.170 (n=4657)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 5.0 (IC base=+0.158)

- **PATRÓN** `ibs_20min` > `0.3062` → IC=+0.195 (n=4464)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 0.3062 (IC base=+0.158)

- **PATRÓN** `dist_vwap_pct` > `0.2214` → IC=+0.181 (n=1689)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.2214 (IC base=+0.158)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.547` → IC=+0.210 (n=729)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.547 (IC base=+0.158)

- **PATRÓN** `volumen_regimen` < `0.8605` → IC=+0.167 (n=2700)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 0.8605 (IC base=+0.158)

- **PATRÓN** `volumen_regimen` > `1.1929` → IC=+0.161 (n=1350)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 1.1929 (IC base=+0.158)

- **PATRÓN** `volumen_pendiente_norm` > `0.1571` → IC=+0.173 (n=1174)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.1571 (IC base=+0.158)

- **PATRÓN** `volumen_spike_ratio` < `1.5268` → IC=+0.162 (n=1915)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 1.5268 (IC base=+0.158)

- **PATRÓN** `volumen_spike_ratio` > `1.8093` → IC=+0.160 (n=2901)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.8093 (IC base=+0.158)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.159 (n=4990)

  - _Acción_: Kelly boost +0.79€ cuando `libro_spread` < 0.02 (IC base=+0.158)

- **PATRÓN** `libro_liquidez` > `7627.5668` → IC=+0.185 (n=2024)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 7627.5668 (IC base=+0.158)

- **PATRÓN** `ibs_20min` < `0.3828` → IC=+0.174 (n=3236)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.3828 (IC base=+0.095)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.136 (n=2080)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 23.0 (IC base=+0.095)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.197 (n=1142)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0061 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.3292` → IC=+0.198 (n=1142)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.3292 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.216 (n=1030)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` > `0.6177` → IC=+0.239 (n=761)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6177 (IC base=+0.182)

- **PATRÓN** `dist_vwap_pct` > `0.3087` → IC=+0.218 (n=346)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3087 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.927` → IC=+0.211 (n=504)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.927 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` < `0.8791` → IC=+0.196 (n=762)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 0.8791 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` < `0.2164` → IC=+0.186 (n=1286)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` < 0.2164 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.0913` → IC=+0.198 (n=395)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.0913 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` < `2.1675` → IC=+0.196 (n=986)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 2.1675 (IC base=+0.182)

- **PATRÓN** `libro_liquidez` > `15742.1193` → IC=+0.192 (n=518)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 15742.1193 (IC base=+0.182)

- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.162 (n=480)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0031 (IC base=+0.082)

- **PATRÓN** `ibs_20min` < `0.2049` → IC=+0.198 (n=628)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.2049 (IC base=+0.082)

- **PATRÓN** `ballena_activa_n` < `164.0` → IC=+0.177 (n=614)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 164.0 (IC base=+0.082)

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

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.124 (n=884)
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
- **PATRÓN** `sigma_h` < `0.0092` → IC=+0.143 (n=771)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.0092 (IC base=+0.124)

- **PATRÓN** `drift_60min` |x|≤ `0.5372` → IC=+0.124 (n=1157)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.62€ cuando `drift_60min` |x|≤ 0.5372 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.166 (n=806)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 11.0 (IC base=+0.124)

- **PATRÓN** `ibs_20min` > `0.5405` → IC=+0.193 (n=1033)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.5405 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` > `0.932` → IC=+0.165 (n=189)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.932 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.848` → IC=+0.228 (n=454)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.848 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` < `1.0462` → IC=+0.136 (n=1017)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 1.0462 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` > `0.7008` → IC=+0.132 (n=1032)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` > 0.7008 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` > `0.2253` → IC=+0.149 (n=203)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.2253 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` < `1.4128` → IC=+0.154 (n=374)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 1.4128 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.126 (n=1213)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.02 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `2760.8656` → IC=+0.167 (n=524)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 2760.8656 (IC base=+0.124)

- **PATRÓN** `ibs_20min` < `0.5556` → IC=+0.152 (n=1129)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` < 0.5556 (IC base=+0.075)

- **PATRÓN** `libro_liquidez` > `2638.5742` → IC=+0.166 (n=581)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2638.5742 (IC base=+0.075)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0166` → IC=+0.243 (n=263)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0166 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.223 (n=189)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.189)

- **PATRÓN** `ibs_20min` > `0.72` → IC=+0.210 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.72 (IC base=+0.189)

- **PATRÓN** `dist_vwap_pct` > `0.8933` → IC=+0.214 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8933 (IC base=+0.189)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.692` → IC=+0.205 (n=388)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.692 (IC base=+0.189)

- **PATRÓN** `volumen_regimen` > `1.1848` → IC=+0.254 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1848 (IC base=+0.189)

- **PATRÓN** `volumen_pendiente_norm` > `0.0785` → IC=+0.198 (n=147)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.0785 (IC base=+0.189)

- **PATRÓN** `volumen_spike_ratio` < `2.1215` → IC=+0.201 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1215 (IC base=+0.189)

- **PATRÓN** `volumen_spike_ratio` > `1.4093` → IC=+0.204 (n=366)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4093 (IC base=+0.189)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.200 (n=428)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.189)

- **PATRÓN** `libro_liquidez` > `2944.973` → IC=+0.202 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2944.973 (IC base=+0.189)

- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.168 (n=432)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` > 0.0107 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.3232` → IC=+0.162 (n=288)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.3232 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.194 (n=207)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 15.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.163 (n=381)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` < 0.5 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` > `1.1745` → IC=+0.279 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1745 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.008` → IC=+0.158 (n=112)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 5.008 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.157` → IC=+0.151 (n=391)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` < 2.157 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `1.2334` → IC=+0.171 (n=432)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 1.2334 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` < `0.113` → IC=+0.161 (n=396)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` < 0.113 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` > `0.2293` → IC=+0.183 (n=80)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.2293 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `1.4792` → IC=+0.202 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4792 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` > `2.6275` → IC=+0.167 (n=139)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 2.6275 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.164 (n=409)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 19.0 (IC base=+0.148)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.229 (n=7550)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0125 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.190 (n=23590)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` > `0.4286` → IC=+0.227 (n=22661)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4286 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` > `0.8785` → IC=+0.211 (n=2663)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8785 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.94` → IC=+0.258 (n=5545)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.94 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` < `1.2131` → IC=+0.159 (n=15250)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.2131 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.241` → IC=+0.208 (n=4071)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.241 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `2.6226` → IC=+0.193 (n=7367)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.6226 (IC base=+0.180)

- **PATRÓN** `ballena_activa_n` < `102.0` → IC=+0.201 (n=21260)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 102.0 (IC base=+0.180)

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.199 (n=6947)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.196)

- **PATRÓN** `sigma_h` > `0.0122` → IC=+0.205 (n=6940)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0122 (IC base=+0.196)

- **PATRÓN** `drift_60min` |x|≤ `0.4815` → IC=+0.199 (n=20812)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4815 (IC base=+0.196)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.216 (n=7790)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.196)

- **PATRÓN** `ibs_20min` < `0.5927` → IC=+0.245 (n=20812)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5927 (IC base=+0.196)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.525` → IC=+0.202 (n=19318)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.525 (IC base=+0.196)

- **PATRÓN** `volumen_regimen` < `0.6319` → IC=+0.179 (n=4661)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` < 0.6319 (IC base=+0.196)

- **PATRÓN** `volumen_pendiente_norm` > `0.293` → IC=+0.253 (n=2860)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.293 (IC base=+0.196)

- **PATRÓN** `volumen_spike_ratio` > `2.6273` → IC=+0.208 (n=6646)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6273 (IC base=+0.196)

- **PATRÓN** `ballena_activa_n` < `91.0` → IC=+0.212 (n=19722)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 91.0 (IC base=+0.196)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.252 (n=1755)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.236)

- **PATRÓN** `ibs_20min` > `0.8641` → IC=+0.296 (n=2415)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8641 (IC base=+0.236)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.822` → IC=+0.343 (n=865)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.822 (IC base=+0.236)

- **PATRÓN** `volumen_pendiente_norm` > `0.2323` → IC=+0.291 (n=653)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2323 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` > `2.2913` → IC=+0.242 (n=1586)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2913 (IC base=+0.236)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.250 (n=3991)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.236)

- **PATRÓN** `libro_liquidez` > `2035.7842` → IC=+0.239 (n=1207)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2035.7842 (IC base=+0.236)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.252 (n=2221)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 14.0 (IC base=+0.236)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.270 (n=3233)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0103 (IC base=+0.269)

- **PATRÓN** `sigma_h` > `0.0092` → IC=+0.271 (n=1470)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0092 (IC base=+0.269)

- **PATRÓN** `drift_60min` |x|≤ `0.1216` → IC=+0.295 (n=1423)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1216 (IC base=+0.269)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.270 (n=3355)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.269)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.272 (n=2921)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.269)

- **PATRÓN** `ibs_20min` < `0.55` → IC=+0.287 (n=3232)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.55 (IC base=+0.269)

- **PATRÓN** `volumen_pendiente_norm` < `0.1607` → IC=+0.271 (n=3261)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1607 (IC base=+0.269)

- **PATRÓN** `volumen_pendiente_norm` > `0.2904` → IC=+0.286 (n=447)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2904 (IC base=+0.269)

- **PATRÓN** `volumen_spike_ratio` < `1.5624` → IC=+0.273 (n=1365)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5624 (IC base=+0.269)

- **PATRÓN** `volumen_spike_ratio` > `2.6447` → IC=+0.280 (n=1034)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6447 (IC base=+0.269)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.275 (n=2308)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.269)

- **PATRÓN** `libro_liquidez` > `1774.215` → IC=+0.277 (n=2155)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1774.215 (IC base=+0.269)

- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.280 (n=1152)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 8.0 (IC base=+0.269)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.178 (n=1239)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0032 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.079` → IC=+0.147 (n=1238)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.079 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.149 (n=3868)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 5.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` > `0.1973` → IC=+0.188 (n=3711)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.1973 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` > `0.32` → IC=+0.198 (n=1205)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.32 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.343` → IC=+0.166 (n=777)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 9.343 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `0.6367` → IC=+0.152 (n=1238)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.6367 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` > `1.0702` → IC=+0.141 (n=1683)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 1.0702 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.2713` → IC=+0.181 (n=522)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.2713 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `2.1711` → IC=+0.141 (n=3207)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.1711 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `1.5209` → IC=+0.142 (n=3256)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.5209 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `218.0` → IC=+0.160 (n=1207)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 218.0 (IC base=+0.137)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.163 (n=3208)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0065 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.3265` → IC=+0.148 (n=3202)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.3265 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.167 (n=1177)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 17.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` < `0.6806` → IC=+0.186 (n=3202)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.6806 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.022` → IC=+0.138 (n=1536)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 3.022 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.024` → IC=+0.139 (n=2893)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` < 4.024 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `1.0441` → IC=+0.152 (n=2817)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.0441 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.2202` → IC=+0.189 (n=593)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.2202 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `2.4315` → IC=+0.144 (n=3092)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.4315 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `1.7706` → IC=+0.141 (n=2061)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 1.7706 (IC base=+0.138)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.138 (n=4160)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `222.0` → IC=+0.160 (n=1003)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 222.0 (IC base=+0.138)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.01` → IC=+0.241 (n=2512)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.01 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.237 (n=3942)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.227)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.227 (n=3374)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.227)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.302 (n=1405)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.994` → IC=+0.322 (n=842)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.994 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` < `0.1322` → IC=+0.229 (n=3567)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1322 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` > `0.351` → IC=+0.233 (n=493)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.351 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` > `2.7431` → IC=+0.242 (n=1670)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7431 (IC base=+0.227)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.233 (n=4546)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.227)

- **PATRÓN** `libro_liquidez` > `1754.1254` → IC=+0.235 (n=2511)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1754.1254 (IC base=+0.227)

- **PATRÓN** `sigma_h` < `0.011` → IC=+0.250 (n=3178)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.011 (IC base=+0.245)

- **PATRÓN** `drift_60min` |x|≤ `0.1771` → IC=+0.266 (n=1588)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1771 (IC base=+0.245)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.263 (n=1374)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.245)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.248 (n=1648)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.245)

- **PATRÓN** `ibs_20min` < `0.0614` → IC=+0.305 (n=1202)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0614 (IC base=+0.245)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.038` → IC=+0.304 (n=381)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.038 (IC base=+0.245)

- **PATRÓN** `volumen_pendiente_norm` > `0.3487` → IC=+0.307 (n=543)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3487 (IC base=+0.245)

- **PATRÓN** `volumen_spike_ratio` > `2.1747` → IC=+0.257 (n=2317)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1747 (IC base=+0.245)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.248 (n=1842)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.245)

- **PATRÓN** `libro_liquidez` > `1989.22` → IC=+0.257 (n=1202)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1989.22 (IC base=+0.245)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.250 (n=3068)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 22.0 (IC base=+0.245)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.195 (n=1314)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0037 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.4311` → IC=+0.145 (n=3915)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.4311 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.149 (n=4058)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 5.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` > `0.8849` → IC=+0.270 (n=1305)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8849 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` > `0.1962` → IC=+0.169 (n=1759)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.1962 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.106` → IC=+0.166 (n=594)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 11.106 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `0.859` → IC=+0.152 (n=2610)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.859 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.2332` → IC=+0.188 (n=694)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.2332 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `1.5173` → IC=+0.152 (n=1685)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 1.5173 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `2.1702` → IC=+0.144 (n=1735)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 2.1702 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `7277.3676` → IC=+0.238 (n=1305)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7277.3676 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `87.0` → IC=+0.144 (n=2544)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 87.0 (IC base=+0.137)

- **PATRÓN** `sigma_h` < `0.0078` → IC=+0.164 (n=3284)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0078 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.4365` → IC=+0.158 (n=3279)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.4365 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.174 (n=1209)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 17.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` < `0.7061` → IC=+0.199 (n=3279)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.7061 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.007` → IC=+0.153 (n=649)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 9.007 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.029` → IC=+0.151 (n=2861)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` < 3.029 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` < `0.6898` → IC=+0.166 (n=1443)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.6898 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` > `0.2942` → IC=+0.213 (n=416)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2942 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `2.2099` → IC=+0.151 (n=2788)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.2099 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` > `1.5288` → IC=+0.155 (n=2830)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.5288 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `6494.5895` → IC=+0.222 (n=1093)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6494.5895 (IC base=+0.147)

- **PATRÓN** `ballena_activa_n` < `58.0` → IC=+0.170 (n=1089)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 58.0 (IC base=+0.147)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0127` → IC=+0.152 (n=1333)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` > 0.0127 (IC base=+0.115)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.146 (n=2808)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 11.0 (IC base=+0.115)

- **PATRÓN** `ibs_20min` > `0.4286` → IC=+0.186 (n=3990)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.4286 (IC base=+0.115)

- **PATRÓN** `dist_vwap_pct` > `1.0061` → IC=+0.200 (n=647)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0061 (IC base=+0.115)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.244` → IC=+0.272 (n=1010)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.244 (IC base=+0.115)

- **PATRÓN** `volumen_regimen` < `0.8751` → IC=+0.128 (n=2656)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 0.8751 (IC base=+0.115)

- **PATRÓN** `volumen_spike_ratio` < `1.8225` → IC=+0.122 (n=2593)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` < 1.8225 (IC base=+0.115)

- **PATRÓN** `libro_liquidez` > `2712.3764` → IC=+0.238 (n=1328)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2712.3764 (IC base=+0.115)

- **PATRÓN** `sigma_h` < `0.0109` → IC=+0.155 (n=3285)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0109 (IC base=+0.129)

- **PATRÓN** `drift_60min` |x|≤ `0.1376` → IC=+0.154 (n=1244)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.1376 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.165 (n=1754)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 15.0 (IC base=+0.129)

- **PATRÓN** `ibs_20min` < `0.6667` → IC=+0.218 (n=3743)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6667 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.042` → IC=+0.151 (n=3612)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` < 3.042 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` < `0.6401` → IC=+0.153 (n=1244)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.6401 (IC base=+0.129)

- **PATRÓN** `volumen_pendiente_norm` > `0.2295` → IC=+0.187 (n=653)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.2295 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` < `1.437` → IC=+0.162 (n=1183)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 1.437 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `2599.7014` → IC=+0.211 (n=1244)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2599.7014 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.143 (n=3151)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 42.0 (IC base=+0.129)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0137` → IC=+0.261 (n=3251)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0137 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.244 (n=3804)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.238)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.243 (n=2433)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.238)

- **PATRÓN** `ibs_20min` > `0.6142` → IC=+0.272 (n=3251)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6142 (IC base=+0.238)

- **PATRÓN** `dist_vwap_pct` > `0.1938` → IC=+0.252 (n=1856)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1938 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.152` → IC=+0.287 (n=637)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.152 (IC base=+0.238)

- **PATRÓN** `volumen_regimen` < `1.2153` → IC=+0.239 (n=3640)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2153 (IC base=+0.238)

- **PATRÓN** `volumen_regimen` > `0.6435` → IC=+0.243 (n=3639)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6435 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` > `0.2393` → IC=+0.252 (n=632)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2393 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` > `2.4984` → IC=+0.257 (n=1187)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4984 (IC base=+0.238)

- **PATRÓN** `libro_liquidez` > `2984.8754` → IC=+0.244 (n=1213)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2984.8754 (IC base=+0.238)

- **PATRÓN** `sigma_h` > `0.0257` → IC=+0.268 (n=1255)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0257 (IC base=+0.244)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.248 (n=3546)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.244)

- **PATRÓN** `ibs_20min` < `0.1398` → IC=+0.308 (n=1658)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1398 (IC base=+0.244)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.072` → IC=+0.277 (n=723)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.072 (IC base=+0.244)

- **PATRÓN** `volumen_regimen` < `0.7155` → IC=+0.246 (n=1657)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7155 (IC base=+0.244)

- **PATRÓN** `volumen_regimen` > `1.214` → IC=+0.264 (n=1255)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.214 (IC base=+0.244)

- **PATRÓN** `volumen_pendiente_norm` > `0.286` → IC=+0.306 (n=520)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.286 (IC base=+0.244)

- **PATRÓN** `volumen_spike_ratio` > `1.4328` → IC=+0.248 (n=3555)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4328 (IC base=+0.244)

- **PATRÓN** `libro_liquidez` > `2971.1415` → IC=+0.248 (n=1255)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2971.1415 (IC base=+0.244)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.201 (n=5965)

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.244 (n=2172)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.221)

- **PATRÓN** `drift_60min` |x|≤ `0.5136` → IC=+0.230 (n=6493)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5136 (IC base=+0.221)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.227 (n=6543)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.221)

- **PATRÓN** `ibs_20min` > `0.9286` → IC=+0.256 (n=2168)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9286 (IC base=+0.221)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.593` → IC=+0.225 (n=3232)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.593 (IC base=+0.221)

- **PATRÓN** `volumen_regimen` < `0.7053` → IC=+0.229 (n=2083)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7053 (IC base=+0.221)

- **PATRÓN** `volumen_regimen` > `0.8784` → IC=+0.222 (n=3156)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8784 (IC base=+0.221)

- **PATRÓN** `volumen_pendiente_norm` < `0.1051` → IC=+0.222 (n=6069)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1051 (IC base=+0.221)

- **PATRÓN** `volumen_pendiente_norm` > `0.165` → IC=+0.229 (n=1829)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.165 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` < `2.2559` → IC=+0.225 (n=5623)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.2559 (IC base=+0.221)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.225 (n=4835)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.221)

- **PATRÓN** `libro_liquidez` > `2587.1297` → IC=+0.224 (n=6492)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2587.1297 (IC base=+0.221)

- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.239 (n=1502)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.200)

- **PATRÓN** `drift_60min` |x|≤ `0.4977` → IC=+0.212 (n=4487)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4977 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.213 (n=1499)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.200)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.212 (n=1984)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.200)

- **PATRÓN** `ibs_20min` < `0.1852` → IC=+0.213 (n=1974)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1852 (IC base=+0.200)

- **PATRÓN** `dist_vwap_pct` > `0.6629` → IC=+0.210 (n=760)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6629 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.762` → IC=+0.212 (n=4040)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.762 (IC base=+0.200)

- **PATRÓN** `volumen_regimen` < `1.0952` → IC=+0.206 (n=3768)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0952 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` < `0.0976` → IC=+0.201 (n=4132)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0976 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` > `0.0732` → IC=+0.204 (n=2002)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0732 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` < `1.5317` → IC=+0.205 (n=1946)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5317 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` > `2.1876` → IC=+0.210 (n=2005)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1876 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.201 (n=5965)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.200)

- **PATRÓN** `ballena_activa_n` < `32.0` → IC=+0.223 (n=1980)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 32.0 (IC base=+0.200)

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
- **PATRÓN** `sigma_h` < `0.0083` → IC=+0.220 (n=1817)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0083 (IC base=+0.207)

- **PATRÓN** `drift_60min` |x|≤ `0.4578` → IC=+0.214 (n=1816)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4578 (IC base=+0.207)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.232 (n=636)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.207)

- **PATRÓN** `ibs_20min` < `0.472` → IC=+0.218 (n=1211)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.472 (IC base=+0.207)

- **PATRÓN** `ibs_20min` > `0.1444` → IC=+0.209 (n=1816)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1444 (IC base=+0.207)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.374` → IC=+0.214 (n=1841)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 6.374 (IC base=+0.207)

- **PATRÓN** `volumen_regimen` < `0.8667` → IC=+0.215 (n=1211)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8667 (IC base=+0.207)

- **PATRÓN** `volumen_pendiente_norm` < `0.1019` → IC=+0.210 (n=1677)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1019 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` < `1.4045` → IC=+0.224 (n=593)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4045 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` > `1.4939` → IC=+0.208 (n=1588)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4939 (IC base=+0.207)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.244 (n=478)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.202)

- **PATRÓN** `drift_60min` |x|≤ `0.4873` → IC=+0.222 (n=1425)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4873 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.205 (n=533)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.202)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.218 (n=966)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.202)

- **PATRÓN** `ibs_20min` < `0.1707` → IC=+0.204 (n=627)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1707 (IC base=+0.202)

- **PATRÓN** `ibs_20min` > `0.6121` → IC=+0.208 (n=646)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6121 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` > `0.6253` → IC=+0.218 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6253 (IC base=+0.202)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.281` → IC=+0.207 (n=1302)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.281 (IC base=+0.202)

- **PATRÓN** `volumen_regimen` < `1.2488` → IC=+0.211 (n=1425)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2488 (IC base=+0.202)

- **PATRÓN** `volumen_pendiente_norm` > `0.0731` → IC=+0.229 (n=585)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0731 (IC base=+0.202)

- **PATRÓN** `volumen_spike_ratio` < `2.183` → IC=+0.205 (n=1229)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.183 (IC base=+0.202)

- **PATRÓN** `volumen_spike_ratio` > `1.7864` → IC=+0.204 (n=931)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7864 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `6565.099` → IC=+0.207 (n=1273)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6565.099 (IC base=+0.202)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0083` → IC=+0.236 (n=472)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0083 (IC base=+0.207)

- **PATRÓN** `hora_utc` > `10.0` → IC=+0.241 (n=731)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.207)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.287 (n=365)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.207)

- **PATRÓN** `dist_vwap_pct` > `0.773` → IC=+0.233 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.773 (IC base=+0.207)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.202` → IC=+0.236 (n=586)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.202 (IC base=+0.207)

- **PATRÓN** `volumen_regimen` < `0.6421` → IC=+0.244 (n=357)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6421 (IC base=+0.207)

- **PATRÓN** `volumen_pendiente_norm` < `0.1064` → IC=+0.213 (n=969)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1064 (IC base=+0.207)

- **PATRÓN** `volumen_pendiente_norm` > `0.2727` → IC=+0.219 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2727 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` < `2.1486` → IC=+0.216 (n=918)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1486 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` > `1.4705` → IC=+0.211 (n=1041)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4705 (IC base=+0.207)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.214 (n=1252)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.207)

- **PATRÓN** `libro_liquidez` > `4106.249` → IC=+0.240 (n=486)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4106.249 (IC base=+0.207)

- **PATRÓN** `ballena_activa_n` < `38.0` → IC=+0.210 (n=936)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 38.0 (IC base=+0.207)

- **PATRÓN** `sigma_h` < `0.0132` → IC=+0.227 (n=748)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0132 (IC base=+0.224)

- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.238 (n=498)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0101 (IC base=+0.224)

- **PATRÓN** `drift_60min` |x|≤ `0.6045` → IC=+0.244 (n=748)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6045 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.227 (n=698)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.248 (n=518)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` < `0.7347` → IC=+0.251 (n=749)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7347 (IC base=+0.224)

- **PATRÓN** `dist_vwap_pct` > `0.5282` → IC=+0.225 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5282 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.816` → IC=+0.239 (n=699)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.816 (IC base=+0.224)

- **PATRÓN** `volumen_regimen` < `0.7555` → IC=+0.229 (n=330)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7555 (IC base=+0.224)

- **PATRÓN** `volumen_regimen` > `1.2706` → IC=+0.233 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2706 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` < `0.0822` → IC=+0.235 (n=632)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0822 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` > `2.1983` → IC=+0.257 (n=331)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1983 (IC base=+0.224)

- **PATRÓN** `libro_liquidez` > `3818.2796` → IC=+0.238 (n=498)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3818.2796 (IC base=+0.224)

- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.260 (n=503)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 25.0 (IC base=+0.224)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.149 (n=756)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0038 (IC base=+0.054)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.184 (n=1452)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.75 (IC base=+0.054)

- **PATRÓN** `dist_vwap_pct` > `0.1445` → IC=+0.142 (n=1067)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.1445 (IC base=+0.054)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.361` → IC=+0.142 (n=484)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 10.361 (IC base=+0.054)

- **PATRÓN** `ibs_20min` < `0.0621` → IC=+0.262 (n=669)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0621 (IC base=+0.049)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `ibs_20min` < `0.5412` → IC=-0.120 (n=301)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5412
  - _Potencial_: sin este filtro IC_bueno=+0.165 (n=613)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.127 (n=631)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.64€ cuando `sigma_h` < 0.0053 (IC base=+0.070)

- **PATRÓN** `ibs_20min` > `0.5412` → IC=+0.165 (n=613)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.5412 (IC base=+0.070)

- **PATRÓN** `dist_vwap_pct` > `0.1215` → IC=+0.170 (n=325)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.1215 (IC base=+0.070)

- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.129 (n=273)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.65€ cuando `sigma_h` < 0.0035 (IC base=+0.042)

- **PATRÓN** `ibs_20min` < `0.0659` → IC=+0.259 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0659 (IC base=+0.042)

- **PATRÓN** `volumen_pendiente_norm` > `0.0697` → IC=+0.122 (n=257)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_pendiente_norm` > 0.0697 (IC base=+0.042)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` > `0.6735` → IC=-0.156 (n=161)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6735
  - _Potencial_: sin este filtro IC_bueno=+0.108 (n=485)

- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.151 (n=322)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0041 (IC base=+0.070)

- **PATRÓN** `ibs_20min` > `0.9361` → IC=+0.259 (n=318)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9361 (IC base=+0.070)

- **PATRÓN** `dist_vwap_pct` > `0.1273` → IC=+0.169 (n=339)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.1273 (IC base=+0.070)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.623` → IC=+0.201 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.623 (IC base=+0.070)

- **PATRÓN** `ibs_20min` < `0.106` → IC=+0.255 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.106 (IC base=+0.026)

### GBM_LATE_60M#SOL#60min
- **PATRÓN** `ibs_20min` > `0.9861` → IC=+0.193 (n=262)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 0.9861 (IC base=+0.024)

- **PATRÓN** `dist_vwap_pct` > `0.4644` → IC=+0.126 (n=263)

  - _Acción_: Kelly boost +0.63€ cuando `dist_vwap_pct` > 0.4644 (IC base=+0.024)

- **PATRÓN** `sigma_h` < `0.0096` → IC=+0.187 (n=314)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0096 (IC base=+0.082)

- **PATRÓN** `ibs_20min` < `0.4783` → IC=+0.179 (n=440)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.4783 (IC base=+0.082)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.779` → IC=+0.280 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.779 (IC base=+0.082)

- **PATRÓN** `volumen_regimen` > `1.1045` → IC=+0.185 (n=147)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` > 1.1045 (IC base=+0.082)

- **PATRÓN** `volumen_pendiente_norm` > `0.2808` → IC=+0.183 (n=58)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.2808 (IC base=+0.082)

- **PATRÓN** `volumen_spike_ratio` > `1.5612` → IC=+0.127 (n=368)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` > 1.5612 (IC base=+0.082)

### GBM_LATE_60M_FADE
- **FILTRO** `sigma_h` < `0.0059` → IC=-0.246 (n=191)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0059
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=191)

- **FILTRO** `dist_vwap_pct` > `0.2381` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2381
  - _Potencial_: sin este filtro IC_bueno=-0.218 (n=367)

- **FILTRO** `volumen_regimen` < `0.8572` → IC=-0.305 (n=126)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.8572
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=256)

- **FILTRO** `libro_liquidez` < `903.3651` → IC=-0.232 (n=95)

  - _Acción_: SKIP cuando `libro_liquidez` < 903.3651
  - _Potencial_: sin este filtro IC_bueno=-0.220 (n=287)

- **FILTRO** `hora_utc` > `11.0` → IC=-0.309 (n=150)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.253 (n=184)

- **FILTRO** `dist_vwap_pct` > `0.4428` → IC=-0.409 (n=20)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4428
  - _Potencial_: sin este filtro IC_bueno=-0.269 (n=314)

- **FILTRO** `sigma_ewma_delta_pct` > `9.697` → IC=-0.328 (n=27)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 9.697
  - _Potencial_: sin este filtro IC_bueno=-0.274 (n=307)

- **FILTRO** `volumen_pendiente_norm` > `0.0453` → IC=-0.375 (n=30)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0453
  - _Potencial_: sin este filtro IC_bueno=-0.264 (n=214)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `volumen_regimen` < `1.4093` → IC=-0.287 (n=73)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.4093
  - _Potencial_: sin este filtro IC_bueno=-0.159 (n=39)

- **FILTRO** `sigma_h` < `0.0033` → IC=-0.257 (n=72)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0033
  - _Potencial_: sin este filtro IC_bueno=-0.240 (n=75)

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
- **FILTRO** `hora_utc` > `5.0` → IC=-0.344 (n=43)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.191 (n=95)

- **FILTRO** `volumen_pendiente_norm` > `0.1196` → IC=-0.258 (n=31)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1196
  - _Potencial_: sin este filtro IC_bueno=-0.238 (n=82)

- **FILTRO** `sigma_h` < `0.0113` → IC=-0.322 (n=43)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0113
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=15)

- **FILTRO** `sigma_ewma_delta_pct` > `4.698` → IC=-0.382 (n=15)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.698
  - _Potencial_: sin este filtro IC_bueno=-0.211 (n=43)

- **FILTRO** `volumen_regimen` < `0.914` → IC=-0.452 (n=19)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.914
  - _Potencial_: sin este filtro IC_bueno=-0.159 (n=39)

### GBM_LATE_60M_PYCONFIRMADO
- **PATRÓN** `sigma_h` > `0.0086` → IC=+0.266 (n=242)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0086 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.194 (n=377)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 15.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` > `0.6774` → IC=+0.183 (n=727)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.6774 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` > `0.8076` → IC=+0.282 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8076 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.608` → IC=+0.161 (n=396)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 3.608 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` < `0.6244` → IC=+0.182 (n=243)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 0.6244 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` > `1.2135` → IC=+0.152 (n=242)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 1.2135 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` < `0.0701` → IC=+0.181 (n=541)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` < 0.0701 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `1.3986` → IC=+0.203 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3986 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.429` → IC=+0.157 (n=199)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 10.429 (IC base=+0.031)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **PATRÓN** `sigma_h` > `0.0065` → IC=+0.153 (n=73)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` > 0.0065 (IC base=+0.043)

- **PATRÓN** `ibs_20min` > `0.7913` → IC=+0.120 (n=193)

  - _Acción_: Kelly boost +0.60€ cuando `ibs_20min` > 0.7913 (IC base=+0.043)

- **PATRÓN** `dist_vwap_pct` > `0.6267` → IC=+0.198 (n=41)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.6267 (IC base=+0.043)

- **PATRÓN** `ibs_20min` < `0.2374` → IC=+0.147 (n=409)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` < 0.2374 (IC base=+0.087)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.162` → IC=+0.125 (n=94)

  - _Acción_: Kelly boost +0.62€ cuando `sigma_ewma_delta_pct` > 11.162 (IC base=+0.087)

- **PATRÓN** `volumen_pendiente_norm` > `0.2729` → IC=+0.143 (n=68)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` > 0.2729 (IC base=+0.087)

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
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=129)

- **FILTRO** `dist_vwap_pct` > `0.1816` → IC=-0.167 (n=37)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1816
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=157)

- **PATRÓN** `sigma_h` > `0.01` → IC=+0.300 (n=123)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.01 (IC base=+0.257)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.302 (n=190)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.257)

- **PATRÓN** `ibs_20min` > `0.5882` → IC=+0.284 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5882 (IC base=+0.257)

- **PATRÓN** `dist_vwap_pct` > `0.6973` → IC=+0.394 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6973 (IC base=+0.257)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.832` → IC=+0.359 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.832 (IC base=+0.257)

- **PATRÓN** `volumen_regimen` < `0.68` → IC=+0.293 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.68 (IC base=+0.257)

- **PATRÓN** `volumen_pendiente_norm` > `0.0966` → IC=+0.318 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0966 (IC base=+0.257)

- **PATRÓN** `volumen_spike_ratio` < `1.3961` → IC=+0.338 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3961 (IC base=+0.257)

- **PATRÓN** `volumen_spike_ratio` > `2.3741` → IC=+0.308 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3741 (IC base=+0.257)

### LATE_WINDOW_5MIN
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.329 (n=115)

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

- **PATRÓN** `drift_ventana_pct` |x|> `0.3474` → IC=+0.302 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3474 (IC base=+0.269)

- **PATRÓN** `elapsed_s` > `230.1` → IC=+0.357 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 230.1 (IC base=+0.269)

- **PATRÓN** `drift_15min` |x|≤ `2.3044` → IC=+0.311 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3044 (IC base=+0.269)

- **PATRÓN** `drift_60min` |x|≤ `0.6421` → IC=+0.312 (n=67)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6421 (IC base=+0.269)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.329 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.269)

- **PATRÓN** `ballena_activa_n` < `1768.0` → IC=+0.314 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1768.0 (IC base=+0.269)

### LATE_WINDOW_5MIN#BTC#5min
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.329 (n=115)

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

- **PATRÓN** `drift_ventana_pct` |x|> `0.3474` → IC=+0.302 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3474 (IC base=+0.269)

- **PATRÓN** `elapsed_s` > `230.1` → IC=+0.357 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 230.1 (IC base=+0.269)

- **PATRÓN** `drift_15min` |x|≤ `2.3044` → IC=+0.311 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3044 (IC base=+0.269)

- **PATRÓN** `drift_60min` |x|≤ `0.6421` → IC=+0.312 (n=67)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6421 (IC base=+0.269)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.329 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.269)

- **PATRÓN** `ballena_activa_n` < `1768.0` → IC=+0.314 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1768.0 (IC base=+0.269)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.124 (n=1467)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` > 0.5 (IC base=+0.098)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.124 (n=1467)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` > 0.5 (IC base=+0.098)

### LIQUIDACIONES_15M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=250)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=250)

- **FILTRO** `libro_liquidez` < `6919.5202` → IC=-0.152 (n=133)

  - _Acción_: SKIP cuando `libro_liquidez` < 6919.5202
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=133)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=914)

### LIQUIDACIONES_15M#BNB#15min
- **PATRÓN** `liq_usd_total` > `1200.92` → IC=+0.227 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `liq_usd_total` > 1200.92 (IC base=+0.037)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `libro_liquidez` < `12324.2702` → IC=-0.152 (n=44)

  - _Acción_: SKIP cuando `libro_liquidez` < 12324.2702
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=90)

### LIQUIDACIONES_15M#DOGE#15min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.152 (n=21)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=28)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.167 (n=28)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 10.0 (IC base=+0.029)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `hora_utc` < `10.0` → IC=-0.184 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=40)

### LIQUIDACIONES_15M#SOL#15min
- **FILTRO** `hora_utc` > `4.0` → IC=-0.180 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 4.0
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=14)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=254)

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
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=3949)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=154)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=111)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.278 (n=34)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=141)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.180 (n=48)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 21.0 (IC base=-0.076)

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
- **PATRÓN** `liq_n` > `3.0` → IC=+0.333 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `liq_n` > 3.0 (IC base=+0.190)

- **PATRÓN** `liq_usd_total` > `3798.53` → IC=+0.364 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `liq_usd_total` > 3798.53 (IC base=+0.190)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.243 (n=33)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.200 (n=38)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.190)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.227 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.505 (IC base=+0.190)

- **PATRÓN** `libro_liquidez` > `2323.928` → IC=+0.207 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2323.928 (IC base=+0.190)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=1609)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=1563)

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
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=730)

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
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=449)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=430)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.143 (n=194)

  - _Acción_: Kelly boost +0.71€ cuando `py_entrada` < 0.495 (IC base=+0.022)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=1017)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=1017)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=1291)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=1291)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=295)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=295)

- **FILTRO** `py_entrada` < `0.42` → IC=-0.141 (n=76)

  - _Acción_: SKIP cuando `py_entrada` < 0.42
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=234)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.136 (n=64)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=356)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=405)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=302)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=405)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=405)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.120 (n=185)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=250)

- **FILTRO** `libro_liquidez` < `553.1995` → IC=-0.145 (n=108)

  - _Acción_: SKIP cuando `libro_liquidez` < 553.1995
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=327)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=370)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `hora_utc` > `14.0` → IC=-0.159 (n=83)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=97)

- **FILTRO** `py_entrada` > `0.52` → IC=-0.121 (n=56)

  - _Acción_: SKIP cuando `py_entrada` > 0.52
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=30)

- **FILTRO** `hora_utc` < `17.0` → IC=-0.131 (n=63)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=23)

### LIQUIDACIONES_DEPTH_FASE0#BTC#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.131 (n=299)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=745)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **FILTRO** `py_entrada` > `0.57` → IC=-0.128 (n=436)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=520)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.143 (n=317)

  - _Acción_: Kelly boost +0.71€ cuando `py_entrada` < 0.5 (IC base=-0.013)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` > `0.57` → IC=-0.123 (n=367)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.075 (n=377)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` > `0.58` → IC=-0.129 (n=348)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=414)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.134 (n=274)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=596)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.44` → IC=-0.133 (n=524)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=527)

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
- **FILTRO** `py_entrada` < `0.46` → IC=-0.175 (n=8051)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=25638)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.173 (n=8526)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=26266)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.189 (n=1562)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=4689)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.147 (n=2079)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.094 (n=4086)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.134 (n=1611)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` > 1.0 (IC base=+0.041)

- **PATRÓN** `py_entrada` < `0.505` → IC=+0.126 (n=3129)

  - _Acción_: Kelly boost +0.63€ cuando `py_entrada` < 0.505 (IC base=+0.013)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` < `0.44` → IC=-0.173 (n=1119)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=3551)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.179 (n=1197)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=3690)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` > `0.62` → IC=-0.201 (n=1548)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.087 (n=4773)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.136 (n=1919)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` > 1.0 (IC base=+0.034)

- **PATRÓN** `libro_liquidez` > `1737.7254` → IC=+0.120 (n=2121)

  - _Acción_: Kelly boost +0.60€ cuando `libro_liquidez` > 1737.7254 (IC base=+0.034)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.485` → IC=-0.161 (n=1556)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=4718)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=2442)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.162 (n=772)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=2366)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.180 (n=973)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=3078)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=4030)

- **FILTRO** `ballena_activa_n` > `32.0` → IC=-0.127 (n=1366)

  - _Acción_: SKIP cuando `ballena_activa_n` > 32.0
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=2652)

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
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=1084)

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
- **FILTRO** `libro_spread` > `0.01` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=974)

- **FILTRO** `ballena_activa_n` > `23.0` → IC=-0.191 (n=390)

  - _Acción_: SKIP cuando `ballena_activa_n` > 23.0
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=799)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.135 (n=22977)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.091 (n=51548)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.299 (n=17930)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=56595)

- **FILTRO** `ibs_7min` < `0.215` → IC=-0.234 (n=18630)

  - _Acción_: SKIP cuando `ibs_7min` < 0.215
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=55895)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.152 (n=25279)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=49246)

- **FILTRO** `py_entrada` > `0.68` → IC=-0.252 (n=21784)

  - _Acción_: SKIP cuando `py_entrada` > 0.68
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=71402)

- **FILTRO** `ibs_7min` > `0.2821` → IC=-0.184 (n=23285)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2821
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=69901)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.158 (n=3226)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=10062)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.318 (n=3283)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=10005)

- **FILTRO** `ibs_7min` < `0.7101` → IC=-0.252 (n=4384)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7101
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=8904)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.152 (n=2793)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=10495)

- **FILTRO** `py_entrada` > `0.72` → IC=-0.277 (n=3934)

  - _Acción_: SKIP cuando `py_entrada` > 0.72
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=12148)

- **FILTRO** `ibs_7min` > `0.7778` → IC=-0.211 (n=4014)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7778
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=12068)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.264 (n=2994)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=9400)

- **FILTRO** `ibs_7min` < `0.7137` → IC=-0.210 (n=3098)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7137
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=9296)

- **FILTRO** `ballena_activa_n` > `156.0` → IC=-0.202 (n=3081)

  - _Acción_: SKIP cuando `ballena_activa_n` > 156.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=9313)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.268 (n=2903)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=9757)

- **FILTRO** `ibs_7min` > `0.2664` → IC=-0.192 (n=3164)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2664
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=9496)

- **FILTRO** `ballena_activa_n` > `153.0` → IC=-0.181 (n=3155)

  - _Acción_: SKIP cuando `ballena_activa_n` > 153.0
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=9505)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.166 (n=3081)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=9647)

- **FILTRO** `py_entrada` < `0.3` → IC=-0.325 (n=3033)

  - _Acción_: SKIP cuando `py_entrada` < 0.3
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=9695)

- **FILTRO** `ibs_7min` < `0.2857` → IC=-0.251 (n=4193)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2857
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=8535)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.202 (n=2522)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=10206)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.259 (n=4128)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=12915)

- **FILTRO** `ibs_7min` > `0.7308` → IC=-0.183 (n=4259)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7308
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=12784)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.263 (n=2994)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=9057)

- **FILTRO** `ibs_7min` < `0.7137` → IC=-0.197 (n=3012)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7137
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=9039)

- **FILTRO** `ballena_activa_n` > `25.0` → IC=-0.192 (n=2914)

  - _Acción_: SKIP cuando `ballena_activa_n` > 25.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=9137)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.259 (n=2920)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=9632)

- **FILTRO** `ibs_7min` > `0.273` → IC=-0.177 (n=3137)

  - _Acción_: SKIP cuando `ibs_7min` > 0.273
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=9415)

- **FILTRO** `ballena_activa_n` > `24.0` → IC=-0.172 (n=3038)

  - _Acción_: SKIP cuando `ballena_activa_n` > 24.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=9514)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.32` → IC=-0.300 (n=2845)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=9090)

- **FILTRO** `ibs_7min` < `0.7` → IC=-0.235 (n=3888)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=8047)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.218 (n=2926)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=9009)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.199 (n=4379)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=13646)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.133 (n=3921)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.108 (n=8208)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.310 (n=2908)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=9221)

- **FILTRO** `ibs_7min` < `0.7344` → IC=-0.221 (n=4002)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7344
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=8127)

- **FILTRO** `ballena_activa_n` > `9.0` → IC=-0.206 (n=2679)

  - _Acción_: SKIP cuando `ballena_activa_n` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.091 (n=9450)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.234 (n=3896)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=12928)

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

- **FILTRO** `py_entrada` > `0.545` → IC=-0.157 (n=170)

  - _Acción_: SKIP cuando `py_entrada` > 0.545
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=627)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=1458)

- **FILTRO** `py_entrada` > `0.565` → IC=-0.172 (n=260)

  - _Acción_: SKIP cuando `py_entrada` > 0.565
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=902)

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
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=581)

- **FILTRO** `libro_liquidez` < `3304.2295` → IC=-0.151 (n=193)

  - _Acción_: SKIP cuando `libro_liquidez` < 3304.2295
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=580)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=396)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.4308` → IC=+0.147 (n=693)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.74€ cuando `delta_ratio` |x|> 0.4308 (IC base=+0.123)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.128 (n=1373)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 14.0 (IC base=+0.123)

- **PATRÓN** `total_vol_5m` < `421.6695` → IC=+0.160 (n=509)

  - _Acción_: Kelly boost +0.80€ cuando `total_vol_5m` < 421.6695 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `3557.272` → IC=+0.135 (n=692)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 3557.272 (IC base=+0.123)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `14.0` → IC=+0.181 (n=183)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 14.0 (IC base=+0.134)

- **PATRÓN** `total_vol_5m` < `287.685` → IC=+0.164 (n=242)

  - _Acción_: Kelly boost +0.82€ cuando `total_vol_5m` < 287.685 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `2506.369` → IC=+0.242 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2506.369 (IC base=+0.134)

- **PATRÓN** `ballena_activa_n` < `6.0` → IC=+0.138 (n=175)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 6.0 (IC base=+0.134)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `delta_ratio` |x|> `0.4381` → IC=+0.151 (n=104)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.75€ cuando `delta_ratio` |x|> 0.4381 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.136 (n=292)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 15.0 (IC base=+0.117)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.122 (n=379)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.04 (IC base=+0.117)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4165` → IC=+0.170 (n=192)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.85€ cuando `delta_ratio` |x|> 0.4165 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.145 (n=266)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.123)

- **PATRÓN** `total_vol_5m` < `857.788` → IC=+0.148 (n=288)

  - _Acción_: Kelly boost +0.74€ cuando `total_vol_5m` < 857.788 (IC base=+0.123)

- **PATRÓN** `ballena_activa_n` < `59.0` → IC=+0.167 (n=97)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 59.0 (IC base=+0.123)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.4317` → IC=+0.208 (n=118)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio` |x|> 0.4317 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.174 (n=188)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 12.0 (IC base=+0.141)

- **PATRÓN** `total_vol_5m` < `4632.142` → IC=+0.182 (n=174)

  - _Acción_: Kelly boost +0.91€ cuando `total_vol_5m` < 4632.142 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `3718.2204` → IC=+0.157 (n=173)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 3718.2204 (IC base=+0.141)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `hora_utc` < `14.0` → IC=+0.130 (n=279)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 14.0 (IC base=+0.100)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.134 (n=203)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.100)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `4.8182` → IC=-0.203 (n=116)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.8182
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=118)

- **FILTRO** `sigma_h` > `0.0055` → IC=-0.194 (n=433)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0055
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=434)

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.147 (n=287)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0045 (IC base=-0.062)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `T_h` > `88.1766` → IC=-0.212 (n=64)

  - _Acción_: SKIP cuando `T_h` > 88.1766
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=196)

- **FILTRO** `pct_vs_K` |x|> `4.2538` → IC=-0.242 (n=64)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.2538
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=196)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.286 (n=87)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=-0.015)

- **PATRÓN** `pct_vs_K` |x|≤ `1.73` → IC=+0.182 (n=86)

  - _Acción_: Kelly boost +0.91€ cuando `pct_vs_K` |x|≤ 1.73 (IC base=-0.015)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `T_h` < `251.7955` → IC=-0.192 (n=63)

  - _Acción_: SKIP cuando `T_h` < 251.7955
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=21)

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

- **FILTRO** `pct_vs_K` |x|> `2.4904` → IC=-0.364 (n=86)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.4904
  - _Potencial_: sin este filtro IC_bueno=-0.110 (n=167)

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

- **FILTRO** `pct_vs_K` |x|> `2.8988` → IC=-0.415 (n=69)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.8988
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=138)

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

- **FILTRO** `T_h` > `34.5304` → IC=-0.219 (n=112)

  - _Acción_: SKIP cuando `T_h` > 34.5304
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
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=436)

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
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=178)

- **PATRÓN** `streak_estiramiento` < `0.2292` → IC=+0.132 (n=66)

  - _Acción_: Kelly boost +0.66€ cuando `streak_estiramiento` < 0.2292 (IC base=+0.036)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.139 (n=120)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 11.0 (IC base=+0.095)

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
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=1073)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=1346)

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
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=5022)

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
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=2887)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.188 (n=1821)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0054 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.2213` → IC=+0.157 (n=5462)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.2213 (IC base=+0.139)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1346` → IC=+0.153 (n=2249)

  - _Acción_: Kelly boost +0.77€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1346 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.150 (n=5032)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 6.0 (IC base=+0.139)

- **PATRÓN** `ibs_15` > `0.5769` → IC=+0.222 (n=4885)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5769 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.135` → IC=+0.130 (n=2563)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` > 0.135 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.281` → IC=+0.246 (n=1036)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.281 (IC base=+0.139)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=3108)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `4530.5934` → IC=+0.168 (n=1821)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 4530.5934 (IC base=+0.139)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=2094)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.221 (n=800)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0057 (IC base=+0.200)

- **PATRÓN** `drift_60min` |x|≤ `0.0774` → IC=+0.246 (n=352)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0774 (IC base=+0.200)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2676` → IC=+0.221 (n=267)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2676 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.227 (n=733)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.200)

- **PATRÓN** `ibs_15` > `0.7064` → IC=+0.272 (n=800)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7064 (IC base=+0.200)

- **PATRÓN** `dist_vwap_pct` > `0.3722` → IC=+0.227 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3722 (IC base=+0.200)

- **PATRÓN** `dist_vwap_pct` < `0.1092` → IC=+0.201 (n=536)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1092 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.371` → IC=+0.313 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.371 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.203 (n=1036)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.200)

- **PATRÓN** `libro_liquidez` > `11847.0948` → IC=+0.220 (n=533)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11847.0948 (IC base=+0.200)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.007` → IC=+0.147 (n=1002)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.007 (IC base=+0.132)

- **PATRÓN** `drift_60min` |x|≤ `0.1094` → IC=+0.151 (n=669)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.1094 (IC base=+0.132)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1408` → IC=+0.133 (n=668)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.66€ cuando `delta_ratio_macro` |x|> 0.1408 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.137 (n=915)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 6.0 (IC base=+0.132)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.133 (n=1005)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 16.0 (IC base=+0.132)

- **PATRÓN** `ibs_15` > `0.4963` → IC=+0.219 (n=1002)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.4963 (IC base=+0.132)

- **PATRÓN** `dist_vwap_pct` > `0.1187` → IC=+0.151 (n=626)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.1187 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.945` → IC=+0.282 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.945 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `5973.6174` → IC=+0.171 (n=454)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 5973.6174 (IC base=+0.132)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `ibs_15` > `0.2551` → IC=-0.124 (n=216)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.2551
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=422)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `ibs_15` > `0.7632` → IC=+0.132 (n=704)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.66€ cuando `ibs_15` > 0.7632 (IC base=+0.052)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` < `0.0253` → IC=+0.164 (n=1367)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0253 (IC base=+0.152)

- **PATRÓN** `sigma_h` > `0.0129` → IC=+0.156 (n=1367)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0129 (IC base=+0.152)

- **PATRÓN** `drift_60min` |x|≤ `0.225` → IC=+0.176 (n=1367)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.225 (IC base=+0.152)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0982` → IC=+0.217 (n=422)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0982 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.159 (n=1250)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 6.0 (IC base=+0.152)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.157 (n=1212)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 14.0 (IC base=+0.152)

- **PATRÓN** `ibs_15` > `0.5417` → IC=+0.225 (n=1223)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5417 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` > `0.5296` → IC=+0.185 (n=319)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.5296 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.919` → IC=+0.199 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.919 (IC base=+0.152)

- **PATRÓN** `libro_liquidez` > `2947.2049` → IC=+0.198 (n=620)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 2947.2049 (IC base=+0.152)

- **PATRÓN** `ibs_15` < `0.1099` → IC=+0.151 (n=1047)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.76€ cuando `ibs_15` < 0.1099 (IC base=+0.068)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` > `0.0054` → IC=+0.393 (n=343)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0054 (IC base=+0.364)

- **PATRÓN** `drift_60min` |x|≤ `0.1115` → IC=+0.366 (n=504)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1115 (IC base=+0.364)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1503` → IC=+0.379 (n=503)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1503 (IC base=+0.364)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1351` → IC=+0.382 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1351 (IC base=+0.364)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.372 (n=797)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.364)

- **PATRÓN** `ibs_15` > `0.7903` → IC=+0.393 (n=756)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7903 (IC base=+0.364)

- **PATRÓN** `dist_vwap_pct` > `0.1534` → IC=+0.380 (n=448)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1534 (IC base=+0.364)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.976` → IC=+0.396 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.976 (IC base=+0.364)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.368 (n=921)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.364)

- **PATRÓN** `libro_liquidez` > `9610.6074` → IC=+0.381 (n=343)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9610.6074 (IC base=+0.364)

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

- **PATRÓN** `libro_liquidez` > `15195.4571` → IC=+0.382 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15195.4571 (IC base=+0.362)

- **PATRÓN** `ballena_activa_n` < `413.0` → IC=+0.389 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 413.0 (IC base=+0.362)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.369 (n=388)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.365)

- **PATRÓN** `sigma_h` > `0.006` → IC=+0.382 (n=176)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.006 (IC base=+0.365)

- **PATRÓN** `drift_60min` |x|≤ `0.1077` → IC=+0.370 (n=259)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1077 (IC base=+0.365)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1294` → IC=+0.381 (n=258)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1294 (IC base=+0.365)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.296` → IC=+0.374 (n=316)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.296 (IC base=+0.365)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.369 (n=388)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.365)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.374 (n=181)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.365)

- **PATRÓN** `ibs_15` > `0.764` → IC=+0.392 (n=387)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.764 (IC base=+0.365)

- **PATRÓN** `dist_vwap_pct` > `0.159` → IC=+0.373 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.159 (IC base=+0.365)

- **PATRÓN** `dist_vwap_pct` < `0.2797` → IC=+0.366 (n=356)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2797 (IC base=+0.365)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.991` → IC=+0.393 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.991 (IC base=+0.365)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.369 (n=440)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.365)

- **PATRÓN** `libro_liquidez` > `4142.643` → IC=+0.376 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4142.643 (IC base=+0.365)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0075` → IC=-0.198 (n=2736)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0075
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=2738)

- **FILTRO** `drift_15min` |x|> `0.9116` → IC=-0.148 (n=1368)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.9116
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=4105)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.219 (n=2308)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=3166)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1411` → IC=+0.213 (n=472)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1411 (IC base=-0.083)

- **PATRÓN** `ibs_15` > `0.6288` → IC=+0.277 (n=1242)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6288 (IC base=-0.083)

- **PATRÓN** `dist_vwap_pct` > `0.1103` → IC=+0.200 (n=728)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1103 (IC base=-0.083)

- **PATRÓN** `dist_vwap_pct` < `0.259` → IC=+0.196 (n=1062)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` < 0.259 (IC base=-0.083)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2343` → IC=+0.270 (n=1672)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2343 (IC base=-0.004)

- **PATRÓN** `ibs_15` < `0.3703` → IC=+0.285 (n=5016)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3703 (IC base=-0.004)

- **PATRÓN** `dist_vwap_pct` > `0.6499` → IC=+0.280 (n=702)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6499 (IC base=-0.004)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0321` → IC=-0.220 (n=2609)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0321
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=872)

- **FILTRO** `sigma_h` < `0.0038` → IC=-0.214 (n=870)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0038
  - _Potencial_: sin este filtro IC_bueno=-0.175 (n=2611)

- **FILTRO** `sigma_ewma_delta_pct` > `22.161` → IC=-0.253 (n=492)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 22.161
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=2989)

- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.156 (n=332)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0031 (IC base=+0.070)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2673` → IC=+0.282 (n=145)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2673 (IC base=+0.070)

- **PATRÓN** `ibs_15` > `0.7593` → IC=+0.317 (n=434)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7593 (IC base=+0.070)

- **PATRÓN** `dist_vwap_pct` > `0.1023` → IC=+0.271 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1023 (IC base=+0.070)

- **PATRÓN** `dist_vwap_pct` < `0.2425` → IC=+0.274 (n=388)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2425 (IC base=+0.070)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.088` → IC=+0.153 (n=223)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 22.088 (IC base=+0.070)

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
  - _Potencial_: sin este filtro IC_bueno=+0.152 (n=815)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.161 (n=550)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0059 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.159` → IC=+0.163 (n=550)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.159 (IC base=+0.146)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3006` → IC=+0.195 (n=490)

  - _Acción_: Kelly boost +0.98€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3006 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.162 (n=445)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 11.0 (IC base=+0.146)

- **PATRÓN** `ibs_15` > `0.5679` → IC=+0.241 (n=624)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5679 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.6301` → IC=+0.161 (n=116)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 0.6301 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` < `0.2672` → IC=+0.147 (n=582)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.2672 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.028` → IC=+0.258 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.028 (IC base=+0.146)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=815)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `7306.8584` → IC=+0.160 (n=283)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 7306.8584 (IC base=+0.146)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.254 (n=1292)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0061 (IC base=+0.243)

- **PATRÓN** `drift_60min` |x|≤ `0.3548` → IC=+0.248 (n=1705)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3548 (IC base=+0.243)

- **PATRÓN** `drift_15min` |x|≤ `0.7801` → IC=+0.259 (n=1705)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7801 (IC base=+0.243)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2137` → IC=+0.264 (n=878)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2137 (IC base=+0.243)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.253 (n=714)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.243)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.242 (n=1330)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.243)

- **PATRÓN** `ibs_15` < `0.3831` → IC=+0.273 (n=1937)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3831 (IC base=+0.243)

- **PATRÓN** `dist_vwap_pct` > `0.3769` → IC=+0.271 (n=483)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3769 (IC base=+0.243)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.263` → IC=+0.248 (n=752)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.263 (IC base=+0.243)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.182` → IC=+0.247 (n=2026)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.182 (IC base=+0.243)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1848` → IC=-0.270 (n=319)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1848
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=958)

- **FILTRO** `sigma_h` > `0.0105` → IC=-0.238 (n=434)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0105
  - _Potencial_: sin este filtro IC_bueno=-0.183 (n=843)

- **FILTRO** `drift_60min` |x|> `0.1722` → IC=-0.268 (n=433)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1722
  - _Potencial_: sin este filtro IC_bueno=-0.168 (n=844)

- **FILTRO** `drift_15min` |x|> `0.9101` → IC=-0.285 (n=319)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.9101
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=958)

- **FILTRO** `sigma_ewma_delta_pct` > `16.92` → IC=-0.135 (n=672)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 16.92
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=5368)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1455` → IC=+0.188 (n=46)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.94€ cuando `delta_ratio_macro` |x|> 0.1455 (IC base=-0.202)

- **PATRÓN** `ibs_15` > `0.5625` → IC=+0.234 (n=62)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5625 (IC base=-0.202)

- **PATRÓN** `dist_vwap_pct` > `0.2752` → IC=+0.143 (n=26)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.2752 (IC base=-0.202)

- **PATRÓN** `dist_vwap_pct` < `0.1292` → IC=+0.154 (n=53)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.1292 (IC base=-0.202)

- **PATRÓN** `delta_ratio_macro` |x|> `0.127` → IC=+0.236 (n=571)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.127 (IC base=-0.030)

- **PATRÓN** `ibs_15` < `0.381` → IC=+0.294 (n=859)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.381 (IC base=-0.030)

- **PATRÓN** `dist_vwap_pct` > `0.6795` → IC=+0.240 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6795 (IC base=-0.030)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0131` → IC=-0.242 (n=1168)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0131
  - _Potencial_: sin este filtro IC_bueno=-0.145 (n=390)

- **FILTRO** `drift_60min` |x|> `0.1514` → IC=-0.244 (n=389)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1514
  - _Potencial_: sin este filtro IC_bueno=-0.209 (n=1169)

- **FILTRO** `libro_spread` > `0.04` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.04
  - _Potencial_: sin este filtro IC_bueno=-0.217 (n=1539)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.218)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.218)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1183` → IC=+0.301 (n=522)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1183 (IC base=-0.015)

- **PATRÓN** `ibs_15` < `0.1364` → IC=+0.310 (n=799)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.1364 (IC base=-0.015)

- **PATRÓN** `dist_vwap_pct` > `0.7602` → IC=+0.332 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7602 (IC base=-0.015)

### UPDOWN_GBM_ETH_15M_HORA7
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.167 (n=52)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0065 (IC base=+0.106)

- **PATRÓN** `drift_60min` |x|≤ `0.1878` → IC=+0.148 (n=52)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.1878 (IC base=+0.106)

- **PATRÓN** `drift_15min` |x|≤ `0.3826` → IC=+0.300 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3826 (IC base=+0.106)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.235` → IC=+0.186 (n=33)

  - _Acción_: Kelly boost +0.93€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.235 (IC base=+0.106)

- **PATRÓN** `ibs_15` > `0.8434` → IC=+0.308 (n=24)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8434 (IC base=+0.106)

- **PATRÓN** `dist_vwap_pct` > `0.4542` → IC=+0.132 (n=17)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` > 0.4542 (IC base=+0.106)

- **PATRÓN** `dist_vwap_pct` < `0.1025` → IC=+0.186 (n=33)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` < 0.1025 (IC base=+0.106)

- **PATRÓN** `libro_liquidez` > `3648.0666` → IC=+0.130 (n=52)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 3648.0666 (IC base=+0.106)

- **PATRÓN** `ballena_activa_n` < `116.0` → IC=+0.147 (n=49)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 116.0 (IC base=+0.106)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.167 (n=52)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0065 (IC base=+0.106)

- **PATRÓN** `drift_60min` |x|≤ `0.1878` → IC=+0.148 (n=52)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.1878 (IC base=+0.106)

- **PATRÓN** `drift_15min` |x|≤ `0.3826` → IC=+0.300 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3826 (IC base=+0.106)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.235` → IC=+0.186 (n=33)

  - _Acción_: Kelly boost +0.93€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.235 (IC base=+0.106)

- **PATRÓN** `ibs_15` > `0.8434` → IC=+0.308 (n=24)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8434 (IC base=+0.106)

- **PATRÓN** `dist_vwap_pct` > `0.4542` → IC=+0.132 (n=17)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` > 0.4542 (IC base=+0.106)

- **PATRÓN** `dist_vwap_pct` < `0.1025` → IC=+0.186 (n=33)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` < 0.1025 (IC base=+0.106)

- **PATRÓN** `libro_liquidez` > `3648.0666` → IC=+0.130 (n=52)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 3648.0666 (IC base=+0.106)

- **PATRÓN** `ballena_activa_n` < `116.0` → IC=+0.147 (n=49)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 116.0 (IC base=+0.106)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.299 (n=456)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0033 (IC base=+0.282)

- **PATRÓN** `drift_60min` |x|≤ `0.072` → IC=+0.311 (n=601)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.072 (IC base=+0.282)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1522` → IC=+0.283 (n=910)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1522 (IC base=+0.282)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2223` → IC=+0.288 (n=833)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2223 (IC base=+0.282)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.294 (n=1412)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.282)

- **PATRÓN** `ibs_15` > `0.838` → IC=+0.309 (n=1367)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.838 (IC base=+0.282)

- **PATRÓN** `dist_vwap_pct` > `0.2619` → IC=+0.313 (n=593)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2619 (IC base=+0.282)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.932` → IC=+0.388 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.932 (IC base=+0.282)

- **PATRÓN** `libro_liquidez` > `13157.6607` → IC=+0.301 (n=456)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13157.6607 (IC base=+0.282)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.302 (n=241)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.274)

- **PATRÓN** `drift_60min` |x|≤ `0.0585` → IC=+0.302 (n=241)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0585 (IC base=+0.274)

- **PATRÓN** `drift_15min` |x|≤ `0.3844` → IC=+0.275 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3844 (IC base=+0.274)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2695` → IC=+0.277 (n=240)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2695 (IC base=+0.274)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3948` → IC=+0.280 (n=647)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3948 (IC base=+0.274)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.292 (n=754)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.274)

- **PATRÓN** `ibs_15` > `0.829` → IC=+0.299 (n=720)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.829 (IC base=+0.274)

- **PATRÓN** `dist_vwap_pct` > `0.2515` → IC=+0.311 (n=310)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2515 (IC base=+0.274)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.742` → IC=+0.395 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.742 (IC base=+0.274)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.276 (n=931)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.274)

- **PATRÓN** `libro_liquidez` > `15771.8702` → IC=+0.314 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15771.8702 (IC base=+0.274)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.295 (n=646)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0069 (IC base=+0.289)

- **PATRÓN** `drift_60min` |x|≤ `0.0506` → IC=+0.321 (n=216)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0506 (IC base=+0.289)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0644` → IC=+0.289 (n=646)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0644 (IC base=+0.289)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1008` → IC=+0.313 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1008 (IC base=+0.289)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.300 (n=618)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.289)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.290 (n=459)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.289)

- **PATRÓN** `ibs_15` > `0.8478` → IC=+0.316 (n=646)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8478 (IC base=+0.289)

- **PATRÓN** `dist_vwap_pct` > `0.2774` → IC=+0.319 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2774 (IC base=+0.289)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.243` → IC=+0.373 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.243 (IC base=+0.289)

### UPDOWN_OU_5M
- **FILTRO** `delta_ratio_macro` |x|≤ `0.126` → IC=-0.156 (n=94)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.126
  - _Potencial_: sin este filtro IC_bueno=-0.099 (n=285)

- **FILTRO** `ballena_activa_n` > `32.0` → IC=-0.130 (n=260)

  - _Acción_: SKIP cuando `ballena_activa_n` > 32.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=87)

- **FILTRO** `sigma_h` < `0.0051` → IC=-0.172 (n=123)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0051
  - _Potencial_: sin este filtro IC_bueno=-0.090 (n=369)

- **FILTRO** `ballena_activa_n` > `60.0` → IC=-0.229 (n=57)

  - _Acción_: SKIP cuando `ballena_activa_n` > 60.0
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=174)

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
  - _Potencial_: sin este filtro IC_bueno=-0.156 (n=30)

- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.0863` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.0863
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=10)

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

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5769 sube el IC de +0.139 a +0.222 en UPDOWN_GBM#15min (n=4885). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7064 sube el IC de +0.200 a +0.272 en UPDOWN_GBM#BTC#15min (n=800). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.4963 sube el IC de +0.132 a +0.219 en UPDOWN_GBM#ETH#15min (n=1002). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5417 sube el IC de +0.152 a +0.225 en UPDOWN_GBM#XRP#15min (n=1223). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1099 sube el IC de +0.068 a +0.151 en UPDOWN_GBM#XRP#15min (n=1047). Ya aplicado como kelly_boost=+0.76€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6288 sube el IC de -0.083 a +0.277 en UPDOWN_GBM_15M_TARDIO (n=1242). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3703 sube el IC de -0.004 a +0.285 en UPDOWN_GBM_15M_TARDIO (n=5016). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7593 sube el IC de +0.070 a +0.317 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=434). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.6255 sube el IC de -0.185 a +0.289 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=74). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.5679 sube el IC de +0.146 a +0.241 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=624). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3831 sube el IC de +0.243 a +0.273 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=1937). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de -0.202 a +0.234 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=62). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.381 sube el IC de -0.030 a +0.294 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=859). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.218 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.1364 sube el IC de -0.015 a +0.310 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=799). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_YES, IBS > 0.8434 sube el IC de +0.106 a +0.308 en UPDOWN_GBM_ETH_15M_HORA7 (n=24). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_YES, IBS > 0.8434 sube el IC de +0.106 a +0.308 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=24). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.838 sube el IC de +0.282 a +0.309 en UPDOWN_GBM_IBS_ALTO (n=1367). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.829 sube el IC de +0.274 a +0.299 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=720). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8478 sube el IC de +0.289 a +0.316 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=646). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7903 sube el IC de +0.364 a +0.393 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=756). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8078 sube el IC de +0.362 a +0.384 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=369). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.764 sube el IC de +0.365 a +0.392 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=387). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

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
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 1146 | -0.021 | +73.47€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 1146 | -0.021 | +73.47€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE | 7 | +0.019 | +3.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE#15min | 7 | +0.019 | +3.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 879 | -0.038 | +57.42€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 879 | -0.038 | +57.42€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 182 | +0.065 | +20.03€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 182 | +0.065 | +20.03€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 78 | -0.037 | -7.24€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 78 | -0.037 | -7.24€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 47603 | -0.084 | -6105.52€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 2966 | +0.073 | -303.18€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 44637 | -0.095 | -5802.34€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4820 | -0.113 | -813.02€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4820 | -0.113 | -813.02€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 2966 | +0.073 | -303.18€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 2966 | +0.073 | -303.18€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 4877 | -0.106 | -938.87€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 4877 | -0.106 | -938.87€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 13071 | -0.043 | -1256.95€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 13071 | -0.043 | -1256.95€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 12960 | -0.112 | -1354.36€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 12960 | -0.112 | -1354.36€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 8909 | -0.129 | -1439.13€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 8909 | -0.129 | -1439.13€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 49579 | -0.012 | +2812.60€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 12823 | +0.004 | +1507.66€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 36756 | -0.018 | +1304.93€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 49579 | -0.012 | +2812.60€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 12823 | +0.004 | +1507.66€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 36756 | -0.018 | +1304.93€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 189664 | +0.113 | -7870.98€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#15min | 21864 | +0.180 | -702.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 871 | +0.011 | -72.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 156109 | +0.105 | -6697.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 10820 | +0.093 | -398.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 25868 | +0.103 | -1833.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 77 | -0.171 | +13.24€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 25776 | +0.104 | -1834.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 35909 | +0.124 | -599.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5611 | +0.178 | -238.12€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 25842 | +0.120 | -175.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 4414 | +0.080 | -162.94€ | 1 | 2 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 25919 | +0.098 | -1879.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 88 | -0.111 | +7.94€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 25816 | +0.099 | -1876.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 40513 | +0.123 | -859.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 10184 | +0.178 | -251.39€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 26251 | +0.106 | -541.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 4066 | +0.102 | -58.19€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#SOL | 35557 | +0.112 | -1586.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 5814 | +0.198 | -251.80€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 774 | +0.037 | -18.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 26629 | +0.096 | -1138.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 2340 | +0.102 | -177.56€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO#XRP | 25898 | +0.107 | -1113.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 90 | -0.109 | +17.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 25795 | +0.108 | -1131.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 30753 | +0.192 | -2147.60€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 30753 | +0.192 | -2147.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 6967 | +0.169 | -727.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 6967 | +0.169 | -727.70€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 4457 | +0.196 | -170.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 4457 | +0.196 | -170.04€ | 3 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 6825 | +0.175 | -598.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 6825 | +0.175 | -598.50€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 5714 | +0.251 | -203.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 5714 | +0.251 | -203.33€ | 0 | 4 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 6711 | +0.185 | -461.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 6711 | +0.185 | -461.78€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 1250 | +0.425 | -47.89€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 1250 | +0.425 | -47.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 518 | +0.439 | -5.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 518 | +0.439 | -5.39€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE#15min | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 505 | +0.423 | -20.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 505 | +0.423 | -20.26€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 213 | +0.398 | -18.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 213 | +0.398 | -18.37€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 108777 | +0.199 | -8043.61€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 108777 | +0.199 | -8043.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 18812 | +0.178 | -2159.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 18812 | +0.178 | -2159.41€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 17538 | +0.224 | -581.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 17538 | +0.224 | -581.58€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 18672 | +0.179 | -1997.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 18672 | +0.179 | -1997.49€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 17685 | +0.218 | -705.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 17685 | +0.218 | -705.93€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 17973 | +0.203 | -1135.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 17973 | +0.203 | -1135.44€ | 1 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 18097 | +0.196 | -1463.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 18097 | +0.196 | -1463.76€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 41965 | +0.117 | +339.56€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 41965 | +0.117 | +339.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 20891 | +0.117 | +207.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 20891 | +0.117 | +207.65€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 21074 | +0.116 | +131.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 21074 | +0.116 | +131.91€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 2599 | +0.293 | -7.20€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 2599 | +0.293 | -7.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 1189 | +0.282 | -28.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 1189 | +0.282 | -28.27€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 1270 | +0.298 | +15.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 1270 | +0.298 | +15.30€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 140 | +0.345 | +5.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 140 | +0.345 | +5.77€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 1201 | +0.438 | -6.24€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 1201 | +0.438 | -6.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 576 | +0.432 | -10.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 576 | +0.432 | -10.41€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 574 | +0.443 | +2.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 574 | +0.443 | +2.92€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 51 | +0.406 | +1.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 51 | +0.406 | +1.25€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1947 | +0.068 | -85.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 725 | +0.046 | -64.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 1222 | +0.081 | -20.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1513 | +0.076 | -39.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 291 | +0.053 | -19.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 1222 | +0.081 | -20.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 85081 | +0.101 | -1997.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 6861 | +0.096 | +145.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 78220 | +0.101 | -2143.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 46497 | +0.106 | -444.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 6861 | +0.096 | +145.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 39636 | +0.107 | -590.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 18100 | +0.108 | -117.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 18100 | +0.108 | -117.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 20484 | +0.082 | -1435.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 20484 | +0.082 | -1435.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 914 | +0.186 | -109.27€ | 5 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 914 | +0.186 | -109.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 914 | +0.186 | -109.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 914 | +0.186 | -109.27€ | 5 | 4 |
| ✅ GBM_LATE_15M | 57741 | +0.100 | +32236.31€ | 0 | 18 |
| ✅ GBM_LATE_15M#15min | 57741 | +0.100 | +32236.31€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 9558 | +0.227 | +8288.32€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 9558 | +0.227 | +8288.32€ | 0 | 22 |
| ✅ GBM_LATE_15M#BTC | 8858 | +0.176 | +6964.01€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 8858 | +0.176 | +6964.01€ | 0 | 20 |
| ✅ GBM_LATE_15M#DOGE | 10348 | +0.208 | +8207.49€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 10348 | +0.208 | +8207.49€ | 0 | 21 |
| ✅ GBM_LATE_15M#ETH | 7731 | +0.056 | +2476.63€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 7731 | +0.056 | +2476.63€ | 1 | 16 |
| ✅ GBM_LATE_15M#SOL | 8055 | -0.030 | +2079.62€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 8055 | -0.030 | +2079.62€ | 4 | 14 |
| ✅ GBM_LATE_15M#XRP | 13191 | -0.022 | +4220.25€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 13191 | -0.022 | +4220.25€ | 3 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 60887 | +0.085 | +35297.21€ | 0 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 60887 | +0.085 | +35297.21€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 11765 | -0.003 | +6236.91€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 11765 | -0.003 | +6236.91€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 13099 | +0.004 | +3487.01€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 13099 | +0.004 | +3487.01€ | 0 | 11 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 8273 | +0.295 | +9469.40€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 8273 | +0.295 | +9469.40€ | 0 | 20 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 11621 | +0.014 | +3609.73€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 11621 | +0.014 | +3609.73€ | 1 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 9336 | +0.044 | +4160.80€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 9336 | +0.044 | +4160.80€ | 3 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 6793 | +0.316 | +8333.37€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 6793 | +0.316 | +8333.37€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 45655 | +0.178 | +37652.68€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 45655 | +0.178 | +37652.68€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 6872 | +0.240 | +6422.91€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 6872 | +0.240 | +6422.91€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 7226 | +0.139 | +5315.14€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 7226 | +0.139 | +5315.14€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 7349 | +0.225 | +6395.31€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 7349 | +0.225 | +6395.31€ | 0 | 19 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 7826 | +0.129 | +6043.91€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 7826 | +0.129 | +6043.91€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 8645 | +0.118 | +6447.42€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 8645 | +0.118 | +6447.42€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 7737 | +0.233 | +7028.00€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 7737 | +0.233 | +7028.00€ | 0 | 25 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 12422 | +0.125 | +6199.42€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 12422 | +0.125 | +6199.42€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 569 | +0.167 | +390.15€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 569 | +0.167 | +390.15€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 3422 | +0.127 | +1859.61€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 3422 | +0.127 | +1859.61€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 506 | +0.158 | +277.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 506 | +0.158 | +277.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 3578 | +0.123 | +1703.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 3578 | +0.123 | +1703.94€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 3247 | +0.098 | +1278.23€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 3247 | +0.098 | +1278.23€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 1100 | +0.168 | +690.05€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 1100 | +0.168 | +690.05€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO | 57925 | +0.188 | +47686.61€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#15min | 57925 | +0.188 | +47686.61€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 9136 | +0.251 | +8883.91€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 9136 | +0.251 | +8883.91€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 9216 | +0.137 | +6359.54€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 9216 | +0.137 | +6359.54€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 9827 | +0.236 | +8929.27€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 9827 | +0.236 | +8929.27€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 9590 | +0.142 | +7072.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 9590 | +0.142 | +7072.83€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 10284 | +0.122 | +7237.39€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 10284 | +0.122 | +7237.39€ | 0 | 18 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 9872 | +0.241 | +9203.68€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 9872 | +0.241 | +9203.68€ | 0 | 20 |
| ✅ GBM_LATE_5M | 14636 | +0.212 | +11987.31€ | 1 | 26 |
| ✅ GBM_LATE_5M#5min | 14636 | +0.212 | +11987.31€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 1161 | +0.251 | +1121.80€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 1161 | +0.251 | +1121.80€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 3267 | +0.211 | +2815.48€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 3267 | +0.211 | +2815.48€ | 0 | 27 |
| ✅ GBM_LATE_5M#DOGE | 1453 | +0.210 | +1160.11€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1453 | +0.210 | +1160.11€ | 0 | 19 |
| ✅ GBM_LATE_5M#ETH | 4320 | +0.205 | +3266.35€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 4320 | +0.205 | +3266.35€ | 0 | 23 |
| ✅ GBM_LATE_5M#SOL | 2423 | +0.214 | +2050.21€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 2423 | +0.214 | +2050.21€ | 0 | 27 |
| ✅ GBM_LATE_5M#XRP | 2012 | +0.208 | +1573.35€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 2012 | +0.208 | +1573.35€ | 0 | 0 |
| ✅ GBM_LATE_60M | 5143 | +0.052 | +1384.64€ | 0 | 5 |
| ✅ GBM_LATE_60M#60min | 5143 | +0.052 | +1384.64€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 1781 | +0.058 | +532.65€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 1781 | +0.058 | +532.65€ | 1 | 6 |
| ✅ GBM_LATE_60M#ETH | 1650 | +0.052 | +518.60€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 1650 | +0.052 | +518.60€ | 1 | 5 |
| ✅ GBM_LATE_60M#SOL | 1712 | +0.045 | +333.39€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 1712 | +0.045 | +333.39€ | 0 | 8 |
| 🚫 GBM_LATE_60M_FADE | 716 | -0.251 | -35.90€ | 8 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 716 | -0.251 | -35.90€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 259 | -0.251 | -18.51€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 259 | -0.251 | -18.51€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 261 | -0.245 | -7.56€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 261 | -0.245 | -7.56€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 196 | -0.253 | -9.83€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 196 | -0.253 | -9.83€ | 5 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 2135 | +0.084 | +545.78€ | 0 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 2135 | +0.084 | +545.78€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 832 | +0.072 | +197.77€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 832 | +0.072 | +197.77€ | 0 | 6 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 749 | +0.058 | +145.65€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 749 | +0.058 | +145.65€ | 1 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 554 | +0.137 | +202.36€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 554 | +0.137 | +202.36€ | 2 | 9 |
| ✅ LATE_WINDOW_5MIN | 248 | +0.296 | +281.38€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 248 | +0.296 | +281.38€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 248 | +0.296 | +281.38€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 248 | +0.296 | +281.38€ | 1 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 4411 | +0.098 | +1011.14€ | 0 | 1 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 4411 | +0.098 | +1011.14€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 4411 | +0.098 | +1011.14€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 4411 | +0.098 | +1011.14€ | 0 | 1 |
| ✅ LIQUIDACIONES_15M | 1201 | -0.000 | +26.27€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 1201 | -0.000 | +26.27€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 81 | +0.030 | +1.96€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 81 | +0.030 | +1.96€ | 0 | 1 |
| ✅ LIQUIDACIONES_15M#BTC | 282 | -0.007 | +7.73€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 282 | -0.007 | +7.73€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 59 | -0.041 | -2.28€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 59 | -0.041 | -2.28€ | 1 | 1 |
| ✅ LIQUIDACIONES_15M#ETH | 307 | +0.018 | +18.33€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 307 | +0.018 | +18.33€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 321 | -0.017 | +0.28€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 321 | -0.017 | +0.28€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 151 | +0.010 | +0.25€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 151 | +0.010 | +0.25€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 4209 | +0.017 | +126.25€ | 4 | 1 |
| ✅ LIQUIDACIONES_5M#5min | 4209 | +0.017 | +126.25€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 218 | +0.023 | -1.43€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 218 | +0.023 | -1.43€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 827 | +0.015 | +40.58€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 827 | +0.015 | +40.58€ | 2 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 253 | +0.025 | +25.79€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 253 | +0.025 | +25.79€ | 0 | 6 |
| ✅ LIQUIDACIONES_5M#ETH | 1661 | +0.019 | +28.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1661 | +0.019 | +28.46€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 771 | +0.011 | +2.03€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 771 | +0.011 | +2.03€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 479 | +0.016 | +30.83€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 479 | +0.016 | +30.83€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 2403 | -0.036 | -15.22€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 2403 | -0.036 | -15.22€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 730 | -0.034 | -13.70€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 730 | -0.034 | -13.70€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 853 | -0.013 | +14.56€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 853 | -0.013 | +14.56€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 820 | -0.060 | -16.08€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 820 | -0.060 | -16.08€ | 5 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 15836 | -0.031 | -105.84€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 7624 | -0.033 | -73.72€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 8212 | -0.029 | -32.12€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 548 | -0.056 | -35.06€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 282 | -0.035 | -4.03€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 266 | -0.078 | -31.03€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 4148 | -0.025 | -10.36€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 1973 | -0.023 | +7.02€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 2175 | -0.026 | -17.37€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 1529 | -0.028 | +18.15€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 785 | -0.034 | -2.61€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 744 | -0.021 | +20.76€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 3575 | -0.032 | -49.57€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 1698 | -0.032 | -25.53€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 1877 | -0.032 | -24.04€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 3052 | -0.022 | +51.85€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 1478 | -0.028 | +3.21€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 1574 | -0.015 | +48.64€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 2984 | -0.043 | -80.86€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 1408 | -0.049 | -51.78€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 1576 | -0.037 | -29.08€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 68481 | -0.001 | +3635.78€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 68481 | -0.001 | +3635.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 12416 | +0.027 | +1692.45€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 12416 | +0.027 | +1692.45€ | 2 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 9557 | -0.037 | -134.62€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 9557 | -0.037 | -134.62€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 12554 | +0.025 | +1393.03€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 12554 | +0.025 | +1393.03€ | 1 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 9505 | -0.053 | -251.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 9505 | -0.053 | -251.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 11682 | -0.004 | +321.35€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 11682 | -0.004 | +321.35€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 12767 | +0.018 | +615.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 12767 | +0.018 | +615.34€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 7190 | -0.055 | -118.45€ | 5 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 7190 | -0.055 | -118.45€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1249 | -0.003 | -16.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1249 | -0.003 | -16.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1992 | -0.063 | -24.95€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1992 | -0.063 | -24.95€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 82 | -0.024 | -0.65€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 82 | -0.024 | -0.65€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 809 | -0.120 | -35.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 809 | -0.120 | -35.98€ | 5 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 2195 | -0.068 | -13.13€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 2195 | -0.068 | -13.13€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 863 | -0.018 | -27.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 863 | -0.018 | -27.52€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3380 | +0.003 | -2.51€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3380 | +0.003 | -2.51€ | 0 | 0 |
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
| ✅ MOMENTUM_IBS_5M#XRP | 194 | -0.015 | -3.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 194 | -0.015 | -3.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 167711 | -0.078 | +2120.99€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 167711 | -0.078 | +2120.99€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 29370 | -0.078 | +1748.65€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 29370 | -0.078 | +1748.65€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 25054 | -0.102 | -1266.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 25054 | -0.102 | -1266.22€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 29771 | -0.068 | +1412.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 29771 | -0.068 | +1412.89€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 24603 | -0.099 | -798.96€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 24603 | -0.099 | -798.96€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 29960 | -0.059 | +253.99€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 29960 | -0.059 | +253.99€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 28953 | -0.070 | +770.64€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 28953 | -0.070 | +770.64€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 9073 | -0.035 | -184.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 9073 | -0.035 | -184.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 1008 | -0.017 | -19.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 1008 | -0.017 | -19.32€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 2115 | -0.047 | -29.16€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 2115 | -0.047 | -29.16€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2653 | -0.025 | -38.01€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2653 | -0.025 | -38.01€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1273 | -0.064 | -31.74€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1273 | -0.064 | -31.74€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 1015 | -0.032 | -34.01€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 1015 | -0.032 | -34.01€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 2171 | +0.119 | +859.01€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#5min | 2035 | +0.123 | +846.42€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 482 | +0.134 | +235.53€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 482 | +0.134 | +235.53€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#DOGE | 416 | +0.117 | +144.45€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 416 | +0.117 | +144.45€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#ETH | 383 | +0.123 | +168.44€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 383 | +0.123 | +168.44€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 346 | +0.141 | +177.04€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 346 | +0.141 | +177.04€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#XRP | 408 | +0.100 | +120.96€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 408 | +0.100 | +120.96€ | 0 | 2 |
| ✅ ORDER_FLOW_5M_REACTIVO | 2216 | -0.016 | -15.19€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 2216 | -0.016 | -15.19€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 399 | +0.014 | +25.74€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 399 | +0.014 | +25.74€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 412 | -0.041 | -21.83€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 412 | -0.041 | -21.83€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 555 | -0.039 | -31.26€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 555 | -0.039 | -31.26€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 450 | +0.004 | +8.07€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 450 | +0.004 | +8.07€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 400 | -0.010 | +4.09€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 400 | -0.010 | +4.09€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 1168 | -0.065 | -18.16€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 539 | -0.103 | -68.40€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 418 | -0.114 | -47.85€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 121 | -0.061 | -20.55€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 409 | -0.023 | +34.22€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 294 | -0.007 | +42.23€ | 2 | 2 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 115 | -0.064 | -8.00€ | 1 | 0 |
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
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 431 | -0.221 | -45.83€ | 2 | 1 |
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
| ✅ STREAK_FADE_15M | 955 | +0.041 | +80.94€ | 2 | 2 |
| ✅ STREAK_FADE_15M#15min | 955 | +0.041 | +80.94€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 358 | +0.017 | +2.85€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 358 | +0.017 | +2.85€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 74 | +0.026 | +3.13€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 74 | +0.026 | +3.13€ | 1 | 1 |
| ✅ STREAK_FADE_15M#SOL | 83 | +0.018 | +6.06€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 83 | +0.018 | +6.06€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 440 | +0.068 | +68.91€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 440 | +0.068 | +68.91€ | 1 | 4 |
| ✅ STREAK_FADE_5M | 3578 | -0.024 | -145.04€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3578 | -0.024 | -145.04€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 1127 | -0.023 | -40.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 1127 | -0.023 | -40.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 616 | -0.031 | -28.72€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 616 | -0.031 | -28.72€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 171 | -0.043 | -14.80€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 171 | -0.043 | -14.80€ | 4 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1664 | -0.020 | -61.31€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1664 | -0.020 | -61.31€ | 2 | 0 |
| ✅ STREAK_FADE_60M | 118 | -0.050 | -12.20€ | 5 | 0 |
| ✅ STREAK_FADE_60M#60min | 118 | -0.050 | -12.20€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 44 | -0.087 | -4.62€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 44 | -0.087 | -4.62€ | 4 | 0 |
| ✅ STREAK_FADE_60M#SOL | 74 | -0.026 | -7.58€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 74 | -0.026 | -7.58€ | 0 | 1 |
| ✅ STREAK_MOM_5M | 11527 | +0.014 | +70.95€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 11527 | +0.014 | +70.95€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2995 | +0.018 | +24.38€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2995 | +0.018 | +24.38€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 3022 | +0.015 | +31.45€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 3022 | +0.015 | +31.45€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2929 | +0.008 | -3.11€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2929 | +0.008 | -3.11€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2581 | +0.014 | +18.23€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2581 | +0.014 | +18.23€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 12164 | +0.018 | +0.88€ | 4 | 0 |
| ✅ STRUCT_NO_15M#15min | 12164 | +0.018 | +0.88€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 5041 | +0.021 | +6.67€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 5041 | +0.021 | +6.67€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 4202 | +0.018 | -3.78€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 4202 | +0.018 | -3.78€ | 4 | 0 |
| ✅ STRUCT_NO_15M#SOL | 2921 | +0.015 | -2.01€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 2921 | +0.015 | -2.01€ | 1 | 0 |
| ✅ UPDOWN_GBM | 108635 | +0.060 | +10308.16€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 26455 | +0.078 | +5293.05€ | 0 | 9 |
| ✅ UPDOWN_GBM#240min | 3192 | -0.000 | +33.91€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 72178 | +0.062 | +4875.08€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 6441 | -0.002 | +112.68€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 9053 | +0.105 | +1667.35€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1781 | +0.164 | +820.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 90 | -0.011 | -2.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 7182 | +0.092 | +849.15€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 24776 | +0.057 | +2186.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 3541 | +0.078 | +784.12€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 913 | -0.001 | +16.94€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 17313 | +0.067 | +1307.78€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 2875 | -0.004 | +73.81€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 134 | -0.066 | +3.73€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 11815 | +0.077 | +1331.28€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1761 | +0.154 | +738.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 86 | +0.023 | -0.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 9968 | +0.064 | +593.71€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 25788 | +0.050 | +1822.30€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 6243 | +0.072 | +958.20€ | 0 | 9 |
| ✅ UPDOWN_GBM#ETH#240min | 883 | +0.005 | +16.54€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 16173 | +0.052 | +809.21€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 2366 | +0.000 | +37.64€ | 1 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 123 | -0.108 | +0.71€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 23027 | +0.039 | +1281.08€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 7122 | +0.031 | +422.57€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#240min | 823 | -0.010 | +4.91€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 13772 | +0.051 | +861.54€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 1200 | -0.002 | +1.23€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#daily | 110 | -0.143 | -9.17€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 14174 | +0.073 | +2021.60€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 6007 | +0.094 | +1569.52€ | 0 | 11 |
| ✅ UPDOWN_GBM#XRP#240min | 397 | +0.006 | -1.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 7770 | +0.060 | +453.69€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 367 | -0.104 | -4.72€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 1007 | +0.364 | +372.64€ | 0 | 10 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 1007 | +0.364 | +372.64€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 491 | +0.362 | +172.01€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 491 | +0.362 | +172.01€ | 0 | 9 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 516 | +0.365 | +200.63€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 516 | +0.365 | +200.63€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO | 25781 | -0.021 | +6374.58€ | 3 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 25781 | -0.021 | +6374.58€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1981 | -0.051 | +561.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1981 | -0.051 | +561.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 4808 | -0.115 | +253.03€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 4808 | -0.115 | +253.03€ | 3 | 11 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 1071 | +0.222 | +899.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 1071 | +0.222 | +899.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 3414 | +0.219 | +2171.67€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 3414 | +0.219 | +2171.67€ | 1 | 20 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 7317 | -0.060 | +1070.35€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 7317 | -0.060 | +1070.35€ | 5 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 7190 | -0.059 | +1418.49€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 7190 | -0.059 | +1418.49€ | 3 | 5 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 316 | +0.060 | +27.30€ | 0 | 9 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 316 | +0.060 | +27.30€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 316 | +0.060 | +27.30€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 316 | +0.060 | +27.30€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1821 | +0.282 | +1523.90€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1821 | +0.282 | +1523.90€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 960 | +0.274 | +749.17€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 960 | +0.274 | +749.17€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 861 | +0.289 | +774.73€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 861 | +0.289 | +774.73€ | 0 | 9 |
| ✅ UPDOWN_OU_5M | 871 | -0.113 | -86.21€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 871 | -0.113 | -86.21€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 277 | -0.081 | -20.93€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 277 | -0.081 | -20.93€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 97 | -0.177 | -11.96€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 97 | -0.177 | -11.96€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 114 | -0.172 | -3.97€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 114 | -0.172 | -3.97€ | 4 | 0 |
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
  - _Estado_: 818 celda(s) pasan gate riguroso completo de 2912 evaluadas (n>=40) y 4031 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.031 < 0.08 — monitorear
  - _Datos_: n=7117 IC=+0.031 PNL=+420.59€

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
  - _Estado_: alineada_con_outcome_prev IC=+0.141 n=1073/60 | contraria IC=+0.185 n=1124 | gap=-0.044 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=596, boost estimado=+0.011. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 0/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=2365/40 IC=+0.001 PNL=+38.15€ | BTC#60min: n=2873/40 IC=-0.004 PNL=+73.69€ | SOL#60min: n=1199/40 IC=-0.001 PNL=+1.79€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.045 n=739586 | tras_1loss IC=+0.100 n=560879 | tras_2loss IC=+0.071 n=224117/40 | gap=-0.026 (umbral 0.05)

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.161 > 0.08 con n=1086 PNL=+656.94€
  - _Datos_: n=1086 IC=+0.161 PNL=+656.94€

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
  - _Estado_: n=4290 IC=+0.000 PNL=-22.76€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=4290 IC=+0.000 PNL=-22.76€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=2147 IC=-0.006 PNL=+136.38€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=2147 IC=-0.006 PNL=+136.38€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.139 > 0.1 con n=7277 PNL=+3603.50€
  - _Datos_: n=7277 IC=+0.139 PNL=+3603.50€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=3540 IC=+0.078 PNL=+783.62€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=3540 IC=+0.078 PNL=+783.62€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.296 n=248) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=248 IC=+0.296 PNL=+281.38€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.117 > 0.02 con n=1273 PNL=+506.06€
  - _Datos_: n=1273 IC=+0.117 PNL=+506.06€

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
  - _Estado_: n=44676 IC=+0.073 PNL=+6126.33€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=44676 IC=+0.073 PNL=+6126.33€

**⏳ H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: 120
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: 0/120 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.139 < -0.1 con n=762 PNL=+100.06€
  - _Datos_: n=762 IC=-0.139 PNL=+100.06€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=4182 IC=+0.068 PNL=+534.94€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=4182 IC=+0.068 PNL=+534.94€

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
  - _Estado_: n=1128 IC=+0.097 PNL=+277.43€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=1128 IC=+0.097 PNL=+277.43€

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
  - _Estado_: n=43859 IC=-0.137 PNL=+2681.55€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=43859 IC=-0.137 PNL=+2681.55€

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
  - _Estado_: n=4575 IC=+0.131 PNL=+3029.69€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=4575 IC=+0.131 PNL=+3029.69€

**⏳ H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: 40
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=11326 IC=+0.058 PNL=+982.76€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=11326 IC=+0.058 PNL=+982.76€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.103 > 0.08 con n=4739 PNL=+2685.28€
  - _Datos_: n=4739 IC=+0.103 PNL=+2685.28€

**⏳ H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: 80
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: 0/80 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.220 < -0.1 con n=4801 PNL=-397.81€
  - _Datos_: n=4801 IC=-0.220 PNL=-397.81€

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
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.097 n=2240) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=2240 IC=+0.097 PNL=+455.27€

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
  - _Estado_: n=18804 IC=+0.178 PNL=-2155.49€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=18804 IC=+0.178 PNL=-2155.49€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.229 > 0.1 con n=300 PNL=+206.54€
  - _Datos_: n=300 IC=+0.229 PNL=+206.54€
