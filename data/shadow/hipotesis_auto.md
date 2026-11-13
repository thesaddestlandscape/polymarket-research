# Hipótesis automáticas — 2026-11-13 04:13 UTC
_Generado por shadow_postmortem.py sobre 1312398 resoluciones (PNL=+180470.06€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.5` → IC=-0.317 (n=195)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.118 (n=699)

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

- **PATRÓN** `py_entrada` > `0.495` → IC=+0.173 (n=47)

  - _Acción_: Kelly boost +0.87€ cuando `py_entrada` > 0.495 (IC base=+0.167)

- **PATRÓN** `n_ballena_banda` > `26.0` → IC=+0.231 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `n_ballena_banda` > 26.0 (IC base=+0.167)

- **PATRÓN** `n_total_lado` > `38.0` → IC=+0.250 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 38.0 (IC base=+0.167)

- **PATRÓN** `banda_hit_calibrado` > `0.6072` → IC=+0.180 (n=23)

  - _Acción_: Kelly boost +0.90€ cuando `banda_hit_calibrado` > 0.6072 (IC base=+0.167)

- **PATRÓN** `banda_z` > `2.495` → IC=+0.236 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 2.495 (IC base=+0.167)

- **PATRÓN** `ballenas_wallet_edge_medio` > `0.729` → IC=+0.167 (n=43)

  - _Acción_: Kelly boost +0.83€ cuando `ballenas_wallet_edge_medio` > 0.729 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `13.0` → IC=+0.278 (n=25)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 13.0 (IC base=+0.167)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.214 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.167)

- **PATRÓN** `libro_liquidez` > `2464.8952` → IC=+0.202 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2464.8952 (IC base=+0.167)

### BALLENAS_TARDIAS
- **FILTRO** `restante_s_al_confirmar` < `132.04` → IC=-0.220 (n=11961)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 132.04
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=35886)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `125.12` → IC=-0.259 (n=1207)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 125.12
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=3623)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `116.46` → IC=-0.287 (n=1219)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 116.46
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=3658)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `restante_s_al_confirmar` < `116.47` → IC=-0.168 (n=3287)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 116.47
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=9863)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `152.03` → IC=-0.240 (n=3253)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 152.03
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=9762)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `128.65` → IC=-0.265 (n=2246)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 128.65
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=6741)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.209 (n=28133)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.103)

- **PATRÓN** `libro_liquidez` > `8239.3149` → IC=+0.158 (n=2341)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 8239.3149 (IC base=+0.103)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.128 (n=24327)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 17.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.131 (n=29520)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.124)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.225 (n=22200)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.140 (n=8371)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `6476.832` → IC=+0.143 (n=3240)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 6476.832 (IC base=+0.124)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.185 (n=2197)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.177)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.358 (n=751)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.177)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.180 (n=2689)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.01 (IC base=+0.177)

- **PATRÓN** `libro_liquidez` > `9412.9736` → IC=+0.180 (n=1870)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 9412.9736 (IC base=+0.177)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.185 (n=1911)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 7.0 (IC base=+0.178)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.181 (n=2138)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 17.0 (IC base=+0.178)

- **PATRÓN** `py_entrada` < `0.295` → IC=+0.312 (n=981)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.295 (IC base=+0.178)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.180 (n=2739)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.01 (IC base=+0.178)

- **PATRÓN** `libro_liquidez` > `16075.8828` → IC=+0.184 (n=707)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 16075.8828 (IC base=+0.178)

### FAVORITO_CONFIRMADO#BTC#60min
- **FILTRO** `py_entrada` < `0.55` → IC=-0.335 (n=95)

  - _Acción_: SKIP cuando `py_entrada` < 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.094 (n=2231)

- **PATRÓN** `py_entrada` > `0.61` → IC=+0.167 (n=613)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` > 0.61 (IC base=+0.076)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.146 (n=1437)

  - _Acción_: Kelly boost +0.73€ cuando `py_entrada` < 0.44 (IC base=+0.084)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.169 (n=5083)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 6.0 (IC base=+0.166)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.171 (n=4522)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 15.0 (IC base=+0.166)

- **PATRÓN** `py_entrada` > `0.77` → IC=+0.374 (n=1768)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.77 (IC base=+0.166)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.208 (n=2430)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.202)

- **PATRÓN** `py_entrada` < `0.275` → IC=+0.331 (n=953)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.275 (IC base=+0.202)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.205 (n=2833)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.202)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.141 (n=653)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 15.0 (IC base=+0.140)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.144 (n=1170)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 15.0 (IC base=+0.140)

- **PATRÓN** `py_entrada` > `0.675` → IC=+0.252 (n=445)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.675 (IC base=+0.140)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.142 (n=1118)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.156 (n=155)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.074)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.251 (n=956)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.227)

- **PATRÓN** `py_entrada` > `0.83` → IC=+0.420 (n=1330)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.83 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.146 (n=1429)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 7.0 (IC base=+0.146)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.157 (n=735)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 7.0 (IC base=+0.146)

- **PATRÓN** `py_entrada` < `0.345` → IC=+0.278 (n=717)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.345 (IC base=+0.146)

### FAVORITO_CONFIRMADO#SOL#60min
- **FILTRO** `libro_liquidez` < `955.8819` → IC=-0.121 (n=159)

  - _Acción_: SKIP cuando `libro_liquidez` < 955.8819
  - _Potencial_: sin este filtro IC_bueno=+0.066 (n=323)

- **PATRÓN** `py_entrada` > `0.55` → IC=+0.165 (n=463)

  - _Acción_: Kelly boost +0.82€ cuando `py_entrada` > 0.55 (IC base=+0.047)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.145 (n=483)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 17.0 (IC base=+0.123)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.248 (n=439)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.123)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `10.0` → IC=-0.297 (n=72)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.231 (n=154)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.201 (n=24293)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.195)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.197 (n=20499)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 15.0 (IC base=+0.195)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.229 (n=7693)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.195)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.338 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.195)

- **PATRÓN** `libro_liquidez` > `4915.142` → IC=+0.338 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4915.142 (IC base=+0.195)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.173 (n=5540)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 5.0 (IC base=+0.169)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.179 (n=5511)

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

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.211 (n=3304)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.208)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.210 (n=2922)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.208)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.249 (n=1637)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.208)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.183 (n=5418)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.177 (n=4593)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 15.0 (IC base=+0.176)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.177 (n=5568)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` < 0.73 (IC base=+0.176)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.184 (n=4253)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` > 0.71 (IC base=+0.176)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.257 (n=4549)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.250)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.252 (n=3841)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.250)

- **PATRÓN** `py_entrada` > `0.8` → IC=+0.363 (n=1463)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.191 (n=5312)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.187)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.190 (n=4494)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 15.0 (IC base=+0.187)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.197 (n=1780)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` > 0.73 (IC base=+0.187)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.429 (n=975)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.425)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.427 (n=966)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.425)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.437 (n=982)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.425)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.431 (n=1039)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.425)

- **PATRÓN** `libro_liquidez` > `4630.8744` → IC=+0.441 (n=627)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4630.8744 (IC base=+0.425)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.440 (n=395)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.439)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.441 (n=405)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.439)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.447 (n=434)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.439)

- **PATRÓN** `libro_liquidez` > `12497.2329` → IC=+0.443 (n=349)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12497.2329 (IC base=+0.439)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.430 (n=386)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.423)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.427 (n=382)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.423)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.443 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.423)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.429 (n=434)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.423)

- **PATRÓN** `libro_liquidez` > `4796.5955` → IC=+0.430 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4796.5955 (IC base=+0.423)

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
  - _Potencial_: sin este filtro IC_bueno=-0.263 (n=36)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.257 (n=35)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.209 (n=27414)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.239 (n=32093)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.199)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.186 (n=4768)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 18.0 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.178 (n=10177)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 12.0 (IC base=+0.177)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.188 (n=14645)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` > 0.71 (IC base=+0.177)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.226 (n=13306)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.224)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.285 (n=4490)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.224)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.183 (n=13343)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 7.0 (IC base=+0.179)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.197 (n=11298)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` > 0.72 (IC base=+0.179)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.835` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.835
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=8)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.228 (n=4471)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.219)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.221 (n=5110)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.219)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.254 (n=7368)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.219)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **FILTRO** `hora_utc` > `3.0` → IC=-0.278 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.214 (n=4531)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.204)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.256 (n=4634)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.204)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.202 (n=5312)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.197 (n=5278)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 6.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.244 (n=5494)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.196)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.194 (n=11484)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.141 (n=12124)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `3.42` → IC=+0.139 (n=13982)

  - _Acción_: Kelly boost +0.70€ cuando `lag_apertura_s` < 3.42 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.194 (n=5599)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.118)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.144 (n=5478)

  - _Acción_: Kelly boost +0.72€ cuando `restante_min` > 4.96 (IC base=+0.118)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.125 (n=7025)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 7.0 (IC base=+0.118)

- **PATRÓN** `lag_apertura_s` < `4.11` → IC=+0.142 (n=6956)

  - _Acción_: Kelly boost +0.71€ cuando `lag_apertura_s` < 4.11 (IC base=+0.118)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.194 (n=5885)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.138 (n=7377)

  - _Acción_: Kelly boost +0.69€ cuando `restante_min` > 4.95 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `3.11` → IC=+0.138 (n=7018)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 3.11 (IC base=+0.116)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.305 (n=1407)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.292)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.291 (n=1739)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.292)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.385 (n=721)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.292)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.284 (n=943)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.280)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.366 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.280)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.315 (n=684)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.295)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.299 (n=999)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.295)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.390 (n=343)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.295)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.439 (n=953)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.436)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.443 (n=922)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.436)

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
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.448 (n=307)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.440)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.439 (n=390)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.440)

- **PATRÓN** `py_entrada` > `0.91` → IC=+0.443 (n=455)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.91 (IC base=+0.440)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4805` → IC=+0.140 (n=18039)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.4805 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.128 (n=18241)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 6.0 (IC base=+0.123)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.126 (n=12544)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 12.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` > `0.9767` → IC=+0.246 (n=6013)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9767 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` > `0.8004` → IC=+0.283 (n=980)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8004 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.477` → IC=+0.187 (n=9037)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 3.477 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` > `0.6261` → IC=+0.266 (n=5427)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6261 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` > `0.3041` → IC=+0.249 (n=1865)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3041 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` > `2.7506` → IC=+0.235 (n=4332)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7506 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.132 (n=14330)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.02 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `4653.8788` → IC=+0.149 (n=6013)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 4653.8788 (IC base=+0.123)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.123 (n=11298)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0063 (IC base=+0.085)

- **PATRÓN** `ibs_20min` < `0.5641` → IC=+0.145 (n=22594)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.5641 (IC base=+0.085)

- **PATRÓN** `dist_vwap_pct` > `0.6217` → IC=+0.190 (n=1473)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.6217 (IC base=+0.085)

- **PATRÓN** `volumen_regimen` < `0.8613` → IC=+0.197 (n=6185)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 0.8613 (IC base=+0.085)

- **PATRÓN** `volumen_pendiente_norm` > `0.2959` → IC=+0.234 (n=2276)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2959 (IC base=+0.085)

- **PATRÓN** `volumen_spike_ratio` > `2.6721` → IC=+0.214 (n=5245)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6721 (IC base=+0.085)

- **PATRÓN** `ballena_activa_n` < `99.0` → IC=+0.230 (n=15645)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 99.0 (IC base=+0.085)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `drift_60min` |x|≤ `0.3665` → IC=+0.212 (n=3838)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3665 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.227 (n=1868)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.211)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.211 (n=2570)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` > `0.9857` → IC=+0.278 (n=1741)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9857 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.435` → IC=+0.278 (n=1710)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.435 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.2339` → IC=+0.254 (n=681)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2339 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `1.4382` → IC=+0.212 (n=3681)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4382 (IC base=+0.211)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.224 (n=4249)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `2035.4776` → IC=+0.213 (n=1280)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2035.4776 (IC base=+0.211)

- **PATRÓN** `ballena_activa_n` < `26.0` → IC=+0.224 (n=3506)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 26.0 (IC base=+0.211)

- **PATRÓN** `sigma_h` > `0.0093` → IC=+0.245 (n=1545)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0093 (IC base=+0.244)

- **PATRÓN** `drift_60min` |x|≤ `0.0897` → IC=+0.281 (n=1133)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0897 (IC base=+0.244)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.248 (n=1274)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.244)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.250 (n=1567)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.244)

- **PATRÓN** `ibs_20min` < `0.5664` → IC=+0.261 (n=3398)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5664 (IC base=+0.244)

- **PATRÓN** `volumen_pendiente_norm` < `0.0949` → IC=+0.247 (n=3077)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0949 (IC base=+0.244)

- **PATRÓN** `volumen_pendiente_norm` > `0.289` → IC=+0.251 (n=455)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.289 (IC base=+0.244)

- **PATRÓN** `volumen_spike_ratio` < `1.4471` → IC=+0.247 (n=1083)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4471 (IC base=+0.244)

- **PATRÓN** `volumen_spike_ratio` > `1.8591` → IC=+0.247 (n=2165)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8591 (IC base=+0.244)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.245 (n=3925)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.244)

- **PATRÓN** `libro_liquidez` > `1773.097` → IC=+0.252 (n=2266)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1773.097 (IC base=+0.244)

- **PATRÓN** `ballena_activa_n` < `6.0` → IC=+0.245 (n=1157)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 6.0 (IC base=+0.244)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.236 (n=1084)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.224)

- **PATRÓN** `drift_60min` |x|≤ `0.1096` → IC=+0.251 (n=1424)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1096 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.235 (n=3388)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.226 (n=2297)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` > `0.901` → IC=+0.257 (n=1080)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.901 (IC base=+0.224)

- **PATRÓN** `dist_vwap_pct` > `0.186` → IC=+0.234 (n=1447)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.186 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.797` → IC=+0.264 (n=473)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.797 (IC base=+0.224)

- **PATRÓN** `volumen_regimen` > `0.629` → IC=+0.230 (n=3236)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.629 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` > `0.2783` → IC=+0.266 (n=447)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2783 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` > `2.4483` → IC=+0.248 (n=1065)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4483 (IC base=+0.224)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.153 (n=3486)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0065 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.0779` → IC=+0.158 (n=1160)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.0779 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.154 (n=1304)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 17.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` < `0.353` → IC=+0.204 (n=2320)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.353 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.97` → IC=+0.140 (n=3175)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` < 3.97 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `0.6334` → IC=+0.156 (n=1160)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.6334 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` > `0.0718` → IC=+0.156 (n=1421)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` > 0.0718 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` < `2.4423` → IC=+0.143 (n=3351)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.4423 (IC base=+0.133)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.133 (n=4517)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.133)

- **PATRÓN** `ballena_activa_n` < `175.0` → IC=+0.189 (n=1112)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 175.0 (IC base=+0.133)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0127` → IC=+0.214 (n=1356)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0127 (IC base=+0.196)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.204 (n=4272)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.196)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.260 (n=1584)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.196)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.975` → IC=+0.281 (n=895)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.975 (IC base=+0.196)

- **PATRÓN** `volumen_pendiente_norm` < `0.0971` → IC=+0.198 (n=3646)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` < 0.0971 (IC base=+0.196)

- **PATRÓN** `volumen_pendiente_norm` > `0.3519` → IC=+0.227 (n=526)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3519 (IC base=+0.196)

- **PATRÓN** `volumen_spike_ratio` > `2.7279` → IC=+0.214 (n=1802)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7279 (IC base=+0.196)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.200 (n=4922)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.196)

- **PATRÓN** `libro_liquidez` > `2011.3986` → IC=+0.203 (n=1356)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2011.3986 (IC base=+0.196)

- **PATRÓN** `sigma_h` < `0.0111` → IC=+0.225 (n=3319)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0111 (IC base=+0.222)

- **PATRÓN** `drift_60min` |x|≤ `0.2929` → IC=+0.234 (n=2512)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2929 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.241 (n=1435)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.227 (n=1712)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` < `0.0488` → IC=+0.268 (n=1259)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0488 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.768` → IC=+0.260 (n=406)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.768 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` > `0.3473` → IC=+0.257 (n=549)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3473 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` < `1.7633` → IC=+0.220 (n=1596)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7633 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` > `2.1568` → IC=+0.230 (n=2417)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1568 (IC base=+0.222)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.223 (n=1905)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.222)

- **PATRÓN** `libro_liquidez` > `1881.0184` → IC=+0.226 (n=1708)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1881.0184 (IC base=+0.222)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.227 (n=3598)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 24.0 (IC base=+0.222)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.174 (n=213)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=4905)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.150 (n=672)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0039 (IC base=+0.061)

- **PATRÓN** `ibs_20min` > `0.9409` → IC=+0.235 (n=669)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9409 (IC base=+0.061)

- **PATRÓN** `dist_vwap_pct` > `0.1402` → IC=+0.340 (n=461)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1402 (IC base=+0.061)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.1` → IC=+0.205 (n=1470)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.1 (IC base=+0.061)

- **PATRÓN** `volumen_regimen` > `1.1075` → IC=+0.355 (n=364)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1075 (IC base=+0.061)

- **PATRÓN** `volumen_pendiente_norm` < `0.1678` → IC=+0.339 (n=649)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1678 (IC base=+0.061)

- **PATRÓN** `volumen_pendiente_norm` > `0.3061` → IC=+0.339 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3061 (IC base=+0.061)

- **PATRÓN** `volumen_spike_ratio` < `1.5458` → IC=+0.350 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5458 (IC base=+0.061)

- **PATRÓN** `volumen_spike_ratio` > `2.2962` → IC=+0.343 (n=355)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2962 (IC base=+0.061)

- **PATRÓN** `ballena_activa_n` < `142.0` → IC=+0.341 (n=797)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 142.0 (IC base=+0.061)

- **PATRÓN** `ibs_20min` < `0.0868` → IC=+0.190 (n=1280)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.0868 (IC base=+0.055)

- **PATRÓN** `dist_vwap_pct` > `0.3396` → IC=+0.161 (n=615)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 0.3396 (IC base=+0.055)

- **PATRÓN** `volumen_regimen` < `0.8329` → IC=+0.167 (n=1645)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 0.8329 (IC base=+0.055)

- **PATRÓN** `volumen_pendiente_norm` > `0.2807` → IC=+0.212 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2807 (IC base=+0.055)

- **PATRÓN** `volumen_spike_ratio` < `1.77` → IC=+0.158 (n=1585)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.77 (IC base=+0.055)

- **PATRÓN** `volumen_spike_ratio` > `1.5065` → IC=+0.162 (n=2122)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.5065 (IC base=+0.055)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.176 (n=146)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=783)

- **FILTRO** `ibs_20min` < `0.2667` → IC=-0.178 (n=231)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2667
  - _Potencial_: sin este filtro IC_bueno=+0.086 (n=698)

- **FILTRO** `ibs_20min` > `0.2` → IC=-0.131 (n=4799)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2
  - _Potencial_: sin este filtro IC_bueno=+0.155 (n=2401)

