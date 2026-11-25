# Hipótesis automáticas — 2026-11-25 20:40 UTC
_Generado por shadow_postmortem.py sobre 1494601 resoluciones (PNL=+211796.28€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.495` → IC=-0.239 (n=236)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.113 (n=731)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.195 (n=1120)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` > 0.505 (IC base=+0.124)

- **PATRÓN** `n_total_lado` > `60.0` → IC=+0.173 (n=362)

  - _Acción_: Kelly boost +0.87€ cuando `n_total_lado` > 60.0 (IC base=+0.124)

- **PATRÓN** `banda_hit_calibrado` > `0.8181` → IC=+0.285 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8181 (IC base=+0.124)

- **PATRÓN** `banda_z` > `8.216` → IC=+0.192 (n=352)

  - _Acción_: Kelly boost +0.96€ cuando `banda_z` > 8.216 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.131 (n=1067)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 6.0 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.134 (n=1147)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.124)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.280 (n=171)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.107 (n=561)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.193 (n=983)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.505 (IC base=+0.126)

- **PATRÓN** `n_total_lado` > `63.0` → IC=+0.181 (n=308)

  - _Acción_: Kelly boost +0.90€ cuando `n_total_lado` > 63.0 (IC base=+0.126)

- **PATRÓN** `banda_hit_calibrado` > `0.8172` → IC=+0.281 (n=308)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8172 (IC base=+0.126)

- **PATRÓN** `banda_z` > `8.3` → IC=+0.194 (n=308)

  - _Acción_: Kelly boost +0.97€ cuando `banda_z` > 8.3 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.139 (n=837)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 8.0 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.129 (n=1047)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.01 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `5101.7817` → IC=+0.132 (n=419)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 5101.7817 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `8596.0083` → IC=+0.130 (n=249)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 8596.0083 (IC base=+0.016)

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
- **FILTRO** `restante_s_al_confirmar` < `130.52` → IC=-0.219 (n=12915)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 130.52
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=38745)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `122.97` → IC=-0.263 (n=1272)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 122.97
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=3816)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `114.34` → IC=-0.279 (n=1281)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 114.34
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=3848)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `restante_s_al_confirmar` < `116.14` → IC=-0.159 (n=3619)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 116.14
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=10858)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `146.81` → IC=-0.256 (n=3533)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 146.81
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=10602)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `128.04` → IC=-0.267 (n=2359)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 128.04
  - _Potencial_: sin este filtro IC_bueno=-0.095 (n=7078)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.208 (n=31013)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `7733.7379` → IC=+0.151 (n=2520)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 7733.7379 (IC base=+0.102)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.127 (n=27570)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 17.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.129 (n=33358)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.124)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.224 (n=24874)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.137 (n=8945)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `6255.203` → IC=+0.136 (n=3519)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 6255.203 (IC base=+0.124)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.182 (n=2239)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 5.0 (IC base=+0.174)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.358 (n=751)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.174)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.176 (n=2741)

  - _Acción_: Kelly boost +0.88€ cuando `libro_spread` < 0.01 (IC base=+0.174)

- **PATRÓN** `libro_liquidez` > `16191.7122` → IC=+0.182 (n=712)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 16191.7122 (IC base=+0.174)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.185 (n=1956)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 7.0 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.182 (n=2190)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 17.0 (IC base=+0.177)

- **PATRÓN** `py_entrada` < `0.265` → IC=+0.328 (n=764)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.265 (IC base=+0.177)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.181 (n=2800)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.01 (IC base=+0.177)

- **PATRÓN** `libro_liquidez` > `16004.1209` → IC=+0.185 (n=723)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 16004.1209 (IC base=+0.177)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.615` → IC=+0.170 (n=641)

  - _Acción_: Kelly boost +0.85€ cuando `py_entrada` > 0.615 (IC base=+0.074)

- **PATRÓN** `libro_liquidez` > `6825.0558` → IC=+0.126 (n=153)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 6825.0558 (IC base=+0.074)

- **PATRÓN** `py_entrada` < `0.45` → IC=+0.122 (n=2236)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` < 0.45 (IC base=+0.089)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.173 (n=5697)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 6.0 (IC base=+0.169)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.175 (n=2777)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 8.0 (IC base=+0.169)

- **PATRÓN** `py_entrada` > `0.78` → IC=+0.377 (n=1923)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.78 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.199 (n=2732)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.193)

- **PATRÓN** `py_entrada` < `0.275` → IC=+0.329 (n=1011)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.275 (IC base=+0.193)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.198 (n=3175)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.01 (IC base=+0.193)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.137 (n=1553)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.138 (n=1311)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 15.0 (IC base=+0.136)

- **PATRÓN** `py_entrada` > `0.65` → IC=+0.242 (n=673)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.65 (IC base=+0.136)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=1214)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `2037.9152` → IC=+0.139 (n=984)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 2037.9152 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `4420.281` → IC=+0.152 (n=156)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 4420.281 (IC base=+0.078)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.253 (n=998)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.230)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.230 (n=2048)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.230)

- **PATRÓN** `py_entrada` > `0.84` → IC=+0.428 (n=1345)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.84 (IC base=+0.230)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.145 (n=1493)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 7.0 (IC base=+0.145)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.155 (n=763)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 7.0 (IC base=+0.145)

- **PATRÓN** `py_entrada` < `0.315` → IC=+0.295 (n=558)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.315 (IC base=+0.145)

### FAVORITO_CONFIRMADO#SOL#60min
- **FILTRO** `py_entrada` < `0.55` → IC=-0.306 (n=153)

  - _Acción_: SKIP cuando `py_entrada` < 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.164 (n=489)

- **PATRÓN** `py_entrada` > `0.55` → IC=+0.164 (n=489)

  - _Acción_: Kelly boost +0.82€ cuando `py_entrada` > 0.55 (IC base=+0.051)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.140 (n=551)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 17.0 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.137 (n=1075)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 12.0 (IC base=+0.126)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.254 (n=506)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.126)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `10.0` → IC=-0.295 (n=76)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.237 (n=158)

- **FILTRO** `libro_liquidez` < `8957.4571` → IC=-0.263 (n=175)

  - _Acción_: SKIP cuando `libro_liquidez` < 8957.4571
  - _Potencial_: sin este filtro IC_bueno=-0.238 (n=59)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.198 (n=26189)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 6.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.191 (n=23304)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 15.0 (IC base=+0.191)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.220 (n=8785)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.191)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.338 (n=362)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.191)

- **PATRÓN** `libro_liquidez` > `8407.3041` → IC=+0.345 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8407.3041 (IC base=+0.191)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.166 (n=6295)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.160)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.174 (n=6073)

  - _Acción_: Kelly boost +0.87€ cuando `py_entrada` < 0.74 (IC base=+0.160)

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

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.210 (n=3907)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.203 (n=2602)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.243 (n=1861)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.203)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.181 (n=5812)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 6.0 (IC base=+0.171)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.172 (n=5187)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 15.0 (IC base=+0.171)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.174 (n=6280)

  - _Acción_: Kelly boost +0.87€ cuando `py_entrada` < 0.73 (IC base=+0.171)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.179 (n=4823)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` > 0.71 (IC base=+0.171)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.257 (n=4846)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.251)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.251 (n=2343)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.251)

- **PATRÓN** `py_entrada` > `0.8` → IC=+0.362 (n=1668)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.187 (n=5988)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.183)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.188 (n=3796)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 11.0 (IC base=+0.183)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.196 (n=1938)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` > 0.73 (IC base=+0.183)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.429 (n=1043)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.425)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.427 (n=1037)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.425)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.438 (n=1048)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.425)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.430 (n=1114)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.425)

- **PATRÓN** `libro_liquidez` > `13981.3978` → IC=+0.450 (n=337)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13981.3978 (IC base=+0.425)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` < `14.0` → IC=+0.445 (n=381)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.439)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.450 (n=474)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.439)

- **PATRÓN** `libro_liquidez` > `15243.1529` → IC=+0.444 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15243.1529 (IC base=+0.439)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.428 (n=402)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.421)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.423 (n=399)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.421)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.430 (n=401)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.421)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.426 (n=455)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.421)

- **PATRÓN** `libro_liquidez` > `4833.5247` → IC=+0.425 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4833.5247 (IC base=+0.421)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.408 (n=161)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.401)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.405 (n=156)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.401)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.420 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.401)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.765` → IC=-0.306 (n=34)

  - _Acción_: SKIP cuando `py_entrada` > 0.765
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=19)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.244 (n=37)

- **FILTRO** `libro_liquidez` < `6428.7632` → IC=-0.281 (n=39)

  - _Acción_: SKIP cuando `libro_liquidez` < 6428.7632
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=14)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.207 (n=36070)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.238 (n=35442)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.199)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.184 (n=5392)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 18.0 (IC base=+0.175)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.176 (n=11574)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 12.0 (IC base=+0.175)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.185 (n=16654)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` > 0.71 (IC base=+0.175)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.227 (n=15057)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.223)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.276 (n=6356)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.223)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.190 (n=6190)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 17.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.197 (n=12744)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` > 0.72 (IC base=+0.180)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.855` → IC=-0.357 (n=19)

  - _Acción_: SKIP cuando `py_entrada` < 0.855
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.228 (n=5045)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.221 (n=5798)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.218)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.259 (n=6146)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.218)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **FILTRO** `py_entrada` < `0.775` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **FILTRO** `libro_liquidez` < `3197.0694` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `libro_liquidez` < 3197.0694
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.210 (n=13715)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.206)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.252 (n=6464)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.206)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.203 (n=6018)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.199 (n=5980)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.239 (n=7416)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.196)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.196 (n=12919)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.138 (n=14248)

  - _Acción_: Kelly boost +0.69€ cuando `restante_min` > 4.96 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `2.28` → IC=+0.140 (n=12087)

  - _Acción_: Kelly boost +0.70€ cuando `lag_apertura_s` < 2.28 (IC base=+0.116)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.197 (n=6280)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.143 (n=6480)

  - _Acción_: Kelly boost +0.71€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.126 (n=8012)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 7.0 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `3.73` → IC=+0.141 (n=7933)

  - _Acción_: Kelly boost +0.71€ cuando `lag_apertura_s` < 3.73 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.196 (n=6639)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.135 (n=8576)

  - _Acción_: Kelly boost +0.67€ cuando `restante_min` > 4.95 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `2.88` → IC=+0.135 (n=8003)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 2.88 (IC base=+0.116)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.307 (n=1464)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.294)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.390 (n=749)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.294)

- **PATRÓN** `libro_liquidez` > `4014.7683` → IC=+0.295 (n=924)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4014.7683 (IC base=+0.294)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.302 (n=311)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.283)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.370 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.283)

- **PATRÓN** `libro_liquidez` > `3967.4956` → IC=+0.294 (n=933)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3967.4956 (IC base=+0.283)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.317 (n=714)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.297)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.301 (n=1037)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.297)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.395 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.297)

- **PATRÓN** `libro_liquidez` > `1486.6908` → IC=+0.307 (n=999)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1486.6908 (IC base=+0.297)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.441 (n=998)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.438)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.444 (n=959)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.438)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.438 (n=1166)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.438)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.440 (n=464)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.435)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.439 (n=326)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.435)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.434 (n=482)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.435)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.439 (n=476)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.435)

- **PATRÓN** `libro_liquidez` > `5550.9682` → IC=+0.437 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5550.9682 (IC base=+0.435)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.448 (n=324)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.441)

- **PATRÓN** `py_entrada` > `0.91` → IC=+0.444 (n=479)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.91 (IC base=+0.441)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.441 (n=558)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.441)

- **PATRÓN** `libro_liquidez` > `1961.5764` → IC=+0.441 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1961.5764 (IC base=+0.441)

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
- **FILTRO** `hora_utc` < `5.0` → IC=-0.286 (n=26)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.205 (n=127)

- **FILTRO** `py_entrada` > `0.765` → IC=-0.372 (n=37)

  - _Acción_: SKIP cuando `py_entrada` > 0.765
  - _Potencial_: sin este filtro IC_bueno=-0.170 (n=116)

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
- **FILTRO** `hora_utc` < `5.0` → IC=-0.286 (n=26)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.205 (n=127)

- **FILTRO** `py_entrada` > `0.765` → IC=-0.372 (n=37)

  - _Acción_: SKIP cuando `py_entrada` > 0.765
  - _Potencial_: sin este filtro IC_bueno=-0.170 (n=116)

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
- **PATRÓN** `drift_60min` |x|≤ `0.5109` → IC=+0.140 (n=20700)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.5109 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.129 (n=20985)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 6.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.126 (n=14393)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 12.0 (IC base=+0.124)

- **PATRÓN** `ibs_20min` > `0.9729` → IC=+0.246 (n=6903)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9729 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` > `0.888` → IC=+0.291 (n=1133)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.888 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.462` → IC=+0.190 (n=10377)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 3.462 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` > `0.6936` → IC=+0.267 (n=5663)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6936 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` > `0.3029` → IC=+0.256 (n=2136)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3029 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` > `2.7385` → IC=+0.234 (n=5006)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7385 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.140 (n=9943)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `4933.3912` → IC=+0.150 (n=6900)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 4933.3912 (IC base=+0.124)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.122 (n=13099)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0066 (IC base=+0.087)

- **PATRÓN** `ibs_20min` < `0.5642` → IC=+0.145 (n=26197)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.5642 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` > `0.6844` → IC=+0.191 (n=1777)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.6844 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` < `0.1797` → IC=+0.194 (n=10762)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` < 0.1797 (IC base=+0.087)

- **PATRÓN** `volumen_regimen` < `0.6925` → IC=+0.199 (n=4817)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_regimen` < 0.6925 (IC base=+0.087)

- **PATRÓN** `volumen_pendiente_norm` > `0.296` → IC=+0.230 (n=2653)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.296 (IC base=+0.087)

- **PATRÓN** `volumen_spike_ratio` > `2.2838` → IC=+0.212 (n=8415)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2838 (IC base=+0.087)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.227 (n=18548)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 100.0 (IC base=+0.087)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `drift_60min` |x|≤ `0.3051` → IC=+0.213 (n=3866)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3051 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.215 (n=4627)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.210)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.212 (n=2937)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `0.981` → IC=+0.273 (n=1992)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.981 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.8` → IC=+0.288 (n=1045)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.8 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.2341` → IC=+0.259 (n=764)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2341 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `1.4382` → IC=+0.212 (n=4221)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4382 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.221 (n=4615)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `2058.42` → IC=+0.213 (n=1464)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2058.42 (IC base=+0.210)

- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.245 (n=1815)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0099 (IC base=+0.238)

- **PATRÓN** `drift_60min` |x|≤ `0.0971` → IC=+0.269 (n=1333)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0971 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.239 (n=4162)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.238)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.245 (n=1830)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.238)

- **PATRÓN** `ibs_20min` < `0.0813` → IC=+0.276 (n=1333)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0813 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` < `0.0962` → IC=+0.240 (n=3642)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0962 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` > `0.2886` → IC=+0.247 (n=532)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2886 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` < `1.555` → IC=+0.237 (n=1685)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.555 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` > `1.8565` → IC=+0.242 (n=2553)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8565 (IC base=+0.238)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.241 (n=4342)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.238)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.233 (n=1256)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0032 (IC base=+0.220)

- **PATRÓN** `drift_60min` |x|≤ `0.1158` → IC=+0.244 (n=1657)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1158 (IC base=+0.220)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.232 (n=3958)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.220)

- **PATRÓN** `ibs_20min` > `0.8896` → IC=+0.248 (n=1256)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8896 (IC base=+0.220)

- **PATRÓN** `dist_vwap_pct` > `0.2064` → IC=+0.229 (n=1639)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2064 (IC base=+0.220)

- **PATRÓN** `dist_vwap_pct` < `0.5806` → IC=+0.220 (n=4162)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5806 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.702` → IC=+0.260 (n=539)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.702 (IC base=+0.220)

- **PATRÓN** `volumen_regimen` > `0.6958` → IC=+0.228 (n=3366)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6958 (IC base=+0.220)

- **PATRÓN** `volumen_pendiente_norm` > `0.2768` → IC=+0.262 (n=519)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2768 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` > `2.4328` → IC=+0.245 (n=1241)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4328 (IC base=+0.220)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.158 (n=3639)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0062 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.3642` → IC=+0.143 (n=4132)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.3642 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.150 (n=1551)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 17.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` < `0.7104` → IC=+0.171 (n=4132)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.7104 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.7771` → IC=+0.141 (n=4998)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.7771 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.586` → IC=+0.136 (n=647)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` > 10.586 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.967` → IC=+0.141 (n=3809)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 3.967 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `0.6285` → IC=+0.157 (n=1378)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.6285 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.0982` → IC=+0.159 (n=1499)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` > 0.0982 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `2.4453` → IC=+0.143 (n=4001)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.4453 (IC base=+0.136)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.136 (n=5367)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `166.0` → IC=+0.186 (n=1321)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 166.0 (IC base=+0.136)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0119` → IC=+0.210 (n=2112)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0119 (IC base=+0.194)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.203 (n=4909)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.194)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.251 (n=1792)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.194)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.879` → IC=+0.276 (n=1030)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.879 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` < `0.0969` → IC=+0.192 (n=4176)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` < 0.0969 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` > `0.3486` → IC=+0.224 (n=595)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3486 (IC base=+0.194)

- **PATRÓN** `volumen_spike_ratio` > `2.7293` → IC=+0.209 (n=2065)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7293 (IC base=+0.194)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.198 (n=5542)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.04 (IC base=+0.194)

- **PATRÓN** `libro_liquidez` > `1904.2584` → IC=+0.202 (n=2111)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1904.2584 (IC base=+0.194)

- **PATRÓN** `sigma_h` < `0.0083` → IC=+0.227 (n=1926)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0083 (IC base=+0.220)

- **PATRÓN** `sigma_h` > `0.0115` → IC=+0.221 (n=1983)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0115 (IC base=+0.220)

- **PATRÓN** `drift_60min` |x|≤ `0.1834` → IC=+0.232 (n=1926)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1834 (IC base=+0.220)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.240 (n=1653)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.220)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.226 (n=1989)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.220)

- **PATRÓN** `ibs_20min` < `0.054` → IC=+0.268 (n=1458)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.054 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.622` → IC=+0.267 (n=470)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.622 (IC base=+0.220)

- **PATRÓN** `volumen_pendiente_norm` > `0.346` → IC=+0.250 (n=634)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.346 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` > `2.1533` → IC=+0.230 (n=2819)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1533 (IC base=+0.220)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.223 (n=2041)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.220)

- **PATRÓN** `libro_liquidez` > `1885.5351` → IC=+0.222 (n=1983)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1885.5351 (IC base=+0.220)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.220 (n=4184)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 21.0 (IC base=+0.220)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.168 (n=260)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=5621)

- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.140 (n=754)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0041 (IC base=+0.070)

- **PATRÓN** `ibs_20min` > `0.9422` → IC=+0.248 (n=753)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9422 (IC base=+0.070)

- **PATRÓN** `dist_vwap_pct` > `0.1608` → IC=+0.349 (n=520)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1608 (IC base=+0.070)

- **PATRÓN** `dist_vwap_pct` < `0.3799` → IC=+0.342 (n=891)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3799 (IC base=+0.070)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.222` → IC=+0.216 (n=1659)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.222 (IC base=+0.070)

- **PATRÓN** `volumen_regimen` > `1.2469` → IC=+0.362 (n=310)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2469 (IC base=+0.070)

- **PATRÓN** `volumen_pendiente_norm` < `0.0737` → IC=+0.344 (n=588)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0737 (IC base=+0.070)

- **PATRÓN** `volumen_pendiente_norm` > `0.2994` → IC=+0.360 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2994 (IC base=+0.070)

- **PATRÓN** `volumen_spike_ratio` < `1.4157` → IC=+0.366 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4157 (IC base=+0.070)

- **PATRÓN** `volumen_spike_ratio` > `2.2709` → IC=+0.350 (n=412)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2709 (IC base=+0.070)

- **PATRÓN** `ballena_activa_n` < `142.0` → IC=+0.348 (n=920)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 142.0 (IC base=+0.070)

- **PATRÓN** `ibs_20min` < `0.0867` → IC=+0.188 (n=1471)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.0867 (IC base=+0.059)

- **PATRÓN** `dist_vwap_pct` > `0.3682` → IC=+0.157 (n=729)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.3682 (IC base=+0.059)

- **PATRÓN** `dist_vwap_pct` < `0.1559` → IC=+0.155 (n=2774)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1559 (IC base=+0.059)

- **PATRÓN** `volumen_regimen` < `0.8259` → IC=+0.161 (n=1936)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.8259 (IC base=+0.059)

- **PATRÓN** `volumen_pendiente_norm` > `0.2779` → IC=+0.195 (n=368)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2779 (IC base=+0.059)

- **PATRÓN** `volumen_spike_ratio` > `2.1345` → IC=+0.168 (n=1270)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 2.1345 (IC base=+0.059)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.181 (n=164)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=911)

- **FILTRO** `ibs_20min` < `0.2727` → IC=-0.181 (n=268)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2727
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=807)

- **FILTRO** `ibs_20min` > `0.1923` → IC=-0.124 (n=5522)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1923
  - _Potencial_: sin este filtro IC_bueno=+0.160 (n=2726)

- **FILTRO** `sigma_ewma_delta_pct` > `8.312` → IC=-0.229 (n=891)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.312
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=7357)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.179 (n=369)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.75 (IC base=+0.021)

- **PATRÓN** `dist_vwap_pct` > `0.9864` → IC=+0.279 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9864 (IC base=+0.021)

