# Hipótesis automáticas — 2026-11-11 12:54 UTC
_Generado por shadow_postmortem.py sobre 1288531 resoluciones (PNL=+176639.35€)_

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
- **FILTRO** `restante_s_al_confirmar` < `132.5` → IC=-0.219 (n=11827)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 132.5
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=35492)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `125.22` → IC=-0.258 (n=1201)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 125.22
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=3605)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `116.46` → IC=-0.287 (n=1219)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 116.46
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=3658)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `restante_s_al_confirmar` < `117.28` → IC=-0.162 (n=3239)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 117.28
  - _Potencial_: sin este filtro IC_bueno=-0.000 (n=9720)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `151.9` → IC=-0.242 (n=3224)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 151.9
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=9672)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `128.77` → IC=-0.263 (n=2211)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 128.77
  - _Potencial_: sin este filtro IC_bueno=-0.084 (n=6636)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.210 (n=27728)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.104)

- **PATRÓN** `libro_liquidez` > `8304.4408` → IC=+0.159 (n=2326)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 8304.4408 (IC base=+0.104)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.128 (n=23782)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 17.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.130 (n=29019)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.124)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.224 (n=21820)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.140 (n=8295)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `6529.2886` → IC=+0.144 (n=3205)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 6529.2886 (IC base=+0.124)

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

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.185 (n=1908)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 7.0 (IC base=+0.178)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.181 (n=2136)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 17.0 (IC base=+0.178)

- **PATRÓN** `py_entrada` < `0.295` → IC=+0.312 (n=981)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.295 (IC base=+0.178)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.181 (n=2735)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.01 (IC base=+0.178)

- **PATRÓN** `libro_liquidez` > `16075.8828` → IC=+0.184 (n=706)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 16075.8828 (IC base=+0.178)

### FAVORITO_CONFIRMADO#BTC#60min
- **FILTRO** `py_entrada` < `0.55` → IC=-0.335 (n=95)

  - _Acción_: SKIP cuando `py_entrada` < 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.095 (n=2202)

- **PATRÓN** `py_entrada` > `0.61` → IC=+0.167 (n=607)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` > 0.61 (IC base=+0.077)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.144 (n=1416)

  - _Acción_: Kelly boost +0.72€ cuando `py_entrada` < 0.44 (IC base=+0.082)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.170 (n=5292)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 5.0 (IC base=+0.166)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.170 (n=4470)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 15.0 (IC base=+0.166)

- **PATRÓN** `py_entrada` > `0.77` → IC=+0.375 (n=1737)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.77 (IC base=+0.166)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.210 (n=2389)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.202)

- **PATRÓN** `py_entrada` < `0.275` → IC=+0.331 (n=949)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.275 (IC base=+0.202)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.205 (n=2786)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.202)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.142 (n=1357)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 5.0 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.146 (n=1156)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 15.0 (IC base=+0.141)

- **PATRÓN** `py_entrada` > `0.675` → IC=+0.253 (n=439)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.675 (IC base=+0.141)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.144 (n=1099)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.156 (n=155)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.073)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.252 (n=944)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.227)

- **PATRÓN** `py_entrada` > `0.83` → IC=+0.420 (n=1316)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.83 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.146 (n=1418)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 7.0 (IC base=+0.145)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.154 (n=729)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 7.0 (IC base=+0.145)

- **PATRÓN** `py_entrada` < `0.345` → IC=+0.278 (n=717)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.345 (IC base=+0.145)

### FAVORITO_CONFIRMADO#SOL#60min
- **FILTRO** `libro_liquidez` < `952.1685` → IC=-0.125 (n=158)

  - _Acción_: SKIP cuando `libro_liquidez` < 952.1685
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=322)

- **PATRÓN** `py_entrada` > `0.55` → IC=+0.163 (n=461)

  - _Acción_: Kelly boost +0.82€ cuando `py_entrada` > 0.55 (IC base=+0.045)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.144 (n=473)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 17.0 (IC base=+0.120)

- **PATRÓN** `py_entrada` < `0.33` → IC=+0.236 (n=457)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.33 (IC base=+0.120)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `10.0` → IC=-0.297 (n=72)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.232 (n=151)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.201 (n=23895)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.198 (n=20214)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 15.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.225 (n=10004)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.196)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.338 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.196)

- **PATRÓN** `libro_liquidez` > `4915.142` → IC=+0.338 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4915.142 (IC base=+0.196)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.174 (n=5451)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 5.0 (IC base=+0.170)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.181 (n=5444)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` < 0.74 (IC base=+0.170)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.380 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.247 (n=89)

- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=90)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.213 (n=3228)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.210)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.213 (n=2863)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.210)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.251 (n=1606)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.210)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.184 (n=5330)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.179 (n=4526)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 15.0 (IC base=+0.177)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.178 (n=5488)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` < 0.73 (IC base=+0.177)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.185 (n=4173)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` > 0.71 (IC base=+0.177)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.257 (n=4489)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.251)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.251 (n=3804)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.251)

- **PATRÓN** `py_entrada` > `0.8` → IC=+0.365 (n=1441)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.190 (n=5230)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.186)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.190 (n=4436)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 15.0 (IC base=+0.186)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.197 (n=1754)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` > 0.73 (IC base=+0.186)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.429 (n=963)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.426)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.427 (n=958)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.426)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.439 (n=974)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.426)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.432 (n=1025)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.426)

- **PATRÓN** `libro_liquidez` > `4616.579` → IC=+0.444 (n=620)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4616.579 (IC base=+0.426)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.439 (n=390)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.440)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.448 (n=267)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.440)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.449 (n=430)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.440)

- **PATRÓN** `libro_liquidez` > `12447.5813` → IC=+0.445 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12447.5813 (IC base=+0.440)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.432 (n=380)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.424)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.426 (n=378)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.424)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.435 (n=384)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.424)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.430 (n=427)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.424)

- **PATRÓN** `libro_liquidez` > `4792.7768` → IC=+0.429 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4792.7768 (IC base=+0.424)

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

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.206 (n=31259)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.240 (n=31599)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.200)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.188 (n=4668)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 18.0 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.180 (n=10038)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 12.0 (IC base=+0.179)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.189 (n=14368)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.71 (IC base=+0.179)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.229 (n=6481)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.224)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.286 (n=4433)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.224)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.183 (n=13127)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 7.0 (IC base=+0.179)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.197 (n=11112)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` > 0.72 (IC base=+0.179)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.835` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.835
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.228 (n=4378)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.221 (n=5029)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.218)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.254 (n=7277)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.218)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **FILTRO** `hora_utc` > `3.0` → IC=-0.278 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.206 (n=11924)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.204)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.256 (n=4569)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.204)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.203 (n=5196)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.199 (n=5195)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 6.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.245 (n=5421)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.196)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.193 (n=11278)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.140 (n=11822)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `3.44` → IC=+0.139 (n=13713)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 3.44 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.194 (n=5496)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.145 (n=5328)

  - _Acción_: Kelly boost +0.72€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.126 (n=6898)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 7.0 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `2.59` → IC=+0.144 (n=5183)

  - _Acción_: Kelly boost +0.72€ cuando `lag_apertura_s` < 2.59 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.192 (n=5782)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.137 (n=7217)

  - _Acción_: Kelly boost +0.69€ cuando `restante_min` > 4.95 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `3.13` → IC=+0.137 (n=6896)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 3.13 (IC base=+0.116)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.307 (n=1384)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.294)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.388 (n=714)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.294)

- **PATRÓN** `libro_liquidez` > `3968.2863` → IC=+0.294 (n=878)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3968.2863 (IC base=+0.294)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.287 (n=931)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.282)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.365 (n=309)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.282)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.319 (n=671)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.298)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.301 (n=985)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.298)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.397 (n=338)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.298)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.443 (n=944)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.439)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.444 (n=912)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.439)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.437 (n=443)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.432)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.435 (n=308)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.432)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.437 (n=457)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.432)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.460 (n=149)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.446)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.446 (n=383)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.446)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.448 (n=419)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.446)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.445 (n=360)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4785` → IC=+0.139 (n=17709)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.4785 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.127 (n=17899)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 6.0 (IC base=+0.123)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.126 (n=12365)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 12.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` > `0.9771` → IC=+0.246 (n=5906)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9771 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` > `0.7974` → IC=+0.284 (n=971)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7974 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.485` → IC=+0.186 (n=8862)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 3.485 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` > `0.6246` → IC=+0.265 (n=5305)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6246 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` > `0.3044` → IC=+0.250 (n=1830)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3044 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` > `2.7512` → IC=+0.235 (n=4246)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7512 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.135 (n=8784)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.123)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.122 (n=11083)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0062 (IC base=+0.083)

- **PATRÓN** `ibs_20min` < `0.5652` → IC=+0.144 (n=22127)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.5652 (IC base=+0.083)

- **PATRÓN** `dist_vwap_pct` > `0.6152` → IC=+0.192 (n=1450)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.6152 (IC base=+0.083)

- **PATRÓN** `volumen_regimen` < `0.6967` → IC=+0.199 (n=3981)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_regimen` < 0.6967 (IC base=+0.083)

- **PATRÓN** `volumen_pendiente_norm` > `0.2966` → IC=+0.234 (n=2224)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2966 (IC base=+0.083)

- **PATRÓN** `volumen_spike_ratio` > `1.4564` → IC=+0.208 (n=15347)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4564 (IC base=+0.083)

- **PATRÓN** `ballena_activa_n` < `99.0` → IC=+0.230 (n=15249)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 99.0 (IC base=+0.083)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `drift_60min` |x|≤ `0.3657` → IC=+0.213 (n=3775)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3657 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.226 (n=1832)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.212)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.212 (n=2537)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` > `0.9862` → IC=+0.278 (n=1711)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9862 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.45` → IC=+0.278 (n=1681)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.45 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` > `0.2333` → IC=+0.259 (n=673)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2333 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `1.4361` → IC=+0.213 (n=3618)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4361 (IC base=+0.212)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.224 (n=4164)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `2038.9448` → IC=+0.212 (n=1258)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2038.9448 (IC base=+0.212)

- **PATRÓN** `ballena_activa_n` < `26.0` → IC=+0.224 (n=3427)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 26.0 (IC base=+0.212)

- **PATRÓN** `sigma_h` > `0.0093` → IC=+0.246 (n=1507)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0093 (IC base=+0.244)

- **PATRÓN** `drift_60min` |x|≤ `0.0893` → IC=+0.283 (n=1107)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0893 (IC base=+0.244)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.251 (n=1236)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.244)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.249 (n=1531)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.244)

- **PATRÓN** `ibs_20min` < `0.5654` → IC=+0.261 (n=3318)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5654 (IC base=+0.244)

- **PATRÓN** `volumen_pendiente_norm` < `0.0952` → IC=+0.247 (n=3007)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0952 (IC base=+0.244)

- **PATRÓN** `volumen_pendiente_norm` > `0.2902` → IC=+0.254 (n=445)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2902 (IC base=+0.244)

- **PATRÓN** `volumen_spike_ratio` < `1.4472` → IC=+0.247 (n=1056)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4472 (IC base=+0.244)

- **PATRÓN** `volumen_spike_ratio` > `1.8601` → IC=+0.248 (n=2111)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8601 (IC base=+0.244)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.246 (n=3819)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.244)

- **PATRÓN** `libro_liquidez` > `1776.2196` → IC=+0.250 (n=2212)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1776.2196 (IC base=+0.244)

- **PATRÓN** `ballena_activa_n` < `6.0` → IC=+0.247 (n=1124)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 6.0 (IC base=+0.244)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.235 (n=1061)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.224)

- **PATRÓN** `drift_60min` |x|≤ `0.1096` → IC=+0.254 (n=1397)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1096 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.235 (n=3322)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.227 (n=2259)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` > `0.9034` → IC=+0.257 (n=1058)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9034 (IC base=+0.224)

- **PATRÓN** `dist_vwap_pct` > `0.1847` → IC=+0.234 (n=1435)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1847 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.797` → IC=+0.263 (n=466)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.797 (IC base=+0.224)

- **PATRÓN** `volumen_regimen` > `0.6994` → IC=+0.232 (n=2834)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6994 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` > `0.2786` → IC=+0.266 (n=442)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2786 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` > `2.4465` → IC=+0.249 (n=1044)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4465 (IC base=+0.224)

- **PATRÓN** `libro_liquidez` > `16033.3314` → IC=+0.225 (n=1058)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16033.3314 (IC base=+0.224)

- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.153 (n=3394)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0064 (IC base=+0.130)

- **PATRÓN** `drift_60min` |x|≤ `0.0775` → IC=+0.153 (n=1132)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.0775 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.152 (n=1263)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 17.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` < `0.3534` → IC=+0.202 (n=2261)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3534 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.618` → IC=+0.130 (n=550)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` > 10.618 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.972` → IC=+0.138 (n=3096)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 3.972 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` < `0.6343` → IC=+0.153 (n=1132)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.6343 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` > `0.0717` → IC=+0.158 (n=1388)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` > 0.0717 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` < `2.442` → IC=+0.141 (n=3264)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 2.442 (IC base=+0.130)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.130 (n=4403)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.01 (IC base=+0.130)

- **PATRÓN** `ballena_activa_n` < `176.0` → IC=+0.183 (n=1076)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 176.0 (IC base=+0.130)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0114` → IC=+0.215 (n=1813)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0114 (IC base=+0.196)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.204 (n=4193)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.196)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.262 (n=1554)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.196)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.988` → IC=+0.280 (n=876)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.988 (IC base=+0.196)

- **PATRÓN** `volumen_pendiente_norm` < `0.0974` → IC=+0.199 (n=3578)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` < 0.0974 (IC base=+0.196)

- **PATRÓN** `volumen_pendiente_norm` > `0.3522` → IC=+0.228 (n=516)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3522 (IC base=+0.196)

- **PATRÓN** `volumen_spike_ratio` > `2.7296` → IC=+0.214 (n=1769)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7296 (IC base=+0.196)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.201 (n=4827)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.196)

- **PATRÓN** `libro_liquidez` > `1911.1684` → IC=+0.202 (n=1811)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1911.1684 (IC base=+0.196)

- **PATRÓN** `sigma_h` < `0.0111` → IC=+0.225 (n=3244)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0111 (IC base=+0.221)

- **PATRÓN** `drift_60min` |x|≤ `0.2922` → IC=+0.234 (n=2459)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2922 (IC base=+0.221)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.242 (n=1397)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.221)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.226 (n=1676)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.221)

- **PATRÓN** `ibs_20min` < `0.0465` → IC=+0.268 (n=1230)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0465 (IC base=+0.221)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.793` → IC=+0.264 (n=400)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.793 (IC base=+0.221)

- **PATRÓN** `volumen_pendiente_norm` > `0.3488` → IC=+0.258 (n=535)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3488 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` < `1.7683` → IC=+0.219 (n=1561)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7683 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` > `2.1602` → IC=+0.230 (n=2365)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1602 (IC base=+0.221)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.223 (n=1878)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.221)

- **PATRÓN** `libro_liquidez` > `1893.3248` → IC=+0.225 (n=1672)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1893.3248 (IC base=+0.221)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.226 (n=3494)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 24.0 (IC base=+0.221)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.174 (n=210)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.063 (n=4800)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.150 (n=666)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0039 (IC base=+0.059)

- **PATRÓN** `ibs_20min` > `0.9422` → IC=+0.232 (n=661)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9422 (IC base=+0.059)

