# Hipótesis automáticas — 2026-11-12 21:43 UTC
_Generado por shadow_postmortem.py sobre 1308432 resoluciones (PNL=+179670.42€)_

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
- **FILTRO** `restante_s_al_confirmar` < `132.04` → IC=-0.220 (n=11939)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 132.04
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=35827)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `125.1` → IC=-0.258 (n=1206)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 125.1
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=3620)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `116.46` → IC=-0.287 (n=1219)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 116.46
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=3658)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `restante_s_al_confirmar` < `116.5` → IC=-0.169 (n=3284)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 116.5
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=9855)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `152.06` → IC=-0.241 (n=3247)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 152.06
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=9742)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `128.65` → IC=-0.264 (n=2237)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 128.65
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=6714)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.209 (n=28054)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.104)

- **PATRÓN** `libro_liquidez` > `8265.2739` → IC=+0.158 (n=2338)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 8265.2739 (IC base=+0.104)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.128 (n=24239)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 17.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.130 (n=29348)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.124)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.225 (n=22115)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.140 (n=8351)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `6492.1732` → IC=+0.143 (n=3233)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 6492.1732 (IC base=+0.124)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.184 (n=2093)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 6.0 (IC base=+0.177)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.358 (n=751)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.177)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.180 (n=2688)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.01 (IC base=+0.177)

- **PATRÓN** `libro_liquidez` > `9392.7207` → IC=+0.180 (n=1870)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 9392.7207 (IC base=+0.177)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.185 (n=1911)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 7.0 (IC base=+0.178)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.181 (n=2137)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 17.0 (IC base=+0.178)

- **PATRÓN** `py_entrada` < `0.295` → IC=+0.312 (n=981)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.295 (IC base=+0.178)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.181 (n=2738)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.01 (IC base=+0.178)

- **PATRÓN** `libro_liquidez` > `16075.8828` → IC=+0.184 (n=707)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 16075.8828 (IC base=+0.178)

### FAVORITO_CONFIRMADO#BTC#60min
- **FILTRO** `py_entrada` < `0.55` → IC=-0.335 (n=95)

  - _Acción_: SKIP cuando `py_entrada` < 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.094 (n=2227)

- **PATRÓN** `py_entrada` > `0.61` → IC=+0.166 (n=612)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` > 0.61 (IC base=+0.076)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.145 (n=1433)

  - _Acción_: Kelly boost +0.73€ cuando `py_entrada` < 0.44 (IC base=+0.084)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.169 (n=5077)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 6.0 (IC base=+0.166)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.171 (n=4518)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 15.0 (IC base=+0.166)

- **PATRÓN** `py_entrada` > `0.77` → IC=+0.374 (n=1765)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.77 (IC base=+0.166)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.208 (n=2425)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.201)

- **PATRÓN** `py_entrada` < `0.275` → IC=+0.331 (n=952)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.275 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.205 (n=2821)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.201)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.140 (n=651)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 15.0 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.144 (n=1168)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 15.0 (IC base=+0.139)

- **PATRÓN** `py_entrada` > `0.675` → IC=+0.251 (n=444)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.675 (IC base=+0.139)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.142 (n=1115)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.156 (n=155)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.074)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.250 (n=954)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.227)

- **PATRÓN** `py_entrada` > `0.83` → IC=+0.420 (n=1329)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.83 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.146 (n=1429)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 7.0 (IC base=+0.146)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.156 (n=733)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 7.0 (IC base=+0.146)

- **PATRÓN** `py_entrada` < `0.345` → IC=+0.278 (n=717)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.345 (IC base=+0.146)

### FAVORITO_CONFIRMADO#SOL#60min
- **FILTRO** `libro_liquidez` < `952.1685` → IC=-0.125 (n=158)

  - _Acción_: SKIP cuando `libro_liquidez` < 952.1685
  - _Potencial_: sin este filtro IC_bueno=+0.066 (n=323)

- **PATRÓN** `py_entrada` > `0.55` → IC=+0.164 (n=462)

  - _Acción_: Kelly boost +0.82€ cuando `py_entrada` > 0.55 (IC base=+0.046)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.147 (n=482)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 17.0 (IC base=+0.122)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.248 (n=438)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.122)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `10.0` → IC=-0.297 (n=72)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.232 (n=151)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.201 (n=24259)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.195)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.197 (n=20471)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 15.0 (IC base=+0.195)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.229 (n=7676)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.195)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.338 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.195)

- **PATRÓN** `libro_liquidez` > `4915.142` → IC=+0.338 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4915.142 (IC base=+0.195)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.173 (n=5532)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 5.0 (IC base=+0.169)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.169 (n=5513)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` < 18.0 (IC base=+0.169)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.179 (n=5501)

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

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.211 (n=3298)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.208)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.210 (n=2916)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.208)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.249 (n=1635)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.208)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.183 (n=5410)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.178 (n=4586)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 15.0 (IC base=+0.176)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.177 (n=5560)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` < 0.73 (IC base=+0.176)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.184 (n=4241)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` > 0.71 (IC base=+0.176)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.256 (n=4301)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.250)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.252 (n=3838)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.250)

- **PATRÓN** `py_entrada` > `0.8` → IC=+0.362 (n=1460)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.191 (n=5306)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.186)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.190 (n=4489)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 15.0 (IC base=+0.186)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.197 (n=1777)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` > 0.73 (IC base=+0.186)

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

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.205 (n=31823)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.239 (n=32019)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.200)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.186 (n=4750)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 18.0 (IC base=+0.178)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.179 (n=10147)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 12.0 (IC base=+0.178)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.188 (n=14605)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` > 0.71 (IC base=+0.178)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.228 (n=6596)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.224)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.285 (n=4481)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.224)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.183 (n=13325)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 7.0 (IC base=+0.179)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.197 (n=11267)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` > 0.72 (IC base=+0.179)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.835` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.835
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=8)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.228 (n=4454)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.219)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.222 (n=5087)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.219)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.254 (n=7353)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.219)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **FILTRO** `hora_utc` > `3.0` → IC=-0.278 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.213 (n=4513)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.256 (n=4621)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.202 (n=5293)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.198 (n=5253)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 6.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.240 (n=6653)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.196)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.194 (n=11442)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.141 (n=12072)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `3.42` → IC=+0.139 (n=13928)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 3.42 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.194 (n=5579)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.144 (n=5450)

  - _Acción_: Kelly boost +0.72€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.125 (n=6983)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 7.0 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `4.13` → IC=+0.141 (n=6932)

  - _Acción_: Kelly boost +0.71€ cuando `lag_apertura_s` < 4.13 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.193 (n=5863)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.138 (n=7352)

  - _Acción_: Kelly boost +0.69€ cuando `restante_min` > 4.95 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `3.11` → IC=+0.138 (n=6994)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 3.11 (IC base=+0.116)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.304 (n=1404)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.291)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.291 (n=1738)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.291)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.385 (n=721)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.291)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.284 (n=942)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.280)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.366 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.280)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.314 (n=682)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.295)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.299 (n=998)
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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.439 (n=952)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.436)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.443 (n=921)

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
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.448 (n=306)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.439)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.439 (n=389)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.439)

- **PATRÓN** `py_entrada` > `0.91` → IC=+0.443 (n=454)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.91 (IC base=+0.439)

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
- **PATRÓN** `drift_60min` |x|≤ `0.48` → IC=+0.140 (n=17993)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.48 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.128 (n=18210)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 6.0 (IC base=+0.123)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.126 (n=12513)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 12.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` > `0.9767` → IC=+0.246 (n=5998)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9767 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` > `0.8004` → IC=+0.283 (n=980)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8004 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.478` → IC=+0.187 (n=9008)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 3.478 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` > `0.6259` → IC=+0.266 (n=5411)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6259 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` > `0.304` → IC=+0.250 (n=1857)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.304 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` > `2.7506` → IC=+0.236 (n=4319)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7506 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.136 (n=8898)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `4653.8788` → IC=+0.149 (n=5997)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 4653.8788 (IC base=+0.123)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.123 (n=11276)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0063 (IC base=+0.084)

- **PATRÓN** `ibs_20min` < `0.5642` → IC=+0.144 (n=22507)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.5642 (IC base=+0.084)

- **PATRÓN** `dist_vwap_pct` > `0.6209` → IC=+0.189 (n=1475)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.6209 (IC base=+0.084)

- **PATRÓN** `volumen_regimen` < `0.8608` → IC=+0.196 (n=6156)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 0.8608 (IC base=+0.084)

- **PATRÓN** `volumen_pendiente_norm` > `0.2958` → IC=+0.234 (n=2266)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2958 (IC base=+0.084)

- **PATRÓN** `volumen_spike_ratio` > `2.6701` → IC=+0.213 (n=5220)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6701 (IC base=+0.084)

- **PATRÓN** `ballena_activa_n` < `99.0` → IC=+0.230 (n=15570)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 99.0 (IC base=+0.084)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `drift_60min` |x|≤ `0.3663` → IC=+0.212 (n=3831)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3663 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.227 (n=1863)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.211)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.211 (n=2564)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` > `0.9857` → IC=+0.278 (n=1737)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9857 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.796` → IC=+0.294 (n=903)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.796 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.2333` → IC=+0.258 (n=681)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2333 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `1.4382` → IC=+0.213 (n=3673)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4382 (IC base=+0.211)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.224 (n=4238)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `2035.77` → IC=+0.213 (n=1277)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2035.77 (IC base=+0.211)

- **PATRÓN** `ballena_activa_n` < `26.0` → IC=+0.223 (n=3497)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 26.0 (IC base=+0.211)

- **PATRÓN** `sigma_h` > `0.0093` → IC=+0.246 (n=1534)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0093 (IC base=+0.244)

- **PATRÓN** `drift_60min` |x|≤ `0.0897` → IC=+0.281 (n=1129)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0897 (IC base=+0.244)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.250 (n=1266)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.244)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.250 (n=1553)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.244)

- **PATRÓN** `ibs_20min` < `0.5659` → IC=+0.260 (n=3382)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5659 (IC base=+0.244)

- **PATRÓN** `volumen_pendiente_norm` < `0.0949` → IC=+0.247 (n=3063)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0949 (IC base=+0.244)

- **PATRÓN** `volumen_pendiente_norm` > `0.2886` → IC=+0.251 (n=452)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2886 (IC base=+0.244)

- **PATRÓN** `volumen_spike_ratio` < `1.4468` → IC=+0.246 (n=1077)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4468 (IC base=+0.244)

- **PATRÓN** `volumen_spike_ratio` > `1.8591` → IC=+0.248 (n=2153)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8591 (IC base=+0.244)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.246 (n=3903)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.244)

- **PATRÓN** `libro_liquidez` > `1774.07` → IC=+0.251 (n=2254)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1774.07 (IC base=+0.244)

- **PATRÓN** `ballena_activa_n` < `6.0` → IC=+0.246 (n=1150)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 6.0 (IC base=+0.244)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.231 (n=2153)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.224)

- **PATRÓN** `drift_60min` |x|≤ `0.1096` → IC=+0.252 (n=1420)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1096 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.235 (n=3384)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.226 (n=2290)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` > `0.9014` → IC=+0.257 (n=1077)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9014 (IC base=+0.224)

- **PATRÓN** `dist_vwap_pct` > `0.186` → IC=+0.234 (n=1447)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.186 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.797` → IC=+0.265 (n=471)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.797 (IC base=+0.224)

- **PATRÓN** `volumen_regimen` > `0.6287` → IC=+0.230 (n=3228)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6287 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` > `0.2784` → IC=+0.267 (n=445)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2784 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` > `2.4483` → IC=+0.249 (n=1062)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4483 (IC base=+0.224)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.153 (n=3466)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0065 (IC base=+0.132)

- **PATRÓN** `drift_60min` |x|≤ `0.0779` → IC=+0.157 (n=1155)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.0779 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.152 (n=1296)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 17.0 (IC base=+0.132)

- **PATRÓN** `ibs_20min` < `0.7058` → IC=+0.172 (n=3461)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.7058 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.981` → IC=+0.139 (n=3162)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 3.981 (IC base=+0.132)

- **PATRÓN** `volumen_regimen` < `0.6333` → IC=+0.155 (n=1154)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.6333 (IC base=+0.132)

- **PATRÓN** `volumen_pendiente_norm` > `0.0717` → IC=+0.156 (n=1416)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` > 0.0717 (IC base=+0.132)

- **PATRÓN** `volumen_spike_ratio` < `2.442` → IC=+0.143 (n=3334)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.442 (IC base=+0.132)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.132 (n=4495)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.01 (IC base=+0.132)

- **PATRÓN** `ballena_activa_n` < `175.0` → IC=+0.186 (n=1103)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 175.0 (IC base=+0.132)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0127` → IC=+0.214 (n=1353)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0127 (IC base=+0.196)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.203 (n=4265)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.196)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.260 (n=1579)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.196)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.97` → IC=+0.282 (n=891)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.97 (IC base=+0.196)

- **PATRÓN** `volumen_pendiente_norm` < `0.0975` → IC=+0.198 (n=3639)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` < 0.0975 (IC base=+0.196)

- **PATRÓN** `volumen_pendiente_norm` > `0.352` → IC=+0.228 (n=524)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.352 (IC base=+0.196)

- **PATRÓN** `volumen_spike_ratio` > `2.7283` → IC=+0.215 (n=1797)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7283 (IC base=+0.196)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.200 (n=4909)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.196)

- **PATRÓN** `libro_liquidez` > `2012.2756` → IC=+0.203 (n=1353)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2012.2756 (IC base=+0.196)

- **PATRÓN** `sigma_h` < `0.0111` → IC=+0.224 (n=3303)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0111 (IC base=+0.221)

- **PATRÓN** `drift_60min` |x|≤ `0.2926` → IC=+0.234 (n=2502)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2926 (IC base=+0.221)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.241 (n=1429)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.221)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.226 (n=1699)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.221)

- **PATRÓN** `ibs_20min` < `0.0486` → IC=+0.269 (n=1251)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0486 (IC base=+0.221)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.768` → IC=+0.261 (n=404)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.768 (IC base=+0.221)

- **PATRÓN** `volumen_pendiente_norm` > `0.3471` → IC=+0.259 (n=546)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3471 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` < `1.7631` → IC=+0.219 (n=1589)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7631 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` > `2.1534` → IC=+0.230 (n=2409)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1534 (IC base=+0.221)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.223 (n=1900)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.221)

- **PATRÓN** `libro_liquidez` > `1882.5784` → IC=+0.225 (n=1701)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1882.5784 (IC base=+0.221)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.226 (n=3580)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 24.0 (IC base=+0.221)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.174 (n=213)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=4885)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.150 (n=672)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0039 (IC base=+0.060)

- **PATRÓN** `ibs_20min` > `0.9409` → IC=+0.234 (n=668)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9409 (IC base=+0.060)

- **PATRÓN** `dist_vwap_pct` > `0.1402` → IC=+0.340 (n=461)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1402 (IC base=+0.060)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.1` → IC=+0.204 (n=1465)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.1 (IC base=+0.060)

- **PATRÓN** `volumen_regimen` > `1.0993` → IC=+0.352 (n=363)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0993 (IC base=+0.060)

- **PATRÓN** `volumen_pendiente_norm` < `0.1677` → IC=+0.338 (n=647)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1677 (IC base=+0.060)

- **PATRÓN** `volumen_pendiente_norm` > `0.3054` → IC=+0.337 (n=219)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3054 (IC base=+0.060)

- **PATRÓN** `volumen_spike_ratio` < `1.5423` → IC=+0.349 (n=343)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5423 (IC base=+0.060)

- **PATRÓN** `volumen_spike_ratio` > `2.2934` → IC=+0.342 (n=353)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2934 (IC base=+0.060)

- **PATRÓN** `ballena_activa_n` < `142.0` → IC=+0.340 (n=793)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 142.0 (IC base=+0.060)

- **PATRÓN** `ibs_20min` < `0.0867` → IC=+0.191 (n=1275)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.0867 (IC base=+0.054)

- **PATRÓN** `dist_vwap_pct` > `0.3398` → IC=+0.161 (n=615)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 0.3398 (IC base=+0.054)

