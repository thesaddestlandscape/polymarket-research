# Hipótesis automáticas — 2026-11-27 04:25 UTC
_Generado por shadow_postmortem.py sobre 1510773 resoluciones (PNL=+214589.88€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.495` → IC=-0.239 (n=236)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.113 (n=735)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.195 (n=1125)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.505 (IC base=+0.124)

- **PATRÓN** `n_total_lado` > `60.0` → IC=+0.172 (n=364)

  - _Acción_: Kelly boost +0.86€ cuando `n_total_lado` > 60.0 (IC base=+0.124)

- **PATRÓN** `banda_hit_calibrado` > `0.818` → IC=+0.284 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.818 (IC base=+0.124)

- **PATRÓN** `banda_z` > `8.174` → IC=+0.194 (n=354)

  - _Acción_: Kelly boost +0.97€ cuando `banda_z` > 8.174 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.130 (n=1071)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 6.0 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.134 (n=1151)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.124)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.280 (n=171)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.108 (n=565)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.193 (n=988)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.505 (IC base=+0.126)

- **PATRÓN** `n_total_lado` > `62.0` → IC=+0.183 (n=317)

  - _Acción_: Kelly boost +0.92€ cuando `n_total_lado` > 62.0 (IC base=+0.126)

- **PATRÓN** `banda_hit_calibrado` > `0.817` → IC=+0.280 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.817 (IC base=+0.126)

- **PATRÓN** `banda_z` > `8.273` → IC=+0.196 (n=310)

  - _Acción_: Kelly boost +0.98€ cuando `banda_z` > 8.273 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.137 (n=841)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 8.0 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.130 (n=1051)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.01 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `5105.3697` → IC=+0.131 (n=421)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 5105.3697 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `8586.1585` → IC=+0.129 (n=251)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 8586.1585 (IC base=+0.018)

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
- **FILTRO** `restante_s_al_confirmar` < `130.2` → IC=-0.219 (n=12979)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 130.2
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=38941)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `122.97` → IC=-0.263 (n=1272)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 122.97
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=3816)

### BALLENAS_TARDIAS#BTC#15min
- **PATRÓN** `restante_s_al_confirmar` < `641.55` → IC=+0.135 (n=2569)

  - _Acción_: Kelly boost +0.68€ cuando `restante_s_al_confirmar` < 641.55 (IC base=+0.093)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `114.34` → IC=-0.279 (n=1281)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 114.34
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=3848)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `restante_s_al_confirmar` < `115.36` → IC=-0.162 (n=3676)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 115.36
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=11030)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.209 (n=31277)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `7670.9285` → IC=+0.151 (n=2542)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 7670.9285 (IC base=+0.102)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.126 (n=27987)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 17.0 (IC base=+0.123)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.129 (n=33808)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 7.0 (IC base=+0.123)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.223 (n=25191)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.135 (n=9017)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.123)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.182 (n=2243)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 5.0 (IC base=+0.174)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.358 (n=751)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.174)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.176 (n=2748)

  - _Acción_: Kelly boost +0.88€ cuando `libro_spread` < 0.01 (IC base=+0.174)

- **PATRÓN** `libro_liquidez` > `16174.6054` → IC=+0.182 (n=714)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 16174.6054 (IC base=+0.174)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.185 (n=1963)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 7.0 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.181 (n=2197)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 17.0 (IC base=+0.177)

- **PATRÓN** `py_entrada` < `0.265` → IC=+0.328 (n=764)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.265 (IC base=+0.177)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.180 (n=2809)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.01 (IC base=+0.177)

- **PATRÓN** `libro_liquidez` > `15988.2314` → IC=+0.185 (n=725)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 15988.2314 (IC base=+0.177)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.615` → IC=+0.174 (n=648)

  - _Acción_: Kelly boost +0.87€ cuando `py_entrada` > 0.615 (IC base=+0.075)

- **PATRÓN** `libro_liquidez` > `6825.0558` → IC=+0.126 (n=153)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 6825.0558 (IC base=+0.075)

- **PATRÓN** `py_entrada` < `0.45` → IC=+0.122 (n=2258)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` < 0.45 (IC base=+0.086)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.172 (n=5763)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 6.0 (IC base=+0.169)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.175 (n=2814)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 8.0 (IC base=+0.169)

- **PATRÓN** `py_entrada` > `0.78` → IC=+0.377 (n=1940)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.78 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.199 (n=2767)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 7.0 (IC base=+0.192)

- **PATRÓN** `py_entrada` < `0.275` → IC=+0.329 (n=1015)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.275 (IC base=+0.192)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.196 (n=3211)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.01 (IC base=+0.192)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.143 (n=502)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 18.0 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.144 (n=997)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 11.0 (IC base=+0.138)

- **PATRÓN** `py_entrada` > `0.65` → IC=+0.244 (n=683)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.65 (IC base=+0.138)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=1219)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `4420.281` → IC=+0.152 (n=156)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 4420.281 (IC base=+0.077)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.253 (n=1001)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.230)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.230 (n=2051)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.230)

- **PATRÓN** `py_entrada` > `0.835` → IC=+0.428 (n=1352)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.835 (IC base=+0.230)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.145 (n=1501)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 7.0 (IC base=+0.143)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.153 (n=767)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 7.0 (IC base=+0.143)

- **PATRÓN** `py_entrada` < `0.315` → IC=+0.295 (n=558)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.315 (IC base=+0.143)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `py_entrada` > `0.55` → IC=+0.164 (n=492)

  - _Acción_: Kelly boost +0.82€ cuando `py_entrada` > 0.55 (IC base=+0.052)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.139 (n=561)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 17.0 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.136 (n=1083)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 12.0 (IC base=+0.126)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.256 (n=511)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.126)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `10.0` → IC=-0.295 (n=76)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.237 (n=158)

- **FILTRO** `libro_liquidez` < `8957.4571` → IC=-0.263 (n=175)

  - _Acción_: SKIP cuando `libro_liquidez` < 8957.4571
  - _Potencial_: sin este filtro IC_bueno=-0.238 (n=59)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.197 (n=27948)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 5.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.191 (n=23580)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.191)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.219 (n=8866)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.191)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.336 (n=363)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.191)

- **PATRÓN** `libro_liquidez` > `5024.6381` → IC=+0.335 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5024.6381 (IC base=+0.191)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.166 (n=6360)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.160)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.174 (n=6152)

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

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.209 (n=3969)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.204 (n=2645)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.244 (n=1883)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.203)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.179 (n=6196)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 5.0 (IC base=+0.172)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.172 (n=5246)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 15.0 (IC base=+0.172)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.175 (n=6353)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` < 0.73 (IC base=+0.172)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.180 (n=4886)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` > 0.71 (IC base=+0.172)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.256 (n=4899)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.251)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.251 (n=2374)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.251)

- **PATRÓN** `py_entrada` > `0.8` → IC=+0.362 (n=1684)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.187 (n=6047)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.184)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.189 (n=3841)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 11.0 (IC base=+0.184)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.198 (n=1950)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` > 0.73 (IC base=+0.184)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.427 (n=1055)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.423)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.424 (n=1051)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.423)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.437 (n=1064)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.423)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.429 (n=1123)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.423)

- **PATRÓN** `libro_liquidez` > `14011.0969` → IC=+0.450 (n=341)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14011.0969 (IC base=+0.423)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.437 (n=459)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.437)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.441 (n=453)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.437)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.449 (n=483)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.437)

- **PATRÓN** `libro_liquidez` > `15238.5904` → IC=+0.445 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15238.5904 (IC base=+0.437)

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
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.405 (n=167)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.397)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.396 (n=161)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.397)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.418 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.397)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.765` → IC=-0.306 (n=34)

  - _Acción_: SKIP cuando `py_entrada` > 0.765
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=19)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.244 (n=37)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.208 (n=36567)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.238 (n=35824)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.199)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.184 (n=5471)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 18.0 (IC base=+0.175)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.175 (n=11715)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 12.0 (IC base=+0.175)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.185 (n=16875)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` > 0.71 (IC base=+0.175)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.227 (n=15226)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.223)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.276 (n=6417)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.223)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.191 (n=6272)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 17.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.197 (n=12896)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` > 0.72 (IC base=+0.180)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.855` → IC=-0.357 (n=19)

  - _Acción_: SKIP cuando `py_entrada` < 0.855
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.230 (n=5117)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.220 (n=5889)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.218)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.259 (n=6212)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.218)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **FILTRO** `hora_utc` > `3.0` → IC=-0.278 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.218 (n=5174)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.206)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.252 (n=6521)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.206)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.204 (n=5229)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.199 (n=6078)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.197)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.239 (n=7506)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.197)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.196 (n=13093)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.138 (n=14441)

  - _Acción_: Kelly boost +0.69€ cuando `restante_min` > 4.96 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `3.31` → IC=+0.138 (n=16133)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 3.31 (IC base=+0.116)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.197 (n=6363)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.143 (n=6567)

  - _Acción_: Kelly boost +0.72€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.126 (n=8119)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 7.0 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `3.73` → IC=+0.142 (n=8040)

  - _Acción_: Kelly boost +0.71€ cuando `lag_apertura_s` < 3.73 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.196 (n=6730)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.115)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.134 (n=8693)

  - _Acción_: Kelly boost +0.67€ cuando `restante_min` > 4.95 (IC base=+0.115)

- **PATRÓN** `lag_apertura_s` < `2.86` → IC=+0.134 (n=8094)

  - _Acción_: Kelly boost +0.67€ cuando `lag_apertura_s` < 2.86 (IC base=+0.115)

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
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=136)

- **FILTRO** `py_entrada` > `0.755` → IC=-0.381 (n=40)

  - _Acción_: SKIP cuando `py_entrada` > 0.755
  - _Potencial_: sin este filtro IC_bueno=-0.153 (n=122)

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
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=136)

- **FILTRO** `py_entrada` > `0.755` → IC=-0.381 (n=40)

  - _Acción_: SKIP cuando `py_entrada` > 0.755
  - _Potencial_: sin este filtro IC_bueno=-0.153 (n=122)

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
- **PATRÓN** `drift_60min` |x|≤ `0.511` → IC=+0.140 (n=20989)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.511 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.129 (n=21250)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 6.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.126 (n=14590)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 12.0 (IC base=+0.124)

- **PATRÓN** `ibs_20min` > `0.973` → IC=+0.247 (n=6998)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.973 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` > `0.8809` → IC=+0.289 (n=1158)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8809 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.462` → IC=+0.189 (n=10525)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 3.462 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` > `0.6932` → IC=+0.266 (n=5749)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6932 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` > `0.3027` → IC=+0.255 (n=2165)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3027 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` > `2.7417` → IC=+0.233 (n=5079)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7417 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.139 (n=10058)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `4999.2146` → IC=+0.150 (n=6996)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 4999.2146 (IC base=+0.124)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.123 (n=13279)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0067 (IC base=+0.087)

- **PATRÓN** `ibs_20min` < `0.5647` → IC=+0.144 (n=26545)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.5647 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` > `0.681` → IC=+0.193 (n=1808)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.681 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` < `0.1795` → IC=+0.194 (n=10910)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` < 0.1795 (IC base=+0.087)

- **PATRÓN** `volumen_regimen` < `0.8563` → IC=+0.196 (n=7400)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 0.8563 (IC base=+0.087)

- **PATRÓN** `volumen_pendiente_norm` > `0.2963` → IC=+0.229 (n=2692)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2963 (IC base=+0.087)

- **PATRÓN** `volumen_spike_ratio` > `1.4564` → IC=+0.208 (n=18817)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4564 (IC base=+0.087)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.227 (n=18800)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 100.0 (IC base=+0.087)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `drift_60min` |x|≤ `0.3062` → IC=+0.213 (n=3920)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3062 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.223 (n=2171)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.210)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.213 (n=2977)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `0.9823` → IC=+0.272 (n=2019)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9823 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.431` → IC=+0.272 (n=1988)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.431 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.2335` → IC=+0.259 (n=777)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2335 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `1.4379` → IC=+0.212 (n=4283)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4379 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.221 (n=4619)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `2059.05` → IC=+0.214 (n=1485)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2059.05 (IC base=+0.210)

- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.243 (n=1838)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0099 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.0975` → IC=+0.266 (n=1352)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0975 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.239 (n=4213)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.237)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.242 (n=1861)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` < `0.0827` → IC=+0.273 (n=1351)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0827 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` < `0.0727` → IC=+0.239 (n=3506)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0727 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.2885` → IC=+0.245 (n=540)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2885 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `1.8558` → IC=+0.242 (n=2589)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8558 (IC base=+0.237)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.240 (n=4347)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.237)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.229 (n=1685)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.219)

- **PATRÓN** `drift_60min` |x|≤ `0.1164` → IC=+0.245 (n=1686)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1164 (IC base=+0.219)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.231 (n=4017)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.219)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.220 (n=2729)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.219)

- **PATRÓN** `ibs_20min` > `0.8881` → IC=+0.246 (n=1276)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8881 (IC base=+0.219)

- **PATRÓN** `dist_vwap_pct` > `0.2058` → IC=+0.228 (n=1658)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2058 (IC base=+0.219)

- **PATRÓN** `dist_vwap_pct` < `0.5775` → IC=+0.220 (n=4226)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5775 (IC base=+0.219)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.693` → IC=+0.260 (n=544)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.693 (IC base=+0.219)

- **PATRÓN** `volumen_regimen` > `0.6958` → IC=+0.227 (n=3420)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6958 (IC base=+0.219)

- **PATRÓN** `volumen_pendiente_norm` > `0.2763` → IC=+0.262 (n=527)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2763 (IC base=+0.219)

- **PATRÓN** `volumen_spike_ratio` > `2.4328` → IC=+0.243 (n=1261)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4328 (IC base=+0.219)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.158 (n=3690)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0062 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.3654` → IC=+0.144 (n=4191)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.3654 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.151 (n=1575)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 17.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` < `0.5915` → IC=+0.179 (n=3687)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.5915 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.1569` → IC=+0.151 (n=4114)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.1569 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.574` → IC=+0.137 (n=654)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 10.574 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.973` → IC=+0.142 (n=3860)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 3.973 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `0.628` → IC=+0.157 (n=1397)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.628 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.0977` → IC=+0.158 (n=1521)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` > 0.0977 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `2.4459` → IC=+0.143 (n=4057)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.4459 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `166.0` → IC=+0.184 (n=1344)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 166.0 (IC base=+0.136)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0119` → IC=+0.211 (n=2141)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0119 (IC base=+0.194)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.203 (n=4969)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.194)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.253 (n=1824)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.194)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.891` → IC=+0.276 (n=1046)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.891 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` < `0.0968` → IC=+0.193 (n=4235)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` < 0.0968 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` > `0.3496` → IC=+0.224 (n=606)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3496 (IC base=+0.194)

- **PATRÓN** `volumen_spike_ratio` > `2.7343` → IC=+0.210 (n=2094)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7343 (IC base=+0.194)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.198 (n=5543)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.04 (IC base=+0.194)

- **PATRÓN** `libro_liquidez` > `1900.1556` → IC=+0.202 (n=2140)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1900.1556 (IC base=+0.194)

- **PATRÓN** `sigma_h` < `0.0083` → IC=+0.226 (n=1948)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0083 (IC base=+0.220)

- **PATRÓN** `sigma_h` > `0.0115` → IC=+0.221 (n=2010)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0115 (IC base=+0.220)

- **PATRÓN** `drift_60min` |x|≤ `0.3084` → IC=+0.229 (n=2951)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3084 (IC base=+0.220)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.240 (n=1674)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.220)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.226 (n=2017)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.220)

- **PATRÓN** `ibs_20min` < `0.0549` → IC=+0.268 (n=1477)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0549 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.611` → IC=+0.266 (n=473)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.611 (IC base=+0.220)

- **PATRÓN** `volumen_pendiente_norm` > `0.3457` → IC=+0.253 (n=645)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3457 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` > `2.1563` → IC=+0.230 (n=2853)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1563 (IC base=+0.220)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.223 (n=2041)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.220)

- **PATRÓN** `libro_liquidez` > `1881.693` → IC=+0.224 (n=2006)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1881.693 (IC base=+0.220)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.220 (n=4253)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 21.0 (IC base=+0.220)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.169 (n=264)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.070 (n=5697)

- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.137 (n=767)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` < 0.0041 (IC base=+0.070)

- **PATRÓN** `ibs_20min` > `0.9414` → IC=+0.247 (n=764)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9414 (IC base=+0.070)

- **PATRÓN** `dist_vwap_pct` > `0.1609` → IC=+0.347 (n=529)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1609 (IC base=+0.070)

- **PATRÓN** `dist_vwap_pct` < `0.3757` → IC=+0.341 (n=904)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3757 (IC base=+0.070)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.225` → IC=+0.216 (n=1684)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.225 (IC base=+0.070)

- **PATRÓN** `volumen_regimen` < `0.8667` → IC=+0.342 (n=630)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8667 (IC base=+0.070)

- **PATRÓN** `volumen_regimen` > `1.2462` → IC=+0.361 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2462 (IC base=+0.070)

- **PATRÓN** `volumen_pendiente_norm` < `0.165` → IC=+0.344 (n=768)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.165 (IC base=+0.070)

- **PATRÓN** `volumen_pendiente_norm` > `0.2994` → IC=+0.358 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2994 (IC base=+0.070)

- **PATRÓN** `volumen_spike_ratio` < `1.4165` → IC=+0.368 (n=308)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4165 (IC base=+0.070)

- **PATRÓN** `volumen_spike_ratio` > `2.2709` → IC=+0.346 (n=419)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2709 (IC base=+0.070)

- **PATRÓN** `ballena_activa_n` < `143.0` → IC=+0.349 (n=932)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 143.0 (IC base=+0.070)

- **PATRÓN** `ibs_20min` < `0.0867` → IC=+0.188 (n=1491)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.0867 (IC base=+0.060)

- **PATRÓN** `dist_vwap_pct` > `0.3678` → IC=+0.156 (n=739)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.3678 (IC base=+0.060)

- **PATRÓN** `dist_vwap_pct` < `0.1554` → IC=+0.155 (n=2810)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1554 (IC base=+0.060)

- **PATRÓN** `volumen_regimen` < `0.8246` → IC=+0.162 (n=1962)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8246 (IC base=+0.060)

- **PATRÓN** `volumen_pendiente_norm` > `0.278` → IC=+0.198 (n=375)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.278 (IC base=+0.060)

- **PATRÓN** `volumen_spike_ratio` > `2.431` → IC=+0.171 (n=946)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 2.431 (IC base=+0.060)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.177 (n=165)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=924)

- **FILTRO** `ibs_20min` < `0.2759` → IC=-0.181 (n=271)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2759
  - _Potencial_: sin este filtro IC_bueno=+0.090 (n=818)

- **FILTRO** `ibs_20min` > `0.1923` → IC=-0.125 (n=5593)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1923
  - _Potencial_: sin este filtro IC_bueno=+0.159 (n=2763)

- **FILTRO** `sigma_ewma_delta_pct` > `8.315` → IC=-0.226 (n=906)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.315
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=7450)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.177 (n=373)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.75 (IC base=+0.022)

- **PATRÓN** `dist_vwap_pct` > `0.9803` → IC=+0.283 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9803 (IC base=+0.022)

- **PATRÓN** `dist_vwap_pct` < `1.3529` → IC=+0.262 (n=384)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 1.3529 (IC base=+0.022)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.712` → IC=+0.174 (n=170)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 6.712 (IC base=+0.022)

- **PATRÓN** `volumen_regimen` > `1.005` → IC=+0.309 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.005 (IC base=+0.022)

- **PATRÓN** `volumen_pendiente_norm` < `0.1591` → IC=+0.269 (n=371)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1591 (IC base=+0.022)

- **PATRÓN** `volumen_spike_ratio` < `1.7847` → IC=+0.277 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7847 (IC base=+0.022)

- **PATRÓN** `volumen_spike_ratio` > `1.5387` → IC=+0.256 (n=297)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5387 (IC base=+0.022)

- **PATRÓN** `ibs_20min` < `0.1923` → IC=+0.159 (n=2763)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.1923 (IC base=-0.031)

- **PATRÓN** `dist_vwap_pct` > `0.8369` → IC=+0.299 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8369 (IC base=-0.031)

- **PATRÓN** `dist_vwap_pct` < `0.2408` → IC=+0.291 (n=1307)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2408 (IC base=-0.031)

- **PATRÓN** `volumen_regimen` < `0.6948` → IC=+0.307 (n=559)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6948 (IC base=-0.031)

- **PATRÓN** `volumen_pendiente_norm` > `0.0783` → IC=+0.319 (n=578)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0783 (IC base=-0.031)

- **PATRÓN** `volumen_spike_ratio` < `2.4493` → IC=+0.305 (n=1197)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4493 (IC base=-0.031)

- **PATRÓN** `volumen_spike_ratio` > `1.525` → IC=+0.299 (n=1069)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.525 (IC base=-0.031)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `ibs_20min` < `0.7949` → IC=-0.161 (n=4290)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7949
  - _Potencial_: sin este filtro IC_bueno=+0.147 (n=2211)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.177 (n=1377)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=5124)

- **FILTRO** `ibs_20min` > `0.72` → IC=-0.190 (n=2246)

  - _Acción_: SKIP cuando `ibs_20min` > 0.72
  - _Potencial_: sin este filtro IC_bueno=+0.074 (n=6770)