- **PATRÓN** `dist_vwap_pct` > `0.14` → IC=+0.340 (n=459)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.14 (IC base=+0.059)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.086` → IC=+0.202 (n=1451)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.086 (IC base=+0.059)

- **PATRÓN** `volumen_regimen` > `1.0989` → IC=+0.347 (n=358)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0989 (IC base=+0.059)

- **PATRÓN** `volumen_pendiente_norm` < `0.1678` → IC=+0.336 (n=639)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1678 (IC base=+0.059)

- **PATRÓN** `volumen_pendiente_norm` > `0.3061` → IC=+0.335 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3061 (IC base=+0.059)

- **PATRÓN** `volumen_spike_ratio` < `1.5415` → IC=+0.347 (n=339)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5415 (IC base=+0.059)

- **PATRÓN** `volumen_spike_ratio` > `2.2842` → IC=+0.338 (n=349)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2842 (IC base=+0.059)

- **PATRÓN** `ballena_activa_n` < `142.0` → IC=+0.338 (n=781)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 142.0 (IC base=+0.059)

- **PATRÓN** `ibs_20min` < `0.087` → IC=+0.188 (n=1253)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.087 (IC base=+0.053)

- **PATRÓN** `dist_vwap_pct` > `0.3354` → IC=+0.164 (n=602)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.3354 (IC base=+0.053)

- **PATRÓN** `volumen_regimen` < `1.0035` → IC=+0.160 (n=2109)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.0035 (IC base=+0.053)

- **PATRÓN** `volumen_pendiente_norm` > `0.2807` → IC=+0.210 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2807 (IC base=+0.053)

- **PATRÓN** `volumen_spike_ratio` < `1.7674` → IC=+0.157 (n=1538)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.7674 (IC base=+0.053)

- **PATRÓN** `volumen_spike_ratio` > `1.5104` → IC=+0.160 (n=2061)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.5104 (IC base=+0.053)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.183 (n=143)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=763)

- **FILTRO** `ibs_20min` < `0.2609` → IC=-0.175 (n=226)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2609
  - _Potencial_: sin este filtro IC_bueno=+0.079 (n=680)

- **FILTRO** `ibs_20min` > `0.2` → IC=-0.132 (n=4722)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2
  - _Potencial_: sin este filtro IC_bueno=+0.154 (n=2341)

- **FILTRO** `sigma_ewma_delta_pct` > `8.28` → IC=-0.226 (n=760)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.28
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=6303)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.176 (n=310)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` > 0.75 (IC base=+0.015)

- **PATRÓN** `dist_vwap_pct` > `0.9754` → IC=+0.275 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9754 (IC base=+0.015)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.917` → IC=+0.159 (n=212)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 4.917 (IC base=+0.015)

- **PATRÓN** `volumen_regimen` > `0.624` → IC=+0.284 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.624 (IC base=+0.015)

- **PATRÓN** `volumen_pendiente_norm` < `0.0791` → IC=+0.279 (n=269)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0791 (IC base=+0.015)

- **PATRÓN** `volumen_spike_ratio` < `2.1931` → IC=+0.285 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1931 (IC base=+0.015)

- **PATRÓN** `volumen_spike_ratio` > `1.449` → IC=+0.264 (n=273)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.449 (IC base=+0.015)

- **PATRÓN** `ballena_activa_n` < `41.0` → IC=+0.268 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 41.0 (IC base=+0.015)

- **PATRÓN** `ibs_20min` < `0.2` → IC=+0.154 (n=2341)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.2 (IC base=-0.037)

- **PATRÓN** `dist_vwap_pct` > `0.2229` → IC=+0.288 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2229 (IC base=-0.037)

- **PATRÓN** `volumen_regimen` < `0.7051` → IC=+0.302 (n=458)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7051 (IC base=-0.037)

- **PATRÓN** `volumen_regimen` > `1.0599` → IC=+0.282 (n=471)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0599 (IC base=-0.037)

- **PATRÓN** `volumen_pendiente_norm` > `0.08` → IC=+0.306 (n=467)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.08 (IC base=-0.037)

- **PATRÓN** `volumen_spike_ratio` < `2.4729` → IC=+0.300 (n=970)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4729 (IC base=-0.037)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `ibs_20min` < `0.7861` → IC=-0.156 (n=3613)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7861
  - _Potencial_: sin este filtro IC_bueno=+0.130 (n=1862)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.172 (n=1176)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=4299)

- **FILTRO** `ibs_20min` > `0.7391` → IC=-0.192 (n=1891)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7391
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=5681)

- **PATRÓN** `ibs_20min` > `0.7861` → IC=+0.130 (n=1862)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` > 0.7861 (IC base=-0.059)

- **PATRÓN** `dist_vwap_pct` > `1.0308` → IC=+0.359 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0308 (IC base=-0.059)

- **PATRÓN** `volumen_regimen` > `0.704` → IC=+0.318 (n=953)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.704 (IC base=-0.059)

- **PATRÓN** `volumen_pendiente_norm` > `0.1715` → IC=+0.303 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1715 (IC base=-0.059)

- **PATRÓN** `volumen_spike_ratio` < `1.5853` → IC=+0.305 (n=460)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5853 (IC base=-0.059)

- **PATRÓN** `volumen_spike_ratio` > `2.5248` → IC=+0.320 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5248 (IC base=-0.059)

- **PATRÓN** `dist_vwap_pct` > `0.8119` → IC=+0.278 (n=362)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8119 (IC base=+0.004)

- **PATRÓN** `volumen_regimen` < `0.6417` → IC=+0.274 (n=740)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6417 (IC base=+0.004)

- **PATRÓN** `volumen_regimen` > `1.066` → IC=+0.285 (n=1007)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.066 (IC base=+0.004)

- **PATRÓN** `volumen_pendiente_norm` > `0.2333` → IC=+0.287 (n=402)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2333 (IC base=+0.004)

- **PATRÓN** `volumen_spike_ratio` < `2.1758` → IC=+0.266 (n=1843)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1758 (IC base=+0.004)

- **PATRÓN** `volumen_spike_ratio` > `1.4374` → IC=+0.270 (n=2094)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4374 (IC base=+0.004)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.196 (n=7680)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` > 0.0107 (IC base=+0.087)

- **PATRÓN** `ibs_20min` > `0.9697` → IC=+0.312 (n=7665)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9697 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` > `0.9331` → IC=+0.302 (n=1603)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9331 (IC base=+0.087)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.475` → IC=+0.169 (n=10306)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 3.475 (IC base=+0.087)

- **PATRÓN** `volumen_regimen` > `0.6928` → IC=+0.278 (n=7567)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6928 (IC base=+0.087)

- **PATRÓN** `volumen_pendiente_norm` > `0.294` → IC=+0.295 (n=1916)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.294 (IC base=+0.087)

- **PATRÓN** `volumen_spike_ratio` > `2.6532` → IC=+0.287 (n=4451)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6532 (IC base=+0.087)

- **PATRÓN** `ballena_activa_n` < `90.0` → IC=+0.309 (n=12992)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 90.0 (IC base=+0.087)

- **PATRÓN** `sigma_h` > `0.0102` → IC=+0.157 (n=7394)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0102 (IC base=+0.082)

- **PATRÓN** `ibs_20min` < `0.5204` → IC=+0.172 (n=19516)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.5204 (IC base=+0.082)

- **PATRÓN** `volumen_regimen` < `0.6989` → IC=+0.282 (n=3235)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6989 (IC base=+0.082)

- **PATRÓN** `volumen_regimen` > `1.1866` → IC=+0.281 (n=2451)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1866 (IC base=+0.082)

- **PATRÓN** `volumen_pendiente_norm` > `0.2943` → IC=+0.329 (n=1638)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2943 (IC base=+0.082)

- **PATRÓN** `volumen_spike_ratio` < `1.5755` → IC=+0.304 (n=4773)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5755 (IC base=+0.082)

- **PATRÓN** `volumen_spike_ratio` > `2.2796` → IC=+0.302 (n=4915)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2796 (IC base=+0.082)

- **PATRÓN** `ballena_activa_n` < `72.0` → IC=+0.312 (n=10813)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 72.0 (IC base=+0.082)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.8028` → IC=-0.132 (n=4084)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8028
  - _Potencial_: sin este filtro IC_bueno=+0.302 (n=2105)

- **FILTRO** `ibs_20min` > `0.7155` → IC=-0.235 (n=1363)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7155
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=4090)

- **FILTRO** `sigma_ewma_delta_pct` > `4.095` → IC=-0.234 (n=1179)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.095
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=4274)

- **PATRÓN** `ibs_20min` > `0.8028` → IC=+0.302 (n=2105)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8028 (IC base=+0.015)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.966` → IC=+0.191 (n=2069)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 2.966 (IC base=+0.015)

- **PATRÓN** `volumen_pendiente_norm` > `0.2294` → IC=+0.330 (n=399)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2294 (IC base=+0.015)

- **PATRÓN** `volumen_spike_ratio` < `1.4503` → IC=+0.281 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4503 (IC base=+0.015)

- **PATRÓN** `volumen_spike_ratio` > `2.2496` → IC=+0.304 (n=895)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2496 (IC base=+0.015)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.304 (n=1975)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 27.0 (IC base=+0.015)

- **PATRÓN** `ibs_20min` < `0.1746` → IC=+0.168 (n=1364)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` < 0.1746 (IC base=-0.022)

- **PATRÓN** `volumen_pendiente_norm` < `0.1519` → IC=+0.406 (n=1056)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1519 (IC base=-0.022)

- **PATRÓN** `volumen_spike_ratio` < `1.4209` → IC=+0.427 (n=341)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4209 (IC base=-0.022)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.403 (n=1063)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 23.0 (IC base=-0.022)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.1693` → IC=+0.225 (n=988)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1693 (IC base=+0.012)

- **PATRÓN** `volumen_regimen` < `1.195` → IC=+0.211 (n=2255)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.195 (IC base=+0.012)

- **PATRÓN** `volumen_regimen` > `0.6953` → IC=+0.218 (n=2015)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6953 (IC base=+0.012)

- **PATRÓN** `volumen_pendiente_norm` > `0.277` → IC=+0.246 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.277 (IC base=+0.012)

- **PATRÓN** `volumen_spike_ratio` < `1.4174` → IC=+0.229 (n=743)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4174 (IC base=+0.012)

- **PATRÓN** `ballena_activa_n` < `260.0` → IC=+0.246 (n=1485)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 260.0 (IC base=+0.012)

- **PATRÓN** `volumen_regimen` > `0.6187` → IC=+0.254 (n=1577)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6187 (IC base=-0.003)

- **PATRÓN** `volumen_pendiente_norm` > `0.2697` → IC=+0.313 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2697 (IC base=-0.003)

- **PATRÓN** `volumen_spike_ratio` < `1.5256` → IC=+0.258 (n=671)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5256 (IC base=-0.003)

- **PATRÓN** `volumen_spike_ratio` > `2.148` → IC=+0.262 (n=691)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.148 (IC base=-0.003)

- **PATRÓN** `ballena_activa_n` < `186.0` → IC=+0.274 (n=512)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 186.0 (IC base=-0.003)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.323 (n=2147)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0094 (IC base=+0.284)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.294 (n=3386)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.284)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.325 (n=1754)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.284)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.582` → IC=+0.305 (n=2164)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.582 (IC base=+0.284)

- **PATRÓN** `volumen_pendiente_norm` < `0.0979` → IC=+0.297 (n=2830)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0979 (IC base=+0.284)

- **PATRÓN** `volumen_spike_ratio` > `1.6102` → IC=+0.290 (n=3130)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6102 (IC base=+0.284)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.293 (n=3863)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.284)

- **PATRÓN** `libro_liquidez` > `2017.8084` → IC=+0.293 (n=1074)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2017.8084 (IC base=+0.284)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.309 (n=2008)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.284)

- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.332 (n=1954)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0089 (IC base=+0.307)

- **PATRÓN** `drift_60min` |x|≤ `0.1771` → IC=+0.327 (n=1291)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1771 (IC base=+0.307)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.327 (n=1121)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.307)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.311 (n=1324)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.307)

- **PATRÓN** `ibs_20min` > `0.1463` → IC=+0.319 (n=1951)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1463 (IC base=+0.307)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.13` → IC=+0.310 (n=351)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.13 (IC base=+0.307)

- **PATRÓN** `volumen_pendiente_norm` < `0.1999` → IC=+0.308 (n=2874)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1999 (IC base=+0.307)

- **PATRÓN** `volumen_pendiente_norm` > `0.3455` → IC=+0.315 (n=474)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3455 (IC base=+0.307)

- **PATRÓN** `volumen_spike_ratio` < `1.5954` → IC=+0.306 (n=941)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5954 (IC base=+0.307)

- **PATRÓN** `volumen_spike_ratio` > `2.7408` → IC=+0.324 (n=1279)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7408 (IC base=+0.307)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.308 (n=1495)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.307)

- **PATRÓN** `libro_liquidez` > `1898.5935` → IC=+0.312 (n=1325)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1898.5935 (IC base=+0.307)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.314 (n=2486)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 23.0 (IC base=+0.307)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7233` → IC=-0.181 (n=1449)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7233
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=4348)

- **PATRÓN** `dist_vwap_pct` > `0.1437` → IC=+0.237 (n=1049)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1437 (IC base=+0.020)

- **PATRÓN** `volumen_regimen` < `1.1603` → IC=+0.236 (n=2059)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1603 (IC base=+0.020)

- **PATRÓN** `volumen_pendiente_norm` < `0.163` → IC=+0.236 (n=2160)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.163 (IC base=+0.020)

- **PATRÓN** `volumen_pendiente_norm` > `0.1031` → IC=+0.242 (n=673)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1031 (IC base=+0.020)

- **PATRÓN** `volumen_spike_ratio` < `2.4363` → IC=+0.240 (n=1998)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4363 (IC base=+0.020)

- **PATRÓN** `ballena_activa_n` < `114.0` → IC=+0.255 (n=2040)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 114.0 (IC base=+0.020)

- **PATRÓN** `ibs_20min` < `0.0918` → IC=+0.157 (n=1451)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.0918 (IC base=+0.006)

- **PATRÓN** `dist_vwap_pct` > `0.7333` → IC=+0.255 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7333 (IC base=+0.006)

- **PATRÓN** `volumen_regimen` < `1.1824` → IC=+0.262 (n=1487)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1824 (IC base=+0.006)

- **PATRÓN** `volumen_pendiente_norm` > `0.2808` → IC=+0.318 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2808 (IC base=+0.006)

- **PATRÓN** `volumen_spike_ratio` < `1.7842` → IC=+0.290 (n=952)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7842 (IC base=+0.006)

- **PATRÓN** `volumen_spike_ratio` > `2.4256` → IC=+0.281 (n=477)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4256 (IC base=+0.006)

- **PATRÓN** `ballena_activa_n` < `115.0` → IC=+0.282 (n=1450)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 115.0 (IC base=+0.006)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7407` → IC=-0.249 (n=2374)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7407
  - _Potencial_: sin este filtro IC_bueno=+0.311 (n=2379)

- **FILTRO** `ibs_20min` > `0.62` → IC=-0.235 (n=1121)

  - _Acción_: SKIP cuando `ibs_20min` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.152 (n=3366)

- **FILTRO** `sigma_ewma_delta_pct` > `8.264` → IC=-0.257 (n=512)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.264
  - _Potencial_: sin este filtro IC_bueno=+0.096 (n=3975)

- **PATRÓN** `ibs_20min` > `0.7407` → IC=+0.311 (n=2379)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7407 (IC base=+0.032)

- **PATRÓN** `dist_vwap_pct` > `1.0406` → IC=+0.357 (n=340)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0406 (IC base=+0.032)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.454` → IC=+0.154 (n=1928)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 2.454 (IC base=+0.032)

- **PATRÓN** `volumen_regimen` < `0.8445` → IC=+0.342 (n=1153)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8445 (IC base=+0.032)

- **PATRÓN** `volumen_regimen` > `0.696` → IC=+0.334 (n=1544)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.696 (IC base=+0.032)

- **PATRÓN** `volumen_pendiente_norm` < `0.156` → IC=+0.335 (n=1783)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.156 (IC base=+0.032)

- **PATRÓN** `volumen_pendiente_norm` > `0.274` → IC=+0.362 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.274 (IC base=+0.032)

- **PATRÓN** `volumen_spike_ratio` < `1.4223` → IC=+0.358 (n=560)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4223 (IC base=+0.032)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.350 (n=1129)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 34.0 (IC base=+0.032)

- **PATRÓN** `ibs_20min` < `0.62` → IC=+0.152 (n=3366)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` < 0.62 (IC base=+0.055)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.025` → IC=+0.130 (n=3163)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` < 3.025 (IC base=+0.055)

- **PATRÓN** `volumen_regimen` < `0.695` → IC=+0.281 (n=741)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.695 (IC base=+0.055)

- **PATRÓN** `volumen_pendiente_norm` > `0.0714` → IC=+0.291 (n=677)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0714 (IC base=+0.055)

- **PATRÓN** `volumen_spike_ratio` < `1.8044` → IC=+0.277 (n=1089)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8044 (IC base=+0.055)

- **PATRÓN** `ballena_activa_n` < `39.0` → IC=+0.280 (n=1479)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 39.0 (IC base=+0.055)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0158` → IC=+0.359 (n=1621)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0158 (IC base=+0.315)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.317 (n=2452)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.315)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.317 (n=1159)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.315)