- **PATRÓN** `volumen_regimen` < `1.0081` → IC=+0.162 (n=2160)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.0081 (IC base=+0.054)

- **PATRÓN** `volumen_pendiente_norm` > `0.2804` → IC=+0.212 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2804 (IC base=+0.054)

- **PATRÓN** `volumen_spike_ratio` < `1.77` → IC=+0.158 (n=1576)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.77 (IC base=+0.054)

- **PATRÓN** `volumen_spike_ratio` > `1.5076` → IC=+0.161 (n=2110)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.5076 (IC base=+0.054)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.176 (n=146)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=779)

- **FILTRO** `ibs_20min` < `0.2667` → IC=-0.178 (n=231)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2667
  - _Potencial_: sin este filtro IC_bueno=+0.085 (n=694)

- **FILTRO** `ibs_20min` > `0.2` → IC=-0.131 (n=4789)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2
  - _Potencial_: sin este filtro IC_bueno=+0.154 (n=2390)

- **FILTRO** `sigma_ewma_delta_pct` > `8.298` → IC=-0.229 (n=774)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.298
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=6405)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.177 (n=317)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.75 (IC base=+0.019)

- **PATRÓN** `dist_vwap_pct` > `0.9797` → IC=+0.283 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9797 (IC base=+0.019)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.888` → IC=+0.154 (n=218)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 4.888 (IC base=+0.019)

- **PATRÓN** `volumen_regimen` > `0.6233` → IC=+0.286 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6233 (IC base=+0.019)

- **PATRÓN** `volumen_pendiente_norm` < `0.0791` → IC=+0.280 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0791 (IC base=+0.019)

- **PATRÓN** `volumen_spike_ratio` < `2.1989` → IC=+0.287 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1989 (IC base=+0.019)

- **PATRÓN** `volumen_spike_ratio` > `1.544` → IC=+0.266 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.544 (IC base=+0.019)

- **PATRÓN** `ballena_activa_n` < `41.0` → IC=+0.271 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 41.0 (IC base=+0.019)

- **PATRÓN** `ibs_20min` < `0.2` → IC=+0.154 (n=2390)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.2 (IC base=-0.036)

- **PATRÓN** `dist_vwap_pct` > `0.5075` → IC=+0.294 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5075 (IC base=-0.036)

- **PATRÓN** `volumen_regimen` < `0.7051` → IC=+0.302 (n=467)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7051 (IC base=-0.036)

- **PATRÓN** `volumen_pendiente_norm` > `0.08` → IC=+0.308 (n=477)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.08 (IC base=-0.036)

- **PATRÓN** `volumen_spike_ratio` < `2.4762` → IC=+0.299 (n=991)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4762 (IC base=-0.036)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `ibs_20min` < `0.7885` → IC=-0.156 (n=3678)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7885
  - _Potencial_: sin este filtro IC_bueno=+0.134 (n=1898)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.173 (n=1184)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=4392)

- **FILTRO** `ibs_20min` > `0.736` → IC=-0.189 (n=1923)

  - _Acción_: SKIP cuando `ibs_20min` > 0.736
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=5773)

- **PATRÓN** `ibs_20min` > `0.7885` → IC=+0.134 (n=1898)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` > 0.7885 (IC base=-0.057)

- **PATRÓN** `dist_vwap_pct` > `1.0084` → IC=+0.356 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0084 (IC base=-0.057)

- **PATRÓN** `volumen_regimen` > `0.7047` → IC=+0.319 (n=981)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7047 (IC base=-0.057)

- **PATRÓN** `volumen_pendiente_norm` < `0.1065` → IC=+0.302 (n=1045)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1065 (IC base=-0.057)

- **PATRÓN** `volumen_spike_ratio` < `1.5808` → IC=+0.304 (n=473)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5808 (IC base=-0.057)

- **PATRÓN** `volumen_spike_ratio` > `2.5237` → IC=+0.320 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5237 (IC base=-0.057)

- **PATRÓN** `dist_vwap_pct` > `0.8149` → IC=+0.275 (n=367)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8149 (IC base=+0.004)

- **PATRÓN** `volumen_regimen` < `0.6428` → IC=+0.273 (n=754)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6428 (IC base=+0.004)

- **PATRÓN** `volumen_regimen` > `1.0651` → IC=+0.283 (n=1025)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0651 (IC base=+0.004)

- **PATRÓN** `volumen_pendiente_norm` > `0.1702` → IC=+0.286 (n=602)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1702 (IC base=+0.004)

- **PATRÓN** `volumen_spike_ratio` < `2.1758` → IC=+0.265 (n=1878)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1758 (IC base=+0.004)

- **PATRÓN** `volumen_spike_ratio` > `1.4406` → IC=+0.271 (n=2133)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4406 (IC base=+0.004)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.196 (n=7799)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` > 0.0107 (IC base=+0.087)

- **PATRÓN** `ibs_20min` > `0.8673` → IC=+0.285 (n=10600)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8673 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` > `0.9332` → IC=+0.302 (n=1621)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9332 (IC base=+0.087)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.468` → IC=+0.168 (n=10483)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 3.468 (IC base=+0.087)

- **PATRÓN** `volumen_regimen` > `0.693` → IC=+0.278 (n=7704)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.693 (IC base=+0.087)

- **PATRÓN** `volumen_pendiente_norm` > `0.2934` → IC=+0.294 (n=1934)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2934 (IC base=+0.087)

- **PATRÓN** `volumen_spike_ratio` > `2.6489` → IC=+0.286 (n=4525)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6489 (IC base=+0.087)

- **PATRÓN** `ballena_activa_n` < `89.0` → IC=+0.309 (n=13190)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 89.0 (IC base=+0.087)

- **PATRÓN** `sigma_h` > `0.0102` → IC=+0.157 (n=7544)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0102 (IC base=+0.084)

- **PATRÓN** `ibs_20min` < `0.52` → IC=+0.172 (n=19878)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.52 (IC base=+0.084)

- **PATRÓN** `volumen_regimen` < `0.6989` → IC=+0.283 (n=3310)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6989 (IC base=+0.084)

- **PATRÓN** `volumen_regimen` > `1.1872` → IC=+0.282 (n=2507)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1872 (IC base=+0.084)

- **PATRÓN** `volumen_pendiente_norm` > `0.294` → IC=+0.330 (n=1676)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.294 (IC base=+0.084)

- **PATRÓN** `volumen_spike_ratio` < `1.4529` → IC=+0.306 (n=3704)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4529 (IC base=+0.084)

- **PATRÓN** `volumen_spike_ratio` > `2.2751` → IC=+0.304 (n=5035)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2751 (IC base=+0.084)

- **PATRÓN** `ballena_activa_n` < `72.0` → IC=+0.312 (n=11083)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 72.0 (IC base=+0.084)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.8028` → IC=-0.135 (n=4152)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8028
  - _Potencial_: sin este filtro IC_bueno=+0.302 (n=2139)

- **FILTRO** `ibs_20min` > `0.7143` → IC=-0.236 (n=1387)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7143
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=4165)

- **FILTRO** `sigma_ewma_delta_pct` > `4.086` → IC=-0.236 (n=1200)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.086
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=4352)

- **PATRÓN** `ibs_20min` > `0.8028` → IC=+0.302 (n=2139)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8028 (IC base=+0.014)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.959` → IC=+0.190 (n=2098)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 2.959 (IC base=+0.014)

- **PATRÓN** `volumen_pendiente_norm` > `0.2294` → IC=+0.331 (n=401)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2294 (IC base=+0.014)

- **PATRÓN** `volumen_spike_ratio` < `1.4484` → IC=+0.282 (n=667)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4484 (IC base=+0.014)

- **PATRÓN** `volumen_spike_ratio` > `2.2443` → IC=+0.304 (n=906)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2443 (IC base=+0.014)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.320 (n=1383)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.014)

- **PATRÓN** `ibs_20min` < `0.1743` → IC=+0.170 (n=1389)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.1743 (IC base=-0.021)

- **PATRÓN** `volumen_pendiente_norm` < `0.1506` → IC=+0.405 (n=1099)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1506 (IC base=-0.021)

- **PATRÓN** `volumen_spike_ratio` < `1.5277` → IC=+0.425 (n=467)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5277 (IC base=-0.021)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.401 (n=1102)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 23.0 (IC base=-0.021)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.3001` → IC=+0.226 (n=750)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3001 (IC base=+0.011)

- **PATRÓN** `volumen_regimen` < `1.1951` → IC=+0.211 (n=2292)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1951 (IC base=+0.011)

- **PATRÓN** `volumen_regimen` > `0.6955` → IC=+0.218 (n=2048)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6955 (IC base=+0.011)

- **PATRÓN** `volumen_pendiente_norm` > `0.2762` → IC=+0.245 (n=308)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2762 (IC base=+0.011)

- **PATRÓN** `volumen_spike_ratio` < `1.4168` → IC=+0.228 (n=755)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4168 (IC base=+0.011)

- **PATRÓN** `ballena_activa_n` < `258.0` → IC=+0.244 (n=1507)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 258.0 (IC base=+0.011)

- **PATRÓN** `volumen_regimen` < `0.6851` → IC=+0.251 (n=714)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6851 (IC base=-0.002)

- **PATRÓN** `volumen_regimen` > `0.6162` → IC=+0.255 (n=1623)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6162 (IC base=-0.002)

- **PATRÓN** `volumen_pendiente_norm` > `0.2697` → IC=+0.301 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2697 (IC base=-0.002)

- **PATRÓN** `volumen_spike_ratio` < `1.5223` → IC=+0.262 (n=691)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5223 (IC base=-0.002)

- **PATRÓN** `volumen_spike_ratio` > `2.1414` → IC=+0.262 (n=712)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1414 (IC base=-0.002)

- **PATRÓN** `ballena_activa_n` < `185.0` → IC=+0.285 (n=528)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 185.0 (IC base=-0.002)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0095` → IC=+0.321 (n=2180)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0095 (IC base=+0.284)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.293 (n=3276)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.284)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.325 (n=1778)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.284)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.584` → IC=+0.315 (n=1102)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.584 (IC base=+0.284)

- **PATRÓN** `volumen_pendiente_norm` < `0.0976` → IC=+0.297 (n=2877)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0976 (IC base=+0.284)

- **PATRÓN** `volumen_spike_ratio` > `1.6075` → IC=+0.290 (n=3179)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6075 (IC base=+0.284)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.293 (n=3926)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.284)

- **PATRÓN** `libro_liquidez` > `2013.3448` → IC=+0.294 (n=1090)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2013.3448 (IC base=+0.284)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.307 (n=1981)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 14.0 (IC base=+0.284)

- **PATRÓN** `sigma_h` > `0.0106` → IC=+0.340 (n=1351)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0106 (IC base=+0.307)

- **PATRÓN** `drift_60min` |x|≤ `0.1772` → IC=+0.326 (n=1310)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1772 (IC base=+0.307)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.326 (n=1144)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.307)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.310 (n=1344)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.307)

- **PATRÓN** `ibs_20min` > `0.148` → IC=+0.318 (n=1984)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.148 (IC base=+0.307)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.122` → IC=+0.310 (n=356)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.122 (IC base=+0.307)

- **PATRÓN** `volumen_pendiente_norm` < `0.1991` → IC=+0.307 (n=2929)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1991 (IC base=+0.307)

- **PATRÓN** `volumen_pendiente_norm` > `0.3449` → IC=+0.319 (n=484)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3449 (IC base=+0.307)

- **PATRÓN** `volumen_spike_ratio` > `2.7378` → IC=+0.325 (n=1303)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7378 (IC base=+0.307)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.307 (n=1513)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.307)

- **PATRÓN** `libro_liquidez` > `1992.8384` → IC=+0.313 (n=992)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1992.8384 (IC base=+0.307)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.312 (n=2499)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 22.0 (IC base=+0.307)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7218` → IC=-0.178 (n=1475)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7218
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=4428)

- **PATRÓN** `dist_vwap_pct` > `0.1449` → IC=+0.238 (n=1056)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1449 (IC base=+0.020)

- **PATRÓN** `volumen_regimen` < `1.1593` → IC=+0.236 (n=2098)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1593 (IC base=+0.020)

- **PATRÓN** `volumen_pendiente_norm` < `0.1626` → IC=+0.236 (n=2202)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1626 (IC base=+0.020)

- **PATRÓN** `volumen_pendiente_norm` > `0.1029` → IC=+0.241 (n=686)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1029 (IC base=+0.020)

- **PATRÓN** `volumen_spike_ratio` < `2.4363` → IC=+0.240 (n=2036)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4363 (IC base=+0.020)

- **PATRÓN** `ballena_activa_n` < `113.0` → IC=+0.254 (n=2072)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 113.0 (IC base=+0.020)

- **PATRÓN** `ibs_20min` < `0.092` → IC=+0.158 (n=1476)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.092 (IC base=+0.007)

- **PATRÓN** `dist_vwap_pct` > `0.7339` → IC=+0.261 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7339 (IC base=+0.007)

- **PATRÓN** `volumen_regimen` < `1.1812` → IC=+0.265 (n=1516)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1812 (IC base=+0.007)

- **PATRÓN** `volumen_pendiente_norm` > `0.2817` → IC=+0.318 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2817 (IC base=+0.007)

- **PATRÓN** `volumen_spike_ratio` < `1.7856` → IC=+0.292 (n=972)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7856 (IC base=+0.007)

- **PATRÓN** `volumen_spike_ratio` > `2.426` → IC=+0.279 (n=486)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.426 (IC base=+0.007)

- **PATRÓN** `ballena_activa_n` < `115.0` → IC=+0.283 (n=1483)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 115.0 (IC base=+0.007)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7407` → IC=-0.250 (n=2409)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7407
  - _Potencial_: sin este filtro IC_bueno=+0.313 (n=2416)

- **FILTRO** `ibs_20min` > `0.6182` → IC=-0.234 (n=1141)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6182
  - _Potencial_: sin este filtro IC_bueno=+0.155 (n=3427)

- **FILTRO** `sigma_ewma_delta_pct` > `8.282` → IC=-0.263 (n=522)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.282
  - _Potencial_: sin este filtro IC_bueno=+0.099 (n=4046)

- **PATRÓN** `ibs_20min` > `0.7407` → IC=+0.313 (n=2416)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7407 (IC base=+0.032)

- **PATRÓN** `dist_vwap_pct` > `1.0425` → IC=+0.357 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0425 (IC base=+0.032)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.456` → IC=+0.155 (n=1958)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 2.456 (IC base=+0.032)

- **PATRÓN** `volumen_regimen` < `0.842` → IC=+0.345 (n=1171)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.842 (IC base=+0.032)

- **PATRÓN** `volumen_regimen` > `0.696` → IC=+0.335 (n=1569)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.696 (IC base=+0.032)

- **PATRÓN** `volumen_pendiente_norm` < `0.1567` → IC=+0.336 (n=1809)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1567 (IC base=+0.032)

- **PATRÓN** `volumen_pendiente_norm` > `0.274` → IC=+0.364 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.274 (IC base=+0.032)

- **PATRÓN** `volumen_spike_ratio` < `1.4239` → IC=+0.360 (n=569)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4239 (IC base=+0.032)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.355 (n=1519)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=+0.032)

- **PATRÓN** `ibs_20min` < `0.6182` → IC=+0.155 (n=3427)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.6182 (IC base=+0.058)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.052` → IC=+0.132 (n=3216)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` < 3.052 (IC base=+0.058)

- **PATRÓN** `volumen_regimen` < `0.6947` → IC=+0.282 (n=760)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6947 (IC base=+0.058)

- **PATRÓN** `volumen_pendiente_norm` > `0.071` → IC=+0.293 (n=695)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.071 (IC base=+0.058)

- **PATRÓN** `volumen_spike_ratio` < `1.8044` → IC=+0.279 (n=1117)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8044 (IC base=+0.058)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.287 (n=1703)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 46.0 (IC base=+0.058)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0156` → IC=+0.361 (n=1652)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0156 (IC base=+0.316)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.318 (n=2506)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.316)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.318 (n=2600)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.316)

- **PATRÓN** `ibs_20min` > `0.66` → IC=+0.344 (n=2480)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.66 (IC base=+0.316)

- **PATRÓN** `dist_vwap_pct` > `0.2942` → IC=+0.339 (n=1193)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2942 (IC base=+0.316)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.76` → IC=+0.335 (n=1211)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.76 (IC base=+0.316)