- **FILTRO** `sigma_ewma_delta_pct` > `8.306` → IC=-0.229 (n=777)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.306
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=6423)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.179 (n=319)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.75 (IC base=+0.020)

- **PATRÓN** `dist_vwap_pct` > `0.9668` → IC=+0.283 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9668 (IC base=+0.020)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.888` → IC=+0.158 (n=220)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 4.888 (IC base=+0.020)

- **PATRÓN** `volumen_regimen` > `0.624` → IC=+0.288 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.624 (IC base=+0.020)

- **PATRÓN** `volumen_pendiente_norm` < `0.0791` → IC=+0.281 (n=276)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0791 (IC base=+0.020)

- **PATRÓN** `volumen_spike_ratio` < `2.2252` → IC=+0.289 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.2252 (IC base=+0.020)

- **PATRÓN** `volumen_spike_ratio` > `1.544` → IC=+0.268 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.544 (IC base=+0.020)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.274 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 40.0 (IC base=+0.020)

- **PATRÓN** `ibs_20min` < `0.2` → IC=+0.155 (n=2401)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.2 (IC base=-0.036)

- **PATRÓN** `dist_vwap_pct` > `0.5114` → IC=+0.294 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5114 (IC base=-0.036)

- **PATRÓN** `volumen_regimen` < `0.7052` → IC=+0.302 (n=469)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7052 (IC base=-0.036)

- **PATRÓN** `volumen_pendiente_norm` > `0.0797` → IC=+0.309 (n=479)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0797 (IC base=-0.036)

- **PATRÓN** `volumen_spike_ratio` < `2.4773` → IC=+0.299 (n=996)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4773 (IC base=-0.036)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `ibs_20min` < `0.7885` → IC=-0.157 (n=3687)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7885
  - _Potencial_: sin este filtro IC_bueno=+0.134 (n=1905)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.174 (n=1187)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=4405)

- **FILTRO** `ibs_20min` > `0.7356` → IC=-0.188 (n=1930)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7356
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=5792)

- **PATRÓN** `ibs_20min` > `0.7885` → IC=+0.134 (n=1905)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` > 0.7885 (IC base=-0.058)

- **PATRÓN** `dist_vwap_pct` > `1.0017` → IC=+0.356 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0017 (IC base=-0.058)

- **PATRÓN** `volumen_regimen` > `0.7047` → IC=+0.319 (n=985)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7047 (IC base=-0.058)

- **PATRÓN** `volumen_pendiente_norm` < `0.1068` → IC=+0.302 (n=1047)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1068 (IC base=-0.058)

- **PATRÓN** `volumen_pendiente_norm` > `0.1692` → IC=+0.300 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1692 (IC base=-0.058)

- **PATRÓN** `volumen_spike_ratio` < `1.5797` → IC=+0.303 (n=475)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5797 (IC base=-0.058)

- **PATRÓN** `volumen_spike_ratio` > `2.523` → IC=+0.318 (n=360)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.523 (IC base=-0.058)

- **PATRÓN** `dist_vwap_pct` > `1.0649` → IC=+0.275 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0649 (IC base=+0.005)

- **PATRÓN** `volumen_regimen` < `0.6428` → IC=+0.273 (n=756)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6428 (IC base=+0.005)

- **PATRÓN** `volumen_regimen` > `1.2094` → IC=+0.286 (n=756)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2094 (IC base=+0.005)

- **PATRÓN** `volumen_pendiente_norm` > `0.1697` → IC=+0.287 (n=604)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1697 (IC base=+0.005)

- **PATRÓN** `volumen_spike_ratio` < `2.1777` → IC=+0.266 (n=1885)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1777 (IC base=+0.005)

- **PATRÓN** `volumen_spike_ratio` > `1.4393` → IC=+0.271 (n=2142)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4393 (IC base=+0.005)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.195 (n=7820)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` > 0.0107 (IC base=+0.086)

- **PATRÓN** `ibs_20min` > `0.8667` → IC=+0.284 (n=10650)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8667 (IC base=+0.086)

- **PATRÓN** `dist_vwap_pct` > `0.9321` → IC=+0.302 (n=1621)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9321 (IC base=+0.086)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.468` → IC=+0.168 (n=10524)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 3.468 (IC base=+0.086)

- **PATRÓN** `volumen_regimen` > `0.6932` → IC=+0.278 (n=7722)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6932 (IC base=+0.086)

- **PATRÓN** `volumen_pendiente_norm` > `0.2933` → IC=+0.295 (n=1943)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2933 (IC base=+0.086)

- **PATRÓN** `volumen_spike_ratio` > `2.6493` → IC=+0.286 (n=4534)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6493 (IC base=+0.086)

- **PATRÓN** `ballena_activa_n` < `89.0` → IC=+0.309 (n=13222)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 89.0 (IC base=+0.086)

- **PATRÓN** `sigma_h` > `0.0103` → IC=+0.157 (n=7561)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0103 (IC base=+0.084)

- **PATRÓN** `ibs_20min` < `0.5198` → IC=+0.172 (n=19960)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.5198 (IC base=+0.084)

- **PATRÓN** `volumen_regimen` < `0.6994` → IC=+0.283 (n=3330)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6994 (IC base=+0.084)

- **PATRÓN** `volumen_regimen` > `1.189` → IC=+0.283 (n=2523)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.189 (IC base=+0.084)

- **PATRÓN** `volumen_pendiente_norm` > `0.2944` → IC=+0.329 (n=1685)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2944 (IC base=+0.084)

- **PATRÓN** `volumen_spike_ratio` < `1.4532` → IC=+0.306 (n=3727)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4532 (IC base=+0.084)

- **PATRÓN** `volumen_spike_ratio` > `2.2804` → IC=+0.304 (n=5068)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2804 (IC base=+0.084)

- **PATRÓN** `ballena_activa_n` < `72.0` → IC=+0.312 (n=11156)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 72.0 (IC base=+0.084)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.8024` → IC=-0.136 (n=4168)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8024
  - _Potencial_: sin este filtro IC_bueno=+0.301 (n=2148)

- **FILTRO** `ibs_20min` > `0.7138` → IC=-0.236 (n=1393)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7138
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=4183)

- **FILTRO** `sigma_ewma_delta_pct` > `4.085` → IC=-0.237 (n=1203)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.085
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=4373)

- **PATRÓN** `ibs_20min` > `0.8024` → IC=+0.301 (n=2148)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8024 (IC base=+0.013)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.955` → IC=+0.189 (n=2107)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 2.955 (IC base=+0.013)

- **PATRÓN** `volumen_pendiente_norm` > `0.2294` → IC=+0.332 (n=402)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2294 (IC base=+0.013)

- **PATRÓN** `volumen_spike_ratio` < `1.4475` → IC=+0.284 (n=668)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4475 (IC base=+0.013)

- **PATRÓN** `volumen_spike_ratio` > `2.2443` → IC=+0.304 (n=908)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2443 (IC base=+0.013)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.305 (n=2007)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 27.0 (IC base=+0.013)

- **PATRÓN** `ibs_20min` < `0.1743` → IC=+0.171 (n=1395)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.1743 (IC base=-0.020)

- **PATRÓN** `volumen_pendiente_norm` < `0.1509` → IC=+0.403 (n=1112)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1509 (IC base=-0.020)

- **PATRÓN** `volumen_spike_ratio` < `1.4225` → IC=+0.428 (n=358)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4225 (IC base=-0.020)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.399 (n=1118)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 23.0 (IC base=-0.020)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.1696` → IC=+0.225 (n=993)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1696 (IC base=+0.010)

- **PATRÓN** `volumen_regimen` < `1.1961` → IC=+0.211 (n=2296)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1961 (IC base=+0.010)

- **PATRÓN** `volumen_regimen` > `0.6956` → IC=+0.218 (n=2051)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6956 (IC base=+0.010)

- **PATRÓN** `volumen_pendiente_norm` > `0.2762` → IC=+0.245 (n=308)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2762 (IC base=+0.010)

- **PATRÓN** `volumen_spike_ratio` < `1.4165` → IC=+0.228 (n=756)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4165 (IC base=+0.010)

- **PATRÓN** `volumen_spike_ratio` > `2.4786` → IC=+0.211 (n=756)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4786 (IC base=+0.010)

- **PATRÓN** `ballena_activa_n` < `258.0` → IC=+0.244 (n=1511)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 258.0 (IC base=+0.010)

- **PATRÓN** `volumen_regimen` > `0.6178` → IC=+0.256 (n=1635)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6178 (IC base=-0.001)

- **PATRÓN** `volumen_pendiente_norm` > `0.2697` → IC=+0.304 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2697 (IC base=-0.001)

- **PATRÓN** `volumen_spike_ratio` < `1.5257` → IC=+0.263 (n=697)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5257 (IC base=-0.001)

- **PATRÓN** `volumen_spike_ratio` > `2.148` → IC=+0.264 (n=718)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.148 (IC base=-0.001)

- **PATRÓN** `ballena_activa_n` < `185.0` → IC=+0.287 (n=534)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 185.0 (IC base=-0.001)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0095` → IC=+0.321 (n=2185)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0095 (IC base=+0.285)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.293 (n=3281)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.285)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.325 (n=1781)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.285)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.586` → IC=+0.305 (n=2205)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.586 (IC base=+0.285)

- **PATRÓN** `volumen_pendiente_norm` < `0.0974` → IC=+0.297 (n=2883)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0974 (IC base=+0.285)

- **PATRÓN** `volumen_spike_ratio` > `1.6063` → IC=+0.290 (n=3185)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6063 (IC base=+0.285)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.293 (n=3934)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.285)

- **PATRÓN** `libro_liquidez` > `2013.026` → IC=+0.294 (n=1092)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2013.026 (IC base=+0.285)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.307 (n=1988)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 14.0 (IC base=+0.285)

- **PATRÓN** `sigma_h` > `0.009` → IC=+0.333 (n=1993)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.009 (IC base=+0.308)

- **PATRÓN** `drift_60min` |x|≤ `0.1774` → IC=+0.326 (n=1315)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1774 (IC base=+0.308)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.326 (n=1149)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.308)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.311 (n=1356)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.308)

- **PATRÓN** `ibs_20min` > `0.1481` → IC=+0.319 (n=1994)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1481 (IC base=+0.308)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.125` → IC=+0.310 (n=356)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.125 (IC base=+0.308)

- **PATRÓN** `volumen_pendiente_norm` < `0.1993` → IC=+0.308 (n=2944)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1993 (IC base=+0.308)

- **PATRÓN** `volumen_pendiente_norm` > `0.3448` → IC=+0.318 (n=486)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3448 (IC base=+0.308)

- **PATRÓN** `volumen_spike_ratio` > `2.7378` → IC=+0.325 (n=1309)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7378 (IC base=+0.308)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.308 (n=1517)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.308)

- **PATRÓN** `libro_liquidez` > `1992.3784` → IC=+0.314 (n=996)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1992.3784 (IC base=+0.308)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.313 (n=2515)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 22.0 (IC base=+0.308)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.72` → IC=-0.178 (n=1481)

  - _Acción_: SKIP cuando `ibs_20min` > 0.72
  - _Potencial_: sin este filtro IC_bueno=+0.070 (n=4446)

- **PATRÓN** `dist_vwap_pct` > `0.1441` → IC=+0.238 (n=1058)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1441 (IC base=+0.020)

- **PATRÓN** `volumen_regimen` < `1.1596` → IC=+0.236 (n=2104)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1596 (IC base=+0.020)

- **PATRÓN** `volumen_pendiente_norm` < `0.1626` → IC=+0.236 (n=2207)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1626 (IC base=+0.020)

- **PATRÓN** `volumen_pendiente_norm` > `0.1029` → IC=+0.243 (n=690)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1029 (IC base=+0.020)

- **PATRÓN** `volumen_spike_ratio` < `2.4504` → IC=+0.240 (n=2043)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4504 (IC base=+0.020)

- **PATRÓN** `ballena_activa_n` < `113.0` → IC=+0.254 (n=2080)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 113.0 (IC base=+0.020)

- **PATRÓN** `ibs_20min` < `0.0918` → IC=+0.156 (n=1483)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.0918 (IC base=+0.008)

- **PATRÓN** `dist_vwap_pct` > `0.7339` → IC=+0.261 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7339 (IC base=+0.008)

- **PATRÓN** `volumen_regimen` < `1.1877` → IC=+0.264 (n=1527)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1877 (IC base=+0.008)

- **PATRÓN** `volumen_pendiente_norm` > `0.2829` → IC=+0.313 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2829 (IC base=+0.008)

- **PATRÓN** `volumen_spike_ratio` < `1.787` → IC=+0.292 (n=979)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.787 (IC base=+0.008)

- **PATRÓN** `volumen_spike_ratio` > `2.4356` → IC=+0.280 (n=489)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4356 (IC base=+0.008)

- **PATRÓN** `ballena_activa_n` < `115.0` → IC=+0.284 (n=1494)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 115.0 (IC base=+0.008)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7407` → IC=-0.251 (n=2417)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7407
  - _Potencial_: sin este filtro IC_bueno=+0.313 (n=2423)

- **FILTRO** `ibs_20min` > `0.617` → IC=-0.234 (n=1146)

  - _Acción_: SKIP cuando `ibs_20min` > 0.617
  - _Potencial_: sin este filtro IC_bueno=+0.155 (n=3441)

- **FILTRO** `sigma_ewma_delta_pct` > `8.282` → IC=-0.265 (n=525)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.282
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=4062)

- **PATRÓN** `ibs_20min` > `0.7407` → IC=+0.313 (n=2423)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7407 (IC base=+0.031)

- **PATRÓN** `dist_vwap_pct` > `1.0414` → IC=+0.357 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0414 (IC base=+0.031)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.461` → IC=+0.155 (n=1964)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 2.461 (IC base=+0.031)

- **PATRÓN** `volumen_regimen` < `0.842` → IC=+0.345 (n=1174)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.842 (IC base=+0.031)

- **PATRÓN** `volumen_regimen` > `0.6962` → IC=+0.336 (n=1573)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6962 (IC base=+0.031)

- **PATRÓN** `volumen_pendiente_norm` < `0.1568` → IC=+0.336 (n=1813)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1568 (IC base=+0.031)

- **PATRÓN** `volumen_pendiente_norm` > `0.274` → IC=+0.365 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.274 (IC base=+0.031)

- **PATRÓN** `volumen_spike_ratio` < `1.4239` → IC=+0.360 (n=570)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4239 (IC base=+0.031)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.355 (n=1523)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=+0.031)

- **PATRÓN** `ibs_20min` < `0.617` → IC=+0.155 (n=3441)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.617 (IC base=+0.058)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.052` → IC=+0.133 (n=3230)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` < 3.052 (IC base=+0.058)

- **PATRÓN** `volumen_regimen` < `0.6947` → IC=+0.282 (n=765)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6947 (IC base=+0.058)

- **PATRÓN** `volumen_pendiente_norm` > `0.0707` → IC=+0.294 (n=698)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0707 (IC base=+0.058)

- **PATRÓN** `volumen_spike_ratio` < `1.8044` → IC=+0.281 (n=1124)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8044 (IC base=+0.058)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.288 (n=1713)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 46.0 (IC base=+0.058)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.359 (n=2222)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.316)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.318 (n=2511)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.316)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.318 (n=2604)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.316)

- **PATRÓN** `ibs_20min` > `0.66` → IC=+0.344 (n=2484)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.66 (IC base=+0.316)

- **PATRÓN** `dist_vwap_pct` > `0.294` → IC=+0.339 (n=1195)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.294 (IC base=+0.316)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.756` → IC=+0.336 (n=1216)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.756 (IC base=+0.316)

- **PATRÓN** `volumen_regimen` > `0.6304` → IC=+0.327 (n=2484)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6304 (IC base=+0.316)

- **PATRÓN** `volumen_pendiente_norm` > `0.2816` → IC=+0.347 (n=365)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2816 (IC base=+0.316)

- **PATRÓN** `volumen_spike_ratio` > `1.5298` → IC=+0.329 (n=2141)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5298 (IC base=+0.316)

- **PATRÓN** `libro_liquidez` > `2995.543` → IC=+0.330 (n=828)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2995.543 (IC base=+0.316)

- **PATRÓN** `ballena_activa_n` < `39.0` → IC=+0.343 (n=2231)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 39.0 (IC base=+0.316)

- **PATRÓN** `sigma_h` > `0.0093` → IC=+0.333 (n=2670)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0093 (IC base=+0.315)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.319 (n=1353)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.315)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.317 (n=1295)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.315)

- **PATRÓN** `ibs_20min` < `0.3828` → IC=+0.332 (n=2668)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3828 (IC base=+0.315)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.608` → IC=+0.326 (n=975)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.608 (IC base=+0.315)

- **PATRÓN** `volumen_regimen` < `0.7206` → IC=+0.321 (n=1174)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7206 (IC base=+0.315)

- **PATRÓN** `volumen_regimen` > `1.2084` → IC=+0.341 (n=890)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2084 (IC base=+0.315)

- **PATRÓN** `volumen_pendiente_norm` > `0.2309` → IC=+0.365 (n=503)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2309 (IC base=+0.315)

- **PATRÓN** `volumen_spike_ratio` < `1.4143` → IC=+0.323 (n=829)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4143 (IC base=+0.315)

- **PATRÓN** `volumen_spike_ratio` > `2.1415` → IC=+0.316 (n=1127)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1415 (IC base=+0.315)

- **PATRÓN** `libro_liquidez` > `2982.6883` → IC=+0.317 (n=890)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2982.6883 (IC base=+0.315)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.223 (n=5799)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0125 (IC base=+0.172)

- **PATRÓN** `drift_60min` |x|≤ `0.1222` → IC=+0.190 (n=7650)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.1222 (IC base=+0.172)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.183 (n=18026)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.172)

- **PATRÓN** `ibs_20min` > `0.5376` → IC=+0.230 (n=17385)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5376 (IC base=+0.172)

- **PATRÓN** `dist_vwap_pct` > `0.1624` → IC=+0.205 (n=6537)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1624 (IC base=+0.172)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.75` → IC=+0.259 (n=3392)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.75 (IC base=+0.172)

- **PATRÓN** `volumen_regimen` < `1.1783` → IC=+0.152 (n=11582)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.1783 (IC base=+0.172)

- **PATRÓN** `volumen_regimen` > `0.6251` → IC=+0.151 (n=11583)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 0.6251 (IC base=+0.172)