- **PATRÓN** `ibs_20min` > `0.7949` → IC=+0.147 (n=2211)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` > 0.7949 (IC base=-0.056)

- **PATRÓN** `dist_vwap_pct` > `0.4517` → IC=+0.341 (n=462)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4517 (IC base=-0.056)

- **PATRÓN** `volumen_regimen` > `0.7043` → IC=+0.317 (n=1184)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7043 (IC base=-0.056)

- **PATRÓN** `volumen_pendiente_norm` > `0.3087` → IC=+0.320 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3087 (IC base=-0.056)

- **PATRÓN** `volumen_spike_ratio` > `2.5382` → IC=+0.314 (n=433)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5382 (IC base=-0.056)

- **PATRÓN** `dist_vwap_pct` > `1.1098` → IC=+0.292 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1098 (IC base=+0.008)

- **PATRÓN** `volumen_regimen` < `0.636` → IC=+0.274 (n=899)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.636 (IC base=+0.008)

- **PATRÓN** `volumen_regimen` > `1.213` → IC=+0.277 (n=899)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.213 (IC base=+0.008)

- **PATRÓN** `volumen_pendiente_norm` > `0.1083` → IC=+0.273 (n=967)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1083 (IC base=+0.008)

- **PATRÓN** `volumen_spike_ratio` < `2.5121` → IC=+0.262 (n=2566)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5121 (IC base=+0.008)

- **PATRÓN** `volumen_spike_ratio` > `1.446` → IC=+0.267 (n=2566)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.446 (IC base=+0.008)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.186 (n=9181)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0113 (IC base=+0.087)

- **PATRÓN** `ibs_20min` > `0.8667` → IC=+0.284 (n=12495)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8667 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` > `1.0085` → IC=+0.304 (n=1911)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0085 (IC base=+0.087)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.456` → IC=+0.169 (n=12412)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 3.456 (IC base=+0.087)

- **PATRÓN** `volumen_regimen` > `0.6924` → IC=+0.279 (n=9210)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6924 (IC base=+0.087)

- **PATRÓN** `volumen_pendiente_norm` > `0.2933` → IC=+0.296 (n=2279)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2933 (IC base=+0.087)

- **PATRÓN** `volumen_spike_ratio` > `2.6501` → IC=+0.289 (n=5342)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6501 (IC base=+0.087)

- **PATRÓN** `ballena_activa_n` < `88.0` → IC=+0.309 (n=15677)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 88.0 (IC base=+0.087)

- **PATRÓN** `sigma_h` > `0.0073` → IC=+0.137 (n=17865)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` > 0.0073 (IC base=+0.089)

- **PATRÓN** `ibs_20min` < `0.5158` → IC=+0.174 (n=23575)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.5158 (IC base=+0.089)

- **PATRÓN** `dist_vwap_pct` < `0.2837` → IC=+0.282 (n=9534)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2837 (IC base=+0.089)

- **PATRÓN** `volumen_regimen` < `0.6918` → IC=+0.279 (n=4043)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6918 (IC base=+0.089)

- **PATRÓN** `volumen_regimen` > `1.1864` → IC=+0.286 (n=3063)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1864 (IC base=+0.089)

- **PATRÓN** `volumen_pendiente_norm` > `0.2951` → IC=+0.321 (n=2019)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2951 (IC base=+0.089)

- **PATRÓN** `volumen_spike_ratio` < `1.4544` → IC=+0.302 (n=4559)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4544 (IC base=+0.089)

- **PATRÓN** `volumen_spike_ratio` > `2.2751` → IC=+0.304 (n=6200)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2751 (IC base=+0.089)

- **PATRÓN** `ballena_activa_n` < `70.0` → IC=+0.311 (n=13661)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 70.0 (IC base=+0.089)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.8195` → IC=-0.149 (n=4867)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8195
  - _Potencial_: sin este filtro IC_bueno=+0.316 (n=2508)

- **FILTRO** `ibs_20min` > `0.6978` → IC=-0.242 (n=1674)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6978
  - _Potencial_: sin este filtro IC_bueno=+0.063 (n=5025)

- **FILTRO** `sigma_ewma_delta_pct` > `4.058` → IC=-0.241 (n=1404)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.058
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=5295)

- **PATRÓN** `ibs_20min` > `0.8195` → IC=+0.316 (n=2508)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8195 (IC base=+0.009)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.164` → IC=+0.177 (n=2742)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 2.164 (IC base=+0.009)

- **PATRÓN** `volumen_pendiente_norm` > `0.2301` → IC=+0.334 (n=468)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2301 (IC base=+0.009)

- **PATRÓN** `volumen_spike_ratio` < `1.4472` → IC=+0.296 (n=773)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4472 (IC base=+0.009)

- **PATRÓN** `volumen_spike_ratio` > `2.2332` → IC=+0.318 (n=1050)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2332 (IC base=+0.009)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.326 (n=1550)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.009)

- **PATRÓN** `ibs_20min` < `0.1702` → IC=+0.170 (n=1677)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.1702 (IC base=-0.013)

- **PATRÓN** `volumen_pendiente_norm` < `0.1559` → IC=+0.383 (n=1527)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1559 (IC base=-0.013)

- **PATRÓN** `volumen_spike_ratio` < `2.6471` → IC=+0.387 (n=1463)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.6471 (IC base=-0.013)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.1838` → IC=+0.229 (n=1119)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1838 (IC base=+0.010)

- **PATRÓN** `dist_vwap_pct` < `0.5278` → IC=+0.214 (n=2988)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5278 (IC base=+0.010)

- **PATRÓN** `volumen_regimen` > `0.694` → IC=+0.221 (n=2406)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.694 (IC base=+0.010)

- **PATRÓN** `volumen_pendiente_norm` > `0.2725` → IC=+0.242 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2725 (IC base=+0.010)

- **PATRÓN** `volumen_spike_ratio` < `1.4148` → IC=+0.230 (n=888)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4148 (IC base=+0.010)

- **PATRÓN** `volumen_spike_ratio` > `2.4465` → IC=+0.223 (n=888)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4465 (IC base=+0.010)

- **PATRÓN** `ballena_activa_n` < `312.0` → IC=+0.237 (n=2344)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 312.0 (IC base=+0.010)

- **PATRÓN** `dist_vwap_pct` < `0.5774` → IC=+0.256 (n=2399)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5774 (IC base=+0.005)

- **PATRÓN** `volumen_regimen` > `1.0128` → IC=+0.268 (n=909)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0128 (IC base=+0.005)

- **PATRÓN** `volumen_pendiente_norm` > `0.2706` → IC=+0.281 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2706 (IC base=+0.005)

- **PATRÓN** `volumen_spike_ratio` < `1.5311` → IC=+0.257 (n=857)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5311 (IC base=+0.005)

- **PATRÓN** `volumen_spike_ratio` > `2.1516` → IC=+0.259 (n=883)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1516 (IC base=+0.005)

- **PATRÓN** `ballena_activa_n` < `175.0` → IC=+0.275 (n=661)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 175.0 (IC base=+0.005)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0118` → IC=+0.317 (n=1706)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0118 (IC base=+0.285)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.293 (n=3770)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.285)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.323 (n=2038)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.285)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.563` → IC=+0.305 (n=2558)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.563 (IC base=+0.285)

- **PATRÓN** `volumen_pendiente_norm` < `0.1306` → IC=+0.293 (n=3490)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1306 (IC base=+0.285)

- **PATRÓN** `volumen_spike_ratio` > `2.1664` → IC=+0.295 (n=2438)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1664 (IC base=+0.285)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.293 (n=4389)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.285)

- **PATRÓN** `libro_liquidez` > `2013.026` → IC=+0.300 (n=1251)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2013.026 (IC base=+0.285)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.301 (n=2397)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.285)

- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.337 (n=1586)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.307)

- **PATRÓN** `drift_60min` |x|≤ `0.189` → IC=+0.328 (n=1541)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.189 (IC base=+0.307)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.322 (n=1344)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.307)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.312 (n=1583)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.307)

- **PATRÓN** `ibs_20min` > `0.1579` → IC=+0.321 (n=2333)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1579 (IC base=+0.307)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.949` → IC=+0.321 (n=400)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.949 (IC base=+0.307)

- **PATRÓN** `volumen_pendiente_norm` < `0.199` → IC=+0.308 (n=3478)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.199 (IC base=+0.307)

- **PATRÓN** `volumen_pendiente_norm` > `0.3448` → IC=+0.314 (n=562)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3448 (IC base=+0.307)

- **PATRÓN** `volumen_spike_ratio` > `2.7501` → IC=+0.325 (n=1539)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7501 (IC base=+0.307)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.308 (n=1625)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.307)

- **PATRÓN** `libro_liquidez` > `1571.4888` → IC=+0.313 (n=3125)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1571.4888 (IC base=+0.307)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.309 (n=3011)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 20.0 (IC base=+0.307)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **PATRÓN** `dist_vwap_pct` > `0.1617` → IC=+0.236 (n=1249)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1617 (IC base=+0.026)

- **PATRÓN** `dist_vwap_pct` < `0.6421` → IC=+0.231 (n=2802)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6421 (IC base=+0.026)

- **PATRÓN** `volumen_regimen` < `1.1742` → IC=+0.234 (n=2546)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1742 (IC base=+0.026)

- **PATRÓN** `volumen_regimen` > `0.5971` → IC=+0.231 (n=2546)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.5971 (IC base=+0.026)

- **PATRÓN** `volumen_pendiente_norm` < `0.1626` → IC=+0.235 (n=2679)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1626 (IC base=+0.026)

- **PATRÓN** `volumen_pendiente_norm` > `0.103` → IC=+0.237 (n=827)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.103 (IC base=+0.026)

- **PATRÓN** `volumen_spike_ratio` < `2.4118` → IC=+0.238 (n=2475)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4118 (IC base=+0.026)

- **PATRÓN** `ballena_activa_n` < `115.0` → IC=+0.249 (n=2528)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 115.0 (IC base=+0.026)

- **PATRÓN** `dist_vwap_pct` < `0.391` → IC=+0.260 (n=2067)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.391 (IC base=+0.014)

- **PATRÓN** `volumen_regimen` < `1.1729` → IC=+0.262 (n=1863)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1729 (IC base=+0.014)

- **PATRÓN** `volumen_regimen` > `0.6129` → IC=+0.258 (n=1863)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6129 (IC base=+0.014)

- **PATRÓN** `volumen_pendiente_norm` < `0.1002` → IC=+0.264 (n=1752)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1002 (IC base=+0.014)

- **PATRÓN** `volumen_pendiente_norm` > `0.2813` → IC=+0.285 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2813 (IC base=+0.014)

- **PATRÓN** `volumen_spike_ratio` < `1.7812` → IC=+0.282 (n=1199)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7812 (IC base=+0.014)

- **PATRÓN** `volumen_spike_ratio` > `2.4232` → IC=+0.267 (n=599)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4232 (IC base=+0.014)

- **PATRÓN** `ballena_activa_n` < `98.0` → IC=+0.284 (n=1616)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 98.0 (IC base=+0.014)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.75` → IC=-0.249 (n=2804)

  - _Acción_: SKIP cuando `ibs_20min` < 0.75
  - _Potencial_: sin este filtro IC_bueno=+0.317 (n=2852)

- **FILTRO** `ibs_20min` > `0.6` → IC=-0.234 (n=1334)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.168 (n=4015)

- **FILTRO** `sigma_ewma_delta_pct` > `8.256` → IC=-0.259 (n=613)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.256
  - _Potencial_: sin este filtro IC_bueno=+0.110 (n=4736)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.317 (n=2852)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.75 (IC base=+0.036)

- **PATRÓN** `dist_vwap_pct` > `1.1232` → IC=+0.354 (n=408)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1232 (IC base=+0.036)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.461` → IC=+0.161 (n=2316)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 2.461 (IC base=+0.036)

- **PATRÓN** `volumen_regimen` < `0.8422` → IC=+0.351 (n=1392)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8422 (IC base=+0.036)

- **PATRÓN** `volumen_regimen` > `0.6962` → IC=+0.338 (n=1865)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6962 (IC base=+0.036)

- **PATRÓN** `volumen_pendiente_norm` < `0.1003` → IC=+0.338 (n=1970)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1003 (IC base=+0.036)

- **PATRÓN** `volumen_pendiente_norm` > `0.2752` → IC=+0.370 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2752 (IC base=+0.036)

- **PATRÓN** `volumen_spike_ratio` < `1.7946` → IC=+0.357 (n=1355)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7946 (IC base=+0.036)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.357 (n=1816)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 42.0 (IC base=+0.036)

- **PATRÓN** `ibs_20min` < `0.6` → IC=+0.168 (n=4015)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` < 0.6 (IC base=+0.068)

- **PATRÓN** `dist_vwap_pct` < `0.3259` → IC=+0.273 (n=2191)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3259 (IC base=+0.068)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.725` → IC=+0.136 (n=4193)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 4.725 (IC base=+0.068)

- **PATRÓN** `volumen_regimen` < `0.6872` → IC=+0.284 (n=933)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6872 (IC base=+0.068)

- **PATRÓN** `volumen_pendiente_norm` > `0.0724` → IC=+0.299 (n=848)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0724 (IC base=+0.068)

- **PATRÓN** `volumen_spike_ratio` < `1.807` → IC=+0.283 (n=1374)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.807 (IC base=+0.068)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.289 (n=2102)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=+0.068)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.349 (n=2666)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.312)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.315 (n=3007)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.312)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.315 (n=3134)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.312)

- **PATRÓN** `ibs_20min` > `0.651` → IC=+0.336 (n=2983)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.651 (IC base=+0.312)

- **PATRÓN** `dist_vwap_pct` > `0.2206` → IC=+0.336 (n=1586)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2206 (IC base=+0.312)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.735` → IC=+0.342 (n=1184)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.735 (IC base=+0.312)

- **PATRÓN** `volumen_regimen` > `0.7029` → IC=+0.327 (n=2665)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7029 (IC base=+0.312)

- **PATRÓN** `volumen_pendiente_norm` > `0.2884` → IC=+0.342 (n=427)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2884 (IC base=+0.312)

- **PATRÓN** `volumen_spike_ratio` > `1.5404` → IC=+0.326 (n=2579)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5404 (IC base=+0.312)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.313 (n=3782)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.312)

- **PATRÓN** `libro_liquidez` > `2996.8018` → IC=+0.322 (n=995)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2996.8018 (IC base=+0.312)

- **PATRÓN** `sigma_h` > `0.0093` → IC=+0.330 (n=3206)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0093 (IC base=+0.314)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.317 (n=3213)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.314)

- **PATRÓN** `ibs_20min` < `0.39` → IC=+0.327 (n=3206)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.39 (IC base=+0.314)

- **PATRÓN** `dist_vwap_pct` > `1.3078` → IC=+0.323 (n=381)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.3078 (IC base=+0.314)

- **PATRÓN** `dist_vwap_pct` < `0.2603` → IC=+0.316 (n=3166)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2603 (IC base=+0.314)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.65` → IC=+0.329 (n=437)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.65 (IC base=+0.314)

- **PATRÓN** `volumen_regimen` < `0.6351` → IC=+0.317 (n=1070)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6351 (IC base=+0.314)

- **PATRÓN** `volumen_regimen` > `1.2096` → IC=+0.340 (n=1069)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2096 (IC base=+0.314)

- **PATRÓN** `volumen_pendiente_norm` > `0.2895` → IC=+0.357 (n=445)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2895 (IC base=+0.314)

- **PATRÓN** `volumen_spike_ratio` < `1.4172` → IC=+0.323 (n=1006)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4172 (IC base=+0.314)

- **PATRÓN** `volumen_spike_ratio` > `2.1632` → IC=+0.318 (n=1368)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1632 (IC base=+0.314)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0129` → IC=+0.219 (n=6723)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0129 (IC base=+0.173)

- **PATRÓN** `drift_60min` |x|≤ `0.1286` → IC=+0.193 (n=8864)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.1286 (IC base=+0.173)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.184 (n=20927)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.173)

- **PATRÓN** `ibs_20min` > `0.534` → IC=+0.228 (n=20147)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.534 (IC base=+0.173)

- **PATRÓN** `dist_vwap_pct` > `0.1715` → IC=+0.205 (n=7560)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1715 (IC base=+0.173)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.685` → IC=+0.259 (n=3950)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.685 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` < `1.1722` → IC=+0.152 (n=13442)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.1722 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` > `0.6196` → IC=+0.151 (n=13443)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.6196 (IC base=+0.173)

- **PATRÓN** `volumen_pendiente_norm` > `0.2936` → IC=+0.207 (n=2899)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2936 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` > `2.6055` → IC=+0.185 (n=6546)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.6055 (IC base=+0.173)

- **PATRÓN** `ballena_activa_n` < `85.0` → IC=+0.192 (n=19112)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 85.0 (IC base=+0.173)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.193 (n=8852)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0063 (IC base=+0.185)

- **PATRÓN** `drift_60min` |x|≤ `0.0863` → IC=+0.222 (n=6698)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0863 (IC base=+0.185)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.206 (n=9640)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.185)

- **PATRÓN** `ibs_20min` < `0.529` → IC=+0.236 (n=20091)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.529 (IC base=+0.185)

- **PATRÓN** `dist_vwap_pct` < `0.1994` → IC=+0.179 (n=14703)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` < 0.1994 (IC base=+0.185)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.369` → IC=+0.189 (n=3154)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 9.369 (IC base=+0.185)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.483` → IC=+0.191 (n=17985)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` < 2.483 (IC base=+0.185)

- **PATRÓN** `volumen_regimen` < `1.1897` → IC=+0.165 (n=14226)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.1897 (IC base=+0.185)

- **PATRÓN** `volumen_pendiente_norm` > `0.2961` → IC=+0.216 (n=3015)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2961 (IC base=+0.185)

- **PATRÓN** `volumen_spike_ratio` < `1.5648` → IC=+0.184 (n=8466)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` < 1.5648 (IC base=+0.185)

- **PATRÓN** `volumen_spike_ratio` > `2.6396` → IC=+0.195 (n=6412)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.6396 (IC base=+0.185)

- **PATRÓN** `ballena_activa_n` < `90.0` → IC=+0.198 (n=19080)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 90.0 (IC base=+0.185)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `drift_60min` |x|≤ `0.0765` → IC=+0.267 (n=1104)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0765 (IC base=+0.228)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.235 (n=3452)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.228)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.229 (n=2238)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.228)

- **PATRÓN** `ibs_20min` > `0.9415` → IC=+0.291 (n=2204)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9415 (IC base=+0.228)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.473` → IC=+0.325 (n=1084)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.473 (IC base=+0.228)

- **PATRÓN** `volumen_pendiente_norm` > `0.2821` → IC=+0.285 (n=491)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2821 (IC base=+0.228)

- **PATRÓN** `volumen_spike_ratio` < `1.8308` → IC=+0.226 (n=2113)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8308 (IC base=+0.228)

- **PATRÓN** `volumen_spike_ratio` > `1.4336` → IC=+0.227 (n=3169)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4336 (IC base=+0.228)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.237 (n=3439)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.228)

- **PATRÓN** `sigma_h` < `0.0105` → IC=+0.252 (n=2797)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0105 (IC base=+0.250)

- **PATRÓN** `drift_60min` |x|≤ `0.1024` → IC=+0.306 (n=1232)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1024 (IC base=+0.250)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.254 (n=2881)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.250)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.253 (n=2552)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.250)

- **PATRÓN** `ibs_20min` < `0.0072` → IC=+0.306 (n=933)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0072 (IC base=+0.250)

- **PATRÓN** `sigma_ewma_delta_pct` < `1.952` → IC=+0.255 (n=2775)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 1.952 (IC base=+0.250)

- **PATRÓN** `volumen_pendiente_norm` < `0.1008` → IC=+0.253 (n=2476)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1008 (IC base=+0.250)

- **PATRÓN** `volumen_pendiente_norm` > `0.3016` → IC=+0.264 (n=421)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3016 (IC base=+0.250)

- **PATRÓN** `volumen_spike_ratio` < `1.5533` → IC=+0.262 (n=1184)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5533 (IC base=+0.250)

- **PATRÓN** `volumen_spike_ratio` > `2.6767` → IC=+0.254 (n=897)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6767 (IC base=+0.250)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.254 (n=3028)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.250)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.190 (n=1030)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0034 (IC base=+0.127)

- **PATRÓN** `drift_60min` |x|≤ `0.0953` → IC=+0.169 (n=1359)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.0953 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.145 (n=3220)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.127)

- **PATRÓN** `ibs_20min` > `0.2429` → IC=+0.201 (n=3088)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2429 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` > `0.1981` → IC=+0.210 (n=1483)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1981 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.497` → IC=+0.203 (n=554)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.497 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` < `0.8511` → IC=+0.136 (n=2059)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.8511 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` > `1.1915` → IC=+0.128 (n=1030)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` > 1.1915 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` > `0.2749` → IC=+0.168 (n=471)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` > 0.2749 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` < `1.5085` → IC=+0.130 (n=1340)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 1.5085 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` > `2.4534` → IC=+0.137 (n=1014)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 2.4534 (IC base=+0.127)