- **PATRÓN** `volumen_regimen` > `0.6296` → IC=+0.327 (n=2477)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6296 (IC base=+0.316)

- **PATRÓN** `volumen_pendiente_norm` > `0.2814` → IC=+0.347 (n=363)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2814 (IC base=+0.316)

- **PATRÓN** `volumen_spike_ratio` > `1.5299` → IC=+0.329 (n=2135)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5299 (IC base=+0.316)

- **PATRÓN** `libro_liquidez` > `2995.543` → IC=+0.330 (n=826)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2995.543 (IC base=+0.316)

- **PATRÓN** `ballena_activa_n` < `33.0` → IC=+0.342 (n=1960)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 33.0 (IC base=+0.316)

- **PATRÓN** `sigma_h` > `0.0149` → IC=+0.351 (n=1769)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0149 (IC base=+0.315)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.318 (n=1348)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.315)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.318 (n=1281)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.315)

- **PATRÓN** `ibs_20min` < `0.3818` → IC=+0.333 (n=2654)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3818 (IC base=+0.315)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.305` → IC=+0.329 (n=494)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.305 (IC base=+0.315)

- **PATRÓN** `volumen_regimen` < `0.7201` → IC=+0.321 (n=1168)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7201 (IC base=+0.315)

- **PATRÓN** `volumen_regimen` > `1.2061` → IC=+0.343 (n=885)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2061 (IC base=+0.315)

- **PATRÓN** `volumen_pendiente_norm` > `0.23` → IC=+0.364 (n=500)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.23 (IC base=+0.315)

- **PATRÓN** `volumen_spike_ratio` < `1.4131` → IC=+0.322 (n=824)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4131 (IC base=+0.315)

- **PATRÓN** `volumen_spike_ratio` > `2.1399` → IC=+0.316 (n=1121)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1399 (IC base=+0.315)

- **PATRÓN** `libro_liquidez` > `2981.8454` → IC=+0.316 (n=885)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2981.8454 (IC base=+0.315)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.223 (n=5789)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0125 (IC base=+0.173)

- **PATRÓN** `drift_60min` |x|≤ `0.1221` → IC=+0.191 (n=7633)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.1221 (IC base=+0.173)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.183 (n=17998)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.173)

- **PATRÓN** `ibs_20min` > `0.5377` → IC=+0.230 (n=17348)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5377 (IC base=+0.173)

- **PATRÓN** `dist_vwap_pct` > `0.1626` → IC=+0.205 (n=6531)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1626 (IC base=+0.173)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.748` → IC=+0.259 (n=3386)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.748 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` < `1.1782` → IC=+0.152 (n=11557)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.1782 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` > `0.6249` → IC=+0.152 (n=11560)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.6249 (IC base=+0.173)

- **PATRÓN** `volumen_pendiente_norm` > `0.2936` → IC=+0.203 (n=2506)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2936 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` > `2.6049` → IC=+0.186 (n=5627)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.6049 (IC base=+0.173)

- **PATRÓN** `ballena_activa_n` < `86.0` → IC=+0.191 (n=16255)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 86.0 (IC base=+0.173)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.193 (n=7523)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0059 (IC base=+0.185)

- **PATRÓN** `drift_60min` |x|≤ `0.0808` → IC=+0.223 (n=5697)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0808 (IC base=+0.185)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.211 (n=6442)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.185)

- **PATRÓN** `ibs_20min` < `0.5254` → IC=+0.240 (n=17092)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5254 (IC base=+0.185)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.505` → IC=+0.189 (n=2719)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 9.505 (IC base=+0.185)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.512` → IC=+0.192 (n=15228)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` < 2.512 (IC base=+0.185)

- **PATRÓN** `volumen_regimen` < `1.1824` → IC=+0.165 (n=12150)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.1824 (IC base=+0.185)

- **PATRÓN** `volumen_pendiente_norm` > `0.2933` → IC=+0.220 (n=2564)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2933 (IC base=+0.185)

- **PATRÓN** `volumen_spike_ratio` > `2.6272` → IC=+0.195 (n=5426)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.6272 (IC base=+0.185)

- **PATRÓN** `ballena_activa_n` < `91.0` → IC=+0.199 (n=16087)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 91.0 (IC base=+0.185)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `drift_60min` |x|≤ `0.104` → IC=+0.257 (n=1255)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.104 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.234 (n=2968)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.227)

- **PATRÓN** `ibs_20min` > `0.9425` → IC=+0.295 (n=1902)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9425 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.449` → IC=+0.328 (n=934)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.449 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` > `0.2808` → IC=+0.288 (n=432)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2808 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` < `1.8356` → IC=+0.225 (n=1816)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8356 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` > `1.4355` → IC=+0.226 (n=2723)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4355 (IC base=+0.227)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.237 (n=3176)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.227)

- **PATRÓN** `sigma_h` < `0.0099` → IC=+0.259 (n=2334)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0099 (IC base=+0.257)

- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.260 (n=1059)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0089 (IC base=+0.257)

- **PATRÓN** `drift_60min` |x|≤ `0.0969` → IC=+0.315 (n=1027)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0969 (IC base=+0.257)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.262 (n=2411)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.257)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.264 (n=1578)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.257)

- **PATRÓN** `ibs_20min` < `0.4396` → IC=+0.274 (n=2333)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4396 (IC base=+0.257)

- **PATRÓN** `volumen_pendiente_norm` < `0.0985` → IC=+0.261 (n=2049)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0985 (IC base=+0.257)

- **PATRÓN** `volumen_pendiente_norm` > `0.301` → IC=+0.269 (n=349)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.301 (IC base=+0.257)

- **PATRÓN** `volumen_spike_ratio` < `1.4456` → IC=+0.277 (n=746)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4456 (IC base=+0.257)

- **PATRÓN** `volumen_spike_ratio` > `2.679` → IC=+0.258 (n=746)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.679 (IC base=+0.257)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.267 (n=1675)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.257)

- **PATRÓN** `libro_liquidez` > `1773.106` → IC=+0.268 (n=1555)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1773.106 (IC base=+0.257)

- **PATRÓN** `ballena_activa_n` < `7.0` → IC=+0.258 (n=869)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 7.0 (IC base=+0.257)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.198 (n=882)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0031 (IC base=+0.128)

- **PATRÓN** `drift_60min` |x|≤ `0.0646` → IC=+0.178 (n=880)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.0646 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.145 (n=2761)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` > `0.2602` → IC=+0.205 (n=2640)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2602 (IC base=+0.128)

- **PATRÓN** `dist_vwap_pct` > `0.1843` → IC=+0.212 (n=1309)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1843 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.616` → IC=+0.210 (n=481)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.616 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` < `0.6953` → IC=+0.132 (n=1162)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 0.6953 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` > `1.0545` → IC=+0.135 (n=1198)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` > 1.0545 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` > `0.2795` → IC=+0.167 (n=409)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.2795 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` < `1.5055` → IC=+0.133 (n=1142)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 1.5055 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` > `2.4677` → IC=+0.149 (n=865)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 2.4677 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `212.0` → IC=+0.142 (n=1127)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 212.0 (IC base=+0.128)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.172 (n=2812)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0065 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.2391` → IC=+0.175 (n=2473)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.2391 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.182 (n=1338)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 15.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` < `0.6098` → IC=+0.211 (n=2810)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6098 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.87` → IC=+0.178 (n=529)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 10.87 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.032` → IC=+0.154 (n=2452)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 4.032 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `1.1967` → IC=+0.162 (n=2810)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.1967 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` < `0.2279` → IC=+0.154 (n=2979)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` < 0.2279 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `2.4631` → IC=+0.155 (n=2685)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.4631 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `208.0` → IC=+0.197 (n=1151)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 208.0 (IC base=+0.150)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0115` → IC=+0.230 (n=1337)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0115 (IC base=+0.211)

- **PATRÓN** `drift_60min` |x|≤ `0.2489` → IC=+0.233 (n=1960)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2489 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.219 (n=3059)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.291 (n=1566)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.064` → IC=+0.304 (n=698)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.064 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` < `0.0988` → IC=+0.210 (n=2561)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0988 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.3513` → IC=+0.241 (n=415)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3513 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `2.71` → IC=+0.227 (n=1301)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.71 (IC base=+0.211)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.215 (n=3553)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `2000.58` → IC=+0.224 (n=980)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2000.58 (IC base=+0.211)

- **PATRÓN** `sigma_h` < `0.0118` → IC=+0.247 (n=2608)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0118 (IC base=+0.240)

- **PATRÓN** `drift_60min` |x|≤ `0.4114` → IC=+0.263 (n=2295)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4114 (IC base=+0.240)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.278 (n=1003)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.240)

- **PATRÓN** `ibs_20min` < `0.0426` → IC=+0.291 (n=1149)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0426 (IC base=+0.240)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.896` → IC=+0.278 (n=341)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.896 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` > `0.3545` → IC=+0.287 (n=435)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3545 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` < `1.7675` → IC=+0.241 (n=1109)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7675 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` > `2.1766` → IC=+0.251 (n=1680)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1766 (IC base=+0.240)

- **PATRÓN** `libro_liquidez` > `1874.7184` → IC=+0.250 (n=1182)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1874.7184 (IC base=+0.240)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.241 (n=1665)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.240)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.201 (n=957)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0038 (IC base=+0.128)

- **PATRÓN** `drift_60min` |x|≤ `0.0783` → IC=+0.184 (n=953)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.0783 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.138 (n=2957)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` > `0.2458` → IC=+0.190 (n=2858)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.2458 (IC base=+0.128)

- **PATRÓN** `dist_vwap_pct` > `0.1399` → IC=+0.186 (n=1628)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1399 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.227` → IC=+0.202 (n=492)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.227 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` < `0.8417` → IC=+0.137 (n=1908)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.8417 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` > `0.2875` → IC=+0.167 (n=431)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` > 0.2875 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` > `2.5096` → IC=+0.142 (n=933)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 2.5096 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `6839.7566` → IC=+0.197 (n=1296)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 6839.7566 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `126.0` → IC=+0.127 (n=2803)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 126.0 (IC base=+0.128)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.165 (n=2680)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0067 (IC base=+0.131)

- **PATRÓN** `drift_60min` |x|≤ `0.398` → IC=+0.147 (n=3043)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.398 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.167 (n=1456)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 15.0 (IC base=+0.131)

- **PATRÓN** `ibs_20min` < `0.6746` → IC=+0.186 (n=3044)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.6746 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.213` → IC=+0.141 (n=730)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 9.213 (IC base=+0.131)

- **PATRÓN** `volumen_regimen` < `0.8521` → IC=+0.152 (n=2030)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.8521 (IC base=+0.131)

- **PATRÓN** `volumen_pendiente_norm` > `0.2941` → IC=+0.175 (n=454)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.2941 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` < `1.8021` → IC=+0.133 (n=1926)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 1.8021 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` > `1.5182` → IC=+0.131 (n=2580)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 1.5182 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `6338.4359` → IC=+0.190 (n=1380)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 6338.4359 (IC base=+0.131)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.158 (n=959)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 48.0 (IC base=+0.131)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0126` → IC=+0.165 (n=1065)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` > 0.0126 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.133 (n=3274)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 5.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` > `0.4706` → IC=+0.204 (n=3202)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4706 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` > `0.1984` → IC=+0.187 (n=1695)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1984 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.972` → IC=+0.287 (n=674)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.972 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` < `1.1668` → IC=+0.128 (n=3194)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 1.1668 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` < `0.163` → IC=+0.122 (n=3256)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_pendiente_norm` < 0.163 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` < `1.7785` → IC=+0.123 (n=2066)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 1.7785 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `2666.8655` → IC=+0.197 (n=1448)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 2666.8655 (IC base=+0.118)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.132 (n=1056)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 16.0 (IC base=+0.118)

- **PATRÓN** `sigma_h` < `0.0119` → IC=+0.143 (n=3333)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.0119 (IC base=+0.120)

- **PATRÓN** `drift_60min` |x|≤ `0.113` → IC=+0.165 (n=1111)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.113 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.135 (n=3406)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 5.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` < `0.65` → IC=+0.220 (n=3334)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.65 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.243` → IC=+0.141 (n=2949)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` < 2.243 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` < `1.1756` → IC=+0.127 (n=3331)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` < 1.1756 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` > `0.275` → IC=+0.149 (n=463)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.275 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` < `1.4348` → IC=+0.136 (n=1051)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.4348 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` > `2.4431` → IC=+0.133 (n=1050)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 2.4431 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `2901.4859` → IC=+0.196 (n=1110)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 2901.4859 (IC base=+0.120)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.126 (n=1054)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 15.0 (IC base=+0.120)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.013` → IC=+0.251 (n=2561)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.013 (IC base=+0.226)

- **PATRÓN** `drift_60min` |x|≤ `0.1653` → IC=+0.243 (n=1262)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1653 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.232 (n=2979)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.226)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.228 (n=2585)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.226)

- **PATRÓN** `ibs_20min` > `0.6667` → IC=+0.258 (n=2868)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6667 (IC base=+0.226)

- **PATRÓN** `dist_vwap_pct` > `0.1809` → IC=+0.233 (n=1745)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1809 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.534` → IC=+0.258 (n=1305)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.534 (IC base=+0.226)

- **PATRÓN** `volumen_regimen` > `0.624` → IC=+0.236 (n=2867)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.624 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` > `0.2348` → IC=+0.264 (n=535)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2348 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` < `2.472` → IC=+0.230 (n=2797)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.472 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` > `1.4338` → IC=+0.231 (n=2797)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4338 (IC base=+0.226)

- **PATRÓN** `libro_liquidez` > `2591.4283` → IC=+0.230 (n=1911)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2591.4283 (IC base=+0.226)

- **PATRÓN** `sigma_h` < `0.0125` → IC=+0.243 (n=1308)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0125 (IC base=+0.240)

- **PATRÓN** `sigma_h` > `0.0226` → IC=+0.249 (n=1347)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0226 (IC base=+0.240)

- **PATRÓN** `drift_60min` |x|≤ `0.5827` → IC=+0.250 (n=2967)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5827 (IC base=+0.240)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.251 (n=1454)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.240)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.248 (n=1322)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.240)

- **PATRÓN** `ibs_20min` < `0.44` → IC=+0.263 (n=2977)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.44 (IC base=+0.240)

- **PATRÓN** `dist_vwap_pct` > `1.1437` → IC=+0.259 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1437 (IC base=+0.240)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.134` → IC=+0.268 (n=568)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.134 (IC base=+0.240)

- **PATRÓN** `volumen_regimen` < `0.8673` → IC=+0.242 (n=1978)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8673 (IC base=+0.240)

- **PATRÓN** `volumen_regimen` > `0.641` → IC=+0.243 (n=2967)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.641 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` > `0.2803` → IC=+0.293 (n=409)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2803 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` < `2.5134` → IC=+0.238 (n=2800)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5134 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` > `1.55` → IC=+0.242 (n=2502)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.55 (IC base=+0.240)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.208 (n=1497)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.157)

- **PATRÓN** `drift_60min` |x|≤ `0.1344` → IC=+0.172 (n=1975)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.1344 (IC base=+0.157)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.170 (n=4677)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 5.0 (IC base=+0.157)

- **PATRÓN** `ibs_20min` > `0.3053` → IC=+0.195 (n=4479)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 0.3053 (IC base=+0.157)

- **PATRÓN** `dist_vwap_pct` > `0.2221` → IC=+0.181 (n=1689)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.2221 (IC base=+0.157)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.538` → IC=+0.209 (n=733)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.538 (IC base=+0.157)

- **PATRÓN** `volumen_regimen` < `0.8606` → IC=+0.167 (n=2708)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 0.8606 (IC base=+0.157)

- **PATRÓN** `volumen_regimen` > `1.1931` → IC=+0.162 (n=1354)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 1.1931 (IC base=+0.157)