- **PATRÓN** `volumen_pendiente_norm` > `0.2935` → IC=+0.202 (n=2516)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2935 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` > `2.6049` → IC=+0.185 (n=5639)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.6049 (IC base=+0.172)

- **PATRÓN** `ballena_activa_n` < `86.0` → IC=+0.191 (n=16294)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 86.0 (IC base=+0.172)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.193 (n=7562)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0059 (IC base=+0.185)

- **PATRÓN** `sigma_h` > `0.0079` → IC=+0.185 (n=11447)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0079 (IC base=+0.185)

- **PATRÓN** `drift_60min` |x|≤ `0.0809` → IC=+0.223 (n=5722)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0809 (IC base=+0.185)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.211 (n=6467)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.185)

- **PATRÓN** `ibs_20min` < `0.5254` → IC=+0.239 (n=17168)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5254 (IC base=+0.185)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.498` → IC=+0.188 (n=2726)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 9.498 (IC base=+0.185)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.506` → IC=+0.192 (n=15301)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` < 2.506 (IC base=+0.185)

- **PATRÓN** `volumen_regimen` < `1.1856` → IC=+0.165 (n=12203)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.1856 (IC base=+0.185)

- **PATRÓN** `volumen_pendiente_norm` > `0.2935` → IC=+0.219 (n=2576)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2935 (IC base=+0.185)

- **PATRÓN** `volumen_spike_ratio` < `1.5598` → IC=+0.184 (n=7197)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` < 1.5598 (IC base=+0.185)

- **PATRÓN** `volumen_spike_ratio` > `2.6297` → IC=+0.195 (n=5452)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.6297 (IC base=+0.185)

- **PATRÓN** `ballena_activa_n` < `91.0` → IC=+0.199 (n=16165)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 91.0 (IC base=+0.185)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `drift_60min` |x|≤ `0.104` → IC=+0.257 (n=1257)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.104 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.233 (n=2972)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.227)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.227 (n=1937)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.227)

- **PATRÓN** `ibs_20min` > `0.9426` → IC=+0.294 (n=1905)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9426 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.458` → IC=+0.327 (n=936)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.458 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` > `0.281` → IC=+0.284 (n=434)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.281 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` < `1.8383` → IC=+0.226 (n=1820)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8383 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` > `1.4361` → IC=+0.226 (n=2727)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4361 (IC base=+0.227)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.237 (n=3182)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.227)

- **PATRÓN** `sigma_h` < `0.0099` → IC=+0.259 (n=2347)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0099 (IC base=+0.257)

- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.258 (n=1065)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0089 (IC base=+0.257)

- **PATRÓN** `drift_60min` |x|≤ `0.097` → IC=+0.314 (n=1034)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.097 (IC base=+0.257)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.261 (n=2416)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.257)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.264 (n=1591)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.257)

- **PATRÓN** `ibs_20min` < `0.4404` → IC=+0.274 (n=2347)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4404 (IC base=+0.257)

- **PATRÓN** `volumen_pendiente_norm` < `0.0985` → IC=+0.260 (n=2061)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0985 (IC base=+0.257)

- **PATRÓN** `volumen_pendiente_norm` > `0.3012` → IC=+0.268 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3012 (IC base=+0.257)

- **PATRÓN** `volumen_spike_ratio` < `1.4462` → IC=+0.277 (n=750)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4462 (IC base=+0.257)

- **PATRÓN** `volumen_spike_ratio` > `2.6858` → IC=+0.257 (n=750)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6858 (IC base=+0.257)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.266 (n=1688)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.257)

- **PATRÓN** `libro_liquidez` > `1772.0818` → IC=+0.267 (n=1564)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1772.0818 (IC base=+0.257)

- **PATRÓN** `ballena_activa_n` < `7.0` → IC=+0.257 (n=875)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 7.0 (IC base=+0.257)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.198 (n=888)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0032 (IC base=+0.127)

- **PATRÓN** `drift_60min` |x|≤ `0.0644` → IC=+0.178 (n=883)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.0644 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.145 (n=2765)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.127)

- **PATRÓN** `ibs_20min` > `0.2602` → IC=+0.204 (n=2647)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2602 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` > `0.1843` → IC=+0.212 (n=1309)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1843 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.616` → IC=+0.209 (n=482)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.616 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` < `0.6958` → IC=+0.132 (n=1165)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 0.6958 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` > `1.0554` → IC=+0.133 (n=1200)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` > 1.0554 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` > `0.2795` → IC=+0.165 (n=410)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.2795 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` < `1.5057` → IC=+0.132 (n=1145)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 1.5057 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` > `2.4677` → IC=+0.147 (n=868)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 2.4677 (IC base=+0.127)

- **PATRÓN** `ballena_activa_n` < `212.0` → IC=+0.141 (n=1132)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 212.0 (IC base=+0.127)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.172 (n=2825)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0065 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.2398` → IC=+0.175 (n=2485)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.2398 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.182 (n=1343)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 15.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` < `0.6093` → IC=+0.211 (n=2824)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6093 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.857` → IC=+0.179 (n=531)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 10.857 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.025` → IC=+0.155 (n=2464)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 4.025 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` < `1.2012` → IC=+0.162 (n=2824)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2012 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` < `0.2281` → IC=+0.155 (n=2996)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` < 0.2281 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `2.4631` → IC=+0.156 (n=2699)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.4631 (IC base=+0.151)

- **PATRÓN** `ballena_activa_n` < `208.0` → IC=+0.200 (n=1160)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 208.0 (IC base=+0.151)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0115` → IC=+0.230 (n=1340)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0115 (IC base=+0.211)

- **PATRÓN** `drift_60min` |x|≤ `0.2489` → IC=+0.233 (n=1965)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2489 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.219 (n=3065)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.290 (n=1570)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.063` → IC=+0.305 (n=700)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.063 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` < `0.0984` → IC=+0.210 (n=2569)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0984 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.3512` → IC=+0.242 (n=416)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3512 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `2.7088` → IC=+0.227 (n=1305)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7088 (IC base=+0.211)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.215 (n=3562)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `2000.3284` → IC=+0.224 (n=982)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2000.3284 (IC base=+0.211)

- **PATRÓN** `sigma_h` < `0.0119` → IC=+0.247 (n=2620)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0119 (IC base=+0.240)

- **PATRÓN** `drift_60min` |x|≤ `0.4123` → IC=+0.263 (n=2305)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4123 (IC base=+0.240)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.278 (n=1005)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.240)

- **PATRÓN** `ibs_20min` < `0.0426` → IC=+0.291 (n=1154)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0426 (IC base=+0.240)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.896` → IC=+0.277 (n=343)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.896 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` > `0.3545` → IC=+0.286 (n=437)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3545 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` < `1.7675` → IC=+0.242 (n=1114)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7675 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` > `2.1788` → IC=+0.251 (n=1687)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1788 (IC base=+0.240)

- **PATRÓN** `libro_liquidez` > `1872.8576` → IC=+0.248 (n=1187)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1872.8576 (IC base=+0.240)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.242 (n=1676)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.240)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.200 (n=958)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0038 (IC base=+0.127)

- **PATRÓN** `drift_60min` |x|≤ `0.0779` → IC=+0.182 (n=957)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.0779 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.138 (n=2960)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.127)

- **PATRÓN** `ibs_20min` > `0.2452` → IC=+0.189 (n=2865)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.2452 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` > `0.1392` → IC=+0.186 (n=1628)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1392 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.227` → IC=+0.203 (n=493)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.227 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` < `0.8417` → IC=+0.137 (n=1912)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.8417 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` > `0.2875` → IC=+0.167 (n=433)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.2875 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` < `1.8108` → IC=+0.125 (n=1871)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 1.8108 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` > `2.5096` → IC=+0.140 (n=936)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 2.5096 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `6842.5359` → IC=+0.198 (n=1299)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 6842.5359 (IC base=+0.127)

- **PATRÓN** `ballena_activa_n` < `125.0` → IC=+0.127 (n=2802)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 125.0 (IC base=+0.127)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.165 (n=2690)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0067 (IC base=+0.131)

- **PATRÓN** `drift_60min` |x|≤ `0.3999` → IC=+0.147 (n=3056)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.3999 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.166 (n=1461)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 15.0 (IC base=+0.131)

- **PATRÓN** `ibs_20min` < `0.6728` → IC=+0.187 (n=3056)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.6728 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.201` → IC=+0.140 (n=731)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 9.201 (IC base=+0.131)

- **PATRÓN** `volumen_regimen` < `0.8526` → IC=+0.150 (n=2038)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.8526 (IC base=+0.131)

- **PATRÓN** `volumen_pendiente_norm` > `0.2944` → IC=+0.175 (n=454)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.2944 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` < `1.8013` → IC=+0.133 (n=1934)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 1.8013 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` > `2.5295` → IC=+0.135 (n=967)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 2.5295 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `6344.3973` → IC=+0.190 (n=1386)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 6344.3973 (IC base=+0.131)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.158 (n=964)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 48.0 (IC base=+0.131)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0126` → IC=+0.163 (n=1068)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` > 0.0126 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.133 (n=3279)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 5.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` > `0.4706` → IC=+0.204 (n=3209)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4706 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` > `0.1984` → IC=+0.187 (n=1695)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1984 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.972` → IC=+0.287 (n=674)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.972 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` < `1.1669` → IC=+0.129 (n=3201)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 1.1669 (IC base=+0.117)

- **PATRÓN** `volumen_pendiente_norm` < `0.1628` → IC=+0.122 (n=3264)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_pendiente_norm` < 0.1628 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` < `1.7791` → IC=+0.124 (n=2071)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 1.7791 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `2666.6432` → IC=+0.196 (n=1451)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 2666.6432 (IC base=+0.117)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.132 (n=1061)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 16.0 (IC base=+0.117)

- **PATRÓN** `sigma_h` < `0.0119` → IC=+0.143 (n=3344)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0119 (IC base=+0.120)

- **PATRÓN** `drift_60min` |x|≤ `0.1135` → IC=+0.164 (n=1115)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.1135 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.135 (n=3409)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 5.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` < `0.6489` → IC=+0.220 (n=3343)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6489 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.239` → IC=+0.142 (n=2959)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 2.239 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` < `1.1776` → IC=+0.127 (n=3343)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 1.1776 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` > `0.275` → IC=+0.148 (n=464)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.275 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` < `1.4343` → IC=+0.137 (n=1055)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.4343 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` > `2.4432` → IC=+0.133 (n=1054)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 2.4432 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `2554.0018` → IC=+0.186 (n=1516)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 2554.0018 (IC base=+0.120)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.127 (n=3151)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 44.0 (IC base=+0.120)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0129` → IC=+0.251 (n=2565)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0129 (IC base=+0.226)

- **PATRÓN** `drift_60min` |x|≤ `0.1653` → IC=+0.242 (n=1264)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1653 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.232 (n=2985)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.226)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.228 (n=2585)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.226)

- **PATRÓN** `ibs_20min` > `0.6667` → IC=+0.257 (n=2873)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6667 (IC base=+0.226)

- **PATRÓN** `dist_vwap_pct` > `0.1805` → IC=+0.233 (n=1747)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1805 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.534` → IC=+0.257 (n=1308)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.534 (IC base=+0.226)

- **PATRÓN** `volumen_regimen` > `0.624` → IC=+0.236 (n=2872)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.624 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` > `0.2348` → IC=+0.264 (n=537)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2348 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` < `2.4718` → IC=+0.229 (n=2802)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4718 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` > `1.4333` → IC=+0.231 (n=2803)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4333 (IC base=+0.226)

- **PATRÓN** `libro_liquidez` > `2591.5202` → IC=+0.230 (n=1914)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2591.5202 (IC base=+0.226)

- **PATRÓN** `sigma_h` < `0.0124` → IC=+0.241 (n=1312)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0124 (IC base=+0.240)

- **PATRÓN** `sigma_h` > `0.0225` → IC=+0.250 (n=1352)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0225 (IC base=+0.240)

- **PATRÓN** `drift_60min` |x|≤ `0.5864` → IC=+0.251 (n=2980)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5864 (IC base=+0.240)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.251 (n=1459)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.240)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.247 (n=1335)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.240)

- **PATRÓN** `ibs_20min` < `0.44` → IC=+0.263 (n=2989)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.44 (IC base=+0.240)

- **PATRÓN** `dist_vwap_pct` > `1.1432` → IC=+0.259 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1432 (IC base=+0.240)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.121` → IC=+0.268 (n=571)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.121 (IC base=+0.240)

- **PATRÓN** `volumen_regimen` < `0.8693` → IC=+0.242 (n=1988)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8693 (IC base=+0.240)

- **PATRÓN** `volumen_regimen` > `0.6412` → IC=+0.242 (n=2980)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6412 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` > `0.2804` → IC=+0.292 (n=411)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2804 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` < `2.5149` → IC=+0.238 (n=2814)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5149 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` > `1.55` → IC=+0.241 (n=2515)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.55 (IC base=+0.240)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.208 (n=1497)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.157)

- **PATRÓN** `drift_60min` |x|≤ `0.1344` → IC=+0.173 (n=1977)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.1344 (IC base=+0.157)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.169 (n=4678)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 5.0 (IC base=+0.157)

- **PATRÓN** `ibs_20min` > `0.3051` → IC=+0.194 (n=4490)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 0.3051 (IC base=+0.157)

- **PATRÓN** `dist_vwap_pct` > `0.2223` → IC=+0.181 (n=1689)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.2223 (IC base=+0.157)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.538` → IC=+0.209 (n=736)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.538 (IC base=+0.157)

- **PATRÓN** `volumen_regimen` < `0.8615` → IC=+0.167 (n=2714)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.8615 (IC base=+0.157)

- **PATRÓN** `volumen_regimen` > `1.1939` → IC=+0.162 (n=1357)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 1.1939 (IC base=+0.157)

- **PATRÓN** `volumen_pendiente_norm` > `0.157` → IC=+0.172 (n=1182)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.157 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` < `1.527` → IC=+0.162 (n=1927)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 1.527 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` > `1.8093` → IC=+0.160 (n=2919)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.8093 (IC base=+0.157)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.158 (n=5010)

  - _Acción_: Kelly boost +0.79€ cuando `libro_spread` < 0.02 (IC base=+0.157)

- **PATRÓN** `libro_liquidez` > `7552.7231` → IC=+0.184 (n=2036)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 7552.7231 (IC base=+0.157)

- **PATRÓN** `ibs_20min` < `0.3833` → IC=+0.175 (n=3274)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.3833 (IC base=+0.097)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.138 (n=2126)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 23.0 (IC base=+0.097)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.197 (n=1143)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0061 (IC base=+0.183)

- **PATRÓN** `drift_60min` |x|≤ `0.3292` → IC=+0.198 (n=1143)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.3292 (IC base=+0.183)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.216 (n=1031)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.183)

- **PATRÓN** `ibs_20min` > `0.6159` → IC=+0.239 (n=762)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6159 (IC base=+0.183)

- **PATRÓN** `dist_vwap_pct` > `0.3087` → IC=+0.218 (n=346)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3087 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.927` → IC=+0.212 (n=505)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.927 (IC base=+0.183)

- **PATRÓN** `volumen_regimen` < `0.8788` → IC=+0.196 (n=762)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 0.8788 (IC base=+0.183)

- **PATRÓN** `volumen_pendiente_norm` < `0.2165` → IC=+0.186 (n=1286)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` < 0.2165 (IC base=+0.183)

- **PATRÓN** `volumen_pendiente_norm` > `0.0913` → IC=+0.199 (n=396)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.0913 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` < `2.1711` → IC=+0.197 (n=987)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 2.1711 (IC base=+0.183)

- **PATRÓN** `libro_liquidez` > `15742.1193` → IC=+0.192 (n=518)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 15742.1193 (IC base=+0.183)

- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.162 (n=480)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0031 (IC base=+0.082)

- **PATRÓN** `ibs_20min` < `0.2049` → IC=+0.197 (n=629)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.2049 (IC base=+0.082)

- **PATRÓN** `ballena_activa_n` < `165.0` → IC=+0.174 (n=618)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 165.0 (IC base=+0.082)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.235 (n=601)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.152)

- **PATRÓN** `drift_60min` |x|≤ `0.2096` → IC=+0.156 (n=909)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.2096 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.172 (n=1411)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 5.0 (IC base=+0.152)

- **PATRÓN** `ibs_20min` > `0.7914` → IC=+0.266 (n=617)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7914 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` > `0.821` → IC=+0.192 (n=222)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.821 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.882` → IC=+0.206 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.882 (IC base=+0.152)

- **PATRÓN** `volumen_regimen` < `0.8322` → IC=+0.164 (n=908)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8322 (IC base=+0.152)

- **PATRÓN** `volumen_pendiente_norm` > `0.2193` → IC=+0.199 (n=247)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2193 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` > `1.7764` → IC=+0.169 (n=895)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 1.7764 (IC base=+0.152)

- **PATRÓN** `libro_liquidez` > `8031.121` → IC=+0.175 (n=617)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 8031.121 (IC base=+0.152)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.125 (n=888)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0053 (IC base=+0.095)

- **PATRÓN** `ibs_20min` < `0.0855` → IC=+0.213 (n=444)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0855 (IC base=+0.095)

- **PATRÓN** `volumen_regimen` < `0.6781` → IC=+0.128 (n=586)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 0.6781 (IC base=+0.095)

- **PATRÓN** `libro_liquidez` > `7946.3404` → IC=+0.153 (n=604)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 7946.3404 (IC base=+0.095)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.132 (n=441)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 35.0 (IC base=+0.095)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` < `0.0092` → IC=+0.143 (n=776)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.0092 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.165 (n=812)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 11.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` > `0.5385` → IC=+0.192 (n=1042)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.5385 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` > `0.936` → IC=+0.165 (n=189)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.936 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.857` → IC=+0.227 (n=455)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.857 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` < `1.0462` → IC=+0.134 (n=1024)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 1.0462 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` > `0.7015` → IC=+0.130 (n=1040)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` > 0.7015 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` > `0.225` → IC=+0.152 (n=205)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` > 0.225 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` < `1.4132` → IC=+0.151 (n=376)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.4132 (IC base=+0.122)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.123 (n=1224)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.02 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `2756.9384` → IC=+0.164 (n=528)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 2756.9384 (IC base=+0.122)

- **PATRÓN** `ibs_20min` < `0.5556` → IC=+0.156 (n=1142)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.5556 (IC base=+0.077)

- **PATRÓN** `libro_liquidez` > `2632.9653` → IC=+0.167 (n=587)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 2632.9653 (IC base=+0.077)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0165` → IC=+0.250 (n=270)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0165 (IC base=+0.192)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.230 (n=194)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.192)

- **PATRÓN** `ibs_20min` > `0.9538` → IC=+0.215 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9538 (IC base=+0.192)

- **PATRÓN** `dist_vwap_pct` > `0.8988` → IC=+0.211 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8988 (IC base=+0.192)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.634` → IC=+0.208 (n=399)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.634 (IC base=+0.192)

- **PATRÓN** `volumen_regimen` > `0.7143` → IC=+0.218 (n=360)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7143 (IC base=+0.192)

- **PATRÓN** `volumen_pendiente_norm` > `0.0785` → IC=+0.206 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0785 (IC base=+0.192)

- **PATRÓN** `volumen_spike_ratio` < `2.1265` → IC=+0.205 (n=330)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1265 (IC base=+0.192)

- **PATRÓN** `volumen_spike_ratio` > `1.4093` → IC=+0.208 (n=375)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4093 (IC base=+0.192)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.203 (n=433)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.192)

- **PATRÓN** `libro_liquidez` > `2944.973` → IC=+0.208 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2944.973 (IC base=+0.192)

- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.170 (n=449)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.0107 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.5075` → IC=+0.157 (n=395)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.5075 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.192 (n=212)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 15.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` < `0.3466` → IC=+0.152 (n=300)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` < 0.3466 (IC base=+0.148)