- **PATRÓN** `ballena_activa_n` < `382.0` → IC=+0.130 (n=3012)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 382.0 (IC base=+0.127)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.181 (n=2948)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0062 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.2622` → IC=+0.175 (n=2946)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.2622 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.176 (n=1601)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 15.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` < `0.6184` → IC=+0.209 (n=3346)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6184 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` < `0.2269` → IC=+0.175 (n=3640)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.2269 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.86` → IC=+0.177 (n=617)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 10.86 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.025` → IC=+0.156 (n=2945)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 4.025 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` < `1.2049` → IC=+0.162 (n=3346)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2049 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` < `0.0968` → IC=+0.154 (n=2943)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` < 0.0968 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `2.148` → IC=+0.158 (n=2832)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.148 (IC base=+0.153)

- **PATRÓN** `ballena_activa_n` < `202.0` → IC=+0.196 (n=1390)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 202.0 (IC base=+0.153)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.012` → IC=+0.231 (n=1541)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.012 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.2606` → IC=+0.234 (n=2266)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2606 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.219 (n=3552)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.286 (n=1801)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.988` → IC=+0.303 (n=807)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.988 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.3496` → IC=+0.235 (n=481)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3496 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `2.1692` → IC=+0.218 (n=2217)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1692 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.213 (n=3994)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `2011.1284` → IC=+0.223 (n=1133)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2011.1284 (IC base=+0.210)

- **PATRÓN** `sigma_h` < `0.0124` → IC=+0.242 (n=3077)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0124 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.256` → IC=+0.265 (n=2047)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.256 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.272 (n=1159)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` < `0.0465` → IC=+0.290 (n=1353)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0465 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.689` → IC=+0.280 (n=403)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.689 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.3528` → IC=+0.279 (n=510)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3528 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` < `1.7646` → IC=+0.241 (n=1311)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7646 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `2.1802` → IC=+0.248 (n=1986)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1802 (IC base=+0.237)

- **PATRÓN** `libro_liquidez` > `1878.6774` → IC=+0.247 (n=1392)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1878.6774 (IC base=+0.237)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.236 (n=2969)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 23.0 (IC base=+0.237)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.189 (n=1114)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.004 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.083` → IC=+0.170 (n=1110)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.083 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.137 (n=3443)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` > `0.2412` → IC=+0.187 (n=3327)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.2412 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` > `0.1511` → IC=+0.188 (n=1868)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1511 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.175` → IC=+0.198 (n=565)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 11.175 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `0.8352` → IC=+0.138 (n=2218)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 0.8352 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` > `0.2869` → IC=+0.179 (n=499)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.2869 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `1.515` → IC=+0.125 (n=1434)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 1.515 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` > `2.5003` → IC=+0.136 (n=1086)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 2.5003 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `6920.671` → IC=+0.196 (n=1508)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 6920.671 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `123.0` → IC=+0.127 (n=3264)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 123.0 (IC base=+0.126)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.173 (n=2371)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0058 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.4405` → IC=+0.151 (n=3550)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.4405 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.163 (n=1706)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 15.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` < `0.6713` → IC=+0.188 (n=3550)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.6713 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` < `0.1748` → IC=+0.157 (n=3643)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.1748 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.496` → IC=+0.142 (n=1208)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 6.496 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `0.8521` → IC=+0.151 (n=2368)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.8521 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` > `0.2922` → IC=+0.169 (n=535)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` > 0.2922 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` < `2.1878` → IC=+0.134 (n=2978)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 2.1878 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` > `1.4096` → IC=+0.135 (n=3384)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 1.4096 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `6662.7463` → IC=+0.190 (n=1609)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 6662.7463 (IC base=+0.133)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.155 (n=1134)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 48.0 (IC base=+0.133)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0132` → IC=+0.177 (n=1235)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.0132 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.137 (n=3808)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` > `0.4722` → IC=+0.206 (n=3706)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4722 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` > `0.8016` → IC=+0.213 (n=942)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8016 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.868` → IC=+0.281 (n=775)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.868 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` < `1.1668` → IC=+0.132 (n=3706)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 1.1668 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` > `0.6237` → IC=+0.126 (n=3705)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` > 0.6237 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` < `0.1632` → IC=+0.125 (n=3781)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.1632 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` > `0.2817` → IC=+0.133 (n=515)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_pendiente_norm` > 0.2817 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` < `1.5452` → IC=+0.128 (n=1584)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 1.5452 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `2710.9922` → IC=+0.198 (n=1680)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 2710.9922 (IC base=+0.123)

- **PATRÓN** `ballena_activa_n` < `26.0` → IC=+0.129 (n=2358)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 26.0 (IC base=+0.123)

- **PATRÓN** `sigma_h` < `0.0113` → IC=+0.152 (n=3420)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0113 (IC base=+0.124)

- **PATRÓN** `drift_60min` |x|≤ `0.1194` → IC=+0.170 (n=1295)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.1194 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.139 (n=3959)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.124)

- **PATRÓN** `ibs_20min` < `0.6471` → IC=+0.220 (n=3884)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6471 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` < `0.2295` → IC=+0.146 (n=3859)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.2295 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.229` → IC=+0.146 (n=3441)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 2.229 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` < `1.1823` → IC=+0.129 (n=3883)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.1823 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` > `0.8584` → IC=+0.125 (n=2591)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` > 0.8584 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` > `0.2786` → IC=+0.153 (n=545)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` > 0.2786 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` < `1.442` → IC=+0.142 (n=1232)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.442 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` > `2.4691` → IC=+0.136 (n=1233)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 2.4691 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `2606.152` → IC=+0.192 (n=1761)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 2606.152 (IC base=+0.124)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.131 (n=3693)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 42.0 (IC base=+0.124)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0123` → IC=+0.248 (n=2970)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0123 (IC base=+0.224)

- **PATRÓN** `drift_60min` |x|≤ `0.4636` → IC=+0.232 (n=2925)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4636 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.229 (n=3452)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.226 (n=2994)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` > `0.6667` → IC=+0.253 (n=3324)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6667 (IC base=+0.224)

- **PATRÓN** `dist_vwap_pct` > `0.1867` → IC=+0.233 (n=2044)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1867 (IC base=+0.224)

- **PATRÓN** `dist_vwap_pct` < `0.842` → IC=+0.226 (n=3436)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.842 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.505` → IC=+0.263 (n=1570)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.505 (IC base=+0.224)

- **PATRÓN** `volumen_regimen` > `0.6165` → IC=+0.233 (n=3324)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6165 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` > `0.2901` → IC=+0.266 (n=456)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2901 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` > `1.5393` → IC=+0.227 (n=2901)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5393 (IC base=+0.224)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.225 (n=4243)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.224)

- **PATRÓN** `libro_liquidez` > `2869.9646` → IC=+0.230 (n=1507)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2869.9646 (IC base=+0.224)

- **PATRÓN** `sigma_h` > `0.0159` → IC=+0.247 (n=2301)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0159 (IC base=+0.238)

- **PATRÓN** `drift_60min` |x|≤ `0.6217` → IC=+0.247 (n=3449)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6217 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.250 (n=1693)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.238)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.242 (n=1548)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.238)

- **PATRÓN** `ibs_20min` < `0.0388` → IC=+0.297 (n=1519)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0388 (IC base=+0.238)

- **PATRÓN** `dist_vwap_pct` > `1.1962` → IC=+0.254 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1962 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.985` → IC=+0.272 (n=652)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.985 (IC base=+0.238)

- **PATRÓN** `volumen_regimen` < `0.8647` → IC=+0.244 (n=2299)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8647 (IC base=+0.238)

- **PATRÓN** `volumen_regimen` > `1.0488` → IC=+0.239 (n=1563)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0488 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` > `0.2891` → IC=+0.299 (n=486)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2891 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` < `1.8564` → IC=+0.237 (n=2183)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8564 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` > `1.5615` → IC=+0.238 (n=2924)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5615 (IC base=+0.238)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.202 (n=1755)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.154)

- **PATRÓN** `drift_60min` |x|≤ `0.1455` → IC=+0.168 (n=2316)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.1455 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.165 (n=5501)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.154)

- **PATRÓN** `ibs_20min` > `0.296` → IC=+0.189 (n=5264)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.296 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` > `0.9188` → IC=+0.179 (n=798)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.9188 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.508` → IC=+0.211 (n=848)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.508 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` < `0.8538` → IC=+0.163 (n=3207)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8538 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` > `1.1863` → IC=+0.158 (n=1603)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 1.1863 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` > `0.1551` → IC=+0.173 (n=1354)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.1551 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` < `1.5247` → IC=+0.157 (n=2262)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.5247 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` > `1.806` → IC=+0.156 (n=3427)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.806 (IC base=+0.154)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.156 (n=5793)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.02 (IC base=+0.154)

- **PATRÓN** `libro_liquidez` > `7293.4233` → IC=+0.191 (n=2387)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 7293.4233 (IC base=+0.154)

- **PATRÓN** `ibs_20min` < `0.7105` → IC=+0.141 (n=5797)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` < 0.7105 (IC base=+0.099)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.139 (n=2557)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 22.0 (IC base=+0.099)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.203 (n=1143)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0057 (IC base=+0.193)

- **PATRÓN** `drift_60min` |x|≤ `0.0809` → IC=+0.231 (n=433)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0809 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.224 (n=1173)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.193)

- **PATRÓN** `ibs_20min` > `0.6069` → IC=+0.250 (n=865)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6069 (IC base=+0.193)

- **PATRÓN** `dist_vwap_pct` > `0.6942` → IC=+0.240 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6942 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.833` → IC=+0.229 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.833 (IC base=+0.193)

- **PATRÓN** `volumen_regimen` < `0.8658` → IC=+0.210 (n=865)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8658 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` > `0.0887` → IC=+0.215 (n=454)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0887 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` < `2.1491` → IC=+0.203 (n=1121)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1491 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` > `1.4006` → IC=+0.196 (n=1274)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.4006 (IC base=+0.193)

- **PATRÓN** `libro_liquidez` > `15568.6179` → IC=+0.207 (n=588)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15568.6179 (IC base=+0.193)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.154 (n=545)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0033 (IC base=+0.071)

- **PATRÓN** `ibs_20min` < `0.2163` → IC=+0.188 (n=716)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.2163 (IC base=+0.071)

- **PATRÓN** `ballena_activa_n` < `164.0` → IC=+0.169 (n=702)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 164.0 (IC base=+0.071)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.237 (n=542)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0038 (IC base=+0.142)

- **PATRÓN** `drift_60min` |x|≤ `0.1349` → IC=+0.155 (n=714)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.1349 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.160 (n=1680)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 5.0 (IC base=+0.142)

- **PATRÓN** `ibs_20min` > `0.7593` → IC=+0.258 (n=734)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7593 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` > `0.1582` → IC=+0.165 (n=768)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.1582 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.976` → IC=+0.184 (n=229)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 9.976 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` < `0.8285` → IC=+0.152 (n=1079)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.8285 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` > `0.1552` → IC=+0.181 (n=412)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.1552 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` > `1.7716` → IC=+0.155 (n=1065)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.7716 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `7799.6121` → IC=+0.175 (n=734)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 7799.6121 (IC base=+0.142)

- **PATRÓN** `ballena_activa_n` < `30.0` → IC=+0.143 (n=530)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 30.0 (IC base=+0.142)

- **PATRÓN** `sigma_h` < `0.0082` → IC=+0.124 (n=1617)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0082 (IC base=+0.109)

- **PATRÓN** `ibs_20min` < `0.1809` → IC=+0.210 (n=711)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1809 (IC base=+0.109)

- **PATRÓN** `volumen_regimen` < `0.6746` → IC=+0.137 (n=711)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.6746 (IC base=+0.109)

- **PATRÓN** `volumen_pendiente_norm` > `0.223` → IC=+0.133 (n=276)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` > 0.223 (IC base=+0.109)

- **PATRÓN** `volumen_spike_ratio` < `1.3989` → IC=+0.136 (n=525)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.3989 (IC base=+0.109)

- **PATRÓN** `libro_liquidez` > `4044.6118` → IC=+0.138 (n=1444)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 4044.6118 (IC base=+0.109)

- **PATRÓN** `ballena_activa_n` < `41.0` → IC=+0.146 (n=709)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 41.0 (IC base=+0.109)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` < `0.0073` → IC=+0.152 (n=472)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0073 (IC base=+0.122)

- **PATRÓN** `sigma_h` > `0.0129` → IC=+0.135 (n=474)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` > 0.0129 (IC base=+0.122)

- **PATRÓN** `drift_60min` |x|≤ `0.1349` → IC=+0.122 (n=472)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.61€ cuando `drift_60min` |x|≤ 0.1349 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.140 (n=1416)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 6.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` > `0.7273` → IC=+0.224 (n=946)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7273 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` > `0.5097` → IC=+0.147 (n=451)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` > 0.5097 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.863` → IC=+0.230 (n=372)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.863 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` < `1.0426` → IC=+0.132 (n=1245)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 1.0426 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` > `0.701` → IC=+0.127 (n=1263)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` > 0.701 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` > `0.2221` → IC=+0.149 (n=243)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.2221 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` < `1.4156` → IC=+0.154 (n=458)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 1.4156 (IC base=+0.122)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.122 (n=1428)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.02 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `3048.1866` → IC=+0.150 (n=472)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 3048.1866 (IC base=+0.122)

- **PATRÓN** `ballena_activa_n` < `9.0` → IC=+0.136 (n=440)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 9.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` < `0.6923` → IC=+0.145 (n=1584)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.6923 (IC base=+0.079)

- **PATRÓN** `libro_liquidez` > `2742.3207` → IC=+0.162 (n=717)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 2742.3207 (IC base=+0.079)

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

- **PATRÓN** `volumen_pendiente_norm` < `0.2469` → IC=+0.191 (n=516)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` < 0.2469 (IC base=+0.173)

- **PATRÓN** `volumen_pendiente_norm` > `0.0806` → IC=+0.191 (n=176)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.0806 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` < `2.5077` → IC=+0.193 (n=451)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 2.5077 (IC base=+0.173)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.190 (n=485)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.03 (IC base=+0.173)

- **PATRÓN** `libro_liquidez` > `2678.1143` → IC=+0.199 (n=320)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 2678.1143 (IC base=+0.173)

- **PATRÓN** `sigma_h` > `0.0105` → IC=+0.178 (n=538)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` > 0.0105 (IC base=+0.163)

- **PATRÓN** `drift_60min` |x|≤ `0.5762` → IC=+0.170 (n=473)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.5762 (IC base=+0.163)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.214 (n=180)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.163)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.174 (n=474)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.5 (IC base=+0.163)

- **PATRÓN** `ibs_20min` > `0.186` → IC=+0.168 (n=480)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` > 0.186 (IC base=+0.163)

- **PATRÓN** `dist_vwap_pct` > `1.2297` → IC=+0.300 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2297 (IC base=+0.163)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.882` → IC=+0.164 (n=582)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` < 4.882 (IC base=+0.163)

- **PATRÓN** `volumen_regimen` < `0.8755` → IC=+0.201 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8755 (IC base=+0.163)

- **PATRÓN** `volumen_pendiente_norm` < `0.1149` → IC=+0.179 (n=503)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` < 0.1149 (IC base=+0.163)

- **PATRÓN** `volumen_pendiente_norm` > `0.242` → IC=+0.201 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.242 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` < `1.4975` → IC=+0.214 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4975 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` > `2.6713` → IC=+0.180 (n=173)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 2.6713 (IC base=+0.163)

- **PATRÓN** `libro_liquidez` > `2230.8308` → IC=+0.166 (n=480)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2230.8308 (IC base=+0.163)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.178 (n=461)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 15.0 (IC base=+0.163)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0129` → IC=+0.226 (n=8881)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0129 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.191 (n=27823)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` > `0.9656` → IC=+0.298 (n=8881)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9656 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` > `0.9572` → IC=+0.216 (n=3076)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9572 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.862` → IC=+0.259 (n=6517)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.862 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` < `0.8654` → IC=+0.163 (n=11982)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8654 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.2925` → IC=+0.217 (n=3491)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2925 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `2.6337` → IC=+0.193 (n=8688)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.6337 (IC base=+0.180)

- **PATRÓN** `libro_liquidez` > `1765.74` → IC=+0.181 (n=26643)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 1765.74 (IC base=+0.180)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.199 (n=25294)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 100.0 (IC base=+0.180)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.199 (n=8266)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0056 (IC base=+0.198)

- **PATRÓN** `sigma_h` > `0.0126` → IC=+0.207 (n=8270)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0126 (IC base=+0.198)

- **PATRÓN** `drift_60min` |x|≤ `0.1144` → IC=+0.203 (n=8263)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1144 (IC base=+0.198)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.217 (n=9270)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.198)

- **PATRÓN** `ibs_20min` < `0.49` → IC=+0.251 (n=21817)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.49 (IC base=+0.198)

- **PATRÓN** `dist_vwap_pct` < `0.1946` → IC=+0.182 (n=15858)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` < 0.1946 (IC base=+0.198)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.491` → IC=+0.205 (n=23130)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.491 (IC base=+0.198)

- **PATRÓN** `volumen_regimen` < `0.6261` → IC=+0.181 (n=5536)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 0.6261 (IC base=+0.198)

- **PATRÓN** `volumen_pendiente_norm` > `0.2941` → IC=+0.255 (n=3406)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2941 (IC base=+0.198)

- **PATRÓN** `volumen_spike_ratio` > `2.6298` → IC=+0.210 (n=7954)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6298 (IC base=+0.198)

- **PATRÓN** `ballena_activa_n` < `58.0` → IC=+0.219 (n=20908)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 58.0 (IC base=+0.198)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `drift_60min` |x|≤ `0.3104` → IC=+0.236 (n=3735)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3104 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.239 (n=4459)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.234)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.236 (n=2846)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.315 (n=1683)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.038` → IC=+0.299 (n=2790)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.038 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.2321` → IC=+0.288 (n=749)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2321 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.2818` → IC=+0.240 (n=1864)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2818 (IC base=+0.234)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.246 (n=4381)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `2059.05` → IC=+0.237 (n=1415)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2059.05 (IC base=+0.234)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.267 (n=1299)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0057 (IC base=+0.262)

- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.263 (n=1767)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0099 (IC base=+0.262)

- **PATRÓN** `drift_60min` |x|≤ `0.1299` → IC=+0.288 (n=1714)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1299 (IC base=+0.262)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.265 (n=4041)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.262)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.264 (n=3511)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.262)

- **PATRÓN** `ibs_20min` < `0.4708` → IC=+0.284 (n=3427)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4708 (IC base=+0.262)

- **PATRÓN** `volumen_pendiente_norm` < `0.0991` → IC=+0.265 (n=3560)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0991 (IC base=+0.262)

- **PATRÓN** `volumen_pendiente_norm` > `0.2909` → IC=+0.285 (n=542)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2909 (IC base=+0.262)

- **PATRÓN** `volumen_spike_ratio` < `1.5664` → IC=+0.263 (n=1652)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5664 (IC base=+0.262)

- **PATRÓN** `volumen_spike_ratio` > `2.6409` → IC=+0.270 (n=1252)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6409 (IC base=+0.262)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.266 (n=4182)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.262)

- **PATRÓN** `ballena_activa_n` < `6.0` → IC=+0.264 (n=1330)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 6.0 (IC base=+0.262)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.168 (n=1930)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0039 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.0845` → IC=+0.147 (n=1462)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.0845 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.152 (n=4569)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 5.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` > `0.1867` → IC=+0.186 (n=4386)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.1867 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.741` → IC=+0.208 (n=748)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.741 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.003` → IC=+0.174 (n=685)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 11.003 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `0.6328` → IC=+0.156 (n=1462)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.6328 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` > `1.0626` → IC=+0.142 (n=1988)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 1.0626 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.2716` → IC=+0.190 (n=611)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.2716 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `2.1671` → IC=+0.143 (n=3799)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.1671 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `1.5193` → IC=+0.145 (n=3856)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.5193 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `288.0` → IC=+0.151 (n=2854)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 288.0 (IC base=+0.139)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.169 (n=3411)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0062 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.085` → IC=+0.175 (n=1292)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.085 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.169 (n=1433)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 17.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` < `0.3239` → IC=+0.232 (n=2584)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3239 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` < `0.1577` → IC=+0.162 (n=3814)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.1577 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.188` → IC=+0.150 (n=3958)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 6.188 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `1.0401` → IC=+0.157 (n=3409)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.0401 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.2216` → IC=+0.198 (n=707)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2216 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `2.4323` → IC=+0.150 (n=3761)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.4323 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` > `1.7751` → IC=+0.152 (n=2507)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.7751 (IC base=+0.146)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.147 (n=5029)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `211.0` → IC=+0.183 (n=1227)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 211.0 (IC base=+0.146)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0122` → IC=+0.243 (n=2008)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0122 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.234 (n=4652)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.224 (n=3950)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.297 (n=1646)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.881` → IC=+0.312 (n=987)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.881 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` > `0.204` → IC=+0.234 (n=1171)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.204 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` > `1.7698` → IC=+0.231 (n=3878)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7698 (IC base=+0.224)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.229 (n=5186)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.224)

- **PATRÓN** `libro_liquidez` > `1897.303` → IC=+0.237 (n=2008)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1897.303 (IC base=+0.224)