- **PATRÓN** `ibs_20min` > `0.66` → IC=+0.344 (n=2433)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.66 (IC base=+0.315)

- **PATRÓN** `dist_vwap_pct` > `0.2942` → IC=+0.340 (n=1182)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2942 (IC base=+0.315)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.78` → IC=+0.333 (n=1186)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.78 (IC base=+0.315)

- **PATRÓN** `volumen_regimen` > `0.6291` → IC=+0.326 (n=2430)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6291 (IC base=+0.315)

- **PATRÓN** `volumen_pendiente_norm` > `0.2811` → IC=+0.347 (n=357)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2811 (IC base=+0.315)

- **PATRÓN** `volumen_spike_ratio` > `1.8021` → IC=+0.333 (n=1563)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8021 (IC base=+0.315)

- **PATRÓN** `libro_liquidez` > `2990.8858` → IC=+0.326 (n=810)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2990.8858 (IC base=+0.315)

- **PATRÓN** `ballena_activa_n` < `33.0` → IC=+0.343 (n=1910)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 33.0 (IC base=+0.315)

- **PATRÓN** `sigma_h` > `0.0151` → IC=+0.350 (n=1735)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0151 (IC base=+0.316)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.322 (n=1315)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.316)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.318 (n=1260)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.316)

- **PATRÓN** `ibs_20min` < `0.3806` → IC=+0.335 (n=2602)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3806 (IC base=+0.316)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.619` → IC=+0.328 (n=957)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.619 (IC base=+0.316)

- **PATRÓN** `volumen_regimen` < `0.7186` → IC=+0.322 (n=1145)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7186 (IC base=+0.316)

- **PATRÓN** `volumen_regimen` > `1.2085` → IC=+0.342 (n=867)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2085 (IC base=+0.316)

- **PATRÓN** `volumen_pendiente_norm` > `0.23` → IC=+0.366 (n=490)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.23 (IC base=+0.316)

- **PATRÓN** `volumen_spike_ratio` < `1.4118` → IC=+0.325 (n=807)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4118 (IC base=+0.316)

- **PATRÓN** `volumen_spike_ratio` > `2.1396` → IC=+0.316 (n=1097)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1396 (IC base=+0.316)

- **PATRÓN** `libro_liquidez` > `2972.0828` → IC=+0.317 (n=867)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2972.0828 (IC base=+0.316)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.224 (n=5706)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0125 (IC base=+0.173)

- **PATRÓN** `drift_60min` |x|≤ `0.122` → IC=+0.191 (n=7526)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.122 (IC base=+0.173)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.183 (n=17727)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.173)

- **PATRÓN** `ibs_20min` > `0.537` → IC=+0.230 (n=17106)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.537 (IC base=+0.173)

- **PATRÓN** `dist_vwap_pct` > `0.1621` → IC=+0.205 (n=6479)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1621 (IC base=+0.173)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.764` → IC=+0.258 (n=3334)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.764 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` < `1.1799` → IC=+0.152 (n=11392)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.1799 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` > `0.6249` → IC=+0.151 (n=11391)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.6249 (IC base=+0.173)

- **PATRÓN** `volumen_pendiente_norm` > `0.2941` → IC=+0.203 (n=2483)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2941 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` > `2.6077` → IC=+0.187 (n=5547)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.6077 (IC base=+0.173)

- **PATRÓN** `ballena_activa_n` < `87.0` → IC=+0.192 (n=16031)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 87.0 (IC base=+0.173)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.193 (n=7416)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0058 (IC base=+0.184)

- **PATRÓN** `sigma_h` > `0.0078` → IC=+0.184 (n=11215)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` > 0.0078 (IC base=+0.184)

- **PATRÓN** `drift_60min` |x|≤ `0.2085` → IC=+0.209 (n=11211)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2085 (IC base=+0.184)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.211 (n=6321)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.184)

- **PATRÓN** `ibs_20min` < `0.5263` → IC=+0.239 (n=16815)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5263 (IC base=+0.184)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.519` → IC=+0.190 (n=2678)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 9.519 (IC base=+0.184)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.509` → IC=+0.190 (n=14969)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` < 2.509 (IC base=+0.184)

- **PATRÓN** `volumen_regimen` < `1.181` → IC=+0.164 (n=11964)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.181 (IC base=+0.184)

- **PATRÓN** `volumen_pendiente_norm` > `0.2938` → IC=+0.220 (n=2518)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2938 (IC base=+0.184)

- **PATRÓN** `volumen_spike_ratio` > `2.6297` → IC=+0.193 (n=5334)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.6297 (IC base=+0.184)

- **PATRÓN** `ballena_activa_n` < `91.0` → IC=+0.198 (n=15792)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 91.0 (IC base=+0.184)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` > `0.0108` → IC=+0.267 (n=940)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0108 (IC base=+0.227)

- **PATRÓN** `drift_60min` |x|≤ `0.1041` → IC=+0.256 (n=1241)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1041 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.234 (n=2929)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.227)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.227 (n=1920)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.227)

- **PATRÓN** `ibs_20min` > `0.9423` → IC=+0.295 (n=1879)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9423 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.46` → IC=+0.329 (n=921)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.46 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` > `0.2814` → IC=+0.287 (n=430)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2814 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` < `1.8383` → IC=+0.226 (n=1793)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8383 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` > `1.4363` → IC=+0.227 (n=2688)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4363 (IC base=+0.227)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.237 (n=3130)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.227)

- **PATRÓN** `sigma_h` < `0.0099` → IC=+0.259 (n=2289)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0099 (IC base=+0.257)

- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.259 (n=1043)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0089 (IC base=+0.257)

- **PATRÓN** `drift_60min` |x|≤ `0.0967` → IC=+0.316 (n=1006)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0967 (IC base=+0.257)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.262 (n=2361)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.257)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.261 (n=2084)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.257)

- **PATRÓN** `ibs_20min` < `0.0544` → IC=+0.302 (n=1006)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0544 (IC base=+0.257)

- **PATRÓN** `volumen_pendiente_norm` < `0.0993` → IC=+0.260 (n=2011)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0993 (IC base=+0.257)

- **PATRÓN** `volumen_pendiente_norm` > `0.3012` → IC=+0.274 (n=343)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3012 (IC base=+0.257)

- **PATRÓN** `volumen_spike_ratio` < `1.4456` → IC=+0.279 (n=730)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4456 (IC base=+0.257)

- **PATRÓN** `volumen_spike_ratio` > `2.6917` → IC=+0.258 (n=730)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6917 (IC base=+0.257)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.267 (n=1631)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.257)

- **PATRÓN** `libro_liquidez` > `1775.5` → IC=+0.265 (n=1524)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1775.5 (IC base=+0.257)

- **PATRÓN** `ballena_activa_n` < `7.0` → IC=+0.259 (n=855)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 7.0 (IC base=+0.257)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.201 (n=876)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.128)

- **PATRÓN** `drift_60min` |x|≤ `0.0657` → IC=+0.176 (n=872)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.0657 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.145 (n=2731)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` > `0.2583` → IC=+0.206 (n=2612)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2583 (IC base=+0.128)

- **PATRÓN** `dist_vwap_pct` > `0.1838` → IC=+0.212 (n=1299)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1838 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.646` → IC=+0.208 (n=478)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.646 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` < `0.6958` → IC=+0.130 (n=1150)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 0.6958 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` > `1.0569` → IC=+0.135 (n=1184)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` > 1.0569 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` > `0.2801` → IC=+0.169 (n=406)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.2801 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` < `1.5061` → IC=+0.132 (n=1130)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 1.5061 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` > `2.4689` → IC=+0.148 (n=856)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 2.4689 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `398.0` → IC=+0.132 (n=2536)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 398.0 (IC base=+0.128)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.172 (n=2764)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0065 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.2376` → IC=+0.173 (n=2432)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.2376 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.180 (n=1314)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 15.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` < `0.6112` → IC=+0.210 (n=2764)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6112 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.86` → IC=+0.179 (n=522)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 10.86 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.023` → IC=+0.152 (n=2411)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` < 4.023 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `1.195` → IC=+0.161 (n=2764)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.195 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` < `0.094` → IC=+0.149 (n=2388)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` < 0.094 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `2.4587` → IC=+0.153 (n=2638)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.4587 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `210.0` → IC=+0.190 (n=1143)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 210.0 (IC base=+0.148)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0115` → IC=+0.231 (n=1317)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0115 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.2482` → IC=+0.233 (n=1932)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2482 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.220 (n=3011)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.293 (n=1539)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.089` → IC=+0.303 (n=689)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.089 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` < `0.0988` → IC=+0.211 (n=2521)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0988 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` > `0.3522` → IC=+0.241 (n=411)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3522 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `2.7137` → IC=+0.224 (n=1282)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7137 (IC base=+0.212)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.216 (n=3499)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `2007.2584` → IC=+0.223 (n=966)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2007.2584 (IC base=+0.212)

- **PATRÓN** `sigma_h` < `0.0118` → IC=+0.246 (n=2561)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0118 (IC base=+0.239)

- **PATRÓN** `drift_60min` |x|≤ `0.4112` → IC=+0.262 (n=2253)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4112 (IC base=+0.239)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.279 (n=980)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.239)

- **PATRÓN** `ibs_20min` < `0.0397` → IC=+0.290 (n=1126)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0397 (IC base=+0.239)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.896` → IC=+0.280 (n=339)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.896 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` > `0.3558` → IC=+0.288 (n=428)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3558 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` < `1.775` → IC=+0.241 (n=1088)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.775 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` > `2.1818` → IC=+0.251 (n=1647)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1818 (IC base=+0.239)

- **PATRÓN** `libro_liquidez` > `1882.2022` → IC=+0.250 (n=1160)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1882.2022 (IC base=+0.239)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.245 (n=1695)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.239)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.203 (n=939)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0038 (IC base=+0.128)

- **PATRÓN** `drift_60min` |x|≤ `0.0775` → IC=+0.183 (n=939)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.0775 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.138 (n=2908)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` > `0.2458` → IC=+0.190 (n=2814)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.2458 (IC base=+0.128)

- **PATRÓN** `dist_vwap_pct` > `0.1389` → IC=+0.186 (n=1617)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1389 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.257` → IC=+0.199 (n=483)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 11.257 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` < `0.8426` → IC=+0.136 (n=1876)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.8426 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` > `0.2881` → IC=+0.167 (n=425)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` > 0.2881 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` > `2.511` → IC=+0.145 (n=919)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 2.511 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `6839.7566` → IC=+0.196 (n=1276)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 6839.7566 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `126.0` → IC=+0.128 (n=2753)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 126.0 (IC base=+0.128)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.165 (n=2641)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0067 (IC base=+0.130)

- **PATRÓN** `drift_60min` |x|≤ `0.3967` → IC=+0.146 (n=2999)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.3967 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.165 (n=1435)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 15.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` < `0.6779` → IC=+0.186 (n=2999)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.6779 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.209` → IC=+0.140 (n=715)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 9.209 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` < `0.851` → IC=+0.150 (n=2001)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.851 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` > `0.2939` → IC=+0.173 (n=448)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.2939 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` < `1.799` → IC=+0.132 (n=1897)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 1.799 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` > `1.4148` → IC=+0.131 (n=2845)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 1.4148 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `6314.0593` → IC=+0.190 (n=1360)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 6314.0593 (IC base=+0.130)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.153 (n=974)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 49.0 (IC base=+0.130)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.160 (n=1426)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0113 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.132 (n=3214)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 5.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` > `0.4706` → IC=+0.204 (n=3146)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4706 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` > `0.1961` → IC=+0.187 (n=1676)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1961 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.984` → IC=+0.286 (n=663)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.984 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` < `1.1689` → IC=+0.129 (n=3140)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 1.1689 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` < `0.1628` → IC=+0.123 (n=3198)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_pendiente_norm` < 0.1628 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` < `1.7794` → IC=+0.125 (n=2031)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 1.7794 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `2663.894` → IC=+0.193 (n=1424)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 2663.894 (IC base=+0.118)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.133 (n=1038)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 16.0 (IC base=+0.118)

- **PATRÓN** `sigma_h` < `0.0119` → IC=+0.142 (n=3285)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.0119 (IC base=+0.119)

- **PATRÓN** `drift_60min` |x|≤ `0.1126` → IC=+0.164 (n=1094)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.1126 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.134 (n=3351)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 5.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` < `0.65` → IC=+0.219 (n=3280)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.65 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.253` → IC=+0.139 (n=2905)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` < 2.253 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` < `1.1719` → IC=+0.126 (n=3280)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` < 1.1719 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` > `0.2749` → IC=+0.145 (n=452)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` > 0.2749 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` < `1.4337` → IC=+0.137 (n=1034)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.4337 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `2900.261` → IC=+0.196 (n=1093)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 2900.261 (IC base=+0.119)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.124 (n=2083)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 27.0 (IC base=+0.119)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0131` → IC=+0.249 (n=2525)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0131 (IC base=+0.226)

- **PATRÓN** `drift_60min` |x|≤ `0.1654` → IC=+0.240 (n=1245)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1654 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.231 (n=2934)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.226)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.228 (n=2551)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.226)

- **PATRÓN** `ibs_20min` > `0.6667` → IC=+0.257 (n=2826)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6667 (IC base=+0.226)

- **PATRÓN** `dist_vwap_pct` > `0.1814` → IC=+0.233 (n=1732)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1814 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.577` → IC=+0.256 (n=1285)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.577 (IC base=+0.226)

- **PATRÓN** `volumen_regimen` > `0.6237` → IC=+0.235 (n=2826)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6237 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` > `0.2352` → IC=+0.267 (n=525)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2352 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` < `2.4732` → IC=+0.229 (n=2757)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4732 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` > `1.4338` → IC=+0.230 (n=2757)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4338 (IC base=+0.226)

- **PATRÓN** `libro_liquidez` > `2584.5792` → IC=+0.232 (n=1884)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2584.5792 (IC base=+0.226)

- **PATRÓN** `sigma_h` > `0.0228` → IC=+0.250 (n=1325)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0228 (IC base=+0.240)

- **PATRÓN** `drift_60min` |x|≤ `0.5789` → IC=+0.249 (n=2923)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5789 (IC base=+0.240)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.252 (n=1432)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.240)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.246 (n=1306)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.240)

- **PATRÓN** `ibs_20min` < `0.44` → IC=+0.264 (n=2930)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.44 (IC base=+0.240)

- **PATRÓN** `dist_vwap_pct` > `1.1462` → IC=+0.257 (n=270)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1462 (IC base=+0.240)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.973` → IC=+0.268 (n=407)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.973 (IC base=+0.240)

- **PATRÓN** `volumen_regimen` < `0.8653` → IC=+0.243 (n=1950)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8653 (IC base=+0.240)

- **PATRÓN** `volumen_regimen` > `0.6401` → IC=+0.244 (n=2923)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6401 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` > `0.2811` → IC=+0.292 (n=406)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2811 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` < `2.5237` → IC=+0.237 (n=2757)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5237 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` > `1.5486` → IC=+0.242 (n=2463)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5486 (IC base=+0.240)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.209 (n=1484)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.159)

- **PATRÓN** `drift_60min` |x|≤ `0.1332` → IC=+0.174 (n=1947)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.1332 (IC base=+0.159)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.171 (n=4618)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 5.0 (IC base=+0.159)

- **PATRÓN** `ibs_20min` > `0.3077` → IC=+0.196 (n=4425)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.3077 (IC base=+0.159)

- **PATRÓN** `dist_vwap_pct` > `0.2206` → IC=+0.183 (n=1680)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.2206 (IC base=+0.159)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.557` → IC=+0.209 (n=722)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.557 (IC base=+0.159)

- **PATRÓN** `volumen_regimen` < `0.8604` → IC=+0.170 (n=2681)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 0.8604 (IC base=+0.159)

- **PATRÓN** `volumen_regimen` > `1.1935` → IC=+0.164 (n=1340)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 1.1935 (IC base=+0.159)

- **PATRÓN** `volumen_pendiente_norm` > `0.1571` → IC=+0.174 (n=1166)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.1571 (IC base=+0.159)

- **PATRÓN** `volumen_spike_ratio` < `1.5271` → IC=+0.164 (n=1898)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.5271 (IC base=+0.159)

- **PATRÓN** `volumen_spike_ratio` > `1.8093` → IC=+0.162 (n=2875)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.8093 (IC base=+0.159)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.160 (n=4952)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.02 (IC base=+0.159)