- **PATRÓN** `dist_vwap_pct` < `1.3801` → IC=+0.266 (n=378)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 1.3801 (IC base=+0.021)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.266` → IC=+0.145 (n=364)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 2.266 (IC base=+0.021)

- **PATRÓN** `volumen_regimen` > `1.0067` → IC=+0.323 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0067 (IC base=+0.021)

- **PATRÓN** `volumen_pendiente_norm` < `0.1622` → IC=+0.273 (n=364)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1622 (IC base=+0.021)

- **PATRÓN** `volumen_spike_ratio` < `2.1724` → IC=+0.279 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1724 (IC base=+0.021)

- **PATRÓN** `ibs_20min` < `0.1923` → IC=+0.160 (n=2726)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.1923 (IC base=-0.030)

- **PATRÓN** `dist_vwap_pct` > `0.8451` → IC=+0.295 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8451 (IC base=-0.030)

- **PATRÓN** `dist_vwap_pct` < `0.2399` → IC=+0.293 (n=1288)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2399 (IC base=-0.030)

- **PATRÓN** `volumen_regimen` < `0.6941` → IC=+0.307 (n=552)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6941 (IC base=-0.030)

- **PATRÓN** `volumen_regimen` > `1.0428` → IC=+0.293 (n=568)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0428 (IC base=-0.030)

- **PATRÓN** `volumen_pendiente_norm` > `0.0789` → IC=+0.318 (n=570)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0789 (IC base=-0.030)

- **PATRÓN** `volumen_spike_ratio` < `1.7994` → IC=+0.311 (n=787)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7994 (IC base=-0.030)

- **PATRÓN** `volumen_spike_ratio` > `1.5263` → IC=+0.301 (n=1054)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5263 (IC base=-0.030)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `ibs_20min` < `0.7959` → IC=-0.160 (n=4243)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7959
  - _Potencial_: sin este filtro IC_bueno=+0.146 (n=2187)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.177 (n=1340)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=5090)

- **FILTRO** `ibs_20min` > `0.7204` → IC=-0.190 (n=2223)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7204
  - _Potencial_: sin este filtro IC_bueno=+0.074 (n=6670)

- **PATRÓN** `ibs_20min` > `0.7959` → IC=+0.146 (n=2187)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` > 0.7959 (IC base=-0.056)

- **PATRÓN** `dist_vwap_pct` > `0.4559` → IC=+0.343 (n=456)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4559 (IC base=-0.056)

- **PATRÓN** `volumen_regimen` > `0.704` → IC=+0.319 (n=1172)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.704 (IC base=-0.056)

- **PATRÓN** `volumen_pendiente_norm` > `0.3081` → IC=+0.320 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3081 (IC base=-0.056)

- **PATRÓN** `volumen_spike_ratio` > `2.5309` → IC=+0.319 (n=429)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5309 (IC base=-0.056)

- **PATRÓN** `dist_vwap_pct` > `1.1147` → IC=+0.289 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1147 (IC base=+0.008)

- **PATRÓN** `volumen_regimen` < `0.636` → IC=+0.275 (n=887)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.636 (IC base=+0.008)

- **PATRÓN** `volumen_regimen` > `1.2131` → IC=+0.278 (n=886)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2131 (IC base=+0.008)

- **PATRÓN** `volumen_pendiente_norm` > `0.2919` → IC=+0.279 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2919 (IC base=+0.008)

- **PATRÓN** `volumen_spike_ratio` < `2.5013` → IC=+0.262 (n=2527)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5013 (IC base=+0.008)

- **PATRÓN** `volumen_spike_ratio` > `1.4437` → IC=+0.268 (n=2527)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4437 (IC base=+0.008)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.185 (n=9059)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0113 (IC base=+0.087)

- **PATRÓN** `ibs_20min` > `0.8658` → IC=+0.283 (n=12318)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8658 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` > `1.015` → IC=+0.306 (n=1868)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.015 (IC base=+0.087)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.454` → IC=+0.168 (n=12242)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 3.454 (IC base=+0.087)

- **PATRÓN** `volumen_regimen` > `0.6925` → IC=+0.279 (n=9058)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6925 (IC base=+0.087)

- **PATRÓN** `volumen_pendiente_norm` > `0.2925` → IC=+0.296 (n=2241)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2925 (IC base=+0.087)

- **PATRÓN** `volumen_spike_ratio` > `2.6453` → IC=+0.288 (n=5260)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6453 (IC base=+0.087)

- **PATRÓN** `ballena_activa_n` < `88.0` → IC=+0.308 (n=15439)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 88.0 (IC base=+0.087)

- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.152 (n=11994)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` > 0.0094 (IC base=+0.089)

- **PATRÓN** `ibs_20min` < `0.5158` → IC=+0.174 (n=23254)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.5158 (IC base=+0.089)

- **PATRÓN** `dist_vwap_pct` < `0.208` → IC=+0.283 (n=9041)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.208 (IC base=+0.089)

- **PATRÓN** `volumen_regimen` < `0.6927` → IC=+0.279 (n=3982)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6927 (IC base=+0.089)

- **PATRÓN** `volumen_regimen` > `1.1877` → IC=+0.286 (n=3017)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1877 (IC base=+0.089)

- **PATRÓN** `volumen_pendiente_norm` > `0.295` → IC=+0.321 (n=1996)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.295 (IC base=+0.089)

- **PATRÓN** `volumen_spike_ratio` < `1.4539` → IC=+0.302 (n=4493)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4539 (IC base=+0.089)

- **PATRÓN** `volumen_spike_ratio` > `2.275` → IC=+0.305 (n=6108)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.275 (IC base=+0.089)

- **PATRÓN** `ballena_activa_n` < `70.0` → IC=+0.311 (n=13459)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 70.0 (IC base=+0.089)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.8172` → IC=-0.148 (n=4806)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8172
  - _Potencial_: sin este filtro IC_bueno=+0.312 (n=2477)

- **FILTRO** `ibs_20min` > `0.698` → IC=-0.242 (n=1648)

  - _Acción_: SKIP cuando `ibs_20min` > 0.698
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=4946)

- **FILTRO** `sigma_ewma_delta_pct` > `4.051` → IC=-0.239 (n=1382)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.051
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=5212)

- **PATRÓN** `ibs_20min` > `0.8172` → IC=+0.312 (n=2477)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8172 (IC base=+0.009)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.153` → IC=+0.175 (n=2712)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 2.153 (IC base=+0.009)

- **PATRÓN** `volumen_pendiente_norm` > `0.2297` → IC=+0.332 (n=461)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2297 (IC base=+0.009)

- **PATRÓN** `volumen_spike_ratio` < `1.4472` → IC=+0.293 (n=762)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4472 (IC base=+0.009)

- **PATRÓN** `volumen_spike_ratio` > `2.2281` → IC=+0.318 (n=1035)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2281 (IC base=+0.009)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.318 (n=2005)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 19.0 (IC base=+0.009)

- **PATRÓN** `ibs_20min` < `0.1705` → IC=+0.172 (n=1649)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.1705 (IC base=-0.013)

- **PATRÓN** `volumen_pendiente_norm` < `0.1556` → IC=+0.384 (n=1492)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1556 (IC base=-0.013)

- **PATRÓN** `volumen_spike_ratio` < `2.6493` → IC=+0.389 (n=1433)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.6493 (IC base=-0.013)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.1845` → IC=+0.229 (n=1105)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1845 (IC base=+0.009)

- **PATRÓN** `volumen_regimen` < `1.1952` → IC=+0.214 (n=2653)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1952 (IC base=+0.009)

- **PATRÓN** `volumen_regimen` > `0.6941` → IC=+0.222 (n=2370)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6941 (IC base=+0.009)

- **PATRÓN** `volumen_pendiente_norm` > `0.2732` → IC=+0.244 (n=353)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2732 (IC base=+0.009)

- **PATRÓN** `volumen_spike_ratio` < `1.4147` → IC=+0.230 (n=875)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4147 (IC base=+0.009)

- **PATRÓN** `volumen_spike_ratio` > `2.4465` → IC=+0.222 (n=875)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4465 (IC base=+0.009)

- **PATRÓN** `ballena_activa_n` < `367.0` → IC=+0.232 (n=2625)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 367.0 (IC base=+0.009)

- **PATRÓN** `dist_vwap_pct` < `0.5781` → IC=+0.258 (n=2366)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5781 (IC base=+0.005)

- **PATRÓN** `volumen_regimen` > `1.0185` → IC=+0.268 (n=895)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0185 (IC base=+0.005)

- **PATRÓN** `volumen_pendiente_norm` > `0.2701` → IC=+0.287 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2701 (IC base=+0.005)

- **PATRÓN** `volumen_spike_ratio` < `1.5317` → IC=+0.258 (n=845)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5317 (IC base=+0.005)

- **PATRÓN** `volumen_spike_ratio` > `2.1516` → IC=+0.262 (n=870)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1516 (IC base=+0.005)

- **PATRÓN** `ballena_activa_n` < `196.0` → IC=+0.275 (n=850)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 196.0 (IC base=+0.005)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0118` → IC=+0.316 (n=1681)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0118 (IC base=+0.284)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.293 (n=3730)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.284)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.322 (n=2007)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.284)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.57` → IC=+0.306 (n=2524)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.57 (IC base=+0.284)

- **PATRÓN** `volumen_pendiente_norm` < `0.13` → IC=+0.292 (n=3448)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.13 (IC base=+0.284)

- **PATRÓN** `volumen_spike_ratio` > `2.1656` → IC=+0.295 (n=2408)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1656 (IC base=+0.284)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.293 (n=4388)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.284)

- **PATRÓN** `libro_liquidez` > `2017.0956` → IC=+0.298 (n=1236)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2017.0956 (IC base=+0.284)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.299 (n=2337)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.284)

- **PATRÓN** `sigma_h` > `0.0123` → IC=+0.343 (n=1154)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0123 (IC base=+0.307)

- **PATRÓN** `drift_60min` |x|≤ `0.189` → IC=+0.328 (n=1525)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.189 (IC base=+0.307)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.322 (n=1328)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.307)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.312 (n=1565)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.307)

- **PATRÓN** `ibs_20min` < `0.0311` → IC=+0.308 (n=1523)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0311 (IC base=+0.307)

- **PATRÓN** `ibs_20min` > `0.1563` → IC=+0.321 (n=2308)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1563 (IC base=+0.307)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.974` → IC=+0.319 (n=396)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.974 (IC base=+0.307)

- **PATRÓN** `volumen_pendiente_norm` < `0.1983` → IC=+0.308 (n=3442)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1983 (IC base=+0.307)

- **PATRÓN** `volumen_pendiente_norm` > `0.3449` → IC=+0.314 (n=556)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3449 (IC base=+0.307)

- **PATRÓN** `volumen_spike_ratio` > `2.7414` → IC=+0.325 (n=1522)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7414 (IC base=+0.307)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.308 (n=1625)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.307)

- **PATRÓN** `libro_liquidez` > `1580.478` → IC=+0.313 (n=3093)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1580.478 (IC base=+0.307)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.309 (n=2963)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 20.0 (IC base=+0.307)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **PATRÓN** `dist_vwap_pct` > `0.1617` → IC=+0.238 (n=1223)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1617 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` < `0.6456` → IC=+0.233 (n=2745)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6456 (IC base=+0.025)

- **PATRÓN** `volumen_regimen` < `1.1742` → IC=+0.236 (n=2494)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1742 (IC base=+0.025)

- **PATRÓN** `volumen_regimen` > `0.5993` → IC=+0.233 (n=2494)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.5993 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` > `0.1023` → IC=+0.237 (n=812)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1023 (IC base=+0.025)

- **PATRÓN** `volumen_spike_ratio` < `2.4059` → IC=+0.241 (n=2423)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4059 (IC base=+0.025)

- **PATRÓN** `ballena_activa_n` < `114.0` → IC=+0.251 (n=2477)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 114.0 (IC base=+0.025)

- **PATRÓN** `ibs_20min` < `0.0925` → IC=+0.152 (n=1715)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` < 0.0925 (IC base=+0.014)

- **PATRÓN** `dist_vwap_pct` < `0.3919` → IC=+0.261 (n=2028)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3919 (IC base=+0.014)

- **PATRÓN** `volumen_regimen` < `1.1763` → IC=+0.262 (n=1831)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1763 (IC base=+0.014)

- **PATRÓN** `volumen_regimen` > `0.6142` → IC=+0.259 (n=1830)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6142 (IC base=+0.014)

- **PATRÓN** `volumen_pendiente_norm` < `0.1002` → IC=+0.264 (n=1720)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1002 (IC base=+0.014)

- **PATRÓN** `volumen_pendiente_norm` > `0.2812` → IC=+0.284 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2812 (IC base=+0.014)

- **PATRÓN** `volumen_spike_ratio` < `1.776` → IC=+0.281 (n=1178)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.776 (IC base=+0.014)

- **PATRÓN** `volumen_spike_ratio` > `2.4173` → IC=+0.270 (n=589)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4173 (IC base=+0.014)

- **PATRÓN** `ballena_activa_n` < `97.0` → IC=+0.284 (n=1579)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 97.0 (IC base=+0.014)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.75` → IC=-0.248 (n=2773)

  - _Acción_: SKIP cuando `ibs_20min` < 0.75
  - _Potencial_: sin este filtro IC_bueno=+0.316 (n=2807)

- **FILTRO** `ibs_20min` > `0.6038` → IC=-0.236 (n=1316)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6038
  - _Potencial_: sin este filtro IC_bueno=+0.169 (n=3960)

- **FILTRO** `sigma_ewma_delta_pct` > `8.259` → IC=-0.263 (n=605)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.259
  - _Potencial_: sin este filtro IC_bueno=+0.111 (n=4671)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.316 (n=2807)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.75 (IC base=+0.036)

- **PATRÓN** `dist_vwap_pct` > `1.1323` → IC=+0.352 (n=398)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1323 (IC base=+0.036)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.448` → IC=+0.161 (n=2284)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 2.448 (IC base=+0.036)

- **PATRÓN** `volumen_regimen` < `0.8444` → IC=+0.352 (n=1370)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8444 (IC base=+0.036)

- **PATRÓN** `volumen_pendiente_norm` < `0.1` → IC=+0.338 (n=1936)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1 (IC base=+0.036)

- **PATRÓN** `volumen_pendiente_norm` > `0.2751` → IC=+0.371 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2751 (IC base=+0.036)

- **PATRÓN** `volumen_spike_ratio` < `1.7937` → IC=+0.356 (n=1333)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7937 (IC base=+0.036)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.357 (n=1771)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 42.0 (IC base=+0.036)

- **PATRÓN** `ibs_20min` < `0.6038` → IC=+0.169 (n=3960)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` < 0.6038 (IC base=+0.068)

- **PATRÓN** `dist_vwap_pct` < `0.2486` → IC=+0.276 (n=2063)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2486 (IC base=+0.068)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.736` → IC=+0.136 (n=4138)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 4.736 (IC base=+0.068)

- **PATRÓN** `volumen_regimen` < `0.6872` → IC=+0.287 (n=918)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6872 (IC base=+0.068)

- **PATRÓN** `volumen_pendiente_norm` > `0.0724` → IC=+0.299 (n=834)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0724 (IC base=+0.068)

- **PATRÓN** `volumen_spike_ratio` < `1.807` → IC=+0.283 (n=1350)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.807 (IC base=+0.068)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.292 (n=2054)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=+0.068)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.350 (n=2629)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.312)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.314 (n=2972)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.312)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.314 (n=3085)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.312)

- **PATRÓN** `ibs_20min` > `0.65` → IC=+0.336 (n=2941)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.65 (IC base=+0.312)

- **PATRÓN** `dist_vwap_pct` > `0.2225` → IC=+0.336 (n=1557)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2225 (IC base=+0.312)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.743` → IC=+0.341 (n=1162)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.743 (IC base=+0.312)

- **PATRÓN** `volumen_regimen` > `0.7017` → IC=+0.327 (n=2626)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7017 (IC base=+0.312)

- **PATRÓN** `volumen_pendiente_norm` > `0.2862` → IC=+0.344 (n=420)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2862 (IC base=+0.312)

- **PATRÓN** `volumen_spike_ratio` > `1.4358` → IC=+0.323 (n=2841)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4358 (IC base=+0.312)

- **PATRÓN** `libro_liquidez` > `3000.8154` → IC=+0.321 (n=980)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3000.8154 (IC base=+0.312)

- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.329 (n=3166)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0094 (IC base=+0.313)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.315 (n=3172)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.313)

- **PATRÓN** `ibs_20min` < `0.39` → IC=+0.326 (n=3166)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.39 (IC base=+0.313)

- **PATRÓN** `dist_vwap_pct` > `1.313` → IC=+0.320 (n=370)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.313 (IC base=+0.313)

- **PATRÓN** `dist_vwap_pct` < `0.2612` → IC=+0.315 (n=3130)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2612 (IC base=+0.313)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.047` → IC=+0.327 (n=577)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.047 (IC base=+0.313)

- **PATRÓN** `volumen_regimen` < `0.6352` → IC=+0.317 (n=1055)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6352 (IC base=+0.313)

- **PATRÓN** `volumen_regimen` > `1.2104` → IC=+0.340 (n=1056)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2104 (IC base=+0.313)

- **PATRÓN** `volumen_pendiente_norm` > `0.2887` → IC=+0.361 (n=436)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2887 (IC base=+0.313)

- **PATRÓN** `volumen_spike_ratio` < `1.4156` → IC=+0.323 (n=993)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4156 (IC base=+0.313)

- **PATRÓN** `volumen_spike_ratio` > `2.1607` → IC=+0.319 (n=1350)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1607 (IC base=+0.313)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0129` → IC=+0.219 (n=6620)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0129 (IC base=+0.172)

- **PATRÓN** `drift_60min` |x|≤ `0.1282` → IC=+0.193 (n=8731)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.1282 (IC base=+0.172)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.184 (n=20672)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.172)

- **PATRÓN** `ibs_20min` > `0.5344` → IC=+0.228 (n=19839)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5344 (IC base=+0.172)

- **PATRÓN** `dist_vwap_pct` > `0.1727` → IC=+0.205 (n=7438)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1727 (IC base=+0.172)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.694` → IC=+0.261 (n=3885)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.694 (IC base=+0.172)

- **PATRÓN** `volumen_regimen` < `1.1739` → IC=+0.152 (n=13239)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.1739 (IC base=+0.172)

- **PATRÓN** `volumen_regimen` > `0.6201` → IC=+0.151 (n=13238)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 0.6201 (IC base=+0.172)

- **PATRÓN** `volumen_pendiente_norm` > `0.2935` → IC=+0.207 (n=2855)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2935 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` > `2.6037` → IC=+0.185 (n=6445)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 2.6037 (IC base=+0.172)

- **PATRÓN** `ballena_activa_n` < `85.0` → IC=+0.191 (n=18801)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 85.0 (IC base=+0.172)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.193 (n=8770)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0062 (IC base=+0.185)

- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.186 (n=13248)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0083 (IC base=+0.185)

- **PATRÓN** `drift_60min` |x|≤ `0.0866` → IC=+0.223 (n=6625)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0866 (IC base=+0.185)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.206 (n=9533)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.185)

- **PATRÓN** `ibs_20min` < `0.5283` → IC=+0.237 (n=19872)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5283 (IC base=+0.185)

- **PATRÓN** `dist_vwap_pct` < `0.1998` → IC=+0.179 (n=14540)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` < 0.1998 (IC base=+0.185)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.387` → IC=+0.190 (n=3114)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 9.387 (IC base=+0.185)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.489` → IC=+0.191 (n=17779)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` < 2.489 (IC base=+0.185)

- **PATRÓN** `volumen_regimen` < `0.6995` → IC=+0.174 (n=6187)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.6995 (IC base=+0.185)

- **PATRÓN** `volumen_pendiente_norm` > `0.2959` → IC=+0.216 (n=2974)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2959 (IC base=+0.185)

- **PATRÓN** `volumen_spike_ratio` > `2.6399` → IC=+0.196 (n=6339)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.6399 (IC base=+0.185)

- **PATRÓN** `ballena_activa_n` < `89.0` → IC=+0.199 (n=18843)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 89.0 (IC base=+0.185)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `drift_60min` |x|≤ `0.0759` → IC=+0.267 (n=1085)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0759 (IC base=+0.228)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.235 (n=3408)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.228)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.229 (n=2203)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.228)

- **PATRÓN** `ibs_20min` > `0.9412` → IC=+0.291 (n=2170)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9412 (IC base=+0.228)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.47` → IC=+0.327 (n=1068)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.47 (IC base=+0.228)

- **PATRÓN** `volumen_pendiente_norm` > `0.2821` → IC=+0.285 (n=482)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2821 (IC base=+0.228)

- **PATRÓN** `volumen_spike_ratio` < `1.8299` → IC=+0.226 (n=2078)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8299 (IC base=+0.228)

- **PATRÓN** `volumen_spike_ratio` > `1.4343` → IC=+0.228 (n=3117)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4343 (IC base=+0.228)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.236 (n=3435)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.228)

- **PATRÓN** `sigma_h` < `0.0105` → IC=+0.254 (n=2767)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0105 (IC base=+0.251)

- **PATRÓN** `drift_60min` |x|≤ `0.1024` → IC=+0.309 (n=1217)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1024 (IC base=+0.251)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.255 (n=2847)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.251)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.255 (n=2518)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.251)

- **PATRÓN** `ibs_20min` < `0.0068` → IC=+0.309 (n=922)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0068 (IC base=+0.251)

- **PATRÓN** `sigma_ewma_delta_pct` < `1.95` → IC=+0.256 (n=2736)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 1.95 (IC base=+0.251)

- **PATRÓN** `volumen_pendiente_norm` < `0.0741` → IC=+0.254 (n=2307)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0741 (IC base=+0.251)

- **PATRÓN** `volumen_pendiente_norm` > `0.3015` → IC=+0.263 (n=416)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3015 (IC base=+0.251)

- **PATRÓN** `volumen_spike_ratio` < `1.554` → IC=+0.264 (n=1170)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.554 (IC base=+0.251)

- **PATRÓN** `volumen_spike_ratio` > `2.6858` → IC=+0.255 (n=886)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6858 (IC base=+0.251)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.260 (n=1849)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.251)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.188 (n=1018)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0034 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.0683` → IC=+0.173 (n=1015)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.0683 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.145 (n=3180)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` > `0.2442` → IC=+0.201 (n=3042)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2442 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` > `0.1993` → IC=+0.210 (n=1466)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1993 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.539` → IC=+0.203 (n=547)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.539 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `0.8519` → IC=+0.134 (n=2029)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 0.8519 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` > `1.1922` → IC=+0.128 (n=1014)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` > 1.1922 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` > `0.2757` → IC=+0.168 (n=462)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` > 0.2757 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `1.4086` → IC=+0.129 (n=999)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 1.4086 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` > `2.4553` → IC=+0.138 (n=999)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 2.4553 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `384.0` → IC=+0.130 (n=2970)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 384.0 (IC base=+0.126)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.181 (n=2911)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0061 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.2619` → IC=+0.175 (n=2907)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.2619 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.175 (n=1579)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 15.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` < `0.6162` → IC=+0.210 (n=3302)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6162 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` < `0.2257` → IC=+0.176 (n=3590)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.2257 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.871` → IC=+0.180 (n=607)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 10.871 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.013` → IC=+0.156 (n=2907)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 4.013 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` < `1.2065` → IC=+0.163 (n=3302)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2065 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` < `0.0974` → IC=+0.154 (n=2907)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` < 0.0974 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `2.1486` → IC=+0.158 (n=2794)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.1486 (IC base=+0.153)

- **PATRÓN** `ballena_activa_n` < `202.0` → IC=+0.196 (n=1367)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 202.0 (IC base=+0.153)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.012` → IC=+0.230 (n=1518)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.012 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.2587` → IC=+0.234 (n=2232)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2587 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.219 (n=3511)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.286 (n=1774)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.982` → IC=+0.305 (n=793)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.982 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.3485` → IC=+0.231 (n=473)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3485 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `2.7121` → IC=+0.222 (n=1485)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7121 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.213 (n=3993)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `2014.9484` → IC=+0.223 (n=1116)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2014.9484 (IC base=+0.210)

- **PATRÓN** `sigma_h` < `0.0124` → IC=+0.242 (n=3046)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0124 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.1419` → IC=+0.275 (n=1339)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1419 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.272 (n=1146)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` < `0.0445` → IC=+0.289 (n=1339)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0445 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.722` → IC=+0.281 (n=399)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.722 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.3531` → IC=+0.279 (n=505)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3531 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` < `1.7646` → IC=+0.241 (n=1298)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7646 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `2.1795` → IC=+0.248 (n=1967)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1795 (IC base=+0.237)