- **PATRÓN** `sigma_h` < `0.0083` → IC=+0.248 (n=1886)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0083 (IC base=+0.243)

- **PATRÓN** `drift_60min` |x|≤ `0.1864` → IC=+0.259 (n=1883)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1864 (IC base=+0.243)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.263 (n=1620)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.243)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.246 (n=1958)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.243)

- **PATRÓN** `ibs_20min` < `0.0707` → IC=+0.295 (n=1426)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0707 (IC base=+0.243)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.86` → IC=+0.303 (n=445)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.86 (IC base=+0.243)

- **PATRÓN** `volumen_pendiente_norm` > `0.3463` → IC=+0.299 (n=639)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3463 (IC base=+0.243)

- **PATRÓN** `volumen_spike_ratio` > `2.1737` → IC=+0.255 (n=2762)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1737 (IC base=+0.243)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.249 (n=1985)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.243)

- **PATRÓN** `libro_liquidez` > `1993.5362` → IC=+0.253 (n=1425)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1993.5362 (IC base=+0.243)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.246 (n=3633)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 19.0 (IC base=+0.243)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.187 (n=1544)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.004 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.3614` → IC=+0.147 (n=4056)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.3614 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.151 (n=4785)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 5.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` > `0.8747` → IC=+0.261 (n=1537)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8747 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.1529` → IC=+0.169 (n=2261)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.1529 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.959` → IC=+0.161 (n=2009)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 2.959 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `0.856` → IC=+0.153 (n=3073)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.856 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.2782` → IC=+0.201 (n=610)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2782 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `1.5173` → IC=+0.154 (n=1985)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 1.5173 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `2.1516` → IC=+0.143 (n=2044)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 2.1516 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `5911.3854` → IC=+0.229 (n=2089)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5911.3854 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `85.0` → IC=+0.142 (n=2998)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 85.0 (IC base=+0.139)

- **PATRÓN** `sigma_h` < `0.0083` → IC=+0.170 (n=3908)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0083 (IC base=+0.152)

- **PATRÓN** `drift_60min` |x|≤ `0.4672` → IC=+0.163 (n=3903)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.4672 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.177 (n=1440)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.152)

- **PATRÓN** `ibs_20min` < `0.3466` → IC=+0.240 (n=2604)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3466 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` < `0.6448` → IC=+0.158 (n=4523)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.6448 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.033` → IC=+0.157 (n=779)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 9.033 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.019` → IC=+0.155 (n=3401)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 3.019 (IC base=+0.152)

- **PATRÓN** `volumen_regimen` < `0.8497` → IC=+0.162 (n=2602)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8497 (IC base=+0.152)

- **PATRÓN** `volumen_pendiente_norm` > `0.29` → IC=+0.210 (n=502)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.29 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` < `2.4844` → IC=+0.156 (n=3784)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.4844 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` > `1.5224` → IC=+0.158 (n=3382)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.5224 (IC base=+0.152)

- **PATRÓN** `libro_liquidez` > `6724.8531` → IC=+0.217 (n=1301)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6724.8531 (IC base=+0.152)

- **PATRÓN** `ballena_activa_n` < `57.0` → IC=+0.171 (n=1281)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 57.0 (IC base=+0.152)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0133` → IC=+0.157 (n=1564)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0133 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.149 (n=3322)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 11.0 (IC base=+0.121)

- **PATRÓN** `ibs_20min` > `0.697` → IC=+0.256 (n=3128)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.697 (IC base=+0.121)

- **PATRÓN** `dist_vwap_pct` > `1.0688` → IC=+0.199 (n=773)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0688 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.195` → IC=+0.269 (n=1193)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.195 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` < `1.2091` → IC=+0.127 (n=4692)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` < 1.2091 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` < `0.1017` → IC=+0.124 (n=4473)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.1017 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` > `0.2791` → IC=+0.141 (n=589)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` > 0.2791 (IC base=+0.121)

- **PATRÓN** `volumen_spike_ratio` < `2.5079` → IC=+0.125 (n=4585)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 2.5079 (IC base=+0.121)

- **PATRÓN** `libro_liquidez` > `2772.0947` → IC=+0.237 (n=1564)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2772.0947 (IC base=+0.121)

- **PATRÓN** `sigma_h` < `0.0114` → IC=+0.158 (n=3859)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0114 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.1441` → IC=+0.149 (n=1464)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.1441 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.149 (n=4507)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 5.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` < `0.5455` → IC=+0.246 (n=3866)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5455 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` < `0.2284` → IC=+0.152 (n=4045)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.2284 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.021` → IC=+0.161 (n=4261)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` < 3.021 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `1.1936` → IC=+0.142 (n=4384)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 1.1936 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.2327` → IC=+0.201 (n=768)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2327 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `1.4399` → IC=+0.163 (n=1397)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 1.4399 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `2.4964` → IC=+0.143 (n=1397)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 2.4964 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `2646.8913` → IC=+0.225 (n=1461)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2646.8913 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.150 (n=4216)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 47.0 (IC base=+0.137)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0109` → IC=+0.254 (n=4289)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0109 (IC base=+0.235)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.240 (n=4484)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.235)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.239 (n=2866)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.235)

- **PATRÓN** `ibs_20min` > `0.9873` → IC=+0.302 (n=1430)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9873 (IC base=+0.235)

- **PATRÓN** `dist_vwap_pct` > `0.204` → IC=+0.249 (n=2172)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.204 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.923` → IC=+0.298 (n=772)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.923 (IC base=+0.235)

- **PATRÓN** `volumen_regimen` > `0.6395` → IC=+0.241 (n=4286)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6395 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` > `0.2961` → IC=+0.260 (n=544)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2961 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` > `2.5294` → IC=+0.254 (n=1401)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5294 (IC base=+0.235)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.236 (n=5450)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.235)

- **PATRÓN** `libro_liquidez` > `2645.421` → IC=+0.238 (n=2857)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2645.421 (IC base=+0.235)

- **PATRÓN** `sigma_h` > `0.0245` → IC=+0.271 (n=1484)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0245 (IC base=+0.245)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.251 (n=4184)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.245)

- **PATRÓN** `ibs_20min` < `0.14` → IC=+0.305 (n=1959)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.14 (IC base=+0.245)

- **PATRÓN** `dist_vwap_pct` > `1.1987` → IC=+0.252 (n=562)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1987 (IC base=+0.245)

- **PATRÓN** `dist_vwap_pct` < `0.2323` → IC=+0.250 (n=4287)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2323 (IC base=+0.245)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.91` → IC=+0.282 (n=822)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.91 (IC base=+0.245)

- **PATRÓN** `volumen_regimen` < `0.6361` → IC=+0.248 (n=1483)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6361 (IC base=+0.245)

- **PATRÓN** `volumen_regimen` > `1.2193` → IC=+0.266 (n=1483)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2193 (IC base=+0.245)

- **PATRÓN** `volumen_pendiente_norm` > `0.2891` → IC=+0.313 (n=608)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2891 (IC base=+0.245)

- **PATRÓN** `volumen_spike_ratio` > `1.4366` → IC=+0.250 (n=4231)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4366 (IC base=+0.245)

- **PATRÓN** `ballena_activa_n` < `26.0` → IC=+0.246 (n=3699)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 26.0 (IC base=+0.245)

### GBM_LATE_5M
- **PATRÓN** `sigma_h` < `0.0109` → IC=+0.233 (n=6624)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0109 (IC base=+0.227)

- **PATRÓN** `drift_60min` |x|≤ `0.5406` → IC=+0.234 (n=7525)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5406 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.235 (n=7546)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.227)

- **PATRÓN** `ibs_20min` > `0.9286` → IC=+0.260 (n=2510)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9286 (IC base=+0.227)

- **PATRÓN** `dist_vwap_pct` < `0.9686` → IC=+0.229 (n=6187)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.9686 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.436` → IC=+0.236 (n=2510)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.436 (IC base=+0.227)

- **PATRÓN** `volumen_regimen` < `0.7051` → IC=+0.231 (n=2361)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7051 (IC base=+0.227)

- **PATRÓN** `volumen_regimen` > `0.8777` → IC=+0.229 (n=3575)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8777 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` > `0.164` → IC=+0.236 (n=2105)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.164 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` < `1.4493` → IC=+0.237 (n=2468)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4493 (IC base=+0.227)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.231 (n=5371)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.227)

- **PATRÓN** `libro_liquidez` > `3770.877` → IC=+0.234 (n=5016)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3770.877 (IC base=+0.227)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.229 (n=1806)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.211)

- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.211 (n=2452)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0101 (IC base=+0.211)

- **PATRÓN** `drift_60min` |x|≤ `0.419` → IC=+0.222 (n=4752)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.419 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.226 (n=1812)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.211)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.222 (n=2448)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` < `0.6132` → IC=+0.215 (n=4752)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6132 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` > `0.7151` → IC=+0.220 (n=930)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7151 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.677` → IC=+0.224 (n=4916)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.677 (IC base=+0.211)

- **PATRÓN** `volumen_regimen` < `1.2537` → IC=+0.211 (n=4906)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2537 (IC base=+0.211)

- **PATRÓN** `volumen_regimen` > `0.7288` → IC=+0.204 (n=4383)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7288 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` < `0.0984` → IC=+0.213 (n=4996)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0984 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` < `1.5356` → IC=+0.217 (n=2340)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5356 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `1.8218` → IC=+0.219 (n=3545)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8218 (IC base=+0.211)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.236 (n=3564)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 49.0 (IC base=+0.211)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.280 (n=640)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0046 (IC base=+0.273)

- **PATRÓN** `drift_60min` |x|≤ `0.0863` → IC=+0.304 (n=320)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0863 (IC base=+0.273)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.280 (n=1017)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.273)

- **PATRÓN** `ibs_20min` < `0.8361` → IC=+0.280 (n=959)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.8361 (IC base=+0.273)

- **PATRÓN** `dist_vwap_pct` < `0.2` → IC=+0.286 (n=884)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2 (IC base=+0.273)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.118` → IC=+0.300 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.118 (IC base=+0.273)

- **PATRÓN** `volumen_regimen` < `1.2271` → IC=+0.278 (n=959)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2271 (IC base=+0.273)

- **PATRÓN** `volumen_regimen` > `0.8786` → IC=+0.292 (n=639)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8786 (IC base=+0.273)

- **PATRÓN** `volumen_pendiente_norm` > `0.2862` → IC=+0.341 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2862 (IC base=+0.273)

- **PATRÓN** `volumen_spike_ratio` < `2.4917` → IC=+0.281 (n=954)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4917 (IC base=+0.273)

- **PATRÓN** `libro_liquidez` > `12942.3284` → IC=+0.285 (n=639)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12942.3284 (IC base=+0.273)

- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.260 (n=519)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0032 (IC base=+0.170)

- **PATRÓN** `drift_60min` |x|≤ `0.3904` → IC=+0.186 (n=1552)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.3904 (IC base=+0.170)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.211 (n=570)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.170)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.173 (n=583)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 5.0 (IC base=+0.170)

- **PATRÓN** `ibs_20min` < `0.1382` → IC=+0.192 (n=683)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.1382 (IC base=+0.170)

- **PATRÓN** `dist_vwap_pct` > `0.3612` → IC=+0.173 (n=334)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.3612 (IC base=+0.170)

- **PATRÓN** `dist_vwap_pct` < `0.5575` → IC=+0.171 (n=1860)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` < 0.5575 (IC base=+0.170)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.338` → IC=+0.191 (n=1525)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` < 6.338 (IC base=+0.170)

- **PATRÓN** `volumen_regimen` < `1.0921` → IC=+0.185 (n=1365)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 1.0921 (IC base=+0.170)

- **PATRÓN** `volumen_pendiente_norm` > `0.1523` → IC=+0.185 (n=474)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.1523 (IC base=+0.170)

- **PATRÓN** `volumen_spike_ratio` < `2.496` → IC=+0.176 (n=1543)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 2.496 (IC base=+0.170)

- **PATRÓN** `volumen_spike_ratio` > `2.1745` → IC=+0.172 (n=700)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.1745 (IC base=+0.170)

- **PATRÓN** `libro_liquidez` > `14616.0048` → IC=+0.170 (n=704)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 14616.0048 (IC base=+0.170)

- **PATRÓN** `ballena_activa_n` < `702.0` → IC=+0.186 (n=1506)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 702.0 (IC base=+0.170)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `drift_60min` |x|≤ `0.6134` → IC=+0.217 (n=1087)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6134 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.230 (n=984)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` < `0.711` → IC=+0.217 (n=725)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.711 (IC base=+0.211)

- **PATRÓN** `ibs_20min` > `0.9885` → IC=+0.253 (n=362)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9885 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.268` → IC=+0.248 (n=399)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.268 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.2052` → IC=+0.248 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2052 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `1.7957` → IC=+0.218 (n=967)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7957 (IC base=+0.211)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.221 (n=969)

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
- **PATRÓN** `sigma_h` < `0.0076` → IC=+0.224 (n=1836)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0076 (IC base=+0.215)

- **PATRÓN** `drift_60min` |x|≤ `0.4741` → IC=+0.221 (n=2083)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4741 (IC base=+0.215)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.244 (n=725)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.215)

- **PATRÓN** `ibs_20min` < `0.4677` → IC=+0.231 (n=1389)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4677 (IC base=+0.215)

- **PATRÓN** `ibs_20min` > `0.8315` → IC=+0.215 (n=694)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8315 (IC base=+0.215)

- **PATRÓN** `dist_vwap_pct` < `0.4283` → IC=+0.225 (n=2095)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4283 (IC base=+0.215)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.231` → IC=+0.221 (n=2117)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 6.231 (IC base=+0.215)

- **PATRÓN** `volumen_regimen` < `0.8625` → IC=+0.217 (n=1389)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8625 (IC base=+0.215)

- **PATRÓN** `volumen_regimen` > `1.2299` → IC=+0.221 (n=694)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2299 (IC base=+0.215)

- **PATRÓN** `volumen_pendiente_norm` < `0.0981` → IC=+0.217 (n=1936)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0981 (IC base=+0.215)

- **PATRÓN** `volumen_pendiente_norm` > `0.1592` → IC=+0.215 (n=588)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1592 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` < `1.4017` → IC=+0.233 (n=679)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4017 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` > `1.4931` → IC=+0.216 (n=1817)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4931 (IC base=+0.215)

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.247 (n=563)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0045 (IC base=+0.206)

- **PATRÓN** `drift_60min` |x|≤ `0.511` → IC=+0.220 (n=1685)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.511 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.216 (n=625)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.206)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.217 (n=1130)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.206)

- **PATRÓN** `ibs_20min` > `0.0847` → IC=+0.214 (n=1685)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.0847 (IC base=+0.206)

- **PATRÓN** `dist_vwap_pct` > `0.7294` → IC=+0.221 (n=331)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7294 (IC base=+0.206)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.199` → IC=+0.211 (n=1539)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.199 (IC base=+0.206)

- **PATRÓN** `volumen_regimen` < `1.1036` → IC=+0.213 (n=1483)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1036 (IC base=+0.206)

- **PATRÓN** `volumen_regimen` > `0.7178` → IC=+0.211 (n=1505)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7178 (IC base=+0.206)

- **PATRÓN** `volumen_pendiente_norm` > `0.0726` → IC=+0.229 (n=696)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0726 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` < `2.1617` → IC=+0.208 (n=1452)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1617 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` > `1.7691` → IC=+0.210 (n=1100)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7691 (IC base=+0.206)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.209 (n=2182)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.206)

- **PATRÓN** `ballena_activa_n` < `96.0` → IC=+0.210 (n=1681)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 96.0 (IC base=+0.206)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0079` → IC=+0.235 (n=444)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0079 (IC base=+0.222)

- **PATRÓN** `sigma_h` > `0.0135` → IC=+0.233 (n=443)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0135 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.252 (n=1194)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.221 (n=1215)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.302 (n=443)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.222)

- **PATRÓN** `dist_vwap_pct` > `1.0956` → IC=+0.244 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0956 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.038` → IC=+0.273 (n=332)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.038 (IC base=+0.222)

- **PATRÓN** `volumen_regimen` < `0.643` → IC=+0.251 (n=444)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.643 (IC base=+0.222)

- **PATRÓN** `volumen_regimen` > `1.2456` → IC=+0.224 (n=443)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2456 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` < `0.106` → IC=+0.224 (n=1220)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.106 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` > `0.2758` → IC=+0.250 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2758 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` < `2.5096` → IC=+0.231 (n=1297)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5096 (IC base=+0.222)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.228 (n=1544)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.222)

- **PATRÓN** `libro_liquidez` > `3376.312` → IC=+0.246 (n=1188)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3376.312 (IC base=+0.222)

- **PATRÓN** `sigma_h` < `0.0141` → IC=+0.247 (n=1009)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0141 (IC base=+0.247)

- **PATRÓN** `sigma_h` > `0.0108` → IC=+0.255 (n=672)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0108 (IC base=+0.247)

- **PATRÓN** `drift_60min` |x|≤ `0.6851` → IC=+0.260 (n=1009)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6851 (IC base=+0.247)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.248 (n=933)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.247)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.266 (n=699)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.247)

- **PATRÓN** `ibs_20min` < `0.6444` → IC=+0.271 (n=888)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6444 (IC base=+0.247)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.043` → IC=+0.265 (n=954)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.043 (IC base=+0.247)

- **PATRÓN** `volumen_regimen` < `0.756` → IC=+0.258 (n=444)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.756 (IC base=+0.247)

- **PATRÓN** `volumen_pendiente_norm` < `0.104` → IC=+0.255 (n=909)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.104 (IC base=+0.247)

- **PATRÓN** `volumen_spike_ratio` < `1.4773` → IC=+0.245 (n=328)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4773 (IC base=+0.247)

- **PATRÓN** `volumen_spike_ratio` > `2.2218` → IC=+0.272 (n=446)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2218 (IC base=+0.247)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.250 (n=1222)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.247)

- **PATRÓN** `libro_liquidez` > `4039.5632` → IC=+0.269 (n=672)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4039.5632 (IC base=+0.247)

- **PATRÓN** `ballena_activa_n` < `32.0` → IC=+0.275 (n=886)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 32.0 (IC base=+0.247)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.145 (n=980)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0043 (IC base=+0.079)

- **PATRÓN** `ibs_20min` > `0.4219` → IC=+0.142 (n=2840)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` > 0.4219 (IC base=+0.079)

- **PATRÓN** `dist_vwap_pct` > `0.1603` → IC=+0.161 (n=1313)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.1603 (IC base=+0.079)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.347` → IC=+0.153 (n=621)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 10.347 (IC base=+0.079)

- **PATRÓN** `ibs_20min` < `0.5789` → IC=+0.178 (n=2255)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.5789 (IC base=+0.098)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.539` → IC=+0.133 (n=1001)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` > 2.539 (IC base=+0.098)

- **PATRÓN** `volumen_pendiente_norm` > `0.1514` → IC=+0.182 (n=633)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.1514 (IC base=+0.098)

- **PATRÓN** `volumen_spike_ratio` < `2.1583` → IC=+0.121 (n=1911)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` < 2.1583 (IC base=+0.098)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `ibs_20min` < `0.5597` → IC=-0.123 (n=348)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5597
  - _Potencial_: sin este filtro IC_bueno=+0.161 (n=709)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.122 (n=725)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0057 (IC base=+0.067)

- **PATRÓN** `ibs_20min` > `0.5597` → IC=+0.161 (n=709)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` > 0.5597 (IC base=+0.067)

- **PATRÓN** `dist_vwap_pct` > `0.1288` → IC=+0.166 (n=366)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1288 (IC base=+0.067)

- **PATRÓN** `ibs_20min` < `0.0639` → IC=+0.247 (n=330)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0639 (IC base=+0.055)

- **PATRÓN** `volumen_pendiente_norm` > `0.2135` → IC=+0.158 (n=153)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` > 0.2135 (IC base=+0.055)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` > `0.4852` → IC=-0.121 (n=275)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4852
  - _Potencial_: sin este filtro IC_bueno=+0.154 (n=535)

- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.162 (n=377)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0044 (IC base=+0.068)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.136 (n=330)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 17.0 (IC base=+0.068)

- **PATRÓN** `ibs_20min` > `0.5307` → IC=+0.162 (n=737)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` > 0.5307 (IC base=+0.068)

- **PATRÓN** `dist_vwap_pct` > `0.1364` → IC=+0.159 (n=394)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.1364 (IC base=+0.068)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.996` → IC=+0.174 (n=182)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 11.996 (IC base=+0.068)

- **PATRÓN** `ibs_20min` < `0.3126` → IC=+0.223 (n=406)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3126 (IC base=+0.047)

- **PATRÓN** `volumen_pendiente_norm` > `0.2584` → IC=+0.140 (n=84)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_pendiente_norm` > 0.2584 (IC base=+0.047)

### GBM_LATE_60M#SOL#60min
- **PATRÓN** `ibs_20min` > `0.7143` → IC=+0.142 (n=635)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` > 0.7143 (IC base=+0.041)