- **PATRÓN** `libro_liquidez` > `7707.6876` → IC=+0.187 (n=2005)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 7707.6876 (IC base=+0.159)

- **PATRÓN** `ibs_20min` < `0.3843` → IC=+0.173 (n=3198)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.3843 (IC base=+0.094)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.136 (n=2086)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 24.0 (IC base=+0.094)

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

- **PATRÓN** `drift_60min` |x|≤ `0.2091` → IC=+0.156 (n=906)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.2091 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.172 (n=1408)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 5.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` > `0.7941` → IC=+0.265 (n=616)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7941 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` > `0.5732` → IC=+0.190 (n=295)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.5732 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.882` → IC=+0.206 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.882 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` < `0.8322` → IC=+0.165 (n=906)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.8322 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` > `0.2202` → IC=+0.199 (n=247)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2202 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` > `1.7764` → IC=+0.169 (n=893)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 1.7764 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `8056.4451` → IC=+0.175 (n=616)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 8056.4451 (IC base=+0.153)

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.123 (n=882)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0052 (IC base=+0.092)

- **PATRÓN** `ibs_20min` < `0.0847` → IC=+0.211 (n=441)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0847 (IC base=+0.092)

- **PATRÓN** `libro_liquidez` > `7996.0605` → IC=+0.151 (n=599)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 7996.0605 (IC base=+0.092)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.131 (n=437)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 35.0 (IC base=+0.092)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` < `0.0092` → IC=+0.148 (n=765)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0092 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.172 (n=799)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 11.0 (IC base=+0.129)

- **PATRÓN** `ibs_20min` > `0.5469` → IC=+0.197 (n=1023)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.5469 (IC base=+0.129)

- **PATRÓN** `dist_vwap_pct` > `0.9272` → IC=+0.175 (n=186)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.9272 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.857` → IC=+0.229 (n=452)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.857 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` < `1.0445` → IC=+0.141 (n=1008)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 1.0445 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` > `0.7005` → IC=+0.137 (n=1023)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` > 0.7005 (IC base=+0.129)

- **PATRÓN** `volumen_pendiente_norm` > `0.225` → IC=+0.157 (n=202)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` > 0.225 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` < `1.4112` → IC=+0.156 (n=370)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.4112 (IC base=+0.129)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.132 (n=1199)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.02 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `2766.388` → IC=+0.170 (n=519)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 2766.388 (IC base=+0.129)

- **PATRÓN** `ibs_20min` < `0.5574` → IC=+0.149 (n=1115)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.5574 (IC base=+0.072)

- **PATRÓN** `libro_liquidez` > `2643.337` → IC=+0.164 (n=575)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 2643.337 (IC base=+0.072)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0175` → IC=+0.240 (n=252)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0175 (IC base=+0.192)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.236 (n=180)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.192)

- **PATRÓN** `ibs_20min` > `0.7222` → IC=+0.209 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7222 (IC base=+0.192)

- **PATRÓN** `dist_vwap_pct` > `0.3129` → IC=+0.208 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3129 (IC base=+0.192)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.49` → IC=+0.218 (n=335)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.49 (IC base=+0.192)

- **PATRÓN** `volumen_regimen` > `1.1939` → IC=+0.258 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1939 (IC base=+0.192)

- **PATRÓN** `volumen_pendiente_norm` > `0.078` → IC=+0.206 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.078 (IC base=+0.192)

- **PATRÓN** `volumen_spike_ratio` < `2.1565` → IC=+0.206 (n=308)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1565 (IC base=+0.192)

- **PATRÓN** `volumen_spike_ratio` > `2.4009` → IC=+0.206 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4009 (IC base=+0.192)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.201 (n=412)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.192)

- **PATRÓN** `libro_liquidez` > `3017.6749` → IC=+0.203 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3017.6749 (IC base=+0.192)

- **PATRÓN** `sigma_h` > `0.0132` → IC=+0.157 (n=368)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0132 (IC base=+0.142)

- **PATRÓN** `drift_60min` |x|≤ `0.3165` → IC=+0.157 (n=275)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.3165 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.196 (n=192)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 15.0 (IC base=+0.142)

- **PATRÓN** `ibs_20min` < `0.4984` → IC=+0.159 (n=362)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.4984 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` > `1.2117` → IC=+0.266 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2117 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.17` → IC=+0.173 (n=108)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 5.17 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.238` → IC=+0.141 (n=369)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 2.238 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` < `0.8853` → IC=+0.190 (n=275)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` < 0.8853 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` < `0.1106` → IC=+0.161 (n=378)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` < 0.1106 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` > `0.2292` → IC=+0.163 (n=78)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.2292 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` < `1.4907` → IC=+0.202 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4907 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` > `2.6497` → IC=+0.157 (n=132)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 2.6497 (IC base=+0.142)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.160 (n=395)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 20.0 (IC base=+0.142)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.229 (n=7476)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0125 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.190 (n=23352)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` > `0.4298` → IC=+0.227 (n=22406)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4298 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` > `0.8803` → IC=+0.212 (n=2623)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8803 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.936` → IC=+0.257 (n=5485)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.936 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` < `1.2141` → IC=+0.159 (n=15091)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.2141 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.2409` → IC=+0.208 (n=4030)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2409 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `2.6231` → IC=+0.194 (n=7293)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.6231 (IC base=+0.180)

- **PATRÓN** `ballena_activa_n` < `103.0` → IC=+0.201 (n=21075)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 103.0 (IC base=+0.180)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.199 (n=9055)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0061 (IC base=+0.196)

- **PATRÓN** `sigma_h` > `0.0122` → IC=+0.205 (n=6861)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0122 (IC base=+0.196)

- **PATRÓN** `drift_60min` |x|≤ `0.4818` → IC=+0.199 (n=20571)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.4818 (IC base=+0.196)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.216 (n=7682)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.196)

- **PATRÓN** `ibs_20min` < `0.5926` → IC=+0.245 (n=20572)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5926 (IC base=+0.196)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.53` → IC=+0.202 (n=19090)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.53 (IC base=+0.196)

- **PATRÓN** `volumen_regimen` < `0.6317` → IC=+0.178 (n=4606)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` < 0.6317 (IC base=+0.196)

- **PATRÓN** `volumen_pendiente_norm` > `0.2931` → IC=+0.254 (n=2827)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2931 (IC base=+0.196)

- **PATRÓN** `volumen_spike_ratio` > `2.6295` → IC=+0.207 (n=6565)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6295 (IC base=+0.196)

- **PATRÓN** `ballena_activa_n` < `91.0` → IC=+0.212 (n=19467)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 91.0 (IC base=+0.196)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.252 (n=1737)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.236)

- **PATRÓN** `ibs_20min` > `0.8644` → IC=+0.297 (n=2393)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8644 (IC base=+0.236)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.034` → IC=+0.301 (n=2353)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.034 (IC base=+0.236)

- **PATRÓN** `volumen_pendiente_norm` > `0.2321` → IC=+0.293 (n=649)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2321 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` < `1.4504` → IC=+0.234 (n=1155)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4504 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` > `2.2898` → IC=+0.241 (n=1571)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2898 (IC base=+0.236)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.250 (n=3947)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.236)

- **PATRÓN** `libro_liquidez` > `2038.12` → IC=+0.240 (n=1197)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2038.12 (IC base=+0.236)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.253 (n=2192)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 14.0 (IC base=+0.236)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.271 (n=3192)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0103 (IC base=+0.269)

- **PATRÓN** `sigma_h` > `0.0092` → IC=+0.270 (n=1452)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0092 (IC base=+0.269)

- **PATRÓN** `drift_60min` |x|≤ `0.1216` → IC=+0.296 (n=1406)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1216 (IC base=+0.269)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.271 (n=3316)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.269)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.272 (n=2890)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.269)

- **PATRÓN** `ibs_20min` < `0.5496` → IC=+0.287 (n=3192)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5496 (IC base=+0.269)

- **PATRÓN** `volumen_pendiente_norm` < `0.0981` → IC=+0.273 (n=2905)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0981 (IC base=+0.269)

- **PATRÓN** `volumen_pendiente_norm` > `0.2905` → IC=+0.286 (n=442)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2905 (IC base=+0.269)

- **PATRÓN** `volumen_spike_ratio` < `1.5629` → IC=+0.273 (n=1348)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5629 (IC base=+0.269)

- **PATRÓN** `volumen_spike_ratio` > `2.6471` → IC=+0.280 (n=1021)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6471 (IC base=+0.269)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.276 (n=2262)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.269)

- **PATRÓN** `libro_liquidez` > `1776.167` → IC=+0.277 (n=2128)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1776.167 (IC base=+0.269)

- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.283 (n=1133)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 8.0 (IC base=+0.269)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.179 (n=1227)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0031 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.0787` → IC=+0.148 (n=1226)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.0787 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.148 (n=3827)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 5.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` > `0.1964` → IC=+0.188 (n=3672)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.1964 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.3199` → IC=+0.199 (n=1189)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.3199 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.333` → IC=+0.167 (n=766)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 9.333 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `0.6358` → IC=+0.154 (n=1226)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.6358 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` > `1.0686` → IC=+0.141 (n=1665)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 1.0686 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.2707` → IC=+0.180 (n=517)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.2707 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `2.1664` → IC=+0.140 (n=3174)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 2.1664 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `1.5203` → IC=+0.142 (n=3222)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.5203 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `219.0` → IC=+0.161 (n=1189)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 219.0 (IC base=+0.136)

- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.163 (n=3163)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0064 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.3264` → IC=+0.146 (n=3163)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.3264 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.167 (n=1160)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 17.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` < `0.6806` → IC=+0.186 (n=3163)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.6806 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.014` → IC=+0.137 (n=1515)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 3.014 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.002` → IC=+0.138 (n=2858)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 4.002 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `1.0457` → IC=+0.150 (n=2784)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 1.0457 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.2196` → IC=+0.195 (n=588)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2196 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `2.4321` → IC=+0.143 (n=3054)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.4321 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `1.7707` → IC=+0.142 (n=2036)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.7707 (IC base=+0.137)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.138 (n=4110)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `223.0` → IC=+0.153 (n=993)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 223.0 (IC base=+0.137)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.242 (n=2490)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0099 (IC base=+0.228)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.237 (n=3903)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.228)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.228 (n=3342)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.228)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.303 (n=1394)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.228)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.01` → IC=+0.323 (n=832)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.01 (IC base=+0.228)

- **PATRÓN** `volumen_pendiente_norm` < `0.132` → IC=+0.230 (n=3533)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.132 (IC base=+0.228)

- **PATRÓN** `volumen_pendiente_norm` > `0.3507` → IC=+0.230 (n=487)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3507 (IC base=+0.228)

- **PATRÓN** `volumen_spike_ratio` > `2.7431` → IC=+0.243 (n=1653)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7431 (IC base=+0.228)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.234 (n=4497)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.228)

- **PATRÓN** `libro_liquidez` > `1910.6984` → IC=+0.238 (n=1691)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1910.6984 (IC base=+0.228)

- **PATRÓN** `sigma_h` < `0.011` → IC=+0.250 (n=3142)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.011 (IC base=+0.245)

- **PATRÓN** `drift_60min` |x|≤ `0.1771` → IC=+0.266 (n=1570)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1771 (IC base=+0.245)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.263 (n=1355)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.245)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.248 (n=1625)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.245)

- **PATRÓN** `ibs_20min` < `0.0606` → IC=+0.304 (n=1190)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0606 (IC base=+0.245)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.06` → IC=+0.304 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.06 (IC base=+0.245)

- **PATRÓN** `volumen_pendiente_norm` > `0.3492` → IC=+0.308 (n=539)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3492 (IC base=+0.245)

- **PATRÓN** `volumen_spike_ratio` > `2.1786` → IC=+0.256 (n=2289)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1786 (IC base=+0.245)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.250 (n=1828)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.245)

- **PATRÓN** `libro_liquidez` > `1992.72` → IC=+0.257 (n=1188)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1992.72 (IC base=+0.245)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.250 (n=3013)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 22.0 (IC base=+0.245)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.193 (n=1296)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0037 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.4311` → IC=+0.145 (n=3875)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.4311 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.149 (n=4017)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 5.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` > `0.8859` → IC=+0.271 (n=1292)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8859 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` > `0.1957` → IC=+0.169 (n=1743)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.1957 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.96` → IC=+0.157 (n=1722)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 2.96 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `0.86` → IC=+0.151 (n=2584)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.86 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.2333` → IC=+0.189 (n=687)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.2333 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `1.5176` → IC=+0.153 (n=1667)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 1.5176 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `2.1727` → IC=+0.143 (n=1717)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 2.1727 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `7279.5454` → IC=+0.239 (n=1292)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7279.5454 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `87.0` → IC=+0.146 (n=2510)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 87.0 (IC base=+0.137)

- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.170 (n=2847)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0068 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.4365` → IC=+0.157 (n=3235)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.4365 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.173 (n=1191)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 17.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` < `0.5737` → IC=+0.212 (n=2848)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5737 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.853` → IC=+0.155 (n=474)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 10.853 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.043` → IC=+0.151 (n=2822)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 3.043 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` < `0.6898` → IC=+0.163 (n=1423)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.6898 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` > `0.2941` → IC=+0.214 (n=410)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2941 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `2.2078` → IC=+0.151 (n=2749)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.2078 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` > `1.5315` → IC=+0.155 (n=2790)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.5315 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `6441.0912` → IC=+0.223 (n=1078)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6441.0912 (IC base=+0.147)

- **PATRÓN** `ballena_activa_n` < `90.0` → IC=+0.162 (n=2117)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 90.0 (IC base=+0.147)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0127` → IC=+0.151 (n=1317)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` > 0.0127 (IC base=+0.115)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.146 (n=2780)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 11.0 (IC base=+0.115)

- **PATRÓN** `ibs_20min` > `0.4286` → IC=+0.185 (n=3953)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.4286 (IC base=+0.115)

- **PATRÓN** `dist_vwap_pct` > `1.0011` → IC=+0.201 (n=630)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0011 (IC base=+0.115)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.244` → IC=+0.269 (n=999)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.244 (IC base=+0.115)

- **PATRÓN** `volumen_regimen` < `0.8761` → IC=+0.128 (n=2628)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 0.8761 (IC base=+0.115)

- **PATRÓN** `volumen_spike_ratio` < `1.8238` → IC=+0.121 (n=2566)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` < 1.8238 (IC base=+0.115)

- **PATRÓN** `libro_liquidez` > `2711.1262` → IC=+0.236 (n=1314)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2711.1262 (IC base=+0.115)

- **PATRÓN** `sigma_h` < `0.0109` → IC=+0.153 (n=3250)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0109 (IC base=+0.128)

- **PATRÓN** `drift_60min` |x|≤ `0.1376` → IC=+0.153 (n=1231)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.1376 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.164 (n=1731)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 15.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` < `0.6667` → IC=+0.217 (n=3700)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6667 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.039` → IC=+0.150 (n=3572)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 3.039 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` < `0.6401` → IC=+0.151 (n=1233)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.6401 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` > `0.2288` → IC=+0.185 (n=649)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.2288 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` < `1.4381` → IC=+0.161 (n=1170)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 1.4381 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `2601.1546` → IC=+0.211 (n=1231)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2601.1546 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.142 (n=3112)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 42.0 (IC base=+0.128)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0138` → IC=+0.260 (n=3221)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0138 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.244 (n=3765)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.238)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.243 (n=2411)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.238)

- **PATRÓN** `ibs_20min` > `0.6142` → IC=+0.272 (n=3219)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6142 (IC base=+0.238)

- **PATRÓN** `dist_vwap_pct` > `0.1935` → IC=+0.253 (n=1842)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1935 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.156` → IC=+0.289 (n=627)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.156 (IC base=+0.238)

- **PATRÓN** `volumen_regimen` < `1.2177` → IC=+0.239 (n=3604)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2177 (IC base=+0.238)

- **PATRÓN** `volumen_regimen` > `0.6434` → IC=+0.243 (n=3604)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6434 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` > `0.2395` → IC=+0.255 (n=623)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2395 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` > `2.5002` → IC=+0.260 (n=1175)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5002 (IC base=+0.238)

- **PATRÓN** `libro_liquidez` > `2981.0662` → IC=+0.245 (n=1201)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2981.0662 (IC base=+0.238)

- **PATRÓN** `sigma_h` > `0.0258` → IC=+0.267 (n=1245)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0258 (IC base=+0.244)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.248 (n=3513)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.244)

- **PATRÓN** `ibs_20min` < `0.1387` → IC=+0.309 (n=1640)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1387 (IC base=+0.244)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.09` → IC=+0.277 (n=719)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.09 (IC base=+0.244)