- **PATRÓN** `ibs_20min` > `0.1049` → IC=+0.152 (n=449)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` > 0.1049 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` > `1.1922` → IC=+0.273 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1922 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.008` → IC=+0.152 (n=116)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 5.008 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.146` → IC=+0.152 (n=409)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` < 2.146 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `1.2585` → IC=+0.167 (n=449)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.2585 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` < `0.113` → IC=+0.163 (n=411)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` < 0.113 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` > `0.2302` → IC=+0.179 (n=82)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.2302 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `1.491` → IC=+0.192 (n=144)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 1.491 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` > `2.6474` → IC=+0.151 (n=144)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 2.6474 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.167 (n=434)

  - _Acción_: Kelly boost +0.84€ cuando `ballena_activa_n` < 20.0 (IC base=+0.148)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.229 (n=7612)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0125 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.190 (n=23785)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` > `0.4286` → IC=+0.227 (n=22822)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4286 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` > `0.8824` → IC=+0.211 (n=2653)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8824 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.934` → IC=+0.258 (n=5593)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.934 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` < `1.2145` → IC=+0.159 (n=15371)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.2145 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.2409` → IC=+0.207 (n=4104)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2409 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `2.6244` → IC=+0.193 (n=7426)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.6244 (IC base=+0.180)

- **PATRÓN** `ballena_activa_n` < `102.0` → IC=+0.201 (n=21451)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 102.0 (IC base=+0.180)

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.201 (n=7023)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.197)

- **PATRÓN** `sigma_h` > `0.0122` → IC=+0.205 (n=7023)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0122 (IC base=+0.197)

- **PATRÓN** `drift_60min` |x|≤ `0.484` → IC=+0.200 (n=21040)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.484 (IC base=+0.197)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.216 (n=7901)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.197)

- **PATRÓN** `ibs_20min` < `0.5918` → IC=+0.245 (n=21040)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5918 (IC base=+0.197)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.52` → IC=+0.203 (n=19545)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.52 (IC base=+0.197)

- **PATRÓN** `volumen_regimen` < `0.6322` → IC=+0.180 (n=4713)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 0.6322 (IC base=+0.197)

- **PATRÓN** `volumen_pendiente_norm` > `0.293` → IC=+0.254 (n=2892)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.293 (IC base=+0.197)

- **PATRÓN** `volumen_spike_ratio` > `2.6294` → IC=+0.209 (n=6721)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6294 (IC base=+0.197)

- **PATRÓN** `ballena_activa_n` < `90.0` → IC=+0.213 (n=19914)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 90.0 (IC base=+0.197)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.252 (n=1772)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.236)

- **PATRÓN** `ibs_20min` > `0.8641` → IC=+0.296 (n=2431)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8641 (IC base=+0.236)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.827` → IC=+0.341 (n=872)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.827 (IC base=+0.236)

- **PATRÓN** `volumen_pendiente_norm` > `0.2325` → IC=+0.287 (n=656)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2325 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` < `1.4509` → IC=+0.233 (n=1175)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4509 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` > `2.2936` → IC=+0.242 (n=1597)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2936 (IC base=+0.236)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.250 (n=4024)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.236)

- **PATRÓN** `libro_liquidez` > `2033.8453` → IC=+0.240 (n=1215)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2033.8453 (IC base=+0.236)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.252 (n=2243)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 14.0 (IC base=+0.236)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.270 (n=3272)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0103 (IC base=+0.268)

- **PATRÓN** `sigma_h` > `0.0093` → IC=+0.271 (n=1485)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0093 (IC base=+0.268)

- **PATRÓN** `drift_60min` |x|≤ `0.1224` → IC=+0.295 (n=1440)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1224 (IC base=+0.268)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.269 (n=3393)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.268)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.272 (n=2952)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.268)

- **PATRÓN** `ibs_20min` < `0.5498` → IC=+0.286 (n=3271)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5498 (IC base=+0.268)

- **PATRÓN** `volumen_pendiente_norm` < `0.1607` → IC=+0.271 (n=3299)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1607 (IC base=+0.268)

- **PATRÓN** `volumen_pendiente_norm` > `0.2898` → IC=+0.286 (n=451)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2898 (IC base=+0.268)

- **PATRÓN** `volumen_spike_ratio` < `1.5631` → IC=+0.274 (n=1382)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5631 (IC base=+0.268)

- **PATRÓN** `volumen_spike_ratio` > `2.6455` → IC=+0.278 (n=1047)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6455 (IC base=+0.268)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.274 (n=2342)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.268)

- **PATRÓN** `libro_liquidez` > `1772.645` → IC=+0.278 (n=2181)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1772.645 (IC base=+0.268)

- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.279 (n=1171)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 8.0 (IC base=+0.268)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.179 (n=1250)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0032 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.0789` → IC=+0.146 (n=1247)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.0789 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.149 (n=3898)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 5.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` > `0.1952` → IC=+0.187 (n=3741)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.1952 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` > `0.3224` → IC=+0.198 (n=1200)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.3224 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.333` → IC=+0.167 (n=781)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 9.333 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `0.6364` → IC=+0.154 (n=1247)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.6364 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` > `1.0705` → IC=+0.142 (n=1696)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 1.0705 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.2713` → IC=+0.181 (n=528)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.2713 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `2.1714` → IC=+0.142 (n=3233)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.1714 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `1.5203` → IC=+0.142 (n=3282)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.5203 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `297.0` → IC=+0.152 (n=2412)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 297.0 (IC base=+0.137)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.164 (n=3251)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0065 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.0801` → IC=+0.170 (n=1082)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.0801 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.170 (n=1197)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` < `0.6766` → IC=+0.189 (n=3244)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.6766 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.998` → IC=+0.141 (n=1553)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 2.998 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.001` → IC=+0.141 (n=2932)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 4.001 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `1.0477` → IC=+0.153 (n=2854)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 1.0477 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.2196` → IC=+0.193 (n=601)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2196 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `2.4315` → IC=+0.147 (n=3134)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 2.4315 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `1.7696` → IC=+0.143 (n=2089)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.7696 (IC base=+0.140)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.141 (n=4215)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `221.0` → IC=+0.166 (n=1017)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 221.0 (IC base=+0.140)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.01` → IC=+0.240 (n=2535)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.01 (IC base=+0.228)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.237 (n=3978)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.228)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.228 (n=3394)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.228)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.302 (n=1416)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.228)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.985` → IC=+0.322 (n=847)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.985 (IC base=+0.228)

- **PATRÓN** `volumen_pendiente_norm` < `0.1321` → IC=+0.229 (n=3602)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1321 (IC base=+0.228)

- **PATRÓN** `volumen_pendiente_norm` > `0.3503` → IC=+0.231 (n=499)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3503 (IC base=+0.228)

- **PATRÓN** `volumen_spike_ratio` > `2.7497` → IC=+0.243 (n=1685)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7497 (IC base=+0.228)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.233 (n=4587)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.228)

- **PATRÓN** `libro_liquidez` > `2011.3382` → IC=+0.240 (n=1266)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2011.3382 (IC base=+0.228)

- **PATRÓN** `sigma_h` < `0.011` → IC=+0.250 (n=3208)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.011 (IC base=+0.245)

- **PATRÓN** `drift_60min` |x|≤ `0.178` → IC=+0.266 (n=1603)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.178 (IC base=+0.245)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.262 (n=1393)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.245)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.249 (n=1661)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.245)

- **PATRÓN** `ibs_20min` < `0.0625` → IC=+0.304 (n=1223)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0625 (IC base=+0.245)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.032` → IC=+0.305 (n=382)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.032 (IC base=+0.245)

- **PATRÓN** `volumen_pendiente_norm` > `0.3487` → IC=+0.304 (n=549)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3487 (IC base=+0.245)

- **PATRÓN** `volumen_spike_ratio` > `2.1738` → IC=+0.257 (n=2342)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1738 (IC base=+0.245)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.249 (n=1855)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.245)

- **PATRÓN** `libro_liquidez` > `1986.7` → IC=+0.258 (n=1214)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1986.7 (IC base=+0.245)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.251 (n=3031)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 21.0 (IC base=+0.245)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.193 (n=1325)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0038 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.4326` → IC=+0.145 (n=3946)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.4326 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.150 (n=4089)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 5.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` > `0.8842` → IC=+0.269 (n=1315)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8842 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` > `0.1963` → IC=+0.169 (n=1759)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.1963 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.072` → IC=+0.167 (n=599)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 11.072 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `0.6184` → IC=+0.161 (n=1316)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.6184 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.2331` → IC=+0.189 (n=699)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.2331 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `1.5173` → IC=+0.152 (n=1697)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 1.5173 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `2.1678` → IC=+0.143 (n=1749)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 2.1678 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `7294.6501` → IC=+0.240 (n=1315)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7294.6501 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `87.0` → IC=+0.145 (n=2578)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 87.0 (IC base=+0.137)

- **PATRÓN** `sigma_h` < `0.0078` → IC=+0.165 (n=3316)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0078 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.4368` → IC=+0.159 (n=3316)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.4368 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.175 (n=1227)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` < `0.7057` → IC=+0.199 (n=3318)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7057 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.007` → IC=+0.155 (n=654)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 9.007 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.028` → IC=+0.152 (n=2898)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` < 3.028 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `0.69` → IC=+0.167 (n=1459)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 0.69 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` > `0.2942` → IC=+0.215 (n=419)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2942 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `2.2097` → IC=+0.152 (n=2820)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.2097 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` > `1.5277` → IC=+0.156 (n=2863)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.5277 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `6526.3907` → IC=+0.224 (n=1106)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6526.3907 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `58.0` → IC=+0.173 (n=1119)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 58.0 (IC base=+0.149)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0127` → IC=+0.151 (n=1340)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` > 0.0127 (IC base=+0.115)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.147 (n=2840)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 11.0 (IC base=+0.115)

- **PATRÓN** `ibs_20min` > `0.4286` → IC=+0.186 (n=4023)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.4286 (IC base=+0.115)

- **PATRÓN** `dist_vwap_pct` > `1.0059` → IC=+0.200 (n=648)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0059 (IC base=+0.115)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.234` → IC=+0.273 (n=1019)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.234 (IC base=+0.115)

- **PATRÓN** `volumen_regimen` < `0.8751` → IC=+0.129 (n=2677)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 0.8751 (IC base=+0.115)

- **PATRÓN** `volumen_spike_ratio` < `1.8225` → IC=+0.123 (n=2613)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` < 1.8225 (IC base=+0.115)

- **PATRÓN** `libro_liquidez` > `2714.612` → IC=+0.240 (n=1339)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2714.612 (IC base=+0.115)

- **PATRÓN** `sigma_h` < `0.0109` → IC=+0.156 (n=3318)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0109 (IC base=+0.130)

- **PATRÓN** `drift_60min` |x|≤ `0.1384` → IC=+0.156 (n=1257)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.1384 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.165 (n=1777)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 15.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` < `0.6667` → IC=+0.219 (n=3781)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6667 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.039` → IC=+0.153 (n=3646)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` < 3.039 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` < `0.6403` → IC=+0.152 (n=1258)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.6403 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` > `0.2292` → IC=+0.191 (n=661)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.2292 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` < `1.437` → IC=+0.161 (n=1195)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 1.437 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `2608.5895` → IC=+0.213 (n=1256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2608.5895 (IC base=+0.130)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.143 (n=3591)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 49.0 (IC base=+0.130)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0136` → IC=+0.261 (n=3280)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0136 (IC base=+0.239)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.245 (n=3838)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.239)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.242 (n=3282)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.239)

- **PATRÓN** `ibs_20min` > `0.6145` → IC=+0.272 (n=3277)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6145 (IC base=+0.239)

- **PATRÓN** `dist_vwap_pct` > `0.1944` → IC=+0.252 (n=1859)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1944 (IC base=+0.239)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.148` → IC=+0.288 (n=644)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.148 (IC base=+0.239)

- **PATRÓN** `volumen_regimen` < `1.2171` → IC=+0.240 (n=3669)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2171 (IC base=+0.239)

- **PATRÓN** `volumen_regimen` > `0.6439` → IC=+0.244 (n=3669)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6439 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` > `0.2393` → IC=+0.252 (n=640)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2393 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` > `2.4984` → IC=+0.258 (n=1197)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4984 (IC base=+0.239)

- **PATRÓN** `libro_liquidez` > `2870.2927` → IC=+0.246 (n=1663)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2870.2927 (IC base=+0.239)

- **PATRÓN** `sigma_h` > `0.0256` → IC=+0.269 (n=1269)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0256 (IC base=+0.244)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.248 (n=3581)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.244)

- **PATRÓN** `ibs_20min` < `0.4387` → IC=+0.276 (n=3345)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4387 (IC base=+0.244)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.054` → IC=+0.278 (n=728)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.054 (IC base=+0.244)

- **PATRÓN** `volumen_regimen` < `0.7166` → IC=+0.246 (n=1675)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7166 (IC base=+0.244)

- **PATRÓN** `volumen_regimen` > `1.2141` → IC=+0.264 (n=1268)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2141 (IC base=+0.244)

- **PATRÓN** `volumen_pendiente_norm` > `0.286` → IC=+0.308 (n=525)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.286 (IC base=+0.244)

- **PATRÓN** `volumen_spike_ratio` > `1.4335` → IC=+0.248 (n=3591)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4335 (IC base=+0.244)

- **PATRÓN** `libro_liquidez` > `2975.74` → IC=+0.249 (n=1267)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2975.74 (IC base=+0.244)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.202 (n=6002)

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.243 (n=2207)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.222)

- **PATRÓN** `drift_60min` |x|≤ `0.5148` → IC=+0.231 (n=6612)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5148 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.229 (n=6663)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` > `0.9274` → IC=+0.257 (n=2204)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9274 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.473` → IC=+0.228 (n=2195)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.473 (IC base=+0.222)

- **PATRÓN** `volumen_regimen` < `0.7053` → IC=+0.231 (n=2109)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7053 (IC base=+0.222)

- **PATRÓN** `volumen_regimen` > `0.8791` → IC=+0.223 (n=3194)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8791 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` < `0.1045` → IC=+0.222 (n=6179)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1045 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` > `0.1652` → IC=+0.230 (n=1865)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1652 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` < `2.2576` → IC=+0.227 (n=5727)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.2576 (IC base=+0.222)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.226 (n=4869)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.222)

- **PATRÓN** `libro_liquidez` > `2584.218` → IC=+0.226 (n=6612)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2584.218 (IC base=+0.222)

- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.239 (n=1511)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.201)

- **PATRÓN** `drift_60min` |x|≤ `0.4997` → IC=+0.213 (n=4514)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4997 (IC base=+0.201)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.209 (n=1765)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.201)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.213 (n=2001)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.201)

- **PATRÓN** `ibs_20min` < `0.0865` → IC=+0.216 (n=1505)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0865 (IC base=+0.201)

- **PATRÓN** `dist_vwap_pct` > `0.6705` → IC=+0.210 (n=751)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6705 (IC base=+0.201)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.764` → IC=+0.214 (n=4068)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.764 (IC base=+0.201)

- **PATRÓN** `volumen_regimen` < `1.0967` → IC=+0.207 (n=3793)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0967 (IC base=+0.201)

- **PATRÓN** `volumen_pendiente_norm` < `0.0978` → IC=+0.202 (n=4158)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0978 (IC base=+0.201)

- **PATRÓN** `volumen_pendiente_norm` > `0.0733` → IC=+0.205 (n=2013)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0733 (IC base=+0.201)

- **PATRÓN** `volumen_spike_ratio` < `1.5329` → IC=+0.206 (n=1958)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5329 (IC base=+0.201)

- **PATRÓN** `volumen_spike_ratio` > `2.1886` → IC=+0.211 (n=2017)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1886 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.202 (n=6002)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.201)

- **PATRÓN** `ballena_activa_n` < `31.0` → IC=+0.224 (n=1967)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 31.0 (IC base=+0.201)

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
- **PATRÓN** `sigma_h` < `0.0083` → IC=+0.220 (n=1821)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0083 (IC base=+0.208)

- **PATRÓN** `drift_60min` |x|≤ `0.458` → IC=+0.215 (n=1820)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.458 (IC base=+0.208)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.233 (n=638)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.208)

- **PATRÓN** `ibs_20min` < `0.4744` → IC=+0.219 (n=1214)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4744 (IC base=+0.208)

- **PATRÓN** `ibs_20min` > `0.1447` → IC=+0.210 (n=1820)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1447 (IC base=+0.208)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.379` → IC=+0.214 (n=1846)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 6.379 (IC base=+0.208)

- **PATRÓN** `volumen_regimen` < `0.8665` → IC=+0.215 (n=1214)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8665 (IC base=+0.208)

- **PATRÓN** `volumen_pendiente_norm` < `0.1018` → IC=+0.211 (n=1679)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1018 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` < `1.4029` → IC=+0.227 (n=594)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4029 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` > `1.4931` → IC=+0.209 (n=1592)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4931 (IC base=+0.208)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.207 (n=1806)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.208)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.244 (n=478)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.202)

- **PATRÓN** `drift_60min` |x|≤ `0.4878` → IC=+0.221 (n=1426)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4878 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.205 (n=533)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.202)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.218 (n=967)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.202)

- **PATRÓN** `ibs_20min` < `0.171` → IC=+0.205 (n=628)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.171 (IC base=+0.202)

- **PATRÓN** `ibs_20min` > `0.6122` → IC=+0.208 (n=646)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6122 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` > `0.6265` → IC=+0.218 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6265 (IC base=+0.202)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.281` → IC=+0.207 (n=1303)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.281 (IC base=+0.202)

- **PATRÓN** `volumen_regimen` < `1.2492` → IC=+0.211 (n=1426)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2492 (IC base=+0.202)

- **PATRÓN** `volumen_pendiente_norm` > `0.0731` → IC=+0.229 (n=585)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0731 (IC base=+0.202)

- **PATRÓN** `volumen_spike_ratio` < `2.1843` → IC=+0.205 (n=1230)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1843 (IC base=+0.202)

- **PATRÓN** `volumen_spike_ratio` > `1.7864` → IC=+0.204 (n=932)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7864 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `6565.099` → IC=+0.207 (n=1273)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6565.099 (IC base=+0.202)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.240 (n=495)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0084 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.243 (n=1006)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` > `0.9863` → IC=+0.288 (n=375)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9863 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` > `0.7953` → IC=+0.233 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7953 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.186` → IC=+0.243 (n=612)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.186 (IC base=+0.212)

- **PATRÓN** `volumen_regimen` < `0.6434` → IC=+0.251 (n=375)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6434 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` < `0.1056` → IC=+0.217 (n=1018)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1056 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` > `0.2735` → IC=+0.226 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2735 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` < `2.1715` → IC=+0.225 (n=962)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1715 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `1.4737` → IC=+0.214 (n=1093)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4737 (IC base=+0.212)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.220 (n=1322)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `4344.7481` → IC=+0.256 (n=375)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4344.7481 (IC base=+0.212)

- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.248 (n=517)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0101 (IC base=+0.228)

- **PATRÓN** `drift_60min` |x|≤ `0.6329` → IC=+0.243 (n=775)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6329 (IC base=+0.228)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.231 (n=718)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.228)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.251 (n=535)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.228)

- **PATRÓN** `ibs_20min` < `0.6404` → IC=+0.254 (n=682)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6404 (IC base=+0.228)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.862` → IC=+0.248 (n=725)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.862 (IC base=+0.228)

- **PATRÓN** `volumen_regimen` < `0.758` → IC=+0.229 (n=341)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.758 (IC base=+0.228)

- **PATRÓN** `volumen_regimen` > `1.2826` → IC=+0.235 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2826 (IC base=+0.228)

- **PATRÓN** `volumen_pendiente_norm` < `0.0838` → IC=+0.238 (n=655)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0838 (IC base=+0.228)

- **PATRÓN** `volumen_spike_ratio` > `2.2105` → IC=+0.262 (n=343)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2105 (IC base=+0.228)

- **PATRÓN** `libro_liquidez` > `3838.455` → IC=+0.249 (n=516)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3838.455 (IC base=+0.228)

- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.263 (n=530)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 25.0 (IC base=+0.228)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.148 (n=763)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0038 (IC base=+0.054)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.184 (n=1465)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.75 (IC base=+0.054)

- **PATRÓN** `dist_vwap_pct` > `0.1459` → IC=+0.141 (n=1065)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.1459 (IC base=+0.054)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.347` → IC=+0.141 (n=489)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 10.347 (IC base=+0.054)

- **PATRÓN** `ibs_20min` < `0.0656` → IC=+0.261 (n=681)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0656 (IC base=+0.051)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.126 (n=635)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.63€ cuando `sigma_h` < 0.0053 (IC base=+0.070)

- **PATRÓN** `ibs_20min` > `0.5427` → IC=+0.163 (n=618)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` > 0.5427 (IC base=+0.070)

- **PATRÓN** `dist_vwap_pct` > `0.1227` → IC=+0.168 (n=323)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.1227 (IC base=+0.070)

- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.129 (n=278)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.64€ cuando `sigma_h` < 0.0035 (IC base=+0.043)

- **PATRÓN** `ibs_20min` < `0.0659` → IC=+0.254 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0659 (IC base=+0.043)

- **PATRÓN** `volumen_pendiente_norm` > `0.2173` → IC=+0.134 (n=121)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` > 0.2173 (IC base=+0.043)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` > `0.6693` → IC=-0.148 (n=163)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6693
  - _Potencial_: sin este filtro IC_bueno=+0.109 (n=492)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.151 (n=325)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0042 (IC base=+0.070)

- **PATRÓN** `ibs_20min` > `0.9375` → IC=+0.259 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9375 (IC base=+0.070)

- **PATRÓN** `dist_vwap_pct` > `0.1273` → IC=+0.169 (n=339)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.1273 (IC base=+0.070)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.623` → IC=+0.203 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.623 (IC base=+0.070)

- **PATRÓN** `ibs_20min` < `0.1105` → IC=+0.253 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1105 (IC base=+0.029)

### GBM_LATE_60M#SOL#60min
- **PATRÓN** `ibs_20min` > `0.981` → IC=+0.188 (n=264)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.981 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` > `0.4664` → IC=+0.127 (n=261)

  - _Acción_: Kelly boost +0.64€ cuando `dist_vwap_pct` > 0.4664 (IC base=+0.025)

- **PATRÓN** `sigma_h` < `0.0096` → IC=+0.185 (n=322)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0096 (IC base=+0.083)

- **PATRÓN** `ibs_20min` < `0.4857` → IC=+0.183 (n=452)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.4857 (IC base=+0.083)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.838` → IC=+0.296 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.838 (IC base=+0.083)

- **PATRÓN** `volumen_regimen` > `1.1079` → IC=+0.186 (n=151)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` > 1.1079 (IC base=+0.083)

- **PATRÓN** `volumen_pendiente_norm` > `0.1572` → IC=+0.167 (n=121)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.1572 (IC base=+0.083)

- **PATRÓN** `volumen_spike_ratio` > `2.5696` → IC=+0.143 (n=141)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 2.5696 (IC base=+0.083)

### GBM_LATE_60M_FADE
- **FILTRO** `hora_utc` > `7.0` → IC=-0.302 (n=94)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=291)

- **FILTRO** `dist_vwap_pct` > `0.2402` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2402
  - _Potencial_: sin este filtro IC_bueno=-0.220 (n=370)

- **FILTRO** `volumen_regimen` < `0.8582` → IC=-0.306 (n=127)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.8582
  - _Potencial_: sin este filtro IC_bueno=-0.185 (n=258)

- **FILTRO** `hora_utc` > `11.0` → IC=-0.309 (n=150)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=186)

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
- **FILTRO** `sigma_h` > `0.0054` → IC=-0.275 (n=38)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0054
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=75)

- **FILTRO** `hora_utc` > `9.0` → IC=-0.293 (n=27)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=86)

- **FILTRO** `sigma_ewma_delta_pct` > `9.679` → IC=-0.250 (n=18)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 9.679
  - _Potencial_: sin este filtro IC_bueno=-0.242 (n=95)

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

- **FILTRO** `ibs_20min` < `0.5872` → IC=-0.471 (n=33)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5872
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=99)

- **FILTRO** `sigma_h` > `0.0054` → IC=-0.379 (n=31)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0054
  - _Potencial_: sin este filtro IC_bueno=-0.280 (n=98)

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

- **FILTRO** `sigma_h` < `0.0115` → IC=-0.330 (n=45)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0115
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=15)

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
- **PATRÓN** `sigma_h` > `0.0087` → IC=+0.256 (n=244)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0087 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.190 (n=333)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 16.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` > `0.6732` → IC=+0.183 (n=732)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` > 0.6732 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` > `0.8076` → IC=+0.282 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8076 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.614` → IC=+0.158 (n=398)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 3.614 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `0.6244` → IC=+0.179 (n=244)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` < 0.6244 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` > `1.2135` → IC=+0.146 (n=244)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 1.2135 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` < `0.0705` → IC=+0.176 (n=547)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` < 0.0705 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `1.3986` → IC=+0.201 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3986 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.404` → IC=+0.158 (n=200)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 10.404 (IC base=+0.032)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.7234` → IC=-0.162 (n=72)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7234
  - _Potencial_: sin este filtro IC_bueno=+0.102 (n=219)

- **PATRÓN** `sigma_h` > `0.0065` → IC=+0.145 (n=74)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` > 0.0065 (IC base=+0.036)

- **PATRÓN** `ibs_20min` > `0.9081` → IC=+0.128 (n=146)

  - _Acción_: Kelly boost +0.64€ cuando `ibs_20min` > 0.9081 (IC base=+0.036)

- **PATRÓN** `dist_vwap_pct` > `0.6315` → IC=+0.191 (n=40)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.6315 (IC base=+0.036)

- **PATRÓN** `ibs_20min` < `0.2374` → IC=+0.148 (n=413)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` < 0.2374 (IC base=+0.089)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.162` → IC=+0.129 (n=95)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` > 11.162 (IC base=+0.089)

- **PATRÓN** `volumen_pendiente_norm` > `0.2751` → IC=+0.144 (n=71)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_pendiente_norm` > 0.2751 (IC base=+0.089)

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
- **FILTRO** `ibs_20min` > `0.1837` → IC=-0.235 (n=66)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1837
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=130)

- **FILTRO** `volumen_regimen` < `0.9199` → IC=-0.170 (n=98)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9199
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=98)

- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.294 (n=124)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0101 (IC base=+0.253)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.295 (n=193)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.253)

- **PATRÓN** `ibs_20min` > `0.6786` → IC=+0.289 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6786 (IC base=+0.253)

- **PATRÓN** `dist_vwap_pct` > `0.6947` → IC=+0.396 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6947 (IC base=+0.253)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.832` → IC=+0.359 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.832 (IC base=+0.253)

- **PATRÓN** `volumen_regimen` < `0.6071` → IC=+0.296 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6071 (IC base=+0.253)

- **PATRÓN** `volumen_pendiente_norm` > `0.0973` → IC=+0.328 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0973 (IC base=+0.253)

- **PATRÓN** `volumen_spike_ratio` < `1.396` → IC=+0.338 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.396 (IC base=+0.253)

- **PATRÓN** `volumen_spike_ratio` > `2.3472` → IC=+0.311 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3472 (IC base=+0.253)

### LATE_WINDOW_5MIN
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.329 (n=121)

- **PATRÓN** `drift_ventana_pct` |x|> `0.349` → IC=+0.324 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.349 (IC base=+0.317)

- **PATRÓN** `elapsed_s` > `207.7` → IC=+0.385 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 207.7 (IC base=+0.317)

- **PATRÓN** `drift_15min` |x|≤ `1.0295` → IC=+0.406 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0295 (IC base=+0.317)

- **PATRÓN** `drift_60min` |x|≤ `0.7805` → IC=+0.375 (n=78)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.7805 (IC base=+0.317)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.381 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.317)

- **PATRÓN** `ballena_activa_n` < `1220.0` → IC=+0.354 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1220.0 (IC base=+0.317)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3488` → IC=+0.300 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3488 (IC base=+0.271)

- **PATRÓN** `elapsed_s` > `229.9` → IC=+0.338 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 229.9 (IC base=+0.271)

- **PATRÓN** `drift_15min` |x|≤ `2.3044` → IC=+0.319 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3044 (IC base=+0.271)

- **PATRÓN** `drift_60min` |x|≤ `0.6424` → IC=+0.319 (n=70)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6424 (IC base=+0.271)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.329 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.271)

- **PATRÓN** `ballena_activa_n` < `1342.0` → IC=+0.361 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1342.0 (IC base=+0.271)

### LATE_WINDOW_5MIN#BTC#5min
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.329 (n=121)

- **PATRÓN** `drift_ventana_pct` |x|> `0.349` → IC=+0.324 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.349 (IC base=+0.317)

- **PATRÓN** `elapsed_s` > `207.7` → IC=+0.385 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 207.7 (IC base=+0.317)

- **PATRÓN** `drift_15min` |x|≤ `1.0295` → IC=+0.406 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0295 (IC base=+0.317)

- **PATRÓN** `drift_60min` |x|≤ `0.7805` → IC=+0.375 (n=78)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.7805 (IC base=+0.317)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.381 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.317)

- **PATRÓN** `ballena_activa_n` < `1220.0` → IC=+0.354 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1220.0 (IC base=+0.317)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3488` → IC=+0.300 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3488 (IC base=+0.271)

- **PATRÓN** `elapsed_s` > `229.9` → IC=+0.338 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 229.9 (IC base=+0.271)

- **PATRÓN** `drift_15min` |x|≤ `2.3044` → IC=+0.319 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3044 (IC base=+0.271)

- **PATRÓN** `drift_60min` |x|≤ `0.6424` → IC=+0.319 (n=70)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6424 (IC base=+0.271)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.329 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.271)

- **PATRÓN** `ballena_activa_n` < `1342.0` → IC=+0.361 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1342.0 (IC base=+0.271)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.124 (n=1469)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` > 0.5 (IC base=+0.098)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.124 (n=1469)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` > 0.5 (IC base=+0.098)

### LIQUIDACIONES_15M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=251)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=251)

- **FILTRO** `libro_liquidez` < `3501.0925` → IC=-0.178 (n=88)

  - _Acción_: SKIP cuando `libro_liquidez` < 3501.0925
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=179)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=961)

### LIQUIDACIONES_15M#BNB#15min
- **PATRÓN** `liq_usd_total` > `2348.39` → IC=+0.269 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `liq_usd_total` > 2348.39 (IC base=+0.071)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.179 (n=26)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 5.0 (IC base=+0.071)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.123 (n=59)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.03 (IC base=+0.071)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `libro_liquidez` < `12324.2702` → IC=-0.152 (n=44)

  - _Acción_: SKIP cuando `libro_liquidez` < 12324.2702
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=91)

### LIQUIDACIONES_15M#DOGE#15min
- **PATRÓN** `hora_utc` < `11.0` → IC=+0.150 (n=38)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 11.0 (IC base=+0.061)

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
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=256)

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
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=3965)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=164)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.077 (n=121)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.278 (n=34)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=151)

- **FILTRO** `ballena_activa_n` > `69.0` → IC=-0.175 (n=75)

  - _Acción_: SKIP cuando `ballena_activa_n` > 69.0
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=76)

- **PATRÓN** `ballena_activa_n` < `69.0` → IC=+0.167 (n=76)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 69.0 (IC base=-0.045)

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
- **PATRÓN** `liq_n` > `3.0` → IC=+0.389 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `liq_n` > 3.0 (IC base=+0.235)

- **PATRÓN** `liq_usd_total` > `2564.96` → IC=+0.386 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `liq_usd_total` > 2564.96 (IC base=+0.235)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.275 (n=38)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.235)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.236 (n=51)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 13.0 (IC base=+0.235)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.229 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.5 (IC base=+0.235)

- **PATRÓN** `libro_liquidez` > `2416.648` → IC=+0.266 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2416.648 (IC base=+0.235)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=1611)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=1565)

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
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=450)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=431)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.145 (n=195)

  - _Acción_: Kelly boost +0.72€ cuando `py_entrada` < 0.495 (IC base=+0.024)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=1025)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=1025)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=1316)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=1316)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=297)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=297)

- **FILTRO** `py_entrada` < `0.42` → IC=-0.141 (n=76)

  - _Acción_: SKIP cuando `py_entrada` < 0.42
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=236)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.136 (n=64)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=361)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=410)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=306)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=407)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=407)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.120 (n=185)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=252)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=376)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.190 (n=85)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=104)

- **FILTRO** `hora_utc` > `14.0` → IC=-0.159 (n=83)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=106)

- **FILTRO** `py_entrada` > `0.52` → IC=-0.121 (n=56)

  - _Acción_: SKIP cuando `py_entrada` > 0.52
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=30)

- **FILTRO** `hora_utc` < `17.0` → IC=-0.131 (n=63)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=23)

### LIQUIDACIONES_DEPTH_FASE0#BTC#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.132 (n=305)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=770)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **FILTRO** `py_entrada` > `0.57` → IC=-0.129 (n=437)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.085 (n=526)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.146 (n=320)

  - _Acción_: Kelly boost +0.73€ cuando `py_entrada` < 0.5 (IC base=-0.012)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.121 (n=167)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=365)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` > `0.57` → IC=-0.121 (n=375)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.075 (n=386)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.120 (n=551)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=595)

- **FILTRO** `py_entrada` > `0.58` → IC=-0.129 (n=351)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=420)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.139 (n=278)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=609)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.41` → IC=-0.156 (n=350)

  - _Acción_: SKIP cuando `py_entrada` < 0.41
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=732)

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
- **FILTRO** `py_entrada` < `0.46` → IC=-0.176 (n=8120)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=25830)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.173 (n=8598)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=26533)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.195 (n=1514)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=4786)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.146 (n=2096)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.095 (n=4130)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.135 (n=1618)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` > 1.0 (IC base=+0.040)

- **PATRÓN** `py_entrada` < `0.505` → IC=+0.128 (n=3162)

  - _Acción_: Kelly boost +0.64€ cuando `py_entrada` < 0.505 (IC base=+0.013)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` < `0.44` → IC=-0.174 (n=1129)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=3565)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.180 (n=1214)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=3729)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` > `0.62` → IC=-0.199 (n=1563)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=4821)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.137 (n=1936)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` > 1.0 (IC base=+0.034)

- **PATRÓN** `libro_liquidez` > `1736.5054` → IC=+0.121 (n=2137)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 1736.5054 (IC base=+0.034)

### MOMENTUM_IBS_15M_BALLENA#ETH#15min
- **FILTRO** `py_entrada` > `0.575` → IC=-0.177 (n=1238)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=3776)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.485` → IC=-0.161 (n=1568)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=4760)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=2444)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.162 (n=772)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=2368)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.180 (n=973)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=3103)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=4055)

- **FILTRO** `ballena_activa_n` > `32.0` → IC=-0.127 (n=1366)

  - _Acción_: SKIP cuando `ballena_activa_n` > 32.0
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=2677)

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
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=1092)

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
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=976)

- **FILTRO** `ballena_activa_n` > `23.0` → IC=-0.191 (n=390)

  - _Acción_: SKIP cuando `ballena_activa_n` > 23.0
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=802)

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

### MOMENTUM_IBS_5M_BALLENA
- **FILTRO** `hora_utc` < `8.0` → IC=-0.136 (n=23086)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.091 (n=52112)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.298 (n=18134)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=57064)

- **FILTRO** `ibs_7min` < `0.2143` → IC=-0.235 (n=18748)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2143
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=56450)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.153 (n=25469)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=49729)

- **FILTRO** `py_entrada` > `0.68` → IC=-0.253 (n=21946)

  - _Acción_: SKIP cuando `py_entrada` > 0.68
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=72085)

- **FILTRO** `ibs_7min` > `0.2816` → IC=-0.184 (n=23502)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2816
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=70529)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.159 (n=3242)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=10177)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.318 (n=3329)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=10090)

- **FILTRO** `ibs_7min` < `0.7095` → IC=-0.254 (n=4427)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7095
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=8992)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.153 (n=2801)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=10618)

- **FILTRO** `py_entrada` > `0.72` → IC=-0.279 (n=3967)

  - _Acción_: SKIP cuando `py_entrada` > 0.72
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=12266)

- **FILTRO** `ibs_7min` > `0.7764` → IC=-0.210 (n=4058)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7764
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=12175)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.122 (n=3015)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.102 (n=9480)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.264 (n=3023)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=9472)

- **FILTRO** `ibs_7min` < `0.7131` → IC=-0.211 (n=3123)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7131
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=9372)

- **FILTRO** `ballena_activa_n` > `156.0` → IC=-0.202 (n=3121)

  - _Acción_: SKIP cuando `ballena_activa_n` > 156.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=9374)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.267 (n=2926)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9844)

- **FILTRO** `ibs_7min` > `0.2655` → IC=-0.192 (n=3192)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2655
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=9578)

- **FILTRO** `ballena_activa_n` > `153.0` → IC=-0.180 (n=3175)

  - _Acción_: SKIP cuando `ballena_activa_n` > 153.0
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=9595)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.166 (n=3095)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=9776)

- **FILTRO** `py_entrada` < `0.3` → IC=-0.325 (n=3069)

  - _Acción_: SKIP cuando `py_entrada` < 0.3
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=9802)