- **PATRÓN** `dist_vwap_pct` > `0.7698` → IC=+0.158 (n=229)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.7698 (IC base=+0.041)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.992` → IC=+0.124 (n=267)

  - _Acción_: Kelly boost +0.62€ cuando `sigma_ewma_delta_pct` > 6.992 (IC base=+0.041)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.179 (n=431)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0103 (IC base=+0.099)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.196 (n=614)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.5 (IC base=+0.099)

- **PATRÓN** `dist_vwap_pct` < `0.2223` → IC=+0.150 (n=610)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.2223 (IC base=+0.099)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.132` → IC=+0.239 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.132 (IC base=+0.099)

- **PATRÓN** `volumen_regimen` > `1.1167` → IC=+0.186 (n=205)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` > 1.1167 (IC base=+0.099)

- **PATRÓN** `volumen_pendiente_norm` > `0.1605` → IC=+0.181 (n=158)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.1605 (IC base=+0.099)

- **PATRÓN** `volumen_spike_ratio` > `1.8705` → IC=+0.139 (n=388)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 1.8705 (IC base=+0.099)

### GBM_LATE_60M#XRP#60min
- **PATRÓN** `sigma_h` > `0.0131` → IC=+0.387 (n=60)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0131 (IC base=+0.302)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.409 (n=31)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.302)

- **PATRÓN** `ibs_20min` > `0.5696` → IC=+0.348 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5696 (IC base=+0.302)

- **PATRÓN** `dist_vwap_pct` > `0.2852` → IC=+0.383 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2852 (IC base=+0.302)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.315` → IC=+0.313 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.315 (IC base=+0.302)

- **PATRÓN** `volumen_regimen` < `1.0244` → IC=+0.315 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0244 (IC base=+0.302)

- **PATRÓN** `volumen_regimen` > `0.6557` → IC=+0.305 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6557 (IC base=+0.302)

- **PATRÓN** `volumen_pendiente_norm` > `0.1895` → IC=+0.364 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1895 (IC base=+0.302)

- **PATRÓN** `volumen_spike_ratio` < `2.8251` → IC=+0.344 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.8251 (IC base=+0.302)

- **PATRÓN** `libro_spread` < `0.07` → IC=+0.306 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.07 (IC base=+0.302)

- **PATRÓN** `libro_liquidez` > `1592.384` → IC=+0.344 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1592.384 (IC base=+0.302)

- **PATRÓN** `sigma_h` < `0.0095` → IC=+0.386 (n=33)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0095 (IC base=+0.333)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.371 (n=99)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.333)

- **PATRÓN** `ibs_20min` < `0.04` → IC=+0.386 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.04 (IC base=+0.333)

- **PATRÓN** `ibs_20min` > `0.3512` → IC=+0.372 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3512 (IC base=+0.333)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.308` → IC=+0.452 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.308 (IC base=+0.333)

- **PATRÓN** `volumen_regimen` > `0.5619` → IC=+0.370 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.5619 (IC base=+0.333)

- **PATRÓN** `volumen_pendiente_norm` > `0.1736` → IC=+0.409 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1736 (IC base=+0.333)

- **PATRÓN** `volumen_spike_ratio` < `1.547` → IC=+0.386 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.547 (IC base=+0.333)

- **PATRÓN** `volumen_spike_ratio` > `3.2641` → IC=+0.382 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.2641 (IC base=+0.333)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.351 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.333)

- **PATRÓN** `libro_liquidez` > `37.2396` → IC=+0.344 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 37.2396 (IC base=+0.333)

### GBM_LATE_60M_FADE
- **FILTRO** `sigma_h` < `0.0063` → IC=-0.248 (n=212)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0063
  - _Potencial_: sin este filtro IC_bueno=-0.212 (n=213)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.310 (n=98)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.205 (n=327)

- **FILTRO** `volumen_regimen` < `0.8808` → IC=-0.307 (n=138)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.8808
  - _Potencial_: sin este filtro IC_bueno=-0.191 (n=283)

- **FILTRO** `sigma_h` < `0.0065` → IC=-0.292 (n=263)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0065
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=136)

- **FILTRO** `dist_vwap_pct` > `0.4684` → IC=-0.405 (n=19)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4684
  - _Potencial_: sin este filtro IC_bueno=-0.264 (n=363)

- **FILTRO** `sigma_ewma_delta_pct` > `9.308` → IC=-0.281 (n=30)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 9.308
  - _Potencial_: sin este filtro IC_bueno=-0.260 (n=369)

- **FILTRO** `volumen_pendiente_norm` > `0.0453` → IC=-0.375 (n=30)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0453
  - _Potencial_: sin este filtro IC_bueno=-0.246 (n=274)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `hora_utc` > `9.0` → IC=-0.312 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.233 (n=103)

- **FILTRO** `ibs_20min` < `0.0328` → IC=-0.300 (n=33)

  - _Acción_: SKIP cuando `ibs_20min` < 0.0328
  - _Potencial_: sin este filtro IC_bueno=-0.235 (n=100)

- **FILTRO** `volumen_spike_ratio` > `1.8166` → IC=-0.260 (n=73)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.8166
  - _Potencial_: sin este filtro IC_bueno=-0.218 (n=37)

- **FILTRO** `drift_60min` |x|> `0.1673` → IC=-0.325 (n=38)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1673
  - _Potencial_: sin este filtro IC_bueno=-0.229 (n=116)

- **FILTRO** `volumen_regimen` > `0.807` → IC=-0.350 (n=38)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.807
  - _Potencial_: sin este filtro IC_bueno=-0.225 (n=118)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `sigma_h` < `0.003` → IC=-0.250 (n=34)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.003
  - _Potencial_: sin este filtro IC_bueno=-0.151 (n=104)

- **FILTRO** `ibs_20min` < `0.6002` → IC=-0.472 (n=34)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6002
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=104)

- **FILTRO** `volumen_regimen` < `0.7594` → IC=-0.250 (n=34)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7594
  - _Potencial_: sin este filtro IC_bueno=-0.151 (n=104)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.372 (n=37)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=106)

- **FILTRO** `volumen_spike_ratio` > `2.2319` → IC=-0.342 (n=36)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.2319
  - _Potencial_: sin este filtro IC_bueno=-0.297 (n=72)

- **FILTRO** `volumen_spike_ratio` < `1.4507` → IC=-0.362 (n=27)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.4507
  - _Potencial_: sin este filtro IC_bueno=-0.295 (n=81)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.300 (n=128)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `sigma_h` < `0.0112` → IC=-0.290 (n=98)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0112
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=52)

- **FILTRO** `drift_60min` |x|> `0.2366` → IC=-0.346 (n=37)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2366
  - _Potencial_: sin este filtro IC_bueno=-0.210 (n=112)

- **FILTRO** `dist_vwap_pct` > `0.2836` → IC=-0.350 (n=18)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2836
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=61)

- **FILTRO** `volumen_regimen` < `0.9756` → IC=-0.429 (n=26)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9756
  - _Potencial_: sin este filtro IC_bueno=-0.118 (n=53)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` > `0.2457` → IC=-0.157 (n=354)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2457
  - _Potencial_: sin este filtro IC_bueno=+0.086 (n=1066)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.202 (n=427)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.167)

- **PATRÓN** `ibs_20min` > `0.6818` → IC=+0.200 (n=943)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6818 (IC base=+0.167)

- **PATRÓN** `dist_vwap_pct` > `0.89` → IC=+0.311 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.89 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.572` → IC=+0.179 (n=537)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 3.572 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` < `0.6206` → IC=+0.188 (n=306)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 0.6206 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` > `1.1915` → IC=+0.175 (n=306)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 1.1915 (IC base=+0.167)

- **PATRÓN** `volumen_pendiente_norm` < `0.2102` → IC=+0.184 (n=935)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` < 0.2102 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` < `1.4189` → IC=+0.211 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4189 (IC base=+0.167)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.140 (n=84)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` > 0.0068 (IC base=+0.067)

- **PATRÓN** `ibs_20min` > `0.7305` → IC=+0.138 (n=252)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` > 0.7305 (IC base=+0.067)

- **PATRÓN** `dist_vwap_pct` > `0.3329` → IC=+0.219 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3329 (IC base=+0.067)

- **PATRÓN** `ibs_20min` < `0.2563` → IC=+0.133 (n=464)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` < 0.2563 (IC base=+0.072)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **PATRÓN** `sigma_h` > `0.0073` → IC=+0.163 (n=90)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` > 0.0073 (IC base=+0.132)

- **PATRÓN** `drift_60min` |x|≤ `0.1124` → IC=+0.136 (n=119)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.68€ cuando `drift_60min` |x|≤ 0.1124 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.163 (n=99)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 18.0 (IC base=+0.132)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.141 (n=90)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 5.0 (IC base=+0.132)

- **PATRÓN** `ibs_20min` > `0.8015` → IC=+0.175 (n=241)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` > 0.8015 (IC base=+0.132)

- **PATRÓN** `dist_vwap_pct` > `0.8305` → IC=+0.189 (n=43)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.8305 (IC base=+0.132)

- **PATRÓN** `dist_vwap_pct` < `0.1137` → IC=+0.153 (n=217)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.1137 (IC base=+0.132)

- **PATRÓN** `volumen_regimen` < `0.6195` → IC=+0.185 (n=90)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 0.6195 (IC base=+0.132)

- **PATRÓN** `volumen_regimen` > `1.1834` → IC=+0.163 (n=90)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 1.1834 (IC base=+0.132)

- **PATRÓN** `volumen_pendiente_norm` < `0.0508` → IC=+0.184 (n=223)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` < 0.0508 (IC base=+0.132)

- **PATRÓN** `volumen_spike_ratio` < `1.7116` → IC=+0.175 (n=161)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 1.7116 (IC base=+0.132)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.142 (n=224)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `1704.1785` → IC=+0.176 (n=270)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 1704.1785 (IC base=+0.132)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.2391` → IC=-0.271 (n=59)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2391
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=181)

- **FILTRO** `volumen_spike_ratio` > `2.2708` → IC=-0.154 (n=50)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.2708
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=152)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.289 (n=349)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.272)

- **PATRÓN** `ibs_20min` > `0.6078` → IC=+0.292 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6078 (IC base=+0.272)

- **PATRÓN** `dist_vwap_pct` > `0.7823` → IC=+0.395 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7823 (IC base=+0.272)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.992` → IC=+0.360 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.992 (IC base=+0.272)

- **PATRÓN** `volumen_regimen` < `0.7978` → IC=+0.293 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7978 (IC base=+0.272)

- **PATRÓN** `volumen_pendiente_norm` < `0.2132` → IC=+0.298 (n=320)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2132 (IC base=+0.272)

- **PATRÓN** `volumen_pendiente_norm` > `0.0894` → IC=+0.309 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0894 (IC base=+0.272)

- **PATRÓN** `volumen_spike_ratio` < `1.4956` → IC=+0.330 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4956 (IC base=+0.272)

- **PATRÓN** `volumen_spike_ratio` > `2.061` → IC=+0.311 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.061 (IC base=+0.272)

- **PATRÓN** `libro_spread` < `0.05` → IC=+0.272 (n=336)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.05 (IC base=+0.272)

### LATE_WINDOW_5MIN
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.315 (n=209)

- **PATRÓN** `drift_ventana_pct` |x|> `0.5455` → IC=+0.357 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.5455 (IC base=+0.321)

- **PATRÓN** `elapsed_s` > `209.5` → IC=+0.373 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 209.5 (IC base=+0.321)

- **PATRÓN** `drift_15min` |x|≤ `1.1328` → IC=+0.377 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.1328 (IC base=+0.321)

- **PATRÓN** `drift_60min` |x|≤ `0.6903` → IC=+0.392 (n=109)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6903 (IC base=+0.321)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.375 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.321)

- **PATRÓN** `ballena_activa_n` < `1043.0` → IC=+0.430 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1043.0 (IC base=+0.321)

- **PATRÓN** `drift_ventana_pct` |x|> `0.445` → IC=+0.314 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.445 (IC base=+0.281)

- **PATRÓN** `elapsed_s` > `232.0` → IC=+0.364 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 232.0 (IC base=+0.281)

- **PATRÓN** `drift_15min` |x|≤ `2.3607` → IC=+0.316 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3607 (IC base=+0.281)

- **PATRÓN** `drift_60min` |x|≤ `0.9999` → IC=+0.303 (n=150)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9999 (IC base=+0.281)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.315 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.281)

- **PATRÓN** `ballena_activa_n` < `1717.0` → IC=+0.326 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1717.0 (IC base=+0.281)

### LATE_WINDOW_5MIN#BTC#5min
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.315 (n=209)

- **PATRÓN** `drift_ventana_pct` |x|> `0.5455` → IC=+0.357 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.5455 (IC base=+0.321)

- **PATRÓN** `elapsed_s` > `209.5` → IC=+0.373 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 209.5 (IC base=+0.321)

- **PATRÓN** `drift_15min` |x|≤ `1.1328` → IC=+0.377 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.1328 (IC base=+0.321)

- **PATRÓN** `drift_60min` |x|≤ `0.6903` → IC=+0.392 (n=109)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6903 (IC base=+0.321)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.375 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.321)

- **PATRÓN** `ballena_activa_n` < `1043.0` → IC=+0.430 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1043.0 (IC base=+0.321)

- **PATRÓN** `drift_ventana_pct` |x|> `0.445` → IC=+0.314 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.445 (IC base=+0.281)

- **PATRÓN** `elapsed_s` > `232.0` → IC=+0.364 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 232.0 (IC base=+0.281)

- **PATRÓN** `drift_15min` |x|≤ `2.3607` → IC=+0.316 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3607 (IC base=+0.281)

- **PATRÓN** `drift_60min` |x|≤ `0.9999` → IC=+0.303 (n=150)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9999 (IC base=+0.281)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.315 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.281)

- **PATRÓN** `ballena_activa_n` < `1717.0` → IC=+0.326 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1717.0 (IC base=+0.281)

### LIQUIDACIONES_15M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.092 (n=297)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=298)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=1696)

### LIQUIDACIONES_15M#BNB#15min
- **PATRÓN** `liq_n` > `2.0` → IC=+0.184 (n=96)

  - _Acción_: Kelly boost +0.92€ cuando `liq_n` > 2.0 (IC base=+0.085)

- **PATRÓN** `liq_usd_total` > `1200.92` → IC=+0.152 (n=90)

  - _Acción_: Kelly boost +0.76€ cuando `liq_usd_total` > 1200.92 (IC base=+0.085)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.167 (n=73)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 6.0 (IC base=+0.085)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.135 (n=102)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.03 (IC base=+0.085)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `libro_liquidez` < `11682.4811` → IC=-0.159 (n=42)

  - _Acción_: SKIP cuando `libro_liquidez` < 11682.4811
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=129)

### LIQUIDACIONES_15M#DOGE#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.095 (n=146)

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
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=287)

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
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=4327)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=269)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.110 (n=226)

- **FILTRO** `ballena_activa_n` > `39.0` → IC=-0.178 (n=85)

  - _Acción_: SKIP cuando `ballena_activa_n` > 39.0
  - _Potencial_: sin este filtro IC_bueno=+0.176 (n=171)

- **PATRÓN** `ballena_activa_n` < `39.0` → IC=+0.176 (n=171)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 39.0 (IC base=+0.024)

### LIQUIDACIONES_5M#BTC#5min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.167 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=15)

- **FILTRO** `libro_liquidez` < `13988.6712` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `libro_liquidez` < 13988.6712
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=19)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.136 (n=300)

  - _Acción_: Kelly boost +0.68€ cuando `py_entrada` < 0.495 (IC base=+0.025)

### LIQUIDACIONES_5M#DOGE#5min
- **PATRÓN** `liq_n` > `3.0` → IC=+0.318 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `liq_n` > 3.0 (IC base=+0.180)

- **PATRÓN** `liq_usd_total` > `750.26` → IC=+0.259 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `liq_usd_total` > 750.26 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.223 (n=92)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 9.0 (IC base=+0.180)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.190 (n=127)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 13.0 (IC base=+0.180)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=1723)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=1677)

- **FILTRO** `hora_utc` > `5.0` → IC=-0.286 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=10)

### LIQUIDACIONES_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.505` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=775)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=784)

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
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=1200)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=1200)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=1640)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=1640)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=377)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=377)

- **FILTRO** `py_entrada` < `0.425` → IC=-0.144 (n=85)

  - _Acción_: SKIP cuando `py_entrada` < 0.425
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=307)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.136 (n=64)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=427)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=476)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=348)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=460)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=460)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=451)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.4` → IC=-0.132 (n=3830)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=9811)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `hora_utc` > `14.0` → IC=-0.147 (n=120)
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
- **FILTRO** `py_entrada` < `0.4` → IC=-0.163 (n=461)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=1114)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **FILTRO** `py_entrada` > `0.6` → IC=-0.144 (n=363)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=988)

- **PATRÓN** `py_entrada` < `0.51` → IC=+0.137 (n=464)

  - _Acción_: Kelly boost +0.69€ cuando `py_entrada` < 0.51 (IC base=-0.011)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` < `0.42` → IC=-0.121 (n=320)

  - _Acción_: SKIP cuando `py_entrada` < 0.42
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=376)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **FILTRO** `py_entrada` < `0.41` → IC=-0.127 (n=231)

  - _Acción_: SKIP cuando `py_entrada` < 0.41
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=471)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.164 (n=251)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=1358)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.139 (n=389)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=820)

### LIQUIDACIONES_DEPTH_FASE0#SOL#5min
- **FILTRO** `py_entrada` < `0.42` → IC=-0.133 (n=594)

  - _Acción_: SKIP cuando `py_entrada` < 0.42
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=750)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.124 (n=629)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=653)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.134 (n=675)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=777)

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
- **FILTRO** `py_entrada` < `0.46` → IC=-0.177 (n=9382)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=29146)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.171 (n=9699)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=30200)

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
- **FILTRO** `py_entrada` > `0.57` → IC=-0.174 (n=1417)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=4362)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` > `0.62` → IC=-0.197 (n=1749)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.089 (n=5429)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.134 (n=2186)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` > 1.0 (IC base=+0.032)

### MOMENTUM_IBS_15M_BALLENA#ETH#15min
- **FILTRO** `ibs_20min` < `0.7644` → IC=-0.148 (n=1323)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7644
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=3974)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.180 (n=1441)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=4380)

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
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=3470)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=4422)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` > `20.0` → IC=-0.146 (n=125)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 20.0
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=447)

- **FILTRO** `py_entrada` < `0.455` → IC=-0.257 (n=142)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=430)

### MOMENTUM_IBS_15M_FADE#DOGE#15min
- **FILTRO** `ibs_20min` > `0.7158` → IC=-0.167 (n=25)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7158
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=50)

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
  - _Potencial_: sin este filtro IC_bueno=-0.098 (n=381)

- **FILTRO** `drift_20min_pct` |x|> `0.16` → IC=-0.127 (n=167)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.16
  - _Potencial_: sin este filtro IC_bueno=-0.120 (n=327)

- **FILTRO** `libro_liquidez` < `3260.3832` → IC=-0.185 (n=163)

  - _Acción_: SKIP cuando `libro_liquidez` < 3260.3832
  - _Potencial_: sin este filtro IC_bueno=-0.092 (n=331)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.192 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=983)

- **FILTRO** `ibs_20min` > `0.8611` → IC=-0.129 (n=650)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8611
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=655)

- **FILTRO** `ballena_activa_n` > `21.0` → IC=-0.175 (n=438)

  - _Acción_: SKIP cuando `ballena_activa_n` > 21.0
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=858)

### MOMENTUM_IBS_15M_FADE#XRP#15min
- **FILTRO** `hora_utc` < `14.0` → IC=-0.141 (n=76)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=235)

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
- **FILTRO** `hora_utc` > `16.0` → IC=-0.167 (n=70)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=237)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.137 (n=26147)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=59163)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.301 (n=20772)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=64538)

- **FILTRO** `ibs_7min` < `0.2105` → IC=-0.237 (n=21324)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2105
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=63986)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.154 (n=28133)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=57177)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.247 (n=26375)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=80103)

- **FILTRO** `ibs_7min` > `0.278` → IC=-0.182 (n=26619)

  - _Acción_: SKIP cuando `ibs_7min` > 0.278
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=79859)

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
- **FILTRO** `hora_utc` < `6.0` → IC=-0.126 (n=3484)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.104 (n=10912)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.266 (n=3527)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=10869)

- **FILTRO** `ibs_7min` < `0.7106` → IC=-0.212 (n=3598)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7106
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=10798)

- **FILTRO** `ballena_activa_n` > `156.0` → IC=-0.204 (n=3598)

  - _Acción_: SKIP cuando `ballena_activa_n` > 156.0
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=10798)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.265 (n=3360)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=11380)

- **FILTRO** `ibs_7min` > `0.2642` → IC=-0.188 (n=3683)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2642
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=11057)

- **FILTRO** `ballena_activa_n` > `152.0` → IC=-0.177 (n=3681)

  - _Acción_: SKIP cuando `ballena_activa_n` > 152.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=11059)

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
- **FILTRO** `py_entrada` < `0.33` → IC=-0.276 (n=3218)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=10870)

- **FILTRO** `ibs_7min` < `0.7119` → IC=-0.201 (n=3521)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7119
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=10567)

- **FILTRO** `ballena_activa_n` > `26.0` → IC=-0.195 (n=3512)

  - _Acción_: SKIP cuando `ballena_activa_n` > 26.0
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=10576)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.259 (n=3408)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=11195)

- **FILTRO** `ibs_7min` > `0.2716` → IC=-0.178 (n=3644)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2716
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=10959)

- **FILTRO** `ballena_activa_n` > `25.0` → IC=-0.173 (n=3564)

  - _Acción_: SKIP cuando `ballena_activa_n` > 25.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=11039)

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
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=1039)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=1328)

- **FILTRO** `py_entrada` > `0.545` → IC=-0.156 (n=187)

  - _Acción_: SKIP cuando `py_entrada` > 0.545
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=687)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=1458)

- **FILTRO** `py_entrada` > `0.565` → IC=-0.172 (n=260)

  - _Acción_: SKIP cuando `py_entrada` > 0.565
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=935)

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
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=595)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.162 (n=255)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=504)

- **FILTRO** `libro_liquidez` < `3306.2556` → IC=-0.146 (n=196)

  - _Acción_: SKIP cuando `libro_liquidez` < 3306.2556
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=591)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=56)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=563)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.4305` → IC=+0.142 (n=792)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.71€ cuando `delta_ratio` |x|> 0.4305 (IC base=+0.122)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.130 (n=889)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 6.0 (IC base=+0.122)