- **PATRÓN** `volumen_regimen` < `0.7154` → IC=+0.245 (n=1640)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7154 (IC base=+0.244)

- **PATRÓN** `volumen_regimen` > `1.2151` → IC=+0.264 (n=1242)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2151 (IC base=+0.244)

- **PATRÓN** `volumen_pendiente_norm` > `0.2862` → IC=+0.306 (n=513)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2862 (IC base=+0.244)

- **PATRÓN** `volumen_spike_ratio` > `1.4324` → IC=+0.248 (n=3516)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4324 (IC base=+0.244)

- **PATRÓN** `libro_liquidez` > `2966.7242` → IC=+0.246 (n=1242)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2966.7242 (IC base=+0.244)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.201 (n=5926)

- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.245 (n=2141)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.221)

- **PATRÓN** `drift_60min` |x|≤ `0.5138` → IC=+0.229 (n=6403)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5138 (IC base=+0.221)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.228 (n=5792)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.221)

- **PATRÓN** `ibs_20min` > `0.9295` → IC=+0.257 (n=2134)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9295 (IC base=+0.221)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.509` → IC=+0.226 (n=2124)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.509 (IC base=+0.221)

- **PATRÓN** `volumen_regimen` < `0.7054` → IC=+0.232 (n=2067)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7054 (IC base=+0.221)

- **PATRÓN** `volumen_regimen` > `0.8791` → IC=+0.221 (n=3130)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8791 (IC base=+0.221)

- **PATRÓN** `volumen_pendiente_norm` < `0.105` → IC=+0.222 (n=5977)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.105 (IC base=+0.221)

- **PATRÓN** `volumen_pendiente_norm` > `0.165` → IC=+0.228 (n=1808)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.165 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` < `2.2533` → IC=+0.224 (n=5546)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.2533 (IC base=+0.221)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.226 (n=4805)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.221)

- **PATRÓN** `libro_liquidez` > `2883.2104` → IC=+0.225 (n=5720)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2883.2104 (IC base=+0.221)

- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.240 (n=1488)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.200)

- **PATRÓN** `drift_60min` |x|≤ `0.4964` → IC=+0.212 (n=4456)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4964 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.213 (n=1488)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.200)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.212 (n=1970)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.200)

- **PATRÓN** `ibs_20min` < `0.1847` → IC=+0.211 (n=1961)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1847 (IC base=+0.200)

- **PATRÓN** `dist_vwap_pct` > `0.6611` → IC=+0.208 (n=745)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6611 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.758` → IC=+0.212 (n=4013)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.758 (IC base=+0.200)

- **PATRÓN** `volumen_regimen` < `1.0959` → IC=+0.206 (n=3743)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0959 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` < `0.0976` → IC=+0.201 (n=4106)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0976 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` > `0.0732` → IC=+0.203 (n=1989)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0732 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` < `1.5307` → IC=+0.206 (n=1933)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5307 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` > `2.1824` → IC=+0.209 (n=1991)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1824 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.201 (n=5926)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.200)

- **PATRÓN** `ballena_activa_n` < `32.0` → IC=+0.222 (n=1951)

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
- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.219 (n=1807)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0084 (IC base=+0.206)

- **PATRÓN** `drift_60min` |x|≤ `0.4596` → IC=+0.213 (n=1806)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4596 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.232 (n=636)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.206)

- **PATRÓN** `ibs_20min` < `0.4744` → IC=+0.217 (n=1204)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4744 (IC base=+0.206)

- **PATRÓN** `ibs_20min` > `0.1447` → IC=+0.208 (n=1806)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1447 (IC base=+0.206)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.374` → IC=+0.214 (n=1831)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 6.374 (IC base=+0.206)

- **PATRÓN** `volumen_regimen` < `0.8673` → IC=+0.213 (n=1204)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8673 (IC base=+0.206)

- **PATRÓN** `volumen_pendiente_norm` < `0.102` → IC=+0.210 (n=1666)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.102 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` < `1.4047` → IC=+0.223 (n=590)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4047 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` > `1.4939` → IC=+0.207 (n=1580)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4939 (IC base=+0.206)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.206 (n=1793)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.206)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.243 (n=473)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.201)

- **PATRÓN** `drift_60min` |x|≤ `0.4897` → IC=+0.220 (n=1417)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4897 (IC base=+0.201)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.205 (n=533)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.201)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.217 (n=959)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.201)

- **PATRÓN** `ibs_20min` < `0.1707` → IC=+0.203 (n=624)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1707 (IC base=+0.201)

- **PATRÓN** `ibs_20min` > `0.6121` → IC=+0.206 (n=642)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6121 (IC base=+0.201)

- **PATRÓN** `dist_vwap_pct` > `0.6324` → IC=+0.217 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6324 (IC base=+0.201)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.266` → IC=+0.205 (n=1293)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.266 (IC base=+0.201)

- **PATRÓN** `volumen_regimen` < `1.2492` → IC=+0.210 (n=1417)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2492 (IC base=+0.201)

- **PATRÓN** `volumen_pendiente_norm` > `0.0728` → IC=+0.230 (n=583)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0728 (IC base=+0.201)

- **PATRÓN** `volumen_spike_ratio` < `1.4106` → IC=+0.210 (n=463)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4106 (IC base=+0.201)

- **PATRÓN** `volumen_spike_ratio` > `1.7831` → IC=+0.202 (n=926)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7831 (IC base=+0.201)

- **PATRÓN** `libro_liquidez` > `6551.6127` → IC=+0.206 (n=1265)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6551.6127 (IC base=+0.201)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0083` → IC=+0.234 (n=465)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0083 (IC base=+0.207)

- **PATRÓN** `hora_utc` > `10.0` → IC=+0.243 (n=718)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.207)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.285 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.207)

- **PATRÓN** `dist_vwap_pct` > `0.7706` → IC=+0.236 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7706 (IC base=+0.207)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.202` → IC=+0.235 (n=580)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.202 (IC base=+0.207)

- **PATRÓN** `volumen_regimen` < `0.7072` → IC=+0.242 (n=464)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7072 (IC base=+0.207)

- **PATRÓN** `volumen_pendiente_norm` < `0.1062` → IC=+0.215 (n=955)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1062 (IC base=+0.207)

- **PATRÓN** `volumen_pendiente_norm` > `0.2735` → IC=+0.213 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2735 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` < `2.1486` → IC=+0.216 (n=904)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1486 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` > `1.4745` → IC=+0.213 (n=1026)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4745 (IC base=+0.207)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.216 (n=1232)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.207)

- **PATRÓN** `libro_liquidez` > `4318.6372` → IC=+0.246 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4318.6372 (IC base=+0.207)

- **PATRÓN** `ballena_activa_n` < `38.0` → IC=+0.212 (n=917)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 38.0 (IC base=+0.207)

- **PATRÓN** `sigma_h` < `0.0118` → IC=+0.226 (n=644)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0118 (IC base=+0.225)

- **PATRÓN** `sigma_h` > `0.01` → IC=+0.244 (n=487)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.01 (IC base=+0.225)

- **PATRÓN** `drift_60min` |x|≤ `0.5987` → IC=+0.243 (n=730)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5987 (IC base=+0.225)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.226 (n=680)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.251 (n=512)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.225)

- **PATRÓN** `ibs_20min` < `0.7312` → IC=+0.254 (n=730)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7312 (IC base=+0.225)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.797` → IC=+0.240 (n=682)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.797 (IC base=+0.225)

- **PATRÓN** `volumen_regimen` < `0.7555` → IC=+0.235 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7555 (IC base=+0.225)

- **PATRÓN** `volumen_regimen` > `1.2667` → IC=+0.228 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2667 (IC base=+0.225)

- **PATRÓN** `volumen_pendiente_norm` < `0.0825` → IC=+0.239 (n=618)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0825 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` > `2.1876` → IC=+0.260 (n=323)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1876 (IC base=+0.225)

- **PATRÓN** `libro_liquidez` > `3802.5298` → IC=+0.238 (n=487)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3802.5298 (IC base=+0.225)

- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.264 (n=486)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 25.0 (IC base=+0.225)

### GBM_LATE_60M
- **FILTRO** `ibs_20min` > `0.6356` → IC=-0.146 (n=498)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6356
  - _Potencial_: sin este filtro IC_bueno=+0.131 (n=1497)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.151 (n=747)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0038 (IC base=+0.055)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.186 (n=1440)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.75 (IC base=+0.055)

- **PATRÓN** `dist_vwap_pct` > `0.1427` → IC=+0.144 (n=1056)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` > 0.1427 (IC base=+0.055)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.365` → IC=+0.148 (n=476)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 10.365 (IC base=+0.055)

- **PATRÓN** `ibs_20min` < `0.0639` → IC=+0.264 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0639 (IC base=+0.047)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.130 (n=627)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.65€ cuando `sigma_h` < 0.0053 (IC base=+0.071)

- **PATRÓN** `ibs_20min` > `0.5427` → IC=+0.165 (n=606)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` > 0.5427 (IC base=+0.071)

- **PATRÓN** `dist_vwap_pct` > `0.1195` → IC=+0.172 (n=321)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.1195 (IC base=+0.071)

- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.129 (n=270)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.64€ cuando `sigma_h` < 0.0035 (IC base=+0.044)

- **PATRÓN** `ibs_20min` < `0.0659` → IC=+0.264 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0659 (IC base=+0.044)

- **PATRÓN** `volumen_pendiente_norm` > `0.2173` → IC=+0.142 (n=118)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` > 0.2173 (IC base=+0.044)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` > `0.6751` → IC=-0.158 (n=159)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6751
  - _Potencial_: sin este filtro IC_bueno=+0.104 (n=478)

- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.150 (n=318)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0041 (IC base=+0.073)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.127 (n=357)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 15.0 (IC base=+0.073)

- **PATRÓN** `ibs_20min` > `0.7774` → IC=+0.219 (n=460)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7774 (IC base=+0.073)

- **PATRÓN** `dist_vwap_pct` > `0.1269` → IC=+0.174 (n=335)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.1269 (IC base=+0.073)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.65` → IC=+0.203 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.65 (IC base=+0.073)

- **PATRÓN** `ibs_20min` < `0.1105` → IC=+0.246 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1105 (IC base=+0.022)

### GBM_LATE_60M#SOL#60min
- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.195 (n=260)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 1.0 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` > `0.7109` → IC=+0.137 (n=177)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` > 0.7109 (IC base=+0.025)

- **PATRÓN** `sigma_h` < `0.0096` → IC=+0.184 (n=308)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0096 (IC base=+0.077)

- **PATRÓN** `ibs_20min` < `0.4857` → IC=+0.177 (n=431)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.4857 (IC base=+0.077)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.827` → IC=+0.276 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.827 (IC base=+0.077)

- **PATRÓN** `volumen_regimen` > `1.0831` → IC=+0.183 (n=143)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 1.0831 (IC base=+0.077)

- **PATRÓN** `volumen_pendiente_norm` > `0.1089` → IC=+0.161 (n=163)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.1089 (IC base=+0.077)

- **PATRÓN** `volumen_spike_ratio` > `1.4557` → IC=+0.123 (n=401)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` > 1.4557 (IC base=+0.077)

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
- **PATRÓN** `sigma_h` > `0.0086` → IC=+0.261 (n=241)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0086 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.193 (n=373)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 15.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` > `0.6774` → IC=+0.182 (n=722)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` > 0.6774 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.8034` → IC=+0.287 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8034 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.607` → IC=+0.160 (n=392)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 3.607 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `0.6244` → IC=+0.183 (n=241)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 0.6244 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` > `1.2135` → IC=+0.150 (n=241)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 1.2135 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` < `0.0701` → IC=+0.179 (n=537)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` < 0.0701 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `1.3961` → IC=+0.201 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3961 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.489` → IC=+0.153 (n=197)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 10.489 (IC base=+0.031)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.725` → IC=-0.153 (n=70)

  - _Acción_: SKIP cuando `ibs_20min` < 0.725
  - _Potencial_: sin este filtro IC_bueno=+0.103 (n=212)

- **PATRÓN** `sigma_h` > `0.0065` → IC=+0.144 (n=71)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` > 0.0065 (IC base=+0.039)

- **PATRÓN** `ibs_20min` > `0.9138` → IC=+0.129 (n=141)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` > 0.9138 (IC base=+0.039)

- **PATRÓN** `dist_vwap_pct` > `0.6135` → IC=+0.207 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6135 (IC base=+0.039)

- **PATRÓN** `ibs_20min` < `0.234` → IC=+0.143 (n=401)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` < 0.234 (IC base=+0.086)

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

- **PATRÓN** `sigma_h` > `0.011` → IC=+0.304 (n=90)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.011 (IC base=+0.256)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.301 (n=189)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.256)

- **PATRÓN** `ibs_20min` > `0.5882` → IC=+0.284 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5882 (IC base=+0.256)

- **PATRÓN** `dist_vwap_pct` > `0.6973` → IC=+0.392 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6973 (IC base=+0.256)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.832` → IC=+0.359 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.832 (IC base=+0.256)

- **PATRÓN** `volumen_regimen` < `0.5991` → IC=+0.304 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.5991 (IC base=+0.256)

- **PATRÓN** `volumen_pendiente_norm` > `0.0973` → IC=+0.327 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0973 (IC base=+0.256)

- **PATRÓN** `volumen_spike_ratio` < `1.396` → IC=+0.336 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.396 (IC base=+0.256)

- **PATRÓN** `volumen_spike_ratio` > `2.3425` → IC=+0.308 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3425 (IC base=+0.256)

### LATE_WINDOW_5MIN
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.326 (n=113)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3975` → IC=+0.347 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3975 (IC base=+0.328)

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

- **PATRÓN** `drift_ventana_pct` |x|> `0.3975` → IC=+0.347 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3975 (IC base=+0.328)

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
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=866)

### LIQUIDACIONES_15M#BNB#15min
- **PATRÓN** `liq_usd_total` > `1412.54` → IC=+0.200 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `liq_usd_total` > 1412.54 (IC base=+0.013)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `libro_liquidez` < `12324.2702` → IC=-0.152 (n=44)

  - _Acción_: SKIP cuando `libro_liquidez` < 12324.2702
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=90)

### LIQUIDACIONES_15M#DOGE#15min
- **PATRÓN** `hora_utc` < `10.0` → IC=+0.154 (n=24)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 10.0 (IC base=+0.033)

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
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=3940)

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

- **FILTRO** `ballena_activa_n` > `21.0` → IC=-0.153 (n=93)

  - _Acción_: SKIP cuando `ballena_activa_n` > 21.0
  - _Potencial_: sin este filtro IC_bueno=+0.188 (n=46)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.188 (n=46)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 21.0 (IC base=-0.077)

### LIQUIDACIONES_5M#BTC#5min
- **FILTRO** `libro_liquidez` < `13988.6712` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `libro_liquidez` < 13988.6712
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=19)

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
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=1606)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=1560)

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
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=1012)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=1012)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=1273)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=1273)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=292)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=292)

- **FILTRO** `py_entrada` < `0.42` → IC=-0.141 (n=76)

  - _Acción_: SKIP cuando `py_entrada` < 0.42
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=231)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.136 (n=64)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=350)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=399)

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
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=365)

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
- **FILTRO** `py_entrada` < `0.4` → IC=-0.135 (n=294)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=728)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **FILTRO** `py_entrada` > `0.57` → IC=-0.127 (n=432)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.085 (n=513)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.143 (n=315)

  - _Acción_: Kelly boost +0.72€ cuando `py_entrada` < 0.5 (IC base=-0.012)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` > `0.57` → IC=-0.123 (n=361)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.068 (n=368)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` > `0.58` → IC=-0.125 (n=345)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=409)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.135 (n=269)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=583)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.120 (n=585)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.068 (n=308)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.44` → IC=-0.139 (n=511)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=516)

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
- **FILTRO** `py_entrada` < `0.46` → IC=-0.175 (n=7966)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=25391)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.174 (n=8452)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=25979)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.188 (n=1547)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=4641)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.149 (n=2056)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.094 (n=4045)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.134 (n=1599)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` > 1.0 (IC base=+0.041)

- **PATRÓN** `py_entrada` < `0.505` → IC=+0.126 (n=3100)

  - _Acción_: Kelly boost +0.63€ cuando `py_entrada` < 0.505 (IC base=+0.012)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` < `0.44` → IC=-0.172 (n=1103)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=3526)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.181 (n=1183)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=3655)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` > `0.62` → IC=-0.202 (n=1530)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.087 (n=4727)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.137 (n=1903)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` > 1.0 (IC base=+0.034)