- **FILTRO** `ibs_7min` < `0.2857` → IC=-0.250 (n=4235)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2857
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=8636)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.202 (n=2536)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=10335)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.260 (n=4161)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=13049)

- **FILTRO** `ibs_7min` > `0.7296` → IC=-0.183 (n=4302)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7296
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=12908)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.263 (n=3027)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=9127)

- **FILTRO** `ibs_7min` < `0.7136` → IC=-0.198 (n=3037)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7136
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=9117)

- **FILTRO** `ballena_activa_n` > `25.0` → IC=-0.192 (n=2939)

  - _Acción_: SKIP cuando `ballena_activa_n` > 25.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=9215)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.260 (n=2945)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=9714)

- **FILTRO** `ibs_7min` > `0.2727` → IC=-0.178 (n=3164)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2727
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=9495)

- **FILTRO** `ballena_activa_n` > `24.0` → IC=-0.173 (n=3057)

  - _Acción_: SKIP cuando `ballena_activa_n` > 24.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=9602)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.32` → IC=-0.300 (n=2881)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=9154)

- **FILTRO** `ibs_7min` < `0.7` → IC=-0.236 (n=3929)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=8106)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.218 (n=2949)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=9086)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.199 (n=4412)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=13769)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.134 (n=3941)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.109 (n=8283)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.310 (n=2935)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=9289)

- **FILTRO** `ibs_7min` < `0.733` → IC=-0.222 (n=4033)

  - _Acción_: SKIP cuando `ibs_7min` < 0.733
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=8191)

- **FILTRO** `ballena_activa_n` > `9.0` → IC=-0.206 (n=2710)

  - _Acción_: SKIP cuando `ballena_activa_n` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.091 (n=9514)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.228 (n=4236)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=12742)

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

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=1458)

- **FILTRO** `py_entrada` > `0.565` → IC=-0.172 (n=260)

  - _Acción_: SKIP cuando `py_entrada` > 0.565
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=906)

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

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.4308` → IC=+0.148 (n=696)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.74€ cuando `delta_ratio` |x|> 0.4308 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.129 (n=1383)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 14.0 (IC base=+0.124)

- **PATRÓN** `total_vol_5m` < `421.9116` → IC=+0.160 (n=512)

  - _Acción_: Kelly boost +0.80€ cuando `total_vol_5m` < 421.9116 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `3557.0392` → IC=+0.138 (n=696)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 3557.0392 (IC base=+0.124)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `14.0` → IC=+0.181 (n=183)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 14.0 (IC base=+0.134)

- **PATRÓN** `total_vol_5m` < `287.685` → IC=+0.165 (n=243)

  - _Acción_: Kelly boost +0.83€ cuando `total_vol_5m` < 287.685 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `2507.387` → IC=+0.240 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2507.387 (IC base=+0.134)

- **PATRÓN** `ballena_activa_n` < `6.0` → IC=+0.137 (n=177)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 6.0 (IC base=+0.134)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `delta_ratio` |x|> `0.4312` → IC=+0.148 (n=143)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.74€ cuando `delta_ratio` |x|> 0.4312 (IC base=+0.121)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.143 (n=278)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 14.0 (IC base=+0.121)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.126 (n=383)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.04 (IC base=+0.121)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4164` → IC=+0.172 (n=193)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.86€ cuando `delta_ratio` |x|> 0.4164 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.147 (n=267)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.125)

- **PATRÓN** `total_vol_5m` < `857.788` → IC=+0.149 (n=289)

  - _Acción_: Kelly boost +0.75€ cuando `total_vol_5m` < 857.788 (IC base=+0.125)

- **PATRÓN** `ballena_activa_n` < `59.0` → IC=+0.167 (n=97)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 59.0 (IC base=+0.125)

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
- **PATRÓN** `hora_utc` < `14.0` → IC=+0.129 (n=281)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 14.0 (IC base=+0.100)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.134 (n=203)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.100)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `7.3154` → IC=-0.250 (n=58)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 7.3154
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=176)

- **FILTRO** `pct_vs_K` |x|> `3.395` → IC=-0.182 (n=297)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.395
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=581)

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.147 (n=290)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0045 (IC base=-0.057)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `pct_vs_K` |x|> `4.2538` → IC=-0.246 (n=65)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.2538
  - _Potencial_: sin este filtro IC_bueno=+0.067 (n=199)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.291 (n=89)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=-0.011)

- **PATRÓN** `pct_vs_K` |x|≤ `1.7678` → IC=+0.192 (n=89)

  - _Acción_: Kelly boost +0.96€ cuando `pct_vs_K` |x|≤ 1.7678 (IC base=-0.011)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `sigma_h` > `0.0107` → IC=-0.136 (n=20)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0107
  - _Potencial_: sin este filtro IC_bueno=-0.121 (n=64)

- **FILTRO** `T_h` < `251.7955` → IC=-0.192 (n=63)

  - _Acción_: SKIP cuando `T_h` < 251.7955
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=21)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `T_h` < `67.1996` → IC=-0.167 (n=55)

  - _Acción_: SKIP cuando `T_h` < 67.1996
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=114)

### PRICE_TARGET_GBM#SOL#reach
- **FILTRO** `T_h` < `146.0708` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `T_h` < 146.0708
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=16)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0114` → IC=-0.236 (n=597)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0114
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=200)

- **FILTRO** `T_h` > `67.5869` → IC=-0.229 (n=533)

  - _Acción_: SKIP cuando `T_h` > 67.5869
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=264)

- **FILTRO** `pct_vs_K` |x|> `3.0348` → IC=-0.397 (n=173)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.0348
  - _Potencial_: sin este filtro IC_bueno=-0.103 (n=520)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `T_h` < `60.8769` → IC=-0.213 (n=85)

  - _Acción_: SKIP cuando `T_h` < 60.8769
  - _Potencial_: sin este filtro IC_bueno=-0.193 (n=177)

- **FILTRO** `T_h` > `143.4421` → IC=-0.223 (n=63)

  - _Acción_: SKIP cuando `T_h` > 143.4421
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=192)

- **FILTRO** `pct_vs_K` |x|> `1.8713` → IC=-0.337 (n=127)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 1.8713
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=128)

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
- **FILTRO** `sigma_h` < `0.0101` → IC=-0.308 (n=149)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0101
  - _Potencial_: sin este filtro IC_bueno=-0.225 (n=78)

- **FILTRO** `T_h` > `49.9834` → IC=-0.285 (n=170)

  - _Acción_: SKIP cuando `T_h` > 49.9834
  - _Potencial_: sin este filtro IC_bueno=-0.263 (n=57)

- **FILTRO** `sigma_h` < `0.0055` → IC=-0.204 (n=52)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0055
  - _Potencial_: sin este filtro IC_bueno=-0.129 (n=157)

- **FILTRO** `pct_vs_K` |x|> `2.0709` → IC=-0.386 (n=103)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.0709
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=106)

- **PATRÓN** `pct_vs_K` |x|≤ `0.9112` → IC=+0.209 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `pct_vs_K` |x|≤ 0.9112 (IC base=-0.149)

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
- **FILTRO** `sigma_h` < `0.0083` → IC=-0.254 (n=55)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0083
  - _Potencial_: sin este filtro IC_bueno=-0.176 (n=168)

- **FILTRO** `T_h` > `64.9601` → IC=-0.222 (n=167)

  - _Acción_: SKIP cuando `T_h` > 64.9601
  - _Potencial_: sin este filtro IC_bueno=-0.121 (n=56)

- **FILTRO** `sigma_h` > `0.014` → IC=-0.311 (n=51)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.014
  - _Potencial_: sin este filtro IC_bueno=-0.131 (n=101)

- **FILTRO** `sigma_h` < `0.0104` → IC=-0.269 (n=50)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0104
  - _Potencial_: sin este filtro IC_bueno=-0.154 (n=102)

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
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=437)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.074 (n=484)

- **PATRÓN** `streak_estiramiento` < `0.8196` → IC=+0.130 (n=333)

  - _Acción_: Kelly boost +0.65€ cuando `streak_estiramiento` < 0.8196 (IC base=+0.062)

- **PATRÓN** `ballena_activa_n` < `29.0` → IC=+0.125 (n=246)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 29.0 (IC base=+0.062)

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
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=179)

- **PATRÓN** `streak_estiramiento` < `0.2356` → IC=+0.123 (n=67)

  - _Acción_: Kelly boost +0.62€ cuando `streak_estiramiento` < 0.2356 (IC base=+0.034)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.142 (n=121)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 11.0 (IC base=+0.096)

- **PATRÓN** `streak_estiramiento` < `0.5577` → IC=+0.169 (n=161)

  - _Acción_: Kelly boost +0.84€ cuando `streak_estiramiento` < 0.5577 (IC base=+0.096)

- **PATRÓN** `ballena_activa_n` < `31.0` → IC=+0.158 (n=156)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 31.0 (IC base=+0.096)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `9.0` → IC=-0.197 (n=31)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=107)

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
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=1079)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=1348)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=1244)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=1296)

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
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=5034)

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
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=2908)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.188 (n=1840)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0054 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.2216` → IC=+0.158 (n=5519)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.2216 (IC base=+0.139)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1346` → IC=+0.154 (n=2276)

  - _Acción_: Kelly boost +0.77€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1346 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.149 (n=5093)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 6.0 (IC base=+0.139)

- **PATRÓN** `ibs_15` > `0.5762` → IC=+0.221 (n=4930)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5762 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.1352` → IC=+0.130 (n=2563)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` > 0.1352 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.315` → IC=+0.244 (n=1044)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.315 (IC base=+0.139)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=3128)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `4519.8806` → IC=+0.169 (n=1840)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 4519.8806 (IC base=+0.139)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=2128)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.220 (n=805)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.201)

- **PATRÓN** `drift_60min` |x|≤ `0.0769` → IC=+0.250 (n=354)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0769 (IC base=+0.201)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2675` → IC=+0.222 (n=268)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2675 (IC base=+0.201)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.228 (n=738)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.201)

- **PATRÓN** `ibs_15` > `0.7082` → IC=+0.272 (n=804)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7082 (IC base=+0.201)

- **PATRÓN** `dist_vwap_pct` > `0.3749` → IC=+0.225 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3749 (IC base=+0.201)

- **PATRÓN** `dist_vwap_pct` < `0.1096` → IC=+0.203 (n=543)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1096 (IC base=+0.201)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.41` → IC=+0.313 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.41 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.204 (n=1042)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.201)

- **PATRÓN** `libro_liquidez` > `11847.0948` → IC=+0.221 (n=536)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11847.0948 (IC base=+0.201)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.146 (n=1010)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0071 (IC base=+0.131)

- **PATRÓN** `drift_60min` |x|≤ `0.1094` → IC=+0.150 (n=675)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.1094 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.137 (n=923)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 6.0 (IC base=+0.131)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.132 (n=1011)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 16.0 (IC base=+0.131)

- **PATRÓN** `ibs_15` > `0.4932` → IC=+0.218 (n=1010)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.4932 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` > `0.1186` → IC=+0.152 (n=627)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.1186 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.945` → IC=+0.282 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.945 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `6020.1719` → IC=+0.172 (n=458)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 6020.1719 (IC base=+0.131)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `ibs_15` > `0.7632` → IC=+0.130 (n=715)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.65€ cuando `ibs_15` > 0.7632 (IC base=+0.051)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` < `0.0252` → IC=+0.164 (n=1386)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0252 (IC base=+0.152)

- **PATRÓN** `sigma_h` > `0.0127` → IC=+0.156 (n=1386)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0127 (IC base=+0.152)

- **PATRÓN** `drift_60min` |x|≤ `0.2255` → IC=+0.176 (n=1386)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.2255 (IC base=+0.152)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0972` → IC=+0.215 (n=429)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0972 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.159 (n=1271)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 6.0 (IC base=+0.152)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.155 (n=1220)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 14.0 (IC base=+0.152)

- **PATRÓN** `ibs_15` > `0.5417` → IC=+0.222 (n=1239)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5417 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` > `0.5403` → IC=+0.181 (n=315)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.5403 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.913` → IC=+0.192 (n=313)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 17.913 (IC base=+0.152)

- **PATRÓN** `libro_liquidez` > `2947.1379` → IC=+0.198 (n=628)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 2947.1379 (IC base=+0.152)

- **PATRÓN** `ibs_15` < `0.1111` → IC=+0.151 (n=1069)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.75€ cuando `ibs_15` < 0.1111 (IC base=+0.068)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` > `0.0054` → IC=+0.396 (n=344)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0054 (IC base=+0.364)

- **PATRÓN** `drift_60min` |x|≤ `0.1114` → IC=+0.364 (n=506)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1114 (IC base=+0.364)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1501` → IC=+0.378 (n=506)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1501 (IC base=+0.364)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1351` → IC=+0.379 (n=296)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1351 (IC base=+0.364)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.373 (n=799)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.364)

- **PATRÓN** `ibs_15` > `0.7883` → IC=+0.392 (n=759)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7883 (IC base=+0.364)

- **PATRÓN** `dist_vwap_pct` > `0.1529` → IC=+0.380 (n=449)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1529 (IC base=+0.364)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.976` → IC=+0.396 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.976 (IC base=+0.364)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.367 (n=924)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.364)

- **PATRÓN** `libro_liquidez` > `9610.6074` → IC=+0.382 (n=344)

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
- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.368 (n=391)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.364)

- **PATRÓN** `sigma_h` > `0.006` → IC=+0.383 (n=177)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.006 (IC base=+0.364)

- **PATRÓN** `drift_60min` |x|≤ `0.1075` → IC=+0.367 (n=261)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1075 (IC base=+0.364)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1293` → IC=+0.382 (n=261)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1293 (IC base=+0.364)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.296` → IC=+0.372 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.296 (IC base=+0.364)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.370 (n=390)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.364)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.370 (n=183)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.364)

- **PATRÓN** `ibs_15` > `0.7632` → IC=+0.393 (n=390)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7632 (IC base=+0.364)

- **PATRÓN** `dist_vwap_pct` > `0.1212` → IC=+0.372 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1212 (IC base=+0.364)

- **PATRÓN** `dist_vwap_pct` < `0.2773` → IC=+0.364 (n=358)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2773 (IC base=+0.364)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.991` → IC=+0.393 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.991 (IC base=+0.364)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.367 (n=443)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.364)

- **PATRÓN** `libro_liquidez` > `4158.7318` → IC=+0.377 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4158.7318 (IC base=+0.364)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0075` → IC=-0.200 (n=2753)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0075
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=2755)

- **FILTRO** `drift_15min` |x|> `0.913` → IC=-0.151 (n=1376)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.913
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=4131)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.221 (n=2328)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=3180)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1412` → IC=+0.212 (n=473)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1412 (IC base=-0.084)

- **PATRÓN** `ibs_15` > `0.6306` → IC=+0.277 (n=1247)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6306 (IC base=-0.084)

- **PATRÓN** `dist_vwap_pct` > `0.1107` → IC=+0.200 (n=727)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1107 (IC base=-0.084)

- **PATRÓN** `dist_vwap_pct` < `0.2602` → IC=+0.197 (n=1073)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` < 0.2602 (IC base=-0.084)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2338` → IC=+0.270 (n=1691)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2338 (IC base=-0.003)

- **PATRÓN** `ibs_15` < `0.3704` → IC=+0.286 (n=5070)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3704 (IC base=-0.003)

- **PATRÓN** `dist_vwap_pct` > `0.655` → IC=+0.281 (n=695)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.655 (IC base=-0.003)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0322` → IC=-0.221 (n=2625)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0322
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=878)

- **FILTRO** `sigma_h` < `0.0038` → IC=-0.216 (n=875)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0038
  - _Potencial_: sin este filtro IC_bueno=-0.175 (n=2628)

- **FILTRO** `sigma_ewma_delta_pct` > `22.22` → IC=-0.251 (n=496)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 22.22
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=3007)

- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.153 (n=335)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0031 (IC base=+0.069)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2668` → IC=+0.277 (n=146)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2668 (IC base=+0.069)

- **PATRÓN** `ibs_15` > `0.7609` → IC=+0.318 (n=437)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7609 (IC base=+0.069)

- **PATRÓN** `dist_vwap_pct` > `0.1039` → IC=+0.274 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1039 (IC base=+0.069)

- **PATRÓN** `dist_vwap_pct` < `0.2432` → IC=+0.277 (n=393)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2432 (IC base=+0.069)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.088` → IC=+0.150 (n=224)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 22.088 (IC base=+0.069)

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
  - _Potencial_: sin este filtro IC_bueno=+0.152 (n=817)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.160 (n=551)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0059 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.159` → IC=+0.164 (n=551)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.159 (IC base=+0.146)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3014` → IC=+0.196 (n=491)

  - _Acción_: Kelly boost +0.98€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3014 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.162 (n=447)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 11.0 (IC base=+0.146)

- **PATRÓN** `ibs_15` > `0.5679` → IC=+0.240 (n=626)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5679 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.6245` → IC=+0.161 (n=116)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 0.6245 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` < `0.2672` → IC=+0.147 (n=584)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.2672 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.001` → IC=+0.258 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.001 (IC base=+0.146)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=817)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `7306.8584` → IC=+0.161 (n=284)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 7306.8584 (IC base=+0.146)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.253 (n=1312)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0061 (IC base=+0.244)

- **PATRÓN** `drift_60min` |x|≤ `0.3569` → IC=+0.249 (n=1731)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3569 (IC base=+0.244)

- **PATRÓN** `drift_15min` |x|≤ `0.7826` → IC=+0.259 (n=1732)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7826 (IC base=+0.244)

- **PATRÓN** `delta_ratio_macro` |x|> `0.212` → IC=+0.264 (n=892)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.212 (IC base=+0.244)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.255 (n=727)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.244)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.244 (n=1347)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.244)

- **PATRÓN** `ibs_15` < `0.1863` → IC=+0.304 (n=1312)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.1863 (IC base=+0.244)

- **PATRÓN** `dist_vwap_pct` > `0.3774` → IC=+0.273 (n=482)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3774 (IC base=+0.244)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.334` → IC=+0.247 (n=761)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.334 (IC base=+0.244)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1869` → IC=-0.271 (n=321)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1869
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=967)

- **FILTRO** `sigma_h` > `0.0105` → IC=-0.240 (n=437)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0105
  - _Potencial_: sin este filtro IC_bueno=-0.183 (n=851)

- **FILTRO** `drift_60min` |x|> `0.1723` → IC=-0.270 (n=437)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1723
  - _Potencial_: sin este filtro IC_bueno=-0.168 (n=851)

- **FILTRO** `drift_15min` |x|> `0.912` → IC=-0.289 (n=321)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.912
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=967)