- **PATRÓN** `volumen_pendiente_norm` > `0.1571` → IC=+0.172 (n=1177)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.1571 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` < `1.5265` → IC=+0.161 (n=1922)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 1.5265 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` > `1.809` → IC=+0.160 (n=2911)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.809 (IC base=+0.157)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.158 (n=5002)

  - _Acción_: Kelly boost +0.79€ cuando `libro_spread` < 0.02 (IC base=+0.157)

- **PATRÓN** `libro_liquidez` > `7598.2599` → IC=+0.184 (n=2031)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 7598.2599 (IC base=+0.157)

- **PATRÓN** `ibs_20min` < `0.3839` → IC=+0.175 (n=3254)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.3839 (IC base=+0.096)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.137 (n=2101)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 23.0 (IC base=+0.096)

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

- **PATRÓN** `ibs_20min` < `0.2049` → IC=+0.198 (n=628)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.2049 (IC base=+0.082)

- **PATRÓN** `ballena_activa_n` < `164.0` → IC=+0.177 (n=614)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 164.0 (IC base=+0.082)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.235 (n=601)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.152)

- **PATRÓN** `drift_60min` |x|≤ `0.2092` → IC=+0.156 (n=907)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.2092 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.172 (n=1411)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 5.0 (IC base=+0.152)

- **PATRÓN** `ibs_20min` > `0.7914` → IC=+0.266 (n=617)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7914 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` > `0.8171` → IC=+0.192 (n=222)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.8171 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.87` → IC=+0.208 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.87 (IC base=+0.152)

- **PATRÓN** `volumen_regimen` < `0.8313` → IC=+0.165 (n=907)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8313 (IC base=+0.152)

- **PATRÓN** `volumen_pendiente_norm` > `0.2193` → IC=+0.199 (n=247)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2193 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` > `1.7764` → IC=+0.170 (n=894)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 1.7764 (IC base=+0.152)

- **PATRÓN** `libro_liquidez` > `8031.121` → IC=+0.175 (n=617)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 8031.121 (IC base=+0.152)

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.125 (n=886)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0052 (IC base=+0.094)

- **PATRÓN** `ibs_20min` < `0.0855` → IC=+0.212 (n=443)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0855 (IC base=+0.094)

- **PATRÓN** `volumen_regimen` < `0.6781` → IC=+0.126 (n=584)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` < 0.6781 (IC base=+0.094)

- **PATRÓN** `libro_liquidez` > `7964.2063` → IC=+0.152 (n=602)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 7964.2063 (IC base=+0.094)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.133 (n=439)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 35.0 (IC base=+0.094)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.153 (n=387)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0067 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.165 (n=811)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 11.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` > `0.5385` → IC=+0.193 (n=1040)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.5385 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` > `0.939` → IC=+0.165 (n=189)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.939 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.857` → IC=+0.226 (n=454)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.857 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` < `1.0462` → IC=+0.135 (n=1021)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 1.0462 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` > `0.7015` → IC=+0.131 (n=1036)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` > 0.7015 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` > `0.2253` → IC=+0.149 (n=203)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.2253 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` < `1.4128` → IC=+0.152 (n=375)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 1.4128 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.125 (n=1219)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.02 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `2758.7926` → IC=+0.165 (n=526)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 2758.7926 (IC base=+0.123)

- **PATRÓN** `ibs_20min` < `0.5556` → IC=+0.154 (n=1136)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.5556 (IC base=+0.076)

- **PATRÓN** `libro_liquidez` > `2635.7469` → IC=+0.166 (n=585)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2635.7469 (IC base=+0.076)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0166` → IC=+0.246 (n=266)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0166 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.223 (n=189)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.189)

- **PATRÓN** `ibs_20min` > `0.9618` → IC=+0.218 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9618 (IC base=+0.189)

- **PATRÓN** `dist_vwap_pct` > `0.3144` → IC=+0.207 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3144 (IC base=+0.189)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.64` → IC=+0.205 (n=395)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.64 (IC base=+0.189)

- **PATRÓN** `volumen_regimen` > `1.1931` → IC=+0.248 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1931 (IC base=+0.189)

- **PATRÓN** `volumen_pendiente_norm` > `0.0785` → IC=+0.198 (n=147)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.0785 (IC base=+0.189)

- **PATRÓN** `volumen_spike_ratio` < `2.1215` → IC=+0.202 (n=327)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1215 (IC base=+0.189)

- **PATRÓN** `volumen_spike_ratio` > `1.4093` → IC=+0.205 (n=371)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4093 (IC base=+0.189)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.202 (n=431)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.189)

- **PATRÓN** `libro_liquidez` > `2944.973` → IC=+0.205 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2944.973 (IC base=+0.189)

- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.167 (n=439)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.0107 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.659` → IC=+0.155 (n=439)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.659 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.190 (n=211)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 15.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` < `0.5043` → IC=+0.158 (n=387)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.5043 (IC base=+0.147)

- **PATRÓN** `ibs_20min` > `0.11` → IC=+0.148 (n=439)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` > 0.11 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` > `1.1805` → IC=+0.276 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1805 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.157` → IC=+0.152 (n=398)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` < 2.157 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` < `1.2353` → IC=+0.169 (n=439)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.2353 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` < `0.1126` → IC=+0.160 (n=401)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` < 0.1126 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` > `0.2284` → IC=+0.159 (n=83)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` > 0.2284 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `1.4819` → IC=+0.192 (n=141)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 1.4819 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` > `2.6304` → IC=+0.150 (n=141)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 2.6304 (IC base=+0.147)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.165 (n=416)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 19.0 (IC base=+0.147)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.229 (n=7592)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0125 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.190 (n=23750)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` > `0.4286` → IC=+0.227 (n=22775)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4286 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` > `0.8834` → IC=+0.212 (n=2651)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8834 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.934` → IC=+0.258 (n=5573)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.934 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `1.2136` → IC=+0.159 (n=15329)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2136 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.2409` → IC=+0.208 (n=4086)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2409 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `2.6235` → IC=+0.193 (n=7406)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.6235 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `102.0` → IC=+0.201 (n=21392)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 102.0 (IC base=+0.181)

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.200 (n=6990)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.196)

- **PATRÓN** `sigma_h` > `0.0122` → IC=+0.204 (n=6991)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0122 (IC base=+0.196)

- **PATRÓN** `drift_60min` |x|≤ `0.4833` → IC=+0.199 (n=20953)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4833 (IC base=+0.196)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.216 (n=7859)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.196)

- **PATRÓN** `ibs_20min` < `0.5923` → IC=+0.245 (n=20950)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5923 (IC base=+0.196)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.524` → IC=+0.202 (n=19452)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.524 (IC base=+0.196)

- **PATRÓN** `volumen_regimen` < `0.6321` → IC=+0.179 (n=4694)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 0.6321 (IC base=+0.196)

- **PATRÓN** `volumen_pendiente_norm` > `0.2929` → IC=+0.254 (n=2880)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2929 (IC base=+0.196)

- **PATRÓN** `volumen_spike_ratio` > `2.6253` → IC=+0.208 (n=6691)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6253 (IC base=+0.196)

- **PATRÓN** `ballena_activa_n` < `90.0` → IC=+0.213 (n=19822)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 90.0 (IC base=+0.196)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.252 (n=1767)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.236)

- **PATRÓN** `ibs_20min` > `0.8641` → IC=+0.297 (n=2425)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8641 (IC base=+0.236)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.821` → IC=+0.342 (n=871)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.821 (IC base=+0.236)

- **PATRÓN** `volumen_pendiente_norm` > `0.2323` → IC=+0.290 (n=654)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2323 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` < `1.4509` → IC=+0.233 (n=1172)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4509 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` > `2.2917` → IC=+0.243 (n=1595)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2917 (IC base=+0.236)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.250 (n=4014)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.236)

- **PATRÓN** `libro_liquidez` > `2035.06` → IC=+0.240 (n=1213)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2035.06 (IC base=+0.236)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.252 (n=2238)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 14.0 (IC base=+0.236)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.270 (n=3256)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0103 (IC base=+0.269)

- **PATRÓN** `sigma_h` > `0.0092` → IC=+0.273 (n=1480)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0092 (IC base=+0.269)

- **PATRÓN** `drift_60min` |x|≤ `0.1218` → IC=+0.294 (n=1432)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1218 (IC base=+0.269)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.270 (n=3385)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.269)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.272 (n=2938)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.269)

- **PATRÓN** `ibs_20min` < `0.55` → IC=+0.286 (n=3256)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.55 (IC base=+0.269)

- **PATRÓN** `volumen_pendiente_norm` < `0.1602` → IC=+0.271 (n=3287)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1602 (IC base=+0.269)

- **PATRÓN** `volumen_pendiente_norm` > `0.2892` → IC=+0.287 (n=449)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2892 (IC base=+0.269)

- **PATRÓN** `volumen_spike_ratio` < `1.5624` → IC=+0.274 (n=1376)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5624 (IC base=+0.269)

- **PATRÓN** `volumen_spike_ratio` > `2.6427` → IC=+0.280 (n=1042)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6427 (IC base=+0.269)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.275 (n=2326)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.269)

- **PATRÓN** `libro_liquidez` > `1773.4468` → IC=+0.278 (n=2170)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1773.4468 (IC base=+0.269)

- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.280 (n=1163)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 8.0 (IC base=+0.269)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.179 (n=1250)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0032 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.0791` → IC=+0.147 (n=1245)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.0791 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.149 (n=3892)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 5.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` > `0.1969` → IC=+0.188 (n=3729)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.1969 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` > `0.672` → IC=+0.207 (n=661)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.672 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.333` → IC=+0.167 (n=778)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 9.333 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `0.6364` → IC=+0.155 (n=1244)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.6364 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` > `1.0702` → IC=+0.142 (n=1691)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 1.0702 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.2707` → IC=+0.182 (n=524)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.2707 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `2.1707` → IC=+0.142 (n=3223)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.1707 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `1.5203` → IC=+0.143 (n=3272)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.5203 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `298.0` → IC=+0.153 (n=2412)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 298.0 (IC base=+0.137)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.164 (n=3227)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0065 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.0798` → IC=+0.169 (n=1077)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.0798 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.168 (n=1189)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 17.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` < `0.678` → IC=+0.188 (n=3227)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.678 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.014` → IC=+0.140 (n=1549)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 3.014 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.021` → IC=+0.140 (n=2915)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` < 4.021 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `1.0448` → IC=+0.153 (n=2840)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 1.0448 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.2196` → IC=+0.192 (n=599)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2196 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `2.4301` → IC=+0.146 (n=3118)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 2.4301 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `1.7693` → IC=+0.142 (n=2078)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.7693 (IC base=+0.139)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.140 (n=4193)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `222.0` → IC=+0.164 (n=1022)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 222.0 (IC base=+0.139)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.01` → IC=+0.240 (n=2526)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.01 (IC base=+0.228)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.237 (n=3971)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.228)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.228 (n=3388)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.228)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.302 (n=1412)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.228)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.987` → IC=+0.323 (n=845)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.987 (IC base=+0.228)

- **PATRÓN** `volumen_pendiente_norm` < `0.1322` → IC=+0.229 (n=3592)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1322 (IC base=+0.228)

- **PATRÓN** `volumen_pendiente_norm` > `0.3506` → IC=+0.231 (n=496)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3506 (IC base=+0.228)

- **PATRÓN** `volumen_spike_ratio` > `2.7503` → IC=+0.243 (n=1680)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7503 (IC base=+0.228)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.233 (n=4574)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.228)

- **PATRÓN** `libro_liquidez` > `2012.1448` → IC=+0.240 (n=1263)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2012.1448 (IC base=+0.228)

- **PATRÓN** `sigma_h` < `0.011` → IC=+0.249 (n=3195)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.011 (IC base=+0.245)

- **PATRÓN** `drift_60min` |x|≤ `0.1776` → IC=+0.265 (n=1596)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1776 (IC base=+0.245)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.262 (n=1387)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.245)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.248 (n=1648)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.245)

- **PATRÓN** `ibs_20min` < `0.0625` → IC=+0.304 (n=1220)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0625 (IC base=+0.245)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.04` → IC=+0.305 (n=382)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.04 (IC base=+0.245)

- **PATRÓN** `volumen_pendiente_norm` > `0.3478` → IC=+0.307 (n=547)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3478 (IC base=+0.245)

- **PATRÓN** `volumen_spike_ratio` > `2.1714` → IC=+0.257 (n=2333)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1714 (IC base=+0.245)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.249 (n=1850)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.245)

- **PATRÓN** `libro_liquidez` > `1988.0484` → IC=+0.257 (n=1209)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1988.0484 (IC base=+0.245)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.250 (n=3014)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 21.0 (IC base=+0.245)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.195 (n=1314)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0037 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.4315` → IC=+0.145 (n=3934)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.4315 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.150 (n=4084)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 5.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` > `0.8847` → IC=+0.269 (n=1312)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8847 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` > `0.1963` → IC=+0.169 (n=1759)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.1963 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.07` → IC=+0.166 (n=596)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 11.07 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `0.8592` → IC=+0.153 (n=2624)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.8592 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.2331` → IC=+0.188 (n=696)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.2331 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `1.5173` → IC=+0.153 (n=1694)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 1.5173 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `2.1678` → IC=+0.143 (n=1744)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 2.1678 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `7289.8412` → IC=+0.239 (n=1312)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7289.8412 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `87.0` → IC=+0.145 (n=2567)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 87.0 (IC base=+0.138)

- **PATRÓN** `sigma_h` < `0.0078` → IC=+0.165 (n=3301)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0078 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.4365` → IC=+0.159 (n=3301)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.4365 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.175 (n=1219)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 17.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` < `0.7057` → IC=+0.199 (n=3301)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.7057 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.009` → IC=+0.155 (n=653)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 9.009 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.029` → IC=+0.151 (n=2882)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` < 3.029 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `0.69` → IC=+0.167 (n=1453)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.69 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` > `0.2941` → IC=+0.214 (n=418)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2941 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `2.2099` → IC=+0.152 (n=2807)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.2099 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` > `1.5286` → IC=+0.155 (n=2849)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.5286 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `6526.3907` → IC=+0.224 (n=1101)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6526.3907 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `58.0` → IC=+0.171 (n=1108)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 58.0 (IC base=+0.148)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0127` → IC=+0.151 (n=1335)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` > 0.0127 (IC base=+0.115)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.147 (n=2834)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 11.0 (IC base=+0.115)

- **PATRÓN** `ibs_20min` > `0.4286` → IC=+0.186 (n=4013)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.4286 (IC base=+0.115)

- **PATRÓN** `dist_vwap_pct` > `1.0085` → IC=+0.199 (n=646)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0085 (IC base=+0.115)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.235` → IC=+0.272 (n=1015)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.235 (IC base=+0.115)

- **PATRÓN** `volumen_regimen` < `0.8751` → IC=+0.129 (n=2671)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 0.8751 (IC base=+0.115)

- **PATRÓN** `volumen_spike_ratio` < `1.8225` → IC=+0.122 (n=2607)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` < 1.8225 (IC base=+0.115)

- **PATRÓN** `libro_liquidez` > `2714.6923` → IC=+0.239 (n=1335)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2714.6923 (IC base=+0.115)

- **PATRÓN** `sigma_h` < `0.0109` → IC=+0.156 (n=3305)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0109 (IC base=+0.130)

- **PATRÓN** `drift_60min` |x|≤ `0.1384` → IC=+0.155 (n=1254)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.1384 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.142 (n=3874)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 5.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` < `0.6667` → IC=+0.218 (n=3768)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6667 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.032` → IC=+0.152 (n=3633)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` < 3.032 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` < `0.6403` → IC=+0.151 (n=1254)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.6403 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` > `0.2292` → IC=+0.190 (n=659)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.2292 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` < `1.4358` → IC=+0.161 (n=1190)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 1.4358 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `2605.25` → IC=+0.212 (n=1252)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2605.25 (IC base=+0.130)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.144 (n=3177)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 42.0 (IC base=+0.130)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0137` → IC=+0.261 (n=3270)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0137 (IC base=+0.239)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.245 (n=3832)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.239)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.242 (n=3277)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.239)

- **PATRÓN** `ibs_20min` > `0.6145` → IC=+0.272 (n=3271)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6145 (IC base=+0.239)