- **PATRÓN** `libro_liquidez` > `1739.0954` → IC=+0.120 (n=2100)

  - _Acción_: Kelly boost +0.60€ cuando `libro_liquidez` > 1739.0954 (IC base=+0.034)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.485` → IC=-0.162 (n=1538)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=4671)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=2436)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.162 (n=772)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=2360)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.180 (n=973)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=3062)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=4014)

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
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=1079)

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
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=972)

- **FILTRO** `ballena_activa_n` > `23.0` → IC=-0.191 (n=390)

  - _Acción_: SKIP cuando `ballena_activa_n` > 23.0
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=793)

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
  - _Potencial_: sin este filtro IC_bueno=-0.090 (n=51066)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.298 (n=17719)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=56085)

- **FILTRO** `ibs_7min` < `0.2162` → IC=-0.234 (n=18446)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2162
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=55358)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.152 (n=25091)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=48713)

- **FILTRO** `py_entrada` > `0.68` → IC=-0.252 (n=21574)

  - _Acción_: SKIP cuando `py_entrada` > 0.68
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=70676)

- **FILTRO** `ibs_7min` > `0.2824` → IC=-0.184 (n=23056)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2824
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=69194)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.157 (n=3189)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=9972)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.316 (n=3251)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=9910)

- **FILTRO** `ibs_7min` < `0.7105` → IC=-0.251 (n=4341)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7105
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=8820)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.152 (n=2784)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=10377)

- **FILTRO** `py_entrada` > `0.72` → IC=-0.276 (n=3897)

  - _Acción_: SKIP cuando `py_entrada` > 0.72
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=12035)

- **FILTRO** `ibs_7min` > `0.7778` → IC=-0.211 (n=3978)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7778
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=11954)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.264 (n=2966)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=9314)

- **FILTRO** `ibs_7min` < `0.7143` → IC=-0.209 (n=3069)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7143
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=9211)

- **FILTRO** `ballena_activa_n` > `155.0` → IC=-0.202 (n=3068)

  - _Acción_: SKIP cuando `ballena_activa_n` > 155.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=9212)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.268 (n=2872)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=9659)

- **FILTRO** `ibs_7min` > `0.2664` → IC=-0.194 (n=3132)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2664
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=9399)

- **FILTRO** `ballena_activa_n` > `153.0` → IC=-0.182 (n=3128)

  - _Acción_: SKIP cuando `ballena_activa_n` > 153.0
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=9403)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.166 (n=3051)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=9548)

- **FILTRO** `py_entrada` < `0.3` → IC=-0.325 (n=2994)

  - _Acción_: SKIP cuando `py_entrada` < 0.3
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=9605)

- **FILTRO** `ibs_7min` < `0.2857` → IC=-0.250 (n=4146)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2857
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=8453)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.202 (n=2511)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=10088)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.260 (n=4089)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=12779)

- **FILTRO** `ibs_7min` > `0.7317` → IC=-0.183 (n=4215)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7317
  - _Potencial_: sin este filtro IC_bueno=-0.000 (n=12653)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.263 (n=2961)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=8975)

- **FILTRO** `ibs_7min` < `0.7143` → IC=-0.196 (n=2982)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7143
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=8954)

- **FILTRO** `ballena_activa_n` > `25.0` → IC=-0.191 (n=2898)

  - _Acción_: SKIP cuando `ballena_activa_n` > 25.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=9038)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.259 (n=2885)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=9537)

- **FILTRO** `ibs_7min` > `0.2734` → IC=-0.177 (n=3105)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2734
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=9317)

- **FILTRO** `ballena_activa_n` > `24.0` → IC=-0.172 (n=3015)

  - _Acción_: SKIP cuando `ballena_activa_n` > 24.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=9407)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.32` → IC=-0.300 (n=2803)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=9015)

- **FILTRO** `ibs_7min` < `0.7` → IC=-0.235 (n=3838)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=7980)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.218 (n=2907)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=8911)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.199 (n=4340)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=13507)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.131 (n=3879)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.108 (n=8131)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.309 (n=2873)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=9137)

- **FILTRO** `ibs_7min` < `0.7368` → IC=-0.219 (n=3960)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7368
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=8050)

- **FILTRO** `ballena_activa_n` > `9.0` → IC=-0.205 (n=2662)

  - _Acción_: SKIP cuando `ballena_activa_n` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.090 (n=9348)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.234 (n=3858)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=12792)

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
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=895)

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
- **PATRÓN** `delta_ratio` |x|> `0.4307` → IC=+0.151 (n=691)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.75€ cuando `delta_ratio` |x|> 0.4307 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.128 (n=1369)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 14.0 (IC base=+0.124)

- **PATRÓN** `total_vol_5m` < `421.6695` → IC=+0.160 (n=507)

  - _Acción_: Kelly boost +0.80€ cuando `total_vol_5m` < 421.6695 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `3556.2094` → IC=+0.139 (n=690)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 3556.2094 (IC base=+0.124)

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
  - _Acción_: Kelly boost +0.79€ cuando `delta_ratio` |x|> 0.4378 (IC base=+0.118)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.138 (n=291)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 15.0 (IC base=+0.118)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.123 (n=377)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.04 (IC base=+0.118)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4164` → IC=+0.174 (n=191)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.87€ cuando `delta_ratio` |x|> 0.4164 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.144 (n=265)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.124)

- **PATRÓN** `total_vol_5m` < `857.788` → IC=+0.149 (n=286)

  - _Acción_: Kelly boost +0.75€ cuando `total_vol_5m` < 857.788 (IC base=+0.124)

- **PATRÓN** `ballena_activa_n` < `59.0` → IC=+0.173 (n=96)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 59.0 (IC base=+0.124)

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
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 14.0 (IC base=+0.101)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.134 (n=203)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.101)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `4.8182` → IC=-0.203 (n=116)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.8182
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=118)

- **FILTRO** `sigma_h` > `0.0068` → IC=-0.227 (n=291)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0068
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=565)

- **FILTRO** `T_h` > `129.6211` → IC=-0.170 (n=213)

  - _Acción_: SKIP cuando `T_h` > 129.6211
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=643)

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.146 (n=283)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0045 (IC base=-0.065)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `T_h` > `87.9981` → IC=-0.223 (n=63)

  - _Acción_: SKIP cuando `T_h` > 87.9981
  - _Potencial_: sin este filtro IC_bueno=+0.046 (n=192)

- **FILTRO** `pct_vs_K` |x|> `4.2515` → IC=-0.254 (n=63)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.2515
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=192)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.282 (n=85)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=-0.021)

- **PATRÓN** `pct_vs_K` |x|≤ `1.73` → IC=+0.178 (n=85)

  - _Acción_: Kelly boost +0.89€ cuando `pct_vs_K` |x|≤ 1.73 (IC base=-0.021)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `pct_vs_K` |x|> `6.6759` → IC=-0.267 (n=28)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 6.6759
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=56)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0156` → IC=-0.167 (n=40)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0156
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=124)

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
- **FILTRO** `T_h` > `49.2217` → IC=-0.210 (n=191)

  - _Acción_: SKIP cuando `T_h` > 49.2217
  - _Potencial_: sin este filtro IC_bueno=-0.157 (n=65)

- **FILTRO** `sigma_h` > `0.0062` → IC=-0.222 (n=124)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0062
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=127)

- **FILTRO** `T_h` > `143.4358` → IC=-0.234 (n=62)

  - _Acción_: SKIP cuando `T_h` > 143.4358
  - _Potencial_: sin este filtro IC_bueno=-0.181 (n=189)

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

- **FILTRO** `pct_vs_K` |x|> `2.8988` → IC=-0.415 (n=69)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.8988
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=136)

- **PATRÓN** `pct_vs_K` |x|≤ `0.8096` → IC=+0.204 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `pct_vs_K` |x|≤ 0.8096 (IC base=-0.152)

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
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=429)

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
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=4993)

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
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=2860)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.188 (n=1793)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0054 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.2206` → IC=+0.159 (n=5379)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.2206 (IC base=+0.141)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1345` → IC=+0.154 (n=2211)

  - _Acción_: Kelly boost +0.77€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1345 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.150 (n=4952)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 6.0 (IC base=+0.141)

- **PATRÓN** `ibs_15` > `0.5789` → IC=+0.224 (n=4808)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5789 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` > `0.1342` → IC=+0.133 (n=2526)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` > 0.1342 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` < `0.3238` → IC=+0.125 (n=4548)

  - _Acción_: Kelly boost +0.63€ cuando `dist_vwap_pct` < 0.3238 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.282` → IC=+0.247 (n=1020)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.282 (IC base=+0.141)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=3079)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `4543.3831` → IC=+0.169 (n=1793)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 4543.3831 (IC base=+0.141)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=2055)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.223 (n=793)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0057 (IC base=+0.202)

- **PATRÓN** `drift_60min` |x|≤ `0.0593` → IC=+0.257 (n=265)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0593 (IC base=+0.202)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2684` → IC=+0.222 (n=264)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2684 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.227 (n=728)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.202)

- **PATRÓN** `ibs_15` > `0.7082` → IC=+0.274 (n=793)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7082 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` > `0.3722` → IC=+0.228 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3722 (IC base=+0.202)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.41` → IC=+0.312 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.41 (IC base=+0.202)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.205 (n=1027)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `11862.3083` → IC=+0.217 (n=529)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11862.3083 (IC base=+0.202)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.147 (n=988)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0071 (IC base=+0.131)

- **PATRÓN** `drift_60min` |x|≤ `0.1103` → IC=+0.150 (n=659)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.1103 (IC base=+0.131)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1405` → IC=+0.132 (n=658)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.66€ cuando `delta_ratio_macro` |x|> 0.1405 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.136 (n=899)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 6.0 (IC base=+0.131)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.133 (n=692)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 11.0 (IC base=+0.131)

- **PATRÓN** `ibs_15` > `0.4943` → IC=+0.217 (n=987)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.4943 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` > `0.1194` → IC=+0.149 (n=620)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.1194 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.889` → IC=+0.275 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.889 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `5997.7147` → IC=+0.171 (n=448)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 5997.7147 (IC base=+0.131)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `ibs_15` > `0.2568` → IC=-0.121 (n=212)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.2568
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=413)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `ibs_15` > `0.5917` → IC=+0.123 (n=1007)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.62€ cuando `ibs_15` > 0.5917 (IC base=+0.053)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` < `0.0254` → IC=+0.167 (n=1342)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0254 (IC base=+0.154)

- **PATRÓN** `sigma_h` > `0.0133` → IC=+0.154 (n=1342)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` > 0.0133 (IC base=+0.154)

- **PATRÓN** `drift_60min` |x|≤ `0.2248` → IC=+0.177 (n=1343)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.2248 (IC base=+0.154)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0986` → IC=+0.216 (n=414)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0986 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.159 (n=1225)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 6.0 (IC base=+0.154)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.158 (n=1190)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 14.0 (IC base=+0.154)

- **PATRÓN** `ibs_15` > `0.5429` → IC=+0.227 (n=1200)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5429 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` > `0.5296` → IC=+0.192 (n=313)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.5296 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.931` → IC=+0.197 (n=216)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 21.931 (IC base=+0.154)

- **PATRÓN** `libro_liquidez` > `2944.984` → IC=+0.199 (n=609)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 2944.984 (IC base=+0.154)

- **PATRÓN** `ibs_15` < `0.1091` → IC=+0.155 (n=1028)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.78€ cuando `ibs_15` < 0.1091 (IC base=+0.068)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` > `0.0053` → IC=+0.389 (n=341)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0053 (IC base=+0.363)

- **PATRÓN** `drift_60min` |x|≤ `0.1117` → IC=+0.365 (n=501)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1117 (IC base=+0.363)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1501` → IC=+0.377 (n=501)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1501 (IC base=+0.363)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1344` → IC=+0.381 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1344 (IC base=+0.363)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.371 (n=792)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.363)

- **PATRÓN** `ibs_15` > `0.7904` → IC=+0.392 (n=751)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7904 (IC base=+0.363)

- **PATRÓN** `dist_vwap_pct` > `0.1534` → IC=+0.380 (n=446)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1534 (IC base=+0.363)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.963` → IC=+0.396 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.963 (IC base=+0.363)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.367 (n=915)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.363)

- **PATRÓN** `libro_liquidez` > `9641.0136` → IC=+0.381 (n=341)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9641.0136 (IC base=+0.363)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `drift_60min` |x|≤ `0.054` → IC=+0.364 (n=123)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.054 (IC base=+0.362)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2196` → IC=+0.376 (n=167)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2196 (IC base=+0.362)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1441` → IC=+0.399 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1441 (IC base=+0.362)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.380 (n=340)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.362)

- **PATRÓN** `ibs_15` > `0.8112` → IC=+0.384 (n=368)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8112 (IC base=+0.362)

- **PATRÓN** `dist_vwap_pct` > `0.3743` → IC=+0.392 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3743 (IC base=+0.362)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.114` → IC=+0.391 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.114 (IC base=+0.362)

- **PATRÓN** `libro_liquidez` > `8119.484` → IC=+0.384 (n=368)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8119.484 (IC base=+0.362)

- **PATRÓN** `ballena_activa_n` < `413.0` → IC=+0.389 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 413.0 (IC base=+0.362)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.368 (n=384)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.363)

- **PATRÓN** `sigma_h` > `0.006` → IC=+0.381 (n=174)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.006 (IC base=+0.363)

- **PATRÓN** `drift_60min` |x|≤ `0.1078` → IC=+0.368 (n=256)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1078 (IC base=+0.363)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1293` → IC=+0.380 (n=256)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1293 (IC base=+0.363)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.296` → IC=+0.373 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.296 (IC base=+0.363)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.368 (n=384)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.363)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.373 (n=179)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.363)

- **PATRÓN** `ibs_15` > `0.7632` → IC=+0.391 (n=384)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7632 (IC base=+0.363)

- **PATRÓN** `dist_vwap_pct` > `0.159` → IC=+0.372 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.159 (IC base=+0.363)

- **PATRÓN** `dist_vwap_pct` < `0.2798` → IC=+0.364 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2798 (IC base=+0.363)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.973` → IC=+0.394 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.973 (IC base=+0.363)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.478` → IC=+0.363 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.478 (IC base=+0.363)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.367 (n=435)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.363)

- **PATRÓN** `libro_liquidez` > `4150.4977` → IC=+0.375 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4150.4977 (IC base=+0.363)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0075` → IC=-0.196 (n=2711)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0075
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=2712)

- **FILTRO** `drift_15min` |x|> `0.9123` → IC=-0.145 (n=1355)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.9123
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=4067)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.218 (n=2285)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=3138)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1398` → IC=+0.215 (n=465)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1398 (IC base=-0.082)

- **PATRÓN** `ibs_15` > `0.6306` → IC=+0.277 (n=1229)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6306 (IC base=-0.082)

- **PATRÓN** `dist_vwap_pct` > `0.1103` → IC=+0.201 (n=720)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1103 (IC base=-0.082)

- **PATRÓN** `dist_vwap_pct` < `0.2595` → IC=+0.198 (n=1052)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` < 0.2595 (IC base=-0.082)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2345` → IC=+0.270 (n=1653)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2345 (IC base=-0.004)

- **PATRÓN** `ibs_15` < `0.3695` → IC=+0.285 (n=4959)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3695 (IC base=-0.004)

- **PATRÓN** `dist_vwap_pct` > `0.6502` → IC=+0.281 (n=679)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6502 (IC base=-0.004)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0321` → IC=-0.221 (n=2578)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0321
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=862)

- **FILTRO** `sigma_h` < `0.0038` → IC=-0.215 (n=860)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0038
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=2580)

- **FILTRO** `sigma_ewma_delta_pct` > `22.129` → IC=-0.257 (n=487)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 22.129
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=2953)

- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.154 (n=330)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0031 (IC base=+0.071)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2674` → IC=+0.286 (n=143)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2674 (IC base=+0.071)

- **PATRÓN** `ibs_15` > `0.7609` → IC=+0.321 (n=429)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7609 (IC base=+0.071)

- **PATRÓN** `dist_vwap_pct` > `0.1039` → IC=+0.278 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1039 (IC base=+0.071)