- **PATRÓN** `total_vol_5m` < `456.9956` → IC=+0.162 (n=580)

  - _Acción_: Kelly boost +0.81€ cuando `total_vol_5m` < 456.9956 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `3678.0144` → IC=+0.129 (n=788)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 3678.0144 (IC base=+0.122)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `14.0` → IC=+0.175 (n=201)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 14.0 (IC base=+0.139)

- **PATRÓN** `total_vol_5m` < `287.798` → IC=+0.170 (n=268)

  - _Acción_: Kelly boost +0.85€ cuando `total_vol_5m` < 287.798 (IC base=+0.139)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.143 (n=362)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.04 (IC base=+0.139)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `delta_ratio` |x|> `0.3988` → IC=+0.134 (n=364)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.67€ cuando `delta_ratio` |x|> 0.3988 (IC base=+0.118)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.137 (n=340)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 15.0 (IC base=+0.118)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.121 (n=441)

  - _Acción_: Kelly boost +0.60€ cuando `libro_spread` < 0.04 (IC base=+0.118)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4156` → IC=+0.165 (n=210)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.83€ cuando `delta_ratio` |x|> 0.4156 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.155 (n=288)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 5.0 (IC base=+0.130)

- **PATRÓN** `total_vol_5m` < `878.6597` → IC=+0.163 (n=315)

  - _Acción_: Kelly boost +0.81€ cuando `total_vol_5m` < 878.6597 (IC base=+0.130)

- **PATRÓN** `ballena_activa_n` < `59.0` → IC=+0.187 (n=113)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 59.0 (IC base=+0.130)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.4317` → IC=+0.215 (n=135)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio` |x|> 0.4317 (IC base=+0.132)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.158 (n=118)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 5.0 (IC base=+0.132)

- **PATRÓN** `total_vol_5m` < `4782.684` → IC=+0.180 (n=198)

  - _Acción_: Kelly boost +0.90€ cuando `total_vol_5m` < 4782.684 (IC base=+0.132)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `hora_utc` < `10.0` → IC=+0.123 (n=245)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 10.0 (IC base=+0.093)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.128 (n=221)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.01 (IC base=+0.093)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `4.4533` → IC=-0.202 (n=129)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.4533
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=131)

- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.150 (n=349)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0048 (IC base=-0.030)

### PRICE_TARGET_GBM#ETH#atexpiry
- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.271 (n=81)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=+0.005)

- **PATRÓN** `pct_vs_K` |x|≤ `2.0557` → IC=+0.222 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `pct_vs_K` |x|≤ 2.0557 (IC base=+0.005)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `T_h` > `76.1623` → IC=-0.125 (n=70)

  - _Acción_: SKIP cuando `T_h` > 76.1623
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=24)

- **FILTRO** `pct_vs_K` |x|> `6.3582` → IC=-0.258 (n=31)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 6.3582
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=63)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0154` → IC=-0.211 (n=50)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0154
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=151)

- **FILTRO** `T_h` < `63.8277` → IC=-0.173 (n=50)

  - _Acción_: SKIP cuando `T_h` < 63.8277
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=151)

### PRICE_TARGET_GBM#SOL#reach
- **FILTRO** `sigma_h` < `0.0173` → IC=-0.167 (n=25)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0173
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.012` → IC=-0.256 (n=675)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.012
  - _Potencial_: sin este filtro IC_bueno=-0.231 (n=225)

- **FILTRO** `T_h` > `67.0844` → IC=-0.258 (n=602)

  - _Acción_: SKIP cuando `T_h` > 67.0844
  - _Potencial_: sin este filtro IC_bueno=-0.233 (n=298)

- **FILTRO** `sigma_h` < `0.0066` → IC=-0.170 (n=283)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0066
  - _Potencial_: sin este filtro IC_bueno=-0.089 (n=577)

- **FILTRO** `T_h` < `108.5242` → IC=-0.150 (n=430)

  - _Acción_: SKIP cuando `T_h` < 108.5242
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=430)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `sigma_h` < `0.01` → IC=-0.232 (n=222)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.218 (n=76)

- **FILTRO** `T_h` > `49.2217` → IC=-0.251 (n=223)

  - _Acción_: SKIP cuando `T_h` > 49.2217
  - _Potencial_: sin este filtro IC_bueno=-0.162 (n=75)

- **FILTRO** `T_h` < `91.0659` → IC=-0.182 (n=105)

  - _Acción_: SKIP cuando `T_h` < 91.0659
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=214)

### PRICE_TARGET_GBM_FADE#BTC#reach
- **FILTRO** `pct_vs_K` |x|> `2.8218` → IC=-0.233 (n=28)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.8218
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **FILTRO** `sigma_h` < `0.0078` → IC=-0.273 (n=20)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0078
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=21)

- **FILTRO** `T_h` > `139.1329` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `T_h` > 139.1329
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=21)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `sigma_h` < `0.0097` → IC=-0.328 (n=132)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0097
  - _Potencial_: sin este filtro IC_bueno=-0.284 (n=132)

- **FILTRO** `T_h` > `135.5844` → IC=-0.336 (n=65)

  - _Acción_: SKIP cuando `T_h` > 135.5844
  - _Potencial_: sin este filtro IC_bueno=-0.296 (n=199)

- **FILTRO** `sigma_h` > `0.0094` → IC=-0.144 (n=88)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0094
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=171)

- **FILTRO** `sigma_h` < `0.0058` → IC=-0.151 (n=64)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0058
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=195)

- **PATRÓN** `pct_vs_K` |x|≤ `1.9843` → IC=+0.167 (n=130)

  - _Acción_: Kelly boost +0.83€ cuando `pct_vs_K` |x|≤ 1.9843 (IC base=-0.094)

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
- **FILTRO** `sigma_h` > `0.0133` → IC=-0.229 (n=83)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0133
  - _Potencial_: sin este filtro IC_bueno=-0.215 (n=163)

- **FILTRO** `T_h` > `61.9454` → IC=-0.231 (n=184)

  - _Acción_: SKIP cuando `T_h` > 61.9454
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=62)

- **FILTRO** `sigma_h` > `0.0139` → IC=-0.306 (n=65)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0139
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=127)

- **FILTRO** `sigma_h` < `0.0099` → IC=-0.260 (n=48)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0099
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=144)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.106` → IC=+0.451 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.106 (IC base=+0.327)

- **PATRÓN** `sigma_h` < `0.0148` → IC=+0.347 (n=135)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0148 (IC base=+0.327)

- **PATRÓN** `T_h` < `0.3392` → IC=+0.415 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.3392 (IC base=+0.327)

- **PATRÓN** `T_h` > `0.7009` → IC=+0.337 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.7009 (IC base=+0.327)

- **PATRÓN** `dist_50` > `0.4594` → IC=+0.484 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4594 (IC base=+0.327)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.345 (n=153)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.327)

- **PATRÓN** `edge` > `0.0992` → IC=+0.424 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.0992 (IC base=+0.392)

- **PATRÓN** `sigma_h` > `0.01` → IC=+0.416 (n=201)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.01 (IC base=+0.392)

- **PATRÓN** `T_h` < `0.7258` → IC=+0.418 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.7258 (IC base=+0.392)

- **PATRÓN** `dist_50` > `0.368` → IC=+0.441 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.368 (IC base=+0.392)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.412 (n=349)
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

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1295 (IC base=+0.276)

- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.340 (n=23)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0084 (IC base=+0.276)

- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.324 (n=15)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0099 (IC base=+0.276)

- **PATRÓN** `T_h` < `0.6127` → IC=+0.375 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.6127 (IC base=+0.276)

- **PATRÓN** `dist_50` > `0.4172` → IC=+0.441 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4172 (IC base=+0.276)

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
- **PATRÓN** `edge` > `0.1338` → IC=+0.487 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1338 (IC base=+0.417)

- **PATRÓN** `sigma_h` < `0.0155` → IC=+0.472 (n=69)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0155 (IC base=+0.417)

- **PATRÓN** `T_h` < `1.0173` → IC=+0.415 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 1.0173 (IC base=+0.417)

- **PATRÓN** `T_h` > `0.5804` → IC=+0.417 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.5804 (IC base=+0.417)

- **PATRÓN** `dist_50` > `0.3288` → IC=+0.475 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3288 (IC base=+0.417)

- **PATRÓN** `edge` > `0.1937` → IC=+0.472 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1937 (IC base=+0.465)

- **PATRÓN** `sigma_h` < `0.0162` → IC=+0.475 (n=161)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0162 (IC base=+0.465)

- **PATRÓN** `T_h` < `0.8021` → IC=+0.459 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.8021 (IC base=+0.465)

- **PATRÓN** `T_h` > `1.4857` → IC=+0.482 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4857 (IC base=+0.465)

- **PATRÓN** `dist_50` > `0.414` → IC=+0.482 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.414 (IC base=+0.465)

- **PATRÓN** `hora_utc` < `2.0` → IC=+0.485 (n=63)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 2.0 (IC base=+0.465)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=501)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.074 (n=538)

- **PATRÓN** `streak_estiramiento` < `0.3787` → IC=+0.137 (n=166)

  - _Acción_: Kelly boost +0.68€ cuando `streak_estiramiento` < 0.3787 (IC base=+0.021)

- **PATRÓN** `streak_estiramiento` < `0.8333` → IC=+0.127 (n=373)

  - _Acción_: Kelly boost +0.63€ cuando `streak_estiramiento` < 0.8333 (IC base=+0.063)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.153 (n=145)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 14.0 (IC base=+0.063)

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
  - _Potencial_: sin este filtro IC_bueno=+0.190 (n=27)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.190 (n=27)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.495 (IC base=+0.068)

- **PATRÓN** `ballena_activa_n` < `26.0` → IC=+0.196 (n=21)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 26.0 (IC base=+0.068)

- **PATRÓN** `libro_liquidez` > `2474.7486` → IC=+0.196 (n=21)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 2474.7486 (IC base=+0.068)

### STREAK_FADE_15M#XRP#15min
- **PATRÓN** `streak_estiramiento` < `0.3854` → IC=+0.127 (n=132)

  - _Acción_: Kelly boost +0.63€ cuando `streak_estiramiento` < 0.3854 (IC base=+0.039)

- **PATRÓN** `streak_estiramiento` < `0.3787` → IC=+0.205 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `streak_estiramiento` < 0.3787 (IC base=+0.084)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.138 (n=205)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 35.0 (IC base=+0.084)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.194 (n=47)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=105)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=71)

- **FILTRO** `libro_liquidez` < `3678.6572` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 3678.6572
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=78)

- **FILTRO** `streak_len` > `3.0` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=65)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=826)

### STREAK_FADE_60M
- **FILTRO** `py_entrada` < `0.515` → IC=-0.214 (n=19)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.134 (n=39)

- **PATRÓN** `py_entrada` > `0.515` → IC=+0.134 (n=39)

  - _Acción_: Kelly boost +0.67€ cuando `py_entrada` > 0.515 (IC base=+0.017)

- **PATRÓN** `streak_estiramiento` < `0.6237` → IC=+0.194 (n=34)

  - _Acción_: Kelly boost +0.97€ cuando `streak_estiramiento` < 0.6237 (IC base=+0.009)

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
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=1121)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=1365)

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
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=5728)

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
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=3424)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.182 (n=2244)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0059 (IC base=+0.132)

- **PATRÓN** `drift_60min` |x|≤ `0.2338` → IC=+0.158 (n=6731)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.2338 (IC base=+0.132)

- **PATRÓN** `drift_15min` |x|≤ `1.1275` → IC=+0.133 (n=6730)

  - _Acción_: Kelly boost +0.66€ cuando `drift_15min` |x|≤ 1.1275 (IC base=+0.132)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0644` → IC=+0.133 (n=6729)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.66€ cuando `delta_ratio_macro` |x|> 0.0644 (IC base=+0.132)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0992` → IC=+0.144 (n=2122)

  - _Acción_: Kelly boost +0.72€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0992 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.143 (n=6233)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 6.0 (IC base=+0.132)

- **PATRÓN** `ibs_15` > `0.551` → IC=+0.206 (n=6012)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.551 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.957` → IC=+0.226 (n=1258)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.957 (IC base=+0.132)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=3517)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `4322.2356` → IC=+0.171 (n=2243)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 4322.2356 (IC base=+0.132)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=2624)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.248 (n=304)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.206)

- **PATRÓN** `drift_60min` |x|≤ `0.0773` → IC=+0.247 (n=401)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0773 (IC base=+0.206)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2662` → IC=+0.226 (n=304)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2662 (IC base=+0.206)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2242` → IC=+0.220 (n=552)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2242 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.232 (n=844)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.206)

- **PATRÓN** `ibs_15` > `0.7013` → IC=+0.274 (n=911)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7013 (IC base=+0.206)

- **PATRÓN** `dist_vwap_pct` > `0.3946` → IC=+0.235 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3946 (IC base=+0.206)

- **PATRÓN** `dist_vwap_pct` < `0.5513` → IC=+0.207 (n=1027)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5513 (IC base=+0.206)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.939` → IC=+0.298 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.939 (IC base=+0.206)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.209 (n=1182)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.206)

- **PATRÓN** `libro_liquidez` > `11847.0948` → IC=+0.219 (n=607)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11847.0948 (IC base=+0.206)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.147 (n=1031)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0068 (IC base=+0.132)

- **PATRÓN** `drift_60min` |x|≤ `0.1094` → IC=+0.145 (n=782)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.1094 (IC base=+0.132)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0831` → IC=+0.137 (n=1047)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.68€ cuando `delta_ratio_macro` |x|> 0.0831 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.143 (n=833)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 11.0 (IC base=+0.132)

- **PATRÓN** `ibs_15` > `0.4761` → IC=+0.216 (n=1172)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.4761 (IC base=+0.132)

- **PATRÓN** `dist_vwap_pct` > `0.1243` → IC=+0.144 (n=726)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` > 0.1243 (IC base=+0.132)

- **PATRÓN** `dist_vwap_pct` < `0.6708` → IC=+0.132 (n=1330)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.6708 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.945` → IC=+0.281 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.945 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `6122.7931` → IC=+0.176 (n=532)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 6122.7931 (IC base=+0.132)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `ibs_15` > `0.8333` → IC=+0.145 (n=703)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.73€ cuando `ibs_15` > 0.8333 (IC base=+0.046)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0118` → IC=+0.143 (n=1698)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` > 0.0118 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.2399` → IC=+0.176 (n=1699)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.2399 (IC base=+0.137)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0586` → IC=+0.139 (n=1698)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.70€ cuando `delta_ratio_macro` |x|> 0.0586 (IC base=+0.137)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.093` → IC=+0.184 (n=533)

  - _Acción_: Kelly boost +0.92€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.093 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.144 (n=1550)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 6.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.142 (n=1497)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 14.0 (IC base=+0.137)

- **PATRÓN** `ibs_15` > `0.6944` → IC=+0.232 (n=1132)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6944 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` > `0.2145` → IC=+0.141 (n=779)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.2145 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` < `0.9149` → IC=+0.142 (n=1963)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.9149 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.915` → IC=+0.183 (n=393)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 16.915 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `2939.0564` → IC=+0.179 (n=770)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 2939.0564 (IC base=+0.137)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` > `0.0057` → IC=+0.382 (n=380)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0057 (IC base=+0.361)

- **PATRÓN** `drift_60min` |x|≤ `0.1504` → IC=+0.362 (n=738)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1504 (IC base=+0.361)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1455` → IC=+0.375 (n=558)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1455 (IC base=+0.361)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.102` → IC=+0.381 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.102 (IC base=+0.361)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.373 (n=885)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.361)

- **PATRÓN** `ibs_15` > `0.7873` → IC=+0.391 (n=838)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7873 (IC base=+0.361)

- **PATRÓN** `dist_vwap_pct` > `0.2698` → IC=+0.383 (n=364)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2698 (IC base=+0.361)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.725` → IC=+0.389 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.725 (IC base=+0.361)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.363 (n=1019)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.361)

- **PATRÓN** `libro_liquidez` > `9681.5596` → IC=+0.372 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9681.5596 (IC base=+0.361)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.359 (n=268)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.360)

- **PATRÓN** `drift_60min` |x|≤ `0.1527` → IC=+0.365 (n=353)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1527 (IC base=+0.360)

- **PATRÓN** `drift_15min` |x|≤ `0.4182` → IC=+0.366 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4182 (IC base=+0.360)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2196` → IC=+0.370 (n=182)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2196 (IC base=+0.360)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1436` → IC=+0.401 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1436 (IC base=+0.360)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.380 (n=372)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.360)

- **PATRÓN** `ibs_15` > `0.8044` → IC=+0.378 (n=401)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8044 (IC base=+0.360)

- **PATRÓN** `dist_vwap_pct` > `0.2546` → IC=+0.395 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2546 (IC base=+0.360)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.649` → IC=+0.378 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.649 (IC base=+0.360)

- **PATRÓN** `libro_liquidez` > `15150.2605` → IC=+0.391 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15150.2605 (IC base=+0.360)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.365 (n=146)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.361)

- **PATRÓN** `sigma_h` > `0.0063` → IC=+0.371 (n=199)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0063 (IC base=+0.361)

- **PATRÓN** `drift_60min` |x|≤ `0.1058` → IC=+0.364 (n=292)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1058 (IC base=+0.361)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1257` → IC=+0.378 (n=292)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1257 (IC base=+0.361)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0998` → IC=+0.384 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0998 (IC base=+0.361)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.368 (n=439)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.361)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.369 (n=204)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.361)

- **PATRÓN** `ibs_15` > `0.7601` → IC=+0.396 (n=438)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7601 (IC base=+0.361)

- **PATRÓN** `dist_vwap_pct` > `0.4608` → IC=+0.381 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4608 (IC base=+0.361)

- **PATRÓN** `dist_vwap_pct` < `0.6708` → IC=+0.362 (n=499)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6708 (IC base=+0.361)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.854` → IC=+0.392 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.854 (IC base=+0.361)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.464` → IC=+0.364 (n=404)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.464 (IC base=+0.361)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.362 (n=497)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.361)

- **PATRÓN** `libro_liquidez` > `4381.4638` → IC=+0.371 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4381.4638 (IC base=+0.361)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0079` → IC=-0.203 (n=3113)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0079
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=3114)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.220 (n=2761)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=3466)

- **FILTRO** `libro_liquidez` < `4431.853` → IC=-0.172 (n=4109)

  - _Acción_: SKIP cuando `libro_liquidez` < 4431.853
  - _Potencial_: sin este filtro IC_bueno=+0.079 (n=2118)

- **PATRÓN** `ibs_15` > `0.6288` → IC=+0.278 (n=1373)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6288 (IC base=-0.086)

- **PATRÓN** `dist_vwap_pct` > `0.1167` → IC=+0.207 (n=811)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1167 (IC base=-0.086)

- **PATRÓN** `dist_vwap_pct` < `0.5972` → IC=+0.200 (n=1458)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5972 (IC base=-0.086)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2274` → IC=+0.268 (n=2056)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2274 (IC base=+0.001)

- **PATRÓN** `ibs_15` < `0.3775` → IC=+0.281 (n=6163)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3775 (IC base=+0.001)

- **PATRÓN** `dist_vwap_pct` > `0.7089` → IC=+0.264 (n=890)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7089 (IC base=+0.001)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0461` → IC=-0.225 (n=2788)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0461
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=1375)

- **FILTRO** `sigma_h` < `0.0041` → IC=-0.206 (n=1040)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0041
  - _Potencial_: sin este filtro IC_bueno=-0.171 (n=3123)

- **FILTRO** `sigma_ewma_delta_pct` > `22.161` → IC=-0.233 (n=583)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 22.161
  - _Potencial_: sin este filtro IC_bueno=-0.171 (n=3580)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1436` → IC=+0.286 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1436 (IC base=+0.066)

- **PATRÓN** `ibs_15` > `0.7503` → IC=+0.313 (n=495)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7503 (IC base=+0.066)

- **PATRÓN** `dist_vwap_pct` > `0.1067` → IC=+0.283 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1067 (IC base=+0.066)