- **PATRÓN** `dist_vwap_pct` > `0.1944` → IC=+0.253 (n=1857)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1944 (IC base=+0.239)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.143` → IC=+0.287 (n=641)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.143 (IC base=+0.239)

- **PATRÓN** `volumen_regimen` < `1.2171` → IC=+0.240 (n=3661)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2171 (IC base=+0.239)

- **PATRÓN** `volumen_regimen` > `0.6437` → IC=+0.244 (n=3660)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6437 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` > `0.2393` → IC=+0.252 (n=635)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2393 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` > `2.4984` → IC=+0.258 (n=1194)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4984 (IC base=+0.239)

- **PATRÓN** `libro_liquidez` > `2870.0504` → IC=+0.245 (n=1660)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2870.0504 (IC base=+0.239)

- **PATRÓN** `sigma_h` > `0.0257` → IC=+0.268 (n=1263)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0257 (IC base=+0.244)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.247 (n=3574)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.244)

- **PATRÓN** `ibs_20min` < `0.1398` → IC=+0.307 (n=1667)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1398 (IC base=+0.244)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.066` → IC=+0.277 (n=725)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.066 (IC base=+0.244)

- **PATRÓN** `volumen_regimen` < `0.7157` → IC=+0.246 (n=1666)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7157 (IC base=+0.244)

- **PATRÓN** `volumen_regimen` > `1.214` → IC=+0.263 (n=1262)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.214 (IC base=+0.244)

- **PATRÓN** `volumen_pendiente_norm` > `0.2857` → IC=+0.306 (n=524)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2857 (IC base=+0.244)

- **PATRÓN** `volumen_spike_ratio` > `1.4335` → IC=+0.248 (n=3576)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4335 (IC base=+0.244)

- **PATRÓN** `libro_liquidez` > `2973.1865` → IC=+0.248 (n=1262)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2973.1865 (IC base=+0.244)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.202 (n=5985)

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.245 (n=2196)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.222)

- **PATRÓN** `drift_60min` |x|≤ `0.5139` → IC=+0.231 (n=6574)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5139 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.230 (n=5977)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` > `0.9283` → IC=+0.257 (n=2191)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9283 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.479` → IC=+0.227 (n=2180)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.479 (IC base=+0.222)

- **PATRÓN** `volumen_regimen` < `0.7051` → IC=+0.231 (n=2101)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7051 (IC base=+0.222)

- **PATRÓN** `volumen_regimen` > `0.8786` → IC=+0.223 (n=3182)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8786 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` < `0.105` → IC=+0.223 (n=6146)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.105 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` > `0.1652` → IC=+0.228 (n=1849)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1652 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` < `2.2556` → IC=+0.227 (n=5694)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.2556 (IC base=+0.222)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.226 (n=4861)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.222)

- **PATRÓN** `libro_liquidez` > `2584.9429` → IC=+0.226 (n=6573)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2584.9429 (IC base=+0.222)

- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.239 (n=1502)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.201)

- **PATRÓN** `drift_60min` |x|≤ `0.4985` → IC=+0.212 (n=4501)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4985 (IC base=+0.201)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.213 (n=1502)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.201)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.212 (n=1984)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.201)

- **PATRÓN** `ibs_20min` < `0.087` → IC=+0.215 (n=1501)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.087 (IC base=+0.201)

- **PATRÓN** `dist_vwap_pct` > `0.6674` → IC=+0.212 (n=754)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6674 (IC base=+0.201)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.762` → IC=+0.213 (n=4055)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.762 (IC base=+0.201)

- **PATRÓN** `volumen_regimen` < `1.0959` → IC=+0.207 (n=3782)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0959 (IC base=+0.201)

- **PATRÓN** `volumen_pendiente_norm` < `0.0978` → IC=+0.202 (n=4146)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0978 (IC base=+0.201)

- **PATRÓN** `volumen_pendiente_norm` > `0.0733` → IC=+0.205 (n=2008)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0733 (IC base=+0.201)

- **PATRÓN** `volumen_spike_ratio` < `1.5321` → IC=+0.206 (n=1952)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5321 (IC base=+0.201)

- **PATRÓN** `volumen_spike_ratio` > `2.1885` → IC=+0.210 (n=2012)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1885 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.202 (n=5985)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.201)

- **PATRÓN** `ballena_activa_n` < `31.0` → IC=+0.224 (n=1956)

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
- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.238 (n=487)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0084 (IC base=+0.210)

- **PATRÓN** `sigma_h` > `0.0131` → IC=+0.210 (n=371)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0131 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `10.0` → IC=+0.245 (n=775)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.287 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.210)

- **PATRÓN** `dist_vwap_pct` > `0.7953` → IC=+0.233 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7953 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.193` → IC=+0.239 (n=603)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.193 (IC base=+0.210)

- **PATRÓN** `volumen_regimen` < `0.6428` → IC=+0.249 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6428 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` < `0.1062` → IC=+0.217 (n=1003)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1062 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.0792` → IC=+0.215 (n=483)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0792 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` < `2.1535` → IC=+0.223 (n=946)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1535 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `1.4705` → IC=+0.213 (n=1075)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4705 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.218 (n=1298)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `4344.6372` → IC=+0.255 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4344.6372 (IC base=+0.210)

- **PATRÓN** `sigma_h` < `0.0132` → IC=+0.228 (n=763)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0132 (IC base=+0.227)

- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.243 (n=508)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0101 (IC base=+0.227)

- **PATRÓN** `drift_60min` |x|≤ `0.6154` → IC=+0.244 (n=763)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6154 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.231 (n=718)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.227)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.249 (n=519)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.227)

- **PATRÓN** `ibs_20min` < `0.7321` → IC=+0.254 (n=763)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7321 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.825` → IC=+0.244 (n=712)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.825 (IC base=+0.227)

- **PATRÓN** `volumen_regimen` < `0.7551` → IC=+0.228 (n=336)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7551 (IC base=+0.227)

- **PATRÓN** `volumen_regimen` > `1.2794` → IC=+0.234 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2794 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` < `0.0838` → IC=+0.237 (n=644)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0838 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` > `2.2105` → IC=+0.261 (n=337)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2105 (IC base=+0.227)

- **PATRÓN** `libro_liquidez` > `3826.995` → IC=+0.247 (n=508)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3826.995 (IC base=+0.227)

- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.263 (n=520)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 25.0 (IC base=+0.227)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.148 (n=763)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0038 (IC base=+0.053)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.183 (n=1462)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.75 (IC base=+0.053)

- **PATRÓN** `dist_vwap_pct` > `0.1459` → IC=+0.141 (n=1065)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.1459 (IC base=+0.053)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.347` → IC=+0.141 (n=488)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 10.347 (IC base=+0.053)

- **PATRÓN** `ibs_20min` < `0.0656` → IC=+0.263 (n=678)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0656 (IC base=+0.051)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.126 (n=635)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.63€ cuando `sigma_h` < 0.0053 (IC base=+0.070)

- **PATRÓN** `ibs_20min` > `0.5427` → IC=+0.162 (n=617)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` > 0.5427 (IC base=+0.070)

- **PATRÓN** `dist_vwap_pct` > `0.1227` → IC=+0.168 (n=323)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.1227 (IC base=+0.070)

- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.130 (n=276)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.65€ cuando `sigma_h` < 0.0035 (IC base=+0.044)

- **PATRÓN** `ibs_20min` < `0.0674` → IC=+0.260 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0674 (IC base=+0.044)

- **PATRÓN** `volumen_pendiente_norm` > `0.2172` → IC=+0.142 (n=121)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` > 0.2172 (IC base=+0.044)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` > `0.6693` → IC=-0.148 (n=163)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6693
  - _Potencial_: sin este filtro IC_bueno=+0.110 (n=490)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.151 (n=325)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0042 (IC base=+0.069)

- **PATRÓN** `ibs_20min` > `0.9375` → IC=+0.258 (n=320)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9375 (IC base=+0.069)

- **PATRÓN** `dist_vwap_pct` > `0.129` → IC=+0.169 (n=339)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.129 (IC base=+0.069)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.623` → IC=+0.201 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.623 (IC base=+0.069)

- **PATRÓN** `ibs_20min` < `0.1087` → IC=+0.257 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1087 (IC base=+0.029)

### GBM_LATE_60M#SOL#60min
- **PATRÓN** `ibs_20min` > `0.981` → IC=+0.188 (n=264)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.981 (IC base=+0.024)

- **PATRÓN** `dist_vwap_pct` > `0.4664` → IC=+0.127 (n=261)

  - _Acción_: Kelly boost +0.64€ cuando `dist_vwap_pct` > 0.4664 (IC base=+0.024)

- **PATRÓN** `sigma_h` < `0.0097` → IC=+0.188 (n=322)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0097 (IC base=+0.084)

- **PATRÓN** `ibs_20min` < `0.4857` → IC=+0.183 (n=449)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.4857 (IC base=+0.084)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.841` → IC=+0.292 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.841 (IC base=+0.084)

- **PATRÓN** `volumen_regimen` > `1.1079` → IC=+0.184 (n=150)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` > 1.1079 (IC base=+0.084)

- **PATRÓN** `volumen_pendiente_norm` > `0.2808` → IC=+0.189 (n=59)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.2808 (IC base=+0.084)

- **PATRÓN** `volumen_spike_ratio` > `1.8727` → IC=+0.132 (n=278)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 1.8727 (IC base=+0.084)

### GBM_LATE_60M_FADE
- **FILTRO** `sigma_h` < `0.0059` → IC=-0.246 (n=191)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0059
  - _Potencial_: sin este filtro IC_bueno=-0.201 (n=192)

- **FILTRO** `dist_vwap_pct` > `0.2381` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2381
  - _Potencial_: sin este filtro IC_bueno=-0.219 (n=368)

- **FILTRO** `volumen_regimen` < `0.8572` → IC=-0.305 (n=126)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.8572
  - _Potencial_: sin este filtro IC_bueno=-0.183 (n=257)

- **FILTRO** `libro_liquidez` < `903.3651` → IC=-0.232 (n=95)

  - _Acción_: SKIP cuando `libro_liquidez` < 903.3651
  - _Potencial_: sin este filtro IC_bueno=-0.221 (n=288)

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
- **FILTRO** `hora_utc` > `5.0` → IC=-0.344 (n=43)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.191 (n=95)

- **FILTRO** `dist_vwap_pct` > `0.0767` → IC=-0.242 (n=29)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.0767
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=109)

- **FILTRO** `libro_spread` > `0.06` → IC=-0.250 (n=30)

  - _Acción_: SKIP cuando `libro_spread` > 0.06
  - _Potencial_: sin este filtro IC_bueno=-0.236 (n=108)

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
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0087 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.189 (n=332)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 16.0 (IC base=+0.143)

- **PATRÓN** `ibs_20min` > `0.6732` → IC=+0.182 (n=731)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` > 0.6732 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` > `0.8076` → IC=+0.282 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8076 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.614` → IC=+0.158 (n=398)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 3.614 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` < `0.6244` → IC=+0.179 (n=244)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` < 0.6244 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` > `1.2135` → IC=+0.146 (n=244)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 1.2135 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` < `0.0702` → IC=+0.176 (n=547)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` < 0.0702 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` < `1.3986` → IC=+0.200 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3986 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.429` → IC=+0.158 (n=200)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 10.429 (IC base=+0.033)

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

- **PATRÓN** `ibs_20min` < `0.2374` → IC=+0.150 (n=412)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.2374 (IC base=+0.090)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.162` → IC=+0.129 (n=95)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` > 11.162 (IC base=+0.090)

- **PATRÓN** `volumen_pendiente_norm` > `0.2735` → IC=+0.153 (n=70)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` > 0.2735 (IC base=+0.090)

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
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=129)

- **FILTRO** `dist_vwap_pct` > `0.1813` → IC=-0.167 (n=37)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1813
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=158)

- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.294 (n=124)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0101 (IC base=+0.253)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.294 (n=192)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.253)

- **PATRÓN** `ibs_20min` > `0.6786` → IC=+0.288 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6786 (IC base=+0.253)

- **PATRÓN** `dist_vwap_pct` > `0.6947` → IC=+0.396 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6947 (IC base=+0.253)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.832` → IC=+0.359 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.832 (IC base=+0.253)

- **PATRÓN** `volumen_regimen` < `0.6071` → IC=+0.296 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6071 (IC base=+0.253)

- **PATRÓN** `volumen_pendiente_norm` > `0.0973` → IC=+0.327 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0973 (IC base=+0.253)

- **PATRÓN** `volumen_spike_ratio` < `1.3961` → IC=+0.338 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3961 (IC base=+0.253)

- **PATRÓN** `volumen_spike_ratio` > `2.3472` → IC=+0.311 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3472 (IC base=+0.253)

### LATE_WINDOW_5MIN
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.333 (n=118)

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

- **PATRÓN** `drift_ventana_pct` |x|> `0.3488` → IC=+0.306 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3488 (IC base=+0.274)

- **PATRÓN** `elapsed_s` > `229.9` → IC=+0.333 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 229.9 (IC base=+0.274)

- **PATRÓN** `drift_15min` |x|≤ `2.3044` → IC=+0.315 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3044 (IC base=+0.274)

- **PATRÓN** `drift_60min` |x|≤ `0.6421` → IC=+0.314 (n=68)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6421 (IC base=+0.274)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.333 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.274)

- **PATRÓN** `ballena_activa_n` < `1750.0` → IC=+0.317 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1750.0 (IC base=+0.274)

### LATE_WINDOW_5MIN#BTC#5min
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.333 (n=118)

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

- **PATRÓN** `drift_ventana_pct` |x|> `0.3488` → IC=+0.306 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3488 (IC base=+0.274)

- **PATRÓN** `elapsed_s` > `229.9` → IC=+0.333 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 229.9 (IC base=+0.274)

- **PATRÓN** `drift_15min` |x|≤ `2.3044` → IC=+0.315 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3044 (IC base=+0.274)

- **PATRÓN** `drift_60min` |x|≤ `0.6421` → IC=+0.314 (n=68)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6421 (IC base=+0.274)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.333 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.274)

- **PATRÓN** `ballena_activa_n` < `1750.0` → IC=+0.317 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1750.0 (IC base=+0.274)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.124 (n=1467)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` > 0.5 (IC base=+0.098)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.124 (n=1467)

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
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=939)

### LIQUIDACIONES_15M#BNB#15min
- **PATRÓN** `liq_usd_total` > `2224.14` → IC=+0.260 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `liq_usd_total` > 2224.14 (IC base=+0.054)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `libro_liquidez` < `12324.2702` → IC=-0.152 (n=44)

  - _Acción_: SKIP cuando `libro_liquidez` < 12324.2702
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=91)

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
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=3958)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=159)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=116)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.278 (n=34)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=146)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.198 (n=51)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 21.0 (IC base=-0.060)

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
- **PATRÓN** `liq_n` > `3.0` → IC=+0.370 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `liq_n` > 3.0 (IC base=+0.214)

- **PATRÓN** `liq_usd_total` > `2129.85` → IC=+0.348 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `liq_usd_total` > 2129.85 (IC base=+0.214)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.265 (n=32)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.214)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.208 (n=46)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 13.0 (IC base=+0.214)

- **PATRÓN** `libro_liquidez` > `2858.428` → IC=+0.283 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2858.428 (IC base=+0.214)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=1611)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=1565)

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
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=450)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=431)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.145 (n=195)

  - _Acción_: Kelly boost +0.72€ cuando `py_entrada` < 0.495 (IC base=+0.024)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=1024)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=1024)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=1309)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=1309)

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
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=359)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=408)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=305)

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
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=375)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.187 (n=81)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=103)

- **FILTRO** `hora_utc` > `14.0` → IC=-0.159 (n=83)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=101)

- **FILTRO** `py_entrada` > `0.52` → IC=-0.121 (n=56)

  - _Acción_: SKIP cuando `py_entrada` > 0.52
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=30)

- **FILTRO** `hora_utc` < `17.0` → IC=-0.131 (n=63)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=23)

### LIQUIDACIONES_DEPTH_FASE0#BTC#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.132 (n=302)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=764)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **FILTRO** `py_entrada` > `0.57` → IC=-0.128 (n=436)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.085 (n=523)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.144 (n=318)

  - _Acción_: Kelly boost +0.72€ cuando `py_entrada` < 0.5 (IC base=-0.012)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` > `0.57` → IC=-0.121 (n=373)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.074 (n=383)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` > `0.58` → IC=-0.129 (n=351)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=418)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.137 (n=276)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=604)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.44` → IC=-0.136 (n=534)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=535)

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
- **FILTRO** `py_entrada` < `0.46` → IC=-0.175 (n=8091)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=25772)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.173 (n=8572)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=26433)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.190 (n=1571)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=4713)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.147 (n=2089)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.094 (n=4115)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.135 (n=1618)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` > 1.0 (IC base=+0.040)

- **PATRÓN** `py_entrada` < `0.505` → IC=+0.127 (n=3150)

  - _Acción_: Kelly boost +0.64€ cuando `py_entrada` < 0.505 (IC base=+0.013)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` < `0.44` → IC=-0.172 (n=1124)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=3560)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.179 (n=1209)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=3714)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` > `0.62` → IC=-0.199 (n=1558)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.087 (n=4803)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.136 (n=1933)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` > 1.0 (IC base=+0.034)