- **PATRÓN** `dist_vwap_pct` < `0.3658` → IC=+0.284 (n=442)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3658 (IC base=+0.071)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.251` → IC=+0.149 (n=220)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 22.251 (IC base=+0.071)

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
  - _Potencial_: sin este filtro IC_bueno=+0.152 (n=803)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.160 (n=542)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0059 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.0722` → IC=+0.181 (n=271)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.0722 (IC base=+0.146)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3006` → IC=+0.194 (n=482)

  - _Acción_: Kelly boost +0.97€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3006 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.167 (n=283)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 15.0 (IC base=+0.146)

- **PATRÓN** `ibs_15` > `0.5679` → IC=+0.241 (n=615)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5679 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.6245` → IC=+0.158 (n=112)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.6245 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` < `0.2675` → IC=+0.148 (n=575)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.2675 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.001` → IC=+0.256 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.001 (IC base=+0.146)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=803)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `4990.9589` → IC=+0.155 (n=410)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 4990.9589 (IC base=+0.146)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.254 (n=1270)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0061 (IC base=+0.242)

- **PATRÓN** `drift_60min` |x|≤ `0.3545` → IC=+0.247 (n=1676)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3545 (IC base=+0.242)

- **PATRÓN** `drift_15min` |x|≤ `0.7818` → IC=+0.258 (n=1676)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7818 (IC base=+0.242)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2142` → IC=+0.263 (n=863)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2142 (IC base=+0.242)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.248 (n=1359)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.242)

- **PATRÓN** `ibs_15` < `0.1845` → IC=+0.301 (n=1270)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.1845 (IC base=+0.242)

- **PATRÓN** `dist_vwap_pct` > `0.3769` → IC=+0.271 (n=470)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3769 (IC base=+0.242)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.267` → IC=+0.247 (n=744)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.267 (IC base=+0.242)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.198` → IC=+0.247 (n=1990)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.198 (IC base=+0.242)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1851` → IC=-0.267 (n=315)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1851
  - _Potencial_: sin este filtro IC_bueno=-0.178 (n=949)

- **FILTRO** `sigma_h` > `0.0105` → IC=-0.235 (n=429)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0105
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=835)

- **FILTRO** `drift_60min` |x|> `0.1723` → IC=-0.266 (n=429)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1723
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=835)

- **FILTRO** `drift_15min` |x|> `0.9101` → IC=-0.282 (n=315)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.9101
  - _Potencial_: sin este filtro IC_bueno=-0.173 (n=949)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1455` → IC=+0.188 (n=46)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.94€ cuando `delta_ratio_macro` |x|> 0.1455 (IC base=-0.201)

- **PATRÓN** `ibs_15` > `0.5625` → IC=+0.234 (n=62)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5625 (IC base=-0.201)

- **PATRÓN** `dist_vwap_pct` > `0.2752` → IC=+0.143 (n=26)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.2752 (IC base=-0.201)

- **PATRÓN** `dist_vwap_pct` < `0.1292` → IC=+0.154 (n=53)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.1292 (IC base=-0.201)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0642` → IC=+0.237 (n=847)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0642 (IC base=-0.030)

- **PATRÓN** `ibs_15` < `0.381` → IC=+0.295 (n=849)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.381 (IC base=-0.030)

- **PATRÓN** `dist_vwap_pct` > `0.6795` → IC=+0.240 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6795 (IC base=-0.030)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0133` → IC=-0.242 (n=1157)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0133
  - _Potencial_: sin este filtro IC_bueno=-0.139 (n=386)

- **FILTRO** `libro_spread` > `0.04` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.04
  - _Potencial_: sin este filtro IC_bueno=-0.216 (n=1524)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.216)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.216)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1185` → IC=+0.302 (n=514)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1185 (IC base=-0.016)

- **PATRÓN** `ibs_15` < `0.1358` → IC=+0.310 (n=788)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.1358 (IC base=-0.016)

- **PATRÓN** `dist_vwap_pct` > `0.7641` → IC=+0.337 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7641 (IC base=-0.016)

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
- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.300 (n=452)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0033 (IC base=+0.282)

- **PATRÓN** `drift_60min` |x|≤ `0.0722` → IC=+0.313 (n=596)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0722 (IC base=+0.282)

- **PATRÓN** `delta_ratio_macro` |x|> `0.152` → IC=+0.284 (n=902)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.152 (IC base=+0.282)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2224` → IC=+0.290 (n=825)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2224 (IC base=+0.282)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.295 (n=1400)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.282)

- **PATRÓN** `ibs_15` > `0.838` → IC=+0.311 (n=1355)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.838 (IC base=+0.282)

- **PATRÓN** `dist_vwap_pct` > `0.263` → IC=+0.313 (n=586)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.263 (IC base=+0.282)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.932` → IC=+0.387 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.932 (IC base=+0.282)

- **PATRÓN** `libro_liquidez` > `13222.7352` → IC=+0.302 (n=452)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13222.7352 (IC base=+0.282)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.305 (n=239)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.276)

- **PATRÓN** `drift_60min` |x|≤ `0.0587` → IC=+0.309 (n=239)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0587 (IC base=+0.276)

- **PATRÓN** `drift_15min` |x|≤ `0.3843` → IC=+0.276 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3843 (IC base=+0.276)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2699` → IC=+0.279 (n=238)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2699 (IC base=+0.276)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3948` → IC=+0.280 (n=642)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3948 (IC base=+0.276)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.294 (n=749)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.276)

- **PATRÓN** `ibs_15` > `0.829` → IC=+0.301 (n=715)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.829 (IC base=+0.276)