- **PATRÓN** `libro_liquidez` > `1880.6384` → IC=+0.247 (n=1379)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1880.6384 (IC base=+0.237)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.235 (n=2932)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 23.0 (IC base=+0.237)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.192 (n=1094)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.004 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.083` → IC=+0.170 (n=1092)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.083 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.138 (n=3400)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` > `0.2434` → IC=+0.188 (n=3274)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.2434 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` > `0.1514` → IC=+0.189 (n=1836)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1514 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.172` → IC=+0.198 (n=555)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 11.172 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `0.8362` → IC=+0.139 (n=2184)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 0.8362 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` > `0.2868` → IC=+0.176 (n=492)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.2868 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `1.5149` → IC=+0.126 (n=1411)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 1.5149 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` > `2.4974` → IC=+0.137 (n=1069)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 2.4974 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `6913.8034` → IC=+0.196 (n=1485)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 6913.8034 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `123.0` → IC=+0.127 (n=3218)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 123.0 (IC base=+0.126)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.173 (n=2340)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0058 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.4368` → IC=+0.150 (n=3511)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.4368 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.164 (n=1685)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 15.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` < `0.6697` → IC=+0.188 (n=3509)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.6697 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` < `0.1747` → IC=+0.156 (n=3601)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1747 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.5` → IC=+0.142 (n=1196)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 6.5 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `0.8521` → IC=+0.152 (n=2340)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.8521 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` > `0.2922` → IC=+0.167 (n=529)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.2922 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` < `2.1878` → IC=+0.135 (n=2945)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 2.1878 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` > `1.4068` → IC=+0.135 (n=3345)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.4068 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `6678.0732` → IC=+0.191 (n=1591)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 6678.0732 (IC base=+0.133)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.156 (n=1131)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 48.0 (IC base=+0.133)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0132` → IC=+0.176 (n=1220)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.0132 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.137 (n=3759)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` > `0.4717` → IC=+0.205 (n=3648)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4717 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` > `0.8078` → IC=+0.214 (n=926)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8078 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.901` → IC=+0.284 (n=766)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.901 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` < `1.1669` → IC=+0.131 (n=3648)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.1669 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` > `0.6237` → IC=+0.125 (n=3648)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` > 0.6237 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` < `0.1631` → IC=+0.124 (n=3725)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.1631 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` > `0.282` → IC=+0.131 (n=508)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_pendiente_norm` > 0.282 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` < `1.544` → IC=+0.127 (n=1559)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 1.544 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `2717.8185` → IC=+0.200 (n=1654)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2717.8185 (IC base=+0.122)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.127 (n=2376)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 27.0 (IC base=+0.122)

- **PATRÓN** `sigma_h` < `0.0113` → IC=+0.153 (n=3380)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0113 (IC base=+0.125)

- **PATRÓN** `drift_60min` |x|≤ `0.1196` → IC=+0.171 (n=1279)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.1196 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.139 (n=3917)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` < `0.6429` → IC=+0.222 (n=3836)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6429 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` < `0.2311` → IC=+0.148 (n=3818)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.2311 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.23` → IC=+0.147 (n=3401)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 2.23 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` < `1.1819` → IC=+0.131 (n=3836)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.1819 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` > `0.8584` → IC=+0.126 (n=2557)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` > 0.8584 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` < `0.1643` → IC=+0.126 (n=3801)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` < 0.1643 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` > `0.2785` → IC=+0.147 (n=537)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.2785 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` < `1.4416` → IC=+0.143 (n=1217)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.4416 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` > `2.4676` → IC=+0.140 (n=1216)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 2.4676 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `2612.8178` → IC=+0.192 (n=1739)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 2612.8178 (IC base=+0.125)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.133 (n=3630)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 42.0 (IC base=+0.125)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0124` → IC=+0.248 (n=2926)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0124 (IC base=+0.224)

- **PATRÓN** `drift_60min` |x|≤ `0.4644` → IC=+0.231 (n=2882)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4644 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.230 (n=3414)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.226 (n=2951)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` > `0.6667` → IC=+0.254 (n=3275)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6667 (IC base=+0.224)

- **PATRÓN** `dist_vwap_pct` > `0.1892` → IC=+0.233 (n=2006)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1892 (IC base=+0.224)

- **PATRÓN** `dist_vwap_pct` < `0.847` → IC=+0.227 (n=3391)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.847 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.436` → IC=+0.273 (n=805)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.436 (IC base=+0.224)

- **PATRÓN** `volumen_regimen` > `0.6171` → IC=+0.233 (n=3275)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6171 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` > `0.2361` → IC=+0.268 (n=609)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2361 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` > `1.4371` → IC=+0.228 (n=3198)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4371 (IC base=+0.224)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.226 (n=4211)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.224)

- **PATRÓN** `libro_liquidez` > `2622.0126` → IC=+0.229 (n=2183)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2622.0126 (IC base=+0.224)

- **PATRÓN** `sigma_h` > `0.016` → IC=+0.247 (n=2277)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.016 (IC base=+0.238)

- **PATRÓN** `drift_60min` |x|≤ `0.6212` → IC=+0.248 (n=3416)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6212 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.250 (n=1675)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.238)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.243 (n=1537)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.238)

- **PATRÓN** `ibs_20min` < `0.0388` → IC=+0.297 (n=1504)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0388 (IC base=+0.238)

- **PATRÓN** `dist_vwap_pct` > `0.3316` → IC=+0.250 (n=805)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3316 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.993` → IC=+0.272 (n=650)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.993 (IC base=+0.238)

- **PATRÓN** `volumen_regimen` < `0.8643` → IC=+0.245 (n=2278)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8643 (IC base=+0.238)

- **PATRÓN** `volumen_regimen` > `1.0479` → IC=+0.239 (n=1549)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0479 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` > `0.2881` → IC=+0.300 (n=478)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2881 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` < `2.5461` → IC=+0.235 (n=3241)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5461 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` > `1.5574` → IC=+0.239 (n=2896)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5574 (IC base=+0.238)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.204 (n=1743)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.154)

- **PATRÓN** `drift_60min` |x|≤ `0.1457` → IC=+0.169 (n=2301)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.1457 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.166 (n=5473)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.154)

- **PATRÓN** `ibs_20min` > `0.2964` → IC=+0.190 (n=5225)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.2964 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` > `0.9247` → IC=+0.179 (n=790)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.9247 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.538` → IC=+0.210 (n=839)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.538 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` < `0.8542` → IC=+0.163 (n=3181)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8542 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` > `1.1862` → IC=+0.160 (n=1590)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 1.1862 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` > `0.1553` → IC=+0.172 (n=1344)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.1553 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` < `1.5258` → IC=+0.158 (n=2245)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.5258 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` > `1.8058` → IC=+0.156 (n=3401)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.8058 (IC base=+0.154)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.157 (n=5750)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.02 (IC base=+0.154)

- **PATRÓN** `libro_liquidez` > `7284.4682` → IC=+0.192 (n=2369)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 7284.4682 (IC base=+0.154)

- **PATRÓN** `ibs_20min` < `0.1973` → IC=+0.204 (n=2527)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1973 (IC base=+0.100)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.142 (n=2530)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 22.0 (IC base=+0.100)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.211 (n=853)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.195)

- **PATRÓN** `drift_60min` |x|≤ `0.0809` → IC=+0.237 (n=427)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0809 (IC base=+0.195)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.226 (n=1160)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.195)

- **PATRÓN** `ibs_20min` > `0.6078` → IC=+0.253 (n=852)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6078 (IC base=+0.195)

- **PATRÓN** `dist_vwap_pct` > `0.699` → IC=+0.245 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.699 (IC base=+0.195)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.858` → IC=+0.230 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.858 (IC base=+0.195)

- **PATRÓN** `volumen_regimen` < `0.866` → IC=+0.212 (n=853)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.866 (IC base=+0.195)

- **PATRÓN** `volumen_pendiente_norm` > `0.0881` → IC=+0.214 (n=446)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0881 (IC base=+0.195)

- **PATRÓN** `volumen_spike_ratio` < `2.1509` → IC=+0.206 (n=1105)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1509 (IC base=+0.195)

- **PATRÓN** `volumen_spike_ratio` > `1.4016` → IC=+0.196 (n=1255)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.4016 (IC base=+0.195)

- **PATRÓN** `libro_liquidez` > `11293.6414` → IC=+0.201 (n=1142)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11293.6414 (IC base=+0.195)

- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.154 (n=535)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0032 (IC base=+0.071)

- **PATRÓN** `ibs_20min` < `0.2184` → IC=+0.186 (n=706)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.2184 (IC base=+0.071)

- **PATRÓN** `ballena_activa_n` < `165.0` → IC=+0.169 (n=695)

  - _Acción_: Kelly boost +0.84€ cuando `ballena_activa_n` < 165.0 (IC base=+0.071)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.241 (n=538)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0038 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.1349` → IC=+0.157 (n=709)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.1349 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.162 (n=1672)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` > `0.7632` → IC=+0.258 (n=729)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7632 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` > `0.1582` → IC=+0.166 (n=761)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1582 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.035` → IC=+0.187 (n=228)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 10.035 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `0.8293` → IC=+0.154 (n=1072)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.8293 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` > `0.2687` → IC=+0.190 (n=217)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.2687 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `1.7708` → IC=+0.158 (n=1057)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.7708 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `7831.4295` → IC=+0.174 (n=729)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 7831.4295 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `30.0` → IC=+0.143 (n=530)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 30.0 (IC base=+0.144)

- **PATRÓN** `sigma_h` < `0.0082` → IC=+0.122 (n=1605)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0082 (IC base=+0.107)

- **PATRÓN** `ibs_20min` < `0.1818` → IC=+0.208 (n=706)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1818 (IC base=+0.107)

- **PATRÓN** `volumen_regimen` < `0.6746` → IC=+0.136 (n=706)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.6746 (IC base=+0.107)

- **PATRÓN** `volumen_pendiente_norm` > `0.2228` → IC=+0.129 (n=273)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` > 0.2228 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `7750.0884` → IC=+0.160 (n=728)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 7750.0884 (IC base=+0.107)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.147 (n=687)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 40.0 (IC base=+0.107)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` < `0.0073` → IC=+0.150 (n=470)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0073 (IC base=+0.120)

- **PATRÓN** `sigma_h` > `0.0129` → IC=+0.134 (n=471)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` > 0.0129 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.140 (n=1410)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 6.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` > `0.5338` → IC=+0.190 (n=1256)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.5338 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` > `1.0624` → IC=+0.148 (n=248)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 1.0624 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.876` → IC=+0.214 (n=526)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.876 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` < `1.0426` → IC=+0.130 (n=1237)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.0426 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` > `0.7012` → IC=+0.126 (n=1256)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` > 0.7012 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` > `0.2222` → IC=+0.146 (n=241)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` > 0.2222 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` < `1.4182` → IC=+0.148 (n=455)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.4182 (IC base=+0.120)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.122 (n=1423)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.02 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `3054.254` → IC=+0.150 (n=469)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 3054.254 (IC base=+0.120)

- **PATRÓN** `ballena_activa_n` < `10.0` → IC=+0.130 (n=465)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 10.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` < `0.5676` → IC=+0.165 (n=1376)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` < 0.5676 (IC base=+0.082)

- **PATRÓN** `libro_liquidez` > `2758.4626` → IC=+0.165 (n=709)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2758.4626 (IC base=+0.082)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0146` → IC=+0.236 (n=320)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0146 (IC base=+0.173)

- **PATRÓN** `drift_60min` |x|≤ `0.3166` → IC=+0.175 (n=321)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.3166 (IC base=+0.173)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.217 (n=224)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.173)

- **PATRÓN** `ibs_20min` < `0.8448` → IC=+0.173 (n=423)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.8448 (IC base=+0.173)

- **PATRÓN** `ibs_20min` > `0.3805` → IC=+0.187 (n=480)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.3805 (IC base=+0.173)

- **PATRÓN** `dist_vwap_pct` > `0.2422` → IC=+0.188 (n=229)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.2422 (IC base=+0.173)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.534` → IC=+0.188 (n=482)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` < 5.534 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` > `1.1972` → IC=+0.253 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1972 (IC base=+0.173)

- **PATRÓN** `volumen_pendiente_norm` < `0.1739` → IC=+0.182 (n=479)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` < 0.1739 (IC base=+0.173)

- **PATRÓN** `volumen_pendiente_norm` > `0.0806` → IC=+0.191 (n=176)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.0806 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` < `2.5077` → IC=+0.193 (n=451)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 2.5077 (IC base=+0.173)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.190 (n=485)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.03 (IC base=+0.173)

- **PATRÓN** `libro_liquidez` > `2678.1143` → IC=+0.199 (n=320)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 2678.1143 (IC base=+0.173)

- **PATRÓN** `sigma_h` > `0.0105` → IC=+0.177 (n=537)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` > 0.0105 (IC base=+0.163)

- **PATRÓN** `drift_60min` |x|≤ `0.5762` → IC=+0.169 (n=472)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.5762 (IC base=+0.163)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.214 (n=180)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.163)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.174 (n=474)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.5 (IC base=+0.163)

- **PATRÓN** `ibs_20min` > `0.1848` → IC=+0.168 (n=480)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` > 0.1848 (IC base=+0.163)

- **PATRÓN** `dist_vwap_pct` > `1.2297` → IC=+0.300 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2297 (IC base=+0.163)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.028` → IC=+0.165 (n=521)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` < 3.028 (IC base=+0.163)

- **PATRÓN** `volumen_regimen` < `0.8755` → IC=+0.200 (n=358)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8755 (IC base=+0.163)

- **PATRÓN** `volumen_pendiente_norm` < `0.1149` → IC=+0.179 (n=503)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` < 0.1149 (IC base=+0.163)

- **PATRÓN** `volumen_pendiente_norm` > `0.2409` → IC=+0.198 (n=94)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2409 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` < `1.4975` → IC=+0.214 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4975 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` > `2.6655` → IC=+0.180 (n=173)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 2.6655 (IC base=+0.163)

- **PATRÓN** `libro_liquidez` > `2230.8308` → IC=+0.166 (n=480)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2230.8308 (IC base=+0.163)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.177 (n=460)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 15.0 (IC base=+0.163)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.013` → IC=+0.226 (n=8761)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.013 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.191 (n=27472)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` > `0.9655` → IC=+0.299 (n=8757)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9655 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` > `0.9637` → IC=+0.216 (n=3014)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9637 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.865` → IC=+0.260 (n=6422)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.865 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` < `0.8666` → IC=+0.162 (n=11806)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8666 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.2922` → IC=+0.216 (n=3435)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2922 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `2.6274` → IC=+0.193 (n=8558)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.6274 (IC base=+0.180)

- **PATRÓN** `libro_liquidez` > `1766.5` → IC=+0.181 (n=26252)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 1766.5 (IC base=+0.180)

- **PATRÓN** `ballena_activa_n` < `99.0` → IC=+0.199 (n=24875)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 99.0 (IC base=+0.180)

- **PATRÓN** `sigma_h` > `0.0126` → IC=+0.207 (n=8165)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0126 (IC base=+0.199)

- **PATRÓN** `drift_60min` |x|≤ `0.1141` → IC=+0.203 (n=8150)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1141 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.216 (n=9135)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.199)

- **PATRÓN** `ibs_20min` < `0.4893` → IC=+0.251 (n=21516)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4893 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` < `0.1949` → IC=+0.182 (n=15653)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` < 0.1949 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.498` → IC=+0.204 (n=22807)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.498 (IC base=+0.199)

- **PATRÓN** `volumen_regimen` < `0.6265` → IC=+0.181 (n=5462)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 0.6265 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` > `0.2937` → IC=+0.254 (n=3359)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2937 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` > `2.6273` → IC=+0.211 (n=7849)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6273 (IC base=+0.199)

- **PATRÓN** `ballena_activa_n` < `58.0` → IC=+0.220 (n=20609)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 58.0 (IC base=+0.199)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `drift_60min` |x|≤ `0.3091` → IC=+0.235 (n=3683)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3091 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.239 (n=4404)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.234)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.235 (n=2808)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.315 (n=1656)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.034` → IC=+0.298 (n=2752)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.034 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.2321` → IC=+0.289 (n=739)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2321 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.2808` → IC=+0.241 (n=1838)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2808 (IC base=+0.234)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.246 (n=4377)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `2058.72` → IC=+0.236 (n=1395)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2058.72 (IC base=+0.234)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.268 (n=1284)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0056 (IC base=+0.264)

- **PATRÓN** `drift_60min` |x|≤ `0.1298` → IC=+0.290 (n=1692)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1298 (IC base=+0.264)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.265 (n=3992)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.264)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.266 (n=3465)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.264)

- **PATRÓN** `ibs_20min` < `0.4699` → IC=+0.285 (n=3381)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4699 (IC base=+0.264)

- **PATRÓN** `volumen_pendiente_norm` < `0.1623` → IC=+0.265 (n=3892)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1623 (IC base=+0.264)

- **PATRÓN** `volumen_pendiente_norm` > `0.2911` → IC=+0.286 (n=536)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2911 (IC base=+0.264)

- **PATRÓN** `volumen_spike_ratio` < `1.5664` → IC=+0.266 (n=1630)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5664 (IC base=+0.264)

- **PATRÓN** `volumen_spike_ratio` > `2.6442` → IC=+0.272 (n=1235)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6442 (IC base=+0.264)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.270 (n=2553)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.264)

- **PATRÓN** `ballena_activa_n` < `6.0` → IC=+0.269 (n=1261)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 6.0 (IC base=+0.264)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.173 (n=1443)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0034 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.0843` → IC=+0.147 (n=1442)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.0843 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.152 (n=4511)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 5.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` > `0.1872` → IC=+0.187 (n=4320)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.1872 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.745` → IC=+0.212 (n=734)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.745 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.01` → IC=+0.174 (n=676)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 11.01 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `0.6328` → IC=+0.156 (n=1441)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.6328 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` > `1.2209` → IC=+0.141 (n=1440)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 1.2209 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.2716` → IC=+0.189 (n=600)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.2716 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `2.1654` → IC=+0.143 (n=3742)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.1654 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `1.5193` → IC=+0.145 (n=3798)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.5193 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `351.0` → IC=+0.148 (n=3698)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 351.0 (IC base=+0.139)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.168 (n=3370)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0062 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.0844` → IC=+0.173 (n=1276)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.0844 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.169 (n=1412)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` < `0.6829` → IC=+0.191 (n=3823)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.6829 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` < `0.1577` → IC=+0.163 (n=3762)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.1577 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.001` → IC=+0.148 (n=1800)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 3.001 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.19` → IC=+0.150 (n=3905)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 6.19 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` < `1.0418` → IC=+0.156 (n=3365)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.0418 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` > `0.2217` → IC=+0.199 (n=698)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2217 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `2.4323` → IC=+0.150 (n=3712)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.4323 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` > `1.7752` → IC=+0.153 (n=2474)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.7752 (IC base=+0.147)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.148 (n=4964)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.147)

- **PATRÓN** `ballena_activa_n` < `212.0` → IC=+0.180 (n=1228)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 212.0 (IC base=+0.147)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0122` → IC=+0.240 (n=1986)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0122 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.234 (n=4593)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.296 (n=1612)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.897` → IC=+0.314 (n=971)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.897 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` > `0.2047` → IC=+0.233 (n=1156)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2047 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` > `1.7675` → IC=+0.231 (n=3823)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7675 (IC base=+0.224)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.229 (n=5185)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.224)

- **PATRÓN** `libro_liquidez` > `1902.2979` → IC=+0.237 (n=1980)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1902.2979 (IC base=+0.224)

- **PATRÓN** `sigma_h` < `0.0083` → IC=+0.249 (n=1864)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0083 (IC base=+0.243)

- **PATRÓN** `drift_60min` |x|≤ `0.1865` → IC=+0.260 (n=1861)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1865 (IC base=+0.243)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.262 (n=1601)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.243)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.247 (n=1931)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.243)

- **PATRÓN** `ibs_20min` < `0.0695` → IC=+0.295 (n=1409)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0695 (IC base=+0.243)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.881` → IC=+0.305 (n=440)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.881 (IC base=+0.243)

- **PATRÓN** `volumen_pendiente_norm` > `0.3457` → IC=+0.296 (n=636)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3457 (IC base=+0.243)

- **PATRÓN** `volumen_spike_ratio` > `2.1676` → IC=+0.256 (n=2730)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1676 (IC base=+0.243)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.249 (n=1985)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.243)

- **PATRÓN** `libro_liquidez` > `1998.1898` → IC=+0.252 (n=1409)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1998.1898 (IC base=+0.243)

- **PATRÓN** `ballena_activa_n` < `26.0` → IC=+0.246 (n=4052)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 26.0 (IC base=+0.243)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.190 (n=1515)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.004 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.3595` → IC=+0.148 (n=3993)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.3595 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.152 (n=4723)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 5.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` > `0.8747` → IC=+0.263 (n=1515)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8747 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.1528` → IC=+0.169 (n=2227)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.1528 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.181` → IC=+0.167 (n=903)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 9.181 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `0.8567` → IC=+0.154 (n=3025)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.8567 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.2322` → IC=+0.197 (n=797)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2322 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `1.5159` → IC=+0.154 (n=1953)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 1.5159 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `2.1479` → IC=+0.142 (n=2012)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 2.1479 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `5904.382` → IC=+0.230 (n=2057)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5904.382 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `85.0` → IC=+0.142 (n=2959)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 85.0 (IC base=+0.139)