- **PATRÓN** `libro_liquidez` > `1736.72` → IC=+0.121 (n=2132)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 1736.72 (IC base=+0.034)

### MOMENTUM_IBS_15M_BALLENA#ETH#15min
- **FILTRO** `py_entrada` > `0.575` → IC=-0.177 (n=1238)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=3759)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.485` → IC=-0.161 (n=1563)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=4747)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=2444)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.162 (n=772)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=2368)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.180 (n=973)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=3092)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=4044)

- **FILTRO** `ballena_activa_n` > `32.0` → IC=-0.127 (n=1366)

  - _Acción_: SKIP cuando `ballena_activa_n` > 32.0
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=2666)

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
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=1086)

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
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=801)

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
  - _Potencial_: sin este filtro IC_bueno=-0.091 (n=52011)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.299 (n=18058)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=56930)

- **FILTRO** `ibs_7min` < `0.215` → IC=-0.235 (n=18746)

  - _Acción_: SKIP cuando `ibs_7min` < 0.215
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=56242)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.153 (n=25405)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=49583)

- **FILTRO** `py_entrada` > `0.68` → IC=-0.252 (n=21900)

  - _Acción_: SKIP cuando `py_entrada` > 0.68
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=71824)

- **FILTRO** `ibs_7min` > `0.2819` → IC=-0.184 (n=23430)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2819
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=70294)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.158 (n=3226)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=10155)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.318 (n=3315)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=10066)

- **FILTRO** `ibs_7min` < `0.7097` → IC=-0.254 (n=4411)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7097
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=8970)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.153 (n=2797)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=10584)

- **FILTRO** `py_entrada` > `0.72` → IC=-0.278 (n=3957)

  - _Acción_: SKIP cuando `py_entrada` > 0.72
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=12218)

- **FILTRO** `ibs_7min` > `0.777` → IC=-0.211 (n=4042)

  - _Acción_: SKIP cuando `ibs_7min` > 0.777
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=12133)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.264 (n=3011)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=9451)

- **FILTRO** `ibs_7min` < `0.7136` → IC=-0.211 (n=3115)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7136
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=9347)

- **FILTRO** `ballena_activa_n` > `156.0` → IC=-0.202 (n=3107)

  - _Acción_: SKIP cuando `ballena_activa_n` > 156.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=9355)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.267 (n=2917)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9813)

- **FILTRO** `ibs_7min` > `0.266` → IC=-0.192 (n=3182)

  - _Acción_: SKIP cuando `ibs_7min` > 0.266
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=9548)

- **FILTRO** `ballena_activa_n` > `153.0` → IC=-0.181 (n=3164)

  - _Acción_: SKIP cuando `ballena_activa_n` > 153.0
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=9566)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.166 (n=3081)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=9751)

- **FILTRO** `py_entrada` < `0.3` → IC=-0.325 (n=3063)

  - _Acción_: SKIP cuando `py_entrada` < 0.3
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=9769)

- **FILTRO** `ibs_7min` < `0.2857` → IC=-0.251 (n=4222)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2857
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=8610)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.202 (n=2529)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=10303)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.260 (n=4151)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=12998)

- **FILTRO** `ibs_7min` > `0.7297` → IC=-0.183 (n=4286)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7297
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=12863)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.264 (n=3012)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=9105)

- **FILTRO** `ibs_7min` < `0.7139` → IC=-0.198 (n=3029)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7139
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=9088)

- **FILTRO** `ballena_activa_n` > `25.0` → IC=-0.193 (n=2929)

  - _Acción_: SKIP cuando `ballena_activa_n` > 25.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=9188)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.260 (n=2938)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=9686)

- **FILTRO** `ibs_7min` > `0.2731` → IC=-0.178 (n=3155)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2731
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=9469)

- **FILTRO** `ballena_activa_n` > `24.0` → IC=-0.173 (n=3051)

  - _Acción_: SKIP cuando `ballena_activa_n` > 24.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=9573)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.32` → IC=-0.301 (n=2867)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=9137)

- **FILTRO** `ibs_7min` < `0.7` → IC=-0.236 (n=3913)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=8091)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.219 (n=2940)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=9064)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.199 (n=4400)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=13723)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.133 (n=3921)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.108 (n=8271)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.310 (n=2922)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=9270)

- **FILTRO** `ibs_7min` < `0.7333` → IC=-0.221 (n=4015)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7333
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=8177)

- **FILTRO** `ballena_activa_n` > `9.0` → IC=-0.206 (n=2699)

  - _Acción_: SKIP cuando `ballena_activa_n` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.091 (n=9493)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.227 (n=4227)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=12696)

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
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=628)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=1458)

- **FILTRO** `py_entrada` > `0.565` → IC=-0.172 (n=260)

  - _Acción_: SKIP cuando `py_entrada` > 0.565
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=905)

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
- **PATRÓN** `delta_ratio` |x|> `0.4308` → IC=+0.147 (n=695)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.74€ cuando `delta_ratio` |x|> 0.4308 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.128 (n=1377)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 14.0 (IC base=+0.124)

- **PATRÓN** `total_vol_5m` < `421.686` → IC=+0.160 (n=510)

  - _Acción_: Kelly boost +0.80€ cuando `total_vol_5m` < 421.686 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `3557.272` → IC=+0.137 (n=694)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 3557.272 (IC base=+0.124)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `14.0` → IC=+0.181 (n=183)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 14.0 (IC base=+0.133)

- **PATRÓN** `total_vol_5m` < `287.685` → IC=+0.164 (n=242)

  - _Acción_: Kelly boost +0.82€ cuando `total_vol_5m` < 287.685 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `2507.387` → IC=+0.240 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2507.387 (IC base=+0.133)

- **PATRÓN** `ballena_activa_n` < `6.0` → IC=+0.135 (n=176)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 6.0 (IC base=+0.133)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `delta_ratio` |x|> `0.4378` → IC=+0.151 (n=107)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.76€ cuando `delta_ratio` |x|> 0.4378 (IC base=+0.118)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.137 (n=293)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 15.0 (IC base=+0.118)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.123 (n=380)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.04 (IC base=+0.118)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4165` → IC=+0.170 (n=192)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.85€ cuando `delta_ratio` |x|> 0.4165 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.147 (n=267)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.124)

- **PATRÓN** `total_vol_5m` < `857.788` → IC=+0.149 (n=289)

  - _Acción_: Kelly boost +0.75€ cuando `total_vol_5m` < 857.788 (IC base=+0.124)

- **PATRÓN** `ballena_activa_n` < `59.0` → IC=+0.167 (n=97)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 59.0 (IC base=+0.124)

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
- **PATRÓN** `hora_utc` < `14.0` → IC=+0.131 (n=280)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 14.0 (IC base=+0.101)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.134 (n=203)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.101)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `4.8182` → IC=-0.203 (n=116)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.8182
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=118)

- **FILTRO** `pct_vs_K` |x|> `3.395` → IC=-0.182 (n=297)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.395
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=581)

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.147 (n=290)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0045 (IC base=-0.057)

### PRICE_TARGET_GBM#ETH#atexpiry
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.291 (n=89)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=-0.011)

- **PATRÓN** `pct_vs_K` |x|≤ `1.7678` → IC=+0.192 (n=89)

  - _Acción_: Kelly boost +0.96€ cuando `pct_vs_K` |x|≤ 1.7678 (IC base=-0.011)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `pct_vs_K` |x|> `6.6759` → IC=-0.267 (n=28)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 6.6759
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=56)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `T_h` < `93.7142` → IC=-0.163 (n=84)

  - _Acción_: SKIP cuando `T_h` < 93.7142
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=85)

### PRICE_TARGET_GBM#SOL#reach
- **FILTRO** `T_h` < `146.0708` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `T_h` < 146.0708
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=16)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0114` → IC=-0.236 (n=597)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0114
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=200)

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

- **FILTRO** `pct_vs_K` |x|> `2.5079` → IC=-0.352 (n=86)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.5079
  - _Potencial_: sin este filtro IC_bueno=-0.108 (n=169)

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

- **FILTRO** `T_h` < `69.3311` → IC=-0.289 (n=74)

  - _Acción_: SKIP cuando `T_h` < 69.3311
  - _Potencial_: sin este filtro IC_bueno=-0.274 (n=153)

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

- **FILTRO** `T_h` < `111.9918` → IC=-0.215 (n=114)

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
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=1076)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=1347)

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
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=5030)

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
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=2901)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.188 (n=1833)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0054 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.2215` → IC=+0.158 (n=5497)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.2215 (IC base=+0.139)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1346` → IC=+0.154 (n=2266)

  - _Acción_: Kelly boost +0.77€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1346 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.149 (n=5079)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 6.0 (IC base=+0.139)

- **PATRÓN** `ibs_15` > `0.5769` → IC=+0.222 (n=4911)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5769 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.1354` → IC=+0.131 (n=2558)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` > 0.1354 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.315` → IC=+0.244 (n=1040)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.315 (IC base=+0.139)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=3122)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `4523.4196` → IC=+0.168 (n=1833)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 4523.4196 (IC base=+0.139)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=2116)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.221 (n=802)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0057 (IC base=+0.201)

- **PATRÓN** `drift_60min` |x|≤ `0.0773` → IC=+0.249 (n=353)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0773 (IC base=+0.201)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2676` → IC=+0.221 (n=267)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2676 (IC base=+0.201)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.228 (n=736)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.201)

- **PATRÓN** `ibs_15` > `0.7077` → IC=+0.272 (n=802)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7077 (IC base=+0.201)

- **PATRÓN** `dist_vwap_pct` > `0.3743` → IC=+0.226 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3743 (IC base=+0.201)

- **PATRÓN** `dist_vwap_pct` < `0.1096` → IC=+0.203 (n=540)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1096 (IC base=+0.201)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.41` → IC=+0.313 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.41 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.204 (n=1039)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.201)

- **PATRÓN** `libro_liquidez` > `11859.2402` → IC=+0.221 (n=535)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11859.2402 (IC base=+0.201)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.146 (n=1007)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0071 (IC base=+0.132)

- **PATRÓN** `drift_60min` |x|≤ `0.1103` → IC=+0.150 (n=672)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.1103 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.136 (n=922)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 6.0 (IC base=+0.132)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.133 (n=1008)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 16.0 (IC base=+0.132)

- **PATRÓN** `ibs_15` > `0.4934` → IC=+0.218 (n=1007)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.4934 (IC base=+0.132)

- **PATRÓN** `dist_vwap_pct` > `0.1194` → IC=+0.151 (n=625)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.1194 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.945` → IC=+0.282 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.945 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `6017.9372` → IC=+0.171 (n=457)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 6017.9372 (IC base=+0.132)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `ibs_15` > `0.7647` → IC=+0.132 (n=710)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.66€ cuando `ibs_15` > 0.7647 (IC base=+0.051)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` < `0.0253` → IC=+0.165 (n=1378)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0253 (IC base=+0.152)

- **PATRÓN** `sigma_h` > `0.0128` → IC=+0.157 (n=1378)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0128 (IC base=+0.152)

- **PATRÓN** `drift_60min` |x|≤ `0.2255` → IC=+0.177 (n=1380)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.2255 (IC base=+0.152)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0978` → IC=+0.219 (n=425)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0978 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.160 (n=1265)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 6.0 (IC base=+0.152)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.156 (n=1216)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 14.0 (IC base=+0.152)

- **PATRÓN** `ibs_15` > `0.5417` → IC=+0.224 (n=1233)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5417 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` > `0.5407` → IC=+0.186 (n=313)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.5407 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.913` → IC=+0.193 (n=311)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 17.913 (IC base=+0.152)

- **PATRÓN** `libro_liquidez` > `2947.2049` → IC=+0.200 (n=625)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2947.2049 (IC base=+0.152)

- **PATRÓN** `ibs_15` < `0.1111` → IC=+0.151 (n=1065)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.76€ cuando `ibs_15` < 0.1111 (IC base=+0.067)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` > `0.0054` → IC=+0.396 (n=343)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0054 (IC base=+0.364)

- **PATRÓN** `drift_60min` |x|≤ `0.1117` → IC=+0.366 (n=505)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1117 (IC base=+0.364)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1503` → IC=+0.379 (n=504)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1503 (IC base=+0.364)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1356` → IC=+0.382 (n=295)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1356 (IC base=+0.364)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.372 (n=798)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.364)

- **PATRÓN** `ibs_15` > `0.7904` → IC=+0.393 (n=756)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7904 (IC base=+0.364)

- **PATRÓN** `dist_vwap_pct` > `0.1534` → IC=+0.380 (n=448)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1534 (IC base=+0.364)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.976` → IC=+0.396 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.976 (IC base=+0.364)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.368 (n=922)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.364)

- **PATRÓN** `libro_liquidez` > `9641.0136` → IC=+0.381 (n=343)

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

- **PATRÓN** `delta_ratio_macro` |x|> `0.1294` → IC=+0.381 (n=259)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1294 (IC base=+0.365)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2969` → IC=+0.375 (n=318)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2969 (IC base=+0.365)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.370 (n=389)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.365)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.374 (n=181)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.365)

- **PATRÓN** `ibs_15` > `0.764` → IC=+0.392 (n=388)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.764 (IC base=+0.365)

- **PATRÓN** `dist_vwap_pct` > `0.159` → IC=+0.373 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.159 (IC base=+0.365)

- **PATRÓN** `dist_vwap_pct` < `0.2796` → IC=+0.366 (n=356)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2796 (IC base=+0.365)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.973` → IC=+0.394 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.973 (IC base=+0.365)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.369 (n=441)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.365)

- **PATRÓN** `libro_liquidez` > `4150.4977` → IC=+0.376 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4150.4977 (IC base=+0.365)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0075` → IC=-0.199 (n=2744)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0075
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=2745)

- **FILTRO** `drift_15min` |x|> `0.913` → IC=-0.150 (n=1371)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.913
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=4117)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.220 (n=2316)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=3173)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1411` → IC=+0.213 (n=472)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1411 (IC base=-0.083)

- **PATRÓN** `ibs_15` > `0.6296` → IC=+0.276 (n=1245)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6296 (IC base=-0.083)

- **PATRÓN** `dist_vwap_pct` > `0.1103` → IC=+0.200 (n=728)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1103 (IC base=-0.083)

- **PATRÓN** `dist_vwap_pct` < `0.2595` → IC=+0.197 (n=1067)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` < 0.2595 (IC base=-0.083)

- **PATRÓN** `delta_ratio_macro` |x|> `0.234` → IC=+0.270 (n=1682)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.234 (IC base=-0.004)

- **PATRÓN** `ibs_15` < `0.3703` → IC=+0.286 (n=5043)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3703 (IC base=-0.004)

- **PATRÓN** `dist_vwap_pct` > `0.656` → IC=+0.281 (n=695)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.656 (IC base=-0.004)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0322` → IC=-0.221 (n=2621)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0322
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=877)

- **FILTRO** `sigma_h` < `0.0038` → IC=-0.216 (n=874)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0038
  - _Potencial_: sin este filtro IC_bueno=-0.175 (n=2624)

- **FILTRO** `sigma_ewma_delta_pct` > `22.22` → IC=-0.251 (n=495)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 22.22
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=3003)

- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.152 (n=334)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0031 (IC base=+0.070)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2673` → IC=+0.282 (n=145)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2673 (IC base=+0.070)

- **PATRÓN** `ibs_15` > `0.7609` → IC=+0.317 (n=435)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7609 (IC base=+0.070)

- **PATRÓN** `dist_vwap_pct` > `0.1039` → IC=+0.274 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1039 (IC base=+0.070)

- **PATRÓN** `dist_vwap_pct` < `0.2429` → IC=+0.276 (n=391)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2429 (IC base=+0.070)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.177` → IC=+0.147 (n=222)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 22.177 (IC base=+0.070)

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

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.254 (n=1302)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0061 (IC base=+0.243)

- **PATRÓN** `drift_60min` |x|≤ `0.3563` → IC=+0.248 (n=1718)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3563 (IC base=+0.243)

- **PATRÓN** `drift_15min` |x|≤ `0.782` → IC=+0.259 (n=1718)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.782 (IC base=+0.243)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2128` → IC=+0.264 (n=885)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2128 (IC base=+0.243)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.255 (n=719)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.243)

- **PATRÓN** `ibs_15` < `0.3844` → IC=+0.274 (n=1952)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3844 (IC base=+0.243)

- **PATRÓN** `dist_vwap_pct` > `0.3788` → IC=+0.272 (n=480)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3788 (IC base=+0.243)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.323` → IC=+0.248 (n=855)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.323 (IC base=+0.243)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.226` → IC=+0.248 (n=2043)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.226 (IC base=+0.243)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `sigma_h` > `0.0105` → IC=-0.239 (n=435)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0105
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=845)

- **FILTRO** `drift_60min` |x|> `0.1722` → IC=-0.268 (n=434)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1722
  - _Potencial_: sin este filtro IC_bueno=-0.169 (n=846)

- **FILTRO** `drift_15min` |x|> `0.912` → IC=-0.288 (n=319)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.912
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=961)

- **FILTRO** `sigma_ewma_delta_pct` > `16.935` → IC=-0.134 (n=676)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 16.935
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=5400)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1455` → IC=+0.188 (n=46)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.94€ cuando `delta_ratio_macro` |x|> 0.1455 (IC base=-0.203)

- **PATRÓN** `ibs_15` > `0.5625` → IC=+0.234 (n=62)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5625 (IC base=-0.203)

- **PATRÓN** `dist_vwap_pct` > `0.2752` → IC=+0.143 (n=26)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.2752 (IC base=-0.203)

- **PATRÓN** `dist_vwap_pct` < `0.1292` → IC=+0.154 (n=53)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.1292 (IC base=-0.203)

- **PATRÓN** `ibs_15` < `0.38` → IC=+0.297 (n=862)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.38 (IC base=-0.030)

- **PATRÓN** `dist_vwap_pct` > `0.6867` → IC=+0.243 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6867 (IC base=-0.030)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.1526` → IC=-0.245 (n=390)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1526
  - _Potencial_: sin este filtro IC_bueno=-0.210 (n=1173)

- **FILTRO** `drift_15min` |x|> `1.2555` → IC=-0.273 (n=390)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.2555
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=1173)

- **FILTRO** `sigma_ewma_delta_pct` > `7.465` → IC=-0.219 (n=478)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 7.465
  - _Potencial_: sin este filtro IC_bueno=-0.218 (n=1085)

- **FILTRO** `libro_spread` > `0.04` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.04
  - _Potencial_: sin este filtro IC_bueno=-0.218 (n=1544)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.219)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.219)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1695` → IC=+0.278 (n=547)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1695 (IC base=-0.015)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1182` → IC=+0.302 (n=524)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1182 (IC base=-0.015)

- **PATRÓN** `ibs_15` < `0.1364` → IC=+0.311 (n=803)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.1364 (IC base=-0.015)

- **PATRÓN** `dist_vwap_pct` > `0.7684` → IC=+0.331 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7684 (IC base=-0.015)

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
- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.300 (n=457)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0033 (IC base=+0.282)

- **PATRÓN** `drift_60min` |x|≤ `0.0719` → IC=+0.313 (n=603)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0719 (IC base=+0.282)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1522` → IC=+0.282 (n=913)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1522 (IC base=+0.282)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2224` → IC=+0.289 (n=836)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2224 (IC base=+0.282)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.294 (n=1417)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.282)

- **PATRÓN** `ibs_15` > `0.838` → IC=+0.310 (n=1371)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.838 (IC base=+0.282)

- **PATRÓN** `dist_vwap_pct` > `0.2627` → IC=+0.313 (n=592)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2627 (IC base=+0.282)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.944` → IC=+0.388 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.944 (IC base=+0.282)

- **PATRÓN** `libro_liquidez` > `13157.6607` → IC=+0.302 (n=457)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13157.6607 (IC base=+0.282)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.300 (n=318)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.275)

- **PATRÓN** `drift_60min` |x|≤ `0.058` → IC=+0.307 (n=241)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.058 (IC base=+0.275)

- **PATRÓN** `drift_15min` |x|≤ `0.3844` → IC=+0.275 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3844 (IC base=+0.275)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2694` → IC=+0.279 (n=242)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2694 (IC base=+0.275)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3931` → IC=+0.282 (n=649)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3931 (IC base=+0.275)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.293 (n=757)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.275)

- **PATRÓN** `ibs_15` > `0.829` → IC=+0.300 (n=723)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.829 (IC base=+0.275)

- **PATRÓN** `dist_vwap_pct` > `0.2516` → IC=+0.310 (n=309)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2516 (IC base=+0.275)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.806` → IC=+0.395 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.806 (IC base=+0.275)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.277 (n=934)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.275)

- **PATRÓN** `libro_liquidez` > `15763.4118` → IC=+0.311 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15763.4118 (IC base=+0.275)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.294 (n=648)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0069 (IC base=+0.288)

- **PATRÓN** `drift_60min` |x|≤ `0.0506` → IC=+0.321 (n=216)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0506 (IC base=+0.288)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1408` → IC=+0.288 (n=432)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1408 (IC base=+0.288)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1009` → IC=+0.314 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1009 (IC base=+0.288)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.299 (n=620)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.288)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.290 (n=459)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.288)

- **PATRÓN** `ibs_15` > `0.8475` → IC=+0.317 (n=648)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8475 (IC base=+0.288)

- **PATRÓN** `dist_vwap_pct` > `0.2773` → IC=+0.316 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2773 (IC base=+0.288)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.243` → IC=+0.373 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.243 (IC base=+0.288)

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