- **FILTRO** `sigma_ewma_delta_pct` > `16.965` → IC=-0.134 (n=678)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 16.965
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=5421)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1478` → IC=+0.188 (n=46)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.94€ cuando `delta_ratio_macro` |x|> 0.1478 (IC base=-0.203)

- **PATRÓN** `ibs_15` > `0.9231` → IC=+0.380 (n=23)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9231 (IC base=-0.203)

- **PATRÓN** `dist_vwap_pct` < `0.1327` → IC=+0.167 (n=55)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.1327 (IC base=-0.203)

- **PATRÓN** `ibs_15` < `0.381` → IC=+0.297 (n=868)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.381 (IC base=-0.029)

- **PATRÓN** `dist_vwap_pct` > `0.6883` → IC=+0.243 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6883 (IC base=-0.029)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.1527` → IC=-0.245 (n=391)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1527
  - _Potencial_: sin este filtro IC_bueno=-0.211 (n=1177)

- **FILTRO** `drift_15min` |x|> `1.2607` → IC=-0.276 (n=391)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.2607
  - _Potencial_: sin este filtro IC_bueno=-0.201 (n=1177)

- **FILTRO** `sigma_ewma_delta_pct` > `7.452` → IC=-0.221 (n=481)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 7.452
  - _Potencial_: sin este filtro IC_bueno=-0.219 (n=1087)

- **FILTRO** `libro_spread` > `0.04` → IC=-0.273 (n=20)

  - _Acción_: SKIP cuando `libro_spread` > 0.04
  - _Potencial_: sin este filtro IC_bueno=-0.219 (n=1548)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.220)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.220)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1695` → IC=+0.279 (n=550)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1695 (IC base=-0.015)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1183` → IC=+0.302 (n=528)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1183 (IC base=-0.015)

- **PATRÓN** `ibs_15` < `0.137` → IC=+0.312 (n=808)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.137 (IC base=-0.015)

- **PATRÓN** `dist_vwap_pct` > `0.7641` → IC=+0.332 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7641 (IC base=-0.015)

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
- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.300 (n=458)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0033 (IC base=+0.282)

- **PATRÓN** `drift_60min` |x|≤ `0.0716` → IC=+0.312 (n=604)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0716 (IC base=+0.282)

- **PATRÓN** `delta_ratio_macro` |x|> `0.152` → IC=+0.283 (n=915)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.152 (IC base=+0.282)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2224` → IC=+0.289 (n=838)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2224 (IC base=+0.282)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.295 (n=1420)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.282)

- **PATRÓN** `ibs_15` > `0.838` → IC=+0.310 (n=1374)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.838 (IC base=+0.282)

- **PATRÓN** `dist_vwap_pct` > `0.2627` → IC=+0.313 (n=592)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2627 (IC base=+0.282)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.932` → IC=+0.388 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.932 (IC base=+0.282)

- **PATRÓN** `libro_liquidez` > `13151.6029` → IC=+0.302 (n=458)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13151.6029 (IC base=+0.282)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.301 (n=319)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.275)

- **PATRÓN** `drift_60min` |x|≤ `0.0772` → IC=+0.301 (n=319)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0772 (IC base=+0.275)

- **PATRÓN** `drift_15min` |x|≤ `0.3844` → IC=+0.276 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3844 (IC base=+0.275)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2694` → IC=+0.279 (n=242)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2694 (IC base=+0.275)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3948` → IC=+0.280 (n=652)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3948 (IC base=+0.275)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.294 (n=759)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.275)

- **PATRÓN** `ibs_15` > `0.829` → IC=+0.299 (n=726)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.829 (IC base=+0.275)

- **PATRÓN** `dist_vwap_pct` > `0.2522` → IC=+0.310 (n=309)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2522 (IC base=+0.275)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.742` → IC=+0.395 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.742 (IC base=+0.275)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.276 (n=937)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.275)

- **PATRÓN** `libro_liquidez` > `15759.911` → IC=+0.311 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15759.911 (IC base=+0.275)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.294 (n=649)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0069 (IC base=+0.289)

- **PATRÓN** `drift_60min` |x|≤ `0.0506` → IC=+0.322 (n=217)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0506 (IC base=+0.289)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1009` → IC=+0.314 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1009 (IC base=+0.289)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.299 (n=621)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.289)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.290 (n=459)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.289)

- **PATRÓN** `ibs_15` > `0.8475` → IC=+0.317 (n=648)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8475 (IC base=+0.289)

- **PATRÓN** `dist_vwap_pct` > `0.2773` → IC=+0.316 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2773 (IC base=+0.289)

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
  - _Potencial_: sin este filtro IC_bueno=-0.091 (n=370)

- **FILTRO** `ballena_activa_n` > `60.0` → IC=-0.229 (n=57)

  - _Acción_: SKIP cuando `ballena_activa_n` > 60.0
  - _Potencial_: sin este filtro IC_bueno=-0.138 (n=175)

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

- **FILTRO** `delta_ratio_macro` |x|≤ `0.2685` → IC=-0.375 (n=22)
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
- **PATRÓN** `ratio` < `0.9701` → IC=+0.375 (n=391)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9701 (IC base=+0.162)

- **PATRÓN** `T_h` > `119.444` → IC=+0.355 (n=2888)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 119.444 (IC base=+0.336)

- **PATRÓN** `ratio` > `1.0204` → IC=+0.387 (n=503)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0204 (IC base=+0.336)

### WEEKLY_PRICE#BTC
- **PATRÓN** `ratio` < `0.9933` → IC=+0.249 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9933 (IC base=+0.120)

- **PATRÓN** `T_h` > `111.9836` → IC=+0.318 (n=1038)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9836 (IC base=+0.301)

- **PATRÓN** `ratio` > `1.0177` → IC=+0.369 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0177 (IC base=+0.301)

### WEEKLY_PRICE#ETH
- **PATRÓN** `ratio` < `0.9849` → IC=+0.400 (n=269)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9849 (IC base=+0.209)

- **PATRÓN** `T_h` > `111.9966` → IC=+0.355 (n=1050)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9966 (IC base=+0.325)