- **PATRÓN** `dist_vwap_pct` < `0.5415` → IC=+0.285 (n=552)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5415 (IC base=+0.066)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.691` → IC=+0.137 (n=246)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 21.691 (IC base=+0.066)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0742` → IC=+0.227 (n=86)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0742 (IC base=-0.180)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1404` → IC=+0.295 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1404 (IC base=-0.180)

- **PATRÓN** `ibs_15` < `0.6283` → IC=+0.295 (n=86)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.6283 (IC base=-0.180)

- **PATRÓN** `dist_vwap_pct` < `0.05` → IC=+0.278 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.05 (IC base=-0.180)

- **PATRÓN** `ballena_activa_n` < `381.0` → IC=+0.316 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 381.0 (IC base=-0.180)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.155 (n=908)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.161 (n=694)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0067 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.159` → IC=+0.162 (n=611)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.159 (IC base=+0.149)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2985` → IC=+0.185 (n=550)

  - _Acción_: Kelly boost +0.92€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2985 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.188 (n=315)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 15.0 (IC base=+0.149)

- **PATRÓN** `ibs_15` > `0.5639` → IC=+0.240 (n=694)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5639 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.6666` → IC=+0.169 (n=137)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.6666 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` < `0.1594` → IC=+0.150 (n=532)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.1594 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.241` → IC=+0.250 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.241 (IC base=+0.149)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.155 (n=908)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `5213.5522` → IC=+0.171 (n=463)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 5213.5522 (IC base=+0.149)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.251 (n=1628)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.4867` → IC=+0.242 (n=2440)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4867 (IC base=+0.234)

- **PATRÓN** `drift_15min` |x|≤ `0.8321` → IC=+0.248 (n=2147)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.8321 (IC base=+0.234)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1963` → IC=+0.256 (n=1107)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1963 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.240 (n=903)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.234)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.240 (n=1082)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.234)

- **PATRÓN** `ibs_15` < `0.1944` → IC=+0.293 (n=1628)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.1944 (IC base=+0.234)

- **PATRÓN** `dist_vwap_pct` > `0.2404` → IC=+0.247 (n=829)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2404 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.508` → IC=+0.240 (n=1049)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.508 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.262` → IC=+0.237 (n=2567)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.262 (IC base=+0.234)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.2006` → IC=-0.300 (n=373)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.2006
  - _Potencial_: sin este filtro IC_bueno=-0.172 (n=1123)

- **FILTRO** `drift_60min` |x|> `0.2016` → IC=-0.292 (n=373)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2016
  - _Potencial_: sin este filtro IC_bueno=-0.175 (n=1123)

- **FILTRO** `drift_15min` |x|> `1.0228` → IC=-0.300 (n=373)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.0228
  - _Potencial_: sin este filtro IC_bueno=-0.172 (n=1123)

- **FILTRO** `sigma_ewma_delta_pct` > `6.067` → IC=-0.210 (n=326)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.067
  - _Potencial_: sin este filtro IC_bueno=-0.202 (n=1170)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1478` → IC=+0.188 (n=46)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.94€ cuando `delta_ratio_macro` |x|> 0.1478 (IC base=-0.204)

- **PATRÓN** `ibs_15` > `0.9231` → IC=+0.380 (n=23)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9231 (IC base=-0.204)

- **PATRÓN** `dist_vwap_pct` < `0.4298` → IC=+0.158 (n=77)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.4298 (IC base=-0.204)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.194 (n=34)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 37.0 (IC base=-0.204)

- **PATRÓN** `ibs_15` < `0.381` → IC=+0.295 (n=1016)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.381 (IC base=-0.026)

- **PATRÓN** `dist_vwap_pct` < `0.1997` → IC=+0.258 (n=927)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1997 (IC base=-0.026)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1213` → IC=-0.271 (n=867)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1213
  - _Potencial_: sin este filtro IC_bueno=-0.170 (n=868)

- **FILTRO** `drift_15min` |x|> `1.2899` → IC=-0.284 (n=433)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.2899
  - _Potencial_: sin este filtro IC_bueno=-0.199 (n=1302)

- **FILTRO** `sigma_ewma_delta_pct` > `7.24` → IC=-0.227 (n=522)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 7.24
  - _Potencial_: sin este filtro IC_bueno=-0.218 (n=1213)

- **FILTRO** `libro_spread` > `0.04` → IC=-0.260 (n=23)

  - _Acción_: SKIP cuando `libro_spread` > 0.04
  - _Potencial_: sin este filtro IC_bueno=-0.220 (n=1712)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.221)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.221)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0706` → IC=+0.282 (n=1267)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0706 (IC base=-0.008)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0937` → IC=+0.288 (n=469)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0937 (IC base=-0.008)

- **PATRÓN** `ibs_15` < `0.3333` → IC=+0.294 (n=1427)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3333 (IC base=-0.008)

- **PATRÓN** `dist_vwap_pct` > `0.786` → IC=+0.327 (n=270)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.786 (IC base=-0.008)

### UPDOWN_GBM_ETH_15M_HORA7
- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.167 (n=58)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0063 (IC base=+0.096)

- **PATRÓN** `drift_15min` |x|≤ `0.7471` → IC=+0.147 (n=66)

  - _Acción_: Kelly boost +0.74€ cuando `drift_15min` |x|≤ 0.7471 (IC base=+0.096)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.235` → IC=+0.159 (n=42)

  - _Acción_: Kelly boost +0.80€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.235 (IC base=+0.096)

- **PATRÓN** `ibs_15` > `0.8357` → IC=+0.312 (n=30)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8357 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` < `0.0949` → IC=+0.214 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0949 (IC base=+0.096)

- **PATRÓN** `sigma_ewma_delta_pct` > `13.113` → IC=+0.167 (n=19)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 13.113 (IC base=+0.096)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.167 (n=28)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 52.0 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` > `0.1943` → IC=+0.135 (n=94)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` > 0.1943 (IC base=+0.050)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.167 (n=58)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0063 (IC base=+0.096)

- **PATRÓN** `drift_15min` |x|≤ `0.7471` → IC=+0.147 (n=66)

  - _Acción_: Kelly boost +0.74€ cuando `drift_15min` |x|≤ 0.7471 (IC base=+0.096)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.235` → IC=+0.159 (n=42)

  - _Acción_: Kelly boost +0.80€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.235 (IC base=+0.096)

- **PATRÓN** `ibs_15` > `0.8357` → IC=+0.312 (n=30)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8357 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` < `0.0949` → IC=+0.214 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0949 (IC base=+0.096)

- **PATRÓN** `sigma_ewma_delta_pct` > `13.113` → IC=+0.167 (n=19)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 13.113 (IC base=+0.096)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.167 (n=28)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 52.0 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` > `0.1943` → IC=+0.135 (n=94)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` > 0.1943 (IC base=+0.050)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.297 (n=510)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0035 (IC base=+0.284)

- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.293 (n=510)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0068 (IC base=+0.284)

- **PATRÓN** `drift_60min` |x|≤ `0.0715` → IC=+0.305 (n=676)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0715 (IC base=+0.284)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0676` → IC=+0.286 (n=1527)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0676 (IC base=+0.284)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2165` → IC=+0.288 (n=939)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2165 (IC base=+0.284)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.297 (n=1592)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.284)

- **PATRÓN** `ibs_15` > `0.8357` → IC=+0.309 (n=1529)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8357 (IC base=+0.284)

- **PATRÓN** `dist_vwap_pct` > `0.2749` → IC=+0.315 (n=653)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2749 (IC base=+0.284)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.521` → IC=+0.383 (n=331)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.521 (IC base=+0.284)

- **PATRÓN** `libro_liquidez` > `13043.7974` → IC=+0.299 (n=510)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13043.7974 (IC base=+0.284)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.307 (n=268)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.279)

- **PATRÓN** `drift_60min` |x|≤ `0.0763` → IC=+0.298 (n=354)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0763 (IC base=+0.279)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0708` → IC=+0.279 (n=803)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0708 (IC base=+0.279)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2264` → IC=+0.293 (n=486)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2264 (IC base=+0.279)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.303 (n=741)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.279)

- **PATRÓN** `ibs_15` > `0.8545` → IC=+0.305 (n=717)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8545 (IC base=+0.279)

- **PATRÓN** `dist_vwap_pct` > `0.2607` → IC=+0.312 (n=338)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2607 (IC base=+0.279)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.34` → IC=+0.388 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.34 (IC base=+0.279)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.280 (n=1040)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.279)

- **PATRÓN** `libro_liquidez` > `14412.9472` → IC=+0.311 (n=364)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14412.9472 (IC base=+0.279)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.301 (n=320)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0046 (IC base=+0.289)

- **PATRÓN** `sigma_h` > `0.0072` → IC=+0.291 (n=242)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0072 (IC base=+0.289)

- **PATRÓN** `drift_60min` |x|≤ `0.0502` → IC=+0.320 (n=242)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0502 (IC base=+0.289)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0634` → IC=+0.293 (n=726)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0634 (IC base=+0.289)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1009` → IC=+0.308 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1009 (IC base=+0.289)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.298 (n=746)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.289)

- **PATRÓN** `ibs_15` > `0.8444` → IC=+0.316 (n=727)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8444 (IC base=+0.289)

- **PATRÓN** `dist_vwap_pct` > `0.2913` → IC=+0.314 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2913 (IC base=+0.289)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.835` → IC=+0.371 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.835 (IC base=+0.289)