- **PATRÓN** `sigma_h` < `0.0083` → IC=+0.169 (n=3853)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0083 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.4668` → IC=+0.162 (n=3850)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.4668 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.174 (n=1418)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 17.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` < `0.5731` → IC=+0.212 (n=3388)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5731 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` < `0.6479` → IC=+0.157 (n=4461)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.6479 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.043` → IC=+0.156 (n=769)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 9.043 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.029` → IC=+0.153 (n=3355)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` < 3.029 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` < `0.8504` → IC=+0.161 (n=2567)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8504 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.2896` → IC=+0.206 (n=495)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2896 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `2.4812` → IC=+0.155 (n=3733)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.4812 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` > `1.5218` → IC=+0.158 (n=3335)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.5218 (IC base=+0.151)

- **PATRÓN** `libro_liquidez` > `6725.1528` → IC=+0.214 (n=1283)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6725.1528 (IC base=+0.151)

- **PATRÓN** `ballena_activa_n` < `57.0` → IC=+0.172 (n=1276)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 57.0 (IC base=+0.151)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0133` → IC=+0.157 (n=1542)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0133 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.149 (n=3280)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 11.0 (IC base=+0.121)

- **PATRÓN** `ibs_20min` > `0.6957` → IC=+0.255 (n=3084)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6957 (IC base=+0.121)

- **PATRÓN** `dist_vwap_pct` > `0.824` → IC=+0.195 (n=1017)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.824 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.193` → IC=+0.269 (n=1180)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.193 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` < `0.8715` → IC=+0.132 (n=3083)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 0.8715 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` < `0.1015` → IC=+0.124 (n=4405)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.1015 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` > `0.2794` → IC=+0.144 (n=580)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_pendiente_norm` > 0.2794 (IC base=+0.121)

- **PATRÓN** `volumen_spike_ratio` < `2.5051` → IC=+0.125 (n=4518)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 2.5051 (IC base=+0.121)

- **PATRÓN** `libro_liquidez` > `2472.9793` → IC=+0.225 (n=2097)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2472.9793 (IC base=+0.121)

- **PATRÓN** `sigma_h` < `0.0114` → IC=+0.159 (n=3799)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0114 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.1439` → IC=+0.152 (n=1439)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.1439 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.170 (n=2043)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 15.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` < `0.5417` → IC=+0.246 (n=3804)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5417 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` < `0.23` → IC=+0.153 (n=3991)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.23 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.023` → IC=+0.161 (n=4195)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` < 3.023 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `1.193` → IC=+0.143 (n=4318)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 1.193 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.232` → IC=+0.197 (n=754)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.232 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `1.4384` → IC=+0.164 (n=1375)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.4384 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `2.4912` → IC=+0.146 (n=1375)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 2.4912 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `2652.1888` → IC=+0.224 (n=1439)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2652.1888 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.151 (n=4127)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 47.0 (IC base=+0.137)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.011` → IC=+0.255 (n=4223)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.011 (IC base=+0.235)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.241 (n=4427)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.235)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.239 (n=2821)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.235)

- **PATRÓN** `ibs_20min` > `0.9873` → IC=+0.302 (n=1410)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9873 (IC base=+0.235)

- **PATRÓN** `dist_vwap_pct` > `0.2057` → IC=+0.250 (n=2133)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2057 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.931` → IC=+0.299 (n=758)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.931 (IC base=+0.235)

- **PATRÓN** `volumen_regimen` < `1.2164` → IC=+0.235 (n=4223)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2164 (IC base=+0.235)

- **PATRÓN** `volumen_regimen` > `0.6403` → IC=+0.242 (n=4223)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6403 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` > `0.2414` → IC=+0.259 (n=731)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2414 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` > `2.5218` → IC=+0.255 (n=1380)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5218 (IC base=+0.235)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.236 (n=5412)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.235)

- **PATRÓN** `libro_liquidez` > `2994.8704` → IC=+0.240 (n=1408)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2994.8704 (IC base=+0.235)

- **PATRÓN** `sigma_h` > `0.0247` → IC=+0.272 (n=1466)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0247 (IC base=+0.245)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.251 (n=4137)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.245)

- **PATRÓN** `ibs_20min` < `0.14` → IC=+0.304 (n=1940)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.14 (IC base=+0.245)

- **PATRÓN** `dist_vwap_pct` > `1.2048` → IC=+0.249 (n=549)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2048 (IC base=+0.245)

- **PATRÓN** `dist_vwap_pct` < `0.2337` → IC=+0.249 (n=4240)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2337 (IC base=+0.245)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.929` → IC=+0.280 (n=816)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.929 (IC base=+0.245)

- **PATRÓN** `volumen_regimen` < `0.6362` → IC=+0.249 (n=1466)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6362 (IC base=+0.245)

- **PATRÓN** `volumen_regimen` > `1.2196` → IC=+0.266 (n=1465)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2196 (IC base=+0.245)

- **PATRÓN** `volumen_pendiente_norm` > `0.2882` → IC=+0.311 (n=601)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2882 (IC base=+0.245)

- **PATRÓN** `volumen_spike_ratio` > `1.4352` → IC=+0.249 (n=4177)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4352 (IC base=+0.245)

- **PATRÓN** `ballena_activa_n` < `26.0` → IC=+0.245 (n=3628)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 26.0 (IC base=+0.245)

### GBM_LATE_5M
- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.241 (n=2484)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0054 (IC base=+0.226)

- **PATRÓN** `drift_60min` |x|≤ `0.5416` → IC=+0.233 (n=7451)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5416 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.234 (n=7481)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.226)

- **PATRÓN** `ibs_20min` > `0.9282` → IC=+0.259 (n=2484)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9282 (IC base=+0.226)

- **PATRÓN** `dist_vwap_pct` < `0.9724` → IC=+0.228 (n=6112)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.9724 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.437` → IC=+0.235 (n=2484)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.437 (IC base=+0.226)

- **PATRÓN** `volumen_regimen` < `0.7051` → IC=+0.231 (n=2328)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7051 (IC base=+0.226)

- **PATRÓN** `volumen_regimen` > `0.8782` → IC=+0.228 (n=3527)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8782 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` > `0.1639` → IC=+0.235 (n=2088)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1639 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` < `1.449` → IC=+0.235 (n=2444)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.449 (IC base=+0.226)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.229 (n=5325)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.226)

- **PATRÓN** `libro_liquidez` > `3758.63` → IC=+0.233 (n=4967)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3758.63 (IC base=+0.226)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.230 (n=1777)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.4187` → IC=+0.222 (n=4690)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4187 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.226 (n=1795)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.212)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.224 (n=2403)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` < `0.6151` → IC=+0.216 (n=4690)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6151 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` > `0.7199` → IC=+0.217 (n=914)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7199 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` < `0.2586` → IC=+0.204 (n=4697)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2586 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.681` → IC=+0.225 (n=4843)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.681 (IC base=+0.212)

- **PATRÓN** `volumen_regimen` < `1.2534` → IC=+0.211 (n=4835)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2534 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` < `0.0983` → IC=+0.215 (n=4929)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0983 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` < `1.5329` → IC=+0.216 (n=2311)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5329 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `1.8176` → IC=+0.218 (n=3499)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8176 (IC base=+0.212)

- **PATRÓN** `ballena_activa_n` < `50.0` → IC=+0.237 (n=3514)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 50.0 (IC base=+0.212)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.278 (n=841)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0059 (IC base=+0.273)

- **PATRÓN** `drift_60min` |x|≤ `0.0857` → IC=+0.304 (n=319)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0857 (IC base=+0.273)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.282 (n=957)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.273)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.272 (n=960)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.273)

- **PATRÓN** `ibs_20min` < `0.4706` → IC=+0.287 (n=638)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4706 (IC base=+0.273)

- **PATRÓN** `dist_vwap_pct` < `0.3337` → IC=+0.284 (n=974)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3337 (IC base=+0.273)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.122` → IC=+0.298 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.122 (IC base=+0.273)

- **PATRÓN** `volumen_regimen` < `1.2269` → IC=+0.278 (n=956)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2269 (IC base=+0.273)

- **PATRÓN** `volumen_regimen` > `0.8786` → IC=+0.293 (n=637)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8786 (IC base=+0.273)

- **PATRÓN** `volumen_pendiente_norm` > `0.2862` → IC=+0.341 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2862 (IC base=+0.273)

- **PATRÓN** `volumen_spike_ratio` < `2.4917` → IC=+0.281 (n=951)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4917 (IC base=+0.273)

- **PATRÓN** `libro_liquidez` > `12917.6999` → IC=+0.284 (n=637)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12917.6999 (IC base=+0.273)

- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.260 (n=519)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0032 (IC base=+0.171)

- **PATRÓN** `drift_60min` |x|≤ `0.3891` → IC=+0.187 (n=1549)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.3891 (IC base=+0.171)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.213 (n=569)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.171)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.175 (n=582)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 5.0 (IC base=+0.171)

- **PATRÓN** `ibs_20min` < `0.1382` → IC=+0.192 (n=683)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.1382 (IC base=+0.171)

- **PATRÓN** `dist_vwap_pct` > `0.3612` → IC=+0.175 (n=333)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.3612 (IC base=+0.171)

- **PATRÓN** `dist_vwap_pct` < `0.5564` → IC=+0.172 (n=1857)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` < 0.5564 (IC base=+0.171)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.334` → IC=+0.193 (n=1521)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` < 6.334 (IC base=+0.171)

- **PATRÓN** `volumen_regimen` < `1.091` → IC=+0.185 (n=1363)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 1.091 (IC base=+0.171)

- **PATRÓN** `volumen_pendiente_norm` > `0.1519` → IC=+0.187 (n=474)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.1519 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` < `2.4957` → IC=+0.177 (n=1540)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 2.4957 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` > `1.8072` → IC=+0.174 (n=1027)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 1.8072 (IC base=+0.171)

- **PATRÓN** `libro_liquidez` > `14629.5629` → IC=+0.172 (n=702)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 14629.5629 (IC base=+0.171)

- **PATRÓN** `ballena_activa_n` < `701.0` → IC=+0.187 (n=1503)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 701.0 (IC base=+0.171)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `drift_60min` |x|≤ `0.6134` → IC=+0.217 (n=1086)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6134 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.230 (n=983)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` < `0.7107` → IC=+0.218 (n=724)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7107 (IC base=+0.211)

- **PATRÓN** `ibs_20min` > `0.988` → IC=+0.253 (n=362)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.988 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.256` → IC=+0.247 (n=398)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.256 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.2053` → IC=+0.248 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2053 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `1.7957` → IC=+0.218 (n=967)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7957 (IC base=+0.211)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.221 (n=968)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.211)

- **PATRÓN** `sigma_h` > `0.0144` → IC=+0.343 (n=49)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0144 (IC base=+0.288)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.312 (n=110)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 3.0 (IC base=+0.288)

- **PATRÓN** `ibs_20min` < `0.4444` → IC=+0.300 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4444 (IC base=+0.288)

- **PATRÓN** `ibs_20min` > `0.1912` → IC=+0.300 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1912 (IC base=+0.288)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.025` → IC=+0.364 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.025 (IC base=+0.288)

- **PATRÓN** `volumen_pendiente_norm` < `0.1188` → IC=+0.327 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1188 (IC base=+0.288)

- **PATRÓN** `volumen_spike_ratio` < `2.3165` → IC=+0.311 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.3165 (IC base=+0.288)

- **PATRÓN** `volumen_spike_ratio` > `1.8484` → IC=+0.296 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8484 (IC base=+0.288)

- **PATRÓN** `libro_liquidez` > `3226.1026` → IC=+0.363 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3226.1026 (IC base=+0.288)

- **PATRÓN** `ballena_activa_n` < `5.0` → IC=+0.368 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 5.0 (IC base=+0.288)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.0076` → IC=+0.223 (n=1808)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0076 (IC base=+0.214)

- **PATRÓN** `drift_60min` |x|≤ `0.4747` → IC=+0.220 (n=2055)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4747 (IC base=+0.214)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.241 (n=717)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.214)

- **PATRÓN** `ibs_20min` < `0.4688` → IC=+0.230 (n=1370)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4688 (IC base=+0.214)

- **PATRÓN** `ibs_20min` > `0.8316` → IC=+0.218 (n=685)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8316 (IC base=+0.214)

- **PATRÓN** `dist_vwap_pct` < `0.4277` → IC=+0.226 (n=2065)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4277 (IC base=+0.214)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.931` → IC=+0.222 (n=1866)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.931 (IC base=+0.214)

- **PATRÓN** `volumen_regimen` < `0.8657` → IC=+0.217 (n=1370)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8657 (IC base=+0.214)

- **PATRÓN** `volumen_regimen` > `1.2314` → IC=+0.221 (n=685)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2314 (IC base=+0.214)

- **PATRÓN** `volumen_pendiente_norm` < `0.0981` → IC=+0.216 (n=1907)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0981 (IC base=+0.214)

- **PATRÓN** `volumen_pendiente_norm` > `0.1592` → IC=+0.217 (n=582)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1592 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` < `1.4017` → IC=+0.231 (n=670)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4017 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` > `1.4931` → IC=+0.216 (n=1792)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4931 (IC base=+0.214)

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.245 (n=558)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0045 (IC base=+0.207)

- **PATRÓN** `drift_60min` |x|≤ `0.512` → IC=+0.220 (n=1667)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.512 (IC base=+0.207)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.217 (n=620)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.207)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.222 (n=751)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.207)

- **PATRÓN** `ibs_20min` > `0.0847` → IC=+0.214 (n=1667)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.0847 (IC base=+0.207)

- **PATRÓN** `dist_vwap_pct` > `0.7294` → IC=+0.223 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7294 (IC base=+0.207)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.241` → IC=+0.211 (n=1521)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.241 (IC base=+0.207)

- **PATRÓN** `volumen_regimen` < `1.2546` → IC=+0.214 (n=1667)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2546 (IC base=+0.207)

- **PATRÓN** `volumen_regimen` > `0.7209` → IC=+0.211 (n=1489)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7209 (IC base=+0.207)

- **PATRÓN** `volumen_pendiente_norm` > `0.0726` → IC=+0.229 (n=685)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0726 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` < `2.4721` → IC=+0.209 (n=1632)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4721 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` > `1.7713` → IC=+0.210 (n=1088)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7713 (IC base=+0.207)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.209 (n=2173)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.207)

- **PATRÓN** `ballena_activa_n` < `96.0` → IC=+0.211 (n=1659)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 96.0 (IC base=+0.207)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0105` → IC=+0.229 (n=866)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0105 (IC base=+0.218)

- **PATRÓN** `sigma_h` > `0.0135` → IC=+0.229 (n=434)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0135 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.248 (n=1162)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.218)

- **PATRÓN** `ibs_20min` > `0.9863` → IC=+0.302 (n=433)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9863 (IC base=+0.218)

- **PATRÓN** `dist_vwap_pct` > `1.1073` → IC=+0.245 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1073 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.998` → IC=+0.270 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.998 (IC base=+0.218)

- **PATRÓN** `volumen_regimen` < `0.6421` → IC=+0.249 (n=433)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6421 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` < `0.1056` → IC=+0.220 (n=1188)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1056 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` > `0.2735` → IC=+0.241 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2735 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` < `2.5042` → IC=+0.227 (n=1267)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5042 (IC base=+0.218)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.226 (n=1520)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.218)

- **PATRÓN** `libro_liquidez` > `3369.9793` → IC=+0.243 (n=1160)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3369.9793 (IC base=+0.218)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.223 (n=1127)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 34.0 (IC base=+0.218)

- **PATRÓN** `sigma_h` < `0.0141` → IC=+0.246 (n=973)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0141 (IC base=+0.246)

- **PATRÓN** `sigma_h` > `0.0108` → IC=+0.252 (n=648)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0108 (IC base=+0.246)

- **PATRÓN** `drift_60min` |x|≤ `0.6917` → IC=+0.259 (n=973)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6917 (IC base=+0.246)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.266 (n=672)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.246)

- **PATRÓN** `ibs_20min` < `0.6471` → IC=+0.272 (n=856)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6471 (IC base=+0.246)

- **PATRÓN** `dist_vwap_pct` > `0.588` → IC=+0.246 (n=340)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.588 (IC base=+0.246)

- **PATRÓN** `dist_vwap_pct` < `0.332` → IC=+0.255 (n=860)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.332 (IC base=+0.246)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.988` → IC=+0.265 (n=918)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.988 (IC base=+0.246)

- **PATRÓN** `volumen_regimen` < `0.7522` → IC=+0.263 (n=428)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7522 (IC base=+0.246)

- **PATRÓN** `volumen_pendiente_norm` < `0.104` → IC=+0.258 (n=873)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.104 (IC base=+0.246)

- **PATRÓN** `volumen_spike_ratio` > `1.8438` → IC=+0.262 (n=633)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8438 (IC base=+0.246)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.248 (n=1199)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.246)

- **PATRÓN** `libro_liquidez` > `4016.482` → IC=+0.269 (n=648)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4016.482 (IC base=+0.246)

- **PATRÓN** `ballena_activa_n` < `33.0` → IC=+0.276 (n=859)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 33.0 (IC base=+0.246)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.147 (n=947)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0043 (IC base=+0.072)

- **PATRÓN** `ibs_20min` > `0.4182` → IC=+0.136 (n=2750)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` > 0.4182 (IC base=+0.072)

- **PATRÓN** `dist_vwap_pct` > `0.1608` → IC=+0.158 (n=1275)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.1608 (IC base=+0.072)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.347` → IC=+0.144 (n=597)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 10.347 (IC base=+0.072)

- **PATRÓN** `ibs_20min` < `0.5777` → IC=+0.180 (n=2183)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.5777 (IC base=+0.097)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.539` → IC=+0.132 (n=969)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` > 2.539 (IC base=+0.097)

- **PATRÓN** `volumen_pendiente_norm` > `0.152` → IC=+0.187 (n=618)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.152 (IC base=+0.097)

- **PATRÓN** `volumen_spike_ratio` < `2.1572` → IC=+0.122 (n=1848)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` < 2.1572 (IC base=+0.097)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `ibs_20min` < `0.5515` → IC=-0.120 (n=343)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5515
  - _Potencial_: sin este filtro IC_bueno=+0.157 (n=698)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.121 (n=715)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.60€ cuando `sigma_h` < 0.0057 (IC base=+0.066)

- **PATRÓN** `ibs_20min` > `0.5515` → IC=+0.157 (n=698)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` > 0.5515 (IC base=+0.066)

- **PATRÓN** `dist_vwap_pct` > `0.1288` → IC=+0.166 (n=363)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1288 (IC base=+0.066)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.121 (n=333)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.60€ cuando `sigma_h` < 0.0037 (IC base=+0.056)

- **PATRÓN** `ibs_20min` < `0.0617` → IC=+0.248 (n=323)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0617 (IC base=+0.056)

- **PATRÓN** `volumen_pendiente_norm` > `0.071` → IC=+0.143 (n=323)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_pendiente_norm` > 0.071 (IC base=+0.056)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` > `0.4872` → IC=-0.127 (n=269)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4872
  - _Potencial_: sin este filtro IC_bueno=+0.155 (n=523)

- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.158 (n=372)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0044 (IC base=+0.063)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.122 (n=424)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 15.0 (IC base=+0.063)

- **PATRÓN** `ibs_20min` > `0.5274` → IC=+0.157 (n=727)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` > 0.5274 (IC base=+0.063)

- **PATRÓN** `dist_vwap_pct` > `0.191` → IC=+0.158 (n=349)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.191 (IC base=+0.063)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.029` → IC=+0.172 (n=178)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 12.029 (IC base=+0.063)

- **PATRÓN** `ibs_20min` < `0.3174` → IC=+0.224 (n=397)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3174 (IC base=+0.046)

### GBM_LATE_60M#SOL#60min
- **PATRÓN** `ibs_20min` > `0.981` → IC=+0.196 (n=310)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.981 (IC base=+0.038)

- **PATRÓN** `dist_vwap_pct` > `0.7761` → IC=+0.161 (n=222)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.7761 (IC base=+0.038)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.178 (n=421)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0103 (IC base=+0.101)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.196 (n=604)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.5 (IC base=+0.101)

- **PATRÓN** `dist_vwap_pct` < `0.2289` → IC=+0.153 (n=601)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.2289 (IC base=+0.101)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.159` → IC=+0.240 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.159 (IC base=+0.101)

- **PATRÓN** `volumen_regimen` > `1.1218` → IC=+0.188 (n=200)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` > 1.1218 (IC base=+0.101)

- **PATRÓN** `volumen_pendiente_norm` > `0.1608` → IC=+0.188 (n=155)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.1608 (IC base=+0.101)

- **PATRÓN** `volumen_spike_ratio` > `1.8705` → IC=+0.140 (n=379)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 1.8705 (IC base=+0.101)

### GBM_LATE_60M#XRP#60min
- **PATRÓN** `sigma_h` > `0.012` → IC=+0.381 (n=65)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.012 (IC base=+0.308)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.371 (n=29)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.308)

- **PATRÓN** `ibs_20min` > `0.6012` → IC=+0.340 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6012 (IC base=+0.308)

- **PATRÓN** `dist_vwap_pct` > `0.5771` → IC=+0.405 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5771 (IC base=+0.308)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.323` → IC=+0.323 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.323 (IC base=+0.308)

- **PATRÓN** `volumen_regimen` < `0.79` → IC=+0.304 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.79 (IC base=+0.308)

- **PATRÓN** `volumen_regimen` > `1.1852` → IC=+0.352 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1852 (IC base=+0.308)

- **PATRÓN** `volumen_pendiente_norm` > `0.0733` → IC=+0.352 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0733 (IC base=+0.308)

- **PATRÓN** `volumen_spike_ratio` < `2.3887` → IC=+0.346 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.3887 (IC base=+0.308)

- **PATRÓN** `volumen_spike_ratio` > `2.1072` → IC=+0.320 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1072 (IC base=+0.308)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.315 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.308)

- **PATRÓN** `libro_liquidez` > `559.0842` → IC=+0.315 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 559.0842 (IC base=+0.308)

- **PATRÓN** `sigma_h` < `0.0097` → IC=+0.403 (n=29)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0097 (IC base=+0.346)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.411 (n=43)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.346)

- **PATRÓN** `ibs_20min` < `0.1158` → IC=+0.375 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1158 (IC base=+0.346)