- **PATRÓN** `ratio` > `1.0082` → IC=+0.348 (n=320)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0082 (IC base=+0.325)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.0624` → IC=+0.417 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.0624 (IC base=+0.397)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5762 sube el IC de +0.139 a +0.221 en UPDOWN_GBM#15min (n=4930). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7082 sube el IC de +0.201 a +0.272 en UPDOWN_GBM#BTC#15min (n=804). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.4932 sube el IC de +0.131 a +0.218 en UPDOWN_GBM#ETH#15min (n=1010). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5417 sube el IC de +0.152 a +0.222 en UPDOWN_GBM#XRP#15min (n=1239). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1111 sube el IC de +0.068 a +0.151 en UPDOWN_GBM#XRP#15min (n=1069). Ya aplicado como kelly_boost=+0.75€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6306 sube el IC de -0.084 a +0.277 en UPDOWN_GBM_15M_TARDIO (n=1247). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3704 sube el IC de -0.003 a +0.286 en UPDOWN_GBM_15M_TARDIO (n=5070). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7609 sube el IC de +0.069 a +0.318 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=437). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.6255 sube el IC de -0.185 a +0.289 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=74). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.5679 sube el IC de +0.146 a +0.240 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=626). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.1863 sube el IC de +0.244 a +0.304 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=1312). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.9231 sube el IC de -0.203 a +0.380 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=23). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.381 sube el IC de -0.029 a +0.297 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=868). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.220 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.137 sube el IC de -0.015 a +0.312 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=808). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_YES, IBS > 0.8434 sube el IC de +0.106 a +0.308 en UPDOWN_GBM_ETH_15M_HORA7 (n=24). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_YES, IBS > 0.8434 sube el IC de +0.106 a +0.308 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=24). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.838 sube el IC de +0.282 a +0.310 en UPDOWN_GBM_IBS_ALTO (n=1374). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.829 sube el IC de +0.275 a +0.299 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=726). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8475 sube el IC de +0.289 a +0.317 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=648). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7883 sube el IC de +0.364 a +0.392 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=759). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8078 sube el IC de +0.362 a +0.384 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=369). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7632 sube el IC de +0.364 a +0.393 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=390). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 2177 | +0.084 | +236.01€ | 1 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 2177 | +0.084 | +236.01€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1770 | +0.085 | +195.31€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1770 | +0.085 | +195.31€ | 1 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 285 | +0.068 | +10.79€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 285 | +0.068 | +10.79€ | 5 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 91 | +0.134 | +30.24€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 91 | +0.134 | +30.24€ | 1 | 9 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 1149 | -0.020 | +73.94€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 1149 | -0.020 | +73.94€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE | 7 | +0.019 | +3.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE#15min | 7 | +0.019 | +3.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 879 | -0.038 | +57.42€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 879 | -0.038 | +57.42€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 182 | +0.065 | +20.03€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 182 | +0.065 | +20.03€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 81 | -0.030 | -6.77€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 81 | -0.030 | -6.77€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 47847 | -0.085 | -6172.22€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 2988 | +0.075 | -303.49€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 44859 | -0.095 | -5868.73€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4830 | -0.112 | -811.49€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4830 | -0.112 | -811.49€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 2988 | +0.075 | -303.49€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 2988 | +0.075 | -303.49€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 4877 | -0.106 | -938.87€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 4877 | -0.106 | -938.87€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 13150 | -0.044 | -1295.60€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 13150 | -0.044 | -1295.60€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 13015 | -0.112 | -1360.20€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 13015 | -0.112 | -1360.20€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 8987 | -0.131 | -1462.58€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 8987 | -0.131 | -1462.58€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 50059 | -0.012 | +2837.86€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 12942 | +0.004 | +1501.22€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 37117 | -0.018 | +1336.64€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 50059 | -0.012 | +2837.86€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 12942 | +0.004 | +1501.22€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 37117 | -0.018 | +1336.64€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 191103 | +0.113 | -7958.02€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#15min | 21963 | +0.180 | -697.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 878 | +0.011 | -73.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 157362 | +0.105 | -6785.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 10900 | +0.093 | -400.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 26077 | +0.103 | -1851.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 78 | -0.175 | +12.07€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 25984 | +0.104 | -1851.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 36153 | +0.124 | -607.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5617 | +0.177 | -243.34€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 26049 | +0.120 | -178.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 4445 | +0.080 | -164.09€ | 1 | 2 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 26128 | +0.098 | -1896.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 89 | -0.104 | +15.61€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 26024 | +0.099 | -1900.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 40825 | +0.123 | -877.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 10255 | +0.178 | -254.37€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 26461 | +0.105 | -552.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 4097 | +0.102 | -61.98€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#SOL | 35811 | +0.112 | -1599.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 5833 | +0.198 | -244.56€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 781 | +0.038 | -19.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 26839 | +0.096 | -1160.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 2358 | +0.103 | -174.83€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO#XRP | 26109 | +0.107 | -1124.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 91 | -0.113 | +16.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 26005 | +0.108 | -1141.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 30967 | +0.192 | -2171.08€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 30967 | +0.192 | -2171.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 7014 | +0.168 | -736.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 7014 | +0.168 | -736.01€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 4497 | +0.196 | -177.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 4497 | +0.196 | -177.30€ | 3 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 6877 | +0.175 | -603.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 6877 | +0.175 | -603.81€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 5744 | +0.250 | -208.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 5744 | +0.250 | -208.11€ | 0 | 4 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 6756 | +0.185 | -459.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 6756 | +0.185 | -459.60€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 1254 | +0.425 | -47.35€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 1254 | +0.425 | -47.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 520 | +0.439 | -5.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 520 | +0.439 | -5.12€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE#15min | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 507 | +0.423 | -19.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 507 | +0.423 | -19.99€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 213 | +0.398 | -18.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 213 | +0.398 | -18.37€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 109586 | +0.199 | -8144.47€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 109586 | +0.199 | -8144.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 18959 | +0.177 | -2193.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 18959 | +0.177 | -2193.53€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 17667 | +0.224 | -601.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 17667 | +0.224 | -601.30€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 18813 | +0.179 | -2017.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 18813 | +0.179 | -2017.36€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 17813 | +0.218 | -709.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 17813 | +0.218 | -709.57€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 18098 | +0.203 | -1140.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 18098 | +0.203 | -1140.49€ | 1 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 18236 | +0.196 | -1482.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 18236 | +0.196 | -1482.22€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 42323 | +0.117 | +369.83€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 42323 | +0.117 | +369.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 21069 | +0.118 | +223.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 21069 | +0.118 | +223.35€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 21254 | +0.116 | +146.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 21254 | +0.116 | +146.48€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 2614 | +0.292 | -19.78€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 2614 | +0.292 | -19.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 1195 | +0.280 | -33.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 1195 | +0.280 | -33.07€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 1279 | +0.295 | +7.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 1279 | +0.295 | +7.52€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 140 | +0.345 | +5.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 140 | +0.345 | +5.77€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 1204 | +0.436 | -10.20€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 1204 | +0.436 | -10.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 576 | +0.432 | -10.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 576 | +0.432 | -10.41€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 577 | +0.440 | -1.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 577 | +0.440 | -1.04€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 51 | +0.406 | +1.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 51 | +0.406 | +1.25€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1954 | +0.068 | -86.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 725 | +0.046 | -64.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 1229 | +0.080 | -22.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1520 | +0.075 | -41.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 291 | +0.053 | -19.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 1229 | +0.080 | -22.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 85853 | +0.101 | -1990.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 6928 | +0.097 | +162.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 78925 | +0.101 | -2153.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 46915 | +0.106 | -430.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 6928 | +0.097 | +162.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 39987 | +0.107 | -593.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 18282 | +0.109 | -103.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 18282 | +0.109 | -103.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 20656 | +0.082 | -1456.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 20656 | +0.082 | -1456.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 914 | +0.186 | -109.27€ | 5 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 914 | +0.186 | -109.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 914 | +0.186 | -109.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 914 | +0.186 | -109.27€ | 5 | 4 |
| ✅ GBM_LATE_15M | 58277 | +0.101 | +32652.17€ | 0 | 18 |
| ✅ GBM_LATE_15M#15min | 58277 | +0.101 | +32652.17€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 9647 | +0.226 | +8363.32€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 9647 | +0.226 | +8363.32€ | 0 | 22 |
| ✅ GBM_LATE_15M#BTC | 8950 | +0.177 | +7083.34€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 8950 | +0.177 | +7083.34€ | 0 | 20 |
| ✅ GBM_LATE_15M#DOGE | 10444 | +0.208 | +8303.68€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 10444 | +0.208 | +8303.68€ | 0 | 21 |
| ✅ GBM_LATE_15M#ETH | 7793 | +0.057 | +2530.31€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 7793 | +0.057 | +2530.31€ | 1 | 16 |
| ✅ GBM_LATE_15M#SOL | 8129 | -0.029 | +2103.23€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 8129 | -0.029 | +2103.23€ | 4 | 13 |
| ✅ GBM_LATE_15M#XRP | 13314 | -0.022 | +4268.29€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 13314 | -0.022 | +4268.29€ | 3 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 61519 | +0.085 | +35726.75€ | 0 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 61519 | +0.085 | +35726.75€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 11892 | -0.002 | +6318.30€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 11892 | -0.002 | +6318.30€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 13235 | +0.004 | +3539.58€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 13235 | +0.004 | +3539.58€ | 0 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 8351 | +0.296 | +9586.43€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 8351 | +0.296 | +9586.43€ | 0 | 21 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 11746 | +0.014 | +3640.05€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 11746 | +0.014 | +3640.05€ | 1 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 9427 | +0.044 | +4221.24€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 9427 | +0.044 | +4221.24€ | 3 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 6868 | +0.316 | +8421.15€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 6868 | +0.316 | +8421.15€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 46066 | +0.179 | +38012.57€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 46066 | +0.179 | +38012.57€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 6937 | +0.240 | +6479.56€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 6937 | +0.240 | +6479.56€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 7293 | +0.139 | +5394.96€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 7293 | +0.139 | +5394.96€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 7419 | +0.225 | +6465.14€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 7419 | +0.225 | +6465.14€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 7893 | +0.129 | +6086.22€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 7893 | +0.129 | +6086.22€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 8723 | +0.119 | +6508.21€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 8723 | +0.119 | +6508.21€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 7801 | +0.233 | +7078.49€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 7801 | +0.233 | +7078.49€ | 0 | 25 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 12532 | +0.126 | +6301.10€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 12532 | +0.126 | +6301.10€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 599 | +0.166 | +406.64€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 599 | +0.166 | +406.64€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 3428 | +0.127 | +1869.46€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 3428 | +0.127 | +1869.46€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 507 | +0.158 | +290.79€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 507 | +0.158 | +290.79€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 3588 | +0.124 | +1718.47€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 3588 | +0.124 | +1718.47€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 3275 | +0.098 | +1296.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 3275 | +0.098 | +1296.28€ | 0 | 13 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 1135 | +0.169 | +719.46€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 1135 | +0.169 | +719.46€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO | 58466 | +0.188 | +48282.88€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#15min | 58466 | +0.188 | +48282.88€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 9221 | +0.251 | +8962.91€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 9221 | +0.251 | +8962.91€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 9311 | +0.138 | +6489.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 9311 | +0.138 | +6489.77€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 9918 | +0.236 | +9035.66€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 9918 | +0.236 | +9035.66€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 9681 | +0.143 | +7158.20€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 9681 | +0.143 | +7158.20€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 10376 | +0.123 | +7337.40€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 10376 | +0.123 | +7337.40€ | 0 | 18 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 9959 | +0.242 | +9298.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 9959 | +0.242 | +9298.94€ | 0 | 20 |
| ✅ GBM_LATE_5M | 14832 | +0.213 | +12206.66€ | 1 | 26 |
| ✅ GBM_LATE_5M#5min | 14832 | +0.213 | +12206.66€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 1244 | +0.248 | +1188.48€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 1244 | +0.248 | +1188.48€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 3267 | +0.211 | +2815.48€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 3267 | +0.211 | +2815.48€ | 0 | 27 |
| ✅ GBM_LATE_5M#DOGE | 1453 | +0.210 | +1160.11€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1453 | +0.210 | +1160.11€ | 0 | 19 |
| ✅ GBM_LATE_5M#ETH | 4326 | +0.205 | +3276.92€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 4326 | +0.205 | +3276.92€ | 0 | 24 |
| ✅ GBM_LATE_5M#SOL | 2529 | +0.219 | +2182.23€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 2529 | +0.219 | +2182.23€ | 0 | 24 |
| ✅ GBM_LATE_5M#XRP | 2013 | +0.209 | +1583.43€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 2013 | +0.209 | +1583.43€ | 0 | 0 |
| ✅ GBM_LATE_60M | 5207 | +0.052 | +1431.49€ | 0 | 5 |
| ✅ GBM_LATE_60M#60min | 5207 | +0.052 | +1431.49€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 1800 | +0.058 | +541.33€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 1800 | +0.058 | +541.33€ | 0 | 6 |
| ✅ GBM_LATE_60M#ETH | 1668 | +0.053 | +542.95€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 1668 | +0.053 | +542.95€ | 1 | 5 |
| ✅ GBM_LATE_60M#SOL | 1739 | +0.046 | +347.21€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 1739 | +0.046 | +347.21€ | 0 | 8 |
| 🚫 GBM_LATE_60M_FADE | 721 | -0.251 | -35.88€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 721 | -0.251 | -35.88€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 260 | -0.252 | -19.02€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 260 | -0.252 | -19.02€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 261 | -0.245 | -7.56€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 261 | -0.245 | -7.56€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 200 | -0.253 | -9.31€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 200 | -0.253 | -9.31€ | 8 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 2149 | +0.083 | +540.36€ | 0 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 2149 | +0.083 | +540.36€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 841 | +0.071 | +194.35€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 841 | +0.071 | +194.35€ | 1 | 6 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 749 | +0.058 | +145.65€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 749 | +0.058 | +145.65€ | 1 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 559 | +0.135 | +200.36€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 559 | +0.135 | +200.36€ | 2 | 9 |
| ✅ LATE_WINDOW_5MIN | 256 | +0.295 | +289.23€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 256 | +0.295 | +289.23€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 256 | +0.295 | +289.23€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 256 | +0.295 | +289.23€ | 1 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 4421 | +0.098 | +1010.44€ | 0 | 1 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 4421 | +0.098 | +1010.44€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 4421 | +0.098 | +1010.44€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 4421 | +0.098 | +1010.44€ | 0 | 1 |
| ✅ LIQUIDACIONES_15M | 1249 | +0.006 | +44.93€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 1249 | +0.006 | +44.93€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 97 | +0.066 | +13.64€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 97 | +0.066 | +13.64€ | 0 | 3 |
| ✅ LIQUIDACIONES_15M#BTC | 284 | -0.004 | +8.98€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 284 | -0.004 | +8.98€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 65 | -0.007 | +2.74€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 65 | -0.007 | +2.74€ | 0 | 1 |
| ✅ LIQUIDACIONES_15M#ETH | 314 | +0.022 | +19.74€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 314 | +0.022 | +19.74€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 323 | -0.017 | +0.36€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 323 | -0.017 | +0.36€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 166 | +0.006 | -0.53€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 166 | +0.006 | -0.53€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 4235 | +0.017 | +142.46€ | 5 | 1 |
| ✅ LIQUIDACIONES_5M#5min | 4235 | +0.017 | +142.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 231 | +0.002 | -6.06€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 231 | +0.002 | -6.06€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 827 | +0.015 | +40.58€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 827 | +0.015 | +40.58€ | 4 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 263 | +0.043 | +45.39€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 263 | +0.043 | +45.39€ | 0 | 6 |
| ✅ LIQUIDACIONES_5M#ETH | 1663 | +0.019 | +28.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1663 | +0.019 | +28.46€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 771 | +0.011 | +2.03€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 771 | +0.011 | +2.03€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 480 | +0.017 | +32.06€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 480 | +0.017 | +32.06€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 2436 | -0.033 | -6.94€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 2436 | -0.033 | -6.94€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 737 | -0.032 | -11.95€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 737 | -0.032 | -11.95€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 871 | -0.011 | +18.13€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 871 | -0.011 | +18.13€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 828 | -0.057 | -13.12€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 828 | -0.057 | -13.12€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 16171 | -0.032 | -164.81€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 7784 | -0.033 | -86.58€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 8387 | -0.031 | -78.23€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 564 | -0.058 | -38.62€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 289 | -0.036 | -4.99€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 275 | -0.081 | -33.63€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 4240 | -0.026 | -26.32€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 2018 | -0.024 | +0.53€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 2222 | -0.028 | -26.85€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 1554 | -0.029 | +13.65€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 795 | -0.035 | -4.49€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 759 | -0.023 | +18.14€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 3659 | -0.034 | -70.55€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 1742 | -0.033 | -29.84€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 1917 | -0.035 | -40.71€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 3106 | -0.022 | +45.19€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 1505 | -0.028 | +2.98€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 1601 | -0.017 | +42.21€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 3048 | -0.043 | -88.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 1435 | -0.048 | -50.77€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 1613 | -0.039 | -37.39€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 69081 | -0.000 | +3679.80€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 69081 | -0.000 | +3679.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 12526 | +0.027 | +1716.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 12526 | +0.027 | +1716.91€ | 2 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 9637 | -0.037 | -144.86€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 9637 | -0.037 | -144.86€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 12668 | +0.025 | +1416.99€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 12668 | +0.025 | +1416.99€ | 1 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 9588 | -0.053 | -257.62€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 9588 | -0.053 | -257.62€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 11780 | -0.004 | +323.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 11780 | -0.004 | +323.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 12882 | +0.018 | +624.67€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 12882 | +0.018 | +624.67€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 7217 | -0.053 | -110.94€ | 5 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 7217 | -0.053 | -110.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1257 | -0.001 | -13.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1257 | -0.001 | -13.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 2000 | -0.061 | -20.58€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 2000 | -0.061 | -20.58€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 88 | -0.011 | +0.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 88 | -0.011 | +0.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 809 | -0.120 | -35.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 809 | -0.120 | -35.98€ | 5 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 2200 | -0.068 | -13.47€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 2200 | -0.068 | -13.47€ | 2 | 0 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 169229 | -0.078 | +2105.35€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 169229 | -0.078 | +2105.35€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 29652 | -0.078 | +1719.03€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 29652 | -0.078 | +1719.03€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 25265 | -0.101 | -1246.81€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 25265 | -0.101 | -1246.81€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 30081 | -0.068 | +1447.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 30081 | -0.068 | +1447.42€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 24813 | -0.100 | -836.45€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 24813 | -0.100 | -836.45€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 30216 | -0.059 | +248.10€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 30216 | -0.059 | +248.10€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 29202 | -0.069 | +774.07€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 29202 | -0.069 | +774.07€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 9085 | -0.035 | -178.69€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 9085 | -0.035 | -178.69€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 1008 | -0.017 | -19.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 1008 | -0.017 | -19.32€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 2118 | -0.046 | -27.51€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 2118 | -0.046 | -27.51€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2657 | -0.025 | -36.69€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2657 | -0.025 | -36.69€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1273 | -0.064 | -31.74€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1273 | -0.064 | -31.74€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 1020 | -0.031 | -31.48€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 1020 | -0.031 | -31.48€ | 0 | 0 |
| ✅ ORDER_FLOW_5M | 2181 | +0.120 | +870.22€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#5min | 2045 | +0.124 | +857.63€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 484 | +0.134 | +235.45€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 484 | +0.134 | +235.45€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#DOGE | 420 | +0.121 | +151.80€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 420 | +0.121 | +151.80€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#ETH | 385 | +0.125 | +172.41€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 385 | +0.125 | +172.41€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 346 | +0.141 | +177.04€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 346 | +0.141 | +177.04€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#XRP | 410 | +0.100 | +120.93€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 410 | +0.100 | +120.93€ | 0 | 2 |
| ✅ ORDER_FLOW_5M_REACTIVO | 2234 | -0.014 | -4.86€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 2234 | -0.014 | -4.86€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 400 | +0.012 | +24.67€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 400 | +0.012 | +24.67€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 415 | -0.040 | -20.36€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 415 | -0.040 | -20.36€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 558 | -0.037 | -30.37€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 558 | -0.037 | -30.37€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 455 | +0.008 | +10.47€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 455 | +0.008 | +10.47€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 406 | -0.005 | +10.73€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 406 | -0.005 | +10.73€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 1179 | -0.061 | -6.37€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 543 | -0.098 | -62.02€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 422 | -0.108 | -41.48€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 121 | -0.061 | -20.55€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 413 | -0.021 | +37.89€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 298 | -0.003 | +45.89€ | 1 | 2 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 115 | -0.064 | -8.00€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 223 | -0.047 | +17.76€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 187 | -0.040 | +15.92€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 36 | -0.079 | +1.84€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 907 | -0.060 | +20.34€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 272 | -0.066 | -26.71€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 1490 | -0.203 | -86.77€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 587 | -0.200 | -45.33€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 517 | -0.198 | -40.88€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#reach | 70 | -0.208 | -4.45€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 498 | -0.208 | -38.65€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 436 | -0.219 | -45.80€ | 4 | 1 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 62 | -0.125 | +7.14€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL | 405 | -0.200 | -2.79€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 375 | -0.198 | -4.94€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 30 | -0.219 | +2.15€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 1328 | -0.205 | -91.61€ | 0 | 0 |
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
| ✅ STREAK_FADE_15M | 959 | +0.041 | +82.03€ | 2 | 2 |
| ✅ STREAK_FADE_15M#15min | 959 | +0.041 | +82.03€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 358 | +0.017 | +2.85€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 358 | +0.017 | +2.85€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 74 | +0.026 | +3.13€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 74 | +0.026 | +3.13€ | 1 | 1 |
| ✅ STREAK_FADE_15M#SOL | 83 | +0.018 | +6.06€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 83 | +0.018 | +6.06€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 444 | +0.067 | +69.99€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 444 | +0.067 | +69.99€ | 1 | 4 |
| ✅ STREAK_FADE_5M | 3587 | -0.024 | -144.41€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3587 | -0.024 | -144.41€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 1127 | -0.023 | -40.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 1127 | -0.023 | -40.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 618 | -0.029 | -27.62€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 618 | -0.029 | -27.62€ | 1 | 0 |
| ✅ STREAK_FADE_5M#SOL | 171 | -0.043 | -14.80€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 171 | -0.043 | -14.80€ | 4 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1671 | -0.020 | -61.78€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1671 | -0.020 | -61.78€ | 2 | 0 |
| ✅ STREAK_FADE_60M | 118 | -0.050 | -12.20€ | 5 | 0 |
| ✅ STREAK_FADE_60M#60min | 118 | -0.050 | -12.20€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 44 | -0.087 | -4.62€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 44 | -0.087 | -4.62€ | 4 | 0 |
| ✅ STREAK_FADE_60M#SOL | 74 | -0.026 | -7.58€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 74 | -0.026 | -7.58€ | 0 | 1 |
| ✅ STREAK_MOM_5M | 11541 | +0.014 | +74.19€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 11541 | +0.014 | +74.19€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2995 | +0.018 | +24.38€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2995 | +0.018 | +24.38€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 3033 | +0.016 | +33.11€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 3033 | +0.016 | +33.11€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2931 | +0.009 | -2.04€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2931 | +0.009 | -2.04€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2582 | +0.014 | +18.75€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2582 | +0.014 | +18.75€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 12229 | +0.019 | +7.96€ | 4 | 0 |
| ✅ STRUCT_NO_15M#15min | 12229 | +0.019 | +7.96€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 5053 | +0.021 | +6.47€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 5053 | +0.021 | +6.47€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 4234 | +0.019 | +2.32€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 4234 | +0.019 | +2.32€ | 4 | 0 |
| ✅ STRUCT_NO_15M#SOL | 2942 | +0.015 | -0.84€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 2942 | +0.015 | -0.84€ | 1 | 0 |
| ✅ UPDOWN_GBM | 109822 | +0.060 | +10424.94€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 26745 | +0.078 | +5338.66€ | 0 | 9 |
| ✅ UPDOWN_GBM#240min | 3216 | -0.000 | +33.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 72970 | +0.062 | +4949.20€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 6518 | -0.003 | +111.88€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 9218 | +0.104 | +1680.88€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1781 | +0.164 | +820.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 90 | -0.011 | -2.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 7347 | +0.091 | +862.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 25016 | +0.058 | +2226.61€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 3577 | +0.080 | +802.70€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 921 | -0.001 | +16.97€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 17475 | +0.068 | +1330.86€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 2907 | -0.005 | +72.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 136 | -0.065 | +3.23€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 11961 | +0.077 | +1334.52€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1761 | +0.154 | +738.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 86 | +0.023 | -0.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 10114 | +0.064 | +596.94€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 26041 | +0.050 | +1843.66€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 6316 | +0.072 | +966.53€ | 0 | 8 |
| ✅ UPDOWN_GBM#ETH#240min | 891 | +0.005 | +16.11€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 16314 | +0.053 | +821.35€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 2396 | +0.000 | +39.52€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 124 | -0.111 | +0.15€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 23251 | +0.039 | +1296.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 7214 | +0.031 | +425.94€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#240min | 831 | -0.010 | +4.78€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 13880 | +0.052 | +876.10€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 1215 | -0.003 | -0.47€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#daily | 111 | -0.146 | -9.73€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 14333 | +0.073 | +2044.50€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 6096 | +0.093 | +1584.86€ | 0 | 11 |
| ✅ UPDOWN_GBM#XRP#240min | 397 | +0.006 | -1.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 7840 | +0.060 | +461.26€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 371 | -0.106 | -6.35€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 1011 | +0.364 | +374.70€ | 0 | 10 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 1011 | +0.364 | +374.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 491 | +0.362 | +172.01€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 491 | +0.362 | +172.01€ | 0 | 9 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 520 | +0.364 | +202.69€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 520 | +0.364 | +202.69€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO | 26000 | -0.020 | +6460.69€ | 3 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 26000 | -0.020 | +6460.69€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1981 | -0.051 | +561.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1981 | -0.051 | +561.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 4841 | -0.115 | +271.31€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 4841 | -0.115 | +271.31€ | 3 | 11 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 1071 | +0.222 | +899.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 1071 | +0.222 | +899.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 3456 | +0.220 | +2215.67€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 3456 | +0.220 | +2215.67€ | 1 | 19 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 7387 | -0.060 | +1080.32€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 7387 | -0.060 | +1080.32€ | 5 | 5 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 7264 | -0.059 | +1432.35€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 7264 | -0.059 | +1432.35€ | 4 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 316 | +0.060 | +27.30€ | 0 | 9 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 316 | +0.060 | +27.30€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 316 | +0.060 | +27.30€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 316 | +0.060 | +27.30€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1830 | +0.282 | +1533.01€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1830 | +0.282 | +1533.01€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 966 | +0.275 | +756.51€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 966 | +0.275 | +756.51€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 864 | +0.289 | +776.50€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 864 | +0.289 | +776.50€ | 0 | 8 |
| ✅ UPDOWN_OU_5M | 872 | -0.113 | -86.72€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 872 | -0.113 | -86.72€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 277 | -0.081 | -20.93€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 277 | -0.081 | -20.93€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 98 | -0.180 | -12.47€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 98 | -0.180 | -12.47€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 114 | -0.172 | -3.97€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 114 | -0.172 | -3.97€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 38 | -0.175 | -6.61€ | 2 | 0 |
| ✅ WEEKLY_PRICE | 4779 | +0.300 | +2142.89€ | 0 | 3 |
| ✅ WEEKLY_PRICE#BTC | 1821 | +0.255 | +228.17€ | 0 | 3 |
| ✅ WEEKLY_PRICE#ETH | 1848 | +0.295 | +785.08€ | 0 | 3 |
| ✅ WEEKLY_PRICE#SOL | 1110 | +0.381 | +1129.64€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**✅ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: n≥15 y IC<-0.05
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: IC=+0.021 n=1346 — no justifica filtro, seguir monitorizando
  - _Datos_: n=1346 IC=+0.021 PNL=+69.31€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 820 celda(s) pasan gate riguroso completo de 2922 evaluadas (n>=40) y 4039 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.031 < 0.08 — monitorear
  - _Datos_: n=7210 IC=+0.031 PNL=+423.93€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=1848/15 IC=+0.295 PNL=+785.08€ | BTC: n=1821/15 IC=+0.255 PNL=+228.17€ | SOL: n=1110/15 IC=+0.381 PNL=+1129.64€

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
  - _Estado_: alineada_con_outcome_prev IC=+0.140 n=1076/60 | contraria IC=+0.184 n=1126 | gap=-0.044 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=598, boost estimado=+0.011. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 0/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=2394/40 IC=+0.000 PNL=+39.46€ | BTC#60min: n=2905/40 IC=-0.005 PNL=+72.85€ | SOL#60min: n=1215/40 IC=-0.003 PNL=-0.47€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.045 n=745995 | tras_1loss IC=+0.100 n=565536 | tras_2loss IC=+0.071 n=225937/40 | gap=-0.026 (umbral 0.05)

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.134 > 0.08 con n=1308 PNL=+618.85€
  - _Datos_: n=1308 IC=+0.134 PNL=+618.85€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.334 > 0.1 con n=3894 PNL=+2163.27€
  - _Datos_: n=3894 IC=+0.334 PNL=+2163.27€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=1113 IC=+0.064 PNL=+106.87€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1113 IC=+0.064 PNL=+106.87€

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
  - _Estado_: n=4334 IC=-0.002 PNL=-31.42€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=4334 IC=-0.002 PNL=-31.42€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=2180 IC=-0.004 PNL=+143.26€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=2180 IC=-0.004 PNL=+143.26€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=1346 IC=+0.021 PNL=+69.31€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=1346 IC=+0.021 PNL=+69.31€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.139 > 0.1 con n=7356 PNL=+3636.05€
  - _Datos_: n=7356 IC=+0.139 PNL=+3636.05€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=3574 IC=+0.079 PNL=+801.05€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=3574 IC=+0.079 PNL=+801.05€

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
  - _Estado_: n=1420 IC=+0.037 PNL=+112.34€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=1420 IC=+0.037 PNL=+112.34€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=181 IC=-0.035 PNL=-7.22€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=181 IC=-0.035 PNL=-7.22€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.298 n=255) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=255 IC=+0.298 PNL=+291.26€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.117 > 0.02 con n=1279 PNL=+509.92€
  - _Datos_: n=1279 IC=+0.117 PNL=+509.92€

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
  - _Estado_: n=45126 IC=+0.072 PNL=+6147.40€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=45126 IC=+0.072 PNL=+6147.40€

**⏳ H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: 120
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: 0/120 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.138 < -0.1 con n=765 PNL=+105.62€
  - _Datos_: n=765 IC=-0.138 PNL=+105.62€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=4245 IC=+0.067 PNL=+533.13€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=4245 IC=+0.067 PNL=+533.13€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=191 IC=-0.096 PNL=-0.50€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=191 IC=-0.096 PNL=-0.50€

**〰️ H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: n=1146 IC=+0.099 PNL=+289.12€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=1146 IC=+0.099 PNL=+289.12€

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
  - _Estado_: n=44220 IC=-0.138 PNL=+2671.74€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=44220 IC=-0.138 PNL=+2671.74€

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
  - _Estado_: n=4632 IC=+0.132 PNL=+3112.73€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=4632 IC=+0.132 PNL=+3112.73€

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
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.221 < -0.1 con n=4838 PNL=-407.68€
  - _Datos_: n=4838 IC=-0.221 PNL=-407.68€

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
  - _Estado_: n=112 IC=+0.053 PNL=+21.42€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=112 IC=+0.053 PNL=+21.42€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.097 n=2245) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=2245 IC=+0.097 PNL=+456.26€

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
  - _Estado_: n=18952 IC=+0.178 PNL=-2186.68€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=18952 IC=+0.178 PNL=-2186.68€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.231 > 0.1 con n=307 PNL=+214.16€
  - _Datos_: n=307 IC=+0.231 PNL=+214.16€