- **FILTRO** `sigma_h` < `0.0047` → IC=-0.326 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0047
  - _Potencial_: sin este filtro IC_bueno=-0.286 (n=12)

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

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5769 sube el IC de +0.139 a +0.222 en UPDOWN_GBM#15min (n=4911). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7077 sube el IC de +0.201 a +0.272 en UPDOWN_GBM#BTC#15min (n=802). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.4934 sube el IC de +0.132 a +0.218 en UPDOWN_GBM#ETH#15min (n=1007). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5417 sube el IC de +0.152 a +0.224 en UPDOWN_GBM#XRP#15min (n=1233). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1111 sube el IC de +0.067 a +0.151 en UPDOWN_GBM#XRP#15min (n=1065). Ya aplicado como kelly_boost=+0.76€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6296 sube el IC de -0.083 a +0.276 en UPDOWN_GBM_15M_TARDIO (n=1245). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3703 sube el IC de -0.004 a +0.286 en UPDOWN_GBM_15M_TARDIO (n=5043). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7609 sube el IC de +0.070 a +0.317 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=435). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.6255 sube el IC de -0.185 a +0.289 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=74). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.5679 sube el IC de +0.146 a +0.240 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=626). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3844 sube el IC de +0.243 a +0.274 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=1952). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de -0.203 a +0.234 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=62). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.38 sube el IC de -0.030 a +0.297 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=862). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.219 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.1364 sube el IC de -0.015 a +0.311 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=803). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_YES, IBS > 0.8434 sube el IC de +0.106 a +0.308 en UPDOWN_GBM_ETH_15M_HORA7 (n=24). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_YES, IBS > 0.8434 sube el IC de +0.106 a +0.308 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=24). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.838 sube el IC de +0.282 a +0.310 en UPDOWN_GBM_IBS_ALTO (n=1371). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.829 sube el IC de +0.275 a +0.300 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=723). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8475 sube el IC de +0.288 a +0.317 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=648). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7904 sube el IC de +0.364 a +0.393 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=756). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8078 sube el IC de +0.362 a +0.384 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=369). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.764 sube el IC de +0.365 a +0.392 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=388). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

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
| ✅ BALLENAS_TARDIAS | 47766 | -0.084 | -6143.22€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 2984 | +0.075 | -303.38€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 44782 | -0.095 | -5839.84€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4826 | -0.113 | -810.52€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4826 | -0.113 | -810.52€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 2984 | +0.075 | -303.38€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 2984 | +0.075 | -303.38€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 4877 | -0.106 | -938.87€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 4877 | -0.106 | -938.87€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 13139 | -0.044 | -1292.64€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 13139 | -0.044 | -1292.64€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 12989 | -0.112 | -1358.15€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 12989 | -0.112 | -1358.15€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 8951 | -0.130 | -1439.66€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 8951 | -0.130 | -1439.66€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 49893 | -0.012 | +2812.72€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 12900 | +0.004 | +1502.50€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 36993 | -0.018 | +1310.22€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 49893 | -0.012 | +2812.72€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 12900 | +0.004 | +1502.50€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 36993 | -0.018 | +1310.22€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 190602 | +0.113 | -7917.97€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#15min | 21927 | +0.180 | -711.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 876 | +0.011 | -72.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 156927 | +0.105 | -6728.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 10872 | +0.093 | -405.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 26004 | +0.103 | -1843.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 77 | -0.171 | +13.24€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 25912 | +0.104 | -1844.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 36068 | +0.124 | -599.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5615 | +0.178 | -239.26€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 25977 | +0.120 | -173.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 4434 | +0.080 | -163.71€ | 1 | 2 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 26055 | +0.098 | -1895.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 88 | -0.111 | +7.94€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 25952 | +0.099 | -1892.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 40718 | +0.123 | -874.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 10231 | +0.178 | -262.55€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 26389 | +0.106 | -539.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 4086 | +0.102 | -63.54€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#SOL | 35722 | +0.112 | -1591.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 5826 | +0.198 | -248.63€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 779 | +0.038 | -18.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 26765 | +0.096 | -1146.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 2352 | +0.102 | -178.05€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO#XRP | 26035 | +0.107 | -1113.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 90 | -0.109 | +17.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 25932 | +0.108 | -1131.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 30902 | +0.192 | -2167.21€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 30902 | +0.192 | -2167.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 6998 | +0.168 | -733.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 6998 | +0.168 | -733.84€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 4485 | +0.196 | -174.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 4485 | +0.196 | -174.81€ | 3 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 6861 | +0.175 | -603.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 6861 | +0.175 | -603.95€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 5735 | +0.250 | -207.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 5735 | +0.250 | -207.82€ | 0 | 4 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 6744 | +0.185 | -460.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 6744 | +0.185 | -460.54€ | 0 | 3 |
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
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 109324 | +0.199 | -8095.18€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 109324 | +0.199 | -8095.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 18911 | +0.178 | -2176.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 18911 | +0.178 | -2176.89€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 17624 | +0.224 | -593.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 17624 | +0.224 | -593.59€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 18766 | +0.179 | -2007.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 18766 | +0.179 | -2007.22€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 17773 | +0.218 | -706.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 17773 | +0.218 | -706.99€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 18058 | +0.203 | -1141.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 18058 | +0.203 | -1141.63€ | 1 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 18192 | +0.196 | -1468.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 18192 | +0.196 | -1468.85€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 42197 | +0.117 | +345.36€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 42197 | +0.117 | +345.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 21005 | +0.117 | +216.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 21005 | +0.117 | +216.07€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 21192 | +0.116 | +129.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 21192 | +0.116 | +129.29€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 2610 | +0.291 | -22.39€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 2610 | +0.291 | -22.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 1194 | +0.280 | -33.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 1194 | +0.280 | -33.70€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 1276 | +0.295 | +5.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 1276 | +0.295 | +5.54€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 140 | +0.345 | +5.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 140 | +0.345 | +5.77€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 1203 | +0.436 | -10.32€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 1203 | +0.436 | -10.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 576 | +0.432 | -10.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 576 | +0.432 | -10.41€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 576 | +0.439 | -1.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 576 | +0.439 | -1.16€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 51 | +0.406 | +1.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 51 | +0.406 | +1.25€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1951 | +0.067 | -87.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 725 | +0.046 | -64.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 1226 | +0.080 | -23.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1517 | +0.075 | -42.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 291 | +0.053 | -19.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 1226 | +0.080 | -23.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 85580 | +0.101 | -1997.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 6905 | +0.097 | +152.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 78675 | +0.101 | -2149.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 46769 | +0.106 | -438.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 6905 | +0.097 | +152.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 39864 | +0.107 | -591.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 18215 | +0.109 | -109.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 18215 | +0.109 | -109.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 20596 | +0.082 | -1448.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 20596 | +0.082 | -1448.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 914 | +0.186 | -109.27€ | 5 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 914 | +0.186 | -109.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 914 | +0.186 | -109.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 914 | +0.186 | -109.27€ | 5 | 4 |
| ✅ GBM_LATE_15M | 58085 | +0.100 | +32512.13€ | 0 | 18 |
| ✅ GBM_LATE_15M#15min | 58085 | +0.100 | +32512.13€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 9614 | +0.227 | +8338.25€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 9614 | +0.227 | +8338.25€ | 0 | 22 |
| ✅ GBM_LATE_15M#BTC | 8917 | +0.176 | +7045.31€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 8917 | +0.176 | +7045.31€ | 0 | 20 |
| ✅ GBM_LATE_15M#DOGE | 10411 | +0.208 | +8258.79€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 10411 | +0.208 | +8258.79€ | 0 | 21 |
| ✅ GBM_LATE_15M#ETH | 7767 | +0.057 | +2510.75€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 7767 | +0.057 | +2510.75€ | 1 | 16 |
| ✅ GBM_LATE_15M#SOL | 8104 | -0.030 | +2095.03€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 8104 | -0.030 | +2095.03€ | 4 | 13 |
| ✅ GBM_LATE_15M#XRP | 13272 | -0.022 | +4264.00€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 13272 | -0.022 | +4264.00€ | 3 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 61289 | +0.085 | +35575.57€ | 0 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 61289 | +0.085 | +35575.57€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 11843 | -0.003 | +6294.63€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 11843 | -0.003 | +6294.63€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 13188 | +0.004 | +3523.47€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 13188 | +0.004 | +3523.47€ | 0 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 8326 | +0.295 | +9529.22€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 8326 | +0.295 | +9529.22€ | 0 | 21 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 11699 | +0.014 | +3637.42€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 11699 | +0.014 | +3637.42€ | 1 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 9393 | +0.044 | +4204.98€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 9393 | +0.044 | +4204.98€ | 3 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 6840 | +0.316 | +8385.85€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 6840 | +0.316 | +8385.85€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 45914 | +0.179 | +37908.27€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 45914 | +0.179 | +37908.27€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 6913 | +0.241 | +6463.78€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 6913 | +0.241 | +6463.78€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 7265 | +0.139 | +5377.46€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 7265 | +0.139 | +5377.46€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 7394 | +0.225 | +6431.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 7394 | +0.225 | +6431.81€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 7867 | +0.129 | +6082.04€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 7867 | +0.129 | +6082.04€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 8698 | +0.119 | +6494.22€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 8698 | +0.119 | +6494.22€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 7777 | +0.233 | +7058.96€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 7777 | +0.233 | +7058.96€ | 0 | 25 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 12477 | +0.125 | +6259.80€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 12477 | +0.125 | +6259.80€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 582 | +0.166 | +396.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 582 | +0.166 | +396.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 3426 | +0.127 | +1868.79€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 3426 | +0.127 | +1868.79€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 506 | +0.158 | +277.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 506 | +0.158 | +277.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 3582 | +0.124 | +1720.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 3582 | +0.124 | +1720.44€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 3264 | +0.098 | +1297.42€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 3264 | +0.098 | +1297.42€ | 0 | 13 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 1117 | +0.168 | +699.59€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 1117 | +0.168 | +699.59€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO | 58268 | +0.188 | +48074.61€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#15min | 58268 | +0.188 | +48074.61€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 9189 | +0.251 | +8939.96€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 9189 | +0.251 | +8939.96€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 9274 | +0.138 | +6454.75€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 9274 | +0.138 | +6454.75€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 9886 | +0.236 | +8988.73€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 9886 | +0.236 | +8988.73€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 9646 | +0.142 | +7125.18€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 9646 | +0.142 | +7125.18€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 10345 | +0.122 | +7304.10€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 10345 | +0.122 | +7304.10€ | 0 | 18 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 9928 | +0.242 | +9261.88€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 9928 | +0.242 | +9261.88€ | 0 | 20 |
| ✅ GBM_LATE_5M | 14764 | +0.213 | +12146.07€ | 1 | 26 |
| ✅ GBM_LATE_5M#5min | 14764 | +0.213 | +12146.07€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 1217 | +0.251 | +1179.56€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 1217 | +0.251 | +1179.56€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 3267 | +0.211 | +2815.48€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 3267 | +0.211 | +2815.48€ | 0 | 27 |
| ✅ GBM_LATE_5M#DOGE | 1453 | +0.210 | +1160.11€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1453 | +0.210 | +1160.11€ | 0 | 19 |
| ✅ GBM_LATE_5M#ETH | 4325 | +0.205 | +3271.94€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 4325 | +0.205 | +3271.94€ | 0 | 24 |
| ✅ GBM_LATE_5M#SOL | 2489 | +0.217 | +2135.54€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 2489 | +0.217 | +2135.54€ | 0 | 26 |
| ✅ GBM_LATE_5M#XRP | 2013 | +0.209 | +1583.43€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 2013 | +0.209 | +1583.43€ | 0 | 0 |
| ✅ GBM_LATE_60M | 5192 | +0.052 | +1431.77€ | 0 | 5 |
| ✅ GBM_LATE_60M#60min | 5192 | +0.052 | +1431.77€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 1796 | +0.058 | +541.19€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 1796 | +0.058 | +541.19€ | 0 | 6 |
| ✅ GBM_LATE_60M#ETH | 1664 | +0.053 | +541.57€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 1664 | +0.053 | +541.57€ | 1 | 5 |
| ✅ GBM_LATE_60M#SOL | 1732 | +0.046 | +349.02€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 1732 | +0.046 | +349.02€ | 0 | 8 |
| 🚫 GBM_LATE_60M_FADE | 719 | -0.250 | -34.86€ | 8 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 719 | -0.250 | -34.86€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 260 | -0.252 | -19.02€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 260 | -0.252 | -19.02€ | 8 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 261 | -0.245 | -7.56€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 261 | -0.245 | -7.56€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 198 | -0.250 | -8.29€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 198 | -0.250 | -8.29€ | 7 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 2146 | +0.083 | +542.03€ | 0 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 2146 | +0.083 | +542.03€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 840 | +0.071 | +196.04€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 840 | +0.071 | +196.04€ | 1 | 6 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 749 | +0.058 | +145.65€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 749 | +0.058 | +145.65€ | 1 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 557 | +0.135 | +200.33€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 557 | +0.135 | +200.33€ | 2 | 9 |
| ✅ LATE_WINDOW_5MIN | 253 | +0.296 | +287.26€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 253 | +0.296 | +287.26€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 253 | +0.296 | +287.26€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 253 | +0.296 | +287.26€ | 1 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 4418 | +0.098 | +1012.11€ | 0 | 1 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 4418 | +0.098 | +1012.11€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 4418 | +0.098 | +1012.11€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 4418 | +0.098 | +1012.11€ | 0 | 1 |
| ✅ LIQUIDACIONES_15M | 1227 | +0.003 | +35.60€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 1227 | +0.003 | +35.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 91 | +0.048 | +9.10€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 91 | +0.048 | +9.10€ | 0 | 1 |
| ✅ LIQUIDACIONES_15M#BTC | 284 | -0.004 | +8.98€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 284 | -0.004 | +8.98€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 59 | -0.041 | -2.28€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 59 | -0.041 | -2.28€ | 1 | 1 |
| ✅ LIQUIDACIONES_15M#ETH | 309 | +0.021 | +19.37€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 309 | +0.021 | +19.37€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 323 | -0.017 | +0.36€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 323 | -0.017 | +0.36€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 161 | +0.009 | +0.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 161 | +0.009 | +0.07€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 4223 | +0.017 | +135.23€ | 4 | 1 |
| ✅ LIQUIDACIONES_5M#5min | 4223 | +0.017 | +135.23€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 224 | +0.013 | -3.49€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 224 | +0.013 | -3.49€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 827 | +0.015 | +40.58€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 827 | +0.015 | +40.58€ | 4 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 258 | +0.035 | +35.59€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 258 | +0.035 | +35.59€ | 0 | 5 |
| ✅ LIQUIDACIONES_5M#ETH | 1663 | +0.019 | +28.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1663 | +0.019 | +28.46€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 771 | +0.011 | +2.03€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 771 | +0.011 | +2.03€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 480 | +0.017 | +32.06€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 480 | +0.017 | +32.06€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 2428 | -0.033 | -6.24€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 2428 | -0.033 | -6.24€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 735 | -0.032 | -12.01€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 735 | -0.032 | -12.01€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 866 | -0.010 | +18.38€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 866 | -0.010 | +18.38€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 827 | -0.056 | -12.61€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 827 | -0.056 | -12.61€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 16051 | -0.031 | -121.63€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 7726 | -0.033 | -77.44€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 8325 | -0.029 | -44.20€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 556 | -0.056 | -34.43€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 286 | -0.035 | -3.47€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 270 | -0.077 | -30.97€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 4207 | -0.026 | -22.02€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 2004 | -0.024 | -0.01€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 2203 | -0.027 | -22.01€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 1545 | -0.028 | +17.96€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 789 | -0.034 | -3.39€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 756 | -0.021 | +21.35€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 3633 | -0.033 | -56.74€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 1726 | -0.032 | -25.04€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 1907 | -0.033 | -31.69€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 3084 | -0.021 | +56.50€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 1494 | -0.027 | +5.28€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 1590 | -0.014 | +51.22€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 3026 | -0.043 | -82.91€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 1427 | -0.049 | -50.80€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 1599 | -0.037 | -32.10€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 68868 | -0.000 | +3669.97€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 68868 | -0.000 | +3669.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 12488 | +0.027 | +1704.16€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 12488 | +0.027 | +1704.16€ | 2 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 9607 | -0.037 | -135.58€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 9607 | -0.037 | -135.58€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 12629 | +0.025 | +1406.82€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 12629 | +0.025 | +1406.82€ | 1 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 9559 | -0.053 | -251.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 9559 | -0.053 | -251.71€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 11746 | -0.004 | +326.67€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 11746 | -0.004 | +326.67€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 12839 | +0.018 | +619.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 12839 | +0.018 | +619.60€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 7206 | -0.054 | -117.09€ | 5 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 7206 | -0.054 | -117.09€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1256 | -0.002 | -14.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1256 | -0.002 | -14.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1994 | -0.063 | -23.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1994 | -0.063 | -23.84€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 85 | -0.029 | -1.13€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 85 | -0.029 | -1.13€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 809 | -0.120 | -35.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 809 | -0.120 | -35.98€ | 5 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 2199 | -0.068 | -14.12€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 2199 | -0.068 | -14.12€ | 2 | 0 |
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
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1391 | +0.007 | -0.19€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 195 | -0.013 | -1.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 195 | -0.013 | -1.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 168712 | -0.078 | +2045.27€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 168712 | -0.078 | +2045.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 29556 | -0.078 | +1715.23€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 29556 | -0.078 | +1715.23€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 25192 | -0.101 | -1258.11€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 25192 | -0.101 | -1258.11€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 29981 | -0.068 | +1428.62€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 29981 | -0.068 | +1428.62€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 24741 | -0.100 | -848.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 24741 | -0.100 | -848.37€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 30127 | -0.060 | +234.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 30127 | -0.060 | +234.02€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 29115 | -0.070 | +773.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 29115 | -0.070 | +773.87€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 9080 | -0.035 | -179.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 9080 | -0.035 | -179.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 1008 | -0.017 | -19.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 1008 | -0.017 | -19.32€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 2116 | -0.047 | -28.62€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 2116 | -0.047 | -28.62€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2656 | -0.025 | -36.18€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2656 | -0.025 | -36.18€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1273 | -0.064 | -31.74€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1273 | -0.064 | -31.74€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 1018 | -0.031 | -31.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 1018 | -0.031 | -31.49€ | 0 | 0 |
| ✅ ORDER_FLOW_5M | 2175 | +0.120 | +862.51€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#5min | 2039 | +0.124 | +849.92€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 483 | +0.133 | +233.49€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 483 | +0.133 | +233.49€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#DOGE | 417 | +0.118 | +146.26€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 417 | +0.118 | +146.26€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#ETH | 384 | +0.124 | +170.49€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 384 | +0.124 | +170.49€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 346 | +0.141 | +177.04€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 346 | +0.141 | +177.04€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#XRP | 409 | +0.101 | +122.63€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 409 | +0.101 | +122.63€ | 0 | 2 |
| ✅ ORDER_FLOW_5M_REACTIVO | 2230 | -0.014 | -6.53€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 2230 | -0.014 | -6.53€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 399 | +0.014 | +25.74€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 399 | +0.014 | +25.74€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 414 | -0.041 | -21.13€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 414 | -0.041 | -21.13€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 556 | -0.039 | -32.33€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 556 | -0.039 | -32.33€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 455 | +0.008 | +10.47€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 455 | +0.008 | +10.47€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 406 | -0.005 | +10.73€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 406 | -0.005 | +10.73€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 1179 | -0.061 | -6.37€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 543 | -0.098 | -62.02€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 422 | -0.108 | -41.48€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 121 | -0.061 | -20.55€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 413 | -0.021 | +37.89€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 298 | -0.003 | +45.89€ | 0 | 2 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 115 | -0.064 | -8.00€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 223 | -0.047 | +17.76€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 187 | -0.040 | +15.92€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 36 | -0.079 | +1.84€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 907 | -0.060 | +20.34€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 272 | -0.066 | -26.71€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 1490 | -0.203 | -86.77€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 587 | -0.200 | -45.33€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 517 | -0.198 | -40.88€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#reach | 70 | -0.208 | -4.45€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 498 | -0.208 | -38.65€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 436 | -0.219 | -45.80€ | 3 | 1 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 62 | -0.125 | +7.14€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL | 405 | -0.200 | -2.79€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 375 | -0.198 | -4.94€ | 5 | 0 |
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
| ✅ STREAK_FADE_5M | 3581 | -0.024 | -146.57€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3581 | -0.024 | -146.57€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 1127 | -0.023 | -40.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 1127 | -0.023 | -40.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 616 | -0.031 | -28.72€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 616 | -0.031 | -28.72€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 171 | -0.043 | -14.80€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 171 | -0.043 | -14.80€ | 4 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1667 | -0.021 | -62.84€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1667 | -0.021 | -62.84€ | 2 | 0 |
| ✅ STREAK_FADE_60M | 118 | -0.050 | -12.20€ | 5 | 0 |
| ✅ STREAK_FADE_60M#60min | 118 | -0.050 | -12.20€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 44 | -0.087 | -4.62€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 44 | -0.087 | -4.62€ | 4 | 0 |
| ✅ STREAK_FADE_60M#SOL | 74 | -0.026 | -7.58€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 74 | -0.026 | -7.58€ | 0 | 1 |
| ✅ STREAK_MOM_5M | 11535 | +0.014 | +71.00€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 11535 | +0.014 | +71.00€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2995 | +0.018 | +24.38€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2995 | +0.018 | +24.38€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 3029 | +0.015 | +30.97€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 3029 | +0.015 | +30.97€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2930 | +0.009 | -2.58€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2930 | +0.009 | -2.58€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2581 | +0.014 | +18.23€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2581 | +0.014 | +18.23€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 12205 | +0.018 | +1.48€ | 4 | 0 |
| ✅ STRUCT_NO_15M#15min | 12205 | +0.018 | +1.48€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 5049 | +0.021 | +5.54€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 5049 | +0.021 | +5.54€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 4221 | +0.018 | -1.84€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 4221 | +0.018 | -1.84€ | 4 | 0 |
| ✅ STRUCT_NO_15M#SOL | 2935 | +0.015 | -2.22€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 2935 | +0.015 | -2.22€ | 1 | 0 |
| ✅ UPDOWN_GBM | 109318 | +0.060 | +10362.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 26629 | +0.078 | +5321.57€ | 0 | 9 |
| ✅ UPDOWN_GBM#240min | 3210 | -0.000 | +33.01€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 72617 | +0.062 | +4904.31€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 6489 | -0.003 | +112.13€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 9145 | +0.104 | +1671.43€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1781 | +0.164 | +820.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 90 | -0.011 | -2.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 7274 | +0.091 | +853.24€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 24917 | +0.058 | +2209.58€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 3563 | +0.078 | +796.19€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 919 | -0.001 | +16.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 17406 | +0.068 | +1320.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 2893 | -0.005 | +73.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 136 | -0.065 | +3.23€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 11893 | +0.076 | +1326.43€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1761 | +0.154 | +738.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 86 | +0.023 | -0.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 10046 | +0.063 | +588.86€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 25931 | +0.050 | +1833.33€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 6286 | +0.072 | +962.51€ | 0 | 8 |
| ✅ UPDOWN_GBM#ETH#240min | 889 | +0.005 | +16.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 16247 | +0.052 | +815.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 2385 | +0.000 | +39.41€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 124 | -0.111 | +0.15€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 23165 | +0.039 | +1283.58€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 7178 | +0.031 | +422.15€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#240min | 829 | -0.010 | +4.67€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 13836 | +0.051 | +866.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 1211 | -0.003 | -0.35€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#daily | 111 | -0.146 | -9.73€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 14265 | +0.073 | +2040.32€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 6060 | +0.093 | +1582.09€ | 0 | 11 |
| ✅ UPDOWN_GBM#XRP#240min | 397 | +0.006 | -1.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 7808 | +0.060 | +459.85€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 371 | -0.106 | -6.35€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 1008 | +0.364 | +374.34€ | 0 | 10 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 1008 | +0.364 | +374.34€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 491 | +0.362 | +172.01€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 491 | +0.362 | +172.01€ | 0 | 9 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 517 | +0.365 | +202.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 517 | +0.365 | +202.33€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO | 25907 | -0.021 | +6439.50€ | 3 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 25907 | -0.021 | +6439.50€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1981 | -0.051 | +561.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1981 | -0.051 | +561.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 4830 | -0.115 | +276.11€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 4830 | -0.115 | +276.11€ | 3 | 11 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 1071 | +0.222 | +899.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 1071 | +0.222 | +899.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 3436 | +0.220 | +2193.21€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 3436 | +0.220 | +2193.21€ | 1 | 19 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 7356 | -0.060 | +1079.19€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 7356 | -0.060 | +1079.19€ | 4 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 7233 | -0.059 | +1429.95€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 7233 | -0.059 | +1429.95€ | 4 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 316 | +0.060 | +27.30€ | 0 | 9 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 316 | +0.060 | +27.30€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 316 | +0.060 | +27.30€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 316 | +0.060 | +27.30€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1826 | +0.282 | +1529.41€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1826 | +0.282 | +1529.41€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 963 | +0.275 | +754.71€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 963 | +0.275 | +754.71€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 863 | +0.288 | +774.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 863 | +0.288 | +774.70€ | 0 | 9 |
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
| ✅ WEEKLY_PRICE | 4779 | +0.300 | +2142.89€ | 0 | 3 |
| ✅ WEEKLY_PRICE#BTC | 1821 | +0.255 | +228.17€ | 0 | 3 |
| ✅ WEEKLY_PRICE#ETH | 1848 | +0.295 | +785.08€ | 0 | 3 |
| ✅ WEEKLY_PRICE#SOL | 1110 | +0.381 | +1129.64€ | 0 | 1 |