- **PATRÓN** `ibs_20min` > `0.4553` → IC=+0.371 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4553 (IC base=+0.346)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.59` → IC=+0.462 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.59 (IC base=+0.346)

- **PATRÓN** `volumen_regimen` > `0.6174` → IC=+0.388 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6174 (IC base=+0.346)

- **PATRÓN** `volumen_pendiente_norm` > `0.0734` → IC=+0.409 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0734 (IC base=+0.346)

- **PATRÓN** `volumen_spike_ratio` < `1.5212` → IC=+0.397 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5212 (IC base=+0.346)

- **PATRÓN** `volumen_spike_ratio` > `3.0999` → IC=+0.400 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.0999 (IC base=+0.346)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.385 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.346)

- **PATRÓN** `libro_liquidez` > `34.75` → IC=+0.354 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 34.75 (IC base=+0.346)

### GBM_LATE_60M_FADE
- **FILTRO** `sigma_h` < `0.0062` → IC=-0.251 (n=211)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0062
  - _Potencial_: sin este filtro IC_bueno=-0.206 (n=212)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.310 (n=98)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=325)

- **FILTRO** `volumen_regimen` < `0.8808` → IC=-0.307 (n=138)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.8808
  - _Potencial_: sin este filtro IC_bueno=-0.189 (n=281)

- **FILTRO** `sigma_h` < `0.0062` → IC=-0.289 (n=254)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0062
  - _Potencial_: sin este filtro IC_bueno=-0.204 (n=133)

- **FILTRO** `dist_vwap_pct` > `0.4704` → IC=-0.450 (n=18)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4704
  - _Potencial_: sin este filtro IC_bueno=-0.260 (n=352)

- **FILTRO** `sigma_ewma_delta_pct` > `9.288` → IC=-0.281 (n=30)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 9.288
  - _Potencial_: sin este filtro IC_bueno=-0.258 (n=357)

- **FILTRO** `volumen_pendiente_norm` > `0.046` → IC=-0.375 (n=30)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.046
  - _Potencial_: sin este filtro IC_bueno=-0.242 (n=262)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `sigma_h` < `0.0069` → IC=-0.253 (n=99)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0069
  - _Potencial_: sin este filtro IC_bueno=-0.243 (n=33)

- **FILTRO** `hora_utc` > `9.0` → IC=-0.312 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.231 (n=102)

- **FILTRO** `ibs_20min` < `0.0328` → IC=-0.300 (n=33)

  - _Acción_: SKIP cuando `ibs_20min` < 0.0328
  - _Potencial_: sin este filtro IC_bueno=-0.233 (n=99)

- **FILTRO** `drift_60min` |x|> `0.132` → IC=-0.327 (n=50)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.132
  - _Potencial_: sin este filtro IC_bueno=-0.206 (n=100)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `sigma_h` < `0.003` → IC=-0.250 (n=34)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.003
  - _Potencial_: sin este filtro IC_bueno=-0.148 (n=103)

- **FILTRO** `hora_utc` < `2.0` → IC=-0.179 (n=26)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 2.0
  - _Potencial_: sin este filtro IC_bueno=-0.173 (n=111)

- **FILTRO** `ibs_20min` < `0.6002` → IC=-0.472 (n=34)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6002
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=103)

- **FILTRO** `volumen_regimen` < `0.7594` → IC=-0.250 (n=34)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7594
  - _Potencial_: sin este filtro IC_bueno=-0.148 (n=103)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.372 (n=37)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.276 (n=105)

- **FILTRO** `volumen_spike_ratio` < `1.8092` → IC=-0.354 (n=53)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.8092
  - _Potencial_: sin este filtro IC_bueno=-0.268 (n=54)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.298 (n=127)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `sigma_h` < `0.0112` → IC=-0.290 (n=98)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0112
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=52)

- **FILTRO** `drift_60min` |x|> `0.2366` → IC=-0.346 (n=37)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2366
  - _Potencial_: sin este filtro IC_bueno=-0.210 (n=112)

- **FILTRO** `hora_utc` > `12.0` → IC=-0.342 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=55)

- **FILTRO** `volumen_regimen` < `0.9252` → IC=-0.460 (n=23)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9252
  - _Potencial_: sin este filtro IC_bueno=-0.108 (n=49)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` > `0.25` → IC=-0.152 (n=349)

  - _Acción_: SKIP cuando `ibs_20min` > 0.25
  - _Potencial_: sin este filtro IC_bueno=+0.085 (n=1050)

- **PATRÓN** `sigma_h` > `0.0103` → IC=+0.261 (n=307)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0103 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.204 (n=417)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.164)

- **PATRÓN** `ibs_20min` > `0.6852` → IC=+0.200 (n=915)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6852 (IC base=+0.164)

- **PATRÓN** `dist_vwap_pct` > `0.9045` → IC=+0.310 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9045 (IC base=+0.164)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.379` → IC=+0.188 (n=219)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 10.379 (IC base=+0.164)

- **PATRÓN** `volumen_regimen` < `0.6243` → IC=+0.191 (n=299)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 0.6243 (IC base=+0.164)

- **PATRÓN** `volumen_regimen` > `1.1982` → IC=+0.173 (n=298)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` > 1.1982 (IC base=+0.164)

- **PATRÓN** `volumen_pendiente_norm` < `0.0683` → IC=+0.186 (n=696)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` < 0.0683 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` < `1.4073` → IC=+0.208 (n=269)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4073 (IC base=+0.164)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.140 (n=84)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` > 0.0068 (IC base=+0.066)

- **PATRÓN** `ibs_20min` > `0.7306` → IC=+0.136 (n=251)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` > 0.7306 (IC base=+0.066)

- **PATRÓN** `dist_vwap_pct` > `0.3329` → IC=+0.216 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3329 (IC base=+0.066)

- **PATRÓN** `ibs_20min` < `0.2563` → IC=+0.134 (n=463)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` < 0.2563 (IC base=+0.074)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **PATRÓN** `sigma_h` > `0.0073` → IC=+0.163 (n=90)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` > 0.0073 (IC base=+0.131)

- **PATRÓN** `drift_60min` |x|≤ `0.1196` → IC=+0.136 (n=119)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.68€ cuando `drift_60min` |x|≤ 0.1196 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.163 (n=99)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 18.0 (IC base=+0.131)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.136 (n=97)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 6.0 (IC base=+0.131)

- **PATRÓN** `ibs_20min` > `0.8015` → IC=+0.175 (n=241)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` > 0.8015 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` > `0.8305` → IC=+0.189 (n=43)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.8305 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` < `0.1137` → IC=+0.153 (n=217)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.1137 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.26` → IC=+0.131 (n=63)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` > 11.26 (IC base=+0.131)

- **PATRÓN** `volumen_regimen` < `0.6229` → IC=+0.185 (n=90)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 0.6229 (IC base=+0.131)

- **PATRÓN** `volumen_regimen` > `1.1834` → IC=+0.163 (n=90)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 1.1834 (IC base=+0.131)

- **PATRÓN** `volumen_pendiente_norm` < `0.052` → IC=+0.184 (n=223)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` < 0.052 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` < `1.7116` → IC=+0.175 (n=161)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 1.7116 (IC base=+0.131)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.142 (n=224)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `1704.1785` → IC=+0.175 (n=269)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 1704.1785 (IC base=+0.131)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.0667` → IC=-0.239 (n=117)

  - _Acción_: SKIP cuando `ibs_20min` > 0.0667
  - _Potencial_: sin este filtro IC_bueno=+0.087 (n=119)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.291 (n=343)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.273)

- **PATRÓN** `ibs_20min` > `0.7` → IC=+0.302 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7 (IC base=+0.273)

- **PATRÓN** `dist_vwap_pct` > `0.7967` → IC=+0.404 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7967 (IC base=+0.273)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.006` → IC=+0.356 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.006 (IC base=+0.273)

- **PATRÓN** `volumen_regimen` < `0.8033` → IC=+0.301 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8033 (IC base=+0.273)

- **PATRÓN** `volumen_pendiente_norm` < `0.2102` → IC=+0.297 (n=309)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2102 (IC base=+0.273)

- **PATRÓN** `volumen_pendiente_norm` > `0.0894` → IC=+0.316 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0894 (IC base=+0.273)

- **PATRÓN** `volumen_spike_ratio` < `1.4854` → IC=+0.324 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4854 (IC base=+0.273)

- **PATRÓN** `volumen_spike_ratio` > `2.0595` → IC=+0.312 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.0595 (IC base=+0.273)

- **PATRÓN** `libro_spread` < `0.05` → IC=+0.274 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.05 (IC base=+0.273)

### LATE_WINDOW_5MIN
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.314 (n=208)

- **PATRÓN** `drift_ventana_pct` |x|> `0.5446` → IC=+0.357 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.5446 (IC base=+0.323)

- **PATRÓN** `elapsed_s` > `209.4` → IC=+0.372 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 209.4 (IC base=+0.323)

- **PATRÓN** `drift_15min` |x|≤ `1.1328` → IC=+0.375 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.1328 (IC base=+0.323)

- **PATRÓN** `drift_60min` |x|≤ `0.6678` → IC=+0.390 (n=107)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6678 (IC base=+0.323)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.379 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.323)

- **PATRÓN** `ballena_activa_n` < `1043.0` → IC=+0.429 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1043.0 (IC base=+0.323)

- **PATRÓN** `drift_ventana_pct` |x|> `0.445` → IC=+0.314 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.445 (IC base=+0.280)

- **PATRÓN** `elapsed_s` > `232.0` → IC=+0.364 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 232.0 (IC base=+0.280)

- **PATRÓN** `drift_15min` |x|≤ `2.3607` → IC=+0.315 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3607 (IC base=+0.280)

- **PATRÓN** `drift_60min` |x|≤ `0.9975` → IC=+0.301 (n=149)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9975 (IC base=+0.280)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.314 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.280)

- **PATRÓN** `ballena_activa_n` < `1717.0` → IC=+0.325 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1717.0 (IC base=+0.280)

### LATE_WINDOW_5MIN#BTC#5min
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.314 (n=208)

- **PATRÓN** `drift_ventana_pct` |x|> `0.5446` → IC=+0.357 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.5446 (IC base=+0.323)

- **PATRÓN** `elapsed_s` > `209.4` → IC=+0.372 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 209.4 (IC base=+0.323)

- **PATRÓN** `drift_15min` |x|≤ `1.1328` → IC=+0.375 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.1328 (IC base=+0.323)

- **PATRÓN** `drift_60min` |x|≤ `0.6678` → IC=+0.390 (n=107)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6678 (IC base=+0.323)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.379 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.323)

- **PATRÓN** `ballena_activa_n` < `1043.0` → IC=+0.429 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1043.0 (IC base=+0.323)

- **PATRÓN** `drift_ventana_pct` |x|> `0.445` → IC=+0.314 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.445 (IC base=+0.280)

- **PATRÓN** `elapsed_s` > `232.0` → IC=+0.364 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 232.0 (IC base=+0.280)

- **PATRÓN** `drift_15min` |x|≤ `2.3607` → IC=+0.315 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3607 (IC base=+0.280)

- **PATRÓN** `drift_60min` |x|≤ `0.9975` → IC=+0.301 (n=149)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9975 (IC base=+0.280)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.314 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.280)

- **PATRÓN** `ballena_activa_n` < `1717.0` → IC=+0.325 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1717.0 (IC base=+0.280)

### LIQUIDACIONES_15M
- **FILTRO** `py_entrada` < `0.415` → IC=-0.171 (n=71)

  - _Acción_: SKIP cuando `py_entrada` < 0.415
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=239)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=294)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=1616)

### LIQUIDACIONES_15M#BNB#15min
- **PATRÓN** `liq_n` > `2.0` → IC=+0.184 (n=93)

  - _Acción_: Kelly boost +0.92€ cuando `liq_n` > 2.0 (IC base=+0.102)

- **PATRÓN** `liq_usd_total` > `100.7` → IC=+0.139 (n=189)

  - _Acción_: Kelly boost +0.69€ cuando `liq_usd_total` > 100.7 (IC base=+0.102)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.147 (n=100)

  - _Acción_: Kelly boost +0.74€ cuando `py_entrada` > 0.5 (IC base=+0.102)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.135 (n=102)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.03 (IC base=+0.102)

### LIQUIDACIONES_15M#DOGE#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.111 (n=129)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.137 (n=111)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 10.0 (IC base=+0.082)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `liq_usd_total` < `1211.34` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_usd_total` < 1211.34
  - _Potencial_: sin este filtro IC_bueno=-0.104 (n=46)

- **FILTRO** `hora_utc` < `15.0` → IC=-0.188 (n=30)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=31)

- **FILTRO** `py_entrada` < `0.425` → IC=-0.309 (n=19)

  - _Acción_: SKIP cuando `py_entrada` < 0.425
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=42)

### LIQUIDACIONES_15M#SOL#15min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=27)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=286)

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
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=4296)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=266)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.118 (n=223)

- **FILTRO** `ballena_activa_n` > `39.0` → IC=-0.178 (n=85)

  - _Acción_: SKIP cuando `ballena_activa_n` > 39.0
  - _Potencial_: sin este filtro IC_bueno=+0.188 (n=168)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.121 (n=159)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` < 0.5 (IC base=+0.029)

- **PATRÓN** `ballena_activa_n` < `39.0` → IC=+0.188 (n=168)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 39.0 (IC base=+0.029)

### LIQUIDACIONES_5M#BTC#5min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.167 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=15)

- **FILTRO** `libro_liquidez` < `13988.6712` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `libro_liquidez` < 13988.6712
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=19)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.136 (n=297)

  - _Acción_: Kelly boost +0.68€ cuando `py_entrada` < 0.495 (IC base=+0.024)

### LIQUIDACIONES_5M#DOGE#5min
- **PATRÓN** `liq_n` > `3.0` → IC=+0.333 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `liq_n` > 3.0 (IC base=+0.192)

- **PATRÓN** `liq_usd_total` > `701.27` → IC=+0.267 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `liq_usd_total` > 701.27 (IC base=+0.192)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.239 (n=90)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 9.0 (IC base=+0.192)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.206 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.192)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=1697)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=1651)

- **FILTRO** `hora_utc` > `5.0` → IC=-0.286 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=10)

### LIQUIDACIONES_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.505` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=773)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=782)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.300 (n=18)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### LIQUIDACIONES_5M#XRP#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=591)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=572)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.138 (n=241)

  - _Acción_: Kelly boost +0.69€ cuando `py_entrada` < 0.495 (IC base=-0.001)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=1185)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=1185)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=1601)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=1601)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=373)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=373)

- **FILTRO** `py_entrada` < `0.425` → IC=-0.144 (n=85)

  - _Acción_: SKIP cuando `py_entrada` < 0.425
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=303)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.136 (n=64)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=421)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=470)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=345)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=452)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=452)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=441)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.4` → IC=-0.131 (n=3783)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=9684)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `hora_utc` > `14.0` → IC=-0.145 (n=119)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=149)

- **FILTRO** `py_entrada` > `0.58` → IC=-0.154 (n=50)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=58)

- **FILTRO** `restante_min` < `3.99` → IC=-0.127 (n=73)

  - _Acción_: SKIP cuando `restante_min` < 3.99
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=35)

- **FILTRO** `hora_utc` < `10.0` → IC=-0.214 (n=33)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=75)

### LIQUIDACIONES_DEPTH_FASE0#BTC#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.162 (n=456)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=1090)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **FILTRO** `py_entrada` > `0.6` → IC=-0.141 (n=357)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=974)

- **PATRÓN** `py_entrada` < `0.51` → IC=+0.135 (n=458)

  - _Acción_: Kelly boost +0.67€ cuando `py_entrada` < 0.51 (IC base=-0.010)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.124 (n=208)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=483)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.121 (n=167)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=532)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.121 (n=765)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=821)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.137 (n=384)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=807)

### LIQUIDACIONES_DEPTH_FASE0#SOL#5min
- **FILTRO** `py_entrada` < `0.42` → IC=-0.129 (n=589)

  - _Acción_: SKIP cuando `py_entrada` < 0.42
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=742)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.123 (n=622)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=648)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.135 (n=671)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=771)

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

### MOMENTUM_IBS_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=1413)

### MOMENTUM_IBS_15M_BALLENA
- **FILTRO** `py_entrada` < `0.46` → IC=-0.178 (n=9331)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=29052)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.171 (n=9680)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=30054)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.199 (n=1732)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=5388)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.145 (n=2372)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.097 (n=4627)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.139 (n=1823)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` > 1.0 (IC base=+0.039)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.136 (n=3292)

  - _Acción_: Kelly boost +0.68€ cuando `py_entrada` < 0.5 (IC base=+0.015)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` > `0.57` → IC=-0.173 (n=1414)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=4269)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` > `0.62` → IC=-0.197 (n=1749)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.089 (n=5429)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.134 (n=2186)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` > 1.0 (IC base=+0.032)

### MOMENTUM_IBS_15M_BALLENA#ETH#15min
- **FILTRO** `ibs_20min` < `0.7645` → IC=-0.148 (n=1304)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7645
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=3918)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.181 (n=1423)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=4329)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.156 (n=1781)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=5358)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=2452)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.162 (n=772)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=2376)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.180 (n=973)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=3425)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=4377)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` < `14.0` → IC=-0.157 (n=135)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=437)

- **FILTRO** `hora_utc` > `20.0` → IC=-0.146 (n=125)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 20.0
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=447)

### MOMENTUM_IBS_15M_FADE#DOGE#15min
- **FILTRO** `ibs_20min` > `0.7158` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7158
  - _Potencial_: sin este filtro IC_bueno=+0.080 (n=48)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `py_entrada` < `0.395` → IC=-0.230 (n=72)

  - _Acción_: SKIP cuando `py_entrada` < 0.395
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=262)

- **FILTRO** `ibs_20min` < `0.1975` → IC=-0.223 (n=110)

  - _Acción_: SKIP cuando `ibs_20min` < 0.1975
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=224)

- **FILTRO** `libro_liquidez` < `3613.7014` → IC=-0.152 (n=110)

  - _Acción_: SKIP cuando `libro_liquidez` < 3613.7014
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=224)

- **FILTRO** `hora_utc` < `7.0` → IC=-0.204 (n=113)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.095 (n=378)

- **FILTRO** `drift_20min_pct` |x|> `0.1999` → IC=-0.129 (n=122)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.1999
  - _Potencial_: sin este filtro IC_bueno=-0.117 (n=369)

- **FILTRO** `libro_liquidez` < `3258.6483` → IC=-0.183 (n=162)

  - _Acción_: SKIP cuando `libro_liquidez` < 3258.6483
  - _Potencial_: sin este filtro IC_bueno=-0.089 (n=329)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.192 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=983)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.224 (n=310)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=976)

### MOMENTUM_IBS_15M_FADE#XRP#15min
- **FILTRO** `hora_utc` < `14.0` → IC=-0.141 (n=76)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=233)

### MOMENTUM_IBS_5M#BNB#5min
- **FILTRO** `hora_utc` > `17.0` → IC=-0.157 (n=33)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=45)

- **PATRÓN** `drift_7min_pct` |x|≤ `0.0331` → IC=+0.214 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `drift_7min_pct` |x|≤ 0.0331 (IC base=-0.026)

### MOMENTUM_IBS_5M#BTC#5min
- **FILTRO** `hora_utc` > `16.0` → IC=-0.175 (n=38)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=98)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.138 (n=25991)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=58935)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.302 (n=20686)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=64240)

- **FILTRO** `ibs_7min` < `0.7273` → IC=-0.225 (n=27904)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7273
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=57022)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.155 (n=27781)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=57145)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.247 (n=26288)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=79846)

- **FILTRO** `ibs_7min` > `0.2782` → IC=-0.182 (n=26525)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2782
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=79609)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.164 (n=3627)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=11593)

- **FILTRO** `py_entrada` < `0.3` → IC=-0.327 (n=3601)

  - _Acción_: SKIP cuando `py_entrada` < 0.3
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=11619)

- **FILTRO** `ibs_7min` < `0.7087` → IC=-0.257 (n=5022)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7087
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=10198)

- **FILTRO** `py_entrada` > `0.72` → IC=-0.280 (n=4447)

  - _Acción_: SKIP cuando `py_entrada` > 0.72
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=13823)

- **FILTRO** `ibs_7min` > `0.7692` → IC=-0.212 (n=4564)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7692
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=13706)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.129 (n=3417)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.104 (n=10793)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.268 (n=3480)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=10730)

- **FILTRO** `ibs_7min` < `0.7111` → IC=-0.213 (n=3552)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7111
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=10658)

- **FILTRO** `ballena_activa_n` > `157.0` → IC=-0.205 (n=3537)

  - _Acción_: SKIP cuando `ballena_activa_n` > 157.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=10673)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.265 (n=3319)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=11244)

- **FILTRO** `ibs_7min` > `0.2642` → IC=-0.188 (n=3639)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2642
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=10924)

- **FILTRO** `ballena_activa_n` > `153.0` → IC=-0.178 (n=3618)

  - _Acción_: SKIP cuando `ballena_activa_n` > 153.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=10945)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.169 (n=3485)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=11100)

- **FILTRO** `py_entrada` < `0.3` → IC=-0.329 (n=3483)

  - _Acción_: SKIP cuando `py_entrada` < 0.3
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=11102)

- **FILTRO** `ibs_7min` < `0.291` → IC=-0.255 (n=4813)

  - _Acción_: SKIP cuando `ibs_7min` < 0.291
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=9772)

- **FILTRO** `ballena_activa_n` > `4.0` → IC=-0.174 (n=3482)

  - _Acción_: SKIP cuando `ballena_activa_n` > 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=11103)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.261 (n=4625)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=14684)

- **FILTRO** `ibs_7min` > `0.7222` → IC=-0.185 (n=4827)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7222
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=14482)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.276 (n=3168)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=10722)

- **FILTRO** `ibs_7min` < `0.7113` → IC=-0.201 (n=3472)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7113
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=10418)

- **FILTRO** `ballena_activa_n` > `26.0` → IC=-0.198 (n=3398)

  - _Acción_: SKIP cuando `ballena_activa_n` > 26.0
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=10492)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.258 (n=3362)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=11074)

- **FILTRO** `ibs_7min` > `0.2717` → IC=-0.177 (n=3606)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2717
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=10830)

- **FILTRO** `ballena_activa_n` > `25.0` → IC=-0.174 (n=3487)

  - _Acción_: SKIP cuando `ballena_activa_n` > 25.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=10949)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.32` → IC=-0.303 (n=3271)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=10131)

- **FILTRO** `ibs_7min` < `0.2941` → IC=-0.234 (n=4408)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2941
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=8994)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.203 (n=4847)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=15553)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.31` → IC=-0.314 (n=3332)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=10287)