### UPDOWN_OU_5M
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1089` → IC=-0.168 (n=239)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1089
  - _Potencial_: sin este filtro IC_bueno=-0.095 (n=119)

- **FILTRO** `ballena_activa_n` > `31.0` → IC=-0.146 (n=272)

  - _Acción_: SKIP cuando `ballena_activa_n` > 31.0
  - _Potencial_: sin este filtro IC_bueno=-0.112 (n=96)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.1254` → IC=-0.223 (n=128)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1254
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=388)

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
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=171)

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
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1635` → IC=-0.283 (n=21)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1635
  - _Potencial_: sin este filtro IC_bueno=-0.144 (n=43)

- **FILTRO** `sigma_h` < `0.0051` → IC=-0.237 (n=17)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0051
  - _Potencial_: sin este filtro IC_bueno=-0.191 (n=53)

- **FILTRO** `drift_15min` |x|> `0.5336` → IC=-0.260 (n=23)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.5336
  - _Potencial_: sin este filtro IC_bueno=-0.173 (n=47)

- **FILTRO** `ballena_activa_n` > `9.0` → IC=-0.203 (n=35)

  - _Acción_: SKIP cuando `ballena_activa_n` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.143 (n=12)

### WEEKLY_PRICE
- **PATRÓN** `ratio` < `0.9866` → IC=+0.252 (n=578)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9866 (IC base=+0.122)

- **PATRÓN** `T_h` > `116.9578` → IC=+0.351 (n=3408)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 116.9578 (IC base=+0.331)

- **PATRÓN** `ratio` > `1.0158` → IC=+0.388 (n=661)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0158 (IC base=+0.331)

### WEEKLY_PRICE#BTC
- **PATRÓN** `ratio` < `0.9756` → IC=+0.190 (n=217)

  - _Acción_: Kelly boost +0.95€ cuando `ratio` < 0.9756 (IC base=+0.064)

- **PATRÓN** `T_h` > `111.011` → IC=+0.322 (n=1263)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.011 (IC base=+0.301)

- **PATRÓN** `ratio` > `1.0004` → IC=+0.300 (n=522)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0004 (IC base=+0.301)

### WEEKLY_PRICE#ETH
- **PATRÓN** `ratio` < `0.9775` → IC=+0.361 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9775 (IC base=+0.185)

- **PATRÓN** `T_h` > `111.9965` → IC=+0.347 (n=1254)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9965 (IC base=+0.313)

- **PATRÓN** `ratio` > `1.0044` → IC=+0.338 (n=424)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0044 (IC base=+0.313)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.0398` → IC=+0.409 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.0398 (IC base=+0.396)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.551 sube el IC de +0.132 a +0.206 en UPDOWN_GBM#15min (n=6012). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7013 sube el IC de +0.206 a +0.274 en UPDOWN_GBM#BTC#15min (n=911). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.4761 sube el IC de +0.132 a +0.216 en UPDOWN_GBM#ETH#15min (n=1172). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.6944 sube el IC de +0.137 a +0.232 en UPDOWN_GBM#XRP#15min (n=1132). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6288 sube el IC de -0.086 a +0.278 en UPDOWN_GBM_15M_TARDIO (n=1373). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3775 sube el IC de +0.001 a +0.281 en UPDOWN_GBM_15M_TARDIO (n=6163). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7503 sube el IC de +0.066 a +0.313 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=495). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.6283 sube el IC de -0.180 a +0.295 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=86). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.5639 sube el IC de +0.149 a +0.240 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=694). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.1944 sube el IC de +0.234 a +0.293 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=1628). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.9231 sube el IC de -0.204 a +0.380 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=23). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.381 sube el IC de -0.026 a +0.295 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=1016). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.221 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3333 sube el IC de -0.008 a +0.294 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=1427). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_YES, IBS > 0.8357 sube el IC de +0.096 a +0.312 en UPDOWN_GBM_ETH_15M_HORA7 (n=30). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_YES, IBS > 0.8357 sube el IC de +0.096 a +0.312 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=30). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8357 sube el IC de +0.284 a +0.309 en UPDOWN_GBM_IBS_ALTO (n=1529). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8545 sube el IC de +0.279 a +0.305 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=717). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8444 sube el IC de +0.289 a +0.316 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=727). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7873 sube el IC de +0.361 a +0.391 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=838). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8044 sube el IC de +0.360 a +0.378 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=401). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7601 sube el IC de +0.361 a +0.396 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=438). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 2386 | +0.085 | +265.15€ | 1 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 2386 | +0.085 | +265.15€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1974 | +0.086 | +225.66€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1974 | +0.086 | +225.66€ | 1 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 285 | +0.068 | +10.79€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 285 | +0.068 | +10.79€ | 5 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 96 | +0.122 | +29.03€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 96 | +0.122 | +29.03€ | 0 | 9 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 1521 | -0.029 | +51.71€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 1521 | -0.029 | +51.71€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE | 7 | +0.019 | +3.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE#15min | 7 | +0.019 | +3.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 1197 | -0.041 | +39.07€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 1197 | -0.041 | +39.07€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 224 | +0.035 | +20.04€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 224 | +0.035 | +20.04€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 93 | -0.037 | -10.65€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 93 | -0.037 | -10.65€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 51920 | -0.086 | -6646.74€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 3425 | +0.093 | -321.47€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 48495 | -0.099 | -6325.27€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 5088 | -0.116 | -816.49€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 5088 | -0.116 | -816.49€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 3425 | +0.093 | -321.47€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 3425 | +0.093 | -321.47€ | 0 | 1 |
| ✅ BALLENAS_TARDIAS#DOGE | 5129 | -0.108 | -957.76€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 5129 | -0.108 | -957.76€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 14706 | -0.043 | -1380.55€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 14706 | -0.043 | -1380.55€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 14135 | -0.121 | -1627.38€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 14135 | -0.121 | -1627.38€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 9437 | -0.138 | -1543.09€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 9437 | -0.138 | -1543.09€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 58682 | -0.012 | +2524.13€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 15125 | +0.004 | +1467.13€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 43557 | -0.017 | +1057.00€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 58682 | -0.012 | +2524.13€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 15125 | +0.004 | +1467.13€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 43557 | -0.017 | +1057.00€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 217755 | +0.112 | -8996.75€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#15min | 23807 | +0.178 | -774.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 1020 | +0.022 | -82.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 180582 | +0.104 | -7724.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 12346 | +0.095 | -415.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 29940 | +0.101 | -2161.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 91 | -0.199 | +8.40€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 29812 | +0.102 | -2179.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#60min | 22 | +0.167 | +21.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 40701 | +0.122 | -690.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5755 | +0.175 | -235.04€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 29891 | +0.119 | -255.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 5013 | +0.081 | -177.76€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 29991 | +0.098 | -2100.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 115 | -0.098 | +21.30€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 29848 | +0.099 | -2115.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#60min | 13 | -0.065 | +4.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 46654 | +0.123 | -1011.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 11615 | +0.176 | -347.19€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 30382 | +0.105 | -575.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 4645 | +0.103 | -80.23€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#SOL | 40519 | +0.111 | -1702.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 6130 | +0.199 | -239.72€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 923 | +0.046 | -28.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 30816 | +0.095 | -1249.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 2650 | +0.108 | -185.79€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO#XRP | 29950 | +0.106 | -1329.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 101 | -0.131 | +17.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 29833 | +0.106 | -1349.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 35567 | +0.188 | -2728.23€ | 2 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 35567 | +0.188 | -2728.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 8049 | +0.159 | -971.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 8049 | +0.159 | -971.50€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 5389 | +0.193 | -244.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 5389 | +0.193 | -244.34€ | 3 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 7853 | +0.171 | -735.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 7853 | +0.171 | -735.65€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 6510 | +0.251 | -237.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 6510 | +0.251 | -237.85€ | 0 | 4 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 7687 | +0.182 | -552.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 7687 | +0.182 | -552.65€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 1364 | +0.423 | -57.67€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 1364 | +0.423 | -57.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 582 | +0.437 | -8.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 582 | +0.437 | -8.53€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE#15min | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 528 | +0.421 | -23.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 528 | +0.421 | -23.69€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 240 | +0.397 | -21.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 240 | +0.397 | -21.58€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 125623 | +0.199 | -9171.30€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 125623 | +0.199 | -9171.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 21785 | +0.174 | -2592.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 21785 | +0.174 | -2592.99€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 20243 | +0.223 | -673.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 20243 | +0.223 | -673.09€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 21541 | +0.180 | -2265.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 21541 | +0.180 | -2265.09€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 20422 | +0.218 | -786.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 20422 | +0.218 | -786.60€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 20717 | +0.206 | -1203.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 20717 | +0.206 | -1203.89€ | 1 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 20915 | +0.197 | -1649.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 20915 | +0.197 | -1649.64€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 48856 | +0.116 | +384.88€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 48856 | +0.116 | +384.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 24329 | +0.117 | +263.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 24329 | +0.117 | +263.15€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 24527 | +0.115 | +121.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 24527 | +0.115 | +121.73€ | 0 | 3 |
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
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 2077 | +0.064 | -105.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 725 | +0.046 | -64.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 1352 | +0.074 | -41.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1643 | +0.070 | -60.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 291 | +0.053 | -19.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 1352 | +0.074 | -41.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 100090 | +0.100 | -2124.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 8124 | +0.097 | +189.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 91966 | +0.101 | -2313.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 54597 | +0.105 | -459.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 8124 | +0.097 | +189.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 46473 | +0.106 | -649.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 21567 | +0.109 | -109.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 21567 | +0.109 | -109.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 23926 | +0.083 | -1555.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 23926 | +0.083 | -1555.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 943 | +0.174 | -108.45€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 943 | +0.174 | -108.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 943 | +0.174 | -108.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 943 | +0.174 | -108.45€ | 2 | 4 |
| ✅ GBM_LATE_15M | 68200 | +0.102 | +38386.00€ | 0 | 19 |
| ✅ GBM_LATE_15M#15min | 68200 | +0.102 | +38386.00€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 11339 | +0.223 | +9662.00€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 11339 | +0.223 | +9662.00€ | 0 | 18 |
| ✅ GBM_LATE_15M#BTC | 10689 | +0.176 | +8618.68€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 10689 | +0.176 | +8618.68€ | 0 | 22 |
| ✅ GBM_LATE_15M#DOGE | 12193 | +0.207 | +9610.18€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 12193 | +0.207 | +9610.18€ | 0 | 21 |
| ✅ GBM_LATE_15M#ETH | 9017 | +0.063 | +3070.18€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 9017 | +0.063 | +3070.18€ | 1 | 18 |
| ✅ GBM_LATE_15M#SOL | 9445 | -0.025 | +2464.43€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 9445 | -0.025 | +2464.43€ | 4 | 15 |
| ✅ GBM_LATE_15M#XRP | 15517 | -0.019 | +4960.54€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 15517 | -0.019 | +4960.54€ | 3 | 11 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 72436 | +0.088 | +42561.55€ | 0 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 72436 | +0.088 | +42561.55€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 14074 | -0.002 | +7450.06€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 14074 | -0.002 | +7450.06€ | 3 | 9 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 15563 | +0.008 | +4333.15€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 15563 | +0.008 | +4333.15€ | 0 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 9666 | +0.296 | +11082.54€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 9666 | +0.296 | +11082.54€ | 0 | 21 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 13878 | +0.020 | +4476.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 13878 | +0.020 | +4476.72€ | 0 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 11005 | +0.052 | +5188.43€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 11005 | +0.052 | +5188.43€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 8250 | +0.313 | +10030.65€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 8250 | +0.313 | +10030.65€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 53646 | +0.179 | +44591.85€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 53646 | +0.179 | +44591.85€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 8135 | +0.238 | +7511.22€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 8135 | +0.238 | +7511.22€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 8578 | +0.140 | +6484.49€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 8578 | +0.140 | +6484.49€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 8622 | +0.223 | +7452.15€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 8622 | +0.223 | +7452.15€ | 0 | 19 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 9167 | +0.130 | +7192.30€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 9167 | +0.130 | +7192.30€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 10116 | +0.123 | +7845.31€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 10116 | +0.123 | +7845.31€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 9028 | +0.231 | +8106.37€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 9028 | +0.231 | +8106.37€ | 0 | 25 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 14746 | +0.125 | +7491.87€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 14746 | +0.125 | +7491.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 680 | +0.161 | +443.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 680 | +0.161 | +443.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 3897 | +0.125 | +2082.56€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 3897 | +0.125 | +2082.56€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 509 | +0.156 | +286.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 509 | +0.156 | +286.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 4311 | +0.126 | +2175.05€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 4311 | +0.126 | +2175.05€ | 0 | 18 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 3993 | +0.100 | +1637.24€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 3993 | +0.100 | +1637.24€ | 0 | 16 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 1356 | +0.168 | +866.50€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 1356 | +0.168 | +866.50€ | 0 | 27 |
| ✅ GBM_LATE_15M_TARDIO | 68553 | +0.189 | +57050.15€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#15min | 68553 | +0.189 | +57050.15€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 10848 | +0.247 | +10367.61€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 10848 | +0.247 | +10367.61€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 11011 | +0.143 | +8044.19€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 11011 | +0.143 | +8044.19€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 11605 | +0.234 | +10430.00€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 11605 | +0.234 | +10430.00€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 11347 | +0.145 | +8554.05€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 11347 | +0.145 | +8554.05€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 12099 | +0.129 | +8863.00€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 12099 | +0.129 | +8863.00€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 11643 | +0.240 | +10791.30€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 11643 | +0.240 | +10791.30€ | 0 | 22 |
| ✅ GBM_LATE_5M | 17231 | +0.220 | +14606.99€ | 0 | 26 |
| ✅ GBM_LATE_5M#5min | 17231 | +0.220 | +14606.99€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 1948 | +0.253 | +1898.73€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 1948 | +0.253 | +1898.73€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 3346 | +0.209 | +2852.58€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 3346 | +0.209 | +2852.58€ | 0 | 25 |
| ✅ GBM_LATE_5M#DOGE | 1592 | +0.218 | +1323.49€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1592 | +0.218 | +1323.49€ | 0 | 18 |
| ✅ GBM_LATE_5M#ETH | 5022 | +0.211 | +3973.52€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 5022 | +0.211 | +3973.52€ | 0 | 27 |
| ✅ GBM_LATE_5M#SOL | 3116 | +0.233 | +2795.06€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 3116 | +0.233 | +2795.06€ | 0 | 28 |
| ✅ GBM_LATE_5M#XRP | 2207 | +0.212 | +1763.61€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 2207 | +0.212 | +1763.61€ | 0 | 0 |
| ✅ GBM_LATE_60M | 7016 | +0.088 | +2547.40€ | 0 | 8 |
| ✅ GBM_LATE_60M#60min | 7016 | +0.088 | +2547.40€ | 0 | 0 |
| ✅ GBM_LATE_60M#BNB | 252 | +0.283 | +286.11€ | 0 | 0 |
| ✅ GBM_LATE_60M#BNB#60min | 252 | +0.283 | +286.11€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 2127 | +0.061 | +628.41€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 2127 | +0.061 | +628.41€ | 1 | 5 |
| ✅ GBM_LATE_60M#DOGE | 246 | +0.310 | +295.75€ | 0 | 0 |
| ✅ GBM_LATE_60M#DOGE#60min | 246 | +0.310 | +295.75€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH | 1980 | +0.059 | +605.52€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 1980 | +0.059 | +605.52€ | 1 | 7 |
| ✅ GBM_LATE_60M#SOL | 2162 | +0.064 | +430.76€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 2162 | +0.064 | +430.76€ | 0 | 10 |
| ✅ GBM_LATE_60M#XRP | 249 | +0.321 | +300.85€ | 0 | 0 |
| ✅ GBM_LATE_60M#XRP#60min | 249 | +0.321 | +300.85€ | 0 | 22 |
| 🚫 GBM_LATE_60M_FADE | 824 | -0.247 | -39.89€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 824 | -0.247 | -39.89€ | 0 | 0 |
| ✅ GBM_LATE_60M_FADE#BNB | 12 | +0.000 | +4.05€ | 0 | 0 |
| ✅ GBM_LATE_60M_FADE#BNB#60min | 12 | +0.000 | +4.05€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 289 | -0.260 | -22.86€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 289 | -0.260 | -22.86€ | 5 | 0 |
| ✅ GBM_LATE_60M_FADE#DOGE | 9 | -0.061 | +0.70€ | 0 | 0 |
| ✅ GBM_LATE_60M_FADE#DOGE#60min | 9 | -0.061 | +0.70€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 281 | -0.246 | -9.46€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 281 | -0.246 | -9.46€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 229 | -0.245 | -11.34€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 229 | -0.245 | -11.34€ | 4 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 2674 | +0.092 | +716.22€ | 1 | 8 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 2674 | +0.092 | +716.22€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 952 | +0.070 | +239.80€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 952 | +0.070 | +239.80€ | 0 | 4 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#DOGE | 59 | +0.205 | +35.64€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#DOGE#60min | 59 | +0.205 | +35.64€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 833 | +0.053 | +160.31€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 833 | +0.053 | +160.31€ | 0 | 13 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 699 | +0.152 | +242.72€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 699 | +0.152 | +242.72€ | 2 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#XRP | 131 | +0.117 | +37.75€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#XRP#60min | 131 | +0.117 | +37.75€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN | 442 | +0.302 | +522.43€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 442 | +0.302 | +522.43€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 442 | +0.302 | +522.43€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 442 | +0.302 | +522.43€ | 1 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 5142 | +0.094 | +1104.05€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 5142 | +0.094 | +1104.05€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 5142 | +0.094 | +1104.05€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 5142 | +0.094 | +1104.05€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M | 2031 | +0.018 | +102.84€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 2031 | +0.018 | +102.84€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 264 | +0.083 | +47.00€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 264 | +0.083 | +47.00€ | 0 | 4 |
| ✅ LIQUIDACIONES_15M#BTC | 374 | -0.011 | +8.62€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 374 | -0.011 | +8.62€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 171 | +0.043 | +19.58€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 171 | +0.043 | +19.58€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 441 | +0.026 | +23.32€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 441 | +0.026 | +23.32€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 361 | -0.023 | -0.42€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 361 | -0.023 | -0.42€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 420 | +0.021 | +4.74€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 420 | +0.021 | +4.74€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 4702 | +0.020 | +218.31€ | 4 | 1 |
| ✅ LIQUIDACIONES_5M#5min | 4702 | +0.020 | +218.31€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 241 | +0.002 | -6.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 241 | +0.002 | -6.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 872 | +0.017 | +52.78€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 872 | +0.017 | +52.78€ | 2 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 367 | +0.072 | +100.84€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 367 | +0.072 | +100.84€ | 0 | 4 |
| ✅ LIQUIDACIONES_5M#ETH | 1775 | +0.024 | +40.30€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1775 | +0.024 | +40.30€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 825 | +0.013 | +4.43€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 825 | +0.013 | +4.43€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 622 | -0.005 | +26.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 622 | -0.005 | +26.11€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 2935 | -0.037 | -16.28€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 2935 | -0.037 | -16.28€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 883 | -0.040 | -19.99€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 883 | -0.040 | -19.99€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 1066 | -0.022 | +11.82€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 1066 | -0.022 | +11.82€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 956 | -0.051 | -7.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 956 | -0.051 | -7.45€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#XRP | 25 | +0.018 | -0.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#XRP#60min | 25 | +0.018 | -0.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 22490 | -0.033 | -231.32€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 10954 | -0.031 | -66.32€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 11536 | -0.034 | -165.00€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 780 | -0.052 | -39.05€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 403 | -0.038 | -5.61€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 377 | -0.067 | -33.44€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 6102 | -0.026 | -29.85€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 2917 | -0.021 | +20.29€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 3185 | -0.031 | -50.14€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 2025 | -0.035 | -19.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 1044 | -0.039 | -22.85€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 981 | -0.031 | +3.51€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 5186 | -0.030 | -30.36€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 2517 | -0.025 | +10.52€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 2669 | -0.034 | -40.89€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 4277 | -0.027 | +22.36€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 2096 | -0.028 | +7.51€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 2181 | -0.026 | +14.84€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 4120 | -0.046 | -135.06€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 1977 | -0.049 | -76.18€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 2143 | -0.042 | -58.88€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 78427 | -0.001 | +4158.18€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 78427 | -0.001 | +4158.18€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 14119 | +0.027 | +1963.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 14119 | +0.027 | +1963.05€ | 2 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 11175 | -0.038 | -150.09€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 11175 | -0.038 | -150.09€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 14267 | +0.026 | +1578.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 14267 | +0.026 | +1578.46€ | 1 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 11118 | -0.054 | -313.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 11118 | -0.054 | -313.30€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 13237 | -0.004 | +377.63€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 13237 | -0.004 | +377.63€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 14511 | +0.020 | +702.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 14511 | +0.020 | +702.42€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 7592 | -0.053 | -113.81€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 7592 | -0.053 | -113.81€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1271 | -0.002 | -14.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1271 | -0.002 | -14.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 2200 | -0.058 | -20.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 2200 | -0.058 | -20.27€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 105 | -0.033 | -1.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 105 | -0.033 | -1.75€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 828 | -0.118 | -35.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 828 | -0.118 | -35.22€ | 6 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 2312 | -0.065 | -11.95€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 2312 | -0.065 | -11.95€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 876 | -0.021 | -29.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 876 | -0.021 | -29.85€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3768 | +0.002 | -6.81€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3768 | +0.002 | -6.81€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 133 | -0.033 | -0.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 133 | -0.033 | -0.70€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 580 | -0.003 | -9.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 580 | -0.003 | -9.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE | 139 | -0.004 | -2.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 139 | -0.004 | -2.34€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1327 | +0.006 | +6.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1327 | +0.006 | +6.88€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1392 | +0.006 | -0.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1392 | +0.006 | -0.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 197 | -0.013 | -0.12€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 197 | -0.013 | -0.12€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 191788 | -0.078 | +2118.68€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 191788 | -0.078 | +2118.68€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 33490 | -0.076 | +1909.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 33490 | -0.076 | +1909.17€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 29136 | -0.101 | -1415.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 29136 | -0.101 | -1415.49€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 33894 | -0.067 | +1650.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 33894 | -0.067 | +1650.49€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 28691 | -0.101 | -1024.96€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 28691 | -0.101 | -1024.96€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 33802 | -0.060 | +156.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 33802 | -0.060 | +156.49€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 32775 | -0.068 | +842.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 32775 | -0.068 | +842.98€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 9428 | -0.035 | -180.41€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 9428 | -0.035 | -180.41€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 1014 | -0.017 | -18.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 1014 | -0.017 | -18.55€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 2217 | -0.046 | -28.86€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 2217 | -0.046 | -28.86€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1012 | -0.021 | -30.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1012 | -0.021 | -30.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2686 | -0.023 | -30.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2686 | -0.023 | -30.29€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1317 | -0.062 | -29.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1317 | -0.062 | -29.98€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 1182 | -0.039 | -42.67€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 1182 | -0.039 | -42.67€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 2452 | +0.119 | +974.87€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#5min | 2316 | +0.122 | +962.27€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 535 | +0.139 | +271.62€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 535 | +0.139 | +271.62€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#DOGE | 485 | +0.118 | +173.49€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 485 | +0.118 | +173.49€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#ETH | 419 | +0.130 | +195.76€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 419 | +0.130 | +195.76€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 395 | +0.132 | +189.46€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 395 | +0.132 | +189.46€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#XRP | 482 | +0.093 | +131.95€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 482 | +0.093 | +131.95€ | 0 | 2 |
| ✅ ORDER_FLOW_5M_REACTIVO | 2613 | -0.023 | -59.41€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 2613 | -0.023 | -59.41€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 453 | +0.003 | +17.93€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 453 | +0.003 | +17.93€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 470 | -0.053 | -36.53€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 470 | -0.053 | -36.53€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 630 | -0.044 | -46.13€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 630 | -0.044 | -46.13€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 543 | -0.014 | -12.53€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 543 | -0.014 | -12.53€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 517 | -0.003 | +17.85€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 517 | -0.003 | +17.85€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 1384 | -0.043 | +141.80€ | 1 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 640 | -0.069 | +27.75€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 502 | -0.066 | +52.61€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 138 | -0.079 | -24.87€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 487 | -0.007 | +76.19€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 355 | +0.010 | +85.80€ | 0 | 2 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 132 | -0.052 | -9.61€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 257 | -0.044 | +37.86€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 219 | -0.043 | +33.44€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 38 | -0.050 | +4.42€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 1076 | -0.036 | +171.85€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 308 | -0.065 | -30.05€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE | 1760 | -0.185 | -32.40€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 696 | -0.173 | -6.39€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 617 | -0.172 | -3.22€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 79 | -0.179 | -3.17€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH | 592 | -0.197 | -31.78€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 523 | -0.203 | -36.89€ | 4 | 1 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 69 | -0.148 | +5.11€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 472 | -0.186 | +5.77€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 438 | -0.182 | +2.63€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 34 | -0.222 | +3.14€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#atexpiry | 1578 | -0.185 | -37.48€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 182 | -0.179 | +5.08€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 614 | +0.373 | +534.37€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#BTC | 141 | +0.178 | +100.38€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 141 | +0.178 | +100.38€ | 0 | 8 |
| ✅ RESOLUTION_SNIPER#ETH | 140 | +0.373 | +108.98€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 140 | +0.373 | +108.98€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#SOL | 333 | +0.452 | +325.01€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 333 | +0.452 | +325.01€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#sniper | 614 | +0.373 | +534.37€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 1077 | +0.043 | +95.80€ | 2 | 3 |
| ✅ STREAK_FADE_15M#15min | 1077 | +0.043 | +95.80€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 361 | +0.018 | +4.74€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 361 | +0.018 | +4.74€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 83 | +0.029 | +3.15€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 83 | +0.029 | +3.15€ | 1 | 3 |
| ✅ STREAK_FADE_15M#SOL | 87 | +0.039 | +10.03€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 87 | +0.039 | +10.03€ | 2 | 3 |
| ✅ STREAK_FADE_15M#XRP | 546 | +0.062 | +77.88€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 546 | +0.062 | +77.88€ | 0 | 3 |
| ✅ STREAK_FADE_5M | 3684 | -0.022 | -142.04€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3684 | -0.022 | -142.04€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 1130 | -0.022 | -39.63€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 1130 | -0.022 | -39.63€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 634 | -0.027 | -26.29€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 634 | -0.027 | -26.29€ | 1 | 0 |
| ✅ STREAK_FADE_5M#SOL | 185 | -0.045 | -15.72€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 185 | -0.045 | -15.72€ | 3 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1735 | -0.019 | -60.40€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1735 | -0.019 | -60.40€ | 1 | 0 |
| ✅ STREAK_FADE_60M | 164 | +0.012 | -0.94€ | 1 | 2 |
| ✅ STREAK_FADE_60M#60min | 164 | +0.012 | -0.94€ | 0 | 0 |
| ✅ STREAK_FADE_60M#BNB | 11 | +0.106 | +6.93€ | 0 | 0 |
| ✅ STREAK_FADE_60M#BNB#60min | 11 | +0.106 | +6.93€ | 0 | 0 |
| ✅ STREAK_FADE_60M#DOGE | 5 | +0.018 | +1.31€ | 0 | 0 |
| ✅ STREAK_FADE_60M#DOGE#60min | 5 | +0.018 | +1.31€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 51 | -0.028 | -2.40€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 51 | -0.028 | -2.40€ | 4 | 0 |
| ✅ STREAK_FADE_60M#SOL | 89 | +0.005 | -5.00€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 89 | +0.005 | -5.00€ | 1 | 1 |
| ✅ STREAK_FADE_60M#XRP | 8 | +0.000 | -1.78€ | 0 | 0 |
| ✅ STREAK_FADE_60M#XRP#60min | 8 | +0.000 | -1.78€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 11772 | +0.013 | +64.23€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 11772 | +0.013 | +64.23€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 3020 | +0.017 | +20.88€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 3020 | +0.017 | +20.88€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 3155 | +0.013 | +24.91€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 3155 | +0.013 | +24.91€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2975 | +0.009 | -0.37€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2975 | +0.009 | -0.37€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2622 | +0.014 | +18.81€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2622 | +0.014 | +18.81€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 14328 | +0.019 | +5.68€ | 4 | 0 |
| ✅ STRUCT_NO_15M#15min | 14328 | +0.019 | +5.68€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 5747 | +0.022 | +11.31€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 5747 | +0.022 | +11.31€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 5123 | +0.019 | -0.05€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 5123 | +0.019 | -0.05€ | 4 | 0 |
| ✅ STRUCT_NO_15M#SOL | 3458 | +0.014 | -5.58€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 3458 | +0.014 | -5.58€ | 1 | 0 |
| ✅ UPDOWN_GBM | 129270 | +0.060 | +12335.57€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 32274 | +0.077 | +6302.45€ | 0 | 10 |
| ✅ UPDOWN_GBM#240min | 3670 | -0.000 | +41.76€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 85109 | +0.062 | +5860.90€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 7774 | -0.001 | +134.90€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 11320 | +0.103 | +2088.69€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 2139 | +0.163 | +995.08€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 90 | -0.011 | -2.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 9091 | +0.090 | +1095.61€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 29374 | +0.056 | +2575.97€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 4392 | +0.081 | +980.48€ | 0 | 11 |
| ✅ UPDOWN_GBM#BTC#240min | 1086 | +0.000 | +22.50€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 20227 | +0.065 | +1484.43€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 3510 | -0.003 | +84.43€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 159 | -0.065 | +4.12€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 14409 | +0.074 | +1589.79€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 2084 | +0.155 | +893.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 86 | +0.023 | -0.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 12239 | +0.061 | +697.22€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 30404 | +0.049 | +2162.64€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 7530 | +0.069 | +1164.10€ | 0 | 9 |
| ✅ UPDOWN_GBM#ETH#240min | 1048 | +0.006 | +15.88€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 18813 | +0.052 | +940.46€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 2865 | -0.002 | +40.53€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 148 | -0.100 | +1.67€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 26567 | +0.041 | +1537.48€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 8688 | +0.033 | +500.44€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#240min | 963 | -0.011 | +7.86€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 15432 | +0.053 | +1028.99€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 1350 | +0.004 | +8.58€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#daily | 134 | -0.140 | -8.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 17194 | +0.073 | +2382.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 7441 | +0.089 | +1768.91€ | 0 | 11 |
| ✅ UPDOWN_GBM#XRP#240min | 397 | +0.006 | -1.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 9307 | +0.064 | +614.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#60min | 49 | +0.010 | +1.35€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 441 | -0.101 | -2.59€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 1117 | +0.361 | +420.32€ | 0 | 10 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 1117 | +0.361 | +420.32€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 534 | +0.360 | +187.54€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 534 | +0.360 | +187.54€ | 0 | 10 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 583 | +0.361 | +232.79€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 583 | +0.361 | +232.79€ | 0 | 14 |
| ✅ UPDOWN_GBM_15M_TARDIO | 30624 | -0.017 | +7721.68€ | 3 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 30624 | -0.017 | +7721.68€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 2418 | -0.046 | +636.63€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 2418 | -0.046 | +636.63€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 5671 | -0.115 | +356.63€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 5671 | -0.115 | +356.63€ | 3 | 10 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 1294 | +0.218 | +1063.04€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 1294 | +0.218 | +1063.04€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 4178 | +0.215 | +2615.02€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 4178 | +0.215 | +2615.02€ | 1 | 20 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 8586 | -0.057 | +1304.52€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 8586 | -0.057 | +1304.52€ | 4 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 8477 | -0.052 | +1745.84€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 8477 | -0.052 | +1745.84€ | 4 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 387 | +0.060 | +38.14€ | 0 | 8 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 387 | +0.060 | +38.14€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 387 | +0.060 | +38.14€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 387 | +0.060 | +38.14€ | 0 | 8 |
| ✅ UPDOWN_GBM_IBS_ALTO | 2037 | +0.284 | +1742.58€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 2037 | +0.284 | +1742.58€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 1070 | +0.279 | +862.79€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 1070 | +0.279 | +862.79€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 967 | +0.289 | +879.79€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 967 | +0.289 | +879.79€ | 0 | 9 |
| ✅ UPDOWN_OU_5M | 916 | -0.124 | -98.97€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#5min | 916 | -0.124 | -98.97€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 312 | -0.080 | -36.02€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 312 | -0.080 | -36.02€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 293 | -0.090 | -24.57€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 293 | -0.090 | -24.57€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 105 | -0.192 | -14.83€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 105 | -0.192 | -14.83€ | 2 | 0 |
| 🚫 UPDOWN_OU_5M#SOL | 134 | -0.206 | -9.71€ | 0 | 0 |
| 🚫 UPDOWN_OU_5M#SOL#5min | 134 | -0.206 | -9.71€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 5567 | +0.291 | +2410.04€ | 0 | 3 |
| ✅ WEEKLY_PRICE#BTC | 2178 | +0.246 | +343.73€ | 0 | 3 |
| ✅ WEEKLY_PRICE#ETH | 2158 | +0.283 | +881.12€ | 0 | 3 |
| ✅ WEEKLY_PRICE#SOL | 1231 | +0.382 | +1185.20€ | 0 | 1 |