- **PATRÓN** `dist_vwap_pct` > `0.2515` → IC=+0.312 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2515 (IC base=+0.276)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.742` → IC=+0.394 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.742 (IC base=+0.276)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.278 (n=924)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.276)

- **PATRÓN** `libro_liquidez` > `15796.8084` → IC=+0.313 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15796.8084 (IC base=+0.276)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.296 (n=641)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0069 (IC base=+0.289)

- **PATRÓN** `drift_60min` |x|≤ `0.0515` → IC=+0.319 (n=214)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0515 (IC base=+0.289)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0642` → IC=+0.289 (n=639)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0642 (IC base=+0.289)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1008` → IC=+0.321 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1008 (IC base=+0.289)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.301 (n=611)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.289)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.291 (n=453)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.289)

- **PATRÓN** `ibs_15` > `0.8478` → IC=+0.318 (n=639)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8478 (IC base=+0.289)

- **PATRÓN** `dist_vwap_pct` > `0.2798` → IC=+0.315 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2798 (IC base=+0.289)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.243` → IC=+0.372 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.243 (IC base=+0.289)

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

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5789 sube el IC de +0.141 a +0.224 en UPDOWN_GBM#15min (n=4808). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7082 sube el IC de +0.202 a +0.274 en UPDOWN_GBM#BTC#15min (n=793). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.4943 sube el IC de +0.131 a +0.217 en UPDOWN_GBM#ETH#15min (n=987). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5429 sube el IC de +0.154 a +0.227 en UPDOWN_GBM#XRP#15min (n=1200). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1091 sube el IC de +0.068 a +0.155 en UPDOWN_GBM#XRP#15min (n=1028). Ya aplicado como kelly_boost=+0.78€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6306 sube el IC de -0.082 a +0.277 en UPDOWN_GBM_15M_TARDIO (n=1229). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3695 sube el IC de -0.004 a +0.285 en UPDOWN_GBM_15M_TARDIO (n=4959). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7609 sube el IC de +0.071 a +0.321 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=429). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.6255 sube el IC de -0.186 a +0.289 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=74). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.5679 sube el IC de +0.146 a +0.241 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=615). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.1845 sube el IC de +0.242 a +0.301 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=1270). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de -0.201 a +0.234 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=62). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.381 sube el IC de -0.030 a +0.295 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=849). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.216 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.1358 sube el IC de -0.016 a +0.310 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=788). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_YES, IBS > 0.8434 sube el IC de +0.109 a +0.340 en UPDOWN_GBM_ETH_15M_HORA7 (n=23). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_YES, IBS > 0.8434 sube el IC de +0.109 a +0.340 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=23). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.838 sube el IC de +0.282 a +0.311 en UPDOWN_GBM_IBS_ALTO (n=1355). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.829 sube el IC de +0.276 a +0.301 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=715). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8478 sube el IC de +0.289 a +0.318 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=639). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7904 sube el IC de +0.363 a +0.392 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=751). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8112 sube el IC de +0.362 a +0.384 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=368). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7632 sube el IC de +0.363 a +0.391 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=384). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

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
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 1142 | -0.022 | +72.22€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 1142 | -0.022 | +72.22€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE | 7 | +0.019 | +3.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE#15min | 7 | +0.019 | +3.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 879 | -0.038 | +57.42€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 879 | -0.038 | +57.42€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 178 | +0.061 | +18.78€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 178 | +0.061 | +18.78€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 78 | -0.037 | -7.24€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 78 | -0.037 | -7.24€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 47319 | -0.084 | -5995.11€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 2934 | +0.071 | -300.79€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 44385 | -0.094 | -5694.31€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4806 | -0.113 | -802.96€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4806 | -0.113 | -802.96€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 2934 | +0.071 | -300.79€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 2934 | +0.071 | -300.79€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 4877 | -0.106 | -938.87€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 4877 | -0.106 | -938.87€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 12959 | -0.041 | -1188.05€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 12959 | -0.041 | -1188.05€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 12896 | -0.112 | -1334.21€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 12896 | -0.112 | -1334.21€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 8847 | -0.128 | -1430.22€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 8847 | -0.128 | -1430.22€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 49018 | -0.012 | +2851.22€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 12682 | +0.004 | +1519.70€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 36336 | -0.018 | +1331.52€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 49018 | -0.012 | +2851.22€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 12682 | +0.004 | +1519.70€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 36336 | -0.018 | +1331.52€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 188005 | +0.113 | -7810.67€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#15min | 21757 | +0.180 | -715.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 862 | +0.009 | -74.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 154650 | +0.105 | -6615.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 10736 | +0.093 | -405.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 25625 | +0.103 | -1804.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 76 | -0.179 | +10.07€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 25534 | +0.104 | -1802.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 35632 | +0.124 | -616.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5610 | +0.178 | -239.62€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 25601 | +0.120 | -194.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 4379 | +0.080 | -160.38€ | 1 | 2 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 25677 | +0.099 | -1847.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 87 | -0.118 | +5.83€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 25575 | +0.100 | -1841.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 40160 | +0.123 | -856.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 10107 | +0.178 | -251.26€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 26008 | +0.105 | -538.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 4033 | +0.102 | -58.95€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#SOL | 35256 | +0.112 | -1582.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 5788 | +0.198 | -255.89€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 765 | +0.036 | -20.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 26379 | +0.096 | -1120.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 2324 | +0.100 | -185.83€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO#XRP | 25655 | +0.107 | -1103.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 89 | -0.115 | +15.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 25553 | +0.108 | -1118.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 30465 | +0.193 | -2094.87€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 30465 | +0.193 | -2094.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 6901 | +0.170 | -706.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 6901 | +0.170 | -706.54€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 4397 | +0.197 | -161.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 4397 | +0.197 | -161.21€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 6762 | +0.176 | -584.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 6762 | +0.176 | -584.45€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 5673 | +0.251 | -202.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 5673 | +0.251 | -202.36€ | 0 | 4 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 6653 | +0.185 | -454.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 6653 | +0.185 | -454.06€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 1240 | +0.426 | -44.97€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 1240 | +0.426 | -44.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 513 | +0.440 | -3.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 513 | +0.440 | -3.96€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE#15min | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 500 | +0.424 | -18.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 500 | +0.424 | -18.77€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 213 | +0.398 | -18.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 213 | +0.398 | -18.37€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 107788 | +0.200 | -7946.77€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 107788 | +0.200 | -7946.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 18634 | +0.179 | -2118.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 18634 | +0.179 | -2118.64€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 17383 | +0.224 | -574.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 17383 | +0.224 | -574.40€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 18504 | +0.179 | -1979.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 18504 | +0.179 | -1979.06€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 17523 | +0.218 | -704.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 17523 | +0.218 | -704.67€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 17811 | +0.203 | -1121.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 17811 | +0.203 | -1121.48€ | 1 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 17933 | +0.196 | -1448.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 17933 | +0.196 | -1448.52€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 41543 | +0.117 | +342.90€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 41543 | +0.117 | +342.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 20678 | +0.117 | +212.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 20678 | +0.117 | +212.16€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 20865 | +0.116 | +130.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 20865 | +0.116 | +130.74€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 2581 | +0.294 | -7.25€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 2581 | +0.294 | -7.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 1182 | +0.282 | -27.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 1182 | +0.282 | -27.39€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 1260 | +0.298 | +14.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 1260 | +0.298 | +14.88€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 139 | +0.344 | +5.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 139 | +0.344 | +5.25€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 1191 | +0.439 | -3.13€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 1191 | +0.439 | -3.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 572 | +0.432 | -10.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 572 | +0.432 | -10.87€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 568 | +0.446 | +6.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 568 | +0.446 | +6.48€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 51 | +0.406 | +1.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 51 | +0.406 | +1.25€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1940 | +0.068 | -84.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 725 | +0.046 | -64.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 1215 | +0.081 | -20.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1506 | +0.076 | -39.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 291 | +0.053 | -19.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 1215 | +0.081 | -20.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 84199 | +0.101 | -1968.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 6788 | +0.096 | +144.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 77411 | +0.101 | -2112.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 46026 | +0.105 | -444.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 6788 | +0.096 | +144.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 39238 | +0.107 | -589.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 17889 | +0.109 | -103.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 17889 | +0.109 | -103.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 20284 | +0.082 | -1420.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 20284 | +0.082 | -1420.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 914 | +0.186 | -109.27€ | 5 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 914 | +0.186 | -109.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 914 | +0.186 | -109.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 914 | +0.186 | -109.27€ | 5 | 4 |
| ✅ GBM_LATE_15M | 57114 | +0.100 | +31875.62€ | 0 | 17 |
| ✅ GBM_LATE_15M#15min | 57114 | +0.100 | +31875.62€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 9455 | +0.227 | +8212.25€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 9455 | +0.227 | +8212.25€ | 0 | 22 |
| ✅ GBM_LATE_15M#BTC | 8749 | +0.176 | +6867.90€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 8749 | +0.176 | +6867.90€ | 0 | 22 |
| ✅ GBM_LATE_15M#DOGE | 10240 | +0.208 | +8122.47€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 10240 | +0.208 | +8122.47€ | 0 | 21 |
| ✅ GBM_LATE_15M#ETH | 7654 | +0.055 | +2450.90€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 7654 | +0.055 | +2450.90€ | 1 | 16 |
| ✅ GBM_LATE_15M#SOL | 7969 | -0.031 | +2050.00€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 7969 | -0.031 | +2050.00€ | 4 | 14 |
| ✅ GBM_LATE_15M#XRP | 13047 | -0.022 | +4172.09€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 13047 | -0.022 | +4172.09€ | 3 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 60223 | +0.085 | +34899.52€ | 0 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 60223 | +0.085 | +34899.52€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 11642 | -0.002 | +6190.65€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 11642 | -0.002 | +6190.65€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 12951 | +0.004 | +3443.29€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 12951 | +0.004 | +3443.29€ | 0 | 11 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 8191 | +0.295 | +9377.90€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 8191 | +0.295 | +9377.90€ | 0 | 22 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 11492 | +0.013 | +3557.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 11492 | +0.013 | +3557.87€ | 1 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 9240 | +0.043 | +4104.34€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 9240 | +0.043 | +4104.34€ | 3 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 6707 | +0.316 | +8225.46€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 6707 | +0.316 | +8225.46€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 45216 | +0.178 | +37298.76€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 45216 | +0.178 | +37298.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 6805 | +0.240 | +6359.92€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 6805 | +0.240 | +6359.92€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 7166 | +0.138 | +5258.84€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 7166 | +0.138 | +5258.84€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 7273 | +0.225 | +6328.17€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 7273 | +0.225 | +6328.17€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 7749 | +0.129 | +6010.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 7749 | +0.129 | +6010.12€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 8558 | +0.118 | +6390.61€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 8558 | +0.118 | +6390.61€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 7665 | +0.233 | +6951.10€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 7665 | +0.233 | +6951.10€ | 0 | 24 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 12289 | +0.125 | +6137.81€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 12289 | +0.125 | +6137.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 534 | +0.168 | +370.03€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 534 | +0.168 | +370.03€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 3411 | +0.127 | +1857.49€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 3411 | +0.127 | +1857.49€ | 0 | 13 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 506 | +0.158 | +277.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 506 | +0.158 | +277.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 3571 | +0.123 | +1689.09€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 3571 | +0.123 | +1689.09€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 3215 | +0.099 | +1295.09€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 3215 | +0.099 | +1295.09€ | 0 | 13 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 1052 | +0.166 | +648.66€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 1052 | +0.166 | +648.66€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO | 57299 | +0.188 | +47177.36€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#15min | 57299 | +0.188 | +47177.36€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 9038 | +0.252 | +8801.56€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 9038 | +0.252 | +8801.56€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 9113 | +0.137 | +6273.74€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 9113 | +0.137 | +6273.74€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 9721 | +0.236 | +8844.17€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 9721 | +0.236 | +8844.17€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 9478 | +0.142 | +7014.43€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 9478 | +0.142 | +7014.43€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 10177 | +0.121 | +7143.29€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 10177 | +0.121 | +7143.29€ | 0 | 18 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 9772 | +0.241 | +9100.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 9772 | +0.241 | +9100.16€ | 0 | 20 |
| ✅ GBM_LATE_5M | 14477 | +0.212 | +11831.19€ | 1 | 26 |
| ✅ GBM_LATE_5M#5min | 14477 | +0.212 | +11831.19€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 1093 | +0.248 | +1044.52€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 1093 | +0.248 | +1044.52€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 3266 | +0.211 | +2814.84€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 3266 | +0.211 | +2814.84€ | 0 | 27 |
| ✅ GBM_LATE_5M#DOGE | 1453 | +0.210 | +1160.11€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1453 | +0.210 | +1160.11€ | 0 | 19 |
| ✅ GBM_LATE_5M#ETH | 4295 | +0.204 | +3225.98€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 4295 | +0.204 | +3225.98€ | 0 | 24 |
| ✅ GBM_LATE_5M#SOL | 2379 | +0.215 | +2017.80€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 2379 | +0.215 | +2017.80€ | 0 | 26 |
| ✅ GBM_LATE_5M#XRP | 1991 | +0.210 | +1567.94€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1991 | +0.210 | +1567.94€ | 0 | 0 |
| ✅ GBM_LATE_60M | 5075 | +0.052 | +1392.06€ | 1 | 5 |
| ✅ GBM_LATE_60M#60min | 5075 | +0.052 | +1392.06€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 1763 | +0.059 | +540.39€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 1763 | +0.059 | +540.39€ | 0 | 6 |
| ✅ GBM_LATE_60M#ETH | 1627 | +0.052 | +520.91€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 1627 | +0.052 | +520.91€ | 1 | 6 |
| ✅ GBM_LATE_60M#SOL | 1685 | +0.044 | +330.76€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 1685 | +0.044 | +330.76€ | 0 | 8 |
| 🚫 GBM_LATE_60M_FADE | 713 | -0.250 | -34.37€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 713 | -0.250 | -34.37€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 258 | -0.250 | -18.00€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 258 | -0.250 | -18.00€ | 5 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 261 | -0.245 | -7.56€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 261 | -0.245 | -7.56€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 194 | -0.250 | -8.81€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 194 | -0.250 | -8.81€ | 8 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 2115 | +0.083 | +536.20€ | 0 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 2115 | +0.083 | +536.20€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 816 | +0.070 | +187.86€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 816 | +0.070 | +187.86€ | 1 | 4 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 749 | +0.058 | +145.65€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 749 | +0.058 | +145.65€ | 1 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 550 | +0.138 | +202.69€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 550 | +0.138 | +202.69€ | 1 | 9 |
| ✅ LATE_WINDOW_5MIN | 244 | +0.297 | +277.58€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 244 | +0.297 | +277.58€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 244 | +0.297 | +277.58€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 244 | +0.297 | +277.58€ | 1 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 4396 | +0.097 | +1002.00€ | 0 | 1 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 4396 | +0.097 | +1002.00€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 4396 | +0.097 | +1002.00€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 4396 | +0.097 | +1002.00€ | 0 | 1 |
| ✅ LIQUIDACIONES_15M | 1151 | -0.004 | +19.78€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 1151 | -0.004 | +19.78€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 73 | +0.007 | -0.80€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 73 | +0.007 | -0.80€ | 0 | 1 |
| ✅ LIQUIDACIONES_15M#BTC | 280 | -0.007 | +7.69€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 280 | -0.007 | +7.69€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 53 | -0.045 | -3.59€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 53 | -0.045 | -3.59€ | 0 | 1 |
| ✅ LIQUIDACIONES_15M#ETH | 298 | +0.020 | +18.58€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 298 | +0.020 | +18.58€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 317 | -0.017 | +0.08€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 317 | -0.017 | +0.08€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 130 | -0.008 | -2.18€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 130 | -0.008 | -2.18€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 4198 | +0.017 | +127.01€ | 5 | 1 |
| ✅ LIQUIDACIONES_5M#5min | 4198 | +0.017 | +127.01€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 215 | +0.025 | -0.90€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 215 | +0.025 | -0.90€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 827 | +0.015 | +40.58€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 827 | +0.015 | +40.58€ | 1 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 251 | +0.026 | +25.87€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 251 | +0.026 | +25.87€ | 0 | 7 |
| ✅ LIQUIDACIONES_5M#ETH | 1658 | +0.020 | +29.99€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1658 | +0.020 | +29.99€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 769 | +0.011 | +1.89€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 769 | +0.011 | +1.89€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 478 | +0.015 | +29.59€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 478 | +0.015 | +29.59€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 2380 | -0.033 | -8.86€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 2380 | -0.033 | -8.86€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 721 | -0.031 | -11.19€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 721 | -0.031 | -11.19€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 845 | -0.011 | +16.55€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 845 | -0.011 | +16.55€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 814 | -0.058 | -14.22€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 814 | -0.058 | -14.22€ | 5 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 15552 | -0.031 | -121.71€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 7482 | -0.033 | -78.18€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 8070 | -0.030 | -43.53€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 541 | -0.054 | -32.02€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 278 | -0.029 | +0.26€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 263 | -0.081 | -32.28€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 4077 | -0.025 | -9.47€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 1938 | -0.024 | +5.37€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 2139 | -0.026 | -14.84€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 1511 | -0.029 | +16.37€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 775 | -0.034 | -0.76€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 736 | -0.023 | +17.12€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 3510 | -0.035 | -63.24€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 1663 | -0.037 | -38.32€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 1847 | -0.033 | -24.92€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 2994 | -0.022 | +51.04€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 1451 | -0.027 | +6.95€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 1543 | -0.017 | +44.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 2919 | -0.043 | -84.39€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 1377 | -0.050 | -51.68€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 1542 | -0.038 | -32.70€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 67788 | -0.000 | +3605.08€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 67788 | -0.000 | +3605.08€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 12289 | +0.027 | +1670.08€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 12289 | +0.027 | +1670.08€ | 2 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 9467 | -0.037 | -129.41€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 9467 | -0.037 | -129.41€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 12429 | +0.025 | +1374.62€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 12429 | +0.025 | +1374.62€ | 1 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 9407 | -0.052 | -246.74€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 9407 | -0.052 | -246.74€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 11559 | -0.004 | +323.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 11559 | -0.004 | +323.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 12637 | +0.017 | +612.66€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 12637 | +0.017 | +612.66€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 7168 | -0.055 | -117.96€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 7168 | -0.055 | -117.96€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1247 | -0.002 | -15.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1247 | -0.002 | -15.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1987 | -0.064 | -25.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1987 | -0.064 | -25.60€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 79 | -0.018 | -0.18€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 79 | -0.018 | -0.18€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 809 | -0.120 | -35.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 809 | -0.120 | -35.98€ | 5 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 2183 | -0.068 | -13.48€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 2183 | -0.068 | -13.48€ | 2 | 0 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 166054 | -0.078 | +2210.11€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 166054 | -0.078 | +2210.11€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 29093 | -0.078 | +1783.09€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 29093 | -0.078 | +1783.09€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 24811 | -0.102 | -1276.69€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 24811 | -0.102 | -1276.69€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 29467 | -0.068 | +1412.86€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 29467 | -0.068 | +1412.86€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 24358 | -0.099 | -775.82€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 24358 | -0.099 | -775.82€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 29665 | -0.059 | +269.83€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 29665 | -0.059 | +269.83€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 28660 | -0.070 | +796.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 28660 | -0.070 | +796.85€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 9061 | -0.035 | -182.57€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 9061 | -0.035 | -182.57€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 1008 | -0.017 | -19.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 1008 | -0.017 | -19.32€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 2112 | -0.047 | -28.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 2112 | -0.047 | -28.71€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2646 | -0.025 | -36.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2646 | -0.025 | -36.71€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1272 | -0.064 | -32.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1272 | -0.064 | -32.38€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 1014 | -0.032 | -33.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 1014 | -0.032 | -33.50€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 2163 | +0.120 | +860.52€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#5min | 2027 | +0.124 | +847.93€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 481 | +0.134 | +233.57€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 481 | +0.134 | +233.57€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#DOGE | 414 | +0.118 | +144.56€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 414 | +0.118 | +144.56€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#ETH | 381 | +0.124 | +169.10€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 381 | +0.124 | +169.10€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 345 | +0.143 | +179.09€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 345 | +0.143 | +179.09€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#XRP | 406 | +0.101 | +121.61€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 406 | +0.101 | +121.61€ | 0 | 2 |
| ✅ ORDER_FLOW_5M_REACTIVO | 2189 | -0.016 | -17.72€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 2189 | -0.016 | -17.72€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 398 | +0.015 | +26.81€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 398 | +0.015 | +26.81€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 402 | -0.042 | -25.08€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 402 | -0.042 | -25.08€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 553 | -0.037 | -29.12€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 553 | -0.037 | -29.12€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 444 | +0.002 | +4.26€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 444 | +0.002 | +4.26€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 392 | -0.010 | +5.40€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 392 | -0.010 | +5.40€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 1157 | -0.068 | -24.76€ | 3 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 535 | -0.103 | -69.04€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 414 | -0.115 | -48.49€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 121 | -0.061 | -20.55€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 404 | -0.027 | +30.89€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 289 | -0.012 | +38.89€ | 2 | 2 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 115 | -0.064 | -8.00€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 218 | -0.054 | +13.39€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 182 | -0.049 | +11.56€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 36 | -0.079 | +1.84€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 885 | -0.068 | +1.96€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 272 | -0.066 | -26.71€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 1461 | -0.203 | -85.53€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 577 | -0.200 | -46.21€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 507 | -0.197 | -41.75€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#reach | 70 | -0.208 | -4.45€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 488 | -0.208 | -37.50€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 426 | -0.220 | -44.65€ | 3 | 1 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 62 | -0.125 | +7.14€ | 3 | 0 |
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
| ✅ STREAK_FADE_15M | 948 | +0.042 | +81.60€ | 2 | 2 |
| ✅ STREAK_FADE_15M#15min | 948 | +0.042 | +81.60€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 356 | +0.020 | +3.92€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 356 | +0.020 | +3.92€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 74 | +0.026 | +3.13€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 74 | +0.026 | +3.13€ | 1 | 1 |
| ✅ STREAK_FADE_15M#SOL | 83 | +0.018 | +6.06€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 83 | +0.018 | +6.06€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 435 | +0.068 | +68.50€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 435 | +0.068 | +68.50€ | 1 | 3 |
| ✅ STREAK_FADE_5M | 3576 | -0.024 | -144.02€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3576 | -0.024 | -144.02€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 1127 | -0.023 | -40.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 1127 | -0.023 | -40.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 615 | -0.030 | -28.21€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 615 | -0.030 | -28.21€ | 2 | 0 |
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
| ✅ STREAK_MOM_5M | 11516 | +0.014 | +73.42€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 11516 | +0.014 | +73.42€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2995 | +0.018 | +24.38€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2995 | +0.018 | +24.38€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 3013 | +0.016 | +32.90€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 3013 | +0.016 | +32.90€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2927 | +0.009 | -2.09€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2927 | +0.009 | -2.09€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2581 | +0.014 | +18.23€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2581 | +0.014 | +18.23€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 12050 | +0.018 | -7.02€ | 4 | 0 |
| ✅ STRUCT_NO_15M#15min | 12050 | +0.018 | -7.02€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 5012 | +0.021 | +4.74€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 5012 | +0.021 | +4.74€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 4144 | +0.016 | -8.67€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 4144 | +0.016 | -8.67€ | 4 | 0 |
| ✅ STRUCT_NO_15M#SOL | 2894 | +0.014 | -3.09€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 2894 | +0.014 | -3.09€ | 1 | 0 |
| ✅ UPDOWN_GBM | 107035 | +0.060 | +10214.74€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 26088 | +0.079 | +5269.99€ | 0 | 10 |
| ✅ UPDOWN_GBM#240min | 3161 | -0.000 | +35.34€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 71077 | +0.062 | +4800.12€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 6343 | -0.001 | +114.32€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 8853 | +0.105 | +1631.16€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1781 | +0.164 | +820.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 90 | -0.011 | -2.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 6982 | +0.091 | +812.96€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 24431 | +0.057 | +2162.18€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 3490 | +0.079 | +781.59€ | 0 | 9 |
| ✅ UPDOWN_GBM#BTC#240min | 902 | +0.000 | +18.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 17071 | +0.067 | +1284.66€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 2835 | -0.004 | +73.55€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 133 | -0.063 | +4.24€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 11637 | +0.079 | +1333.69€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1761 | +0.154 | +738.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 86 | +0.023 | -0.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 9790 | +0.065 | +596.11€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 25436 | +0.050 | +1797.28€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 6156 | +0.072 | +946.04€ | 0 | 9 |
| ✅ UPDOWN_GBM#ETH#240min | 871 | +0.005 | +16.66€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 15955 | +0.052 | +795.92€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 2332 | +0.001 | +37.44€ | 1 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 122 | -0.105 | +1.22€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 22737 | +0.040 | +1282.06€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 7001 | +0.031 | +424.76€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#240min | 815 | -0.010 | +5.02€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 13636 | +0.052 | +857.60€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 1176 | +0.000 | +3.34€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#daily | 109 | -0.140 | -8.66€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 13939 | +0.073 | +2010.20€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 5899 | +0.094 | +1558.96€ | 0 | 11 |
| ✅ UPDOWN_GBM#XRP#240min | 397 | +0.006 | -1.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 7643 | +0.060 | +452.86€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 364 | -0.101 | -3.19€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 1001 | +0.363 | +366.68€ | 0 | 10 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 1001 | +0.363 | +366.68€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 490 | +0.362 | +171.09€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 490 | +0.362 | +171.09€ | 0 | 9 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 511 | +0.363 | +195.59€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 511 | +0.363 | +195.59€ | 0 | 14 |
| ✅ UPDOWN_GBM_15M_TARDIO | 25502 | -0.021 | +6321.29€ | 3 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 25502 | -0.021 | +6321.29€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1981 | -0.051 | +561.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1981 | -0.051 | +561.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 4756 | -0.115 | +239.96€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 4756 | -0.115 | +239.96€ | 3 | 11 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 1071 | +0.222 | +899.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 1071 | +0.222 | +899.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 3358 | +0.219 | +2143.74€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 3358 | +0.219 | +2143.74€ | 1 | 19 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 7236 | -0.060 | +1067.74€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 7236 | -0.060 | +1067.74€ | 4 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 7100 | -0.059 | +1408.80€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 7100 | -0.059 | +1408.80€ | 2 | 5 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 312 | +0.060 | +27.61€ | 0 | 10 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 312 | +0.060 | +27.61€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 312 | +0.060 | +27.61€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 312 | +0.060 | +27.61€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1805 | +0.282 | +1517.87€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1805 | +0.282 | +1517.87€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 953 | +0.276 | +748.68€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 953 | +0.276 | +748.68€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 852 | +0.289 | +769.19€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 852 | +0.289 | +769.19€ | 0 | 9 |
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
| ✅ WEEKLY_PRICE | 4702 | +0.300 | +2113.75€ | 0 | 3 |
| ✅ WEEKLY_PRICE#BTC | 1796 | +0.256 | +226.16€ | 0 | 3 |
| ✅ WEEKLY_PRICE#ETH | 1814 | +0.295 | +770.40€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 1092 | +0.381 | +1117.20€ | 0 | 1 |