- **FILTRO** `ibs_7min` < `0.72` → IC=-0.232 (n=4483)

  - _Acción_: SKIP cuando `ibs_7min` < 0.72
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=9136)

- **FILTRO** `ballena_activa_n` > `8.0` → IC=-0.195 (n=3395)

  - _Acción_: SKIP cuando `ballena_activa_n` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=10224)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.231 (n=4655)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=14501)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1046` → IC=-0.135 (n=61)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1046
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=122)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `py_entrada` < `0.455` → IC=-0.163 (n=304)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=1036)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=1325)

- **FILTRO** `py_entrada` > `0.545` → IC=-0.156 (n=187)

  - _Acción_: SKIP cuando `py_entrada` > 0.545
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=685)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=1458)

- **FILTRO** `py_entrada` > `0.565` → IC=-0.172 (n=260)

  - _Acción_: SKIP cuando `py_entrada` > 0.565
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=933)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=251)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=279)

- **FILTRO** `ballena_activa_n` > `24.0` → IC=-0.141 (n=129)

  - _Acción_: SKIP cuando `ballena_activa_n` > 24.0
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=400)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.231 (n=50)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=480)

- **FILTRO** `py_entrada` > `0.58` → IC=-0.216 (n=192)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=594)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.162 (n=255)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=503)

- **FILTRO** `libro_liquidez` < `3306.2556` → IC=-0.146 (n=196)

  - _Acción_: SKIP cuando `libro_liquidez` < 3306.2556
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=590)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=56)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=561)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.4305` → IC=+0.143 (n=780)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.72€ cuando `delta_ratio` |x|> 0.4305 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.133 (n=627)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 4.0 (IC base=+0.124)

- **PATRÓN** `total_vol_5m` < `459.6089` → IC=+0.165 (n=574)

  - _Acción_: Kelly boost +0.82€ cuando `total_vol_5m` < 459.6089 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `3672.897` → IC=+0.132 (n=780)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 3672.897 (IC base=+0.124)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `14.0` → IC=+0.182 (n=196)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 14.0 (IC base=+0.141)

- **PATRÓN** `total_vol_5m` < `381.605` → IC=+0.164 (n=349)

  - _Acción_: Kelly boost +0.82€ cuando `total_vol_5m` < 381.605 (IC base=+0.141)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.147 (n=358)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.04 (IC base=+0.141)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `delta_ratio` |x|> `0.3987` → IC=+0.136 (n=361)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.68€ cuando `delta_ratio` |x|> 0.3987 (IC base=+0.119)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.139 (n=336)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 15.0 (IC base=+0.119)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.121 (n=439)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.04 (IC base=+0.119)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4161` → IC=+0.167 (n=208)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.83€ cuando `delta_ratio` |x|> 0.4161 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.154 (n=287)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 5.0 (IC base=+0.129)

- **PATRÓN** `total_vol_5m` < `878.6597` → IC=+0.160 (n=313)

  - _Acción_: Kelly boost +0.80€ cuando `total_vol_5m` < 878.6597 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `59.0` → IC=+0.187 (n=113)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 59.0 (IC base=+0.129)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.4317` → IC=+0.218 (n=133)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio` |x|> 0.4317 (IC base=+0.134)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.164 (n=117)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 5.0 (IC base=+0.134)

- **PATRÓN** `total_vol_5m` < `4782.684` → IC=+0.182 (n=196)

  - _Acción_: Kelly boost +0.91€ cuando `total_vol_5m` < 4782.684 (IC base=+0.134)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `hora_utc` < `13.0` → IC=+0.125 (n=315)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 13.0 (IC base=+0.096)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.132 (n=218)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.01 (IC base=+0.096)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `6.1729` → IC=-0.222 (n=88)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 6.1729
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=172)

- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.150 (n=344)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0048 (IC base=-0.029)

### PRICE_TARGET_GBM#ETH#atexpiry
- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.268 (n=80)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=+0.003)

- **PATRÓN** `pct_vs_K` |x|≤ `2.0091` → IC=+0.220 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `pct_vs_K` |x|≤ 2.0091 (IC base=+0.003)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `T_h` > `76.1623` → IC=-0.125 (n=70)

  - _Acción_: SKIP cuando `T_h` > 76.1623
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=24)

- **FILTRO** `pct_vs_K` |x|> `6.3582` → IC=-0.258 (n=31)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 6.3582
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=63)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `T_h` < `75.4654` → IC=-0.157 (n=65)

  - _Acción_: SKIP cuando `T_h` < 75.4654
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=133)

### PRICE_TARGET_GBM#SOL#reach
- **FILTRO** `sigma_h` < `0.0173` → IC=-0.167 (n=25)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0173
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0118` → IC=-0.255 (n=667)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0118
  - _Potencial_: sin este filtro IC_bueno=-0.238 (n=223)

- **FILTRO** `T_h` > `66.9347` → IC=-0.257 (n=595)

  - _Acción_: SKIP cuando `T_h` > 66.9347
  - _Potencial_: sin este filtro IC_bueno=-0.237 (n=295)

- **FILTRO** `sigma_h` < `0.0058` → IC=-0.173 (n=212)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0058
  - _Potencial_: sin este filtro IC_bueno=-0.095 (n=638)

- **FILTRO** `pct_vs_K` |x|> `3.0008` → IC=-0.368 (n=210)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.0008
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=640)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `sigma_h` < `0.01` → IC=-0.230 (n=220)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=75)

- **FILTRO** `T_h` > `49.2217` → IC=-0.249 (n=221)

  - _Acción_: SKIP cuando `T_h` > 49.2217
  - _Potencial_: sin este filtro IC_bueno=-0.171 (n=74)

- **FILTRO** `sigma_h` < `0.0069` → IC=-0.179 (n=157)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0069
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=158)

- **FILTRO** `pct_vs_K` |x|> `2.8429` → IC=-0.348 (n=77)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.8429
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=238)

### PRICE_TARGET_GBM_FADE#BTC#reach
- **FILTRO** `T_h` < `142.7845` → IC=-0.278 (n=25)

  - _Acción_: SKIP cuando `T_h` < 142.7845
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=13)

- **FILTRO** `sigma_h` < `0.0078` → IC=-0.273 (n=20)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0078
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=21)

- **FILTRO** `T_h` > `139.1329` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `T_h` > 139.1329
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=21)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `sigma_h` < `0.0097` → IC=-0.326 (n=130)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0097
  - _Potencial_: sin este filtro IC_bueno=-0.288 (n=130)

- **FILTRO** `T_h` > `95.1632` → IC=-0.317 (n=129)

  - _Acción_: SKIP cuando `T_h` > 95.1632
  - _Potencial_: sin este filtro IC_bueno=-0.297 (n=131)

- **FILTRO** `sigma_h` < `0.0058` → IC=-0.162 (n=63)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0058
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=192)

- **PATRÓN** `pct_vs_K` |x|≤ `1.9861` → IC=+0.157 (n=129)

  - _Acción_: Kelly boost +0.78€ cuando `pct_vs_K` |x|≤ 1.9861 (IC base=-0.095)

### PRICE_TARGET_GBM_FADE#ETH#reach
- **FILTRO** `sigma_h` < `0.0095` → IC=-0.180 (n=23)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0095
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **FILTRO** `sigma_h` < `0.0098` → IC=-0.214 (n=19)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0098
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=19)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` < `0.0101` → IC=-0.232 (n=80)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0101
  - _Potencial_: sin este filtro IC_bueno=-0.215 (n=163)

- **FILTRO** `T_h` > `61.9454` → IC=-0.228 (n=182)

  - _Acción_: SKIP cuando `T_h` > 61.9454
  - _Potencial_: sin este filtro IC_bueno=-0.198 (n=61)

- **FILTRO** `sigma_h` < `0.0097` → IC=-0.255 (n=47)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0097
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=143)

- **FILTRO** `T_h` > `46.7258` → IC=-0.136 (n=127)

  - _Acción_: SKIP cuando `T_h` > 46.7258
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=63)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.106` → IC=+0.450 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.106 (IC base=+0.329)

- **PATRÓN** `sigma_h` < `0.0148` → IC=+0.343 (n=132)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0148 (IC base=+0.329)

- **PATRÓN** `sigma_h` > `0.0134` → IC=+0.339 (n=60)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0134 (IC base=+0.329)

- **PATRÓN** `T_h` < `0.3439` → IC=+0.391 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.3439 (IC base=+0.329)

- **PATRÓN** `T_h` > `0.7009` → IC=+0.344 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.7009 (IC base=+0.329)

- **PATRÓN** `dist_50` > `0.4594` → IC=+0.484 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4594 (IC base=+0.329)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.345 (n=153)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.329)

- **PATRÓN** `edge` > `0.0992` → IC=+0.424 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.0992 (IC base=+0.392)

- **PATRÓN** `T_h` < `0.7258` → IC=+0.418 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.7258 (IC base=+0.392)

- **PATRÓN** `dist_50` > `0.368` → IC=+0.440 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.368 (IC base=+0.392)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.411 (n=348)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.392)

### RESOLUTION_SNIPER#BTC#sniper
- **PATRÓN** `edge` > `0.0939` → IC=+0.276 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.0939 (IC base=+0.201)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.271 (n=33)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0067 (IC base=+0.201)

- **PATRÓN** `sigma_h` > `0.0115` → IC=+0.250 (n=26)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0115 (IC base=+0.201)

- **PATRÓN** `T_h` < `0.659` → IC=+0.278 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.659 (IC base=+0.201)

- **PATRÓN** `T_h` > `1.4441` → IC=+0.245 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4441 (IC base=+0.201)

- **PATRÓN** `dist_50` > `0.3235` → IC=+0.303 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3235 (IC base=+0.201)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.236 (n=70)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.201)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.235 (n=66)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.201)

### RESOLUTION_SNIPER#ETH#sniper
- **PATRÓN** `edge` > `0.1295` → IC=+0.441 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1295 (IC base=+0.271)

- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.324 (n=15)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0099 (IC base=+0.271)

- **PATRÓN** `dist_50` > `0.4172` → IC=+0.441 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4172 (IC base=+0.271)

- **PATRÓN** `edge` > `0.1011` → IC=+0.468 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1011 (IC base=+0.416)

- **PATRÓN** `sigma_h` < `0.0073` → IC=+0.438 (n=30)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0073 (IC base=+0.416)

- **PATRÓN** `T_h` < `1.178` → IC=+0.442 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 1.178 (IC base=+0.416)

- **PATRÓN** `dist_50` > `0.4122` → IC=+0.484 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4122 (IC base=+0.416)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.405 (n=40)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.416)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.444 (n=34)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.416)

### RESOLUTION_SNIPER#SOL#sniper
- **PATRÓN** `edge` > `0.1449` → IC=+0.487 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1449 (IC base=+0.424)

- **PATRÓN** `sigma_h` < `0.0155` → IC=+0.471 (n=67)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0155 (IC base=+0.424)

- **PATRÓN** `T_h` < `1.0409` → IC=+0.427 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 1.0409 (IC base=+0.424)

- **PATRÓN** `T_h` > `0.3968` → IC=+0.436 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.3968 (IC base=+0.424)

- **PATRÓN** `dist_50` > `0.3288` → IC=+0.474 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3288 (IC base=+0.424)

- **PATRÓN** `edge` > `0.1937` → IC=+0.472 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1937 (IC base=+0.465)

- **PATRÓN** `sigma_h` < `0.0162` → IC=+0.475 (n=160)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0162 (IC base=+0.465)

- **PATRÓN** `T_h` < `0.8021` → IC=+0.459 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.8021 (IC base=+0.465)

- **PATRÓN** `T_h` > `1.4857` → IC=+0.482 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4857 (IC base=+0.465)

- **PATRÓN** `dist_50` > `0.414` → IC=+0.481 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.414 (IC base=+0.465)

- **PATRÓN** `hora_utc` < `2.0` → IC=+0.485 (n=63)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 2.0 (IC base=+0.465)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=497)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.073 (n=534)

- **PATRÓN** `streak_estiramiento` < `0.3783` → IC=+0.135 (n=165)

  - _Acción_: Kelly boost +0.67€ cuando `streak_estiramiento` < 0.3783 (IC base=+0.021)

- **PATRÓN** `streak_estiramiento` < `0.8333` → IC=+0.126 (n=370)

  - _Acción_: Kelly boost +0.63€ cuando `streak_estiramiento` < 0.8333 (IC base=+0.062)

- **PATRÓN** `ballena_activa_n` < `29.0` → IC=+0.125 (n=283)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 29.0 (IC base=+0.062)

### STREAK_FADE_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=17)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.152 (n=21)

  - _Acción_: Kelly boost +0.76€ cuando `py_entrada` < 0.495 (IC base=+0.085)

- **PATRÓN** `streak_estiramiento` < `0.5551` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `streak_estiramiento` < 0.5551 (IC base=+0.085)

- **PATRÓN** `ballena_activa_n` < `68.0` → IC=+0.143 (n=26)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 68.0 (IC base=+0.085)

### STREAK_FADE_15M#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=30)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.179 (n=26)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.179 (n=26)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` < 0.495 (IC base=+0.058)

### STREAK_FADE_15M#XRP#15min
- **PATRÓN** `streak_estiramiento` < `0.3787` → IC=+0.129 (n=130)

  - _Acción_: Kelly boost +0.64€ cuando `streak_estiramiento` < 0.3787 (IC base=+0.039)

- **PATRÓN** `streak_estiramiento` < `0.3787` → IC=+0.211 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `streak_estiramiento` < 0.3787 (IC base=+0.085)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.139 (n=203)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 35.0 (IC base=+0.085)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.194 (n=47)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=104)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=71)

- **FILTRO** `libro_liquidez` < `3678.6572` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 3678.6572
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=78)

- **FILTRO** `streak_len` > `3.0` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=62)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.136 (n=31)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=47)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=826)

### STREAK_FADE_60M
- **FILTRO** `py_entrada` < `0.515` → IC=-0.214 (n=19)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.134 (n=39)

- **FILTRO** `streak_estiramiento` > `0.6393` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.6393
  - _Potencial_: sin este filtro IC_bueno=+0.258 (n=31)

- **PATRÓN** `py_entrada` > `0.515` → IC=+0.134 (n=39)

  - _Acción_: Kelly boost +0.67€ cuando `py_entrada` > 0.515 (IC base=+0.017)

- **PATRÓN** `streak_estiramiento` < `0.6393` → IC=+0.258 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `streak_estiramiento` < 0.6393 (IC base=+0.015)

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
- **FILTRO** `py_entrada` < `0.525` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.525
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=13)

- **PATRÓN** `streak_estiramiento` < `0.6237` → IC=+0.227 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `streak_estiramiento` < 0.6237 (IC base=+0.040)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=1118)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=1362)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=1244)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=1336)

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
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=5642)

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
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=3406)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.184 (n=2217)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0059 (IC base=+0.132)

- **PATRÓN** `drift_60min` |x|≤ `0.2338` → IC=+0.158 (n=6648)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.2338 (IC base=+0.132)

- **PATRÓN** `drift_15min` |x|≤ `1.1273` → IC=+0.133 (n=6648)

  - _Acción_: Kelly boost +0.66€ cuando `drift_15min` |x|≤ 1.1273 (IC base=+0.132)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0642` → IC=+0.132 (n=6647)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.66€ cuando `delta_ratio_macro` |x|> 0.0642 (IC base=+0.132)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0995` → IC=+0.143 (n=2096)

  - _Acción_: Kelly boost +0.71€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0995 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.143 (n=6167)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 6.0 (IC base=+0.132)

- **PATRÓN** `ibs_15` > `0.551` → IC=+0.207 (n=5940)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.551 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.974` → IC=+0.228 (n=1242)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.974 (IC base=+0.132)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=3481)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `4313.8395` → IC=+0.171 (n=2216)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 4313.8395 (IC base=+0.132)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=2589)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.249 (n=301)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.206)

- **PATRÓN** `drift_60min` |x|≤ `0.0772` → IC=+0.249 (n=396)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0772 (IC base=+0.206)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2668` → IC=+0.231 (n=299)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2668 (IC base=+0.206)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2244` → IC=+0.218 (n=544)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2244 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.233 (n=832)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.206)

- **PATRÓN** `ibs_15` > `0.7031` → IC=+0.276 (n=898)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7031 (IC base=+0.206)

- **PATRÓN** `dist_vwap_pct` > `0.4048` → IC=+0.231 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4048 (IC base=+0.206)

- **PATRÓN** `dist_vwap_pct` < `0.5549` → IC=+0.210 (n=1014)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5549 (IC base=+0.206)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.047` → IC=+0.301 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.047 (IC base=+0.206)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.209 (n=1165)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.206)

- **PATRÓN** `libro_liquidez` > `11859.2402` → IC=+0.221 (n=599)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11859.2402 (IC base=+0.206)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.147 (n=1015)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0068 (IC base=+0.132)

- **PATRÓN** `drift_60min` |x|≤ `0.1093` → IC=+0.146 (n=769)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.1093 (IC base=+0.132)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0833` → IC=+0.137 (n=1030)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.68€ cuando `delta_ratio_macro` |x|> 0.0833 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.144 (n=821)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 11.0 (IC base=+0.132)

- **PATRÓN** `ibs_15` > `0.4799` → IC=+0.218 (n=1153)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.4799 (IC base=+0.132)

- **PATRÓN** `dist_vwap_pct` > `0.1241` → IC=+0.147 (n=717)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` > 0.1241 (IC base=+0.132)

- **PATRÓN** `dist_vwap_pct` < `0.6708` → IC=+0.132 (n=1309)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.6708 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.889` → IC=+0.283 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.889 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `6107.0908` → IC=+0.176 (n=523)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 6107.0908 (IC base=+0.132)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `ibs_15` > `0.8333` → IC=+0.146 (n=699)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.73€ cuando `ibs_15` > 0.8333 (IC base=+0.045)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0119` → IC=+0.143 (n=1680)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` > 0.0119 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.24` → IC=+0.175 (n=1683)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.24 (IC base=+0.137)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0583` → IC=+0.140 (n=1680)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.70€ cuando `delta_ratio_macro` |x|> 0.0583 (IC base=+0.137)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0928` → IC=+0.186 (n=526)

  - _Acción_: Kelly boost +0.93€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0928 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.144 (n=1538)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 6.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.138 (n=1555)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 15.0 (IC base=+0.137)

- **PATRÓN** `ibs_15` > `0.697` → IC=+0.232 (n=1120)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.697 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` > `0.2152` → IC=+0.143 (n=765)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.2152 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` < `0.9158` → IC=+0.141 (n=1943)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.9158 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.978` → IC=+0.183 (n=389)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 16.978 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `2943.2931` → IC=+0.179 (n=762)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 2943.2931 (IC base=+0.137)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `drift_60min` |x|≤ `0.1089` → IC=+0.364 (n=549)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1089 (IC base=+0.363)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1426` → IC=+0.377 (n=549)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1426 (IC base=+0.363)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1039` → IC=+0.379 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1039 (IC base=+0.363)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.370 (n=762)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.363)

- **PATRÓN** `ibs_15` > `0.7881` → IC=+0.394 (n=822)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7881 (IC base=+0.363)

- **PATRÓN** `dist_vwap_pct` > `0.2719` → IC=+0.383 (n=356)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2719 (IC base=+0.363)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.787` → IC=+0.394 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.787 (IC base=+0.363)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.365 (n=1001)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.363)

- **PATRÓN** `libro_liquidez` > `9641.0136` → IC=+0.377 (n=373)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9641.0136 (IC base=+0.363)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `drift_60min` |x|≤ `0.1523` → IC=+0.365 (n=346)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1523 (IC base=+0.363)

- **PATRÓN** `drift_15min` |x|≤ `0.4182` → IC=+0.363 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4182 (IC base=+0.363)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2167` → IC=+0.378 (n=178)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2167 (IC base=+0.363)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1441` → IC=+0.399 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1441 (IC base=+0.363)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.380 (n=366)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.363)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.363 (n=400)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.363)

- **PATRÓN** `ibs_15` > `0.8057` → IC=+0.384 (n=393)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8057 (IC base=+0.363)

- **PATRÓN** `dist_vwap_pct` > `0.2555` → IC=+0.393 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2555 (IC base=+0.363)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.667` → IC=+0.384 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.667 (IC base=+0.363)

- **PATRÓN** `libro_liquidez` > `15150.2605` → IC=+0.390 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15150.2605 (IC base=+0.363)

- **PATRÓN** `ballena_activa_n` < `409.0` → IC=+0.385 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 409.0 (IC base=+0.363)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.363 (n=144)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.362)

- **PATRÓN** `sigma_h` > `0.0063` → IC=+0.373 (n=195)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0063 (IC base=+0.362)

- **PATRÓN** `drift_60min` |x|≤ `0.1058` → IC=+0.365 (n=288)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1058 (IC base=+0.362)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1258` → IC=+0.379 (n=286)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1258 (IC base=+0.362)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2925` → IC=+0.370 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2925 (IC base=+0.362)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.379 (n=147)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.362)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.376 (n=200)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.362)

- **PATRÓN** `ibs_15` > `0.764` → IC=+0.396 (n=429)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.764 (IC base=+0.362)

- **PATRÓN** `dist_vwap_pct` > `0.4608` → IC=+0.378 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4608 (IC base=+0.362)

- **PATRÓN** `dist_vwap_pct` < `0.6782` → IC=+0.364 (n=490)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6782 (IC base=+0.362)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.857` → IC=+0.399 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.857 (IC base=+0.362)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.587` → IC=+0.364 (n=396)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.587 (IC base=+0.362)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.363 (n=488)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.362)

- **PATRÓN** `libro_liquidez` > `4327.6083` → IC=+0.368 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4327.6083 (IC base=+0.362)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0079` → IC=-0.204 (n=3082)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0079
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=3083)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.221 (n=2730)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=3435)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1392` → IC=+0.217 (n=521)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1392 (IC base=-0.087)

- **PATRÓN** `ibs_15` > `0.6296` → IC=+0.280 (n=1356)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6296 (IC base=-0.087)

- **PATRÓN** `dist_vwap_pct` > `0.1169` → IC=+0.209 (n=803)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1169 (IC base=-0.087)

- **PATRÓN** `dist_vwap_pct` < `0.602` → IC=+0.201 (n=1438)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.602 (IC base=-0.087)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2273` → IC=+0.267 (n=2034)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2273 (IC base=+0.002)

- **PATRÓN** `ibs_15` < `0.3769` → IC=+0.282 (n=6099)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3769 (IC base=+0.002)

- **PATRÓN** `dist_vwap_pct` > `0.7132` → IC=+0.263 (n=877)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7132 (IC base=+0.002)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0746` → IC=-0.239 (n=2046)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0746
  - _Potencial_: sin este filtro IC_bueno=-0.121 (n=2048)

- **FILTRO** `sigma_h` < `0.0041` → IC=-0.208 (n=1023)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0041
  - _Potencial_: sin este filtro IC_bueno=-0.171 (n=3071)

- **FILTRO** `sigma_ewma_delta_pct` > `22.185` → IC=-0.238 (n=578)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 22.185
  - _Potencial_: sin este filtro IC_bueno=-0.171 (n=3516)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.180 (n=95)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=3999)

- **FILTRO** `libro_liquidez` < `10184.0512` → IC=-0.191 (n=1351)

  - _Acción_: SKIP cuando `libro_liquidez` < 10184.0512
  - _Potencial_: sin este filtro IC_bueno=-0.175 (n=2743)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.148 (n=373)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0033 (IC base=+0.065)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2673` → IC=+0.282 (n=163)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2673 (IC base=+0.065)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1446` → IC=+0.283 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1446 (IC base=+0.065)

- **PATRÓN** `ibs_15` > `0.7533` → IC=+0.318 (n=487)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7533 (IC base=+0.065)

- **PATRÓN** `dist_vwap_pct` > `0.1067` → IC=+0.287 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1067 (IC base=+0.065)

- **PATRÓN** `dist_vwap_pct` < `0.5501` → IC=+0.287 (n=543)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5501 (IC base=+0.065)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.729` → IC=+0.142 (n=244)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 21.729 (IC base=+0.065)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0742` → IC=+0.221 (n=84)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0742 (IC base=-0.180)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1389` → IC=+0.289 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1389 (IC base=-0.180)

- **PATRÓN** `ibs_15` < `0.6283` → IC=+0.291 (n=84)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.6283 (IC base=-0.180)

- **PATRÓN** `dist_vwap_pct` < `0.0474` → IC=+0.271 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0474 (IC base=-0.180)

- **PATRÓN** `ballena_activa_n` < `392.0` → IC=+0.300 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 392.0 (IC base=-0.180)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.155 (n=895)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.162 (n=685)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0067 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.0718` → IC=+0.178 (n=302)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.0718 (IC base=+0.150)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2988` → IC=+0.188 (n=542)

  - _Acción_: Kelly boost +0.94€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2988 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.174 (n=492)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 11.0 (IC base=+0.150)

- **PATRÓN** `ibs_15` > `0.5657` → IC=+0.243 (n=684)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5657 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.6763` → IC=+0.176 (n=134)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.6763 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` < `0.1598` → IC=+0.151 (n=525)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.1598 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.241` → IC=+0.254 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.241 (IC base=+0.150)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.155 (n=895)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.01 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `5211.9622` → IC=+0.172 (n=456)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 5211.9622 (IC base=+0.150)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.250 (n=1600)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.4846` → IC=+0.242 (n=2400)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4846 (IC base=+0.234)

- **PATRÓN** `drift_15min` |x|≤ `0.832` → IC=+0.248 (n=2112)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.832 (IC base=+0.234)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1966` → IC=+0.255 (n=1088)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1966 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.238 (n=885)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.234)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.239 (n=1640)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.234)

- **PATRÓN** `ibs_15` < `0.1929` → IC=+0.295 (n=1600)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.1929 (IC base=+0.234)

- **PATRÓN** `dist_vwap_pct` > `0.2392` → IC=+0.245 (n=814)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2392 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.514` → IC=+0.242 (n=1036)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.514 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.323` → IC=+0.237 (n=2525)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.323 (IC base=+0.234)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.2012` → IC=-0.298 (n=370)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.2012
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=1111)

- **FILTRO** `drift_60min` |x|> `0.2016` → IC=-0.296 (n=370)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2016
  - _Potencial_: sin este filtro IC_bueno=-0.175 (n=1111)

- **FILTRO** `drift_15min` |x|> `1.0228` → IC=-0.304 (n=370)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.0228
  - _Potencial_: sin este filtro IC_bueno=-0.172 (n=1111)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.241 (n=353)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.194 (n=1128)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1478` → IC=+0.188 (n=46)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.94€ cuando `delta_ratio_macro` |x|> 0.1478 (IC base=-0.205)

- **PATRÓN** `ibs_15` > `0.9231` → IC=+0.380 (n=23)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9231 (IC base=-0.205)

- **PATRÓN** `dist_vwap_pct` < `0.4298` → IC=+0.158 (n=77)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.4298 (IC base=-0.205)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.194 (n=34)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 37.0 (IC base=-0.205)

- **PATRÓN** `ibs_15` < `0.381` → IC=+0.295 (n=1008)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.381 (IC base=-0.025)

- **PATRÓN** `dist_vwap_pct` < `0.2022` → IC=+0.257 (n=920)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2022 (IC base=-0.025)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0142` → IC=-0.250 (n=1154)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0142
  - _Potencial_: sin este filtro IC_bueno=-0.162 (n=569)

- **FILTRO** `drift_60min` |x|> `0.1231` → IC=-0.244 (n=584)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1231
  - _Potencial_: sin este filtro IC_bueno=-0.209 (n=1139)

- **FILTRO** `drift_15min` |x|> `1.2906` → IC=-0.285 (n=430)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.2906
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=1293)

- **FILTRO** `libro_spread` > `0.04` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.04
  - _Potencial_: sin este filtro IC_bueno=-0.220 (n=1702)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.221)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.221)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0705` → IC=+0.283 (n=1257)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0705 (IC base=-0.008)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1183` → IC=+0.287 (n=614)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1183 (IC base=-0.008)

- **PATRÓN** `ibs_15` < `0.3333` → IC=+0.294 (n=1417)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3333 (IC base=-0.008)

- **PATRÓN** `dist_vwap_pct` > `0.7901` → IC=+0.325 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7901 (IC base=-0.008)

### UPDOWN_GBM_ETH_15M_HORA7
- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.161 (n=57)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0063 (IC base=+0.086)

- **PATRÓN** `drift_15min` |x|≤ `0.7315` → IC=+0.151 (n=64)

  - _Acción_: Kelly boost +0.76€ cuando `drift_15min` |x|≤ 0.7315 (IC base=+0.086)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.235` → IC=+0.151 (n=41)

  - _Acción_: Kelly boost +0.76€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.235 (IC base=+0.086)

- **PATRÓN** `ibs_15` > `0.8692` → IC=+0.333 (n=22)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8692 (IC base=+0.086)

- **PATRÓN** `dist_vwap_pct` < `0.0949` → IC=+0.200 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0949 (IC base=+0.086)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.155 (n=27)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 49.0 (IC base=+0.086)

- **PATRÓN** `dist_vwap_pct` > `0.1929` → IC=+0.135 (n=94)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` > 0.1929 (IC base=+0.050)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.161 (n=57)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0063 (IC base=+0.086)

- **PATRÓN** `drift_15min` |x|≤ `0.7315` → IC=+0.151 (n=64)

  - _Acción_: Kelly boost +0.76€ cuando `drift_15min` |x|≤ 0.7315 (IC base=+0.086)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.235` → IC=+0.151 (n=41)

  - _Acción_: Kelly boost +0.76€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.235 (IC base=+0.086)

- **PATRÓN** `ibs_15` > `0.8692` → IC=+0.333 (n=22)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8692 (IC base=+0.086)

- **PATRÓN** `dist_vwap_pct` < `0.0949` → IC=+0.200 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0949 (IC base=+0.086)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.155 (n=27)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 49.0 (IC base=+0.086)

- **PATRÓN** `dist_vwap_pct` > `0.1929` → IC=+0.135 (n=94)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` > 0.1929 (IC base=+0.050)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.302 (n=504)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0035 (IC base=+0.285)

- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.294 (n=503)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0068 (IC base=+0.285)

- **PATRÓN** `drift_60min` |x|≤ `0.0714` → IC=+0.310 (n=665)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0714 (IC base=+0.285)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1501` → IC=+0.288 (n=1006)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1501 (IC base=+0.285)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2178` → IC=+0.290 (n=928)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2178 (IC base=+0.285)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.296 (n=1575)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.285)

- **PATRÓN** `ibs_15` > `0.8361` → IC=+0.311 (n=1509)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8361 (IC base=+0.285)

- **PATRÓN** `dist_vwap_pct` > `0.2762` → IC=+0.316 (n=645)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2762 (IC base=+0.285)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.6` → IC=+0.387 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.6 (IC base=+0.285)

- **PATRÓN** `libro_liquidez` > `13070.3814` → IC=+0.300 (n=503)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13070.3814 (IC base=+0.285)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.309 (n=265)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.280)

- **PATRÓN** `drift_60min` |x|≤ `0.076` → IC=+0.301 (n=349)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.076 (IC base=+0.280)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2694` → IC=+0.283 (n=265)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2694 (IC base=+0.280)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2268` → IC=+0.290 (n=480)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2268 (IC base=+0.280)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.304 (n=732)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.280)

- **PATRÓN** `ibs_15` > `0.8549` → IC=+0.309 (n=709)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8549 (IC base=+0.280)

- **PATRÓN** `dist_vwap_pct` > `0.2612` → IC=+0.310 (n=335)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2612 (IC base=+0.280)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.41` → IC=+0.393 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.41 (IC base=+0.280)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.281 (n=1027)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.280)

- **PATRÓN** `libro_liquidez` > `14467.1785` → IC=+0.309 (n=360)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14467.1785 (IC base=+0.280)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.302 (n=316)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0046 (IC base=+0.291)

- **PATRÓN** `sigma_h` > `0.0072` → IC=+0.293 (n=240)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0072 (IC base=+0.291)

- **PATRÓN** `drift_60min` |x|≤ `0.0504` → IC=+0.326 (n=240)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0504 (IC base=+0.291)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0642` → IC=+0.295 (n=717)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0642 (IC base=+0.291)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1009` → IC=+0.310 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1009 (IC base=+0.291)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.297 (n=642)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.291)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.292 (n=359)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.291)

- **PATRÓN** `ibs_15` > `0.8448` → IC=+0.315 (n=717)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8448 (IC base=+0.291)

- **PATRÓN** `dist_vwap_pct` > `0.2918` → IC=+0.315 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2918 (IC base=+0.291)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.851` → IC=+0.382 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.851 (IC base=+0.291)

### UPDOWN_OU_5M
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1078` → IC=-0.161 (n=237)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1078
  - _Potencial_: sin este filtro IC_bueno=-0.097 (n=117)

- **FILTRO** `ballena_activa_n` > `31.0` → IC=-0.146 (n=272)

  - _Acción_: SKIP cuando `ballena_activa_n` > 31.0
  - _Potencial_: sin este filtro IC_bueno=-0.096 (n=92)

- **FILTRO** `sigma_h` < `0.0051` → IC=-0.162 (n=128)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0051
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=385)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.197 (n=186)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=66)

### UPDOWN_OU_5M#BNB#5min
- **FILTRO** `sigma_h` < `0.0065` → IC=-0.447 (n=17)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0065
  - _Potencial_: sin este filtro IC_bueno=-0.375 (n=6)

- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1682` → IC=-0.191 (n=40)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1682
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=41)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.160 (n=48)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=54)

### UPDOWN_OU_5M#BTC#5min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1431` → IC=-0.155 (n=56)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1431
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=170)

- **FILTRO** `sigma_h` < `0.006` → IC=-0.167 (n=49)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.006
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=17)

- **FILTRO** `drift_15min` |x|> `0.4064` → IC=-0.278 (n=16)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.4064
  - _Potencial_: sin este filtro IC_bueno=-0.096 (n=50)

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
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1667` → IC=-0.167 (n=22)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1667
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=45)

- **FILTRO** `sigma_h` < `0.0052` → IC=-0.315 (n=25)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0052
  - _Potencial_: sin este filtro IC_bueno=-0.300 (n=13)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1729` → IC=-0.273 (n=20)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1729
  - _Potencial_: sin este filtro IC_bueno=-0.128 (n=41)

- **FILTRO** `sigma_h` < `0.0081` → IC=-0.188 (n=30)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0081
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=31)

- **FILTRO** `sigma_h` < `0.0063` → IC=-0.243 (n=33)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0063
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=34)

- **FILTRO** `drift_15min` |x|> `0.5336` → IC=-0.250 (n=22)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.5336
  - _Potencial_: sin este filtro IC_bueno=-0.181 (n=45)

### WEEKLY_PRICE
- **PATRÓN** `ratio` < `0.9866` → IC=+0.252 (n=578)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9866 (IC base=+0.122)

- **PATRÓN** `T_h` > `115.9003` → IC=+0.352 (n=3372)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 115.9003 (IC base=+0.331)

- **PATRÓN** `ratio` > `1.0158` → IC=+0.387 (n=650)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0158 (IC base=+0.331)

### WEEKLY_PRICE#BTC
- **PATRÓN** `ratio` < `0.9756` → IC=+0.190 (n=217)

  - _Acción_: Kelly boost +0.95€ cuando `ratio` < 0.9756 (IC base=+0.064)

- **PATRÓN** `T_h` > `110.2068` → IC=+0.325 (n=1248)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 110.2068 (IC base=+0.302)

- **PATRÓN** `ratio` > `1.0004` → IC=+0.298 (n=517)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0004 (IC base=+0.302)

### WEEKLY_PRICE#ETH
- **PATRÓN** `ratio` < `0.9775` → IC=+0.361 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9775 (IC base=+0.185)

- **PATRÓN** `T_h` > `111.9957` → IC=+0.347 (n=1241)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9957 (IC base=+0.313)

- **PATRÓN** `ratio` > `1.0221` → IC=+0.406 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0221 (IC base=+0.313)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.0398` → IC=+0.409 (n=296)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.0398 (IC base=+0.396)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.551 sube el IC de +0.132 a +0.207 en UPDOWN_GBM#15min (n=5940). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7031 sube el IC de +0.206 a +0.276 en UPDOWN_GBM#BTC#15min (n=898). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.4799 sube el IC de +0.132 a +0.218 en UPDOWN_GBM#ETH#15min (n=1153). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.697 sube el IC de +0.137 a +0.232 en UPDOWN_GBM#XRP#15min (n=1120). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6296 sube el IC de -0.087 a +0.280 en UPDOWN_GBM_15M_TARDIO (n=1356). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3769 sube el IC de +0.002 a +0.282 en UPDOWN_GBM_15M_TARDIO (n=6099). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7533 sube el IC de +0.065 a +0.318 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=487). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.6283 sube el IC de -0.180 a +0.291 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=84). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.5657 sube el IC de +0.150 a +0.243 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=684). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.1929 sube el IC de +0.234 a +0.295 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=1600). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.9231 sube el IC de -0.205 a +0.380 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=23). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.381 sube el IC de -0.025 a +0.295 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=1008). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.221 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3333 sube el IC de -0.008 a +0.294 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=1417). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_YES, IBS > 0.8692 sube el IC de +0.086 a +0.333 en UPDOWN_GBM_ETH_15M_HORA7 (n=22). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_YES, IBS > 0.8692 sube el IC de +0.086 a +0.333 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=22). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8361 sube el IC de +0.285 a +0.311 en UPDOWN_GBM_IBS_ALTO (n=1509). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8549 sube el IC de +0.280 a +0.309 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=709). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8448 sube el IC de +0.291 a +0.315 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=717). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7881 sube el IC de +0.363 a +0.394 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=822). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8057 sube el IC de +0.363 a +0.384 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=393). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.764 sube el IC de +0.362 a +0.396 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=429). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 2375 | +0.084 | +262.83€ | 1 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 2375 | +0.084 | +262.83€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1963 | +0.085 | +223.34€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1963 | +0.085 | +223.34€ | 1 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 285 | +0.068 | +10.79€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 285 | +0.068 | +10.79€ | 5 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 96 | +0.122 | +29.03€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 96 | +0.122 | +29.03€ | 0 | 9 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 1506 | -0.029 | +48.81€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 1506 | -0.029 | +48.81€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE | 7 | +0.019 | +3.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE#15min | 7 | +0.019 | +3.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 1182 | -0.041 | +36.17€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 1182 | -0.041 | +36.17€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 224 | +0.035 | +20.04€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 224 | +0.035 | +20.04€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 93 | -0.037 | -10.65€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 93 | -0.037 | -10.65€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 51660 | -0.086 | -6585.59€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 3394 | +0.096 | -315.56€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 48266 | -0.099 | -6270.03€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 5088 | -0.116 | -816.49€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 5088 | -0.116 | -816.49€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 3394 | +0.096 | -315.56€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 3394 | +0.096 | -315.56€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 5129 | -0.108 | -957.76€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 5129 | -0.108 | -957.76€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 14477 | -0.043 | -1325.31€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 14477 | -0.043 | -1325.31€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 14135 | -0.121 | -1627.38€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 14135 | -0.121 | -1627.38€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 9437 | -0.138 | -1543.09€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 9437 | -0.138 | -1543.09€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 57886 | -0.012 | +2577.07€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 14923 | +0.004 | +1476.54€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 42963 | -0.017 | +1100.54€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 57886 | -0.012 | +2577.07€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 14923 | +0.004 | +1476.54€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 42963 | -0.017 | +1100.54€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 215242 | +0.112 | -8887.36€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#15min | 23625 | +0.179 | -755.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 1005 | +0.022 | -78.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 178402 | +0.104 | -7647.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 12210 | +0.095 | -404.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 29581 | +0.101 | -2121.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 89 | -0.192 | +10.74€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 29455 | +0.102 | -2141.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#60min | 22 | +0.167 | +21.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 40267 | +0.122 | -655.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5739 | +0.176 | -237.80€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 29532 | +0.119 | -228.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 4954 | +0.081 | -167.43€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 29630 | +0.098 | -2102.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 111 | -0.102 | +21.70€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 29491 | +0.099 | -2116.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#60min | 13 | -0.065 | +4.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 46089 | +0.123 | -994.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 11474 | +0.177 | -329.19€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 30010 | +0.106 | -574.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 4593 | +0.103 | -82.99€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 40084 | +0.111 | -1707.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 6112 | +0.200 | -234.37€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 908 | +0.046 | -25.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 30439 | +0.095 | -1266.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 2625 | +0.108 | -182.32€ | 1 | 4 |
| ✅ FAVORITO_CONFIRMADO#XRP | 29591 | +0.106 | -1305.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 100 | -0.137 | +13.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 29475 | +0.107 | -1320.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 35125 | +0.188 | -2694.91€ | 2 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 35125 | +0.188 | -2694.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 7955 | +0.159 | -963.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 7955 | +0.159 | -963.19€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 5298 | +0.193 | -234.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 5298 | +0.193 | -234.13€ | 3 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 7760 | +0.171 | -731.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 7760 | +0.171 | -731.26€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 6431 | +0.251 | -230.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 6431 | +0.251 | -230.69€ | 0 | 4 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 7602 | +0.182 | -549.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 7602 | +0.182 | -549.41€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 1345 | +0.425 | -51.13€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 1345 | +0.425 | -51.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 572 | +0.439 | -5.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 572 | +0.439 | -5.23€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE#15min | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 528 | +0.421 | -23.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 528 | +0.421 | -23.69€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 231 | +0.401 | -18.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 231 | +0.401 | -18.34€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 124091 | +0.199 | -9100.92€ | 3 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 124091 | +0.199 | -9100.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 21520 | +0.175 | -2560.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 21520 | +0.175 | -2560.46€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 19992 | +0.223 | -669.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 19992 | +0.223 | -669.22€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 21277 | +0.180 | -2244.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 21277 | +0.180 | -2244.73€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 20177 | +0.217 | -792.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 20177 | +0.217 | -792.66€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 20468 | +0.205 | -1199.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 20468 | +0.205 | -1199.45€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 20657 | +0.196 | -1634.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 20657 | +0.196 | -1634.40€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 48265 | +0.116 | +400.95€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 48265 | +0.116 | +400.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 24039 | +0.117 | +265.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 24039 | +0.117 | +265.24€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 24226 | +0.116 | +135.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 24226 | +0.116 | +135.71€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 2717 | +0.294 | -7.95€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 2717 | +0.294 | -7.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 1243 | +0.283 | -25.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 1243 | +0.283 | -25.31€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 1332 | +0.297 | +10.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 1332 | +0.297 | +10.63€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 142 | +0.347 | +6.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 142 | +0.347 | +6.73€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 1258 | +0.438 | -5.42€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 1258 | +0.438 | -5.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 600 | +0.435 | -7.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 600 | +0.435 | -7.20€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 606 | +0.441 | +0.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 606 | +0.441 | +0.37€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 52 | +0.407 | +1.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 52 | +0.407 | +1.41€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 2067 | +0.063 | -111.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 725 | +0.046 | -64.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 1342 | +0.071 | -47.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1633 | +0.068 | -66.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 291 | +0.053 | -19.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 1342 | +0.071 | -47.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 98756 | +0.101 | -2083.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 8014 | +0.097 | +194.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 90742 | +0.101 | -2278.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 53873 | +0.105 | -441.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 8014 | +0.097 | +194.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 45859 | +0.106 | -636.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 21266 | +0.109 | -89.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 21266 | +0.109 | -89.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 23617 | +0.083 | -1551.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 23617 | +0.083 | -1551.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 934 | +0.176 | -111.00€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 934 | +0.176 | -111.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 934 | +0.176 | -111.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 934 | +0.176 | -111.00€ | 2 | 4 |
| ✅ GBM_LATE_15M | 67290 | +0.102 | +37895.25€ | 0 | 19 |
| ✅ GBM_LATE_15M#15min | 67290 | +0.102 | +37895.25€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 11184 | +0.223 | +9557.73€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 11184 | +0.223 | +9557.73€ | 0 | 19 |
| ✅ GBM_LATE_15M#BTC | 10530 | +0.176 | +8510.25€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 10530 | +0.176 | +8510.25€ | 0 | 22 |
| ✅ GBM_LATE_15M#DOGE | 12038 | +0.206 | +9479.48€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 12038 | +0.206 | +9479.48€ | 0 | 21 |
| ✅ GBM_LATE_15M#ETH | 8892 | +0.063 | +3032.54€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 8892 | +0.063 | +3032.54€ | 1 | 17 |
| ✅ GBM_LATE_15M#SOL | 9323 | -0.025 | +2420.56€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 9323 | -0.025 | +2420.56€ | 4 | 15 |
| ✅ GBM_LATE_15M#XRP | 15323 | -0.019 | +4894.70€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 15323 | -0.019 | +4894.70€ | 3 | 11 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 71455 | +0.088 | +41919.75€ | 0 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 71455 | +0.088 | +41919.75€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 13877 | -0.002 | +7338.89€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 13877 | -0.002 | +7338.89€ | 3 | 9 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 15351 | +0.007 | +4268.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 15351 | +0.007 | +4268.93€ | 0 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 9558 | +0.295 | +10940.13€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 9558 | +0.295 | +10940.13€ | 0 | 22 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 13676 | +0.019 | +4412.09€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 13676 | +0.019 | +4412.09€ | 0 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 10856 | +0.051 | +5096.51€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 10856 | +0.051 | +5096.51€ | 3 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 8137 | +0.312 | +9863.20€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 8137 | +0.312 | +9863.20€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 52938 | +0.179 | +43993.53€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 52938 | +0.179 | +43993.53€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 8022 | +0.238 | +7421.88€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 8022 | +0.238 | +7421.88€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 8458 | +0.140 | +6386.98€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 8458 | +0.140 | +6386.98€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 8518 | +0.223 | +7352.48€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 8518 | +0.223 | +7352.48€ | 0 | 19 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 9043 | +0.130 | +7087.84€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 9043 | +0.130 | +7087.84€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 9977 | +0.123 | +7725.00€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 9977 | +0.123 | +7725.00€ | 0 | 26 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 8920 | +0.232 | +8019.36€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 8920 | +0.232 | +8019.36€ | 0 | 25 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 14622 | +0.126 | +7437.11€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 14622 | +0.126 | +7437.11€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 678 | +0.162 | +445.31€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 678 | +0.162 | +445.31€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 3842 | +0.126 | +2066.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 3842 | +0.126 | +2066.94€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 509 | +0.156 | +286.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 509 | +0.156 | +286.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 4281 | +0.126 | +2165.67€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 4281 | +0.126 | +2165.67€ | 0 | 17 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 3957 | +0.100 | +1613.70€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 3957 | +0.100 | +1613.70€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 1355 | +0.168 | +858.78€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 1355 | +0.168 | +858.78€ | 0 | 27 |
| ✅ GBM_LATE_15M_TARDIO | 67601 | +0.189 | +56294.03€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#15min | 67601 | +0.189 | +56294.03€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 10699 | +0.248 | +10251.57€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 10699 | +0.248 | +10251.57€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 10857 | +0.143 | +7938.26€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 10857 | +0.143 | +7938.26€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 11456 | +0.233 | +10291.06€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 11456 | +0.233 | +10291.06€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 11181 | +0.145 | +8436.67€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 11181 | +0.145 | +8436.67€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 11920 | +0.129 | +8735.04€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 11920 | +0.129 | +8735.04€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 11488 | +0.240 | +10641.43€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 11488 | +0.240 | +10641.43€ | 0 | 23 |
| ✅ GBM_LATE_5M | 17038 | +0.220 | +14428.17€ | 0 | 25 |
| ✅ GBM_LATE_5M#5min | 17038 | +0.220 | +14428.17€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 1948 | +0.253 | +1898.73€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 1948 | +0.253 | +1898.73€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 3338 | +0.210 | +2861.08€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 3338 | +0.210 | +2861.08€ | 0 | 26 |
| ✅ GBM_LATE_5M#DOGE | 1591 | +0.218 | +1323.18€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1591 | +0.218 | +1323.18€ | 0 | 18 |
| ✅ GBM_LATE_5M#ETH | 4961 | +0.211 | +3931.99€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 4961 | +0.211 | +3931.99€ | 0 | 27 |
| ✅ GBM_LATE_5M#SOL | 3027 | +0.230 | +2688.61€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 3027 | +0.230 | +2688.61€ | 0 | 27 |
| ✅ GBM_LATE_5M#XRP | 2173 | +0.211 | +1724.58€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 2173 | +0.211 | +1724.58€ | 0 | 0 |
| ✅ GBM_LATE_60M | 6799 | +0.083 | +2381.67€ | 0 | 8 |
| ✅ GBM_LATE_60M#60min | 6799 | +0.083 | +2381.67€ | 0 | 0 |
| ✅ GBM_LATE_60M#BNB | 218 | +0.268 | +235.77€ | 0 | 0 |
| ✅ GBM_LATE_60M#BNB#60min | 218 | +0.268 | +235.77€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 2091 | +0.061 | +615.51€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 2091 | +0.061 | +615.51€ | 1 | 6 |
| ✅ GBM_LATE_60M#DOGE | 213 | +0.309 | +255.11€ | 0 | 0 |
| ✅ GBM_LATE_60M#DOGE#60min | 213 | +0.309 | +255.11€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH | 1946 | +0.056 | +593.74€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 1946 | +0.056 | +593.74€ | 1 | 6 |
| ✅ GBM_LATE_60M#SOL | 2119 | +0.063 | +417.44€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 2119 | +0.063 | +417.44€ | 0 | 9 |
| ✅ GBM_LATE_60M#XRP | 212 | +0.332 | +264.10€ | 0 | 0 |
| ✅ GBM_LATE_60M#XRP#60min | 212 | +0.332 | +264.10€ | 0 | 23 |
| 🚫 GBM_LATE_60M_FADE | 810 | -0.245 | -34.72€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 810 | -0.245 | -34.72€ | 0 | 0 |
| ✅ GBM_LATE_60M_FADE#BNB | 12 | +0.000 | +4.05€ | 0 | 0 |
| ✅ GBM_LATE_60M_FADE#BNB#60min | 12 | +0.000 | +4.05€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 284 | -0.255 | -20.31€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 284 | -0.255 | -20.31€ | 4 | 0 |
| ✅ GBM_LATE_60M_FADE#DOGE | 9 | -0.061 | +0.70€ | 0 | 0 |
| ✅ GBM_LATE_60M_FADE#DOGE#60min | 9 | -0.061 | +0.70€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 279 | -0.244 | -8.44€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 279 | -0.244 | -8.44€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 222 | -0.245 | -9.74€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 222 | -0.245 | -9.74€ | 4 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 2618 | +0.090 | +694.71€ | 1 | 9 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 2618 | +0.090 | +694.71€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 949 | +0.071 | +241.77€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 949 | +0.071 | +241.77€ | 0 | 4 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#DOGE | 51 | +0.198 | +29.17€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#DOGE#60min | 51 | +0.198 | +29.17€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 832 | +0.053 | +160.11€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 832 | +0.053 | +160.11€ | 0 | 14 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 683 | +0.153 | +242.55€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 683 | +0.153 | +242.55€ | 1 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#XRP | 103 | +0.090 | +21.11€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#XRP#60min | 103 | +0.090 | +21.11€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN | 438 | +0.302 | +515.04€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 438 | +0.302 | +515.04€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 438 | +0.302 | +515.04€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 438 | +0.302 | +515.04€ | 1 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 5053 | +0.095 | +1096.19€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 5053 | +0.095 | +1096.19€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 5053 | +0.095 | +1096.19€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 5053 | +0.095 | +1096.19€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M | 1947 | +0.021 | +117.73€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 1947 | +0.021 | +117.73€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 253 | +0.100 | +58.63€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 253 | +0.100 | +58.63€ | 0 | 4 |
| ✅ LIQUIDACIONES_15M#BTC | 363 | -0.012 | +7.44€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 363 | -0.012 | +7.44€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 154 | +0.051 | +24.30€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 154 | +0.051 | +24.30€ | 1 | 1 |
| ✅ LIQUIDACIONES_15M#ETH | 423 | +0.022 | +21.23€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 423 | +0.022 | +21.23€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 360 | -0.022 | +0.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 360 | -0.022 | +0.09€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 394 | +0.025 | +6.04€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 394 | +0.025 | +6.04€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 4668 | +0.020 | +224.40€ | 4 | 2 |
| ✅ LIQUIDACIONES_5M#5min | 4668 | +0.020 | +224.40€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 241 | +0.002 | -6.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 241 | +0.002 | -6.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 869 | +0.017 | +51.52€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 869 | +0.017 | +51.52€ | 2 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 364 | +0.076 | +106.96€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 364 | +0.076 | +106.96€ | 0 | 4 |
| ✅ LIQUIDACIONES_5M#ETH | 1749 | +0.025 | +41.54€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1749 | +0.025 | +41.54€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 823 | +0.013 | +4.42€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 823 | +0.013 | +4.42€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 622 | -0.005 | +26.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 622 | -0.005 | +26.11€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 2881 | -0.037 | -16.96€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 2881 | -0.037 | -16.96€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 873 | -0.042 | -21.35€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 873 | -0.042 | -21.35€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 1044 | -0.019 | +15.36€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 1044 | -0.019 | +15.36€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 938 | -0.054 | -10.32€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 938 | -0.054 | -10.32€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#XRP | 21 | +0.022 | -0.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#XRP#60min | 21 | +0.022 | -0.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 22159 | -0.033 | -234.26€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 10758 | -0.031 | -69.55€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 11401 | -0.034 | -164.72€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 775 | -0.052 | -39.22€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 399 | -0.039 | -6.85€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 376 | -0.066 | -32.37€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 5990 | -0.025 | -13.81€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 2856 | -0.020 | +23.34€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 3134 | -0.030 | -37.15€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 2006 | -0.035 | -18.06€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 1031 | -0.037 | -18.57€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 975 | -0.033 | +0.51€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 5105 | -0.031 | -47.32€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 2468 | -0.025 | +7.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 2637 | -0.036 | -54.78€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 4214 | -0.028 | +16.51€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 2058 | -0.029 | +3.59€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 2156 | -0.027 | +12.92€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 4069 | -0.045 | -132.36€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 1946 | -0.050 | -78.51€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 2123 | -0.041 | -53.85€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M | 14662 | -0.012 | -218.19€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 14662 | -0.012 | -218.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 578 | -0.010 | -0.50€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC | 3379 | -0.021 | -71.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 3379 | -0.021 | -71.38€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 3075 | -0.015 | -29.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 3075 | -0.015 | -29.21€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL | 3388 | -0.018 | -66.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 3388 | -0.018 | -66.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 78117 | -0.000 | +4176.41€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 78117 | -0.000 | +4176.41€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 14119 | +0.027 | +1963.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 14119 | +0.027 | +1963.05€ | 2 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 11009 | -0.038 | -147.69€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 11009 | -0.038 | -147.69€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 14267 | +0.026 | +1578.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 14267 | +0.026 | +1578.46€ | 1 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 10974 | -0.054 | -297.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 10974 | -0.054 | -297.46€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 13237 | -0.004 | +377.63€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 13237 | -0.004 | +377.63€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 14511 | +0.020 | +702.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 14511 | +0.020 | +702.42€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 7547 | -0.052 | -102.83€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 7547 | -0.052 | -102.83€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1270 | -0.002 | -14.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1270 | -0.002 | -14.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 2183 | -0.057 | -17.08€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 2183 | -0.057 | -17.08€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 102 | -0.019 | -0.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 102 | -0.019 | -0.22€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 825 | -0.117 | -33.69€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 825 | -0.117 | -33.69€ | 6 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 2293 | -0.064 | -8.76€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 2293 | -0.064 | -8.76€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 874 | -0.019 | -28.83€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 874 | -0.019 | -28.83€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3435 | +0.003 | -3.01€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3435 | +0.003 | -3.01€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 133 | -0.033 | -0.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 133 | -0.033 | -0.70€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 247 | -0.006 | -6.03€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 247 | -0.006 | -6.03€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE | 139 | -0.004 | -2.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 139 | -0.004 | -2.34€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1327 | +0.006 | +6.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1327 | +0.006 | +6.88€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1392 | +0.006 | -0.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1392 | +0.006 | -0.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 197 | -0.013 | -0.12€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 197 | -0.013 | -0.12€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 191060 | -0.078 | +2117.27€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 191060 | -0.078 | +2117.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 33490 | -0.076 | +1909.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 33490 | -0.076 | +1909.17€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 28773 | -0.102 | -1439.99€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 28773 | -0.102 | -1439.99€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 33894 | -0.067 | +1650.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 33894 | -0.067 | +1650.49€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 28326 | -0.101 | -1001.86€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 28326 | -0.101 | -1001.86€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 33802 | -0.060 | +156.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 33802 | -0.060 | +156.49€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 32775 | -0.068 | +842.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 32775 | -0.068 | +842.98€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 9414 | -0.035 | -182.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 9414 | -0.035 | -182.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 1014 | -0.017 | -18.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 1014 | -0.017 | -18.55€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 2212 | -0.046 | -29.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 2212 | -0.046 | -29.54€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1011 | -0.020 | -29.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1011 | -0.020 | -29.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2684 | -0.023 | -30.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2684 | -0.023 | -30.37€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1316 | -0.063 | -30.57€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1316 | -0.063 | -30.57€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 1177 | -0.039 | -43.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 1177 | -0.039 | -43.89€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 2428 | +0.121 | +978.59€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#5min | 2292 | +0.124 | +966.00€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 528 | +0.141 | +273.90€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 528 | +0.141 | +273.90€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#DOGE | 481 | +0.119 | +173.54€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 481 | +0.119 | +173.54€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#ETH | 416 | +0.129 | +193.87€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 416 | +0.129 | +193.87€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 391 | +0.134 | +189.37€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 391 | +0.134 | +189.37€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#XRP | 476 | +0.096 | +135.31€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 476 | +0.096 | +135.31€ | 0 | 2 |
| ✅ ORDER_FLOW_5M_REACTIVO | 2571 | -0.022 | -49.75€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 2571 | -0.022 | -49.75€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 449 | +0.005 | +20.50€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 449 | +0.005 | +20.50€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 467 | -0.050 | -33.32€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 467 | -0.050 | -33.32€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 618 | -0.045 | -45.21€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 618 | -0.045 | -45.21€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 532 | -0.009 | -6.17€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 532 | -0.009 | -6.17€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 505 | -0.007 | +14.45€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 505 | -0.007 | +14.45€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 1369 | -0.042 | +144.35€ | 1 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 634 | -0.068 | +29.00€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 496 | -0.064 | +53.87€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 138 | -0.079 | -24.87€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 481 | -0.009 | +75.96€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 350 | +0.009 | +85.64€ | 0 | 2 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 131 | -0.056 | -9.68€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 254 | -0.039 | +39.39€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 216 | -0.037 | +34.97€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 38 | -0.050 | +4.42€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 1062 | -0.035 | +174.48€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 307 | -0.066 | -30.13€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE | 1740 | -0.185 | -32.94€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 689 | -0.173 | -7.66€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 610 | -0.172 | -4.49€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 79 | -0.179 | -3.17€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH | 584 | -0.198 | -32.28€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 515 | -0.204 | -37.39€ | 3 | 1 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 69 | -0.148 | +5.11€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 467 | -0.184 | +7.00€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 433 | -0.180 | +3.86€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 34 | -0.222 | +3.14€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#atexpiry | 1558 | -0.185 | -38.02€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 182 | -0.179 | +5.08€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 609 | +0.374 | +534.96€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#BTC | 141 | +0.178 | +100.38€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 141 | +0.178 | +100.38€ | 0 | 8 |
| ✅ RESOLUTION_SNIPER#ETH | 139 | +0.372 | +108.29€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 139 | +0.372 | +108.29€ | 0 | 9 |
| ✅ RESOLUTION_SNIPER#SOL | 329 | +0.455 | +326.29€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 329 | +0.455 | +326.29€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#sniper | 609 | +0.374 | +534.96€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 1069 | +0.043 | +93.89€ | 2 | 3 |
| ✅ STREAK_FADE_15M#15min | 1069 | +0.043 | +93.89€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 360 | +0.017 | +3.61€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 360 | +0.017 | +3.61€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 83 | +0.029 | +3.15€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 83 | +0.029 | +3.15€ | 1 | 3 |
| ✅ STREAK_FADE_15M#SOL | 86 | +0.034 | +8.76€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 86 | +0.034 | +8.76€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 540 | +0.063 | +78.37€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 540 | +0.063 | +78.37€ | 0 | 3 |
| ✅ STREAK_FADE_5M | 3676 | -0.022 | -140.06€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3676 | -0.022 | -140.06€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 1130 | -0.022 | -39.63€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 1130 | -0.022 | -39.63€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 633 | -0.028 | -26.83€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 633 | -0.028 | -26.83€ | 1 | 0 |
| ✅ STREAK_FADE_5M#SOL | 182 | -0.038 | -14.19€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 182 | -0.038 | -14.19€ | 4 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1731 | -0.018 | -59.41€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1731 | -0.018 | -59.41€ | 1 | 0 |
| ✅ STREAK_FADE_60M | 155 | +0.016 | +1.10€ | 2 | 2 |
| ✅ STREAK_FADE_60M#60min | 155 | +0.016 | +1.10€ | 0 | 0 |
| ✅ STREAK_FADE_60M#BNB | 7 | +0.097 | +7.39€ | 0 | 0 |
| ✅ STREAK_FADE_60M#BNB#60min | 7 | +0.097 | +7.39€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 51 | -0.028 | -2.40€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 51 | -0.028 | -2.40€ | 4 | 0 |
| ✅ STREAK_FADE_60M#SOL | 89 | +0.005 | -5.00€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 89 | +0.005 | -5.00€ | 1 | 1 |
| ✅ STREAK_FADE_60M#XRP | 5 | +0.018 | -0.23€ | 0 | 0 |
| ✅ STREAK_FADE_60M#XRP#60min | 5 | +0.018 | -0.23€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 11750 | +0.013 | +65.07€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 11750 | +0.013 | +65.07€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 3013 | +0.017 | +21.38€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 3013 | +0.017 | +21.38€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 3148 | +0.013 | +25.37€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 3148 | +0.013 | +25.37€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2967 | +0.009 | -0.49€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2967 | +0.009 | -0.49€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2622 | +0.014 | +18.81€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2622 | +0.014 | +18.81€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 14133 | +0.019 | +8.99€ | 4 | 0 |
| ✅ STRUCT_NO_15M#15min | 14133 | +0.019 | +8.99€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 5661 | +0.021 | +9.07€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 5661 | +0.021 | +9.07€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 5032 | +0.019 | +2.27€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 5032 | +0.019 | +2.27€ | 4 | 0 |
| ✅ STRUCT_NO_15M#SOL | 3440 | +0.015 | -2.34€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 3440 | +0.015 | -2.34€ | 1 | 0 |
| ✅ UPDOWN_GBM | 127626 | +0.059 | +12145.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 31917 | +0.077 | +6237.30€ | 0 | 10 |
| ✅ UPDOWN_GBM#240min | 3626 | -0.001 | +39.89€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 83982 | +0.062 | +5742.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 7661 | -0.002 | +128.60€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 11162 | +0.103 | +2058.94€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 2120 | +0.165 | +992.53€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 90 | -0.011 | -2.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 8952 | +0.090 | +1068.41€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 28904 | +0.056 | +2539.10€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 4308 | +0.081 | +968.71€ | 0 | 11 |
| ✅ UPDOWN_GBM#BTC#240min | 1070 | +0.000 | +22.09€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 19915 | +0.065 | +1460.73€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 3453 | -0.004 | +82.94€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 158 | -0.062 | +4.63€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 14238 | +0.074 | +1569.91€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 2084 | +0.155 | +893.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 86 | +0.023 | -0.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 12068 | +0.060 | +677.34€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 29941 | +0.049 | +2124.58€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 7421 | +0.070 | +1152.64€ | 0 | 9 |
| ✅ UPDOWN_GBM#ETH#240min | 1034 | +0.005 | +14.90€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 18514 | +0.051 | +916.94€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 2825 | -0.003 | +37.91€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 147 | -0.097 | +2.18€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 26333 | +0.041 | +1510.43€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 8611 | +0.033 | +487.59€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#240min | 949 | -0.011 | +7.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 15306 | +0.053 | +1016.93€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 1334 | +0.002 | +6.40€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#daily | 133 | -0.137 | -7.88€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 17046 | +0.073 | +2343.96€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 7373 | +0.088 | +1742.39€ | 0 | 11 |
| ✅ UPDOWN_GBM#XRP#240min | 397 | +0.006 | -1.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 9227 | +0.063 | +601.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#60min | 49 | +0.010 | +1.35€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 438 | -0.098 | -1.06€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 1096 | +0.363 | +418.05€ | 0 | 9 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 1096 | +0.363 | +418.05€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 524 | +0.363 | +189.40€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 524 | +0.363 | +189.40€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 572 | +0.362 | +228.65€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 572 | +0.362 | +228.65€ | 0 | 14 |
| ✅ UPDOWN_GBM_15M_TARDIO | 30261 | -0.016 | +7610.95€ | 2 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 30261 | -0.016 | +7610.95€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 2392 | -0.045 | +638.46€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 2392 | -0.045 | +638.46€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 5583 | -0.115 | +332.94€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 5583 | -0.115 | +332.94€ | 5 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 1294 | +0.218 | +1063.04€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 1294 | +0.218 | +1063.04€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 4111 | +0.216 | +2586.36€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 4111 | +0.216 | +2586.36€ | 1 | 20 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 8493 | -0.057 | +1280.38€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 8493 | -0.057 | +1280.38€ | 4 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 8388 | -0.052 | +1709.77€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 8388 | -0.052 | +1709.77€ | 4 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 383 | +0.058 | +34.37€ | 0 | 7 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 383 | +0.058 | +34.37€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 383 | +0.058 | +34.37€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 383 | +0.058 | +34.37€ | 0 | 7 |
| ✅ UPDOWN_GBM_IBS_ALTO | 2012 | +0.285 | +1733.82€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 2012 | +0.285 | +1733.82€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 1057 | +0.280 | +858.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 1057 | +0.280 | +858.70€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 955 | +0.291 | +875.13€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 955 | +0.291 | +875.13€ | 0 | 10 |
| ✅ UPDOWN_OU_5M | 909 | -0.122 | -97.36€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 909 | -0.122 | -97.36€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 312 | -0.080 | -36.02€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 312 | -0.080 | -36.02€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 292 | -0.088 | -24.06€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 292 | -0.088 | -24.06€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 105 | -0.192 | -14.83€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 105 | -0.192 | -14.83€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 128 | -0.200 | -8.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 128 | -0.200 | -8.61€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 5520 | +0.291 | +2401.59€ | 0 | 3 |
| ✅ WEEKLY_PRICE#BTC | 2159 | +0.247 | +346.57€ | 0 | 3 |
| ✅ WEEKLY_PRICE#ETH | 2139 | +0.283 | +875.85€ | 0 | 3 |
| ✅ WEEKLY_PRICE#SOL | 1222 | +0.382 | +1179.17€ | 0 | 1 |